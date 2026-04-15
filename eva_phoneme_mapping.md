# EVA-to-Phoneme Mapping: Sandhi-Based Phonological Analysis

**Date:** 2026-04-05
**Source:** RF1b-e.txt (37,780 words extracted)
**Method:** Cross-word sandhi conditioning analysis

---

## Executive Summary

The Voynich manuscript's suffix alternation system (-r / -l / -n) provides a window into the phonological classes of EVA characters. By examining which suffix a preceding word selects when followed by a given initial character, we can classify EVA characters into phonological categories -- without needing to know their actual phonetic values.

Key findings:
1. Only EVA 'a' and 'i' behave as true vowels. EVA 'o' behaves as a fricative/nasal. EVA 'e' behaves as a stop.
2. The language has 3 clear consonant classes and at most 2-3 true vowels.
3. EVA 'y' (40% of all word-finals) is NOT part of the r/l/n system and functions as a default/unmarked ending.
4. The phonological system most closely resembles a Semitic language (few vowels, rich consonant classes) rather than Latin or Italian.

---

## 1. Phonological Class Assignment

### Method

For every word-initial EVA character (minimum 20 occurrences), we tabulate what suffix (-r, -l, -n) appears on the preceding word. The known sandhi rules predict:
- Vowel-initial words should be preceded by -r (65-67%)
- Stop-initial words should be preceded by -l (47-68%)
- Fricative-initial words should be preceded by -n (38-46%)

### Results: Simple Initial Characters (first letter)

| EVA char | N (as initial) | -r among r/l/n | -l among r/l/n | -n among r/l/n | Assigned class |
|----------|---------------|-----------------|-----------------|-----------------|----------------|
| **a** | 2333 | **64.6%** | 15.1% | 20.2% | VOWEL |
| **i** | 27 | **66.7%** | 27.8% | 5.6% | VOWEL |
| **x** | 21 | **50.0%** | 33.3% | 16.7% | VOWEL (tentative, low N) |
| **k** | 1142 | 15.5% | **66.7%** | 17.7% | STOP |
| **l** | 1415 | 20.5% | **60.1%** | 19.4% | STOP |
| **r** | 510 | 27.6% | **56.0%** | 16.4% | STOP |
| **d** | 3105 | 21.3% | **47.7%** | 31.0% | STOP |
| **t** | 1018 | 22.5% | **45.3%** | 32.2% | STOP |
| **e** | 354 | 34.4% | **40.7%** | 24.9% | STOP (weak) |
| **p** | 538 | 25.3% | 29.6% | **45.2%** | FRICATIVE |
| **f** | 129 | 32.6% | 30.4% | **37.0%** | FRICATIVE (weak) |
| **c** | 6881 | 30.2% | 31.5% | **38.2%** | FRICATIVE |
| **o** | 8654 | 33.8% | 27.2% | **39.0%** | FRICATIVE |
| **q** | 5387 | 23.5% | 38.5% | **38.1%** | FRICATIVE |
| **y** | 1925 | 34.1% | 25.9% | **40.0%** | FRICATIVE |
| **s** | 4286 | 31.1% | 34.3% | **34.6%** | MIXED (near-equal) |

### Results: Digraph Initials

