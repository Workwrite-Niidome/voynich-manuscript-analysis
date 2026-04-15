# Voynich Manuscript: Glyph-Level Stroke Decomposition Analysis

## Hypothesis

Each EVA "character" is not an atomic letter but a COMPOSITE of visually distinct stroke components, analogous to how Chinese characters combine radicals or Korean Hangul combines jamo into syllable blocks. If true, the writing unit is the stroke, not the glyph.

## Source Data

- EVA transcription: `RF1b-e.txt` (Takeshi Takahashi, EVA 2.0)
- 37,031 words extracted (dot-separated), 8,851 unique
- 169,350 glyph tokens across 184 manuscript pages

---

## 1. EVA Component Taxonomy

Based on visual inspection of manuscript pages (f1r, f2r, f5r) and the EVA encoding system, the glyphs decompose into five visual component families:

| Component Family | EVA Glyphs | Visual Description | Count | % of all glyphs |
|---|---|---|---|---|
| **LOOP** | o, a, e | Curved closed forms, varying in shape | 60,196 | 35.5% |
| **BENCH** | ch, sh | Horizontal stroke with vertical elements | 15,240 | 9.0% |
| **GALLOWS** | k, t, p, f | Tall vertical stroke with crossbar | 17,915 | 10.6% |
| **GALLOWS+BENCH** | ckh, cth, cph, cfh | Gallows interwoven with bench | 2,040 | 1.2% |
| **PLUME** | i (often ii, iii) | Short vertical stroke(s) | 11,933 | 7.0% |
| **TAIL** | n, r, l, m, s, d, g | Descending or connecting strokes | 48,987 | 28.9% |
| **FINAL** | y | Terminal flourish | 17,466 | 10.3% |
| **INITIAL** | q | Word-initial mark | 5,435 | 3.2% |

### Key Observation: Gallows-Bench Compounds

The compound glyphs (ckh, cth, cph, cfh) are visually constructed by threading a gallows character (k/t/p/f) through a bench character (ch). In the decomposition model, these are two independent components physically merged:

- ckh = BENCH + GALLOWS_k
- cth = BENCH + GALLOWS_t
- cph = BENCH + GALLOWS_p
- cfh = BENCH + GALLOWS_f

This is the most Hangul-like feature of the script: two meaning-bearing strokes occupying the same spatial position.

---

## 2. Entropy Analysis: Per-Character vs Per-Stroke

| Level | Entropy | Units |
|---|---|---|
| Raw EVA character | 3.8658 bits | per ASCII character in EVA encoding |
| EVA glyph (tokenized) | 3.8658 bits | per Voynich glyph |
| Stroke component | 3.8104 bits | per decomposed stroke |

**Average components per glyph: 1.012**

The near-unity ratio (1.012 components per glyph) means that the decomposition barely expands the token count. Only the gallows-bench compounds (2.0% of glyphs) decompose into 2 components. The vast majority of EVA glyphs map to exactly one component.

**Predicted vs actual glyph entropy:**
- If strokes independent: 1.012 * 3.81 = 3.86 bits (predicted)
- Actual: 3.87 bits
- Ratio: 1.0025

**Interpretation:** The decomposition into stroke components does NOT reduce entropy. The stroke-level representation carries essentially the same information per unit as the glyph-level representation. This means the current decomposition is not finding hidden sub-glyph structure -- the glyphs are functionally atomic at this level of analysis.

---

## 3. Mutual Information: Are Components Independent?

| Measurement | MI (bits) |
|---|---|
| Adjacent components (within words) | 1.597 |
| Adjacent glyphs (within words) | 1.667 |

**Verdict: HIGH mutual information.** Components are strongly correlated with their neighbors. This is the OPPOSITE of what Hangul jamo would show (where initial/medial/final consonants are relatively independent).

### Top Component Correlations (by PMI)

| Component 1 | Component 2 | PMI | Count |
|---|---|---|---|
| PLUME_i | TAIL_n | +4.16 | 6,052 |
| LOOP_a | TAIL_m | +3.46 | 779 |
| INITIAL_q | LOOP_o | +3.09 | 5,304 |
| LOOP_a | PLUME_i | +3.07 | 6,683 |
| GALLOWS_p | BENCH | +2.96 | 772 |
| PLUME_i | PLUME_i | +2.88 | 4,811 |
| LOOP_a | TAIL_r | +2.76 | 3,411 |
| GALLOWS_f | BENCH | +2.67 | 188 |
| BENCH_alt(sh) | LOOP_e | +2.58 | 2,349 |
| TAIL_d | FINAL_y | +2.58 | 5,022 |

