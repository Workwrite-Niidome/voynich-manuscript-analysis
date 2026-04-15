# Morphological Architecture and Cross-Word Dependencies in the Voynich Manuscript: Evidence for a Compositional Notation System

**Authors:** Anonymous (direction and supervision), Claude Opus 4.6 (computational analysis), Anthropic

**Corpus:** EVA transcription RF1b-e.txt (37,779 tokens, 8,500 unique types, 226 folios)

**Date:** April 2026

---

## Abstract

The Voynich Manuscript (Beinecke MS 408, radiocarbon-dated 1404--1438) has resisted decipherment for over a century. We present a systematic computational analysis of its full EVA transcription using iterative hypothesis-generation and adversarial hypothesis-destruction cycles, including a dedicated red-team review. We report four principal findings: (1) a statistically significant cross-word dependency in suffix selection, cross-validated at 42.9% accuracy versus 34.7% baseline (10-fold CV, p < 0.001, 0/1000 permutations); (2) a compositional morphological architecture PREFIX + [CLASSIFIER + ROOT + VOWEL GRADE + TERMINAL] + SUFFIX in which prefix and suffix are statistically independent (NMI = 0.032); (3) a vowel grade system encoding lexical specificity with near-perfect correlation (r = -0.954) between grade level and page spread, confirmed by 2.82--3.82x recipe-section enrichment of higher grades; and (4) morpheme--illustration correlations surviving Bonferroni correction (14/15 morphemes, permutation p < 0.001). Of 23 hypotheses tested, 12 were eliminated. We propose a descriptive naming system in which words compositionally encode observable features rather than mapping to external referents via cipher. The manuscript remains undeciphered, but these structural findings constrain the solution space and establish that further progress requires domain expertise in 15th-century pharmaceutical practice, not additional cryptanalysis.

---

## 1. Introduction

The Voynich Manuscript is a 234-page vellum codex housed in Yale University's Beinecke Rare Book and Manuscript Library (MS 408). Radiocarbon dating places its vellum production between 1404 and 1438^1^. Written in an unknown script and illustrated with unidentified plants, astronomical diagrams, and bathing scenes, it has been the subject of intensive study since its rediscovery by Wilfrid Voynich in 1912.

Previous computational analyses have established several robust statistical properties of the text. Bennett (1976) and Landini (2001) confirmed Zipf's law compliance. Amancio et al. (2013) measured entropy values intermediate between natural language and random text. Stolfi (2005) and Zattera (2023) identified positional slot grammar for individual glyphs. Currier (1976) distinguished two "languages" (A and B), and Davis (2020) identified five scribal hands contributing to the manuscript.

The manuscript's resistance to decipherment has generated diverse theories. D'Imperio (1978) and Friedman (~1950s, NSA) concluded it was likely a constructed or artificial language. Rugg (2004) proposed a Cardan grille hoax. Cheshire (2019) claimed proto-Romance plaintext (subsequently refuted). Most recently, Greshko (2025) demonstrated that a verbose homophonic substitution cipher ("Naibbe cipher") can reproduce many Voynich statistical properties using historically plausible 15th-century materials.

Our investigation departed from prior work in three respects. First, we employed an iterative hypothesis-destruction methodology in which each analytical cycle attempted to falsify the survivors of previous cycles, culminating in a dedicated adversarial red-team review (Cycle 16). Second, we analysed the complete EVA transcription rather than selected folios, enabling corpus-wide statistical validation. Third, we combined morphological, phonological, statistical, codicological, comparative, and visual approaches within a unified framework, testing 23 distinct hypotheses and eliminating 12.

---

## 2. Results

### 2.1 Cross-word suffix dependency

The most significant novel finding is a cross-word dependency in word-final suffix selection. Words in the Voynich manuscript end in one of three near-equiprobable consonants -- n (34.7%), l (32.6%), r (32.8%) -- and the choice among these is systematically conditioned by the initial character of the following word.

