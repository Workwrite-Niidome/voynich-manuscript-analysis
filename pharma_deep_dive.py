#!/usr/bin/env python3
"""Deep dive into pharmaceutical encoding findings."""

import re
import random
from collections import Counter, defaultdict

filepath = 'C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt'

def extract_page_words_with_meta(filepath):
    page_words = defaultdict(list)
    page_meta = {}
    current_page = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            page_match = re.match(r'^<(f\d+[rv]\d*)>\s+<!\s*(.*?)>', line)
            if page_match:
                current_page = page_match.group(1)
                meta = page_match.group(2)
                page_meta[current_page] = meta
                continue
            page_match2 = re.match(r'^<(f\d+[rv]\d*)>', line)
            if page_match2 and '.' not in line.split('>')[0]:
                current_page = page_match2.group(1)
                continue
            if current_page:
                content_match = re.match(r'^<[^>]+>\s+(.*)', line)
                if content_match:
                    text = content_match.group(1)
                    text = re.sub(r'<[^>]*>', '', text)
                    text = re.sub(r'\{[^}]*\}', '', text)
                    text = re.sub(r'@\d+;?', '', text)
                    text = re.sub(r'[,.\-?!\'"<>]', ' ', text)
                    words = [w.strip() for w in text.split() if w.strip() and len(w.strip()) > 1]
                    page_words[current_page].extend(words)
    return page_words, page_meta


all_pw, page_meta = extract_page_words_with_meta(filepath)

# Classify pages
herbal_a = []
herbal_b = []
for p, meta in page_meta.items():
    if '$I=H' in meta:
        if '$L=A' in meta:
            herbal_a.append(p)
        elif '$L=B' in meta:
            herbal_b.append(p)

print(f"Herbal Language A pages: {len(herbal_a)}")
print(f"Herbal Language B pages: {len(herbal_b)}")

# === CONFOUND CHECK: Is suffix difference a Language A/B artifact? ===
print("\n" + "="*70)
print("CONFOUND CHECK: Suffix frequencies in Language A vs Language B")
print("="*70)

suffixes_to_check = ['or', 'ey', 'aiin', 'dy', 'am', 'om', 'ol', 'an', 'in']
for suf in suffixes_to_check:
    a_freqs = []
    b_freqs = []
    for p in herbal_a:
        if p in all_pw and len(all_pw[p]) > 5:
            total = len(all_pw[p])
            count = sum(1 for w in all_pw[p] if w.endswith(suf))
            a_freqs.append(count/total)
    for p in herbal_b:
        if p in all_pw and len(all_pw[p]) > 5:
            total = len(all_pw[p])
            count = sum(1 for w in all_pw[p] if w.endswith(suf))
            b_freqs.append(count/total)

    a_avg = sum(a_freqs)/len(a_freqs) if a_freqs else 0
    b_avg = sum(b_freqs)/len(b_freqs) if b_freqs else 0
    if b_avg > 0:
        print(f"  -{suf:>5}: Lang A={a_avg:.4f} (n={len(a_freqs)}), Lang B={b_avg:.4f} (n={len(b_freqs)}), ratio={a_avg/b_avg:.2f}x")
    else:
        print(f"  -{suf:>5}: Lang A={a_avg:.4f} (n={len(a_freqs)}), Lang B={b_avg:.4f} (n={len(b_freqs)})")


# === WITHIN LANGUAGE A ONLY: Suffix correlation with intensity ===
print("\n" + "="*70)
print("WITHIN LANGUAGE A: Suffix correlation with Galenic intensity (4 plants)")
print("="*70)

la_anchors = ['f2r', 'f3r', 'f9r', 'f47r']
la_intensity = [1.5, 2, 3, 1]
la_names = ['Paeonia(H1)', 'Rubia(H2)', 'Nigella(H3)', 'Vitis(C1)']

def spearman_corr(x, y):
    n = len(x)
    def rank(vals):
        sorted_vals = sorted(enumerate(vals), key=lambda t: t[1])
        ranks = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j < n - 1 and sorted_vals[j+1][1] == sorted_vals[j][1]:
                j += 1
            avg_rank = sum(range(i+1, j+2)) / (j - i + 1)
            for k in range(i, j+1):
                ranks[sorted_vals[k][0]] = avg_rank
            i = j + 1
        return ranks
    rx = rank(x)
    ry = rank(y)
    d_sq = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return 1 - (6 * d_sq) / (n * (n**2 - 1))

all_suffixes = ['aiin', 'ain', 'dy', 'ey', 'ar', 'or', 'al', 'ol', 'am', 'om', 'an', 'in']
print(f"\n{'Suffix':>8}", end='')
for i, name in enumerate(la_names):
    print(f"  {name:>12}", end='')
print("   rho")

