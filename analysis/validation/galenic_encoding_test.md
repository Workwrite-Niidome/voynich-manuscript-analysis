# Galenic Pharmaceutical Encoding Hypothesis Test

## Hypothesis

The Voynich word structure PREFIX + ROOT + SUFFIX encodes Galenic pharmaceutical properties:
- **PREFIX** encodes quality axis: ch=Hot, sh=Cold, d=Dry, s=Moist
- **ROOT** encodes substance identity (arbitrary code)
- **SUFFIX** encodes degree (1st-4th) or preparation method

This would be consistent with a Llullian combinatorial system applied to medieval pharmacy.

---

## Test 1: ch- / sh- Prefix Co-occurrence on Herbal Folios

**Prediction**: If ch=Hot and sh=Cold, both prefixes should co-occur on the same folio (Galenic descriptions always specify both hot/cold and dry/moist qualities for a plant).

### Results

Pearson correlation across 113 herbal folios:
- **ch- vs sh-: r = 0.457** (moderate positive correlation)
- d- vs s-: r = 0.168 (weak)
- ch- vs d-: r = 0.077 (negligible)

### Interpretation

The moderate positive correlation (r=0.457) means ch- and sh- words **do tend to appear together** on the same pages. This is consistent with a Galenic system where both hot/cold qualities are described for each plant.

However, this could also simply reflect that longer pages have more of every word type. The correlation is not strong enough to be conclusive.

**Verdict: WEAKLY SUPPORTIVE.** Co-occurrence is real but could be trivially explained by page length.

---

## Test 2: Four-Degree Suffix Distribution

**Prediction**: If suffixes encode Galenic degrees (1st-4th), we expect exactly 4 common suffix variants with roughly equal frequency.

### Results

Overall suffix distribution (37,165 words):

| Suffix | Count | % |
|--------|------:|----:|
| y | 14,672 | 39.5% |
| n | 5,932 | 16.0% |
| l | 5,742 | 15.5% |
| r | 5,690 | 15.3% |
| s | 1,342 | 3.6% |
| (others) | <4% each | |

n/l/r/y collectively account for **86.2%** of all word endings -- the dominance of exactly these 4 is striking.

However, the distribution is **highly non-uniform** (chi-squared = 7,395, p << 0.001):
- **-y accounts for 45.8%** of the n/l/r/y group
- **n/l/r each account for ~17-18%** -- remarkably balanced among themselves

### -y as Morphological Default

The suffix -y dominates across all prefix types:
- ch-words ending in -y: 50.2%
- sh-words ending in -y: 53.6%
- q-words ending in -y: 46.5%
- d-words ending in -y: 23.1% (lower -- d-words prefer -n instead)

This massive dominance rules out -y as "4th degree" -- no medical system would have nearly half of all quality specifications be "4th degree." Instead, **-y appears to be a morphological default or unmarked form**.

### Revised Interpretation

If we set aside -y as a default/unmarked ending, the remaining n/l/r show an almost perfectly uniform distribution (~17-18% each). This is consistent with a **three-way distinction**, not four:
- Possibly 3 degrees (mild/moderate/strong)
- Or 3 preparation methods (raw/dried/ground)
- Or 3 grammatical categories

**Verdict: PARTIALLY SUPPORTIVE.** The n/l/r uniformity is genuinely interesting and suggests a systematic three-way distinction. But -y is clearly a morphological default, not a 4th degree, which breaks the clean 4-degree mapping.

---

## Test 3: Cross-reference with Known Galenic Properties

**Prediction**: Hot plants (Paeonia, Rubia, Nigella, Laurus, Rosmarinus) should have relatively more ch- words; Cold plants (Adiantum, Vitis) should have relatively more sh- words.

### Raw Counts

| Folio | Plant | Quality | ch- | sh- | ch>sh? | Prediction |
|-------|-------|---------|----:|----:|--------|-----------|
| f1r | Laurus nobilis | Hot 2nd / Dry 1st | 28 | 33 | sh>=ch | WRONG |
| f2r | Paeonia officinalis | Hot 1st / Dry 2nd | 10 | 9 | ch>sh | OK |
| f3r | Rubia tinctorum | Hot 2nd / Dry 2nd | 25 | 7 | ch>sh | OK |
| f4r | Rosmarinus officinalis | Hot 2nd / Dry 2nd | 11 | 12 | sh>=ch | WRONG |
| f9r | Nigella damascena | Hot 3rd / Dry 1st | 15 | 5 | ch>sh | OK |
| f41r | Adiantum (maidenhair) | Cold 2nd / Dry 1st | 17 | 7 | ch>sh | WRONG |
| f47r | Vitis vinifera | Cold 1st / Moist 2nd | 27 | 8 | ch>sh | WRONG |

