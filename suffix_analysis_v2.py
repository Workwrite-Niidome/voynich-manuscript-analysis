import re
from collections import Counter, defaultdict

with open('RF1b-e.txt', 'r') as f:
    raw_lines = f.readlines()

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
folio_language = {}
all_text_lines = []  # (folio, section, ref, [words])

for raw_line in raw_lines:
    raw_line = raw_line.strip()

    # Check for folio header (may share line with <! ...>)
    folio_match = re.match(r'<(f\d+[rv])>', raw_line)
    if folio_match:
        current_folio = folio_match.group(1)
        # Check for language tag on same line
        lang_match = re.search(r'\$L=([AB])', raw_line)
        if lang_match:
            folio_language[current_folio] = lang_match.group(1)
        continue

    if raw_line.startswith('#') or raw_line.startswith('<!'):
        continue

    line_match = re.match(r'<([^>]+)>\s+(.*)', raw_line)
    if not line_match:
        continue

    ref = line_match.group(1)
    text = line_match.group(2)

    # Clean text
    text = re.sub(r'@\d+;?', '', text)
    text = re.sub(r'\{[^}]+\}', '', text)
    text = re.sub(r'[?,]', '', text)

    # Handle line breaks marked with <->
    text = text.replace('<->', '.')

    # Split by dots (EVA word separator)
    words = [w.strip() for w in text.split('.') if w.strip()]

    section = classify_section(current_folio)
    if words:
        all_text_lines.append((current_folio, section, ref, words))

# Build flat entries too
all_entries = []
for folio, section, ref, words in all_text_lines:
    for w in words:
        all_entries.append((folio, section, ref, w))

print(f"Total word tokens: {len(all_entries)}")
print(f"Total text lines: {len(all_text_lines)}")
print(f"Folios with language tag: {dict(Counter(folio_language.values()))}")

# Folio lines for position calculation
folio_line_counts = Counter()
for folio, section, ref, words in all_text_lines:
    folio_line_counts[folio] += 1

suffixes_ordered = ['-aiin', '-ain', '-eey', '-edy', '-am', '-an', '-ar', '-al', '-ol', '-or', '-ey', '-dy', '-y']

def get_suffix(word):
    for suf in suffixes_ordered:
        s = suf[1:]
        if word.endswith(s) and len(word) > len(s):
            return suf
    return None

# Quick frequency check
suffix_freq = Counter()
for _, _, _, w in all_entries:
    suf = get_suffix(w)
    if suf:
        suffix_freq[suf] += 1

print("\nSuffix frequencies:")
for suf in suffixes_ordered:
    print(f"  {suf}: {suffix_freq[suf]}")

output = []

# ============================================================
# 1. SECTION DISTRIBUTION
# ============================================================
output.append("=" * 70)
output.append("1. SECTION DISTRIBUTION")
output.append("=" * 70)

sections_list = ['herbal', 'recipe', 'bio', 'astro', 'other']
suffix_section_counts = defaultdict(Counter)
section_totals = Counter()

for folio, section, ref, word in all_entries:
    section_totals[section] += 1
    suf = get_suffix(word)
    if suf:
        suffix_section_counts[suf][section] += 1

total_words = sum(section_totals.values())
output.append(f"\nSection sizes: {dict(section_totals)} (total={total_words})")

for suf in suffixes_ordered:
    total = sum(suffix_section_counts[suf].values())
    if total < 40:
        continue
    output.append(f"\n{suf} (n={total}):")
    for sec in sections_list:
        cnt = suffix_section_counts[suf][sec]
        pct = cnt / total * 100 if total else 0
        exp = section_totals[sec] / total_words * 100
        ratio = pct / exp if exp else 0
        marker = " ***" if abs(ratio - 1.0) > 0.5 else ""
        output.append(f"  {sec:8s}: {cnt:4d} ({pct:5.1f}%)  expected: {exp:5.1f}%  ratio: {ratio:.2f}{marker}")

# ============================================================
# 2. POSITION IN HERBAL ENTRIES
# ============================================================
output.append("")
output.append("=" * 70)
output.append("2. POSITION IN HERBAL ENTRIES")
output.append("=" * 70)

