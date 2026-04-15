#!/usr/bin/env python3
"""
Phonological re-analysis of Voynich manuscript vocabulary.
Tests whether chol/chor are sandhi variants of the same stem,
calculates true vocabulary size based on stems, and attempts
sentence-level readings.
"""

import re
from collections import defaultdict, Counter

def load_words(filepath):
    """Load all words from EVA transcription, preserving folio/line context."""
    words_with_context = []  # (folio, line_num, word_index, word)
    current_folio = ""

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Detect folio headers
            m = re.match(r'^<(f\d+[rv]\d?)>', line)
            if m:
                current_folio = m.group(1)
                continue
            # Parse text lines
            m = re.match(r'^<(f\d+[rv]\d?)\.(\d+)', line)
            if not m:
                continue
            folio = m.group(1)
            line_num = int(m.group(2))
            # Extract text after the >
            text_match = re.search(r'>\s+(.*)', line)
            if not text_match:
                continue
            text = text_match.group(1)
            # Remove annotations
            text = re.sub(r'\{[^}]*\}', '', text)
            text = re.sub(r'@\d+;?', '', text)
            text = re.sub(r'<->', ' ', text)
            text = re.sub(r'[,?!]', '', text)
            # Split into words
            raw_words = text.split('.')
            for i, w in enumerate(raw_words):
                w = w.strip()
                if w and len(w) > 0 and re.match(r'^[a-z]+$', w):
                    words_with_context.append((folio, line_num, i, w))
    return words_with_context

def get_stem_suffix(word):
    """Split word into stem + suffix (n/l/r) if applicable."""
    if len(word) < 2:
        return None, None
    last = word[-1]
    if last in ('n', 'l', 'r'):
        return word[:-1], last
    return None, None

def analyze_chol_vs_chor(words_with_context):
    """Analyze what words follow chol vs chor to test sandhi hypothesis."""
    print("=" * 80)
    print("ANALYSIS 1: chol vs chor -- Next-Word Analysis")
    print("=" * 80)

    # Build bigrams within same folio+line
    chol_next = []
    chor_next = []

    for idx in range(len(words_with_context) - 1):
        folio1, line1, _, word1 = words_with_context[idx]
        folio2, line2, _, word2 = words_with_context[idx + 1]

        # Only within same folio and line
        if folio1 == folio2 and line1 == line2:
            if word1 == 'chol':
                chol_next.append(word2)
            elif word1 == 'chor':
                chor_next.append(word2)

    print(f"\nchol followed by {len(chol_next)} words (within-line)")
    print(f"chor followed by {len(chor_next)} words (within-line)")

    # Categorize by initial character
    def initial_dist(next_words):
        dist = Counter()
        for w in next_words:
            if w:
                dist[w[0]] += 1
        return dist

    chol_init = initial_dist(chol_next)
    chor_init = initial_dist(chor_next)

    print("\n--- Initial character of following word ---")
    print(f"{'Init':>5} {'After chol':>12} {'After chor':>12} {'chol%':>8} {'chor%':>8}")
    all_inits = sorted(set(list(chol_init.keys()) + list(chor_init.keys())))
    total_chol = len(chol_next)
    total_chor = len(chor_next)

    vowels_chol = 0
    vowels_chor = 0
    stops_chol = 0
    stops_chor = 0

    for init in all_inits:
        c = chol_init.get(init, 0)
        r = chor_init.get(init, 0)
        cp = f"{100*c/total_chol:.1f}%" if total_chol > 0 else "0%"
        rp = f"{100*r/total_chor:.1f}%" if total_chor > 0 else "0%"
        print(f"{init:>5} {c:>12} {r:>12} {cp:>8} {rp:>8}")

        if init in ('a', 'e', 'i', 'o'):
            vowels_chol += c
            vowels_chor += r
        if init in ('k', 't', 'p', 'd'):
            stops_chol += c
            stops_chor += r

    print(f"\n--- Phonological class summary ---")
    print(f"Before VOWELS:  chol={vowels_chol} ({100*vowels_chol/total_chol:.1f}%), chor={vowels_chor} ({100*vowels_chor/total_chor:.1f}%)")
    print(f"Before STOPS:   chol={stops_chol} ({100*stops_chol/total_chol:.1f}%), chor={stops_chor} ({100*stops_chor/total_chor:.1f}%)")

    # Test: if sandhi, chor should appear more before vowels, chol before stops
    print(f"\n--- SANDHI TEST ---")
    if total_chor > 0 and total_chol > 0:
        chor_vowel_pct = 100 * vowels_chor / total_chor
        chol_vowel_pct = 100 * vowels_chol / total_chol
        chor_stop_pct = 100 * stops_chor / total_chor
        chol_stop_pct = 100 * stops_chol / total_chol
        print(f"chor before vowels: {chor_vowel_pct:.1f}% vs chol before vowels: {chol_vowel_pct:.1f}%")
        print(f"chol before stops:  {chol_stop_pct:.1f}% vs chor before stops:  {chor_stop_pct:.1f}%")

        if chor_vowel_pct > chol_vowel_pct + 5:
            print(">> SANDHI CONFIRMED: chor significantly more likely before vowels")
        else:
            print(">> SANDHI NOT CONFIRMED: chor not significantly more before vowels")

    # Show most common full words following each
    print(f"\nTop 10 words following chol:")
    for w, c in Counter(chol_next).most_common(10):
        print(f"  {w}: {c}")
    print(f"\nTop 10 words following chor:")
    for w, c in Counter(chor_next).most_common(10):
        print(f"  {w}: {c}")

    return chol_next, chor_next


