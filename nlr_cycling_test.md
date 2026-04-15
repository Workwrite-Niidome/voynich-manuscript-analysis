# Voynich Manuscript: n/l/r Suffix Cycling Analysis

## Overview

- Source: RF1b-e.txt (EVA transcription)
- Total folios: 226
- Total words parsed: 37276
- Words ending in n/l/r: 17290 (46.4%)
  - n: 6005 (34.7%)
  - l: 5680 (32.9%)
  - r: 5605 (32.4%)
- Words NOT ending in n/l/r: 19986 (53.6%)

---

## 1. Cycling Hypothesis (n -> l -> r -> n ...)

Total n/l/r words in sequence: 17290

Suffix-to-suffix step (mod 3):
  +1 (forward cycle): 5514 (31.9%)
  +2 (backward/skip): 5201 (30.1%)
   0 (same suffix):   6574 (38.0%)
  Expected if random: 33.3% each

Lag-1 autocorrelation per suffix indicator:
  n: 0.0654
  l: 0.0774
  r: 0.0671

Interpretation: If cycling, lag-1 autocorrelation should be strongly negative
(approximately -0.5 for perfect cycling). Near 0 = independent.

---

## 2. Avoidance Hypothesis

Suffix frequencies: n=0.347, l=0.329, r=0.324

P(suffix_i = suffix_{i-1}) observed:  0.3802 (6574/17289)
P(same) expected if independent:      0.3336
P(same) expected if uniform (1/3):     0.3333

Binomial test (observed vs independent expectation):
  p-value (one-sided, less): 1.000000e+00
  Significant avoidance: NO (alpha=0.01)

Binomial test (observed vs uniform 1/3):
  p-value (one-sided, less): 1.000000e+00
  Significant avoidance: NO (alpha=0.01)

---

## 3. Stem-Level Rotation

Top stems (appearing 2+ times per folio): o, daii, a, aii, cho, da, qoka, qokai, qokaii, oka

Per-stem same-suffix repetition rate (within folio):
Stem          Same  Diff  Total  P(same) Sequences
--------------------------------------------------
o              411   266    677    0.607   112
daii           505    33    538    0.939   162
a              273   259    532    0.513    98
aii            392    45    437    0.897   101
cho            232   181    413    0.562   121
da             164   143    307    0.534   102
qoka           146   105    251    0.582    55
qokai          224    19    243    0.922    37
qokaii         187     3    190    0.984    47
oka             90    78    168    0.536    62
--------------------------------------------------
OVERALL       2624  1132   3756    0.699

Test vs 1/3 expected (if uniform suffix per stem):
  Observed P(same): 0.6986
  p-value: 0.000000e+00
  Perfect rotation would give P(same) = 0
  Independence gives P(same) ~= 1/3

---

## 4. Global Balance Mechanism

Folios analyzed: 223
Folio-thirds analyzed: 669

Mean chi-squared (folio thirds): 4.745
Mean chi-squared (whole folios): 8.870
Expected chi-squared under uniform random: 2.000

T-test (folio thirds chi2 < 2.0):
  t-statistic: 15.214, one-sided p: 1.000000e+00
  More balanced than random: NO

T-test (whole folios chi2 < 2.0):
  t-statistic: 12.282, one-sided p: 1.000000e+00
  More balanced than random: NO

Comparison: thirds vs whole folio balance:
  Mean chi2 thirds: 4.745
  Mean chi2 whole:  8.870
  Thirds are MORE balanced (lower chi2) than whole folios

---

## 5. Cross-Word Suffix Transition Matrix

Observed transition counts (row = current, col = next):
              n        l        r    Total
     n     2342     1876     1787     6005
     l     1772     2161     1747     5680
     r     1891     1642     2071     5604

Transition probabilities (row = current, col = next):
              n        l        r
     n    0.390    0.312    0.298
     l    0.312    0.380    0.308
     r    0.337    0.293    0.370

Chi-squared test of independence:
  chi2 = 179.954, dof = 4, p-value = 7.628347e-38
  Transitions are DEPENDENT (not independent) (alpha=0.01)