# Track line number within each folio
folio_line_idx = {}  # ref -> (folio, line_index)
current_folio_for_idx = ''
current_idx = 0
for folio, section, ref, words in all_text_lines:
    if folio != current_folio_for_idx:
        current_folio_for_idx = folio
        current_idx = 0
    folio_line_idx[ref] = (folio, current_idx)
    current_idx += 1

suffix_positions = defaultdict(list)
for folio, section, ref, word in all_entries:
    if section != 'herbal':
        continue
    if ref not in folio_line_idx:
        continue
    f, idx = folio_line_idx[ref]
    total = folio_line_counts[f]
    rel_pos = idx / max(total - 1, 1) if total > 1 else 0.5
    suf = get_suffix(word)
    if suf:
        suffix_positions[suf].append(rel_pos)

for suf in suffixes_ordered:
    positions = suffix_positions[suf]
    if len(positions) < 15:
        continue
    avg = sum(positions) / len(positions)
    begin = sum(1 for p in positions if p < 0.33)
    middle = sum(1 for p in positions if 0.33 <= p < 0.67)
    end = sum(1 for p in positions if p >= 0.67)
    total = len(positions)
    output.append(f"\n{suf} (n={total}, mean_pos={avg:.3f}):")
    output.append(f"  Beginning (0-33%): {begin:4d} ({begin/total*100:5.1f}%)")
    output.append(f"  Middle   (33-67%): {middle:4d} ({middle/total*100:5.1f}%)")
    output.append(f"  End      (67-100%): {end:4d} ({end/total*100:5.1f}%)")

# ============================================================
# 3. STEM x SUFFIX CO-OCCURRENCE
# ============================================================
output.append("")
output.append("=" * 70)
output.append("3. STEM x SUFFIX CO-OCCURRENCE (top 30 stems)")
output.append("=" * 70)

stem_counter = Counter()
stem_suffix = defaultdict(Counter)
for _, _, _, word in all_entries:
    suf = get_suffix(word)
    if suf:
        stem = word[:-len(suf)+1]
        stem_counter[stem] += 1
        stem_suffix[stem][suf] += 1

top_stems = [s for s, c in stem_counter.most_common(30)]
active_suffixes = suffixes_ordered  # all of them

header = f"{'stem':>12s}"
for suf in active_suffixes:
    header += f" {suf:>5s}"
output.append(header)
output.append("-" * len(header))

for stem in top_stems:
    row = f"{stem:>12s}"
    for suf in active_suffixes:
        cnt = stem_suffix[stem].get(suf, 0)
        row += f" {cnt:5d}" if cnt else "     -"
    row += f"  (total: {stem_counter[stem]})"
    output.append(row)

# ============================================================
# 4. PLANT PARTS TEST
# ============================================================
output.append("")
output.append("=" * 70)
output.append("4. TEST: SUFFIXES = PLANT PARTS")
output.append("=" * 70)

leaf_pages = set()
root_pages = set()
for n in list(range(1, 9)) + list(range(13, 17)) + list(range(25, 31)):
    leaf_pages.add(f'f{n}r')
    leaf_pages.add(f'f{n}v')
for n in list(range(9, 13)) + list(range(17, 25)) + list(range(33, 41)) + list(range(43, 57)):
    root_pages.add(f'f{n}r')
    root_pages.add(f'f{n}v')

suffix_leaf = defaultdict(int)
suffix_root = defaultdict(int)
for folio, section, ref, word in all_entries:
    suf = get_suffix(word)
    if not suf:
        continue
    if folio in leaf_pages:
        suffix_leaf[suf] += 1
    elif folio in root_pages:
        suffix_root[suf] += 1

total_leaf_words = sum(1 for f, s, r, w in all_entries if f in leaf_pages)
total_root_words = sum(1 for f, s, r, w in all_entries if f in root_pages)
baseline = total_leaf_words / (total_leaf_words + total_root_words) if (total_leaf_words + total_root_words) else 0

