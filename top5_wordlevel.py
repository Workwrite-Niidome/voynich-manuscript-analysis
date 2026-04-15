#!/usr/bin/env python3
"""Word-level chi-squared analysis for top 5 morphemes."""

import re

def parse_eva(filepath):
    folios = {}
    current = None
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            m = re.match(r'<(f\d+[rv])>', line)
            if m:
                current = m.group(1)
                folios[current] = []
                continue
            m2 = re.match(r'<(f\d+[rv])\.\d+', line)
            if m2:
                current = m2.group(1)
                if current not in folios:
                    folios[current] = []
                text = re.sub(r'^<[^>]+>\s*', '', line)
                text = re.sub(r'\{[^}]*\}', '', text)
                text = re.sub(r'@\d+;?', '', text)
                text = re.sub(r'<[^>]*>', '', text)
                text = text.replace('<->', '.')
                text = re.sub(r"[,?!;']", '', text)
                raw = re.split(r'[.\s]+', text)
                words = [w.strip() for w in raw if w.strip() and re.match(r'^[a-z]+$', w.strip())]
                folios[current].extend(words)
    return folios

folios = parse_eva('RF1b-e.txt')
herbal = sorted([f for f in folios if int(re.match(r'f(\d+)', f).group(1)) <= 57])

# Feature sets
FRUIT_VISIBLE = {'f4r','f6r','f6v','f7v','f14v','f15r','f18r','f20v','f22v',
    'f25r','f25v','f27r','f29r','f29v','f33r','f33v','f34r','f35r',
    'f37r','f38r','f39r','f41r','f42r','f43r','f45r','f49r','f50r','f53r','f56r'}

DIVIDED_LEAVES = {'f2r','f9r','f9v','f16v','f19r','f23v','f17v','f19v',
    'f25r','f27r','f29r','f34r','f38r','f41v','f43r','f47r','f49r','f50r','f53r','f56r'}
UNDIVIDED_LEAVES = {'f1v','f2v','f5r','f7v','f8r','f8v','f11r','f13v','f18v','f20v',
    'f22r','f24r','f24v','f3v','f4v','f15v','f21r','f25v','f26r','f26v','f27v','f28r',
    'f28v','f30r','f31r','f32r','f35r','f36r','f37r','f39r','f40r','f42r','f44r','f45r',
    'f46r','f48r','f50v','f51r','f52r','f54r','f55r','f57r'}

TALL_PLANTS = {'f11v','f13r','f20r','f25r','f25v','f26r','f26v','f28r','f31r','f34r',
    'f35r','f36r','f38r','f40r','f42r','f44r','f46r','f50r','f50v','f54r','f55r','f56r'}
SHORT_PLANTS = {'f1v','f2r','f2v','f3r','f3v','f4r','f4v','f5r','f6r','f6v','f7r','f7v',
    'f8r','f8v','f9r','f9v','f10r','f11r','f13v','f14v','f15r','f15v','f16r','f16v',
    'f17r','f17v','f18r','f18v','f19r','f19v','f20v','f21r','f21v','f22r','f22v','f23r','f23v','f24r','f24v'}

LINEAR_LEAVES = {'f4r','f14v','f21r','f21v','f6r','f17v','f29r','f29v','f33r','f33v',
    'f37r','f39r','f41r','f45r','f49r','f53r'}
BROAD_LEAVES = {'f1v','f2v','f5r','f7v','f8r','f8v','f11r','f13v','f18v','f20v','f22r',
    'f24r','f24v','f2r','f3r','f3v','f4v','f9r','f9v','f10r','f15r','f15v','f16r','f19r',
    'f20r','f23r','f25r','f25v','f26r','f26v','f27r','f27v','f28r','f28v','f30r','f31r',
    'f32r','f34r','f35r','f36r','f38r','f40r','f42r','f44r','f46r','f47r','f48r','f50r',
    'f50v','f51r','f52r','f54r','f55r','f56r','f57r'}

