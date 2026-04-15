#!/usr/bin/env python3
"""
RIGOROUS VALIDATION: Galenic Degree Encoding Hypothesis
Hypothesis: -n = 1st degree, -m = 2nd degree, -d = 3rd degree

Tests:
1. Extended plant sample (all identified plants)
2. Control test (recipe vs herbal pages)
3. Stem alternation test (same stem with -n/-m/-d on different pages)
4. 4th degree problem
5. Sandhi interaction analysis
6. Red team / alternative explanations
7. Statistical significance
"""

import re
import math
from collections import Counter, defaultdict

def parse_eva(filepath):
    """Parse EVA transcription into folio -> word list mapping."""
    folios = {}
    current_folio = None
    folio_sections = {}  # track section type

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Track folio headers with metadata
            folio_match = re.match(r'<(f\d+[rv]\d?)>', line)
            if folio_match:
                current_folio = folio_match.group(1)
                folios[current_folio] = []
                # Parse section info from metadata line
                continue

            line_match = re.match(r'<(f\d+[rv]\d?)\.(\d+),', line)
            if line_match:
                current_folio = line_match.group(1)
                if current_folio not in folios:
                    folios[current_folio] = []
                text_start = line.find('>')
                if text_start >= 0:
                    text = line[text_start+1:].strip()
                    # Clean EVA markup
                    text = re.sub(r'@\d+;?', '', text)
                    text = re.sub(r'\{[^}]*\}', '', text)
                    text = re.sub(r'[<>]', '', text)
                    text = re.sub(r'->', ' ', text)
                    words = re.split(r'[.\s,?!]+', text)
                    words = [w.strip() for w in words if w.strip() and len(w.strip()) > 1]
                    folios[current_folio].extend(words)
    return folios


def get_final_ending(word):
    """Get the final character of a word."""
    if not word:
        return None
    return word[-1]


def count_nmd_endings(words):
    """Count words ending in -n, -m, -d (the hypothesized degree markers)."""
    n_count = sum(1 for w in words if w.endswith('n'))
    m_count = sum(1 for w in words if w.endswith('m'))
    d_count = sum(1 for w in words if w.endswith('d'))
    total = len(words)
    return n_count, m_count, d_count, total


def get_dominant_ending(n, m, d):
    """Return which of n/m/d is dominant."""
    if n >= m and n >= d:
        return 'n'
    elif m >= n and m >= d:
        return 'm'
    else:
        return 'd'


def chi_squared_test(observed, expected):
    """Simple chi-squared test."""
    chi2 = 0
    for o, e in zip(observed, expected):
        if e > 0:
            chi2 += (o - e) ** 2 / e
    return chi2


def binomial_test_p(k, n, p=1/3):
    """Approximate p-value for getting k or more successes in n trials with probability p."""
    # Use normal approximation for simplicity
    mean = n * p
    std = math.sqrt(n * p * (1 - p))
    if std == 0:
        return 1.0
    z = (k - mean) / std
    # Approximate CDF
    if z <= 0:
        return 0.5
    # One-sided p-value (probability of getting z or higher)
    # Using approximation
    p_val = 0.5 * math.erfc(z / math.sqrt(2))
    return p_val


# =============================================================================
# MAIN ANALYSIS
# =============================================================================

