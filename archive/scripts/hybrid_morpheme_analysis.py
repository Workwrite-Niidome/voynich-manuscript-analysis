#!/usr/bin/env python3
"""
Hybrid Morpheme-Cipher Analysis of the Voynich Manuscript
Tests hypothesis: PREFIX (category) + STEM (concept) + SUFFIX (grammar)
Each slot independently encodes one cipher dimension.
"""

import re
import math
import random
from collections import Counter, defaultdict
from itertools import product

# ============================================================
# 1. PARSE EVA TRANSCRIPTION
# ============================================================

def parse_eva(filepath):
    """Extract words from EVA transcription, removing markup."""
    words = []
    page_words = defaultdict(list)  # page -> [words]
    line_words = defaultdict(list)  # (page, line) -> [words]

    current_page = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Page header
            page_match = re.match(r'<(f\d+[rv]\d*)>', line)
            if page_match and '<!' in line:
                current_page = page_match.group(1)
                continue

            # Content line
            line_match = re.match(r'<(f\d+[rv]\d*)\.(\d+)', line)
            if line_match:
                current_page = line_match.group(1)
                line_num = line_match.group(2)

                # Extract text after the tag
                text = re.sub(r'<[^>]+>', '', line)
                # Remove annotations like @221; @152; etc
                text = re.sub(r'@\d+;?', '', text)
                # Remove {cto} style annotations - extract the content
                text = re.sub(r'\{([^}]+)\}', r'\1', text)
                # Remove special chars
                text = re.sub(r"[',\?\*!]", '', text)
                # Split on dots, spaces, hyphens
                tokens = re.split(r'[\s.\-<>]+', text)
                for t in tokens:
                    t = t.strip()
                    if t and len(t) > 0 and re.match(r'^[a-z]+$', t):
                        words.append(t)
                        page_words[current_page].append(t)
                        line_words[(current_page, line_num)].append(t)

    return words, page_words, line_words


# ============================================================
# 2. MORPHEME SEGMENTATION
# ============================================================

# Sorted by length (longest first) for greedy matching
PREFIXES = sorted([
    'cth', 'sh', 'ch', 'qo', 'ok', 'ot', 'ct',
    'o', 'd', 's', 'k', 't', 'p', 'f', 'y'
], key=len, reverse=True)

SUFFIXES = sorted([
    'aiin', 'ain', 'iin',
    'eey', 'edy', 'ey',
    'ol', 'or', 'al', 'ar', 'an', 'am',
    'dy', 'y',
    'n', 'l', 'r'
], key=len, reverse=True)

def segment_word(word):
    """Segment a word into (prefix, stem, suffix)."""
    if len(word) <= 1:
        return ('', word, '')

    prefix = ''
    suffix = ''
    remaining = word

    # Try to match prefix (greedy longest match)
    for p in PREFIXES:
        if remaining.startswith(p) and len(remaining) > len(p):
            prefix = p
            remaining = remaining[len(p):]
            break

    # Try to match suffix (greedy longest match)
    for s in SUFFIXES:
        if remaining.endswith(s) and len(remaining) > len(s):
            suffix = s
            remaining = remaining[:-len(s)]
            break
        # Also try if remaining == suffix (no stem)
        elif remaining.endswith(s) and len(remaining) == len(s) and prefix:
            suffix = s
            remaining = ''
            break

    stem = remaining
    return (prefix, stem, suffix)


# ============================================================
# 3. MUTUAL INFORMATION CALCULATION
# ============================================================

def calc_entropy(counter):
    """Calculate Shannon entropy."""
    total = sum(counter.values())
    if total == 0:
        return 0
    entropy = 0
    for count in counter.values():
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)
    return entropy

def calc_mi(slot_a, slot_b):
    """Calculate mutual information between two slots."""
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

    # Normalized MI
    h_a = calc_entropy(count_a)
    h_b = calc_entropy(count_b)
    nmi = mi / min(h_a, h_b) if min(h_a, h_b) > 0 else 0

    return mi, nmi

def calc_conditional_entropy(target, given):
    """H(target|given) = H(target,given) - H(given)"""
    joint = Counter(zip(given, target))
    h_joint = calc_entropy(joint)
    h_given = calc_entropy(Counter(given))
    return h_joint - h_given


