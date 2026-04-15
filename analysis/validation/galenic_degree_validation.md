# Galenic Degree Encoding Validation: -n = 1st, -m = 2nd, -d = 3rd

## Hypothesis Under Test

Word-final consonants in Voynichese encode Galenic degrees of elemental quality:
- **-n** = 1st degree (mild)
- **-m** = 2nd degree (moderate)
- **-d** = 3rd degree (strong)

This was observed on 5 initial plant pages and is now subjected to rigorous validation across the full corpus.

---

## Test 1: Extended Plant Sample (14 Identified Plants)

For every herbal folio where a plant identification has been attempted, we looked up the plant's Galenic degree in Dioscorides/Galen and counted -n, -m, -d endings.

### Galenic Degrees from Classical Sources

| Folio | Plant | Primary Quality | Degree | Expected Ending |
|-------|-------|----------------|--------|-----------------|
| f1r | Laurus nobilis | Hot | 2nd | -m |
| f2r | Paeonia officinalis | Hot | 1st | -n |
| f2v | Cyclamen | Hot | 3rd | -d |
| f3r | Rubia tinctorum | Hot | 2nd | -m |
| f3v | Cynara scolymus | Hot | 2nd | -m |
| f4r | Rosmarinus officinalis | Hot | 2nd | -m |
| f5r | Aristolochia rotunda | Hot | 3rd | -d |
| f8v | Hypericum perforatum | Hot | 2nd | -m |
| f9r | Nigella damascena | Hot | 3rd | -d |
| f9v | Mandragora officinarum | Cold | 3rd | -d |
| f41r | Adiantum capillus-veneris | Cold | 2nd | -m |
| f42r | Daucus carota | Hot | 2nd | -m |
| f43r | Rubia tinctorum (cult.) | Hot | 2nd | -m |
| f47r | Vitis vinifera | Cold | 1st | -n |

### Raw Results

| Folio | Plant | Deg | -n | -m | -d | Dominant | Match? |
|-------|-------|-----|---:|---:|---:|----------|--------|
| f1r | Laurus | 2nd | 50 | 1 | 4 | **n** | NO |
| f2r | Paeonia | 1st | 22 | 0 | 0 | **n** | YES |
| f2v | Cyclamen | 3rd | 11 | 0 | 0 | **n** | NO |
| f3r | Rubia | 2nd | 7 | 21 | 0 | **m** | YES |
| f3v | Cynara | 2nd | 6 | 12 | 0 | **m** | YES |
| f4r | Rosmarinus | 2nd | 19 | 2 | 0 | **n** | NO |
| f5r | Aristolochia | 3rd | 10 | 0 | 0 | **n** | NO |
| f8v | Hypericum | 2nd | 25 | 2 | 1 | **n** | NO |
| f9r | Nigella | 3rd | 16 | 1 | 3 | **n** | NO |
| f9v | Mandragora | 3rd | 16 | 1 | 0 | **n** | NO |
| f41r | Adiantum | 2nd | 2 | 0 | 5 | **d** | NO |
| f42r | Daucus | 2nd | 31 | 3 | 0 | **n** | NO |
| f43r | Rubia (cult.) | 2nd | 15 | 5 | 3 | **n** | NO |
| f47r | Vitis | 1st | 15 | 2 | 2 | **n** | YES |

**Prediction accuracy: 4/14 (29%) -- BELOW chance level (33%)**

The p-value (binomial, one-sided) is 0.50, meaning this result is exactly what random chance would produce. There is zero statistical evidence that the hypothesis outperforms guessing.

### Critical Observation

The dominant ending is -n on 10 of 14 pages, regardless of the plant's actual Galenic degree. This is because -n accounts for 78.7% of all n+m+d endings globally. The hypothesis is confounded by the overwhelming baseline frequency of -n.

### Normalized Deviation Analysis

Even after normalizing for global baseline frequencies, only 6/14 folios show positive deviation for the expected ending -- not significantly above the 4.7 expected by chance.

The two folios that most strongly support the hypothesis are:
- **f3r (Rubia, 2nd degree)**: -m deviates +0.621 above baseline -- a massive signal
- **f3v (Cynara, 2nd degree)**: -m deviates +0.538 above baseline

These two folios are ADJACENT (f3r and f3v). This clustering raises the question of whether the -m enrichment is a property of these specific folios rather than a degree-encoding system.

---

## Test 2: Control Test (Recipe vs. Herbal Pages)

If -n/-m/-d encode Galenic degrees, the distribution should differ between herbal pages (where degrees are discussed) and recipe pages (where they are not primary).