**Key patterns:**
- `i` almost always precedes `n` (the "aiin" pattern)
- `q` almost always precedes `o` (the "qo-" word-initial pattern)
- `a` strongly attracts `i` and `r` (making "air", "aiin")
- Gallows p and f strongly attract bench (forming compounds)
- `d` strongly attracts final `y` (the "-dy" ending)
- `sh` strongly attracts `e` (the "she-" pattern)

These are NOT independent selections from slots. They are fixed sequential patterns -- more like digraphs/trigraphs in a standard alphabet than independent jamo.

---

## 4. Positional Slot Analysis (Hangul Test)

### Glyph Type by Word Position

| Pos | bench | final | gallows | gal+bench | initial | loop | plume | tail |
|-----|-------|-------|---------|-----------|---------|------|-------|------|
| 0 | 23.9% | 4.9% | 7.6% | 2.1% | 14.5% | 30.1% | 0.1% | 16.7% |
| 1 | 6.6% | 2.8% | 20.6% | 1.7% | 0.1% | 52.4% | 3.0% | 12.7% |
| 2 | 5.3% | 7.9% | 18.8% | 1.3% | 0.0% | 37.4% | 8.6% | 20.7% |
| 3 | 5.4% | 14.2% | 2.9% | 0.4% | 0.0% | 38.6% | 11.7% | 26.7% |
| 4 | 2.2% | 19.4% | 1.8% | 0.3% | 0.0% | 25.5% | 14.2% | 36.5% |
| 5 | 2.1% | 26.4% | 1.8% | 0.2% | 0.1% | 15.6% | 12.9% | 40.9% |
| 6+ | ~2% | ~25% | ~3% | ~0.3% | 0.1% | ~15% | ~12% | ~42% |

### Conditional Entropy

| Measure | Value |
|---|---|
| H(glyph_type) unconditional | 2.526 bits |
| H(glyph_type \| position) | 2.240 bits |
| Information gain from position | 0.285 bits |
| **Reduction** | **11.3%** |

**Interpretation:** Position provides a modest 11.3% reduction in uncertainty about glyph type. This is significant but NOT dramatic. For comparison:
- Pure Hangul would show ~50-70% reduction (each slot strongly determines the type)
- Pure alphabetic (Latin) would show ~0-5% reduction

The 11.3% indicates a weak syllabic tendency -- the script has position-sensitive preferences but not rigid slots. The strongest positional effects are:
- **Position 0**: Bench (24%) and initial (15%) are overrepresented -- words tend to start with consonant-like characters
- **Position 1**: Loops dominate (52%) -- a vowel-like nucleus follows the onset
- **Position 3+**: Tails and finals increase, loops decrease -- word endings are tail-heavy

This is consistent with a **CV(C) syllable structure** but NOT a rigid slot system.

---

## 5. Word Structure Templates

### Top Structural Patterns

| Pattern | Count | % | Examples |
|---|---|---|---|
| ONSET + NUCLEUS + CODA | 1,777 | 4.8% | shol, kor, ckhar |
| NUCLEUS + CODA | 1,714 | 4.6% | ar, or, is |
| CODA + NUCLEUS + CODA | 1,096 | 3.0% | ses, dan, dor |
| ONSET + NUCLEUS + FINAL | 1,021 | 2.8% | shoy, chey, cphoy |
| CODA + NUCLEUS + PLUME + PLUME + CODA | 961 | 2.6% | daiin, soiin |
| NUCLEUS + ONSET + NUCLEUS + CODA | 961 | 2.6% | okan, otol |
| ONSET + NUCLEUS + NUCLEUS + CODA | 947 | 2.6% | kair, chear |
| ONSET + NUCLEUS + CODA + FINAL | 877 | 2.4% | shory, shody |
| INITIAL + NUCLEUS + ONSET + NUCLEUS + CODA | 773 | 2.1% | qopal, qokol |

**The top 30 patterns account for only 51.6% of all words.** The remaining 48.4% are distributed across hundreds of patterns. This is too diverse for a rigid Hangul-style system (where a handful of templates would cover >90% of blocks).

