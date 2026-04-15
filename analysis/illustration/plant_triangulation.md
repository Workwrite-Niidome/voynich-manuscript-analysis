# Plant Page Cross-Triangulation Analysis

## Method

Five botanically identified Voynich folios are used as a differential filter. By comparing word distributions across pages with known Galenic properties (hot/cold, dry/moist), we isolate candidate stems for property vocabulary, plant-part terminology, and degree markers.

| Folio | Plant | Temp | Moisture | Key Part | Galenic Degree |
|-------|-------|------|----------|----------|----------------|
| f2r/v | Paeonia (peony) | HOT | DRY | root | Hot 1st, Dry 2nd |
| f3r/v | Rubia (madder) | HOT | DRY | root | Hot 2nd, Dry 2nd |
| f9r/v | Nigella (black cumin) | HOT | DRY | seed | Hot 3rd, Dry 1st |
| f41r/v | Adiantum (maidenhair fern) | COLD | DRY | frond/leaf | Cold (unspec.), Dry |
| f47r/v | Vitis (grape vine) | COLD | MOIST | leaf/fruit | Cold 1st, Moist 2nd |

---

## 1. Page Statistics

| Page | Plant | Total words | Unique words |
|------|-------|-------------|--------------|
| f2 | Paeonia | 156 | 115 |
| f3 | Rubia | 195 | 149 |
| f9 | Nigella | 163 | 125 |
| f41 | Adiantum | 159 | 132 |
| f47 | Vitis | 161 | 104 |

**Observation**: f41 (Adiantum) has the highest unique-to-total ratio (83%), suggesting highly specialized vocabulary. f47 (Vitis) has the lowest (65%), suggesting more repetitive/formulaic text.

---

## 2. Core Vocabulary (All 5 Pages)

Only **2 words** appear on every single page:

| Word | f2 | f3 | f9 | f41 | f47 | Interpretation |
|------|----|----|----|----|-----|----------------|
| **chol** | 7 | 8 | 6 | 1 | 14 | Extremely common function word; possibly "of/the" or a core botanical term like "plant" or "herb" |
| **daiin** | 8 | 3 | 9 | 3 | 8 | Ubiquitous; possibly a grammatical particle, "is/has", or a universal descriptor |

These two words alone account for a significant fraction of all text. `chol` is the single most common word on f47 (14 occurrences). `daiin` is the most common word on f2 and f9.

---

## 3. Near-Core Vocabulary (4 of 5 Pages)

| Word | Missing from | Counts (f2/f3/f9/f41/f47) | Notes |
|------|-------------|---------------------------|-------|
| **chor** | f41 | 7/11/4/0/2 | Absent from Adiantum; very high on Rubia |
| **chy** | f41 | 4/1/3/0/8 | Absent from Adiantum |
| **cthy** | f41 | 2/3/4/0/1 | Absent from Adiantum |
| **shol** | f41 | 3/1/2/0/5 | Absent from Adiantum |
| **dain** | f41 | 1/1/1/0/4 | Absent from Adiantum |
| **dor** | f3 | 2/0/2/1/2 | Absent from Rubia |
| **dair** | f9 | 1/1/0/1/2 | Absent from Nigella |
| **chey** | f3 | 1/0/1/4/3 | Absent from Rubia; high on Adiantum |
| **aiin** | f2 | 0/1/1/1/3 | Absent from Paeonia |

**Critical finding**: Five words (chor, chy, cthy, shol, dain) are present on all pages EXCEPT f41 (Adiantum). This is striking. f41 has a radically different vocabulary profile from the other four pages. This may reflect:
- A different scribe/language variant (Currier Hand B?)
- Adiantum's unique botanical character (fern, not flowering plant)
- Different textual genre on f41

---

## 4. Hot-Only Vocabulary

Words appearing on 2+ hot pages (f2, f3, f9) but NEVER on cold pages (f41, f47):

### On all 3 hot pages (strongest "hot" candidates):
| Word | f2 | f3 | f9 | Assessment |
|------|----|----|-----|------------|
| **ckhy** | 1 | 1 | 1 | **Prime candidate for "hot" (calidus)**. Perfect 3/3 hot distribution, 0/2 cold. |
| **s** | 2 | 6 | 2 | High frequency on f3 (Rubia). Could be abbreviation/particle rather than "hot" specifically. |

### On 2 of 3 hot pages:
| Word | Pages | Assessment |
|------|-------|------------|
| **shor** | f2, f9 | Possibly "pungent" or taste descriptor |
| **cthor** | f2, f9 | Related to `cth-` stem family |
| **otchor** | f2, f3 | Related to `ot-` prefix + `chor` |
| **otchal** | f2, f3 | Related to `ot-` prefix + `chal` |
| **shodaiin** | f2, f3 | Compound: `sho` + `daiin` |
| **shaiin** | f2, f9 | Related to `sh-` stem |
| **dal** | f2, f9 | Possibly a measurement/degree term |
| **qotcho** | f2, f9 | `qo-` prefix compound |
| **ytoldy** | f2, f9 | `y-` prefix compound |

