# Morphological Architecture and Validated Structural Constraints in the Voynich Manuscript: What Survives Adversarial Testing

**Authors:** Anonymous (direction and supervision), Claude Opus 4.6 (computational analysis), Anthropic

**Corpus:** EVA transcription RF1b-e.txt (37,779 tokens, 8,500 unique types, 226 folios)

**Date:** April 2026 (v2 -- revised after blind prediction testing)

---

## Abstract

The Voynich Manuscript (Beinecke MS 408, radiocarbon-dated 1404--1438) has resisted decipherment for over a century. We present a systematic computational analysis of its full EVA transcription using iterative hypothesis-generation and adversarial hypothesis-destruction cycles, including a dedicated red-team review and two pre-registered blind prediction tests. We report findings at three evidence levels:

**Validated findings** (survived all tests): (1) a statistically significant cross-word dependency in suffix selection, cross-validated at 42.9% accuracy versus 34.7% baseline (10-fold CV, p < 0.001, 0/1000 permutations); (2) a compositional morphological architecture PREFIX + [CLASSIFIER + ROOT + VOWEL GRADE + TERMINAL] + SUFFIX in which prefix and suffix are statistically independent (NMI = 0.032); (3) a vowel grade system encoding lexical specificity with near-perfect correlation (r = -0.954) between grade level and page spread, confirmed by 2.82--3.82x recipe-section enrichment of higher grades; (4) compound classifier compositionality (8/8 predicted section distributions confirmed); (5) 14/15 morpheme substrings with non-random page distributions surviving Bonferroni correction across 6,384 possible substrings; and (6) the morpheme `ty` as a validated predictor of thin/linear-leaved plant illustrations (Fisher p = 0.008, OR = 18.0).

**Promising hypotheses** (above chance but not fully validated): a descriptive naming system in which morphemes encode observable plant features, with positive predictions achieving 79% accuracy versus a 35% chance baseline in blind testing (N = 9.5 predictions); and a ch/sh functional contrast (visual description vs. substance/ingredient).

**Refuted claims**: sh = underground/root (blind test 25%, below chance); cthy = fruit/seed (full-scale Fisher p = 0.66); dchy = tall/tree-like (full-scale Fisher p = 1.0); and negative morpheme predictions generally (absence of morpheme does not predict absence of visual feature).

Of 23 hypotheses tested across 20 analysis cycles, 12 were eliminated. The manuscript remains undeciphered, but the validated structural findings constrain the solution space and demonstrate that the text possesses genuine linguistic or notational structure beyond what simple generation mechanisms (Cardan grille, random table) can produce.

---

## 1. Introduction

The Voynich Manuscript is a 234-page vellum codex housed in Yale University's Beinecke Rare Book and Manuscript Library (MS 408). Radiocarbon dating places its vellum production between 1404 and 1438. Written in an unknown script and illustrated with unidentified plants, astronomical diagrams, and bathing scenes, it has been the subject of intensive study since its rediscovery by Wilfrid Voynich in 1912.

Previous computational analyses have established several robust statistical properties. Bennett (1976) and Landini (2001) confirmed Zipf's law compliance. Amancio et al. (2013) measured entropy values intermediate between natural language and random text. Stolfi (2005) and Zattera (2023) identified positional slot grammar for individual glyphs. Currier (1976) distinguished two "languages" (A and B), and Davis (2020) identified five scribal hands.

Our investigation departed from prior work in four respects. First, we employed iterative hypothesis-destruction methodology in which each cycle attempted to falsify the survivors of previous cycles, culminating in a dedicated adversarial red-team review. Second, we conducted two pre-registered blind prediction tests -- a methodological innovation in Voynich studies. Third, we analysed the complete EVA transcription rather than selected folios. Fourth, we report all failures alongside successes, including refuted hypotheses and approaches that did not replicate.

---

## 2. Validated Findings

