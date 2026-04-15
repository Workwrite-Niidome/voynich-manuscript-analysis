"""
Visual classification of ALL herbal folios based on examination of illustrations.
Then correlation analysis with high-frequency words.
"""
import json
import numpy as np
from scipy import stats

# Visual features for each herbal folio
# Based on systematic examination of all herbal page images
# Features: leaves_prominent, roots_visible, flowers_visible, fruits_seeds,
#           tall_plant, leaves_divided, leaves_linear, leaves_round

# Format: folio -> (leaves_prom, roots, flowers, fruits, tall, divided, linear, round)
# 1=yes, 0=no

visual_data = {
    # Herbal A: f1v through f57r
    'f1v': (1, 1, 0, 0, 1, 0, 0, 1),  # oval leaves, roots, tall
    'f2r': (1, 1, 1, 0, 1, 1, 0, 0),  # divided leaves, flower clusters, roots
    'f2v': (1, 0, 0, 0, 0, 0, 0, 1),  # single large round leaf
    'f3r': (1, 1, 0, 0, 1, 0, 0, 0),  # striped leaves, roots
    'f3v': (1, 1, 1, 0, 1, 1, 0, 0),  # divided leaves, dotted flower, roots
    'f4r': (1, 1, 0, 0, 1, 0, 1, 0),  # narrow linear leaves, roots, tall
    'f4v': (1, 1, 1, 0, 1, 0, 1, 0),  # linear leaves, blue flower, bulb root
    'f5r': (1, 0, 0, 0, 0, 0, 0, 1),  # large round leaves, no roots
    'f5v': (1, 1, 1, 0, 1, 1, 0, 0),  # lobed/divided leaves, flowers, roots
    'f6r': (1, 1, 0, 1, 1, 1, 0, 0),  # deeply divided, fruit pods, roots
    'f6v': (1, 1, 0, 1, 1, 1, 0, 0),  # star divided, fruits/seeds, roots
    'f7r': (1, 1, 0, 0, 0, 0, 0, 0),  # star-shaped radiating leaves, root
    'f7v': (1, 1, 0, 1, 0, 0, 0, 1),  # oval rosette, red fruits, roots
    'f8r': (1, 1, 0, 0, 1, 0, 0, 1),  # single large arrow leaf, roots, tall
    'f8v': (1, 1, 1, 0, 1, 0, 0, 1),  # oval leaves, flowers, roots, tall
    'f9r': (1, 1, 1, 0, 1, 1, 0, 0),  # lobed oak-like, flower spike, roots
    'f9v': (1, 1, 1, 0, 1, 1, 0, 0),  # divided leaves, blue flowers, roots
    'f10r': (1, 1, 1, 1, 1, 0, 0, 1),  # broad serrated, sunflower, orange fruits
    'f10v': (1, 1, 1, 0, 1, 0, 0, 1),  # large broad leaves, hanging flowers, roots
    'f11r': (1, 1, 1, 0, 0, 0, 0, 0),  # dense small leaves, flowers, roots
    'f11v': (1, 1, 1, 0, 1, 0, 0, 0),  # scale-like leaves, flower, roots
    'f13r': (1, 1, 0, 0, 0, 1, 0, 1),  # round/lobed leaves, bulbous root
    'f13v': (1, 1, 1, 0, 1, 0, 0, 1),  # round leaves in pairs, flowers, roots
    'f14r': (1, 1, 1, 0, 1, 0, 1, 0),  # long narrow/linear, flower, root
    'f14v': (1, 1, 0, 1, 1, 1, 0, 0),  # divided leaves, fruits/seeds, roots
    'f15r': (1, 1, 1, 1, 1, 1, 0, 0),  # lobed leaves, flower, seeds, roots
    'f15v': (1, 1, 0, 0, 0, 0, 0, 1),  # simple round/clover leaves, roots
    'f16r': (1, 1, 1, 0, 1, 1, 1, 0),  # narrow divided, flower spike, roots
    'f16v': (1, 1, 1, 0, 0, 1, 0, 0),  # star flowers, divided leaves, root
    'f17r': (1, 1, 1, 0, 1, 0, 1, 0),  # fern-like linear, dark flowers, roots
    'f17v': (1, 1, 0, 1, 1, 0, 0, 1),  # oval leaves on vine, fruit clusters
    'f18r': (1, 1, 1, 0, 1, 0, 0, 1),  # broad oval, blue flowers, tall, roots
    'f18v': (1, 1, 1, 0, 1, 1, 0, 0),  # lobed leaves, round flower head, root
    'f19r': (1, 1, 1, 1, 1, 1, 0, 0),  # divided leaves, flower, seed pods, roots
    'f19v': (1, 1, 0, 0, 1, 0, 0, 0),  # tree-like, dense small leaves, roots
    'f20r': (1, 1, 0, 0, 0, 0, 0, 1),  # small round leaves, roots
    'f20v': (1, 1, 1, 0, 0, 0, 1, 0),  # linear leaves, blue flowers, roots
    'f21r': (1, 1, 0, 0, 0, 0, 1, 0),  # small narrow leaves, bushy, tiny roots
    'f21v': (1, 0, 1, 0, 1, 0, 0, 0),  # compound leaves, blue flowers, no roots
    'f22r': (1, 1, 0, 1, 1, 0, 0, 1),  # round leaves, seed spikes, roots
    'f22v': (1, 1, 1, 0, 1, 0, 0, 1),  # round/broad striped, flower, roots
    'f23r': (1, 1, 1, 0, 1, 1, 0, 0),  # divided/lobed, blue flowers, roots
    'f23v': (1, 1, 1, 0, 1, 0, 0, 1),  # round/broad leaves, flowers, roots
    'f24r': (1, 1, 1, 0, 1, 1, 0, 0),  # lobed leaves, flower top, roots
    'f24v': (1, 1, 1, 0, 1, 0, 0, 1),  # round broad, blue flowers, roots
    'f25r': (1, 1, 0, 0, 1, 0, 0, 1),  # broad oval leaves, small roots
    'f25v': (1, 1, 0, 0, 0, 1, 0, 0),  # large divided/lobed, roots
    'f26r': (1, 1, 0, 1, 1, 0, 0, 1),  # round small leaves, fruits, roots
    'f26v': (1, 1, 0, 1, 1, 0, 0, 1),  # scalloped tree-like, fruits, roots
    'f27r': (1, 1, 1, 0, 0, 0, 0, 1),  # broad leaves, flowers, roots
    'f27v': (1, 1, 1, 0, 1, 0, 0, 1),  # oval serrated, round flowers, roots
    'f28r': (1, 1, 0, 1, 0, 1, 0, 0),  # lobed leaf, fruit/seed pod, root
    'f28v': (1, 1, 0, 0, 0, 0, 1, 0),  # narrow/linear leaves, roots
    'f29r': (1, 1, 0, 1, 0, 0, 0, 1),  # broad leaves, berry cluster, roots
    'f29v': (1, 1, 0, 1, 1, 0, 1, 0),  # narrow linear, buds/fruits, roots
    'f30r': (1, 1, 0, 1, 1, 0, 0, 1),  # broad leaves, seed pods, roots
    'f30v': (1, 1, 0, 1, 1, 0, 0, 1),  # broad serrated, fruit clusters, roots
    'f31r': (1, 1, 1, 0, 1, 0, 0, 1),  # broad leaves, flower clusters, roots
    'f31v': (1, 1, 1, 0, 1, 1, 0, 0),  # lobed/compound, dense, flowers, roots
    'f32r': (1, 0, 1, 0, 1, 0, 0, 1),  # broad oval, small flowers, tall
    'f32v': (1, 1, 1, 0, 1, 1, 0, 0),  # star/lobed, large blue flowers, root
    'f33r': (1, 1, 1, 0, 1, 0, 0, 1),  # broad leaves, round flower heads, roots
    'f33v': (1, 1, 0, 1, 1, 1, 0, 0),  # divided/star leaves, seed pods, roots
    'f34r': (1, 1, 1, 0, 1, 1, 0, 0),  # divided/lobed, flower heads, roots
    'f34v': (1, 1, 0, 1, 1, 0, 0, 1),  # round fruits on branches, roots
    'f35r': (1, 1, 1, 0, 0, 0, 0, 1),  # large broad leaf/bract, flower, roots
    'f35v': (1, 1, 0, 1, 1, 1, 0, 0),  # lobed, blue fruits, large roots
    'f36r': (1, 1, 0, 1, 1, 1, 0, 0),  # deeply lobed oak-like, fruits, roots
    'f36v': (1, 1, 0, 1, 1, 1, 0, 0),  # deeply divided palmate, seeds, roots
    'f37r': (1, 1, 1, 0, 1, 0, 0, 1),  # broad oval, flower clusters, roots
    'f37v': (1, 1, 1, 0, 1, 0, 0, 1),  # broad oval on stem, flowers, roots
    'f38r': (1, 1, 0, 0, 0, 1, 0, 0),  # single large divided leaf, roots
    'f38v': (1, 1, 1, 0, 1, 0, 0, 0),  # scale/diamond leaves, tall, flower
    'f39r': (1, 1, 1, 0, 0, 0, 0, 1),  # broad leaves row, flower, lots roots
    'f39v': (1, 1, 1, 0, 1, 1, 0, 1),  # broad lobed, flower clusters, roots
    'f40r': (1, 1, 1, 0, 1, 1, 0, 0),  # deeply divided fern, elaborate flower, roots
    'f40v': (1, 1, 1, 0, 1, 1, 0, 0),  # deeply divided fern, large flower, roots
    'f41r': (1, 1, 0, 0, 1, 1, 0, 0),  # fan-shaped/lobed, tall, roots
    'f41v': (1, 1, 0, 0, 0, 1, 0, 0),  # deeply divided, large tuberous root
    'f42r': (1, 1, 1, 1, 0, 0, 0, 1),  # large broad leaf, red flowers/fruits
    'f42v': (1, 1, 0, 0, 0, 1, 0, 0),  # broad palmate/lobed, roots
    'f43r': (1, 1, 1, 0, 0, 0, 0, 0),  # row small plants, flowers, many roots
    'f43v': (1, 1, 0, 1, 1, 1, 0, 0),  # narrow/lobed, seed spikes, roots, snake
    'f44r': (1, 1, 1, 0, 0, 0, 0, 1),  # large broad fan, flower, large root
    'f44v': (1, 1, 1, 0, 0, 1, 0, 0),  # lobed/divided, flowers, thick root
    'f45r': (1, 1, 0, 1, 1, 1, 0, 0),  # lobed/divided, seed heads, thick root
    'f45v': (1, 1, 0, 1, 1, 0, 0, 1),  # oval/serrated, blue fruits, root
    'f46r': (1, 1, 1, 0, 1, 0, 0, 1),  # broad round, flower buds, many roots
    'f46v': (1, 1, 1, 0, 0, 1, 0, 1),  # broad serrated/divided, flower heads, roots
    'f47r': (1, 1, 0, 0, 0, 1, 0, 1),  # two large round/lobed leaves, root
    'f47v': (1, 1, 1, 0, 0, 0, 0, 1),  # broad leaves, blue flowers, roots
    'f48r': (1, 1, 1, 0, 0, 1, 0, 0),  # divided/star leaves, flower head, roots
    'f48v': (1, 1, 1, 0, 1, 1, 0, 0),  # divided/lobed, blue flowers, roots
    'f49r': (1, 0, 1, 0, 0, 0, 0, 1),  # large round leaves, flowers, creature
    'f49v': (1, 1, 1, 0, 0, 0, 0, 1),  # spiral/round leaves, flower, root
    'f50r': (1, 1, 1, 0, 0, 1, 0, 0),  # ornate/lobed, large flower, roots
    'f50v': (1, 1, 0, 0, 0, 1, 0, 1),  # broad lobed, fern top, roots
    'f51r': (1, 1, 1, 0, 0, 1, 0, 0),  # spiny/lobed, red flowers, tuberous root
    'f51v': (1, 1, 0, 1, 1, 0, 1, 0),  # twisting narrow, seed spike, roots
    'f52r': (1, 1, 1, 0, 1, 1, 0, 0),  # narrow divided, flower, ornamental root
    'f52v': (1, 1, 0, 0, 1, 1, 0, 0),  # spiny star leaves, tall, small roots
    'f53r': (1, 1, 1, 0, 1, 1, 0, 0),  # spiny/serrated, flower vine, roots
    'f53v': (1, 1, 1, 0, 0, 0, 1, 0),  # narrow/linear, red flower, root
    'f54r': (1, 1, 1, 1, 1, 0, 1, 0),  # small narrow serrated, flower/seeds, roots
    'f54v': (1, 1, 0, 1, 1, 0, 1, 0),  # narrow leaves, blue fruits, tuberous roots
    'f55r': (1, 1, 1, 0, 1, 1, 0, 0),  # lobed, flowers with red bracts, roots
    'f55v': (1, 1, 1, 0, 1, 0, 0, 1),  # large broad, flower cluster, roots
    'f56r': (1, 1, 0, 1, 0, 1, 0, 0),  # spiny/star with blue, spiral seed, roots
    'f56v': (1, 1, 0, 1, 0, 1, 0, 0),  # broad palmate/divided, seed head, roots
    'f57r': (1, 1, 1, 0, 1, 1, 0, 0),  # deeply divided, blue flowers, root

    # Herbal edge cases: f65r, f65v, f66v
    'f65r': (1, 1, 1, 0, 1, 1, 0, 0),  # divided/lobed, star flowers, roots
    'f65v': (1, 1, 1, 0, 1, 0, 0, 1),  # round seed heads, flower, tall, roots
    'f66v': (1, 1, 1, 0, 0, 0, 1, 0),  # curved/linear leaves, flowers, roots

    # Herbal B: f87r-f96v (pharmaceutical-herbal pages)
    'f87r': (1, 1, 1, 0, 1, 1, 0, 0),  # two plants, divided leaves, flowers, roots
    'f87v': (1, 1, 1, 0, 0, 1, 0, 1),  # lobed leaves, flower, roots
    'f90r1': (1, 1, 1, 0, 1, 0, 1, 0),  # narrow leaves, flower, roots
    'f90r2': (1, 1, 0, 0, 0, 0, 0, 1),  # round leaves, roots
    'f90v1': (1, 1, 0, 1, 0, 1, 0, 0),  # divided, fruits, roots
    'f90v2': (1, 1, 0, 0, 0, 0, 1, 0),  # narrow leaves, roots
    'f93r': (1, 1, 1, 0, 1, 1, 0, 0),  # divided, flowers, roots
    'f93v': (1, 1, 0, 1, 0, 0, 0, 1),  # round leaves, fruits, roots
    'f94r': (1, 1, 1, 0, 1, 0, 1, 0),  # narrow, flowers, roots
    'f94v': (1, 1, 0, 0, 0, 1, 0, 0),  # divided, roots
    'f95r1': (1, 1, 1, 0, 0, 0, 0, 1),  # round, flowers, roots
    'f95r2': (1, 1, 0, 1, 0, 1, 0, 0),  # divided, fruits, roots
    'f95v1': (1, 1, 1, 0, 1, 0, 0, 1),  # broad, flowers, tall, roots
    'f95v2': (1, 1, 0, 0, 0, 0, 1, 0),  # narrow, roots
    'f96r': (1, 1, 1, 0, 0, 1, 0, 0),  # divided, flowers, roots
    'f96v': (1, 1, 0, 1, 0, 0, 0, 1),  # round, fruits, roots
}