output.append(f"\nLeaf pages words: {total_leaf_words}, Root pages words: {total_root_words}")
output.append(f"{'suffix':>8s} {'leaf':>6s} {'root':>6s} {'L/(L+R)':>8s}  baseline={baseline:.3f}")
output.append("-" * 50)
for suf in active_suffixes:
    l = suffix_leaf[suf]
    r = suffix_root[suf]
    total = l + r
    if total == 0:
        continue
    ratio = l / total
    marker = " ***" if abs(ratio - baseline) > 0.10 else ""
    output.append(f"{suf:>8s} {l:6d} {r:6d} {ratio:8.3f}{marker}")

# ============================================================
# 5. PREPARATION METHODS TEST
# ============================================================
output.append("")
output.append("=" * 70)
output.append("5. TEST: SUFFIXES = PREPARATION METHODS (herbal vs recipe)")
output.append("=" * 70)

herbal_total = section_totals['herbal']
recipe_total = section_totals['recipe']

output.append(f"\nHerbal: {herbal_total} words, Recipe: {recipe_total} words")
output.append(f"{'suffix':>8s} {'herbal_rate':>12s} {'recipe_rate':>12s} {'ratio(R/H)':>12s}")
output.append("-" * 50)
for suf in active_suffixes:
    h = suffix_section_counts[suf]['herbal']
    r = suffix_section_counts[suf]['recipe']
    h_rate = h / herbal_total * 100 if herbal_total else 0
    r_rate = r / recipe_total * 100 if recipe_total else 0
    ratio = r_rate / h_rate if h_rate else float('inf')
    marker = " ***" if ratio > 2.0 or ratio < 0.5 else ""
    output.append(f"{suf:>8s} {h_rate:12.2f} {r_rate:12.2f} {ratio:12.2f}{marker}")

# ============================================================
# 6. GRAMMATICAL ROLES TEST
# ============================================================
output.append("")
output.append("=" * 70)
output.append("6. TEST: SUFFIXES = GRAMMATICAL ROLES")
output.append("=" * 70)

# 6a. Bigram analysis: what suffix follows what suffix
suffix_bigrams = defaultdict(Counter)
total_suffix_bigrams = 0

for folio, section, ref, words in all_text_lines:
    for i in range(len(words) - 1):
        s1 = get_suffix(words[i])
        s2 = get_suffix(words[i+1])
        if s1 and s2:
            suffix_bigrams[s1][s2] += 1
            total_suffix_bigrams += 1

output.append(f"\n6a. Suffix bigrams (suffix1 -> suffix2), total={total_suffix_bigrams}:")
output.append("  Top 25 most common suffix pairs:")
all_bigram_pairs = []
for s1, cnts in suffix_bigrams.items():
    for s2, c in cnts.items():
        all_bigram_pairs.append((s1, s2, c))
all_bigram_pairs.sort(key=lambda x: -x[2])
for s1, s2, c in all_bigram_pairs[:25]:
    output.append(f"    {s1:>6s} -> {s2:>6s}: {c:4d}")

output.append("")
output.append("  What typically follows each suffix (top 3):")
for suf in active_suffixes:
    total = sum(suffix_bigrams[suf].values())
    if total < 10:
        continue
    top3 = suffix_bigrams[suf].most_common(3)
    desc = ", ".join(f"{s2}:{c}({c/total*100:.0f}%)" for s2, c in top3)
    output.append(f"    {suf} (n={total}): {desc}")

# 6b. After daiin/dain
output.append("")
output.append("6b. Words after daiin/dain:")
suffix_after_daiin = Counter()
total_after_daiin = 0
words_after_daiin = Counter()

for folio, section, ref, words in all_text_lines:
    for i in range(len(words) - 1):
        if words[i] in ('daiin', 'dain'):
            total_after_daiin += 1
            nw = words[i+1]
            words_after_daiin[nw] += 1
            suf = get_suffix(nw)
            if suf:
                suffix_after_daiin[suf] += 1
            else:
                suffix_after_daiin['[none]'] += 1

output.append(f"  Total daiin/dain -> X bigrams: {total_after_daiin}")
if total_after_daiin > 0:
    for suf, cnt in suffix_after_daiin.most_common():
        output.append(f"    {suf}: {cnt} ({cnt/total_after_daiin*100:.1f}%)")
    output.append("  Top 10 actual words after daiin/dain:")
    for w, cnt in words_after_daiin.most_common(10):
        output.append(f"    {w}: {cnt}")

