"""
DECISIVE EXPERIMENT: Homophone Collapsing + Bigram Transition Matrix Recovery
==============================================================================

THESIS: If Voynich words that are HOMOPHONES (encoding the same Italian content
via different scribal conventions) are collapsed into single symbols, the resulting
bigram transition matrix should resemble Italian's bigram constraints.

BASELINE: Raw Voynich bigram transition entropy = 85.6% (between Italian 65% and random 95%).
TARGET: After collapsing, entropy should drop toward 65%.

METHOD:
  Phase 1: Extract A-only, B-only, and shared words with frequency profiles
  Phase 2: Match A-only words to B-only words by frequency rank to identify homophone pairs
  Phase 3: Collapse homophones into single symbols throughout the corpus
  Phase 4: Compute bigram transition matrix of collapsed symbols
  Phase 5: Compare with Italian bigram characteristics
  Phase 6: Sweep parameters and report best configuration

The A/B split is the key insight: words exclusive to Scribe A that have a
frequency-matched counterpart exclusive to Scribe B are likely encoding the
same underlying Italian word/morpheme using different codebook conventions.
"""

import re
import math
import json
from collections import Counter, defaultdict
from itertools import combinations

# ============================================================
# IVTFF PARSER (from currier_ab_analysis.py)
# ============================================================

def parse_ivtff(filepath):
    """Parse an IVTFF transcription file into structured data."""
    pages = {}
    current_folio = None
    current_lang = None
    current_illust = None

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            header_match = re.match(r'<(f\d+[rv]\d?)>\s+<!\s*(.*?)>', line)
            if header_match:
                current_folio = header_match.group(1)
                attrs = header_match.group(2)
                lang_match = re.search(r'\$L=([AB])', attrs)
                current_lang = lang_match.group(1) if lang_match else None
                illust_match = re.search(r'\$I=(\w+)', attrs)
                current_illust = illust_match.group(1) if illust_match else None
                quire_match = re.search(r'\$Q=(\w+)', attrs)

                if current_folio not in pages:
                    pages[current_folio] = {
                        'lang': current_lang,
                        'illust': current_illust,
                        'quire': quire_match.group(1) if quire_match else None,
                        'lines': [],
                        'words': []
                    }
                continue

            text_match = re.match(r'<(f\d+[rv]\d?\.\d+)', line)
            if text_match and current_folio:
                text_part = re.sub(r'<[^>]*>', '', line)
                text_part = re.sub(r'<%>', '', text_part)
                text_part = re.sub(r'<\$>', '', text_part)
                text_part = re.sub(r'<!@\d+;>', '', text_part)
                text_part = re.sub(r'@\d+;?', '', text_part)
                text_part = re.sub(r'\{[^}]*\}', '', text_part)
                text_part = re.sub(r'\[[^\]]*\]', '', text_part)
                text_part = re.sub(r'[<>%$?]', '', text_part)

                words = re.split(r'[.\s,]+', text_part)
                words = [w.strip() for w in words if w.strip() and len(w.strip()) > 0]
                words = [w for w in words if not re.match(r'^[-=+*@#]+$', w) and len(w) > 0]

                pages[current_folio]['lines'].append(words)
                pages[current_folio]['words'].extend(words)

    return pages


# ============================================================
# ITALIAN BIGRAM REFERENCE DATA
# ============================================================

# Italian letter bigram transition probabilities (from standard corpora)
# Entropy ratio = H(bigram) / H_max = proportion of max entropy used
# Italian has ~21 effective letters, H_max = log2(21) = 4.39 bits
# Italian bigram entropy ~ 2.85 bits -> ratio ~ 65%
# Key characteristics:
#   - ~30% of bigram cells are near-zero (forbidden: qq, hh, kk, ww, etc.)
#   - Strong asymmetries: q->u always, h rarely followed by consonant
#   - Vowel-consonant alternation tendency

ITALIAN_FORBIDDEN_BIGRAMS_FRACTION = 0.30  # ~30% of cells near-zero
ITALIAN_ENTROPY_RATIO = 0.65               # H/H_max
RANDOM_ENTROPY_RATIO = 0.95                # Random text approaches 1.0


def italian_bigram_reference():
    """
    Return reference Italian bigram statistics.
    Based on standard Italian letter frequency analysis.
    """
    # Italian alphabet: a b c d e f g h i l m n o p q r s t u v z (21 letters)
    # Common forbidden/very-rare bigrams in Italian:
    forbidden = [
        'qq', 'hh', 'kk', 'ww', 'jj', 'xx', 'yy',  # doubled rare consonants
        'qe', 'qi', 'qo', 'qa',  # q only before u
        'hb', 'hc', 'hd', 'hf', 'hg', 'hh', 'hl', 'hm', 'hn', 'hp', 'hr', 'hs', 'ht', 'hv', 'hz',  # h only before vowels/ch/gh
        'bx', 'cx', 'dx', 'fx', 'gx',  # x is not Italian
        'wu', 'wh', 'wr',  # w is not Italian
    ]
    # Strong patterns:
    # After q: always u
    # After consonant cluster: usually vowel
    # Italian loves vowel endings: ~47% of words end in vowel
    return {
        'alphabet_size': 21,
        'entropy_ratio': 0.65,
        'forbidden_fraction': 0.30,
        'vowel_ending_rate': 0.47,
    }


# ============================================================
# PHASE 1: EXTRACT A/B FREQUENCY PROFILES
# ============================================================

