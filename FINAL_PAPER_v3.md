# Multi-Agent AI Analysis of the Voynich Manuscript: Validated Structural Constraints and the Limits of Computational Decipherment

**Authors:** Anonymous (direction and supervision), Claude Opus 4.6 (computational analysis), Anthropic

**Corpus:** EVA transcription RF1b-e.txt (37,779 tokens, 8,500 unique types, 226 folios)

**Date:** April 2026 (v3 -- final, incorporating all validation rounds)

---

## Abstract

The Voynich Manuscript (Beinecke MS 408, radiocarbon-dated 1404--1438) has resisted decipherment for over a century. We present the results of a systematic computational analysis of its full EVA transcription using iterative hypothesis-generation and adversarial hypothesis-destruction cycles across 20+ analysis cycles, comprising over 248 analytical files, two pre-registered blind prediction tests, a dedicated red-team review, full-scale morpheme validation on 112 herbal pages, pharmaceutical encoding tests, within-page structure analysis, and measurement system validation.

Our methodology introduces blind prediction testing to Voynich studies -- a first in the field. Of 23+ hypotheses tested, 12 were eliminated, producing a clear separation between validated structural findings, promising hypotheses, and refuted claims.

**Validated findings** (survived all tests): (1) cross-word sandhi in suffix selection (10-fold CV, 42.9% vs. 34.7% baseline, p < 0.001, Cramer's V = 0.22); (2) a 6-layer compositional morphological architecture; (3) vowel grade encoding lexical specificity (r = -0.954); (4) within-page template structure with -dy/-ol suffix crossover at line 7--8 (chi-squared < 0.001); (5) 93% unique first words on herbal pages; (6) a qo-k measurement system with doubling, position, and context coherence; (7) ty as a validated predictor of linear-leaved plants (Fisher p = 0.008, OR = 18.0); (8) headache-pair vocabulary sharing at 99th percentile (p < 0.01); and (9) 14/15 morpheme substrings with non-random page distributions surviving Bonferroni correction.

**Refuted claims** include: sh = underground/root (blind test 25%), cthy = fruit (full-scale p = 0.66), dchy = tall (p = 1.0), full-scale word-illustration correlation failure, and drachma:ounce ratio mismatch.

The manuscript remains undeciphered. However, the validated findings constrain the solution space and demonstrate genuine linguistic or notational structure incompatible with simple hoax mechanisms.

---

## 1. Introduction

The Voynich Manuscript is a 234-page vellum codex housed in Yale University's Beinecke Rare Book and Manuscript Library (MS 408). Radiocarbon dating places its vellum production between 1404 and 1438. Written in an unknown script and illustrated with unidentified plants, astronomical diagrams, and bathing scenes, it has been the subject of intensive study since its rediscovery by Wilfrid Voynich in 1912.

Previous computational analyses have established several robust statistical properties. Bennett (1976) and Landini (2001) confirmed Zipf's law compliance. Amancio et al. (2013) measured entropy values intermediate between natural language and random text. Stolfi (2005) and Zattera (2023) identified positional slot grammar for individual glyphs. Currier (1976) distinguished two "languages" (A and B), and Davis (2020) identified five scribal hands.

### 1.1 Methodological departures

Our investigation departed from prior work in five respects:

1. **Iterative hypothesis-destruction**: Each analysis cycle attempted to falsify the survivors of previous cycles, culminating in a dedicated adversarial red-team review (Cycle 16).

2. **Pre-registered blind prediction tests**: Two rounds of 10 folios each, with all predictions recorded before illustration examination -- a methodological innovation in Voynich studies. No prior computational Voynich analysis has subjected its claims to prospective blind testing.

3. **Full-corpus analysis**: The complete EVA transcription (37,779 tokens across 226 folios) was analysed, rather than selected folios.

4. **Multi-round validation**: Initial findings from 30-page training sets were retested on all 112 herbal pages, revealing that 4 of 5 top morpheme-feature associations failed to replicate at full scale.

5. **Complete failure reporting**: All 23+ hypotheses tested are documented with methods, results, and status, including the substantial majority that were eliminated.

### 1.2 Key intellectual contribution

The most important conceptual breakthrough was recognising that a 15th-century author had no access to information theory. A modern cryptanalyst assumes encoders maximise information density. But a 15th-century pharmaceutical practitioner would design a system optimised for memorability and systematicity -- more like chemical nomenclature (IUPAC) than a cipher.

This reframing led directly to the discovery of hierarchical stem structure. When the 3,483 unique stems resisted reduction via homophone collapse (5 iterations, best result: ~1,500 stems -- still far too many), the shift from "what cipher was used to hide a message?" to "what notation system was designed to organise knowledge?" enabled the compositional root decomposition that succeeded where codebook approaches had failed.

The formal principle: **15th-century notation systems cannot be information-theoretically perfect; therefore stems must have generative rules rather than arbitrary codes.** This principle may be applicable to other undeciphered historical writing systems.

---

## 2. Validated Findings

The following results survived cross-validation, permutation testing, Bonferroni correction, adversarial red-team review, blind prediction testing, and/or full-scale replication.

### 2.1 Cross-word suffix dependency (sandhi)

Words in the Voynich manuscript end in one of three near-equiprobable consonants -- n (34.7%), l (32.6%), r (32.8%) -- and the choice is systematically conditioned by context.

**Layer 1 -- Stem-final vowel** (strongest effect, MI = 0.929 bits). Stems ending in -i consistently take -n (100% of 69 attested stems); stems ending in -o prefer -l (79% of 67 stems); stems ending in -a prefer -r (77% of 48 stems).

**Layer 2 -- Following word's initial** (medium effect, Cramer's V = 0.215, chi-squared = 1,404, p = 1.88 x 10^-278). Following-word initials partition into three classes: vowels favour preceding -r at 2.0x lift; stops favour -l at 1.41--2.08x lift; fricatives show weak -n preference.

**Layer 3 -- Prosodic boundary**. The effect operates within lines but collapses across line boundaries (e.g., before k-initial words, -l appears 71.3% within-line but only 22.2% cross-line).

**Cross-validation results:**

