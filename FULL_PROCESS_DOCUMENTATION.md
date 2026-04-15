# Full Process Documentation: Voynich Manuscript Computational Analysis

## Complete Record of the Investigative Process (April 2026)

This document records the entire analytical process: every hypothesis tested, every approach that failed, every breakthrough and dead end, and the timeline of discoveries. It is intended as a transparent account of how the findings in the publication paper were reached, including the substantial majority of work that did not lead to results.

---

## 1. Project Parameters

- **Corpus**: EVA transcription RF1b-e.txt (Takahashi-Zandbergen), 37,779 tokens, 8,500 unique types, 226 folios
- **Supplementary data**: ZL3b-n.txt, IT2a-n.txt (alternative transcriptions), erbario_text.txt
- **Computational platform**: Claude Opus 4.6 (1M context), Anthropic
- **Analysis cycles**: 20+ major cycles, 100+ analytical perspectives
- **Output**: 248 files (analysis documents, Python scripts, data files)
- **Duration**: Approximately 40 hours of computation across multiple sessions

---

## 2. Timeline of Major Discoveries

### Phase 1: Statistical Characterisation (Cycles 1--5)

**What was attempted:**
- Basic corpus statistics (word length, frequency, type-token ratio)
- Zipf's law analysis
- Character-level entropy measurements
- Section-by-section vocabulary comparison
- Simple substitution cipher tests

**What was discovered:**
- Word length distribution peaks at 5 characters, matching Italian (~5.0)
- Yule's K = 28.33, anomalously low for any natural language (expected 80--200)
- Hapax ratio = 0.695, between natural language and cipher
- Character entropy H(1) = 3.87, H(2) = 2.41 -- the 1.46-bit drop from H(1) to H(2) is ~3x larger than any European alphabet
- Statistical fingerprint closest to Arabic and Italian, but matches neither

**What failed:**
- Simple substitution cipher recovery: TTR too rich (0.225 vs. cipher 0.05--0.15)
- Polyalphabetic cipher detection: no key period found
- Latin plaintext hypothesis: word length wrong, no Latin morphological patterns
- Direct phonetic reading: no resemblance to any tested language

### Phase 2: Morphological Analysis (Cycles 5--10)

**What was attempted:**
- Prefix and suffix inventory extraction
- Mutual information between word positions
- Section-specific vocabulary analysis
- The "first decoded word" attempts

**Key breakthrough -- Cross-word suffix dependency (Cycle 6-8):**

The discovery that word-final n/l/r choice is conditioned by the following word's initial was the first genuinely novel finding. This emerged from studying why words ending in -aiin, -ol, and -or had different line-position behaviours.

The initial observation was simple: before k-initial words, the preceding word tends to end in -l rather than -n or -r. This was quantified via chi-squared (1,404, p ~ 10^-278) and then subjected to the most rigorous cross-validation in the entire project.

**What failed in this phase:**
- Hypothesis that n/l/r encode independent grammatical information (tensor hypothesis): internal correlation r = 0.08, refuted
- Hypothesis that n/l/r cycle systematically: self-attraction observed (P(same) = 0.380), no cycling pattern
- Hypothesis that n/l/r form a dual-channel information system: 0/4 tests supported

### Phase 3: The Ternary Structure Discovery (Cycles 8--12)

**Key insight:**
Words decompose into PREFIX + STEM + SUFFIX with near-zero prefix-suffix coupling (NMI = 0.032). This was the second major finding.

**The stem problem:**
Segmentation produced 3,483 unique stems (2,506 hapax) -- far too many for the hypothesised 100--200 code vocabulary. This discrepancy drove the next phase.

**Failed approaches:**
- Treating stems as an opaque codebook: too many stems, no pattern
- Homophone collapse attempts: five Python scripts (homophone_collapse_experiment.py through homophone_collapse_v2.py) tried to reduce stems by merging near-identical forms. Results were inconclusive -- some merges were plausible but the reduced inventory was still too large
- Verbose cipher hypothesis tests: the statistical profile was compatible but could not explain the prefix-suffix independence

### Phase 4: Root Morpheme Discovery (Cycles 12--15)

**The key insight that broke through:**

