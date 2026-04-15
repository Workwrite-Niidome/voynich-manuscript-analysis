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

# Find herbal section (f1r-f57v approximately)
herbal_end = None
for i, line in enumerate(lines):
    if '<f58r>' in line:
        herbal_end = i
        break
if herbal_end is None:
    herbal_end = 500

herbal_text_lines = lines[0:herbal_end]

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

# Extract @Lf words (ingredient labels in recipe margin)
lf_words = []
for line in recipe_text_lines:
    if '@Lf' in line:
        match = re.match(r'<[^>]+>\s+(.*)', line.strip())
        if match:
            text = match.group(1)
            text = re.sub(r'@\d+;?', '', text)
            text = re.sub(r'\{[^}]+\}', '', text)
            text = re.sub(r"['\?\*,.<>]", '', text)
            tokens = re.split(r'[\s.]+', text.strip())
            for t in tokens:
                t = re.sub(r'[^a-z]', '', t)
                if t and len(t) > 1:
                    lf_words.append(t)

lf_freq = Counter(lf_words)
print(f"=== @Lf WORDS (ingredient labels) -- Total: {len(lf_words)}, Unique: {len(set(lf_words))} ===")
for w, c in lf_freq.most_common(40):
    in_herbal = "HERBAL" if w in herbal_set else "recipe-only"
    print(f"  {w:20} {c:5}   [{in_herbal}]")

# Non-qo content words
print("\n=== NON-QO CONTENT WORDS IN RECIPES (length >= 3) ===")
content_words = Counter()
for w in recipe_words:
    if not w.startswith('qo') and len(w) >= 3:
        content_words[w] += 1

for i, (w, c) in enumerate(content_words.most_common(40), 1):
    in_herbal = "HERBAL" if w in herbal_set else "recipe-only"
    print(f"  {i:3}. {w:20} {c:5}   [{in_herbal}]")

# RECIPE-ONLY words
print("\n=== RECIPE-ONLY WORDS (not in herbal section) - candidates for imported spices ===")
recipe_only = Counter()
for w, c in recipe_freq.items():
    if w not in herbal_set and len(w) >= 3 and not w.startswith('qo') and c >= 5:
        recipe_only[w] = c

for i, (w, c) in enumerate(sorted(recipe_only.items(), key=lambda x: -x[1])[:30], 1):
    print(f"  {i:3}. {w:20} {c:5}")

# Words in BOTH recipe and herbal
print("\n=== WORDS IN BOTH RECIPE AND HERBAL (candidates for herbs) ===")
both = Counter()
for w, c in recipe_freq.items():
    if w in herbal_set and len(w) >= 3 and not w.startswith('qo') and c >= 10:
        both[w] = c

for i, (w, c) in enumerate(sorted(both.items(), key=lambda x: -x[1])[:30], 1):
    h_count = herbal_freq[w]
    print(f"  {i:3}. {w:20}  recipe:{c:5}  herbal:{h_count:5}")

# Recipe structure samples
print("\n=== RECIPE STRUCTURE SAMPLES (first 30 @Lc/@Lf lines) ===")
count = 0
for line in recipe_text_lines:
    line = line.strip()
    if '@Lc' in line or '@Lf' in line:
        print(f"  {line[:100]}")
        count += 1
        if count >= 30:
            break

# Ingredient candidates: non-qo words before qo-words
print("\n=== INGREDIENT CANDIDATES (non-qo words before qo-words) ===")
before_qo_nonqo = Counter()
for i in range(1, len(recipe_words)):
    if recipe_words[i].startswith('qo') and not recipe_words[i-1].startswith('qo'):
        before_qo_nonqo[recipe_words[i-1]] += 1

for i, (w, c) in enumerate(before_qo_nonqo.most_common(30), 1):
    in_herbal = "HERBAL" if w in herbal_set else "recipe-only"
    in_lf = "LF" if w in set(lf_words) else ""
    print(f"  {i:3}. {w:20} {c:5}   [{in_herbal}] {in_lf}")

# @Lf words that are NOT in herbal section
print("\n=== @Lf RECIPE-ONLY (imported spice candidates) ===")
for w, c in sorted(lf_freq.items(), key=lambda x: -x[1]):
    if w not in herbal_set:
        print(f"  {w:20} {c:5}")

# Honey test
print("\n=== HONEY TEST: freq>=10 in recipe, absent from herbal ===")
honey_candidates = []
for w, c in recipe_freq.items():
    if c >= 10 and w not in herbal_set and len(w) >= 2 and not w.startswith('qo'):
        honey_candidates.append((w, c))