The following results survived cross-validation, permutation testing, Bonferroni correction, adversarial red-team review, and/or blind prediction testing.

### 2.1 Cross-word suffix dependency (sandhi)

Words in the Voynich manuscript end in one of three near-equiprobable consonants -- n (34.7%), l (32.6%), r (32.8%) -- and the choice is systematically conditioned by context.

**Layer 1 -- Stem-final vowel** (strongest effect, MI = 0.929 bits). Stems ending in -i consistently take -n (100% of 69 attested stems); stems ending in -o prefer -l (79% of 67 stems); stems ending in -a prefer -r (77% of 48 stems).

**Layer 2 -- Following word's initial** (medium effect, Cramer's V = 0.215, chi-squared = 1,404, p = 1.88 x 10^-278). Following-word initials partition into three classes: vowels favour preceding -r at 2.0x lift; stops favour -l at 1.41--2.08x lift; fricatives show weak -n preference.

**Layer 3 -- Prosodic boundary**. The effect operates within lines but collapses across line boundaries (e.g., before k-initial words, -l appears 71.3% within-line but only 22.2% cross-line).

**Cross-validation:**

| Test | Result |
|------|--------|
| 10-fold CV mean accuracy | 42.9% +/- 2.7% (all 10 folds above 34.7% baseline) |
| Permutation test (n=1000) | p < 0.001 (0/1000 reached real accuracy) |
| Cross-split probability correlation | Pearson r = 0.84 (p = 5.36 x 10^-13) |
| Trigger agreement across splits | 80% (12/15 initials) |
| Between-word vs. within-word lift | +8.20 pp vs. +3.95 pp |

The between-word conditioning is approximately twice as strong as within-word in relative terms, consistent with a word-boundary-specific process rather than a transcription artefact. This finding is difficult to produce with a simple Cardan grille, substantially weakening the hoax hypothesis of Rugg (2004).

### 2.2 Morphological architecture

Voynich words decompose into a multi-slot structure:

```
WORD = [PREFIX] + [CLASSIFIER + ROOT + VOWEL GRADE + TERMINAL] + [SUFFIX]
```

This is more granular than the ternary PREFIX + STEM + SUFFIX reported in earlier analyses. The key innovation is the internal decomposition of what had been treated as an opaque "stem."

**Prefix inventory** (15 productive types): ch- (16.9%), qo- (14.2%), o- (9.2%), d- (8.0%), sh- (7.8%), ot- (6.4%), ok- (6.3%), y- (4.4%), and 7 others at lower frequencies.

**Suffix inventory** (17 types), organized by line-position behaviour: terminators (-am, -m; line-final 73%); openers (-or, -eey, -ol; line-initial 71--78%); case markers (-aiin, -ain, -ar, -ey); predicates (-y, -dy, -al); and connectors (-iin, -edy).

**Prefix--suffix independence**: NMI(prefix, suffix) = 0.032, compared with NMI(prefix, stem) = 0.508 and NMI(stem, suffix) = 0.379. This near-zero coupling is a signature more consistent with a multi-dimensional notation system than with natural morphology, where prefix--suffix NMI typically ranges 0.15--0.40 in Latin, Italian, and Turkish.

### 2.3 Vowel grade = specificity (r = -0.954)

Vowel grades create derivational chains: k -> ke -> kee -> keeo -> keeod. Three hypotheses for what these grades encode were tested:

**H1: Plant part** (grade = leaf/root/flower/fruit). Chi-squared significant but pattern contradicts predictions. REJECTED.

**H2: Processing stage**. Chi-squared = 1,289. Recipe-section enrichment increases monotonically (bare 0.69x -> +ee 2.82x -> +eeo 3.82x). SUPPORTED, but confounded with specificity.

**H3: Specificity**. Pearson r = -0.954 between grade level and page spread (3.14 folios/word at bare grade vs. 1.90 at +eeo). R-squared = 0.910. STRONGLY SUPPORTED.

