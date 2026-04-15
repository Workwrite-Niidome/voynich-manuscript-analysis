#!/usr/bin/env python3
"""
Voynich Manuscript: Homophone Collapse Language Identification
Analyze distributional similarity of EVA characters and test collapse mappings.
"""

import re
import math
import json
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(r"C:\Users\kazuk\Downloads\voynich_analysis")

###############################################################################
# 1. Parse EVA transcription
###############################################################################

def parse_eva(filepath):
    """Extract words from EVA transcription, stripping metadata."""
    words = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            # Skip page/section headers
            if line.startswith('<') and '>' in line and not any(c.isalpha() and c.islower() for c in line.split('>')[-1][:5]):
                # header-only lines
                parts = line.split('>')
                if len(parts) > 1:
                    text = parts[-1].strip()
                else:
                    continue
            else:
                # Lines like <f1r.1,@P0>  text
                m = re.match(r'<[^>]+>\s*(.*)', line)
                if m:
                    text = m.group(1)
                else:
                    continue

            if not text:
                continue

            # Remove comments {}, @-codes, ?, !, *, etc.
            text = re.sub(r'\{[^}]*\}', '', text)  # remove {cto} etc
            text = re.sub(r'@\d+;?', '', text)      # remove @221; etc
            text = re.sub(r'[<>]', '', text)         # remove < >
            text = re.sub(r"['\",!?\*]", '', text)   # remove punctuation

            # Split on dots and hyphens (word separators in EVA)
            tokens = re.split(r'[.\-\s]+', text)
            for t in tokens:
                t = t.strip()
                if t and re.match(r'^[a-z]+$', t):
                    words.append(t)
    return words


###############################################################################
# 2. Character-level analysis
###############################################################################

def char_frequency(words):
    """Compute character frequencies."""
    counter = Counter()
    total = 0
    for w in words:
        for c in w:
            counter[c] += 1
            total += 1
    return counter, total


def bigram_contexts(words):
    """For each character, compute left-context and right-context distributions."""
    left_ctx = defaultdict(Counter)   # what appears before char
    right_ctx = defaultdict(Counter)  # what appears after char

    for w in words:
        padded = '^' + w + '$'  # start/end markers
        for i in range(1, len(padded) - 1):
            c = padded[i]
            left_ctx[c][padded[i-1]] += 1
            right_ctx[c][padded[i+1]] += 1

    return left_ctx, right_ctx


def context_similarity(ctx1, ctx2):
    """Cosine similarity between two context distributions."""
    all_keys = set(ctx1.keys()) | set(ctx2.keys())
    if not all_keys:
        return 0.0

    dot = sum(ctx1.get(k, 0) * ctx2.get(k, 0) for k in all_keys)
    mag1 = math.sqrt(sum(v*v for v in ctx1.values()))
    mag2 = math.sqrt(sum(v*v for v in ctx2.values()))

    if mag1 == 0 or mag2 == 0:
        return 0.0
    return dot / (mag1 * mag2)


def find_homophones(words, min_freq=50):
    """Find character pairs with high distributional similarity."""
    left_ctx, right_ctx = bigram_contexts(words)
    freq, _ = char_frequency(words)

    # Only consider characters with sufficient frequency
    chars = [c for c, f in freq.items() if f >= min_freq]
    chars.sort()

    pairs = []
    for i in range(len(chars)):
        for j in range(i+1, len(chars)):
            c1, c2 = chars[i], chars[j]
            left_sim = context_similarity(left_ctx[c1], left_ctx[c2])
            right_sim = context_similarity(right_ctx[c1], right_ctx[c2])
            combined = (left_sim + right_sim) / 2
            pairs.append((c1, c2, left_sim, right_sim, combined, freq[c1], freq[c2]))

    pairs.sort(key=lambda x: -x[4])
    return pairs


###############################################################################
# 3. Multi-character token analysis (EVA digraphs)
###############################################################################

