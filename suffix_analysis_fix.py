import re
from collections import Counter, defaultdict

with open('RF1b-e.txt', 'r') as f:
    lines = f.readlines()

def classify_section(folio):
    m = re.match(r'f(\d+)', folio)
    if not m:
        return 'unknown'
    num = int(m.group(1))
    if num <= 57:
        return 'herbal'
    elif 67 <= num <= 73:
        return 'astro'
    elif 75 <= num <= 84:
        return 'bio'
    elif 88 <= num <= 116:
        return 'recipe'
    else:
        return 'other'

current_folio = ''
all_lines = []  # (folio, section, ref, [words])
folio_language = {}

for line in lines:
    line = line.strip()
    folio_match = re.match(r'<(f\d+[rv])>', line)
    if folio_match:
        current_folio = folio_match.group(1)
        continue
    lang_match = re.search(r'\$L=([AB])', line)
    if lang_match:
        folio_language[current_folio] = lang_match.group(1)
        continue
    if line.startswith('#') or line.startswith('<!'):
        continue
    line_match = re.match(r'<([^>]+)>\s+(.*)', line)
    if not line_match:
        continue
    ref = line_match.group(1)
    text = line_match.group(2)
    text = re.sub(r'@\d+;?', '', text)
    text = re.sub(r'\{[^}]+\}', '', text)
    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'[?,.]', '', text)
    words = [w.strip() for w in text.split() if w.strip()]
    section = classify_section(current_folio)
    all_lines.append((current_folio, section, ref, words))

suffixes_ordered = ['-aiin', '-ain', '-eey', '-edy', '-am', '-an', '-ar', '-al', '-ol', '-or', '-ey', '-dy', '-y']

def get_suffix(word):
    for suf in suffixes_ordered:
        s = suf[1:]
        if word.endswith(s) and len(word) > len(s):
            return suf
    return None

output = []

# ============================================================
# 6. GRAMMATICAL ROLES TEST (FIXED)
# ============================================================
output.append("=" * 70)
output.append("6. TEST: SUFFIXES = GRAMMATICAL ROLES (FIXED)")
output.append("=" * 70)

# Build bigrams from all lines
suffix_next_suffix = defaultdict(Counter)
suffix_prev_word = defaultdict(Counter)  # what word precedes suffix-bearing words
total_bigrams = 0

for folio, section, ref, words in all_lines:
    for i in range(len(words) - 1):
        w1 = words[i]
        w2 = words[i + 1]
        suf1 = get_suffix(w1)
        suf2 = get_suffix(w2)
        if suf1:
            next_label = suf2 if suf2 else f"[{w2}]" if len(w2) <= 6 else "NONE"
            suffix_next_suffix[suf1][suf2 if suf2 else 'NONE'] += 1
        total_bigrams += 1

output.append("")
output.append("6a. What suffix follows each suffix type (top 5):")
active_suffixes = [s for s in suffixes_ordered]
for suf in active_suffixes:
    total = sum(suffix_next_suffix[suf].values())
    if total < 10:
        continue
    top5 = suffix_next_suffix[suf].most_common(5)
    desc = ", ".join(f"{s}:{c}({c/total*100:.0f}%)" for s, c in top5)
    output.append(f"  {suf} (n={total}): {desc}")

# After daiin/dain analysis
output.append("")
output.append("6b. Words appearing after daiin/dain:")
suffix_after_daiin = Counter()
total_after_daiin = 0
words_after_daiin = Counter()

for folio, section, ref, words in all_lines:
    for i in range(len(words) - 1):
        if words[i] in ('daiin', 'dain'):
            total_after_daiin += 1
            next_word = words[i + 1]
            words_after_daiin[next_word] += 1
            suf = get_suffix(next_word)
            if suf:
                suffix_after_daiin[suf] += 1
            else:
                suffix_after_daiin['[no suffix]'] += 1

output.append(f"  Total daiin/dain bigrams: {total_after_daiin}")
for suf, cnt in suffix_after_daiin.most_common():
    output.append(f"  {suf}: {cnt} ({cnt/total_after_daiin*100:.1f}%)")

output.append("")
output.append("  Top 10 actual words after daiin/dain:")
for w, cnt in words_after_daiin.most_common(10):
    output.append(f"    {w}: {cnt}")