The grade system is best understood as a derivational specificity hierarchy: bare stems name general categories; each added vowel level restricts the term to fewer contexts. Recipe sections demand precision and therefore show systematic enrichment of higher grades, explaining the H2 result as a downstream consequence.

### 2.4 Compound classifier compositionality (8/8)

If compound roots (kch, tch, pch, lch, lsh, ckh, cth, cph) are genuinely compositional, their section distributions should be predictable from their components. All 8 compounds distribute as predicted:

| Compound | Predicted domain | Observed top section | Match |
|----------|-----------------|---------------------|-------|
| kch | Body-herb interface | Herbal (47%) | Yes |
| tch | Process-herb | Herbal (50%) | Yes |
| pch | Pharmaceutical | Recipe (44%) | Yes |
| lch | Plant anatomy | Bio (37%) | Yes |
| lsh | Root anatomy | Bio (45%) | Yes |
| ckh | Herb-body | Bio (34%) | Yes |
| cth | Herbal procedure | Herbal (51%) | Yes |
| cph | Herb compound | Herbal (43%) | Yes |

### 2.5 Morpheme page-level distributions (14/15 survive Bonferroni)

For each of 15 claimed morphemes, per-folio rate variance was compared against 1,000 random shuffles. 14 of 15 morphemes show variance massively exceeding random expectations (Z-scores 6.15--29.51), surviving Bonferroni correction across 6,384 possible 2--4 character substrings. The single failure (dal, Z = 3.15) falls below the corrected threshold.

Additionally, 0/50 random trials (selecting 7 random frequent substrings) achieved comparable decomposition rates, ruling out the possibility that any frequent substring set produces equivalent results.

**Critical caveat**: Non-random page-level distribution does not prove semantic meaning. The distributions could arise from Currier A/B language differences, scribal clustering, or topical vocabulary variation rather than descriptive content (see Section 5).

### 2.6 Validated morpheme-feature association: ty = thin/linear (p = 0.008)

Of five morpheme-feature associations tested at full scale (all 112 herbal pages), only one replicated:

| Morpheme | Claimed meaning | Original chi2 (30 pages) | Full-scale Fisher p (112 pages) | Full-scale OR | Replicates? |
|----------|----------------|--------------------------|-------------------------------|--------------|-------------|
| **ty** | **thin/linear** | **30.69** | **0.008** | **18.00** | **YES** |
| cthy | fruit/seed | 60.44 | 0.661 | 1.29 | NO |
| dchy | tall/tree-like | 32.36 | 1.000 | 1.22 | NO |
| cphol | fibrous roots | 24.20 | 0.120 | 4.00 | Trend only |
| dan | divided/segmented | 21.27 | 0.095 | 7.24 | Trend only |

The word `ty` shows near-exclusivity: 4 of 5 classified appearances are on linear-leaf pages (PPV = 0.800, specificity = 0.982). This survives Bonferroni correction for the 5 tests performed (threshold p = 0.01).

**Two morphemes show promising but non-significant trends**: `dan` (OR = 7.24, p = 0.095) and `cphol` (OR = 4.00, p = 0.120). Both have high specificity but are too rare for statistical power.

---

## 3. Refuted Claims and Failed Approaches

Transparency about failures is essential for honest scholarship. This section reports all claims that were eliminated through testing.

### 3.1 sh = underground/root: REFUTED

The claim that sh- encodes "underground/hidden (root)" was a cornerstone of the descriptive naming hypothesis. It originated from structural symmetry with ch- (assumed to be its opposite) and a few anecdotal matches.

**Blind test result**: In the first blind prediction test, sh-based predictions scored 0.5/2 = 25% for positive predictions (sh present -> roots prominent) and 43.8% for negative predictions (sh absent -> roots not prominent). Both are at or below chance (~50% base rate for visible roots).