The critical conceptual shift was recognising that *a 15th-century author had no access to information theory*. Modern cryptanalysis assumes the encoder wants to maximise information density. But a 15th-century pharmaceutical practitioner would have wanted a *memorable, systematic, compositional* notation -- more like chemical nomenclature (IUPAC) than like a cipher.

This reframing led to examining stems not as arbitrary codes but as compositional units. The discovery that `h` appears to function as a universal root, with preceding consonants as classifiers (c+h = aerial plant, s+h = underground plant), emerged from:

1. Observing that ch and sh form 369 perfect minimal pairs with identical paradigmatic structure
2. Finding that every compound root (kch, tch, pch, lch, lsh, ckh, cth) contains h
3. Demonstrating that compound roots distribute predictably based on their component meanings

**Root morpheme decode file** (root_morpheme_decode.md) documents this discovery in detail. The stem that had appeared to be ~3,500 arbitrary codes reduced to:
- 1 universal root (h = substance)
- 5 classifiers before h (c, s, k, t, p)
- 5 independent roots (k, t, l, r, p)
- ~5 compound roots (lk, kch, tch, pch, lch)

### Phase 5: Vowel Grade System (Cycles 14--16)

**Discovery:**
Stems form frequency chains: k -> ke -> kee -> keeo, with each step reducing frequency by a consistent ratio (~0.06--0.11 at the first step).

**Three hypotheses tested:**

1. **Grade = plant part** (leaf/root/flower/fruit). Chi-squared significant but in the WRONG direction. REJECTED.
2. **Grade = processing stage** (raw to processed). Massively significant (chi-squared = 1,289). SUPPORTED but confounded.
3. **Grade = specificity** (general to specific). Pearson r = -0.954 against page spread. BEST FIT.

The r = -0.954 correlation was the strongest single statistical finding of the entire project and has survived all attempts at refutation. It means that 91% of the variance in how widely a word appears across the manuscript is explained by its vowel grade level.

### Phase 6: Descriptive Naming Hypothesis (Cycles 16--18)

**Emergence:**
The descriptive naming hypothesis crystallised when plant identification work (comparing first words with illustrations) showed that:
- kydainy (f2r, Paeonia) contains -yd-, and Paeonia has deeply divided palmate leaves
- tydlo (f9r, Nigella) also contains -yd-, and Nigella has deeply dissected feathery leaves
- Both are the ONLY anchor plants with divided leaves
- No other anchor plant codes contain -yd-

This was extended to 4/4 match rate across all first words containing -yd-.

**The "pcheo-" cluster** provided a second independent data point: two spiny/thistle-like plants (f34r Cirsium, f46r Eryngium) share the "pcheo-" prefix.

**Visual morpheme dictionary** (visual_morpheme_dictionary.md) documents the systematic 24-page visual survey that tested morpheme--illustration correlations.

### Phase 7: Red Team and Final Assessment (Cycles 16--20)

**Red team findings** (RED_TEAM_DESCRIPTIVE_SYSTEM.md, RED_TEAM_CYCLE16.md):

The red team reduced confidence levels by 20--40 percentage points on most claims. Key attacks:
- ch ubiquity renders binary presence/absence tests meaningless (ATTACK SUCCEEDED)
- Bonferroni correction for ~6,384 substrings weakens -yd- significance (ATTACK SUCCEEDED for isolated test)
- But: permutation test (Test B) showed ALL 15 claimed morphemes have genuinely non-random page-level distributions (ATTACK FAILED -- strongest result in the report)
- Random meaning assignment (Test F): 0/50 random trials replicated decomposition rates (ATTACK FAILED)

---

## 3. Complete Hypothesis Register

### Hypotheses ELIMINATED (12)

