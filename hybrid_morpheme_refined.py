#!/usr/bin/env python3
"""
Refined hybrid morpheme analysis.
The initial run showed:
- 3,483 stems (way too many) => segmentation too aggressive on prefix/suffix
- prefix-stem NMI=0.51 => NOT independent (but prefix-suffix NMI=0.03 IS independent!)
- Need to investigate: is the correlation due to phonotactic constraints or semantic?

Key insight: prefix-suffix independence + stem correlations suggests
the system might be a 2-LEVEL encoding:
  Level 1: prefix+suffix = grammatical frame (independent of each other)
  Level 2: stem = content word from a large vocabulary
  And the stem constrains which prefixes/suffixes can attach (= natural morphology)
"""

import re
import math
from collections import Counter, defaultdict
import random

def parse_eva(filepath):
    words = []
    page_words = defaultdict(list)
    with open(filepath, 'r', encoding='utf-8') as f:
        current_page = None
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            page_match = re.match(r'<(f\d+[rv]\d*)>', line)
            if page_match and '<!' in line:
                current_page = page_match.group(1)
                continue
            line_match = re.match(r'<(f\d+[rv]\d*)\.(\d+)', line)
            if line_match:
                current_page = line_match.group(1)
                text = re.sub(r'<[^>]+>', '', line)
                text = re.sub(r'@\d+;?', '', text)
                text = re.sub(r'\{([^}]+)\}', r'\1', text)
                text = re.sub(r"[',\?\*!]", '', text)
                tokens = re.split(r'[\s.\-<>]+', text)
                for t in tokens:
                    t = t.strip()
                    if t and re.match(r'^[a-z]+$', t):
                        words.append(t)
                        page_words[current_page].append(t)
    return words, page_words


# ============================================================
# REVISED SEGMENTATION with "bench" (gallows) recognition
# ============================================================

# The issue: "stems" like 'k', 'e', 'a', 'ch', 't' are just single chars
# because greedy prefix/suffix matching consumes everything.
#
# Better approach: recognize that Voynich words have STRUCTURAL patterns.
# The "bench" characters (ch, sh, cth, ckh, cph, cfh) are word-internal.
# Gallows (t, k, p, f) appear in specific positions.
#
# Let's try a STRUCTURAL decomposition:
# - Initial: word-initial glyph sequence (before first vowel-like sequence)
# - Core: the central part containing vowel sequences
# - Final: word-final glyph sequence (after last vowel-like sequence)

def structural_segment(word):
    """
    Segment based on Voynich glyph structure:
    - Consonant-like: ch, sh, cth, ckh, cph, cfh, d, s, k, t, p, f, l, r, n, m, q
    - Vowel-like: o, a, e, y, i
    - Bench: ch, sh (can be initial or medial)

    Pattern: (onset)(nucleus)(coda)
    """
    # First, tokenize into glyphs
    glyphs = tokenize_glyphs(word)
    if not glyphs:
        return ('', word, '')

    # Classify glyphs
    vowel_like = {'o', 'a', 'e', 'y', 'i'}
    classified = []
    for g in glyphs:
        if g in vowel_like:
            classified.append(('V', g))
        elif g in ('ii', 'ai', 'ei', 'oi'):
            classified.append(('V', g))
        else:
            classified.append(('C', g))

    return glyphs

def tokenize_glyphs(word):
    """Tokenize EVA word into minimal glyphs."""
    glyphs = []
    i = 0
    while i < len(word):
        # Multi-char glyphs (longest first)
        matched = False
        for glyph in ['cth', 'ckh', 'cph', 'cfh', 'sh', 'ch', 'qo',
                       'ii', 'ai', 'ei', 'oi', 'ee']:
            if word[i:].startswith(glyph):
                glyphs.append(glyph)
                i += len(glyph)
                matched = True
                break
        if not matched:
            glyphs.append(word[i])
            i += 1
    return glyphs


def calc_entropy(counter):
    total = sum(counter.values())
    if total == 0:
        return 0
    return -sum((c/total) * math.log2(c/total) for c in counter.values() if c > 0)