feature_names = [
    'leaves_prominent', 'roots_visible', 'flowers_visible', 'fruits_seeds',
    'tall_plant', 'leaves_divided', 'leaves_linear', 'leaves_round'
]

# Load word frequency data
with open(r'C:\Users\kazuk\Downloads\voynich_analysis\herbal_word_data.json', 'r') as f:
    word_data = json.load(f)

herbal_folios = word_data['herbal_folios']
per_folio_counts = word_data['per_folio_counts']
total_counts = word_data['total_counts']

# Use words with 50+ occurrences (since only 8 have 100+)
high_freq_words = sorted([w for w, c in total_counts.items() if c >= 50])
print(f"Words with 50+ occurrences: {len(high_freq_words)}")
print(f"Herbal folios in text: {len(herbal_folios)}")
print(f"Herbal folios with visual data: {len(visual_data)}")

# Find overlapping folios
common_folios = [f for f in herbal_folios if f in visual_data]
print(f"Common folios (text + visual): {len(common_folios)}")

# Build matrices
n_folios = len(common_folios)
n_features = len(feature_names)
n_words = len(high_freq_words)

# Visual feature matrix
visual_matrix = np.zeros((n_folios, n_features))
for i, folio in enumerate(common_folios):
    visual_matrix[i] = visual_data[folio]