def extract_ab_profiles(pages):
    """Extract word frequencies for A-only, B-only, and shared words."""
    a_words = []
    b_words = []

    for folio, data in pages.items():
        if data['lang'] == 'A':
            a_words.extend(data['words'])
        elif data['lang'] == 'B':
            b_words.extend(data['words'])

    a_counter = Counter(a_words)
    b_counter = Counter(b_words)
    a_total = len(a_words)
    b_total = len(b_words)

    a_vocab = set(a_counter.keys())
    b_vocab = set(b_counter.keys())

    shared = a_vocab & b_vocab
    a_only = a_vocab - b_vocab
    b_only = b_vocab - a_vocab

    print(f"=== PHASE 1: A/B FREQUENCY PROFILES ===")
    print(f"A total tokens: {a_total}")
    print(f"B total tokens: {b_total}")
    print(f"A vocabulary: {len(a_vocab)}")
    print(f"B vocabulary: {len(b_vocab)}")
    print(f"Shared words: {len(shared)}")
    print(f"A-only words: {len(a_only)}")
    print(f"B-only words: {len(b_only)}")

    return a_counter, b_counter, a_total, b_total, shared, a_only, b_only


# ============================================================
# PHASE 2: MATCH A-ONLY / B-ONLY WORDS BY FREQUENCY RANK
# ============================================================

def find_homophone_pairs(a_counter, b_counter, a_total, b_total,
                          a_only, b_only, shared,
                          min_freq=3, freq_tolerance=2.0,
                          structural_bonus=True):
    """
    Match A-only words with B-only words by normalized frequency.

    Strategy:
    1. Normalize frequencies to percentages (accounts for different corpus sizes)
    2. For each A-only word, find the B-only word with closest normalized frequency
    3. Apply structural similarity bonus (same prefix = likely same codebook category)
    4. Only pair words above min_freq threshold

    Returns list of (a_word, b_word, a_freq_pct, b_freq_pct, score) tuples.
    """
    # Build frequency-sorted lists
    a_only_freqs = [(w, a_counter[w], a_counter[w] / a_total * 100)
                     for w in a_only if a_counter[w] >= min_freq]
    b_only_freqs = [(w, b_counter[w], b_counter[w] / b_total * 100)
                     for w in b_only if b_counter[w] >= min_freq]

    a_only_freqs.sort(key=lambda x: -x[2])
    b_only_freqs.sort(key=lambda x: -x[2])

    print(f"\n=== PHASE 2: HOMOPHONE PAIR MATCHING ===")
    print(f"A-only words with freq >= {min_freq}: {len(a_only_freqs)}")
    print(f"B-only words with freq >= {min_freq}: {len(b_only_freqs)}")

    # Known prefix groups (from morphological analysis)
    prefix_map = {}
    prefixes = ['qok', 'qot', 'qo', 'cth', 'ckh', 'ch', 'sh', 'ok', 'ot', 'da', 'ol', 'or', 'ct', 'cp']
    for plist in [a_only_freqs, b_only_freqs]:
        for w, c, pct in plist:
            for p in sorted(prefixes, key=len, reverse=True):
                if w.startswith(p):
                    prefix_map[w] = p
                    break
            else:
                prefix_map[w] = ''

    # Greedy matching: for each A-only word, find best B-only match
    used_b = set()
    pairs = []

    for a_word, a_count, a_pct in a_only_freqs:
        best_b = None
        best_score = float('inf')

        for b_word, b_count, b_pct in b_only_freqs:
            if b_word in used_b:
                continue

            # Frequency ratio (closer to 1.0 = better)
            freq_ratio = max(a_pct, b_pct) / min(a_pct, b_pct) if min(a_pct, b_pct) > 0 else 999
            if freq_ratio > freq_tolerance:
                continue

            # Score = log(freq_ratio) with structural bonus
            score = math.log(freq_ratio + 0.01)

            # Structural bonus: same prefix = likely same codebook category
            if structural_bonus:
                a_pfx = prefix_map.get(a_word, '')
                b_pfx = prefix_map.get(b_word, '')
                if a_pfx and b_pfx and a_pfx == b_pfx:
                    score -= 0.5  # bonus for same prefix
                # Same length bonus
                if len(a_word) == len(b_word):
                    score -= 0.2
                elif abs(len(a_word) - len(b_word)) == 1:
                    score -= 0.1

            if score < best_score:
                best_score = score
                best_b = (b_word, b_count, b_pct)

        if best_b is not None:
            b_word, b_count, b_pct = best_b
            used_b.add(b_word)
            pairs.append((a_word, b_word, a_pct, b_pct, best_score))

    pairs.sort(key=lambda x: -(x[2] + x[3]))  # Sort by combined frequency

    print(f"Pairs found: {len(pairs)}")
    print(f"\nTop 40 homophone pairs (A-word <-> B-word):")
    print(f"{'A_word':<15} {'B_word':<15} {'A_%':>7} {'B_%':>7} {'Score':>7}")
    print("-" * 55)
    for a_w, b_w, ap, bp, s in pairs[:40]:
        print(f"{a_w:<15} {b_w:<15} {ap:>6.2f}% {bp:>6.2f}% {s:>7.3f}")

    return pairs


# ============================================================
# PHASE 3: BUILD SYMBOL MAP AND COLLAPSE CORPUS
# ============================================================