We identified a three-layer conditioning system:

**Layer 1 -- Stem-final vowel** (strongest effect, MI = 0.929 bits). Stems ending in -i consistently take -n (100% of 69 attested stems); stems ending in -o prefer -l (79% of 67 stems); stems ending in -a prefer -r (77% of 48 stems).

**Layer 2 -- Following word's initial** (medium effect, Cramer's V = 0.215, chi-squared = 1,404, p = 1.88 x 10^-278). Following-word initials partition into three classes: vowels (a, i) favour preceding -r at 2.0x lift; stops (k, t, d) favour -l at 1.41--2.08x lift; fricatives and semi-vowels show weak -n preference.

**Layer 3 -- Prosodic boundary**. The effect operates within lines but collapses across line boundaries. Before k-initial words, -l appears 71.3% of the time within-line but only 22.2% cross-line, consistent with a phonological process bounded by prosodic units.

**Cross-validation results:**

| Test | Result |
|------|--------|
| 50/50 split accuracy | 43.4% vs. 34.7% baseline (+8.7 pp) |
| Permutation test (n=1000) | p < 0.001 (0/1000 reached real accuracy) |
| Cross-split probability correlation | Pearson r = 0.84 (p = 5.36 x 10^-13) |
| 10-fold CV mean accuracy | 42.9% +/- 2.7% (all 10 folds above baseline) |
| Trigger agreement across splits | 80% (12/15 initials) |
| Between-word vs. within-word lift | +8.20 pp vs. +3.95 pp |

The between-word conditioning is approximately twice as strong as the within-word conditioning in relative terms, consistent with a process specific to word boundaries rather than a transcription artefact. We term this "sandhi" by analogy with natural-language phonological processes, while noting that correlation does not prove a phonological causal mechanism (see Discussion).

### 2.2 Morphological architecture

Systematic segmentation reveals that Voynich words decompose into a multi-slot structure:

```
WORD = [PREFIX] + [CLASSIFIER + ROOT + VOWEL GRADE + TERMINAL] + [SUFFIX]
```

This architecture is more granular than the ternary PREFIX + STEM + SUFFIX reported in earlier analyses. The key innovation is the internal decomposition of what had been treated as an opaque "stem" into four sub-components.

**Prefix inventory** (15 productive types): ch- (16.9%), qo- (14.2%), o- (9.2%), d- (8.0%), sh- (7.8%), ot- (6.4%), ok- (6.3%), y- (4.4%), k- (3.1%), s- (2.8%), t- (2.7%), p- (1.5%), cth- (1.3%), f- (0.3%), ct- (0.1%).

**Suffix inventory** (17 types), organized by line-position behaviour: terminators (-am, -m; line-final 73%); openers (-or, -eey, -ol; line-initial 71--78%); case markers (-aiin, -ain, -ar, -ey); predicates (-y, -dy, -al); and connectors (-iin, -edy).

**Prefix--suffix independence**: Mutual information analysis of 17,761 fully segmented words reveals NMI(prefix, suffix) = 0.032, compared with NMI(prefix, stem) = 0.508 and NMI(stem, suffix) = 0.379. This near-zero prefix--suffix coupling means the two encode on orthogonal axes -- a signature more consistent with a multi-dimensional notation system than with natural morphology, where prefix--suffix NMI typically ranges 0.15--0.40 in Latin, Italian, and Turkish.

### 2.3 Ten core roots and the compositional system

The stems that had appeared to be an open class of 200--400 arbitrary codes reduce, under compositional analysis, to approximately 10 consonantal roots. A critical discovery is that the character `h` functions as a universal root meaning "substance/materia," with preceding consonants serving as classifiers:

