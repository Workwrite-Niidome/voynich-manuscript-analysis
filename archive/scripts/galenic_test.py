#!/usr/bin/env python3
"""
Test the hypothesis that Voynich word structure encodes Galenic pharmaceutical properties.

Hypothesis: PREFIX + ROOT + SUFFIX where
  PREFIX -> Quality axis (ch=hot? sh=cold? d=dry? s=moist?)
  ROOT -> Substance identity
  SUFFIX -> Degree (1st-4th) or preparation method
"""

import re
from collections import Counter, defaultdict

# ============================================================
# 1. Parse the EVA transcription
# ============================================================

def parse_eva(filepath):
    """Parse EVA transcription into {folio: [list of words]}"""
    folios = {}
    current_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Match folio headers like <f1r> or inline folio refs
            folio_match = re.match(r'<(f\d+[rv]\d?)>', line)
            if folio_match:
                current_folio = folio_match.group(1)
                folios[current_folio] = []
                continue

            # Match text lines like <f1r.1,@P0>  text here
            line_match = re.match(r'<(f\d+[rv]\d?)\.(\d+),', line)
            if line_match:
                current_folio = line_match.group(1)
                if current_folio not in folios:
                    folios[current_folio] = []

                # Extract text after the >
                text_start = line.find('>')
                if text_start >= 0:
                    text = line[text_start+1:].strip()
                    # Remove annotations like @221; {cto} etc
                    text = re.sub(r'@\d+;?', '', text)
                    text = re.sub(r'\{[^}]*\}', '', text)
                    text = re.sub(r'[<>]', '', text)
                    # Split into words
                    words = re.split(r'[.\s,?!]+', text)
                    words = [w.strip() for w in words if w.strip() and len(w.strip()) > 0]
                    folios[current_folio].extend(words)

    return folios

# ============================================================
# 2. Classify words by prefix
# ============================================================

def classify_prefix(word):
    """Classify a word by its Galenic prefix hypothesis."""
    w = word.lower().strip()
    if not w:
        return None

    # Check prefixes in order of specificity
    if w.startswith('cth'):
        return 'cth'
    elif w.startswith('ckh'):
        return 'ckh'
    elif w.startswith('cph'):
        return 'cph'
    elif w.startswith('ch'):
        return 'ch'
    elif w.startswith('sh'):
        return 'sh'
    elif w.startswith('d'):
        return 'd'
    elif w.startswith('s') and not w.startswith('sh'):
        return 's'
    elif w.startswith('q'):
        return 'q'
    elif w.startswith('o'):
        return 'o'
    elif w.startswith('k'):
        return 'k'
    elif w.startswith('t'):
        return 't'
    elif w.startswith('p'):
        return 'p'
    elif w.startswith('y'):
        return 'y'
    else:
        return 'other'

def get_suffix(word):
    """Extract the final character as suffix."""
    w = word.lower().strip()
    if not w:
        return None
    return w[-1]

def get_suffix_group(word):
    """Get suffix, focusing on n/l/r/y hypothesis."""
    s = get_suffix(word)
    if s in ('n', 'l', 'r', 'y'):
        return s
    return 'other'

# ============================================================
# 3. Analysis functions
# ============================================================

