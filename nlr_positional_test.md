# Voynich Manuscript: n/l/r Word-Final Suffix Positional Analysis

## Overview

- **Total words parsed**: 37277
- **Words ending in -n**: 6005 (16.1%)
- **Words ending in -l**: 5680 (15.2%)
- **Words ending in -r**: 5605 (15.0%)
- **Total n/l/r words**: 17290 (46.4%)
- **Paragraphs (folios)**: 226

Significance threshold: p < 0.05 (with Bonferroni correction for 8 tests, effective threshold p < 0.00625)

---

## Hypothesis 1: Line Position

**Question**: Do words ending in -n/-l/-r correlate with their position within a line?

### 1a. Quartile-based position (start/middle/end)

| Position | -n | -l | -r | Total | %n | %l | %r |
|----------|----|----|----|----|----|----|-----|
| start | 1817 | 1677 | 1882 | 5376 | 33.8% | 31.2% | 35.0% |
| middle | 2390 | 2434 | 2151 | 6975 | 34.3% | 34.9% | 30.8% |
| end | 1746 | 1449 | 1477 | 4672 | 37.4% | 31.0% | 31.6% |

**Chi-squared**: 46.32, df=4, **p=0.000000**
**Result**: SIGNIFICANT

### 1b. First word vs Last word vs Others

| Position | -n | -l | -r | Total | %n | %l | %r |
|----------|----|----|----|----|----|----|-----|
| first | 917 | 739 | 996 | 2652 | 34.6% | 27.9% | 37.6% |
| other | 4438 | 4447 | 4220 | 13105 | 33.9% | 33.9% | 32.2% |
| last | 650 | 494 | 389 | 1533 | 42.4% | 32.2% | 25.4% |

**Chi-squared**: 98.98, df=4, **p=0.000000**
**Result**: SIGNIFICANT

---

## Hypothesis 2: Adjacent Word Dependency

### 2a. Suffix vs Next Word Starting Character

**Question**: Does the suffix depend on the starting character of the NEXT word?

**Baseline rates**: P(n)=0.347, P(l)=0.329, P(r)=0.324

| Next starts with | P(n) | P(l) | P(r) | N |
|-----------------|------|------|------|---|
| a | 0.201 | 0.146 | 0.653 | 1488 |
| c | 0.384 | 0.318 | 0.298 | 4152 |
| d | 0.303 | 0.498 | 0.199 | 1070 |
| e | 0.095 | 0.429 | 0.476 | 63 |
| f | 0.250 | 0.357 | 0.393 | 28 |
| i | 0.050 | 0.250 | 0.700 | 20 |
| k | 0.126 | 0.714 | 0.160 | 406 |
| l | 0.193 | 0.611 | 0.196 | 316 |
| o | 0.400 | 0.265 | 0.335 | 3835 |
| p | 0.214 | 0.476 | 0.310 | 42 |
| q | 0.371 | 0.391 | 0.238 | 1059 |
| r | 0.165 | 0.560 | 0.275 | 109 |
| s | 0.340 | 0.339 | 0.321 | 2083 |
| t | 0.207 | 0.603 | 0.190 | 174 |
| y | 0.415 | 0.227 | 0.358 | 620 |

**Chi-squared**: 1573.76, df=28, **p=0.000000**
**Result**: SIGNIFICANT

**Top 10 deviations from baseline**:

| Next char | Suffix | Observed | Baseline | Deviation | N |
|-----------|--------|----------|----------|-----------|---|
| k | -l | 0.714 | 0.329 | +0.386 | 406 |
| i | -r | 0.700 | 0.324 | +0.376 | 20 |
| a | -r | 0.653 | 0.324 | +0.329 | 1488 |
| i | -n | 0.050 | 0.347 | -0.297 | 20 |
| l | -l | 0.611 | 0.329 | +0.282 | 316 |
| t | -l | 0.603 | 0.329 | +0.275 | 174 |
| e | -n | 0.095 | 0.347 | -0.252 | 63 |
| r | -l | 0.560 | 0.329 | +0.231 | 109 |
| k | -n | 0.126 | 0.347 | -0.222 | 406 |
| a | -l | 0.146 | 0.329 | -0.183 | 1488 |

### 2b. Suffix vs Previous Word Ending Character

| Prev ends with | P(n) | P(l) | P(r) | N |
|----------------|------|------|------|---|
| d | 0.372 | 0.340 | 0.288 | 215 |
| e | 0.325 | 0.307 | 0.368 | 114 |
| h | 0.429 | 0.306 | 0.265 | 49 |
| k | 0.281 | 0.312 | 0.406 | 32 |
| l | 0.314 | 0.384 | 0.302 | 2468 |
| m | 0.240 | 0.364 | 0.397 | 121 |
| n | 0.343 | 0.350 | 0.307 | 2427 |
| o | 0.333 | 0.337 | 0.331 | 484 |
| r | 0.329 | 0.299 | 0.372 | 2562 |
| s | 0.438 | 0.244 | 0.319 | 640 |
| t | 0.258 | 0.323 | 0.419 | 31 |
| y | 0.367 | 0.341 | 0.293 | 5431 |

