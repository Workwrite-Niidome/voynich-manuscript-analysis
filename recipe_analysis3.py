import re, sys, io
from collections import Counter, defaultdict
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open("C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find recipe section boundaries
recipe_start = None
recipe_end = None
for i, line in enumerate(lines):
    if '<f88r>' in line and recipe_start is None:
        recipe_start = i
    if recipe_start is not None and i > recipe_start:
        folio_match = re.match(r'<(f(\d+))', line)
        if folio_match:
            fnum = int(folio_match.group(2))
            if fnum > 116:
                recipe_end = i
                break
if recipe_end is None:
    recipe_end = len(lines)

recipe_text_lines = lines[recipe_start:recipe_end]

# Herbal section
herbal_end = None
for i, line in enumerate(lines):
    if '<f58r>' in line:
        herbal_end = i
        break
herbal_text_lines = lines[0:herbal_end or 500]

def extract_words(text_lines):
    words = []
    for line in text_lines:
        line = line.strip()
        if line.startswith('#'):
            continue
        match = re.match(r'<[^>]+>\s+(.*)', line)
        if match:
            text = match.group(1)
        else:
            continue
        text = re.sub(r'@\d+;?', '', text)
        text = re.sub(r'\{[^}]+\}', '', text)
        text = re.sub(r'<[^>]*>', '', text)
        text = re.sub(r"['\?\*,]", '', text)
        tokens = re.split(r'[\s.]+', text)
        for t in tokens:
            t = re.sub(r'[^a-z]', '', t.strip())
            if t and len(t) > 1:
                words.append(t)
    return words

recipe_words = extract_words(recipe_text_lines)
herbal_words = extract_words(herbal_text_lines)
recipe_freq = Counter(recipe_words)
herbal_freq = Counter(herbal_words)
herbal_set = set(herbal_words)

# ============================================================
# DETAILED RECIPE PARAGRAPH ANALYSIS
# Extract word sequences per recipe paragraph (between @Lc markers)
# ============================================================
print("=== DETAILED RECIPE PARAGRAPH STRUCTURE ===")

# Parse recipes as structured blocks
recipes = []
current = {"title": "", "lf_words": [], "paragraph_words": []}
for line in recipe_text_lines:
    line = line.strip()
    if '@Lc' in line:
        if current["paragraph_words"] or current["lf_words"]:
            recipes.append(current)
        match = re.match(r'<[^>]+>\s+(.*)', line)
        title = match.group(1) if match else ""
        current = {"title": title, "lf_words": [], "paragraph_words": []}
    elif '@Lf' in line:
        match = re.match(r'<[^>]+>\s+(.*)', line)
        if match:
            text = match.group(1)
            text = re.sub(r'@\d+;?', '', text)
            text = re.sub(r'\{[^}]+\}', '', text)
            text = re.sub(r"['\?\*,.<>]", '', text).strip()
            t = re.sub(r'[^a-z\s]', '', text).strip()
            if t:
                current["lf_words"].append(t)
    elif '@P0' in line or '+P0' in line:
        match = re.match(r'<[^>]+>\s+(.*)', line)
        if match:
            text = match.group(1)
            text = re.sub(r'@\d+;?', '', text)
            text = re.sub(r'\{[^}]+\}', '', text)
            text = re.sub(r'<[^>]*>', '', text)
            text = re.sub(r"['\?\*,]", '', text)
            tokens = re.split(r'[\s.]+', text)
            for t in tokens:
                t = re.sub(r'[^a-z]', '', t.strip())
                if t and len(t) > 1:
                    current["paragraph_words"].append(t)
if current["paragraph_words"] or current["lf_words"]:
    recipes.append(current)

# Print first 5 recipes in detail
for i, r in enumerate(recipes[:8]):
    print(f"\n--- Recipe {i+1}: {r['title']} ---")
    print(f"  @Lf ingredients: {r['lf_words']}")
    # Show paragraph words in groups showing qo-word patterns
    words = r["paragraph_words"]
    # Identify ingredient+quantity pairs
    pairs = []
    j = 0
    while j < len(words):
        if j+1 < len(words) and words[j+1].startswith('qo'):
            pairs.append(f"  [{words[j]}] -> {words[j+1]}")
            j += 2
        elif words[j].startswith('qo'):
            pairs.append(f"  [?] -> {words[j]}")
            j += 1
        else:
            pairs.append(f"  {words[j]}")
            j += 1
    print(f"  Paragraph ({len(words)} words):")
    for p in pairs[:30]:
        print(f"    {p}")

# ============================================================
# PATTERN: word BEFORE qo-word, grouped by qo-word type
# This reveals which ingredients get which quantity types
# ============================================================
print("\n\n=== INGREDIENT-QUANTITY PATTERNS ===")
print("Which words precede which qo-types:")

# Group by the qo-word
qo_patterns = defaultdict(Counter)
for i in range(1, len(recipe_words)):
    if recipe_words[i].startswith('qo') and not recipe_words[i-1].startswith('qo'):
        qo_patterns[recipe_words[i]][recipe_words[i-1]] += 1

# Show top 5 qo-words and their preceding words
for qo_word, preceding in sorted(qo_patterns.items(), key=lambda x: -sum(x[1].values()))[:10]:
    total = sum(preceding.values())
    print(f"\n  {qo_word} (total: {total}):")
    for w, c in preceding.most_common(5):
        print(f"    {w:20} {c:3}")

# ============================================================
# WORD FAMILY ANALYSIS: words sharing stems
# In AN recipes, the same ingredient appears in different forms
# (e.g., piperis, piper, pipere for pepper)
# ============================================================
print("\n\n=== WORD FAMILY ANALYSIS (shared prefixes in recipe section) ===")
# Group words by first 3 characters
prefix_families = defaultdict(Counter)
for w, c in recipe_freq.items():
    if len(w) >= 3:
        prefix_families[w[:3]][w] += c

# Show families with many members
for prefix, members in sorted(prefix_families.items(), key=lambda x: -sum(x[1].values())):
    total = sum(members.values())
    if total >= 30 and len(members) >= 3:
        print(f"\n  {prefix}- family (total: {total}, {len(members)} members):")
        for w, c in members.most_common(8):
            in_herbal = "H" if w in herbal_set else " "
            print(f"    [{in_herbal}] {w:20} {c:3}")

# ============================================================
# DISTRIBUTION TEST: words that appear in MANY recipes vs FEW
# High-frequency AN ingredients (pepper, ginger) appear in many recipes
# Low-frequency ones (euphorbium) appear in few
# ============================================================
print("\n\n=== WORD DISTRIBUTION ACROSS RECIPES ===")
word_recipe_dist = defaultdict(set)
recipe_idx = 0
for line in recipe_text_lines:
    line = line.strip()
    if '@Lc' in line:
        recipe_idx += 1
    elif '@P0' in line or '+P0' in line:
        match = re.match(r'<[^>]+>\s+(.*)', line)
        if match:
            text = match.group(1)
            text = re.sub(r'@\d+;?', '', text)
            text = re.sub(r'\{[^}]+\}', '', text)
            text = re.sub(r'<[^>]*>', '', text)
            text = re.sub(r"['\?\*,]", '', text)
            tokens = re.split(r'[\s.]+', text)
            for t in tokens:
                t = re.sub(r'[^a-z]', '', t.strip())
                if t and len(t) > 1:
                    word_recipe_dist[t].add(recipe_idx)

print("Words appearing in MOST recipes (top 30):")
for w, recipes_set in sorted(word_recipe_dist.items(), key=lambda x: -len(x[1]))[:30]:
    total_count = recipe_freq[w]
    in_herbal = "H" if w in herbal_set else " "
    is_qo = "qo" if w.startswith('qo') else "  "
    print(f"  [{in_herbal}] {is_qo} {w:20}  in {len(recipes_set):3} recipes, count={total_count:4}")

# Non-qo content words by recipe spread
print("\nNon-qo words (len>=3) by recipe spread:")
non_qo_spread = [(w, len(rs), recipe_freq[w]) for w, rs in word_recipe_dist.items()
                  if not w.startswith('qo') and len(w) >= 3]
non_qo_spread.sort(key=lambda x: -x[1])
for w, spread, count in non_qo_spread[:40]:
    in_herbal = "H" if w in herbal_set else " "
    print(f"  [{in_herbal}] {w:20}  in {spread:3} recipes, count={count:4}")

# ============================================================
# LINE-END WORDS (potential vehicle/binder like honey)
# In AN, honey often comes at the end as "confice cum melle"
# ============================================================
print("\n\n=== LINE-END PATTERNS ===")
# Collect last 3 words of each paragraph text block
last_words_of_recipes = Counter()
for r in recipes:
    if r["paragraph_words"]:
        # Last 3 words
        for w in r["paragraph_words"][-3:]:
            last_words_of_recipes[w] += 1

print("Words most often in LAST 3 positions of recipe paragraphs:")
for w, c in last_words_of_recipes.most_common(20):
    in_herbal = "H" if w in herbal_set else " "
    print(f"  [{in_herbal}] {w:20} {c:5}")

# ============================================================
# QO-WORD QUANTITY HIERARCHY
# Different qo- forms likely encode different quantities
# If we can order them, small quantities = rare/dangerous ingredients
# ============================================================
print("\n\n=== QO-WORD FREQUENCY RANKING (potential quantity hierarchy) ===")
qo_freq = Counter()
for w in recipe_words:
    if w.startswith('qo'):
        qo_freq[w] += 1

# Hypothesis: most common qo-word = most common quantity = moderate doses
# Rare qo-words = unusual quantities (very large or very small)
for i, (w, c) in enumerate(qo_freq.most_common(20), 1):
    print(f"  {i:3}. {w:20} {c:5}")

# Which ingredients precede the RAREST qo-words (opium candidates)
print("\nIngredients before RARE qo-words (count<=5):")
rare_qo_ingredients = Counter()
for i in range(1, len(recipe_words)):
    if recipe_words[i].startswith('qo') and qo_freq[recipe_words[i]] <= 5:
        if not recipe_words[i-1].startswith('qo'):
            rare_qo_ingredients[recipe_words[i-1]] += 1

for w, c in rare_qo_ingredients.most_common(15):
    print(f"  {w:20} {c:3}")
