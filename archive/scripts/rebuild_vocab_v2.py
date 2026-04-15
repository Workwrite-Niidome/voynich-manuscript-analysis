#!/usr/bin/env python3
"""
Rebuild Voynich vocabulary v2 - using correct $L (Currier language A/B) field.
"""

import re
from collections import Counter, defaultdict

filepath = r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt'

# Parse with correct scribe/language identification
folio_lang = {}  # folio -> 'A' or 'B' (Currier language)
parsed_lines = []

with open(filepath, 'r', encoding='utf-8') as f:
    current_folio = None
    for raw in f:
        raw = raw.rstrip('\n')
        if raw.startswith('#'):
            continue
        m = re.match(r'^<(f\d+[rv]\d?)>\s+<.*?\$L=(\w).*?>', raw)
        if m:
            current_folio = m.group(1)
            folio_lang[current_folio] = m.group(2)
            continue
        m2 = re.match(r'^<(f\d+[rv]\d?\.\d+(?:,\S+)?)>\s+(.*)', raw)
        if m2:
            parsed_lines.append((current_folio, m2.group(1), m2.group(2)))

def extract_words(text):
    text = re.sub(r'\{[^}]*\}', '', text)
    text = re.sub(r'@\d+;?', '', text)
    text = text.replace('<->', ' ')
    text = text.replace('.', ' ')
    tokens = re.split(r'[^a-z\']+', text.lower())
    return [t for t in tokens if t and re.match(r'^[a-z\']+$', t)]

# Build data by Currier language
all_words_by_lang = defaultdict(list)
word_freq_by_lang = defaultdict(Counter)
word_freq_total = Counter()
word_bigrams = []

for folio, line_id, text in parsed_lines:
    lang = folio_lang.get(folio, '?')
    words = extract_words(text)
    for w in words:
        all_words_by_lang[lang].append(w)
        word_freq_by_lang[lang][w] += 1
        word_freq_total[w] += 1
    for i in range(len(words) - 1):
        word_bigrams.append((words[i], words[i+1], lang))

total_A = len(all_words_by_lang['A'])
total_B = len(all_words_by_lang['B'])
print(f"Currier A words: {total_A}")
print(f"Currier B words: {total_B}")

# -edy by Currier language
edy_A = sum(f for w, f in word_freq_by_lang['A'].items() if w.endswith('edy'))
edy_B = sum(f for w, f in word_freq_by_lang['B'].items() if w.endswith('edy'))
ol_A = sum(f for w, f in word_freq_by_lang['A'].items() if w.endswith('ol'))
ol_B = sum(f for w, f in word_freq_by_lang['B'].items() if w.endswith('ol'))

print(f"\n-edy: Currier-A={edy_A} ({100*edy_A/total_A:.1f}%), Currier-B={edy_B} ({100*edy_B/total_B:.1f}%)")
print(f"-ol:  Currier-A={ol_A} ({100*ol_A/total_A:.1f}%), Currier-B={ol_B} ({100*ol_B/total_B:.1f}%)")

# -eey by Currier language
eey_A = sum(f for w, f in word_freq_by_lang['A'].items() if w.endswith('eey'))
eey_B = sum(f for w, f in word_freq_by_lang['B'].items() if w.endswith('eey'))
print(f"-eey: Currier-A={eey_A} ({100*eey_A/total_A:.1f}%), Currier-B={eey_B} ({100*eey_B/total_B:.1f}%)")

# -y total by language
y_A = sum(f for w, f in word_freq_by_lang['A'].items() if w.endswith('y'))
y_B = sum(f for w, f in word_freq_by_lang['B'].items() if w.endswith('y'))
print(f"-y total: Currier-A={y_A} ({100*y_A/total_A:.1f}%), Currier-B={y_B} ({100*y_B/total_B:.1f}%)")

# Top -edy words in A vs B
print("\nTop -edy words in Currier-A:")
edy_words_A = [(w, f) for w, f in word_freq_by_lang['A'].items() if w.endswith('edy')]
edy_words_A.sort(key=lambda x: -x[1])
for w, f in edy_words_A[:10]:
    print(f"  {w:>15} {f:>4}")

print("\nTop -edy words in Currier-B:")
edy_words_B = [(w, f) for w, f in word_freq_by_lang['B'].items() if w.endswith('edy')]
edy_words_B.sort(key=lambda x: -x[1])
for w, f in edy_words_B[:10]:
    print(f"  {w:>15} {f:>4}")

# Check -edy sandhi: does -edy ever alternate with -edn, -edl, -edr?
for suffix in ['edn', 'edl', 'edr']:
    count = sum(f for w, f in word_freq_total.items() if w.endswith(suffix))
    print(f"\nWords ending in -{suffix}: {count}")
    if count > 0:
        examples = [(w, f) for w, f in word_freq_total.items() if w.endswith(suffix)]
        examples.sort(key=lambda x: -x[1])
        for w, f in examples[:5]:
            print(f"  {w} ({f})")

# Check: what follows -edy words? Compare suffix distribution
# If -edy were subject to sandhi, we'd expect -edn before c/s/f and -edr before vowels
print("\n--- Following-word analysis for -edy ---")
edy_next = defaultdict(Counter)
for w1, w2, lang in word_bigrams:
    if w1.endswith('edy') and w2:
        edy_next[w2[0]]['edy'] += 1
    elif w1.endswith('eey') and w2:
        edy_next[w2[0]]['eey'] += 1

# For comparison: what follows -ol words?
ol_next = defaultdict(Counter)
for w1, w2, lang in word_bigrams:
    if w1.endswith('ol') and w2:
        ol_next[w2[0]]['ol'] += 1
    elif w1.endswith('or') and w2 and not w1.endswith('eor'):
        ol_next[w2[0]]['or'] += 1
    elif w1.endswith('on') and w2:
        ol_next[w2[0]]['on'] += 1