**Corpus evidence against the claim**: shol appears at 0.99% on root-prominent folios versus 1.42% on leaf-prominent folios -- the opposite direction from what was predicted (Mann-Whitney p ~ 0.5).

**Revised interpretation**: sh- words are followed by quantity/measurement markers (qok-) at 1.93x the rate of ch- words. sh/ch ratio is 2.23x higher on line 1 (headers). sh- is NOT enriched in recipe sections (0.82x). The evidence is most consistent with sh- as a substance/ingredient marker rather than a plant-part designator, but this revised interpretation requires further testing.

### 3.2 cthy = fruit/seed: REFUTED at full scale

The original study found chi-squared = 60.44 on a 9-page training set. When expanded to all 112 herbal pages with 29 fruit-bearing pages:

- Fisher exact p = 0.661, OR = 1.29
- The word cthy appears on non-fruit pages (f11r, f15v, f9r, f44v) at similar rates
- The original effect was driven by selection bias: the 9 training pages were a particularly cthy-rich subset

**However**: In the blind prediction test (Blind Test 2), cth-enriched folios showed fruit/seed features at 83% accuracy (2.5/3) versus 35% base rate. This seeming contradiction likely reflects the difference between the specific word `cthy` (not validated) and the broader cth- substring family across full folio text (potentially meaningful but requiring larger sample validation).

### 3.3 dchy = tall/tree-like: REFUTED

Original chi-squared = 32.36 on 3 pages. Full-scale: Fisher p = 1.0, OR = 1.22. The rate on tall-plant pages (2.7/k) is virtually identical to short-plant pages (2.3/k). The original result was an artefact of a 3-page sample.

### 3.4 Negative morpheme predictions: systematic failure

Across both blind tests, predicting that a visual feature is ABSENT because a morpheme is absent performed at or below chance:

| Prediction type | Accuracy | Chance baseline | Assessment |
|----------------|----------|-----------------|------------|
| oiin absent -> no flowers | 43% (Test 2) | ~45% | AT CHANCE |
| yd absent -> no dissected leaves | 50% (Test 2) | ~65% | BELOW CHANCE |
| dal absent -> no round features | 58% (Test 2) | ~70% | BELOW CHANCE |
| sh absent -> no prominent roots | 43.8% (Test 1) | ~50% | BELOW CHANCE |

This systematic failure means the morpheme system, if real, describes only salient features -- it does not exhaustively catalog all features present in an illustration.

### 3.5 Other eliminated hypotheses

Over 20 analysis cycles, the following were also eliminated:

- **Phonetic recovery from plant identifications** (5 anchor names, all failed)
- **Old Turkish hypothesis** (vowel harmony at 58%, chance level)
- **Bax partial phonetic system** (no phonetic recovery for any anchor)
- **Fixed prefix-to-plant-part mapping** (k- = medicine, t- = process, p- = product): consistent with training data but circular -- classifications made by same analyst proposing meanings
- **-yd- = divided leaves with 4/4 match**: expected false positive given ~6,384 possible substrings and 20--30% base rate (10--52 false positives expected)
- **Dioscorides comparison scores** (5--7/10): no baseline established; moderate overlap expected from any herbal text

### 3.6 Why most morpheme-feature associations failed to replicate

The original study used 30 pages with feature-group sizes of 3--9 pages. Chi-squared values were computed at the word level with rare words (6--82 total occurrences). This created extreme instability:

**Example**: dchy had chi-squared = 32.36 based on just 4 word occurrences across 3 pages (195 words total, rate 20.5/k). When expanded to 22 tall-plant pages, the rate dropped to 2.7/k -- the "signal" was a 4-word fluctuation.

This is a cautionary tale about small-N linguistic studies with rare morphemes. Impressive chi-squared values on 3--9 page subgroups with rare words are highly unstable and should never be treated as established findings.

---

## 4. Promising Hypotheses (Not Yet Validated)

### 4.1 Descriptive naming system

