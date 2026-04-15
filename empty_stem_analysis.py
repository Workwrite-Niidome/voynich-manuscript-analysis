#!/usr/bin/env python3
"""
Comprehensive analysis of empty-stem words in the Voynich manuscript.
Empty-stem = prefix + suffix with nothing in between.
"""

import re
from collections import defaultdict, Counter

# Known prefixes (from morphological analysis)
PREFIXES = [
    'qo', 'o', 'd', 's', 'ch', 'sh', 'k', 'ct', 'cth', 'ck', 'cfh', 'cph',
    'ot', 'ok', 'y', 'p', 't', 'q'
]

# Known suffixes
SUFFIXES = [
    'aiin', 'aiiin', 'ain', 'ar', 'al', 'ol', 'or', 'am', 'an',
    'y', 'ey', 'eey', 'eeey', 'dy', 'chy', 'shy',
    'airy', 'air', 'ary',
    'l', 'r', 'n', 'm',
    'os', 'es', 'is',
    'on', 'om'
]

# Sort prefixes longest first to avoid partial matches
PREFIXES_SORTED = sorted(PREFIXES, key=len, reverse=True)
SUFFIXES_SORTED = sorted(SUFFIXES, key=len, reverse=True)


def parse_voynich_file(filepath):
    """Parse the EVA transcription file, returning list of (folio, line_num, word, line_position, total_words_in_line)."""
    words_data = []
    current_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            # Track folio changes
            folio_match = re.match(r'<(f\d+[rv]\d*|f\d+[rv])>', line)
            if folio_match:
                current_folio = folio_match.group(1)
                continue

            # Parse content lines
            content_match = re.match(r'<(f\d+[rv]\d*)\.\d+', line)
            if not content_match:
                continue

            current_folio = content_match.group(1)

            # Extract the text after the tag
            text_match = re.search(r'>\s+(.+)$', line)
            if not text_match:
                continue

            text = text_match.group(1)

            # Remove annotations like @221; @152; etc
            text = re.sub(r'@\d+;?', '', text)
            # Remove {cto} {ct} {ch'} etc
            text = re.sub(r'\{[^}]+\}', '', text)
            # Remove ? , ' and other noise
            text = re.sub(r'[?,\']', '', text)
            # Split on delimiters
            tokens = re.split(r'[\s.<>\-]+', text)
            tokens = [t for t in tokens if t and len(t) > 0 and not t.startswith('#') and not t.startswith('$')]

            for pos, word in enumerate(tokens):
                # Clean word further
                word = word.strip()
                if not word or not re.match(r'^[a-z]+$', word):
                    continue
                words_data.append({
                    'folio': current_folio,
                    'word': word,
                    'line_position': pos,
                    'total_in_line': len(tokens),
                    'is_line_start': pos == 0,
                    'is_line_end': pos == len(tokens) - 1,
                    'relative_position': pos / max(len(tokens) - 1, 1)
                })

    return words_data


def get_section(folio):
    """Determine manuscript section from folio number."""
    if not folio:
        return 'unknown'

    # Extract folio number
    m = re.match(r'f(\d+)', folio)
    if not m:
        return 'unknown'
    num = int(m.group(1))

    if num <= 56:
        return 'herbal'
    elif num <= 67:
        return 'astronomical'
    elif num <= 73:
        return 'biological'
    elif num <= 84:
        return 'cosmological'
    elif num <= 86:
        return 'pharmaceutical'
    elif num <= 116:
        return 'recipe'  # "stars" section, often recipe-like
    else:
        return 'recipe'


def is_empty_stem(word):
    """Check if a word is prefix+suffix with no stem in between.
    Returns (prefix, suffix) if empty-stem, else None."""

    results = []

    for prefix in PREFIXES_SORTED:
        if word.startswith(prefix):
            remainder = word[len(prefix):]
            if not remainder:
                continue
            for suffix in SUFFIXES_SORTED:
                if remainder == suffix:
                    results.append((prefix, suffix))

    # Also check bare suffixes (no prefix)
    for suffix in SUFFIXES_SORTED:
        if word == suffix and len(word) > 1:
            results.append(('', suffix))

    if results:
        # Return the decomposition with longest prefix
        results.sort(key=lambda x: len(x[0]), reverse=True)
        return results[0]

    return None


def analyze_collocations(words_data, target_word, window=2):
    """Analyze what words appear near a target word."""
    neighbors_before = Counter()
    neighbors_after = Counter()

    word_list = [w['word'] for w in words_data]

    for i, w in enumerate(word_list):
        if w == target_word:
            for j in range(max(0, i-window), i):
                neighbors_before[word_list[j]] += 1
            for j in range(i+1, min(len(word_list), i+window+1)):
                neighbors_after[word_list[j]] += 1

    return neighbors_before, neighbors_after


