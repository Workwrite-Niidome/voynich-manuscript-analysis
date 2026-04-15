import re
from collections import defaultdict, Counter

filepath = 'C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_section = None
parsed_lines = []

for line in lines:
    line = line.strip()
    if line.startswith('<f') and '$I=' in line:
        m = re.search(r'\$I=(\w+)', line)
        if m:
            current_section = m.group(1)
        continue

    line_m = re.match(r'<(f\d+[rv]?)\.(\d+)', line)
    if line_m and current_section:
        folio = line_m.group(1)
        line_num = int(line_m.group(2))
        text_part = re.sub(r'^<[^>]+>\s*', '', line)
        text_part = re.sub(r'@\d+;?', '', text_part)
        text_part = re.sub(r'\{[^}]+\}', '', text_part)
        text_part = re.sub(r'<->', '.', text_part)
        words = [w.strip() for w in re.split(r'[.,\s]+', text_part) if w.strip()]
        parsed_lines.append((folio, line_num, current_section, words))

print(f"Total parsed lines: {len(parsed_lines)}")
section_counts = Counter(s for _,_,s,_ in parsed_lines)
print(f"Section distribution: {dict(section_counts)}")

# ============================================================
# 1. QO- WORD INVENTORY
# ============================================================
qo_words = Counter()
qo_section = defaultdict(lambda: Counter())

for folio, lnum, sec, words in parsed_lines:
    for w in words:
        if w.startswith('qo'):
            qo_words[w] += 1
            qo_section[w][sec] += 1

print("\n=== QO- WORD FREQUENCIES (top 25) ===")
for word, count in qo_words.most_common(25):
    secs = dict(qo_section[word])
    print(f"  {word:20s} {count:5d}  sections: {secs}")

# ============================================================
# 2. RECIPE LINE POSITION
# ============================================================
recipe_lines_data = [(folio, lnum, words) for folio, lnum, sec, words in parsed_lines if sec == 'P']
recipe_folios = defaultdict(list)
for folio, lnum, words in recipe_lines_data:
    recipe_folios[folio].append((lnum, words))

qo_positions = defaultdict(list)

for folio, lines_in_folio in recipe_folios.items():
    max_line = max(ln for ln, _ in lines_in_folio)
    min_line = min(ln for ln, _ in lines_in_folio)
    span = max_line - min_line if max_line > min_line else 1

    for lnum, words_list in lines_in_folio:
        norm_pos = (lnum - min_line) / span if span > 0 else 0.5
        for w in words_list:
            if w.startswith('qok'):
                qo_positions[w].append(norm_pos)

print("\n=== RECIPE LINE POSITION (normalized 0=start, 1=end) ===")
target_words = ['qokeeey', 'qokeey', 'qokeedy', 'qokey', 'qokedy', 'qokain', 'qokaiin', 'qokal', 'qoky', 'qokar', 'qokol', 'qokeed', 'qokam']
results = []
for w in target_words:
    positions = qo_positions.get(w, [])
    if positions:
        avg = sum(positions) / len(positions)
        results.append((avg, w, len(positions), min(positions), max(positions)))

for avg, w, n, mn, mx in sorted(results):
    print(f"  {w:15s}  avg={avg:.3f}  n={n:3d}  min={mn:.3f}  max={mx:.3f}")

# ============================================================
# 3. DOUBLING PATTERNS
# ============================================================
print("\n=== DOUBLING PATTERNS (qo- word repeated consecutively) ===")
double_counts = Counter()

for folio, lnum, sec, words in parsed_lines:
    for i in range(len(words) - 1):
        if words[i].startswith('qo') and words[i] == words[i+1]:
            double_counts[words[i]] += 1

for word, count in double_counts.most_common(20):
    total = qo_words[word]
    pct = count / total * 100 if total else 0
    print(f"  {word:20s} doubled {count:3d} times  (total: {total}, doubled%: {pct:.1f}%)")

# ============================================================
# 4. FREQUENCY RATIOS
# ============================================================
print("\n=== FREQUENCY RATIOS (recipe section only) ===")
qo_recipe = Counter()
for folio, lnum, sec, words in parsed_lines:
    if sec == 'P':
        for w in words:
            if w.startswith('qok'):
                qo_recipe[w] += 1

print("Recipe frequencies:")
for w in target_words:
    print(f"  {w:15s}  recipe={qo_recipe.get(w,0):4d}  total={qo_words.get(w,0):4d}")

r_ain = qo_recipe.get('qokain', 0)
r_eey = qo_recipe.get('qokeey', 0)
r_key = qo_recipe.get('qokey', 0)
r_aiin = qo_recipe.get('qokaiin', 0)
r_eeey = qo_recipe.get('qokeeey', 0)

print(f"\nRatios (recipe only):")
if r_ain > 0:
    print(f"  qokeey:qokain = {r_eey}:{r_ain} = {r_eey/r_ain:.1f}:1  (expected ~8:1 if drachma:ounce)")
if r_key > 0:
    print(f"  qokeey:qokey  = {r_eey}:{r_key} = {r_eey/r_key:.1f}:1  (expected ~3:1 if drachma:scruple)")
if r_eeey > 0:
    print(f"  qokeey:qokeeey = {r_eey}:{r_eeey} = {r_eey/r_eeey:.1f}:1  (expected ~96:1 if drachma:pound)")