# ============================================================
# 4. STATISTICAL TESTS
# ============================================================

def zipf_test(counter, label=""):
    """Test Zipf's law fit."""
    ranks = sorted(counter.values(), reverse=True)
    if len(ranks) < 10:
        return None

    # Log-log regression
    log_ranks = [math.log(i+1) for i in range(len(ranks))]
    log_freqs = [math.log(f) if f > 0 else 0 for f in ranks]

    n = len(log_ranks)
    sum_x = sum(log_ranks)
    sum_y = sum(log_freqs)
    sum_xy = sum(x*y for x,y in zip(log_ranks, log_freqs))
    sum_x2 = sum(x*x for x in log_ranks)

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    intercept = (sum_y - slope * sum_x) / n

    # R-squared
    y_mean = sum_y / n
    ss_tot = sum((y - y_mean)**2 for y in log_freqs)
    ss_res = sum((y - (slope * x + intercept))**2 for x, y in zip(log_ranks, log_freqs))
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0

    return slope, r_squared

def conditional_entropy_decay(words, max_order=5):
    """Measure conditional entropy at increasing context sizes."""
    results = []
    for order in range(max_order + 1):
        if order == 0:
            h = calc_entropy(Counter(words))
            results.append((0, h))
        else:
            ngrams = []
            targets = []
            for i in range(order, len(words)):
                context = tuple(words[i-order:i])
                ngrams.append(context)
                targets.append(words[i])
            h_cond = calc_conditional_entropy(targets, ngrams)
            results.append((order, h_cond))
    return results


# ============================================================
# 5. SIMULATION
# ============================================================

def simulate_morpheme_cipher(prefix_dist, stem_dist, suffix_dist, n_words,
                             independence=True):
    """Generate synthetic text from morpheme-cipher model."""
    prefixes_list = list(prefix_dist.keys())
    prefix_probs = [prefix_dist[p] for p in prefixes_list]
    total_p = sum(prefix_probs)
    prefix_probs = [p/total_p for p in prefix_probs]

    stems_list = list(stem_dist.keys())
    stem_probs = [stem_dist[s] for s in stems_list]
    total_s = sum(stem_probs)
    stem_probs = [p/total_s for p in stem_probs]

    suffixes_list = list(suffix_dist.keys())
    suffix_probs = [suffix_dist[s] for s in suffixes_list]
    total_sf = sum(suffix_probs)
    suffix_probs = [p/total_sf for p in suffix_probs]

    words = []
    for _ in range(n_words):
        p = random.choices(prefixes_list, weights=prefix_probs, k=1)[0]
        s = random.choices(stems_list, weights=stem_probs, k=1)[0]
        sf = random.choices(suffixes_list, weights=suffix_probs, k=1)[0]
        words.append(p + s + sf)

    return words


# ============================================================
# MAIN ANALYSIS
# ============================================================