| EVA digraph | N | -r% | -l% | -n% | Assigned class |
|-------------|-----|------|------|------|----------------|
| **a** | 2333 | **64.6%** | 15.1% | 20.2% | VOWEL |
| **i** | 27 | **66.7%** | 27.8% | 5.6% | VOWEL |
| **cfh** | 35 | **45.5%** | 36.4% | 18.2% | VOWEL (!) |
| **k** | 1142 | 15.5% | **66.7%** | 17.7% | STOP |
| **l** | 1415 | 20.5% | **60.1%** | 19.4% | STOP |
| **r** | 510 | 27.6% | **56.0%** | 16.4% | STOP |
| **d** | 3105 | 21.3% | **47.7%** | 31.0% | STOP |
| **t** | 938 | 22.1% | **47.6%** | 30.3% | STOP |
| **s** (alone) | 1332 | 23.7% | **45.8%** | 30.5% | STOP |
| **e** | 354 | 34.4% | **40.7%** | 24.9% | STOP (weak) |
| **qo** | 5262 | 23.5% | **38.5%** | 37.9% | borderline STOP/FRIC |
| **ch** | 6062 | 30.1% | 32.4% | **37.4%** | FRICATIVE |
| **sh** | 2954 | 33.0% | 31.4% | **35.7%** | FRICATIVE |
| **cth** | 469 | 29.3% | 24.9% | **45.8%** | FRICATIVE |
| **ckh** | 184 | 34.4% | 18.8% | **46.9%** | FRICATIVE |
| **cph** | 122 | 27.0% | 27.0% | **46.0%** | FRICATIVE |
| **tsh** | 80 | 26.9% | 19.2% | **53.8%** | FRICATIVE |
| **p** | 538 | 25.3% | 29.6% | **45.2%** | FRICATIVE |
| **o** | 8654 | 33.8% | 27.2% | **39.0%** | FRICATIVE |
| **y** | 1925 | 34.1% | 25.9% | **40.0%** | FRICATIVE |

---

## 2. Vowel Identification

### The Traditional View

EVA scholars traditionally consider 'a', 'o', 'e' as vowels. The sandhi data **strongly contradicts** this:

| EVA char | Traditional | Sandhi evidence | Verdict |
|----------|-------------|-----------------|---------|
| **a** | vowel | -r 64.6% -- clear vowel trigger | CONFIRMED VOWEL |
| **i** | vowel/semi | -r 66.7% -- clear vowel trigger | CONFIRMED VOWEL |
| **o** | vowel | -n 39.0% -- fricative trigger | **NOT A VOWEL** |
| **e** | vowel | -l 40.7% -- stop trigger | **NOT A VOWEL** |
| **y** | semivowel? | -n 40.0% -- fricative trigger | NOT A VOWEL |

### Critical Finding

**EVA 'o' is NOT a vowel in this phonological system.** It triggers -n (fricative behavior) with 39.0% among r/l/n, and is the most common word-initial character (22.9%). This is consistent with 'o' representing a consonant or a consonantal prefix.

**EVA 'e' is NOT a vowel either.** It triggers -l (stop behavior) with 40.7% among r/l/n.

**Only 'a' and 'i' are confirmed vowels.** This is a two-vowel system (possibly three if 'x' counts, though 'x' is very rare with only 21 occurrences).

### Implications

The Voynich script may encode a language with a minimal vowel inventory, or EVA 'o' and 'e' may represent consonants that were misidentified as vowels by transcribers due to their glyph shapes.

---

## 3. Consonant Subclasses

### Class 1: STOPS (trigger -l, 47-67%)

| Character | -l among r/l/n | Strength |
|-----------|---------------|----------|
| k | 66.7% | very strong |
| l | 60.1% | strong |
| r | 56.0% | strong |
| d | 47.7% | moderate |
| t | 47.6% | moderate |
| s (alone) | 45.8% | moderate |
| e | 40.7% | weak |

**Internal structure:**
- **Hard stops:** k (67%), l (60%) -- these are the most stop-like
- **Moderate stops:** d (48%), t (48%), r (56%) -- classic voiced/voiceless pair (d/t) plus r
- **Weak/marginal stops:** e (41%), s-alone (46%)

The grouping {k, t, d} matches the known sandhi rule. That EVA 'l' and 'r' also belong here is surprising -- in the Voynich phonology, they behave as stops, not liquids.

### Class 2: FRICATIVES/AFFRICATES (trigger -n, 37-54%)

| Character | -n among r/l/n | Strength |
|-----------|---------------|----------|
| tsh | 53.8% | strong |
| ckh | 46.9% | strong |
| cph | 46.0% | strong |
| cth | 45.8% | strong |
| p | 45.2% | strong |
| y | 40.0% | moderate |
| o | 39.0% | moderate |
| c/ch | 37.4% | moderate |
| f | 37.0% | moderate |
| sh | 35.7% | moderate |

