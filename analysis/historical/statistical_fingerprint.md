# Voynich Manuscript: Statistical Fingerprint Analysis

**Date**: 2026-04-10
**Source**: EVA transcription (RF1b-e.txt)
**Corpus**: 37,779 tokens, 8,500 unique types, 226,468 characters

---

## 1. Type-Token Ratio (TTR)

| Text Type | TTR |
|---|---|
| **Voynich (EVA)** | **0.2250** |
| Medieval Latin herbal | 0.15--0.25 |
| Italian prose (14th c.) | 0.20--0.30 |
| English prose | 0.20--0.30 |
| Simple substitution cipher | 0.05--0.15 |

**Interpretation**: The Voynich TTR of 0.225 falls squarely within the range for **natural language** -- specifically matching medieval Latin herbals and Italian prose. This immediately rules out simple substitution ciphers, which produce drastically lower TTR due to vocabulary compression.

---

## 2. Hapax Legomena Ratio

| Text Type | Hapax / Types |
|---|---|
| **Voynich (EVA)** | **0.6952** |
| Natural language (typical) | 0.50--0.60 |
| Cipher text | 0.70--0.80 |

- Hapax legomena (words appearing exactly once): 5,909
- Total unique words: 8,500

**Interpretation**: At 0.695, the Voynich sits **between** natural language and cipher, but closer to cipher territory. This elevated hapax ratio could indicate:
- A highly inflected or agglutinative language (many rare word forms)
- An encoding system that generates many near-unique forms
- A natural language with productive morphology

This is notably higher than typical European natural language but lower than pure cipher.

---

## 3. Average Word Length

| Language | Avg Word Length |
|---|---|
| **Voynich (EVA)** | **4.99** |
| Latin | ~5.5 |
| Italian | ~5.0 |
| English | ~4.7 |
| Arabic | ~4.5 |
| Hebrew | ~4.0 |
| German | ~5.8 |

**Interpretation**: The average word length of 4.99 is a near-exact match for **Italian**. This is one of the most frequently cited statistical parallels in Voynich research and aligns with the hypothesis that the underlying language may be an Italian dialect.

---

## 4. Word Length Distribution

```
Length | Count |    %  | Histogram
-------|-------|-------|------------------------------------------
   1   |  1041 |  2.8% | #####
   2   |  2449 |  6.5% | ############
   3   |  3648 |  9.7% | ###################
   4   |  7323 | 19.4% | ######################################
   5   |  9104 | 24.1% | ################################################
   6   |  7155 | 18.9% | #####################################
   7   |  4189 | 11.1% | ######################
   8   |  1745 |  4.6% | #########
   9   |   722 |  1.9% | ###
  10   |   250 |  0.7% | #
  11   |    85 |  0.2% |
  12   |    43 |  0.1% |
  13+  |    25 |  0.1% |
```

- **Mode**: 5 characters
- **Median**: 5 characters
- **Shape**: Unimodal, slightly right-skewed, smooth bell curve

**Interpretation**: The distribution is a smooth, unimodal bell curve peaking at length 5 -- characteristic of natural language. Cipher texts typically show more irregular, multi-modal, or flat distributions. The smooth shape strongly suggests a natural language or a system that faithfully preserves word-length structure.

**Closest match**: Italian and Latin both peak at 4--5 characters. The distribution shape is more consistent with Italian.

---

## 5. Repeat Rate

| Text Type | Repeat Rate |
|---|---|
| **Voynich (EVA)** | **0.002833** |
| Natural language (rich vocab) | 0.002--0.010 |
| Cipher/code (limited vocab) | 0.010--0.050 |

**Interpretation**: The repeat rate of 0.00283 is at the **low end** of natural language -- indicating an exceptionally rich vocabulary. This is inconsistent with cipher systems, which tend to recycle tokens. The Voynich text has vocabulary diversity comparable to or exceeding most natural languages.

---

## 6. Yule's K Constant

| Text Type | Yule's K |
|---|---|
| **Voynich (EVA)** | **28.33** |
| Latin prose | ~80--120 |
| Italian prose | ~90--130 |
| English prose | ~100--140 |
| Technical/medical | ~120--200 |
| Cipher/code | ~200--500+ |

**Interpretation**: This is the most anomalous result. The Voynich K of 28.33 is **dramatically lower** than any known natural language text of comparable length. For context:

- A K of 28 implies an **extraordinarily even** word frequency distribution -- words are used with remarkably uniform frequency rather than following the steep Zipfian drop-off typical of natural language.
- Natural language texts at ~38,000 tokens invariably produce K values of 80--200.
- The only texts that achieve such low K values are:
  - Very long texts (100,000+ tokens) -- but the Voynich is only 37,779 tokens
  - Texts with unusual generative morphology
  - Glossolalia or constructed language with productive word-formation rules

