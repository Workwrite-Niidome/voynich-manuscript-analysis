# SH Morpheme Diagnosis and Revision

## Date: 2026-04-10

## The Problem

The blind prediction test showed sh=underground/root **FAILS** at 25% accuracy (0.5/2 for positive predictions, 43.8% for negative predictions). This is below chance. The cornerstone claim that sh encodes "underground/hidden (root)" does not survive blind testing.

This document diagnoses WHY it fails and proposes a revised interpretation.

---

## PART I: DIAGNOSIS -- Where Did sh=underground Come From?

### 1.1 Origin of the Claim

The sh=underground/root claim originated from two observations:

1. **shol appeared on pages with root illustrations** (e.g., f3r, f4r) -- but the expanded illustration correlation study (illustration_correlation_expanded.md) itself reported shol at 2.70% on LEAF pages vs 1.11% on ROOT pages. **shol was actually MORE frequent on leaf pages than root pages.** This counter-evidence was noted but rationalized away.

2. **Structural symmetry with ch-**: Since ch- was assigned to "above-ground/visible," sh- was assumed to be its opposite: "below-ground/hidden." This is an aesthetic assumption, not an empirical one.

3. **The PLANT_VOCABULARY_SYSTEM.md** stated shol="root" at 75% confidence, but this confidence was never empirically calibrated. It was a subjective estimate that became treated as established fact.

### 1.2 The Evidence That Was Ignored

The chol_discrimination_test.md already showed:

| Category | Mean shol% |
|----------|-----------|
| Root-prominent folios (n=44) | **0.99%** |
| Leaf-prominent folios (n=81) | **1.42%** |
| Mann-Whitney p | ~0.5 (not significant) |

shol is 0.70x on root pages vs leaf pages. **If shol meant "root," it should be HIGHER on root pages, not lower.** This was noted as "shol may mean something broader than root" but no revision followed.

### 1.3 Confirmation Bias Chain