**Internal structure:**
- **Strong fricatives:** tsh, ckh, cph, cth -- all complex digraphs/trigraphs, likely affricates
- **Moderate fricatives:** p, ch, sh, f -- includes 'p' which is traditionally a stop in most languages
- **Consonantal "vowels":** o, y -- classified here but may represent glides or special consonants

The grouping {c, p} triggering -n matches the known sandhi rule. The inclusion of EVA 'p' in the fricative class (not stop) suggests it may represent a fricative (like /f/, /v/, or /phi/) rather than a plosive.

### Class 3: VOWELS (trigger -r, 50-67%)

| Character | -r among r/l/n | Strength |
|-----------|---------------|----------|
| i | 66.7% | strong (low N=27) |
| a | 64.6% | very strong |
| x | 50.0% | moderate (low N=21) |
| cfh | 45.5% | borderline (low N=35) |

### Class 4: MIXED/AMBIGUOUS

| Character | Profile | Notes |
|-----------|---------|-------|
| s (as c-initial) | 31/34/35 | Nearly equal distribution |
| qo | 24/39/38 | Borderline stop/fricative |

---

## 4. Stem-Suffix Correlation (Internal Confirmation)

The suffix chosen is also conditioned by the stem-final character of the SAME word:

| Stem-final | Total | ->r | ->l | ->n |
|------------|-------|------|------|------|
| **i** | 6585 | 9.4% | 0.5% | **90.2%** |
| **o** | 5351 | 37.8% | **62.0%** | 0.1% |
| **a** | 4862 | **56.0%** | 41.6% | 2.4% |
| **e** | 85 | **58.8%** | 38.8% | 2.4% |
| **h** | 90 | 41.1% | **58.9%** | 0.0% |
| **d** | 69 | 30.4% | **69.6%** | 0.0% |
| **k** | 67 | 37.3% | **62.7%** | 0.0% |

**Key observations:**
- **-i stems almost exclusively take -n (90.2%)** -- this is the strongest rule in the entire system
- **-o stems strongly prefer -l (62.0%)** -- confirms known rule (79% was previously reported; our 62% may differ due to corpus section)
- **-a stems prefer -r (56.0%)** -- confirms known rule (77% previously; again our section shows 56%)
- **-e stems prefer -r (58.8%)** -- behaves like -a stems (vowel-like) in stem-final position

**Contradiction alert:** EVA 'e' triggers -l when it begins the NEXT word (stop behavior), but triggers -r when it ends the CURRENT word (vowel behavior). This suggests 'e' may represent different phonemes in different positions, or the stem-final and sandhi systems operate on different principles.

---

## 5. Proposed Phoneme Inventory

### Phonological Categories (Based on Sandhi Behavior)

**Category A -- Vowels (2-3 phonemes, trigger -r):**
- EVA 'a' = a true vowel (likely /a/)
- EVA 'i' = a true vowel (likely /i/)
- EVA 'x' = possibly a third vowel (insufficient data)

**Category B -- Stops/Plosives (5-6 phonemes, trigger -l):**
- EVA 'k' = strong stop (likely /k/ or /g/)
- EVA 't' = stop (likely /t/)
- EVA 'd' = stop (likely /d/)
- EVA 'l' = stop-like (possibly /l/ but functioning as stop in sandhi)
- EVA 'r' = stop-like (possibly a trill/tap functioning as stop)
- EVA 'e' = stop-like (nature unclear)

**Category C -- Fricatives/Affricates (8+ phonemes, trigger -n):**
- EVA 'ch' = fricative/affricate (possibly /tsh/, /x/, /kh/)
- EVA 'sh' = fricative (possibly /sh/)
- EVA 'cth' = fricative/affricate
- EVA 'ckh' = fricative/affricate
- EVA 'cph' = fricative/affricate
- EVA 'tsh' = strong fricative/affricate
- EVA 'p' = fricative (possibly /f/, /ph/, not /p/!)
- EVA 'f' = fricative
- EVA 'o' = consonantal (possibly a glide, /w/, or labialized consonant)
- EVA 'y' (initial) = consonantal (possibly a glide /j/)