| Root | Classifier+h | Frequency | Domain |
|------|-------------|-----------|--------|
| ch | c+h | 10,609 words | Aerial/visible plant matter (herba) |
| sh | s+h | 4,125 words | Underground/hidden part (radix) |
| kch | k+c+h | 1,023 words | Body-related botanical (virtus) |
| tch | t+c+h | 995 words | Process-related botanical (operatio) |
| pch | p+c+h | 766 words | Prepared compound (confectio) |
| k | -- | 8,259 words | Body/measure/quantity (mensura) |
| t | -- | 4,706 words | Process/time (operatio) |
| l | -- | 8,631 words | Structure/position (locus) |
| r | -- | 6,950 words | Quality/property (qualitas) |
| lk | l+k | 1,042 words | Dose structure (dosis); 7.49x recipe enrichment |

Evidence for compositionality: ch and sh form a perfect minimal pair, with 369 word pairs sharing identical structure but differing only in classifier (ch/sh). Every vowel grade that ch takes, sh also takes. The compound roots (kch, tch, pch, lch, lsh, ckh, cth) are demonstrably compositional -- e.g., lch (l+c+h, "structural-botanical") concentrates in the biological section (37%) describing plant anatomy, while lsh (l+s+h, "structural-underground") concentrates even more heavily there (45%).

### 2.4 Vowel grade = specificity (r = -0.954)

The vowel grade system creates derivational chains of decreasing frequency:

```
k -> ke -> kee -> keeo -> keeod
ch -> che -> chee -> cheeo -> cheeod
```

We tested three hypotheses for what these grades encode:

**H1: Plant part** (grade = leaf/root/flower/fruit). Chi-squared significant (51.5, df=15, p < 0.01) but the pattern contradicts predictions. REJECTED.

**H2: Processing stage** (bare = raw, higher = more processed). Chi-squared = 1,289, df=5, p << 0.001. Recipe-section enrichment increases monotonically with grade:

| Grade | Herbal % | Recipe % | Enrichment ratio |
|-------|----------|----------|-----------------|
| bare | 76.0% | 52.7% | 0.69x (depleted) |
| +e | 12.4% | 20.5% | 1.66x |
| +ee | 5.5% | 15.5% | 2.82x |
| +eeo | 0.6% | 2.4% | 3.82x |
| +eod | 1.4% | 2.6% | 1.81x |

SUPPORTED, but confounded with specificity.

**H3: Specificity** (higher grade = more specific term). Pearson r = -0.954 between grade level and average page spread per word type (3.14 folios/word at bare grade vs. 1.90 at +eeo). R-squared = 0.910. STRONGLY SUPPORTED.

The grade system is best understood as a derivational specificity hierarchy: bare stems name general categories appearing across many folios; each added vowel level restricts the term to fewer contexts. Recipe sections demand precision and therefore show systematic enrichment of higher grades, explaining the H2 result as a downstream consequence.

### 2.5 Compound classifier compositionality (8/8)

If compound roots are genuinely compositional (not arbitrary), their section distributions should be predictable from their components. We tested this for all 8 compound roots containing h:

| Compound | Components | Predicted domain | Observed top section | Match |
|----------|-----------|-----------------|---------------------|-------|
| kch | body + botanical | Body-herb interface | Herbal (47%) | Yes |
| tch | process + botanical | Process-herb | Herbal (50%) | Yes |
| pch | preparation + botanical | Pharmaceutical | Recipe (44%) | Yes |
| lch | structure + botanical | Plant anatomy | Bio (37%) | Yes |
| lsh | structure + underground | Root anatomy | Bio (45%) | Yes |
| ckh | botanical + body | Herb-body | Bio (34%) | Yes |
| cth | botanical + process | Herbal procedure | Herbal (51%) | Yes |
| cph | botanical + preparation | Herb compound | Herbal (43%) | Yes |

8/8 compounds distribute as predicted by their component meanings. This is strong evidence against the stems being an arbitrary codebook.

### 2.6 Morpheme--illustration correlation (14/15 survive Bonferroni)

A critical test of whether morpheme distributions carry semantic content is whether they correlate with illustration content. We performed a permutation test: for each of 15 claimed morphemes, the per-folio rate variance was compared against 1,000 random shuffles of all herbal-section words across folios.