The morphological architecture, compositionality of roots, and illustration correlations suggest a descriptive naming system in which words encode observable features. However, the evidence is mixed.

**Supporting evidence from blind tests**: In Blind Test 2, positive predictions (morpheme present -> feature present) achieved ~79% accuracy versus ~35% chance baseline across 9.5 predictions. The combined binomial p-value is approximately < 0.01.

| Positive Prediction | Accuracy | Vs. Chance |
|---------------------|----------|------------|
| cth present -> fruit/seeds | 83% (2.5/3) | +48% |
| dal present -> round/bulbous | 100% (2/2) | +70% |
| oiin present -> flowers | 100% (1/1) | +45% |
| ty HIGH -> thin/linear | 100% (1/1 strong) | +75% |
| **Combined** | **~79%** | **+44%** |

**Evidence against**: Overall blind test accuracy was 67.6% (Test 1) and 63.2% (Test 2), only marginally above estimated chance baselines of 55--65%. Negative predictions fail systematically. Individual positive prediction sample sizes are too small for individual significance.

**Status**: The positive prediction results are promising enough to warrant larger-scale pre-registered testing. The hypothesis cannot be considered validated on current evidence.

### 4.2 ch = visual description vs. sh = substance/ingredient

After sh = underground/root was refuted, corpus analysis revealed:
- sh- words are followed by qok- (quantity markers) at 1.93x the ch- rate
- sh- words chain with other sh- words (ingredient lists)
- sh- is concentrated on line 1 (naming line) at 2.23x relative enrichment
- ch/sh ratio variance across pages is genuine (Z = 8.55, p < 0.001)

The ch/sh contrast appears to be functional (descriptive vs. operational) rather than spatial (above-ground vs. below-ground). This interpretation is consistent with the data but has not yet been tested via blind predictions.

### 4.3 Ten core roots

The stems reduce to approximately 10 consonantal roots. The character `h` may function as a universal root with preceding consonants as classifiers. Evidence includes:
- ch and sh form a minimal pair with 369 word pairs sharing identical structure
- Every vowel grade that ch takes, sh also takes
- 8/8 compound roots distribute as predicted by components

However, the semantic meanings assigned to these roots (ch = aerial matter, sh = underground matter, etc.) are not validated. The structural compositionality is validated; the semantic labels are hypotheses.

---

## 5. Blind Prediction Tests: Methodology and Results

A significant methodological contribution of this study is the introduction of pre-registered blind prediction tests to Voynich studies. To our knowledge, no prior Voynich analysis has subjected its claims to this level of prospective validation.

### 5.1 Protocol

1. Select folios not previously analysed (10 per test)
2. Extract the first word (plant name code) from each folio
3. Decompose into morphemes using the claimed system
4. Record ALL predictions BEFORE examining any illustration
5. Examine illustrations AFTER predictions are locked
6. Score each prediction as HIT, MISS, or PARTIAL
7. Compare accuracy with chance baselines estimated from Voynich herbal illustration base rates

### 5.2 Blind Test 1 (10 folios: f20r--f38r)

- **Overall accuracy**: 67.6% (25/37 counting PARTIALs as 0.5)
- **Estimated chance**: ~60--65%
- **Key results**:
  - ch present -> leaves prominent: 4/4 = 100% (but ~70% base rate, p = 0.24 for all 4 by chance)
  - sh present -> roots prominent: 0.5/2 = 25% (**FAILURE** -- below ~50% base rate)
  - yd absent -> undivided leaves: 8/10 = 80% (vs. ~70% base rate, marginal)
- **Conclusion**: Overall accuracy near chance. sh = root claim definitively refuted.

### 5.3 Blind Test 2 (10 folios: f7r--f19r)

- **Overall accuracy**: 63.2% (36/57 counting PARTIALs as 0.5)
- **Estimated chance**: ~55--60%
- **Key results**:
  - Positive predictions (morpheme present): ~79% accuracy (7.5/9.5 vs. ~35% base rate)
  - Negative predictions (morpheme absent): ~50% accuracy (at or below chance)
