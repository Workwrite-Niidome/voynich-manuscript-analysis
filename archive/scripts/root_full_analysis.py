#!/usr/bin/env python3
"""
Complete root morpheme analysis for the Voynich manuscript.
Analyzes all ~10 core consonant roots across all dimensions.
"""

import re
from collections import defaultdict, Counter

# Read the transcription
with open(r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Parse folio structure
folio_words = {}
current_folio = None
all_words = []
folio_sections = {}

def classify_folio(folio):
    f = folio.lower().replace('f','')
    num_match = re.match(r'(\d+)', f)
    if not num_match:
        return 'unknown'
    num = int(num_match.group(1))
    if num <= 57:
        return 'herbal'
    elif num <= 67:
        return 'pharma'
    elif num <= 73:
        return 'astro'
    elif num <= 84:
        return 'bio'
    elif num <= 86:
        return 'cosmo'
    elif num <= 98:
        return 'stars'
    elif num <= 116:
        return 'recipe'
    else:
        return 'other'

for line in lines:
    line = line.strip()
    folio_match = re.match(r'<(f\d+[rv]\d?)>', line)
    if folio_match:
        current_folio = folio_match.group(1)
        if current_folio not in folio_words:
            folio_words[current_folio] = []
            folio_sections[current_folio] = classify_folio(current_folio)
        continue

    line_match = re.match(r'<[^>]+>\s+(.*)', line)
    if line_match and current_folio:
        text = line_match.group(1)
        text = re.sub(r'\{[^}]*\}', '', text)
        text = re.sub(r'@\d+;?', '', text)
        text = re.sub(r'<[^>]*>', '', text)
        text = re.sub(r"['\?\*!,]", '', text)
        words = re.split(r'[\s.]+', text)
        words = [w.strip() for w in words if w.strip() and len(w.strip()) > 0]
        folio_words[current_folio].extend(words)
        for w in words:
            all_words.append((w, current_folio))

print(f"Total words extracted: {len(all_words)}")
print(f"Total folios: {len(folio_words)}")
print(f"Sections: {Counter(folio_sections.values())}")
print()

# Root detection - find which root consonant cluster a word contains
# Check longest patterns first to avoid substring false matches
def find_roots_in_word(word):
    found = set()
    w = word

    # 3-char roots (check first)
    if 'ckh' in w:
        found.add('ckh')
    if 'cth' in w:
        found.add('cth')
    # tch - but not cth (already caught)
    for m in re.finditer(r'tch', w):
        pos = m.start()
        if pos > 0 and w[pos-1] == 'c':
            continue  # part of cth+ch overlap
        found.add('tch')
    # kch
    if 'kch' in w:
        found.add('kch')
    if 'pch' in w:
        found.add('pch')
    if 'lch' in w:
        found.add('lch')
    if 'lsh' in w:
        found.add('lsh')
    if 'cph' in w or 'cfh' in w:
        found.add('cph')

    # 2-char roots
    # lk - not part of lkch etc
    if 'lk' in w and 'lkch' not in w:
        found.add('lk')

    # ch - standalone (not part of kch, tch, pch, lch, ckh, cth)
    for m in re.finditer(r'ch', w):
        pos = m.start()
        # Check if part of a longer root
        if pos > 0 and w[pos-1] in 'ktpl':
            continue  # kch, tch, pch, lch
        if pos > 0 and w[pos-1] == 'c':
            # Could be cch or part of something
            continue
        if pos + 2 < len(w) and w[pos+2] == 'k':
            # Could be ckh variant
            pass
        found.add('ch')

    # sh - standalone (not part of lsh)
    for m in re.finditer(r'sh', w):
        pos = m.start()
        if pos > 0 and w[pos-1] == 'l':
            continue  # lsh
        found.add('sh')

    # k - standalone
    for m in re.finditer(r'k', w):
        pos = m.start()
        end = m.end()
        # Skip if part of ck, lk, kch
        if pos > 0 and w[pos-1] in 'cl':
            continue
        if end < len(w) and w[end] == 'c':
            continue  # kch, kch
        if end < len(w) and w[end] == 'h':
            continue  # kh (part of ckh)
        found.add('k')

    # t - standalone
    for m in re.finditer(r't', w):
        pos = m.start()
        end = m.end()
        if pos > 0 and w[pos-1] == 'c':
            continue  # ct (part of cth)
        if end < len(w) and w[end] == 'c':
            continue  # tch
        if end < len(w) and w[end] == 'h':
            continue
        found.add('t')

    # l - standalone
    for m in re.finditer(r'l', w):
        pos = m.start()
        end = m.end()
        if end < len(w) and w[end] in 'kcs':
            continue  # lk, lch, lsh
        found.add('l')

    # r
    if 'r' in w:
        found.add('r')

    # p - standalone
    for m in re.finditer(r'p', w):
        pos = m.start()
        end = m.end()
        if pos > 0 and w[pos-1] == 'c':
            continue  # cph
        if end < len(w) and w[end] == 'c':
            continue  # pch
        if end < len(w) and w[end] == 'h':
            continue
        found.add('p')

    return found

# Prefix detection
def find_prefix(word):
    if word.startswith('qo'):
        return 'qo'
    elif word.startswith('ot'):
        return 'ot'
    elif word.startswith('ok'):
        return 'ok'
    elif word.startswith('ol'):
        return 'ol'
    elif word.startswith('do') or word.startswith('da') or (word.startswith('d') and len(word) > 1 and word[1] not in 'aeiouy'):
        return 'd'
    elif word.startswith('sh') and len(word) > 3:
        return 'sh'
    elif word.startswith('ch') and len(word) > 3:
        return 'ch'
    elif word.startswith('s') and not word.startswith('sh'):
        return 's'
    elif word.startswith('y'):
        return 'y'
    elif word.startswith('o') and not word.startswith('ot') and not word.startswith('ok') and not word.startswith('ol'):
        return 'o'
    elif word.startswith('p'):
        return 'p'
    else:
        return 'none'

# Count everything
root_freq = Counter()
root_section = defaultdict(Counter)
root_folio_set = defaultdict(set)
root_prefix_dist = defaultdict(Counter)
root_words_examples = defaultdict(Counter)
root_grade = defaultdict(Counter)
root_cooccur = defaultdict(Counter)

for word, folio in all_words:
    if len(word) < 2:
        continue

    roots = find_roots_in_word(word)
    section = folio_sections.get(folio, 'unknown')
    prefix = find_prefix(word)

    # Grade
    if 'eeod' in word:
        grade = 'eod'
    elif 'eod' in word:
        grade = 'eod'
    elif 'eeo' in word:
        grade = 'eeo'
    elif 'ee' in word:
        grade = 'ee'
    elif 'eo' in word:
        grade = 'eo'
    else:
        grade = 'bare/e'

    for root in roots:
        root_freq[root] += 1
        root_section[root][section] += 1
        root_folio_set[root].add(folio)
        root_prefix_dist[root][prefix] += 1
        root_words_examples[root][word] += 1
        root_grade[root][grade] += 1

    root_list = list(roots)
    for i in range(len(root_list)):
        for j in range(i+1, len(root_list)):
            root_cooccur[root_list[i]][root_list[j]] += 1
            root_cooccur[root_list[j]][root_list[i]] += 1

# ============ OUTPUT ============

print("=" * 80)
print("ROOT FREQUENCY TABLE (sorted by frequency)")
print("=" * 80)
print(f"{'Root':<8} {'Freq':>7} {'Folios':>7} {'TopSection':>12} {'%':>5} {'TopPrefix':>10} {'%':>5}")
print("-" * 60)

for root, freq in root_freq.most_common():
    sections = root_section[root]
    top_sec = sections.most_common(1)[0]
    sec_pct = top_sec[1] / freq * 100
    prefixes = root_prefix_dist[root]
    top_pre = prefixes.most_common(1)[0]
    pre_pct = top_pre[1] / freq * 100
    n_folios = len(root_folio_set[root])
    print(f"{root:<8} {freq:>7} {n_folios:>7} {top_sec[0]:>12} {sec_pct:>4.0f}% {top_pre[0]:>10} {pre_pct:>4.0f}%")

print()
print("=" * 80)
print("SECTION DISTRIBUTION FOR EACH ROOT")
print("=" * 80)

for root, freq in root_freq.most_common(15):
    sections = root_section[root]
    total = sum(sections.values())
    print(f"\n{root} (total={total}):")
    for sec in ['herbal','pharma','astro','bio','cosmo','stars','recipe','other','unknown']:
        cnt = sections.get(sec, 0)
        if cnt > 0:
            pct = cnt / total * 100
            bar = '#' * int(pct / 2)
            print(f"  {sec:>10}: {cnt:>5} ({pct:>5.1f}%) {bar}")

print()
print("=" * 80)
print("PREFIX DISTRIBUTION FOR EACH ROOT")
print("=" * 80)

for root, freq in root_freq.most_common(15):
    prefixes = root_prefix_dist[root]
    total = sum(prefixes.values())
    print(f"\n{root} (total={total}):")
    for pre, cnt in prefixes.most_common(8):
        pct = cnt / total * 100
        print(f"  {pre:>10}: {cnt:>5} ({pct:>5.1f}%)")

print()
print("=" * 80)
print("GRADE DISTRIBUTION PER ROOT")
print("=" * 80)

print(f"\n{'Root':<8} {'bare/e':>8} {'ee':>8} {'eo':>8} {'eeo':>8} {'eod':>8}")
print("-" * 50)
for root, freq in root_freq.most_common(15):
    grades = root_grade[root]
    bare = grades.get('bare/e', 0)
    ee = grades.get('ee', 0)
    eo = grades.get('eo', 0)
    eeo = grades.get('eeo', 0)
    eod = grades.get('eod', 0)
    print(f"{root:<8} {bare:>8} {ee:>8} {eo:>8} {eeo:>8} {eod:>8}")

print()
print("=" * 80)
print("TOP 10 WORDS FOR EACH ROOT")
print("=" * 80)

for root, freq in root_freq.most_common(15):
    print(f"\n{root} ({freq} total):")
    for word, cnt in root_words_examples[root].most_common(10):
        print(f"  {word:>25}: {cnt:>5}")

print()
print("=" * 80)
print("CO-OCCURRENCE (roots in same word)")
print("=" * 80)

top_roots = [r for r, _ in root_freq.most_common(12)]
header = f"{'':>8}"
for r in top_roots:
    header += f" {r:>6}"
print(header)

for r1 in top_roots:
    row = f"{r1:>8}"
    for r2 in top_roots:
        if r1 == r2:
            row += "     -"
        else:
            cnt = root_cooccur[r1].get(r2, 0)
            row += f" {cnt:>6}"
    print(row)

# LINE POSITION
print()
print("=" * 80)
print("LINE POSITION ANALYSIS")
print("=" * 80)

root_line_pos = defaultdict(list)

for line_raw in lines:
    line_raw = line_raw.strip()
    line_match = re.match(r'<[^>]+>\s+(.*)', line_raw)
    if not line_match:
        continue
    text = line_match.group(1)
    text = re.sub(r'\{[^}]*\}', '', text)
    text = re.sub(r'@\d+;?', '', text)
    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r"['\?\*!,]", '', text)
    words = re.split(r'[\s.]+', text)
    words = [w.strip() for w in words if w.strip()]

    if len(words) < 2:
        continue

    for idx, w in enumerate(words):
        pos_frac = idx / (len(words) - 1)
        roots = find_roots_in_word(w)
        for root in roots:
            root_line_pos[root].append(pos_frac)