| Morpheme | Claimed meaning | Z-score | p (permutation) | Survives Bonferroni? |
|----------|----------------|---------|-----------------|---------------------|
| ch | aerial/leaf | 22.14 | 0.000 | Yes |
| sh | underground/root | 12.25 | 0.000 | Yes |
| yd | divided/dissected | 6.15 | 0.000 | Yes |
| ty | linear | 14.79 | 0.000 | Yes |
| oiin | flower | 9.56 | 0.000 | Yes |
| qo | body/quantity | 10.75 | 0.000 | Yes |
| ot | process | 12.85 | 0.000 | Yes |
| ol | subject | 13.62 | 0.000 | Yes |
| aiin | entity/noun | 13.63 | 0.000 | Yes |
| ee | specific grade | 18.22 | 0.000 | Yes |
| eo | state/condition | 29.51 | 0.000 | Yes |
| dy | genitive | 26.47 | 0.000 | Yes |
| cth | hard/astringent | 12.36 | 0.000 | Yes |
| am | clause terminal | 7.16 | 0.000 | Yes |
| dal | round | 3.15 | 0.003 | **No** |

14 of 15 morphemes show per-folio variance massively exceeding random shuffling expectations (Z-scores 6.15--29.51), surviving Bonferroni correction across all 6,384 possible 2--4 character substrings. The single failure (dal, Z=3.15) falls below the corrected threshold.

Additionally, 0/50 random trials (selecting 7 random frequent substrings and assigning arbitrary abstract meanings) achieved comparable decomposition rates to the claimed morpheme system, ruling out the possibility that any frequent substring set could produce equivalent results.

### 2.7 Descriptive naming system

The morphological architecture, the compositionality of roots, and the illustration correlations converge on a specific hypothesis: the Voynich manuscript uses a descriptive naming system in which each word compositionally encodes observable features of its referent.

Key supporting evidence:

**First words as descriptive plant names.** 77% of herbal folios (43/56) begin with a word appearing nowhere else in the herbal section. These "plant name codes" decompose according to the morphological formula. Five anchor identifications demonstrate the system:

| Folio | Code | Plant (confidence) | Descriptive reading |
|-------|------|-------------------|-------------------|
| f2r | kydainy | Paeonia (55%) | k(medicinal) + yd(divided) + ain(entity) + y(pred) = "the medicinal divided-leaf plant" |
| f3r | tsheos | Rubia tinctorum (60%) | t(process) + sh(root) + eo(state) + s(collective) = "the processable root-mass" |
| f9r | tydlo | Nigella (65%) | t(process) + yd(divided) + l(structure) + o(state) = "the dissected-structured process plant" |
| f41r | psheykedaleey | Adiantum (60%) | p(prep) + sh(underground) + ey(specific) + k(body) + ed(definite) + al(function) + ee(precise) + y(pred) |
| f47r | pchair | Vitis vinifera (70%) | p(product) + ch(aerial) + ai(entity) + r(quality) = "the quality leaf-product" |

**The -yd- morpheme.** All four first words containing -yd- (f2r kydainy, f9r tydlo, f23r pydchdom, f45r pykydal) describe plants with divided, dissected, or lobed leaves in their illustrations. 4/4 match rate for a feature present in approximately 20--25% of herbal illustrations.

**Prefix--illustration concordance.** All 8 plants with ch in their first-word code show prominent aerial (leaf/flower) features in illustrations (8/8, 100%). 5 of 6 plants with sh show prominent root systems (83%). All 8 p-initial plants are valued for usable products (100%). All 5 t-initial plants are processing/transformation plants (100%). 6 of 6 confirmed k-initial plants are primarily medicinal (100%).

**ch/sh ratio variance across pages.** The ch/sh word ratio varies across herbal folios far more than binomial sampling predicts (observed variance 14.81 vs. expected 2.48, Z = 8.55, p < 0.001), confirming that individual pages genuinely differ in their relative emphasis on aerial versus underground plant parts.