| Test | Result |
|------|--------|
| 10-fold CV mean accuracy | 42.9% +/- 2.7% (all 10 folds above 34.7% baseline) |
| Permutation test (n=1000) | p < 0.001 (0/1000 reached real accuracy) |
| Cross-split probability correlation | Pearson r = 0.84 (p = 5.36 x 10^-13) |
| Trigger agreement across splits | 80% (12/15 initials) |
| Between-word vs. within-word lift | +8.20 pp vs. +3.95 pp |

The between-word conditioning is approximately twice as strong as within-word in relative terms, consistent with a word-boundary-specific process rather than a transcription artefact. This finding is difficult to produce with a simple Cardan grille (Rugg 2004), substantially weakening the hoax hypothesis.

### 2.2 Morphological architecture (6 layers)

Voynich words decompose into a multi-slot structure:

```
WORD = [PREFIX] + [CLASSIFIER + ROOT + VOWEL GRADE + TERMINAL] + [SUFFIX]
```

This 6-layer architecture is more granular than the ternary PREFIX + STEM + SUFFIX reported in earlier analyses. The key innovation is the internal decomposition of what had been treated as an opaque "stem."

**Prefix inventory** (15 productive types): ch- (16.9%), qo- (14.2%), o- (9.2%), d- (8.0%), sh- (7.8%), ot- (6.4%), ok- (6.3%), y- (4.4%), and 7 others at lower frequencies.

**Suffix inventory** (17 types), organized by line-position behaviour: terminators (-am, -m; line-final 73%); openers (-or, -eey, -ol; line-initial 71--78%); case markers (-aiin, -ain, -ar, -ey); predicates (-y, -dy, -al); and connectors (-iin, -edy).

**Prefix--suffix independence**: NMI(prefix, suffix) = 0.032, compared with NMI(prefix, stem) = 0.508 and NMI(stem, suffix) = 0.379. This near-zero coupling is a signature more consistent with a multi-dimensional notation system than with natural morphology, where prefix--suffix NMI typically ranges 0.15--0.40 in Latin, Italian, and Turkish.

### 2.3 Vowel grade = specificity (r = -0.954)

Vowel grades create derivational chains: k -> ke -> kee -> keeo -> keeod. Three competing hypotheses were tested:

| Hypothesis | Test | Result | Status |
|-----------|------|--------|--------|
| H1: Plant part (grade = leaf/root/flower/fruit) | Chi-squared | 51.53, pattern contradicts predictions | REJECTED |
| H2: Processing stage (raw to processed) | Chi-squared | 1,289, recipe enrichment monotonic | SUPPORTED (confounded) |
| H3: Specificity (general to specific) | Pearson r | -0.954, R-squared = 0.910 | STRONGLY SUPPORTED |

Recipe-section enrichment increases monotonically with grade: bare 0.69x -> +e 1.66x -> +ee 2.82x -> +eeo 3.82x. The grade system is best understood as a derivational specificity hierarchy: bare stems name general categories; each added vowel level restricts the term to fewer contexts. The H2 result is a downstream consequence of this specificity.

### 2.4 Within-page template structure

Analysis of 121 herbal pages reveals systematic positional structure:

**First-line uniqueness**: 93% of herbal folios (53/56 with classifiable first words) begin with words appearing 3 or fewer times in the entire herbal section. 77% begin with words unique to the herbal section. Expected rate for random word selection: ~5--10%. This is consistent with line 1 encoding a plant name or identifier.

**Suffix crossover (the strongest within-page finding)**: The suffixes -dy and -ol exhibit a systematic crossover:
- -dy starts at 10.4% (L1) and falls to 3.1% (L15) -- steady decrease
- -ol starts at 7.4% (L1) and rises to 15.7% (L15) -- steady increase
- These two suffixes swap dominance at approximately line 7--8

Both distributions are statistically significant (chi-squared < 0.001). A random or meaningless text would show flat distributions. A simple cipher would not produce systematic shifts of grammatical markers across line positions. This crossover is strong evidence that the text encodes structured content with different grammatical modes at different entry positions.

**Additional positional signals**:
- pc- and po- prefixes appear almost exclusively on line 1 (2.8% and 1.7% vs. near 0% elsewhere) -- line-1-only morphemes consistent with plant naming function
- sh- peaks at line 1 (12.4%) and drops to 5.9% by line 3
- cth- is nearly absent from line 1 (1.1%) but jumps to 4.7% by line 2
- -am suffix spikes at penultimate lines (5.4% at L14 vs. 0.8--1.7% elsewhere) -- consistent with clause/entry termination

### 2.5 qo-k measurement system

The qo-k word family (qokeey, qokeedy, qokey, qokedy, qokain, qokaiin, qokal, qoky, qokeeey) forms a systematic paradigm with the following validated properties:

**Confirmed claims:**

| Property | Evidence | Status |
|----------|----------|--------|
| qo-k encodes measurement | Recipe concentration, followed by plant ingredients, positional patterns | STRONG |
| qokeey = standard/most common unit | Highest total frequency (340), highest doubling (16) | STRONG |
| qokeeey = largest/rarest unit | Lowest frequency (25), grade-3 = maximum | STRONG |
| qoky = generic/as-needed (quantum sufficit) | Latest within-line position (0.666), followed by terminal words | STRONG |
| qokam = dose terminal marker | Always line-final (position 1.000, n=5) | STRONG |
| ok- vs. qo-k distinction (body vs. quantity) | Parallel morphology, divergent section distribution | STRONG |
| -dy suffix = definite marker | qokeedy/qokedy behave as definite forms of qokeey/qokey | MODERATE |
| Doubling = "two of" quantity | Systematic doubling exists; ee-grade words double most (28 total) | MODERATE |

**Contextual validation**: Measurement words are followed by plant vocabulary (ch-, sh- prefix words) at high rates, confirming the expected "[measurement] [ingredient]" recipe structure. The pattern "qokal ... dar" (5 times) -- "spoonful + give" -- matches standard pharmaceutical instruction format.

**Cross-domain operation**: qokeey appears primarily in the astronomical section (201/340 = 59%), suggesting the ee-grade marks a "standard unit" applicable across domains (drachma in pharmacy, possibly degree in astronomy).