### Results

| Section | Folios | -n | -m | -d |
|---------|-------:|---:|---:|---:|
| Herbal (f1-f57) | 112 | 79.0% | 13.9% | 7.2% |
| Recipe (f99-f116) | 34 | 79.7% | 11.1% | 9.2% |
| Astro (f67-f86) | 52 | 79.5% | 11.7% | 8.7% |

Chi-squared (herbal vs. recipe): 13.09 (df=2, p < 0.01) -- the difference is statistically significant.

### Interpretation

The herbal section does show a slightly higher -m proportion (13.9% vs. 11.1%) compared to recipes. This is mildly consistent with the hypothesis. However:

1. The -n proportion is virtually identical across all sections (~79%). If -n encoded "1st degree," it should be far more concentrated in herbal pages.
2. The -m enrichment in the herbal section is small (2.8 percentage points) and could reflect topic-related vocabulary differences unrelated to Galenic degrees.
3. The -d proportion is actually LOWER in herbal (7.2%) than in recipe (9.2%), the opposite of what we would expect if herbal pages discussed 3rd-degree plants.

**Verdict: WEAKLY SUPPORTIVE at best.** The herbal-recipe difference is real but small and inconsistent across all three endings.

---

## Test 3: Stem Alternation

If -n/-m/-d encode degrees, the same stem should appear with -n on 1st-degree pages, -m on 2nd-degree pages, and -d on 3rd-degree pages.

### Results

Only **5 stems** appear with all three endings (-n, -m, -d) at 10+ total occurrences:

| Stem | stem+n | stem+m | stem+d |
|------|-------:|-------:|-------:|
| dai- | 152 | 7 | 2 |
| cha- | 9 | 24 | 1 |
| oka- | 5 | 23 | 1 |
| cho- | 1 | 15 | 9 |
| chea- | 2 | 7 | 1 |

### Degree-Match Check

For each stem, we checked whether the -m form clusters on 2nd-degree plant pages:

- **dai-**: -n on 1st-degree folios: 2.6% (no clustering). -m on 2nd-degree folios: 0.0%. -d on 3rd-degree folios: 0.0%.
- **cha-**: -m on 2nd-degree folios: 20.8% (5/24). This is roughly proportional to how many of all herbal pages are identified 2nd-degree pages (~8 of ~112), so this is about 2.5x enrichment. Mildly interesting but not conclusive.
- **cho-**: -m on 2nd-degree folios: 33.3% (5/15). 2 of these are on f3r, which already shows anomalous -m enrichment.

### Key Finding

The stem **dai-** is by far the most productive, and it is overwhelmingly locked to -n (94.4%). The -m and -d forms are extremely rare. This pattern is identical to what was found in sandhi analysis: stems ending in -aii- are morphologically locked to -n. This is a MORPHOLOGICAL property of the stem, not a degree marker.

**Verdict: NOT SUPPORTED.** Stem alternation exists but does not correlate with plant degree. The rare stems showing some degree correlation (cha-, cho-) are heavily influenced by f3r/f3v.

---

## Test 4: The 4th Degree Problem

The Galenic system fundamentally uses 4 degrees. This hypothesis only covers 3 (-n/-m/-d). What encodes 4th degree?

### Analysis

No plants in our identified sample are classified as 4th degree (Euphorbia, Cantharides, etc. are not identified in the manuscript). The test is therefore inconclusive.

Possible 4th-degree encodings:
- **-s**: 1,053 occurrences (2.9%) -- plausible frequency
- **-g**: 137 occurrences (0.4%) -- too rare
- **-l, -r, -y**: Already assigned other functions (sandhi/morphological)

### Structural Problem

Some medieval herbals did simplify to 3 degrees, particularly in the Salernitan tradition. However, the major reference works (Galen, Dioscorides, Avicenna) all use 4 degrees. A system encoding only 3 would be unusual but not impossible.

**Verdict: INCONCLUSIVE but a structural weakness.**

---

## Test 5: Interaction with Sandhi

### The Contradiction

Previous analysis established that -n is a sandhi variant:
- -n appears before fricatives (s, c, f) and at phrase boundaries
- -l appears before stops (k, t, d)
- -r appears before vowels (a, i, o)

The degree hypothesis claims -n = 1st degree. These are potentially contradictory: -n cannot simultaneously be determined by the following word's phonology AND by the plant's Galenic degree.

### Resolution Attempt