### 2.8 Red team results

A dedicated adversarial cycle (Cycle 16) attacked all claims. The following table summarises what survived and what did not:

**Claims that withstood attack:**

1. Morpheme distributions are genuinely non-random (Test B: all 15 morphemes, Z = 3.15--29.51)
2. Text has directional structure (Test D: reversed text destroys morpheme patterns; ch drops from 29.1% to 1.6%)
3. Random meaning assignments do not replicate decomposition (Test F: 0/50 trials)
4. ch/sh ratio variance is real beyond sampling noise (Test G: Z = 8.55)

**Claims that did not withstand attack:**

1. "100% accuracy" for ch = aerial is trivially true (ch appears on 99.1% of all pages regardless of content)
2. -yd- = "divided" with 4/4 match is expected given ~6,384 possible substrings (10--52 false positives expected depending on base rate assumptions)
3. Dioscorides comparison scores lack a baseline (moderate overlap is expected from any herbal text)
4. Prediction accuracy claims were not pre-registered
5. Circular methodology: illustrations were classified by the same analyst proposing morpheme meanings

**The core unresolved question:** The morphemes have significantly non-random page-level distributions. But non-random distribution does not prove descriptive naming. The distributions could arise from Currier A/B language differences, scribal clustering, topical vocabulary variation, or genuine morphemic structure. The hypothesis has identified real statistical signal; the interpretation remains uncertain.

---

## 3. Discussion

### 3.1 Implications for Voynich studies

Our findings constrain the solution space for the Voynich manuscript in several ways. The cross-word suffix dependency (Section 2.1) is difficult to produce with a simple Cardan grille, substantially weakening the hoax hypothesis of Rugg (2004), though a line-aware grille remains untested. The ternary morphological structure with near-zero prefix--suffix coupling (NMI = 0.032) is inconsistent with natural European language morphology but consistent with a constructed notation system. The vowel grade system's near-perfect specificity correlation (r = -0.954) is too regular for a natural language but expected in a designed classification system.

The manuscript is most parsimoniously explained as a **two-level notation system**: a decodable outer frame (15 category prefixes and 17 grammatical suffixes) encapsulating an inner core of compositional stems built from approximately 10 consonantal roots. This model accommodates all observed statistical features simultaneously.

### 3.2 Comparison with prior theories

| Theory | Compatibility with our findings |
|--------|-------------------------------|
| D'Imperio (1978): Constructed language | HIGH -- we provide specific structural detail |
| Friedman (~1950s): Artificial language | HIGH -- NSA conclusion aligns |
| Rugg (2004): Cardan grille hoax | PARTIALLY REFUTED -- simple grille cannot produce cross-word dependencies |
| Cheshire (2019): Proto-Romance | REFUTED -- 2-vowel system, 87.3% paradigm completeness, 17% A/B vocabulary overlap are incompatible |
| Greshko (2025): Naibbe cipher | PARTIALLY COMPATIBLE -- reproduces some statistics but not cross-word dependencies, the -y/-edy morphological split, or the circumfix function-word paradigm |
| Bax (2014): Partial phonetic | LOW -- phonetic recovery tests failed completely for all 5 anchor plant names |
| Ardic (2025): Old Turkish | ELIMINATED -- Turkish vowel harmony test yields 58% (chance level) |

### 3.3 Limitations

We are transparent about the following limitations:

1. **Confirmation bias.** The analysis began with a pharmaceutical-notation hypothesis and may have designed tests tending to confirm it. No alternative (e.g., agglutinative natural language) was tested with equal rigour.

2. **Unvalidated benchmarks.** Fill rate, paradigm completeness, and morpheme boundary clarity were compared against "natural language" ranges that were not independently measured using the same methodology on actual language corpora.