def analyze_all_nlr_pairs(words_with_context):
    """For all major n/l/r stem groups, test sandhi hypothesis."""
    print("\n" + "=" * 80)
    print("ANALYSIS 2: Systematic Sandhi Test for Major Stems")
    print("=" * 80)

    # Define stem groups to test
    test_stems = {
        'cho': ['chol', 'chor', 'chon'],
        'sho': ['shol', 'shor', 'shon'],
        'da': ['dal', 'dar', 'dan'],
        'daii': ['daiin', 'daiir', 'daiil'],
        'o': ['ol', 'or', 'on'],
        'a': ['al', 'ar', 'an'],
        'ctho': ['cthol', 'cthor', 'cthon'],
        'cha': ['chal', 'char', 'chan'],
        'sha': ['shal', 'shar', 'shan'],
    }

    results = {}

    for stem, variants in test_stems.items():
        next_by_variant = defaultdict(list)

        for idx in range(len(words_with_context) - 1):
            folio1, line1, _, word1 = words_with_context[idx]
            folio2, line2, _, word2 = words_with_context[idx + 1]

            if folio1 == folio2 and line1 == line2:
                for v in variants:
                    if word1 == v:
                        next_by_variant[v].append(word2)

        if sum(len(v) for v in next_by_variant.values()) < 10:
            continue

        print(f"\n--- Stem '{stem}' ---")
        for v in variants:
            nw = next_by_variant.get(v, [])
            if len(nw) == 0:
                continue
            vowel_count = sum(1 for w in nw if w and w[0] in 'aeiou')
            stop_count = sum(1 for w in nw if w and w[0] in 'ktpd')
            fric_count = sum(1 for w in nw if w and w[0] in 'scf')
            total = len(nw)
            print(f"  {v:>10}: N={total:>4}, before vowels={vowel_count:>3} ({100*vowel_count/total:.0f}%), "
                  f"before stops={stop_count:>3} ({100*stop_count/total:.0f}%), "
                  f"before fric={fric_count:>3} ({100*fric_count/total:.0f}%)")

        results[stem] = next_by_variant

    return results


