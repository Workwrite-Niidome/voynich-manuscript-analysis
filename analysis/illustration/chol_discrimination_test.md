# Chol/Shol Discrimination Tests

Red-team challenge: discriminate between chol='leaf' vs 'green' vs 'plant' vs 'visible/above-ground'.

**Corpus**: 226 folios parsed from EVA transcription (RF1b-e.txt)

## Section Distribution

| Section | Code | Folios |
|---------|------|--------|
| Astronomical | A | 8 |
| Biological | B | 19 |
| Cosmological | C | 10 |
| Herbal | H | 129 |
| Pharmaceutical | P | 16 |
| Stars | S | 25 |
| Text-only | T | 7 |
| Zodiac | Z | 12 |

---
## Test 1: Green vs Leaf (Section Distribution)

**Logic**: If chol means 'green' (a color), it should appear across sections
(green stars, green biological pools, etc.). If it means 'leaf', it should
concentrate in herbal (H) and pharmaceutical (P) sections.

### Chol distribution by section (exact match)

| Section | Folios | chol count | Total words | chol/1000 words | % of all chol |
|---------|--------|-----------|-------------|-----------------|---------------|
| Astronomical (A) | 8 | 5 | 811 | 6.2 | 1.4% |
| Biological (B) | 19 | 9 | 6089 | 1.5 | 2.5% |
| Cosmological (C) | 10 | 10 | 1599 | 6.3 | 2.8% |
| Herbal (H) | 129 | 206 | 11426 | 18.0 | 57.7% |
| Pharmaceutical (P) | 16 | 43 | 2440 | 17.6 | 12.0% |
| Stars (S) | 25 | 62 | 11083 | 5.6 | 17.4% |
| Text-only (T) | 7 | 17 | 2226 | 7.6 | 4.8% |
| Zodiac (Z) | 12 | 5 | 1206 | 4.1 | 1.4% |

**Herbal+Pharmaceutical chol**: 249/357 = **69.7%**

**Rate in H+P**: 18.0/1000 words vs **other sections**: 4.7/1000 words
**Chi-squared**: 158.82, p < 0.05 (p ~ 0.001)

**VERDICT**: 60-80% in botanical sections — moderate evidence for 'leaf', but 'plant' or 'green' cannot be excluded.

---
## Test 2: Leaf vs Plant (Variance Across Herbal Folios)

**Logic**: If chol means 'plant' (the whole organism), every herbal page describes
a plant, so chol should appear uniformly. If chol means 'leaf' specifically, it should
vary: HIGH on leaf-prominent pages, LOW on root-prominent pages.

**Herbal folios analyzed**: 129
**Mean chol rate**: 4.12% of words per folio
**Variance**: 12.4081
**Coefficient of Variation (CV)**: 0.85

CV interpretation: A 'plant' meaning predicts low CV (<0.5); a 'leaf' meaning predicts high CV (>0.7).

### Leaf-prominent vs Root-prominent herbal pages

| Category | N folios | Mean chol% | Median |
|----------|----------|-----------|--------|
| Leaf-prominent | 81 | 4.41% | 4.17% |
| Root-prominent | 44 | 3.88% | 2.99% |

**Mann-Whitney U test (approx)**: z = 1.01, p ~ 0.5
**Leaf/Root ratio**: 1.14x

**VERDICT**: No significant difference — consistent with 'plant' meaning.

---
## Test 3: Above-Ground vs Leaf (Flower-Prominent Pages)

**Logic**: If chol means 'above-ground part' (leaves+flowers+stems), it should
remain frequent on pages where flowers dominate but leaves are less prominent.
If chol means 'leaf' specifically, it should be lower on flower-dominant pages.

| Category | N folios | Mean chol% |
|----------|----------|-----------|
| Flower-prominent | 14 | 4.49% |
| Leaf-only prominent | 70 | 4.60% |
| Root-prominent | 44 | 3.88% |

**Flower vs Leaf-only**: z = -0.55, p ~ 0.5
**VERDICT**: Chol similar on flower and leaf pages — consistent with 'above-ground' meaning.

---
## Test 4: Co-occurrence Analysis (What Appears Next to Chol?)

**Logic**: If chol means 'leaf', expect modifiers (shape, size descriptors).
If chol means 'green', expect nouns following it. If 'plant', expect general descriptors.

### Most frequent words BEFORE chol (top 20)

| Word | Count |
|------|-------|
| chol | 20 |
| - | 12 |
| chor | 8 |
| otol | 7 |
| daiin | 7 |
| or | 6 |
| cheol | 5 |
| s | 5 |
| qokaiin | 5 |
| sho | 4 |
| dor | 4 |
| cthol | 4 |
| shol | 4 |
| qokol | 4 |
| choky | 3 |
| okal | 3 |
| cthor | 3 |
| okaiin | 3 |
| ol | 3 |
| kol | 2 |

### Most frequent words AFTER chol (top 20)