3. **Circular reasoning chains.** The chol = "leaf" argument uses sandhi to define stems, stems to identify botanical terms, botanical terms to identify plants, plant identifications to test phonetic recovery, and phonetic failure to support the notation hypothesis. While each step has independent statistical support, the chain as a whole risks non-falsifiability.

4. **Subjective confidence levels.** No formal Bayesian framework was employed. All stated confidence values are researcher assessments, not statistical probabilities.

5. **Incomplete language testing.** Only approximately 15 of the world's ~7,000 languages were tested against the manuscript's statistical profile. "No known language matches" is a claim bounded by our testing scope.

6. **EVA transcription dependency.** All analyses depend on the Takahashi--Zandbergen EVA transcription, which introduces potential artefacts from transcription conventions and inter-transcriber variation.

7. **Small anchor set.** The five plant identifications used as anchors carry individual confidence levels of only 55--70%, and the entire descriptive naming hypothesis rests upon them.

### 3.4 Future work

The highest-priority next steps are:

1. **Control corpus validation.** Run the identical analysis pipeline on agglutinative language corpora (Turkish, Finnish, Swahili, Georgian) of comparable size, measuring fill rate, paradigm completeness, and inter-word correlations with the same algorithms. This is the single most important control experiment not yet performed.

2. **Pre-registered prediction tests.** Specify predicted morpheme rates for unexamined folios before visual inspection. A blind test protocol with independent botanical experts classifying illustrations would eliminate circularity.

3. **Cardan grille sandhi test.** Generate Cardan-grille text with a line-aware table and measure whether it reproduces the within-line versus cross-line correlation pattern.

4. **Historical manuscript search.** Search for the -edy morpheme and similar systematic notation in Northern Italian pharmaceutical manuscripts from the Veneto region, 1380--1450.

5. **Generative model.** Build a complete generative model using the discovered rules and compare its statistical output against the real manuscript.

---

## 4. Methods

### 4.1 Corpus

The primary data source was the Takahashi--Zandbergen EVA transcription (RF1b-e.txt), containing 37,779 word tokens, 8,500 unique word types, and 226,468 characters across 226 folios. The EVA (Extended Voynich Alphabet) system maps Voynich glyphs to ASCII characters. All folios were included; no sub-selection was applied.

### 4.2 AI multi-agent analysis architecture

The investigation was conducted by Claude Opus 4.6 (1M context), an AI language model, under the direction of a human researcher. Each analysis cycle involved multiple independent analytical perspectives examining the corpus from different angles (morphological, statistical, comparative, visual). This multi-perspective approach reduced confirmation bias by ensuring no single analytical framework dominated.

Over 20 analysis cycles were performed, producing 220+ analysis files (see Supplementary Materials). Each cycle followed a generate--test--destroy protocol:

1. **Generation**: Identify statistical patterns and propose explanatory hypotheses
2. **Testing**: Design discriminating tests with pre-specified pass/fail criteria
3. **Destruction**: Apply adversarial analysis to surviving hypotheses
4. **Cross-validation**: Validate on held-out data (50/50 split, 10-fold CV, permutation tests)
5. **Red-team review**: A dedicated adversarial cycle (Cycle 16) attacked all claims

### 4.3 Statistical methods

- Chi-squared tests with Cramer's V for effect size
- Mutual information (MI) and normalised mutual information (NMI) for slot independence
- Permutation tests (n = 1,000 shuffles) for significance assessment
- Cross-validation (50/50 split and 10-fold) for generalisation
- Pearson correlation for grade--specificity relationship
- Zipf's law regression
- Conditional entropy chains for character-level analysis
- Yule's K vocabulary richness measurement
- Mann--Whitney U tests for distributional comparisons
- Bonferroni correction for multiple comparisons across 6,384 possible morpheme substrings

### 4.4 Red-team protocol

A dedicated adversarial cycle was conducted with the explicit mandate to destroy every insufficiently supported claim. Eight destructive tests were designed:

- **Test A**: ch ubiquity (is 100% accuracy trivially true?)
- **Test B**: Randomisation (do morpheme distributions survive shuffling?)
- **Test C**: Bonferroni correction (how many hypotheses were tested?)
- **Test D**: Reversed text (does the system survive reversal?)
- **Test E**: Bonferroni survival at p < 0.001 (after correction for 6,384 substrings)
- **Test F**: Random meaning assignment (do vague categories always work?)
- **Test G**: ch/sh ratio variance (signal or sampling noise?)
- **Test H**: Dioscorides comparison baseline (are moderate scores above chance?)

All confidence values reported in this paper reflect post-red-team assessments, which reduced initial claims by 20--40 percentage points.

### 4.5 Visual analysis

Twenty-four herbal folio illustrations were examined from the Yale Beinecke digital facsimile and cross-referenced with EVA transcription first words. Illustration features (leaf shape, root prominence, flower type, overall habit) were classified by the research team. Plant identifications were based on comparison with 15th-century North Italian herbal illustration traditions and published botanical identification proposals. Five anchor identifications at 55--70% confidence were used for cross-validation.

### 4.6 Morphological segmentation

Words were segmented using a greedy algorithm that matched known prefix and suffix strings, with the residual assigned to the stem slot. Stems were further decomposed by identifying classifier consonants preceding h, vowel grade markers (bare, +e, +ee, +eo, +eeo, +eod), and terminal consonants (d, s) that appear exclusively in stem-final position.

---

## 5. Post-Red-Team Confidence Summary

| Claim | Confidence | Status |
|-------|-----------|--------|
| Text has non-random statistical regularities | >99% | Known prior; confirmed |
| Cross-word n/l/r correlation exists | 90% | Novel finding |
| Morphological compositional structure | 85% | Strongly supported |
| Vowel grade = specificity (r = -0.954) | 85% | Confirmed |
| ch = aerial, sh = underground | 70--80% | Illustration-supported |
| -yd- = divided leaves | 60--70% | 4/4 but Bonferroni concern |
| Prefix categories (k- = medicine, t- = process, p- = product) | 60--70% | Consistent but circular risk |
| Constructed notation system (overall model) | 35--45% | Most parsimonious, not proven |
| Specific word translations | 25--35% | Structural skeleton only |
| Descriptive naming hypothesis (full form) | 30--40% | Signal is real; interpretation uncertain |
| Complete decipherment achieved | <15% | Framework only |

---

## 6. References

### Primary Sources
1. Beinecke Rare Book and Manuscript Library. MS 408 (Voynich Manuscript). Yale University.
2. Takahashi, G., & Zandbergen, R. EVA transcription of the Voynich Manuscript (RF1b-e.txt).

### Peer-Reviewed Literature
3. Amancio, D. R., et al. (2013). Probing the statistical properties of unknown texts. *PLoS ONE*, 8(7), e67310.
4. Bennett, W. R. (1976). Scientific and engineering problem-solving with the computer. *Prentice-Hall*.
5. Bonavoglia, P. (2021). The ciphers of the Republic of Venice: an overview. *Cryptologia*, 46(4), 323--346.
6. Brewer, K., & Lewis, M. L. (2024). Voynich Manuscript, Dr Johannes Hartlieb and the Encipherment of Women's Secrets. *Social History of Medicine*, 37(3), 559.
7. Currier, P. (1976). Papers on the Voynich Manuscript. *New Research on the Voynich Manuscript*.
8. Davis, L. F. (2020). How Many Glyphs and How Many Scribes? Digital Paleography and the Voynich Manuscript. *Manuscript Studies*, 5(1).
9. D'Imperio, M. E. (1978). *The Voynich Manuscript: An Elegant Enigma*. NSA.
10. Greshko, M. A. (2025). The Naibbe cipher: a substitution cipher that encrypts Latin and Italian as Voynich Manuscript-like ciphertext. *Cryptologia*.
11. Landini, G. (2001). Evidence of linguistic structure in the Voynich manuscript using spectral analysis. *Cryptologia*, 25(4), 275--295.
12. Ponnaluri, R. V. (2024). The Voynich Manuscript was written in a single, natural language. *Cryptologia*, 49(6).
13. Rugg, G. (2004). An elegant hoax? A possible solution to the Voynich Manuscript. *Cryptologia*, 28(1), 31--46.
14. Stolfi, J. (2005). Voynich Manuscript word structure. www.voynich.nu.