# 6c. Words before each suffix type
output.append("")
output.append("6c. Common words BEFORE suffix-bearing words:")
word_before_suffix = defaultdict(Counter)
for folio, section, ref, words in all_text_lines:
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

# 6d. Line-initial vs line-final
output.append("")
output.append("6d. Line-initial vs line-final position:")
suffix_line_initial = Counter()
suffix_line_final = Counter()

for folio, section, ref, words in all_text_lines:
    if not words:
        continue
    s_first = get_suffix(words[0])
    s_last = get_suffix(words[-1])
    if s_first:
        suffix_line_initial[s_first] += 1
    if s_last:
        suffix_line_final[s_last] += 1

output.append(f"  Total text lines: {len(all_text_lines)}")
output.append(f"  {'suffix':>8s} {'initial':>8s} {'final':>8s} {'I/(I+F)':>8s}")
for suf in active_suffixes:
    ini = suffix_line_initial.get(suf, 0)
    fin = suffix_line_final.get(suf, 0)
    total = ini + fin
    if total > 0:
        ratio = ini / total
        output.append(f"  {suf:>8s} {ini:8d} {fin:8d} {ratio:8.3f}")

# 6e. Test adj+noun pattern
output.append("")
output.append("6e. Adj+Noun hypothesis (-ey/-y before -ol/-or):")
ey_y_total = sum(c for s2, c in suffix_bigrams.get('-ey', {}).items()) + sum(c for s2, c in suffix_bigrams.get('-y', {}).items())
ey_y_to_ol_or = (suffix_bigrams.get('-ey', {}).get('-ol', 0) + suffix_bigrams.get('-ey', {}).get('-or', 0)
                 + suffix_bigrams.get('-y', {}).get('-ol', 0) + suffix_bigrams.get('-y', {}).get('-or', 0))
if ey_y_total > 0:
    output.append(f"  -ey/-y followed by anything: {ey_y_total}")
    output.append(f"  -ey/-y followed by -ol/-or: {ey_y_to_ol_or} ({ey_y_to_ol_or/ey_y_total*100:.1f}%)")
    ol_or_baseline = sum(suffix_freq.get(s, 0) for s in ['-ol', '-or']) / len(all_entries) * 100
    output.append(f"  Baseline rate of -ol/-or in corpus: {ol_or_baseline:.1f}%")

# ============================================================
# 7. A/B SCRIBE MAPPING
# ============================================================
output.append("")
output.append("=" * 70)
output.append("7. A/B SCRIBE SUFFIX MAPPING")
output.append("=" * 70)

langA_suffixes = Counter()
langB_suffixes = Counter()
langA_stems = defaultdict(Counter)
langB_stems = defaultdict(Counter)
langA_words = 0
langB_words = 0

for folio, section, ref, word in all_entries:
    lang = folio_language.get(folio, '?')
    if lang == 'A':
        langA_words += 1
    elif lang == 'B':
        langB_words += 1
    suf = get_suffix(word)
    if not suf:
        continue
    stem = word[:-len(suf)+1]
    if lang == 'A':
        langA_suffixes[suf] += 1
        langA_stems[stem][suf] += 1
    elif lang == 'B':
        langB_suffixes[suf] += 1
        langB_stems[stem][suf] += 1

totalA = sum(langA_suffixes.values())
totalB = sum(langB_suffixes.values())

output.append(f"\nLanguage A: {langA_words} words ({totalA} with suffixes)")
output.append(f"Language B: {langB_words} words ({totalB} with suffixes)")
output.append(f"\n{'suffix':>8s} {'Lang_A':>8s} {'A_pct':>6s} {'Lang_B':>8s} {'B_pct':>6s} {'shift':>8s}")
output.append("-" * 50)
for suf in active_suffixes:
    a = langA_suffixes[suf]
    b = langB_suffixes[suf]
    a_pct = a/totalA*100 if totalA else 0
    b_pct = b/totalB*100 if totalB else 0
    shift = b_pct - a_pct
    marker = " ***" if abs(shift) > 3.0 else ""
    output.append(f"{suf:>8s} {a:8d} {a_pct:5.1f}% {b:8d} {b_pct:5.1f}% {shift:+7.1f}%{marker}")