---

## 5. Cold-Only Vocabulary

Words on BOTH cold pages but NO hot pages:

| Word | f41 | f47 | Assessment |
|------|-----|-----|------------|
| **oteey** | 1 | 1 | **Only candidate for "cold" (frigidus)**. Unique cold-only distribution. |

The extremely small cold-only vocabulary (just 1 word) suggests either:
- Cold pages share very little specialized vocabulary with each other
- f41 is so lexically divergent that overlap with f47 is minimal
- The "cold" property may be encoded differently (morphologically, not lexically)

---

## 6. Root Vocabulary

Words on BOTH root-prominent pages (f2 Paeonia + f3 Rubia) but NOT on leaf pages (f41 + f47):

| Word | f2 | f3 | Also on f9? | Assessment |
|------|----|----|-------------|------------|
| **cheol** | 1 | 1 | No | Root-exclusive. Candidate for "root" (radix) |
| **chodaiin** | 1 | 1 | No | Root-exclusive. Compound form |
| **otchal** | 1 | 1 | No | Root-exclusive. `ot-` prefix |
| **otchor** | 1 | 1 | No | Root-exclusive. `ot-` prefix |
| **shodaiin** | 1 | 1 | No | Root-exclusive. `sho-` prefix |
| **ckhy** | 1 | 1 | Yes | Also on f9 = hot, not root-specific |
| **s** | 2 | 6 | Yes | Also on f9 = hot, not root-specific |

**Best candidates for "root"**: `cheol`, `chodaiin`, `otchal`, `otchor`. These appear exclusively on Paeonia and Rubia (both described by Dioscorides as having prominent, medicinally important roots) and nowhere else.

Note that `cheol` looks morphologically like `che` + `ol`, while `otchal` = `ot` + `chal` and `otchor` = `ot` + `chor`. The `ot-` prefix may indicate a plant part or preparation method.

---

## 7. Seed/Nigella-Specific Vocabulary

Words appearing ONLY on f9 (Nigella, the seed-medicine plant): **79 unique words**.

High-interest candidates (appearing 2+ times on f9):

| Word | Count | Assessment |
|------|-------|------------|
| **cthod** | 2 | `cth-` stem + `-od` ending. Nigella-exclusive. |
| **chkaiin** | 2 | `chk-` stem. Nigella-exclusive. |
| **otaiin** | 2 | `ot-` prefix + `aiin`. Nigella-exclusive. |
| **oty** | 3 | Short word, 3 occurrences. Candidate for "seed" (semen) |

**oty** is the strongest single candidate for "seed" -- it appears 3 times on the seed-medicine page and nowhere else among the 5 target pages. Its short length is consistent with being a basic botanical term.

---

## 8. Plant-Specific Hapax Analysis

Words unique to exactly one page (potential plant names or unique descriptors):

| Page | Plant | Unique words | Notable patterns |
|------|-------|-------------|-----------------|
| f2 | Paeonia | 65 | `-an` ending cluster: dan(4), chan(2), an(2), shan -- ONLY page with `-an` words |
| f3 | Rubia | 106 | `-om`/`-am` endings dominant: cham(4), chom(4), okom, soeom, okeom |
| f9 | Nigella | 79 | `cthod` type compounds; many `ot-` prefix words |
| f41 | Adiantum | 99 | `-edy`/`-eey` endings dominate: qokedy(7), okedy(4), chekedy(2) |
| f47 | Vitis | 55 | `cho-` compounds: chokchol, cholsho, chotcho, chokolg |

---

## 9. Morphological Ending Distribution

Percentage of words on each page ending with given suffix:

### Endings strongly skewed toward HOT pages:

| Ending | f2 | f3 | f9 | f41 | f47 | Pattern |
|--------|----|----|-----|-----|-----|---------|
| **-or** | 13.5% | 16.9% | 13.5% | **1.3%** | 6.2% | Hot pages 13-17%; cold pages 1-6% |
| **-chor** | 7.1% | 9.7% | 4.9% | **0.0%** | 2.5% | Absent from f41, low on f47 |
| **-om** | 0.0% | **8.2%** | 0.0% | 0.0% | 0.0% | EXCLUSIVE to f3 (Rubia) |
| **-an** | **6.4%** | 0.0% | 0.0% | 0.0% | 0.0% | EXCLUSIVE to f2 (Paeonia) |

### Endings strongly skewed toward COLD pages:

| Ending | f2 | f3 | f9 | f41 | f47 | Pattern |
|--------|----|----|-----|-----|-----|---------|
| **-dy** | 5.1% | 2.6% | 6.7% | **30.2%** | 5.6% | f41 has 6x the rate of other pages |
| **-edy** | ~0% | ~0% | ~0% | **~17%** | ~0% | Nearly exclusive to f41 |
| **-ey** | 7.1% | 3.6% | 3.7% | **21.4%** | 10.6% | High on cold pages, esp. f41 |
| **-eey** | 3.2% | 1.5% | 1.2% | **7.5%** | 4.3% | Higher on cold pages |

### Endings with notable page-specific distributions:

| Ending | Distribution | Interpretation |
|--------|-------------|----------------|
| **-am** | f3 = 8.2%, all others < 1.3% | Rubia-specific morpheme |
| **-an** | f2 = 6.4%, all others = 0% | Paeonia-specific morpheme |
| **-chy** | f47 = 9.3%, f9 = 6.1%, others lower | Possibly leaf/moist-related |
| **-ol** | Fairly even 11-16%, but f41 only 3.8% | General botanical suffix, reduced on f41 |

---

## 10. Galenic Property Distribution Matching

### Exact distribution matches:

| Expected Distribution | Matching Word(s) | Confidence |
|-----------------------|-------------------|------------|
| HOT = f2+f3+f9 only | **ckhy** (3 occ.), **s** (10 occ.) | HIGH for `ckhy`; `s` may be grammatical |
| COLD = f41+f47 only | **oteey** (2 occ.) | MEDIUM -- only 1 word matches |
| ROOT = f2+f3 only | **cheol**, **chodaiin**, **otchal**, **otchor**, **shodaiin** | MEDIUM |
| SEED = f9 only | **oty** (3 occ.), **cthod** (2 occ.), **chkaiin** (2 occ.) | MEDIUM for `oty` |
| DRY = f2+f3+f9+f41 not f47 | **(none)** | No word matches all 4 dry pages exclusively |

---

## 11. Degree Marking Analysis

If the Voynich text encodes Galenic degrees, we should find markers distinguishing:
- Hot 1st (f2) from Hot 2nd (f3) from Hot 3rd (f9)

### Words shared by f2+f3 (degrees 1-2) but NOT f9 (degree 3):
- `cheol`, `chodaiin`, `otchal`, `otchor`, `shodaiin` (root vocabulary, not degree markers)
- `sho` (also on cold pages -- general term)
- `cheor`, `dair` (also on cold pages)

### The `-an` / `-am` / `-om` ending divergence as degree encoding?

A striking pattern emerges from page-specific endings:
- f2 (Hot 1st): dominant ending **-an** (6.4%, exclusive)
- f3 (Hot 2nd): dominant endings **-am** (8.2%) and **-om** (8.2%, exclusive)
- f9 (Hot 3rd): neither -an nor -am/-om; instead **-od** endings (cthod)

This could represent a systematic encoding where the FINAL CONSONANT of certain words encodes degree or intensity:
- **-n** = 1st degree
- **-m** = 2nd degree  
- **-d** = 3rd degree (or simply a different morphological class)

Supporting evidence:
- f2 has `dan` (4x), `chan` (2x), `an` (2x), `shan` -- all ending in `-n`
- f3 has `cham` (4x), `chom` (4x), `dam`, `soeom`, `okeom` -- all ending in `-m`
- f9 has `cthod` (2x), `chcthod`, numerous `-od` forms
- The base stems `ch-`, `da-` appear across pages, only the final consonant changes

**This is the most structurally significant finding in this analysis.** If confirmed, it would mean the Voynich script uses terminal consonant alternation (-n/-m/-d) to encode Galenic degree categories.

---

## 12. Stem Family Analysis

### The `ch-` stem family (most productive):
- `chol` (core), `chor` (near-core), `chy` (near-core)
- `chal`, `cham`, `chan` -- differ only in final consonant
- Likely the most basic descriptive root in the system

### The `ot-` prefix:
- Appears in compounds: `otchor`, `otchal`, `otchol`, `otaiin`, `oty`
- Found across multiple pages
- May indicate a preparation method ("decoction of"?) or intensifier

### The `qo-` prefix:
- Very frequent on f3 (Rubia) and f41 (Adiantum)
- `qokedy` (7x on f41), `qokeey` (3x on f41), `qokchor` (f3)
- May indicate "use/application" or a modal/imperative marker ("one should...")

### The `sho-`/`sh-` prefix:
- Present on hot pages: `shor`, `shodaiin`, `shaiin`
- Less frequent on cold pages
- Possibly related to preparation or heating

### The `dai-` stem:
- `daiin` (core), `dain`, `dair`, `daiiin`, `daiidy`, `daiildy`
- Present on every page -- grammatical function or universal descriptor

---

## 13. f41 (Adiantum) Anomaly