# Before suffix analysis - what words commonly precede suffix-bearing words
output.append("")
output.append("6c. Common words BEFORE each suffix type:")
word_before_suffix = defaultdict(Counter)
for folio, section, ref, words in all_lines:
    for i in range(1, len(words)):
        suf = get_suffix(words[i])
        if suf:
            word_before_suffix[suf][words[i-1]] += 1

for suf in active_suffixes:
    total = sum(word_before_suffix[suf].values())
    if total < 10:
        continue
    top5 = word_before_suffix[suf].most_common(5)
    desc = ", ".join(f"{w}:{c}" for w, c in top5)
    output.append(f"  before {suf}: {desc}")

# Line-initial vs line-final
output.append("")
output.append("6d. Line-initial vs line-final position:")
suffix_line_initial = Counter()
suffix_line_final = Counter()
total_lines_counted = 0

for folio, section, ref, words in all_lines:
    if not words:
        continue
    total_lines_counted += 1
    s_first = get_suffix(words[0])
    s_last = get_suffix(words[-1])
    if s_first:
        suffix_line_initial[s_first] += 1
    if s_last:
        suffix_line_final[s_last] += 1

output.append(f"  Total lines: {total_lines_counted}")
output.append(f"  {'suffix':>8s} {'initial':>8s} {'final':>8s} {'I/(I+F)':>8s}")
for suf in active_suffixes:
    ini = suffix_line_initial.get(suf, 0)
    fin = suffix_line_final.get(suf, 0)
    total = ini + fin
    ratio = ini / total if total else 0
    if total > 0:
        output.append(f"  {suf:>8s} {ini:8d} {fin:8d} {ratio:8.3f}")

# Word-initial position (first word of a folio page)
output.append("")
output.append("6e. First word of each folio page - suffix distribution:")
folio_first_word_suffix = Counter()
seen_folios = set()
for folio, section, ref, words in all_lines:
    if folio not in seen_folios and words:
        seen_folios.add(folio)
        suf = get_suffix(words[0])
        if suf:
            folio_first_word_suffix[suf] += 1
        else:
            folio_first_word_suffix['[none]'] += 1

for suf, cnt in folio_first_word_suffix.most_common():
    output.append(f"  {suf}: {cnt}")

# ============================================================
# 6f. Test: -ey/-y before nouns vs -ol/-or after "of"
# ============================================================
output.append("")
output.append("6f. Suffix pairs: do -ey/-y words precede -ol/-or words (adjective+noun pattern)?")

pair_counts = defaultdict(int)
total_pairs = 0
for folio, section, ref, words in all_lines:
    for i in range(len(words) - 1):
        s1 = get_suffix(words[i])
        s2 = get_suffix(words[i+1])
        if s1 and s2:
            pair_counts[(s1, s2)] += 1
            total_pairs += 1

output.append(f"  Total suffix-suffix bigrams: {total_pairs}")
output.append("")
output.append("  Top 20 suffix bigrams:")
for (s1, s2), cnt in sorted(pair_counts.items(), key=lambda x: -x[1])[:20]:
    output.append(f"    {s1} -> {s2}: {cnt}")

# Expected if random
output.append("")
output.append("  Testing -ey/-y -> -ol/-or (adj->noun hypothesis):")
ey_y_total = sum(cnt for (s1, s2), cnt in pair_counts.items() if s1 in ('-ey', '-y'))
ey_y_to_ol_or = sum(cnt for (s1, s2), cnt in pair_counts.items() if s1 in ('-ey', '-y') and s2 in ('-ol', '-or'))
output.append(f"    -ey/-y followed by anything: {ey_y_total}")
output.append(f"    -ey/-y followed by -ol/-or: {ey_y_to_ol_or} ({ey_y_to_ol_or/ey_y_total*100:.1f}% of total)" if ey_y_total else "    N/A")

ol_or_total_in_pairs = sum(cnt for (s1, s2), cnt in pair_counts.items() if s2 in ('-ol', '-or'))
if total_pairs > 0:
    output.append(f"    Overall rate of -ol/-or as second element: {ol_or_total_in_pairs}/{total_pairs} = {ol_or_total_in_pairs/total_pairs*100:.1f}%")
else:
    output.append(f"    No suffix-suffix bigrams found")

print('\n'.join(output))
