# Full-Scale Morpheme-Illustration Validation

## Methodology

### Dataset
- **129 herbal folios** examined (all pages with `$I=H` tag in EVA transcription)
- **Herbal A**: f1v-f57r (111 pages)
- **Herbal edge**: f65r, f65v, f66v (3 pages)
- **Herbal B**: f87r-f96v (15 pages, pharmaceutical-herbal)
- **Text source**: RF1b-e.txt (EVA transcription, Takahashi reading)

### Visual Classification
Every herbal folio was examined from PDF scans and classified on 8 binary features:

| Feature | Description | Positive Count | % |
|---------|-------------|---------------|---|
| leaves_prominent | Leaves >50% of illustration | 129/129 | 100% |
| roots_visible | Roots drawn | 124/129 | 96% |
| flowers_visible | Flowers visible | 74/129 | 57% |
| fruits_seeds | Fruits or seeds visible | 34/129 | 26% |
| tall_plant | Plant >half page height | 80/129 | 62% |
| leaves_divided | Leaves divided/lobed/compound | 57/129 | 44% |
| leaves_linear | Leaves narrow/linear | 18/129 | 14% |
| leaves_round | Leaves round/broad/oval | 53/129 | 41% |

Note: `leaves_prominent` has zero variance (all herbal pages have prominent leaves) and was excluded from correlation analysis. `roots_visible` has very low variance (96%).

### Word Selection
- **21 words** with 50+ total occurrences across the herbal section were tested
- **8 words** with 100+ occurrences: `daiin` (352), `chol` (197), `aiin` (146), `chor` (143), `s` (139), `chy` (121), `or` (115), `chey` (106)
- Total words in herbal section: 10,592
- Unique word types: 3,645

---

## Results

### 1. Pearson Correlation: Word Frequency vs Visual Features

Out of **168 word-feature combinations tested**, the number of statistically significant correlations:

| Threshold | Count |
|-----------|-------|
| p < 0.05 (uncorrected) | ~15 (expected ~8 by chance) |
| p < 0.01 (uncorrected) | **1** (expected ~2 by chance) |
| Bonferroni-corrected (p < 0.000298) | **1** |
| BH FDR (q < 0.05) | **1** |

### The ONE Significant Correlation

| Word | Feature | Pearson r | p-value |
|------|---------|-----------|---------|
| `sho` | roots_visible | -0.334 | 0.000110 |

**Interpretation**: The word `sho` (78 occurrences total) appears at higher frequency on pages where roots are NOT drawn. However, this is based on only 5 pages without visible roots (vs 124 with roots), making it fragile despite the low p-value. The mean frequency of `sho` is 0.0303 on rootless pages vs 0.0071 on rooted pages.

This result is **negative** for the descriptive hypothesis: if `sho` described roots, the correlation would be positive.

### 2. TOP 10 Correlations by Effect Size (uncorrected)

| Rank | Word | Feature | r | p | Direction |
|------|------|---------|---|---|-----------|
| 1 | `sho` | roots_visible | -0.334 | 0.0001 | More `sho` when NO roots |
| 2-10 | various | various | |r| < 0.2 | p > 0.01 | Not significant |

No other word-feature correlation reaches p < 0.01. The expected number of false positives at p < 0.01 across 168 tests is ~1.7, and we found exactly 1. This is consistent with pure chance.

### 3. CH/SH Ratio Analysis

#### CH-rate vs Illustration Complexity
- ch-frequency rate vs complexity (sum of visual features): **r = -0.231, p = 0.008**
- sh-frequency rate vs complexity: **r = -0.148, p = 0.095** (not significant)

CH words appear **slightly less** on visually complex pages. This is the opposite of what we'd expect if CH were descriptive (more features = more to describe = more CH). However, the effect is small.

#### SH-rate vs Specific Features

The one notable pattern in the sh morpheme:

| Feature | sh-rate correlation | p-value | |
|---------|--------------------|---------|-|
| leaves_divided | r = -0.319 | p = 0.0002 | *** |
| leaves_linear | r = +0.218 | p = 0.013 | * |