**Category D -- Unmarked/Default:**
- EVA 'y' (final) = see Analysis 6 below

**Category E -- Ambiguous:**
- EVA 's' = near-equal distribution across all three classes
- EVA 'qo' = borderline stop/fricative (may be a single phoneme)

### Proposed Consonant-Vowel Chart

```
              Labial    Dental/Alv   Palatal    Velar     Glottal?
Stops:        ---       t, d         ---        k         ---
              (trigger -l)
Fricatives:   p/f       s?           sh, ch     ckh       ---
              (trigger -n)
Affricates:   cph       tsh          cth        ---       ---
              (trigger -n)
Glides:       o (/w/?)  ---          y (/j/?)   ---       ---
              (trigger -n)

Vowels:       a (/a/)   ---          i (/i/)    ---       ---
              (trigger -r)
```

**Total distinct phonological classes: 3 consonant types + 2 vowels = 5 categories**
**Estimated phoneme count: 2-3 vowels, 10-15 consonants**

---

## 6. Comparison with Known Language Phonologies

### Arabic (3 vowels, emphatic consonants)

| Feature | Arabic | Voynich (sandhi-based) | Match? |
|---------|--------|----------------------|--------|
| Vowel count | 3 (a, i, u) | 2-3 (a, i, x?) | STRONG |
| Consonant-heavy | Yes | Yes (15+ consonants) | STRONG |
| Fricative-rich | Yes (many fricatives) | Yes (8+ fricatives) | STRONG |
| Emphatic consonants | Yes (pharyngealized) | Possibly (cth, ckh, cph) | MODERATE |
| Root-pattern morphology | Yes | Unknown | ? |

**Match score: HIGH.** The 2-3 vowel system with rich fricatives is very Arabic-like.

### Hebrew

| Feature | Hebrew | Voynich | Match? |
|---------|--------|---------|--------|
| Vowel count | 5 (often reduced to 3) | 2-3 | MODERATE |
| Consonant classes | Stops, fricatives, gutturals | 3 classes | MODERATE |
| Prefix system | Yes (definite article, prepositions) | 'o-' as common prefix? | MODERATE |
| Suffix inflection | Yes | -r/-l/-n system | MODERATE |

**Match score: MODERATE.** The consonant system is broadly similar but Hebrew has more vowel distinctions.

### Latin (5 vowels, complex consonants)

| Feature | Latin | Voynich | Match? |
|---------|-------|---------|--------|
| Vowel count | 5 (a, e, i, o, u) | 2-3 | POOR |
| Sandhi system | Minimal | Extensive | POOR |
| Suffix-based case | Yes (but not sandhi) | -r/-l/-n alternation | WEAK |

**Match score: LOW.** Latin has too many vowels and no comparable sandhi system.

### Northern Italian Dialects

| Feature | N. Italian | Voynich | Match? |
|---------|-----------|---------|--------|
| Vowel count | 7-8 | 2-3 | POOR |
| Consonant types | Moderate | Rich fricatives | WEAK |
| Sandhi | Limited liaison | Extensive | POOR |

**Match score: LOW.** Northern Italian dialects have rich vowel systems, the opposite of what we observe.

### Turkish/Turkic Languages

| Feature | Turkish | Voynich | Match? |
|---------|---------|---------|--------|
| Vowel harmony | Yes (front/back) | -r/-l/-n could be harmony | MODERATE |
| Suffix alternation | Yes (e.g., -ler/-lar) | -r/-l/-n alternation | STRONG |
| Agglutinative | Yes | Possible | ? |
| Vowel count | 8 | 2-3 | POOR |

**Match score: MODERATE.** The suffix alternation pattern is remarkably similar to Turkish vowel harmony, but the vowel count is too low.