FIBROUS_ROOTS = {'f9v','f17v','f18v','f19v','f20v','f21r','f21v','f22r','f25v','f27v',
    'f29r','f33r','f37r','f39r','f41r','f45r','f49r','f53r'}
NON_FIBROUS_ROOTS = {'f2r','f3r','f3v','f4v','f7r','f9r','f11r','f13v','f15v','f16v',
    'f18r','f19r','f23r','f24r','f1v','f4r','f5r','f6r','f6v','f7v','f8r','f8v','f10r',
    'f11v','f13r','f14v','f15r','f16r','f17r','f20r','f22v','f23v','f24v','f25r','f26r',
    'f26v','f27r','f28r','f28v','f29v','f30r','f31r','f32r','f33v','f34r','f35r','f36r',
    'f38r','f40r','f42r','f43r','f44r','f46r','f47r','f48r','f50r','f50v','f51r','f52r',
    'f54r','f55r','f56r','f57r'}

def word_level_chi2(pages, morpheme, feat_present, feat_absent, mode='exact'):
    m_in = 0; t_in = 0; m_out = 0; t_out = 0
    for fid in pages:
        words = folios.get(fid, [])
        if mode == 'exact':
            cnt = sum(1 for w in words if w == morpheme)
        else:
            cnt = sum(1 for w in words if morpheme in w)
        if fid in feat_present:
            m_in += cnt; t_in += len(words)
        elif fid in feat_absent:
            m_out += cnt; t_out += len(words)

    a = m_in; b = m_out; c = t_in - m_in; d = t_out - m_out
    N = a+b+c+d
    denom = (a+b)*(c+d)*(a+c)*(b+d)
    if denom == 0:
        chi2 = 0
    else:
        chi2 = N * (abs(a*d - b*c) - N/2)**2 / denom

    rate_in = m_in/t_in*1000 if t_in > 0 else 0
    rate_out = m_out/t_out*1000 if t_out > 0 else 0
    enrich = rate_in/rate_out if rate_out > 0 else float('inf')

    return {
        'a': a, 'b': b, 'c': c, 'd': d, 'N': N,
        'chi2': chi2, 'rate_in': rate_in, 'rate_out': rate_out,
        'enrichment': enrich, 't_in': t_in, 't_out': t_out
    }

print("WORD-LEVEL CHI-SQUARED (all 112 herbal pages)")
print("="*100)
tests = [
    ('cthy', 'exact', 'Fruit/seed', FRUIT_VISIBLE, set(herbal)-FRUIT_VISIBLE),
    ('cth', 'substring', 'Fruit/seed', FRUIT_VISIBLE, set(herbal)-FRUIT_VISIBLE),
    ('dan', 'exact', 'Divided leaves', DIVIDED_LEAVES, UNDIVIDED_LEAVES),
    ('dan', 'substring', 'Divided leaves', DIVIDED_LEAVES, UNDIVIDED_LEAVES),
    ('dchy', 'exact', 'Tall/tree-like', TALL_PLANTS, SHORT_PLANTS),
    ('ty', 'exact', 'Linear leaves', LINEAR_LEAVES, BROAD_LEAVES),
    ('cphol', 'exact', 'Fibrous roots', FIBROUS_ROOTS, NON_FIBROUS_ROOTS),
    ('cph', 'substring', 'Fibrous roots', FIBROUS_ROOTS, NON_FIBROUS_ROOTS),
]

for morph, mode, feat, present, absent in tests:
    r = word_level_chi2(herbal, morph, present, absent, mode)
    print(f"  {morph:>8} ({mode:>9}) vs {feat:<16} chi2={r['chi2']:>7.2f}  IN={r['rate_in']:>5.1f}/k OUT={r['rate_out']:>5.1f}/k enrich={r['enrichment']:>6.2f}x  (a={r['a']},b={r['b']},t_in={r['t_in']},t_out={r['t_out']})")