`sh` words appear **less often on pages with divided/lobed leaves** and **more often on pages with linear/narrow leaves**. This survives multiple testing for the sh-divided relationship.

#### CH-rate vs Specific Features

| Feature | ch-rate correlation | p-value | |
|---------|--------------------|---------|-|
| leaves_round | r = +0.213 | p = 0.015 | * |
| flowers_visible | r = -0.211 | p = 0.016 | * |
| leaves_divided | r = -0.185 | p = 0.036 | * |

CH words appear slightly more on pages with round leaves and slightly less on pages with flowers. None survive strict multiple testing correction.

### 4. Text Amount vs Visual Features

No visual feature significantly predicts how much text appears on a page (all p > 0.05). This is important: the text amount is not driven by illustration complexity, which undermines any simple "description" model.

---

## Assessment

### What the Data Says

1. **No high-frequency word robustly predicts any visual feature.** Across 168 tests, we found 1 significant result (sho vs roots_visible), which is within the expected false positive range. After removing that one fragile result (n=5 for rootless pages), zero robust correlations remain.

2. **The ch/sh ratio does NOT track illustration complexity.** CH-rate actually decreases slightly with complexity (r = -0.23), opposite to what a descriptive system would predict.

3. **The one promising lead: sh-frequency vs leaf shape.** Pages with divided/lobed leaves have significantly fewer sh-words (r = -0.319, p = 0.0002). This could mean:
   - sh-words describe something that divided-leaf plants lack (e.g., smoothness, simplicity)
   - Or it's a structural artifact: divided-leaf plants tend to have more text containing ch-words, diluting sh
   - Or coincidence with page position in the manuscript

4. **The descriptive-system hypothesis is not dead but is in critical condition.** If the text described the illustrations, we would expect multiple word-feature correlations at the p < 0.001 level. We found essentially none for individual words.

### Why This Might Still Be Too Pessimistic

- The herbal pages may describe **uses, preparations, or properties** rather than **visual appearance**. A word meaning "boil the leaves" would not correlate with leaf shape.
- The EVA transcription may merge distinct Voynich characters that have different meanings.
- Word-level analysis may miss morpheme-level patterns (e.g., prefixes/suffixes that modify meaning).

### Why This Might Still Be Too Optimistic

- The sh vs leaves_divided correlation (r = -0.319) has no clear interpretation under any proposed decipherment. It is opposite in sign to what "sh = leaf" would predict.
- We tested 21 words x 8 features. Finding one correlation at p = 0.0002 among 168 tests is not as surprising as it seems (expected ~0.03 at that threshold, so it is somewhat notable, but a single result is unreliable).

---

## Full Classification Table

The complete visual classification of all 129 herbal folios is embedded in the analysis script at `visual_classification.py`. Key summary:

- Leaves are always prominent (100%)
- Roots are almost always visible (96%)  
- Flowers appear on 57% of pages
- Fruits/seeds appear on 26%
- Divided/lobed leaves on 44%
- Round/broad leaves on 41%
- Linear/narrow leaves on 14% (the least common feature)

---

## Verdict

**The descriptive system hypothesis -- that Voynichese words describe the illustrated plants -- receives no support from this full-scale analysis.** Zero individual high-frequency words reliably predict any visual feature of the illustrated plant across all 129 herbal folios.

The single surviving correlation (sh-rate vs leaves_divided, r = -0.319) is intriguing but has no clear semantic interpretation and is in the wrong direction for the "sh = plant substance" hypothesis.

The text could still be meaningful but is not straightforwardly describing the visible illustrations. It may be pharmaceutical (recipes, dosages), astrological, or entirely unrelated to the pictures.

---

## Technical Details

- **Statistics**: Pearson correlation, Bonferroni correction, Benjamini-Hochberg FDR
- **Word frequencies**: Normalized per-page rates (word count / total words on page)
- **Visual classification**: Manual binary coding by systematic examination of Yale Beinecke MS 408 digital scans
- **Software**: Python 3.13, NumPy, SciPy
- **Analysis scripts**: `extract_words.py`, `visual_classification.py`
