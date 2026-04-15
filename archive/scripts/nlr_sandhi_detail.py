#!/usr/bin/env python3
"""Extended analysis: stems with higher frequency, and cross-line sandhi."""

import re
from collections import Counter, defaultdict

def parse_voynich(filepath):
    lines_data = []
    current_folio = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            folio_match = re.match(r'<(f\d+[rv]\d?)>\s', line)
            if folio_match:
                current_folio = folio_match.group(1)
                continue
            line_match = re.match(r'<(f\d+[rv]\d?)\.(\d+),([^>]+)>\s+(.*)', line)
            if line_match:
                folio = line_match.group(1)
                line_num = int(line_match.group(2))
                line_type = line_match.group(3)
                text = line_match.group(4)
                current_folio = folio
                lines_data.append({
                    'folio': folio, 'line_num': line_num,
                    'line_type': line_type, 'text': text,
                })
    return lines_data

def extract_words(text):
    text = re.sub(r'\{[^}]+\}', '', text)
    text = re.sub(r'@\d+;?', '', text)
    text = re.sub(r'<->', ' ', text)
    text = re.sub(r'[,?.!\'"]', '', text)
    words = re.split(r'[\s.]+', text)
    return [w for w in words if w and re.match(r'^[a-z]+$', w)]

def get_suffix_type(word):
    if word and word[-1] in ('n', 'l', 'r'):
        return word[-1]
    return None

def main():
    filepath = "C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt"
    lines_data = parse_voynich(filepath)

    # Build word list
    all_words = []
    for ld in lines_data:
        words = extract_words(ld['text'])
        for i, w in enumerate(words):
            all_words.append({
                'word': w, 'folio': ld['folio'],
                'line_num': ld['line_num'],
                'is_line_end': (i == len(words) - 1),
                'is_line_start': (i == 0),
            })

    # Instead of single-char stems, look at FULL WORDS ending in n/l/r
    # and find the most common word-families (same prefix, different n/l/r ending)
    # A "stem" = word minus final n/l/r
    stem_words = defaultdict(lambda: Counter())
    for w in all_words:
        s = get_suffix_type(w['word'])
        if s and len(w['word']) > 1:
            stem = w['word'][:-1]
            stem_words[stem][s] += 1

    # Find stems with alternation (appear with at least 2 different suffixes)
    alternating = {}
    for stem, counts in stem_words.items():
        total = sum(counts.values())
        if total >= 10 and len(counts) >= 2:
            alternating[stem] = counts

    print("STEMS WITH ALTERNATION (>=10 occurrences, >=2 suffix types):")
    print(f"{'Stem':>15} {'Total':>6} {'n':>6} {'l':>6} {'r':>6} {'Default':>8}")
    print("-" * 55)

    sorted_stems = sorted(alternating.items(), key=lambda x: sum(x[1].values()), reverse=True)
    for stem, counts in sorted_stems[:30]:
        total = sum(counts.values())
        dominant = counts.most_common(1)[0][0]
        print(f"{stem:>15} {total:>6} {counts.get('n',0):>6} {counts.get('l',0):>6} {counts.get('r',0):>6} {dominant:>8}")

    # Now for the top 10 alternating stems, check sandhi interaction
    print("\n\nSTEM-SANDHI INTERACTION (top alternating stems):")

    # Build bigram data
    sandhi = []
    for i in range(len(all_words) - 1):
        w = all_words[i]
        nw = all_words[i+1]
        s = get_suffix_type(w['word'])
        if s is None or len(w['word']) <= 1:
            continue
        if w['folio'] != nw['folio']:
            continue
        stem = w['word'][:-1]
        next_init = nw['word'][0]
        sandhi.append({'stem': stem, 'suffix': s, 'next_init': next_init})

    for stem, counts in sorted_stems[:10]:
        total = sum(counts.values())
        default = counts.most_common(1)[0][0]
        print(f"\n--- Stem: '{stem}' (default: -{default}, total: {total}) ---")

        # Collect sandhi data for this stem
        stem_sandhi = defaultdict(lambda: Counter())
        for sd in sandhi:
            if sd['stem'] == stem:
                stem_sandhi[sd['next_init']][sd['suffix']] += 1

        # Group by broad class
        vowels = set('aoei')
        stops = set('ktpdgb')
        for init_char in sorted(stem_sandhi.keys(), key=lambda x: sum(stem_sandhi[x].values()), reverse=True):
            sc = stem_sandhi[init_char]
            st = sum(sc.values())
            if st < 2:
                continue
            dom = sc.most_common(1)[0][0]
            override = " *** OVERRIDE" if dom != default else ""
            print(f"  before {init_char}-: n={sc.get('n',0)} l={sc.get('l',0)} r={sc.get('r',0)} (total {st}){override}")

    # Cross-line vs within-line sandhi
    print("\n\nCROSS-LINE vs WITHIN-LINE SANDHI:")
    cross_line = defaultdict(lambda: Counter())
    within_line = defaultdict(lambda: Counter())

    for i in range(len(all_words) - 1):
        w = all_words[i]
        nw = all_words[i+1]
        s = get_suffix_type(w['word'])
        if s is None:
            continue
        if w['folio'] != nw['folio']:
            continue
        next_init = nw['word'][0]

        if w['is_line_end'] and nw['is_line_start']:
            cross_line[next_init][s] += 1
        elif not w['is_line_end']:
            within_line[next_init][s] += 1

    # Compare for key initials
    print(f"\n{'Init':>6} {'Context':>15} {'Total':>6} {'P(n)':>8} {'P(l)':>8} {'P(r)':>8}")
    print("-" * 55)

    for init in ['o', 's', 'd', 'c', 'k', 'p', 'q', 't']:
        for label, data in [('within-line', within_line), ('cross-line', cross_line)]:
            if init in data:
                c = data[init]
                t = sum(c.values())
                if t >= 3:
                    print(f"{init:>6} {label:>15} {t:>6} {c.get('n',0)/t:>8.1%} {c.get('l',0)/t:>8.1%} {c.get('r',0)/t:>8.1%}")

    # Words ending in -n that are NOT "daiin/dain/aiin" etc.
    print("\n\nSUFFIX -n WORDS (most common):")
    n_words = Counter()
    for w in all_words:
        if get_suffix_type(w['word']) == 'n':
            n_words[w['word']] += 1
    for word, count in n_words.most_common(20):
        print(f"  {word}: {count}")

    print("\nSUFFIX -l WORDS (most common):")
    l_words = Counter()
    for w in all_words:
        if get_suffix_type(w['word']) == 'l':
            l_words[w['word']] += 1
    for word, count in l_words.most_common(20):
        print(f"  {word}: {count}")

    print("\nSUFFIX -r WORDS (most common):")
    r_words = Counter()
    for w in all_words:
        if get_suffix_type(w['word']) == 'r':
            r_words[w['word']] += 1
    for word, count in r_words.most_common(20):
        print(f"  {word}: {count}")

if __name__ == '__main__':
    main()