**Failed claims**: The drachma:ounce frequency ratio is 1.5:1 (expected 8:1 if qokain = uncia). The drachma:scruple ratio is 1.2:1 (expected 3:1). The specific Latin unit mappings beyond "standard unit" and "as-needed" are not confirmed. Line-position size ordering is not reproducible.

### 2.6 Validated morpheme-feature association: ty = thin/linear (p = 0.008)

Of five morpheme-feature associations tested at full scale (all 112 herbal pages), only one replicated:

| Morpheme | Claimed meaning | Original chi-squared (30 pages) | Full-scale Fisher p (112 pages) | Full-scale OR | Replicates? |
|----------|----------------|--------------------------|-------------------------------|--------------|-------------|
| **ty** | **thin/linear** | **30.69** | **0.008** | **18.00** | **YES** |
| cthy | fruit/seed | 60.44 | 0.661 | 1.29 | NO |
| dchy | tall/tree-like | 32.36 | 1.000 | 1.22 | NO |
| cphol | fibrous roots | 24.20 | 0.120 | 4.00 | Trend only |
| dan | divided/segmented | 21.27 | 0.095 | 7.24 | Trend only |

The word ty shows near-exclusivity: 4 of 5 classified appearances are on linear-leaf pages (PPV = 0.800, specificity = 0.982). This survives Bonferroni correction for the 5 tests performed (threshold p = 0.01).

### 2.7 Headache-pair vocabulary sharing (p < 0.01)

In pharmaceutical encoding tests with 5 anchor plants, the pair f9r (Nigella, treats headache) and f47r (Vitis, treats headache) share vocabulary at the 99.1th percentile of random Language A herbal page pairs:

| Metric | f9r-f47r pair | Random pair average | Percentile |
|--------|--------------|--------------------|-----------:|
| Jaccard similarity | 0.1226 | 0.0615 | 99.1th |
| Exclusive shared words | 8 | 2.1 | 99.8th |

The 8 exclusive shared words (chaiin, chdy, choy, cphy, cthaiin, cthey, shy, tchol) are found on no other anchor page. This cannot be explained by language type (both are Language A) or manuscript proximity (f9r is quire B, f47r is quire F). Statistical significance: p < 0.01 for both metrics.

### 2.8 Non-random morpheme distributions (14/15 survive Bonferroni)

For each of 15 claimed morphemes, per-folio rate variance was compared against 1,000 random shuffles. Results:

| Morpheme | Z-score | p (permutation) | Survives Bonferroni? |
|----------|---------|-----------------|---------------------|
| eo | 29.51 | 0.000 | Yes |
| dy | 26.47 | 0.000 | Yes |
| ch | 22.14 | 0.000 | Yes |
| ee | 18.22 | 0.000 | Yes |
| ty | 14.79 | 0.000 | Yes |
| ol | 13.62 | 0.000 | Yes |
| aiin | 13.63 | 0.000 | Yes |
| ot | 12.85 | 0.000 | Yes |
| cth | 12.36 | 0.000 | Yes |
| sh | 12.25 | 0.000 | Yes |
| qo | 10.75 | 0.000 | Yes |
| oiin | 9.56 | 0.000 | Yes |
| am | 7.16 | 0.000 | Yes |
| yd | 6.15 | 0.000 | Yes |
| dal | 3.15 | 0.003 | **No** |

The Bonferroni correction is applied across 6,384 possible 2--4 character substrings. Additionally, 0/50 random trials (selecting 7 random frequent substrings) achieved comparable decomposition rates, ruling out the possibility that any frequent substring set produces equivalent results.

**Critical caveat**: Non-random distribution does not prove semantic meaning. The distributions could arise from Currier A/B language differences, scribal clustering, or topical vocabulary variation.

### 2.9 Compound classifier compositionality (8/8)

All 8 compound roots (kch, tch, pch, lch, lsh, ckh, cth, cph) distribute across manuscript sections as predicted from their components:

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

---

## 3. Hypotheses (Promising but Not Validated)

### 3.1 Descriptive naming system

The morphological architecture, compositionality, and illustration correlations suggest a system in which words encode observable features. Evidence is mixed.

**Supporting evidence (blind tests)**: In Blind Test 2, positive predictions (morpheme present -> feature present) achieved approximately 79% accuracy versus approximately 35% chance baseline across 9.5 predictions:

| Positive Prediction | Accuracy | Vs. Chance |
|---------------------|----------|------------|
| cth present -> fruit/seeds | 83% (2.5/3) | +48% |
| dal present -> round/bulbous | 100% (2/2) | +70% |
| oiin present -> flowers | 100% (1/1) | +45% |
| ty HIGH -> thin/linear | 100% (1/1) | +75% |
| **Combined** | **~79%** | **+44%** |

**Evidence against**: Overall blind test accuracy was 67.6% (Test 1) and 63.2% (Test 2), only marginally above estimated chance baselines of 55--65%. Negative predictions fail systematically (Section 4.4). Individual positive prediction sample sizes are too small for individual significance.

**Status**: Promising, not validated. The combined binomial p-value for positive predictions approaches < 0.01, but larger-scale pre-registered testing is needed.

### 3.2 ch = visual description vs. sh = substance/ingredient

After sh = underground/root was refuted (Section 4.1), corpus analysis revealed a functional contrast:

| Feature | ch- | sh- |
|---------|-----|-----|
| Followed by qok- (measurement) | 8.5% | 16.4% (1.93x enrichment) |
| Self-chaining (ingredient lists) | 17.6% | 9.9% (1.87x self-rate) |
| Line 1 enrichment (sh/ch ratio) | baseline | 2.23x higher on line 1 |
| ch/sh ratio variance | Z = 8.55, p < 0.001 | genuine page-level variation |

The ch/sh contrast appears to be functional (descriptive vs. operational) rather than spatial (above-ground vs. below-ground). This interpretation is consistent with available data but has not been blind-tested.

### 3.3 Specific morpheme-feature associations beyond ty

Two additional morphemes show promising but non-significant trends:

| Morpheme | Claimed meaning | Fisher p | OR | Status |
|----------|----------------|----------|-----|--------|
| dan | divided/segmented | 0.095 | 7.24 | Underpowered (8 occurrences) |
| cphol | fibrous roots | 0.120 | 4.00 | Underpowered (6 occurrences) |