f41 is dramatically different from all other pages:
- 5 common words (chor, chy, cthy, shol, dain) present everywhere else are ABSENT here
- The `-dy` ending is 6x more frequent than on any other page (30.2%)
- The `-edy` cluster is essentially exclusive to f41 (`qokedy` x7, `okedy` x4)
- The `qok-` prefix is disproportionately common (21 words, vs 3-11 on other pages)

Possible explanations:
1. **Different scribe (Currier B)**: f41 may be written by a different hand with different spelling conventions
2. **Different plant-part vocabulary**: Fern fronds require different descriptive terms than roots/seeds/leaves
3. **Different textual function**: f41 may contain recipe/dosage text rather than morphological description
4. The `-edy` cluster might encode the concept of "frond" or "delicate" (Adiantum = "unwetted")

---

## 14. Summary of Stem Candidates

| Concept | Best Candidate(s) | Evidence Strength | Rationale |
|---------|-------------------|-------------------|-----------|
| **"Hot" (calidus)** | `ckhy` | STRONG | Perfect 3/3 hot, 0/2 cold distribution |
| **"Cold" (frigidus)** | `oteey` | WEAK | Only word matching, but only 2 occurrences |
| **"Root" (radix)** | `cheol` or `otchal` | MEDIUM | Exclusive to root-prominent pages f2+f3 |
| **"Seed" (semen)** | `oty` | MEDIUM | 3x on seed page f9, nowhere else among 5 targets |
| **Degree 1st** | `-n` terminal | SPECULATIVE | Exclusive to f2 (Hot 1st) in `-an`/`-dan` forms |
| **Degree 2nd** | `-m` terminal | SPECULATIVE | Exclusive to f3 (Hot 2nd) in `-am`/`-om` forms |
| **Degree 3rd** | `-d` terminal | SPECULATIVE | Concentrated on f9 (Hot 3rd) in `-od` forms |
| **Plant/herb** | `chol` | STRONG | Universal (5/5 pages), highest frequency |
| **Grammatical particle** | `daiin` | STRONG | Universal (5/5 pages), extremely frequent |
| **"Leaf"/"frond"** | `-edy` cluster | WEAK | Nearly exclusive to f41 (fern), but could be scribe variation |

---

## 15. Next Steps

1. **Validate `ckhy` = "hot"**: Check if `ckhy` appears on other hot-plant pages beyond these 5 (e.g., Capsicum, Zingiber equivalents). If it consistently appears on hot plants and is absent from cold ones, confidence increases substantially.

2. **Validate `-n/-m/-d` degree encoding**: Examine f4r-f8v (other identified plants with known Galenic degrees). If `-an` endings correlate with 1st degree and `-am` with 2nd degree across more pages, this would be a breakthrough.

3. **Resolve the f41 anomaly**: Compare f41's vocabulary with other pages identified as Currier Language B. If the divergence is scribal rather than semantic, the f41 data should be analyzed separately.

4. **Extend to 3-page and 4-page distributions**: Many words appear on exactly 3 pages. Cross-referencing with additional identified plants could disambiguate property terms from plant-specific vocabulary.

5. **Test `oty` = "seed"**: Check if `oty` appears on other seed-prominent plant pages (e.g., Coriandrum, Cuminum).

6. **Structural grammar**: The `qo-` prefix is extremely productive. Testing whether it functions as a modal/imperative ("take...", "use...") by examining its positional distribution (line-initial vs. medial) could crack the grammar.

---

## Appendix A: Complete Word Lists

### f2 (Paeonia) - Top words
daiin(8), chor(7), chol(7), chy(4), dan(4), saiin(3), shol(3), sho(3), s(2), shor(2), cthy(2), cthey(2), sheey(2), keol(2), an(2), chan(2), chcthy(2), dor(2)

### f3 (Rubia) - Top words
chor(11), chol(8), s(6), cham(4), chom(4), daiin(3), cthy(3), or(3), ol(3), tchor(3), cthol(2), ycheor(2), sho(2), y(2), dar(2), qokeey(2), shar(2), cheor(2)

### f9 (Nigella) - Top words
daiin(9), chol(6), cthy(4), dy(4), chor(4), cthor(3), or(3), oty(3), chy(3), s(2), shor(2), otaiin(2), cthod(2), dor(2), shol(2), choy(2), chkaiin(2)

### f41 (Adiantum) - Top words
qokedy(7), chey(4), okedy(4), qokeey(3), daiin(3), y(2), ypchedy(2), yteedy(2), shedy(2), qokeoy(2), ykey(2), qokal(2), chekedy(2), ykeey(2), okey(2), okeey(2)

### f47 (Vitis) - Top words
chol(14), daiin(8), chy(8), shol(5), dain(4), chdy(3), aiin(3), chaiin(3), chey(3), sho(3), shy(3), dair(2), dor(2), chor(2), keey(2), sy(2), cphy(2), cheor(2), sal(2), sary(2)
