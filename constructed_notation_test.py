#!/usr/bin/env python3
"""
Constructed Pharmaceutical Notation Hypothesis Test
Tests whether the Voynich manuscript is a designed notation system
rather than encoding a natural language.
"""

import re
import math
import random
from collections import Counter, defaultdict
from itertools import product as iter_product

# ============================================================
# STEP 1: Parse EVA transcription
# ============================================================

def parse_eva(filepath):
    """Extract words from EVA transcription, ignoring metadata."""
    words = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Skip comments and metadata
            if not line or line.startswith('#') or line.startswith('<f') and '>' in line and line.endswith('>'):
                continue
            # Extract the text part (after the folio/line reference)
            m = re.match(r'<[^>]+>\s+(.*)', line)
            if m:
                text = m.group(1)
            else:
                continue
            # Remove uncertain readings, alternate markers, etc.
            text = re.sub(r'\{[^}]*\}', '', text)  # Remove {alternatives}
            text = re.sub(r'@\d+;?', '', text)       # Remove @codes
            text = re.sub(r'[<>\[\]!*%\?]', '', text) # Remove markup
            text = re.sub(r"[',]", '', text)           # Remove quotes/commas
            # Split on dots and hyphens (word separators in EVA)
            tokens = re.split(r'[.\-\s]+', text)
            for t in tokens:
                t = t.strip()
                if t and len(t) > 0 and not t.startswith('$'):
                    words.append(t)
    return words

# ============================================================
# STEP 2: Morphological segmentation
# ============================================================

# Known prefixes (from prior analysis, ordered longest first)
PREFIXES = [
    'qok', 'qot', 'cph', 'cfh', 'cth', 'ckh',
    'ot', 'ok', 'op', 'ol',
    'qo', 'sh', 'ch', 'ck', 'ct',
    'd', 'k', 'p', 'q', 's', 't', 'y', 'o', 'f',
]

# Known suffixes (ordered longest first)
SUFFIXES = [
    'aiin', 'aiir', 'aiim', 'aiil', 'aiis',
    'ain', 'air', 'aim', 'ail',
    'iin', 'iir', 'iim',
    'eey', 'ees', 'eeg',
    'edy', 'ely', 'ory', 'ary', 'ody',
    'am', 'an', 'ar', 'al',
    'dy', 'ty', 'sy', 'ky', 'ry', 'ly', 'my',
    'ol', 'or', 'om', 'os',
    'ey', 'ay',
    'y', 'n', 'l', 'r', 'm', 's', 'o',
]

def segment_word(word):
    """Attempt to segment a Voynich word into prefix + root + suffix."""
    if len(word) < 2:
        return (None, word, None)

    prefix = None
    suffix = None
    remainder = word

    # Try prefixes
    for p in PREFIXES:
        if remainder.startswith(p) and len(remainder) > len(p):
            prefix = p
            remainder = remainder[len(p):]
            break

    # Try suffixes
    for s in SUFFIXES:
        if remainder.endswith(s) and len(remainder) > len(s):
            suffix = s
            remainder = remainder[:-len(s)]
            break

    # If remainder is empty after stripping, treat whole word as root
    if not remainder:
        return (None, word, None)

    return (prefix, remainder, suffix)


def segment_word_strict(word):
    """Stricter segmentation: only segment if root is 1-4 chars."""
    prefix, root, suffix = segment_word(word)
    if root and 1 <= len(root) <= 4:
        return (prefix, root, suffix)
    # Try without prefix
    if prefix:
        new_root = prefix + root
        if 1 <= len(new_root) <= 4:
            return (None, new_root, suffix)
    # Try without suffix
    if suffix:
        new_root = root + suffix
        if 1 <= len(new_root) <= 4:
            return (prefix, new_root, None)
    return (None, word, None)


# ============================================================
# MAIN ANALYSIS
# ============================================================

