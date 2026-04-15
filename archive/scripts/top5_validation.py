#!/usr/bin/env python3
"""
Top 5 Morpheme Validation for Voynich Manuscript Herbal Section
Tests the 5 strongest morpheme-feature associations with full statistics.
"""

import re
import math
import json
from collections import defaultdict

###############################################################################
# 1. Parse EVA transcription
###############################################################################

def parse_eva(filepath):
    folios = {}
    current_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            m = re.match(r'<(f\d+[rv])>', line)
            if m:
                current_folio = m.group(1)
                folios[current_folio] = []
                continue

            m2 = re.match(r'<(f\d+[rv])\.\d+', line)
            if m2:
                current_folio = m2.group(1)
                if current_folio not in folios:
                    folios[current_folio] = []
                text_part = re.sub(r'^<[^>]+>\s*', '', line)
                text_part = re.sub(r'\{[^}]*\}', '', text_part)
                text_part = re.sub(r'@\d+;?', '', text_part)
                text_part = re.sub(r'<[^>]*>', '', text_part)
                # EVA uses periods as word separators and <-> for line breaks
                text_part = text_part.replace('<->', '.')
                text_part = re.sub(r"[,?!;']", '', text_part)
                # Split on periods AND whitespace
                raw_words = re.split(r'[.\s]+', text_part)
                words = [w.strip() for w in raw_words if w.strip()]
                words = [w for w in words if re.match(r'^[a-z]+$', w)]
                folios[current_folio].extend(words)

    return folios

def is_herbal(folio_id):
    m = re.match(r'f(\d+)([rv])', folio_id)
    if not m:
        return False
    num = int(m.group(1))
    return 1 <= num <= 57

###############################################################################
# 2. Visual feature classifications
###############################################################################

# MORPHEME 1: cthy = fruit/seed
# Pages where fruits, seeds, berries, or seed pods are CLEARLY VISIBLE in illustrations
FRUIT_VISIBLE = {
    'f4r',   # red berries throughout
    'f6r',   # spiky leaves with green seed pods
    'f6v',   # star-shaped leaves with blue seed balls
    'f7v',   # rosette leaves with orange buds/fruits
    'f14v',  # green leaves with white spotted fruits
    'f15r',  # seed-bearing structures visible
    'f18r',  # fruit/seed structures present
    'f20v',  # small rounded structures (fruits)
    'f22v',  # fruit-bearing plant
    'f25r',  # visible seed pods
    'f25v',  # fruit structures
    'f27r',  # berry-like structures
    'f29r',  # visible fruits/seeds
    'f29v',  # seed structures present
    'f33r',  # fruit visible
    'f33v',  # fruit/seed structures
    'f34r',  # berry/fruit structures
    'f35r',  # seed pods visible
    'f37r',  # visible fruit structures
    'f38r',  # fruit/seed present
    'f39r',  # seed structures
    'f41r',  # small seed structures at tips
    'f42r',  # visible fruit
    'f43r',  # fruit/berry structures
    'f45r',  # visible fruits
    'f49r',  # seed heads visible
    'f50r',  # fruit-bearing
    'f53r',  # visible seeds
    'f56r',  # fruit visible
}

# MORPHEME 2: -dan- = divided/segmented leaves
DIVIDED_LEAVES = {
    'f2r',   # deeply palmately lobed (peony)
    'f9r',   # bushy deeply lobed leaves
    'f9v',   # palmate divided leaves
    'f16v',  # narrow divided segments
    'f19r',  # palmate lobed leaves
    'f23v',  # palmate/geranium-like divided
    'f17v',  # fern-like pinnate (divided)
    'f19v',  # pinnate serrate (divided segments)
    'f25r',  # lobed/divided
    'f27r',  # divided leaf segments
    'f29r',  # compound/divided leaves
    'f34r',  # lobed leaves
    'f38r',  # divided/lobed
    'f41v',  # divided leaves
    'f43r',  # lobed/divided
    'f47r',  # palmately lobed (grape vine)
    'f49r',  # divided/dissected
    'f50r',  # divided leaves
    'f53r',  # divided/lobed
    'f56r',  # divided segments
}

