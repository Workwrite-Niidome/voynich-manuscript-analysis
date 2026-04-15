#!/usr/bin/env python3
"""
Deeper analysis: sandhi/next-word conditioning for flexible stems,
and section-level default suffix switching.
"""

import re
from collections import defaultdict, Counter

def parse_voynich(filepath):
    words = []
    current_folio = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            folio_match = re.match(r'^<(f\d+[rv]\d*)>', line)
            if folio_match and '.' not in folio_match.group(1):
                current_folio = folio_match.group(1)
                continue
            line_match = re.match(r'^<(f\d+[rv]\d*\.\d+)', line)
            if line_match:
                line_id = line_match.group(1)
                folio = re.match(r'(f\d+[rv]\d*)', line_id).group(1)
                current_folio = folio
                text_part = re.sub(r'^<[^>]+>\s*', '', line)
                text_part = re.sub(r'<[^>]*>', '', text_part)
                text_part = re.sub(r'\{[^}]*\}', '', text_part)
                text_part = re.sub(r'@\d+;?', '', text_part)
                text_part = re.sub(r"[',?!]", '', text_part)
                tokens = re.split(r'[\s.<>\-]+', text_part)
                for token in tokens:
                    token = token.strip()
                    if token and len(token) > 1:
                        words.append((current_folio, line_id, token))
    return words

def get_section(folio):
    m = re.match(r'f(\d+)', folio)
    if not m:
        return 'unknown'
    num = int(m.group(1))
    if num <= 56: return 'herbal_a'
    elif num <= 66: return 'astro'
    elif num <= 73: return 'herbal_b'
    elif num <= 84: return 'bio'
    elif num <= 86: return 'cosmo'
    elif num <= 102: return 'pharma'
    elif num <= 116: return 'recipe'
    else: return 'other'

filepath = r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt'
words_data = parse_voynich(filepath)

# Key question: for "or" vs "ol" (stem="o"), is suffix conditioned by next word?
# Check if -r appears before vowel-initial next words (sandhi)

print("="*80)
print("SANDHI ANALYSIS: Does suffix depend on next word's initial character?")
print("="*80)

# For the top flexible stems, compute P(suffix | next_initial)
top_flex_stems = ['o', 'a', 'cho', 'da', 'sho', 'cheo', 'do', 'cha']

for stem in top_flex_stems:
    # Collect (suffix, next_word_initial) pairs
    pairs = []
    for i, (folio, line_id, word) in enumerate(words_data):
        if len(word) > 1 and word[-1] in 'lr' and word[:-1] == stem:
            if i + 1 < len(words_data):
                next_w = words_data[i+1][2]
                next_init = next_w[0]
                pairs.append((word[-1], next_init))

    if not pairs:
        continue

    print(f"\nStem '{stem}' ({len(pairs)} l/r tokens with following word):")

    # Group by next_initial, compute l:r ratio
    init_counts = defaultdict(Counter)
    for suffix, init in pairs:
        init_counts[init][suffix] += 1

    # Show for vowel vs consonant starts
    vowel_lr = Counter()
    cons_lr = Counter()
    vowels = set('aeiou')
    for init, counter in init_counts.items():
        if init in vowels:
            vowel_lr += counter
        else:
            cons_lr += counter

    vt = sum(vowel_lr.values())
    ct = sum(cons_lr.values())
    print(f"  Before vowel-initial: l={vowel_lr.get('l',0)}, r={vowel_lr.get('r',0)} (total={vt}, r%={vowel_lr.get('r',0)/vt*100:.1f}%)" if vt > 0 else "  Before vowel: none")
    print(f"  Before cons-initial:  l={cons_lr.get('l',0)}, r={cons_lr.get('r',0)} (total={ct}, r%={cons_lr.get('r',0)/ct*100:.1f}%)" if ct > 0 else "  Before cons: none")

    # Show per-initial breakdown for most common
    sorted_inits = sorted(init_counts.items(), key=lambda x: -sum(x[1].values()))
    for init, counter in sorted_inits[:6]:
        t = sum(counter.values())
        print(f"    '{init}': l={counter.get('l',0)}, r={counter.get('r',0)} (r%={counter.get('r',0)/t*100:.1f}%)")