def count_unique_stems(words_with_context):
    """Calculate true vocabulary size based on stems."""
    print("\n" + "=" * 80)
    print("ANALYSIS 3: True Vocabulary Size (Stem-Based)")
    print("=" * 80)

    all_words = [w for _, _, _, w in words_with_context]
    surface_vocab = set(all_words)
    surface_counts = Counter(all_words)

    # Method 1: Simple strip n/l/r from end
    stem_map = defaultdict(set)  # stem -> set of surface forms
    stem_counts = Counter()

    for word in all_words:
        if len(word) >= 2 and word[-1] in 'nlr':
            stem = word[:-1]
            stem_map[stem].add(word)
            stem_counts[stem] += 1
        else:
            stem_map[word].add(word)
            stem_counts[word] += 1

    # Words ending in -y (not part of n/l/r system)
    y_words = [w for w in all_words if w.endswith('y')]
    y_vocab = set(y_words)

    # Words ending in n/l/r
    nlr_words = [w for w in all_words if len(w) >= 2 and w[-1] in 'nlr']
    nlr_surface = set(nlr_words)

    # Other words
    other_words = [w for w in all_words if not w.endswith('y') and not (len(w) >= 2 and w[-1] in 'nlr')]
    other_vocab = set(other_words)

    # Count stems that have multiple n/l/r variants
    multi_variant_stems = {s: forms for s, forms in stem_map.items()
                           if len(forms) > 1 and any(f[-1] in 'nlr' for f in forms if len(f) >= 2)}

    print(f"\n--- Surface Form Counts ---")
    print(f"Total tokens: {len(all_words)}")
    print(f"Total unique surface forms: {len(surface_vocab)}")
    print(f"  Words ending in -y: {len(y_vocab)} types, {len(y_words)} tokens")
    print(f"  Words ending in -n/l/r: {len(nlr_surface)} types, {len(nlr_words)} tokens")
    print(f"  Other words: {len(other_vocab)} types, {len(other_words)} tokens")

    # Stems
    nlr_stems = set()
    for word in nlr_words:
        nlr_stems.add(word[:-1])

    print(f"\n--- Stem-Based Counts ---")
    print(f"Unique stems (from n/l/r words): {len(nlr_stems)}")
    print(f"Reduction: {len(nlr_surface)} surface forms -> {len(nlr_stems)} stems")
    print(f"  Collapsed: {len(nlr_surface) - len(nlr_stems)} surface forms are sandhi variants")

    # Total effective vocabulary
    total_stem_vocab = len(nlr_stems) + len(y_vocab) + len(other_vocab)
    print(f"\n--- Effective Vocabulary ---")
    print(f"Stems (n/l/r words): {len(nlr_stems)}")
    print(f"Y-ending words: {len(y_vocab)}")
    print(f"Other words: {len(other_vocab)}")
    print(f"TOTAL EFFECTIVE VOCABULARY: {total_stem_vocab}")
    print(f"Reduction from surface: {len(surface_vocab)} -> {total_stem_vocab} ({100*(1-total_stem_vocab/len(surface_vocab)):.1f}% reduction)")

    # Show top stems with multiple variants
    print(f"\n--- Top 30 Stems with Multiple n/l/r Variants ---")
    sorted_multi = sorted(multi_variant_stems.items(),
                          key=lambda x: stem_counts[x[0]], reverse=True)[:30]
    for stem, forms in sorted_multi:
        form_strs = []
        for f in sorted(forms):
            form_strs.append(f"{f}({surface_counts[f]})")
        print(f"  {stem:>15}: {stem_counts[stem]:>5} tokens -> {', '.join(form_strs)}")

    return stem_map, nlr_stems, surface_vocab


def analyze_y_endings(words_with_context):
    """Analyze -y ending words separately."""
    print("\n" + "=" * 80)
    print("ANALYSIS 4: -y Ending Words (Outside n/l/r System)")
    print("=" * 80)

    all_words = [w for _, _, _, w in words_with_context]
    y_words = [w for w in all_words if w.endswith('y')]

    print(f"\nTotal -y words: {len(y_words)} tokens")
    print(f"Unique -y words: {len(set(y_words))} types")
    print(f"Percentage of corpus: {100*len(y_words)/len(all_words):.1f}%")

    # Top -y words
    y_counts = Counter(y_words)
    print(f"\nTop 30 -y words:")
    for w, c in y_counts.most_common(30):
        print(f"  {w:>20}: {c}")

    # Are -y words ever followed by specific patterns?
    # If -y is a specific morphological marker, what follows?
    y_next_init = Counter()
    for idx in range(len(words_with_context) - 1):
        folio1, line1, _, word1 = words_with_context[idx]
        folio2, line2, _, word2 = words_with_context[idx + 1]
        if folio1 == folio2 and line1 == line2 and word1.endswith('y'):
            if word2:
                y_next_init[word2[0]] += 1

    print(f"\n-y words: initial of following word:")
    total = sum(y_next_init.values())
    for init, c in y_next_init.most_common():
        print(f"  {init}: {c} ({100*c/total:.1f}%)")


