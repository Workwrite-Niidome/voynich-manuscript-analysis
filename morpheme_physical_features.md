# Voynich Morpheme Analysis: Plant Physical Features

## Methodology

30 herbal pages (f1v through f24v) were visually examined from the PDF illustrations and classified by multiple physical features: leaf shape, flower presence/color, fruit/seed presence, root type, and plant habit. EVA transcription text was extracted for all 112 herbal-section folios (f1-f57). For each visual feature category, word-level and substring-level enrichment was computed using chi-squared tests on 2x2 contingency tables (feature-present vs feature-absent pages). Only associations with p < 0.05 are reported.

**Already decoded morphemes** (from prior work):
- ch- = aerial/visible domain, sh- = underground domain
- -yd- = divided leaves
- cth- = hard/astringent property, ckh- = hot/thermal property
- Grade system: null -> e -> ee -> eeo (general -> specific -> preparation)

---

## Section 1: Leaf Shape Morphemes

### 1.1 Round/Orbicular Leaves

**Pages classified**: f2v (giant round leaf), f5r (giant round water-lily), f13v (round lobed), f16r (trefoil/clover), f24r (round waxy), f24v (cordate), f23r (round bulging), f11r (wavy round) -- 8 pages, 569 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| *eee* (substring) | 21.1/k | 7.1/k | 2.96x | 13.25 | <0.001 |
| *ees* (substring) | 21.1/k | 7.8/k | 2.71x | 11.14 | <0.001 |
| *dal* (substring) | 31.6/k | 14.5/k | 2.19x | 10.36 | <0.01 |
| *om* (substring) | 19.3/k | 7.8/k | 2.48x | 8.49 | <0.01 |
| *yd* (substring) | 19.3/k | 9.7/k | 2.00x | 4.92 | <0.05 |
| otchy (word) | 12.3/k | 2.8/k | 4.42x | 14.55 | <0.001 |
| dal (word) | 14.1/k | 4.3/k | 3.24x | 10.34 | <0.01 |

**FINDING**: The triple-e sequence (*eee*) is strongly enriched on round-leaf pages (3x rate). This extended vowel may encode roundness or fullness of leaf shape. The suffix *-ees* shows the same pattern. The word `dal` is also enriched, possibly serving as a size/shape modifier for round forms.

**DEPLETED**: `aiin` (standalone) is significantly depleted on round-leaf pages (3.5/k vs 15.1/k, ratio 0.23, chi2=5.07), suggesting it may encode a contrasting feature (angularity or narrowness).

---

### 1.2 Linear/Needle-like Leaves

**Pages classified**: f14v (iris-like narrow), f21r (grass-like), f21v (fine rosemary-like), f4r (small scattered) -- 4 pages, 269 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| **-yd-** (substring) | **37.2/k** | **9.5/k** | **3.93x** | **19.78** | **<0.001** |
| *ot* (substring) | 148.7/k | 90.2/k | 1.65x | 10.73 | <0.01 |
| *aiin* (substring) | 189.6/k | 124.7/k | 1.52x | 9.95 | <0.01 |
| *chy* (substring) | 111.5/k | 64.4/k | 1.73x | 9.48 | <0.01 |
| *cth* (substring) | 85.5/k | 46.8/k | 1.83x | 8.58 | <0.01 |
| ty (word) | 11.2/k | 0.6/k | 17.27x | 30.69 | <0.001 |
| yty (word) | 11.2/k | 1.2/k | 9.42x | 17.77 | <0.001 |
| choty (word) | 14.9/k | 2.0/k | 7.27x | 17.92 | <0.001 |

**CRITICAL FINDING**: The morpheme **-yd-** is confirmed as a leaf-shape morpheme, but its strongest enrichment is on LINEAR/NEEDLE pages (ratio 3.93x, chi2=19.78), not just "divided" leaves as previously decoded. This is surprising -- -yd- may encode "narrow/elongated" rather than "divided." Both linear and divided leaves share the property of being narrow-segmented compared to round/broad leaves.

The word `ty` (standalone) and `yty` are nearly exclusive to linear-leaf pages. `ty` may be a minimal morpheme meaning "thin" or "linear."

---

### 1.3 Divided/Lobed Leaves