# Word frequency matrix (per-page rate)
word_matrix = np.zeros((n_folios, n_words))
for i, folio in enumerate(common_folios):
    total_words = sum(per_folio_counts[folio].values())
    if total_words > 0:
        for j, word in enumerate(high_freq_words):
            word_matrix[i, j] = per_folio_counts[folio].get(word, 0) / total_words

# Feature statistics
print()
print("VISUAL FEATURE DISTRIBUTION:")
print("=" * 50)
for j, feat in enumerate(feature_names):
    count = int(visual_matrix[:, j].sum())
    print(f"  {feat:25s}: {count:3d}/{n_folios} folios ({100*count/n_folios:.0f}%)")

# Correlation analysis
print()
print("CORRELATION ANALYSIS: Word frequency vs Visual feature")
print("Only showing correlations with p < 0.01")
print("=" * 80)

results = []
for j, feat in enumerate(feature_names):
    feature_vec = visual_matrix[:, j]
    # Skip features with too little variance
    if feature_vec.std() < 0.05:
        continue
    for k, word in enumerate(high_freq_words):
        word_vec = word_matrix[:, k]
        if word_vec.std() < 1e-6:
            continue
        r, p = stats.pearsonr(word_vec, feature_vec)
        if p < 0.01:
            results.append((feat, word, r, p, total_counts.get(word, 0)))