### Caucasian Languages (Georgian, etc.)

| Feature | Caucasian | Voynich | Match? |
|---------|-----------|---------|--------|
| Few vowels | Yes (some have 2-3) | 2-3 | STRONG |
| Rich consonants | Yes (ejectives, affricates) | Rich fricatives/affricates | STRONG |
| Complex onsets | Yes | Digraph/trigraph initials | MODERATE |

**Match score: MODERATE-HIGH.** The minimal vowel inventory with rich consonantal system is characteristic of Northwest Caucasian languages.

### Summary of Typological Fit

| Language family | Vowels | Consonants | Sandhi | Overall |
|----------------|--------|------------|--------|---------|
| Arabic/Semitic | STRONG | STRONG | MODERATE | **BEST FIT** |
| Caucasian | STRONG | STRONG | WEAK | GOOD FIT |
| Turkish | WEAK | MODERATE | STRONG | MODERATE |
| Hebrew | MODERATE | MODERATE | MODERATE | MODERATE |
| Latin | POOR | WEAK | POOR | POOR |
| N. Italian | POOR | WEAK | POOR | POOR |

---

## 7. The EVA 'y' Character: A Special Analysis

### Positional Distribution

| Position | Count | % of all 'y' |
|----------|-------|---------------|
| Word-final | 14,900 | 85.3% |
| Word-initial | 1,712 | 9.8% |
| Word-medial | 641 | 3.7% |
| Standalone word | 213 | 1.2% |
| **Total** | **17,466** | |

### Word-final 'y' -- What precedes it?

| Preceding char | Count | % |
|---------------|-------|-----|
| e | 5,094 | 34.2% |
| d | 4,865 | 32.7% |
| h | 2,263 | 15.2% |
| k | 715 | 4.8% |
| l | 603 | 4.0% |
| t | 427 | 2.9% |
| o | 303 | 2.0% |
| r | 293 | 2.0% |

Three characters account for 82.1% of all pre-y contexts: 'e' (34.2%), 'd' (32.7%), 'h' (15.2%).

### Does -y participate in sandhi?

**No.** The selectivity test (Analysis 9 in the raw data) shows that -y words are followed by a DIFFERENT distribution of initials than -r/-l/-n words:

| Following init | After -r | After -l | After -n | After -y | Baseline |
|---------------|----------|----------|----------|----------|----------|
| a- | 17.5% | 4.1% | 5.2% | **1.9%** | 6.2% |
| q- | 5.1% | 8.4% | 7.9% | **24.0%** | 14.3% |
| c- | 21.5% | 22.3% | 25.6% | **13.7%** | 18.2% |

Key deviations from baseline after -y:
- **q- is massively over-represented (+9.8%)** after -y
- **a- is massively under-represented (-4.3%)** after -y
- **c- is under-represented (-4.5%)** after -y

This means **-y is NOT phonologically neutral**. Words ending in -y preferentially appear before q-initial words and avoid a-initial words. This is the OPPOSITE of vowel behavior (vowels trigger -r which precedes a-initial words).

### Interpretation of -y

Several hypotheses:

1. **-y as a DIFFERENT morphological category.** The r/l/n suffixes may mark one grammatical class (e.g., nouns), while -y marks another (e.g., verbs, adjectives, or particles). The different distributional pattern after -y suggests it belongs to a different syntactic slot.

2. **-y as a consonant-final marker.** If -y represents a final consonant (like a glottal stop or a nasal), it would explain why it does not participate in the vowel/stop/fricative sandhi system -- sandhi only applies to vowel-final words (those ending in the stem vowel + r/l/n).

3. **-y as a "closed syllable" marker.** In many languages, open syllables (ending in vowels) behave differently from closed syllables (ending in consonants). The -r/-l/-n words may be "open" (suffix is a linking vowel or semivowel), while -y words are "closed."

4. **-y as a default/unmarked ending.** At 40% of all word-finals, -y may simply be the most common word-final phoneme (possibly /i/, /e/, or a reduced vowel). Its strong association with preceding 'e', 'd', 'h' suggests common morphological patterns (-ey, -dy, -hy as frequent word endings).