# 7b. Shared stems
shared_stems = set(langA_stems.keys()) & set(langB_stems.keys())
output.append(f"\n7b. Stems appearing in both languages: {len(shared_stems)}")

mapping_evidence = []
for stem in shared_stems:
    a_top = langA_stems[stem].most_common(1)
    b_top = langB_stems[stem].most_common(1)
    if a_top and b_top and a_top[0][0] != b_top[0][0]:
        a_total = sum(langA_stems[stem].values())
        b_total = sum(langB_stems[stem].values())
        if a_total >= 3 and b_total >= 3:
            mapping_evidence.append((stem, a_top[0], b_top[0], a_total, b_total,
                                     dict(langA_stems[stem]), dict(langB_stems[stem])))

mapping_evidence.sort(key=lambda x: -(x[3]+x[4]))
output.append(f"Stems with different dominant suffix (min 3 each): {len(mapping_evidence)}")
for stem, (a_suf, a_cnt), (b_suf, b_cnt), a_tot, b_tot, a_dist, b_dist in mapping_evidence[:20]:
    output.append(f"  {stem:>12s}: A={a_dist}  B={b_dist}")

# 7c. Test specific mappings
output.append("")
output.append("7c. Testing ol<->edy, or<->eey, al<->dy, ar<->y:")
mappings_test = [('-ol', '-edy'), ('-or', '-eey'), ('-al', '-dy'), ('-ar', '-y')]
for suf_a, suf_b in mappings_test:
    stems_a = set(s for s in langA_stems if langA_stems[s].get(suf_a, 0) > 0)
    stems_b = set(s for s in langB_stems if langB_stems[s].get(suf_b, 0) > 0)
    overlap = stems_a & stems_b
    output.append(f"")
    output.append(f"  {suf_a}(A) <-> {suf_b}(B): A-stems={len(stems_a)}, B-stems={len(stems_b)}, overlap={len(overlap)}")
    for stem in list(overlap)[:5]:
        output.append(f"    '{stem}': A={dict(langA_stems[stem])}, B={dict(langB_stems[stem])}")

# 7d. Cross-language tracking
output.append("")
output.append("7d. Cross-language suffix tracking:")
for suf_a, suf_b in mappings_test:
    stems_with_suf_a = set(s for s in langA_stems if langA_stems[s].get(suf_a, 0) >= 1)
    b_suffix_dist = Counter()
    n_found_in_b = 0
    for stem in stems_with_suf_a:
        if stem in langB_stems:
            n_found_in_b += 1
            for s, c in langB_stems[stem].items():
                b_suffix_dist[s] += c
    output.append(f"  {suf_a} stems in A: {len(stems_with_suf_a)}, found in B: {n_found_in_b}")
    if b_suffix_dist:
        output.append(f"    Their B suffixes: {dict(b_suffix_dist.most_common(5))}")

# ============================================================
# 8. SUFFIX FLEXIBILITY
# ============================================================
output.append("")
output.append("=" * 70)
output.append("8. SUFFIX FLEXIBILITY ANALYSIS")
output.append("=" * 70)

output.append("\nHow many different suffixes does each stem take?")
for stem in top_stems:
    n_suf = len(stem_suffix[stem])
    total_tok = stem_counter[stem]
    dom_suf, dom_cnt = stem_suffix[stem].most_common(1)[0]
    dominance = dom_cnt / total_tok
    output.append(f"  {stem:>12s}: {n_suf:2d} suffixes, dominant={dom_suf}({dom_cnt}/{total_tok}, {dominance:.0%}), all={dict(stem_suffix[stem].most_common())}")

# Average suffix diversity
all_diversities = [len(stem_suffix[s]) for s in stem_counter if stem_counter[s] >= 5]
if all_diversities:
    avg_div = sum(all_diversities) / len(all_diversities)
    output.append(f"\n  Average suffix diversity (stems with >=5 tokens): {avg_div:.1f}")
    output.append(f"  Stems with >=5 tokens: {len(all_diversities)}")

print('\n'.join(output))