def calc_mi(slot_a, slot_b):
    joint = Counter(zip(slot_a, slot_b))
    count_a = Counter(slot_a)
    count_b = Counter(slot_b)
    total = len(slot_a)
    mi = 0
    for (a, b), count_ab in joint.items():
        p_ab = count_ab / total
        p_a = count_a[a] / total
        p_b = count_b[b] / total
        if p_ab > 0 and p_a > 0 and p_b > 0:
            mi += p_ab * math.log2(p_ab / (p_a * p_b))
    h_a = calc_entropy(count_a)
    h_b = calc_entropy(count_b)
    nmi = mi / min(h_a, h_b) if min(h_a, h_b) > 0 else 0
    return mi, nmi


def main():
    filepath = r"C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt"
    words, page_words = parse_eva(filepath)

    print(f"Total words: {len(words)}, Types: {len(set(words))}")

    # ============================================================
    # APPROACH 1: Position-based glyph analysis
    # ============================================================
    print("\n" + "=" * 60)
    print("GLYPH-POSITION ANALYSIS")
    print("=" * 60)

    all_glyphs = []
    glyph_positions = defaultdict(Counter)  # glyph -> position counter

    word_glyph_seqs = []
    for w in words:
        glyphs = tokenize_glyphs(w)
        all_glyphs.extend(glyphs)
        word_glyph_seqs.append(glyphs)
        n = len(glyphs)
        for pos, g in enumerate(glyphs):
            # Normalize position: start, middle, end
            if pos == 0:
                loc = 'initial'
            elif pos == n - 1:
                loc = 'final'
            else:
                loc = 'medial'
            glyph_positions[g][loc] += 1

    glyph_counter = Counter(all_glyphs)
    print(f"\nUnique glyphs: {len(glyph_counter)}")
    print(f"\nGlyph frequency and positional distribution:")
    print(f"{'Glyph':>6} {'Total':>6} {'Init%':>6} {'Med%':>6} {'Fin%':>6}")
    for g, c in glyph_counter.most_common(30):
        pos = glyph_positions[g]
        total_pos = sum(pos.values())
        init = 100 * pos.get('initial', 0) / total_pos
        med = 100 * pos.get('medial', 0) / total_pos
        fin = 100 * pos.get('final', 0) / total_pos
        print(f"{g:>6} {c:6d} {init:5.1f}% {med:5.1f}% {fin:5.1f}%")

    # ============================================================
    # APPROACH 2: Syllable-structure segmentation
    # ============================================================
    print("\n" + "=" * 60)
    print("SYLLABLE-STRUCTURE SEGMENTATION")
    print("=" * 60)

    # Based on glyph positions, define:
    # - Initial-only glyphs: these are "prefix" indicators
    # - Final-only glyphs: these are "suffix" indicators
    # - Position-free glyphs: these form the "stem"

    # Calculate position bias
    initial_bias = {}
    final_bias = {}
    for g, pos in glyph_positions.items():
        total = sum(pos.values())
        if total < 10:
            continue
        init_rate = pos.get('initial', 0) / total
        fin_rate = pos.get('final', 0) / total
        initial_bias[g] = init_rate
        final_bias[g] = fin_rate

    print("\nStrongly initial glyphs (>60% initial):")
    for g, rate in sorted(initial_bias.items(), key=lambda x: -x[1]):
        if rate > 0.6:
            print(f"  {g:>6}: {rate:.1%} initial (n={sum(glyph_positions[g].values())})")

    print("\nStrongly final glyphs (>60% final):")
    for g, rate in sorted(final_bias.items(), key=lambda x: -x[1]):
        if rate > 0.6:
            print(f"  {g:>6}: {rate:.1%} final (n={sum(glyph_positions[g].values())})")

    # ============================================================
    # APPROACH 3: Revised prefix/stem/suffix with data-driven boundaries
    # ============================================================
    print("\n" + "=" * 60)
    print("DATA-DRIVEN MORPHEME SEGMENTATION")
    print("=" * 60)

    # Use positional data to define prefix = all initial-biased glyphs at start
    # and suffix = all final-biased glyphs at end
    initial_glyphs = {g for g, rate in initial_bias.items() if rate > 0.5}
    final_glyphs = {g for g, rate in final_bias.items() if rate > 0.5}

    print(f"Initial-biased glyphs: {sorted(initial_glyphs)}")
    print(f"Final-biased glyphs: {sorted(final_glyphs)}")

    segmented = []
    for glyphs in word_glyph_seqs:
        # Find prefix: contiguous initial-biased glyphs from start
        prefix_end = 0
        for i, g in enumerate(glyphs):
            if g in initial_glyphs and i == prefix_end:
                prefix_end = i + 1
            else:
                break

        # Find suffix: contiguous final-biased glyphs from end
        suffix_start = len(glyphs)
        for i in range(len(glyphs) - 1, -1, -1):
            if glyphs[i] in final_glyphs and i == suffix_start - 1:
                suffix_start = i
            else:
                break

        # Ensure stem exists
        if prefix_end >= suffix_start:
            # Overlap - assign to stem
            prefix = ''
            suffix = ''
            stem = ''.join(glyphs)
        else:
            prefix = ''.join(glyphs[:prefix_end])
            stem = ''.join(glyphs[prefix_end:suffix_start])
            suffix = ''.join(glyphs[suffix_start:])

        segmented.append((prefix, stem, suffix))

    prefix_counter = Counter(s[0] for s in segmented)
    stem_counter = Counter(s[1] for s in segmented)
    suffix_counter = Counter(s[2] for s in segmented)

    non_empty_p = {k: v for k, v in prefix_counter.items() if k}
    non_empty_s = {k: v for k, v in stem_counter.items() if k}
    non_empty_sf = {k: v for k, v in suffix_counter.items() if k}

    print(f"\nDistinct prefixes: {len(non_empty_p)}")
    print(f"Distinct stems: {len(non_empty_s)}")
    print(f"Distinct suffixes: {len(non_empty_sf)}")

    print(f"\nTop prefixes:")
    for p, c in sorted(non_empty_p.items(), key=lambda x: -x[1])[:20]:
        print(f"  {p:>8}: {c:5d}")

    print(f"\nTop stems:")
    for s, c in sorted(non_empty_s.items(), key=lambda x: -x[1])[:30]:
        print(f"  {s:>12}: {c:5d}")

    print(f"\nTop suffixes:")
    for s, c in sorted(non_empty_sf.items(), key=lambda x: -x[1])[:20]:
        print(f"  {s:>8}: {c:5d}")

    # MI test on data-driven segmentation
    full = [(p, s, sf) for p, s, sf in segmented if p and s and sf]
    if len(full) > 100:
        fw_p = [x[0] for x in full]
        fw_s = [x[1] for x in full]
        fw_sf = [x[2] for x in full]

        mi_ps, nmi_ps = calc_mi(fw_p, fw_s)
        mi_ss, nmi_ss = calc_mi(fw_s, fw_sf)
        mi_psf, nmi_psf = calc_mi(fw_p, fw_sf)

        print(f"\nMI (data-driven segmentation, n={len(full)}):")
        print(f"  MI(prefix,stem)   = {mi_ps:.4f} (NMI={nmi_ps:.4f})")
        print(f"  MI(stem,suffix)   = {mi_ss:.4f} (NMI={nmi_ss:.4f})")
        print(f"  MI(prefix,suffix) = {mi_psf:.4f} (NMI={nmi_psf:.4f})")

    # ============================================================
    # APPROACH 4: Common word structure patterns
    # ============================================================
    print("\n" + "=" * 60)
    print("WORD STRUCTURE PATTERNS (Glyph-class sequences)")
    print("=" * 60)

    # Classify each glyph as C (consonant-cluster), V (vowel-like), G (gallows)
    def classify_glyph(g):
        if g in ('a', 'o', 'e', 'i', 'y', 'ai', 'ei', 'oi', 'ee', 'ii'):
            return 'V'
        elif g in ('t', 'k', 'p', 'f'):
            return 'G'  # gallows
        elif g in ('ch', 'sh', 'cth', 'ckh', 'cph', 'cfh', 'd', 's', 'l', 'r', 'n', 'm', 'q'):
            return 'C'
        else:
            return 'X'

    pattern_counter = Counter()
    for glyphs in word_glyph_seqs:
        pattern = ''.join(classify_glyph(g) for g in glyphs)
        pattern_counter[pattern] += 1

    print(f"\nUnique structural patterns: {len(pattern_counter)}")
    print(f"\nTop 30 patterns:")
    for pat, c in pattern_counter.most_common(30):
        pct = 100 * c / len(words)
        # Get example word
        example = ''
        for i, glyphs in enumerate(word_glyph_seqs):
            p2 = ''.join(classify_glyph(g) for g in glyphs)
            if p2 == pat:
                example = words[i]
                break
        print(f"  {pat:>12}: {c:5d} ({pct:5.1f}%)  e.g. {example}")

    # ============================================================
    # APPROACH 5: PARADIGM DETECTION
    # ============================================================
    print("\n" + "=" * 60)
    print("PARADIGM DETECTION (stem families)")
    print("=" * 60)

    # Group words that share the same stem (using original segmentation approach)
    # but with MINIMAL prefix/suffix
    PREFIXES_MIN = ['qo', 'ok', 'ot', 'sh', 'ch', 'cth', 'd', 's', 'k', 't', 'p', 'f', 'y', 'o']
    SUFFIXES_MIN = ['aiin', 'ain', 'iin', 'eey', 'edy', 'ey', 'ol', 'or', 'al', 'ar', 'an', 'am', 'dy', 'y', 'n', 'l', 'r']

    # Sort by length for greedy match
    PREFIXES_MIN.sort(key=len, reverse=True)
    SUFFIXES_MIN.sort(key=len, reverse=True)

    def segment_minimal(word):
        prefix = ''
        suffix = ''
        remaining = word
        for p in PREFIXES_MIN:
            if remaining.startswith(p) and len(remaining) > len(p) + 1:
                prefix = p
                remaining = remaining[len(p):]
                break
        for s in SUFFIXES_MIN:
            if remaining.endswith(s) and len(remaining) > len(s) + 1:
                suffix = s
                remaining = remaining[:-len(s)]
                break
        return (prefix, remaining, suffix)

    # Find paradigms: sets of words sharing a stem
    stem_families = defaultdict(set)
    word_to_seg = {}
    for w in set(words):
        seg = segment_minimal(w)
        if seg[1] and len(seg[1]) >= 2:  # stem at least 2 chars
            stem_families[seg[1]].add(w)
            word_to_seg[w] = seg

    # Paradigms with 4+ members
    large_paradigms = {stem: members for stem, members in stem_families.items()
                       if len(members) >= 4}

    print(f"\nStems with 2+ char and 4+ paradigm members: {len(large_paradigms)}")
    print(f"\nTop 20 paradigms by size:")
    for stem, members in sorted(large_paradigms.items(), key=lambda x: -len(x[1]))[:20]:
        prefixes_seen = set()
        suffixes_seen = set()
        for w in members:
            seg = word_to_seg[w]
            if seg[0]: prefixes_seen.add(seg[0])
            if seg[2]: suffixes_seen.add(seg[2])
        print(f"\n  Stem '{stem}' ({len(members)} words):")
        print(f"    Prefixes: {sorted(prefixes_seen)}")
        print(f"    Suffixes: {sorted(suffixes_seen)}")
        sorted_members = sorted(members)[:12]
        print(f"    Words: {', '.join(sorted_members)}{'...' if len(members) > 12 else ''}")

    # ============================================================
    # APPROACH 6: Compare natural language paradigm sizes
    # ============================================================
    print("\n" + "=" * 60)
    print("PARADIGM SIZE ANALYSIS")
    print("=" * 60)

    paradigm_sizes = [len(m) for m in stem_families.values() if len(m) >= 2]
    if paradigm_sizes:
        print(f"\nParadigms (stem families with 2+ members):")
        print(f"  Count: {len(paradigm_sizes)}")
        print(f"  Mean size: {sum(paradigm_sizes)/len(paradigm_sizes):.1f}")
        print(f"  Max size: {max(paradigm_sizes)}")

        size_dist = Counter(paradigm_sizes)
        print(f"\n  Size distribution:")
        for size in sorted(size_dist.keys())[:15]:
            print(f"    {size} members: {size_dist[size]} paradigms")

    # ============================================================
    # CRITICAL TEST: Prefix-Suffix independence deeper analysis
    # ============================================================
    print("\n" + "=" * 60)
    print("CRITICAL: PREFIX-SUFFIX FRAME ANALYSIS")
    print("=" * 60)

    # The KEY finding from initial analysis: NMI(prefix,suffix) = 0.03
    # This near-zero MI means prefix and suffix are INDEPENDENT
    # This is UNUSUAL for natural language (where case/gender/number create correlations)
    # But EXPECTED for a cipher where each position encodes independently

    # Create prefix-suffix frames
    frames = Counter()
    for seg in segmented:
        frame = (seg[0], seg[2])
        frames[frame] += 1

    print(f"\nTotal unique prefix-suffix frames: {len(frames)}")
    non_empty_frames = {k: v for k, v in frames.items() if k[0] and k[1]}
    print(f"Non-empty frames: {len(non_empty_frames)}")

    # Compare to expected if independent
    p_dist = Counter(s[0] for s in segmented)
    sf_dist = Counter(s[2] for s in segmented)
    total_w = len(segmented)

    # Chi-squared test for independence
    chi2 = 0
    df = 0
    for p in p_dist:
        for sf in sf_dist:
            observed = frames.get((p, sf), 0)
            expected = p_dist[p] * sf_dist[sf] / total_w
            if expected > 5:  # standard chi2 condition
                chi2 += (observed - expected)**2 / expected
                df += 1

    print(f"\nChi-squared test of prefix-suffix independence:")
    print(f"  Chi2 = {chi2:.1f}, df = {df}")
    print(f"  Chi2/df = {chi2/df:.2f}" if df > 0 else "  (insufficient data)")
    # Chi2/df ~ 1.0 => independent, >> 1.0 => dependent

    # ============================================================
    # COMPARISON: Latin/Italian morpheme correlations
    # ============================================================
    print("\n" + "=" * 60)
    print("REFERENCE: Expected correlations")
    print("=" * 60)
    print("""
Natural language (Latin/Italian):
  - MI(prefix, suffix) typically HIGH (0.15-0.40 NMI)
    because grammatical categories constrain endings
  - MI(stem, suffix) typically HIGH (0.20-0.50 NMI)
    because noun vs verb determines available suffixes

Voynich observed:
  - MI(prefix, suffix) = 0.03 NMI  => ABNORMALLY LOW
  - MI(prefix, stem) = 0.51 NMI    => HIGH (stems prefer certain prefixes)
  - MI(stem, suffix) = 0.38 NMI    => MODERATE-HIGH

Interpretation options:
  A) Simple cipher: prefix and suffix are independent cipher dimensions
     but both correlate with stem because stem constrains phonotactics
  B) Notation system: prefix = category marker, suffix = qualifier,
     stem = concept. Category and qualifier are orthogonal.
  C) Agglutinative natural language where prefix and suffix are from
     different grammatical systems (e.g., Turkish: person prefix + case suffix)
""")

    # ============================================================
    # REDUCED STEM VOCABULARY
    # ============================================================
    print("\n" + "=" * 60)
    print("STEM REDUCTION: Collapsing similar stems")
    print("=" * 60)

    # Many "stems" are just glyph-level variants.
    # Collapse stems that differ only by gallows substitution
    # (t/k/p/f are interchangeable in some theories)

    def normalize_stem(stem):
        """Collapse gallows to single symbol, bench chars to single symbol."""
        s = stem
        # Gallows normalization
        s = re.sub(r'[tkpf]', 'G', s)
        return s

    normalized_stems = Counter()
    for stem, count in non_empty_s.items():
        ns = normalize_stem(stem)
        normalized_stems[ns] += count

    print(f"Before normalization: {len(non_empty_s)} stems")
    print(f"After gallows collapse: {len(normalized_stems)} stems")

    # Also try collapsing bench characters
    def normalize_stem_v2(stem):
        s = stem
        s = re.sub(r'(cth|ckh|cph|cfh)', 'B', s)  # complex bench
        s = re.sub(r'(ch|sh)', 'H', s)  # simple bench
        s = re.sub(r'[tkpf]', 'G', s)  # gallows
        return s

    normalized_stems_v2 = Counter()
    for stem, count in non_empty_s.items():
        ns = normalize_stem_v2(stem)
        normalized_stems_v2[ns] += count

    print(f"After bench+gallows collapse: {len(normalized_stems_v2)} stems")

    # Stems appearing 5+ times after normalization
    freq_norm = {s: c for s, c in normalized_stems_v2.items() if c >= 5}
    print(f"Normalized stems with 5+ occurrences: {len(freq_norm)}")

    return segmented


if __name__ == '__main__':
    main()
