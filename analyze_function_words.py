import re
import sys
from collections import Counter, defaultdict

with open('RF1b-e.txt', 'r') as f:
    content = f.read()

lines = content.split('\n')
parsed = []
for line in lines:
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    m = re.match(r'<(f\d+\w*)', line)
    if not m:
        continue
    folio = m.group(1)
    text_part = re.sub(r'<[^>]*>', '', line).strip()
    text_part = re.sub(r'\{[^}]*\}', '', text_part)
    text_part = re.sub(r'@\d+;?', '', text_part)
    words = re.split(r'[.\s,<>\-\?\!]+', text_part)
    words = [w.strip() for w in words if w.strip() and re.match(r'^[a-z]+$', w.strip())]
    parsed.append((folio, words))

# Build word sequences per folio line
all_words = []
word_contexts = []  # (word, prev_word, next_word, folio, position_in_line, line_length)
for folio, words in parsed:
    for i, w in enumerate(words):
        all_words.append(w)
        prev_w = words[i-1] if i > 0 else None
        next_w = words[i+1] if i < len(words)-1 else None
        word_contexts.append((w, prev_w, next_w, folio, i, len(words)))

wf = Counter(all_words)
print(f'Total: {len(all_words)} words, {len(wf)} unique')
print()

# Top 40
print('=== Top 40 most frequent words ===')
for w, c in wf.most_common(40):
    print(f'  {w}: {c}')

# -aiin words
print('\n=== ALL words ending in -aiin ===')
aiin_words = sorted(((w,c) for w,c in wf.items() if w.endswith('aiin')), key=lambda x:-x[1])
for w, c in aiin_words:
    print(f'  {w}: {c}')
print(f'  TOTAL: {len(aiin_words)} types, {sum(c for _,c in aiin_words)} tokens')

# Group by prefix
print('\n=== -aiin words grouped by prefix ===')
prefix_groups = defaultdict(list)
for w, c in aiin_words:
    prefix = w[:-4]  # remove 'aiin'
    prefix_groups[prefix].append((w, c))
for prefix in sorted(prefix_groups, key=lambda p: -sum(c for _,c in prefix_groups[p])):
    total = sum(c for _,c in prefix_groups[prefix])
    items = prefix_groups[prefix]
    print(f'  PREFIX "{prefix}": total={total}  ->  {items}')

# -ain words (not -aiin)
print('\n=== ALL words ending in -ain (not -aiin) ===')
ain_words = sorted(((w,c) for w,c in wf.items() if w.endswith('ain') and not w.endswith('aiin')), key=lambda x:-x[1])
for w, c in ain_words:
    print(f'  {w}: {c}')
print(f'  TOTAL: {len(ain_words)} types, {sum(c for _,c in ain_words)} tokens')

# bare aiin
print(f'\n=== Bare "aiin" frequency: {wf.get("aiin", 0)} ===')
print(f'=== Bare "ain" frequency: {wf.get("ain", 0)} ===')

# -iin words
print('\n=== Words ending in -iin (not -aiin) ===')
iin_words = sorted(((w,c) for w,c in wf.items() if w.endswith('iin') and not w.endswith('aiin')), key=lambda x:-x[1])
for w, c in iin_words[:20]:
    print(f'  {w}: {c}')

# ol, or, ar, al analysis
print('\n=== Short function words: ol, or, ar, al ===')
for sw in ['ol', 'or', 'ar', 'al', 'aiin', 'ain']:
    print(f'  {sw}: {wf.get(sw, 0)}')

print('\n' + '='*60)
print('DISTRIBUTIONAL ANALYSIS OF FREQUENT -aiin WORDS')
print('='*60)

# For each -aiin word with freq >= 5
target_words = [w for w, c in aiin_words if c >= 5] + ['aiin', 'ol', 'or', 'ar', 'al']
target_words = [w for w in target_words if wf.get(w, 0) >= 3]

for tw in target_words:
    freq = wf.get(tw, 0)
    if freq < 3:
        continue
    print(f'\n--- "{tw}" (freq={freq}) ---')

    preceding = Counter()
    following = Counter()
    folios = Counter()
    positions = []

    for w, prev_w, next_w, folio, pos, line_len in word_contexts:
        if w == tw:
            if prev_w:
                preceding[prev_w] += 1
            if next_w:
                following[next_w] += 1
            folios[folio] += 1
            if line_len > 1:
                positions.append(pos / (line_len - 1) if line_len > 1 else 0)

    print(f'  Top preceding: {preceding.most_common(10)}')
    print(f'  Top following: {following.most_common(10)}')

    # Position stats
    if positions:
        avg_pos = sum(positions) / len(positions)
        line_start = sum(1 for p in positions if p < 0.2)
        line_mid = sum(1 for p in positions if 0.2 <= p <= 0.8)
        line_end = sum(1 for p in positions if p > 0.8)
        print(f'  Position: avg={avg_pos:.2f}, start(<0.2)={line_start}, mid={line_mid}, end(>0.8)={line_end}')

    # Top folios
    top_folios = folios.most_common(10)
    print(f'  Top folios: {top_folios}')

print('\n' + '='*60)
print('DAIIN DEEP ANALYSIS')
print('='*60)

daiin_contexts = []
for w, prev_w, next_w, folio, pos, line_len in word_contexts:
    if w == 'daiin':
        daiin_contexts.append((prev_w, next_w, folio, pos, line_len))