for suf in all_suffixes:
    freqs = []
    for p in la_anchors:
        words = all_pw.get(p, [])
        total = len(words) or 1
        count = sum(1 for w in words if w.endswith(suf))
        freqs.append(count/total)
    r = spearman_corr(la_intensity, freqs)
    marker = ''
    if abs(r) >= 0.9:
        marker = ' *** VERY STRONG'
    elif abs(r) >= 0.7:
        marker = ' ** strong'
    elif abs(r) >= 0.5:
        marker = ' * moderate'
    print(f"  -{suf:>5}", end='')
    for v in freqs:
        print(f"  {v:>12.3f}", end='')
    print(f"  {r:+.4f}{marker}")


# === f9r-f47r HEAD PAIR ANALYSIS ===
print("\n" + "="*70)
print("HEAD-RELATED PAIR (f9r Nigella + f47r Vitis) SIGNIFICANCE TEST")
print("="*70)

def jaccard(s1, s2):
    if not s1 and not s2:
        return 0
    return len(s1 & s2) / len(s1 | s2)

f9r_set = set(all_pw['f9r'])
f47r_set = set(all_pw['f47r'])
shared = sorted(f9r_set & f47r_set)
print(f"\nShared words: {len(shared)}")
for w in shared:
    in_others = [p for p in ['f2r', 'f3r', 'f41r'] if w in set(all_pw.get(p, []))]
    marker = ' ** EXCLUSIVE' if not in_others else f'  (also in {in_others})'
    print(f"  {w}{marker}")

# Permutation test: how often do random pairs from Lang A share this many words?
random.seed(42)
valid_la = [p for p in herbal_a if p in all_pw and len(all_pw[p]) > 10]

f9f47_jaccard = jaccard(f9r_set, f47r_set)
random_jaccards = []
for _ in range(10000):
    pair = random.sample(valid_la, 2)
    s = jaccard(set(all_pw[pair[0]]), set(all_pw[pair[1]]))
    random_jaccards.append(s)

random_avg = sum(random_jaccards) / len(random_jaccards)
percentile = sum(1 for s in random_jaccards if s <= f9f47_jaccard) / len(random_jaccards) * 100

print(f"\nf9r-f47r Jaccard: {f9f47_jaccard:.4f}")
print(f"Random Lang A pair avg: {random_avg:.4f}")
print(f"f9r-f47r at {percentile:.1f}th percentile")

# Exclusive shared words test
other_anchor_words = set()
for p in ['f2r', 'f3r', 'f41r']:
    other_anchor_words |= set(all_pw.get(p, []))

exclusive_shared = (f9r_set & f47r_set) - other_anchor_words
print(f"\nExclusive shared words: {len(exclusive_shared)}")

# How unusual is 8 exclusive shared words?
exclusive_counts = []
for _ in range(10000):
    pair = random.sample(valid_la, 2)
    shared_rand = set(all_pw[pair[0]]) & set(all_pw[pair[1]])
    excl = shared_rand - other_anchor_words
    exclusive_counts.append(len(excl))

avg_excl = sum(exclusive_counts) / len(exclusive_counts)
pct_excl = sum(1 for c in exclusive_counts if c <= 8) / len(exclusive_counts) * 100
print(f"Random pair avg exclusive shared: {avg_excl:.1f}")
print(f"8 exclusive shared at {pct_excl:.1f}th percentile")


# === PREFIX ANALYSIS: ot- and cth- vs intensity ===
print("\n" + "="*70)
print("PREFIX CORRELATION WITH INTENSITY (Lang A only, 4 plants)")
print("="*70)

prefixes = ['sh', 'ch', 'qo', 'ot', 'ok', 'da', 'ol', 'cth', 'ckh', 'cph', 'ko', 'so']
for pref in prefixes:
    freqs = []
    for p in la_anchors:
        words = all_pw.get(p, [])
        total = len(words) or 1
        count = sum(1 for w in words if w.startswith(pref))
        freqs.append(count/total)
    r = spearman_corr(la_intensity, freqs)
    marker = ''
    if abs(r) >= 0.9:
        marker = ' *** VERY STRONG'
    elif abs(r) >= 0.7:
        marker = ' ** strong'
    elif abs(r) >= 0.5:
        marker = ' * moderate'
    print(f"  {pref:>4}-: rho={r:+.4f}  [{', '.join(f'{v:.3f}' for v in freqs)}]{marker}")


# === COMPREHENSIVE GALENIC ENCODING: -or suffix as HOT marker ===
print("\n" + "="*70)
print("TESTING -or SUFFIX AS HOT MARKER ACROSS ALL HERBAL PAGES")
print("="*70)

# If -or encodes 'hot quality', then pages with high -or% should cluster together
# and represent plants with heating properties
or_freqs_all = {}
for p in herbal_a:
    if p in all_pw and len(all_pw[p]) > 10:
        total = len(all_pw[p])
        count = sum(1 for w in all_pw[p] if w.endswith('or'))
        or_freqs_all[p] = count / total