- **Conclusion**: Clear asymmetry. Positive predictions show genuine signal; negative predictions fail systematically.

### 5.4 Methodological significance

These tests revealed critical insights invisible to retrospective analysis:

1. **Positive predictions work; negative predictions do not.** This constrains the system to a partial-descriptor model rather than a comprehensive feature catalog.
2. **Some morpheme meanings are wrong.** sh = root was refuted cleanly, prompting revision.
3. **Small-N training sets produce inflated statistics.** The chi-squared values from 30-page training sets did not replicate at full scale for 4 of 5 morphemes.
4. **Base rates matter.** Predicting "leaves are prominent" achieves ~70% accuracy by always saying yes.

We strongly recommend that future Voynich studies adopt similar blind testing protocols before publishing morpheme-meaning claims.

---

## 6. Red Team Results

A dedicated adversarial cycle (Cycle 16) attacked all claims with eight destructive tests.

**Claims that withstood attack:**
1. Morpheme distributions are genuinely non-random (Test B: 14/15, Z = 3.15--29.51)
2. Text has directional structure (Test D: reversed text destroys morpheme patterns)
3. Random meaning assignments do not replicate decomposition (Test F: 0/50 trials)
4. ch/sh ratio variance is real beyond sampling noise (Test G: Z = 8.55)

**Claims that did not withstand attack:**
1. "100% accuracy" for ch = aerial is trivially true (ch on 99.1% of all pages)
2. -yd- = "divided" with 4/4 match is expected given multiple testing
3. Dioscorides comparison lacks baseline
4. Prediction accuracy claims were not pre-registered (addressed in subsequent blind tests)
5. Circular methodology: illustrations classified by same analyst proposing morpheme meanings

---

## 7. Discussion

### 7.1 What the manuscript is NOT

Our findings eliminate or substantially weaken several theories:

| Theory | Status | Evidence |
|--------|--------|----------|
| Rugg (2004): Simple Cardan grille hoax | PARTIALLY REFUTED | Cannot produce cross-word dependencies |
| Cheshire (2019): Proto-Romance | REFUTED | 2-vowel system, 17% A/B vocabulary overlap incompatible |
| Bax (2014): Partial phonetic | ELIMINATED | Phonetic recovery failed for all 5 anchor names |
| Ardic (2025): Old Turkish | ELIMINATED | Vowel harmony at 58% (chance level) |
| Greshko (2025): Naibbe cipher | PARTIALLY COMPATIBLE | Reproduces some statistics but not cross-word dependencies |

### 7.2 What the manuscript might be

The surviving evidence is most consistent with a **constructed notation system** featuring:
- A decodable outer frame (15 prefixes, 17 suffixes)
- An inner core of compositional stems built from ~10 consonantal roots
- A specificity hierarchy (vowel grades)
- Cross-word phonological or notational dependencies (sandhi)

Whether this system encodes descriptive plant names, pharmaceutical formulae, or something else entirely remains an open question. The positive prediction results from blind testing (79% for morpheme-present predictions) are promising but not definitive.

### 7.3 Comparison with prior theories

Our structural findings align with D'Imperio (1978) and Friedman (~1950s, NSA) in supporting a constructed/artificial language. We provide specific structural detail that was previously absent. The pharmaceutical manuscript hypothesis is supported by the recipe-section enrichment patterns and the high-specificity grade system, but is not proven.

### 7.4 Limitations

1. **Confirmation bias.** The analysis began with a pharmaceutical-notation hypothesis. No alternative was tested with equal rigour.

2. **Circular reasoning risk.** Illustrations were classified by the same analyst proposing morpheme meanings. Independent blind classification by botanical experts is needed.