**Pages classified**: f2r (deeply lobed), f9r (bushy lobed), f9v (palmate divided), f19r (palmate lobed), f23v (palmate/geranium), f16v (narrow divided) -- 6 pages, 483 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| *or* (substring) | 176.0/k | 101.7/k | 1.73x | 26.85 | <0.001 |
| *dan* (substring) | 12.4/k | 1.9/k | **6.63x** | **21.27** | **<0.001** |
| *dor* (substring) | 20.7/k | 5.0/k | **4.18x** | **19.88** | **<0.001** |
| *chor* (substring) | 64.2/k | 36.4/k | 1.77x | 9.78 | <0.01 |
| dan (word) | 10.4/k | 1.0/k | **10.44x** | **27.48** | **<0.001** |
| chkr (word) | 6.2/k | 0.0/k | INF | 56.40 | <0.001 |
| dor (word) | 14.5/k | 3.5/k | 4.11x | 13.58 | <0.001 |
| cthor (word) | 14.5/k | 3.7/k | 3.87x | 12.41 | <0.001 |

**FINDING**: The substring **-dan-** is powerfully enriched on divided-leaf pages (6.63x, chi2=21.27). The word `dan` itself appears at 10.4x the background rate. This morpheme likely encodes "divided/split/segmented" -- the actual leaf-division morpheme.

The substring **-dor-** is also strongly enriched (4.18x). Since -or is a common suffix (flower/visible form), `dor` may be a compound: d(ivided) + or (form) = "divided appearance."

`chkr` appears exclusively on divided-leaf pages (INF ratio), though with only 3 occurrences.

---

### 1.4 Toothed/Serrated Leaves

**Pages classified**: f6r (deeply serrated spiky), f10r (serrated), f15r (deeply toothed), f17v (fern-like pinnate), f19v (pinnate serrate), f3v (spiky) -- 6 pages, 532 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| ***cth*** (substring) | **101.5/k** | **44.7/k** | **2.27x** | **35.49** | **<0.001** |
| ***cthy*** (substring) | **41.4/k** | **16.2/k** | **2.56x** | **18.46** | **<0.001** |
| *or* (substring) | 195.5/k | 100.1/k | 1.95x | 48.45 | <0.001 |
| *chor* (substring) | 69.5/k | 35.9/k | 1.94x | 15.67 | <0.001 |
| *om* (substring) | 22.6/k | 7.6/k | 2.95x | 13.30 | <0.001 |
| otcham (word) | 5.6/k | 0.0/k | INF | 50.93 | <0.001 |
| cthy (word) | 24.4/k | 8.2/k | 2.98x | 14.70 | <0.001 |
| cthaiin (word) | 7.5/k | 1.1/k | 6.79x | 14.12 | <0.001 |
| tchor (word) | 7.5/k | 1.0/k | 7.54x | 15.74 | <0.001 |

**CRITICAL FINDING**: The prefix **cth-** is the strongest correlate of toothed/serrated leaves (2.27x enrichment, chi2=35.49). Previously decoded as "hard/astringent," the correlation with toothed leaves reveals a deeper semantic connection: toothed/serrated edges are physically hard, sharp, prickly features. The cth- morpheme may encode "sharp/pointed/hard-edged" rather than purely taste-based "astringent."

The word `cthy` (cth + y minimal form) at 2.98x enrichment on serrated pages is the most robust single-word correlate. `otcham` appears exclusively on serrated/toothed pages.

The very strong *-or* enrichment here (1.95x, chi2=48.45) suggests -or may encode "edge/margin" or "appearance" specifically in the context of serrated leaves.

---

### 1.5 Smooth Oval Leaves

**Pages classified**: f1v (oval smooth), f8v (medium oval), f18v (oblong/elliptic), f20v (small rounded smooth), f7v (rosette smooth), f18r (ovate), f22r (pinnate compound) -- 7 pages, 596 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| ***ol*** (substring) | **221.5/k** | **144.8/k** | **1.53x** | **25.84** | **<0.001** |
| ***dol*** (substring) | **23.5/k** | **5.8/k** | **4.05x** | **25.51** | **<0.001** |
| ***shol*** (substring) | **35.2/k** | **13.7/k** | **2.57x** | **17.44** | **<0.001** |
| *dar* (substring) | 33.6/k | 17.2/k | 1.95x | 8.39 | <0.01 |
| dar (word) | 25.2/k | 8.8/k | 2.86x | 15.36 | <0.001 |
| dol (word) | 11.7/k | 3.3/k | 3.51x | 10.23 | <0.01 |
| dchor (word) | 10.1/k | 1.9/k | 5.31x | 15.55 | <0.001 |