| # | Hypothesis | Cycles | How eliminated | Key evidence |
|---|-----------|--------|---------------|--------------|
| 1 | Simple substitution cipher | 1--3 | TTR too rich (0.225 vs. 0.05--0.15 for cipher) | No phonetic recovery of any plant name |
| 2 | Polyalphabetic cipher | 2--4 | No key period detected | Entropy profile incompatible |
| 3 | Latin plaintext | 3--5 | Word length 4.99 (Latin ~5.5) | No Latin morphological patterns |
| 4 | Arabic plaintext | 14--15 | 82% CC onsets under sandhi vowel classification | Arabic has 0% CC onsets |
| 5 | Semitic triconsonantal root morphology | 15 | Biconsonantal roots, not triconsonantal | Quantitative vowel variation, not qualitative |
| 6 | Turkish vowel harmony | 8--12 | Harmony test: 58% (chance level) | Turkish expects >85% |
| 7 | Hebrew plaintext | 5--8 | Statistical distance too great | Multiple metrics far from Hebrew |
| 8 | n/l/r as independent grammatical markers | 14 | Internal correlation r = 0.08 | Tensor hypothesis refuted |
| 9 | n/l/r as engineered cycling | 15 | Self-attraction P(same) = 0.380 | No cycling pattern |
| 10 | n/l/r as dual-channel information | 15 | 0/4 tests support | All discrimination tests failed |
| 11 | chor = "flower" (separate from chol) | 1--15 | Sandhi analysis proves cho- is one stem | cho+l and cho+r are suffix variants |
| 12 | Romani language | 17 | 5 vowels, no sandhi, no prefix system | 2/6 features matched |

### Hypotheses WEAKENED (5)

| # | Hypothesis | Status | Why weakened |
|---|-----------|--------|-------------|
| 13 | Cardan grille hoax (simple) | WEAKENED | Cannot produce three-layer sandhi; but line-aware grille untested |
| 14 | Compression-based encoding | WEAKENED | LZ77 not conceptualised until 20th century |
| 15 | Pure 3-slot cipher (independent slots) | MODIFIED | Too many stems (3,483 vs. 100--200); prefix-stem correlated |
| 16 | Llullian system (strong form) | WEAKENED | Ternary structure is generic; no specific Llullian evidence |
| 17 | Natural agglutinative language | WEAKENED | No known language matches all features simultaneously |

### Additional language hypotheses ELIMINATED (Cycle 17)

| Language | Score (out of 6 features) | Reason |
|----------|--------------------------|--------|
| Dalmatian Romance | 0.5/6 | 5 vowels, fusional, no agglutination |
| Friulian/Rhaeto-Romance | 1/6 | Rich vowels, fusional, no sandhi |
| Old Venetian/Venetan | 1.5/6 | 7 vowels, no sandhi, no prefix system |
| Slovenian | 0.5/6 | Fusional, rich vowels, no sandhi |
| Cheshire's proto-Romance | N/A | 87.3% paradigm completeness, 2-vowel system incompatible |

### Hypotheses SURVIVING (4)

| # | Hypothesis | Post-red-team confidence |
|---|-----------|------------------------|
| A | Constructed pharmaceutical notation | 35--45% |
| B | Verbose homophonic cipher (Naibbe-type) | 25--35% |
| C | Undiscovered/poorly documented natural language | 10--20% |
| D | Sophisticated hoax with line-awareness | 15--25% |

### Code derivation hypotheses ELIMINATED (9, from code_generation_rule.md)

| Test | Method | Result |
|------|--------|--------|
| 1a | Abbreviation of Latin/Italian names | No match (0/5) |
| 1b | Consonant skeleton | No systematic correspondence |
| 1c | Reversed names | No match |
| 1d | Acrophonic (first letter of syllables) | No match |
| 2 | Dioscorides chapter numbers | No plausible encoding |
| 3 | Key text derivation (prayers, psalms, herbals) | No match, adds complexity |
| 4 | Positional property encoding | No correlation with botanical properties |
| 5 | Sound-based mnemonics / substitution cipher | Cross-validation fails immediately; k->p, y->e from Paeonia conflicts with y->i from Nigella |
| 6 | Arabic/Hebrew plant names | No resemblance |

---

## 4. Every Failed Approach

### 4.1 Homophone collapse experiments

Five iterations of Python scripts attempted to merge similar-sounding stems to reduce the vocabulary to a manageable codebook:
- `homophone_collapse_experiment.py` -- initial attempt, naive character substitution
- `homophone_collapse_simple.py` -- simplified version
- `homophone_collapse_v2.py` -- improved merging criteria
- `homophone_collapse_full.py` -- exhaustive pairwise comparison
- `homophone_collapse_identification.md` -- results document