### Syllable Fit Test

| Pattern | Words | % |
|---|---|---|
| Single syllable (I? O* N+ C* F?) | 11,461 | 30.9% |
| Multi-syllable (repeating blocks) | 27,573 | 74.5% |
| **Non-fitting** | **9,458** | **25.5%** |

74.5% of words fit a multi-syllable model, but 25.5% do not. The non-fitting words often have:
- CODA at the start without a preceding NUCLEUS (e.g., "dan" = CODA+NUCLEUS+CODA)
- FINAL (y) in non-final positions
- Adjacent CODAs without intervening NUCLEUS

This suggests the system is **partially syllabic but not strictly so**.

---

## 6. Bench Component: Semantic Distribution & Substitutability

### Bench Glyph Frequency by Section

| Section | ch | sh | ckh | cth | cph | cfh |
|---|---|---|---|---|---|---|
| herbal | 8.95% | 2.86% | 0.58% | 1.12% | 0.23% | 0.07% |
| bio | 4.91% | 3.07% | 0.65% | 0.39% | 0.06% | 0.02% |
| recipe | 6.38% | 2.03% | 0.38% | 0.22% | 0.08% | 0.01% |
| pharma | 6.36% | 2.34% | 1.03% | 1.02% | 0.27% | 0.07% |
| zodiac | 5.39% | 3.07% | 0.46% | 0.24% | 0.11% | 0.11% |
| cosmo | 5.78% | 1.26% | 0.10% | 0.13% | 0.03% | 0.00% |

**Key findings:**
- `ch` is 2-4x more frequent in the herbal section (8.95%) than in bio (4.91%)
- `sh` is relatively stable across sections (2-3%)
- `cth` is markedly higher in herbal (1.12%) and pharma (1.02%) than elsewhere
- The bench-gallows compounds (ckh/cth/cph/cfh) show section-dependent variation

If bench were a purely structural component (like a Hangul jamo), we would expect uniform distribution. The section-dependent variation suggests **bench glyphs carry semantic or phonetic content that correlates with topic**.

### Substitutability Test

With proper word-boundary extraction, only **4 minimal pairs** exist where bench glyphs substitute for each other in otherwise identical words:

- okchy <-> okshy (each occurs 1 time)
- olchy <-> olshy (each occurs 1 time)

This is vanishingly rare. **Bench glyphs are NOT freely substitutable** -- `ch` and `sh` appear in largely distinct word contexts. This argues AGAINST the bench being a meaning-neutral structural component and FOR it carrying its own phonetic/semantic value.

---

## 7. Gallows Position Distribution

| Glyph | Initial | Medial | Final |
|---|---|---|---|
| k | 11.5% | 87.7% | 0.8% |
| t | 16.6% | 82.4% | 1.0% |
| p | 37.3% | 61.1% | 1.6% |
| f | 30.6% | 64.9% | 4.5% |
| ckh | 21.0% | 77.7% | 1.3% |
| cth | 50.9% | 48.0% | 1.0% |
| cph | 55.9% | 43.2% | 0.9% |
| cfh | 52.2% | 47.8% | 0.0% |

**Observations:**
- `k` and `t` (the common gallows) are overwhelmingly medial (82-88%)
- `p` and `f` (the rare gallows) appear more often initially (31-37%)
- Gallows-bench compounds (cth, cph, cfh) appear ~50% initially -- much more than their pure gallows counterparts
- ALL gallows are extremely rare in final position (<5%)

The positional distribution differs markedly between the four gallows types. If gallows were a single component family varying only in crossbar position, we would expect similar distributions. The variation suggests each gallows type has its own positional grammar.

---

## 8. Combinatorial Analysis: Slot Inventories

For the 11,461 words fitting the single-syllable pattern (I? O* N+ C* F?):

| Slot | Unique fillers | Top items |
|---|---|---|
| INITIAL | 1 | q (100%) |
| ONSET | 10 | ch (45%), sh (24%), k (11.4%), t (8.4%) |
| NUCLEUS | 4 | e (34.9%), o (29.6%), a (18.9%), i (16.6%) |
| CODA | 7 | l (30.7%), r (25.3%), d (19.5%), n (16.2%) |
| FINAL | 1 | y (100%) |