**FINDING**: The suffix **-ol** is significantly enriched on smooth-leaf pages (1.53x, chi2=25.84). More strikingly, **dol** (d + ol) shows 4.05x enrichment as a substring and 3.51x as a standalone word. The word `dol` may encode "smooth" or "entire" (i.e., smooth-edged, as opposed to toothed `cth-` leaves).

**shol** is also enriched on smooth-leaf pages (2.57x, chi2=17.44), which contradicts the prior hypothesis that shol = "root." Instead, shol on smooth-leaf pages may indicate smooth/underground-like texture or the smooth, fleshy quality of these leaves.

---

### 1.6 Heart-shaped Leaves (Cordate)

**Pages classified**: f8r (giant arrowhead), f24v (cordate climbing) -- 2 pages only, 221 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| *sho* (substring) | 95.0/k | 53.5/k | 1.78x | 7.21 | <0.01 |
| *od* (substring) | 113.1/k | 68.1/k | 1.66x | 6.80 | <0.01 |
| *om* (substring) | 22.6/k | 8.1/k | 2.78x | 5.39 | <0.05 |
| do (word) | 18.1/k | 0.9/k | 21.13x | 51.21 | <0.001 |

**FINDING**: With only 2 pages, individual word associations are inflated. However, `do` (standalone) is remarkably enriched (21x). The *-od-* enrichment may relate to pointed tips (heart-shaped leaves have a pointed apex). Sample too small for confident morpheme identification.

---

## Section 2: Flower Morphemes

### 2.1 Prominent Flowers Present (any color)

**Pages**: f4v, f7r, f9v, f11r, f17r, f22r, f15v, f21r, f23v, f10r -- 10 pages, 783 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| ***oiin*** (substring) | **24.3/k** | **7.4/k** | **3.28x** | **23.47** | **<0.001** |
| *or* (substring) | 159.6/k | 100.6/k | 1.59x | 26.58 | <0.001 |
| *yp* (substring) | 12.8/k | 3.6/k | 3.50x | 13.69 | <0.001 |
| *cth* (substring) | 79.2/k | 45.1/k | 1.76x | 18.30 | <0.001 |
| oiin (word) | 6.4/k | 0.5/k | **14.01x** | **26.88** | **<0.001** |
| chkaiin (word) | 5.1/k | 0.5/k | 11.21x | 18.62 | <0.001 |
| cthy (word) | 20.4/k | 8.1/k | 2.53x | 12.15 | <0.001 |

**CRITICAL FINDING**: The morpheme **-oiin** is the strongest flower correlate (3.28x as substring, 14.01x as standalone word `oiin`). This diphthong-like ending appears predominantly on flower-bearing pages and is nearly absent from leaf-only and root-only pages.

The suffix **-oiin** may be a variant of -aiin with the vowel shifted to mark "flowering" as opposed to the more general -aiin. Alternatively, `oiin` may be the word for "flower" or "blossom" itself.

**DEPLETED on flower pages**: `aiin` standalone (ratio 0.33x), `chey` (0.33x), `ar` (0.27x). The depletion of `aiin` on flower pages while `oiin` is enriched suggests these are contrastive morphemes.

---

### 2.2 Blue Flowers

**Pages**: f4v, f9v, f11r, f17v, f19v, f22r, f23v, f10r, f18v -- 9 pages, 756 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| *or* (substring) | 172.0/k | 99.7/k | 1.72x | 38.53 | <0.001 |
| *ol* (substring) | 216.9/k | 143.8/k | 1.51x | 29.29 | <0.001 |
| *dor* (substring) | 14.6/k | 5.0/k | 2.91x | 11.11 | <0.001 |
| *oiin* (substring) | 17.2/k | 8.1/k | 2.13x | 6.67 | <0.01 |
| kchol (word) | 9.3/k | 1.2/k | 7.41x | 23.77 | <0.001 |
| okeol (word) | 5.3/k | 0.5/k | 11.65x | 19.48 | <0.001 |