# Sort by absolute correlation
results.sort(key=lambda x: abs(x[2]), reverse=True)

print(f"\nTotal significant correlations (p<0.01): {len(results)}")
print()
print(f"{'Feature':25s} {'Word':15s} {'r':>8s} {'p':>12s} {'Total_count':>12s}")
print("-" * 80)
for feat, word, r, p, count in results[:30]:
    print(f"  {feat:25s} {word:15s} {r:8.3f} {p:12.6f} {count:12d}")

print()
print("TOP 10 CORRELATIONS BY EFFECT SIZE:")
print("=" * 80)
for i, (feat, word, r, p, count) in enumerate(results[:10]):
    direction = "MORE on pages WITH" if r > 0 else "MORE on pages WITHOUT"
    print(f"  {i+1}. {word} x {feat}: r={r:.3f}, p={p:.6f}")
    print(f"     {word} ({count} total) appears {direction} {feat}")
    # Show mean frequency on feature-present vs feature-absent pages
    feat_idx = feature_names.index(feat)
    word_idx = high_freq_words.index(word)
    present = word_matrix[visual_matrix[:, feat_idx] == 1, word_idx]
    absent = word_matrix[visual_matrix[:, feat_idx] == 0, word_idx]
    if len(present) > 0 and len(absent) > 0:
        print(f"     Mean freq when {feat}=1: {present.mean():.4f} (n={len(present)})")
        print(f"     Mean freq when {feat}=0: {absent.mean():.4f} (n={len(absent)})")
    print()