We tested whether -m (the proposed 2nd-degree marker) shows sandhi-like behavior. If -m is purely a degree marker, its proportion should be constant regardless of the following word's initial.

**Result: -m varies from 6.1% to 35.4% depending on the following word's initial.**

| Following initial | -n% | -m% | -d% |
|-------------------|-----|-----|-----|
| Before c- | 88.2% | 6.1% | 5.7% |
| Before a- | 82.2% | 6.7% | 11.1% |
| Before t- | 57.7% | **35.4%** | 6.9% |
| Before y- | 63.0% | **28.0%** | 9.0% |
| Before p- | 69.2% | **27.9%** | 2.9% |
| Before d- | 71.0% | **22.6%** | 6.5% |

**-m shows a 5.8x variation ratio** across phonological contexts. This is far too large for a degree marker. It means -m behaves more like a sandhi variant than a semantic marker.

### Critical Finding: -m is Conditioned by Following Word

-m is strongly elevated before t-, y-, p-, and d-initial words. This pattern is consistent with -m being a phonological variant triggered by specific following environments, NOT a degree marker.

This is the single most damaging finding for the hypothesis: if -m were encoding "2nd degree," its frequency should depend on the plant being described, not on what word happens to come next.

### Degree-Grouped Analysis

| Plant degree | -n% | -m% | -d% |
|-------------|-----|-----|-----|
| 1st degree (2 folios) | 90.2% | 4.9% | 4.9% |
| 2nd degree (8 folios) | 72.4% | 21.5% | 6.1% |
| 3rd degree (4 folios) | 91.4% | 3.4% | 5.2% |

The 2nd-degree folios do show elevated -m (21.5% vs. 4.9% and 3.4%). However, this is driven almost entirely by f3r and f3v. Removing those two folios would collapse the effect.

**Verdict: REFUTED.** The -m ending is conditioned by phonological context (following word initial), not by semantic content (plant degree). The degree-grouped analysis showing elevated -m on 2nd-degree pages is an artifact of f3r/f3v's anomalous -m density, not a systematic encoding.

---

## Test 6: Red Team -- Alternative Explanations

### 6a: Scribe Variation

Chi-squared between Currier A (f1-f57) and Currier B (f75+): **14.71 (p < 0.01)**.

The two scribes show significantly different n/m/d distributions:
- Currier A: n=79.0%, m=13.9%, d=7.2%
- Currier B: n=80.3%, m=11.0%, d=8.7%

Scribe variation can explain some of the page-to-page variation in -m frequency without invoking degree encoding.

### 6b: Section Variation

Within the herbal section itself:
- Herbal A (f1-f25): m=13.7%
- Herbal B (f26-f57): m=14.0%

No significant subsection variation. The -m enrichment on f3r/f3v is a localized anomaly, not a section-wide trend.

### 6c: Random Fluctuation

With 14 data points at 29% accuracy (below the 33% chance level), the result is fully consistent with random chance (p = 0.50). We cannot reject the null hypothesis.

### 6d: -m as a Morphological Ending

Analysis of -m word structure:
- **74.4% of -m words end in -am** (dam, cham, qokam, otam, sam, etc.)
- **16.2% end in -om** (chom, om, etc.)
- **6.6% end in -im** (daim, etc.)

The overwhelming dominance of -am suggests that -m is part of a specific morphological pattern (likely the vowel sequence -a- + -m), not a productive degree suffix. The -am ending may encode a specific grammatical function (e.g., accusative case, a specific tense, or a noun class marker) rather than "2nd degree."

### 6e: The f3r Anomaly

f3r (Rubia tinctorum) has the highest -m proportion of any herbal folio at 75.0%. The f3v page (immediately following) has the second highest at 66.7%. These two adjacent pages account for a disproportionate share of the evidence supporting the hypothesis.

Possible explanations for f3r/f3v's -m enrichment:
1. **Coincidence**: With 112 herbal folios, some will have extreme -m values by chance (CV = 1.27, meaning high variance)
2. **Scribe behavior**: These folios may represent a passage where the scribe used a specific construction or formula rich in -am/-om words
3. **Text content**: The content of these pages may involve vocabulary that happens to end in -m for linguistic reasons unrelated to Galenic degrees
4. **The hypothesis is partially correct for these specific pages**: It is possible that f3r/f3v discuss the degree of Rubia/Cynara and use a degree marker, but this would be a local phenomenon, not a manuscript-wide encoding system

---

## Statistical Significance

### Summary of Statistical Tests