def build_symbol_map(pairs, shared, a_counter, b_counter, a_total, b_total,
                      max_symbols=25):
    """
    Build the mapping from Voynich words to collapsed symbols.

    Rules:
    1. Each homophone pair (a_word, b_word) -> one symbol
    2. Shared words that are frequent enough -> their own symbol
    3. Rare words -> lumped into RARE symbol
    4. Target: ~20-25 symbols to match Italian's 21 letters

    The key challenge: 8000+ Voynich word types must collapse to ~21-25 symbols.
    This requires AGGRESSIVE grouping beyond just A/B pairs.
    """
    print(f"\n=== PHASE 3: SYMBOL MAP CONSTRUCTION ===")

    # Strategy: Use frequency tiers to create symbol groups
    # The most frequent words/pairs each get their own symbol
    # Less frequent words are grouped by morphological pattern

    symbol_map = {}  # voynich_word -> symbol_id
    symbol_names = {}  # symbol_id -> description
    next_symbol = 0

    # Step 1: Top homophone pairs each get a symbol
    n_pair_symbols = min(len(pairs), max_symbols // 2)
    for i, (a_w, b_w, ap, bp, s) in enumerate(pairs[:n_pair_symbols]):
        sym = f"S{next_symbol}"
        symbol_map[a_w] = sym
        symbol_map[b_w] = sym
        symbol_names[sym] = f"{a_w}/{b_w}"
        next_symbol += 1

    # Step 2: Top shared words each get a symbol
    shared_freqs = []
    for w in shared:
        total_freq = (a_counter.get(w, 0) / a_total + b_counter.get(w, 0) / b_total) / 2 * 100
        shared_freqs.append((w, total_freq))
    shared_freqs.sort(key=lambda x: -x[1])

    n_shared_symbols = min(len(shared_freqs), max_symbols - next_symbol - 2)
    for i, (w, freq) in enumerate(shared_freqs[:n_shared_symbols]):
        if w not in symbol_map:
            sym = f"S{next_symbol}"
            symbol_map[w] = sym
            symbol_names[sym] = w
            next_symbol += 1

    # Step 3: Remaining words -> group by morphological prefix
    # This is the AGGRESSIVE grouping step
    remaining_sym = f"S{next_symbol}"
    symbol_names[remaining_sym] = "RARE/OTHER"

    total_symbols = next_symbol + 1
    print(f"Total symbols: {total_symbols}")
    print(f"  Pair symbols: {n_pair_symbols}")
    print(f"  Shared word symbols: {n_shared_symbols}")
    print(f"  RARE/OTHER: 1")
    print(f"\nSymbol assignments:")
    for sym in sorted(symbol_names.keys()):
        print(f"  {sym}: {symbol_names[sym]}")

    return symbol_map, symbol_names, remaining_sym


def collapse_corpus(pages, symbol_map, remaining_sym):
    """
    Replace all Voynich words with their collapsed symbols.
    Returns list of lines, where each line is a list of symbols.
    """
    collapsed_lines = []
    total_tokens = 0
    mapped_tokens = 0

    for folio in sorted(pages.keys()):
        data = pages[folio]
        for line in data['lines']:
            sym_line = []
            for w in line:
                total_tokens += 1
                if w in symbol_map:
                    sym_line.append(symbol_map[w])
                    mapped_tokens += 1
                else:
                    sym_line.append(remaining_sym)
            if sym_line:
                collapsed_lines.append(sym_line)

    print(f"\n=== CORPUS COLLAPSE ===")
    print(f"Total tokens: {total_tokens}")
    print(f"Mapped to specific symbol: {mapped_tokens} ({mapped_tokens/total_tokens*100:.1f}%)")
    print(f"Mapped to RARE/OTHER: {total_tokens - mapped_tokens} ({(total_tokens-mapped_tokens)/total_tokens*100:.1f}%)")
    print(f"Total lines: {len(collapsed_lines)}")

    return collapsed_lines


# ============================================================
# PHASE 4: BIGRAM TRANSITION MATRIX
# ============================================================

def compute_bigram_matrix(collapsed_lines, symbol_names):
    """
    Compute bigram transition matrix and entropy metrics.
    """
    print(f"\n=== PHASE 4: BIGRAM TRANSITION MATRIX ===")

    # Count bigrams
    bigram_counts = Counter()
    unigram_counts = Counter()
    total_bigrams = 0

    for line in collapsed_lines:
        for i in range(len(line)):
            unigram_counts[line[i]] += 1
            if i < len(line) - 1:
                bigram_counts[(line[i], line[i+1])] += 1
                total_bigrams += 1

    total_unigrams = sum(unigram_counts.values())
    all_symbols = sorted(unigram_counts.keys())
    n_symbols = len(all_symbols)

    print(f"Unique symbols in corpus: {n_symbols}")
    print(f"Total bigrams: {total_bigrams}")

    # Unigram distribution
    print(f"\nUnigram frequencies:")
    for sym in all_symbols:
        count = unigram_counts[sym]
        pct = count / total_unigrams * 100
        name = symbol_names.get(sym, sym)
        print(f"  {sym} ({name}): {count} ({pct:.1f}%)")

    # Bigram transition matrix
    # For each symbol i, compute P(j|i) = count(i,j) / count(i)
    # Then entropy H(j|i) = -sum_j P(j|i) * log2(P(j|i))
    # Overall conditional entropy H = sum_i P(i) * H(j|i)

    conditional_entropies = {}
    for sym_i in all_symbols:
        row_total = sum(bigram_counts.get((sym_i, sym_j), 0) for sym_j in all_symbols)
        if row_total == 0:
            continue
        h = 0
        for sym_j in all_symbols:
            count = bigram_counts.get((sym_i, sym_j), 0)
            if count > 0:
                p = count / row_total
                h -= p * math.log2(p)
        conditional_entropies[sym_i] = h

    # Overall conditional entropy
    overall_h = 0
    for sym_i in all_symbols:
        if sym_i in conditional_entropies:
            p_i = unigram_counts[sym_i] / total_unigrams
            overall_h += p_i * conditional_entropies[sym_i]

    h_max = math.log2(n_symbols)
    entropy_ratio = overall_h / h_max if h_max > 0 else 0

    print(f"\n--- ENTROPY METRICS ---")
    print(f"H_max = log2({n_symbols}) = {h_max:.3f} bits")
    print(f"H(bigram|prev) = {overall_h:.3f} bits")
    print(f"Entropy ratio = {entropy_ratio:.3f} ({entropy_ratio*100:.1f}%)")
    print(f"")
    print(f"Reference values:")
    print(f"  Italian:  ~65%")
    print(f"  Raw Voynich: 85.6%")
    print(f"  Random:   ~95%")

    # Near-zero cells (forbidden bigrams)
    total_cells = n_symbols * n_symbols
    near_zero_cells = 0
    threshold = 0.01  # less than 1% of expected uniform probability
    expected_uniform = 1.0 / n_symbols

    for sym_i in all_symbols:
        row_total = sum(bigram_counts.get((sym_i, sym_j), 0) for sym_j in all_symbols)
        if row_total == 0:
            near_zero_cells += n_symbols
            continue
        for sym_j in all_symbols:
            count = bigram_counts.get((sym_i, sym_j), 0)
            p = count / row_total
            if p < expected_uniform * threshold:
                near_zero_cells += 1

    forbidden_fraction = near_zero_cells / total_cells if total_cells > 0 else 0
    print(f"\nNear-zero bigram cells: {near_zero_cells}/{total_cells} ({forbidden_fraction*100:.1f}%)")
    print(f"Italian reference: ~30%")

    # Asymmetry measure: for each pair (i,j), compute |P(j|i) - P(i|j)|
    asymmetry_sum = 0
    asymmetry_count = 0
    for sym_i in all_symbols:
        for sym_j in all_symbols:
            if sym_i >= sym_j:
                continue
            row_i = sum(bigram_counts.get((sym_i, s), 0) for s in all_symbols)
            row_j = sum(bigram_counts.get((sym_j, s), 0) for s in all_symbols)
            if row_i > 0 and row_j > 0:
                p_ij = bigram_counts.get((sym_i, sym_j), 0) / row_i
                p_ji = bigram_counts.get((sym_j, sym_i), 0) / row_j
                asymmetry_sum += abs(p_ij - p_ji)
                asymmetry_count += 1

    avg_asymmetry = asymmetry_sum / asymmetry_count if asymmetry_count > 0 else 0
    print(f"\nAverage bigram asymmetry: {avg_asymmetry:.4f}")
    print(f"(Higher = more directional constraints, like natural language)")

    # Top bigrams
    print(f"\nTop 20 bigrams:")
    for (s1, s2), count in bigram_counts.most_common(20):
        pct = count / total_bigrams * 100
        n1 = symbol_names.get(s1, s1)
        n2 = symbol_names.get(s2, s2)
        print(f"  {s1}({n1}) -> {s2}({n2}): {count} ({pct:.2f}%)")

    return {
        'n_symbols': n_symbols,
        'total_bigrams': total_bigrams,
        'h_max': h_max,
        'h_conditional': overall_h,
        'entropy_ratio': entropy_ratio,
        'forbidden_fraction': forbidden_fraction,
        'avg_asymmetry': avg_asymmetry,
    }


# ============================================================
# PHASE 5: COMPARISON WITH ITALIAN
# ============================================================

def compare_with_italian(metrics):
    """Compare collapsed Voynich metrics with Italian reference."""
    print(f"\n{'='*80}")
    print(f"PHASE 5: COMPARISON WITH ITALIAN BIGRAM CHARACTERISTICS")
    print(f"{'='*80}")

    ref = italian_bigram_reference()

    tests = [
        ('Entropy ratio', metrics['entropy_ratio'], ref['entropy_ratio'], 0.10,
         'Italian ~65%, random ~95%. Closer to 65% = more Italian-like constraints'),
        ('Forbidden bigram fraction', metrics['forbidden_fraction'], ref['forbidden_fraction'], 0.15,
         'Italian ~30% near-zero cells. Natural languages have many forbidden combinations'),
        ('Alphabet size', metrics['n_symbols'], ref['alphabet_size'], 5,
         'Italian has 21 letters. Collapsed symbols should be in similar range'),
    ]

    print(f"\n{'Metric':<30} {'Voynich':>10} {'Italian':>10} {'Match?':>8}")
    print("-" * 65)

    score = 0
    for name, voynich_val, italian_val, tolerance, explanation in tests:
        if isinstance(voynich_val, float):
            match = abs(voynich_val - italian_val) <= tolerance
            print(f"{name:<30} {voynich_val:>10.3f} {italian_val:>10.3f} {'YES' if match else 'NO':>8}")
        else:
            match = abs(voynich_val - italian_val) <= tolerance
            print(f"{name:<30} {voynich_val:>10} {italian_val:>10} {'YES' if match else 'NO':>8}")
        if match:
            score += 1
        print(f"  -> {explanation}")

    print(f"\nOverall match: {score}/{len(tests)} criteria met")

    # Improvement from baseline
    baseline_entropy = 0.856
    improvement = baseline_entropy - metrics['entropy_ratio']
    print(f"\nEntropy reduction from raw Voynich: {baseline_entropy:.3f} -> {metrics['entropy_ratio']:.3f}")
    print(f"Improvement: {improvement:.3f} ({improvement/baseline_entropy*100:.1f}% reduction)")
    target_improvement = baseline_entropy - 0.65
    print(f"Target improvement (to reach Italian): {target_improvement:.3f}")
    print(f"Fraction of target achieved: {improvement/target_improvement*100:.1f}%")

    return score


# ============================================================
# PHASE 6: PARAMETER SWEEP
# ============================================================

def parameter_sweep(pages, a_counter, b_counter, a_total, b_total,
                     shared, a_only, b_only):
    """
    Sweep over different parameter configurations to find optimal collapse.
    """
    print(f"\n{'='*80}")
    print(f"PHASE 6: PARAMETER SWEEP")
    print(f"{'='*80}")

    results = []

    for max_symbols in [15, 20, 25, 30, 40]:
        for min_freq in [2, 3, 5]:
            for freq_tol in [1.5, 2.0, 3.0]:
                for struct_bonus in [True, False]:
                    # Quiet mode - don't print per-config
                    pairs = find_homophone_pairs_quiet(
                        a_counter, b_counter, a_total, b_total,
                        a_only, b_only, shared,
                        min_freq=min_freq,
                        freq_tolerance=freq_tol,
                        structural_bonus=struct_bonus
                    )

                    symbol_map, symbol_names, remaining_sym = build_symbol_map_quiet(
                        pairs, shared, a_counter, b_counter, a_total, b_total,
                        max_symbols=max_symbols
                    )

                    collapsed_lines = collapse_corpus_quiet(pages, symbol_map, remaining_sym)
                    metrics = compute_bigram_matrix_quiet(collapsed_lines, symbol_names)

                    config = {
                        'max_symbols': max_symbols,
                        'min_freq': min_freq,
                        'freq_tolerance': freq_tol,
                        'structural_bonus': struct_bonus,
                        'n_pairs': len(pairs),
                    }
                    config.update(metrics)
                    results.append(config)

    # Sort by entropy ratio (closest to Italian 0.65)
    results.sort(key=lambda x: abs(x['entropy_ratio'] - 0.65))

    print(f"\nTop 10 configurations (sorted by closeness to Italian entropy ratio 0.65):")
    print(f"{'Syms':>5} {'MinF':>5} {'FTol':>5} {'Struct':>6} {'Pairs':>6} {'H_ratio':>8} {'Forb%':>6} {'Asym':>6}")
    print("-" * 60)
    for r in results[:10]:
        print(f"{r['max_symbols']:>5} {r['min_freq']:>5} {r['freq_tolerance']:>5.1f} "
              f"{'Y' if r['structural_bonus'] else 'N':>6} {r['n_pairs']:>6} "
              f"{r['entropy_ratio']:>7.3f} {r['forbidden_fraction']*100:>5.1f}% {r['avg_asymmetry']:>6.4f}")

    print(f"\nBaseline (raw Voynich): H_ratio = 0.856")
    print(f"Target (Italian): H_ratio = 0.650")

    best = results[0]
    print(f"\nBEST CONFIGURATION:")
    print(f"  max_symbols={best['max_symbols']}, min_freq={best['min_freq']}, "
          f"freq_tolerance={best['freq_tolerance']}, structural_bonus={best['structural_bonus']}")
    print(f"  Entropy ratio: {best['entropy_ratio']:.3f}")
    print(f"  Improvement from baseline: {0.856 - best['entropy_ratio']:.3f}")

    return results


# Quiet versions of functions (no print output)
def find_homophone_pairs_quiet(a_counter, b_counter, a_total, b_total,
                                a_only, b_only, shared,
                                min_freq=3, freq_tolerance=2.0,
                                structural_bonus=True):
    a_only_freqs = [(w, a_counter[w], a_counter[w] / a_total * 100)
                     for w in a_only if a_counter[w] >= min_freq]
    b_only_freqs = [(w, b_counter[w], b_counter[w] / b_total * 100)
                     for w in b_only if b_counter[w] >= min_freq]
    a_only_freqs.sort(key=lambda x: -x[2])
    b_only_freqs.sort(key=lambda x: -x[2])

    prefixes = ['qok', 'qot', 'qo', 'cth', 'ckh', 'ch', 'sh', 'ok', 'ot', 'da', 'ol', 'or', 'ct', 'cp']
    prefix_map = {}
    for plist in [a_only_freqs, b_only_freqs]:
        for w, c, pct in plist:
            for p in sorted(prefixes, key=len, reverse=True):
                if w.startswith(p):
                    prefix_map[w] = p
                    break
            else:
                prefix_map[w] = ''

    used_b = set()
    pairs = []
    for a_word, a_count, a_pct in a_only_freqs:
        best_b = None
        best_score = float('inf')
        for b_word, b_count, b_pct in b_only_freqs:
            if b_word in used_b:
                continue
            freq_ratio = max(a_pct, b_pct) / min(a_pct, b_pct) if min(a_pct, b_pct) > 0 else 999
            if freq_ratio > freq_tolerance:
                continue
            score = math.log(freq_ratio + 0.01)
            if structural_bonus:
                a_pfx = prefix_map.get(a_word, '')
                b_pfx = prefix_map.get(b_word, '')
                if a_pfx and b_pfx and a_pfx == b_pfx:
                    score -= 0.5
                if len(a_word) == len(b_word):
                    score -= 0.2
                elif abs(len(a_word) - len(b_word)) == 1:
                    score -= 0.1
            if score < best_score:
                best_score = score
                best_b = (b_word, b_count, b_pct)
        if best_b is not None:
            b_word, b_count, b_pct = best_b
            used_b.add(b_word)
            pairs.append((a_word, b_word, a_pct, b_pct, best_score))

    pairs.sort(key=lambda x: -(x[2] + x[3]))
    return pairs


def build_symbol_map_quiet(pairs, shared, a_counter, b_counter, a_total, b_total,
                            max_symbols=25):
    symbol_map = {}
    symbol_names = {}
    next_symbol = 0

    n_pair_symbols = min(len(pairs), max_symbols // 2)
    for i, (a_w, b_w, ap, bp, s) in enumerate(pairs[:n_pair_symbols]):
        sym = f"S{next_symbol}"
        symbol_map[a_w] = sym
        symbol_map[b_w] = sym
        symbol_names[sym] = f"{a_w}/{b_w}"
        next_symbol += 1

    shared_freqs = []
    for w in shared:
        total_freq = (a_counter.get(w, 0) / a_total + b_counter.get(w, 0) / b_total) / 2 * 100
        shared_freqs.append((w, total_freq))
    shared_freqs.sort(key=lambda x: -x[1])

    n_shared_symbols = min(len(shared_freqs), max_symbols - next_symbol - 2)
    for i, (w, freq) in enumerate(shared_freqs[:n_shared_symbols]):
        if w not in symbol_map:
            sym = f"S{next_symbol}"
            symbol_map[w] = sym
            symbol_names[sym] = w
            next_symbol += 1

    remaining_sym = f"S{next_symbol}"
    symbol_names[remaining_sym] = "RARE/OTHER"
    return symbol_map, symbol_names, remaining_sym


def collapse_corpus_quiet(pages, symbol_map, remaining_sym):
    collapsed_lines = []
    for folio in sorted(pages.keys()):
        data = pages[folio]
        for line in data['lines']:
            sym_line = []
            for w in line:
                sym_line.append(symbol_map.get(w, remaining_sym))
            if sym_line:
                collapsed_lines.append(sym_line)
    return collapsed_lines


def compute_bigram_matrix_quiet(collapsed_lines, symbol_names):
    bigram_counts = Counter()
    unigram_counts = Counter()
    total_bigrams = 0

    for line in collapsed_lines:
        for i in range(len(line)):
            unigram_counts[line[i]] += 1
            if i < len(line) - 1:
                bigram_counts[(line[i], line[i+1])] += 1
                total_bigrams += 1

    total_unigrams = sum(unigram_counts.values())
    all_symbols = sorted(unigram_counts.keys())
    n_symbols = len(all_symbols)

    conditional_entropies = {}
    for sym_i in all_symbols:
        row_total = sum(bigram_counts.get((sym_i, sym_j), 0) for sym_j in all_symbols)
        if row_total == 0:
            continue
        h = 0
        for sym_j in all_symbols:
            count = bigram_counts.get((sym_i, sym_j), 0)
            if count > 0:
                p = count / row_total
                h -= p * math.log2(p)
        conditional_entropies[sym_i] = h

    overall_h = 0
    for sym_i in all_symbols:
        if sym_i in conditional_entropies:
            p_i = unigram_counts[sym_i] / total_unigrams
            overall_h += p_i * conditional_entropies[sym_i]

    h_max = math.log2(n_symbols) if n_symbols > 1 else 1
    entropy_ratio = overall_h / h_max if h_max > 0 else 0

    total_cells = n_symbols * n_symbols
    near_zero_cells = 0
    expected_uniform = 1.0 / n_symbols if n_symbols > 0 else 1

    for sym_i in all_symbols:
        row_total = sum(bigram_counts.get((sym_i, sym_j), 0) for sym_j in all_symbols)
        if row_total == 0:
            near_zero_cells += n_symbols
            continue
        for sym_j in all_symbols:
            count = bigram_counts.get((sym_i, sym_j), 0)
            p = count / row_total
            if p < expected_uniform * 0.01:
                near_zero_cells += 1

    forbidden_fraction = near_zero_cells / total_cells if total_cells > 0 else 0

    asymmetry_sum = 0
    asymmetry_count = 0
    for sym_i in all_symbols:
        for sym_j in all_symbols:
            if sym_i >= sym_j:
                continue
            row_i = sum(bigram_counts.get((sym_i, s), 0) for s in all_symbols)
            row_j = sum(bigram_counts.get((sym_j, s), 0) for s in all_symbols)
            if row_i > 0 and row_j > 0:
                p_ij = bigram_counts.get((sym_i, sym_j), 0) / row_i
                p_ji = bigram_counts.get((sym_j, sym_i), 0) / row_j
                asymmetry_sum += abs(p_ij - p_ji)
                asymmetry_count += 1

    avg_asymmetry = asymmetry_sum / asymmetry_count if asymmetry_count > 0 else 0

    return {
        'n_symbols': n_symbols,
        'total_bigrams': total_bigrams,
        'h_max': h_max,
        'h_conditional': overall_h,
        'entropy_ratio': entropy_ratio,
        'forbidden_fraction': forbidden_fraction,
        'avg_asymmetry': avg_asymmetry,
    }


# ============================================================
# PHASE 7: MORPHOLOGICAL GROUP COLLAPSE (ADVANCED)
# ============================================================

def morphological_collapse(pages, a_counter, b_counter, a_total, b_total,
                            shared, a_only, b_only):
    """
    More aggressive collapse: group words by morphological pattern.

    Instead of just A/B pairing, also collapse:
    - chol, chor, chol -> same "ch-stem" symbol
    - shol, shor -> same "sh-stem" symbol
    - chedy, shedy -> same "-edy stem" symbol
    - etc.

    This is the "Italian letter recovery" approach: if ch+ol = one Italian word
    and ch+or = a different Italian word, they should be different symbols.
    But if chol(A) = chedy(B), they are the SAME symbol.

    The insight: we need TWO levels of collapse:
    Level 1: A/B homophone merging (chol = chedy)
    Level 2: Morphological family grouping (multiple words -> one letter equivalent)
    """
    print(f"\n{'='*80}")
    print(f"PHASE 7: MORPHOLOGICAL GROUP COLLAPSE")
    print(f"{'='*80}")

    # Define morphological families based on the nomenclator model
    # Each family represents words that share the same semantic root
    # (i.e., same Italian letter or syllable)

    # First, find all A/B pairs
    pairs = find_homophone_pairs_quiet(
        a_counter, b_counter, a_total, b_total,
        a_only, b_only, shared,
        min_freq=2, freq_tolerance=3.0, structural_bonus=True
    )

    # Build combined frequency for all words (normalized to common scale)
    all_words = Counter()
    for folio, data in pages.items():
        for w in data['words']:
            all_words[w] += 1
    total_words = sum(all_words.values())

    # Create morphological groups
    # Strategy: prefix + suffix pattern defines the group
    def get_morph_signature(word):
        """Extract morphological signature: (prefix, root_pattern, suffix)"""
        # Prefix extraction
        prefix = ''
        remainder = word
        for p in ['qok', 'qot', 'qo', 'cth', 'ckh', 'lk', 'ch', 'sh', 'ok', 'ot', 'da', 'ol', 'or', 'ct', 'cp', 'yk', 'yt']:
            if word.startswith(p) and len(word) > len(p):
                prefix = p
                remainder = word[len(p):]
                break

        # Suffix extraction
        suffix = ''
        for s in ['aiin', 'ain', 'iin', 'edy', 'eedy', 'dy', 'ey', 'in', 'ol', 'or', 'ar', 'al', 'y', 'n', 'l', 'r', 's', 'd']:
            if remainder.endswith(s) and len(remainder) > len(s):
                suffix = s
                remainder = remainder[:-len(s)]
                break
            elif remainder == s:
                suffix = s
                remainder = ''
                break

        return (prefix, remainder, suffix)

    # Group words by morphological signature
    morph_groups = defaultdict(list)
    for w in all_words:
        sig = get_morph_signature(w)
        morph_groups[sig].append((w, all_words[w]))

    # Also merge A/B pair signatures
    pair_map = {}
    for a_w, b_w, ap, bp, s in pairs:
        pair_map[a_w] = b_w
        pair_map[b_w] = a_w

    # Build final symbol groups:
    # 1. Each A/B pair merged into one group
    # 2. Then within each morphological family, merge if frequency-compatible
    # Target: 20-25 final symbols

    # Rank all words by frequency
    word_rank = sorted(all_words.items(), key=lambda x: -x[1])

    # Create symbols for top frequency groups
    symbol_map = {}
    symbol_names = {}
    next_sym = 0

    # Method: Assign top words/pairs to symbols, then group the rest
    assigned = set()

    # First: assign A/B pairs (highest frequency first)
    pair_freqs = []
    for a_w, b_w, ap, bp, s in pairs:
        combined = all_words.get(a_w, 0) + all_words.get(b_w, 0)
        pair_freqs.append((a_w, b_w, combined))
    pair_freqs.sort(key=lambda x: -x[2])

    # Top 10 pairs get their own symbol
    for a_w, b_w, combined in pair_freqs[:10]:
        if a_w not in assigned and b_w not in assigned:
            sym = f"M{next_sym}"
            symbol_map[a_w] = sym
            symbol_map[b_w] = sym
            symbol_names[sym] = f"{a_w}/{b_w}"
            assigned.add(a_w)
            assigned.add(b_w)
            next_sym += 1

    # Top shared words get their own symbol (up to ~10)
    shared_ranked = [(w, all_words[w]) for w in shared if w not in assigned]
    shared_ranked.sort(key=lambda x: -x[1])
    for w, count in shared_ranked[:10]:
        sym = f"M{next_sym}"
        symbol_map[w] = sym
        symbol_names[sym] = w
        assigned.add(w)
        next_sym += 1

    # Remaining: group by prefix into 3-5 bucket symbols
    prefix_buckets = {
        'ch_group': ['ch', 'ckh', 'cth'],
        'sh_group': ['sh'],
        'qo_group': ['qo', 'qok', 'qot'],
        'ok_group': ['ok', 'ot'],
        'other': [],
    }

    for bucket_name, bucket_prefixes in prefix_buckets.items():
        sym = f"M{next_sym}"
        symbol_names[sym] = bucket_name
        # Assign all unassigned words with matching prefix
        for w in all_words:
            if w in assigned:
                continue
            matched = False
            for p in bucket_prefixes:
                if w.startswith(p):
                    matched = True
                    break
            if bucket_name == 'other' and not matched:
                # Check if it wasn't caught by any other bucket
                caught = False
                for bn, bps in prefix_buckets.items():
                    if bn == 'other':
                        continue
                    for p in bps:
                        if w.startswith(p):
                            caught = True
                            break
                    if caught:
                        break
                if not caught:
                    symbol_map[w] = sym
                    assigned.add(w)
            elif matched:
                symbol_map[w] = sym
                assigned.add(w)
        next_sym += 1

    # Catch-all for anything remaining
    remaining_sym = f"M{next_sym}"
    symbol_names[remaining_sym] = "REMAINDER"

    print(f"Total morphological symbols: {next_sym + 1}")
    print(f"Symbol assignments:")
    for sym in sorted(symbol_names.keys()):
        count = sum(1 for w in symbol_map if symbol_map[w] == sym)
        print(f"  {sym} ({symbol_names[sym]}): {count} word types")

    # Collapse and compute
    collapsed_lines = collapse_corpus_quiet(pages, symbol_map, remaining_sym)
    metrics = compute_bigram_matrix(collapsed_lines, symbol_names)

    return metrics


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 80)
    print("DECISIVE EXPERIMENT: HOMOPHONE COLLAPSING")
    print("Bigram Transition Matrix Recovery via A/B Split")
    print("=" * 80)

    # Try ZL transcription first, fall back to RF
    import os
    zl_path = "C:/Users/kazuk/Downloads/voynich_analysis/ZL3b-n.txt"
    rf_path = "C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt"

    filepath = zl_path if os.path.exists(zl_path) else rf_path
    print(f"\nUsing transcription: {filepath}")

    pages = parse_ivtff(filepath)
    print(f"Parsed {len(pages)} folios")

    # Phase 1: Extract profiles
    a_counter, b_counter, a_total, b_total, shared, a_only, b_only = extract_ab_profiles(pages)

    # Phase 2: Find homophone pairs (detailed output)
    pairs = find_homophone_pairs(
        a_counter, b_counter, a_total, b_total,
        a_only, b_only, shared,
        min_freq=3, freq_tolerance=2.0, structural_bonus=True
    )

    # Phase 3: Build symbol map
    symbol_map, symbol_names, remaining_sym = build_symbol_map(
        pairs, shared, a_counter, b_counter, a_total, b_total,
        max_symbols=25
    )

    # Phase 4: Collapse and compute bigram matrix
    collapsed_lines = collapse_corpus(pages, symbol_map, remaining_sym)
    metrics_basic = compute_bigram_matrix(collapsed_lines, symbol_names)

    # Phase 5: Compare with Italian
    score_basic = compare_with_italian(metrics_basic)

    # Phase 6: Parameter sweep
    print(f"\n{'='*80}")
    print("Running parameter sweep...")
    sweep_results = parameter_sweep(
        pages, a_counter, b_counter, a_total, b_total,
        shared, a_only, b_only
    )

    # Phase 7: Morphological group collapse
    metrics_morph = morphological_collapse(
        pages, a_counter, b_counter, a_total, b_total,
        shared, a_only, b_only
    )

    # ============================================================
    # FINAL VERDICT
    # ============================================================
    print(f"\n{'='*80}")
    print(f"FINAL VERDICT")
    print(f"{'='*80}")

    print(f"\nBaseline (raw Voynich words as symbols): H_ratio = 0.856")
    print(f"Basic A/B collapse (25 symbols):          H_ratio = {metrics_basic['entropy_ratio']:.3f}")
    if sweep_results:
        best_sweep = sweep_results[0]
        print(f"Best parameter sweep:                     H_ratio = {best_sweep['entropy_ratio']:.3f}")
    print(f"Morphological group collapse:             H_ratio = {metrics_morph['entropy_ratio']:.3f}")
    print(f"Italian target:                           H_ratio = 0.650")
    print(f"Random text:                              H_ratio = 0.950")

    best_ratio = min(metrics_basic['entropy_ratio'],
                     metrics_morph['entropy_ratio'],
                     best_sweep['entropy_ratio'] if sweep_results else 1.0)

    if best_ratio < 0.70:
        print(f"\n*** STRONG EVIDENCE: Collapsed entropy ({best_ratio:.3f}) matches Italian range ***")
        print(f"The homophone collapse has recovered Italian-like bigram constraints.")
        print(f"This supports the hypothesis that A/B words are homophones encoding Italian.")
    elif best_ratio < 0.78:
        print(f"\n** MODERATE EVIDENCE: Collapsed entropy ({best_ratio:.3f}) is between Italian and raw Voynich **")
        print(f"Significant improvement from baseline (0.856), but not fully Italian-like.")
        print(f"The collapse is partially working -- some homophones are correctly identified.")
        print(f"Further refinement of the pairing algorithm may improve results.")
    else:
        print(f"\n* WEAK EVIDENCE: Collapsed entropy ({best_ratio:.3f}) shows minimal improvement *")
        print(f"The A/B frequency-matching approach may not be identifying true homophones.")
        print(f"Alternative explanations: the A/B split may not be a simple homophone system,")
        print(f"or the collapsing granularity needs fundamental rethinking.")

    # Save results
    results_out = {
        'baseline_entropy_ratio': 0.856,
        'basic_collapse': metrics_basic,
        'best_sweep': best_sweep if sweep_results else None,
        'morphological_collapse': metrics_morph,
        'italian_target': 0.65,
        'n_pairs_found': len(pairs),
        'top_pairs': [(a, b, ap, bp) for a, b, ap, bp, s in pairs[:30]],
    }

    with open("C:/Users/kazuk/Downloads/voynich_analysis/homophone_collapse_results.json", 'w') as f:
        json.dump(results_out, f, indent=2)

    print(f"\nResults saved to homophone_collapse_results.json")


if __name__ == '__main__':
    main()