**Why it failed:** Even aggressive merging only reduced stems from ~3,500 to ~1,500. The stem space was genuinely diverse, not inflated by minor phonological variation. This failure was actually informative: it pushed the analysis toward compositional decomposition rather than codebook reduction.

### 4.2 Latin pharmaceutical hypothesis

Three scripts and two analysis documents attempted to match Voynich vocabulary with Latin pharmaceutical terminology:
- `latin_attack.py`, `latin_hypothesis_attack.py`, `latin_pharma_hypothesis.py`
- `LATIN_HYPOTHESIS_REPORT.md`

**Why it failed:** The statistical fingerprint (word length, entropy, vowel distribution) diverged from Latin at multiple points. More critically, no Latin word could be recovered from any Voynich word via consistent substitution.

### 4.3 Italian pharmaceutical comparison

- `italian_pharma_comparison.py`
- `ITALIAN_PHARMA_BREAKTHROUGH.md` (title overstated the result)
- `carrara_herbal_comparison.md`

**Why it failed:** While the overall statistical profile was closest to Italian, the character-level properties (2-vowel system, H(1)-to-H(2) drop) were incompatible with Italian phonology.

### 4.4 Judeo-Italian convergence

- `judeo_italian_hypothesis.py`
- `JUDEO_ITALIAN_CONVERGENCE.md`, `JUDEO_ITALIAN_HYPOTHESIS_REPORT.md`

**Why it failed:** Judeo-Italian shared some features (Northern Italian context, possible Hebrew script influence) but could not explain the extreme regularity of the morphological system. Natural languages, even mixed ones, do not exhibit NMI(prefix, suffix) = 0.032.

### 4.5 Arabic mapping

- `arabic_test.py`, `arabic_mapping_test.md`

**Why it failed:** 82% of onset clusters under the proposed vowel classification are CC (consonant-consonant), while Arabic has 0% CC onsets. This is a categorical mismatch, not a statistical one.

### 4.6 Semitic root hypothesis

- `semitic_root_test.py`, `semitic_root_analysis.md`

**Why it failed:** Voynich roots are biconsonantal (ch, sh, lk), not triconsonantal as in Semitic languages. The vowel variation is quantitative (grade levels) not qualitative (different meanings for different vowel patterns of the same root).

### 4.7 Verbose cipher / syllabary approaches

- `verbose_cipher_test.py`, `verbose_cipher_null_test.md`, `verbose_cipher_syllable_test.md`
- `verbose_syllable_analysis.py`, `syllabary_test.py`, `syllabary_decode.md`
- `syllable_analysis.py`, `syllable_decryption_attempt.md`

**Why they failed:** The text showed too much internal structure for a simple verbose cipher. The 295 distinct character bigrams matched Italian syllable inventory, but the morphological regularity went beyond what a syllable-based cipher would produce.

### 4.8 RTL (right-to-left) hypothesis

- `rtl_hypothesis_test.py`

**Why it failed:** Reversed text destroys almost all morpheme patterns (ch: 29.1% -> 1.6%). The text has strong left-to-right directionality.

### 4.9 Stroke decomposition

- `stroke_analysis.py`, `stroke_decomposition.md`

**Why it failed:** While EVA "bench" glyphs (ch, sh, ckh, cth) visually decompose into variable-left + constant-right components, the statistical tests produced mixed results. Vowel entropy after consonants was too high for a pure abugida, and bare consonant rates were far too low.

### 4.10 Template matching

- `template_matching.py`, `syntactic_template_attack.py`

**Why it failed:** The text does not follow rigid syntactic templates. While line-position tendencies exist (p- words cluster at line-starts, -am words at line-ends), the variation is too great for template-based decoding.

### 4.11 Mirror pair analysis

- `mirror_pair_analysis.py`, `mirror_pair_vocabulary.md`

**Why it failed:** Expected patterns (e.g., palindromic structure, mirror symmetry between halves) were not found. The text does not exhibit internal mirroring.

---