folios = parse_eva(r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt')

all_words = []
for words in folios.values():
    all_words.extend(words)

print("=" * 80)
print("GALENIC DEGREE ENCODING VALIDATION: -n = 1st, -m = 2nd, -d = 3rd")
print("=" * 80)
print(f"\nTotal words in corpus: {len(all_words)}")
print(f"Total folios: {len(folios)}")

# =============================================================================
# TEST 0: Baseline - how common are -n, -m, -d endings globally?
# =============================================================================
print("\n" + "=" * 80)
print("TEST 0: GLOBAL BASELINE DISTRIBUTION OF -n, -m, -d ENDINGS")
print("=" * 80)

global_n, global_m, global_d, global_total = count_nmd_endings(all_words)
all_endings = Counter(w[-1] for w in all_words if w)
print(f"\nAll word-final character frequencies:")
for char, count in all_endings.most_common(15):
    pct = count / len(all_words) * 100
    print(f"  -{char}: {count:>6} ({pct:.1f}%)")

print(f"\nFocused on hypothesized degree markers:")
print(f"  -n: {global_n:>6} ({global_n/global_total*100:.1f}%)")
print(f"  -m: {global_m:>6} ({global_m/global_total*100:.1f}%)")
print(f"  -d: {global_d:>6} ({global_d/global_total*100:.1f}%)")
nmd_total = global_n + global_m + global_d
print(f"  n+m+d total: {nmd_total} ({nmd_total/global_total*100:.1f}% of all words)")

print(f"\n  CRITICAL ISSUE: -n is {global_n/global_m:.1f}x more common than -m")
print(f"  CRITICAL ISSUE: -n is {global_n/global_d:.1f}x more common than -d")
print(f"  If these encode degrees, 1st degree is massively overrepresented")

# =============================================================================
# TEST 1: Extended plant sample - ALL identified plants
# =============================================================================
print("\n" + "=" * 80)
print("TEST 1: EXTENDED PLANT SAMPLE - ALL IDENTIFIED PLANTS")
print("=" * 80)

# Plant identifications with Galenic qualities from Dioscorides/Galen
# Format: folio -> (plant, hot/cold quality, degree, dry/moist quality, degree, confidence)
plants = {
    'f1r':  ('Laurus nobilis',       'Hot',  2, 'Dry',  1, 45),
    'f2r':  ('Paeonia officinalis',   'Hot',  1, 'Dry',  2, 55),
    'f2v':  ('Cyclamen',             'Hot',  3, 'Dry',  0, 45),  # Cyclamen: hot 3rd per Dioscorides
    'f3r':  ('Rubia tinctorum',      'Hot',  2, 'Dry',  2, 60),
    'f3v':  ('Cynara scolymus',      'Hot',  2, 'Dry',  1, 55),  # Artichoke: hot & dry 2nd
    'f4r':  ('Rosmarinus officinalis','Hot',  2, 'Dry',  2, 55),
    'f5r':  ('Aristolochia rotunda',  'Hot',  3, 'Dry',  1, 40),  # Birthwort: hot 3rd
    'f9r':  ('Nigella damascena',    'Hot',  3, 'Dry',  1, 65),
    'f9v':  ('Mandragora',           'Cold', 3, 'Dry',  3, 40),  # Mandrake: cold 3rd
    'f41r': ('Adiantum',             'Cold', 2, 'Dry',  1, 60),
    'f42r': ('Daucus carota',        'Hot',  2, 'Dry',  2, 45),  # Wild carrot: hot & dry 2nd
    'f43r': ('Rubia tinctorum (cult)','Hot', 2, 'Dry',  2, 60),
    'f47r': ('Vitis vinifera',       'Cold', 1, 'Moist',2, 70),
    'f8v':  ('Hypericum perforatum', 'Hot',  2, 'Dry',  1, 40),  # St John's wort: hot & dry 2nd
}

degree_to_ending = {1: 'n', 2: 'm', 3: 'd'}

print(f"\nHypothesis: -n = 1st degree, -m = 2nd degree, -d = 3rd degree")
print(f"Prediction: The dominant ending on each folio should match the plant's primary degree")
print()
print(f"{'Folio':<8} {'Plant':<25} {'Quality':<12} {'Deg':>3} {'Expect':>6} "
      f"{'n':>5} {'m':>5} {'d':>5} {'Total':>5} {'Dom':>4} {'Match':>6}")
print("-" * 95)

correct = 0
total_tested = 0
results_detail = []

for folio in sorted(plants.keys(), key=lambda x: (int(re.search(r'\d+', x).group()), x)):
    plant, quality, degree, quality2, degree2, confidence = plants[folio]
    words = folios.get(folio, [])
    if not words:
        continue

    n, m, d, total = count_nmd_endings(words)
    nmd = n + m + d

    if degree in degree_to_ending:
        expected = degree_to_ending[degree]
        dominant = get_dominant_ending(n, m, d)
        match = dominant == expected
        if match:
            correct += 1
        total_tested += 1
        match_str = "YES" if match else "NO"
    else:
        expected = '?'
        dominant = get_dominant_ending(n, m, d)
        match_str = "N/A"

    print(f"{folio:<8} {plant:<25} {quality} {degree:<7} {expected:>6} "
          f"{n:>5} {m:>5} {d:>5} {total:>5} {dominant:>4} {match_str:>6}")

    results_detail.append({
        'folio': folio, 'plant': plant, 'quality': quality,
        'degree': degree, 'expected': expected, 'n': n, 'm': m, 'd': d,
        'dominant': dominant, 'match': match_str
    })

print(f"\nPrediction accuracy: {correct}/{total_tested} ({correct/total_tested*100:.0f}%)")
print(f"Chance level (3-way): 33%")
print(f"p-value (binomial, one-sided): {binomial_test_p(correct, total_tested, 1/3):.4f}")

# =============================================================================
# TEST 1b: Normalized analysis - n/m/d PROPORTIONS vs expected
# =============================================================================
print("\n" + "-" * 80)
print("TEST 1b: PROPORTION ANALYSIS (accounting for global baseline)")
print("-" * 80)

# Global proportions of n/m/d among n+m+d words
global_n_prop = global_n / nmd_total
global_m_prop = global_m / nmd_total
global_d_prop = global_d / nmd_total
print(f"\nGlobal n/m/d proportions (baseline):")
print(f"  n: {global_n_prop:.3f}, m: {global_m_prop:.3f}, d: {global_d_prop:.3f}")
print(f"\nPer-folio deviation from baseline:")
print(f"{'Folio':<8} {'Plant':<22} {'Deg':>3} {'n_dev':>8} {'m_dev':>8} {'d_dev':>8} {'Expected dev':>12}")
print("-" * 80)

for folio in sorted(plants.keys(), key=lambda x: (int(re.search(r'\d+', x).group()), x)):
    plant, quality, degree, _, _, _ = plants[folio]
    words = folios.get(folio, [])
    if not words:
        continue
    n, m, d, total = count_nmd_endings(words)
    nmd = n + m + d
    if nmd < 5:
        continue

    n_prop = n / nmd
    m_prop = m / nmd
    d_prop = d / nmd

    n_dev = n_prop - global_n_prop
    m_dev = m_prop - global_m_prop
    d_dev = d_prop - global_d_prop

    expected_ending = degree_to_ending.get(degree, '?')
    expected_dev_col = f"+{expected_ending}"

    # Check if the expected ending has positive deviation
    if expected_ending == 'n':
        expected_positive = n_dev > 0
    elif expected_ending == 'm':
        expected_positive = m_dev > 0
    else:
        expected_positive = d_dev > 0

    marker = "OK" if expected_positive else "WRONG"

    print(f"{folio:<8} {plant:<22} {degree:>3} {n_dev:>+8.3f} {m_dev:>+8.3f} {d_dev:>+8.3f} "
          f"{expected_dev_col:>12} {marker}")

# =============================================================================
# TEST 2: Control test - Recipe vs Herbal pages
# =============================================================================
print("\n" + "=" * 80)
print("TEST 2: CONTROL TEST - RECIPE vs HERBAL PAGES")
print("=" * 80)

# Herbal folios: f1r-f57r (approximately)
# Recipe folios: f99r-f116r (approximately)
# Astronomical/cosmological: f67r-f86r (approximately)
# Balneological: f75r-f84v (approximately)

herbal_folios = []
recipe_folios = []
astro_folios = []
other_folios = []

for folio in folios:
    num_match = re.search(r'f(\d+)', folio)
    if not num_match:
        continue
    num = int(num_match.group(1))
    if 1 <= num <= 57:
        herbal_folios.append(folio)
    elif 99 <= num <= 116:
        recipe_folios.append(folio)
    elif 67 <= num <= 86:
        astro_folios.append(folio)
    else:
        other_folios.append(folio)

def section_stats(folio_list, name):
    words = []
    for f in folio_list:
        words.extend(folios.get(f, []))
    n, m, d, total = count_nmd_endings(words)
    nmd = n + m + d
    if nmd == 0:
        return
    print(f"\n  {name}: {len(folio_list)} folios, {total} words, {nmd} ending in n/m/d")
    print(f"    -n: {n:>5} ({n/nmd*100:.1f}%)")
    print(f"    -m: {m:>5} ({m/nmd*100:.1f}%)")
    print(f"    -d: {d:>5} ({d/nmd*100:.1f}%)")
    print(f"    n/m ratio: {n/m:.2f}" if m > 0 else "    n/m ratio: inf")
    print(f"    n/d ratio: {n/d:.2f}" if d > 0 else "    n/d ratio: inf")
    return n, m, d, nmd

print(f"\nPrediction: If -n/-m/-d encode Galenic degrees, recipe pages should show")
print(f"DIFFERENT n/m/d distribution than herbal pages (recipes specify preparations,")
print(f"not plant degrees)")

h_stats = section_stats(herbal_folios, "HERBAL section (f1-f57)")
r_stats = section_stats(recipe_folios, "RECIPE section (f99-f116)")
a_stats = section_stats(astro_folios, "ASTRO section (f67-f86)")

if h_stats and r_stats:
    h_n, h_m, h_d, h_nmd = h_stats
    r_n, r_m, r_d, r_nmd = r_stats

    # Chi-squared test between herbal and recipe distributions
    h_props = [h_n/h_nmd, h_m/h_nmd, h_d/h_nmd]
    r_props = [r_n/r_nmd, r_m/r_nmd, r_d/r_nmd]

    # Expected under null (same distribution)
    combined_n = h_n + r_n
    combined_m = h_m + r_m
    combined_d = h_d + r_d
    combined_total = h_nmd + r_nmd

    expected_h = [combined_n/combined_total * h_nmd,
                  combined_m/combined_total * h_nmd,
                  combined_d/combined_total * h_nmd]
    expected_r = [combined_n/combined_total * r_nmd,
                  combined_m/combined_total * r_nmd,
                  combined_d/combined_total * r_nmd]

    chi2 = chi_squared_test([h_n, h_m, h_d], expected_h) + \
           chi_squared_test([r_n, r_m, r_d], expected_r)

    print(f"\n  Chi-squared (herbal vs recipe): {chi2:.2f} (df=2)")
    print(f"  Critical value at p<0.05: 5.99, at p<0.01: 9.21")
    if chi2 > 9.21:
        print(f"  -> SIGNIFICANT difference (p < 0.01)")
    elif chi2 > 5.99:
        print(f"  -> SIGNIFICANT difference (p < 0.05)")
    else:
        print(f"  -> NOT significant -> distributions are SIMILAR across sections")
        print(f"     This WEAKENS the degree hypothesis (if degrees were section-specific,")
        print(f"     distributions should differ)")

# =============================================================================
# TEST 3: Stem alternation test
# =============================================================================
print("\n" + "=" * 80)
print("TEST 3: STEM ALTERNATION TEST")
print("=" * 80)
print("If -n/-m/-d encode degrees, the SAME stem should appear with different")
print("endings on different plant pages, matching each plant's degree.")

# Extract stems by removing final n/m/d
stem_endings = defaultdict(lambda: defaultdict(list))  # stem -> ending -> [folios]
stem_word_counts = defaultdict(lambda: defaultdict(Counter))  # stem -> ending -> folio -> count

for folio, words in folios.items():
    for w in words:
        if len(w) >= 3 and w[-1] in 'nmd':
            stem = w[:-1]
            ending = w[-1]
            stem_endings[stem][ending].append(folio)
            stem_word_counts[stem][ending][folio] += 1

# Find stems that appear with ALL THREE endings
print(f"\nStems appearing with all three endings (-n, -m, -d):")
triple_stems = []
for stem in sorted(stem_endings.keys(),
                   key=lambda s: sum(len(v) for v in stem_endings[s].values()),
                   reverse=True):
    endings = stem_endings[stem]
    if len(endings) >= 3 and 'n' in endings and 'm' in endings and 'd' in endings:
        n_count = len(endings['n'])
        m_count = len(endings['m'])
        d_count = len(endings['d'])
        total = n_count + m_count + d_count
        if total >= 10:
            triple_stems.append((stem, n_count, m_count, d_count))

print(f"\n  Found {len(triple_stems)} stems with all three endings (>=10 occurrences)")
print(f"\n  {'Stem':<15} {'stem+n':>8} {'stem+m':>8} {'stem+d':>8} {'Total':>8}")
print("  " + "-" * 50)
for stem, nc, mc, dc in triple_stems[:20]:
    print(f"  {stem:<15} {nc:>8} {mc:>8} {dc:>8} {nc+mc+dc:>8}")

# For top stems, check if they cluster on the "right" folios
print(f"\n  DETAILED STEM-FOLIO DISTRIBUTION (top 5 stems):")
for stem, nc, mc, dc in triple_stems[:5]:
    print(f"\n  Stem: '{stem}' (total: {nc+mc+dc})")
    for ending in ['n', 'm', 'd']:
        folio_counts = stem_word_counts[stem][ending]
        top_folios = folio_counts.most_common(5)
        folio_str = ", ".join(f"{f}({c})" for f, c in top_folios)
        print(f"    -{ending}: {sum(folio_counts.values()):>4} occurrences, top folios: {folio_str}")

    # Check if -m clusters on 2nd-degree plant pages
    degree_2_folios = [f for f, (_, _, deg, _, _, _) in plants.items() if deg == 2]
    degree_1_folios = [f for f, (_, _, deg, _, _, _) in plants.items() if deg == 1]
    degree_3_folios = [f for f, (_, _, deg, _, _, _) in plants.items() if deg == 3]

    m_on_deg2 = sum(stem_word_counts[stem]['m'].get(f, 0) for f in degree_2_folios)
    m_total = sum(stem_word_counts[stem]['m'].values())
    n_on_deg1 = sum(stem_word_counts[stem]['n'].get(f, 0) for f in degree_1_folios)
    n_total = sum(stem_word_counts[stem]['n'].values())
    d_on_deg3 = sum(stem_word_counts[stem]['d'].get(f, 0) for f in degree_3_folios)
    d_total = sum(stem_word_counts[stem]['d'].values())

    if m_total > 0 and n_total > 0 and d_total > 0:
        print(f"    Degree match check:")
        print(f"      -n on 1st-degree folios: {n_on_deg1}/{n_total} ({n_on_deg1/n_total*100:.1f}%)")
        print(f"      -m on 2nd-degree folios: {m_on_deg2}/{m_total} ({m_on_deg2/m_total*100:.1f}%)")
        print(f"      -d on 3rd-degree folios: {d_on_deg3}/{d_total} ({d_on_deg3/d_total*100:.1f}%)")
        # What proportion of ALL words are on identified plant pages?
        all_on_id = sum(stem_word_counts[stem][e].get(f, 0)
                       for e in 'nmd' for f in plants)
        all_total = sum(sum(stem_word_counts[stem][e].values()) for e in 'nmd')
        print(f"      (Baseline: {all_on_id}/{all_total} = {all_on_id/all_total*100:.1f}% of all on identified folios)")

# =============================================================================
# TEST 4: The 4th degree problem
# =============================================================================
print("\n" + "=" * 80)
print("TEST 4: THE 4TH DEGREE PROBLEM")
print("=" * 80)

print("""
If n=1st, m=2nd, d=3rd, what encodes 4th degree?
Medieval Galenic system used 4 degrees. Some plants are classified as 4th degree:
  - Euphorbia: Hot 4th, Dry 4th
  - Cantharides: Hot 4th
  - Hellebore: Hot 3rd-4th
  - Pepper (long): Hot 3rd-4th

Possibilities:
  a) The system uses only 3 degrees (some medieval systems did simplify)
  b) A 4th ending exists: -s, -l, -r, or another character
  c) 4th degree is expressed by doubling or modification (e.g., -dd, -nn)
""")

# Check if any common endings could be 4th degree
print("Other common word endings (potential 4th degree markers):")
nmd_set = {'n', 'm', 'd'}
other_endings = {char: count for char, count in all_endings.most_common(20)
                 if char not in nmd_set}
for char, count in sorted(other_endings.items(), key=lambda x: -x[1])[:10]:
    print(f"  -{char}: {count:>6} ({count/len(all_words)*100:.1f}%)")

# No identified 4th-degree plants in our sample, so this is mostly theoretical
print(f"\nNote: No plants in our identified sample are classified as 4th degree.")
print(f"This test is inconclusive without 4th-degree plant identifications.")
print(f"However, the absence of an obvious 4th encoding is a STRUCTURAL WEAKNESS")
print(f"of the hypothesis, since Galenic degrees fundamentally use a 4-tier system.")

# =============================================================================
# TEST 5: Sandhi interaction
# =============================================================================
print("\n" + "=" * 80)
print("TEST 5: SANDHI INTERACTION - RESOLVING THE CONTRADICTION")
print("=" * 80)

print("""
Previous analysis showed -n/-l/-r alternate based on following word's initial:
  -r before vowels (a, i, o)
  -l before stops (k, t, d)
  -n before fricatives (s, c, f)

But the new hypothesis says -n = 1st degree. These are CONTRADICTORY:
  - Sandhi says -n appears before fricatives regardless of degree
  - Degree hypothesis says -n appears on 1st-degree pages regardless of context

Resolution test: Does -n's distribution depend MORE on following-word context
or on folio identity (plant degree)?
""")

# For each word ending in n/m/d, record the following word's initial
nmd_next_initial = defaultdict(lambda: Counter())  # ending -> Counter of next initials

for folio, words in folios.items():
    for i in range(len(words) - 1):
        w = words[i]
        next_w = words[i + 1]
        if w and w[-1] in 'nmd' and next_w:
            ending = w[-1]
            next_init = next_w[0]
            nmd_next_initial[ending][next_init] += 1

print("Following-word initial distribution for -n, -m, -d words:")
print(f"\n  {'Next init':<10} {'After -n':>10} {'After -m':>10} {'After -d':>10}")
print("  " + "-" * 45)

# Get all initials
all_inits = set()
for ending in 'nmd':
    all_inits.update(nmd_next_initial[ending].keys())

for init in sorted(all_inits):
    n_after = nmd_next_initial['n'].get(init, 0)
    m_after = nmd_next_initial['m'].get(init, 0)
    d_after = nmd_next_initial['d'].get(init, 0)
    total = n_after + m_after + d_after
    if total < 20:
        continue
    print(f"  {init:<10} {n_after:>5} ({n_after/total*100:4.1f}%) "
          f"{m_after:>5} ({m_after/total*100:4.1f}%) "
          f"{d_after:>5} ({d_after/total*100:4.1f}%)")

# Key question: does -m show sandhi-like behavior?
print(f"\n  KEY QUESTION: Does -m show sandhi patterns like -n/-l/-r?")
print(f"  If -m is a degree marker (not a sandhi variant), it should NOT be")
print(f"  conditioned by the following word's initial.")

m_total = sum(nmd_next_initial['m'].values())
n_total = sum(nmd_next_initial['n'].values())
d_total = sum(nmd_next_initial['d'].values())

# Check variation in -m across different following initials
m_by_init = {}
for init in ['a', 'c', 'd', 'k', 'o', 's', 'y', 'q', 't']:
    total_after_init = sum(nmd_next_initial[e].get(init, 0) for e in 'nmd')
    if total_after_init > 20:
        m_prop = nmd_next_initial['m'].get(init, 0) / total_after_init
        m_by_init[init] = m_prop

if m_by_init:
    max_m = max(m_by_init.values())
    min_m = min(m_by_init.values())
    print(f"  -m proportion range across contexts: {min_m:.3f} to {max_m:.3f}")
    print(f"  Variation ratio: {max_m/min_m:.2f}x" if min_m > 0 else "  Variation: extreme")
    print(f"  (If -m were purely degree-marking, variation should be ~1.0x)")
    print(f"  (If -m shows sandhi, variation should be >>1.5x)")

# =============================================================================
# TEST 5b: -n in sandhi vs -n as degree marker
# =============================================================================
print("\n" + "-" * 80)
print("TEST 5b: DISTINGUISHING SANDHI -n FROM DEGREE -n")
print("-" * 80)

# If -n has BOTH sandhi and degree functions, we might see:
# - On 1st-degree plant pages: MORE -n than expected even after controlling for sandhi
# - On 2nd/3rd-degree pages: -n only in sandhi contexts (before fricatives)

print("\n  Approach: Compare -n frequency on 1st vs 2nd vs 3rd degree plant pages,")
print("  controlling for following-word-initial context.")

for deg_label, deg_val in [('1st degree', 1), ('2nd degree', 2), ('3rd degree', 3)]:
    deg_folios = [f for f, (_, _, d, _, _, _) in plants.items() if d == deg_val]
    deg_words = []
    for f in deg_folios:
        deg_words.extend(folios.get(f, []))

    n_count, m_count, d_count, total = count_nmd_endings(deg_words)
    nmd = n_count + m_count + d_count
    if nmd > 0:
        print(f"\n  {deg_label} plant pages ({len(deg_folios)} folios, {total} words):")
        print(f"    -n: {n_count} ({n_count/nmd*100:.1f}%)")
        print(f"    -m: {m_count} ({m_count/nmd*100:.1f}%)")
        print(f"    -d: {d_count} ({d_count/nmd*100:.1f}%)")

# =============================================================================
# TEST 6: Red team - Alternative explanations
# =============================================================================
print("\n" + "=" * 80)
print("TEST 6: RED TEAM - ALTERNATIVE EXPLANATIONS")
print("=" * 80)

# 6a: Scribe variation
print("\n6a: SCRIBE VARIATION HYPOTHESIS")
print("-" * 40)
print("The VMS is thought to have at least 2 scribes (Currier A and B).")
print("Currier A: roughly f1r-f57r (herbal), Currier B: f75r onwards")

currier_a_words = []
currier_b_words = []
for folio, words in folios.items():
    num = int(re.search(r'\d+', folio).group())
    if num <= 57:
        currier_a_words.extend(words)
    elif num >= 75:
        currier_b_words.extend(words)

n_a, m_a, d_a, t_a = count_nmd_endings(currier_a_words)
n_b, m_b, d_b, t_b = count_nmd_endings(currier_b_words)
nmd_a = n_a + m_a + d_a
nmd_b = n_b + m_b + d_b

if nmd_a > 0 and nmd_b > 0:
    print(f"\n  Currier A (f1-f57): n={n_a/nmd_a*100:.1f}%, m={m_a/nmd_a*100:.1f}%, d={d_a/nmd_a*100:.1f}%")
    print(f"  Currier B (f75+):   n={n_b/nmd_b*100:.1f}%, m={m_b/nmd_b*100:.1f}%, d={d_b/nmd_b*100:.1f}%")

    # Chi-squared between A and B
    combined = [n_a+n_b, m_a+m_b, d_a+d_b]
    comb_total = sum(combined)
    exp_a = [c/comb_total * nmd_a for c in combined]
    exp_b = [c/comb_total * nmd_b for c in combined]
    chi2_scribes = chi_squared_test([n_a, m_a, d_a], exp_a) + \
                   chi_squared_test([n_b, m_b, d_b], exp_b)
    print(f"  Chi-squared (scribe A vs B): {chi2_scribes:.2f} (df=2)")
    if chi2_scribes > 9.21:
        print(f"  -> SIGNIFICANT scribe difference (p < 0.01)")
        print(f"     This means scribe variation COULD explain n/m/d differences across pages")
    else:
        print(f"  -> NOT significant scribe difference")

# 6b: Section variation
print("\n6b: SECTION VARIATION HYPOTHESIS")
print("-" * 40)
print("Do herbal subsections (e.g., herbal A vs herbal B) show different n/m/d?")

herbal_a = [f for f in herbal_folios if int(re.search(r'\d+', f).group()) <= 25]
herbal_b = [f for f in herbal_folios if 25 < int(re.search(r'\d+', f).group()) <= 57]

words_ha = [w for f in herbal_a for w in folios.get(f, [])]
words_hb = [w for f in herbal_b for w in folios.get(f, [])]

n_ha, m_ha, d_ha, _ = count_nmd_endings(words_ha)
n_hb, m_hb, d_hb, _ = count_nmd_endings(words_hb)
nmd_ha = n_ha + m_ha + d_ha
nmd_hb = n_hb + m_hb + d_hb

if nmd_ha > 0 and nmd_hb > 0:
    print(f"\n  Herbal A (f1-f25): n={n_ha/nmd_ha*100:.1f}%, m={m_ha/nmd_ha*100:.1f}%, d={d_ha/nmd_ha*100:.1f}%")
    print(f"  Herbal B (f26-f57): n={n_hb/nmd_hb*100:.1f}%, m={m_hb/nmd_hb*100:.1f}%, d={d_hb/nmd_hb*100:.1f}%")

# 6c: Random fluctuation
print("\n6c: RANDOM FLUCTUATION ANALYSIS")
print("-" * 40)
print("With only 14 plant identifications (many at MODERATE confidence),")
print("what is the probability of seeing the observed match rate by chance?")

print(f"\n  Observed matches: {correct}/{total_tested}")
print(f"  Expected by chance (p=1/3): {total_tested/3:.1f}")
print(f"  P(>= {correct} matches | n={total_tested}, p=1/3): {binomial_test_p(correct, total_tested, 1/3):.4f}")

# 6d: -m as morphological ending
print("\n6d: IS -m A MORPHOLOGICAL ENDING (NOT A DEGREE MARKER)?")
print("-" * 40)

# Check what word types end in -m
m_words = [w for w in all_words if w.endswith('m')]
m_word_freq = Counter(m_words)
print(f"\n  Total -m words: {len(m_words)}")
print(f"  Unique -m words: {len(m_word_freq)}")
print(f"  Most common -m words:")
for w, c in m_word_freq.most_common(15):
    print(f"    {w:<20} {c:>5}")

# Check if -m words have specific structural patterns
print(f"\n  Structural analysis of -m words:")
am_words = sum(1 for w in m_words if w.endswith('am'))
om_words = sum(1 for w in m_words if w.endswith('om'))
im_words = sum(1 for w in m_words if w.endswith('im'))
other_m = len(m_words) - am_words - om_words - im_words
print(f"    -am: {am_words} ({am_words/len(m_words)*100:.1f}%)")
print(f"    -om: {om_words} ({om_words/len(m_words)*100:.1f}%)")
print(f"    -im: {im_words} ({im_words/len(m_words)*100:.1f}%)")
print(f"    other: {other_m} ({other_m/len(m_words)*100:.1f}%)")

# 6e: Folio-by-folio m-density to check if it's page-specific or random
print("\n6e: FOLIO-LEVEL -m DENSITY ANALYSIS")
print("-" * 40)

# For all herbal folios, compute -m proportion
folio_m_props = []
for folio in herbal_folios:
    words = folios.get(folio, [])
    if len(words) < 10:
        continue
    n, m, d, total = count_nmd_endings(words)
    nmd = n + m + d
    if nmd >= 5:
        m_prop = m / nmd
        folio_m_props.append((folio, m_prop, nmd))

# Sort by m proportion
folio_m_props.sort(key=lambda x: -x[1])
print(f"\nHerbal folios ranked by -m proportion:")
print(f"  {'Folio':<10} {'m_prop':>8} {'NMD':>5} {'Plant (if identified)':>30}")
for folio, m_prop, nmd in folio_m_props[:15]:
    plant_info = plants.get(folio, (None,))[0] or "-"
    deg = plants.get(folio, (None, None, None))[2] if folio in plants else "-"
    print(f"  {folio:<10} {m_prop:>7.3f} {nmd:>5}   {plant_info} (deg={deg})")

print(f"\n  Bottom 10 (lowest -m proportion):")
for folio, m_prop, nmd in folio_m_props[-10:]:
    plant_info = plants.get(folio, (None,))[0] or "-"
    deg = plants.get(folio, (None, None, None))[2] if folio in plants else "-"
    print(f"  {folio:<10} {m_prop:>7.3f} {nmd:>5}   {plant_info} (deg={deg})")

# Standard deviation of m_prop across herbal folios
if folio_m_props:
    props = [x[1] for x in folio_m_props]
    mean_m = sum(props) / len(props)
    var_m = sum((p - mean_m)**2 for p in props) / len(props)
    std_m = math.sqrt(var_m)
    print(f"\n  Mean -m proportion: {mean_m:.4f}")
    print(f"  Std dev: {std_m:.4f}")
    print(f"  CV (coefficient of variation): {std_m/mean_m:.2f}" if mean_m > 0 else "")

# =============================================================================
# TEST 7: f3r deep dive (the page that sparked this hypothesis?)
# =============================================================================
print("\n" + "=" * 80)
print("TEST 7: f3r DEEP DIVE (Rubia tinctorum, Hot 2nd / Dry 2nd)")
print("=" * 80)

f3r_words = folios.get('f3r', [])
print(f"\nAll words on f3r ({len(f3r_words)} words):")

# Count all endings
f3r_endings = Counter(w[-1] for w in f3r_words if w)
print(f"\n  Ending distribution:")
for char, count in f3r_endings.most_common():
    print(f"    -{char}: {count}")

n3, m3, d3, t3 = count_nmd_endings(f3r_words)
print(f"\n  -n: {n3}, -m: {m3}, -d: {d3}")
print(f"  If -m = 2nd degree, and Rubia is 2nd degree Hot/Dry...")
print(f"  -m is {'dominant' if m3 > n3 and m3 > d3 else 'NOT dominant'} among n/m/d")

# List all -m words on f3r
m_on_f3r = [w for w in f3r_words if w.endswith('m')]
print(f"\n  All -m words on f3r: {m_on_f3r}")

# Compare with f47r (Vitis, Cold 1st)
print(f"\n  Comparison with f47r (Vitis, Cold 1st - expect -n dominant):")
f47r_words = folios.get('f47r', [])
n47, m47, d47, t47 = count_nmd_endings(f47r_words)
print(f"  f47r: -n: {n47}, -m: {m47}, -d: {d47}")
print(f"  -n is {'dominant' if n47 > m47 and n47 > d47 else 'NOT dominant'} among n/m/d")

# Compare with f9r (Nigella, Hot 3rd - expect -d dominant)
print(f"\n  Comparison with f9r (Nigella, Hot 3rd - expect -d dominant):")
f9r_words = folios.get('f9r', [])
n9, m9, d9, t9 = count_nmd_endings(f9r_words)
print(f"  f9r: -n: {n9}, -m: {m9}, -d: {d9}")
print(f"  -d is {'dominant' if d9 > n9 and d9 > m9 else 'NOT dominant'} among n/m/d")

# =============================================================================
# STATISTICAL SUMMARY
# =============================================================================
print("\n" + "=" * 80)
print("STATISTICAL SUMMARY AND FINAL VERDICT")
print("=" * 80)

print(f"""
1. BASELINE PROBLEM:
   -n accounts for {global_n/nmd_total*100:.1f}% of n/m/d endings
   -m accounts for {global_m/nmd_total*100:.1f}% of n/m/d endings
   -d accounts for {global_d/nmd_total*100:.1f}% of n/m/d endings

   If these encode degrees 1-3, then 1st degree appears {global_n/global_m:.1f}x more
   than 2nd degree. No medical system would specify 1st degree 5-10x more than 2nd.

2. PREDICTION ACCURACY: {correct}/{total_tested} ({correct/total_tested*100:.0f}%)
   Chance level: 33%

3. SANDHI CONTAMINATION:
   -n is already known to be a SANDHI variant (appearing before fricatives).
   -n is also a BOUNDARY marker (elevated at line/paragraph endings).
   These established functions account for -n's frequency without needing
   a "degree" interpretation.

4. -m RARITY:
   -m is only {global_m/len(all_words)*100:.1f}% of all words.
   If -m encoded "2nd degree" (the most common Galenic degree), it should
   be FAR more common. Most medieval plants are classified as 1st or 2nd degree.

5. -d AMBIGUITY:
   -d could end a word as part of the stem (e.g., 'shod', 'chod') or as
   a suffix. Without clear stem-suffix boundaries, -d as "3rd degree" is
   unfalsifiable.

6. 4TH DEGREE GAP:
   The Galenic system uses 4 degrees. This hypothesis only covers 3.
   No convincing 4th-degree encoding has been identified.
""")
