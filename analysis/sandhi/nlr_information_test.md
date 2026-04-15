# Voynich Manuscript n/l/r Suffix Information Analysis

## Overview

- **Total words parsed**: 35817
- **Words ending in n/l/r**: 16423 (45.9% of all words)
- **Suffix distribution**: n=5781 (35.2%), l=5350 (32.6%), r=5292 (32.2%)

---
## 1. Dual-Channel Hypothesis: Entropy Analysis

If the n/l/r suffix sequence carries its own independent message, its entropy
should decay with context order like natural language (not like random data).

- **Maximum entropy (uniform ternary)**: 1.5850 bits/symbol
- **H(0) unigram entropy of n/l/r sequence**: 1.5838 bits/symbol

### Conditional Entropy Decay

| Order k | Voynich n/l/r | Random Ternary | NL-like Markov |
|---------|---------------|----------------|----------------|
| 0 (H0)  | 1.5838        | 1.5849          | 1.5351          |
| 1       | 1.5764        | 1.5848          | 1.5008          |
| 2       | 1.5704        | 1.5842          | 1.5002          |
| 3       | 1.5646        | 1.5827          | 1.4989          |
| 4       | 1.5573        | 1.5786          | 1.4933          |
| 5       | 1.5412        | 1.5664          | 1.4784          |

### Entropy Drop Summary

- **Voynich n/l/r drop H0->H1**: 0.0075 bits (0.5% reduction)
- **Voynich n/l/r drop H0->H5**: 0.0426 bits (2.7% reduction)
- **Random ternary drop H0->H1**: 0.0001 bits
- **NL-like Markov drop H0->H1**: 0.0342 bits

**Finding**: The n/l/r sequence shows minimal entropy reduction, near-random.
This weakens the dual-channel hypothesis.

---
## 2. Mutual Information: Stem vs. Suffix

- **MI(stem, suffix)**: 0.9378 bits
- **H(suffix)**: 1.5838 bits
- **H(stem)**: 8.2668 bits
- **Normalized MI**: 0.5921

**Finding**: High NMI -- strong dependence. Against independent channel.

### Top 15 Stems by Suffix Bias (freq >= 10)

| Stem | Total | n | l | r | Dominant % |
|------|-------|---|---|---|------------|
| taii | 44 | 44 | 0 | 0 | 100% |
| soii | 16 | 16 | 0 | 0 | 100% |
| chodaii | 38 | 38 | 0 | 0 | 100% |
| daiii | 20 | 20 | 0 | 0 | 100% |
| shaii | 20 | 20 | 0 | 0 | 100% |
| cheaii | 16 | 16 | 0 | 0 | 100% |
| qodaii | 39 | 39 | 0 | 0 | 100% |
| shodaii | 19 | 19 | 0 | 0 | 100% |
| chaii | 46 | 46 | 0 | 0 | 100% |
| qotaii | 79 | 79 | 0 | 0 | 100% |
| chotaii | 10 | 10 | 0 | 0 | 100% |
| chokaii | 15 | 15 | 0 | 0 | 100% |
| choaii | 11 | 11 | 0 | 0 | 100% |
| sheaii | 12 | 12 | 0 | 0 | 100% |
| oraii | 32 | 32 | 0 | 0 | 100% |

- **Average dominant suffix % across frequent stems**: 73%
  (expected for random: 33%, for fully determined: 100%)

---
## 3. Section-Dependent Entropy Rates

| Section | Count | n% | l% | r% | H(0) | H(1) | H(2) | Drop H0->H1 |
|---------|-------|----|----|----|------|------|------|-------------|
| herbal_a | 4232 | 35% | 29% | 35% | 1.580 | 1.572 | 1.567 | 0.008 |
| astronomical | 1147 | 23% | 37% | 40% | 1.545 | 1.527 | 1.521 | 0.018 |
| biological | 2733 | 34% | 43% | 23% | 1.539 | 1.535 | 1.528 | 0.004 |
| recipe | 6740 | 39% | 31% | 30% | 1.575 | 1.571 | 1.566 | 0.004 |
| other | 1571 | 30% | 28% | 42% | 1.560 | 1.550 | 1.535 | 0.010 |

- **Range of H(0) across sections**: 0.040 bits
- **Range of H(1) across sections**: 0.045 bits
- **Finding**: Entropy rates similar across sections (uniform behavior).

---
## 4. Ternary Encoding Capacity

- **Raw capacity (uniform ternary)**: 1.5850 bits/symbol
- **Effective capacity H(X|X_i-1,X_i-2)**: 1.5704 bits/symbol
- **Efficiency**: 99.1%

- **Average n/l/r symbols per page**: 161.0
- **Average effective bits per page**: 252.8
- **Total n/l/r symbols**: 16423
- **Total effective bits in manuscript**: 25791

- **Equivalent English characters (~5 bits/char)**: ~5158
- **Equivalent English words (~25 bits/word)**: ~1032

---
## 5. Numeric / Base-3 Encoding Test

### 5a. Autocorrelation (mapping n=0, l=1, r=2)

| Lag | Match Rate | Expected (random) |
|-----|------------|-------------------|
| 1 | 0.3814 | 0.3333 |
| 2 | 0.3774 | 0.3333 |
| 3 | 0.3733 | 0.3333 |
| 5 | 0.3767 | 0.3333 |
| 10 | 0.3692 | 0.3333 |

- Consecutive increases: 5117
- Consecutive decreases: 5042
- Consecutive equals: 6263
- Inc/Dec ratio: 1.015 (expected ~1.0)

### 5b. Correlation with Page Number

- **Pearson r(page_number, avg_suffix_value)**: -0.0517
- **Finding**: No correlation between suffix values and page position.

### 5c. Triplet Decoding (base-3, 0..26)

- **Total triplets**: 5474
- **Triplet entropy**: 4.728 bits (max 4.755)
- **Entropy efficiency**: 99.4%

- Values in 0-25 (alphabet range): 5216/5474 (95%)

Top 10 triplet values:

| Value | Count | If A=0 |
|-------|-------|--------|
| 0 | 336 | A |
| 13 | 301 | N |
| 26 | 258 | - |
| 2 | 228 | C |
| 1 | 221 | B |
| 18 | 220 | S |
| 6 | 218 | G |
| 3 | 218 | D |
| 24 | 212 | Y |
| 12 | 209 | M |

### 5d. Within-Page Monotonic Trends

- Pages with upward trend: 22
- Pages with downward trend: 38
- Pages with no clear trend: 41
- **Finding**: No systematic monotonic trends within pages.

---
## Synthesis and Conclusions

1. **Entropy structure**: NEGATIVE -- near-random sequence.

2. **Independence from stem**: NEGATIVE -- NMI = 0.5921.

3. **Section variation**: NEGATIVE -- H(1) range = 0.045 bits (uniform).

4. **Numeric encoding**: NEGATIVE -- no base-3 patterns, no page correlation.

### Overall Assessment (0/4 tests support dual-channel)

**Weak or no support for the dual-channel hypothesis.** The n/l/r suffixes
do not appear to function as an independent information channel.