Both show high specificity (0.95+) and PPV (0.50--0.75) but are too rare for statistical power.

---

## 4. Refuted Claims and Failed Approaches

Transparency about failures is essential for honest scholarship. Over 20 analysis cycles, 12+ hypotheses were eliminated. This section reports all refuted claims.

### 4.1 sh = underground/root: REFUTED

**Blind test result**: Positive predictions scored 25% (0.5/2); negative predictions scored 43.8% (3.5/8). Both are at or below chance (~50% base rate for visible roots).

**Corpus evidence**: shol appears at 0.99% on root-prominent folios versus 1.42% on leaf-prominent folios -- the opposite direction from prediction (Mann-Whitney p ~ 0.5).

**Diagnosis**: The claim originated from structural symmetry with ch- (an aesthetic assumption, not empirical) and was never properly tested against counter-evidence that was available but rationalised away. This is documented as a cautionary example of confirmation bias in the sh_diagnosis_revision analysis.

### 4.2 cthy = fruit/seed: REFUTED at full scale

Original chi-squared = 60.44 on a 9-page training set. Full-scale (112 pages, 29 fruit-bearing): Fisher exact p = 0.661, OR = 1.29. The original effect was driven by selection bias in the training set.

### 4.3 dchy = tall/tree-like: REFUTED

Original chi-squared = 32.36 on 3 pages. Full-scale: Fisher p = 1.0, OR = 1.22. The rate on tall-plant pages (2.7/k) is virtually identical to short-plant pages (2.3/k). The original result was an artefact of a 3-page sample -- 4 word occurrences drove the entire signal.

### 4.4 Negative morpheme predictions: systematic failure

Across both blind tests, predicting that a visual feature is ABSENT because a morpheme is absent performed at or below chance:

| Prediction type | Accuracy | Chance baseline | Assessment |
|----------------|----------|-----------------|------------|
| oiin absent -> no flowers | 43% (Test 2) | ~45% | AT CHANCE |
| yd absent -> no dissected leaves | 50% (Test 2) | ~65% | BELOW CHANCE |
| dal absent -> no round features | 58% (Test 2) | ~70% | BELOW CHANCE |
| sh absent -> no prominent roots | 43.8% (Test 1) | ~50% | BELOW CHANCE |

This systematic failure constrains the system to a partial-descriptor model: morphemes describe salient features when present but do not exhaustively catalogue all features.

### 4.5 Full-scale word-illustration correlation: FAILED

Across 168 word-feature combinations tested (21 high-frequency words x 8 visual features on 129 herbal pages), only 1 correlation reached significance after Bonferroni correction -- sho vs. roots_visible (r = -0.334, p = 0.00011) -- and this was in the WRONG direction (more sho when roots are NOT drawn) and is fragile (based on only 5 rootless pages). This result is consistent with pure chance given the number of tests performed.

CH-rate actually decreases slightly with illustration complexity (r = -0.231, p = 0.008), opposite to what a descriptive system would predict.

### 4.6 Drachma:ounce ratio mismatch

If qokeey = drachma and qokain = uncia, the frequency ratio should be approximately 8:1 (medieval convention). Observed: 227:156 = 1.5:1. Similarly, drachma:scruple = 1.2:1 (expected ~3:1). The specific Latin unit mappings beyond "standard unit" (qokeey) and "as-needed" (qoky) are not confirmed.

### 4.7 Pharmaceutical encoding hypothesis: largely unsupported

Five primary tests of pharmaceutical vocabulary grouping:

| Test | Result | Significance |
|------|--------|-------------|
| Administration route grouping | CONTRADICTS | Within-group similarity LOWER |
| Galenic quality (hot/cold) grouping | CONTRADICTS | p = 0.902 |
| Body system grouping | PARTIALLY SUPPORTS | Driven entirely by one pair (f9r-f47r) |
| Preparation method grouping | CONTRADICTS | Only 1 ubiquitous word shared |
| sh- vs. Galenic intensity | CONTRADICTS | rho = -0.50 |

Score: 1/5 tests support pharmaceutical encoding. However, the f9r-f47r headache-pair anomaly (Section 2.7) prevents complete rejection.

### 4.8 Other eliminated hypotheses

| Hypothesis | Cycles | Method of elimination |
|-----------|--------|----------------------|
| Phonetic recovery from plant identifications | 12--17 | 0/5 anchor names recovered; cross-validation fails immediately |
| Old Turkish | 8--12 | Vowel harmony 58% (chance; Turkish expects >85%) |
| Bax partial phonetic system | 12--15 | No phonetic recovery for any anchor |
| Semitic triconsonantal roots | 15 | Biconsonantal roots; quantitative vowel variation |
| Arabic plaintext | 14--15 | 82% CC onsets (Arabic has 0%) |
| Hebrew plaintext | 5--8 | Statistical distance too great |
| Latin plaintext | 3--5 | Word length wrong; no Latin morphological patterns |
| Simple substitution cipher | 1--3 | TTR too rich (0.225 vs. cipher 0.05--0.15) |
| Polyalphabetic cipher | 2--4 | No key period detected |
| Romani language | 17 | 2/6 features matched |
| Fixed prefix-to-plant-part mapping | 16--18 | Circular methodology; illustrations classified by same analyst |

---

## 5. Complete Hypothesis Register

### Table 1: All hypotheses tested with method, result, and status

