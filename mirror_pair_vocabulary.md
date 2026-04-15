# Voynich Manuscript: Mirror/Anagram Pair Vocabulary Analysis

## Executive Summary

Systematic analysis of the EVA transcription (8,926 unique words, 226 pages) reveals that **ckhy/kchy is the ONLY statistically significant complementary mirror pair** in the entire manuscript (p=0.0452). The hypothesis that the Voynich uses a systematic mirror-pair encoding for opposing concepts is **not supported by the data**. While numerous anagram pairs exist (192 at freq>=5), their distributional patterns are consistent with chance.

---

## 1. Corpus Statistics

| Metric | Value |
|--------|-------|
| Total unique words | 8,926 |
| Words freq >= 5 | 961 |
| Words freq >= 3 | 1,573 |
| Total pages | 226 |

---

## 2. ckhy/kchy Verification (The Original Discovery)

| Word | Frequency | Pages |
|------|-----------|-------|
| ckhy | 36x | 34 pages |
| kchy | 34x | 29 pages |

- **Page overlap**: 1 page (f22r only)
- **Jaccard similarity**: 0.016
- **Monte Carlo p-value**: 0.0452 (significant at alpha=0.05)

### Distribution Pattern
- **ckhy**: f1v, f2r, f3v, f6v, f8r, f9v, f10v, f17v, f22r, f24r, f32r, f35r, f35v, f37r, f42r, f44v, f48r, f49v, f51r, f52v, f55r, f57r, f58r, f75v, f78r, f89v1, f89v2, f90r1, f93v, f99r, f102v2, f105v, f115r, f116r
- **kchy**: f1r, f5r, f11r, f11v, f13r, f14r, f14v, f15r, f16r, f17r, f18v, f19v, f22r, f22v, f25r, f27v, f29r, f31r, f34v, f36v, f39v, f42v, f49r, f50v, f53v, f66v, f85r1, f86v3, f86v5

This remains the strongest finding: near-perfect complementary distribution, consistent with encoding hot/cold or a similar binary opposition.

---

## 3. All Exact Mirror Pairs (reversed string)

### Frequency >= 5 (8 pairs found)

| Pair | Freq | Pages | Overlap | Jaccard | p-value | Assessment |
|------|------|-------|---------|---------|---------|------------|
| **so / os** | 6/28 | 5/25 | **0** | 0.000 | 0.559 | Complementary but NOT significant |
| **do / od** | 16/6 | 14/6 | **0** | 0.000 | 0.684 | Complementary but NOT significant |
| **lo / ol** | 17/577 | 14/123 | 12 | 0.096 | -- | High asymmetry, ol ubiquitous |
| **or / ro** | 378/11 | 122/9 | 6 | 0.048 | -- | High asymmetry, or ubiquitous |
| **sol / los** | 55/6 | 34/6 | 3 | 0.081 | -- | High asymmetry |
| **lor / rol** | 38/19 | 28/15 | 7 | 0.194 | -- | Moderate overlap |
| **ral / lar** | 16/12 | 15/12 | 3 | 0.125 | -- | Moderate overlap |
| **yk / ky** | 6/15 | 6/15 | 1 | 0.050 | -- | Near-complementary but low freq |

### Frequency >= 3 (14 pairs total, additional 6)

| Pair | Freq | Pages | Overlap | Jaccard |
|------|------|-------|---------|---------|
| **ys / sy** | 3/26 | 3/23 | **0** | 0.000 |
| **ls / sl** | 16/4 | 14/4 | **0** | 0.000 |
| **ly / yl** | 15/3 | 13/3 | **0** | 0.000 |
| oty / yto | 108/4 | 72/4 | 2 | 0.027 |
| od / do | 6/16 | 6/14 | 0 | 0.000 |
| so / os | 6/28 | 5/25 | 0 | 0.000 |

**Critical observation**: The zero-overlap mirror pairs (so/os, do/od, ys/sy, ls/sl, ly/yl) are all very short words (2 characters) with highly asymmetric frequencies. Their complementary distribution is NOT statistically significant -- with only 3-6 pages for the rare member, zero overlap is expected by chance approximately 50-70% of the time. These do NOT represent a designed encoding system.

---

## 4. All Anagram Pairs with Low Overlap (J < 0.10)

192 total anagram pairs found at freq >= 5. Below are those with the lowest overlap:

### Complementary (zero overlap) anagram pairs:

| Pair | Freq | Pages | Type | p-value |
|------|------|-------|------|---------|
| sal / als | 47/7 | 38/7 | anagram | 0.278 |
| checkhy / chekchy | 45/6 | 31/5 | anagram | 0.482 |
| otchey / octhey | 42/5 | 30/5 | anagram | 0.490 |
| okchey / cheoky | 37/8 | 30/8 | anagram | 0.310 |
| ckhol / kchol | 19/23 | 15/19 | anagram | 0.264 |
| chkeey / cheeky | 12/26 | 11/25 | anagram | 0.265 |
| dshy / shdy | 8/27 | 8/19 | anagram | 0.485 |
| oral / arol | 9/8 | 9/8 | partial rev | -- |
| alol / olal | 7/7 | 6/7 | partial rev | -- |
| orar / aror | 7/7 | 7/5 | partial rev | -- |
| deey / eedy | 8/5 | 7/5 | partial rev | -- |