# CH/SH analysis
print()
print("CH vs SH RATIO ANALYSIS:")
print("=" * 80)

# For each folio, calculate ch-word count and sh-word count
ch_per_folio = np.zeros(n_folios)
sh_per_folio = np.zeros(n_folios)
total_per_folio = np.zeros(n_folios)
for i, folio in enumerate(common_folios):
    folio_words = per_folio_counts[folio]
    total = sum(folio_words.values())
    total_per_folio[i] = total
    for w, c in folio_words.items():
        if 'ch' in w:
            ch_per_folio[i] += c
        if 'sh' in w:
            sh_per_folio[i] += c

# Normalize to rates
ch_rate = ch_per_folio / np.maximum(total_per_folio, 1)
sh_rate = sh_per_folio / np.maximum(total_per_folio, 1)

# Complexity = number of features present
complexity = visual_matrix.sum(axis=1)

print(f"Complexity (sum of visual features) range: {complexity.min():.0f} - {complexity.max():.0f}")
print(f"Mean complexity: {complexity.mean():.2f}")
print()

# Correlate ch-rate with complexity
r_ch_complex, p_ch_complex = stats.pearsonr(ch_rate, complexity)
print(f"ch-rate vs complexity: r={r_ch_complex:.4f}, p={p_ch_complex:.6f}")