def test1_ch_sh_correlation(folios):
    """Test 1: Are ch- and sh- words correlated or anti-correlated on same pages?"""
    results = []

    # Focus on herbal folios (f1r through f57v approximately)
    herbal_folios = {}
    for folio, words in folios.items():
        match = re.match(r'f(\d+)', folio)
        if match:
            num = int(match.group(1))
            if 1 <= num <= 57:  # Herbal section
                herbal_folios[folio] = words

    print("=" * 70)
    print("TEST 1: ch- vs sh- PREFIX CO-OCCURRENCE ON HERBAL FOLIOS")
    print("=" * 70)
    print()
    print("If ch=hot and sh=cold, they should co-occur (both qualities described")
    print("for the same plant in Galenic medicine).")
    print()

    ch_counts = []
    sh_counts = []
    d_counts = []
    s_counts = []
    folio_names = []

    print(f"{'Folio':<10} {'ch-':>6} {'sh-':>6} {'d-':>6} {'s-':>6} {'Total':>6} {'ch%':>6} {'sh%':>6}")
    print("-" * 60)

    for folio in sorted(herbal_folios.keys(), key=lambda x: (int(re.search(r'\d+', x).group()), x)):
        words = herbal_folios[folio]
        if len(words) < 5:  # skip very short folios
            continue

        prefixes = [classify_prefix(w) for w in words]
        ch = prefixes.count('ch')
        sh = prefixes.count('sh')
        d = prefixes.count('d')
        s = prefixes.count('s')
        total = len(words)

        ch_counts.append(ch)
        sh_counts.append(sh)
        d_counts.append(d)
        s_counts.append(s)
        folio_names.append(folio)

        ch_pct = (ch / total * 100) if total > 0 else 0
        sh_pct = (sh / total * 100) if total > 0 else 0

        print(f"{folio:<10} {ch:>6} {sh:>6} {d:>6} {s:>6} {total:>6} {ch_pct:>5.1f}% {sh_pct:>5.1f}%")

    # Calculate correlation
    if len(ch_counts) > 2:
        n = len(ch_counts)
        mean_ch = sum(ch_counts) / n
        mean_sh = sum(sh_counts) / n

        cov = sum((ch_counts[i] - mean_ch) * (sh_counts[i] - mean_sh) for i in range(n)) / n
        std_ch = (sum((x - mean_ch)**2 for x in ch_counts) / n) ** 0.5
        std_sh = (sum((x - mean_sh)**2 for x in sh_counts) / n) ** 0.5

        if std_ch > 0 and std_sh > 0:
            corr = cov / (std_ch * std_sh)
        else:
            corr = 0

        print(f"\nPearson correlation (ch- vs sh-): r = {corr:.3f}")
        if corr > 0.5:
            print("-> STRONG POSITIVE correlation: ch- and sh- co-occur -> SUPPORTS Galenic hypothesis")
        elif corr > 0.2:
            print("-> MODERATE POSITIVE correlation: some co-occurrence")
        elif corr > -0.2:
            print("-> WEAK/NO correlation: independent distribution")
        elif corr > -0.5:
            print("-> MODERATE NEGATIVE correlation: somewhat exclusive")
        else:
            print("-> STRONG NEGATIVE correlation: ch- and sh- are exclusive -> AGAINST Galenic hypothesis")

        # Also correlate d- and s-
        mean_d = sum(d_counts) / n
        mean_s = sum(s_counts) / n
        cov_ds = sum((d_counts[i] - mean_d) * (s_counts[i] - mean_s) for i in range(n)) / n
        std_d = (sum((x - mean_d)**2 for x in d_counts) / n) ** 0.5
        std_s = (sum((x - mean_s)**2 for x in s_counts) / n) ** 0.5
        if std_d > 0 and std_s > 0:
            corr_ds = cov_ds / (std_d * std_s)
        else:
            corr_ds = 0
        print(f"Pearson correlation (d- vs s-): r = {corr_ds:.3f}")

        # Cross: ch vs d
        cov_cd = sum((ch_counts[i] - mean_ch) * (d_counts[i] - mean_d) for i in range(n)) / n
        if std_ch > 0 and std_d > 0:
            corr_cd = cov_cd / (std_ch * std_d)
        else:
            corr_cd = 0
        print(f"Pearson correlation (ch- vs d-): r = {corr_cd:.3f}")

    return ch_counts, sh_counts, folio_names