UNDIVIDED_LEAVES = {
    'f1v',   # oval smooth leaves
    'f2v',   # single giant round leaf
    'f5r',   # giant round water-lily leaves
    'f7v',   # rosette smooth leaves
    'f8r',   # single large arrowhead leaf
    'f8v',   # medium oval leaves
    'f11r',  # wavy broad leaves
    'f13v',  # round lobed (but mostly entire)
    'f18v',  # oblong/elliptic smooth
    'f20v',  # small rounded smooth
    'f22r',  # broad smooth leaves
    'f24r',  # round waxy entire
    'f24v',  # cordate (heart-shaped, entire)
    'f3v',   # spiky but not divided
    'f4v',   # broad green leaves
    'f15v',  # broad simple leaves
    'f21r',  # grass-like (linear but not divided)
    'f25v',  # entire/simple leaves
    'f26r',  # broad simple
    'f26v',  # entire leaves
    'f27v',  # broad undivided
    'f28r',  # simple broad
    'f28v',  # entire leaves
    'f30r',  # simple leaves
    'f31r',  # broad undivided
    'f32r',  # entire leaves
    'f35r',  # simple smooth
    'f36r',  # broad simple
    'f37r',  # entire leaves
    'f39r',  # simple leaves
    'f40r',  # undivided broad
    'f42r',  # simple leaves
    'f44r',  # entire leaves
    'f45r',  # simple leaves
    'f46r',  # broad simple
    'f48r',  # entire leaves
    'f50v',  # simple broad
    'f51r',  # simple leaves
    'f52r',  # undivided
    'f54r',  # simple
    'f55r',  # entire
    'f57r',  # simple
}

# MORPHEME 3: dchy = tall/tree-like
TALL_PLANTS = {
    'f11v',  # tall tree-like plant
    'f13r',  # tall upright plant
    'f20r',  # tall/tree-like habitus
    'f25r',  # tall vertical stem
    'f25v',  # tall plant form
    'f26r',  # tall upright
    'f26v',  # tall stem dominant
    'f28r',  # tall vertical plant
    'f31r',  # tall upright form
    'f34r',  # tall tree-like
    'f35r',  # tall plant
    'f36r',  # tall upright
    'f38r',  # tall stem
    'f40r',  # tall vertical
    'f42r',  # tall plant form
    'f44r',  # tall upright
    'f46r',  # tall plant
    'f50r',  # tall tree-like
    'f50v',  # tall plant
    'f54r',  # tall upright
    'f55r',  # tall form
    'f56r',  # tall plant
}

SHORT_PLANTS = {
    'f1v',   # compact rosette
    'f2r',   # low spreading
    'f2v',   # single giant leaf, low
    'f3r',   # short bushy
    'f3v',   # low compact
    'f4r',   # small scattered
    'f4v',   # low with flowers
    'f5r',   # flat water-lily
    'f6r',   # low spiky
    'f6v',   # low spreading
    'f7r',   # compact star shape
    'f7v',   # low rosette
    'f8r',   # single leaf, compact
    'f8v',   # low spreading
    'f9r',   # bushy low
    'f9v',   # low spreading
    'f10r',  # compact
    'f11r',  # compact hanging
    'f13v',  # low round
    'f14v',  # low iris-like
    'f15r',  # short
    'f15v',  # compact
    'f16r',  # low trefoil
    'f16v',  # low divided
    'f17r',  # compact
    'f17v',  # low fern
    'f18r',  # short
    'f18v',  # compact
    'f19r',  # low bushy
    'f19v',  # compact
    'f20v',  # small rounded
    'f21r',  # grass, low
    'f21v',  # low fine
    'f22r',  # compact
    'f22v',  # short
    'f23r',  # low
    'f23v',  # compact
    'f24r',  # low round
    'f24v',  # compact cordate
}