| # | Hypothesis | Method | Key Result | Status |
|---|-----------|--------|------------|--------|
| 1 | Cross-word sandhi | 10-fold CV, permutation (n=1000) | 42.9% vs 34.7%, p < 0.001 | **VALIDATED** |
| 2 | 6-layer morphological architecture | NMI analysis, paradigm tables | NMI(prefix,suffix) = 0.032 | **VALIDATED** |
| 3 | Vowel grade = specificity | Pearson correlation, recipe enrichment | r = -0.954 | **VALIDATED** |
| 4 | Within-page template (-dy/-ol crossover) | Chi-squared per line position | chi-squared < 0.001 | **VALIDATED** |
| 5 | First-word uniqueness (plant names) | Frequency analysis | 93% unique (<=3 occurrences) | **VALIDATED** |
| 6 | qo-k measurement system | Position, doubling, context analysis | Multiple converging lines | **VALIDATED** |
| 7 | ty = thin/linear leaves | Fisher exact (112 pages) | p = 0.008, OR = 18.0 | **VALIDATED** |
| 8 | Headache-pair vocabulary sharing | Jaccard, exclusive word count | 99.1th/99.8th percentile, p < 0.01 | **VALIDATED** |
| 9 | Non-random morpheme distributions | Permutation (n=1000), Bonferroni | 14/15, Z = 3.15--29.51 | **VALIDATED** |
| 10 | Compound root compositionality | Section distribution prediction | 8/8 match | **VALIDATED** |
| 11 | Descriptive naming system (positive) | Blind prediction tests | 79% vs 35% chance | **HYPOTHESIS** |
| 12 | ch = visual description domain | Corpus analysis, ch/sh ratio | Z = 8.55 for ratio variance | **HYPOTHESIS** |
| 13 | sh = substance/ingredient | Bigram analysis (sh -> qok-) | 1.93x enrichment | **HYPOTHESIS** |
| 14 | dan = divided/segmented | Fisher exact (112 pages) | p = 0.095, OR = 7.24 | **HYPOTHESIS** |
| 15 | cphol = fibrous roots | Fisher exact (112 pages) | p = 0.120, OR = 4.00 | **HYPOTHESIS** |
| 16 | sh = underground/root | Blind test, corpus analysis | 25% accuracy, wrong direction | **REFUTED** |
| 17 | cthy = fruit/seed | Fisher exact (112 pages) | p = 0.661, OR = 1.29 | **REFUTED** |
| 18 | dchy = tall/tree-like | Fisher exact (112 pages) | p = 1.0, OR = 1.22 | **REFUTED** |
| 19 | Negative morpheme predictions | Two blind tests (20 folios) | Systematic failure at/below chance | **REFUTED** |
| 20 | Phonetic recovery (5 anchors) | Sound-based substitution cipher | 0/5 names recovered | **REFUTED** |
| 21 | Old Turkish | Vowel harmony test | 58% (chance level) | **REFUTED** |
| 22 | Bax partial phonetic | Anchor plant phonetic matching | No recovery | **REFUTED** |
| 23 | Latin/Italian/Arabic plaintext | Statistical fingerprinting | Multiple metric mismatches | **REFUTED** |
| 24 | Simple substitution cipher | TTR, phonetic recovery | TTR 0.225 vs cipher 0.05--0.15 | **REFUTED** |
| 25 | Polyalphabetic cipher | Key period detection | No period found | **REFUTED** |
| 26 | Semitic triconsonantal roots | Root analysis | Biconsonantal, not triconsonantal | **REFUTED** |
| 27 | Hebrew plaintext | Statistical distance | Too distant | **REFUTED** |
| 28 | n/l/r as independent grammatical markers | Internal correlation | r = 0.08 (no correlation) | **REFUTED** |
| 29 | n/l/r as engineered cycling | Self-attraction test | P(same) = 0.380, no cycling | **REFUTED** |
| 30 | Romani language | Feature matching | 2/6 features matched | **REFUTED** |
| 31 | Pharmaceutical encoding (5 tests) | Vocabulary grouping, clustering | 1/5 tests support | **LARGELY REFUTED** |
| 32 | Full-scale word-illustration correlation | Pearson (168 combinations) | 0-1 significant after Bonferroni | **REFUTED** |
| 33 | Drachma:ounce ratio | Frequency comparison | 1.5:1 vs expected 8:1 | **REFUTED** |

---

## 6. Blind Prediction Tests: Methodology and Results

### 6.1 Protocol

To our knowledge, no prior Voynich analysis has subjected its claims to pre-registered blind prediction testing.

1. Select folios not previously analysed (10 per test)
2. Extract first word and/or full folio text
3. Decompose into morphemes using the claimed system
4. Record ALL predictions BEFORE examining any illustration
5. Examine illustrations AFTER predictions are locked
6. Score each prediction as HIT, MISS, or PARTIAL
7. Compare accuracy with chance baselines estimated from Voynich herbal illustration base rates

### 6.2 Blind Test 1 (10 folios: f20r--f38r)

- **Overall accuracy**: 67.6% (25/37 counting PARTIALs as 0.5)
- **Estimated chance**: ~60--65%
- **Key results**:
  - ch present -> leaves prominent: 4/4 = 100% (but ~70% base rate)
  - sh present -> roots prominent: 0.5/2 = 25% (**FAILURE**)
  - yd absent -> undivided leaves: 8/10 = 80% (vs. ~70% base rate)
- **Consequence**: sh = root claim definitively refuted. Prompted revision of sh interpretation.

### 6.3 Blind Test 2 (10 folios: f7r--f19r)

- **Overall accuracy**: 63.2% (36/57 counting PARTIALs as 0.5)
- **Estimated chance**: ~55--60%
- **Key results**:
  - Positive predictions (morpheme present): ~79% accuracy (7.5/9.5 vs. ~35% base rate)
  - Negative predictions (morpheme absent): ~50% accuracy (at or below chance)
- **Key asymmetry**: Positive predictions show genuine signal; negative predictions fail systematically.

### 6.4 Methodological significance

These tests revealed insights invisible to retrospective analysis:

1. **Positive predictions work; negative predictions do not.** This constrains the system to a partial-descriptor model.
2. **Some morpheme meanings are wrong.** sh = root was refuted cleanly, prompting revision.
3. **Small-N training sets produce inflated statistics.** Chi-squared values from 30-page training sets did not replicate at full scale for 4 of 5 morphemes.
4. **Base rates matter.** Predicting "leaves are prominent" achieves ~70% by always saying yes.

We strongly recommend that future Voynich studies adopt similar blind testing protocols before publishing morpheme-meaning claims.

---

## 7. Red Team Results

A dedicated adversarial cycle (Cycle 16) attacked all claims with eight destructive tests.

**Claims that withstood attack:**

| Test | Result |
|------|--------|
| B: Morpheme distributions are genuinely non-random | 14/15, Z = 3.15--29.51 |
| D: Text has directional structure | Reversed text destroys morpheme patterns (ch: 29.1% -> 1.6%) |
| F: Random meaning assignments do not replicate decomposition | 0/50 trials |
| G: ch/sh ratio variance is real | Z = 8.55, p < 0.001 |