def test2_suffix_distribution(folios):
    """Test 2: Do suffixes show a 4-way distribution consistent with degrees?"""
    print("\n" + "=" * 70)
    print("TEST 2: SUFFIX DISTRIBUTION (4-DEGREE TEST)")
    print("=" * 70)
    print()
    print("If suffixes encode Galenic degrees, we expect exactly 4 common variants.")
    print("Candidate: n=1st, l=2nd, r=3rd, y=4th degree")
    print()

    all_words = []
    for words in folios.values():
        all_words.extend(words)

    suffix_counts = Counter()
    for w in all_words:
        s = get_suffix(w)
        if s:
            suffix_counts[s] += 1

    total = sum(suffix_counts.values())
    print("Overall suffix distribution:")
    print(f"{'Suffix':<10} {'Count':>8} {'%':>8}")
    print("-" * 30)
    for suffix, count in suffix_counts.most_common(20):
        print(f"{suffix:<10} {count:>8} {count/total*100:>7.1f}%")

    # Focus on n, l, r, y
    nlry = {s: suffix_counts.get(s, 0) for s in ['n', 'l', 'r', 'y']}
    nlry_total = sum(nlry.values())
    print(f"\nn/l/r/y combined: {nlry_total} ({nlry_total/total*100:.1f}% of all words)")
    print("Distribution within n/l/r/y:")
    for s in ['n', 'l', 'r', 'y']:
        c = nlry[s]
        print(f"  {s}: {c} ({c/nlry_total*100:.1f}%)")

    # Test if distribution is uniform (expected for degrees) or skewed
    expected = nlry_total / 4
    chi2 = sum((nlry[s] - expected)**2 / expected for s in ['n', 'l', 'r', 'y'])
    print(f"\nChi-squared (uniformity test, df=3): {chi2:.1f}")
    print("  Critical values: 7.81 (p=0.05), 11.34 (p=0.01)")
    if chi2 > 11.34:
        print("  -> HIGHLY NON-UNIFORM: Suffixes are NOT evenly distributed")
        print("     This WEAKENS the degree hypothesis (degrees should be ~equal)")
    elif chi2 > 7.81:
        print("  -> SIGNIFICANTLY NON-UNIFORM at p<0.05")
    else:
        print("  -> CONSISTENT WITH UNIFORM distribution -> SUPPORTS degree hypothesis")

    # Now test: for each prefix (ch-, sh-), what's the suffix distribution?
    print("\n--- Suffix distribution by prefix ---")
    for prefix in ['ch', 'sh', 'd', 's', 'cth', 'o', 'k', 'q']:
        prefix_words = [w for w in all_words if classify_prefix(w) == prefix]
        if len(prefix_words) < 10:
            continue
        suffix_by_prefix = Counter(get_suffix(w) for w in prefix_words)
        total_p = sum(suffix_by_prefix.values())
        top5 = suffix_by_prefix.most_common(5)
        top5_str = ', '.join(f"{s}:{c}" for s, c in top5)
        print(f"  {prefix}-: n={total_p:>5}  top suffixes: {top5_str}")

    return suffix_counts

