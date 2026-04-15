#!/usr/bin/env python3
"""
Homophone Collapse Analysis of the Voynich Manuscript
Based on the sandhi discovery: words ending in n/l/r are variants of the same stem.
"""

import re
import math
from collections import Counter, defaultdict

def parse_eva_file(filepath):
    """Parse EVA transcription file (IVTFF format), extract words per line."""
    lines = []
    all_words = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for raw_line in f:
            raw_line = raw_line.strip()
            # Skip comments and empty lines
            if raw_line.startswith('#') or not raw_line:
                continue
            # Skip page headers like <f1r>  <! $Q=A ...>
            # These contain only metadata, no text
            if re.match(r'^<[^.]+>\s+<!\s+\$', raw_line):
                continue
            # Extract text after the folio/line identifier
            # Format: <f1r.1,@P0>  text here
            m = re.match(r'<[^>]+>\s+(.*)', raw_line)
            if not m:
                continue
            text = m.group(1)
            # Remove inline comments like <! ...>
            text = re.sub(r'<!.*?>', '', text)
            # Remove curly-brace annotations {cto} etc - keep content inside as it's glyph info
            text = re.sub(r'\{([^}]*)\}', r'\1', text)
            # Remove @-codes (plant references, uncertain readings)
            text = re.sub(r'@\d+;?', '', text)
            # Replace <-> (line breaks in multi-column text) with space
            text = re.sub(r'<->', ' ', text)
            # Replace dots with spaces (EVA word separator)
            text = text.replace('.', ' ')
            # Remove commas and other punctuation that aren't part of words
            text = re.sub(r'[,;:?!]', '', text)
            # Remove single quotes used as glyph modifiers in some notations
            text = re.sub(r"'", '', text)
            # Split into words
            words = text.split()
            # Filter: remove single characters, remove words that are just punctuation/noise
            clean_words = []
            for w in words:
                w = w.strip()
                if len(w) < 2:
                    continue
                # Skip if it looks like metadata (contains = or $ or >)
                if '=' in w or '$' in w or '>' in w or '<' in w:
                    continue
                clean_words.append(w)
            if clean_words:
                lines.append(clean_words)
                all_words.extend(clean_words)
    return lines, all_words


def collapse_sandhi(word):
    """
    Collapse sandhi variants: if a word ends in n, l, or r,
    replace the final character with '*' to get the stem form.
    Words ending in y are left unchanged (different morphological class).
    """
    if len(word) < 2:
        return word
    if word[-1] in ('n', 'l', 'r'):
        return word[:-1] + '*'
    return word


def build_bigram_matrix(words):
    """Build bigram transition counts."""
    bigrams = Counter()
    for i in range(len(words) - 1):
        bigrams[(words[i], words[i+1])] += 1
    return bigrams


def build_trigram_counts(words):
    """Build trigram counts."""
    trigrams = Counter()
    for i in range(len(words) - 2):
        trigrams[(words[i], words[i+1], words[i+2])] += 1
    return trigrams


def calculate_entropy(words):
    """Calculate unigram entropy (bits per word)."""
    total = len(words)
    freq = Counter(words)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy


def calculate_conditional_entropy(words):
    """Calculate conditional entropy H(W_i | W_{i-1}) from bigrams."""
    bigram_counts = defaultdict(Counter)
    unigram_counts = Counter()
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        bigram_counts[w1][w2] += 1
        unigram_counts[w1] += 1

    total_bigrams = sum(unigram_counts.values())
    cond_entropy = 0.0
    for w1, next_words in bigram_counts.items():
        p_w1 = unigram_counts[w1] / total_bigrams
        for w2, count in next_words.items():
            p_w2_given_w1 = count / unigram_counts[w1]
            if p_w2_given_w1 > 0:
                cond_entropy -= p_w1 * p_w2_given_w1 * math.log2(p_w2_given_w1)
    return cond_entropy


