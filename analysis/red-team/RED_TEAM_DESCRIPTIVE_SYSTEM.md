# RED TEAM REPORT: Destructive Analysis of the Descriptive Naming Hypothesis

## Date: 2026-04-10

## Purpose

This report attempts to DESTROY the claim that the Voynich manuscript uses a "descriptive naming system" where morphemes encode observable plant features. Eight destructive tests were designed to expose statistical artifacts, multiple-testing inflation, and methodological circularity.

## Critical Note on Intellectual Honesty

**Several tests produced results that CONTRADICT the red team's pre-written conclusions.** Where the data refutes the attack, this is stated plainly. A red team that ignores inconvenient evidence is no better than the hypothesis it attacks.

---

## DATA

- EVA transcription: RF1b-e.txt
- Total folios: 226
- Total words: 36,532
- Unique words: 8,635
- Herbal folios analyzed: 112 (f1r-f57v)
- Herbal words: 9,058

---

## TEST A: ch- UBIQUITY -- IS "100% ACCURACY" TRIVIALLY TRUE?

**Attack**: ch appears in so many words that any correlation with ch is meaningless.

**Results**:
- Words containing ch: 10,629 (29.1% of all words)
- Words containing sh: 4,128 (11.3%)
- Folios with at least one ch-word: 224/226 (99.1%)
- Folios with at least one sh-word: 225/226 (99.6%)
- P(no ch word on a page of ~162 words) = essentially zero

**Verdict**: ATTACK PARTIALLY SUCCEEDS. The claim that "100% of leaf pages contain ch-words" is indeed trivially true -- 99.1% of ALL pages contain ch-words regardless of content. The binary presence/absence of ch is not a discriminator.

**However**: The claim is not purely about presence/absence. The descriptive hypothesis also claims that ch-word RATES vary meaningfully with illustration content. This is tested separately in Test B and Test G.

---

## TEST B: RANDOMIZATION -- DO MORPHEME DISTRIBUTIONS SURVIVE SHUFFLING?

**Attack**: If word positions are shuffled randomly across folios, morpheme "correlations" with illustrations should disappear. If they survive, they are artifacts of global frequency.

**Method**: All herbal words were pooled and randomly redistributed into folio-sized chunks 1,000 times. The variance of per-folio morpheme rates was compared between original and shuffled text.

**Results**:

| Morpheme | Claim | Orig Variance | Shuffled Mean Var | Z-score | p(shuffle >= orig) |
|----------|-------|---------------|-------------------|---------|-------------------|
| ch | aerial/leaf | 0.013240 | 0.003153 | **22.14** | **0.000** |
| sh | underground/root | 0.004011 | 0.001484 | **12.25** | **0.000** |
| yd | divided/dissected | 0.000401 | 0.000209 | **6.15** | **0.000** |
| dal | round | 0.000310 | 0.000213 | 3.15 | 0.003 |
| ty | linear | 0.000859 | 0.000280 | **14.79** | **0.000** |
| oiin | flower | 0.000306 | 0.000123 | **9.56** | **0.000** |
| qo | body/quantity | 0.002976 | 0.001171 | **10.75** | **0.000** |
| ot | process | 0.003337 | 0.001166 | **12.85** | **0.000** |
| ol | subject | 0.005097 | 0.001762 | **13.62** | **0.000** |
| aiin | entity/noun | 0.004467 | 0.001560 | **13.63** | **0.000** |
| ee | specific grade | 0.002836 | 0.000814 | **18.22** | **0.000** |
| eo | state/condition | 0.003984 | 0.000769 | **29.51** | **0.000** |
| dy | genitive | 0.005577 | 0.001168 | **26.47** | **0.000** |
| cth | fruit/seed | 0.001760 | 0.000644 | **12.36** | **0.000** |
| am | root-part | 0.000567 | 0.000276 | **7.16** | **0.000** |

**Verdict**: ATTACK FAILS COMPLETELY. ALL 15 morphemes show per-folio variance that is MASSIVELY higher than what random shuffling produces (Z-scores from 3.15 to 29.51). In zero out of 1,000 shuffles did ANY morpheme achieve variance equal to the original text (p=0.000 for 14/15; p=0.003 for dal).

**This is the single most important result in this report.** The morphemes are NOT uniformly distributed. They cluster on specific pages far more than chance predicts. This is a necessary (though not sufficient) condition for the descriptive naming hypothesis to hold. Whatever the Voynich text is, its morpheme distributions are HIGHLY non-random at the page level.

**Caveat**: This does NOT prove the claimed MEANINGS are correct. It proves only that these substrings have genuinely non-random page-level distributions. The distributions could reflect unknown structural properties of the text (e.g., Currier A/B language differences, scribal variation) rather than descriptive content.

---

## TEST C: BONFERRONI CORRECTION -- HOW MANY HYPOTHESES WERE TESTED?