# Correlate sh-rate with complexity
r_sh_complex, p_sh_complex = stats.pearsonr(sh_rate, complexity)
print(f"sh-rate vs complexity: r={r_sh_complex:.4f}, p={p_sh_complex:.6f}")

# Correlate ch/sh ratio with each feature
print()
print("ch-rate and sh-rate vs individual features:")
for j, feat in enumerate(feature_names):
    feature_vec = visual_matrix[:, j]
    if feature_vec.std() < 0.05:
        print(f"  {feat:25s}: skipped (too little variance)")
        continue
    r_ch, p_ch = stats.pearsonr(ch_rate, feature_vec)
    r_sh, p_sh = stats.pearsonr(sh_rate, feature_vec)
    sig_ch = "***" if p_ch < 0.001 else "**" if p_ch < 0.01 else "*" if p_ch < 0.05 else ""
    sig_sh = "***" if p_sh < 0.001 else "**" if p_sh < 0.01 else "*" if p_sh < 0.05 else ""
    print(f"  {feat:25s}: ch r={r_ch:+.3f} p={p_ch:.4f}{sig_ch:4s}  sh r={r_sh:+.3f} p={p_sh:.4f}{sig_sh:4s}")

# Text amount vs features
print()
print("TEXT AMOUNT (total words per page) vs features:")
for j, feat in enumerate(feature_names):
    feature_vec = visual_matrix[:, j]
    if feature_vec.std() < 0.05:
        continue
    r, p = stats.pearsonr(total_per_folio, feature_vec)
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""
    print(f"  {feat:25s}: r={r:+.3f} p={p:.4f}{sig}")

# Multiple testing correction (Bonferroni)
n_tests = n_features * n_words
bonferroni_threshold = 0.05 / n_tests
print()
print(f"MULTIPLE TESTING CORRECTION:")
print(f"  Total tests: {n_tests}")
print(f"  Bonferroni threshold: {bonferroni_threshold:.6f}")

bonf_results = [(f, w, r, p, c) for f, w, r, p, c in results if p < bonferroni_threshold]
print(f"  Significant after Bonferroni: {len(bonf_results)}")
for feat, word, r, p, count in bonf_results:
    print(f"    {word} x {feat}: r={r:.3f}, p={p:.8f}")

# FDR correction (Benjamini-Hochberg)
all_pvalues = []
all_results_full = []
for j, feat in enumerate(feature_names):
    feature_vec = visual_matrix[:, j]
    if feature_vec.std() < 0.05:
        continue
    for k, word in enumerate(high_freq_words):
        word_vec = word_matrix[:, k]
        if word_vec.std() < 1e-6:
            continue
        r, p = stats.pearsonr(word_vec, feature_vec)
        all_pvalues.append(p)
        all_results_full.append((feat, word, r, p, total_counts.get(word, 0)))

# BH FDR
sorted_pvals = sorted(enumerate(all_pvalues), key=lambda x: x[1])
n_total = len(sorted_pvals)
fdr_significant = []
for rank, (idx, pval) in enumerate(sorted_pvals, 1):
    bh_threshold = 0.05 * rank / n_total
    if pval <= bh_threshold:
        fdr_significant.append(all_results_full[idx])

print(f"\n  Significant after BH FDR (q<0.05): {len(fdr_significant)}")
fdr_significant.sort(key=lambda x: abs(x[2]), reverse=True)
for feat, word, r, p, count in fdr_significant[:20]:
    print(f"    {word} x {feat}: r={r:.3f}, p={p:.8f}")

# Save classification table
print()
print("FULL CLASSIFICATION TABLE:")
print("=" * 120)
header = f"{'Folio':10s}"
for feat in feature_names:
    header += f" {feat[:12]:>12s}"
print(header)
print("-" * 120)
for folio in common_folios:
    row = f"{folio:10s}"
    features = visual_data[folio]
    for val in features:
        row += f" {'Y':>12s}" if val else f" {'-':>12s}"
    print(row)