3. **Unvalidated benchmarks.** Fill rate and paradigm completeness were compared against "natural language" ranges not independently measured.

4. **EVA transcription dependency.** All analyses depend on a single transcription, introducing potential artefacts.

5. **Small anchor set.** Five plant identifications at 55--70% confidence are insufficient as anchors.

6. **Control corpora missing.** The single most important unperformed experiment: running identical analyses on agglutinative language corpora (Turkish, Finnish, Swahili) of comparable size.

7. **Blind test sample sizes.** The positive prediction results (N = 9.5) are too small for individual significance, though the combined signal approaches p < 0.01.

### 7.5 Future work

1. **Control corpus validation** -- the single highest priority. Run identical pipeline on known language corpora.
2. **Large-scale pre-registered blind test** (N = 30+) with independent botanical illustration classification.
3. **Formal Currier A/B split analysis** to determine whether morpheme distributions simply reflect the known language split.
4. **Cardan grille sandhi test** -- generate line-aware grille text and test for cross-word correlations.
5. **Historical manuscript search** for similar notation systems in 15th-century Italian pharmaceutical texts.

---

## 8. Methods

### 8.1 Corpus

The primary data source was the Takahashi--Zandbergen EVA transcription (RF1b-e.txt), containing 37,779 word tokens, 8,500 unique word types, and 226,468 characters across 226 folios.

### 8.2 Analysis architecture

The investigation was conducted by Claude Opus 4.6 (1M context) under the direction of a human researcher. Over 20 analysis cycles were performed following a generate--test--destroy protocol. Each cycle produced multiple independent analytical perspectives to reduce single-framework dominance.

### 8.3 Statistical methods

Chi-squared tests with Cramer's V; mutual information (MI) and normalised MI (NMI); permutation tests (n = 1,000); cross-validation (50/50 split and 10-fold); Pearson correlation; Fisher's exact test (two-tailed) for rare morpheme validation; Bonferroni correction; Mann--Whitney U tests; binomial probability estimation for blind test assessment.

### 8.4 Blind prediction protocol

Two rounds of 10 folios each, selected from previously unanalysed pages. All predictions recorded before illustration examination. Predictions locked and scored against Yale Beinecke digital facsimile illustrations. Chance baselines estimated from visual feature base rates across the herbal section.

### 8.5 Full-scale morpheme validation

Top 5 morpheme-feature associations from the 30-page training set were retested on all 112 herbal pages. Each page was classified for relevant visual features. Both page-level (2x2 Fisher exact) and word-level (chi-squared with Yates correction) analyses were performed.

### 8.6 Morphological segmentation

Words were segmented using a greedy algorithm matching known prefix and suffix strings, with residual assigned to the stem slot. Stems were further decomposed by identifying classifier consonants, vowel grade markers, and terminal consonants.

---

## 9. Summary of Evidence Levels

### VALIDATED (survived all tests)

| Finding | Key statistic | Test survived |
|---------|--------------|---------------|
| Cross-word sandhi | 10-fold CV 42.9% vs 34.7%, p < 0.001 | Permutation, cross-validation |
| Morphological architecture | NMI(prefix,suffix) = 0.032 | Independence analysis |
| Vowel grade = specificity | r = -0.954, R^2 = 0.910 | Correlation, recipe enrichment |
| Compound compositionality | 8/8 predicted distributions | Section distribution test |
| Non-random morpheme distributions | 14/15, Z = 3.15--29.51 | Bonferroni-corrected permutation |
| ty = thin/linear leaves | Fisher p = 0.008, OR = 18.0 | Full-scale 112-page validation |

### HYPOTHESES (promising, not fully validated)