print()
print("WORD-LEVEL CHI-SQUARED (original ~30 pages f1-f24)")
print("="*100)
original_30 = [f for f in herbal if int(re.match(r'f(\d+)', f).group(1)) <= 24]
orig_fruit = {'f4r','f6r','f6v','f7v','f14v','f15r','f20v','f22v','f18r'}
orig_divided = {'f2r','f9r','f9v','f16v','f19r','f23v','f17v','f19v'}
orig_undivided = {'f1v','f2v','f5r','f7v','f8r','f8v','f11r','f13v','f18v','f20v',
    'f22r','f24r','f24v','f3v','f4v','f15v','f21r'}
orig_tall = {'f11v','f13r','f20r'}
orig_short = set(original_30) - orig_tall
orig_linear = {'f4r','f14v','f21r','f21v'}
orig_broad = set(original_30) - orig_linear
orig_fibrous = {'f9v','f17v','f18v','f19v','f20v'}
orig_nonfibrous = set(original_30) - orig_fibrous

tests_orig = [
    ('cthy', 'exact', 'Fruit/seed', orig_fruit, set(original_30)-orig_fruit),
    ('cth', 'substring', 'Fruit/seed', orig_fruit, set(original_30)-orig_fruit),
    ('dan', 'exact', 'Divided leaves', orig_divided, orig_undivided),
    ('dan', 'substring', 'Divided leaves', orig_divided, orig_undivided),
    ('dchy', 'exact', 'Tall/tree-like', orig_tall, orig_short),
    ('ty', 'exact', 'Linear leaves', orig_linear, orig_broad),
    ('cphol', 'exact', 'Fibrous roots', orig_fibrous, orig_nonfibrous),
]

for morph, mode, feat, present, absent in tests_orig:
    r = word_level_chi2(original_30, morph, present, absent, mode)
    print(f"  {morph:>8} ({mode:>9}) vs {feat:<16} chi2={r['chi2']:>7.2f}  IN={r['rate_in']:>5.1f}/k OUT={r['rate_out']:>5.1f}/k enrich={r['enrichment']:>6.2f}x  (a={r['a']},b={r['b']},t_in={r['t_in']},t_out={r['t_out']})")

# Additional: look at pages that have MANY cthy words to understand clustering
print()
print("TOP 20 PAGES BY CTHY RATE:")
page_rates = []
for fid in herbal:
    words = folios[fid]
    cnt = sum(1 for w in words if w == 'cthy')
    total = len(words)
    rate = cnt/total*1000 if total > 0 else 0
    fruit = 'FRUIT' if fid in FRUIT_VISIBLE else ''
    page_rates.append((fid, cnt, total, rate, fruit))
page_rates.sort(key=lambda x: -x[3])
for fid, cnt, total, rate, fruit in page_rates[:20]:
    print(f"  {fid}: {cnt}/{total} = {rate:.1f}/k  {fruit}")

print()
print("TOP 20 PAGES BY DAN (exact) RATE:")
page_rates2 = []
for fid in herbal:
    words = folios[fid]
    cnt = sum(1 for w in words if w == 'dan')
    total = len(words)
    rate = cnt/total*1000 if total > 0 else 0
    div = 'DIV' if fid in DIVIDED_LEAVES else ('UNDIV' if fid in UNDIVIDED_LEAVES else '')
    page_rates2.append((fid, cnt, total, rate, div))
page_rates2.sort(key=lambda x: -x[3])
for fid, cnt, total, rate, label in page_rates2[:20]:
    print(f"  {fid}: {cnt}/{total} = {rate:.1f}/k  {label}")

print()
print("TOP 20 PAGES BY TY (exact) RATE:")
page_rates3 = []
for fid in herbal:
    words = folios[fid]
    cnt = sum(1 for w in words if w == 'ty')
    total = len(words)
    rate = cnt/total*1000 if total > 0 else 0
    lin = 'LINEAR' if fid in LINEAR_LEAVES else ('BROAD' if fid in BROAD_LEAVES else '')
    page_rates3.append((fid, cnt, total, rate, lin))
page_rates3.sort(key=lambda x: -x[3])
for fid, cnt, total, rate, label in page_rates3[:20]:
    print(f"  {fid}: {cnt}/{total} = {rate:.1f}/k  {label}")