def main():
    filepath = r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt'
    words_data = parse_voynich_file(filepath)

    print(f"Total word tokens parsed: {len(words_data)}")

    # Count all unique words
    all_words = Counter(w['word'] for w in words_data)
    print(f"Unique word types: {len(all_words)}")

    # Find all empty-stem words
    empty_stem_words = {}
    for word, count in all_words.items():
        decomp = is_empty_stem(word)
        if decomp:
            empty_stem_words[word] = {
                'count': count,
                'prefix': decomp[0],
                'suffix': decomp[1],
                'decomposition': f"{decomp[0]}+{decomp[1]}" if decomp[0] else f"(bare){decomp[1]}"
            }

    # Sort by frequency
    sorted_empty = sorted(empty_stem_words.items(), key=lambda x: x[1]['count'], reverse=True)

    print(f"\n{'='*80}")
    print(f"EMPTY-STEM WORDS: {len(sorted_empty)} types, {sum(v['count'] for v in empty_stem_words.values())} tokens")
    print(f"{'='*80}")

    total_tokens = len(words_data)
    empty_tokens = sum(v['count'] for v in empty_stem_words.values())
    print(f"Empty-stem tokens as % of corpus: {empty_tokens/total_tokens*100:.1f}%")

    # Section distribution for each empty-stem word
    section_counts = defaultdict(lambda: defaultdict(int))
    position_data = defaultdict(list)
    line_start_counts = defaultdict(int)
    line_end_counts = defaultdict(int)

    for w in words_data:
        word = w['word']
        if word in empty_stem_words:
            section = get_section(w['folio'])
            section_counts[word][section] += 1
            position_data[word].append(w['relative_position'])
            if w['is_line_start']:
                line_start_counts[word] += 1
            if w['is_line_end']:
                line_end_counts[word] += 1

    # Print detailed table
    print(f"\n{'Word':<12} {'Freq':>5} {'Decomp':<15} {'Herbal':>7} {'Astro':>7} {'Bio':>7} {'Cosmo':>7} {'Pharma':>7} {'Recipe':>7} {'LineStart%':>10} {'AvgPos':>7}")
    print('-' * 110)

    for word, info in sorted_empty:
        sections = section_counts[word]
        positions = position_data[word]
        avg_pos = sum(positions) / len(positions) if positions else 0
        ls_pct = line_start_counts[word] / info['count'] * 100 if info['count'] > 0 else 0

        print(f"{word:<12} {info['count']:>5} {info['decomposition']:<15} "
              f"{sections.get('herbal',0):>7} {sections.get('astronomical',0):>7} "
              f"{sections.get('biological',0):>7} {sections.get('cosmological',0):>7} "
              f"{sections.get('pharmaceutical',0):>7} {sections.get('recipe',0):>7} "
              f"{ls_pct:>9.1f}% {avg_pos:>6.2f}")

    # Top 20 collocations analysis
    print(f"\n{'='*80}")
    print("COLLOCATION ANALYSIS (top 15 empty-stem words)")
    print(f"{'='*80}")

    for word, info in sorted_empty[:15]:
        before, after = analyze_collocations(words_data, word, window=1)
        print(f"\n--- {word} (freq={info['count']}, {info['decomposition']}) ---")
        print(f"  Preceding words:  {', '.join(f'{w}({c})' for w,c in before.most_common(8))}")
        print(f"  Following words:  {', '.join(f'{w}({c})' for w,c in after.most_common(8))}")

    # Syntactic position analysis
    print(f"\n{'='*80}")
    print("SYNTACTIC POSITION CLUSTERS")
    print(f"{'='*80}")

    # Group by position tendency
    line_initial = []  # >30% line-start
    line_final = []    # >20% line-end
    mid_line = []      # avg position 0.3-0.7, low line-start/end
    pre_content = []   # avg position < 0.3, not line-initial

    for word, info in sorted_empty:
        if info['count'] < 5:
            continue
        ls_pct = line_start_counts[word] / info['count'] * 100
        le_pct = line_end_counts[word] / info['count'] * 100
        positions = position_data[word]
        avg_pos = sum(positions) / len(positions) if positions else 0

        if ls_pct > 25:
            line_initial.append((word, info['count'], ls_pct))
        elif le_pct > 20:
            line_final.append((word, info['count'], le_pct))
        elif 0.3 <= avg_pos <= 0.7:
            mid_line.append((word, info['count'], avg_pos))
        else:
            pre_content.append((word, info['count'], avg_pos))

    print(f"\nLINE-INITIAL (>25% at line start) - likely articles/demonstratives:")
    for w, c, pct in sorted(line_initial, key=lambda x: x[2], reverse=True):
        print(f"  {w:<12} freq={c:>4}  line-start={pct:.1f}%")

    print(f"\nLINE-FINAL (>20% at line end) - likely verbs/copulas:")
    for w, c, pct in sorted(line_final, key=lambda x: x[2], reverse=True):
        print(f"  {w:<12} freq={c:>4}  line-end={pct:.1f}%")

    print(f"\nMID-LINE (avg pos 0.3-0.7) - likely conjunctions/copulas:")
    for w, c, pos in sorted(mid_line, key=lambda x: x[1], reverse=True):
        print(f"  {w:<12} freq={c:>4}  avg_pos={pos:.2f}")

    print(f"\nPRE-CONTENT (avg pos < 0.3, not line-initial) - likely prepositions:")
    for w, c, pos in sorted(pre_content, key=lambda x: x[1], reverse=True):
        print(f"  {w:<12} freq={c:>4}  avg_pos={pos:.2f}")

    # Section variation analysis
    print(f"\n{'='*80}")
    print("SECTION DISTRIBUTION ANALYSIS")
    print(f"{'='*80}")

    # Calculate section totals
    section_totals = defaultdict(int)
    for w in words_data:
        section_totals[get_section(w['folio'])] += 1

    print(f"\nSection totals: {dict(section_totals)}")

    # For each word, compute normalized section distribution
    print(f"\n{'Word':<12} {'Freq':>5}  Distribution (normalized to per-1000-words-in-section)")
    print('-' * 90)

    for word, info in sorted_empty[:30]:
        if info['count'] < 10:
            continue
        sections = section_counts[word]
        norm = {}
        for sec in ['herbal', 'astronomical', 'biological', 'cosmological', 'pharmaceutical', 'recipe']:
            if section_totals[sec] > 0:
                norm[sec] = sections.get(sec, 0) / section_totals[sec] * 1000
            else:
                norm[sec] = 0

        # Compute coefficient of variation
        values = [v for v in norm.values() if v > 0]
        if values:
            mean_v = sum(values) / len(values)
            variance = sum((v - mean_v)**2 for v in values) / len(values)
            cv = (variance ** 0.5) / mean_v if mean_v > 0 else 0
        else:
            cv = 0

        dist_str = ' '.join(f"{sec[:4]}={norm[sec]:5.1f}" for sec in ['herbal', 'astronomical', 'biological', 'cosmological', 'pharmaceutical', 'recipe'])
        uniformity = "UNIFORM" if cv < 0.4 else "VARIABLE" if cv < 0.8 else "CONCENTRATED"
        print(f"{word:<12} {info['count']:>5}  {dist_str}  [{uniformity}, CV={cv:.2f}]")

    # Frequency ranking and Latin mapping
    print(f"\n{'='*80}")
    print("FREQUENCY RANK -> LATIN FUNCTION WORD MAPPING")
    print(f"{'='*80}")

    print(f"\nTop 10 Latin pharmaceutical function words: et, in, de, ad, cum, est, per, quod, hic, sed")
    print(f"\nTop 10 empty-stem Voynich words by frequency:")
    for i, (word, info) in enumerate(sorted_empty[:10]):
        sections = section_counts[word]
        ls_pct = line_start_counts[word] / info['count'] * 100
        positions = position_data[word]
        avg_pos = sum(positions) / len(positions) if positions else 0

        print(f"  {i+1}. {word:<12} freq={info['count']:>4}  {info['decomposition']:<12}  "
              f"line-start={ls_pct:.0f}%  avg_pos={avg_pos:.2f}")

    # Next-word analysis for preposition detection
    print(f"\n{'='*80}")
    print("PREPOSITION TEST: Does word precede content words?")
    print(f"{'='*80}")

    # Content words = non-empty-stem words with freq > 5
    content_words = set(w for w, c in all_words.items() if c > 5 and w not in empty_stem_words)

    for word, info in sorted_empty[:15]:
        if info['count'] < 10:
            continue
        before, after = analyze_collocations(words_data, word, window=1)

        content_after = sum(c for w, c in after.items() if w in content_words)
        func_after = sum(c for w, c in after.items() if w in empty_stem_words)
        total_after = content_after + func_after

        content_before = sum(c for w, c in before.items() if w in content_words)
        func_before = sum(c for w, c in before.items() if w in empty_stem_words)

        if total_after > 0:
            content_pct = content_after / total_after * 100
        else:
            content_pct = 0

        print(f"  {word:<12} content_after={content_pct:.0f}%  "
              f"(content={content_after}, func={func_after})")


if __name__ == '__main__':
    main()
