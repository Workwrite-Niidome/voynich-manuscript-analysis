#!/usr/bin/env python3
"""
Rebuild Voynich vocabulary with sandhi-collapsed stems.
Performs all 5 analyses requested.
"""

import re
from collections import Counter, defaultdict

# --- Parse the EVA transcription ---
def parse_eva(filepath):
    """Parse RF1b-e.txt, return list of (folio, line_id, line_type, words)."""
    lines = []
    current_folio = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for raw in f:
            raw = raw.rstrip('\n')
            # Skip header
            if raw.startswith('#'):
                continue
            # Folio header
            m = re.match(r'^<(f\d+[rv]\d?)>\s+<.*?\$Q=(\w).*?>', raw)
            if m:
                current_folio = m.group(1)
                scribe = m.group(2)  # A or B from $Q
                continue
            # Text line
            m2 = re.match(r'^<(f\d+[rv]\d?\.\d+(?:,\S+)?)>\s+(.*)', raw)
            if m2:
                line_id = m2.group(1)
                text = m2.group(2)
                # Determine line type from tag
                line_type = 'text'
                if ',@L' in line_id or ',+L' in line_id or ',=L' in line_id:
                    line_type = 'label'
                elif ',=Pt' in line_id:
                    line_type = 'title'
                lines.append((current_folio, line_id, line_type, text))
    return lines

def extract_words(text):
    """Extract clean words from an EVA line, removing markup."""
    # Remove comments in {}
    # Remove @-codes
    text = re.sub(r'\{[^}]*\}', '', text)
    text = re.sub(r'@\d+;?', '', text)
    # Split on periods, commas (not within words), spaces, <->
    text = text.replace('<->', ' ')
    text = text.replace('.', ' ')
    # Remove ? and other non-EVA chars but keep letters
    tokens = re.split(r'[^a-z\']+', text.lower())
    words = [t for t in tokens if t and len(t) > 0 and re.match(r'^[a-z\']+$', t)]
    return words

def get_scribe(folio):
    """Determine scribe from folio. Rough: A = Herbal-A, B = Herbal-B, etc."""
    # Based on Currier's assignment:
    # A: f1r-f57v (Herbal A, Pharma, some astro)
    # B: f75r-f116v (Herbal B, Bio, Stars)
    # This is approximate
    m = re.match(r'f(\d+)', folio)
    if m:
        num = int(m.group(1))
        if num <= 57:
            return 'A'
        else:
            return 'B'
    return '?'

# --- Load data ---
filepath = r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt'
parsed_lines = parse_eva(filepath)

# Build word list with context
all_words = []  # (word, folio, line_id, position, scribe)
word_bigrams = []  # (word1, word2, folio)
folio_words = defaultdict(list)  # folio -> list of words
scribe_words = defaultdict(list)  # scribe -> list of words

# Also track scribe per folio from $Q tag
folio_scribe_map = {}
with open(filepath, 'r', encoding='utf-8') as f:
    for raw in f:
        m = re.match(r'^<(f\d+[rv]\d?)>\s+<.*?\$Q=(\w).*?>', raw)
        if m:
            folio_scribe_map[m.group(1)] = m.group(2)

for folio, line_id, line_type, text in parsed_lines:
    words = extract_words(text)
    scribe = folio_scribe_map.get(folio, get_scribe(folio))
    for i, w in enumerate(words):
        all_words.append((w, folio, line_id, i, scribe))
        folio_words[folio].append(w)
        scribe_words[scribe].append(w)
    for i in range(len(words) - 1):
        word_bigrams.append((words[i], words[i+1], folio))

total_words = len(all_words)
word_freq = Counter(w for w, _, _, _, _ in all_words)

print(f"Total words: {total_words}")
print(f"Unique words: {len(word_freq)}")

# ============================================================
# ANALYSIS 1: Collapse sandhi variants - stem frequency
# ============================================================