# MORPHEME 4: ty = thin/linear
LINEAR_LEAVES = {
    'f4r',   # small scattered narrow leaves
    'f14v',  # iris-like narrow leaves
    'f21r',  # grass-like linear leaves
    'f21v',  # fine rosemary-like linear
    'f6r',   # narrow spiky leaves
    'f17v',  # fern-like narrow pinnae
    'f29r',  # narrow linear leaves
    'f29v',  # thin linear
    'f33r',  # narrow leaves
    'f33v',  # thin linear
    'f37r',  # narrow thin leaves
    'f39r',  # linear thin
    'f41r',  # fine narrow (maidenhair)
    'f45r',  # thin linear
    'f49r',  # narrow dissected
    'f53r',  # thin fine leaves
}

BROAD_LEAVES = {
    'f1v',   # broad oval
    'f2v',   # giant round broad
    'f5r',   # giant round broad
    'f7v',   # broad rosette
    'f8r',   # broad arrowhead
    'f8v',   # broad medium oval
    'f11r',  # broad wavy
    'f13v',  # round broad
    'f18v',  # broad oblong
    'f20v',  # broad rounded
    'f22r',  # broad compound
    'f24r',  # broad round
    'f24v',  # broad cordate
    'f2r',   # broad lobed
    'f3r',   # broad striped
    'f3v',   # broad spiky
    'f4v',   # broad green
    'f9r',   # broad lobed
    'f9v',   # broad palmate
    'f10r',  # broad leaves
    'f15r',  # broad toothed
    'f15v',  # broad simple
    'f16r',  # broad trefoil
    'f19r',  # broad palmate
    'f20r',  # broad large
    'f23r',  # broad round
    'f25r',  # broad lobed
    'f25v',  # broad simple
    'f26r',  # broad simple
    'f26v',  # broad entire
    'f27r',  # broad leaves
    'f27v',  # broad
    'f28r',  # broad simple
    'f28v',  # broad entire
    'f30r',  # broad simple
    'f31r',  # broad
    'f32r',  # broad entire
    'f34r',  # broad lobed
    'f35r',  # broad simple
    'f36r',  # broad
    'f38r',  # broad divided
    'f40r',  # broad
    'f42r',  # broad simple
    'f44r',  # broad entire
    'f46r',  # broad
    'f47r',  # broad palmate
    'f48r',  # broad
    'f50r',  # broad
    'f50v',  # broad
    'f51r',  # broad
    'f52r',  # broad
    'f54r',  # broad
    'f55r',  # broad
    'f56r',  # broad divided
    'f57r',  # broad
}

# MORPHEME 5: cphol = fibrous roots
FIBROUS_ROOTS = {
    'f9v',   # fibrous root system visible
    'f17v',  # fine fibrous roots
    'f18v',  # thread-like fibrous roots
    'f19v',  # fibrous root mass
    'f20v',  # fibrous roots
    'f21r',  # grass-like fibrous roots
    'f21v',  # fine fibrous
    'f22r',  # fibrous roots visible
    'f25v',  # fibrous root system
    'f27v',  # fibrous roots
    'f29r',  # fibrous thin roots
    'f33r',  # thread-like roots
    'f37r',  # fibrous roots
    'f39r',  # fibrous root system
    'f41r',  # delicate fibrous roots
    'f45r',  # fibrous thin
    'f49r',  # fibrous roots
    'f53r',  # fibrous
}

