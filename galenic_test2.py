#!/usr/bin/env python3
"""
Supplementary tests for Galenic hypothesis.
Focus on: suffix-degree prediction accuracy and ch/sh ratio normalization.
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

def classify_prefix(word):
    w = word.lower().strip()
    if not w:
        return None
    if w.startswith('cth'): return 'cth'
    if w.startswith('ckh'): return 'ckh'
    if w.startswith('cph'): return 'cph'
    if w.startswith('cfh'): return 'cfh'
    if w.startswith('ch'): return 'ch'
    if w.startswith('sh'): return 'sh'
    if w.startswith('d'): return 'd'
    if w.startswith('s') and not w.startswith('sh'): return 's'
    if w.startswith('q'): return 'q'
    if w.startswith('o'): return 'o'
    if w.startswith('k'): return 'k'
    if w.startswith('t'): return 't'
    if w.startswith('p'): return 'p'
    if w.startswith('y'): return 'y'
    return 'other'

folios = parse_eva(r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt')

# Compute global ch/sh ratio as baseline
all_words = []
for words in folios.values():
    all_words.extend(words)

global_ch = sum(1 for w in all_words if classify_prefix(w) == 'ch')
global_sh = sum(1 for w in all_words if classify_prefix(w) == 'sh')
global_ratio = global_ch / global_sh if global_sh > 0 else 999
print(f"Global ch/sh ratio: {global_ch}/{global_sh} = {global_ratio:.2f}")
print(f"ch- is {global_ratio:.1f}x more common than sh- globally")
print()

# This means ch>sh is the DEFAULT. We need to check if hot plants have
# HIGHER ch/sh ratio than cold plants.

plants = {
    'f2r': ('Paeonia', 'Hot', 1),
    'f3r': ('Rubia', 'Hot', 2),
    'f9r': ('Nigella', 'Hot', 3),
    'f1r': ('Laurus', 'Hot', 2),
    'f4r': ('Rosmarinus', 'Hot', 2),
    'f41r': ('Adiantum', 'Cold', 2),
    'f47r': ('Vitis', 'Cold', 1),
}

print("NORMALIZED ch/sh RATIO TEST")
print("If ch=hot, hot plants should have ABOVE-average ch/sh ratio")
print("If sh=cold, cold plants should have BELOW-average ch/sh ratio")
print()
print(f"{'Folio':<8} {'Plant':<15} {'Quality':<8} {'ch':>5} {'sh':>5} {'ratio':>8} {'vs avg':>10}")
print("-" * 65)

hot_ratios = []
cold_ratios = []

for folio, (name, quality, degree) in sorted(plants.items()):
    words = folios.get(folio, [])
    ch = sum(1 for w in words if classify_prefix(w) == 'ch')
    sh = sum(1 for w in words if classify_prefix(w) == 'sh')
    ratio = ch / sh if sh > 0 else float('inf')
    vs_avg = ratio / global_ratio if global_ratio > 0 else 0

    marker = "ABOVE" if vs_avg > 1.0 else "BELOW"
    expected = "ABOVE" if quality == "Hot" else "BELOW"
    correct = marker == expected

    if quality == "Hot":
        hot_ratios.append(ratio)
    else:
        cold_ratios.append(ratio)

    print(f"{folio:<8} {name:<15} {quality:<8} {ch:>5} {sh:>5} {ratio:>7.2f}  {vs_avg:>6.2f}x {'OK' if correct else 'WRONG'}")

print()
avg_hot = sum(hot_ratios) / len(hot_ratios) if hot_ratios else 0
avg_cold = sum(cold_ratios) / len(cold_ratios) if cold_ratios else 0
print(f"Average ch/sh ratio for Hot plants: {avg_hot:.2f}")
print(f"Average ch/sh ratio for Cold plants: {avg_cold:.2f}")
print(f"Global average: {global_ratio:.2f}")

if avg_hot > avg_cold:
    print("-> Hot plants DO have higher ch/sh ratio than Cold plants")
else:
    print("-> Hot plants do NOT have higher ch/sh ratio -> AGAINST hypothesis")

# Suffix-degree accuracy check
print()
print("=" * 65)
print("SUFFIX-DEGREE PREDICTION (most common suffix for ch- words)")
print("=" * 65)
print()
print("If n=1st, l=2nd, r=3rd, y=4th degree:")
print()

degree_map = {1: 'n', 2: 'l', 3: 'r', 4: 'y'}
correct_count = 0
total_count = 0

for folio, (name, quality, degree) in sorted(plants.items()):
    words = folios.get(folio, [])
    ch_words = [w for w in words if classify_prefix(w) == 'ch']
    if len(ch_words) < 5:
        continue

    suffixes = Counter(w[-1] for w in ch_words if w)
    # Only consider n,l,r,y
    nlry = {s: suffixes.get(s, 0) for s in ['n', 'l', 'r', 'y']}
    most_common_nlry = max(nlry, key=nlry.get)
    expected = degree_map[degree]
    correct = most_common_nlry == expected
    if correct:
        correct_count += 1
    total_count += 1

    dist_str = ', '.join(f"{s}:{nlry[s]}" for s in ['n', 'l', 'r', 'y'])
    print(f"  {folio} {name:<15} degree={degree} expected=-{expected}  "
          f"actual top=-{most_common_nlry}  [{dist_str}]  {'MATCH' if correct else 'miss'}")

print(f"\nSuffix-degree prediction: {correct_count}/{total_count}")

# Special: Rubia f3r shows l as top suffix for ch-words, and degree is 2
# That would be a match for l=2nd degree!
print()
print("NOTABLE: f3r (Rubia, Hot 2nd degree) ch-words top suffix is -l")
print("  If l = 2nd degree, this is a PERFECT match")
print("  But this could be coincidence given the small sample")

# Check if -y dominance is just because 'y' is a word-final default
print()
print("=" * 65)
print("IS -y A DEFAULT ENDING OR MEANINGFUL?")
print("=" * 65)
print()

# Check: does -y appear more in certain positions?
# If -y is 4th degree, it should NOT dominate all prefixes equally
y_by_prefix = {}
for pfx in ['ch', 'sh', 'd', 'o', 'q', 'k']:
    pfx_words = [w for w in all_words if classify_prefix(w) == pfx]
    y_count = sum(1 for w in pfx_words if w.endswith('y'))
    total = len(pfx_words)
    y_pct = y_count / total * 100 if total > 0 else 0
    y_by_prefix[pfx] = y_pct
    print(f"  {pfx}-words ending in -y: {y_count}/{total} ({y_pct:.1f}%)")

print()
print("If -y were '4th degree', it should NOT dominate ~50% of all words")
print("  -> -y is likely a MORPHOLOGICAL default, not a degree marker")
print("  -> This severely weakens the degree hypothesis for -y")
print()
print("However, n/l/r show ~17-18% each, remarkably uniform.")
print("  -> n/l/r COULD encode 3 degrees (not 4)")
print("  -> Or n/l/r could encode preparation method: raw/dried/ground")