def get_stem_and_suffix(word):
    """Strip n/l/r suffix to get stem. Return (stem, suffix) or (word, None)."""
    if len(word) >= 2 and word[-1] in ('n', 'l', 'r'):
        return word[:-1], word[-1]
    return word, None

# Build stem counter
stem_counter = Counter()
stem_variants = defaultdict(lambda: Counter())  # stem -> {variant_word: count}
stem_suffix_dist = defaultdict(lambda: Counter())  # stem -> {n/l/r: count}

for w, freq in word_freq.items():
    stem, suffix = get_stem_and_suffix(w)
    if suffix:
        stem_counter[stem] += freq
        stem_variants[stem][w] += freq
        stem_suffix_dist[stem][suffix] += freq
    # Also count words that don't end in n/l/r as their own stems
    # (they appear in the -y analysis later)

# Also count standalone stems (words not ending in n/l/r but matching a stem)
for w, freq in word_freq.items():
    stem, suffix = get_stem_and_suffix(w)
    if suffix is None and w in stem_counter:
        # This word IS a stem form without suffix
        stem_variants[w][w + ' (bare)'] += freq

# Top 100 stems
top100_stems = stem_counter.most_common(100)

print("\n=== TOP 100 STEMS (n/l/r collapsed) ===")
print(f"{'Rank':>4} {'Stem':>15} {'Total':>6} {'n':>5} {'l':>5} {'r':>5} | Variants")
for i, (stem, total) in enumerate(top100_stems, 1):
    n = stem_suffix_dist[stem].get('n', 0)
    l = stem_suffix_dist[stem].get('l', 0)
    r = stem_suffix_dist[stem].get('r', 0)
    variants = ', '.join(f"{v}({c})" for v, c in stem_variants[stem].most_common(5))
    print(f"{i:>4}. {stem:>15} {total:>6} {n:>5} {l:>5} {r:>5} | {variants}")

# ============================================================
# ANALYSIS 2: A/B scribe -ol vs -edy
# ============================================================

print("\n\n=== ANALYSIS 2: A/B SCRIBE -ol vs -edy ===")

# Count -edy words by scribe
edy_words = [(w, f, s) for w, f, _, _, s in all_words if w.endswith('edy')]
edy_by_scribe = Counter()
for w, f, s in edy_words:
    edy_by_scribe[s] += 1

ol_words_by_scribe = Counter()
for w, f, _, _, s in all_words:
    if w.endswith('ol'):
        ol_words_by_scribe[s] += 1

print(f"\n-edy words by scribe: {dict(edy_by_scribe)}")
print(f"-ol words by scribe: {dict(ol_words_by_scribe)}")

# Check -edy frequency list
edy_freq = Counter()
for w, f, s in edy_words:
    edy_freq[w] += 1
print(f"\nTop -edy words: {edy_freq.most_common(20)}")

# Check if -edy words show sandhi variants: edn, edr?
edn_words = Counter(w for w, _ in word_freq.items() if w.endswith('edn'))
edr_words = Counter(w for w, _ in word_freq.items() if w.endswith('edr'))
print(f"\n-edn words: {dict(Counter(w for w in word_freq if w.endswith('edn')))}")
print(f"-edr words: {dict(Counter(w for w in word_freq if w.endswith('edr')))}")

# Check sandhi behavior of -edy words with following word
edy_bigrams = []
for w1, w2, folio in word_bigrams:
    if w1.endswith('edy'):
        edy_bigrams.append((w1, w2))

if edy_bigrams:
    edy_next_initial = Counter()
    for w1, w2 in edy_bigrams:
        if w2:
            edy_next_initial[w2[0]] += 1
    print(f"\nAfter -edy words, next word initials: {edy_next_initial.most_common(15)}")

# Check -eey, -ey distribution by scribe
eey_by_scribe = Counter()
ey_by_scribe = Counter()
for w, f, _, _, s in all_words:
    if w.endswith('eey'):
        eey_by_scribe[s] += 1
    elif w.endswith('ey') and not w.endswith('eey'):
        ey_by_scribe[s] += 1