NON_FIBROUS_ROOTS = {
    'f2r',   # thick fleshy taproot
    'f3r',   # thick prominent root
    'f3v',   # thick root
    'f4v',   # bulbous root
    'f7r',   # thick orange root
    'f9r',   # large root mass (thick)
    'f11r',  # thick taproot
    'f13v',  # bulbous root
    'f15v',  # thick root
    'f16v',  # thick root
    'f18r',  # taproot
    'f19r',  # thick bulbous root
    'f23r',  # bulbous root
    'f24r',  # thick root
    'f1v',   # visible root, not fibrous
    'f4r',   # root visible, not fibrous
    'f5r',   # thick root
    'f6r',   # thick root
    'f6v',   # thick root
    'f7v',   # root visible
    'f8r',   # thick root
    'f8v',   # root visible
    'f10r',  # thick root
    'f11v',  # root visible
    'f13r',  # thick root
    'f14v',  # bulbous/thick root
    'f15r',  # root visible
    'f16r',  # thick root
    'f17r',  # root visible
    'f20r',  # thick root
    'f22v',  # thick root
    'f23v',  # root visible
    'f24v',  # root visible
    'f25r',  # thick root
    'f26r',  # root
    'f26v',  # root
    'f27r',  # root
    'f28r',  # root
    'f28v',  # root
    'f29v',  # root, not clearly fibrous
    'f30r',  # root
    'f31r',  # root
    'f32r',  # root
    'f33v',  # root, uncertain
    'f34r',  # root
    'f35r',  # root
    'f36r',  # root
    'f38r',  # root
    'f40r',  # root
    'f42r',  # root
    'f43r',  # root
    'f44r',  # root
    'f46r',  # root
    'f47r',  # root
    'f48r',  # root
    'f50r',  # root
    'f50v',  # root
    'f51r',  # root
    'f52r',  # root
    'f54r',  # root
    'f55r',  # root
    'f56r',  # root
    'f57r',  # root
}

###############################################################################
# 3. Statistical functions
###############################################################################

def chi2_yates(a, b, c, d):
    N = a + b + c + d
    if N == 0:
        return 0.0
    num = N * (abs(a*d - b*c) - N/2.0)**2
    denom = (a+b) * (c+d) * (a+c) * (b+d)
    if denom == 0:
        return 0.0
    return num / denom

def fisher_exact_p(a, b, c, d):
    """Fisher exact test p-value (two-tailed) using log-factorials."""
    N = a + b + c + d

    max_n = N + 1
    logfact = [0.0] * (max_n + 1)
    for i in range(1, max_n + 1):
        logfact[i] = logfact[i-1] + math.log(i)

    def hypergeom_log_pmf(x, M, n, N_draw):
        if x < max(0, N_draw - (M - n)) or x > min(n, N_draw):
            return float('-inf')
        return (logfact[n] - logfact[x] - logfact[n-x] +
                logfact[M-n] - logfact[N_draw-x] - logfact[M-n-N_draw+x] -
                logfact[M] + logfact[N_draw] + logfact[M-N_draw])

    M = N
    n_success = a + b
    N_draw = a + c

    log_p_obs = hypergeom_log_pmf(a, M, n_success, N_draw)

    total_p = 0.0
    for x in range(max(0, N_draw - (M - n_success)), min(n_success, N_draw) + 1):
        log_p_x = hypergeom_log_pmf(x, M, n_success, N_draw)
        if log_p_x <= log_p_obs + 1e-10:
            total_p += math.exp(log_p_x)

    return min(total_p, 1.0)

def odds_ratio(a, b, c, d):
    if b == 0 or c == 0:
        return ((a + 0.5) * (d + 0.5)) / ((b + 0.5) * (c + 0.5))
    return (a * d) / (b * c)

def sensitivity_fn(a, c):
    return a / (a + c) if (a + c) > 0 else 0.0

def specificity_fn(b, d):
    return d / (b + d) if (b + d) > 0 else 0.0

def ppv_fn(a, b):
    return a / (a + b) if (a + b) > 0 else 0.0

def npv_fn(c, d):
    return d / (c + d) if (c + d) > 0 else 0.0

###############################################################################
# 4. Main analysis
###############################################################################

def check_morpheme(words, morpheme, mode):
    count = 0
    for w in words:
        if mode == 'exact':
            if w == morpheme:
                count += 1
        else:  # substring
            if morpheme in w:
                count += 1
    total = len(words)
    rate = (count / total) * 1000 if total > 0 else 0.0
    return count > 0, count, rate