def test3_galenic_properties(folios):
    """Test 3: Cross-reference with known Galenic properties of identified plants."""
    print("\n" + "=" * 70)
    print("TEST 3: GALENIC PROPERTIES CROSS-REFERENCE")
    print("=" * 70)
    print()
    print("Known plant identifications with Galenic properties:")
    print()

    # Plant identifications with their Galenic properties and folios
    plants = {
        'f2r': {
            'name': 'Paeonia officinalis (peony)',
            'confidence': 'HIGH (55%)',
            'hot_cold': 'Hot',
            'degree_hc': 1,
            'dry_moist': 'Dry',
            'degree_dm': 2,
            'source': 'Dioscorides/Galen',
            'prediction': 'More ch- words (hot plant)'
        },
        'f3r': {
            'name': 'Rubia tinctorum (madder)',
            'confidence': 'HIGH (60%)',
            'hot_cold': 'Hot',
            'degree_hc': 2,
            'dry_moist': 'Dry',
            'degree_dm': 2,
            'source': 'Galen',
            'prediction': 'More ch- words (hot plant)'
        },
        'f9r': {
            'name': 'Nigella damascena',
            'confidence': 'HIGH (65%)',
            'hot_cold': 'Hot',
            'degree_hc': 3,
            'dry_moist': 'Dry',
            'degree_dm': 1,
            'source': 'Avicenna/Dioscorides',
            'prediction': 'More ch- words (hot plant), high degree'
        },
        'f41r': {
            'name': 'Adiantum capillus-veneris (maidenhair fern)',
            'confidence': 'HIGH (60%)',
            'hot_cold': 'Cold',
            'degree_hc': 2,
            'dry_moist': 'Dry',
            'degree_dm': 1,
            'source': 'Galen',
            'prediction': 'More sh- words (cold plant)'
        },
        'f47r': {
            'name': 'Vitis vinifera (grape vine)',
            'confidence': 'HIGH (70%)',
            'hot_cold': 'Cold',
            'degree_hc': 1,
            'dry_moist': 'Moist',
            'degree_dm': 2,
            'source': 'Galen/Dioscorides',
            'prediction': 'More sh- words (cold plant)'
        },
        'f1r': {
            'name': 'Laurus nobilis (bay laurel)',
            'confidence': 'MODERATE (45%)',
            'hot_cold': 'Hot',
            'degree_hc': 2,
            'dry_moist': 'Dry',
            'degree_dm': 1,
            'source': 'Galen',
            'prediction': 'More ch- words (hot plant)'
        },
        'f4r': {
            'name': 'Rosmarinus officinalis (rosemary)',
            'confidence': 'HIGH (55%)',
            'hot_cold': 'Hot',
            'degree_hc': 2,
            'dry_moist': 'Dry',
            'degree_dm': 2,
            'source': 'Galen',
            'prediction': 'More ch- words (hot plant)'
        },
    }

    results = []

    print(f"{'Folio':<8} {'Plant':<35} {'Quality':<12} {'ch-':>5} {'sh-':>5} {'d-':>5} {'s-':>5} {'ch>sh?':>8} {'Predict':>8}")
    print("-" * 100)

    for folio_base, info in plants.items():
        # Collect words from both recto and verso of the folio
        all_words = []
        for folio_key, words in folios.items():
            if folio_key.startswith(folio_base.replace('r', '').replace('v', '')):
                # Match e.g. f2r, f2v for base f2r
                pass
            if folio_key == folio_base:
                all_words.extend(words)

        if not all_words:
            print(f"{folio_base:<8} {info['name']:<35} NO DATA FOUND")
            continue

        prefixes = [classify_prefix(w) for w in all_words]
        ch = prefixes.count('ch')
        sh = prefixes.count('sh')
        d = prefixes.count('d')
        s = prefixes.count('s')
        total = len(all_words)

        quality = f"{info['hot_cold']}{info['degree_hc']}/{info['dry_moist']}{info['degree_dm']}"

        if info['hot_cold'] == 'Hot':
            correct = ch > sh
        else:
            correct = sh > ch

        result_str = "YES" if correct else "NO"

        results.append({
            'folio': folio_base,
            'plant': info['name'],
            'quality': quality,
            'ch': ch,
            'sh': sh,
            'correct': correct,
            'total': total
        })

        print(f"{folio_base:<8} {info['name'][:34]:<35} {quality:<12} {ch:>5} {sh:>5} {d:>5} {s:>5} {'ch>sh' if ch>sh else 'sh>=ch':>8} {result_str:>8}")

    # Summary
    correct_count = sum(1 for r in results if r['correct'])
    total_count = len(results)
    print(f"\nPrediction accuracy: {correct_count}/{total_count} ({correct_count/total_count*100:.0f}%)")
    print(f"Baseline (random): 50%")

    if correct_count / total_count > 0.7:
        print("-> ABOVE CHANCE: Prefix-quality mapping shows promise")
    elif correct_count / total_count > 0.55:
        print("-> MARGINALLY above chance: Weak support")
    else:
        print("-> AT OR BELOW CHANCE: No support for prefix-quality mapping")

    # Additional: check suffix distribution by degree
    print("\n--- Suffix distribution for plants with known degrees ---")
    for folio_base, info in plants.items():
        all_words = folios.get(folio_base, [])
        if not all_words:
            continue

        # Get ch- and sh- words separately
        for prefix_type in ['ch', 'sh']:
            prefix_words = [w for w in all_words if classify_prefix(w) == prefix_type]
            if len(prefix_words) < 3:
                continue
            suffixes = Counter(get_suffix(w) for w in prefix_words)
            top3 = suffixes.most_common(3)
            top_str = ', '.join(f"{s}:{c}" for s, c in top3)

            expected_degree = info['degree_hc'] if prefix_type == 'ch' else info['degree_hc']
            degree_map = {1: 'n', 2: 'l', 3: 'r', 4: 'y'}
            expected_suffix = degree_map.get(expected_degree, '?')

            print(f"  {folio_base} {info['name'][:25]:<25} {prefix_type}-words: n={len(prefix_words):>3}  "
                  f"suffixes: {top_str}  (expected: -{expected_suffix} for degree {expected_degree})")

    return results

