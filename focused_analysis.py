import re
from collections import Counter

def extract_folio_text(filename, folio_id):
    lines = open(filename, 'r', encoding='utf-8').readlines()
    in_folio = False
    tokens = []
    folio_tag = '<' + folio_id + '>'
    folio_line_prefix = '<' + folio_id + '.'
    next_folio = re.compile(r'^<f\d+[rv]>')
    for line in lines:
        line = line.strip()
        if line.startswith(folio_tag) or line.startswith(folio_line_prefix):
            in_folio = True
        elif in_folio and next_folio.match(line) and not line.startswith('<' + folio_id):
            break
        if in_folio and ',' in line:
            parts = line.split('>', 1)
            if len(parts) > 1:
                text = parts[-1].strip()
                text = re.sub(r'@\d+;?', '', text)
                text = re.sub(r'\{[^}]+\}', '', text)
                text = re.sub(r'<->', ' ', text)
                text = re.sub(r'[,?!]', '', text)
                words = [w.strip() for w in text.replace('.', ' ').split() if len(w.strip()) > 1]
                tokens.extend(words)
    return tokens

filename = "C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt"

# Extended page classification from visual inspection
# Format: (folio, page_num, description, features)
classified_pages = [
    # FLOWER-DOMINANT PAGES
    ('f4v', 10, 'Blue flower top, bulbous root, small leaves', 'FLOWER'),
    ('f7r', 15, 'Star-flower dominant, green+white, orange root', 'FLOWER'),
    ('f9v', 20, 'Many blue flowers prominent, lobed leaves', 'FLOWER'),
    ('f11r', 22, 'Blue hanging bell-flowers, large wavy green leaves', 'FLOWER'),
    ('f16v', 32, 'Red star-flowers + blue top flower, very prominent', 'FLOWER'),

    # LEAF-DOMINANT PAGES (no/minimal flowers)
    ('f1v', 4, 'Large green+orange leaves dominant, small top flower', 'LEAF'),
    ('f2v', 6, 'Single giant round green leaf', 'LEAF'),
    ('f5r', 11, 'Giant round green leaves, no flowers', 'LEAF'),
    ('f8r', 17, 'Large arrowhead leaf, no flowers', 'LEAF'),
    ('f8v', 18, 'Many medium leaves, tiny flowers', 'LEAF'),

    # ROOT-PROMINENT PAGES
    ('f2r', 5, 'Lobed leaves, spiky top, prominent red roots', 'ROOT'),
    ('f3r', 7, 'Striped red/green leaves, prominent red roots', 'ROOT'),
    ('f3v', 8, 'Spiky leaves, blue top, prominent red root', 'ROOT'),
    ('f9r', 19, 'Bushy lobed leaves, large brown root', 'ROOT'),

    # FRUIT/SEED PAGES
    ('f4r', 9, 'Small leaves with red berries/fruits', 'FRUIT'),
    ('f6r', 13, 'Spiky jagged leaves with green seed pods', 'FRUIT'),
    ('f6v', 14, 'Star-shaped leaves with blue seed balls', 'FRUIT'),
    ('f7v', 16, 'Rosette oval leaves with orange buds/fruits', 'FRUIT'),
    ('f14v', 28, 'Green leaves with white spotted fruits, red roots', 'FRUIT'),
]

# Group by category
categories = {}
for folio, pg, desc, cat in classified_pages:
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(folio)

print("=" * 80)
print("CATEGORY COMPARISON: FLOWER vs LEAF vs ROOT vs FRUIT")
print("=" * 80)

# Get all tokens per category
cat_tokens = {}
for cat, folios in categories.items():
    all_tok = []
    for f in folios:
        all_tok.extend(extract_folio_text(filename, f))
    cat_tokens[cat] = all_tok

# Common stems to test
stems = ['chol', 'chor', 'shol', 'daiin', 'dar', 'sho', 'cthy', 'chy',
         'dain', 'shey', 'chey', 'dal', 'dol', 'or', 'ol', 'shy',
         'shody', 'otaiin', 'dam', 'cham', 'chom', 'cthol', 'cthor',
         'shor', 'char', 'otchy', 'okal', 'okol', 'cheor', 'kchor',
         'dchor', 'dor', 'aiin', 'oky', 'oty', 'chody', 'ar', 'dy',
         'chaiin', 'otol', 'dair', 'okaiin', 'sor', 'kchy', 'tchy',
         'chear', 'kol', 'saiin', 'dan', 'shaiin']

print(f"\n{'Stem':<12}", end="")
for cat in ['FLOWER', 'LEAF', 'ROOT', 'FRUIT']:
    print(f" {cat:>10}", end="")
print(f" {'F-L diff':>10} {'F-R diff':>10} {'R-L diff':>10}")
print("-" * 82)

results = []
for stem in stems:
    freqs = {}
    for cat in ['FLOWER', 'LEAF', 'ROOT', 'FRUIT']:
        tokens = cat_tokens[cat]
        count = sum(1 for t in tokens if t == stem)
        freqs[cat] = count / len(tokens) * 100 if tokens else 0

    fl_diff = freqs['FLOWER'] - freqs['LEAF']
    fr_diff = freqs['FLOWER'] - freqs['ROOT']
    rl_diff = freqs['ROOT'] - freqs['LEAF']
    max_diff = max(abs(fl_diff), abs(fr_diff), abs(rl_diff))

    if max_diff > 0.5:
        results.append((stem, freqs, fl_diff, fr_diff, rl_diff, max_diff))

results.sort(key=lambda x: x[5], reverse=True)