print(f"\n-eey words by scribe: {dict(eey_by_scribe)}")
print(f"-ey words by scribe: {dict(ey_by_scribe)}")

# Compare stems: do -edy stems match -ol stems?
edy_stems = set()
for w in edy_freq:
    if w.endswith('edy'):
        edy_stems.add(w[:-3])  # strip 'edy'

ol_stems = set()
for w in word_freq:
    if w.endswith('ol'):
        ol_stems.add(w[:-2])  # strip 'ol'

shared = edy_stems & ol_stems
print(f"\nStems shared between -edy and -ol: {shared}")
print(f"Stems only in -edy: {edy_stems - ol_stems}")
print(f"Stems only in -ol (sample): {list(ol_stems - edy_stems)[:20]}")

# ============================================================
# ANALYSIS 3: The -y class
# ============================================================

print("\n\n=== ANALYSIS 3: THE -y CLASS ===")

y_words = [(w, freq) for w, freq in word_freq.items() if w.endswith('y') and not w.endswith('ey')]
y_words_all = [(w, freq) for w, freq in word_freq.items() if w.endswith('y')]
ey_words_list = [(w, freq) for w, freq in word_freq.items() if w.endswith('ey')]

total_y = sum(freq for _, freq in y_words_all)
print(f"Total words ending in -y: {total_y} ({100*total_y/total_words:.1f}%)")

# Top 30 -y words
y_sorted = sorted(y_words_all, key=lambda x: -x[1])[:30]
print(f"\nTop 30 -y words:")
print(f"{'Rank':>4} {'Word':>15} {'Freq':>6}")
for i, (w, f) in enumerate(y_sorted, 1):
    print(f"{i:>4}. {w:>15} {f:>6}")

# Do -y words share stems with n/l/r words?
y_stems_map = defaultdict(int)
for w, freq in y_words_all:
    if w.endswith('y'):
        stem = w[:-1]
        y_stems_map[stem] += freq

# Find overlap
nlr_stems_set = set(stem_counter.keys())
y_stems_set = set(y_stems_map.keys())
overlap = nlr_stems_set & y_stems_set

print(f"\n-y stems that also have n/l/r variants: {len(overlap)}")
print(f"Top overlapping stems:")
overlap_data = []
for stem in overlap:
    y_f = y_stems_map[stem]
    nlr_f = stem_counter[stem]
    overlap_data.append((stem, y_f, nlr_f))
overlap_data.sort(key=lambda x: -(x[1]+x[2]))
for stem, yf, nlrf in overlap_data[:30]:
    variants_nlr = stem_variants[stem].most_common(3)
    y_word = stem + 'y'
    y_freq_val = word_freq.get(y_word, 0)
    print(f"  {stem:>12} -> {y_word}({y_freq_val}) vs n/l/r({nlrf}): {variants_nlr}")

# Distribution of -y vs n/l/r across sections
print(f"\n-y vs n/l/r by scribe:")
y_by_scribe = Counter()
nlr_by_scribe = Counter()
other_by_scribe = Counter()
for w, f, _, _, s in all_words:
    if w.endswith('y'):
        y_by_scribe[s] += 1
    elif w[-1:] in ('n', 'l', 'r') and len(w) >= 2:
        nlr_by_scribe[s] += 1
    else:
        other_by_scribe[s] += 1

for s in sorted(set(s for _, _, _, _, s in all_words)):
    total_s = y_by_scribe[s] + nlr_by_scribe[s] + other_by_scribe[s]
    if total_s > 0:
        print(f"  Scribe {s}: -y={y_by_scribe[s]}({100*y_by_scribe[s]/total_s:.1f}%) "
              f"n/l/r={nlr_by_scribe[s]}({100*nlr_by_scribe[s]/total_s:.1f}%) "
              f"other={other_by_scribe[s]}({100*other_by_scribe[s]/total_s:.1f}%)")