**Chi-squared**: 127.49, df=22, **p=0.000000**
**Result**: SIGNIFICANT

---

## Hypothesis 3: Checksum Functions

**Question**: Does the suffix correlate with a function of the preceding characters (stem)?

### Stem length mod 3

| Value | -n | -l | -r | Total | %n | %l | %r |
|-------|----|----|----|----|----|----|-----|
| 0 | 2027 | 1713 | 1719 | 5459 | 37.1% | 31.4% | 31.5% |
| 1 | 2114 | 2311 | 2151 | 6576 | 32.1% | 35.1% | 32.7% |
| 2 | 1860 | 1530 | 1583 | 4973 | 37.4% | 30.8% | 31.8% |

**Chi-squared**: 52.06, df=4, **p=0.000000**
**Result**: SIGNIFICANT

### Sum of character ordinals mod 3

| Value | -n | -l | -r | Total | %n | %l | %r |
|-------|----|----|----|----|----|----|-----|
| 0 | 1672 | 1859 | 1838 | 5369 | 31.1% | 34.6% | 34.2% |
| 1 | 1775 | 1694 | 1721 | 5190 | 34.2% | 32.6% | 33.2% |
| 2 | 2554 | 2001 | 1894 | 6449 | 39.6% | 31.0% | 29.4% |

**Chi-squared**: 97.98, df=4, **p=0.000000**
**Result**: SIGNIFICANT

### Vowel count (a,e,i,o) mod 3

| Value | -n | -l | -r | Total | %n | %l | %r |
|-------|----|----|----|----|----|----|-----|
| 0 | 3082 | 697 | 750 | 4529 | 68.1% | 15.4% | 16.6% |
| 1 | 1914 | 2827 | 2686 | 7427 | 25.8% | 38.1% | 36.2% |
| 2 | 1005 | 2030 | 2017 | 5052 | 19.9% | 40.2% | 39.9% |

**Chi-squared**: 2951.30, df=4, **p=0.000000**
**Result**: SIGNIFICANT

---

## Hypothesis 4: Paragraph/Page Position

**Question**: Does n/l/r usage change from beginning to end of a paragraph/page?

| Position | -n | -l | -r | Total | %n | %l | %r |
|----------|----|----|----|----|----|----|-----|
| beginning | 1960 | 1846 | 2033 | 5839 | 33.6% | 31.6% | 34.8% |
| middle | 2018 | 1920 | 1835 | 5773 | 35.0% | 33.3% | 31.8% |
| end | 2027 | 1914 | 1736 | 5677 | 35.7% | 33.7% | 30.6% |

**Chi-squared**: 25.21, df=4, **p=0.000046**
**Result**: SIGNIFICANT

---

## Summary of Results

| Hypothesis | Chi-squared | df | p-value | Significant (p<0.00625)? |
|-----------|------------|-----|---------|----------------------|
| H1a: Line position (quartile) | 46.32 | 4 | 0.000000 | YES |
| H1b: First/last word | 98.98 | 4 | 0.000000 | YES |
| H2a: Next word starting character | 1573.76 | 28 | 0.000000 | YES |
| H2b: Previous word ending character | 127.49 | 22 | 0.000000 | YES |
| H3a: Stem length mod 3 | 52.06 | 4 | 0.000000 | YES |
| H3b: Ordinal sum mod 3 | 97.98 | 4 | 0.000000 | YES |
| H3c: Vowel count mod 3 | 2951.30 | 4 | 0.000000 | YES |
| H4: Paragraph position | 25.21 | 4 | 0.000046 | YES |

## Interpretation

The following hypotheses show statistically significant results (after Bonferroni correction for 8 tests):

- **H1a: Line position (quartile)**: chi2=46.32, p=0.000000
- **H1b: First/last word**: chi2=98.98, p=0.000000
- **H2a: Next word starting character**: chi2=1573.76, p=0.000000
- **H2b: Previous word ending character**: chi2=127.49, p=0.000000
- **H3a: Stem length mod 3**: chi2=52.06, p=0.000000
- **H3b: Ordinal sum mod 3**: chi2=97.98, p=0.000000
- **H3c: Vowel count mod 3**: chi2=2951.30, p=0.000000
- **H4: Paragraph position**: chi2=25.21, p=0.000046

**Adjacent-word dependency**: The choice of n/l/r suffix appears to depend on
the adjacent word's characters. This is consistent with theories that n/l/r may
function as phonological liaison markers, grammatical agreement markers, or some
form of inter-word binding in the Voynich script. If the suffix is conditioned on
the next word, it could represent a sandhi-like phenomenon where word boundaries
trigger phonological alternation.

**Checksum correlation**: The suffix correlates with properties of the stem,
suggesting it may encode information about the word's own structure. This could
indicate a self-check mechanism, a morphological pattern (e.g., stem class determines
suffix), or an artifact of the underlying encoding system.

**Line-position effect**: The suffix distribution varies by position in the line,
suggesting syntactic or formatting information. This could indicate clause-boundary
marking, case markers, or a positional encoding layer in the script.

**Paragraph-position effect**: Suffix usage changes from beginning to end of a page,
potentially indicating discourse-level structure or topic/section markers.