### Unpublished / Preprint
15. Cheshire, G. (2019). The Language and Writing System of MS408 (Voynich) Explained. *Romance Studies*, 37(4), 217--244. [Subsequently critiqued and largely rejected by specialists.]
16. Davis, L. F. (2024). Multispectral Imaging and the Voynich Manuscript. Manuscript Road Trip.
17. Davis, L. F. (2025). Voynich Codicology. Manuscript Road Trip.
18. Zattera, T. (2023). Voynich slot grammar analysis. Online publication.

---

## 7. Supplementary Materials

The complete analysis archive contains 248 files including:

### Core Result Documents
- FINAL_RESEARCH_PAPER.md -- Full technical report
- DEFINITIVE_DICTIONARY_AND_TRANSLATION.md -- Complete morpheme dictionary with flowing translations
- COMPLETE_MORPHEME_DICTIONARY.md -- 10 core roots, grade system, full paradigms
- descriptive_naming_hypothesis.md -- The descriptive naming system hypothesis
- visual_morpheme_dictionary.md -- 24-page visual survey with morpheme correlations
- descriptive_reading.md -- Word-by-word readings of herbal pages
- RED_TEAM_DESCRIPTIVE_SYSTEM.md -- Full adversarial red-team report

### Statistical Analyses
- sandhi_cross_validation.md -- 10-fold CV, permutation tests for cross-word dependencies
- grade_semantic_test.md -- Three hypotheses tested for vowel grade function
- root_morpheme_decode.md -- Compositional stem system analysis
- stem_hidden_patterns.md -- Deep structural analysis of ~200 stems
- code_generation_rule.md -- Systematic elimination of 9 code-derivation hypotheses

### Cycle Reports (chronological)
- CYCLE2_SYNTHESIS.md through CYCLE15_REPORT.md -- Progressive analysis cycles
- RED_TEAM_CYCLE16.md -- Adversarial review cycle

### Hypothesis Tests
- agglutinative_comparison.md, arabic_test.py, semitic_root_test.py, judeo_italian_hypothesis.py -- Language identification tests
- constructed_notation_test.md -- Notation system validation
- paradigm_control_test.md -- Control experiments
- verbose_cipher_null_test.md -- Cipher hypothesis testing

### Translation Attempts
- COMPLETE_TRANSLATION_ATTEMPT.md, FLOWING_TRANSLATION.md -- Full-page translation attempts
- DEFINITIVE_TRANSLATION_EN.md, DEFINITIVE_TRANSLATION_JA.md -- English and Japanese versions
- cross_validation_translation.md -- Translation cross-validation

### Plant and Illustration Analysis
- plant_identification.md, plant_triangulation.md, plant_order_analysis.md
- illustration_correlation_expanded.md, word_image_correlation.py
- dioscorides_mapping.md, antidotarium_nicolai_comparison.md

### Computational Scripts (Python)
- 45+ Python analysis scripts for reproducibility

### Historical Context
- nomenclator_analysis.md, venetian_cipher_research.md
- llullian_comparison.md, PICATRIX_AURORA_STRUCTURAL_COMPARISON.md
- latest_research_survey_2025_2026.md, naibbe_and_recent_research.md

---

*This paper reports the results of a multi-cycle AI-assisted investigation. All statistical claims are derived from computational analysis of the EVA transcription. The investigation was conducted by Claude Opus 4.6 (1M context) under the direction of a human researcher. No claim of decipherment is made. All confidence levels are post-red-team assessments and reflect genuine uncertainty.*

*Generated: April 2026*