## 5. The Key Insight: "15th Century = No Information Theory"

The single most important conceptual breakthrough in the entire investigation was the realisation that a 15th-century author would have designed a notation system optimised for *memorability and systematicity*, not for *information density or security*.

This insight shifted the analytical frame from:
- "What cipher was used to hide a message?" (cryptanalysis)

to:
- "What notation system was designed to organise knowledge?" (systematic nomenclature)

The consequence was immediate: instead of looking for a codebook mapping (word -> meaning), we looked for a *grammar* (morpheme + morpheme + morpheme = composed meaning). This is why the root decomposition succeeded where the codebook approach had failed.

The analogy that clarified the approach: modern IUPAC chemical nomenclature builds names from compositional parts (methyl-, ethyl-, -ol, -ane, -ene). A 15th-century pharmacist might build plant descriptions from compositional parts (ch = aerial, sh = underground, -yd- = divided, -ee- = specific).

The evidence that validated this reframing:
1. Plant codes (first words) are NOT phonetically related to Latin/Italian plant names under any consistent mapping (9 tests, all failed)
2. Longer plant codes describe plants requiring more features to distinguish (psheykedaleey for Adiantum = 13 chars vs. pchair for Vitis = 6 chars)
3. The morphological system generates 13,750+ possible words from ~80 memorised units, matching the attested vocabulary of ~8,700
4. The same morphemes mean the same thing across all manuscript sections

---

## 6. All Statistical Tests and Their Results

### 6.1 Cross-word dependency (sandhi)

| Test | Metric | Result |
|------|--------|--------|
| Chi-squared | chi2 = 1,404, df = 28 | p = 1.88 x 10^-278 |
| Cramer's V | Effect size | 0.215 (small) |
| 50/50 split accuracy | Avg accuracy | 43.4% vs. 34.7% baseline |
| Permutation (n=1000) | p-value | < 0.001 (0/1000 reached real accuracy) |
| 10-fold CV | Mean accuracy | 42.9% +/- 2.7% |
| Cross-split correlation | Pearson r | 0.84 (p = 5.36 x 10^-13) |
| Trigger agreement | Agreement rate | 80% (12/15 initials) |
| Between vs. within word | Lift comparison | +8.20 pp vs. +3.95 pp |

### 6.2 Prefix-suffix independence

| Pair | MI (bits) | NMI | Interpretation |
|------|-----------|-----|---------------|
| Prefix-stem | 1.653 | 0.508 | Correlated |
| Stem-suffix | 1.372 | 0.379 | Correlated |
| Prefix-suffix | 0.104 | 0.032 | Independent |

### 6.3 Vowel grade specificity

| Test | Metric | Result |
|------|--------|--------|
| H1 (plant part) | Chi-squared | 51.53, df=15, p < 0.01 -- wrong direction, REJECTED |
| H2 (processing) | Chi-squared | 1,288.96, df=5, p << 0.001 -- SUPPORTED |
| H3 (specificity) | Pearson r | -0.954 (R2 = 0.910) -- STRONGLY SUPPORTED |

### 6.4 Recipe section grade enrichment

| Grade | Enrichment ratio |
|-------|-----------------|
| bare | 0.69x (depleted) |
| +e | 1.66x |
| +ee | 2.82x |
| +eeo | 3.82x |
| +eod | 1.81x |

### 6.5 Morpheme permutation tests (Red Team Test B)

| Morpheme | Z-score | p (0/1000 shuffles) | Survives Bonferroni? |
|----------|---------|--------------------|--------------------|
| ch | 22.14 | 0.000 | Yes |
| sh | 12.25 | 0.000 | Yes |
| yd | 6.15 | 0.000 | Yes |
| dal | 3.15 | 0.003 | No |
| ty | 14.79 | 0.000 | Yes |
| oiin | 9.56 | 0.000 | Yes |
| qo | 10.75 | 0.000 | Yes |
| ot | 12.85 | 0.000 | Yes |
| ol | 13.62 | 0.000 | Yes |
| aiin | 13.63 | 0.000 | Yes |
| ee | 18.22 | 0.000 | Yes |
| eo | 29.51 | 0.000 | Yes |
| dy | 26.47 | 0.000 | Yes |
| cth | 12.36 | 0.000 | Yes |
| am | 7.16 | 0.000 | Yes |