**FINDING**: Blue-flower pages show strong enrichment of the compound `kchol` (7.41x). Given ckh- = "hot/thermal," `kchol` may be an inversion or variant encoding "cold-blue" through the k-ch combination. The word `okeol` is also highly enriched.

---

### 2.3 Red Flowers

**Pages**: f17r, f5v, f14v, f15v -- 4 pages, 250 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| ***yd*** (substring) | **48.0/k** | **9.2/k** | **5.20x** | **36.06** | **<0.001** |
| *or* (substring) | 192.0/k | 103.1/k | 1.86x | 20.40 | <0.001 |
| *oiin* (substring) | 28.0/k | 8.3/k | 3.39x | 10.88 | <0.001 |
| cthor (word) | 20.0/k | 3.9/k | 5.17x | 14.84 | <0.001 |
| okshy (word) | 8.0/k | 0.4/k | 18.62x | 22.25 | <0.001 |
| oiin (word) | 8.0/k | 0.8/k | 10.64x | 13.60 | <0.001 |

**FINDING**: Red-flower pages show the strongest -yd- enrichment of ANY category (5.20x, chi2=36.06). This is unexpected if -yd- means "divided." The connection may be: many red-flowered plants in the manuscript also have divided/narrow leaves, OR -yd- encodes a broader property shared by both red coloring and divided form (perhaps "hot/fiery/sharp").

`cthor` is enriched on red-flower pages (5.17x), consistent with cth- = "astringent/sharp" properties often associated with red-pigmented plants.

---

## Section 3: Fruit/Seed Morphemes

### 3.1 Fruits/Seeds Present

**Pages**: f4r, f6r, f6v, f7v, f14v, f15r, f20v, f22v, f18r -- 9 pages, 692 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| ***cth*** (substring) | **104.0/k** | **43.5/k** | **2.39x** | **51.56** | **<0.001** |
| ***cthy*** (substring) | **49.1/k** | **15.1/k** | **3.25x** | **43.05** | **<0.001** |
| ***ych*** (substring) | **26.0/k** | **7.6/k** | **3.44x** | **24.82** | **<0.001** |
| *yd* (substring) | 21.7/k | 9.4/k | 2.32x | 9.60 | <0.01 |
| cthy (word) | **36.1/k** | **7.0/k** | **5.17x** | **60.44** | **<0.001** |
| cthaiin (word) | 7.2/k | 1.0/k | 7.12x | 16.93 | <0.001 |
| cthom (word) | 4.3/k | 0.3/k | 12.82x | 16.35 | <0.001 |

**CRITICAL FINDING**: The **cth-** prefix is the single strongest correlate of fruit/seed pages, with `cthy` reaching the highest chi2 of ANY word-feature association in this entire study (chi2=60.44, p<0.001, 5.17x enrichment).

This reframes the cth- morpheme: rather than purely "hard/astringent" (a taste property), cth- may primarily encode **"fruit/seed"** -- which ARE characteristically hard/astringent in many medicinal plants. The semantic connection: fruits and seeds are the hard, dried, astringent parts of plants.

The substring **-ych-** is also strongly enriched (3.44x, chi2=24.82). This may represent a reversed or compound form where y- modifies ch- in the context of fruit/seed descriptions.

`cthom` (cth + om) appears almost exclusively on fruit pages (12.82x) -- confirming it as a fruit/seed-specific term, possibly "seed" vs `cthy` = "fruit" (general).

---

## Section 4: Root Type Morphemes

### 4.1 Bulbous Root (onion/garlic/tuber type)

**Pages**: f4v, f13v, f23r, f24r, f16v, f19r, f9r -- 7 pages, 548 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| *dal* (substring) | 31.0/k | 14.5/k | 2.13x | 9.21 | <0.01 |
| *chy* (substring) | 96.7/k | 63.8/k | 1.52x | 9.12 | <0.01 |
| *chor* (substring) | 60.2/k | 36.4/k | 1.65x | 8.07 | <0.01 |
| dal (word) | 20.1/k | 4.0/k | **5.03x** | **27.30** | **<0.001** |
| chkr (word) | 5.5/k | 0.0/k | INF | 49.36 | <0.001 |
| otchy (word) | 10.9/k | 2.9/k | 3.80x | 10.07 | <0.01 |