def main():
    filepath = "C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt"
    words = parse_eva(filepath)

    print(f"Total words extracted: {len(words)}")
    print(f"Unique words: {len(set(words))}")

    freq = Counter(words)
    print(f"\nTop 30 words:")
    for w, c in freq.most_common(30):
        print(f"  {w:20s} {c}")

    # ============================================================
    # TEST 1: PRODUCTIVITY TEST (Fill Rate)
    # ============================================================
    print("\n" + "="*70)
    print("TEST 1: PRODUCTIVITY (Fill Rate)")
    print("="*70)

    # Segment all words
    segmented = []
    for w in words:
        seg = segment_word(w)
        segmented.append((w, seg))

    # Count segmented vs unsegmented
    has_prefix = sum(1 for _, (p, r, s) in segmented if p is not None)
    has_suffix = sum(1 for _, (p, r, s) in segmented if s is not None)
    has_both = sum(1 for _, (p, r, s) in segmented if p is not None and s is not None)

    print(f"Words with prefix: {has_prefix} ({100*has_prefix/len(words):.1f}%)")
    print(f"Words with suffix: {has_suffix} ({100*has_suffix/len(words):.1f}%)")
    print(f"Words with both:   {has_both} ({100*has_both/len(words):.1f}%)")

    # Collect observed prefixes, roots, suffixes
    obs_prefixes = set()
    obs_roots = set()
    obs_suffixes = set()
    obs_combinations = set()

    for w, (p, r, s) in segmented:
        if p: obs_prefixes.add(p)
        obs_roots.add(r)
        if s: obs_suffixes.add(s)
        obs_combinations.add((p, r, s))

    # Use top prefixes, roots, suffixes for fill rate calculation
    prefix_freq = Counter(p for _, (p, r, s) in segmented if p)
    root_freq = Counter(r for _, (p, r, s) in segmented)
    suffix_freq = Counter(s for _, (p, r, s) in segmented if s)

    print(f"\nDistinct prefixes: {len(obs_prefixes)}")
    print(f"Distinct roots: {len(obs_roots)}")
    print(f"Distinct suffixes: {len(obs_suffixes)}")

    # Top N for fill rate
    top_prefixes = [p for p, _ in prefix_freq.most_common(15)]
    top_roots = [r for r, _ in root_freq.most_common(50)]
    top_suffixes = [s for s, _ in suffix_freq.most_common(10)]

    print(f"\nTop 15 prefixes: {top_prefixes}")
    print(f"Top 10 suffixes: {[s for s, _ in suffix_freq.most_common(10)]}")

    # Calculate theoretical vs actual combinations
    # Include None as a prefix/suffix option
    all_p = [None] + top_prefixes
    all_s = [None] + top_suffixes

    theoretical = len(all_p) * len(top_roots) * len(all_s)
    actual = len(obs_combinations.intersection(
        set(iter_product(all_p, top_roots, all_s))
    ))

    # Count more carefully
    actual_in_space = 0
    for combo in obs_combinations:
        p, r, s = combo
        if (p is None or p in top_prefixes) and r in top_roots and (s is None or s in top_suffixes):
            actual_in_space += 1

    fill_rate = actual_in_space / theoretical if theoretical > 0 else 0

    print(f"\nTheoretical space (16 prefix slots x 50 roots x 11 suffix slots): {theoretical}")
    print(f"Actually observed combinations in this space: {actual_in_space}")
    print(f"FILL RATE: {fill_rate:.4f} ({100*fill_rate:.2f}%)")
    print(f"\nInterpretation:")
    print(f"  Natural language typical fill rate: 1-5%")
    print(f"  Constructed notation expected: 20-80%")
    print(f"  Observed: {100*fill_rate:.2f}%")

    # ============================================================
    # TEST 2: PARADIGM REGULARITY
    # ============================================================
    print("\n" + "="*70)
    print("TEST 2: PARADIGM REGULARITY")
    print("="*70)

    # For each prefix, which roots does it combine with?
    prefix_root_pairs = defaultdict(set)
    for _, (p, r, s) in segmented:
        if p:
            prefix_root_pairs[p].add(r)

    # Top roots by frequency
    common_roots = [r for r, _ in root_freq.most_common(20)]

    print(f"\nTop 20 roots: {common_roots}")
    print(f"\nPrefix-Root matrix (top 10 prefixes x top 20 roots):")

    top10_prefixes = [p for p, _ in prefix_freq.most_common(10)]

    # Header
    header = f"{'prefix':>8} | " + " ".join(f"{r:>6}" for r in common_roots[:15])
    print(header)
    print("-" * len(header))

    paradigm_completeness = {}
    for p in top10_prefixes:
        roots_with_p = prefix_root_pairs[p]
        row = f"{p:>8} | "
        count = 0
        for r in common_roots[:15]:
            if r in roots_with_p:
                row += f"{'X':>6} "
                count += 1
            else:
                row += f"{'.':>6} "
        completeness = count / 15
        paradigm_completeness[p] = completeness
        row += f"  ({100*completeness:.0f}%)"
        print(row)

    avg_completeness = sum(paradigm_completeness.values()) / len(paradigm_completeness)
    print(f"\nAverage paradigm completeness: {100*avg_completeness:.1f}%")
    print(f"  Natural language expected: 30-60% (many lexical gaps)")
    print(f"  Constructed notation expected: 70-100% (all combinations valid)")

    # ============================================================
    # TEST 3: PHONOTACTIC CONSTRAINTS
    # ============================================================
    print("\n" + "="*70)
    print("TEST 3: PHONOTACTIC CONSTRAINTS (Bigram Analysis)")
    print("="*70)

    # EVA alphabet
    eva_chars = set()
    for w in words:
        for c in w:
            eva_chars.add(c)

    eva_chars = sorted(eva_chars)
    print(f"Distinct characters: {len(eva_chars)}")
    print(f"Characters: {' '.join(eva_chars)}")

    # Count bigrams
    bigram_counts = Counter()
    for w in words:
        for i in range(len(w) - 1):
            bigram_counts[w[i:i+2]] += 1

    # Theoretical possible bigrams
    possible_bigrams = len(eva_chars) ** 2
    observed_bigrams = len(bigram_counts)

    bigram_fill = observed_bigrams / possible_bigrams

    print(f"\nPossible bigrams: {possible_bigrams}")
    print(f"Observed bigrams: {observed_bigrams}")
    print(f"Bigram fill rate: {100*bigram_fill:.1f}%")
    print(f"Forbidden bigrams: {possible_bigrams - observed_bigrams}")

    # Find forbidden sequences among common characters
    common_chars = [c for c, _ in Counter(c for w in words for c in w).most_common(15)]
    print(f"\nTop 15 characters: {common_chars}")

    forbidden_common = []
    for a in common_chars[:10]:
        for b in common_chars[:10]:
            bg = a + b
            if bg not in bigram_counts:
                forbidden_common.append(bg)

    print(f"Forbidden bigrams among top 10 chars: {len(forbidden_common)}")
    print(f"  (out of {100} possible = {100*len(forbidden_common)/100:.0f}% forbidden)")
    if forbidden_common:
        print(f"  Examples: {forbidden_common[:20]}")

    # Compare with natural language ratios
    print(f"\nComparative bigram fill rates:")
    print(f"  Latin (26 chars):     ~45-55% of bigrams observed")
    print(f"  Italian (26 chars):   ~40-50% of bigrams observed")
    print(f"  Esperanto (28 chars): ~35-45% of bigrams observed")
    print(f"  Voynich ({len(eva_chars)} chars): {100*bigram_fill:.1f}% of bigrams observed")

    # Top and bottom bigrams
    print(f"\nTop 20 bigrams:")
    for bg, c in bigram_counts.most_common(20):
        print(f"  {bg}: {c}")

    # ============================================================
    # TEST 4: MORPHEME BOUNDARY CLARITY
    # ============================================================
    print("\n" + "="*70)
    print("TEST 4: MORPHEME BOUNDARY CLARITY")
    print("="*70)

    # Try to segment every word; measure how cleanly
    clean_seg = 0  # Prefix+known_root+suffix
    partial_seg = 0  # At least one affix identified
    unsegmentable = 0
    ambiguous = 0  # Could be segmented multiple ways

    root_lengths = []

    for w in set(words):
        p, r, s = segment_word(w)

        if p is not None and s is not None:
            clean_seg += 1
            root_lengths.append(len(r))
        elif p is not None or s is not None:
            partial_seg += 1
            root_lengths.append(len(r))
        else:
            unsegmentable += 1

    total_unique = len(set(words))
    print(f"Clean segmentation (prefix+root+suffix): {clean_seg} ({100*clean_seg/total_unique:.1f}%)")
    print(f"Partial segmentation (prefix or suffix): {partial_seg} ({100*partial_seg/total_unique:.1f}%)")
    print(f"Unsegmentable: {unsegmentable} ({100*unsegmentable/total_unique:.1f}%)")

    if root_lengths:
        avg_root = sum(root_lengths) / len(root_lengths)
        print(f"\nAverage root length: {avg_root:.2f} characters")
        print(f"Root length distribution:")
        rl_counter = Counter(root_lengths)
        for length in sorted(rl_counter.keys()):
            print(f"  {length} chars: {rl_counter[length]} roots ({100*rl_counter[length]/len(root_lengths):.1f}%)")

    # Test for fusion: do roots change form depending on affixes?
    print(f"\nFusion test: Do roots change form with different affixes?")
    root_variants = defaultdict(lambda: defaultdict(set))
    for w, (p, r, s) in segmented:
        if r and len(r) >= 2:
            # Group roots that share first 2 chars
            root_base = r[:2]
            root_variants[root_base][(p, s)].add(r)

    fusion_count = 0
    no_fusion = 0
    for base, contexts in root_variants.items():
        unique_roots = set()
        for ctx, roots in contexts.items():
            unique_roots.update(roots)
        if len(unique_roots) > 1:
            fusion_count += 1
        else:
            no_fusion += 1

    total_bases = fusion_count + no_fusion
    if total_bases > 0:
        print(f"  Root bases with variant forms: {fusion_count} ({100*fusion_count/total_bases:.1f}%)")
        print(f"  Root bases with invariant form: {no_fusion} ({100*no_fusion/total_bases:.1f}%)")
        print(f"  Natural language: high fusion (30-60%)")
        print(f"  Constructed notation: low fusion (5-15%)")

    # ============================================================
    # TEST 5: HISTORICAL CONTEXT
    # ============================================================
    print("\n" + "="*70)
    print("TEST 5: HISTORICAL CONTEXT (Summary)")
    print("="*70)
    print("""
    15th-century systematic notation precedents:

    1. Ramon Llull's Ars Magna (1305): Combinatorial system using letters
       to represent concepts, combined by wheels to generate propositions.
       DIRECTLY RELEVANT: shows the idea of systematic combination existed.

    2. Alchemical notation (13th-16th c.): Systematic symbols for substances
       (mercury, sulfur, etc.) and processes (distillation, calcination).
       Intentionally obscure to protect trade secrets.

    3. Pharmacopeial abbreviations: Apothecaries used abbreviations like
       'aa' (ana = equal parts), 'Rx' (recipe), quantity markers.
       A MORE SYSTEMATIC version would look like prefix+ingredient+preparation.

    4. Giovanni Fontana (1395-1455): Venetian engineer who used a cipher
       system in his notebooks. Contemporary with Voynich dating.

    5. Steganography: The 15th century saw growing interest in hidden writing
       (Trithemius later formalized this in 1499).

    6. Herbarium tradition: Systematic plant catalogs existed (Dioscorides),
       but no systematic NOTATION for plant properties.

    The KEY INSIGHT: A 15th-century pharmaceutical practitioner who knew
    Llull's combinatorial method could design a notation where:
    - Prefixes = plant/substance categories
    - Roots = specific plants or preparations
    - Suffixes = dosage form, preparation method, or application
    """)

    # ============================================================
    # TEST 6: SIMULATION - Can a notation system produce natural stats?
    # ============================================================
    print("\n" + "="*70)
    print("TEST 6: SIMULATION - Constructed Notation with Natural-Like Statistics")
    print("="*70)

    # Design a notation system
    N_PREFIXES = 15
    N_ROOTS = 150
    N_SUFFIXES = 7

    # Assign Zipfian frequencies to roots (some plants/concepts more common)
    root_probs = [1.0/(i+1)**1.0 for i in range(N_ROOTS)]
    root_sum = sum(root_probs)
    root_probs = [p/root_sum for p in root_probs]

    # Prefix probabilities (some categories more discussed)
    prefix_probs = [1.0/(i+1)**0.8 for i in range(N_PREFIXES)]
    # Add "no prefix" option
    prefix_probs = [0.3] + [0.7 * p / sum(prefix_probs) for p in prefix_probs]
    psum = sum(prefix_probs)
    prefix_probs = [p/psum for p in prefix_probs]

    # Suffix probabilities
    suffix_probs = [1.0/(i+1)**0.7 for i in range(N_SUFFIXES)]
    suffix_probs = [0.25] + [0.75 * p / sum(suffix_probs) for p in suffix_probs]
    ssum = sum(suffix_probs)
    suffix_probs = [p/ssum for p in suffix_probs]

    # Generate pseudo-morphemes
    sim_prefixes = [''] + [f'P{i}' for i in range(N_PREFIXES)]
    sim_roots = [f'R{i}' for i in range(N_ROOTS)]
    sim_suffixes = [''] + [f'S{i}' for i in range(N_SUFFIXES)]

    # Sandhi rules: some prefix+root combinations are modified
    # (about 10% of combinations have a variant form)
    sandhi_rules = set()
    random.seed(42)
    for _ in range(int(0.1 * N_PREFIXES * N_ROOTS)):
        pi = random.randint(0, N_PREFIXES)
        ri = random.randint(0, N_ROOTS - 1)
        sandhi_rules.add((pi, ri))

    # Generate text
    sim_words = []
    N_WORDS = len(words)  # Same length as Voynich

    for _ in range(N_WORDS):
        pi = random.choices(range(len(sim_prefixes)), weights=prefix_probs)[0]
        ri = random.choices(range(N_ROOTS), weights=root_probs)[0]
        si = random.choices(range(len(sim_suffixes)), weights=suffix_probs)[0]

        word = sim_prefixes[pi] + sim_roots[ri] + sim_suffixes[si]

        # Apply sandhi
        if (pi, ri) in sandhi_rules:
            word = word + 'x'  # Modification marker

        sim_words.append(word)

    # Measure Zipf's law compliance
    sim_freq = Counter(sim_words)
    sim_ranked = sim_freq.most_common()

    print(f"Simulated text: {len(sim_words)} words, {len(sim_freq)} unique")

    # Zipf test: log(freq) vs log(rank) correlation
    import numpy as np

    # Voynich Zipf
    voynich_ranked = freq.most_common()
    v_ranks = np.log([i+1 for i in range(min(200, len(voynich_ranked)))])
    v_freqs = np.log([c for _, c in voynich_ranked[:200]])
    v_corr = np.corrcoef(v_ranks, v_freqs)[0, 1]

    # Simulation Zipf
    s_ranks = np.log([i+1 for i in range(min(200, len(sim_ranked)))])
    s_freqs = np.log([c for _, c in sim_ranked[:200]])
    s_corr = np.corrcoef(s_ranks, s_freqs)[0, 1]

    print(f"\nZipf's law (log-log correlation, top 200 words):")
    print(f"  Voynich:    r = {v_corr:.4f}")
    print(f"  Simulation: r = {s_corr:.4f}")

    # Zipf exponent (slope)
    v_slope = np.polyfit(v_ranks, v_freqs, 1)[0]
    s_slope = np.polyfit(s_ranks, s_freqs, 1)[0]
    print(f"  Voynich Zipf exponent:    {-v_slope:.3f}")
    print(f"  Simulation Zipf exponent: {-s_slope:.3f}")
    print(f"  Natural language typical:  0.8-1.2")

    # Entropy measurement
    def word_entropy(word_list):
        """Calculate Shannon entropy of word distribution."""
        total = len(word_list)
        counts = Counter(word_list)
        H = 0
        for c in counts.values():
            p = c / total
            if p > 0:
                H -= p * math.log2(p)
        return H

    def char_entropy(word_list):
        """Calculate character-level entropy."""
        all_chars = ''.join(word_list)
        total = len(all_chars)
        counts = Counter(all_chars)
        H = 0
        for c in counts.values():
            p = c / total
            if p > 0:
                H -= p * math.log2(p)
        return H

    def conditional_entropy_char(word_list, order=1):
        """Character-level conditional entropy."""
        text = ' '.join(word_list)
        ngram_counts = Counter()
        context_counts = Counter()
        for i in range(len(text) - order):
            context = text[i:i+order]
            ngram = text[i:i+order+1]
            context_counts[context] += 1
            ngram_counts[ngram] += 1

        H = 0
        total = sum(ngram_counts.values())
        for ngram, count in ngram_counts.items():
            context = ngram[:-1]
            p_joint = count / total
            p_cond = count / context_counts[context]
            H -= p_joint * math.log2(p_cond)
        return H

    v_H0 = char_entropy(words)
    v_H1 = conditional_entropy_char(words, 1)
    v_H2 = conditional_entropy_char(words, 2)

    s_H0 = char_entropy(sim_words)

    print(f"\nEntropy measures:")
    print(f"  Voynich char entropy H0: {v_H0:.3f} bits")
    print(f"  Voynich H1 (1st order): {v_H1:.3f} bits")
    print(f"  Voynich H2 (2nd order): {v_H2:.3f} bits")
    print(f"  Simulation char entropy H0: {s_H0:.3f} bits")

    # Hapax legomena ratio
    v_hapax = sum(1 for w, c in freq.items() if c == 1)
    s_hapax = sum(1 for w, c in sim_freq.items() if c == 1)

    print(f"\nHapax legomena (words occurring once):")
    print(f"  Voynich: {v_hapax} / {len(freq)} unique = {100*v_hapax/len(freq):.1f}%")
    print(f"  Simulation: {s_hapax} / {len(sim_freq)} unique = {100*s_hapax/len(sim_freq):.1f}%")
    print(f"  Natural language typical: 40-60%")

    # Type-token ratio
    v_ttr = len(freq) / len(words)
    s_ttr = len(sim_freq) / len(sim_words)
    print(f"\nType-token ratio:")
    print(f"  Voynich: {v_ttr:.4f}")
    print(f"  Simulation: {s_ttr:.4f}")

    # ============================================================
    # TEST 6b: Enhanced simulation with context-dependent usage
    # ============================================================
    print(f"\n--- Enhanced simulation with topic clustering ---")

    # In a pharmaceutical text, topics cluster (e.g., a page about digestive herbs)
    # This creates long-range correlations

    sim2_words = []
    topic_roots = {}  # Each topic emphasizes certain roots
    N_TOPICS = 30
    for t in range(N_TOPICS):
        # Each topic has 10-20 preferred roots
        n_topic_roots = random.randint(10, 20)
        topic_roots[t] = random.sample(range(N_ROOTS), n_topic_roots)

    words_per_topic = N_WORDS // N_TOPICS

    for t in range(N_TOPICS):
        preferred = topic_roots[t]
        # Modified root probabilities for this topic
        topic_probs = list(root_probs)
        for ri in preferred:
            topic_probs[ri] *= 5.0  # 5x boost for topic-relevant roots
        tp_sum = sum(topic_probs)
        topic_probs = [p/tp_sum for p in topic_probs]

        for _ in range(words_per_topic):
            pi = random.choices(range(len(sim_prefixes)), weights=prefix_probs)[0]
            ri = random.choices(range(N_ROOTS), weights=topic_probs)[0]
            si = random.choices(range(len(sim_suffixes)), weights=suffix_probs)[0]

            word = sim_prefixes[pi] + sim_roots[ri] + sim_suffixes[si]
            if (pi, ri) in sandhi_rules:
                word = word + 'x'
            sim2_words.append(word)

    sim2_freq = Counter(sim2_words)
    sim2_ranked = sim2_freq.most_common()

    s2_ranks = np.log([i+1 for i in range(min(200, len(sim2_ranked)))])
    s2_freqs = np.log([c for _, c in sim2_ranked[:200]])
    s2_corr = np.corrcoef(s2_ranks, s2_freqs)[0, 1]
    s2_slope = np.polyfit(s2_ranks, s2_freqs, 1)[0]

    s2_hapax = sum(1 for w, c in sim2_freq.items() if c == 1)

    print(f"Topic-clustered simulation: {len(sim2_words)} words, {len(sim2_freq)} unique")
    print(f"  Zipf correlation: r = {s2_corr:.4f}")
    print(f"  Zipf exponent: {-s2_slope:.3f}")
    print(f"  Hapax ratio: {100*s2_hapax/len(sim2_freq):.1f}%")
    print(f"  Type-token ratio: {len(sim2_freq)/len(sim2_words):.4f}")

    # ============================================================
    # SYNTHESIS
    # ============================================================
    print("\n" + "="*70)
    print("SYNTHESIS: CONSTRUCTED NOTATION HYPOTHESIS ASSESSMENT")
    print("="*70)

    print(f"""
    Test 1 - Fill Rate: {100*fill_rate:.2f}%
      Verdict: {'SUPPORTS constructed' if fill_rate > 0.10 else 'SUPPORTS natural language' if fill_rate < 0.05 else 'INCONCLUSIVE'}

    Test 2 - Paradigm Completeness: {100*avg_completeness:.1f}%
      Verdict: {'SUPPORTS constructed' if avg_completeness > 0.60 else 'SUPPORTS natural language' if avg_completeness < 0.35 else 'INCONCLUSIVE'}

    Test 3 - Bigram Fill Rate: {100*bigram_fill:.1f}%
      Verdict: Analysis needed (see comparative data above)

    Test 4 - Segmentability: {100*clean_seg/total_unique:.1f}% cleanly segmented
      Verdict: {'SUPPORTS constructed' if clean_seg/total_unique > 0.40 else 'INCONCLUSIVE'}

    Test 6 - Simulation Match:
      Zipf: Voynich={-v_slope:.3f}, Sim={-s_slope:.3f}, Topic-Sim={-s2_slope:.3f}
      Verdict: {'YES' if abs(v_slope - s2_slope) < 0.3 else 'NO'} - simulation CAN reproduce Zipf-like distribution
    """)

    return {
        'fill_rate': fill_rate,
        'paradigm_completeness': avg_completeness,
        'bigram_fill': bigram_fill,
        'segmentability': clean_seg / total_unique,
        'voynich_zipf_slope': -v_slope,
        'sim_zipf_slope': -s_slope,
        'sim2_zipf_slope': -s2_slope,
        'voynich_hapax': v_hapax / len(freq),
        'voynich_ttr': v_ttr,
        'voynich_H0': v_H0,
        'voynich_H1': v_H1,
        'voynich_H2': v_H2,
    }

if __name__ == '__main__':
    results = main()