honey_candidates.sort(key=lambda x: -x[1])
for w, c in honey_candidates[:20]:
    print(f"  {w:20} {c:5}")

# Recipe count
print("\n=== RECIPE COUNT AND SIZE ===")
recipes = []
current_recipe = []
current_title = ""
for line in recipe_text_lines:
    line = line.strip()
    if '@Lc' in line:
        if current_recipe:
            recipes.append((current_title, current_recipe))
        current_title = line
        current_recipe = []
    else:
        current_recipe.append(line)
if current_recipe:
    recipes.append((current_title, current_recipe))

print(f"Total recipes (by @Lc titles): {len(recipes)}")

ingredient_counts = []
for title, rlines in recipes:
    lf_count = sum(1 for l in rlines if '@Lf' in l)
    ingredient_counts.append(lf_count)

if ingredient_counts:
    print(f"  Min ingredients: {min(ingredient_counts)}")
    print(f"  Max ingredients: {max(ingredient_counts)}")
    print(f"  Avg ingredients: {sum(ingredient_counts)/len(ingredient_counts):.1f}")

# Word position analysis within recipe paragraphs
print("\n=== POSITION ANALYSIS: words at END of @P0 lines ===")
end_words = Counter()
for line in recipe_text_lines:
    if '@P0' in line or '+P0' in line:
        match = re.match(r'<[^>]+>\s+(.*)', line.strip())
        if match:
            text = match.group(1)
            text = re.sub(r'@\d+;?', '', text)
            text = re.sub(r'\{[^}]+\}', '', text)
            text = re.sub(r'<[^>]*>', '', text)
            text = re.sub(r"['\?\*,]", '', text)
            tokens = [re.sub(r'[^a-z]', '', t) for t in re.split(r'[\s.]+', text) if t.strip()]
            tokens = [t for t in tokens if t and len(t) > 1]
            if tokens:
                end_words[tokens[-1]] += 1

print("Words most often at END of recipe text lines:")
for w, c in end_words.most_common(20):
    in_herbal = "HERBAL" if w in herbal_set else "recipe-only"
    print(f"  {w:20} {c:5}   [{in_herbal}]")

# Bigrams in recipe section
print("\n=== COMMON BIGRAMS IN RECIPES ===")
bigrams = Counter()
for i in range(len(recipe_words)-1):
    bg = f"{recipe_words[i]} {recipe_words[i+1]}"
    bigrams[bg] += 1

for bg, c in bigrams.most_common(30):
    print(f"  {bg:40} {c:5}")

# Co-occurrence analysis: which @Lf words appear together in same recipe
print("\n=== @Lf CO-OCCURRENCE (which ingredients appear together) ===")
recipe_ingredients = []
current_ingredients = []
for line in recipe_text_lines:
    line = line.strip()
    if '@Lc' in line:
        if current_ingredients:
            recipe_ingredients.append(current_ingredients)
        current_ingredients = []
    elif '@Lf' in line:
        match = re.match(r'<[^>]+>\s+(.*)', line)
        if match:
            text = match.group(1)
            text = re.sub(r'@\d+;?', '', text)
            text = re.sub(r'\{[^}]+\}', '', text)
            text = re.sub(r"['\?\*,.<>]", '', text).strip()
            t = re.sub(r'[^a-z\s]', '', text).strip()
            if t:
                current_ingredients.append(t)
if current_ingredients:
    recipe_ingredients.append(current_ingredients)

cooccur = Counter()
for ingredients in recipe_ingredients:
    for i in range(len(ingredients)):
        for j in range(i+1, len(ingredients)):
            pair = tuple(sorted([ingredients[i], ingredients[j]]))
            cooccur[pair] += 1

print(f"Recipes with ingredient lists: {len(recipe_ingredients)}")
for pair, c in cooccur.most_common(20):
    print(f"  {str(pair):50} {c:3}")

# How many recipes each @Lf word appears in
print("\n=== @Lf WORDS BY NUMBER OF RECIPES THEY APPEAR IN ===")
lf_recipe_count = Counter()
for ingredients in recipe_ingredients:
    unique_ing = set(ingredients)
    for ing in unique_ing:
        lf_recipe_count[ing] += 1

for w, c in lf_recipe_count.most_common(30):
    in_herbal = "HERBAL" if w in herbal_set else "recipe-only"
    print(f"  {w:25} appears in {c:3} recipes   [{in_herbal}]")