**FINDING**: The word **`dal`** is the strongest correlate of bulbous roots (5.03x, chi2=27.30). Since `dal` also appeared enriched on round-leaf pages, this morpheme may encode **"round/bulbous/swollen"** -- a shape descriptor applying to both round leaves and bulbous roots.

`chkr` appears exclusively on bulbous-root pages (INF ratio, also found on divided-leaf pages). This rare word may specifically denote a tuber or bulb.

---

### 4.2 Fibrous Root

**Pages**: f9v, f17v, f18v, f19v, f20v -- 5 pages, 427 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| *ol* (substring) | 217.8/k | 146.4/k | 1.49x | 16.36 | <0.001 |
| *ych* (substring) | 23.4/k | 8.2/k | 2.85x | 10.71 | <0.01 |
| *chol* (substring) | 77.3/k | 44.0/k | 1.76x | 10.40 | <0.01 |
| cphol (word) | 7.0/k | 0.4/k | **16.04x** | **24.20** | **<0.001** |
| ychor (word) | 7.0/k | 0.5/k | 12.83x | 20.48 | <0.001 |

**FINDING**: The word **`cphol`** (cph + ol) is strongly associated with fibrous roots (16.04x). The `cph-` prefix variant may encode "fibrous/threadlike" texture. This is a sub-category within the sh- (underground) domain, where `cph-` = fine/thread-like fibers.

---

### 4.3 Taproot

**Pages**: f11r, f18r, f3r, f7r, f15v -- 5 pages, 367 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| ***om*** (substring) | **35.4/k** | **7.4/k** | **4.79x** | **33.00** | **<0.001** |
| *chor* (substring) | 81.7/k | 36.0/k | 2.27x | 20.32 | <0.001 |
| *cho* (substring) | 245.2/k | 146.3/k | 1.68x | 27.08 | <0.001 |
| *cthy* (substring) | 38.1/k | 16.8/k | 2.28x | 9.36 | <0.01 |
| chom (word) | 8.2/k | 1.0/k | **8.35x** | **14.58** | **<0.001** |
| cham (word) | 8.2/k | 1.2/k | **6.83x** | **11.75** | **<0.001** |

**CRITICAL FINDING**: The suffix **-om** is the strongest taproot correlate (4.79x, chi2=33.00). The words `chom` and `cham` are both highly enriched on taproot pages, confirming the prior hypothesis that these words encode "root" (underground main structure).

The morphological pattern emerges:
- **-om/-am** = taproot/main root (the singular, thick underground organ)
- vs **cphol** = fibrous root (fine, thread-like roots)
- vs **dal** = bulbous root (round, swollen underground structure)

---

## Section 5: Size and Habit Morphemes

### 5.1 Tall/Tree-like Plants

**Pages**: f20r, f11v, f13r -- 3 pages, 195 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| ***chy*** (substring) | **164.1/k** | **63.6/k** | **2.58x** | **31.42** | **<0.001** |
| *cho* (substring) | 251.3/k | 148.0/k | 1.70x | 15.98 | <0.001 |
| *pch* (substring) | 46.2/k | 18.5/k | 2.50x | 7.84 | <0.01 |
| dchy (word) | 20.5/k | 1.7/k | **12.01x** | **32.36** | **<0.001** |
| qoteey (word) | 15.4/k | 0.4/k | 36.02x | 58.42 | <0.001 |
| oldy (word) | 10.3/k | 0.2/k | 48.03x | 46.07 | <0.001 |

**FINDING**: The suffix **-chy** (and -y minimal form) is strongly enriched on tree-like plants (2.58x). The word `dchy` (12.01x) may encode "tall" or "tree-like." The compound `oldy` (48x enrichment) appears almost exclusively on tall plant pages.

---

### 5.2 Bushy Habit

**Pages**: f9r, f19r, f21v, f11v, f23v -- 5 pages, 333 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| ***dor*** (substring) | **27.0/k** | **5.0/k** | **5.42x** | **27.30** | **<0.001** |
| ***shy*** (substring) | **39.0/k** | **14.6/k** | **2.67x** | **12.57** | **<0.001** |
| *or* (substring) | 171.2/k | 103.1/k | 1.66x | 15.81 | <0.001 |
| dor (word) | 21.0/k | 3.5/k | **6.06x** | **24.38** | **<0.001** |
| tchy (word) | 12.0/k | 1.2/k | 10.08x | 24.02 | <0.001 |
| shy (word) | 18.0/k | 5.5/k | 3.26x | 8.46 | <0.01 |