print(f"\n{'Root':<8} {'MeanPos':>8} {'Start%':>8} {'Mid%':>8} {'End%':>8}")
print("-" * 45)
for root, freq in root_freq.most_common(15):
    positions = root_line_pos.get(root, [])
    if not positions:
        continue
    mean_pos = sum(positions) / len(positions)
    start = sum(1 for p in positions if p < 0.2) / len(positions) * 100
    mid = sum(1 for p in positions if 0.2 <= p <= 0.8) / len(positions) * 100
    end = sum(1 for p in positions if p > 0.8) / len(positions) * 100
    print(f"{root:<8} {mean_pos:>8.3f} {start:>7.1f}% {mid:>7.1f}% {end:>7.1f}%")

# ADJACENT WORD ANALYSIS
print()
print("=" * 80)
print("ADJACENT WORDS (what typically precedes/follows each root)")
print("=" * 80)

# Build adjacency
root_prev = defaultdict(Counter)
root_next = defaultdict(Counter)

for folio, words_list in folio_words.items():
    for i, w in enumerate(words_list):
        roots = find_roots_in_word(w)
        for root in roots:
            if i > 0:
                root_prev[root][words_list[i-1]] += 1
            if i < len(words_list) - 1:
                root_next[root][words_list[i+1]] += 1

for root, freq in root_freq.most_common(10):
    print(f"\n{root}:")
    print(f"  Preceded by: {', '.join(f'{w}({c})' for w, c in root_prev[root].most_common(5))}")
    print(f"  Followed by: {', '.join(f'{w}({c})' for w, c in root_next[root].most_common(5))}")