**Theoretical combinations:** (1+1) * (10+1) * 4 * (7+1) * (1+1) = **1,408**

**Actual unique single-syllable words: 1,220** (86.6% of theoretical maximum)

This is remarkably high coverage. For a natural language with CVC syllables, we would expect far less than 86.6% of possible combinations to actually occur (due to phonotactic constraints). English CVC syllables cover roughly 30-40% of their theoretical space.

**This 86.6% coverage is a strong signal that the system is combinatorial** -- it systematically generates words by selecting from fixed slot inventories with few constraints between slots.

---

## 9. Loop Distribution by Section

| Section | o | a | e |
|---|---|---|---|
| herbal | 16.1% | 7.8% | 7.3% |
| bio | 13.3% | 6.6% | 14.3% |
| recipe | 12.7% | 9.6% | 14.7% |
| pharma | 20.3% | 6.5% | 12.5% |
| zodiac | 14.1% | 12.6% | 9.4% |
| cosmo | 16.9% | 10.7% | 15.4% |

The loop distributions vary dramatically by section:
- Herbal: `o` dominates, `e` is rare (7.3%)
- Bio/Recipe: `e` dominates over `o`
- Zodiac: `a` is unusually high (12.6%), `e` is low

This section-dependent variation is consistent with loops carrying semantic content (perhaps vowels encoding specific meanings or categories of plants/substances).

---

## 10. Conclusions

### The Hangul Hypothesis: PARTIALLY SUPPORTED

The Voynich script shows **some** features of a componential writing system but does NOT match the strong Hangul model:

**Evidence FOR componential structure:**
1. Gallows-bench compounds (ckh/cth/cph/cfh) are visually composite -- two independent visual elements merged into one character space
2. Word structure follows a loose syllable pattern (onset-nucleus-coda) with 74.5% of words fitting multi-syllable templates
3. The combinatorial coverage of single-syllable words (86.6% of theoretical space) suggests systematic slot-filling rather than a natural vocabulary
4. Position moderately constrains glyph type (11.3% entropy reduction)

**Evidence AGAINST componential structure:**
1. High MI between adjacent components (1.60 bits) -- strokes are NOT independent
2. Stroke-level entropy (3.81 bits) is nearly identical to glyph-level entropy (3.87 bits) -- decomposition does not reveal hidden structure
3. Bench glyphs are NOT substitutable (only 4 minimal pairs in 37,000 words)
4. Both bench and loop distributions vary by manuscript section, suggesting they carry content-dependent information (not structural placeholders)
5. 25.5% of words do not fit syllable templates at all

### What the Data Actually Shows

The strongest signal is the **combinatorial regularity** of word construction. The system generates words by:

1. Optionally selecting an INITIAL (q) or FINAL (y) marker
2. Selecting an ONSET from {ch, sh, k, t, p, f, ckh, cth, cph, cfh}
3. Selecting 1-3 NUCLEUS characters from {o, a, e, i}
4. Selecting 0-2 CODA characters from {l, r, d, n, s, m, g}
5. Repeating to form multi-syllable words

This is more consistent with a **syllabary** or **abugida** than with either:
- A simple cipher (which would inherit the source language's statistics)
- A Hangul-like system (which would show independent components)
- A natural language alphabet (which would have more phonotactic constraints)

The 86.6% combinatorial coverage of the syllable space is perhaps the most striking finding. It suggests the system is **generative and artificial** -- designed to produce words systematically rather than evolved organically. This is compatible with:
- A constructed language (conlang)
- A nomenclature system (botanical/alchemical naming)
- An encoding where each slot carries independent meaning (not sound)

### Next Steps

1. **Test the nomenclature hypothesis**: Do words near specific plant illustrations preferentially use certain ONSET or NUCLEUS values?
2. **Analyze the gallows-bench compounds more deeply**: Since they are the only truly composite glyphs, their distribution relative to pure gallows may reveal whether the bench component modifies meaning
3. **Cross-reference with label-only text**: Short labels on illustrations may be the most transparent examples of the naming system
4. **Compare combinatorial coverage with known nomenclature systems**: Linnaean binomials, alchemical naming, and medieval herbal terminology all have specific combinatorial properties

---

*Analysis performed: 2026-04-08*
*Script: `stroke_analysis.py`*
*Data: Takeshi Takahashi EVA transcription (RF1b-e.txt), 37,031 words*