if r_aiin > 0:
    print(f"  qokeey:qokaiin = {r_eey}:{r_aiin} = {r_eey/r_aiin:.1f}:1")

# ============================================================
# 5. SEQUENTIAL PATTERNS in recipes
# ============================================================
print("\n=== SEQUENTIAL QO-K PATTERNS IN RECIPES ===")
seq_counts = Counter()
for folio, lnum, sec, words in parsed_lines:
    if sec == 'P':
        qo_in_line = [w for w in words if w.startswith('qok')]
        for i in range(len(qo_in_line) - 1):
            pair = (qo_in_line[i], qo_in_line[i+1])
            seq_counts[pair] += 1

for (w1, w2), count in seq_counts.most_common(20):
    print(f"  {w1:15s} -> {w2:15s}  {count:3d} times")

# ============================================================
# 6. "ANA" PATTERN
# ============================================================
print("\n=== WORDS BETWEEN CONSECUTIVE QO- WORDS (recipe) ===")
between_words = Counter()
for folio, lnum, sec, words in parsed_lines:
    if sec == 'P':
        for i in range(len(words)):
            if words[i].startswith('qo'):
                for j in range(i+1, min(i+4, len(words))):
                    if words[j].startswith('qo'):
                        between = tuple(words[i+1:j])
                        if between:
                            between_words[between] += 1
                        break

print("Words appearing between consecutive qo- words:")
for words_tuple, count in between_words.most_common(20):
    print(f"  {str(words_tuple):40s}  {count:3d} times")

# ============================================================
# 7. OK- vs QO-K comparison
# ============================================================
print("\n=== OK- WORD FREQUENCIES (top 15) ===")
ok_words = Counter()
ok_section_data = defaultdict(lambda: Counter())
for folio, lnum, sec, words in parsed_lines:
    for w in words:
        if re.match(r'^ok[a-z]', w):
            ok_words[w] += 1
            ok_section_data[w][sec] += 1

for word, count in ok_words.most_common(15):
    secs = dict(ok_section_data[word])
    print(f"  {word:20s} {count:5d}  sections: {secs}")

# ============================================================
# 8. GRADE SYSTEM CONSISTENCY
# ============================================================
print("\n=== GRADE SYSTEM: vowel count vs recipe position ===")
grade_map = {
    'qoky': ('bare', 0),
    'qokey': ('e', 1),
    'qokedy': ('e+dy', 1),
    'qokeey': ('ee', 2),
    'qokeedy': ('ee+dy', 2),
    'qokeeey': ('eee', 3),
}
for w, (grade, level) in sorted(grade_map.items(), key=lambda x: x[1][1]):
    positions = qo_positions.get(w, [])
    if positions:
        avg = sum(positions) / len(positions)
        print(f"  Grade {level} ({grade:8s}) {w:15s}  position={avg:.3f}  freq={qo_words.get(w,0)}")

# ============================================================
# 9. AN PATTERN: multi-measurement lines
# ============================================================
print("\n=== RECIPE LINES WITH 2+ QO-K WORDS (first 20) ===")
multi_qo_lines = []
for folio, lnum, sec, words in parsed_lines:
    if sec == 'P':
        qo_in_line = [w for w in words if w.startswith('qok')]
        if len(qo_in_line) >= 2:
            multi_qo_lines.append((folio, lnum, words, qo_in_line))

for folio, lnum, words, qo_list in multi_qo_lines[:20]:
    qo_str = ' '.join(qo_list)
    print(f"  {folio}.{lnum}: [{qo_str}]  full: {' '.join(words[:12])}...")

# ============================================================
# 10. WORD-POSITION ANALYSIS (within line, not across folio)
# ============================================================
print("\n=== WITHIN-LINE POSITION (word index / total words) ===")
qo_word_pos = defaultdict(list)
for folio, lnum, sec, words in parsed_lines:
    if sec == 'P' and len(words) > 1:
        for i, w in enumerate(words):
            if w.startswith('qok'):
                norm = i / (len(words) - 1)
                qo_word_pos[w].append(norm)

results2 = []
for w in target_words:
    positions = qo_word_pos.get(w, [])
    if positions:
        avg = sum(positions) / len(positions)
        results2.append((avg, w, len(positions)))

print("Word position within line (0=first word, 1=last word):")
for avg, w, n in sorted(results2):
    print(f"  {w:15s}  avg={avg:.3f}  n={n:3d}")

# ============================================================
# 11. CO-OCCURRENCE with plant words
# ============================================================
print("\n=== QO-K + PLANT WORD CO-OCCURRENCE (same line, recipe) ===")
plant_prefixes = ['ch', 'sh', 'cth']
qo_plant_cooccur = defaultdict(Counter)
for folio, lnum, sec, words in parsed_lines:
    if sec == 'P':
        qo_in = [w for w in words if w.startswith('qok')]
        plant_in = [w for w in words if any(w.startswith(p) for p in plant_prefixes)]
        for q in qo_in:
            for p in plant_in:
                qo_plant_cooccur[q][p] += 1

print("Top plant-word co-occurrences for key measurement words:")
for qw in ['qokaiin', 'qokeey', 'qokain', 'qokal']:
    top_plants = qo_plant_cooccur[qw].most_common(5)
    if top_plants:
        plants_str = ', '.join(f"{p}({c})" for p,c in top_plants)
        print(f"  {qw:15s}: {plants_str}")