This is a **key anomaly** that distinguishes the Voynich from all known natural languages and suggests either a constructed system with regular word-formation patterns or a very unusual encoding.

---

## 7. Conditional Entropy (Character-Level)

| Order | Voynich | Latin | Italian | English | Arabic | Hebrew | Random Cipher |
|---|---|---|---|---|---|---|---|
| H(0) | **4.70** | 4.70 | 4.70 | 4.70 | 4.50 | 4.50 | 4.70 |
| H(1) | **3.87** | 4.00 | 3.90 | 4.10 | 3.80 | 3.70 | 4.50 |
| H(2) | **2.41** | 3.50 | 3.30 | 3.60 | 3.00 | 2.90 | 4.40 |
| H(3) | **2.17** | 2.80 | 2.60 | 3.00 | 2.30 | 2.20 | 4.30 |

**Entropy Decay Pattern**:
```
H(1) -> H(2) drop:  1.46 bits (Voynich)   vs  ~0.50-0.60 (European)  vs  ~0.80 (Semitic)
H(2) -> H(3) drop:  0.23 bits (Voynich)   vs  ~0.60-0.70 (European)  vs  ~0.70 (Semitic)
```

**Interpretation**: This is the most revealing fingerprint:

1. **H(1) = 3.87** is close to Italian (3.90) and Arabic (3.80) -- within normal range.

2. **The massive H(1)->H(2) drop of 1.46 bits** is extraordinary. European languages lose ~0.5-0.6 bits from H(1) to H(2). The Voynich loses nearly three times as much. This means:
   - Character bigrams in Voynichese are **extremely predictable**
   - Once you know one character, the next is highly constrained
   - This matches a system with **strong positional rules** for characters within words

3. **The tiny H(2)->H(3) drop of 0.23 bits** means that knowing 2 characters already captures most of the information -- adding a 3rd character of context adds very little.

4. **The decay pattern** does not match any European language. It is closest to **Arabic** and **Hebrew** in having low H(2) and H(3), but the extreme H(1)->H(2) drop is unique. This pattern is consistent with:
   - A constructed writing system with strong positional character constraints
   - An abugida or syllabary where character combinations follow strict rules
   - A shorthand or notation system (not an alphabet in the usual sense)

---

## 8. Character-Level vs. Word-Level Entropy

| Measure | Value |
|---|---|
| Character H(1) | 3.8673 bits |
| Word H(1) | 10.5919 bits |
| Ratio (char/word) | **0.3651** |

| Text Type | Expected Ratio |
|---|---|
| Natural language | 0.30--0.45 |
| Simple substitution | 0.35--0.50 |
| Verbose cipher | much lower |

**Interpretation**: The ratio of 0.365 is within the normal range for natural language. This rules out verbose cipher systems (which would show much lower character entropy relative to word entropy). The encoding, whatever it is, maintains the entropy balance of a natural language.

---

## 9. Benford's Law for Word Frequencies

| Leading Digit | Observed | Benford Expected | Deviation |
|---|---|---|---|
| 1 | **0.7291** | 0.3010 | +0.4281 |
| 2 | 0.1253 | 0.1761 | -0.0508 |
| 3 | 0.0498 | 0.1249 | -0.0751 |
| 4 | 0.0340 | 0.0969 | -0.0629 |
| 5 | 0.0205 | 0.0792 | -0.0587 |
| 6 | 0.0144 | 0.0669 | -0.0525 |
| 7 | 0.0121 | 0.0580 | -0.0459 |
| 8 | 0.0094 | 0.0512 | -0.0418 |
| 9 | 0.0055 | 0.0458 | -0.0403 |

**Chi-squared**: 0.8999

**Interpretation**: The Voynich word frequencies **strongly violate** Benford's law, with a massive excess of leading digit 1 (73% vs. expected 30%). However, this is actually consistent with **Zipf's law** operating on a large vocabulary: in any Zipfian distribution, the vast majority of words have low frequencies (starting with 1), so the leading-digit distribution is dominated by digit 1. This is a known property of natural language frequency distributions and is not diagnostic either way.

---

## 10. Multi-Dimensional Distance Analysis