# -y by folio section (herbal, pharma, astro, bio, stars)
def get_section(folio):
    m = re.match(r'f(\d+)', folio)
    if not m: return 'unknown'
    n = int(m.group(1))
    if n <= 56: return 'herbal_A'
    if n <= 66: return 'pharma'
    if n <= 73: return 'astro'
    if n <= 84: return 'bio'
    if n <= 86: return 'stars'
    if n <= 102: return 'herbal_B'
    return 'recipe'

y_by_section = Counter()
nlr_by_section = Counter()
total_by_section = Counter()
for w, folio, _, _, _ in all_words:
    sec = get_section(folio)
    total_by_section[sec] += 1
    if w.endswith('y'):
        y_by_section[sec] += 1
    elif w[-1:] in ('n', 'l', 'r') and len(w) >= 2:
        nlr_by_section[sec] += 1

print(f"\n-y vs n/l/r by section:")
for sec in ['herbal_A', 'pharma', 'astro', 'bio', 'stars', 'herbal_B', 'recipe']:
    t = total_by_section[sec]
    if t > 0:
        yp = 100*y_by_section[sec]/t
        np = 100*nlr_by_section[sec]/t
        print(f"  {sec:>10}: -y={y_by_section[sec]:>4}({yp:>5.1f}%) n/l/r={nlr_by_section[sec]:>4}({np:>5.1f}%) total={t}")

# ============================================================
# ANALYSIS 4: Function words (>90% -n preference)
# ============================================================

print("\n\n=== ANALYSIS 4: FUNCTION WORDS (>90% -n) ===")

function_candidates = []
for stem in stem_counter:
    total = stem_counter[stem]
    if total < 5:
        continue
    n_count = stem_suffix_dist[stem].get('n', 0)
    n_pct = 100 * n_count / total
    if n_pct >= 90:
        function_candidates.append((stem, total, n_count, n_pct))

function_candidates.sort(key=lambda x: -x[1])
print(f"\nStems with >90% -n preference and freq >= 5:")
print(f"{'Stem':>15} {'Total':>6} {'n':>5} {'%n':>6} | Full forms")
for stem, total, n_count, n_pct in function_candidates:
    variants = ', '.join(f"{v}({c})" for v, c in stem_variants[stem].most_common())
    print(f"{stem:>15} {total:>6} {n_count:>5} {n_pct:>5.1f}% | {variants}")

# Also check words always ending in -n (not from stem analysis)
print(f"\n\nAll high-frequency -n words (freq >= 10):")
n_words = [(w, f) for w, f in word_freq.items() if w.endswith('n') and f >= 10]
n_words.sort(key=lambda x: -x[1])
for w, f in n_words[:30]:
    stem = w[:-1]
    # Check if this stem also appears with -l or -r
    l_form = stem + 'l'
    r_form = stem + 'r'
    l_f = word_freq.get(l_form, 0)
    r_f = word_freq.get(r_form, 0)
    total_nlr = f + l_f + r_f
    n_pct = 100 * f / total_nlr if total_nlr > 0 else 0
    print(f"  {w:>15} freq={f:>4}  l-form={l_form}({l_f})  r-form={r_form}({r_f})  %n={n_pct:.0f}%")

# ============================================================
# ANALYSIS 5: Attempt to read f1r lines 1-3 and f47r lines 5-8
# ============================================================

print("\n\n=== ANALYSIS 5: READING ATTEMPTS ===")

# Extract specific lines
target_lines = {}
for folio, line_id, line_type, text in parsed_lines:
    if folio == 'f1r' and any(f'f1r.{i},' in line_id for i in [1,2,3]):
        target_lines[line_id] = text
    if folio == 'f47r' and any(f'f47r.{i},' in line_id for i in [5,6,7,8]):
        target_lines[line_id] = text

print("\n--- f1r lines 1-3 (raw) ---")
for lid in sorted(target_lines):
    if 'f1r' in lid:
        print(f"  {lid}: {target_lines[lid]}")

print("\n--- f47r lines 5-8 (raw) ---")
for lid in sorted(target_lines):
    if 'f47r' in lid:
        print(f"  {lid}: {target_lines[lid]}")

