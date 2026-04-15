import re
from collections import defaultdict, Counter

# Read the EVA transcription
with open("C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Parse text by folio
folio_texts = defaultdict(list)
current_folio = None
for line in text.split("\n"):
    m = re.match(r'<(f\d+[rv])>', line)
    if m:
        current_folio = m.group(1)
        continue
    m = re.match(r'<(f\d+[rv])\.\d+', line)
    if m:
        current_folio = m.group(1)
    if current_folio:
        clean = re.sub(r'<[^>]*>', '', line)
        clean = re.sub(r'\{[^}]*\}', '', clean)
        clean = re.sub(r'@\d+;?', '', clean)
        words = re.split(r'[.\s,<>]+', clean)
        words = [w.strip() for w in words if w.strip() and len(w.strip()) > 1]
        folio_texts[current_folio].extend(words)

def extract_stem_grade(word):
    """Extract vowel grade from a word."""
    if 'eod' in word:
        return 'eod'
    if 'eeo' in word:
        return 'eeo'
    if 'ee' in word:
        return 'ee'
    if 'eo' in word:
        return 'eo'
    if re.search(r'(?<![e])e(?![eo])', word):
        return 'e'
    return 'bare'

# Classification of herbal pages by dominant illustration feature
page_classifications = {
    3:  ('f1v', 'LEAF', 'small plant with green/yellow leaves'),
    4:  ('f2r', 'LEAF', 'large plant with many oval leaves, visible root'),
    5:  ('f2v', 'FLOWER', 'plant with prominent flower tufts at top, visible root'),
    6:  ('f3r', 'LEAF', 'single giant leaf dominates the page'),
    7:  ('f3v', 'ROOT', 'striped leaves but very prominent roots at bottom'),
    8:  ('f4r', 'FLOWER', 'prominent flower/seed head at top, curling leaves'),
    9:  ('f4v', 'LEAF', 'dense small leaves on branching stems'),
    10: ('f5r', 'ROOT', 'prominent tuber/root at bottom, bulbous'),
    11: ('f5v', 'LEAF', 'large rosette of green leaves'),
    12: ('f6r', 'FLOWER', 'small red/orange flowers with leaves and root'),
    13: ('f6v', 'FRUIT', 'spiny seed pods/fruits with jagged leaves'),
    14: ('f7r', 'FRUIT', 'star-shaped fruits/seeds on branches'),
    15: ('f7v', 'LEAF', 'star-shaped leaves, long root'),
    16: ('f8r', 'FRUIT', 'rosette leaves with red/orange fruits'),
    17: ('f8v', 'LEAF', 'large single heart/arrow leaf'),
    18: ('f9r', 'FLOWER', 'plant with small orange/red flowers, many leaves'),
    19: ('f9v', 'LEAF', 'lobed leaves with flower spike, prominent root'),
    20: ('f10r', 'FLOWER', 'prominent blue flowers dominate'),
}

grades_list = ['bare', 'e', 'ee', 'eo', 'eeo', 'eod']

# ============================================================
# HYPOTHESIS 1
# ============================================================
print("=" * 80)
print("HYPOTHESIS 1: VOWEL GRADE = PLANT PART")
print("=" * 80)
print()

feature_groups = defaultdict(list)
for page, (folio, feature, notes) in page_classifications.items():
    feature_groups[feature].append(folio)

feature_grade_counts = {}
print(f"{'Feature':<10} {'bare':>6} {'e':>6} {'ee':>6} {'eo':>5} {'eeo':>5} {'eod':>5} {'Total':>6}")
print("-" * 55)

for feature in ['LEAF', 'ROOT', 'FLOWER', 'FRUIT']:
    folios = feature_groups[feature]
    total_grades = Counter()
    for folio in folios:
        words = folio_texts.get(folio, [])
        for w in words:
            grade = extract_stem_grade(w)
            total_grades[grade] += 1
    total = sum(total_grades.values())
    feature_grade_counts[feature] = (total_grades, total)
    print(f"{feature:<10} {total_grades['bare']:>6} {total_grades['e']:>6} {total_grades['ee']:>6} {total_grades['eo']:>5} {total_grades['eeo']:>5} {total_grades['eod']:>5} {total:>6}")

print()
print("Grade proportions (%):")
print(f"{'Feature':<10} {'bare':>7} {'e':>7} {'ee':>7} {'eo':>6} {'eeo':>6} {'eod':>6}")
print("-" * 55)
for feature in ['LEAF', 'ROOT', 'FLOWER', 'FRUIT']:
    grades, total = feature_grade_counts[feature]
    if total > 0:
        vals = [f"{100*grades[g]/total:.1f}%" for g in grades_list]
        print(f"{feature:<10} {vals[0]:>7} {vals[1]:>7} {vals[2]:>7} {vals[3]:>6} {vals[4]:>6} {vals[5]:>6}")

# ============================================================
# HYPOTHESIS 2
# ============================================================
print()
print("=" * 80)
print("HYPOTHESIS 2: GRADE = PROCESSING STAGE")
print("=" * 80)
print()

herbal_folios = [f"f{n}{s}" for n in range(1, 58) for s in ['r', 'v']]
recipe_folios = [f"f{n}{s}" for n in range(99, 117) for s in ['r', 'v']]

def count_section_grades(folio_list):
    total_grades = Counter()
    word_count = 0
    folio_count = 0
    for folio in folio_list:
        words = folio_texts.get(folio, [])
        if words:
            folio_count += 1
            word_count += len(words)
            for w in words:
                grade = extract_stem_grade(w)
                total_grades[grade] += 1
    return total_grades, word_count, folio_count

herbal_grades, herbal_words, herbal_fc = count_section_grades(herbal_folios)
recipe_grades, recipe_words, recipe_fc = count_section_grades(recipe_folios)

print(f"Section analysis:")
print(f"  Herbal: {herbal_fc} folios, {herbal_words} words")
print(f"  Recipe: {recipe_fc} folios, {recipe_words} words")
print()

print(f"{'Section':<10} {'bare':>6} {'e':>6} {'ee':>6} {'eo':>5} {'eeo':>5} {'eod':>5} {'Total':>6}")
print("-" * 55)
for name, grd, total in [("Herbal", herbal_grades, herbal_words), ("Recipe", recipe_grades, recipe_words)]:
    print(f"{name:<10} {grd['bare']:>6} {grd['e']:>6} {grd['ee']:>6} {grd['eo']:>5} {grd['eeo']:>5} {grd['eod']:>5} {total:>6}")

print()
print("Grade proportions (%):")
print(f"{'Section':<10} {'bare':>7} {'e':>7} {'ee':>7} {'eo':>6} {'eeo':>6} {'eod':>6}")
print("-" * 55)
for name, grd, total in [("Herbal", herbal_grades, herbal_words), ("Recipe", recipe_grades, recipe_words)]:
    if total > 0:
        vals = [f"{100*grd[g]/total:.1f}%" for g in grades_list]
        print(f"{name:<10} {vals[0]:>7} {vals[1]:>7} {vals[2]:>7} {vals[3]:>6} {vals[4]:>6} {vals[5]:>6}")

# Enrichment ratios
print()
print("Enrichment ratio (Recipe / Herbal):")
for g in grades_list:
    h_pct = 100 * herbal_grades[g] / herbal_words if herbal_words else 0
    r_pct = 100 * recipe_grades[g] / recipe_words if recipe_words else 0
    ratio = r_pct / h_pct if h_pct > 0 else float('inf')
    print(f"  {g:<6}: {ratio:.3f}x  (Herbal {h_pct:.1f}% vs Recipe {r_pct:.1f}%)")

# ============================================================
# HYPOTHESIS 3
# ============================================================
print()
print("=" * 80)
print("HYPOTHESIS 3: GRADE = SPECIFICITY (page spread)")
print("=" * 80)
print()

print(f"{'Grade':<8} {'Distinct Words':>15} {'Folios with':>15} {'Avg Folios/Word':>16}")
print("-" * 60)

avg_pages_per_grade = {}
for grade in grades_list:
    grade_words_all = set()
    for folio, words in folio_texts.items():
        for w in words:
            if extract_stem_grade(w) == grade:
                grade_words_all.add(w)

    word_page_counts = []
    for word in grade_words_all:
        pages_with_word = sum(1 for folio, words in folio_texts.items() if word in words)
        word_page_counts.append(pages_with_word)

    if word_page_counts:
        avg = sum(word_page_counts) / len(word_page_counts)
        avg_pages_per_grade[grade] = avg
        n_words = len(grade_words_all)
        n_folios = len(set(f for f, ws in folio_texts.items() for w in ws if extract_stem_grade(w) == grade))
        print(f"{grade:<8} {n_words:>15} {n_folios:>15} {avg:>16.2f}")

# Pearson correlation
x_vals = list(range(len(grades_list)))
y_vals = [avg_pages_per_grade.get(g, 0) for g in grades_list]
n = len(x_vals)
x_mean = sum(x_vals) / n
y_mean = sum(y_vals) / n
num = sum((x_vals[i] - x_mean) * (y_vals[i] - y_mean) for i in range(n))
dx = sum((x_vals[i] - x_mean) ** 2 for i in range(n)) ** 0.5
dy = sum((y_vals[i] - y_mean) ** 2 for i in range(n)) ** 0.5
if dx > 0 and dy > 0:
    r = num / (dx * dy)
    print(f"\nPearson r (grade level vs avg page spread) = {r:.4f}")
    if r < -0.7:
        print("STRONG negative correlation -> SUPPORTS specificity hypothesis")
    elif r < -0.3:
        print("Moderate negative correlation -> Partially supports specificity")
    elif r > 0.3:
        print("Positive correlation -> CONTRADICTS specificity hypothesis")
    else:
        print("Weak/no correlation -> DOES NOT support specificity hypothesis")

# ============================================================
# CHI-SQUARED TESTS
# ============================================================
print()
print("=" * 80)
print("CHI-SQUARED TESTS")
print("=" * 80)
print()

def chi_squared_test(table):
    n_rows = len(table)
    n_cols = len(table[0])
    row_totals = [sum(row) for row in table]
    col_totals = [sum(table[r][c] for r in range(n_rows)) for c in range(n_cols)]
    grand_total = sum(row_totals)
    if grand_total == 0:
        return 0, 0
    chi2 = 0
    for r in range(n_rows):
        for c in range(n_cols):
            expected = (row_totals[r] * col_totals[c]) / grand_total
            if expected > 0:
                chi2 += (table[r][c] - expected) ** 2 / expected
    df = (n_rows - 1) * (n_cols - 1)
    return chi2, df

# H1
table_h1 = []
for feature in ['LEAF', 'ROOT', 'FLOWER', 'FRUIT']:
    g, t = feature_grade_counts[feature]
    table_h1.append([g[grade] for grade in grades_list])

chi2_h1, df_h1 = chi_squared_test(table_h1)
print(f"H1 (Plant Part): chi2 = {chi2_h1:.2f}, df = {df_h1}")
# Critical values for df=15: p=0.05 -> 25.00, p=0.01 -> 30.58
cv_05 = {5: 11.07, 10: 18.31, 15: 25.00, 20: 31.41}
cv_01 = {5: 15.09, 10: 23.21, 15: 30.58, 20: 37.57}
print(f"  Critical value (p=0.05, df={df_h1}): {cv_05.get(df_h1, '?')}")
print(f"  Result: {'SIGNIFICANT' if chi2_h1 > cv_05.get(df_h1, 999) else 'NOT SIGNIFICANT'} at p=0.05")

# H2
table_h2 = [
    [herbal_grades[g] for g in grades_list],
    [recipe_grades[g] for g in grades_list],
]
chi2_h2, df_h2 = chi_squared_test(table_h2)
print(f"\nH2 (Processing Stage): chi2 = {chi2_h2:.2f}, df = {df_h2}")
print(f"  Critical value (p=0.05, df={df_h2}): {cv_05.get(df_h2, '?')}")
print(f"  Result: {'SIGNIFICANT' if chi2_h2 > cv_05.get(df_h2, 999) else 'NOT SIGNIFICANT'} at p=0.05")

# ============================================================
# STEM CHAIN ANALYSIS
# ============================================================
print()
print("=" * 80)
print("STEM CHAIN FREQUENCY ANALYSIS")
print("=" * 80)
print()

all_words = []
for folio, words in folio_texts.items():
    all_words.extend(words)
word_counter = Counter(all_words)

stem_chains = {
    'k-chain':  ['ky', 'key', 'keey', 'keeoy', 'keeody'],
    'ch-chain': ['chy', 'chey', 'cheey', 'cheeoy', 'cheeody'],
    'sh-chain': ['shy', 'shey', 'sheey', 'sheeoy', 'sheeody'],
    'ok-chain': ['oky', 'okey', 'okeey', 'okeeoy', 'okeeody'],
    'd-chain':  ['dy', 'dey', 'deey', 'deeoy', 'deeody'],
}

# Also look for words containing these patterns (not just exact match)
for chain_name, patterns in stem_chains.items():
    print(f"  {chain_name}:")
    for pat in patterns:
        # Words containing this pattern
        contains = [(w, word_counter[w]) for w in word_counter if pat in w]
        total_tokens = sum(c for _, c in contains)
        print(f"    contains '{pat}': {len(contains):>4} types, {total_tokens:>6} tokens")
    print()

# More focused: look at common grade-bearing words
print("Most common words by grade:")
for grade in grades_list:
    grade_counter = Counter()
    for w in all_words:
        if extract_stem_grade(w) == grade:
            grade_counter[w] += 1
    print(f"\n  {grade.upper()} grade (top 10):")
    for w, c in grade_counter.most_common(10):
        print(f"    {w:<20} {c:>5}")

# ============================================================
# PER-PAGE GRADE DETAIL
# ============================================================
print()
print("=" * 80)
print("PER-PAGE GRADE DISTRIBUTION (classified pages)")
print("=" * 80)
print()

for page_num in sorted(page_classifications.keys()):
    folio, feature, notes = page_classifications[page_num]
    words = folio_texts.get(folio, [])

    grade_words = defaultdict(list)
    for w in words:
        g = extract_stem_grade(w)
        grade_words[g].append(w)

    total = len(words)
    print(f"Page {page_num:>3} ({folio}) [{feature}] - {notes}")
    for g in grades_list:
        count = len(grade_words[g])
        pct = 100 * count / total if total else 0
        sample = ', '.join(sorted(set(grade_words[g]))[:5])
        print(f"  {g:<6}: {count:>3} ({pct:>5.1f}%)  e.g. {sample}")
    print()
