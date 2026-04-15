# Pharmaceutical Encoding Hypothesis Test

**Hypothesis**: The herbal page text encodes PHARMACEUTICAL PROPERTIES (what plants DO medicinally), not VISUAL FEATURES (what plants LOOK LIKE).

**Method**: Using 5 anchor plants with known identifications and Dioscorides/Galen pharmaceutical properties, test whether pages with similar medical uses share more vocabulary than pages with different uses.

## Anchor Plant Properties

| Page | Plant | Galenic Quality | Treats | Preparation | Admin Route |
|------|-------|----------------|--------|-------------|-------------|
| f2r | Paeonia | Hot 1st, Dry 2nd | Epilepsy, nightmares, menstruation | Root in wine | Internal liquid |
| f3r | Rubia | Hot 2nd, Dry 2nd | Jaundice, urinary, dyeing | Root decoction | Internal/External |
| f9r | Nigella | Hot 3rd, Dry 1st | Nasal congestion, headache, digestion | Seeds chewed/inhaled | Seeds/inhalation |
| f41r | Adiantum | Cold, Dry | Coughs, kidney stones, hair loss | Decoction drunk | Internal liquid |
| f47r | Vitis | Cold 1st, Moist 2nd | Headache, inflammation, diarrhea | Leaves/juice applied | External |

**CRITICAL CONFOUND DISCOVERED**: f41r (Adiantum) is Currier Language B ($L=B); the other 4 anchors are Language A ($L=A). Language A and B have dramatically different suffix distributions (e.g., -dy is 3x more frequent in B, -or is 2.5x more frequent in A). This means f41r's distinctiveness may be purely linguistic, not pharmaceutical.

## Test Results

### TEST 1: Administration Route Grouping
**Prediction**: Pages with same administration route share more vocabulary.

| Comparison | Jaccard | Cosine |
|-----------|---------|--------|
| Internal liquid within-group (f2r, f41r, f47r) | 0.0410 | 0.749 |
| Between internal-liquid and others | 0.0488 | 0.825 |

**Result: CONTRADICTS** (within-group similarity LOWER than between-group)

### TEST 2: Galenic Quality Grouping (Hot vs Cold)
**Prediction**: Hot plants (f2r, f3r, f9r) share vocabulary distinct from Cold plants (f41r, f47r).

| Comparison | Jaccard |
|-----------|---------|
| Hot within-group | 0.0460 |
| Cold within-group | 0.0246 |
| Hot-Cold between | 0.0503 |
| Within - Between | -0.0150 |

Permutation test: p = 0.902 (NOT significant)

**Result: CONTRADICTS** -- but this test is confounded by Language A/B.

### TEST 3: Body System Grouping
**Prediction**: Pages treating same body system share vocabulary.

| Body System Pair | Jaccard |
|-----------------|---------|
| Head-related (f9r, f47r) | **0.1226** |
| Kidney/urinary (f3r, f41r) | 0.0196 |
| Average matching pairs | 0.0711 |
| Average non-matching pairs | 0.0513 |

**Result: PARTIALLY SUPPORTS** -- driven entirely by the f9r-f47r pair.

### The f9r-f47r Anomaly (KEY FINDING)

The pair f9r (Nigella = headache) and f47r (Vitis = headache) shows **strikingly** high similarity:

- Jaccard 0.1226 -- at the **99.1th percentile** of random Language A herbal page pairs (avg = 0.0615)
- **13 shared words**, of which **8 are exclusive** to this pair (99.8th percentile; random avg = 2.1)

Exclusive shared words (not found in any other anchor page):
| Word | Notes |
|------|-------|
| chaiin | ch- root + -aiin suffix |
| chdy | ch- root + -dy suffix |
| choy | ch- root + -oy |
| cphy | cph- root |
| cthaiin | cth- root + -aiin |
| cthey | cth- root + -ey |
| shy | sh- prefix alone |
| tchol | t+ch- root + -ol |

**Statistical significance**: p < 0.01 for both Jaccard and exclusive word count. This is the strongest result in the entire analysis.

### TEST 4: Preparation Method Grouping
**Prediction**: Decoction plants share preparation vocabulary.

| Comparison | Jaccard |
|-----------|---------|
| Decoction within-group (f2r, f41r, f3r) | 0.0302 |
| Decoction vs others | 0.0419 |

Only 1 word shared by ALL decoction plants: "daiin" (ubiquitous function word).

**Result: CONTRADICTS**

### TEST 5: sh- Morpheme vs Galenic Intensity
**Prediction**: sh- frequency correlates with dosage intensity (Hot 3rd > Hot 2nd > Hot 1st > Cold).

| Page | Plant | sh- freq | Intensity |
|------|-------|----------|-----------|
| f2r | Paeonia (H1) | 0.117 | 1.5 |
| f3r | Rubia (H2) | 0.067 | 2 |
| f9r | Nigella (H3) | 0.072 | 3 |
| f41r | Adiantum (C) | 0.085 | 1 |
| f47r | Vitis (C1) | 0.104 | 1 |

Spearman rho = -0.50

**Result: CONTRADICTS** (negative correlation -- more sh- in MILDER plants)

## Secondary Findings: Suffix Correlations with Galenic Intensity

After removing the Language B confound (f41r), testing within Language A only (n=4):