The chain of error:
1. ch=visible/aerial was assigned first (plausible, given chol's leaf-page correlation)
2. sh was assumed to be ch's opposite (structural symmetry fallacy)
3. sh=underground was locked in as a "fact"
4. Counter-evidence (shol on leaf pages, failed predictions) was rationalized
5. The blind test exposed the failure unambiguously

---

## PART II: What Does sh- ACTUALLY Do?

### 2.1 Frequency Profile

From the comprehensive analysis (shol_analysis.py + sh_line_position_analysis.py):

**Total sh- words in corpus**: ~2,908 tokens
**Overall sh- frequency**: ~8.6% of herbal text, ~7.1% of recipe text

Top sh- words (entire corpus):
| Word | Count | Followed by |
|------|-------|-------------|
| shey | 339 | qokain(13), qokaiin(9), qokar(8) |
| shedy | 253 | qokedy(11), qokey(11), qokeedy(9) |
| shol | 166 | shol(6), daiin(6), aiin(4) |
| sheey | 139 | qokain(5), qokey(4), qokeey(4) |
| sho | 110 | chol(5), shol(5), ykeey(3) |
| shy | 96 | daiin(5), qokar(3), dchy(2) |
| sheol | 94 | shey(3), qokedy(2), okedy(2) |
| shor | 86 | shol(5), daiin(3), chor(2) |

### 2.2 The sh-to-qok Bigram Pattern (Smoking Gun)

What follows sh- words vs ch- words:

| Following prefix | After sh- | sh-% | After ch- | ch-% | sh/ch ratio |
|-----------------|-----------|------|-----------|------|-------------|
| **qok-** | 476 | **16.4%** | 505 | 8.5% | **1.93x** |
| **qo-** | 322 | **11.1%** | 372 | 6.2% | **1.77x** |
| **sh-** | 288 | **9.9%** | 315 | 5.3% | **1.87x** |
| ch- | 320 | 11.0% | 1051 | 17.6% | 0.62 |
| d- | 183 | 6.3% | 550 | 9.2% | 0.68 |
| l- | 84 | 2.9% | 299 | 5.0% | 0.58 |

sh- words are followed by **quantity/measurement markers (qok-)** at nearly 2x the rate of ch- words. And sh- words chain with other sh- words at 1.87x the rate that ch- words chain with sh- words.

Meanwhile, ch- words are followed by other ch- words (17.6%) -- self-describing sequences typical of descriptive text.

### 2.3 Line Position Analysis

| Metric | ch- | sh- |
|--------|-----|-----|
| Mean position in folio (0=start, 1=end) | 0.495 | 0.466 |
| Early third (0-0.33) | 34.4% | 35.8% |
| Middle third (0.33-0.67) | 32.1% | 34.1% |
| Late third (0.67-1.0) | 33.6% | 30.1% |

**sh- words are NOT concentrated later in the text.** If anything, they are slightly EARLIER than ch- words. This kills the "sh=preparation/use (late lines)" hypothesis.

But a subtler pattern emerges in the absolute line numbers:

| Line | ch-% | sh-% | ch/sh ratio |
|------|------|------|-------------|
| 1 | 13.8% | **13.2%** | 1.04 |
| 2 | 17.5% | 7.2% | 2.41 |
| 3 | 19.7% | 6.2% | 3.19 |
| 4 | 20.4% | 7.2% | 2.85 |
| 5 | 17.2% | 7.7% | 2.24 |
| 6-12 | ~19% | ~8% | ~2.3 |
| 13+ | ~20% | ~7% | ~3.0 |

**Line 1 is anomalous**: sh- is nearly equal to ch- (13.2% vs 13.8%), but from line 2 onward ch- jumps to 17-20% while sh- drops to 6-8%. The sh/ch ratio is 0.96 on line 1 but 0.43 on lines 2+, making it **2.23x higher on line 1.**

### 2.4 chol vs shol on Line 1

| Word | Line 1 rate (among ch-/sh- words) | Lines 2+ rate |
|------|----------------------------------|---------------|
| chol | **2.5%** of ch-words | 10.3% of ch-words |
| shol | 10.3% of sh-words | 10.9% of sh-words |

chol is depleted on line 1 (the title/header line) by 4x. shol maintains its rate. This suggests:
- chol is a **descriptive** word (leaf/foliage) used in the body text describing the plant
- shol is used consistently both in titles and descriptions -- consistent with a **substance/ingredient** marker

### 2.5 Recipe Section Test

If sh=preparation, sh should be ENRICHED in recipe sections. Result:

| Section | ch-% | sh-% | ch/sh | sh enrichment |
|---------|------|------|-------|---------------|
| Herbal | 18.7% | 8.6% | 2.16 | baseline |
| Recipe | 16.8% | 7.1% | 2.38 | **0.82x (DEPLETED)** |

sh- is actually **less** frequent in recipe sections than in herbal sections. This eliminates "sh=preparation/cooking" as a meaning.

### 2.6 First-Word sh Content

Folios where the first word (plant name) contains "sh": n=24 (20% of herbal folios).
Mean sh-% on these folios: 9.2%
Mean sh-% on folios without sh in first word: 8.4%
Ratio: 1.10x (negligible enrichment)

The presence of sh in the plant name does NOT strongly predict higher sh- frequency throughout the page. This argues against sh encoding a fixed plant-part category.

---

## PART III: Revised Model -- What Is sh-?

### 3.1 Hypotheses Tested

| Hypothesis | Prediction | Result | Verdict |
|-----------|-----------|--------|---------|
| sh = underground/root | sh+ pages show prominent roots | 25% accuracy | **REJECTED** |
| sh = preparation/use | sh concentrates in late lines | sh is EARLIER (0.466 vs 0.495) | **REJECTED** |
| sh = preparation/use | sh enriched in recipe sections | sh DEPLETED in recipes (0.82x) | **REJECTED** |
| sh = ingredient/substance marker | sh followed by qok- (quantity) | **1.93x enrichment** | **SUPPORTED** |
| sh = naming/classification | sh enriched on line 1 | **2.23x enrichment on line 1** | **SUPPORTED** |

### 3.2 Proposed New Interpretation: sh- = SUBSTANCE/INGREDIENT Marker

The data supports sh- as marking **substances, ingredients, or named entities** -- the things being measured, combined, or referenced, as distinct from ch- which marks **descriptions of visible/physical features**.

Evidence:
1. sh- words are followed by qok- (quantity markers) at 1.93x the rate of ch- words
2. sh- words chain with other sh- words (ingredient lists)
3. sh- is concentrated on line 1 (the naming/title line) relative to ch-
4. sh- does NOT correlate with root illustrations
5. sh- is NOT enriched in recipes (argues against "preparation")
6. The most common sh- words (shey, shedy) are consistently followed by quantity words (qokain, qokedy, qokar, qokey)

### 3.3 The ch/sh Contrast Revised

| Feature | ch- | sh- |
|---------|-----|-----|
| **Function** | Visual/physical description | Substance/ingredient reference |
| **Typical context** | "the [ch-leaf] of the [ch-flower]..." | "[sh-substance] [qok-amount]..." |
| **Line 1 rate** | Low (naming is not visual) | High (naming IS substance reference) |
| **Self-chaining** | ch-ch (descriptive sequences) | sh-sh (ingredient lists) |
| **Followed by qok-** | 8.5% | 16.4% |
| **Visual prediction** | Correlates with leaf prominence | Does NOT correlate with any specific visual feature |

### 3.4 What shol Specifically Means

shol = sh + ol (substance marker + default suffix)

Under the old model: "root" (underground part)
Under the new model: "substance/material" or "ingredient" -- the primary material of the plant being discussed

This explains:
- Why shol appears on LEAF pages as much as ROOT pages (the substance of the plant is discussed regardless of which part is illustrated)
- Why shol appears consistently on line 1 (naming the substance)
- Why shol appears alongside chol (chol = the leaf [visual], shol = the substance/material [functional])

---

## PART IV: Revised Blind Predictions

### 4.1 What Changes

Under the new model, sh- makes NO visual predictions about illustrations. sh- encodes functional/pharmaceutical information, not visual/anatomical information. Therefore:

- "sh present in first word" no longer predicts "roots prominent in illustration"
- "sh absent" no longer predicts "no prominent roots"
- Instead, sh- presence in the body text predicts: "this entry discusses specific ingredients with quantities"

### 4.2 Re-Scoring the 10 Folios

**Predictions that change:**

| Old Prediction | Old Result | Revised Under New Model |
|---------------|------------|------------------------|
| f26r: Roots prominent (sh in psheoky) | MISS | WITHDRAWN -- sh does not predict visual features |
| f33r: Roots prominent (sh in tshdar) | PARTIAL | WITHDRAWN |
| f22r: No prominent roots (no sh) | MISS | WITHDRAWN |
| f28r: No prominent roots (no sh) | MISS | WITHDRAWN |
| f31r: No prominent roots (no sh) | MISS | WITHDRAWN |
| f34r: No prominent roots (no sh) | MISS | WITHDRAWN |
| f36r: No prominent roots (no sh) | PARTIAL | WITHDRAWN |

By withdrawing the failed sh-based visual predictions, the remaining predictions become:

### 4.3 New Prediction Type: sh+qok Ingredient Pattern

For the folios with sh in the first word, the revised model predicts: "this folio should contain sh-word + qok-word bigrams (ingredient + quantity pairs)."

| Folio | First word | sh in first word? | sh+qok bigrams found | Prediction |
|-------|-----------|-------------------|---------------------|------------|
| f20r | kdchody | No | 0 | N/A |
| f22r | pol | No | 0 | N/A |
| f26r | psheoky | Yes | 1 | HIT |
| f28r | pchodar | No | 0 | N/A |
| f29r | posaiin | No | 1 | N/A |
| f31r | keedey | No | 3 | N/A |
| f33r | tshdar | Yes | 1 | HIT |
| f34r | pcheoepchy | No | 1 | N/A |
| f36r | pchadn | No | 0 | N/A |
| f38r | tolor | No | 0 | N/A |

Both folios with sh in the first word contain sh+qok bigrams. However, folios without sh in the first word also contain them (f29r, f31r, f34r), so the predictive power is modest.

### 4.4 Revised Overall Accuracy

Removing the 9 sh-related visual predictions (2 positive, 7 negative) from the 37 total:

- Remaining testable predictions: 28
- Remaining HITs: 23 (all the non-sh predictions that already worked)
- Remaining MISSes: 4 (the yd- and oiin misses, plus f38r no-emphasis miss)
- Remaining PARTIALs: 1

**Revised accuracy: 23.5/28 = 83.9%** (up from 67.6%)

But this is cheating -- we removed the failures. The honest statement is: **the sh-based predictions were not valid predictions because sh does not encode visual/anatomical information.**

---

## PART V: Implications for the Overall Model

### 5.1 What Survives

| Morpheme | Meaning | Blind Test Result | Status |
|----------|---------|------------------|--------|
| ch- | Visual/aerial/leaf description | 4/4 = 100% | SURVIVES (but high base rate) |
| -yd- | Divided/dissected leaves | 8/10 = 80% | SURVIVES (marginal) |
| oiin | Flower-related | 6/8 = 75% | SURVIVES (marginal) |
| sh- | ~~Underground/root~~ | 0.5/2 = 25% | **REVISED: Substance/ingredient marker** |

### 5.2 What This Means for the Ternary System

The PREFIX + ROOT + SUFFIX model survives, but the prefix meanings need revision:

| Prefix | Old Meaning | New Meaning | Confidence |
|--------|------------|-------------|------------|
| ch- | Above-ground/visible | Visual description (what you SEE) | 60% |
| sh- | Below-ground/hidden | Substance/ingredient (what you USE) | 45% |
| cth- | Fruit/seed | Possibly a sub-category of ch- or sh- | 40% |

The ch/sh contrast is not spatial (above vs below) but **functional** (descriptive vs operational). ch- words describe the plant. sh- words name the substances and are quantified.

### 5.3 Remaining Questions

1. **Why is sh- depleted in recipes?** If sh=ingredient, recipes should be full of ingredients. One possibility: recipe sections use DIFFERENT vocabulary for ingredients (perhaps the qo- or ok- prefix families), and sh- is specifically a herbal-section convention for naming plant substances.

2. **What are shor and shol specifically?** Under the new model, shor and shol could be different case/suffix forms of the same substance-stem sh+o, rather than "root" and "fruit." The -ol/-or alternation may indicate grammatical function (subject vs object) rather than different plant parts.

3. **Why is sh/ch nearly equal on line 1?** If line 1 functions as a title or header, it may name both the plant's substance (sh-) and its identifying features (ch-), explaining the balanced ratio.

### 5.4 Lessons for Voynich Analysis

1. **Structural symmetry is not evidence.** Assuming sh is the "opposite" of ch because they look like a pair was the core error. The relationship may be complementary rather than oppositional.

2. **Test negative predictions.** The sh=root claim survived unchallenged because nobody checked whether pages WITHOUT sh also show roots. They do, frequently.

3. **Bigram context is more informative than page-level correlation.** The sh+qok pattern (what follows sh-words) was more diagnostic than the sh-vs-illustration correlation (where sh-words appear). Text-internal structure beats text-illustration correlation.

4. **Lock confidence to empirical tests.** The original "75% confidence" for shol=root was never earned. Any confidence estimate should be pinned to a specific blind test result.

---

## Summary

| Question | Answer |
|----------|--------|
| Why did sh=underground/root fail? | shol is MORE frequent on leaf pages than root pages (0.70x). The claim was based on structural symmetry with ch-, not data. |
| What does sh- actually correlate with? | sh- words are followed by qok- (quantity/measurement) at 1.93x the rate of ch-. sh/ch ratio is 2.23x higher on line 1 (headers). sh- does NOT correlate with root illustrations. |
| Is sh=preparation? | No. sh- is NOT enriched in recipe sections (0.82x) and NOT concentrated in late lines. |
| Is sh=later-in-entry (use vs description)? | No. sh- mean position (0.466) is actually slightly EARLIER than ch- (0.495). |
| What is sh-? | Most likely: a **substance/ingredient marker** -- marking the material being measured/referenced, as opposed to ch- which marks visual descriptions. |
| Does the revised model improve predictions? | It eliminates the false predictions (removing 9 wrong/partial scores), but does not yet generate new positive testable predictions. The model is more honest but less falsifiable. |