Feature vector: (TTR, Hapax Ratio, Avg Word Length, Yule's K / 1000, H(1), H(2))

| Rank | Language / System | Distance |
|---|---|---|
| 1 | **Arabic (classical)** | **0.789** |
| 2 | Italian prose (14th c.) | 0.909 |
| 3 | Italian (scientific) | 1.038 |
| 4 | Verbose cipher | 1.079 |
| 5 | Hebrew (medieval) | 1.134 |
| 6 | Medieval Latin (herbal) | 1.223 |
| 7 | Medieval Latin (general) | 1.226 |
| 8 | English (medieval) | 1.262 |
| 9 | Simple substitution cipher | 2.019 |
| 10 | Random text | 2.277 |

**Interpretation**: In multi-dimensional statistical space, the Voynich is closest to **Arabic**, followed by **Italian**, with cipher systems ranking further away (except verbose cipher, which is 4th). The distance to all reference profiles is substantial (>0.78), indicating that the Voynich does not perfectly match any known system.

---

## Summary of Key Findings

### What the Voynich IS like:
| Metric | Points toward |
|---|---|
| TTR (0.225) | Natural language (Latin herbal / Italian) |
| Avg word length (4.99) | Italian |
| Repeat rate (0.0028) | Natural language with rich vocabulary |
| Word length distribution | Natural language (smooth bell curve) |
| Char/word entropy ratio | Natural language |
| Multi-dim closest match | Arabic, then Italian |

### What the Voynich is NOT like:
| Metric | Rules out |
|---|---|
| TTR (0.225) | Simple substitution cipher |
| Repeat rate (0.0028) | Cipher / code systems |
| Word length distribution | Random or cipher text |
| Char/word entropy ratio | Verbose cipher |
| Multi-dim distance | Random text, simple substitution |

### Anomalous metrics (matching NO known system):
| Metric | Anomaly |
|---|---|
| Yule's K (28.33) | Far too low for any natural language (~80-200 expected). Suggests artificially regular word frequency distribution |
| Hapax ratio (0.695) | Between natural language and cipher -- ambiguous |
| H(1)->H(2) entropy drop (1.46) | Much larger than any natural language (~0.5-0.6). Characters are extremely predictable in pairs |
| Benford chi-sq (0.90) | Poor fit, though explained by Zipf dominance |

### The Entropy Fingerprint is the Smoking Gun

The decay pattern H(0)=4.70, H(1)=3.87, H(2)=2.41, H(3)=2.17 is unlike any known natural language. The enormous drop from H(1) to H(2) followed by a tiny drop from H(2) to H(3) indicates that **character bigrams encode almost all the information**, and higher-order contexts add very little. This is consistent with:

1. **A syllabary or abugida** where each "character" in EVA actually represents a syllable, making bigrams (= disyllabic sequences) highly constrained
2. **A constructed notation system** with strict positional rules for glyph combination
3. **A generative morphological system** where words are built from a small number of productive affixes following rigid rules

### Overall Verdict

The Voynich manuscript occupies a **unique position** in statistical space. Its word-level statistics (TTR, word length, repeat rate) are consistent with natural language, particularly Italian. But its character-level statistics (entropy decay, Yule's K) are anomalous for any known natural language, suggesting the script is not a simple alphabet but rather a **syllabary, abugida, or constructed notation system** that encodes a natural language (most likely Italian or a related Romance language, possibly with Semitic influences in its encoding structure).

The statistical fingerprint is inconsistent with:
- Random or meaningless text (too structured)
- Simple substitution cipher (vocabulary too rich)
- Verbose cipher (entropy balance too natural)
- Any unmodified European alphabetic text (entropy decay too steep)

The fingerprint IS consistent with:
- A natural language encoded through a non-alphabetic writing system
- An agglutinative or constructed language with regular morphology
- A phonetic notation system (like shorthand) applied to a Romance language

---

## Zipf's Law Check

| Rank | Word | Frequency | Rank x Freq |
|---|---|---|---|
| 1 | daiin | 713 | 713 |
| 2 | aiin | 565 | 1,130 |
| 3 | ol | 523 | 1,569 |
| 4 | chey | 495 | 1,980 |
| 5 | ar | 406 | 2,030 |
| 10 | chedy | 327 | 3,270 |
| 15 | qokaiin | 255 | 3,825 |
| 20 | chor | 209 | 4,180 |

Rank x Frequency is **not constant** (rises from 713 to 4180), meaning the Voynich has a **flatter frequency distribution** than Zipf's law predicts. The most frequent word ("daiin" at 1.89%) is far less dominant than Zipf would predict for a 37,000-token text (expected ~5-7% for rank 1). This flatter-than-Zipf distribution is another manifestation of the anomalously low Yule's K and is consistent with a system where common function words are either absent or encoded differently.