def test4_recipe_section(folios):
    """Test 4: Recipe section (f103-f116) suffix patterns."""
    print("\n" + "=" * 70)
    print("TEST 4: RECIPE SECTION SUFFIX PATTERNS")
    print("=" * 70)
    print()
    print("In pharmaceutical recipes, ingredients are specified with degrees.")
    print("If suffixes encode degrees, recipe sections should show distinct patterns.")
    print()

    # Separate herbal vs recipe sections
    herbal_words = []
    recipe_words = []
    astro_words = []

    for folio, words in folios.items():
        match = re.match(r'f(\d+)', folio)
        if not match:
            continue
        num = int(match.group(1))

        if 1 <= num <= 57:
            herbal_words.extend(words)
        elif 67 <= num <= 73:
            astro_words.extend(words)
        elif 99 <= num <= 116:
            recipe_words.extend(words)

    sections = {
        'Herbal (f1-f57)': herbal_words,
        'Recipe (f99-f116)': recipe_words,
        'Astro (f67-f73)': astro_words,
    }

    for section_name, words in sections.items():
        if not words:
            print(f"{section_name}: NO DATA")
            continue

        total = len(words)
        suffix_dist = Counter(get_suffix(w) for w in words)
        nlry = {s: suffix_dist.get(s, 0) for s in ['n', 'l', 'r', 'y']}
        nlry_total = sum(nlry.values())

        print(f"\n{section_name} ({total} words):")
        print(f"  n/l/r/y total: {nlry_total} ({nlry_total/total*100:.1f}%)")
        for s in ['n', 'l', 'r', 'y']:
            c = nlry[s]
            pct = c / nlry_total * 100 if nlry_total > 0 else 0
            bar = '#' * int(pct / 2)
            print(f"    {s}: {c:>5} ({pct:>5.1f}%) {bar}")

        # Prefix distribution
        prefix_dist = Counter(classify_prefix(w) for w in words)
        print(f"  Prefix distribution:")
        for p in ['ch', 'sh', 'd', 's', 'o', 'q', 'k', 'cth']:
            c = prefix_dist.get(p, 0)
            print(f"    {p}-: {c:>5} ({c/total*100:>5.1f}%)")

    # Compare suffix ratios between sections
    print("\n--- Section comparison ---")
    print("If recipes specify degrees more explicitly, suffix patterns should differ.")
    for s in ['n', 'l', 'r', 'y']:
        h_pct = Counter(get_suffix(w) for w in herbal_words).get(s, 0) / len(herbal_words) * 100 if herbal_words else 0
        r_pct = Counter(get_suffix(w) for w in recipe_words).get(s, 0) / len(recipe_words) * 100 if recipe_words else 0
        print(f"  Suffix -{s}: Herbal={h_pct:.1f}%, Recipe={r_pct:.1f}%")