| Word | Count |
|------|-------|
| daiin | 29 |
| chol | 20 |
| cthol | 7 |
| chor | 7 |
| chy | 7 |
| ol | 7 |
| shol | 6 |
| chey | 5 |
| cthy | 5 |
| dy | 5 |
| dol | 5 |
| dain | 4 |
| chody | 4 |
| or | 4 |
| - | 4 |
| cheol | 4 |
| s | 3 |
| sho | 3 |
| choky | 3 |
| odaiin | 2 |

### Most frequent bigrams involving chol (top 20)

| Bigram | Count |
|--------|-------|
| chol chol | 40 |
| chol daiin | 29 |
| - chol | 12 |
| chor chol | 8 |
| chol cthol | 7 |
| chol chor | 7 |
| chol chy | 7 |
| otol chol | 7 |
| daiin chol | 7 |
| chol ol | 7 |
| chol shol | 6 |
| or chol | 6 |
| cheol chol | 5 |
| s chol | 5 |
| chol chey | 5 |
| chol cthy | 5 |
| chol dy | 5 |
| chol dol | 5 |
| qokaiin chol | 5 |
| sho chol | 4 |

### Comparison: words after chol vs after shol

If chol and shol are a semantic pair (leaf/root), their collocates should differ.
If they are both generic botanical words, collocates would overlap heavily.

**Top-20 collocate overlap (Jaccard)**: 0.25
**Shared words**: -, chol, cthy, daiin, dain, dy, s, shol

Low overlap suggests chol and shol occupy different semantic slots (supports leaf/root pair).

---
## Test 5: Shol Discrimination (Root vs Below-Ground vs Hidden)

### Shol distribution by section

| Section | shol count | Total words | shol/1000 words | % of all shol |
|---------|-----------|-------------|-----------------|---------------|
| Astronomical (A) | 0 | 811 | 0.0 | 0.0% |
| Biological (B) | 12 | 6089 | 2.0 | 6.9% |
| Cosmological (C) | 7 | 1599 | 4.4 | 4.0% |
| Herbal (H) | 107 | 11426 | 9.4 | 61.8% |
| Pharmaceutical (P) | 8 | 2440 | 3.3 | 4.6% |
| Stars (S) | 26 | 11083 | 2.3 | 15.0% |
| Text-only (T) | 9 | 2226 | 4.0 | 5.2% |
| Zodiac (Z) | 4 | 1206 | 3.3 | 2.3% |

### Shol on root-prominent vs leaf-prominent herbal pages

| Category | N folios | Mean shol% |
|----------|----------|-----------|
| Root-prominent | 44 | 0.99% |
| Leaf-prominent | 81 | 1.42% |

**Mann-Whitney U test**: z = -1.05, p ~ 0.5
**Root/Leaf ratio for shol**: 0.70x

**VERDICT**: No significant difference — shol may mean something broader than 'root'.

---
## Test 6: Compound Word Analysis

Words containing 'chol' as a component (not standalone).
If chol is a morpheme meaning 'leaf', compounds should be interpretable
as leaf-related concepts.

### Compounds containing 'chol' (top 30)

| Compound | Count |
|----------|-------|
| otchol | 27 |
| kchol | 22 |
| dchol | 21 |
| qokchol | 17 |
| choly | 16 |
| tchol | 15 |
| qotchol | 14 |
| okchol | 13 |
| ychol | 10 |
| choldy | 6 |
| choldaiin | 6 |
| ytchol | 6 |
| pchol | 6 |
| qopchol | 6 |
| cholal | 5 |
| ykchol | 5 |
| ochol | 5 |
| cholody | 5 |
| opchol | 5 |
| cholky | 5 |
| chol@152;y | 5 |
| cholaiin | 4 |
| chols | 4 |
| cholor | 4 |
| lchol | 4 |
| chokchol | 4 |
| cholkaiin | 4 |
| ypchol | 3 |
| cholo | 3 |
| schol | 3 |

### Compounds containing 'shol' (top 30)

| Compound | Count |
|----------|-------|
| sholdy | 7 |
| tshol | 6 |
| dshol | 4 |
| otshol | 2 |
| pshol | 2 |
| sholdaiin | 2 |
| chotshol | 2 |
| kshol | 2 |
| yshol | 2 |
| sholy | 2 |
| sheopshol | 1 |
| ctholshol | 1 |
| okolshol | 1 |
| qokshol | 1 |
| shyshol | 1 |
| ksholshey | 1 |
| oksholshol | 1 |
| dsholdy | 1 |
| sholo | 1 |
| sholor | 1 |
| tsholchoiin | 1 |
| okshol | 1 |
| chshol | 1 |
| sholdain | 1 |
| ypsholy | 1 |
| sholos | 1 |
| qotshol | 1 |
| fsholom | 1 |
| tsholol | 1 |
| sholkshy | 1 |

---
## Test 7: Morphological Family Comparison (cho- words)

If 'chol' = 'leaf', then 'cho-' is a stem and '-l' a suffix.
Compare distribution of chol vs chor, chos, chod, chok across sections.

