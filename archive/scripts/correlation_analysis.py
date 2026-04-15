import re
from collections import Counter

def extract_folio_text(filename, folio_id):
    """Extract all text tokens for a given folio."""
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

# Pages I have visually examined with their illustration features
pages = [
    ('f1r', 3, {'leaves': 'prominent', 'flowers': 'small', 'roots': 'none', 'fruits': 'none', 'color_special': 'green+brown', 'size': 'medium'}),
    ('f1v', 4, {'leaves': 'dominant_large', 'flowers': 'small_top', 'roots': 'visible', 'fruits': 'none', 'color_special': 'green+orange', 'size': 'large'}),
    ('f2r', 5, {'leaves': 'prominent_lobed', 'flowers': 'spiky_top', 'roots': 'prominent_red', 'fruits': 'none', 'color_special': 'green+red_roots', 'size': 'large'}),
    ('f2v', 6, {'leaves': 'single_giant', 'flowers': 'tiny_top', 'roots': 'minimal', 'fruits': 'none', 'color_special': 'dark_green', 'size': 'very_large'}),
    ('f3r', 7, {'leaves': 'prominent_striped', 'flowers': 'none', 'roots': 'prominent_red', 'fruits': 'none', 'color_special': 'red+green_striped', 'size': 'large'}),
    ('f3v', 8, {'leaves': 'spiky_along_stem', 'flowers': 'blue_top', 'roots': 'prominent_red', 'fruits': 'seed_pods', 'color_special': 'blue+green', 'size': 'large'}),
    ('f4r', 9, {'leaves': 'small_many', 'flowers': 'none', 'roots': 'small_spider', 'fruits': 'red_berries', 'color_special': 'red_berries+green', 'size': 'large'}),
    ('f4v', 10, {'leaves': 'small_scattered', 'flowers': 'blue_prominent', 'roots': 'bulbous_brown', 'fruits': 'none', 'color_special': 'blue+brown_root', 'size': 'medium'}),
    ('f5r', 11, {'leaves': 'giant_round', 'flowers': 'none', 'roots': 'minimal', 'fruits': 'none', 'color_special': 'deep_green', 'size': 'very_large'}),
    ('f5v', 12, {'leaves': 'prominent_lobed', 'flowers': 'small_red_star', 'roots': 'visible_brown', 'fruits': 'none', 'color_special': 'green+red_flowers', 'size': 'medium'}),
    ('f6r', 13, {'leaves': 'spiky_jagged', 'flowers': 'none', 'roots': 'visible_white', 'fruits': 'green_pods', 'color_special': 'dark_green', 'size': 'large'}),
    ('f6v', 14, {'leaves': 'star_shaped', 'flowers': 'none', 'roots': 'visible', 'fruits': 'blue_seed_balls', 'color_special': 'blue+green', 'size': 'medium'}),
    ('f7r', 15, {'leaves': 'none_star_petals', 'flowers': 'star_flower_dominant', 'roots': 'prominent_orange', 'fruits': 'none', 'color_special': 'green+white', 'size': 'large'}),
    ('f7v', 16, {'leaves': 'rosette_oval', 'flowers': 'none', 'roots': 'minimal', 'fruits': 'orange_buds', 'color_special': 'green+orange', 'size': 'medium'}),
    ('f8r', 17, {'leaves': 'single_large_arrowhead', 'flowers': 'none', 'roots': 'visible_brown', 'fruits': 'none', 'color_special': 'green', 'size': 'large'}),
    ('f8v', 18, {'leaves': 'many_medium', 'flowers': 'small_red_orange', 'roots': 'visible_orange', 'fruits': 'none', 'color_special': 'green+red_flowers', 'size': 'tall'}),
    ('f9r', 19, {'leaves': 'many_lobed', 'flowers': 'spiky_brown_top', 'roots': 'large_brown', 'fruits': 'none', 'color_special': 'green+red_stems', 'size': 'large_bushy'}),
    ('f9v', 20, {'leaves': 'medium_lobed', 'flowers': 'blue_many_prominent', 'roots': 'visible_small', 'fruits': 'none', 'color_special': 'blue_flowers', 'size': 'medium'}),
]

# Group pages by illustration features