def sentence_level_reading(words_with_context):
    """Attempt sentence-level reading of f47r line 7 and f1r lines 1-5."""
    print("\n" + "=" * 80)
    print("ANALYSIS 5: Sentence-Level Reading Attempts")
    print("=" * 80)

    # Extract specific lines
    target_lines = [
        ('f1r', 1), ('f1r', 2), ('f1r', 3), ('f1r', 4), ('f1r', 5),
        ('f47r', 7),
    ]

    for target_folio, target_line in target_lines:
        line_words = [(i, w) for folio, line_num, i, w in words_with_context
                      if folio == target_folio and line_num == target_line]

        if not line_words:
            print(f"\n{target_folio}.{target_line}: NO WORDS FOUND")
            continue

        print(f"\n--- {target_folio}.{target_line} ---")
        print(f"Raw: {' '.join(w for _, w in line_words)}")

        # For each word, identify stem and suffix type
        analysis = []
        for idx, (i, word) in enumerate(line_words):
            stem, suffix = get_stem_suffix(word)

            # Get next word for sandhi check
            next_word = None
            if idx + 1 < len(line_words):
                next_word = line_words[idx + 1][1]

            if stem is not None:
                # Check if suffix matches default for stem-final vowel
                stem_final = stem[-1] if stem else '?'
                expected = {'i': 'n', 'o': 'l', 'a': 'r'}.get(stem_final, '?')
                is_default = suffix == expected

                # Check sandhi prediction
                sandhi_pred = None
                if next_word and len(next_word) > 0:
                    next_init = next_word[0]
                    if next_init in 'aeiou':
                        sandhi_pred = 'r'
                    elif next_init in 'ktpdlr':
                        sandhi_pred = 'l'
                    elif next_init in 'scf':
                        sandhi_pred = 'n'

                sandhi_match = ''
                if sandhi_pred:
                    if suffix == sandhi_pred:
                        sandhi_match = 'SANDHI-OK'
                    elif is_default:
                        sandhi_match = 'DEFAULT'
                    else:
                        sandhi_match = f'UNEXPECTED (expected {expected} or {sandhi_pred})'
                elif is_default:
                    sandhi_match = 'DEFAULT'
                else:
                    sandhi_match = f'NON-DEFAULT (expected {expected})'

                analysis.append({
                    'word': word,
                    'stem': stem,
                    'suffix': suffix,
                    'stem_final': stem_final,
                    'expected': expected,
                    'is_default': is_default,
                    'next_word': next_word,
                    'sandhi_pred': sandhi_pred,
                    'sandhi_match': sandhi_match,
                })
            else:
                # Word doesn't end in n/l/r
                ending = word[-1] if word else '?'
                analysis.append({
                    'word': word,
                    'stem': word,
                    'suffix': None,
                    'stem_final': '?',
                    'expected': None,
                    'is_default': None,
                    'next_word': next_word if idx + 1 < len(line_words) else None,
                    'sandhi_pred': None,
                    'sandhi_match': f'-{ending} ending',
                })

        # Print analysis
        for a in analysis:
            if a['suffix']:
                nw = a.get('next_word') or 'EOL'
                print(f"  {a['word']:>15}  stem={a['stem']:>10}  -{a['suffix']}  "
                      f"(stem-final={a['stem_final']}, expected=-{a['expected']})  "
                      f"next={nw:>10}  {a['sandhi_match']}")
            else:
                print(f"  {a['word']:>15}  [no n/l/r suffix]  {a['sandhi_match']}")

        # Group by stem (collapse sandhi variants)
        stems_in_line = []
        for a in analysis:
            stems_in_line.append(a['stem'])
        print(f"  Stems: {' '.join(stems_in_line)}")


def main():
    filepath = "C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt"
    words = load_words(filepath)
    print(f"Loaded {len(words)} word tokens from transcription")

    chol_next, chor_next = analyze_chol_vs_chor(words)
    results = analyze_all_nlr_pairs(words)
    stem_map, nlr_stems, surface_vocab = count_unique_stems(words)
    analyze_y_endings(words)
    sentence_level_reading(words)


if __name__ == '__main__':
    main()