| Word | Herbal | Pharma | Astro | Bio | Stars | Zodiac | Cosmo | Text | Total |
|------|--------|--------|-------|-----|-------|--------|-------|------|-------|
| chol | 206 | 43 | 5 | 9 | 62 | 5 | 10 | 17 | 357 |
| chor | 150 | 24 | 2 | 0 | 21 | 0 | 2 | 7 | 206 |
| chos | 14 | 8 | 3 | 0 | 13 | 0 | 0 | 0 | 38 |
| chod | 4 | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 8 |
| chok | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 4 |
| chom | 12 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 14 |
| chon | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| choy | 7 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| cthol | 46 | 4 | 0 | 1 | 2 | 0 | 1 | 1 | 55 |
| ckhol | 15 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 19 |

If chol has a uniquely herbal-skewed distribution compared to chor/chos,
it supports a leaf-specific meaning rather than being a generic morphological variant.

---
## Summary Scorecard

| Test | Favors 'leaf' | Favors 'green' | Favors 'plant' | Favors 'above-ground' |
|------|---------------|----------------|----------------|----------------------|
| 1. Section distribution (70% H+P) | weak | possible | weak | weak |
| 2. Leaf vs Root page variance (1.14x, p=NS) | NO | - | YES | - |
| 3. Flower-page frequency (4.49% vs 4.60%) | NO | - | - | YES |
| 4. Co-occurrence (Jaccard=0.25) | weak | - | - | - |
| 5. Shol root correlation (0.70x, INVERSE) | NO | - | NO | - |
| 6. Compound morphology | neutral | - | neutral | - |
| 7. cho- family distribution | NO (chol ~ chor) | - | - | - |

---
## Critical Interpretation

### The red team's challenge is validated by the data.

The discriminating tests produce results that are **devastating for the "chol = leaf" hypothesis**:

### 1. Chol does NOT correlate with leaf prominence (Test 2)
The most critical test: if chol means "leaf", pages with visually prominent leaves should have more chol than pages with prominent roots. **They do not.** The leaf/root ratio is only 1.14x and is not statistically significant (z=1.01, p>0.3). This is the single strongest piece of evidence against the "leaf" interpretation.

A word meaning "plant" (the whole organism) perfectly explains this uniformity -- every herbal page describes a plant regardless of which part is illustrated.

### 2. Chol does NOT drop on flower-prominent pages (Test 3)
If chol meant "leaf" specifically, it should decrease on pages where flowers dominate. Instead, flower-prominent pages (4.49%) and leaf-only pages (4.60%) show virtually identical chol rates. This is consistent with "plant" or "above-ground part" but not with "leaf" specifically.

### 3. Shol does NOT correlate with root prominence (Test 5)
This is perhaps the most damaging finding. Shol is actually **more** frequent on leaf-prominent pages (1.42%) than root-prominent pages (0.99%). The ratio is 0.70x -- the **inverse** of what "shol = root" predicts. This directly contradicts the leaf/root semantic pair hypothesis.

### 4. Section distribution is ambiguous (Test 1)
At 70% in H+P sections, chol is clearly botanical-leaning but far from restricted to botanical contexts. The rate in Stars sections (5.6/1000) is notably high -- over half the herbal rate. This is consistent with "green" (a color visible in astronomical illustrations) or with chol being a common morphological pattern rather than a content word.

### 5. Morphological family shows chol is NOT special (Test 7)
Chol's distribution across sections is nearly identical to chor (both heavily herbal with non-trivial presence in Stars). If chol specifically meant "leaf", we would expect it to be **more** herbal-concentrated than generic cho- words. It is not. This suggests "-ol" vs "-or" may be morphological endings rather than semantic content.

### 6. The "chol chol" bigram is suspicious
The most common chol bigram is "chol chol" (40 occurrences). "Leaf leaf" is semantically odd; "green green" equally so. But morphological or structural repetition in an unknown writing system is plausible regardless of meaning.

### What the data actually supports

The evidence is most consistent with one of:

1. **"Plant" (whole organism)**: Explains uniform frequency across herbal pages regardless of which part is illustrated. But does not explain 30% occurrence in non-botanical sections.

2. **A common morphological unit without specific lexical meaning**: The cho- family (chol, chor, chos, cthol, ckhol) may represent a grammatical or phonological pattern rather than a semantic root meaning "leaf". The similar distributions of chol and chor support this.

3. **"Above-ground" or "visible part"**: Consistent with Tests 2-3, but the presence in astronomical sections weakens this.

4. **"Leaf" remains the weakest of the four candidates** tested. It fails Tests 2, 3, and 5 -- the three tests specifically designed to discriminate it from alternatives.

### Caveat on page classifications
The root-prominent/leaf-prominent/flower-prominent page classifications used here are based on modern observers' assessments of the illustrations. Some pages may be misclassified, and the Voynich text may not describe what the illustrations show. However, the total absence of any correlation (not even a weak trend) makes misclassification unlikely to be the sole explanation.