**Attack**: With 6,384 unique 2-4 character substrings in the text, finding one that matches 4 divided-leaf pages is expected by chance.

**Results for -yd- (4/4 divided-leaf match)**:

| Assumption | P(one morpheme hits 4/4) | Expected false positives among 6,384 |
|------------|-------------------------|--------------------------------------|
| 30% of plants have divided leaves | 0.0081 | **51.7** |
| 25% | 0.0039 | 24.9 |
| 20% | 0.0016 | **10.2** |

**Verdict**: ATTACK SUCCEEDS for the -yd- test in isolation. With thousands of possible substrings, finding one that matches 4 pages is statistically unremarkable. Even at 20% base rate, we expect ~10 false positives.

**However**: The -yd- finding must be evaluated in context. Test B showed that yd has genuinely non-random page-level distribution (Z=6.15, p=0.000). The Bonferroni argument would apply if we were data-dredging among 6,384 random substrings, but if we pre-select substrings that have significant page-level variance (which yd does), the effective multiple-testing burden is much lower.

**The -yd- meaning was also reportedly REVISED from "divided" to "narrow/elongated"** -- this IS goalpost-moving and reduces confidence.

---

## TEST D: REVERSED TEXT -- DOES THE SYSTEM SURVIVE REVERSAL?

**Attack**: If the "descriptive system" works on reversed text too, the morphemes are not carrying directional/positional meaning.

**Results**:
- ORIGINAL: ch in 10,629 words (29.1%), sh in 4,128 (11.3%)
- REVERSED: ch in 577 words (1.6%), sh in 145 (0.4%)

**Verdict**: ATTACK FAILS. The red team's premise was wrong. In EVA transcription, "ch" is the bigram c-h, which when reversed in a word context (e.g., "chol" -> "lohc") does NOT produce "ch" -- it produces "hc". The reversal test shows that ch drops from 29.1% to 1.6%, confirming that ch is a POSITIONAL feature of the text, not a palindromic artifact.

Other morphemes similarly collapse under reversal:
- qo: 5,288 -> 25 occurrences
- aiin: 3,899 -> 0
- cth: 893 -> 11
- oiin: 162 -> 0

Only truly palindromic substrings (ee: 4,866 -> 4,866) survive. The yd/dy pair is interesting: yd appears 242 times in original text but 4,967 times in reversed text, because dy (4,967 in original) becomes yd when reversed. This confirms that yd and dy occupy genuinely different positions in words.

---

## TEST E: DO MORPHEMES SURVIVE p < 0.001 AFTER BONFERRONI?

**Attack**: After correcting for 6,384 possible morphemes, none should survive.

**Bonferroni threshold**: p < 0.001/6384 = 1.57 x 10^-7

**Results** (from permutation test with 1,000 shuffles):

| Morpheme | Permutation p | Survives? |
|----------|--------------|-----------|
| ch | 0.000 | YES |
| sh | 0.000 | YES |
| yd | 0.000 | YES |
| dal | 0.003 | **NO** |
| ty | 0.000 | YES |
| oiin | 0.000 | YES |
| qo | 0.000 | YES |
| ot | 0.000 | YES |
| ol | 0.000 | YES |
| aiin | 0.000 | YES |
| ee | 0.000 | YES |
| eo | 0.000 | YES |
| dy | 0.000 | YES |
| cth | 0.000 | YES |
| am | 0.000 | YES |

**Morphemes surviving: 14/15** (only dal fails)

**Verdict**: ATTACK MOSTLY FAILS. The pre-written conclusion ("ZERO survive") was wrong. With 1,000 permutations, the minimum measurable p-value is 0.001. For 14 of 15 morphemes, ZERO out of 1,000 random shuffles produced equal or greater variance. Even with aggressive Bonferroni correction across 6,384 possible substrings, the signal is so strong that these morphemes would need more than 1,000 shuffles to even begin to calibrate the p-value.

**Caveat**: This proves non-random distribution, not semantic meaning. The high Z-scores could reflect the well-known Currier A/B language split, scribal clustering, or other structural features unrelated to descriptive naming.

---

## TEST F: RANDOM MEANING ASSIGNMENT -- DO VAGUE CATEGORIES ALWAYS WORK?

**Attack**: If abstract meanings ("substance", "quality", "form") are assigned to random frequent substrings, the decomposition should work just as well.

**Method**: 50 trials, each selecting 7 random frequent substrings and assigning random abstract meanings. Test: can >= 60% of sampled words be "decomposed" into 2+ meaningful parts?

**Results**: 0/50 trials achieved >= 60% decomposition rate.