**Raw prediction accuracy: 3/7 (43%)** -- worse than chance (50%).

### Normalized Analysis

Since ch- is globally 2.06x more common than sh-, we must normalize. Even after normalization:

- **Average ch/sh ratio for HOT plants: 1.89**
- **Average ch/sh ratio for COLD plants: 2.90**
- **Global average: 2.06**

Cold plants actually have a **higher** ch/sh ratio than hot plants -- the **opposite** of what the hypothesis predicts.

### Individual Failures

The most damaging cases:
- **f1r (Laurus, Hot)**: sh- EXCEEDS ch- (28 vs 33). If ch=hot, the hottest herbal plant should not have more sh- words.
- **f47r (Vitis, Cold 1st)**: ch/sh ratio of 3.38 -- the highest of any identified plant. If ch=hot, the coldest plant should not have the highest ch- ratio.
- **f41r (Adiantum, Cold)**: ch/sh ratio of 2.43 -- above average despite being a cold plant.

**Verdict: REFUTED.** The prefix-quality mapping ch=Hot, sh=Cold is contradicted by the data. The identified cold plants (Vitis, Adiantum) have above-average ch- ratios, while some hot plants (Laurus, Rosmarinus) have below-average ratios.

---

## Test 4: Suffix-Degree Prediction for Specific Plants

**Prediction**: If n=1st degree, l=2nd, r=3rd, y=4th -- then the dominant suffix of ch-words on a folio should match the plant's known degree.

### Results

| Folio | Plant | Degree | Expected Suffix | Actual Top Suffix | Match? |
|-------|-------|--------|----------------|-------------------|--------|
| f1r | Laurus | 2nd | -l | **-l** | YES |
| f2r | Paeonia | 1st | -n | -y | no |
| f3r | Rubia | 2nd | -l | **-l** | YES |
| f4r | Rosmarinus | 2nd | -l | -n | no |
| f9r | Nigella | 3rd | -r | -y | no |
| f41r | Adiantum | 2nd | -l | -y | no |
| f47r | Vitis | 1st | -n | -l | no |

**Prediction accuracy: 2/7 (29%)** -- worse than the 25% baseline for random 4-way choice, though with only 7 samples this is not statistically meaningful.

The two matches (f1r Laurus -l and f3r Rubia -l) are interesting but likely coincidental given the overall failure rate.

**Verdict: NOT SUPPORTED.** Suffix-degree mapping fails in 5 of 7 cases.

---

## Test 5: Paradigmatic Root Structure (Llullian Compatibility)

**Prediction**: If words encode quality+substance+degree, the same ROOT should appear with multiple prefixes and suffixes, forming paradigmatic sets.

### Results

This test produced the **most interesting findings**:

**The root "ol"** appears with 9 different prefixes:
| Word | Count |
|------|------:|
| chol | 353 |
| shol | 165 |
| dol | 92 |
| otol | 76 |
| okol | 69 |
| sol | 55 |
| cthol | 52 |
| kol | 35 |
| qool | 5 |

**The root "ey"** appears with ch-, sh-, ok-, ot-, cth-, k-, d-, q-, and more:
- chey: 506, shey: 337, okeey: 193, cheey: 189, oteey: 155, sheey: 138...

**The root "aiin"** combines with 9 prefixes:
- daiin: 673, okaiin: 198, otaiin: 147, saiin: 117, kaiin: 72, chaiin: 45...

**43 roots** appear with both ch- and sh- prefixes AND 3+ of the n/l/r/y suffixes.

### Distribution Pattern

The root "chol" appears on **144 folios** -- it is not substance-specific but appears everywhere. If roots encoded substance identity, we would expect each root to cluster on specific folios.

Top folios for "chol": f56v(10), f47r(9), f1r(8) -- widespread.
Top folios for "shol": f42r(12), f4r(4), f44v(4) -- also widespread.