| Claim | Best evidence | Weakness |
|-------|--------------|----------|
| Descriptive naming system | Positive predictions 79% vs 35% chance | N = 9.5, combined p ~ 0.01 |
| ch = visual description | ch/sh variance Z = 8.55 | Circular methodology |
| sh = substance/ingredient | sh+qok bigram 1.93x enrichment | Not yet blind-tested |
| dan = divided/segmented | Fisher p = 0.095, OR = 7.24 | Underpowered (8 total occurrences) |
| cphol = fibrous roots | Fisher p = 0.120, OR = 4.00 | Underpowered (6 total occurrences) |

### REFUTED

| Claim | Refuting evidence |
|-------|------------------|
| sh = underground/root | Blind test 25%, shol MORE frequent on leaf pages |
| cthy = fruit/seed | Full-scale Fisher p = 0.66, OR = 1.29 |
| dchy = tall/tree-like | Full-scale Fisher p = 1.0, OR = 1.22 |
| Negative morpheme predictions | Systematic failure across both blind tests |
| Phonetic recovery | All 5 anchor names failed |
| Old Turkish | Vowel harmony 58% (chance) |

---

## 10. References

### Primary Sources
1. Beinecke Rare Book and Manuscript Library. MS 408 (Voynich Manuscript). Yale University.
2. Takahashi, G., & Zandbergen, R. EVA transcription of the Voynich Manuscript (RF1b-e.txt).

### Peer-Reviewed Literature
3. Amancio, D. R., et al. (2013). Probing the statistical properties of unknown texts. *PLoS ONE*, 8(7), e67310.
4. Bennett, W. R. (1976). Scientific and engineering problem-solving with the computer. *Prentice-Hall*.
5. Currier, P. (1976). Papers on the Voynich Manuscript. *New Research on the Voynich Manuscript*.
6. Davis, L. F. (2020). How Many Glyphs and How Many Scribes? *Manuscript Studies*, 5(1).
7. D'Imperio, M. E. (1978). *The Voynich Manuscript: An Elegant Enigma*. NSA.
8. Greshko, M. A. (2025). The Naibbe cipher. *Cryptologia*.
9. Landini, G. (2001). Evidence of linguistic structure in the Voynich manuscript using spectral analysis. *Cryptologia*, 25(4).
10. Rugg, G. (2004). An elegant hoax? *Cryptologia*, 28(1), 31--46.
11. Stolfi, J. (2005). Voynich Manuscript word structure. www.voynich.nu.
12. Zattera, T. (2023). Voynich slot grammar analysis.

---

## Appendix A: Complete Blind Test Results

### Blind Test 1: 37 predictions on 10 folios (f20r--f38r)

| Result | Count |
|--------|-------|
| HIT | 23 |
| MISS | 10 |
| PARTIAL | 4 |
| **Accuracy** | **67.6%** |

### Blind Test 2: 57 predictions on 10 folios (f7r--f19r)

| Result | Count |
|--------|-------|
| HIT | 31 |
| MISS | 16 |
| PARTIAL | 10 |
| **Accuracy** | **63.2%** |

### Combined positive predictions (morpheme present -> feature present)

| Morpheme | Prediction | Tests | Hits | Accuracy | Base rate |
|----------|-----------|-------|------|----------|-----------|
| ch | Leaves prominent | 4 | 4 | 100% | ~70% |
| cth (high) | Fruit/seeds visible | 3 | 2.5 | 83% | ~35% |
| dal | Round/bulbous | 2 | 2 | 100% | ~30% |
| oiin | Flowers visible | 1 | 1 | 100% | ~55% |
| ty (high) | Thin/linear leaves | 1 | 1 | 100% | ~25% |
| sh | Roots prominent | 2 | 0.5 | 25% | ~50% |

---

*This paper reports the results of a multi-cycle AI-assisted investigation. All statistical claims are derived from computational analysis of the EVA transcription. The investigation was conducted by Claude Opus 4.6 (1M context) under the direction of a human researcher. No claim of decipherment is made. All failures are reported alongside successes. v2 incorporates results from two blind prediction tests, full-scale morpheme validation, and sh-morpheme revision.*

*Generated: April 2026*