# Check if -l/-r correlates with LINE POSITION
print("\n" + "="*80)
print("LINE POSITION ANALYSIS: Does suffix depend on position in line?")
print("="*80)

# Group by line, check if suffix correlates with position
for stem in ['o', 'cho', 'da']:
    first_half = Counter()
    second_half = Counter()

    # Group words by line
    line_words = defaultdict(list)
    for folio, line_id, word in words_data:
        line_words[line_id].append(word)

    for line_id, wlist in line_words.items():
        mid = len(wlist) // 2
        for i, word in enumerate(wlist):
            if len(word) > 1 and word[-1] in 'lr' and word[:-1] == stem:
                if i < mid:
                    first_half[word[-1]] += 1
                else:
                    second_half[word[-1]] += 1

    ft = sum(first_half.values())
    st = sum(second_half.values())
    print(f"\nStem '{stem}':")
    if ft > 0:
        print(f"  First half of line:  l={first_half.get('l',0)}, r={first_half.get('r',0)} (r%={first_half.get('r',0)/ft*100:.1f}%)")
    if st > 0:
        print(f"  Second half of line: l={second_half.get('l',0)}, r={second_half.get('r',0)} (r%={second_half.get('r',0)/st*100:.1f}%)")

# Section-level analysis for the equality paradox
print("\n" + "="*80)
print("SECTION-LEVEL n:l:r RATIOS")
print("="*80)

section_nlr = defaultdict(Counter)
for folio, line_id, word in words_data:
    if word[-1] in 'nlr' and len(word) > 1:
        sec = get_section(folio)
        section_nlr[sec][word[-1]] += 1

for sec in ['herbal_a', 'astro', 'herbal_b', 'bio', 'cosmo', 'pharma', 'recipe']:
    c = section_nlr[sec]
    t = sum(c.values())
    if t > 0:
        print(f"  {sec:12s}: n={c.get('n',0):4d} ({c.get('n',0)/t*100:.1f}%), l={c.get('l',0):4d} ({c.get('l',0)/t*100:.1f}%), r={c.get('r',0):4d} ({c.get('r',0)/t*100:.1f}%)  total={t}")

# Stem-final phonology determines suffix?
print("\n" + "="*80)
print("STEM-FINAL PHONEME vs DEFAULT SUFFIX")
print("="*80)
# For stems ending in specific chars, what's the default?
stem_suffix = defaultdict(Counter)
for folio, line_id, word in words_data:
    if word[-1] in 'nlr' and len(word) > 1:
        stem = word[:-1]
        stem_suffix[stem][word[-1]] += 1

final_char_defaults = defaultdict(Counter)
for stem, counter in stem_suffix.items():
    total = sum(counter.values())
    if total >= 10:
        best = counter.most_common(1)[0][0]
        final_char = stem[-1] if stem else '?'
        final_char_defaults[final_char][best] += 1

print("\nStem-final character -> default suffix distribution:")
for char in sorted(final_char_defaults.keys()):
    c = final_char_defaults[char]
    t = sum(c.values())
    if t >= 3:
        parts = ', '.join(f"{s}={cnt}" for s, cnt in sorted(c.items()))
        print(f"  Stems ending in '{char}': {parts}  (total={t})")

# The key insight: stems ending in 'ii' almost always default to -n
# Stems ending in 'o' almost always default to -l
# Stems ending in 'a' almost always default to -r
print("\n--- Summary of phonological conditioning ---")
for final in ['o', 'a', 'i', 'e']:
    c = final_char_defaults.get(final, Counter())
    t = sum(c.values())
    if t > 0:
        parts = ', '.join(f"-{s}: {cnt} ({cnt/t*100:.1f}%)" for s, cnt in sorted(c.items()))
        print(f"  Stems ending in '{final}': {parts}")