def analyze(folios, herbal_pages, morpheme, feature_present, feature_absent,
            morph_name, feat_name, mode='substring'):
    a = b = c = d = 0
    morph_in_w = 0
    morph_in_t = 0
    morph_out_w = 0
    morph_out_t = 0

    pages_morph_present_feat_present = []
    pages_morph_present_feat_absent = []
    pages_morph_absent_feat_present = []

    for fid in herbal_pages:
        words = folios.get(fid, [])
        if len(words) < 3:
            continue

        in_feat = fid in feature_present
        in_absent = fid in feature_absent

        if not in_feat and not in_absent:
            continue

        has_morph, cnt, rate = check_morpheme(words, morpheme, mode)

        if in_feat:
            morph_in_t += len(words)
            morph_in_w += cnt
            if has_morph:
                a += 1
                pages_morph_present_feat_present.append(fid)
            else:
                c += 1
                pages_morph_absent_feat_present.append(fid)
        elif in_absent:
            morph_out_t += len(words)
            morph_out_w += cnt
            if has_morph:
                b += 1
                pages_morph_present_feat_absent.append(fid)
            else:
                d += 1

    chi2 = chi2_yates(a, b, c, d)
    fp = fisher_exact_p(a, b, c, d)
    oratio = odds_ratio(a, b, c, d)
    sens = sensitivity_fn(a, c)
    spec = specificity_fn(b, d)
    pv = ppv_fn(a, b)
    nv = npv_fn(c, d)

    rate_in = (morph_in_w / morph_in_t * 1000) if morph_in_t > 0 else 0
    rate_out = (morph_out_w / morph_out_t * 1000) if morph_out_t > 0 else 0
    enrichment = rate_in / rate_out if rate_out > 0 else float('inf')

    return {
        'morph_name': morph_name,
        'feat_name': feat_name,
        'a': a, 'b': b, 'c': c, 'd': d,
        'N': a+b+c+d,
        'chi2': chi2,
        'fisher_p': fp,
        'odds_ratio': oratio,
        'sensitivity': sens,
        'specificity': spec,
        'ppv': pv,
        'npv': nv,
        'rate_in': rate_in,
        'rate_out': rate_out,
        'enrichment': enrichment,
        'morph_in_w': morph_in_w,
        'morph_in_t': morph_in_t,
        'morph_out_w': morph_out_w,
        'morph_out_t': morph_out_t,
        'pages_tp': pages_morph_present_feat_present,
        'pages_fp': pages_morph_present_feat_absent,
        'pages_fn': pages_morph_absent_feat_present,
    }