print(f'Total "daiin" occurrences: {len(daiin_contexts)}')

# Pattern: X daiin Y (between two content words)
between_count = sum(1 for p, n, _, _, _ in daiin_contexts if p and n)
only_follows = sum(1 for p, n, _, _, _ in daiin_contexts if not p and n)
only_precedes = sum(1 for p, n, _, _, _ in daiin_contexts if p and not n)
print(f'  Between two words (X daiin Y): {between_count}')
print(f'  At line start (daiin Y): {only_follows}')
print(f'  At line end (X daiin): {only_precedes}')

# What follows daiin?
daiin_following = Counter()
for p, n, _, _, _ in daiin_contexts:
    if n:
        daiin_following[n] += 1

print(f'\n  What follows "daiin":')
for w, c in daiin_following.most_common(20):
    print(f'    {w}: {c}')

# Check for plant-related words (cho-, sho-, cth-)
plant_prefixes = ['cho', 'sho', 'cth', 'ck', 'ch']
plant_following = 0
for w, c in daiin_following.items():
    for pp in ['cho', 'sho', 'cth']:
        if w.startswith(pp):
            plant_following += c
            break

total_following = sum(daiin_following.values())
print(f'\n  Following words starting with cho/sho/cth: {plant_following}/{total_following} = {plant_following/total_following*100:.1f}%')

# What precedes daiin?
daiin_preceding = Counter()
for p, n, _, _, _ in daiin_contexts:
    if p:
        daiin_preceding[p] += 1

print(f'\n  What precedes "daiin":')
for w, c in daiin_preceding.most_common(20):
    print(f'    {w}: {c}')

print('\n' + '='*60)
print('PREFIX + OTHER SUFFIXES (Agglutinative model test)')
print('='*60)

# Check if d-, s-, k-, r-, t- prefixes combine with other suffixes
prefixes_to_test = ['d', 's', 'k', 'r', 't', 'ch', 'sh', 'ok', 'ot', 'qo']
suffixes_to_test = ['aiin', 'ain', 'ol', 'or', 'al', 'ar', 'an', 'am', 'air', 'ey', 'ody', 'chy']

for prefix in prefixes_to_test:
    found = []
    for suffix in suffixes_to_test:
        word = prefix + suffix
        if word in wf:
            found.append((word, wf[word]))
    if found:
        print(f'  PREFIX "{prefix}"+suffix: {found}')

# Also check: does PREFIX alone appear?
print('\n  Bare prefixes:')
for prefix in prefixes_to_test:
    if prefix in wf:
        print(f'    "{prefix}": {wf[prefix]}')

print('\n' + '='*60)
print('SHORT WORD ANALYSIS: ol, or, ar, al')
print('='*60)

for sw in ['ol', 'or', 'ar', 'al']:
    freq = wf.get(sw, 0)
    print(f'\n--- "{sw}" (freq={freq}) ---')
    preceding = Counter()
    following = Counter()
    positions = []

    for w, prev_w, next_w, folio, pos, line_len in word_contexts:
        if w == sw:
            if prev_w:
                preceding[prev_w] += 1
            if next_w:
                following[next_w] += 1
            if line_len > 1:
                positions.append(pos / (line_len - 1))

    print(f'  Top preceding: {preceding.most_common(10)}')
    print(f'  Top following: {following.most_common(10)}')
    if positions:
        avg_pos = sum(positions) / len(positions)
        line_start = sum(1 for p in positions if p < 0.2)
        line_mid = sum(1 for p in positions if 0.2 <= p <= 0.8)
        line_end = sum(1 for p in positions if p > 0.8)
        print(f'  Position: avg={avg_pos:.2f}, start={line_start}, mid={line_mid}, end={line_end}')

# Section analysis for key words
print('\n' + '='*60)
print('SECTION DISTRIBUTION')
print('='*60)

# Determine section from folio number
def get_section(folio):
    m = re.match(r'f(\d+)', folio)
    if not m:
        return 'unknown'
    num = int(m.group(1))
    if num <= 11:
        return 'A-herbal1(f1-f11)'
    elif num <= 25:
        return 'B-herbal2(f12-f25)'
    elif num <= 56:
        return 'C-herbal3(f26-f56)'
    elif num <= 67:
        return 'D-astro(f57-f67)'
    elif num <= 73:
        return 'E-cosmo(f68-f73)'
    elif num <= 84:
        return 'F-pharma(f75-f84)'
    elif num <= 86:
        return 'G-recipes(f85-f86)'
    elif num <= 102:
        return 'H-herbal4(f87-f102)'
    elif num <= 116:
        return 'I-stars(f103-f116)'
    else:
        return 'J-other'

key_words = ['daiin', 'saiin', 'kaiin', 'chol', 'chor', 'shol', 'shor', 'ol', 'or', 'ar', 'al', 'aiin', 'dain', 'dar', 'dal']
for kw in key_words:
    if wf.get(kw, 0) < 3:
        continue
    section_counts = Counter()
    for w, _, _, folio, _, _ in word_contexts:
        if w == kw:
            section_counts[get_section(folio)] += 1
    print(f'  "{kw}" ({wf[kw]}): {dict(sorted(section_counts.items()))}')

print('\nDone.')