def main():
    filepath = r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt'
    lines, all_words = parse_eva_file(filepath)

    print(f"Total words extracted: {len(all_words)}")
    print(f"Total lines: {len(lines)}")
    print(f"Sample words (first 30): {all_words[:30]}")

    # ===== BEFORE COLLAPSE =====
    vocab_before = set(all_words)
    freq_before = Counter(all_words)
    entropy_before = calculate_entropy(all_words)
    cond_entropy_before = calculate_conditional_entropy(all_words)

    print(f"\n=== BEFORE COLLAPSE ===")
    print(f"Unique words: {len(vocab_before)}")
    print(f"Unigram entropy: {entropy_before:.4f} bits/word")
    print(f"Conditional entropy H(W|W-1): {cond_entropy_before:.4f} bits/word")

    # ===== COLLAPSE =====
    collapsed_words = [collapse_sandhi(w) for w in all_words]
    collapsed_lines = [[collapse_sandhi(w) for w in line] for line in lines]

    vocab_after = set(collapsed_words)
    freq_after = Counter(collapsed_words)
    entropy_after = calculate_entropy(collapsed_words)
    cond_entropy_after = calculate_conditional_entropy(collapsed_words)

    print(f"\n=== AFTER COLLAPSE ===")
    print(f"Unique words: {len(vocab_after)}")
    print(f"Vocabulary reduction: {len(vocab_before) - len(vocab_after)} words ({(1 - len(vocab_after)/len(vocab_before))*100:.1f}%)")
    print(f"Unigram entropy: {entropy_after:.4f} bits/word")
    print(f"Conditional entropy H(W|W-1): {cond_entropy_after:.4f} bits/word")
    print(f"Entropy reduction (unigram): {entropy_before - entropy_after:.4f} bits/word")
    print(f"Conditional entropy reduction: {cond_entropy_before - cond_entropy_after:.4f} bits/word")

    # ===== SHOW COLLAPSE EXAMPLES =====
    print(f"\n=== COLLAPSE EXAMPLES (top 40 by combined frequency) ===")
    # Find words that collapsed together
    collapse_map = defaultdict(set)
    for orig in vocab_before:
        col = collapse_sandhi(orig)
        if col.endswith('*'):
            collapse_map[col].add(orig)

    # Show top collapse groups by total frequency
    collapse_groups = []
    for stem, originals in collapse_map.items():
        total_freq = sum(freq_before.get(o, 0) for o in originals)
        collapse_groups.append((stem, originals, total_freq))
    collapse_groups.sort(key=lambda x: -x[2])
    for stem, originals, total in collapse_groups[:40]:
        orig_freqs = [(o, freq_before[o]) for o in sorted(originals, key=lambda x: -freq_before[x])]
        detail = ', '.join(f'{o}({f})' for o, f in orig_freqs if f > 0)
        print(f"  {stem} <- {detail} = total {total}")

    # ===== NLR suffix distribution =====
    print(f"\n=== NLR SUFFIX DISTRIBUTION ===")
    suffix_counts = Counter()
    suffix_by_stem = defaultdict(Counter)
    for w in all_words:
        if len(w) >= 2 and w[-1] in ('n', 'l', 'r'):
            suffix_counts[w[-1]] += 1
            stem = w[:-1]
            suffix_by_stem[stem][w[-1]] += 1
    total_nlr = sum(suffix_counts.values())
    total_all = len(all_words)
    print(f"Total NLR-final words: {total_nlr} ({total_nlr/total_all*100:.1f}% of all tokens)")
    for s in ('n', 'l', 'r'):
        print(f"  -{s}: {suffix_counts[s]} ({suffix_counts[s]/total_nlr*100:.1f}% of NLR)")

    # Stems that appear with multiple suffixes (true sandhi alternation)
    multi_suffix_stems = {stem: dict(suffixes) for stem, suffixes in suffix_by_stem.items()
                         if len(suffixes) > 1}
    print(f"\nStems appearing with 2+ different suffixes (true alternation): {len(multi_suffix_stems)}")
    # Sort by total frequency
    sorted_multi = sorted(multi_suffix_stems.items(), key=lambda x: -sum(x[1].values()))
    for stem, suffixes in sorted_multi[:30]:
        total = sum(suffixes.values())
        detail = ', '.join(f'-{s}:{c}' for s, c in sorted(suffixes.items(), key=lambda x: -x[1]))
        print(f"  {stem}- : {detail} (total {total})")

    # ===== BIGRAM ANALYSIS =====
    bigrams = build_bigram_matrix(collapsed_words)
    print(f"\n=== TOP 50 BIGRAMS (collapsed) ===")
    for (w1, w2), count in bigrams.most_common(50):
        print(f"  {w1} -> {w2}: {count}")

    # ===== TRIGRAM ANALYSIS =====
    trigrams = build_trigram_counts(collapsed_words)
    print(f"\n=== TOP 40 TRIGRAMS (collapsed) ===")
    for (w1, w2, w3), count in trigrams.most_common(40):
        print(f"  {w1} {w2} {w3}: {count}")

    # ===== SYNTACTIC PATTERNS =====
    print(f"\n=== SYNTACTIC PATTERNS ===")

    # Top collapsed words by frequency
    print(f"\n--- Top 60 collapsed words ---")
    for w, c in freq_after.most_common(60):
        pct = c / len(collapsed_words) * 100
        print(f"  {w}: {c} ({pct:.2f}%)")

    # What follows cho*?
    print(f"\n--- What follows 'cho*'? (cho* = chol/chor/chon collapsed) ---")
    cho_followers = Counter()
    for i in range(len(collapsed_words) - 1):
        if collapsed_words[i] == 'cho*':
            cho_followers[collapsed_words[i+1]] += 1
    for w, c in cho_followers.most_common(20):
        print(f"  cho* -> {w}: {c}")

    # What follows sho*?
    print(f"\n--- What follows 'sho*'? ---")
    sho_followers = Counter()
    for i in range(len(collapsed_words) - 1):
        if collapsed_words[i] == 'sho*':
            sho_followers[collapsed_words[i+1]] += 1
    for w, c in sho_followers.most_common(20):
        print(f"  sho* -> {w}: {c}")

    # What follows ctho*?
    print(f"\n--- What follows 'ctho*'? ---")
    ctho_followers = Counter()
    for i in range(len(collapsed_words) - 1):
        if collapsed_words[i] == 'ctho*':
            ctho_followers[collapsed_words[i+1]] += 1
    for w, c in ctho_followers.most_common(20):
        print(f"  ctho* -> {w}: {c}")

    # What precedes daii*?
    print(f"\n--- What precedes 'daii*'? ---")
    daii_pred = Counter()
    for i in range(1, len(collapsed_words)):
        if collapsed_words[i] == 'daii*':
            daii_pred[collapsed_words[i-1]] += 1
    for w, c in daii_pred.most_common(20):
        print(f"  {w} -> daii*: {c}")

    # What follows daii*?
    print(f"\n--- What follows 'daii*'? ---")
    daii_foll = Counter()
    for i in range(len(collapsed_words) - 1):
        if collapsed_words[i] == 'daii*':
            daii_foll[collapsed_words[i+1]] += 1
    for w, c in daii_foll.most_common(20):
        print(f"  daii* -> {w}: {c}")

    # What precedes cho*?
    print(f"\n--- What precedes 'cho*'? ---")
    cho_pred = Counter()
    for i in range(1, len(collapsed_words)):
        if collapsed_words[i] == 'cho*':
            cho_pred[collapsed_words[i-1]] += 1
    for w, c in cho_pred.most_common(20):
        print(f"  {w} -> cho*: {c}")

    # What follows qo- words?
    print(f"\n--- What follows 'qo*'? ---")
    qo_followers = Counter()
    for i in range(len(collapsed_words) - 1):
        if collapsed_words[i] == 'qo*':
            qo_followers[collapsed_words[i+1]] += 1
    for w, c in qo_followers.most_common(15):
        print(f"  qo* -> {w}: {c}")

    # What follows 'o*'?
    print(f"\n--- What follows 'o*'? ---")
    o_followers = Counter()
    for i in range(len(collapsed_words) - 1):
        if collapsed_words[i] == 'o*':
            o_followers[collapsed_words[i+1]] += 1
    for w, c in o_followers.most_common(15):
        print(f"  o* -> {w}: {c}")

    # ===== LINE-INITIAL AND LINE-FINAL =====
    print(f"\n=== LINE-INITIAL WORDS (collapsed) ===")
    line_initial = Counter()
    for line in collapsed_lines:
        if line:
            line_initial[line[0]] += 1
    for w, c in line_initial.most_common(25):
        print(f"  {w}: {c}")

    print(f"\n=== LINE-FINAL WORDS (collapsed) ===")
    line_final = Counter()
    for line in collapsed_lines:
        if line:
            line_final[line[-1]] += 1
    for w, c in line_final.most_common(25):
        print(f"  {w}: {c}")

    # ===== WORD-CLASS TRANSITION ANALYSIS =====
    print(f"\n=== WORD CLASS TRANSITIONS ===")
    def classify(w):
        if w.endswith('y') and not w.endswith('*'):
            return 'Y-class'
        elif w.endswith('*'):
            return 'NLR-stem'
        else:
            return 'Other'

    class_bigrams = Counter()
    for i in range(len(collapsed_words) - 1):
        c1 = classify(collapsed_words[i])
        c2 = classify(collapsed_words[i+1])
        class_bigrams[(c1, c2)] += 1

    total_cb = sum(class_bigrams.values())
    for (c1, c2), count in class_bigrams.most_common():
        print(f"  {c1} -> {c2}: {count} ({count/total_cb*100:.1f}%)")

    # ===== HAPAX =====
    hapax_before = sum(1 for w, c in freq_before.items() if c == 1)
    hapax_after = sum(1 for w, c in freq_after.items() if c == 1)
    print(f"\n=== HAPAX LEGOMENA ===")
    print(f"Before collapse: {hapax_before} ({hapax_before/len(vocab_before)*100:.1f}% of vocabulary)")
    print(f"After collapse: {hapax_after} ({hapax_after/len(vocab_after)*100:.1f}% of vocabulary)")

    # ===== ENTROPY SUMMARY =====
    print(f"\n=== ENTROPY SUMMARY ===")
    print(f"                          Before     After     Delta")
    print(f"Unigram entropy:         {entropy_before:8.4f}   {entropy_after:8.4f}   {entropy_before - entropy_after:+.4f}")
    print(f"Conditional entropy:     {cond_entropy_before:8.4f}   {cond_entropy_after:8.4f}   {cond_entropy_before - cond_entropy_after:+.4f}")
    print(f"Unique vocabulary:       {len(vocab_before):8d}   {len(vocab_after):8d}   {len(vocab_before) - len(vocab_after):+d}")

    bigram_entropy_before = calculate_conditional_entropy(all_words)
    bigram_entropy_after = calculate_conditional_entropy(collapsed_words)

    print(f"\nReference ranges (from NLP literature):")
    print(f"  Medieval Latin prose:              ~8-10 bits/word unigram")
    print(f"  Medieval pharmaceutical Latin:     ~7-9 bits/word (restricted vocab)")
    print(f"  Highly formulaic recipe text:      ~5-7 bits/word unigram")
    print(f"  Random/meaningless text:           ~10-12+ bits/word")
    print(f"  Modern English:                    ~9-11 bits/word unigram, ~6-8 conditional")
    print(f"  Voynich (collapsed):               {entropy_after:.4f} bits/word unigram")

    # ===== SPECIFIC PATTERN SEARCHES =====
    print(f"\n=== COMMON PATTERNS IN COLLAPSED TEXT ===")
    # Look for repeated sentence-like patterns
    # Find 4-grams
    fourgrams = Counter()
    for i in range(len(collapsed_words) - 3):
        fourgrams[(collapsed_words[i], collapsed_words[i+1], collapsed_words[i+2], collapsed_words[i+3])] += 1
    print(f"\n--- Top 20 4-grams ---")
    for gram, count in fourgrams.most_common(20):
        if count >= 2:
            print(f"  {' '.join(gram)}: {count}")

    # ===== Y-CLASS vs NLR-STEM FREQUENCY =====
    print(f"\n=== MORPHOLOGICAL CLASS DISTRIBUTION ===")
    y_count = sum(1 for w in collapsed_words if w.endswith('y') and not w.endswith('*'))
    nlr_count = sum(1 for w in collapsed_words if w.endswith('*'))
    other_count = len(collapsed_words) - y_count - nlr_count
    print(f"  Y-class tokens: {y_count} ({y_count/len(collapsed_words)*100:.1f}%)")
    print(f"  NLR-stem tokens: {nlr_count} ({nlr_count/len(collapsed_words)*100:.1f}%)")
    print(f"  Other tokens: {other_count} ({other_count/len(collapsed_words)*100:.1f}%)")

    y_types = sum(1 for w in vocab_after if w.endswith('y') and not w.endswith('*'))
    nlr_types = sum(1 for w in vocab_after if w.endswith('*'))
    other_types = len(vocab_after) - y_types - nlr_types
    print(f"  Y-class types: {y_types} ({y_types/len(vocab_after)*100:.1f}%)")
    print(f"  NLR-stem types: {nlr_types} ({nlr_types/len(vocab_after)*100:.1f}%)")
    print(f"  Other types: {other_types} ({other_types/len(vocab_after)*100:.1f}%)")

    return {
        'total_words': len(all_words),
        'vocab_before': len(vocab_before),
        'vocab_after': len(vocab_after),
        'entropy_before': entropy_before,
        'entropy_after': entropy_after,
        'cond_entropy_before': cond_entropy_before,
        'cond_entropy_after': cond_entropy_after,
        'freq_after': freq_after,
        'bigrams': bigrams,
        'trigrams': trigrams,
    }


if __name__ == '__main__':
    results = main()