print("\nContext: next-word initial distribution after -edy vs -ol/-or")
print(f"{'Init':>5} {'after -edy':>10} {'after -eey':>10} {'after -ol':>10} {'after -or':>10}")
for init in 'acdeklopqrsty':
    e_edy = edy_next[init].get('edy', 0)
    e_eey = edy_next[init].get('eey', 0)
    e_ol = ol_next[init].get('ol', 0)
    e_or = ol_next[init].get('or', 0)
    print(f"  {init:>3} {e_edy:>10} {e_eey:>10} {e_ol:>10} {e_or:>10}")

# -y words: check if they share stems with the main n/l/r paradigm
print("\n\n--- KEY QUESTION: Do -y endings participate in sandhi? ---")
# Check -y words before different initials
y_next_init = Counter()
non_y_next_init = Counter()
for w1, w2, lang in word_bigrams:
    if not w2:
        continue
    if w1.endswith('y'):
        y_next_init[w2[0]] += 1
    else:
        non_y_next_init[w2[0]] += 1

print(f"\nFollowing-word initial after -y words vs non-y words:")
print(f"{'Init':>5} {'after -y':>10} {'%':>6} {'after non-y':>10} {'%':>6}")
total_y_next = sum(y_next_init.values())
total_nony_next = sum(non_y_next_init.values())
for init in 'acdeklopqrsty':
    yc = y_next_init[init]
    nc = non_y_next_init[init]
    yp = 100*yc/total_y_next if total_y_next else 0
    np = 100*nc/total_nony_next if total_nony_next else 0
    print(f"  {init:>3} {yc:>10} {yp:>5.1f}% {nc:>10} {np:>5.1f}%")

# Check specific hypothesis: is -y the citation form?
# If so, -y words should NOT correlate with following word initial
# (unlike n/l/r words which DO correlate)
# Also: -y words should be more common in labels/titles
print("\n--- -y in labels vs body text ---")
label_words = []
body_words = []
for folio, line_id, text in parsed_lines:
    words = extract_words(text)
    if ',@L' in line_id or ',+L' in line_id or ',=L' in line_id or ',=Pt' in line_id:
        label_words.extend(words)
    else:
        body_words.extend(words)

label_y = sum(1 for w in label_words if w.endswith('y'))
body_y = sum(1 for w in body_words if w.endswith('y'))
print(f"Labels: {len(label_words)} words, {label_y} end in -y ({100*label_y/len(label_words) if label_words else 0:.1f}%)")
print(f"Body:   {len(body_words)} words, {body_y} end in -y ({100*body_y/len(body_words) if body_words else 0:.1f}%)")

# Deep analysis: -edy morphological breakdown
print("\n\n--- DEEP -edy ANALYSIS ---")
# Strip -edy, get base. Compare with -ol bases (strip -ol).
# If chedy=chol, then ch+edy = ch+ol. The base is 'ch'.
# What does the -ed- infix mean?

print("Morphological comparison: -ol vs -edy")
print(f"{'Base':>10} {'-ol freq':>10} {'-edy freq':>10} {'-or freq':>10} {'-eey freq':>10} {'-ey freq':>10}")

# Find common bases
ol_base_freq = Counter()
edy_base_freq = Counter()
or_base_freq = Counter()
eey_base_freq = Counter()
ey_base_freq = Counter()

for w, f in word_freq_total.items():
    if w.endswith('ol') and len(w) > 2:
        ol_base_freq[w[:-2]] += f
    if w.endswith('edy') and len(w) > 3:
        edy_base_freq[w[:-3]] += f
    if w.endswith('or') and len(w) > 2:
        or_base_freq[w[:-2]] += f
    if w.endswith('eey') and len(w) > 3:
        eey_base_freq[w[:-3]] += f
    if w.endswith('ey') and not w.endswith('eey') and len(w) > 2:
        ey_base_freq[w[:-2]] += f

all_bases = set(ol_base_freq) | set(edy_base_freq)
base_data = []
for base in all_bases:
    ol_f = ol_base_freq.get(base, 0)
    edy_f = edy_base_freq.get(base, 0)
    or_f = or_base_freq.get(base, 0)
    eey_f = eey_base_freq.get(base, 0)
    ey_f = ey_base_freq.get(base, 0)
    total = ol_f + edy_f + or_f + eey_f + ey_f
    if total >= 20:
        base_data.append((base, ol_f, edy_f, or_f, eey_f, ey_f, total))

base_data.sort(key=lambda x: -x[6])
for base, ol_f, edy_f, or_f, eey_f, ey_f, total in base_data[:25]:
    print(f"  {base:>10} {ol_f:>10} {edy_f:>10} {or_f:>10} {eey_f:>10} {ey_f:>10}")

# Check: does -edy correlate with Currier-B specifically?
print("\n\nPer-base -edy vs -ol by Currier language:")
for base in ['ch', 'sh', 'qok', 'ot', 'ok', 'lch', 'qot', 'opch', 'pch']:
    ol_w = base + 'ol'
    edy_w = base + 'edy'
    ol_a = word_freq_by_lang['A'].get(ol_w, 0)
    ol_b = word_freq_by_lang['B'].get(ol_w, 0)
    edy_a = word_freq_by_lang['A'].get(edy_w, 0)
    edy_b = word_freq_by_lang['B'].get(edy_w, 0)
    print(f"  {base:>6}: {ol_w}  A={ol_a:>3} B={ol_b:>3}  |  {edy_w}  A={edy_a:>3} B={edy_b:>3}")
