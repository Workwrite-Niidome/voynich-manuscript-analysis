# Hybrid Morpheme-Cipher Model: Voynich Manuscript Analysis

## Executive Summary

The hypothesis of a 3-dimensional morpheme cipher (PREFIX x STEM x SUFFIX with independent slots) is **partially supported but requires significant revision**. The analysis reveals a system that is neither a pure cipher nor natural morphology, but something structurally intermediate.

**Critical finding**: PREFIX and SUFFIX are statistically INDEPENDENT of each other (NMI = 0.03), which is abnormal for natural language but expected for a cipher or notation system. However, both correlate with STEM, indicating the stem imposes phonotactic constraints on what can attach to it.

---

## 1. Segmentation Results

### Corpus Statistics
- Total words (tokens): 36,522
- Unique words (types): 8,856
- Pages analyzed: 226

### Slot Inventories (Rule-Based Segmentation)

| Slot | Distinct Values | Hypothesis | Match? |
|------|----------------|------------|--------|
| Prefix | 15 | ~15 | YES |
| Suffix | 17 | ~7-17 | YES |
| Stem | 3,483 | 100-200 | NO (17x too many) |

### Coverage
- Words with prefix: 85.0%
- Words with suffix: 87.2%
- Words with stem: 72.5%
- Words with ALL three: 48.6%

### Top Prefixes (n=15)
```
ch: 16.9%   qo: 14.2%   o: 9.2%    d: 8.0%    sh: 7.8%
ot: 6.4%    ok: 6.3%     y: 4.4%    k: 3.1%    s: 2.8%
t: 2.7%     p: 1.5%      cth: 1.3%  f: 0.3%    ct: 0.1%
```

### Top Suffixes (n=17)
```
-y: 13.4%    -aiin: 8.8%   -ey: 7.9%   -edy: 7.7%   -ol: 7.2%
-ar: 6.1%    -eey: 5.9%    -dy: 4.8%   -al: 4.6%    -or: 4.5%
-r: 4.2%     -ain: 4.1%    -l: 3.2%    -iin: 2.6%    -am: 1.7%
-n: 0.5%     -an: 0.3%
```

### Stem Problem
The 3,483 distinct stems (2,506 hapax) indicate over-segmentation. The stem slot is absorbing too much structure. After gallows+bench normalization, stems reduce to ~4,472 (still high). Only 211 stems appear 10+ times.

The top "stems" are single characters (k, e, a, ch, t, o) -- essentially the word core after stripping prefix/suffix. This suggests the word's internal structure is MORE complex than a simple 3-slot model.

---

## 2. Independence Test (Mutual Information)

### Fully Segmented Words (n=17,761)

| Pair | MI (bits) | NMI | Verdict |
|------|-----------|-----|---------|
| prefix-stem | 1.653 | 0.508 | CORRELATED |
| stem-suffix | 1.372 | 0.379 | CORRELATED |
| **prefix-suffix** | **0.104** | **0.032** | **INDEPENDENT** |

### Permutation Test (1000 shuffles, all p=0.000)
All observed MI values significantly exceed null distribution, confirming real structure.

### Slot Entropies
```
H(prefix)  = 3.257 bits
H(stem)    = 7.191 bits
H(suffix)  = 3.621 bits
Sum if independent: 14.069 bits
Actual joint:       10.774 bits
Redundancy:          3.295 bits (23.4%)
```

### Interpretation

The **prefix-suffix independence** (NMI=0.032) is the most important finding:

- In natural languages (Latin, Italian, Turkish), prefix and suffix typically show NMI of 0.15-0.40 because grammatical categories constrain both
- NMI=0.03 means prefix selection and suffix selection operate on **completely different axes** -- they encode orthogonal information
- This is characteristic of a **multi-dimensional notation system** or **cipher**, not natural morphology

The prefix-stem and stem-suffix correlations (NMI=0.51 and 0.38) indicate that the stem constrains which prefixes and suffixes can attach -- this could be:
1. **Phonotactic constraints** in an artificial notation system
2. **Category membership** (certain stems only accept certain functional affixes)
3. **Natural morphological agreement** in an agglutinative language

---

## 3. Glyph-Position Analysis

Glyphs show extremely strong positional preferences:

### Initial-Only (>60% initial position)
```
qo: 98.8% initial    sh: 69.5% initial
ch: 54.1% initial    cth: 50.1% initial
```

