#!/usr/bin/env python3
"""
Final supplementary: paradigmatic structure and Llullian compatibility.
"""
import re
from collections import Counter, defaultdict

def parse_eva(filepath):
    folios = {}
    current_folio = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            folio_match = re.match(r'<(f\d+[rv]\d?)>', line)
            if folio_match:
                current_folio = folio_match.group(1)
                folios[current_folio] = []
                continue
            line_match = re.match(r'<(f\d+[rv]\d?)\.(\d+),', line)
            if line_match:
                current_folio = line_match.group(1)
                if current_folio not in folios:
                    folios[current_folio] = []
                text_start = line.find('>')
                if text_start >= 0:
                    text = line[text_start+1:].strip()
                    text = re.sub(r'@\d+;?', '', text)
                    text = re.sub(r'\{[^}]*\}', '', text)
                    text = re.sub(r'[<>]', '', text)
                    words = re.split(r'[.\s,?!]+', text)
                    words = [w.strip() for w in words if w.strip()]
                    folios[current_folio].extend(words)
    return folios

folios = parse_eva(r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt')

all_words = []
for words in folios.values():
    all_words.extend(words)

# Count the most common words
word_freq = Counter(all_words)
print("TOP 30 MOST COMMON WORDS:")
for w, c in word_freq.most_common(30):
    print(f"  {w:<20} {c:>5}")

# Check if top words show prefix+root+suffix structure
print()
print("PARADIGMATIC ANALYSIS OF TOP WORDS:")
print("Do common words form prefix x suffix paradigms?")
print()

# Group words by stripping first 2-3 chars and last char
# to find "root" clusters
root_clusters = defaultdict(list)
for w, c in word_freq.items():
    if len(w) < 3 or c < 5:
        continue
    # Try stripping ch/sh/d prefix and n/l/r/y suffix
    core = w
    prefix = ''
    for pfx in ['cth', 'ckh', 'cph', 'cfh', 'ch', 'sh', 'qo', 'ok', 'ot']:
        if core.startswith(pfx):
            prefix = pfx
            core = core[len(pfx):]
            break
    suffix = ''
    if core and core[-1] in 'nlry' and len(core) > 1:
        suffix = core[-1]
        core = core[:-1]

    if len(core) >= 2:
        root_clusters[core].append((w, prefix, suffix, c))

# Show clusters with multiple prefix/suffix variants
print(f"{'Root':<10} {'Variants (prefix-root-suffix x count)'}")
print("-" * 70)
paradigm_count = 0
for root in sorted(root_clusters.keys(), key=lambda r: sum(x[3] for x in root_clusters[r]), reverse=True):
    entries = root_clusters[root]
    if len(entries) < 4:
        continue
    # Check if multiple prefixes exist
    prefixes = set(e[1] for e in entries)
    suffixes = set(e[2] for e in entries)
    if len(prefixes) < 2 and len(suffixes) < 2:
        continue

    total = sum(e[3] for e in entries)
    variants = ', '.join(f"{e[0]}({e[3]})" for e in sorted(entries, key=lambda x: -x[3])[:8])
    print(f"{root:<10} [{len(entries)} variants, {len(prefixes)} pfx, {len(suffixes)} sfx] {variants}")
    paradigm_count += 1
    if paradigm_count >= 25:
        break

# The key question: is the "ol" root truly combining with prefixes?
print()
print("DETAILED: 'ol' root paradigm")
ol_words = [(w, c) for w, c in word_freq.items() if re.match(r'^(ch|sh|d|cth|ok|qo|ot|k|s)ol$', w)]
ol_words.sort(key=lambda x: -x[1])
print(f"  Words matching [prefix]ol: {len(ol_words)}")
for w, c in ol_words:
    print(f"    {w}: {c}")

print()
print("DETAILED: 'ai' / 'aiin' root paradigm")
aiin_words = [(w, c) for w, c in word_freq.items() if re.match(r'^(ch|sh|d|cth|ok|qo|ot|k|s)aiin$', w)]
aiin_words.sort(key=lambda x: -x[1])
print(f"  Words matching [prefix]aiin: {len(aiin_words)}")
for w, c in aiin_words:
    print(f"    {w}: {c}")

print()
print("DETAILED: 'ey' root paradigm")
ey_words = [(w, c) for w, c in word_freq.items() if re.match(r'^(ch|sh|d|cth|ok|qo|ot|k|s)e+y$', w)]
ey_words.sort(key=lambda x: -x[1])
print(f"  Words matching [prefix]e+y: {len(ey_words)}")
for w, c in ey_words:
    print(f"    {w}: {c}")

# Check: if Galenic, then the same root+suffix should appear more on
# specific folios (= specific substance). Does 'ol' cluster?
print()
print("FOLIO DISTRIBUTION OF 'chol' vs 'shol':")
for target in ['chol', 'shol']:
    folio_counts = []
    for folio, words in folios.items():
        c = words.count(target)
        if c > 0:
            folio_counts.append((folio, c))
    folio_counts.sort(key=lambda x: -x[1])
    print(f"  {target}: appears on {len(folio_counts)} folios, total {sum(c for _, c in folio_counts)}")
    print(f"    Top folios: {', '.join(f'{f}({c})' for f, c in folio_counts[:10])}")