def main():
    filepath = r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt'
    folios = parse_eva(filepath)

    herbal_pages = sorted([f for f in folios if is_herbal(f)],
                          key=lambda x: (int(re.match(r'f(\d+)', x).group(1)), x[-1]))

    print(f"Total folios parsed: {len(folios)}")
    print(f"Herbal folios (f1-f57): {len(herbal_pages)}")
    total_hw = sum(len(folios[f]) for f in herbal_pages)
    print(f"Total herbal words: {total_hw}")

    # List herbal pages with word counts
    for hp in herbal_pages:
        wc = len(folios[hp])
        if wc < 3:
            print(f"  WARNING: {hp} has only {wc} words")
    print()

    tests = [
        # Morpheme 1: cthy
        ('cthy', 'exact', 'cthy (exact word)', 'Fruit/seed visible', FRUIT_VISIBLE, set(herbal_pages) - FRUIT_VISIBLE),
        ('cth', 'substring', 'cth- (substring)', 'Fruit/seed visible', FRUIT_VISIBLE, set(herbal_pages) - FRUIT_VISIBLE),
        # Morpheme 2: -dan-
        ('dan', 'substring', '-dan- (substring)', 'Divided leaves', DIVIDED_LEAVES, UNDIVIDED_LEAVES),
        ('dan', 'exact', 'dan (exact word)', 'Divided leaves', DIVIDED_LEAVES, UNDIVIDED_LEAVES),
        # Morpheme 3: dchy
        ('dchy', 'exact', 'dchy (exact word)', 'Tall/tree-like', TALL_PLANTS, SHORT_PLANTS),
        ('dchy', 'substring', 'dchy (substring)', 'Tall/tree-like', TALL_PLANTS, SHORT_PLANTS),
        # Morpheme 4: ty
        ('ty', 'exact', 'ty (exact word)', 'Thin/linear leaves', LINEAR_LEAVES, BROAD_LEAVES),
        # Morpheme 5: cphol
        ('cphol', 'exact', 'cphol (exact word)', 'Fibrous roots', FIBROUS_ROOTS, NON_FIBROUS_ROOTS),
        ('cphol', 'substring', 'cphol (substring)', 'Fibrous roots', FIBROUS_ROOTS, NON_FIBROUS_ROOTS),
        ('cph', 'substring', 'cph- (substring)', 'Fibrous roots', FIBROUS_ROOTS, NON_FIBROUS_ROOTS),
    ]

    all_results = []
    for morpheme, mode, mname, fname, present, absent in tests:
        r = analyze(folios, herbal_pages, morpheme, present, absent, mname, fname, mode)
        all_results.append(r)

        print(f"=== {mname} vs {fname} ===")
        print(f"  Feature+ pages: {r['a']+r['c']}, Feature- pages: {r['b']+r['d']}")
        print(f"  2x2: a={r['a']}, b={r['b']}, c={r['c']}, d={r['d']} (N={r['N']})")
        print(f"  Chi2(Yates): {r['chi2']:.4f}")
        print(f"  Fisher p:    {r['fisher_p']:.6e}")
        print(f"  Odds ratio:  {r['odds_ratio']:.2f}")
        print(f"  Sensitivity: {r['sensitivity']:.3f} ({r['a']}/{r['a']+r['c']})")
        print(f"  Specificity: {r['specificity']:.3f} ({r['d']}/{r['b']+r['d']})")
        print(f"  PPV:         {r['ppv']:.3f} ({r['a']}/{r['a']+r['b']})")
        print(f"  NPV:         {r['npv']:.3f} ({r['d']}/{r['c']+r['d']})")
        print(f"  Word rate: IN={r['rate_in']:.1f}/k, OUT={r['rate_out']:.1f}/k, enrichment={r['enrichment']:.2f}x")
        if r['pages_fn']:
            print(f"  FALSE NEGATIVES (feature present, morpheme absent): {r['pages_fn']}")
        if r['pages_fp']:
            fp_sample = r['pages_fp'][:10]
            print(f"  FALSE POSITIVES (morpheme present, feature absent): {fp_sample}{'...' if len(r['pages_fp'])>10 else ''}")
        print()

    # Output JSON for report generation
    output = []
    for r in all_results:
        output.append({
            'morph_name': r['morph_name'],
            'feat_name': r['feat_name'],
            'a': r['a'], 'b': r['b'], 'c': r['c'], 'd': r['d'],
            'N': r['N'],
            'chi2': round(r['chi2'], 4),
            'fisher_p': r['fisher_p'],
            'odds_ratio': round(r['odds_ratio'], 2),
            'sensitivity': round(r['sensitivity'], 3),
            'specificity': round(r['specificity'], 3),
            'ppv': round(r['ppv'], 3),
            'npv': round(r['npv'], 3),
            'rate_in': round(r['rate_in'], 1),
            'rate_out': round(r['rate_out'], 1),
            'enrichment': round(r['enrichment'], 2),
            'pages_fn': r['pages_fn'],
            'pages_fp': r['pages_fp'],
        })

    with open(r'C:\Users\kazuk\Downloads\voynich_analysis\top5_results.json', 'w') as f:
        json.dump(output, f, indent=2)

    print("Results saved to top5_results.json")

if __name__ == '__main__':
    main()