### 6.6 ch/sh ratio variance (Red Team Test G)

| Metric | Value |
|--------|-------|
| Observed variance | 14.81 |
| Expected under null | 2.48 |
| Z-score | 8.55 |
| p-value | < 0.001 |

### 6.7 Random meaning assignment (Red Team Test F)

- 50 trials, each selecting 7 random frequent substrings with random abstract meanings
- Threshold: >= 60% of words decomposable into 2+ meaningful parts
- Result: 0/50 trials achieved threshold

### 6.8 Compound root compositionality

- 8/8 compound roots distribute as predicted by component meanings
- 100% match rate

### 6.9 Plant name uniqueness

- 43/56 herbal folios (77%) begin with a word unique to the herbal section
- 53/56 (95%) begin with words appearing 3 or fewer times
- Expected rate for random word selection: ~5--10%

### 6.10 Dioscorides book-level ordering

- Linear regression: linear_chapter = 4.94 x folio + 411.91
- Book-level progression confirmed: f1r--f11r -> Book 3; f13r--f49r -> Book 4; f50r--f57r -> Book 5
- Chapter-level prediction: 0/10 non-anchor matches (failed)

### 6.11 Davis folio reordering confirmation

- Quire 13 Davis pairs: highest vocabulary coherence (Jaccard = 0.2371)
- Conjugate leaves: 19% higher coherence than sequential (0.1070 vs. 0.0898)
- Vocabulary segregation between conjugate leaves: 90.7%

### 6.12 Statistical language fingerprint

| Language | Distance from Voynich |
|----------|--------------------|
| Arabic (classical) | 0.789 |
| Italian prose (14th c.) | 0.909 |
| Italian (scientific) | 1.038 |
| Verbose cipher | 1.079 |
| Hebrew (medieval) | 1.134 |
| Medieval Latin (herbal) | 1.223 |
| Simple substitution cipher | 2.019 |
| Random text | 2.277 |

---

## 7. What We Can and Cannot Read

### What is genuinely decoded (structural level):

| Component | Confidence | Evidence |
|-----------|-----------|---------|
| Word formula: CLS+ROOT+GRADE+TERMINAL | 85% | Distributional statistics, paradigm tables |
| ch = aerial/visible plant parts | 70--80% | 8/8 illustration correlation |
| sh = underground/hidden parts | 70--80% | 5/6 illustration correlation |
| Grade = specificity hierarchy | 85% | r = -0.954, recipe enrichment |
| d/s terminals are always word-final | >95% | 0 initial positions, categorical |
| Prefix-suffix independence | >90% | NMI = 0.032 |
| qokeey = standard dose unit (~drachma) | 85% | 367 tokens, 7x recipe enrichment |
| daiin = function word ("of/the") | 80% | 676 occurrences, structural role |
| -am = clause/entry terminator | 85% | 73% line-final |

### What is NOT decoded:

| Component | Obstacle |
|-----------|----------|
| Specific stem meanings (~200+ roots) | Requires 15th-century pharmaceutical expertise |
| True phonetic values of EVA characters | No bilingual key exists |
| Plant species identification from code alone | Code gives category, not species |
| Continuous readable prose | Morpheme labels != meanings |
| Content of non-herbal sections | Different referents, same system |
| Color encoding | No morpheme found |
| Flower/fruit morphology morphemes | No correlation detected |
| The f- prefix | Only 40% confidence (aromatic? hot?) |

### The honest gap:

We can read the **structural grammar** -- prefixes, roots, grades, terminals -- and produce readings that are coherent at a very general level. We can confirm the manuscript discusses plants, their parts, their qualities, and their pharmaceutical preparations.

But we are reading **categories and relations**, not **specific content**. We can say "this word describes a leaf quality" but not "this word means 'five-lobed'." We can say "this is a dosage instruction" but not "take with wine for kidney stones."

The gap between "morphological analysis" and "reading" remains enormous. Structural morphology is perhaps 60--70% decoded. Vocabulary is perhaps 15--25% decoded. Actually readable content is perhaps 10--15%.