# FLOWER PROMINENCE
flower_prominent = []
flower_absent = []
for folio, pg, feat in pages:
    fl = str(feat.get('flowers', ''))
    if 'prominent' in fl or 'dominant' in fl or 'many' in fl:
        flower_prominent.append(folio)
    elif feat.get('flowers') == 'none' or feat.get('flowers') == 'minimal':
        flower_absent.append(folio)

# ROOT PROMINENCE
root_prominent = []
root_absent = []
for folio, pg, feat in pages:
    rt = str(feat.get('roots', ''))
    if 'prominent' in rt or 'large' in rt or 'bulbous' in rt:
        root_prominent.append(folio)
    elif feat.get('roots') == 'none' or feat.get('roots') == 'minimal':
        root_absent.append(folio)

# FRUIT/SEED PRESENCE
fruit_present = []
fruit_absent_list = []
for folio, pg, feat in pages:
    if feat.get('fruits') not in ('none', ''):
        fruit_present.append(folio)
    else:
        fruit_absent_list.append(folio)

# BLUE COLOR
blue_present = []
blue_absent = []
for folio, pg, feat in pages:
    cs = str(feat.get('color_special', ''))
    fl = str(feat.get('flowers', ''))
    if 'blue' in cs or 'blue' in fl:
        blue_present.append(folio)
    else:
        blue_absent.append(folio)

# RED COLOR
red_present = []
red_absent = []
for folio, pg, feat in pages:
    cs = str(feat.get('color_special', ''))
    fr = str(feat.get('fruits', ''))
    if 'red' in cs or 'red' in fr:
        red_present.append(folio)
    else:
        red_absent.append(folio)

# GIANT/DOMINANT LEAVES
leaf_giant = []
leaf_normal = []
for folio, pg, feat in pages:
    lv = str(feat.get('leaves', ''))
    if 'giant' in lv or 'dominant' in lv or 'single_large' in lv:
        leaf_giant.append(folio)
    else:
        leaf_normal.append(folio)

def avg_freq(folios, word_pattern, normalize=True):
    if not folios:
        return 0.0
    total_freq = 0
    total_words = 0
    for folio in folios:
        tokens = extract_folio_text(filename, folio)
        if not tokens:
            continue
        count = sum(1 for t in tokens if re.search(word_pattern, t))
        total_freq += count
        total_words += len(tokens)
    if normalize and total_words > 0:
        return total_freq / total_words * 100
    return total_freq / len(folios) if folios else 0

all_stems = ['chol', 'chor', 'shol', 'daiin', 'dar', 'sho', 'cthy', 'chy',
             'dain', 'shey', 'chey', 'dal', 'dol', 'or', 'ol', 'shy',
             'shody', 'otaiin', 'dam', 'cham', 'chom', 'cthol', 'cthor',
             'shor', 'char', 'otchy', 'okal', 'okol', 'cheor', 'kchor',
             'dchor', 'dor', 'aiin', 'oky', 'oty', 'chody', 'ar', 'dy',
             'chaiin', 'otol', 'dair', 'okaiin', 'sor', 'kchy', 'tchy',
             'chear', 'kol', 'saiin', 'dan', 'shaiin', 'qotor', 'otor',
             'choy', 'chal', 'sheey', 'cheey', 'keey', 'okeey',
             'qotchy', 'qokchy', 'qokol', 'qoky', 'qoty']

print("=" * 80)
print("ILLUSTRATION-TEXT CORRELATION ANALYSIS")
print("=" * 80)

feature_groups = [
    ("PROMINENT FLOWERS", flower_prominent, flower_absent),
    ("PROMINENT ROOTS", root_prominent, root_absent),
    ("FRUITS/SEEDS PRESENT", fruit_present, fruit_absent_list),
    ("BLUE COLOR ELEMENTS", blue_present, blue_absent),
    ("RED COLOR ELEMENTS", red_present, red_absent),
    ("GIANT/DOMINANT LEAVES", leaf_giant, leaf_normal),
]