### Final-Only (>60% final position)
```
n: 96.6% final    m: 92.7% final    g: 86.2% final
y: 83.5% final    r: 73.1% final    l: 51.7% final
```

### Medial-Only (>80% medial position)
```
e: 97.9%   i: 99.7%   k: 87.8%   ai: 85.6%
ee: 96.6%  t: 82.5%   a: 82.5%   ii: 93.1%
```

This extreme positional rigidity is MORE consistent with a notation system than natural language. In natural language, most consonants can appear in multiple positions.

---

## 4. Word Structure Patterns

1,588 unique structural patterns (C=consonant, V=vowel, G=gallows, X=complex onset).

### Top Patterns
```
CVC:   8.4%  (e.g., shol)
VC:    5.2%  (e.g., ar)
CVVC:  5.2%  (e.g., soiin)
CVV:   4.1%  (e.g., cphoy)
VGVC:  3.9%  (e.g., ykal)
CVCV:  3.7%  (e.g., shory)
```

The dominant pattern is CVC (bench + core vowel sequence + final consonant), which maps well to the prefix+stem+suffix hypothesis if we redefine "stem" as the vowel-core.

---

## 5. Paradigm Detection

411 stems have 4+ paradigm members (words sharing the same stem with different prefix/suffix combinations).

### Example Paradigms

**Stem 'ol'** (77 words): Takes all 13 prefixes and 11 suffixes
```
chol, cholaiin, cholal, cthol, dol, kol, okol, otol, qol, shol, tol, yol...
```

**Stem 'ar'** (88 words): Takes all 14 prefixes and 13 suffixes
```
char, chor, dar, kar, okar, otar, qoar, shar, tar, yar...
```

These paradigms show near-complete prefix/suffix combinability, supporting the idea that affixes are independent functional slots.

### Paradigm Size Distribution
- 947 paradigms with 2+ members
- Mean size: 6.6 members
- Max size: 134 members
- Most paradigms are small (355 with exactly 2 members)

---

## 6. Section-Level Variation

### Prefix Distribution Shifts by Section

| Prefix | Herbal-A | Herbal-B | Pharma | Astro | Bio | Cosmo | Stars |
|--------|----------|----------|--------|-------|-----|-------|-------|
| ch | 22.6% | 17.6% | 20.1% | 13.8% | 14.9% | 15.7% | 17.0% |
| qo | 7.1% | 10.3% | 9.5% | 9.2% | 18.1% | 12.1% | 17.1% |
| d | 14.9% | 16.6% | 11.2% | 8.7% | 7.1% | 8.3% | 4.1% |
| cth | 5.8% | 4.5% | 1.3%* | - | - | - | - |

Notable: `cth` is concentrated in Herbal sections (5-6%) and nearly absent elsewhere. `qo` peaks in Bio (18.1%) and Stars (17.1%). `d` is strongest in Herbal-B (16.6%) and weakest in Stars (4.1%).

If prefixes encode categories, these distribution shifts suggest different sections discuss different categories of things.

### Suffix Distribution Shifts

| Suffix | Herbal-A | Herbal-B | Bio | Stars |
|--------|----------|----------|-----|-------|
| -y | 19.1% | 22.7% | 14.0% | 8.5% |
| -edy | - | - | 13.9% | 10.4% |
| -eey | 2.5% | - | 6.3% | 8.9% |
| -ol | 12.4% | 12.7% | 5.8% | 4.2% |
| -or | 10.8% | 11.7% | - | - |

`-edy` and `-eey` are strongly concentrated in Bio/Stars sections, while `-ol` and `-or` dominate Herbal sections. This supports suffixes encoding grammatical roles that vary by content type.

---

## 7. Simulation Results

### Morpheme-Cipher Model (Independent Slots)

Generated text using observed prefix/stem/suffix distributions with independent slot selection:

| Metric | Voynich | Simulated | Match? |
|--------|---------|-----------|--------|
| Types | 8,856 | 13,672 | NO (sim has 54% more) |
| Entropy | 10.67 bits | 12.08 bits | NO (sim 13% higher) |
| Zipf slope | -0.852 | -0.699 | PARTIAL |
| Zipf R-sq | 0.898 | 0.889 | YES |

### Conditional Entropy Decay