### Interpretation

The paradigmatic structure is real and strong. Voynichese demonstrably uses a system where the same "root" combines with different prefixes and suffixes. This is consistent with:
1. A combinatorial/agglutinative system (Llullian or otherwise)
2. A natural language with regular morphology
3. An encoding system where positions carry different information

However, the fact that common "roots" like "ol" and "ey" appear on virtually every folio **argues against** them encoding specific substances. If "ol" meant a specific plant, it would not appear on 144 different folios.

**Verdict: SUPPORTS combinatorial structure, but AGAINST substance-specific root encoding.**

---

## Recipe Section Comparison

### Prefix Distribution Differences

| Prefix | Herbal | Recipe | Astro |
|--------|-------:|-------:|------:|
| ch- | 19.3% | 16.4% | 16.2% |
| sh- | 8.4% | 7.0% | 5.9% |
| d- | 13.2% | 4.8% | 7.6% |
| o- | 17.0% | 22.7% | 38.6% |
| q- | 9.3% | 16.5% | 2.6% |
| cth- | 3.4% | 0.4% | 0.4% |

Notable: **d- drops dramatically in recipes (13.2% -> 4.8%)** while **q- nearly doubles (9.3% -> 16.5%)**. If prefixes encoded qualities, we would expect similar distributions across sections (all substances have qualities). The dramatic shifts suggest prefixes are more likely tied to topic or syntax than to universal pharmaceutical categories.

### Suffix Distribution (n/l/r/y)

Nearly identical across sections -- the 3-way uniformity of n/l/r holds everywhere:

| Suffix | Herbal | Recipe |
|--------|-------:|-------:|
| n | 20.2% | 21.5% |
| l | 17.0% | 17.1% |
| r | 20.8% | 17.0% |
| y | 42.1% | 44.4% |

The consistency of suffix ratios across sections is interesting but works against the degree hypothesis: if recipe sections specified degrees more precisely, we would expect different distributions.

**Verdict: AGAINST Galenic prefix encoding.** The strong section-dependent prefix variation is inconsistent with prefixes encoding universal pharmaceutical qualities.

---

## Overall Assessment

### What WORKS about the hypothesis:

1. **Paradigmatic structure is real.** Voynichese genuinely has a combinatorial system where roots combine with different prefixes and suffixes. This is the strongest finding.

2. **The n/l/r uniformity is genuinely interesting.** Three suffixes at ~17-18% each suggests a systematic three-way distinction -- not random.

3. **The ch/sh co-occurrence** on herbal pages is weakly consistent with describing multiple qualities per plant.

### What FAILS:

1. **The specific mapping ch=Hot, sh=Cold is refuted.** Cold plants (Vitis, Adiantum) have higher ch/sh ratios than some hot plants. The prediction accuracy (43%) is below chance.

2. **The suffix-degree mapping fails.** Only 2/7 predictions match, and -y is clearly a morphological default (50% of ch-words end in -y), not "4th degree."

3. **Roots are not substance-specific.** Common roots appear on 100+ folios, making it impossible for them to encode specific plant identities.

4. **Prefix distributions vary by section type.** If prefixes encoded universal qualities, they should maintain similar ratios across herbal, recipe, and astronomical sections. They do not.

### Revised Conclusion

The Voynich script's word structure is genuinely combinatorial and agglutinative, consistent with a Llullian-inspired system. However, the specific mapping to Galenic pharmaceutical categories (hot/cold/dry/moist x 4 degrees) does not hold. The combinatorial structure likely encodes something else -- possibly:

- **Grammatical categories** (noun/verb/adjective + case/tense/number)
- **Phonological units** (syllable onset + nucleus + coda in a constructed phonology)
- **A different classification system** (not Galenic qualities but perhaps astrological, elemental, or alchemical categories)
- **Cipher artifacts** (the regularity is a property of the encoding method, not the underlying content)

The Llullian combinatorial hypothesis remains viable at the structural level, but the Galenic pharmaceutical interpretation of the specific slots is not supported by the data.

---

## Data Files

- Analysis scripts: `galenic_test.py`, `galenic_test2.py`, `galenic_test3.py`
- Source transcription: `RF1b-e.txt`
- Plant identifications: `plant_identification.md`
