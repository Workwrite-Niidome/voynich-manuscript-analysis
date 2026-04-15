# Abugida Hypothesis: Voynich Glyph Decomposition Analysis

## Overview

This analysis tests whether Voynich manuscript glyphs are composed of consonant + vowel components in an abugida structure (like Devanagari, Ethiopic, or Tibetan), where each character represents a consonant with an inherent vowel, and diacritical marks modify the vowel.

Data source: EVA transcription of 37,190 word tokens (8,518 unique) across 226 folios. Visual examination of manuscript pages f1r (page_003), f3r (page_005), f9r (page_020), f47r (page_093), f58r (page_115/116), and recipe sections (page_200).

---

## 1. Visual Decomposition of Glyphs

### Bench Series (ch, sh, ckh, cth, cph, cfh)

Examining the manuscript pages at 300dpi, the bench-family glyphs show clear two-part or three-part structure:

| EVA | Left component | Middle | Right component | Visually separable? |
|-----|---------------|--------|-----------------|-------------------|
| ch  | c-shaped curve | -- | vertical stroke + horizontal foot ("bench") | YES - distinct pen strokes |
| sh  | s-shaped curve | -- | identical bench as ch | YES |
| ckh | c-curve | gallows-k | bench | YES - three parts |
| cth | c-curve | gallows-t | bench | YES - three parts |
| cph | c-curve | gallows-p | bench | YES - three parts |
| cfh | c-curve | gallows-f | bench | YES - three parts |

The shared right component (the "bench" or EVA "h") is visually identical across all six glyphs. This is the strongest visual evidence for decomposability. The left component varies while the right stays constant -- exactly the pattern expected in an abugida where a consonant radical combines with a constant vowel marker.

### Gallows Characters (k, t, p, f)

Tall vertical strokes with varying top ornaments:
- **k**: vertical stroke with a loop/knot at top-left
- **t**: vertical stroke with a different loop configuration
- **p**: vertical stroke with two loops (resembles bench + gallows combined)
- **f**: vertical stroke with different double-loop

These share a common vertical stroke but differ in their upper decorations. This COULD represent consonant (top ornament) + vowel (vertical stroke), but the decomposition is less clean than for bench glyphs. The top ornaments are more integrated into the stroke than the separate left/right parts of bench glyphs.

### Loop Characters (e, o, a)

Simple, unitary shapes:
- **e**: a small pen loop (like a cursive 'e')
- **o**: a slightly different loop
- **a**: a loop with a tail or flourish

These show NO internal decomposition. If abugida, these would be pure vowels (no consonant component), analogous to standalone vowel characters in Devanagari.

### Coda Characters (y, n, r, l, m, s)

Appear overwhelmingly at word-final position:
- **y**: 85% at word-end
- **n**: 97% at word-end
- **r**: 78% at word-end
- **l**: 57% at word-end

These are simple strokes (tails, flourishes, final marks). Under the abugida hypothesis, these could be consonant codas without an inherent vowel -- analogous to virama-marked consonants in Devanagari.

---

## 2. Statistical Tests

### Test A: Vowel Distribution After Onset Types

If bench glyphs are C+V(inherent), then the explicit vowel following them should show a specific pattern. In a true abugida, the inherent vowel appears when NO explicit vowel mark is written.

| Onset | n | e% | o% | a% | y% | Dominant |
|-------|---|----|----|----|----|----------|
| ch    | 9384 | 53.9 | 28.1 | 5.5 | 12.5 | e |
| sh    | 3707 | 63.0 | 25.4 | 3.7 | 7.8 | e |
| ckh   | 817 | 29.4 | 12.0 | 4.2 | 54.5 | y |
| cth   | 841 | 22.4 | 26.3 | 7.8 | 43.5 | y |
| k     | 8364 | 47.5 | 8.6 | 35.0 | 8.9 | e |
| t     | 4693 | 40.4 | 15.5 | 33.9 | 10.3 | e |
| p     | 504 | 3.0 | 44.0 | 39.1 | 13.9 | o |

**Key observation**: The dominant vowel DIFFERS by onset type. ch/sh prefer 'e', ckh/cth prefer 'y', k/t prefer 'e', p prefers 'o'. In a true abugida, we would expect the SAME inherent vowel for all characters of the same visual class (bench or gallows). The variation suggests these are not simple C+V units.

### Test B: Entropy of Vowel Selection

Maximum entropy (4 equal vowels) = 2.00 bits. Expected values:
- Pure abugida (one inherent vowel >70%): H < 1.0 bits
- Pure alphabet (vowels independent): H > 1.5 bits