| Suffix | Paeonia(H1) | Rubia(H2) | Nigella(H3) | Vitis(C1) | Spearman rho | Interpretation |
|--------|-------------|-----------|-------------|-----------|-------------|----------------|
| -ar | 0.013 | 0.029 | 0.029 | 0.013 | **+0.95** | Increases with heat |
| -al | 0.026 | 0.029 | 0.029 | 0.026 | **+0.95** | Increases with heat |
| -or | 0.117 | 0.192 | 0.130 | 0.078 | **+0.80** | Increases with heat |
| -ey | 0.104 | 0.067 | 0.043 | 0.104 | **-0.85** | Increases with cold |
| -ain | 0.039 | 0.000 | 0.029 | 0.052 | **-0.80** | Increases with cold |
| -ol | 0.143 | 0.183 | 0.101 | 0.208 | **-0.80** | Increases with cold |

**IMPORTANT CAVEAT**: With n=4, even random data can produce rho values this high. The probability of obtaining |rho| >= 0.80 by chance with n=4 is approximately 17% per suffix. With 12 suffixes tested, we expect ~2 false positives by chance alone. We found 6 strong correlations, which is above expectation but not overwhelmingly so.

**Cross-validation across all herbal pages**: The -or and -ey suffixes show a **global negative correlation of rho = -0.36** across all 95 Language A herbal pages. This is modest but consistent with the hypothesis that they encode opposite Galenic qualities.

## Prefix Correlations (Language A, n=4)

| Prefix | rho | Direction |
|--------|-----|-----------|
| cth- | **+0.95** | Increases with heat |
| qo- | **+0.80** | Increases with heat |
| ot- | +0.75 | Increases with heat |
| ok- | +0.80 | Increases with heat |
| da- | **-0.80** | Increases with cold |

## K-Means Clustering of All Herbal Pages

At k=3, the 128 herbal pages cluster into:

| Cluster | Size | Anchor Plants | Top Morphemes |
|---------|------|---------------|---------------|
| 0 | 28 | Vitis | High ch-, root:ch, root:sh |
| 1 | 43 | Adiantum | High ok-, suffix:dy, suffix:ey |
| 2 | 57 | Paeonia, Rubia, Nigella | High root:or, suffix:ol |

**Note**: Cluster 1 maps almost perfectly to Currier Language B pages, and Cluster 2 to Language A. The clustering is driven primarily by the Language A/B distinction, not pharmaceutical categories. Cluster 0 appears to be a sub-dialect or transition group.

At k=5, more structure emerges but anchor plants still group by language type rather than pharmaceutical category.

## Category-Specific Vocabulary

| Category | Shared Words | Exclusive Words | Examples |
|----------|-------------|----------------|----------|
| Hot (f2r,f3r,f9r) | 3 | 1 | cthy |
| Cold (f41r,f47r) | 3 | 0 | -- |
| Internal liquid | 2 | 1 | chey |
| **Head-related (f9r,f47r)** | **13** | **8** | chaiin, chdy, cphy, cthaiin, cthey, shy, tchol, choy |
| Kidney/urinary (f3r,f41r) | 3 | 1 | qokeey |

The head-related category stands out dramatically with 8 exclusive shared words.

## Overall Verdict

### Score: 1/5 primary tests support pharmaceutical encoding

| Test | Result | Significance |
|------|--------|-------------|
| Administration route | CONTRADICTS | -- |
| Galenic quality | CONTRADICTS | p=0.90 |
| Body system | PARTIALLY SUPPORTS | Driven by one pair |
| Preparation method | CONTRADICTS | -- |
| sh- dosage intensity | CONTRADICTS | rho=-0.50 |

### Assessment

**The pharmaceutical encoding hypothesis is NOT confirmed by this analysis.**

However, three findings prevent outright rejection:

1. **The f9r-f47r head-pair**: Two plants that both treat headache share vocabulary at the 99th percentile of random pairs, with 8 exclusive shared words (99.8th percentile). This is statistically significant (p < 0.01) and cannot be explained by language type (both are Language A) or physical proximity in the manuscript (f9r is quire B, f47r is quire F).

2. **Suffix polarity**: -or and -ey show a global anti-correlation (rho = -0.36) across all Language A herbal pages, consistent with encoding opposing Galenic qualities (hot vs cold). However, this could also reflect other structural features.

3. **cth- prefix**: Shows the strongest single correlation with Galenic intensity (rho = +0.95), and cth- is entirely absent from f41r (the coldest plant). But n=4 makes this unreliable.

### Critical Limitations

1. **Sample size**: n=5 plants (n=4 after removing Language B confound) is fundamentally insufficient for statistical inference. Most correlations could arise by chance.

2. **Currier A/B confound**: The Language A/B distinction dominates all clustering and similarity measures. Any cross-language comparison is contaminated.

3. **Multiple comparisons**: Testing 12 suffixes and 12 prefixes against a single variable inflates false positive rates. After Bonferroni correction, no individual correlation reaches significance.

4. **Plant identification uncertainty**: The identifications themselves are debated. If even one is wrong, correlations collapse.

### Recommendation

To properly test pharmaceutical encoding:
- Need 15-20 confidently identified plants, balanced across Language A and B
- Need independent plant identifications (not influenced by text analysis)
- Should test against VISUAL FEATURE encoding as a competing hypothesis
- The f9r-f47r pair merits detailed investigation: what specific headache vocabulary do they share, and does it appear in OTHER headache-treating plants in the manuscript?

---

*Analysis performed: 2026-04-10*
*Scripts: pharmaceutical_test.py, pharma_deep_dive.py*
*Data: RF1b-e.txt (EVA transcription)*