**FINDING**: The word/substring **`dor`** is a powerful correlate of bushy habit (5.42x as substring, 6.06x as word). Since divided-leaf pages also showed `dor` enrichment, and bushy plants often have divided leaves, `dor` may encode "spreading/branching" -- applicable to both leaf division and plant bushiness.

The word **`shy`** (standalone) is enriched on bushy pages (3.26x). Since sh- = underground/hidden, `shy` on bushy plants may describe the hidden/concealed quality of a dense, bushy canopy.

---

### 5.3 Single Stem Upright

**Pages**: f1v, f8r, f18v, f7r, f24v, f22r -- 6 pages, 537 words

| Morpheme | In (rate/k) | Out (rate/k) | Ratio | Chi2 | p |
|----------|------------|-------------|-------|------|---|
| ***dol*** (substring) | **20.5/k** | **6.1/k** | **3.36x** | **15.31** | **<0.001** |
| *shol* (substring) | 31.7/k | 14.1/k | 2.25x | 10.56 | <0.01 |
| *ko* (substring) | 50.3/k | 27.4/k | 1.84x | 9.55 | <0.01 |
| do (word) | 9.3/k | 0.8/k | **12.00x** | **29.46** | **<0.001** |
| dol (word) | 13.0/k | 3.3/k | 3.92x | 12.40 | <0.001 |
| dchor (word) | 9.3/k | 2.0/k | 4.67x | 11.31 | <0.001 |

**FINDING**: The word `dol` and substring *dol* are enriched on single-stem pages (3.36x). Combined with its enrichment on smooth-leaf pages, `dol` may encode "simple/single/undivided" -- contrasting with `dor` (branching/divided) and `dal` (round/bulbous).

---

## Consolidated Morpheme Dictionary

### NEW MORPHEME IDENTIFICATIONS (p < 0.05)

| # | Morpheme | Meaning | Best Evidence | Chi2 | p | Confidence |
|---|----------|---------|--------------|------|---|-----------|
| 1 | **-dan-** | divided/lobed/segmented (leaves) | 6.63x on divided-leaf pages | 21.27 | <0.001 | HIGH |
| 2 | **-eee-** | round/full/orbicular (leaf shape) | 2.96x on round-leaf pages | 13.25 | <0.001 | MEDIUM-HIGH |
| 3 | **cthy** / **cth-** | fruit/seed (hard reproductive part) | 5.17x / 2.39x on fruit pages | 60.44 / 51.56 | <0.001 | HIGH |
| 4 | **oiin** | flower/blossom | 14.01x word, 3.28x substring on flower pages | 26.88 / 23.47 | <0.001 | HIGH |
| 5 | **dal** | round/bulbous/swollen | 5.03x on bulbous root, 3.24x on round leaves | 27.30 / 10.34 | <0.001 | HIGH |
| 6 | **-om/-am** | taproot/main root | 4.79x on taproot pages | 33.00 | <0.001 | HIGH |
| 7 | **dol** | simple/single/smooth | 4.05x on smooth leaves, 3.36x on single-stem | 25.51 / 15.31 | <0.001 | MEDIUM-HIGH |
| 8 | **dor** | branching/spreading | 5.42x on bushy, 4.18x on divided-leaf | 27.30 / 19.88 | <0.001 | MEDIUM-HIGH |
| 9 | **cphol** | fibrous/thread-like (roots) | 16.04x on fibrous-root pages | 24.20 | <0.001 | MEDIUM |
| 10 | **ty** | thin/linear/needle-like | 17.27x on linear-leaf pages | 30.69 | <0.001 | MEDIUM |
| 11 | **dchy** | tall/tree-like/upright | 12.01x on tall/tree pages | 32.36 | <0.001 | MEDIUM |
| 12 | **shy** (standalone) | bushy/dense/hidden-canopy | 3.26x on bushy-habit pages | 8.46 | <0.01 | MEDIUM |
| 13 | **-ych-** | fruit-bearing modification | 3.44x on fruit/seed pages | 24.82 | <0.001 | MEDIUM |
| 14 | **chkr** | bulb/tuber (underground swelling) | INF (exclusive to bulbous-root + divided) | 49.36-56.40 | <0.001 | LOW-MEDIUM |
| 15 | **cthom** | seed (specific fruit/seed term) | 12.82x on fruit/seed pages | 16.35 | <0.001 | MEDIUM |