| Test | Result | Significance |
|------|--------|-------------|
| Prediction accuracy (dominant ending) | 4/14 = 29% | p = 0.50 (NOT significant, below chance) |
| Herbal vs. recipe -m proportion | 13.9% vs. 11.1% | chi2 = 13.09, p < 0.01 (significant but small effect) |
| -m conditioned by following word | 5.8x variation | Strongly significant (chi2 >> critical) |
| Scribe A vs. B difference | 13.9% vs. 11.0% | chi2 = 14.71, p < 0.01 (significant) |
| Stem-degree clustering | Near zero | NOT significant |

### Effect Size Analysis

Even where differences are statistically significant (herbal vs. recipe), the effect size is very small:
- Herbal -m proportion: 13.9%
- Recipe -m proportion: 11.1%
- Difference: 2.8 percentage points
- Cohen's h: ~0.09 (negligible effect size)

For comparison, the sandhi effect on -m is enormous: from 6.1% before c-initial words to 35.4% before t-initial words -- a 29.3 percentage point swing. The phonological conditioning is **10x stronger** than any section-level effect.

---

## Final Verdict

### The hypothesis (-n = 1st, -m = 2nd, -d = 3rd degree) is **NOT SUPPORTED**.

**Reasons:**

1. **Prediction accuracy is below chance (29% vs. 33%).** The dominant ending fails to match the expected degree in 10 of 14 cases, primarily because -n dominates on nearly every page regardless of plant degree.

2. **-n is not a degree marker.** -n accounts for 78.7% of all n+m+d endings. Its dominance is fully explained by its established roles as (a) a sandhi variant before fricatives, and (b) a phrase-boundary marker. No additional "degree" function is needed to explain its distribution.

3. **-m is phonologically conditioned.** -m varies 5.8x across following-word contexts, proving it is sensitive to phonological environment. A degree marker should be invariant to phonological context.

4. **The supporting evidence is concentrated on 2 adjacent folios (f3r/f3v).** Remove these two pages and the hypothesis has zero support. This is a classic overfitting pattern: the hypothesis was likely discovered on these pages and then fails to generalize.

5. **-d is too rare (1.8% of words) to encode "3rd degree."** Many plants in medieval pharmacopeia are classified as 3rd degree. If -d encoded this, it should appear far more frequently.

6. **The 4th degree is missing.** No convincing encoding for 4th degree has been identified, creating a structural gap in the hypothesis.

### What f3r/f3v Actually Shows

The anomalous -m enrichment on f3r (Rubia) and f3v (Cynara) is real and striking. However, the most parsimonious explanation is:

- These pages use specific vocabulary/formulae that happen to contain many -am/-om words
- The -am ending likely represents a morphological category (possibly a verb form, noun case, or grammatical construction) rather than a degree marker
- The correlation with 2nd-degree plants is coincidental, especially since f4r (Rosmarinus, also 2nd degree Hot) and f42r (Daucus, also 2nd degree Hot) show NO -m enrichment

### Relationship to n/l/r Sandhi System

The n/l/r sandhi analysis (documented in `nlr_sandhi_analysis.md`) established a three-layer system:
1. Morphological/lexical layer (stem determines default)
2. Sandhi/phonological layer (following word shifts choice)
3. Prosodic/boundary layer (-n marks closures, -r marks openings)

**-m does not fit cleanly into this system.** Unlike n/l/r, which are in complementary distribution governed by phonological rules, -m appears in specific morphological contexts (-am, -om) and may represent an entirely different grammatical category. The correct interpretation of -m likely lies in morphological analysis (what grammatical function does -am serve?) rather than in Galenic pharmacology.

---

## Data and Methods

- **Source**: RF1b-e.txt (EVA transcription, 36,009 words, 226 folios)
- **Plant identifications**: Based on illustration analysis (see `plant_identification.md`), with Galenic degrees from Dioscorides *De Materia Medica* and Galen *De Simplicium Medicamentorum*
- **Statistical tests**: Chi-squared, binomial, coefficient of variation
- **Analysis script**: `galenic_nmd_validation.py`

---

## Appendix: Comparison with Previous n/l/r/y Hypothesis

The earlier test (documented in `galenic_encoding_test.md`) tested -n=1st, -l=2nd, -r=3rd, -y=4th. That hypothesis also failed (29% accuracy). The current -n/-m/-d hypothesis performs identically poorly (29%), suggesting that neither specific mapping to Galenic degrees is supported.

The consistent finding across both tests is that **word endings in Voynichese are governed by phonological/morphological rules (sandhi, boundary marking, stem morphology), not by the Galenic properties of the plant being described.**