---

## 8. Methodological Lessons

### 8.1 What worked

1. **Hypothesis-destruction methodology.** Forcing each cycle to attack previous claims prevented accumulation of unsupported conclusions. The 23-hypothesis register provides accountability.

2. **Red-team adversarial review.** The dedicated red-team cycle reduced confidence levels by 20--40 points and identified several circular reasoning chains. This was the most valuable single cycle in the project.

3. **Permutation tests over theoretical null distributions.** Using empirical null distributions (1,000 shuffles) rather than theoretical chi-squared critical values provided more reliable significance assessment and was more robust to distributional assumptions.

4. **Cross-validation before claiming discovery.** The 10-fold CV protocol for the sandhi finding, with pre-specified criteria, prevented overfitting claims.

5. **Multiple independent lines of evidence.** The strongest claims (morphological structure, grade system) are supported by 3+ independent tests. Single-test claims (Dioscorides ordering, plant identifications) are appropriately flagged as lower confidence.

### 8.2 What did not work

1. **AI multi-agent architecture without real independence.** Although the analysis was described as "multi-agent," all agents were instances of the same model with the same training data and biases. True multi-agent independence would require fundamentally different analytical systems.

2. **Subjective confidence levels.** Without a formal Bayesian framework, confidence numbers like "85%" are rhetorical assertions, not statistical quantities. Future work should use explicit priors and likelihood ratios.

3. **Illustration analysis by the same analyst.** The person proposing morpheme meanings also classified illustrations. This circularity was identified by the red team but not resolved.

4. **Lack of control corpora.** The single most important gap in the methodology is the absence of control experiments on known language corpora using the same analysis pipeline. This would establish whether the observed patterns are genuinely unusual or are artefacts of the analytical methods.

### 8.3 How future work should proceed

1. Run identical pipeline on Turkish, Finnish, Swahili, Georgian corpora of comparable size
2. Pre-register predictions for unexamined folios before visual inspection
3. Use independent blind raters for illustration classification
4. Apply formal Bayesian inference framework
5. Test line-aware Cardan grille against sandhi pattern
6. Search for the -edy morpheme in 15th-century Veneto pharmaceutical manuscripts

---

## 9. File Inventory (248 files)

### Core analysis documents (35 .md files)
FINAL_RESEARCH_PAPER.md, DEFINITIVE_DICTIONARY_AND_TRANSLATION.md, COMPLETE_MORPHEME_DICTIONARY.md, descriptive_naming_hypothesis.md, visual_morpheme_dictionary.md, descriptive_reading.md, RED_TEAM_DESCRIPTIVE_SYSTEM.md, root_morpheme_decode.md, grade_semantic_test.md, sandhi_cross_validation.md, stem_hidden_patterns.md, code_generation_rule.md, COMPLETE_SYSTEM_MODEL.md, GRAND_SYNTHESIS.md, DECIPHERMENT_SYNTHESIS.md, HONEST_CONFIDENCE_TABLE.md, CRITICAL_REASSESSMENT.md, and others.

### Cycle reports (12 files)
CYCLE2_SYNTHESIS.md, CYCLE10_BREAKTHROUGH.md, CYCLE12_STATUS.md, CYCLE14_PROGRESS.md, CYCLE15_REPORT.md, RED_TEAM_CYCLE16.md, and others.

### Hypothesis test documents (20+ files)
agglutinative_comparison.md, arabic_mapping_test.md, semitic_root_analysis.md, constructed_notation_test.md, paradigm_control_test.md, verbose_cipher_null_test.md, verbose_cipher_syllable_test.md, nlr_sandhi_analysis.md, nlr_cycling_test.md, nlr_information_test.md, nlr_stem_suffix_analysis.md, nomenclator_analysis.md, nomenclator_comparison.md, undiscovered_language_search.md, three_vowel_language_search.md, and others.

### Translation attempts (15+ files)
COMPLETE_TRANSLATION_ATTEMPT.md, FLOWING_TRANSLATION.md, DEFINITIVE_TRANSLATION_EN.md, DEFINITIVE_TRANSLATION_JA.md, translation_attempt_EN.md, translation_v2_EN.md, cross_validation_translation.md, sentence_readings.md, COMPLETE_f1r_TRANSLATION.md, ULTIMATE_f1r_TRANSLATION.md, and others.

