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
current_section = ''
all_entries = []
folio_lines_map = defaultdict(list)
folio_language = {}

for line in lines:
    line = line.strip()
    folio_match = re.match(r'<(f\d+[rv])>', line)
    if folio_match:
        current_folio = folio_match.group(1)
        current_section = classify_section(current_folio)
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
    folio_lines_map[current_folio].append((ref, words))
    for w in words:
        all_entries.append((current_folio, current_section, ref, w))

folio_total_lines = {f: len(lns) for f, lns in folio_lines_map.items()}

suffixes_ordered = ['-aiin', '-ain', '-eey', '-edy', '-am', '-an', '-ar', '-al', '-ol', '-or', '-ey', '-dy', '-y']

def get_suffix(word):
    for suf in suffixes_ordered:
        s = suf[1:]
        if word.endswith(s) and len(word) > len(s):
            return suf
    return None

# ============================================================
# 1. SECTION DISTRIBUTION
# ============================================================
output = []
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

for suf in suffixes_ordered:
    total = sum(suffix_section_counts[suf].values())
    if total < 40:
        continue
    output.append("")
    output.append(f"{suf} (n={total}):")
    for sec in sections_list:
        cnt = suffix_section_counts[suf][sec]
        pct = cnt / total * 100 if total else 0
        exp = section_totals[sec] / sum(section_totals.values()) * 100
        ratio = pct / exp if exp else 0
        output.append(f"  {sec:8s}: {cnt:4d} ({pct:5.1f}%)  expected: {exp:5.1f}%  ratio: {ratio:.2f}")

# ============================================================
# 2. POSITION IN ENTRY
# ============================================================
output.append("")
output.append("=" * 70)
output.append("2. POSITION IN HERBAL ENTRIES")
output.append("=" * 70)

suffix_positions = defaultdict(list)
for folio, section, ref, word in all_entries:
    if section != 'herbal':
        continue
    m = re.match(r'f\d+[rv]\.(\d+)', ref)
    if not m:
        continue
    line_num = int(m.group(1))
    total = folio_total_lines.get(folio, 1)
    rel_pos = line_num / total
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
    output.append("")
    output.append(f"{suf} (n={total}, mean_pos={avg:.3f}):")
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
for folio, section, ref, word in all_entries:
    suf = get_suffix(word)
    if suf:
        stem = word[:-len(suf)+1]
        stem_counter[stem] += 1
        stem_suffix[stem][suf] += 1

top_stems = [s for s, c in stem_counter.most_common(30)]
active_suffixes = [s for s in suffixes_ordered if sum(suffix_section_counts[s].values()) >= 40]

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

total_leaf = sum(1 for f, s, r, w in all_entries if f in leaf_pages)
total_root = sum(1 for f, s, r, w in all_entries if f in root_pages)
baseline = total_leaf / (total_leaf + total_root) if (total_leaf + total_root) else 0

output.append(f"")
output.append(f"{'suffix':>8s} {'leaf':>6s} {'root':>6s} {'L/(L+R)':>8s}  baseline={baseline:.3f}")
output.append("-" * 45)
for suf in active_suffixes:
    l = suffix_leaf[suf]
    r = suffix_root[suf]
    total = l + r
    ratio = l / total if total else 0
    output.append(f"{suf:>8s} {l:6d} {r:6d} {ratio:8.3f}")

# ============================================================
# 5. PREPARATION METHODS TEST
# ============================================================
output.append("")
output.append("=" * 70)
output.append("5. TEST: SUFFIXES = PREPARATION METHODS (herbal vs recipe)")
output.append("=" * 70)

herbal_total = section_totals['herbal']
recipe_total = section_totals['recipe']

output.append(f"")
output.append(f"{'suffix':>8s} {'herbal_rate':>12s} {'recipe_rate':>12s} {'ratio(R/H)':>12s}")
output.append("-" * 50)
for suf in active_suffixes:
    h = suffix_section_counts[suf]['herbal']
    r = suffix_section_counts[suf]['recipe']
    h_rate = h / herbal_total * 100
    r_rate = r / recipe_total * 100
    ratio = r_rate / h_rate if h_rate else float('inf')
    output.append(f"{suf:>8s} {h_rate:12.2f} {r_rate:12.2f} {ratio:12.2f}")

# ============================================================
# 6. GRAMMATICAL ROLES TEST
# ============================================================
output.append("")
output.append("=" * 70)
output.append("6. TEST: SUFFIXES = GRAMMATICAL ROLES")
output.append("=" * 70)

line_words = []
for folio, section, ref, word in all_entries:
    if not line_words or line_words[-1][0] != ref:
        line_words.append((ref, [word]))
    else:
        line_words[-1][1].append(word)

suffix_next_suffix = defaultdict(Counter)
suffix_after_daiin = Counter()
total_after_daiin = 0

for ref, words in line_words:
    for i, w in enumerate(words):
        suf = get_suffix(w)
        if suf and i + 1 < len(words):
            next_suf = get_suffix(words[i+1])
            suffix_next_suffix[suf][next_suf if next_suf else 'NONE'] += 1
        if i > 0 and words[i-1] in ('daiin', 'dain'):
            total_after_daiin += 1
            suf_w = get_suffix(w)
            if suf_w:
                suffix_after_daiin[suf_w] += 1

output.append("")
output.append("6a. What suffix follows each suffix type (top 3):")
for suf in active_suffixes:
    total = sum(suffix_next_suffix[suf].values())
    if total < 10:
        continue
    top3 = suffix_next_suffix[suf].most_common(3)
    desc = ", ".join(f"{s}:{c}({c/total*100:.0f}%)" for s, c in top3)
    output.append(f"  {suf}: {desc}")