| After | Entropy (bits) | Assessment |
|-------|---------------|------------|
| ch    | 1.60 | Intermediate |
| sh    | 1.39 | Slightly low |
| ckh   | 1.55 | Intermediate |
| cth   | 1.80 | Near-alphabetic |
| k     | 1.66 | Intermediate |
| t     | 1.81 | Near-alphabetic |
| p     | 1.60 | Intermediate |

**Result**: Entropy ranges 1.39-1.81 bits. This is INCONSISTENT with pure abugida (too much vowel variation; all values above 1.0) but also somewhat skewed compared to pure alphabet. The system shows vowel PREFERENCES but not vowel DETERMINATION by the preceding consonant.

### Test C: Bare vs. Vowel-Marked Frequency

In a true abugida, the bare consonant (without explicit vowel mark) represents C + inherent_vowel and should be a significant proportion:

| Glyph | Bare (word-end) | + Vowel | + Consonant |
|-------|----------------|---------|-------------|
| ch    | 0.4% | 85.6% | 14.0% |
| sh    | 0.9% | 89.4% | 9.7% |
| ckh   | 1.4% | 94.9% | 3.7% |
| cth   | 1.6% | 94.1% | 4.4% |
| k     | 1.1% | 85.4% | 13.6% |
| t     | 1.3% | 78.1% | 20.6% |
| p     | 2.3% | 36.0% | 61.7% |
| f     | 7.4% | 41.5% | 51.1% |

**Result**: Bench glyphs almost NEVER appear bare (0.4-1.6%). They are almost always followed by an explicit vowel character. In Devanagari, bare consonants (with inherent 'a') account for roughly 30-40% of consonant occurrences. The near-zero bare rate suggests the "h" component of bench glyphs is NOT functioning as an inherent vowel marker.

**Exception**: p and f show high consonant-following rates (52-62%), mostly followed by 'c' (forming cph, cfh bench compounds). This means p and f rarely appear independently -- they are usually embedded within bench glyphs.

### Test D: Positional Distribution

| Glyph | Start | Early | Mid | Late | End |
|-------|-------|-------|-----|------|-----|
| ch    | 0.59 | 0.18 | 0.15 | 0.08 | 0.00 |
| sh    | 0.74 | 0.12 | 0.09 | 0.05 | 0.00 |
| k     | 0.16 | 0.39 | 0.31 | 0.12 | 0.02 |
| t     | 0.23 | 0.46 | 0.19 | 0.11 | 0.02 |
| e     | 0.03 | 0.12 | 0.31 | 0.40 | 0.14 |
| o     | 0.42 | 0.20 | 0.10 | 0.17 | 0.11 |
| y     | 0.10 | 0.02 | 0.02 | 0.01 | 0.85 |
| n     | 0.00 | 0.01 | 0.01 | 0.01 | 0.97 |

Bench glyphs (ch, sh) are strongly word-initial (59-74% at start). Gallows (k, t) are more medial (39-46% in early-to-mid positions). Loop characters (e) cluster late. Codas (y, n) are overwhelmingly final.

This is consistent with an onset-nucleus-coda syllable model: **bench/gallows = onset**, **loops = nucleus**, **codas = coda**. This pattern works for BOTH abugida and alphabetic systems.

---

## 3. The ckh/cth Problem

The bench compounds ckh, cth, cph, cfh present a structural problem for the abugida hypothesis:

If ch = C(c) + V(h), then what is ckh?
- Option A: C(ck) + V(h) -- but 'ck' as a single consonant is unusual
- Option B: C(c) + C(k) + V(h) -- a consonant CLUSTER with vowel marker
- Option C: Three separate components: c + k + h

Option B is most consistent with the visual structure (three separable parts) and with the statistical behavior (ckh behaves differently from ch in vowel preferences).

But consonant clusters before a vowel marker are rare in true abugidas. In Devanagari, clusters use special conjunct forms. In Ethiopic, there are no clusters at all. The existence of freely combinable C+C+V sequences is more characteristic of an ALPHABET with ligature conventions.

---

## 4. Inventory Comparison with Italian

### Abugida Decomposition

If we decompose all glyphs into consonant and vowel components:

**Consonant components (11)**:
c, s, k, t, p, f (from bench and gallows), d, l, r, n, m (standalone)

**Vowel components (6)**:
h (bench marker), e, o, a, y, i

**Special**: q (always paired with o; possibly a determiner or article marker)

**Italian phonology**: ~15 consonants (p, b, t, d, k, g, f, v, s, z, ts, dz, m, n, l, r + affricates), 7 vowels (a, e open, e closed, i, o open, o closed, u)