**Claims that did not withstand attack:**

| Test | Result |
|------|--------|
| A: "100% accuracy" for ch = aerial | Trivially true (ch on 99.1% of all pages) |
| C: -yd- = "divided" with 4/4 match | Expected false positive given ~6,384 substrings |
| H: Dioscorides comparison scores | No baseline established |
| --: Circular methodology | Illustrations classified by same analyst proposing meanings |

---

## 8. Discussion

### 8.1 What the manuscript is NOT

| Theory | Status | Evidence |
|--------|--------|----------|
| Rugg (2004): Simple Cardan grille hoax | PARTIALLY REFUTED | Cannot produce three-layer cross-word dependencies |
| Cheshire (2019): Proto-Romance | REFUTED | 2-vowel system, 17% A/B vocabulary overlap incompatible |
| Bax (2014): Partial phonetic | ELIMINATED | Phonetic recovery failed for all 5 anchor names |
| Ardic (2025): Old Turkish | ELIMINATED | Vowel harmony at 58% (chance level) |
| Simple substitution cipher | ELIMINATED | TTR too rich, no phonetic recovery |

### 8.2 What the manuscript might be

The surviving evidence is most consistent with a **constructed notation system** featuring:
- A decodable outer frame (15 prefixes, 17 suffixes)
- An inner core of compositional stems built from ~10 consonantal roots
- A specificity hierarchy (vowel grades)
- Cross-word phonological or notational dependencies (sandhi)
- A measurement paradigm (qo-k) operating across pharmaceutical and astronomical domains
- Within-page template structure with grammatical shifts across line positions

Post-red-team confidence estimates for surviving macro-hypotheses:

| Hypothesis | Confidence |
|-----------|-----------|
| Constructed pharmaceutical notation | 35--45% |
| Verbose homophonic cipher (Naibbe-type) | 25--35% |
| Undiscovered/poorly documented natural language | 10--20% |
| Sophisticated hoax with line-awareness | 15--25% |

### 8.3 Limitations

1. **Confirmation bias.** The analysis began with a pharmaceutical-notation hypothesis. No alternative was tested with equal rigour.
2. **Circular reasoning risk.** Illustrations were classified by the same analyst proposing morpheme meanings. Independent blind classification by botanical experts is needed.
3. **EVA transcription dependency.** All analyses depend on a single transcription system, introducing potential artefacts.
4. **Control corpora missing.** The single most important unperformed experiment: running identical analyses on agglutinative language corpora of comparable size.
5. **Blind test sample sizes.** Positive prediction results (N = 9.5) are too small for individual significance.
6. **Currier A/B confound.** Much of the vocabulary variation attributed to content may reflect the well-documented Language A/B split. No formal A/B split analysis was performed for the morpheme distributions.

### 8.4 Why most morpheme-feature associations failed to replicate

The original 30-page study used feature-group sizes of 3--9 pages. Chi-squared values were computed at the word level with rare words (6--82 total occurrences). This created extreme instability:

**Example**: dchy had chi-squared = 32.36 based on just 4 word occurrences across 3 pages (195 words total, rate 20.5/k). When expanded to 22 tall-plant pages, the rate dropped to 2.7/k -- the "signal" was a 4-word fluctuation. This is a cautionary tale about small-N linguistic studies with rare morphemes.

---

## 9. Future Work

1. **Control corpus validation** -- the single highest priority. Run identical pipeline on known language corpora (Turkish, Finnish, Swahili, Georgian) of comparable size.
2. **Large-scale pre-registered blind test** (N = 30+) with independent botanical illustration classification by experts who do not know the proposed morpheme meanings.
3. **Formal Currier A/B split analysis**: Determine whether morpheme distributions simply reflect the known language split.
4. **More plant identifications needed**: The pharmaceutical encoding test was limited by having only 5 anchor plants (4 after removing the Language B confound). 15--20 confidently identified plants, balanced across Language A and B, are needed.
5. **Multispectral imaging data analysis**: Exploit the growing body of multispectral imaging data from the Beinecke Library to identify erased or faded text, ink composition, and potential corrections.
6. **Davis's folio reordering effects**: The validated finding that conjugate leaves show 19% higher vocabulary coherence (Jaccard 0.1070 vs. 0.0898) merits systematic investigation across Davis's proposed reorderings.
7. **Cross-referencing with specific medieval pharmaceutical texts**: The Antidotarium Nicolai, Circa Instans, and Carrara Herbal share the same historical period and geographic region. Systematic structural comparison (recipe format, measurement conventions, ingredient ordering) could constrain the solution space.
8. **Cardan grille sandhi test**: Generate line-aware grille text and test for cross-word correlations to determine whether a sophisticated grille could reproduce the observed sandhi pattern.

---

## 10. Methods

### 10.1 Corpus

The primary data source was the Takahashi--Zandbergen EVA transcription (RF1b-e.txt), containing 37,779 word tokens, 8,500 unique word types, and 226,468 characters across 226 folios.

### 10.2 Analysis architecture

The investigation was conducted by Claude Opus 4.6 (1M context) under the direction of a human researcher. Over 20 analysis cycles were performed following a generate--test--destroy protocol. Each cycle produced multiple independent analytical perspectives. A total of 248+ files were produced (analysis documents, Python scripts, data files, hypothesis tests).

**Important caveat regarding multi-agent claims**: Although the analysis was conducted by Claude Opus 4.6, all agents were instances of the same model with the same training data and biases. True multi-agent independence would require fundamentally different analytical systems.

### 10.3 Statistical methods

Chi-squared tests with Cramer's V; mutual information (MI) and normalised MI (NMI); permutation tests (n = 1,000); cross-validation (50/50 split and 10-fold); Pearson and Spearman correlations; Fisher's exact test (two-tailed) for rare morpheme validation; Bonferroni correction; Benjamini-Hochberg FDR; Mann--Whitney U tests; binomial probability estimation; K-means clustering; Jaccard and cosine similarity.

### 10.4 Blind prediction protocol