output.append(f"")
output.append(f"6b. Words appearing after daiin/dain (total={total_after_daiin}):")
for suf, cnt in suffix_after_daiin.most_common():
    output.append(f"  {suf}: {cnt} ({cnt/total_after_daiin*100:.1f}%)")

output.append("")
output.append("6c. Line-initial vs line-final position:")
suffix_line_initial = Counter()
suffix_line_final = Counter()
for ref, words in line_words:
    if words:
        s1 = get_suffix(words[0])
        if s1:
            suffix_line_initial[s1] += 1
        sn = get_suffix(words[-1])
        if sn:
            suffix_line_final[sn] += 1

output.append(f"{'suffix':>8s} {'initial':>8s} {'final':>8s} {'I/(I+F)':>8s}")
for suf in active_suffixes:
    ini = suffix_line_initial[suf]
    fin = suffix_line_final[suf]
    total = ini + fin
    ratio = ini / total if total else 0
    output.append(f"{suf:>8s} {ini:8d} {fin:8d} {ratio:8.3f}")

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

for folio, section, ref, word in all_entries:
    lang = folio_language.get(folio, '?')
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

output.append(f"")
output.append(f"Suffix distribution by Currier language (A: {totalA} tokens, B: {totalB} tokens):")
output.append(f"{'suffix':>8s} {'Lang_A':>8s} {'Lang_B':>8s} {'A_pct':>6s} {'B_pct':>6s}")
for suf in active_suffixes:
    a = langA_suffixes[suf]
    b = langB_suffixes[suf]
    a_pct = f"{a/totalA*100:.1f}" if totalA else "0"
    b_pct = f"{b/totalB*100:.1f}" if totalB else "0"
    output.append(f"{suf:>8s} {a:8d} {b:8d} {a_pct:>5s}% {b_pct:>5s}%")

shared_stems = set(langA_stems.keys()) & set(langB_stems.keys())
output.append(f"")
output.append(f"7b. Stems in both languages: {len(shared_stems)}")

mapping_evidence = []
for stem in shared_stems:
    a_top = langA_stems[stem].most_common(1)
    b_top = langB_stems[stem].most_common(1)
    if a_top and b_top and a_top[0][0] != b_top[0][0]:
        a_total = sum(langA_stems[stem].values())
        b_total = sum(langB_stems[stem].values())
        if a_total >= 3 and b_total >= 3:
            mapping_evidence.append((stem, a_top[0], b_top[0], a_total, b_total))

mapping_evidence.sort(key=lambda x: -(x[3]+x[4]))
output.append(f"Stems with different dominant suffix in A vs B (min 3 each):")
for stem, (a_suf, a_cnt), (b_suf, b_cnt), a_tot, b_tot in mapping_evidence[:20]:
    output.append(f"  {stem:>12s}: A={a_suf}({a_cnt}/{a_tot})  B={b_suf}({b_cnt}/{b_tot})")

output.append("")
output.append("7c. Testing mapping hypothesis (ol<->edy, or<->eey, al<->dy, ar<->y):")
mappings_test = [('-ol', '-edy'), ('-or', '-eey'), ('-al', '-dy'), ('-ar', '-y')]
for suf_a, suf_b in mappings_test:
    stems_a = set(s for s in langA_stems if langA_stems[s].get(suf_a, 0) > 0)
    stems_b = set(s for s in langB_stems if langB_stems[s].get(suf_b, 0) > 0)
    overlap = stems_a & stems_b
    output.append(f"")
    output.append(f"  {suf_a} (A) <-> {suf_b} (B):")
    output.append(f"    Stems with {suf_a} in A: {len(stems_a)}")
    output.append(f"    Stems with {suf_b} in B: {len(stems_b)}")
    output.append(f"    Overlap: {len(overlap)}")
    for stem in list(overlap)[:5]:
        output.append(f"      stem='{stem}': A-{suf_a}={langA_stems[stem].get(suf_a,0)}, B-{suf_b}={langB_stems[stem].get(suf_b,0)}")

output.append("")
output.append("7d. Cross-language stem tracking (do -ol stems in A become -edy in B?):")
for suf_a, suf_b in mappings_test:
    stems_with_suf_a_in_A = set(s for s in langA_stems if langA_stems[s].get(suf_a, 0) >= 2)
    if not stems_with_suf_a_in_A:
        output.append(f"  No stems with {suf_a}(>=2) in A")
        continue
    b_suffix_dist = Counter()
    for stem in stems_with_suf_a_in_A:
        if stem in langB_stems:
            for s, c in langB_stems[stem].items():
                b_suffix_dist[s] += c
    if b_suffix_dist:
        output.append(f"  Stems with {suf_a}(>=2) in A -> their B suffixes: {dict(b_suffix_dist.most_common(5))}")
    else:
        output.append(f"  Stems with {suf_a}(>=2) in A -> no occurrences in B")

# ============================================================
# SUMMARY: suffix flexibility vs specialization
# ============================================================
output.append("")
output.append("=" * 70)
output.append("8. SUFFIX FLEXIBILITY ANALYSIS")
output.append("=" * 70)
output.append("")
output.append("How many different suffixes does each stem take?")

stem_diversity = {}
for stem in top_stems:
    n_suffixes = len(stem_suffix[stem])
    total_tokens = stem_counter[stem]
    top_suf = stem_suffix[stem].most_common(1)[0]
    dominance = top_suf[1] / total_tokens
    stem_diversity[stem] = (n_suffixes, total_tokens, top_suf, dominance)

for stem in top_stems:
    n_suf, total, (dom_suf, dom_cnt), dominance = stem_diversity[stem]
    output.append(f"  {stem:>12s}: {n_suf} suffixes, dominant={dom_suf}({dom_cnt}/{total}, {dominance:.0%})")

print('\n'.join(output))