def main():
    filepath = r"C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt"
    words, page_words, line_words = parse_eva(filepath)

    print(f"Total words extracted: {len(words)}")
    print(f"Unique words (types): {len(set(words))}")
    print(f"Pages: {len(page_words)}")
    print()

    # ---- SEGMENTATION ----
    segmented = [segment_word(w) for w in words]

    prefixes_found = [s[0] for s in segmented]
    stems_found = [s[1] for s in segmented]
    suffixes_found = [s[2] for s in segmented]

    prefix_counter = Counter(prefixes_found)
    stem_counter = Counter(stems_found)
    suffix_counter = Counter(suffixes_found)

    # Exclude empty slots for some stats
    non_empty_prefixes = [p for p in prefixes_found if p]
    non_empty_suffixes = [s for s in suffixes_found if s]
    non_empty_stems = [s for s in stems_found if s]

    print("=" * 60)
    print("SEGMENTATION RESULTS")
    print("=" * 60)
    print(f"\nUnique prefixes (incl. empty): {len(prefix_counter)}")
    print(f"Unique stems: {len(stem_counter)}")
    print(f"Unique suffixes (incl. empty): {len(suffix_counter)}")
    print()

    # Words with all three parts
    full_seg = sum(1 for p, s, sf in segmented if p and s and sf)
    has_prefix = sum(1 for p, s, sf in segmented if p)
    has_suffix = sum(1 for p, s, sf in segmented if sf)
    has_stem = sum(1 for p, s, sf in segmented if s)

    print(f"Words with prefix: {has_prefix} ({100*has_prefix/len(words):.1f}%)")
    print(f"Words with stem: {has_stem} ({100*has_stem/len(words):.1f}%)")
    print(f"Words with suffix: {has_suffix} ({100*has_suffix/len(words):.1f}%)")
    print(f"Words with all three: {full_seg} ({100*full_seg/len(words):.1f}%)")
    print()

    print("Top 20 prefixes:")
    for p, c in prefix_counter.most_common(20):
        label = p if p else '(none)'
        print(f"  {label:>6}: {c:5d} ({100*c/len(words):.1f}%)")

    print("\nTop 30 stems:")
    for s, c in stem_counter.most_common(30):
        label = s if s else '(none)'
        print(f"  {label:>12}: {c:5d} ({100*c/len(words):.1f}%)")

    print("\nTop 20 suffixes:")
    for s, c in suffix_counter.most_common(20):
        label = s if s else '(none)'
        print(f"  {label:>6}: {c:5d} ({100*c/len(words):.1f}%)")

    # ---- MUTUAL INFORMATION ----
    print("\n" + "=" * 60)
    print("MUTUAL INFORMATION (INDEPENDENCE TEST)")
    print("=" * 60)

    # Only use words that have all three slots
    full_words = [(p, s, sf) for p, s, sf in segmented if p and s and sf]
    if len(full_words) > 100:
        fw_p = [x[0] for x in full_words]
        fw_s = [x[1] for x in full_words]
        fw_sf = [x[2] for x in full_words]

        mi_ps, nmi_ps = calc_mi(fw_p, fw_s)
        mi_ss, nmi_ss = calc_mi(fw_s, fw_sf)
        mi_psf, nmi_psf = calc_mi(fw_p, fw_sf)

        h_p = calc_entropy(Counter(fw_p))
        h_s = calc_entropy(Counter(fw_s))
        h_sf = calc_entropy(Counter(fw_sf))

        print(f"\nSlot entropies (fully segmented words, n={len(full_words)}):")
        print(f"  H(prefix)  = {h_p:.3f} bits")
        print(f"  H(stem)    = {h_s:.3f} bits")
        print(f"  H(suffix)  = {h_sf:.3f} bits")
        print(f"  Total if independent: {h_p + h_s + h_sf:.3f} bits")

        # Joint entropy
        joint_all = Counter(full_words)
        h_joint = calc_entropy(joint_all)
        print(f"  Actual joint entropy: {h_joint:.3f} bits")
        print(f"  Redundancy: {(h_p + h_s + h_sf) - h_joint:.3f} bits")

        print(f"\nMutual Information:")
        print(f"  MI(prefix, stem)   = {mi_ps:.4f} bits  (NMI = {nmi_ps:.4f})")
        print(f"  MI(stem, suffix)   = {mi_ss:.4f} bits  (NMI = {nmi_ss:.4f})")
        print(f"  MI(prefix, suffix) = {mi_psf:.4f} bits  (NMI = {nmi_psf:.4f})")

        print(f"\nInterpretation:")
        if max(nmi_ps, nmi_ss, nmi_psf) < 0.1:
            print("  ALL NMI < 0.1: STRONG independence => compositional cipher!")
        elif max(nmi_ps, nmi_ss, nmi_psf) < 0.2:
            print("  ALL NMI < 0.2: Moderate independence => likely compositional")
        else:
            print("  Some NMI >= 0.2: Significant correlation => morphological, not purely cipher")
            if nmi_ps >= 0.2:
                print(f"    prefix-stem correlated (NMI={nmi_ps:.3f})")
            if nmi_ss >= 0.2:
                print(f"    stem-suffix correlated (NMI={nmi_ss:.3f})")
            if nmi_psf >= 0.2:
                print(f"    prefix-suffix correlated (NMI={nmi_psf:.3f})")

    # ---- ALSO: MI for ALL words (including partial segmentation) ----
    print("\n\nMI for ALL words (including words with empty slots):")
    mi_ps2, nmi_ps2 = calc_mi(prefixes_found, stems_found)
    mi_ss2, nmi_ss2 = calc_mi(stems_found, suffixes_found)
    mi_psf2, nmi_psf2 = calc_mi(prefixes_found, suffixes_found)
    print(f"  MI(prefix, stem)   = {mi_ps2:.4f} bits  (NMI = {nmi_ps2:.4f})")
    print(f"  MI(stem, suffix)   = {mi_ss2:.4f} bits  (NMI = {nmi_ss2:.4f})")
    print(f"  MI(prefix, suffix) = {mi_psf2:.4f} bits  (NMI = {nmi_psf2:.4f})")

    # ---- PERMUTATION TEST for MI significance ----
    print("\n\nPermutation test (1000 shuffles) for fully-segmented words:")
    if len(full_words) > 100:
        n_perm = 1000
        mi_ps_null = []
        mi_ss_null = []
        mi_psf_null = []

        for _ in range(n_perm):
            shuf_p = list(fw_p)
            shuf_s = list(fw_s)
            shuf_sf = list(fw_sf)
            random.shuffle(shuf_p)
            random.shuffle(shuf_s)
            random.shuffle(shuf_sf)

            mi1, _ = calc_mi(shuf_p, fw_s)
            mi2, _ = calc_mi(fw_s, shuf_sf)
            mi3, _ = calc_mi(shuf_p, shuf_sf)
            mi_ps_null.append(mi1)
            mi_ss_null.append(mi2)
            mi_psf_null.append(mi3)

        print(f"  MI(prefix,stem):   observed={mi_ps:.4f}, null mean={sum(mi_ps_null)/n_perm:.4f}, "
              f"p={sum(1 for x in mi_ps_null if x >= mi_ps)/n_perm:.4f}")
        print(f"  MI(stem,suffix):   observed={mi_ss:.4f}, null mean={sum(mi_ss_null)/n_perm:.4f}, "
              f"p={sum(1 for x in mi_ss_null if x >= mi_ss)/n_perm:.4f}")
        print(f"  MI(prefix,suffix): observed={mi_psf:.4f}, null mean={sum(mi_psf_null)/n_perm:.4f}, "
              f"p={sum(1 for x in mi_psf_null if x >= mi_psf)/n_perm:.4f}")

    # ---- STEM ANALYSIS ----
    print("\n" + "=" * 60)
    print("STEM ANALYSIS")
    print("=" * 60)

    # Stems that appear in fully segmented words
    full_stem_counter = Counter(fw_s) if len(full_words) > 100 else Counter()
    all_stem_counter = Counter(stems_found)

    non_empty_stem_counter = Counter(s for s in stems_found if s)
    print(f"\nTotal unique stems (non-empty): {len(non_empty_stem_counter)}")

    # Hapax legomena
    hapax = sum(1 for s, c in non_empty_stem_counter.items() if c == 1)
    print(f"Hapax legomena (stems appearing once): {hapax}")
    print(f"Stems appearing 2+ times: {len(non_empty_stem_counter) - hapax}")
    print(f"Stems appearing 5+ times: {sum(1 for s, c in non_empty_stem_counter.items() if c >= 5)}")
    print(f"Stems appearing 10+ times: {sum(1 for s, c in non_empty_stem_counter.items() if c >= 10)}")

    # Stem length distribution
    stem_lengths = Counter(len(s) for s in stems_found if s)
    print(f"\nStem length distribution:")
    for length in sorted(stem_lengths.keys()):
        print(f"  length {length}: {stem_lengths[length]} ({100*stem_lengths[length]/sum(stem_lengths.values()):.1f}%)")

    # ---- SECTION ANALYSIS (prefix distribution by section) ----
    print("\n" + "=" * 60)
    print("PREFIX DISTRIBUTION BY SECTION")
    print("=" * 60)

    # Group pages into sections based on folio numbers
    sections = defaultdict(list)
    for page, pw in page_words.items():
        # Extract folio number
        fnum = re.match(r'f(\d+)', page)
        if fnum:
            n = int(fnum.group(1))
            if n <= 11:
                section = "Herbal-A"
            elif n <= 25:
                section = "Herbal-B"
            elif n <= 56:
                section = "Pharma"
            elif n <= 67:
                section = "Astro"
            elif n <= 84:
                section = "Bio"
            elif n <= 102:
                section = "Cosmo"
            elif n <= 116:
                section = "Stars"
            else:
                section = "Recipes"
        else:
            section = "Unknown"

        for w in pw:
            seg = segment_word(w)
            sections[section].append(seg)

    # Show prefix distribution per section
    for section in sorted(sections.keys()):
        segs = sections[section]
        sec_prefixes = Counter(s[0] for s in segs if s[0])
        total_sec = len(segs)
        if total_sec < 20:
            continue
        print(f"\n{section} (n={total_sec}):")
        for p, c in sec_prefixes.most_common(10):
            print(f"  {p:>5}: {c:4d} ({100*c/total_sec:.1f}%)")

    # ---- SUFFIX DISTRIBUTION BY SECTION ----
    print("\n" + "=" * 60)
    print("SUFFIX DISTRIBUTION BY SECTION")
    print("=" * 60)

    for section in sorted(sections.keys()):
        segs = sections[section]
        sec_suffixes = Counter(s[2] for s in segs if s[2])
        total_sec = len(segs)
        if total_sec < 20:
            continue
        print(f"\n{section} (n={total_sec}):")
        for sf, c in sec_suffixes.most_common(10):
            print(f"  {sf:>6}: {c:4d} ({100*c/total_sec:.1f}%)")

    # ---- STATISTICAL COMPARISON ----
    print("\n" + "=" * 60)
    print("STATISTICAL PROPERTIES")
    print("=" * 60)

    word_counter = Counter(words)

    # Entropy
    h_words = calc_entropy(word_counter)
    print(f"\nWord-level entropy: {h_words:.3f} bits")
    print(f"  (Natural language: 9-12 bits, Simple cipher: 6-8 bits)")

    # Zipf
    zipf = zipf_test(word_counter)
    if zipf:
        print(f"\nZipf slope: {zipf[0]:.3f} (ideal: -1.0)")
        print(f"Zipf R-squared: {zipf[1]:.3f}")

    # Conditional entropy decay
    print(f"\nConditional entropy decay:")
    ced = conditional_entropy_decay(words, max_order=4)
    for order, h in ced:
        print(f"  H(w|w_{'{-' + str(order) + '...-1}' if order > 0 else ''}) = {h:.3f} bits")

    # ---- SIMULATION ----
    print("\n" + "=" * 60)
    print("SIMULATION: Morpheme-Cipher Model")
    print("=" * 60)

    random.seed(42)

    # Use observed distributions
    sim_words = simulate_morpheme_cipher(
        prefix_counter, stem_counter, suffix_counter,
        n_words=len(words)
    )

    sim_counter = Counter(sim_words)

    print(f"\nSimulated text: {len(sim_words)} words, {len(sim_counter)} types")
    print(f"Voynich text:   {len(words)} words, {len(word_counter)} types")

    h_sim = calc_entropy(sim_counter)
    print(f"\nEntropy: simulated={h_sim:.3f}, voynich={h_words:.3f}")

    sim_zipf = zipf_test(sim_counter)
    if sim_zipf and zipf:
        print(f"Zipf slope: simulated={sim_zipf[0]:.3f}, voynich={zipf[0]:.3f}")
        print(f"Zipf R-sq:  simulated={sim_zipf[1]:.3f}, voynich={zipf[1]:.3f}")

    sim_ced = conditional_entropy_decay(sim_words, max_order=4)
    print(f"\nConditional entropy decay comparison:")
    for (o1, h1), (o2, h2) in zip(ced, sim_ced):
        print(f"  Order {o1}: voynich={h1:.3f}, simulated={h2:.3f}")

    # ---- TYPE-TOKEN RATIO ----
    print("\n" + "=" * 60)
    print("VOCABULARY FILL RATE")
    print("=" * 60)

    n_prefix = len([p for p in prefix_counter if p])  # non-empty
    n_stem = len([s for s in stem_counter if s])
    n_suffix = len([s for s in suffix_counter if s])
    theoretical_max = (n_prefix + 1) * (n_stem + 1) * (n_suffix + 1)  # +1 for empty

    print(f"\nDistinct prefixes: {n_prefix}")
    print(f"Distinct stems: {n_stem}")
    print(f"Distinct suffixes: {n_suffix}")
    print(f"Theoretical max vocabulary: {theoretical_max}")
    print(f"Observed vocabulary: {len(word_counter)}")
    print(f"Fill rate: {100*len(word_counter)/theoretical_max:.2f}%")

    # ---- CROSS-SLOT PATTERN ANALYSIS ----
    print("\n" + "=" * 60)
    print("SANDHI / CROSS-SLOT PATTERNS")
    print("=" * 60)

    # Check if suffix of word N correlates with prefix of word N+1
    suffix_prefix_pairs = []
    for i in range(len(segmented) - 1):
        sf = segmented[i][2]
        p_next = segmented[i+1][0]
        if sf and p_next:
            suffix_prefix_pairs.append((sf, p_next))

    if suffix_prefix_pairs:
        mi_sandhi, nmi_sandhi = calc_mi(
            [x[0] for x in suffix_prefix_pairs],
            [x[1] for x in suffix_prefix_pairs]
        )
        print(f"\nSuffix(N) -> Prefix(N+1) correlation:")
        print(f"  Pairs: {len(suffix_prefix_pairs)}")
        print(f"  MI = {mi_sandhi:.4f} bits  (NMI = {nmi_sandhi:.4f})")

        if nmi_sandhi > 0.05:
            print(f"  Sandhi detected: suffix influences next prefix")
            # Show top transitions
            trans = Counter(suffix_prefix_pairs)
            print(f"  Top transitions:")
            for (sf, p), c in trans.most_common(15):
                print(f"    {sf:>5} -> {p:<5}: {c:4d}")

    # ---- SUMMARY ----
    print("\n" + "=" * 60)
    print("SUMMARY / VERDICT")
    print("=" * 60)

    print(f"""
Morpheme Decomposition:
  - {n_prefix} distinct prefixes (hypothesis: ~15) {'MATCH' if 10 <= n_prefix <= 20 else 'MISMATCH'}
  - {n_stem} distinct stems (hypothesis: 100-200) {'MATCH' if 80 <= n_stem <= 300 else 'MISMATCH'}
  - {n_suffix} distinct suffixes (hypothesis: ~7-17) {'MATCH' if 5 <= n_suffix <= 25 else 'MISMATCH'}

Independence Test:
  - NMI(prefix,stem)   = {nmi_ps:.4f} {'INDEPENDENT' if nmi_ps < 0.15 else 'CORRELATED'}
  - NMI(stem,suffix)   = {nmi_ss:.4f} {'INDEPENDENT' if nmi_ss < 0.15 else 'CORRELATED'}
  - NMI(prefix,suffix) = {nmi_psf:.4f} {'INDEPENDENT' if nmi_psf < 0.15 else 'CORRELATED'}

Vocabulary:
  - Theoretical: {theoretical_max}, Observed: {len(word_counter)}, Fill: {100*len(word_counter)/theoretical_max:.1f}%

Statistical Match (simulated vs actual):
  - Entropy: sim={h_sim:.2f} vs actual={h_words:.2f}
  - Zipf slope: sim={sim_zipf[0]:.2f} vs actual={zipf[0]:.2f}
""")

    return {
        'words': words,
        'segmented': segmented,
        'prefix_counter': prefix_counter,
        'stem_counter': stem_counter,
        'suffix_counter': suffix_counter,
        'word_counter': word_counter,
        'mi_ps': (mi_ps, nmi_ps),
        'mi_ss': (mi_ss, nmi_ss),
        'mi_psf': (mi_psf, nmi_psf),
        'h_words': h_words,
        'n_prefix': n_prefix,
        'n_stem': n_stem,
        'n_suffix': n_suffix,
        'full_words': full_words,
        'sections': sections,
        'zipf': zipf,
        'sim_zipf': sim_zipf,
        'h_sim': h_sim,
        'ced': ced,
        'sim_ced': sim_ced,
    }

if __name__ == '__main__':
    results = main()