def tokenize_eva(word):
    """Tokenize EVA word into multi-character tokens.
    EVA uses digraphs like 'ch', 'sh', 'ii', 'ee', 'ai', 'ck', etc.
    """
    tokens = []
    i = 0
    while i < len(word):
        # Try trigraphs first
        if i + 2 < len(word):
            tri = word[i:i+3]
            if tri in ('iii', 'iin', 'eee', 'ees', 'eed', 'eel'):
                # Handle iii as ii + i, iin as ii + n, etc.
                pass  # fall through to digraphs

        # Digraphs
        if i + 1 < len(word):
            di = word[i:i+2]
            if di in ('ch', 'sh', 'ck', 'ph', 'cf', 'ct', 'ii', 'ee',
                       'ai', 'ei', 'oi', 'cp', 'qo', 'ot', 'ol', 'or',
                       'ar', 'an', 'in', 'dy', 'ky', 'ty', 'sy', 'ry',
                       'th', 'fh'):
                tokens.append(di)
                i += 2
                continue

        tokens.append(word[i])
        i += 1
    return tokens


###############################################################################
# 4. Collapse mappings
###############################################################################

def apply_collapse(words, mapping):
    """Apply a character-level collapse mapping to words.
    mapping is a dict: old_substring -> new_substring
    Applied in order of decreasing key length.
    """
    collapsed = []
    sorted_keys = sorted(mapping.keys(), key=len, reverse=True)

    for w in words:
        new_w = w
        for old in sorted_keys:
            new_w = new_w.replace(old, mapping[old])
        if new_w:
            collapsed.append(new_w)
    return collapsed


COLLAPSE_MAPPINGS = {
    'minimal': {
        'ii': 'i',
        'ee': 'e',
        'iii': 'i',
        'eee': 'e',
        'iiii': 'i',
    },
    'moderate': {
        'ii': 'i',
        'ee': 'e',
        'iii': 'i',
        'eee': 'e',
        'iiii': 'i',
        'sh': 'ch',
        'f': 'p',
    },
    'aggressive': {
        'ii': 'i',
        'ee': 'e',
        'iii': 'i',
        'eee': 'e',
        'iiii': 'i',
        'sh': 'ch',
        'f': 'p',
        'q': 'k',
        'y': 'i',
    },
    'very_aggressive': {
        'ii': 'i',
        'ee': 'e',
        'iii': 'i',
        'eee': 'e',
        'iiii': 'i',
        'sh': 'ch',
        'f': 'p',
        'q': 'k',
        'y': 'i',
        'ck': 'k',
        'ph': 'p',
        'ct': 't',
        'd': 't',
    },
}


###############################################################################
# 5. Language comparison data
###############################################################################

# Character frequencies for comparison languages (approximate, from large corpora)
LANG_CHAR_FREQ = {
    'Latin': {'e': 11.0, 'i': 10.5, 'a': 8.5, 'u': 8.0, 't': 7.5, 's': 7.0,
              'n': 6.5, 'r': 6.0, 'o': 5.5, 'c': 4.5, 'm': 4.0, 'l': 3.5,
              'd': 3.5, 'p': 3.0, 'b': 2.5, 'q': 2.0, 'g': 1.5, 'f': 1.0,
              'h': 1.0, 'v': 0.8, 'x': 0.5},
    'Italian': {'e': 11.8, 'a': 11.7, 'i': 10.1, 'o': 9.8, 'n': 6.9, 'l': 6.5,
                'r': 6.4, 't': 5.6, 's': 5.0, 'c': 4.5, 'd': 3.7, 'u': 3.0,
                'p': 3.0, 'm': 2.5, 'g': 1.6, 'v': 2.1, 'f': 1.1, 'b': 0.9,
                'h': 0.6, 'z': 0.5, 'q': 0.5},
    'German': {'e': 16.4, 'n': 9.8, 'i': 7.6, 's': 7.3, 'r': 7.0, 'a': 6.5,
               't': 6.2, 'd': 5.1, 'h': 4.8, 'u': 4.4, 'l': 3.4, 'c': 3.1,
               'g': 3.0, 'm': 2.5, 'o': 2.5, 'b': 1.9, 'w': 1.9, 'f': 1.7,
               'k': 1.4, 'z': 1.1, 'p': 0.8},
    'Arabic_Roman': {'a': 14.0, 'l': 10.0, 'i': 8.0, 'n': 7.0, 'm': 6.0,
                     'h': 5.5, 'r': 5.0, 'w': 4.5, 'b': 4.0, 't': 4.0,
                     's': 3.5, 'k': 3.0, 'f': 2.5, 'd': 2.5, 'q': 2.0,
                     'y': 2.0, 'j': 1.5, 'z': 1.0, 'g': 0.8},
    'Hebrew_Roman': {'h': 8.0, 'a': 7.5, 'l': 7.0, 'e': 6.5, 'i': 6.0,
                     'm': 5.5, 'n': 5.0, 'r': 4.5, 'k': 4.0, 'v': 4.0,
                     't': 3.5, 's': 3.0, 'b': 3.0, 'd': 2.5, 'y': 2.0,
                     'sh': 2.0, 'g': 1.5, 'p': 1.5, 'z': 1.0},
}