for name, present, absent in feature_groups:
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"  Present in: {present}")
    print(f"  Absent in: {absent}")
    print(f"{'='*60}")

    results = []
    for stem in all_stems:
        pattern = r'^' + re.escape(stem) + r'$'
        freq_present = avg_freq(present, pattern)
        freq_absent = avg_freq(absent, pattern)
        diff = freq_present - freq_absent
        if freq_present > 0.3 or freq_absent > 0.3:
            results.append((stem, freq_present, freq_absent, diff))

    results.sort(key=lambda x: abs(x[3]), reverse=True)

    print(f"  {'Stem':<12} {'When Present':>12} {'When Absent':>12} {'Diff':>8}")
    print(f"  {'-'*12} {'-'*12} {'-'*12} {'-'*8}")
    for stem, fp, fa, diff in results[:20]:
        marker = "***" if abs(diff) > 1.5 else "**" if abs(diff) > 0.8 else "*" if abs(diff) > 0.4 else ""
        print(f"  {stem:<12} {fp:>11.2f}% {fa:>11.2f}% {diff:>+7.2f}% {marker}")

# Also: contains-match for stems (not just exact)
print("\n\n" + "=" * 80)
print("CONTAINS-MATCH ANALYSIS (stem appears as substring)")
print("=" * 80)

contain_stems = ['chol', 'chor', 'shol', 'daiin', 'dar', 'sho', 'dain',
                 'chey', 'shey', 'eey', 'dam', 'cham', 'chom', 'ol',
                 'otch', 'qo', 'ckh', 'cph', 'cfh', 'ody', 'oty']

for name, present, absent in feature_groups:
    print(f"\n--- {name} ---")
    results = []
    for stem in contain_stems:
        freq_present = avg_freq(present, stem)
        freq_absent = avg_freq(absent, stem)
        diff = freq_present - freq_absent
        if freq_present > 1.0 or freq_absent > 1.0:
            results.append((stem, freq_present, freq_absent, diff))
    results.sort(key=lambda x: abs(x[3]), reverse=True)
    for stem, fp, fa, diff in results[:10]:
        marker = "***" if abs(diff) > 3.0 else "**" if abs(diff) > 1.5 else "*" if abs(diff) > 0.8 else ""
        print(f"  *{stem}*  present={fp:.2f}%  absent={fa:.2f}%  diff={diff:+.2f}% {marker}")

# QO- prefix analysis
print("\n\n" + "=" * 80)
print("QO- PREFIX ANALYSIS")
print("=" * 80)
for name, present, absent in feature_groups:
    qo_present = avg_freq(present, r'^qo')
    qo_absent = avg_freq(absent, r'^qo')
    print(f"  {name}: present={qo_present:.2f}% absent={qo_absent:.2f}% diff={qo_present-qo_absent:+.2f}%")

# -dy suffix analysis
print("\n" + "=" * 80)
print("-DY SUFFIX ANALYSIS")
print("=" * 80)
for name, present, absent in feature_groups:
    dy_present = avg_freq(present, r'dy$')
    dy_absent = avg_freq(absent, r'dy$')
    print(f"  {name}: present={dy_present:.2f}% absent={dy_absent:.2f}% diff={dy_present-dy_absent:+.2f}%")

# -aiin suffix analysis
print("\n" + "=" * 80)
print("-AIIN SUFFIX ANALYSIS")
print("=" * 80)
for name, present, absent in feature_groups:
    aiin_present = avg_freq(present, r'aiin')
    aiin_absent = avg_freq(absent, r'aiin')
    print(f"  {name}: present={aiin_present:.2f}% absent={aiin_absent:.2f}% diff={aiin_present-aiin_absent:+.2f}%")

# Per-page detailed word dump for pages with flowers
print("\n\n" + "=" * 80)
print("DETAILED: PAGES WITH PROMINENT FLOWERS")
print("=" * 80)
for folio in flower_prominent:
    tokens = extract_folio_text(filename, folio)
    counts = Counter(tokens)
    top20 = counts.most_common(20)
    print(f"\n  {folio}: {top20}")

print("\n\n" + "=" * 80)
print("DETAILED: PAGES WITH NO FLOWERS")
print("=" * 80)
for folio in flower_absent:
    tokens = extract_folio_text(filename, folio)
    counts = Counter(tokens)
    top20 = counts.most_common(20)
    print(f"\n  {folio}: {top20}")