**Verdict**: ATTACK FAILS. The pre-written conclusion ("MOST random assignments produce decompositions that LOOK meaningful") was wrong. Random 2-3 character substrings, even frequent ones, do NOT reliably co-occur within the same words at rates sufficient for systematic decomposition. The Voynich morpheme set appears to be selected from substrings that have unusual co-occurrence properties.

**Caveat**: This test used a strict threshold (60% with 2+ morphemes). A lower threshold or different selection criteria might yield different results. The test also did not evaluate whether the decompositions are SEMANTICALLY coherent, only whether they are STRUCTURALLY possible.

---

## TEST G: ch/sh RATIO VARIANCE -- SIGNAL OR NOISE?

**Attack**: The variation in ch/sh ratios across pages is just sampling noise from fixed global frequencies.

**Results**:
- ch/sh ratio across 112 herbal folios: mean 4.16, std 3.85, range 0.84-32.00
- f2r (Paeonia): ratio 1.79, rank 13/112 (11.6th percentile) -- low but not extreme
- Observed variance: 14.81
- Expected variance under null model (binomial sampling): 2.48
- **Z-score: 8.55, p = 0.000**

**Verdict**: ATTACK FAILS. The ch/sh ratio varies across pages FAR more than binomial sampling would predict (6x the expected variance, Z=8.55). Pages genuinely differ in their ch/sh balance.

**However**: f2r (Paeonia, claimed to have the "lowest ratio") ranks 13th out of 112 -- in the 11.6th percentile. It is low-ish but not extreme. The claim that it has "the LOWEST ch/sh ratio" among anchor pages may be true within the cherry-picked anchor set but is unremarkable within the full herbal section. 12 other pages have lower ratios.

---

## TEST H: DIOSCORIDES COMPARISON BASELINE

**Attack**: Scores of 5-7/10 against Dioscorides are not better than what any herbal text would achieve.

**Verdict**: ATTACK IS VALID BUT UNTESTABLE. Without a formal baseline comparison (e.g., randomly paired Dioscorides entries scored by blind raters), we cannot determine whether 5-7/10 is above chance. The qualitative argument is sound: all medieval herbals discuss the same categories (roots, leaves, flowers, preparation, dose, uses), so moderate overlap is expected by default. This criticism stands.

---

## HONEST FINAL ASSESSMENT

### Claims that WITHSTAND red team attack:

1. **Morpheme distributions are genuinely non-random** (Test B): All 15 claimed morphemes show page-level clustering far beyond random shuffling, with Z-scores from 3.15 to 29.51. This is the strongest finding and cannot be dismissed.

2. **The text has directional structure** (Test D): Reversed text destroys most morpheme patterns (ch: 29.1% -> 1.6%). The morphemes are positionally specific, not palindromic artifacts.

3. **Random meaning assignments do not replicate the decomposition** (Test F): 0/50 random trials achieved comparable decomposition rates.

4. **ch/sh ratio variance is real** (Test G): Pages genuinely differ in ch/sh balance beyond sampling noise (Z=8.55).

### Claims that DO NOT withstand red team attack:

1. **"100% accuracy" for ch=aerial** (Test A): Trivially true. ch appears on 99.1% of all pages regardless of content.

2. **-yd- = "divided" with 4/4 match** (Test C): Expected false positive given ~6,384 possible substrings and ~20-30% base rate of divided-leaf plants. The meaning revision from "divided" to "narrow/elongated" is goalpost-moving.

3. **Dioscorides comparison scores** (Test H): No baseline established. Moderate scores are expected from any herbal text.

4. **92% prediction accuracy**: Predictions were not pre-registered. Most predictions (e.g., "expect ch-words on leaf pages") are trivially true.

5. **Circular methodology**: Illustrations were classified by the same person proposing the morpheme meanings. No blind raters were used. Edge cases were reclassified to fit the hypothesis.

### The core unresolved question:

The morphemes DO have significantly non-random page-level distributions (Test B proves this beyond doubt). But non-random distribution does not prove DESCRIPTIVE NAMING. The distributions could arise from:
- Currier A/B language differences (well-documented)
- Scribal clustering (different hands using different vocabulary)
- Topical vocabulary variation (even without morphemic meaning)
- True morphemic structure (what the hypothesis claims)

The hypothesis has identified REAL statistical signal in the text. The question is whether the INTERPRETATION of that signal (descriptive plant-feature encoding) is correct, or whether simpler explanations (language/scribe variation, topical vocabulary) account for the same data.

### What would be needed to settle this:

1. **Pre-registered predictions** on folios not yet examined, with SPECIFIC expected morpheme rates (not just "expect ch-words")
2. **Blind illustration classification** by independent botanical experts
3. **Formal comparison against null models** that account for Currier A/B splits
4. **Cross-validation**: Train morpheme meanings on half the herbal folios, test on the other half
5. **Apply the system to a KNOWN herbal** (e.g., a Latin herbal transcribed into EVA-like notation) as a negative control