**Most likely interpretation:** -y marks a different morphosyntactic category from words ending in -r/-l/-n. The r/l/n system is a sandhi-driven suffix alternation on one word class, while -y endings belong to a different word class that does not undergo sandhi.

---

## 8. Revised EVA-to-Phoneme Mapping

Based on all analyses, here is the proposed mapping:

### High Confidence

| EVA | Phonological class | Possible phoneme | Confidence |
|-----|-------------------|------------------|------------|
| a | Vowel | /a/ | HIGH |
| i | Vowel | /i/ | HIGH (low N) |
| k | Stop | /k/ or /g/ | HIGH |
| d | Stop | /d/ | HIGH |
| t | Stop | /t/ | HIGH |
| ch | Fricative/Affricate | /x/, /kh/, or /tsh/ | HIGH |
| sh | Fricative | /sh/ or /s/ | HIGH |
| p | Fricative (not stop!) | /f/, /ph/, or /v/ | MODERATE |
| cth | Fricative | affricate or emphatic | MODERATE |

### Moderate Confidence

| EVA | Phonological class | Possible phoneme | Confidence |
|-----|-------------------|------------------|------------|
| l | Stop-class | /l/ (lateral stop?) | MODERATE |
| r | Stop-class | /r/ (tap as stop?) | MODERATE |
| o | Fricative-class | /w/, labiovelar, or consonantal prefix | MODERATE |
| y (initial) | Fricative-class | /j/ or palatal glide | MODERATE |
| y (final) | Separate system | morphological marker | MODERATE |
| e | Stop-class (initial), Vowel (final) | dual role or /e/ | LOW |
| s | Ambiguous | /s/ or /z/ | LOW |

### Low Confidence / Speculative

| EVA | Notes |
|-----|-------|
| q/qo | May be a single phoneme; borderline stop/fricative |
| x | Possibly a vowel but too rare to confirm |
| f | Fricative but very rare (130 occurrences as initial) |
| cfh | Behaves as vowel in sandhi (!) -- anomalous |

---

## 9. Open Questions

1. **Why does EVA 'o' behave as a consonant?** If 'o' = /w/ or a labialized consonant, this would explain both its high frequency (22.9% of initials) and its fricative sandhi behavior. Many Voynich words begin with 'o-' which may be a consonantal prefix.

2. **What is EVA 'e' really?** It behaves as a stop when word-initial but as a vowel when stem-final. This dual behavior could indicate:
   - Two different phonemes written with the same glyph
   - A phoneme that changes class by position (like English 'r')
   - An orthographic convention rather than a single phoneme

3. **Is EVA 's' one phoneme or two?** Its near-equal distribution across all three sandhi classes could mean it represents a phoneme at the boundary between classes, or that 's-' words are heterogeneous (multiple phonemes written as 's').

4. **The 'qo-' problem.** EVA 'q' almost always appears as 'qo-'. If this is a single phoneme, it has borderline stop/fricative behavior. If 'q' and 'o' are separate, the analysis needs revision.

5. **Morphological vs. phonological conditioning.** The sandhi system might not be purely phonological. The strong selectivity of -y for following q-words suggests there may be syntactic/morphological factors at play beyond pure phonology.

---

## 10. Methodological Notes

- **Corpus:** 37,780 words from RF1b-e.txt (full Voynich EVA transcription)
- **Bigram pairs analyzed:** 37,779
- **Minimum frequency threshold:** 20 occurrences for simple initials, 15 for digraph initials
- **Sandhi metric:** Percentage of -r/-l/-n among only r/l/n-final preceding words (excludes -y, -s, -m, etc.)
- **Digraph identification:** Trigraphs (cth, ckh, cfh, cph, tsh) checked before digraphs (ch, sh, ck, ct, cf, cp, qo, ts)
- **Cleaning:** Removed curly-brace annotations, @-codes, line-break markers (<->), punctuation