---

## Revised Morpheme System

### The d- Shape Paradigm (NEW)

A previously undetected paradigm emerges in the `d-` prefix family:

| Morpheme | Shape | Evidence |
|----------|-------|---------|
| **dal** | round/bulbous/swollen | bulbous roots, round leaves |
| **dol** | simple/single/smooth/entire | smooth leaves, single stems |
| **dor** | branching/spreading/divided | bushy habit, divided leaves |
| **dan** | segmented/divided/lobed | divided/lobed leaves specifically |

This is a **shape vowel-alternation paradigm**: the consonant frame d-l/d-r/d-n is constant, while the vowel (a/o/or/an) specifies the type of shape. This parallels the ch- plant-part paradigm (chol/chor/cham/chom) but operates in the domain of **physical shape description**.

### The cth- Domain Reframing

| Previous | Revised | Evidence |
|----------|---------|---------|
| cth = hard/astringent (taste) | cth = fruit/seed/hard-part | chi2=60.44 for cthy on fruit pages |
| -- | cthy = fruit (general) | 5.17x on fruit pages |
| -- | cthom = seed (specific) | 12.82x on fruit pages |
| -- | cthor = fruit-appearance | enriched on red-flower + fruit pages |
| -- | cthaiin = fruit-of (genitive) | 7.12x on fruit pages |

The "hard/astringent" reading was a secondary property of the primary referent: fruits and seeds are the hardest, most astringent parts of medicinal plants.

### The Root-Type Sub-paradigm within sh- (Underground)

| Morpheme | Root Type | Evidence |
|----------|-----------|---------|
| **cham/chom** | taproot (main, thick) | 4.79x (-om) on taproot pages |
| **dal** | bulbous root (swollen) | 5.03x on bulbous-root pages |
| **cphol** | fibrous root (threads) | 16.04x on fibrous-root pages |

### Revised -yd- Interpretation

Previously decoded as "divided leaves," -yd- shows its strongest enrichment on:
1. Linear/needle leaves: 3.93x (chi2=19.78)
2. Red flowers: 5.20x (chi2=36.06)
3. Fruit/seed pages: 2.32x (chi2=9.60)

Revised interpretation: **-yd- = narrow/fine/elongated**, which encompasses both divided/dissected leaves (narrow segments) and linear/needle leaves (inherently narrow). The red-flower correlation may reflect co-occurrence (many red-flowered plants have narrow leaves in the manuscript's illustrations).

---

## Statistical Confidence Summary

| Threshold | Morphemes meeting it |
|-----------|---------------------|
| chi2 > 10 (p < 0.001) | dan, eee, cthy/cth, oiin, dal, om/am, dol, dor, cphol, ty, dchy, ych, chkr, cthom |
| chi2 > 6.6 (p < 0.01) | + shy, ees |
| chi2 > 3.8 (p < 0.05) | + (all reported) |

14 morphemes meet the p < 0.001 threshold. 15 total meet p < 0.05.

---

## Caveats

1. **Multiple testing**: With ~50 substrings tested against ~15 categories, some associations may be false positives even at p < 0.05. The strongest findings (chi2 > 20) remain robust after Bonferroni correction.

2. **Page classification subjectivity**: Visual classification of leaf shapes and root types from 600-year-old illustrations involves judgment calls. Different classifiers might categorize borderline pages differently.

3. **Confounding features**: Many physical features co-occur (e.g., toothed leaves often appear with fibrous roots, bushy plants often have divided leaves). Some morpheme-feature associations may reflect confounded features rather than direct encoding.

4. **Small sample sizes**: Categories with fewer than 5 pages (heart-shaped: 2 pages; tall/tree: 3 pages) produce inflated ratios and should be treated with lower confidence.

5. **The -yd- puzzle**: This morpheme correlates with multiple, seemingly unrelated features (linear leaves, red flowers, divided leaves, fruits). It may encode a broader physical property ("fine/narrow/thin") or may be a Galenic/humoral category ("hot-dry") that cross-cuts visible morphology.