**None of these reach statistical significance.** With p-values ranging from 0.26 to 0.73, the zero overlap is entirely consistent with random page sampling given the word frequencies involved.

### Near-complementary (overlap = 1)

| Pair | Freq | Pages | Overlap | Jaccard | p-value |
|------|------|-------|---------|---------|---------|
| **kchy / ckhy** | 34/36 | 29/34 | **1** | **0.016** | **0.045** |
| oty / toy | 108/5 | 72/5 | 1 | 0.013 | 0.493 |
| okeedy / keeody | 62/9 | 34/9 | 1 | 0.024 | 0.595 |
| otchy / octhy | 51/10 | 40/10 | 1 | 0.020 | 0.449 |
| tol / otl | 41/8 | 32/7 | 1 | 0.026 | 0.740 |

**Only kchy/ckhy is significant.** All other pairs with overlap=1 have p-values well above 0.05.

---

## 5. The ct/tc and ck/kc Pattern

A notable structural pattern emerges: many anagram pairs involve the transposition of digraphs **ct/tc** and **ck/kc**:

| Pair | Freq | J | Pattern |
|------|------|---|---------|
| cthy / tchy | 94/25 | 0.083 | ct <-> tc |
| cthor / tchor | 42/19 | 0.067 | ct <-> tc |
| cthol / tchol | 52/16 | 0.040 | ct <-> tc |
| tchey / cthey | 32/42 | 0.066 | tc <-> ct |
| ckhy / kchy | 36/34 | 0.016 | ck <-> kc |
| ckhey / kchey | 31/26 | 0.043 | ck <-> kc |
| ckhol / kchol | 19/23 | 0.000 | ck <-> kc |
| qokchy / qockhy | 80/17 | 0.068 | kc <-> ck |
| qotchy / qocthy | 62/7 | 0.019 | tc <-> ct |
| chckhy / chkchy | 135/5 | 0.026 | ck <-> kc |
| checkhy / chekchy | 45/6 | 0.000 | ck <-> kc |
| chdy / dchy | 102/26 | 0.041 | ch <-> d+ch |
| okchey / ockhey | 37/5 | 0.000 | kch <-> ckh |

**This is NOT a mirror-pair semantic system.** Rather, it reflects the well-known ambiguity in EVA transcription of the **ck/kc** and **ct/tc** glyph sequences, which are visually similar and may represent scribal variation or reading ambiguity. The distributional differences (when significant) likely reflect different scribes or writing habits in different sections of the manuscript (consistent with the Currier A/B language distinction).

---

## 6. Dry/Moist Axis Search

### Expected distribution:
- Dry pages: f2r, f3r, f9r, f41r
- Moist page: f47r

### Anagram/mirror pairs showing dry/moist separation:

| Pair | Dry member | Moist member | Assessment |
|------|-----------|--------------|------------|
| dchy / chdy | dchy (on f2r) | chdy (on f47r, f9r) | Both appear on target pages; but chdy is on BOTH dry AND moist pages |
| cthol / tchol | cthol (on f3r) | tchol (on f47r, f9r) | tchol is on both dry and moist |
| chety / cthey | chety (on f2r) | cthey (on f47r, f9r) | cthey is on both |
| otchy / octhy | otchy (on f47r) | octhy (on f3r) | Interesting split but both are widespread |
| ckhey / kchey | ckhey (on f47r) | kchey (on f41r) | Promising but both appear on many other pages |
| ckhor / kchor | ckhor (on f2r) | kchor (on f47r) | **Best candidate**: 7pp/21pp, zero overlap between them |

### ckhor/kchor as dry/moist candidate:
- **ckhor** (7x, 7pp): f2r, f6r, f24v, f37r, f90r2, f96r, f99r -- includes expected dry page f2r
- **kchor** (21x, 21pp): f2v, f6v, f7v, f8v, f13v, f14r, f17v, f18r, f19r, f19v, f25v, f29v, f30v, f35v, f44v, f47r, f49v, f87v, f90r1, f93r, f115r -- includes expected moist page f47r

However: ckhor/kchor is just the ck/kc glyph ambiguity applied to the common word "chor." Its distributional pattern more likely reflects different scribes than semantic opposition.

### No convincing dry/moist mirror pair was found.

---

## 7. Partial Reversal Pairs (First 2-3 Characters Swapped)

### First 3 chars reversed, J < 0.15:

| Pair | Freq | Pages | Jaccard | Pattern |
|------|------|-------|---------|---------|
| sol / los | 55/6 | 34/6 | 0.081 | sol <-> los (full mirror) |
| lar / ral | 12/16 | 12/15 | 0.125 | lar <-> ral (full mirror) |
| olar / alor | 19/8 | 16/6 | 0.048 | ol-ar <-> al-or |
| **oral / arol** | 9/8 | 9/8 | **0.000** | or-al <-> ar-ol |
| **alol / olal** | 7/7 | 6/7 | **0.000** | al-ol <-> ol-al |
| **orar / aror** | 7/7 | 7/5 | **0.000** | or-ar <-> ar-or |
| **deey / eedy** | 8/5 | 7/5 | **0.000** | de-ey <-> ee-dy |

The zero-overlap partial reversals (oral/arol, alol/olal, orar/aror) are interesting but not statistically significant given their low frequencies. They involve transpositions of common Voynichese syllable-like elements (ol, or, al, ar), which may simply be positional variants.

---

## 8. Semantic Axis Mapping

### Confirmed axis (statistically significant):
| Axis | Word 1 | Word 2 | Overlap | p-value | Proposed meaning |
|------|--------|--------|---------|---------|-----------------|
| Thermal? | ckhy | kchy | 1/62 pages | 0.045 | hot/cold (hypothesized) |

### Candidate axes (complementary but not significant):
| Axis | Word 1 | Word 2 | Overlap | p-value | Notes |
|------|--------|--------|---------|---------|-------|
| ? | so | os | 0/30 | 0.559 | Too few occurrences of "so" |
| ? | do | od | 0/20 | 0.684 | Too few occurrences of "od" |
| ? | sal | als | 0/45 | 0.278 | Possibly interesting, sal=38pp |
| ? | ys | sy | 0/26 | 0.725 | "ys" only 3 occurrences |

### No other axes confirmed.

---

## 9. Critical Assessment

### Is there a systematic mirror-pair encoding system?

**No. The evidence does not support this hypothesis.**

1. **Only one significant pair**: Out of 8 exact mirror pairs (freq>=5) and 192 anagram pairs, only ckhy/kchy shows statistically significant complementary distribution (p=0.045). At alpha=0.05 with ~200 tests, we would expect ~10 false positives by chance. Having only 1 significant result is actually FEWER than expected by chance.

2. **The ck/kc pattern is scribal, not semantic**: The most common source of "anagram pairs" in Voynichese is the ck/kc and ct/tc digraph ambiguity. These are known paleographic issues where the EVA transcription preserves visual ambiguity in glyph order. The pairs cthy/tchy, cthor/tchor, cthol/tchol, etc., are likely the SAME WORD read differently by different scribes or in different scribal hands.

3. **ckhy/kchy may itself be a scribal variant**: The ck/kc transposition is the most common source of "mirror pairs" in the manuscript. ckhy and kchy could be the same word written by different hands (Currier A vs B). The distributional split (kchy concentrated in early folios f11-f19; ckhy in later folios) is consistent with different scribes rather than different meanings.

4. **Frequency asymmetry**: Most mirror pairs show extreme frequency asymmetry (e.g., ol=577 vs lo=17, or=378 vs ro=11). A designed encoding system for opposing concepts would be expected to produce roughly equal frequencies for each member of a pair.

5. **No dry/moist pair found**: The search for a specific dry/moist mirror pair yielded no convincing candidates.

### Alternative explanation for ckhy/kchy

The near-perfect complementary distribution of ckhy/kchy may be better explained by:
- **Two scribes** (Hand 1 writes "ckhy", Hand 2 writes "kchy") encoding the SAME concept
- The single overlap page (f22r) represents a transitional section
- This is consistent with the Currier A/B language hypothesis

### What this means for decipherment

The mirror-pair hypothesis, while creative, should not be pursued further as a systematic key to the Voynich cipher. The ckhy/kchy complementary distribution is real but is better explained by scribal variation than by semantic opposition encoding. The Voynich script does not appear to use character reversal as a productive morphological device for marking opposites.

---

## 10. Raw Data: All Tested Pairs with Significance

Only the top result shown (the only significant one):

```
[ANAGRAM] kchy (34x,29pp) <-> ckhy (36x,34pp) | ov=1 J=0.016 p=0.0452 *** SIGNIFICANT ***
```

All other pairs: p > 0.17 (none approach significance after the single hit).

---

## Methodology

- **Source**: RF1b-e.txt (EVA transcription of Voynich MS)
- **Parsing**: EVA markup removed; words split on dots, spaces, commas, hyphens; special markers (@NNN) removed; curly-brace groups flattened
- **Mirror test**: For each word w with freq >= N, check if reverse(w) exists with freq >= N
- **Anagram test**: Group words by sorted character set; enumerate all pairs within groups
- **Distribution test**: Jaccard similarity of page sets; Monte Carlo permutation test (10,000 trials, random seed 42) for significance
- **Script**: `mirror_pair_analysis.py`