# Common words in candidate languages
COMMON_WORDS = {
    'Latin': ['et', 'in', 'de', 'ad', 'est', 'non', 'cum', 'per', 'sed', 'ut',
              'que', 'ab', 'ex', 'si', 'aut', 'vel', 'qua', 'hoc', 'quo', 'iam'],
    'Italian': ['di', 'e', 'il', 'la', 'che', 'in', 'un', 'per', 'con', 'del',
                'le', 'da', 'si', 'al', 'lo', 'se', 'no', 'ma', 'li', 'ne'],
    'German': ['der', 'die', 'und', 'in', 'den', 'von', 'zu', 'das', 'mit', 'ist',
               'ein', 'des', 'auf', 'fur', 'als', 'dem', 'an', 'es', 'im', 'er'],
    'Arabic_function': ['al', 'wa', 'fi', 'min', 'ila', 'an', 'la', 'ma', 'bi', 'li'],
    'Hebrew_function': ['ve', 'be', 'le', 'ha', 'et', 'al', 'lo', 'ki', 'im', 'mi',
                        'el', 'ad', 'ze', 'hu', 'hi', 'kol', 'la', 'she', 'al', 'ken'],
}

# Average word lengths
LANG_WORD_LEN = {
    'Latin': 5.5,
    'Italian': 5.0,
    'German': 5.5,
    'Arabic': 4.5,
    'Hebrew': 4.0,
    'English': 4.7,
}


###############################################################################
# 6. Analysis functions
###############################################################################

def word_length_stats(words):
    """Compute word length statistics."""
    lengths = [len(w) for w in words]
    if not lengths:
        return 0, 0, 0
    avg = sum(lengths) / len(lengths)
    variance = sum((l - avg)**2 for l in lengths) / len(lengths)
    return avg, math.sqrt(variance), Counter(lengths)


def freq_correlation(freq1, freq2):
    """Pearson correlation between two frequency distributions (by rank)."""
    # Normalize both to percentages
    total1 = sum(freq1.values())
    total2 = sum(freq2.values())
    if total1 == 0 or total2 == 0:
        return 0.0

    norm1 = {k: v/total1*100 for k, v in freq1.items()}
    norm2 = {k: v/total2*100 for k, v in freq2.items()}

    # Compare rank distributions (position-based, not letter-matching)
    ranks1 = sorted(norm1.values(), reverse=True)
    ranks2 = sorted(norm2.values(), reverse=True)

    # Pad to same length
    max_len = max(len(ranks1), len(ranks2))
    ranks1.extend([0] * (max_len - len(ranks1)))
    ranks2.extend([0] * (max_len - len(ranks2)))

    # Pearson correlation
    n = max_len
    sum_x = sum(ranks1)
    sum_y = sum(ranks2)
    sum_xy = sum(a*b for a, b in zip(ranks1, ranks2))
    sum_x2 = sum(a*a for a in ranks1)
    sum_y2 = sum(b*b for b in ranks2)

    numer = n * sum_xy - sum_x * sum_y
    denom = math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))

    if denom == 0:
        return 0.0
    return numer / denom


def bigram_frequency(words, top_n=30):
    """Compute bigram frequencies within words."""
    counter = Counter()
    for w in words:
        for i in range(len(w) - 1):
            counter[w[i:i+2]] += 1
    return counter.most_common(top_n)


def word_frequency(words, top_n=30):
    """Top N most frequent words."""
    return Counter(words).most_common(top_n)


def match_common_words(word_list, common_words_dict):
    """Check overlap between top words and common words of languages."""
    top_words = set(w for w, _ in word_frequency(word_list, 50))
    results = {}
    for lang, common in common_words_dict.items():
        matches = top_words & set(common)
        results[lang] = (len(matches), matches)
    return results