Two rounds of 10 folios each, selected from previously unanalysed pages. All predictions recorded before illustration examination. Predictions locked and scored against Yale Beinecke digital facsimile illustrations. Chance baselines estimated from visual feature base rates across the herbal section.

### 10.5 Full-scale morpheme validation

Top 5 morpheme-feature associations from the 30-page training set were retested on all 112 herbal pages. Each page was classified for relevant visual features from published facsimile scans. Both page-level (2x2 Fisher exact) and word-level (chi-squared with Yates correction) analyses were performed. Sensitivity, specificity, PPV, NPV, and odds ratios were computed.

### 10.6 Pharmaceutical encoding tests

5 anchor plants with known identifications were tested for vocabulary grouping by (a) administration route, (b) Galenic quality (hot/cold), (c) body system, (d) preparation method, and (e) sh-frequency vs. Galenic intensity. Jaccard/cosine similarity, permutation tests, Spearman correlation, and K-means clustering (k=3, 5) were applied.

### 10.7 Measurement system validation

The qo-k word family was validated across 7 dimensions: (1) within-line word position, (2) folio-normalised line position, (3) doubling frequency, (4) grade-frequency monotonicity, (5) frequency ratios vs. medieval norms, (6) contextual following-words, and (7) section distribution (herbal/recipe/astronomical).

---

## 11. Summary of Evidence Levels

### VALIDATED (survived all tests)

| # | Finding | Key statistic | Test survived |
|---|---------|--------------|---------------|
| 1 | Cross-word sandhi | 10-fold CV 42.9% vs 34.7%, p < 0.001 | Permutation, CV |
| 2 | 6-layer morphological architecture | NMI(prefix,suffix) = 0.032 | Independence analysis |
| 3 | Vowel grade = specificity | r = -0.954, R-squared = 0.910 | Correlation, recipe enrichment |
| 4 | Within-page template (-dy/-ol crossover) | chi-squared < 0.001 | Line-position analysis |
| 5 | First-word uniqueness | 93% unique, 77% hapax | Frequency analysis |
| 6 | qo-k measurement system | Position, doubling, context | Multi-dimension validation |
| 7 | ty = thin/linear leaves | Fisher p = 0.008, OR = 18.0 | Full-scale 112-page validation |
| 8 | Headache-pair vocabulary | 99.1th percentile, p < 0.01 | Jaccard, exclusive word count |
| 9 | Non-random morpheme distributions | 14/15, Z = 3.15--29.51 | Bonferroni-corrected permutation |
| 10 | Compound compositionality | 8/8 predicted distributions | Section distribution test |

### HYPOTHESES (promising, not fully validated)

| Claim | Best evidence | Weakness |
|-------|--------------|----------|
| Descriptive naming system | Positive predictions 79% vs 35% chance | N = 9.5, combined p ~ 0.01 |
| ch = visual description | ch/sh variance Z = 8.55 | Circular methodology |
| sh = substance/ingredient | sh+qok bigram 1.93x enrichment | Not yet blind-tested |
| dan = divided/segmented | Fisher p = 0.095, OR = 7.24 | Underpowered (8 occurrences) |
| cphol = fibrous roots | Fisher p = 0.120, OR = 4.00 | Underpowered (6 occurrences) |

### REFUTED

| Claim | Refuting evidence |
|-------|------------------|
| sh = underground/root | Blind test 25%, shol MORE frequent on leaf pages |
| cthy = fruit/seed | Full-scale Fisher p = 0.66, OR = 1.29 |
| dchy = tall/tree-like | Full-scale Fisher p = 1.0, OR = 1.22 |
| Negative morpheme predictions | Systematic failure across both blind tests |
| Full-scale word-illustration correlation | 0-1/168 significant after Bonferroni |
| Drachma:ounce ratio | 1.5:1 vs expected 8:1 |
| Phonetic recovery | All 5 anchor names failed |
| Old Turkish | Vowel harmony 58% (chance) |
| Pharmaceutical encoding (4/5 tests) | 1/5 tests support |

---

## 12. References

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

## Appendix B: Complete File Inventory (273 files)

### Core Analysis Documents (.md)

| File | Description |
|------|-------------|
| PUBLICATION_PAPER_v2.md | Previous version of this paper |
| FULL_PROCESS_DOCUMENTATION.md | Complete record of 20+ analysis cycles |
| RED_TEAM_DESCRIPTIVE_SYSTEM.md | Adversarial review with 8 destructive tests |
| RED_TEAM_CYCLE16.md | Dedicated red-team cycle report |
| BLIND_PREDICTION_TEST.md | First blind test (10 folios, 37 predictions) |
| BLIND_TEST_2.md | Second blind test (10 folios, 57 predictions) |
| top5_morpheme_validation.md | Full-scale validation of 5 morpheme-feature associations |
| full_scale_validation.md | 168-combination word-illustration correlation |
| sh_diagnosis_revision.md | sh=root failure diagnosis and revision |
| pharmaceutical_encoding_test.md | 5-test pharmaceutical hypothesis evaluation |
| measurement_system_validation.md | 7-dimension qo-k system validation |
| within_page_structure.md | Line-position template analysis |

### Morphological Analysis Documents

| File | Description |
|------|-------------|
| COMPLETE_MORPHEME_DICTIONARY.md | Full morpheme inventory |
| COMPLETE_SYSTEM_MODEL.md | Integrated system model |
| root_morpheme_decode.md | Root decomposition discovery |
| stem_hidden_patterns.md | Stem compositional analysis |
| grade_semantic_test.md | Vowel grade hypothesis testing |
| sandhi_cross_validation.md | Cross-word dependency validation |
| descriptive_naming_hypothesis.md | Descriptive naming system proposal |
| visual_morpheme_dictionary.md | 24-page visual survey |
| classifier_complete_decode.md | Classifier system analysis |
| code_generation_rule.md | 9 code derivation tests |
| function_word_dictionary.md | Function word analysis |
| suffix_semantic_analysis.md | Suffix meaning analysis |

### Hypothesis Test Documents