| | Abugida model | Italian |
|---|---|---|
| Consonants | 11 | 15 |
| Vowels | 6 | 7 |
| Gap | 4 consonants short | -- |

The consonant gap of 4 could be filled by: voiced stops (b, d, g -- but d exists), affricates (ts, dz), palatals (gn, gl), or the voiced/voiceless distinction could be unwritten.

The vowel count (6) is close to Italian (7), especially if 'y' and 'i' represent different vowel qualities (e.g., open vs. closed 'e').

---

## 5. Verdict: Is the Voynich Script an Abugida?

### Evidence FOR abugida structure:

1. **Visual decomposability**: Bench glyphs clearly consist of a variable left element + constant right element ("bench/h"). This is the structural hallmark of an abugida.

2. **Shared component**: The "h" bench component is visually identical across ch, sh, ckh, cth, cph, cfh -- exactly as a vowel diacritic would be.

3. **Inventory size**: Decomposition yields 11 consonants + 6 vowels, which is a plausible match for a Romance language (Italian: 15C + 7V).

4. **Positional behavior**: Bench/gallows at word-onset, loops at nucleus, codas at word-end follows C-V-C syllable structure.

### Evidence AGAINST abugida structure:

1. **No inherent vowel behavior**: Bench glyphs appear bare only 0.4-1.6% of the time. In real abugidas, the bare consonant (= inherent vowel) is the most common form (30-40%). Bench glyphs are almost always followed by an explicit vowel.

2. **Vowel entropy too high**: After each consonant type, the following vowel has entropy of 1.4-1.8 bits (max 2.0). In abugidas, this should be well below 1.0 bit (one vowel dominant >70%).

3. **Different vowel preferences per consonant**: ch/sh prefer 'e', ckh/cth prefer 'y', p prefers 'o'. In an abugida, the inherent vowel is the SAME for all consonants of a class.

4. **Consonant clusters in bench compounds**: ckh = c+k+h with three components. True abugidas rarely allow free consonant clustering before the vowel marker.

5. **Bench "h" is NOT the inherent vowel**: If "h" were the inherent vowel, then "ch" alone should represent a full syllable (like "ka" in Devanagari). But "ch" almost always requires an additional vowel character (e, o, y). The "h" functions more as a structural element of the glyph than as a phonetic vowel.

### Conclusion

**The Voynich script is NOT a true abugida**, but it does show **abugida-LIKE visual structure** in the bench series. The most accurate characterization is:

**A featural or semi-featural alphabet with ligature conventions.**

The bench component ("h") is a shared structural element that groups certain consonant glyphs into a visual family, but it does not encode an inherent vowel. It may represent:

- A graphical convention (like the shared vertical stroke in Latin b, d, h, k, l)
- A phonetic FEATURE (e.g., marking manner of articulation: all bench consonants are fricatives/affricates?)
- A cipher construction element (grouping functionally related characters)

The system behaves statistically like an **alphabet** (explicit vowels required, moderate vowel entropy, positional independence) with **visual compositionality** that superficially resembles an abugida.

### Alternative: "Pseudo-Abugida" Cipher Design

One possibility is that the script was deliberately DESIGNED to resemble an abugida (to an observer familiar with Near Eastern scripts) while actually functioning as a simple alphabet or cipher. This would be consistent with a 15th-century European author who had seen but not deeply understood abugida scripts (e.g., through Ethiopic texts reaching Italy, or knowledge of Hebrew/Arabic consonantal writing).

---

## 6. Summary Table: Glyph Classes

| Class | EVA glyphs | Visual structure | Phonetic role | Count |
|-------|-----------|-----------------|---------------|-------|
| Bench | ch, sh, ckh, cth, cph, cfh | left-element + bench | Onset consonant (+ implicit structural marker) | 6 |
| Gallows | k, t, p, f | vertical + top ornament | Onset consonant (k,t standalone; p,f mostly in bench compounds) | 4 |
| Loops | e, o, a | simple loops | Vowels / syllable nucleus | 3 |
| Codas | y, n, r, l, m, s | tails/flourishes | Word-final consonants or vowels | 6 |
| Special | q (+o), i, d | various | q=determiner?; i=in sequences (aiin); d=onset/medial | 3 |
| **Total** | | | | **22** |

---

*Analysis date: 2026-04-10*
*Data: Voynich MS EVA transcription, 37,190 tokens, 226 folios*
*Visual sources: Yale Beinecke MS 408 facsimile pages at 300dpi*