def cv_pattern(word, vowels='aeiouy'):
    """Convert word to CV pattern."""
    return ''.join('V' if c in vowels else 'C' for c in word)


def cv_analysis(words, vowels='aeiouy'):
    """Analyze consonant/vowel patterns."""
    patterns = Counter()
    v_count = 0
    c_count = 0
    for w in words:
        pat = cv_pattern(w, vowels)
        patterns[pat] += 1
        v_count += pat.count('V')
        c_count += pat.count('C')

    total = v_count + c_count
    v_ratio = v_count / total if total > 0 else 0

    return v_ratio, patterns.most_common(20)


###############################################################################
# 7. Main analysis
###############################################################################

def main():
    print("=" * 80)
    print("VOYNICH MANUSCRIPT: HOMOPHONE COLLAPSE LANGUAGE IDENTIFICATION")
    print("=" * 80)

    # Parse
    words = parse_eva(BASE / "RF1b-e.txt")
    print(f"\nTotal words extracted: {len(words)}")
    print(f"Unique words: {len(set(words))}")

    freq, total_chars = char_frequency(words)
    print(f"Total characters: {total_chars}")
    print(f"Distinct characters: {len(freq)}")

    results = {}

    # =========================================================================
    # STEP 1: Distributional similarity
    # =========================================================================
    print("\n" + "=" * 80)
    print("STEP 1: DISTRIBUTIONAL SIMILARITY (HOMOPHONE DETECTION)")
    print("=" * 80)

    pairs = find_homophones(words, min_freq=30)

    print(f"\nTop 25 most similar character pairs (by context):")
    print(f"{'Pair':>8} {'Left sim':>10} {'Right sim':>10} {'Combined':>10} {'Freq1':>6} {'Freq2':>6}")
    print("-" * 60)

    top_pairs = []
    for c1, c2, ls, rs, comb, f1, f2 in pairs[:25]:
        print(f"  {c1}-{c2:>4} {ls:10.4f} {rs:10.4f} {comb:10.4f} {f1:6d} {f2:6d}")
        top_pairs.append({'pair': f"{c1}-{c2}", 'left_sim': ls, 'right_sim': rs,
                         'combined': comb, 'freq1': f1, 'freq2': f2})

    results['distributional_similarity'] = top_pairs

    # =========================================================================
    # STEP 2: Baseline (no collapse)
    # =========================================================================
    print("\n" + "=" * 80)
    print("STEP 2: BASELINE ANALYSIS (NO COLLAPSE)")
    print("=" * 80)

    avg_len, std_len, len_dist = word_length_stats(words)
    print(f"\nWord length: avg={avg_len:.2f}, std={std_len:.2f}")
    print(f"Length distribution: {dict(sorted(len_dist.items())[:15])}")

    print(f"\nCharacter frequencies (top 15):")
    for c, count in freq.most_common(15):
        print(f"  {c}: {count} ({count/total_chars*100:.1f}%)")

    top_words_base = word_frequency(words, 30)
    print(f"\nTop 30 words:")
    for w, count in top_words_base:
        print(f"  {w}: {count}")

    # =========================================================================
    # STEP 3: Collapse experiments
    # =========================================================================
    print("\n" + "=" * 80)
    print("STEP 3: COLLAPSE MAPPING EXPERIMENTS")
    print("=" * 80)

    collapse_results = {}

    for name, mapping in COLLAPSE_MAPPINGS.items():
        print(f"\n{'─' * 70}")
        print(f"MAPPING: {name}")
        print(f"Rules: {mapping}")
        print(f"{'─' * 70}")

        collapsed = apply_collapse(words, mapping)
        c_freq, c_total = char_frequency(collapsed)
        c_avg, c_std, c_len_dist = word_length_stats(collapsed)

        print(f"  Distinct chars: {len(c_freq)}")
        print(f"  Word length: avg={c_avg:.2f}, std={c_std:.2f}")
        print(f"  Unique words: {len(set(collapsed))} (from {len(set(words))})")

        print(f"\n  Character frequencies (top 15):")
        for c, count in c_freq.most_common(15):
            print(f"    {c}: {count} ({count/c_total*100:.1f}%)")

        # Top words after collapse
        top_collapsed = word_frequency(collapsed, 30)
        print(f"\n  Top 30 words after collapse:")
        for w, count in top_collapsed:
            print(f"    {w}: {count}")

        # Common word matching
        matches = match_common_words(collapsed, COMMON_WORDS)
        print(f"\n  Common word matches:")
        for lang, (n, matched) in sorted(matches.items(), key=lambda x: -x[1][0]):
            if n > 0:
                print(f"    {lang}: {n} matches - {matched}")

        # CV analysis
        v_ratio, cv_patterns = cv_analysis(collapsed, vowels='aeiou')
        print(f"\n  Vowel ratio: {v_ratio:.3f}")
        print(f"  (Latin ~0.45, Italian ~0.48, Arabic ~0.35, Hebrew ~0.35, German ~0.40)")

        # Frequency correlation with languages
        print(f"\n  Rank-frequency correlation with known languages:")
        for lang, lang_freq in LANG_CHAR_FREQ.items():
            lang_counter = Counter({k: int(v*100) for k, v in lang_freq.items()})
            corr = freq_correlation(c_freq, lang_counter)
            print(f"    {lang}: {corr:.4f}")

        # Word length comparison
        print(f"\n  Word length comparison:")
        for lang, target_len in LANG_WORD_LEN.items():
            diff = abs(c_avg - target_len)
            print(f"    {lang} (target {target_len}): diff = {diff:.2f}")

        # Bigram analysis
        bigrams = bigram_frequency(collapsed, 20)
        print(f"\n  Top 20 bigrams:")
        for bg, count in bigrams:
            print(f"    {bg}: {count}")

        collapse_results[name] = {
            'distinct_chars': len(c_freq),
            'unique_words': len(set(collapsed)),
            'avg_word_len': c_avg,
            'vowel_ratio': v_ratio,
            'top_words': [(w, c) for w, c in top_collapsed[:20]],
            'char_freq': [(c, count) for c, count in c_freq.most_common(20)],
        }

    results['collapse_experiments'] = collapse_results

    # =========================================================================
    # STEP 4: Focused bigram-context homophone analysis
    # =========================================================================
    print("\n" + "=" * 80)
    print("STEP 4: BIGRAM-LEVEL DISTRIBUTIONAL ANALYSIS")
    print("=" * 80)

    # Analyze ch vs sh, o vs a, etc. at the word context level
    # For each candidate pair, show words where one is substituted for the other
    candidate_pairs = [('o', 'a'), ('ch', 'sh'), ('d', 's'), ('e', 'y'),
                       ('k', 'q'), ('ck', 'k'), ('ct', 'ch'), ('p', 'f')]

    word_set = set(words)
    word_counter = Counter(words)

    for c1, c2 in candidate_pairs:
        print(f"\n  Pair: {c1} <-> {c2}")
        # Find minimal pairs
        minimal_pairs = []
        for w in sorted(word_set):
            if c1 in w:
                variant = w.replace(c1, c2, 1)
                if variant in word_set and variant != w:
                    minimal_pairs.append((w, variant, word_counter[w], word_counter[variant]))

        if minimal_pairs:
            print(f"    Minimal pairs found: {len(minimal_pairs)}")
            for w1, w2, f1, f2 in minimal_pairs[:10]:
                print(f"      {w1} ({f1}) <-> {w2} ({f2})")
        else:
            print(f"    No minimal pairs found")

    # =========================================================================
    # STEP 5: Word initial/final patterns (morphological clues)
    # =========================================================================
    print("\n" + "=" * 80)
    print("STEP 5: MORPHOLOGICAL PATTERN ANALYSIS")
    print("=" * 80)

    # Word-initial character frequency
    initial = Counter(w[0] for w in words if w)
    print("\nWord-initial character frequencies:")
    for c, count in initial.most_common(15):
        print(f"  {c}: {count} ({count/len(words)*100:.1f}%)")

    # Word-final character frequency
    final = Counter(w[-1] for w in words if w)
    print("\nWord-final character frequencies:")
    for c, count in final.most_common(15):
        print(f"  {c}: {count} ({count/len(words)*100:.1f}%)")

    # Word-initial bigram
    initial_bi = Counter(w[:2] for w in words if len(w) >= 2)
    print("\nWord-initial bigram frequencies:")
    for bg, count in initial_bi.most_common(15):
        print(f"  {bg}: {count} ({count/len(words)*100:.1f}%)")

    # Word-final bigram
    final_bi = Counter(w[-2:] for w in words if len(w) >= 2)
    print("\nWord-final bigram frequencies:")
    for bg, count in final_bi.most_common(15):
        print(f"  {bg}: {count} ({count/len(words)*100:.1f}%)")

    # =========================================================================
    # STEP 6: Data-driven collapse (auto-merge most similar pairs)
    # =========================================================================
    print("\n" + "=" * 80)
    print("STEP 6: DATA-DRIVEN COLLAPSE")
    print("=" * 80)

    # Use distributional similarity to build automatic mapping
    # Merge pairs with combined similarity > 0.90
    threshold_results = {}
    for threshold in [0.95, 0.90, 0.85, 0.80]:
        merge_groups = {}  # char -> canonical form
        for c1, c2, ls, rs, comb, f1, f2 in pairs:
            if comb >= threshold:
                # Merge less frequent into more frequent
                if f1 >= f2:
                    canon, other = c1, c2
                else:
                    canon, other = c2, c1
                # Follow chains
                while canon in merge_groups:
                    canon = merge_groups[canon]
                merge_groups[other] = canon

        if merge_groups:
            collapsed_dd = []
            for w in words:
                new_w = ''.join(merge_groups.get(c, c) for c in w)
                collapsed_dd.append(new_w)

            dd_freq, dd_total = char_frequency(collapsed_dd)
            dd_avg, _, _ = word_length_stats(collapsed_dd)

            print(f"\n  Threshold: {threshold}")
            print(f"  Merges: {merge_groups}")
            print(f"  Distinct chars: {len(dd_freq)}")
            print(f"  Unique words: {len(set(collapsed_dd))}")
            print(f"  Avg word length: {dd_avg:.2f}")

            top_dd = word_frequency(collapsed_dd, 15)
            print(f"  Top 15 words:")
            for w, count in top_dd:
                print(f"    {w}: {count}")

            threshold_results[threshold] = {
                'merges': {k: v for k, v in merge_groups.items()},
                'distinct_chars': len(dd_freq),
                'unique_words': len(set(collapsed_dd)),
            }

    results['data_driven'] = threshold_results

    # =========================================================================
    # STEP 7: Summary scoring
    # =========================================================================
    print("\n" + "=" * 80)
    print("STEP 7: OVERALL LANGUAGE IDENTIFICATION SCORING")
    print("=" * 80)

    # For each collapse level, score against each language
    print("\nScoring each collapse mapping against candidate languages:")
    print("(Higher = better match)")
    print()

    for name, mapping in COLLAPSE_MAPPINGS.items():
        collapsed = apply_collapse(words, mapping)
        c_freq, c_total = char_frequency(collapsed)
        c_avg, _, _ = word_length_stats(collapsed)
        v_ratio, _ = cv_analysis(collapsed, vowels='aeiou')
        matches = match_common_words(collapsed, COMMON_WORDS)

        print(f"\n  [{name}]")
        for lang in ['Latin', 'Italian', 'German']:
            score = 0

            # Word length score (max 25)
            target = LANG_WORD_LEN.get(lang, 5.0)
            len_diff = abs(c_avg - target)
            score += max(0, 25 - len_diff * 10)

            # Char count score (max 25)
            target_chars = {'Latin': 23, 'Italian': 21, 'German': 26}
            char_diff = abs(len(c_freq) - target_chars.get(lang, 23))
            score += max(0, 25 - char_diff * 3)

            # Vowel ratio score (max 25)
            target_vr = {'Latin': 0.45, 'Italian': 0.48, 'German': 0.40}
            vr_diff = abs(v_ratio - target_vr.get(lang, 0.42))
            score += max(0, 25 - vr_diff * 100)

            # Common word match score (max 25)
            lang_key = lang
            if lang_key in matches:
                score += matches[lang_key][0] * 5

            print(f"    {lang}: {score:.1f}/100")

        for lang in ['Arabic_function', 'Hebrew_function']:
            score = 0
            if lang in matches:
                score += matches[lang][0] * 5
            target_vr = 0.35
            vr_diff = abs(v_ratio - target_vr)
            score += max(0, 25 - vr_diff * 100)
            print(f"    {lang}: {score:.1f}/100 (partial)")

    return results


if __name__ == '__main__':
    results = main()