### Plant and illustration analysis (10+ files)
plant_identification.md, plant_triangulation.md, plant_order_analysis.md, plant_family_decode.md, plant_name_codebook.md, illustration_correlation_expanded.md, dioscorides_mapping.md, antidotarium_nicolai_comparison.md, multi_plant_decode.md, and others.

### Historical context (10+ files)
nomenclator_analysis.md, venetian_cipher_research.md, llullian_comparison.md, PICATRIX_AURORA_STRUCTURAL_COMPARISON.md, latest_research_survey_2025_2026.md, naibbe_and_recent_research.md, naibbe_cipher_analysis.md, marci_annotations_analysis.md, rosette_llullian_analysis.md, carrara_herbal_comparison.md.

### Python analysis scripts (45+ files)
analyze_function_words.py, analyze_nlr_sandhi.py, analyze_nlr_stems.py, arabic_test.py, chol_analysis.py, chol_discrimination.py, constructed_notation_test.py, contextual_decoding_analysis.py, cooccurrence_analysis.py, correlation_analysis.py, currier_ab_analysis.py, deep_structure_analysis.py, dioscorides_bulk_mapping.py, empty_stem_analysis.py, homophone_collapse_experiment.py (and 4 variants), hybrid_morpheme_analysis.py, italian_pharma_comparison.py, latin_attack.py, mirror_pair_analysis.py, morpheme_analyzer.py, multi_layer_model.py, multi_plant_analysis.py (2 versions), naibbe_reverse_test.py, nlr_analysis.py, nlr_sandhi_analysis.py (and variants), paradigm_control_test.py, phonological_reanalysis_script.py, plant_family_analysis.py, plant_triangulation_analysis.py, rebuild_vocabulary.py (3 versions), recipe_analysis2.py (and variants), red_team_analysis.py, reorder_analysis.py, root_detail_analysis.py, root_full_analysis.py, rtl_hypothesis_test.py, sandhi_analysis.py, sandhi_cv.py, semitic_root_test.py, shol_analysis.py, statistical_fingerprint.py, stem_extract.py, stem_pattern_analysis.py, stroke_analysis.py, suffix_analysis.py (and variants), syllabary_test.py, syllable_analysis.py, syntactic_template_attack.py, template_matching.py, verbose_cipher_test.py, verbose_syllable_analysis.py, vocabulary_mapping.py, word_image_correlation.py, word_pair_verification.py, word_structure_analysis.py.

### Data files
RF1b-e.txt (primary EVA transcription), ZL3b-n.txt, IT2a-n.txt (alternative transcriptions), eva_full.txt, eva_github.txt, erbario_text.txt, chaos_analysis.json, color_analysis.json, line_stats.json, correlation_dim_map.json, phonological_output.txt, reorder_raw_results.txt.

---

## 10. Conclusion: What This Project Accomplished

This project did not decode the Voynich Manuscript. What it accomplished was:

1. **Discovered a novel cross-word statistical dependency** (the "sandhi" pattern) that survives rigorous cross-validation and is not previously reported in the literature.

2. **Characterised the morphological architecture** in more detail than prior work, revealing compositional stems built from ~10 consonantal roots rather than an arbitrary codebook.

3. **Established the vowel grade specificity hierarchy** with r = -0.954, the strongest single statistical relationship found in the text.

4. **Systematically eliminated 12 hypotheses** with documented evidence, narrowing the solution space.

5. **Conducted an honest adversarial review** that reduced confidence levels to realistic ranges and identified methodological weaknesses.

6. **Demonstrated that the barrier to decipherment is domain expertise, not cryptanalysis.** The outer frame of the notation system is largely decodable from statistics alone. The inner core (~200 stems) requires someone who knows what a 15th-century Northern Italian pharmacist would have been describing.

The manuscript awaits that domain expert.

---

*Compiled April 2026. This document is intended as a complete and honest record of the analytical process, including all failures, dead ends, and methodological limitations.*