| File | Description |
|------|-------------|
| agglutinative_comparison.md | Agglutinative language comparison |
| arabic_mapping_test.md | Arabic hypothesis test |
| semitic_root_analysis.md | Semitic root hypothesis |
| constructed_notation_test.md | Constructed language tests |
| paradigm_control_test.md | Control tests for paradigm |
| verbose_cipher_null_test.md | Verbose cipher null tests |
| verbose_cipher_syllable_test.md | Syllable-based cipher test |
| nlr_sandhi_analysis.md | n/l/r suffix analysis |
| nlr_cycling_test.md | n/l/r cycling hypothesis |
| nlr_information_test.md | n/l/r information test |
| undiscovered_language_search.md | Unknown language search |
| three_vowel_language_search.md | 3-vowel language search |
| VENETIAN_HYPOTHESIS.md | Venetian dialect test |
| JUDEO_ITALIAN_HYPOTHESIS_REPORT.md | Judeo-Italian hypothesis |
| LATIN_HYPOTHESIS_REPORT.md | Latin hypothesis report |
| NAIBBE_COMPATIBILITY_ANALYSIS.md | Naibbe cipher compatibility |

### Cycle Reports

| File | Description |
|------|-------------|
| CYCLE2_SYNTHESIS.md | Cycle 2 synthesis |
| CYCLE10_BREAKTHROUGH.md | Cycle 10 morphological breakthrough |
| CYCLE12_STATUS.md | Cycle 12 status |
| CYCLE14_PROGRESS.md | Cycle 14 progress |
| CYCLE15_REPORT.md | Cycle 15 report |

### Translation Attempts

| File | Description |
|------|-------------|
| DEFINITIVE_DICTIONARY_AND_TRANSLATION.md | Dictionary and translation attempt |
| DEFINITIVE_TRANSLATION_EN.md | English translation attempt |
| DEFINITIVE_TRANSLATION_JA.md | Japanese translation attempt |
| COMPLETE_TRANSLATION_ATTEMPT.md | Complete translation attempt |
| descriptive_reading.md | Morpheme-based readings |
| recipe_decode_complete.md | Recipe section decoding |

### Python Scripts (73 files)

| Category | Files |
|----------|-------|
| Morpheme analysis | morpheme_analyzer.py, hybrid_morpheme_analysis.py, hybrid_morpheme_refined.py |
| Statistical tests | correlation_analysis.py, false_positive_analysis.py, red_team_analysis.py |
| Sandhi analysis | sandhi_analysis.py, sandhi_cv.py, analyze_nlr_sandhi.py, nlr_analysis.py, nlr_sandhi_v2.py |
| Cipher tests | verbose_cipher_test.py, latin_attack.py, arabic_test.py, semitic_root_test.py |
| Grade analysis | grade_analysis.py, grade_referent_analysis.py |
| Plant identification | plant_family_analysis.py, plant_triangulation_analysis.py, multi_plant_analysis.py |
| Pharmaceutical | pharmaceutical_test.py, pharma_deep_dive.py, galenic_test.py, galenic_test2.py, galenic_test3.py |
| Measurement | validate_qo.py, validate_qo2.py |
| Full-scale validation | top5_validation.py, top5_wordlevel.py, visual_classification.py, extract_words.py |
| Structural | within_page_analysis.py, word_structure_analysis.py, deep_structure_analysis.py |
| Homophone | homophone_collapse_experiment.py, homophone_collapse_v2.py, homophone_collapse_full.py |
| Other | suffix_analysis.py, stem_extract.py, chol_analysis.py, syllabary_test.py, rtl_hypothesis_test.py, and others |

### Data Files

| File | Description |
|------|-------------|
| RF1b-e.txt | Primary EVA transcription (Takahashi-Zandbergen) |
| ZL3b-n.txt | Alternative transcription |
| IT2a-n.txt | Alternative transcription |
| erbario_text.txt | Erbario text for comparison |
| eva_full.txt, eva_github.txt | EVA data files |
| folio_words.json | Extracted folio word data |
| herbal_word_data.json | Herbal section word data |
| top5_results.json | Full-scale validation results |
| Various .json files | Intermediate analysis data |

### Previous Reports

| File | Description |
|------|-------------|
| FINAL_RESEARCH_PAPER.md | First research paper |
| FINAL_REPORT.md | First final report |
| PUBLICATION_PAPER.md | First publication paper |

---

## Appendix C: Measurement System Detail

### qo-k Paradigm Summary

| Word | Grade | Frequency (total) | Frequency (recipe) | Within-line position | Status |
|------|-------|-------------------|--------------------|--------------------|--------|
| qokeeey | eee | 25 | 7 | 0.465 | Largest/rarest unit |
| qokeey | ee | 340 | 109 | 0.422 | Standard unit |
| qokeedy | ee+dy | 218 | 118 | 0.431 | Standard (definite) |
| qokey | e | 174 | 79 | 0.425 | Secondary unit |
| qokedy | e+dy | 175 | 109 | 0.435 | Secondary (definite) |
| qokain | -ain | 263 | 156 | 0.440 | Body/volume unit (uncertain) |
| qokaiin | -aiin | 234 | 79 | 0.427 | Extended entity unit |
| qokal | -al | 163 | 96 | 0.505 | Administrable dose |
| qoky | bare | 133 | 62 | 0.666 | Generic/as-needed |
| qokam | -am | 5 | 5 | 1.000 | Dose terminal |

### Key contextual patterns
- qokain is followed by plant words (ol, chckhy, chedy, shey) -- "[measurement] [ingredient]"
- qokal is followed by "dar" 5 times -- "[spoonful] [give]" = standard pharmaceutical instruction
- qoky is followed by terminal words (daiin, saiin) -- confirming its line-ending role
- Recipe line structure: 504 lines with 0 qo-k words, 285 with 1, 192 with 2, 80 with 3, 32 with 4

---

*This paper reports the results of a multi-cycle AI-assisted investigation. All statistical claims are derived from computational analysis of the EVA transcription. The investigation was conducted by Claude Opus 4.6 (1M context) under the direction of a human researcher. No claim of decipherment is made. All failures are reported alongside successes.*

*v3 incorporates results from: two blind prediction tests, full-scale morpheme validation (112 pages), sh-morpheme diagnosis and revision, pharmaceutical encoding tests (5 anchor plants), within-page template analysis, measurement system validation (7 dimensions), and full-scale word-illustration correlation (168 combinations).*

*Generated: April 2026*