def test5_integration(folios):
    """Test 5: Integrative analysis - does word = quality + substance + degree?"""
    print("\n" + "=" * 70)
    print("TEST 5: INTEGRATIVE ANALYSIS — WORD = QUALITY + SUBSTANCE + DEGREE?")
    print("=" * 70)
    print()

    # If each word encodes quality+substance+degree, then:
    # 1. The same ROOT should appear with different prefixes and suffixes
    # 2. A "paradigm" should exist: chXn, chXl, chXr, chXy, shXn, shXl, etc.

    all_words = []
    for words in folios.values():
        all_words.extend(words)

    # Extract roots (strip prefix and suffix)
    def extract_root(word):
        w = word.lower().strip()
        # Strip prefix
        for pfx in ['cth', 'ckh', 'cph', 'cfh', 'ch', 'sh', 'qo', 'ok', 'ot']:
            if w.startswith(pfx):
                w = w[len(pfx):]
                break
        # Strip single-char suffix
        if len(w) > 1 and w[-1] in 'nlry':
            w = w[:-1]
        return w if len(w) > 0 else None

    # Find roots that appear with multiple prefixes
    root_prefixes = defaultdict(set)
    root_suffixes = defaultdict(set)
    root_words = defaultdict(list)

    for w in all_words:
        root = extract_root(w)
        if root and len(root) >= 2:
            pfx = classify_prefix(w)
            sfx = get_suffix(w)
            root_prefixes[root].add(pfx)
            root_suffixes[root].add(sfx)
            root_words[root].append(w)

    # Find paradigmatic roots
    print("Roots appearing with BOTH ch- and sh- prefixes (potential Galenic paradigms):")
    print(f"{'Root':<15} {'Prefixes':<30} {'Suffixes':<20} {'Example words'}")
    print("-" * 90)

    paradigm_count = 0
    for root in sorted(root_prefixes.keys(), key=lambda r: len(root_words[r]), reverse=True):
        prefixes = root_prefixes[root]
        if 'ch' in prefixes and 'sh' in prefixes:
            suffixes = root_suffixes[root]
            examples = list(set(root_words[root]))[:6]
            print(f"{root:<15} {str(prefixes):<30} {str(suffixes):<20} {', '.join(examples[:6])}")
            paradigm_count += 1
            if paradigm_count >= 20:
                break

    print(f"\nTotal roots with both ch- and sh-: {paradigm_count}")

    # Check how many of these also have all 4 suffix variants
    full_paradigms = 0
    for root in root_prefixes:
        if 'ch' in root_prefixes[root] and 'sh' in root_prefixes[root]:
            nlry_suffixes = root_suffixes[root] & {'n', 'l', 'r', 'y'}
            if len(nlry_suffixes) >= 3:
                full_paradigms += 1

    print(f"Roots with ch-/sh- AND 3+ of n/l/r/y suffixes: {full_paradigms}")
    if full_paradigms > 10:
        print("-> MANY full paradigms exist -> SUPPORTS combinatorial encoding")
    elif full_paradigms > 3:
        print("-> SOME paradigms exist -> Partial support")
    else:
        print("-> FEW paradigms -> WEAK support for combinatorial encoding")

# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    filepath = r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt'

    print("GALENIC PHARMACEUTICAL ENCODING HYPOTHESIS TEST")
    print("Voynich Manuscript -- EVA Transcription Analysis")
    print("=" * 70)
    print()

    folios = parse_eva(filepath)
    print(f"Parsed {len(folios)} folios, {sum(len(w) for w in folios.values())} total words")
    print()

    # Show folio overview
    herbal_count = sum(1 for f in folios if re.match(r'f[1-5]\d?[rv]', f))
    print(f"Herbal section folios: ~{herbal_count}")

    ch_sh_data = test1_ch_sh_correlation(folios)
    suffix_data = test2_suffix_distribution(folios)
    galenic_results = test3_galenic_properties(folios)
    test4_recipe_section(folios)
    test5_integration(folios)

    # Final verdict
    print("\n" + "=" * 70)
    print("FINAL ASSESSMENT")
    print("=" * 70)
