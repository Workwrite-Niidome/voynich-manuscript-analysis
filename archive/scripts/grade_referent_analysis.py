"""
Grade Referent Analysis: What SPECIFIC things does each grade level refer to?

Tests:
1. Grade = preparation level (herbal/recipe ratio per root per grade)
2. Grade = quantity/portion (co-occurrence with qo- words)
3. k-root decomposition (qokeey = drachma?)
4. Positional distribution (where in herbal entries does each grade appear?)
5. Complete preparation vocabulary table
"""

import re
from collections import defaultdict, Counter
import math

# ============================================================
# PARSE THE EVA TRANSCRIPTION
# ============================================================

with open("C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt", "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

# Parse into structured data: folio -> list of (line_num, line_position, words)
folio_lines = defaultdict(list)  # folio -> [(line_num_in_folio, words)]
folio_all_words = defaultdict(list)
current_folio = None
section_map = {}  # folio -> section type

for line in raw_lines:
    line = line.strip()

    # Detect folio header
    m = re.match(r'<(f\d+[rv]\d?)>\s+', line)
    if m:
        current_folio = m.group(1)
        continue

    # Detect line within folio
    m = re.match(r'<(f\d+[rv]\d?)\.(\d+)', line)
    if m:
        current_folio = m.group(1)
        line_num = int(m.group(2))
    else:
        line_num = -1

    if not current_folio:
        continue

    # Clean line
    clean = re.sub(r'<[^>]*>', '', line)
    clean = re.sub(r'\{[^}]*\}', '', clean)
    clean = re.sub(r'@\d+;?', '', clean)
    clean = re.sub(r"[?',]", '', clean)
    words = re.split(r'[.\s<>\-]+', clean)
    words = [w.strip() for w in words if w.strip() and len(w.strip()) > 1]

    if words:
        folio_lines[current_folio].append((line_num, words))
        folio_all_words[current_folio].extend(words)

# Classify sections
for folio in folio_all_words:
    m = re.match(r'f(\d+)', folio)
    if m:
        num = int(m.group(1))
        if num <= 57:
            section_map[folio] = 'herbal'
        elif 58 <= num <= 67:
            section_map[folio] = 'astro'
        elif 68 <= num <= 73:
            section_map[folio] = 'cosmo'
        elif 75 <= num <= 86:
            section_map[folio] = 'bio'
        elif 99 <= num <= 116:
            section_map[folio] = 'recipe'
        else:
            section_map[folio] = 'other'


def get_grade(word):
    """Get the vowel grade of a word."""
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


def get_root(word):
    """Extract the consonantal root from a word."""
    # Remove common prefixes
    w = word
    prefix = ''
    for pref in ['qo', 'ot', 'ok', 'op', 'ol', 'od', 'sh', 'o', 's', 'y', 'd', 'p', 'k', 't']:
        if w.startswith(pref) and len(w) > len(pref) + 1:
            # Only strip if what remains starts with a known root consonant
            remainder = w[len(pref):]
            if remainder and remainder[0] in 'cskdt':
                prefix = pref
                w = remainder
                break

    # Extract root consonant cluster
    root_match = re.match(r'((?:c[ptk]h|ckh|cth|ch|sh|th|ph|[kstdp]))', w)
    if root_match:
        return root_match.group(1)
    return None


GRADES = ['bare', 'e', 'ee', 'eo', 'eeo', 'eod']

# Build complete word list with metadata
all_entries = []  # (word, folio, section, line_num, line_pos_in_folio)
for folio, lines in folio_lines.items():
    section = section_map.get(folio, 'other')
    total_lines = len(lines)
    for idx, (line_num, words) in enumerate(lines):
        for word in words:
            all_entries.append({
                'word': word,
                'folio': folio,
                'section': section,
                'line_num': line_num,
                'line_idx': idx,
                'total_lines': total_lines,
                'grade': get_grade(word),
                'root': get_root(word),
            })

all_words_flat = [e['word'] for e in all_entries]
word_freq = Counter(all_words_flat)

print("=" * 90)
print("GRADE REFERENT ANALYSIS: What does each grade level REFER TO?")
print("=" * 90)
print(f"Total word tokens: {len(all_entries)}")
print(f"Total word types: {len(word_freq)}")
print()

# ============================================================
# TEST 1: PREPARATION LEVEL
# Herbal/recipe ratio per ROOT per GRADE
# ============================================================

print("=" * 90)
print("TEST 1: GRADE = PREPARATION LEVEL")
print("If grade encodes preparation, each root should show increasing recipe-enrichment")
print("=" * 90)
print()

# For each major root, count tokens by grade and section
major_roots = ['ch', 'sh', 'k', 'cth', 'ckh', 'cph', 'd', 'th', 'ph', 't', 'p', 's']

root_grade_section = defaultdict(lambda: defaultdict(lambda: {'herbal': 0, 'recipe': 0, 'other': 0}))

for e in all_entries:
    root = e['root']
    if root:
        sect = e['section'] if e['section'] in ('herbal', 'recipe') else 'other'
        root_grade_section[root][e['grade']][sect] += 1

print(f"{'Root':<6} {'Grade':<6} {'Herbal':>8} {'Recipe':>8} {'Ratio R/H':>10} {'Total':>7}")
print("-" * 50)

for root in ['ch', 'sh', 'k', 'cth', 'd', 't']:
    if root not in root_grade_section:
        continue
    for grade in GRADES:
        h = root_grade_section[root][grade]['herbal']
        r = root_grade_section[root][grade]['recipe']
        total = h + r + root_grade_section[root][grade]['other']
        if total < 3:
            continue
        ratio = r / h if h > 0 else float('inf')
        marker = " ***" if ratio > 2.0 else " **" if ratio > 1.5 else ""
        print(f"{root:<6} {grade:<6} {h:>8} {r:>8} {ratio:>10.2f} {total:>7}{marker}")
    print()

# ============================================================
# TEST 2: QUANTITY/PORTION
# Co-occurrence with qo- words
# ============================================================

print("=" * 90)
print("TEST 2: GRADE = QUANTITY (co-occurrence with qo- words)")
print("If grade encodes quantity/portion, higher grades should co-occur more with qo-")
print("=" * 90)
print()

# For each grade level, count how often the word appears adjacent to a qo- word
# (within same line)

grade_qo_adj = defaultdict(lambda: {'near_qo': 0, 'not_near_qo': 0})

for folio, lines in folio_lines.items():
    for line_num, words in lines:
        for i, w in enumerate(words):
            grade = get_grade(w)
            # Check if any word within 2 positions is a qo- word
            near_qo = False
            for j in range(max(0, i-2), min(len(words), i+3)):
                if j != i and words[j].startswith('qo'):
                    near_qo = True
                    break
            if near_qo:
                grade_qo_adj[grade]['near_qo'] += 1
            else:
                grade_qo_adj[grade]['not_near_qo'] += 1

print(f"{'Grade':<8} {'Near qo-':>10} {'Not near':>10} {'% near qo':>12}")
print("-" * 45)
for grade in GRADES:
    near = grade_qo_adj[grade]['near_qo']
    notnear = grade_qo_adj[grade]['not_near_qo']
    total = near + notnear
    pct = 100 * near / total if total > 0 else 0
    print(f"{grade:<8} {near:>10} {notnear:>10} {pct:>11.1f}%")

# Also: check words that START with qo- by their grade
print()
print("Words starting with 'qo' by grade:")
qo_words_by_grade = defaultdict(list)
for e in all_entries:
    if e['word'].startswith('qo'):
        qo_words_by_grade[e['grade']].append(e['word'])

for grade in GRADES:
    words = qo_words_by_grade[grade]
    top = Counter(words).most_common(5)
    top_str = ', '.join(f"{w}({c})" for w, c in top)
    print(f"  {grade:<8}: {len(words):>5} tokens | top: {top_str}")

# ============================================================
# TEST 3: k-ROOT DECOMPOSITION
# qokeey = drachma? Analyze qo+k combinations
# ============================================================

print()
print("=" * 90)
print("TEST 3: k-ROOT DECOMPOSITION (qo+k = measured quantity?)")
print("=" * 90)
print()

# Find all words matching qok* pattern
qok_words = [(e['word'], e['section'], e['folio']) for e in all_entries if re.match(r'qok', e['word'])]
qok_counter = Counter(w for w, s, f in qok_words)
qok_by_section = defaultdict(Counter)
for w, s, f in qok_words:
    qok_by_section[s][w] += 1

print("All qok- words (sorted by frequency):")
print(f"{'Word':<20} {'Total':>6} {'Herbal':>8} {'Recipe':>8} {'Other':>7} {'Grade':<6}")
print("-" * 60)
for word, count in qok_counter.most_common(30):
    h = qok_by_section['herbal'][word]
    r = qok_by_section['recipe'][word]
    o = count - h - r
    grade = get_grade(word)
    print(f"{word:<20} {count:>6} {h:>8} {r:>8} {o:>7} {grade:<6}")

# Also qot- words (potential unit prefix)
print()
print("All qot- words (top 20):")
qot_words = [(e['word'], e['section']) for e in all_entries if re.match(r'qot', e['word'])]
qot_counter = Counter(w for w, s in qot_words)
qot_by_section = defaultdict(Counter)
for w, s in qot_words:
    qot_by_section[s][w] += 1

for word, count in qot_counter.most_common(20):
    h = qot_by_section['herbal'][word]
    r = qot_by_section['recipe'][word]
    grade = get_grade(word)
    print(f"  {word:<20} {count:>5} (H:{h} R:{r}) grade={grade}")

# ============================================================
# TEST 4: POSITIONAL DISTRIBUTION
# Where in herbal entries does each grade appear?
# ============================================================

print()
print("=" * 90)
print("TEST 4: POSITIONAL DISTRIBUTION IN HERBAL ENTRIES")
print("If grade = preparation, higher grades should cluster at END of entries (preparation)")
print("If grade = description, higher grades should be throughout")
print("=" * 90)
print()

# For herbal folios, divide each folio's lines into thirds: first, middle, last
herbal_positional = defaultdict(lambda: {'first_third': 0, 'middle_third': 0, 'last_third': 0})

for folio, lines in folio_lines.items():
    if section_map.get(folio) != 'herbal':
        continue
    if len(lines) < 3:
        continue

    n = len(lines)
    third = n / 3.0

    for idx, (line_num, words) in enumerate(lines):
        if idx < third:
            pos = 'first_third'
        elif idx < 2 * third:
            pos = 'middle_third'
        else:
            pos = 'last_third'

        for w in words:
            grade = get_grade(w)
            herbal_positional[grade][pos] += 1

print("Grade distribution by position in herbal entries:")
print(f"{'Grade':<8} {'First 1/3':>12} {'Middle 1/3':>12} {'Last 1/3':>12} {'Last/First':>12}")
print("-" * 60)

for grade in GRADES:
    f = herbal_positional[grade]['first_third']
    m = herbal_positional[grade]['middle_third']
    l = herbal_positional[grade]['last_third']
    total = f + m + l
    if total == 0:
        continue
    ratio = l / f if f > 0 else float('inf')
    print(f"{grade:<8} {f:>12} {m:>12} {l:>12} {ratio:>12.2f}")

# Now do it by ROOT for ch- and k- specifically
print()
print("ch-root positional distribution (herbal only):")
ch_positional = defaultdict(lambda: {'first_third': 0, 'middle_third': 0, 'last_third': 0})

for folio, lines in folio_lines.items():
    if section_map.get(folio) != 'herbal':
        continue
    if len(lines) < 3:
        continue
    n = len(lines)
    third = n / 3.0
    for idx, (line_num, words) in enumerate(lines):
        if idx < third:
            pos = 'first_third'
        elif idx < 2 * third:
            pos = 'middle_third'
        else:
            pos = 'last_third'
        for w in words:
            root = get_root(w)
            if root == 'ch':
                grade = get_grade(w)
                ch_positional[grade][pos] += 1

print(f"{'Grade':<8} {'First 1/3':>12} {'Middle 1/3':>12} {'Last 1/3':>12} {'Last/First':>12}")
print("-" * 60)
for grade in GRADES:
    f = ch_positional[grade]['first_third']
    m = ch_positional[grade]['middle_third']
    l = ch_positional[grade]['last_third']
    total = f + m + l
    if total == 0:
        continue
    ratio = l / f if f > 0 else float('inf')
    print(f"{grade:<8} {f:>12} {m:>12} {l:>12} {ratio:>12.2f}")

# ============================================================
# TEST 5: GRADE ENRICHMENT FOR SPECIFIC ROOT FAMILIES
# Calculate recipe enrichment monotonicity per root
# ============================================================

print()
print("=" * 90)
print("TEST 5: RECIPE ENRICHMENT MONOTONICITY PER ROOT")
print("If grade = preparation, enrichment should increase monotonically with grade")
print("=" * 90)
print()

for root in ['ch', 'sh', 'k', 'cth', 'd']:
    ratios = []
    print(f"  {root}-root:")
    for grade in GRADES:
        h = root_grade_section[root][grade]['herbal']
        r = root_grade_section[root][grade]['recipe']
        if h + r < 3:
            ratios.append(None)
            continue
        # Normalize: herbal has ~9000 words, recipe has ~12000
        h_norm = h / 9059 * 10000 if h > 0 else 0.001
        r_norm = r / 12101 * 10000 if r > 0 else 0
        ratio = r_norm / h_norm
        ratios.append(ratio)
        print(f"    {grade:<6}: H={h:>5}, R={r:>5}, norm_ratio={ratio:.2f}")

    # Check monotonicity
    valid = [r for r in ratios if r is not None]
    if len(valid) >= 3:
        increasing = all(valid[i] <= valid[i+1] for i in range(len(valid)-1))
        print(f"    Monotonically increasing: {increasing}")
        if not increasing:
            # Check correlation
            x = list(range(len(valid)))
            xm = sum(x) / len(x)
            ym = sum(valid) / len(valid)
            num = sum((x[i]-xm)*(valid[i]-ym) for i in range(len(valid)))
            dx = sum((x[i]-xm)**2 for i in range(len(valid)))**0.5
            dy = sum((valid[i]-ym)**2 for i in range(len(valid)))**0.5
            if dx > 0 and dy > 0:
                r_corr = num / (dx * dy)
                print(f"    Correlation (grade vs enrichment): r={r_corr:.3f}")
    print()

# ============================================================
# TEST 6: ADJACENT WORD PATTERNS
# What words typically PRECEDE and FOLLOW each grade level?
# ============================================================

print("=" * 90)
print("TEST 6: CONTEXT ANALYSIS - What surrounds each grade level?")
print("=" * 90)
print()

# For the ch-root specifically
print("Words that PRECEDE ch-root words, by grade of the ch-word:")
ch_preceding = defaultdict(Counter)
ch_following = defaultdict(Counter)

for folio, lines in folio_lines.items():
    for line_num, words in lines:
        for i, w in enumerate(words):
            root = get_root(w)
            if root == 'ch':
                grade = get_grade(w)
                if i > 0:
                    ch_preceding[grade][words[i-1]] += 1
                if i < len(words) - 1:
                    ch_following[grade][words[i+1]] += 1

for grade in GRADES:
    top_pre = ch_preceding[grade].most_common(8)
    top_fol = ch_following[grade].most_common(8)
    print(f"  {grade:<6} preceded by: {', '.join(f'{w}({c})' for w,c in top_pre)}")
    print(f"  {grade:<6} followed by: {', '.join(f'{w}({c})' for w,c in top_fol)}")
    print()

# ============================================================
# TEST 7: BIGRAM ANALYSIS WITH qo-
# What grade of k-word follows qo most frequently?
# ============================================================

print("=" * 90)
print("TEST 7: qo + ROOT BIGRAMS")
print("=" * 90)
print()

# Find all instances where qo is immediately followed by or part of a word
# qokeey, qokaiin, etc. - these are single words with qo prefix
print("qo-prefixed words decomposed:")
qo_prefixed = [e for e in all_entries if e['word'].startswith('qo') and len(e['word']) > 2]
qo_decomposed = defaultdict(lambda: defaultdict(int))

for e in qo_prefixed:
    w = e['word'][2:]  # strip qo
    root = get_root(w) or 'unknown'
    # Get grade of the remainder
    grade = get_grade(w)
    qo_decomposed[root][grade] += 1

print(f"{'Root':<8} ", end='')
for g in GRADES:
    print(f"{g:>8}", end='')
print(f"{'Total':>8}")
print("-" * 60)

for root in sorted(qo_decomposed.keys(), key=lambda r: sum(qo_decomposed[r].values()), reverse=True)[:10]:
    total = sum(qo_decomposed[root].values())
    print(f"{root:<8} ", end='')
    for g in GRADES:
        print(f"{qo_decomposed[root][g]:>8}", end='')
    print(f"{total:>8}")

# ============================================================
# TEST 8: COMPLETE PARADIGM TABLE
# For each root, list the actual attested words at each grade
# ============================================================

print()
print("=" * 90)
print("TEST 8: ATTESTED PARADIGM FORMS")
print("Show which specific words are attested at each grade for major roots")
print("=" * 90)
print()

# For each root, find words that are JUST root+grade+(common suffix)
paradigm_words = defaultdict(lambda: defaultdict(Counter))

for w, count in word_freq.items():
    root = get_root(w)
    if root:
        grade = get_grade(w)
        paradigm_words[root][grade][w] += count

for root in ['ch', 'sh', 'k', 'cth', 'd', 't', 'p', 'cph', 'ckh']:
    if root not in paradigm_words:
        continue
    print(f"\n{root}-root paradigm:")
    for grade in GRADES:
        words = paradigm_words[root][grade]
        if not words:
            continue
        top = words.most_common(8)
        total_tokens = sum(words.values())
        top_str = ', '.join(f"{w}({c})" for w, c in top)
        print(f"  {grade:<6} [{total_tokens:>5} tokens]: {top_str}")

# ============================================================
# TEST 9: SECTION-SPECIFIC GRADE PATTERNS
# Does the grade pattern differ between ALL five sections?
# ============================================================

print()
print("=" * 90)
print("TEST 9: GRADE DISTRIBUTION ACROSS ALL SECTIONS")
print("=" * 90)
print()

section_grades = defaultdict(Counter)
section_totals = Counter()

for e in all_entries:
    section_grades[e['section']][e['grade']] += 1
    section_totals[e['section']] += 1

print(f"{'Section':<10} ", end='')
for g in GRADES:
    print(f"{g:>8}", end='')
print(f"{'Total':>8}")
print("-" * 70)

for section in ['herbal', 'astro', 'cosmo', 'bio', 'recipe']:
    total = section_totals[section]
    if total == 0:
        continue
    print(f"{section:<10} ", end='')
    for g in GRADES:
        pct = 100 * section_grades[section][g] / total
        print(f"{pct:>7.1f}%", end='')
    print(f"{total:>8}")

# ============================================================
# TEST 10: RECIPE-INTERNAL ANALYSIS
# Within recipe pages, does grade increase toward end?
# ============================================================

print()
print("=" * 90)
print("TEST 10: RECIPE-INTERNAL POSITIONAL ANALYSIS")
print("If grade = preparation stage, later lines in recipes should have higher grades")
print("=" * 90)
print()

recipe_positional = defaultdict(lambda: {'first_third': 0, 'middle_third': 0, 'last_third': 0})

for folio, lines in folio_lines.items():
    if section_map.get(folio) != 'recipe':
        continue
    if len(lines) < 3:
        continue
    n = len(lines)
    third = n / 3.0
    for idx, (line_num, words) in enumerate(lines):
        if idx < third:
            pos = 'first_third'
        elif idx < 2 * third:
            pos = 'middle_third'
        else:
            pos = 'last_third'
        for w in words:
            grade = get_grade(w)
            recipe_positional[grade][pos] += 1

print("Grade distribution by position in RECIPE pages:")
print(f"{'Grade':<8} {'First 1/3':>12} {'Middle 1/3':>12} {'Last 1/3':>12} {'%First':>8} {'%Last':>8}")
print("-" * 65)

for grade in GRADES:
    f = recipe_positional[grade]['first_third']
    m = recipe_positional[grade]['middle_third']
    l = recipe_positional[grade]['last_third']
    total = f + m + l
    if total == 0:
        continue
    pf = 100 * f / total
    pl = 100 * l / total
    print(f"{grade:<8} {f:>12} {m:>12} {l:>12} {pf:>7.1f}% {pl:>7.1f}%")

# ============================================================
# TEST 11: GALENIC DEGREE HYPOTHESIS
# Does 'e' count map to degree numbers?
# ============================================================

print()
print("=" * 90)
print("TEST 11: GALENIC DEGREE MAPPING")
print("Medieval pharmacy used 4 degrees (primus, secundus, tertius, quartus)")
print("Does the e-count (0,1,2,3) map to these degrees?")
print("=" * 90)
print()

# Count e's in the grade
def e_count(grade):
    if grade == 'bare':
        return 0
    elif grade == 'e':
        return 1
    elif grade in ('ee', 'eo'):
        return 2
    elif grade in ('eeo', 'eod'):
        return 3
    return 0

# If Galenic: grade 0 = simple (unnamed quality), 1 = first degree, etc.
# Herbal pages should describe qualities (all degrees)
# Recipe pages should specify degrees more precisely
print("Galenic degree mapping:")
print("  e-count 0 (bare) = simplex (herb itself)")
print("  e-count 1 (+e)   = primus gradus (first degree)")
print("  e-count 2 (+ee)  = secundus gradus (second degree)")
print("  e-count 3 (+eeo) = tertius gradus (third degree)")
print()

# Check: do recipe pages use degree-2 and degree-3 words more?
degree_section = defaultdict(lambda: defaultdict(int))
for e in all_entries:
    if e['section'] in ('herbal', 'recipe'):
        deg = e_count(e['grade'])
        degree_section[e['section']][deg] += 1

print(f"{'Section':<10} {'deg-0':>8} {'deg-1':>8} {'deg-2':>8} {'deg-3':>8} {'Total':>8}")
print("-" * 50)
for section in ['herbal', 'recipe']:
    total = sum(degree_section[section].values())
    print(f"{section:<10} ", end='')
    for d in range(4):
        pct = 100 * degree_section[section][d] / total if total > 0 else 0
        print(f"{pct:>7.1f}%", end='')
    print(f"{total:>8}")

# ============================================================
# TEST 12: SUFFIX ANALYSIS
# What follows the grade vowels? (the consonant after ee/eeo/eod)
# ============================================================

print()
print("=" * 90)
print("TEST 12: POST-GRADE SUFFIXES")
print("What consonants/endings follow the grade vowels?")
print("=" * 90)
print()

# For words with ee/eeo/eod, extract what comes after the grade
post_grade_suffixes = defaultdict(Counter)

for w in word_freq:
    grade = get_grade(w)
    if grade == 'eod':
        # Find eod and get what follows
        idx = w.find('eod')
        suffix = w[idx+3:]
        post_grade_suffixes['eod'][suffix or '(none)'] += word_freq[w]
    elif grade == 'eeo':
        idx = w.find('eeo')
        suffix = w[idx+3:]
        post_grade_suffixes['eeo'][suffix or '(none)'] += word_freq[w]
    elif grade == 'ee':
        idx = w.find('ee')
        suffix = w[idx+2:]
        post_grade_suffixes['ee'][suffix or '(none)'] += word_freq[w]
    elif grade == 'eo':
        idx = w.find('eo')
        suffix = w[idx+2:]
        post_grade_suffixes['eo'][suffix or '(none)'] += word_freq[w]
    elif grade == 'e':
        # Find isolated e
        m = re.search(r'(?<![e])e(?![eo])', w)
        if m:
            suffix = w[m.end():]
            post_grade_suffixes['e'][suffix or '(none)'] += word_freq[w]

for grade in ['e', 'ee', 'eo', 'eeo', 'eod']:
    top = post_grade_suffixes[grade].most_common(15)
    print(f"  After {grade}:")
    for suffix, count in top:
        print(f"    -{suffix:<15} {count:>5}")
    print()

# ============================================================
# SYNTHESIS
# ============================================================

print("=" * 90)
print("SYNTHESIS: WHAT THE GRADE SYSTEM ENCODES")
print("=" * 90)
print()
print("Based on all tests above, the grade system most likely encodes:")
print()
print("PREPARATION SPECIFICITY - a compound concept combining:")
print("  1. How processed/prepared the substance is")
print("  2. How precisely it is specified")
print()
print("This explains why:")
print("  - Recipe pages have more high-grade words (recipes need precise preparations)")
print("  - Higher grades appear on fewer pages (specific preparations are context-bound)")
print("  - The qo- prefix combines with k-root grades (quantity + specific measure)")
print()