Expected counts under independence:
              n        l        r
     n   2085.7   1972.5   1946.8
     l   1972.8   1865.7   1841.4
     r   1946.4   1840.8   1816.8

Standardized residuals (observed - expected) / sqrt(expected):
              n        l        r
     n     5.61    -2.17    -3.62
     l    -4.52     6.84    -2.20
     r    -1.26    -4.63     5.96

Residuals > +2 or < -2 indicate significant over/under-representation.

---

## Summary of Findings

| Test | Hypothesis | Result |
|------|-----------|--------|
| 1. Cycling | n->l->r->n strict rotation | **REJECTED** -- no cycling detected |
| 2. Avoidance | Consecutive words avoid same suffix | **REJECTED** -- opposite: ATTRACTION observed |
| 3. Stem rotation | Same stem rotates through n/l/r | **REJECTED** -- strong same-suffix PERSISTENCE |
| 4. Global balance | n:l:r balanced within folio thirds | **REJECTED** -- LESS balanced than random |
| 5. Transition matrix | Suffix transitions are independent | **REJECTED** -- significant SELF-TRANSITION bias |

## Interpretation

### The n/l/r suffixes show ATTRACTION, not cycling or avoidance

The results unanimously reject all cycling/avoidance hypotheses and instead reveal a **self-attraction pattern**: the same suffix tends to repeat.

**Key findings:**

1. **No cycling whatsoever.** Lag-1 autocorrelations are weakly POSITIVE (+0.065 to +0.077), not the strongly negative values (-0.5) that cycling would produce. The suffix-step distribution shows 38% same-suffix pairs vs 33.3% expected -- the opposite of cycling.

2. **Same-suffix attraction, not avoidance.** P(same suffix) = 0.380, significantly ABOVE the 0.334 independence expectation (p = 1.0 for the one-sided "less" test). Consecutive words are ~14% more likely to share a suffix than chance predicts.

3. **Stems strongly prefer a single suffix.** This is the most striking result. Stems like "daii" appear with the same suffix 93.9% of the time, and "qokaii" at 98.4%. Even "flexible" stems like "cho" (56.2%) and "da" (53.4%) still exceed the 33% independence baseline. Overall P(same) = 0.699 vs expected 0.333. This suggests that n/l/r are NOT interchangeable suffixes being rotated -- each stem has a strongly preferred ending.

4. **No global balancing mechanism.** Chi-squared values are HIGHER than expected under uniform random distribution (mean 4.75 for thirds, 8.87 for whole folios vs expected 2.0). The n:l:r distribution is less balanced than chance, not more. However, thirds are more balanced than whole folios, which is consistent with local variation in suffix preference across different sections of text (a natural property of any structured text).

5. **Transition matrix shows significant self-transition bias.** The chi-squared test massively rejects independence (chi2 = 179.95, p = 7.6e-38). The diagonal of the transition matrix (same->same) consistently exceeds expectation, with standardized residuals of +5.6, +6.8, and +6.0. This is not cycling but clustering.

### Implications for Voynich studies

These results argue against the hypothesis that n, l, and r function as interchangeable "null suffixes" that are cycled for variety or aesthetic balance. Instead, the data suggest:

- **n/l/r carry meaning** (or at least are structurally determined). If they were meaningless decorations cycled for visual variety, we would expect avoidance of same-suffix repetition. The opposite is observed.
- **Stem+suffix combinations are relatively fixed.** "daiin" strongly prefers the -n ending, not rotating through "daiil" and "daiir". This is more consistent with morphological structure than with a cipher substitution or meaningless ornamentation.
- **The near-uniform global frequencies (34.7% / 32.9% / 32.4%) arise from text composition, not intentional balancing.** Different stems prefer different suffixes, and the aggregate happens to be roughly balanced -- much as English morphemes produce roughly balanced letter frequencies without any intentional balancing mechanism.

The self-attraction pattern is consistent with Voynichese having genuine linguistic structure where suffix choice is lexically or grammatically determined, not a decorative or entropic feature.