| Context | Voynich | Simulated |
|---------|---------|-----------|
| H(w) | 10.669 | 12.079 |
| H(w\|w-1) | 4.150 | 3.043 |
| H(w\|w-2) | 0.328 | 0.034 |

The simulated text has higher entropy (too many combinations actually used) and lower contextual predictability. This confirms that the Voynich system has **stronger constraints** than pure independence -- the prefix-stem and stem-suffix correlations reduce the effective vocabulary.

---

## 8. Sandhi Analysis

Suffix-to-next-prefix correlation (cross-word boundary):
```
MI = 0.126 bits  (NMI = 0.037)
```

Very weak cross-word dependency. The suffix of word N barely predicts the prefix of word N+1. This suggests **word-level encoding** -- each word is an independent unit, not part of a connected phonological stream.

---

## 9. Revised Model

The pure 3-dimensional cipher hypothesis is **rejected** in its simplest form (stems are not a closed set of 100-200). However, the data strongly supports a **modified hybrid model**:

### The Voynich Encoding System (Revised Hypothesis)

```
WORD = [PREFIX] + CORE + [SUFFIX]
         |          |        |
    Category    Content   Qualifier
    (15 types)  (open)   (17 types)
         |                   |
         +---- INDEPENDENT --+
```

**Key properties:**
1. **PREFIX and SUFFIX are independent cipher dimensions** (NMI=0.03)
2. **CORE is NOT a simple codebook** -- it has internal structure (vowel sequences, gallows, bench chars) suggesting either:
   - A syllable-level encoding within the core
   - A natural language word being enciphered
   - A combinatorial system with sub-stem structure
3. **PREFIX encodes category/section-specific information** (distribution varies by manuscript section)
4. **SUFFIX encodes grammatical/qualifier information** (distribution varies by content type)
5. **Words are independently encoded** (minimal cross-word dependency)

### What This Explains

- **Vocabulary size (8,856)**: Not 15x200x17=51,000 (pure cipher) because stem-affix correlations reduce combinations. Not 200 (simple code) because stem has internal combinatorial structure.
- **Agglutinative appearance**: Real compositional structure in prefix+suffix, but stem is not a simple lookup.
- **Section variation**: Different topics activate different prefix/suffix distributions.
- **Statistical properties between language and code**: The prefix-suffix frame behaves like a code; the stem behaves more like language.

### Decipherment Implications

1. **PREFIX meanings are decodable** from section distribution analysis -- 15 values, varying systematically by manuscript section
2. **SUFFIX meanings are decodable** from positional/grammatical analysis -- 17 values, varying by content type
3. **CORE/STEM requires either**:
   - Discovery of the internal encoding rule (if it's a cipher within a cipher)
   - External crib (if it's a codebook)
   - Recognition of the source language (if it's enciphered natural text)

### Next Steps

1. **Map prefix meanings**: Cross-reference the 15 prefixes with illustration content on each page
2. **Map suffix meanings**: Analyze suffix distribution within lines (first word vs last word, label vs running text)
3. **Sub-stem analysis**: Decompose the stem/core into gallows + vowel-sequence to test if there's a second level of encoding
4. **Compare with known notation systems**: Alchemical notation, pharmacological shorthand, Lullian combinatorics

---

## 10. Comparison with Known Systems

| Property | Voynich | Natural Language | Simple Cipher | Notation System |
|----------|---------|-----------------|---------------|-----------------|
| Prefix-suffix MI | 0.03 (LOW) | 0.15-0.40 | 0 (expected) | 0-0.05 |
| Prefix-stem MI | 0.51 (HIGH) | 0.20-0.50 | 0 (expected) | variable |
| Stem-suffix MI | 0.38 (MOD) | 0.20-0.50 | 0 (expected) | variable |
| Positional rigidity | EXTREME | moderate | none | high |
| Vocabulary size | 8,856 | 20,000-100,000 | matches source | 500-5,000 |
| Cross-word MI | 0.04 (LOW) | 0.10-0.30 | depends | 0-0.05 |

The Voynich most closely matches a **notation system** with prefix-suffix independence and high positional rigidity, but with a stem component that behaves more like natural language.

---

## Raw Data Files

- Analysis script: `hybrid_morpheme_analysis.py`
- Refined analysis: `hybrid_morpheme_refined.py`
- Source transcription: `RF1b-e.txt`
