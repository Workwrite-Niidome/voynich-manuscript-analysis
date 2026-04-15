import re
import math
from collections import defaultdict, Counter

def parse_eva(filepath):
    folios = {}
    current_folio = None
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            m = re.match(r'^<(f\d+[rv])>', line)
            if m:
                current_folio = m.group(1)
                if current_folio not in folios:
                    folios[current_folio] = []
            m2 = re.match(r'^<(f\d+[rv])\.\d+', line)
            if m2:
                current_folio = m2.group(1)
                if current_folio not in folios:
                    folios[current_folio] = []
                text_part = re.sub(r'^<[^>]+>\s*', '', line)
                text_part = re.sub(r'\{[^}]*\}', '', text_part)
                text_part = re.sub(r'@\d+;?', '', text_part)
                text_part = re.sub(r'[<>{}]', '', text_part)
                words = re.split(r'[.\s,;:!?\-]+', text_part)
                words = [w.strip() for w in words if w.strip() and len(w.strip()) > 1]
                folios[current_folio].extend(words)
    return folios

folios = parse_eva(r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt')

# Get herbal folios only
herbal = {k: v for k, v in folios.items()
          if int(re.search(r'(\d+)', k).group(1)) <= 57 and len(v) > 5}

all_herbal_folios = list(herbal.keys())

# ============================================================
# VISUAL CLASSIFICATION FROM ILLUSTRATIONS
# ============================================================

# LEAF SHAPE
ROUND_LEAVES = ['f2v', 'f5r', 'f13v', 'f16r', 'f24r', 'f24v', 'f23r', 'f11r']
LINEAR_LEAVES = ['f14v', 'f21r', 'f21v', 'f4r']
DIVIDED_LEAVES = ['f2r', 'f9r', 'f9v', 'f19r', 'f23v', 'f16v']
TOOTHED_LEAVES = ['f6r', 'f10r', 'f15r', 'f17v', 'f19v', 'f3v']
SMOOTH_OVAL = ['f1v', 'f8v', 'f18v', 'f20v', 'f7v', 'f18r', 'f22r']
HEART_SHAPED = ['f8r', 'f24v']

# FLOWERS
PROMINENT_FLOWERS = ['f4v', 'f7r', 'f9v', 'f11r', 'f17r', 'f22r', 'f15v', 'f21r', 'f23v', 'f10r']
NO_FLOWERS = ['f1v', 'f2v', 'f5r', 'f8r', 'f3r', 'f16r', 'f13v', 'f9r']
BLUE_FLOWERS = ['f4v', 'f9v', 'f11r', 'f17v', 'f19v', 'f22r', 'f23v', 'f10r', 'f18v']
RED_FLOWERS = ['f17r', 'f5v', 'f12r', 'f14v', 'f15v']

# FRUIT/SEED
WITH_FRUITS = ['f4r', 'f6r', 'f6v', 'f7v', 'f14v', 'f15r', 'f20v', 'f22v', 'f18r']
NO_FRUITS = ['f1v', 'f2v', 'f5r', 'f8r', 'f3r', 'f9v', 'f11r', 'f16r']

# ROOT TYPE
BULBOUS_ROOT = ['f4v', 'f13v', 'f23r', 'f24r', 'f16v', 'f19r', 'f9r']
FIBROUS_ROOT = ['f9v', 'f17v', 'f18v', 'f19v', 'f20v']
TAPROOT = ['f11r', 'f18r', 'f3r', 'f7r', 'f15v']

# SIZE/HABIT
TALL_TREE = ['f20r', 'f11v', 'f13r']
BUSHY = ['f9r', 'f19r', 'f21v', 'f11v', 'f23v']
SINGLE_STEM = ['f1v', 'f8r', 'f18v', 'f7r', 'f24v', 'f22r']


def chi_squared_2x2(a, b, c, d):
    n = a + b + c + d
    if n == 0:
        return 0, 1.0
    expected_a = (a + b) * (a + c) / n
    expected_b = (a + b) * (b + d) / n
    expected_c = (c + d) * (a + c) / n
    expected_d = (c + d) * (b + d) / n
    chi2 = 0
    for obs, exp in [(a, expected_a), (b, expected_b), (c, expected_c), (d, expected_d)]:
        if exp > 0:
            chi2 += (obs - exp) ** 2 / exp
    if chi2 <= 0:
        return 0, 1.0
    # p-value approximation for 1 df
    if chi2 >= 10.828:
        p = 0.001
    elif chi2 >= 6.635:
        p = 0.01
    elif chi2 >= 5.024:
        p = 0.025
    elif chi2 >= 3.841:
        p = 0.05
    elif chi2 >= 2.706:
        p = 0.10
    else:
        p = 0.50
    return chi2, p


def find_enriched_words(target_folios, other_folios, all_folios, min_count=3):
    target_words = Counter()
    target_total = 0
    for f in target_folios:
        if f in all_folios:
            for w in all_folios[f]:
                target_words[w] += 1
                target_total += 1

    other_words = Counter()
    other_total = 0
    for f in other_folios:
        if f in all_folios:
            for w in all_folios[f]:
                other_words[w] += 1
                other_total += 1

    all_words_set = set(target_words.keys()) | set(other_words.keys())
    results = []
    for word in all_words_set:
        tc = target_words.get(word, 0)
        oc = other_words.get(word, 0)
        if tc + oc < min_count:
            continue
        target_rate = (tc / target_total * 1000) if target_total > 0 else 0
        other_rate = (oc / other_total * 1000) if other_total > 0 else 0
        if other_rate == 0:
            ratio = float('inf') if target_rate > 0 else 1.0
        else:
            ratio = target_rate / other_rate
        a, b, c, d = tc, target_total - tc, oc, other_total - oc
        chi2, p = chi_squared_2x2(a, b, c, d)
        results.append({
            'word': word, 'tc': tc, 'oc': oc,
            'tr': target_rate, 'otr': other_rate,
            'ratio': ratio, 'chi2': chi2, 'p': p
        })
    results.sort(key=lambda x: x['chi2'], reverse=True)
    return results


def find_enriched_substrings(target_folios, other_folios, all_folios, substrings):
    results = []
    for ss in substrings:
        tc = tt = oc = ot = 0
        for f in target_folios:
            if f in all_folios:
                for w in all_folios[f]:
                    tt += 1
                    if ss in w:
                        tc += 1
        for f in other_folios:
            if f in all_folios:
                for w in all_folios[f]:
                    ot += 1
                    if ss in w:
                        oc += 1
        if tc + oc < 3:
            continue
        tr = (tc / tt * 1000) if tt > 0 else 0
        otr = (oc / ot * 1000) if ot > 0 else 0
        ratio = tr / otr if otr > 0 else (float('inf') if tr > 0 else 1.0)
        a, b, c, d = tc, tt - tc, oc, ot - oc
        chi2, p = chi_squared_2x2(a, b, c, d)
        results.append({
            'ss': ss, 'tc': tc, 'tt': tt, 'oc': oc, 'ot': ot,
            'tr': tr, 'otr': otr, 'ratio': ratio, 'chi2': chi2, 'p': p
        })
    results.sort(key=lambda x: x['chi2'], reverse=True)
    return results


# Candidate substrings to test
SUBSTRINGS = [
    'yd', 'ol', 'or', 'am', 'om', 'ey', 'dy', 'al', 'ar',
    'od', 'ok', 'ot', 'ch', 'sh', 'cth', 'ckh', 'qo', 'ko',
    'ee', 'eee', 'aiin', 'oiin', 'ain', 'chy', 'shy',
    'chol', 'shol', 'chor', 'cthy', 'ody', 'oly', 'ory',
    'oky', 'oky', 'dal', 'dol', 'kch', 'pch', 'tch',
    'eed', 'ees', 'eey', 'eel', 'eer',
    'sho', 'cho', 'oto', 'oka', 'che', 'she',
    'dar', 'kor', 'dor', 'sar', 'tar',
    'dan', 'kan', 'san',
    'ols', 'oly', 'oly',
    'oph', 'cph', 'cfh',
    'yt', 'yk', 'yp', 'yd', 'ysh', 'ych',
]
# Remove duplicates
SUBSTRINGS = list(dict.fromkeys(SUBSTRINGS))


def run_analysis(name, target, desc=""):
    other = [f for f in all_herbal_folios if f not in target]
    valid_target = [f for f in target if f in herbal]
    valid_other = [f for f in other if f in herbal]

    print(f"\n{'='*70}")
    print(f"  {name} ({len(valid_target)} valid pages: {', '.join(valid_target)})")
    print(f"  vs {len(valid_other)} other herbal pages")
    print(f"{'='*70}")

    # Word enrichment
    enriched = find_enriched_words(valid_target, valid_other, herbal, min_count=3)
    sig = [r for r in enriched if r['p'] <= 0.05 and r['ratio'] > 1.5]

    print(f"\n  ENRICHED WORDS (p<=0.05, ratio>1.5x):")
    if not sig:
        print(f"    (none found)")
    for r in sig[:12]:
        ratio_str = f"{r['ratio']:.2f}" if r['ratio'] < 100 else "INF"
        print(f"    {r['word']:20s}  in={r['tc']:3d} ({r['tr']:5.1f}/k)  "
              f"out={r['oc']:3d} ({r['otr']:5.1f}/k)  "
              f"ratio={ratio_str:>6s}  chi2={r['chi2']:6.2f}  p<{r['p']}")

    # Substring enrichment
    ss_results = find_enriched_substrings(valid_target, valid_other, herbal, SUBSTRINGS)
    sig_ss = [r for r in ss_results if r['p'] <= 0.05 and r['ratio'] > 1.2]

    print(f"\n  ENRICHED SUBSTRINGS (p<=0.05, ratio>1.2x):")
    if not sig_ss:
        print(f"    (none found)")
    for r in sig_ss[:10]:
        print(f"    *{r['ss']:8s}*  in={r['tc']:3d}/{r['tt']:4d} ({r['tr']:5.1f}/k)  "
              f"out={r['oc']:3d}/{r['ot']:5d} ({r['otr']:5.1f}/k)  "
              f"ratio={r['ratio']:5.2f}  chi2={r['chi2']:6.2f}")

    # Also show DEPLETED words
    depleted = [r for r in enriched if r['p'] <= 0.05 and r['ratio'] < 0.5 and r['oc'] >= 5]
    if depleted:
        print(f"\n  DEPLETED WORDS (p<=0.05, ratio<0.5x):")
        for r in depleted[:5]:
            print(f"    {r['word']:20s}  in={r['tc']:3d} ({r['tr']:5.1f}/k)  "
                  f"out={r['oc']:3d} ({r['otr']:5.1f}/k)  "
                  f"ratio={r['ratio']:.2f}  chi2={r['chi2']:6.2f}")

    return sig, sig_ss


# RUN ALL ANALYSES
print("VOYNICH MORPHEME ANALYSIS: PLANT PHYSICAL FEATURES")
print("=" * 70)

all_results = {}

# 1. LEAF SHAPE
print("\n\n### SECTION 1: LEAF SHAPE MORPHEMES ###")
for name, target in [
    ("ROUND/ORBICULAR LEAVES", ROUND_LEAVES),
    ("LINEAR/NEEDLE LEAVES", LINEAR_LEAVES),
    ("DIVIDED/LOBED LEAVES", DIVIDED_LEAVES),
    ("TOOTHED/SERRATED LEAVES", TOOTHED_LEAVES),
    ("SMOOTH OVAL LEAVES", SMOOTH_OVAL),
    ("HEART-SHAPED LEAVES", HEART_SHAPED),
]:
    w, s = run_analysis(name, target)
    all_results[name] = (w, s)

# 2. FLOWERS
print("\n\n### SECTION 2: FLOWER MORPHEMES ###")
for name, target in [
    ("PROMINENT FLOWERS (any color)", PROMINENT_FLOWERS),
    ("NO FLOWERS VISIBLE", NO_FLOWERS),
    ("BLUE FLOWERS", BLUE_FLOWERS),
    ("RED FLOWERS", RED_FLOWERS),
]:
    w, s = run_analysis(name, target)
    all_results[name] = (w, s)

# 3. FRUIT/SEED
print("\n\n### SECTION 3: FRUIT/SEED MORPHEMES ###")
for name, target in [
    ("FRUITS/SEEDS PRESENT", WITH_FRUITS),
    ("NO FRUITS/SEEDS", NO_FRUITS),
]:
    w, s = run_analysis(name, target)
    all_results[name] = (w, s)

# 4. ROOT TYPE
print("\n\n### SECTION 4: ROOT TYPE MORPHEMES ###")
for name, target in [
    ("BULBOUS ROOT", BULBOUS_ROOT),
    ("FIBROUS ROOT", FIBROUS_ROOT),
    ("TAPROOT", TAPROOT),
]:
    w, s = run_analysis(name, target)
    all_results[name] = (w, s)

# 5. SIZE/HABIT
print("\n\n### SECTION 5: SIZE/HABIT MORPHEMES ###")
for name, target in [
    ("TALL/TREE-LIKE", TALL_TREE),
    ("BUSHY HABIT", BUSHY),
    ("SINGLE STEM UPRIGHT", SINGLE_STEM),
]:
    w, s = run_analysis(name, target)
    all_results[name] = (w, s)


# ============================================================
# SUMMARY: Best morpheme candidates across all categories
# ============================================================
print("\n\n" + "=" * 70)
print("SUMMARY: ALL SIGNIFICANT MORPHEME-FEATURE ASSOCIATIONS")
print("=" * 70)

for cat_name, (word_results, ss_results) in all_results.items():
    if word_results or ss_results:
        print(f"\n  {cat_name}:")
        for r in word_results[:3]:
            ratio_str = f"{r['ratio']:.2f}" if r['ratio'] < 100 else "INF"
            print(f"    WORD: {r['word']:15s}  ratio={ratio_str}  chi2={r['chi2']:.1f}  p<{r['p']}")
        for r in ss_results[:3]:
            print(f"    SUB:  *{r['ss']}*  ratio={r['ratio']:.2f}  chi2={r['chi2']:.1f}")