for stem, freqs, fl_diff, fr_diff, rl_diff, max_diff in results:
    marker = ""
    if max_diff > 2.0:
        marker = " ***"
    elif max_diff > 1.0:
        marker = " **"
    elif max_diff > 0.5:
        marker = " *"

    print(f"{stem:<12}", end="")
    for cat in ['FLOWER', 'LEAF', 'ROOT', 'FRUIT']:
        print(f" {freqs[cat]:>9.2f}%", end="")
    print(f" {fl_diff:>+9.2f}% {fr_diff:>+9.2f}% {rl_diff:>+9.2f}%{marker}")

# Now do CONTAINS match for important patterns
print("\n\n" + "=" * 80)
print("CONTAINS-MATCH BY CATEGORY")
print("=" * 80)

contain_stems = ['chol', 'chor', 'shol', 'daiin', 'dar', 'sho', 'dain',
                 'chey', 'shey', 'eey', 'dam', 'cham', 'chom', 'ol',
                 'otch', 'qo', 'ckh', 'cph', 'cfh', 'ody', 'oty',
                 'aiin', 'oiin', 'ain', 'cheor', 'sheo']

print(f"\n{'*stem*':<14}", end="")
for cat in ['FLOWER', 'LEAF', 'ROOT', 'FRUIT']:
    print(f" {cat:>10}", end="")
print(f" {'F-L diff':>10}")
print("-" * 76)

results2 = []
for stem in contain_stems:
    freqs = {}
    for cat in ['FLOWER', 'LEAF', 'ROOT', 'FRUIT']:
        tokens = cat_tokens[cat]
        count = sum(1 for t in tokens if stem in t)
        freqs[cat] = count / len(tokens) * 100 if tokens else 0
    fl_diff = freqs['FLOWER'] - freqs['LEAF']
    max_diff = max(abs(freqs[c1] - freqs[c2]) for c1 in ['FLOWER','LEAF','ROOT','FRUIT'] for c2 in ['FLOWER','LEAF','ROOT','FRUIT'])
    if max_diff > 1.0:
        results2.append((stem, freqs, fl_diff, max_diff))

results2.sort(key=lambda x: x[3], reverse=True)
for stem, freqs, fl_diff, max_diff in results2:
    marker = " ***" if max_diff > 4.0 else " **" if max_diff > 2.0 else " *"
    print(f"*{stem+'*':<13}", end="")
    for cat in ['FLOWER', 'LEAF', 'ROOT', 'FRUIT']:
        print(f" {freqs[cat]:>9.2f}%", end="")
    print(f" {fl_diff:>+9.2f}%{marker}")

# SPECIFIC: which words appear on flower pages but NOT on leaf pages?
print("\n\n" + "=" * 80)
print("WORDS UNIQUE TO OR STRONGLY FAVORING FLOWER PAGES")
print("=" * 80)
flower_counter = Counter(cat_tokens['FLOWER'])
leaf_counter = Counter(cat_tokens['LEAF'])
root_counter = Counter(cat_tokens['ROOT'])
fruit_counter = Counter(cat_tokens['FRUIT'])

flower_total = len(cat_tokens['FLOWER'])
leaf_total = len(cat_tokens['LEAF'])

print("\nWords with frequency >= 2 on FLOWER pages, normalized rate > 2x LEAF pages:")
for word, count in flower_counter.most_common(100):
    if count >= 2:
        flower_rate = count / flower_total * 100
        leaf_rate = leaf_counter.get(word, 0) / leaf_total * 100
        if leaf_rate == 0 or flower_rate / max(leaf_rate, 0.01) > 2.0:
            print(f"  {word:<20} FLOWER: {count} ({flower_rate:.2f}%)   LEAF: {leaf_counter.get(word,0)} ({leaf_rate:.2f}%)   ROOT: {root_counter.get(word,0)}   FRUIT: {fruit_counter.get(word,0)}")

print("\n\nWords with frequency >= 2 on ROOT pages, normalized rate > 2x LEAF pages:")
for word, count in root_counter.most_common(100):
    if count >= 2:
        root_rate = count / len(cat_tokens['ROOT']) * 100
        leaf_rate = leaf_counter.get(word, 0) / leaf_total * 100
        if leaf_rate == 0 or root_rate / max(leaf_rate, 0.01) > 2.0:
            print(f"  {word:<20} ROOT: {count} ({root_rate:.2f}%)   LEAF: {leaf_counter.get(word,0)} ({leaf_rate:.2f}%)   FLOWER: {flower_counter.get(word,0)}   FRUIT: {fruit_counter.get(word,0)}")

print("\n\nWords with frequency >= 2 on FRUIT pages, normalized rate > 2x LEAF pages:")
for word, count in fruit_counter.most_common(100):
    if count >= 2:
        fruit_rate = count / len(cat_tokens['FRUIT']) * 100
        leaf_rate = leaf_counter.get(word, 0) / leaf_total * 100
        if leaf_rate == 0 or fruit_rate / max(leaf_rate, 0.01) > 2.0:
            print(f"  {word:<20} FRUIT: {count} ({fruit_rate:.2f}%)   LEAF: {leaf_counter.get(word,0)} ({leaf_rate:.2f}%)   FLOWER: {flower_counter.get(word,0)}   ROOT: {root_counter.get(word,0)}")

# PER-PAGE word lists for each flower page
print("\n\n" + "=" * 80)
print("PER-PAGE TOP WORDS")
print("=" * 80)
for folio, pg, desc, cat in classified_pages:
    tokens = extract_folio_text(filename, folio)
    counts = Counter(tokens)
    print(f"\n  {folio} (p{pg}) [{cat}] {desc}")
    print(f"    Total words: {len(tokens)}")
    print(f"    Top 25: {counts.most_common(25)}")