# Stem-collapse function
def collapse_to_stem(word):
    """Collapse word to stem + morphological annotation."""
    stem, suffix = get_stem_and_suffix(word)
    if suffix:
        return f"{stem}[-{suffix}]"
    return word

# Parse and annotate
print("\n--- f1r lines 1-3 (stem-collapsed) ---")
for lid in sorted(target_lines):
    if 'f1r' in lid:
        words = extract_words(target_lines[lid])
        collapsed = [collapse_to_stem(w) for w in words]
        print(f"  {lid}: {' . '.join(collapsed)}")

print("\n--- f47r lines 5-8 (stem-collapsed) ---")
for lid in sorted(target_lines):
    if 'f47r' in lid:
        words = extract_words(target_lines[lid])
        collapsed = [collapse_to_stem(w) for w in words]
        print(f"  {lid}: {' . '.join(collapsed)}")

# Annotated reading with function word and plant-part labels
def annotate_word(word):
    """Annotate word with morphological/semantic information."""
    stem, suffix = get_stem_and_suffix(word)

    # Function words (locked -n)
    func_stems = {
        'daii': 'FUNC(of?)',
        'aii': 'FUNC(and?)',
        'okai': 'FUNC(each?)',
        'qokai': 'FUNC(prep?)',
        'otai': 'FUNC(?)',
        'dai': 'FUNC(this?)',
        'sai': 'FUNC(?)',
        'tai': 'FUNC(?)',
        'cphaii': 'FUNC(?)',
        'cthai': 'FUNC(?)',
        'chai': 'FUNC(?)',
        'shai': 'FUNC(?)',
    }

    # Plant part stems
    plant_stems = {
        'cho': 'LEAF',
        'sho': 'ROOT',
        'cho': 'LEAF',
        'ctho': 'BARK?',
        'oto': 'STEM?',
    }

    # Check function words
    if suffix and stem in func_stems:
        return f"[{func_stems[stem]}]"
    if word in func_stems.values():
        return word

    # Check plant parts
    if suffix and stem in plant_stems:
        return f"[{plant_stems[stem]}-{suffix}]"
    if stem in plant_stems and not suffix:
        return f"[{plant_stems[stem]}]"

    # Other known patterns
    if suffix:
        return f"{stem}[-{suffix}]"
    return word

print("\n--- f1r lines 1-3 (annotated) ---")
for lid in sorted(target_lines):
    if 'f1r' in lid:
        words = extract_words(target_lines[lid])
        annotated = [annotate_word(w) for w in words]
        print(f"  {lid}: {' . '.join(annotated)}")

print("\n--- f47r lines 5-8 (annotated) ---")
for lid in sorted(target_lines):
    if 'f47r' in lid:
        words = extract_words(target_lines[lid])
        annotated = [annotate_word(w) for w in words]
        print(f"  {lid}: {' . '.join(annotated)}")

# ============================================================
# Save all results for the markdown output
# ============================================================

print("\n\n=== SUMMARY STATS ===")
print(f"Total words: {total_words}")
print(f"Words ending n/l/r: {sum(1 for w,_,_,_,_ in all_words if len(w)>=2 and w[-1] in 'nlr')}")
print(f"Words ending -y: {sum(1 for w,_,_,_,_ in all_words if w.endswith('y'))}")
print(f"Words ending -edy: {sum(1 for w,_,_,_,_ in all_words if w.endswith('edy'))}")
print(f"Unique stems (n/l/r): {len(stem_counter)}")
print(f"Function word candidates (>90% -n, freq>=5): {len(function_candidates)}")
print(f"Overlap between -y and n/l/r stems: {len(overlap)}")

# Check specific items for f47r
print("\n--- Checking f47r availability ---")
f47r_lines = [(lid, text) for folio, lid, _, text in parsed_lines if folio == 'f47r']
for lid, text in f47r_lines:
    print(f"  {lid}: {text[:80]}")