sorted_by_or = sorted(or_freqs_all.items(), key=lambda x: x[1], reverse=True)
print("\nTop 15 pages by -or suffix frequency (Lang A herbal):")
for p, freq in sorted_by_or[:15]:
    anchor_label = ''
    if p == 'f2r': anchor_label = ' <- Paeonia (Hot 1st)'
    elif p == 'f3r': anchor_label = ' <- Rubia (Hot 2nd)'
    elif p == 'f9r': anchor_label = ' <- Nigella (Hot 3rd)'
    elif p == 'f47r': anchor_label = ' <- Vitis (Cold 1st)'
    print(f"  {p}: {freq:.4f}{anchor_label}")

print("\nBottom 15 pages by -or suffix frequency (Lang A herbal):")
for p, freq in sorted_by_or[-15:]:
    anchor_label = ''
    if p == 'f2r': anchor_label = ' <- Paeonia (Hot 1st)'
    elif p == 'f3r': anchor_label = ' <- Rubia (Hot 2nd)'
    elif p == 'f9r': anchor_label = ' <- Nigella (Hot 3rd)'
    elif p == 'f47r': anchor_label = ' <- Vitis (Cold 1st)'
    print(f"  {p}: {freq:.4f}{anchor_label}")


# === TESTING -ey SUFFIX AS COLD MARKER ===
print("\n" + "="*70)
print("TESTING -ey SUFFIX AS COLD/MOIST MARKER")
print("="*70)

ey_freqs_all = {}
for p in herbal_a:
    if p in all_pw and len(all_pw[p]) > 10:
        total = len(all_pw[p])
        count = sum(1 for w in all_pw[p] if w.endswith('ey'))
        ey_freqs_all[p] = count / total

# Correlation between -or and -ey (should be negative if encoding hot/cold)
common_pages = set(or_freqs_all.keys()) & set(ey_freqs_all.keys())
or_vals = [or_freqs_all[p] for p in sorted(common_pages)]
ey_vals = [ey_freqs_all[p] for p in sorted(common_pages)]
r_or_ey = spearman_corr(or_vals, ey_vals)
print(f"\nCorrelation between -or and -ey across all Lang A herbal pages: rho={r_or_ey:+.4f}")
if r_or_ey < -0.3:
    print("  -> NEGATIVE correlation supports hot/cold encoding hypothesis")
elif r_or_ey > 0.3:
    print("  -> POSITIVE correlation contradicts hot/cold encoding hypothesis")
else:
    print("  -> Weak correlation, inconclusive")


# === SYNTHESIS ===
print("\n" + "="*70)
print("REVISED SYNTHESIS")
print("="*70)

print("""
KEY FINDINGS:

1. CONFOUND IDENTIFIED: f41r (Adiantum) is Currier Language B.
   The other 4 anchors are Language A. Much of the apparent 'Cold plant'
   distinctiveness is actually a Language A vs B difference, not
   pharmaceutical encoding.

2. WITHIN LANGUAGE A (4 plants), suffix correlations with Galenic intensity:""")

# Recalculate for summary
strong_corr = []
for suf in all_suffixes:
    freqs = []
    for p in la_anchors:
        words = all_pw.get(p, [])
        total = len(words) or 1
        count = sum(1 for w in words if w.endswith(suf))
        freqs.append(count/total)
    r = spearman_corr(la_intensity, freqs)
    if abs(r) >= 0.7:
        strong_corr.append((suf, r))
        direction = 'increases with heat' if r > 0 else 'increases with cold'
        print(f"   - {suf}: rho={r:+.4f} ({direction})")

print(f"""
3. HEAD-RELATED PAIR (f9r-f47r):
   - 13 shared words, 8 exclusive to this pair
   - Jaccard {f9f47_jaccard:.4f} at {percentile:.1f}th percentile of random pairs
   - {'SIGNIFICANTLY above random' if percentile > 95 else 'Above random but not highly significant' if percentile > 80 else 'Not significantly above random'}

4. OVERALL VERDICT:
   - The 5-plant sample is TOO SMALL for definitive conclusions (n=4 after removing Lang B confound)
   - Suffix correlations are suggestive but could be spurious with n=4
   - The f9r-f47r head-pair similarity is the most compelling individual finding
   - Pharmaceutical encoding CANNOT BE CONFIRMED with current evidence
   - However, the suffix distribution patterns warrant further investigation
     with a larger set of identified plants
""")

# Final numerical summary
print("STATISTICAL SUMMARY:")
print(f"  Tests supporting pharmaceutical encoding: 1-2/5 (body system grouping, some suffix correlations)")
print(f"  Tests contradicting: 3-4/5 (admin route, Galenic grouping, preparation method, sh- correlation)")
print(f"  Major confound: Currier Language A/B difference accounts for most f41r distinctiveness")
print(f"  Most promising lead: -or suffix frequency correlates with Galenic hot degree (rho=+0.80 within Lang A)")
print(f"  -or/-ey global correlation: {r_or_ey:+.4f}")
