# Voynich Manuscript: Homophone Collapse Language Identification

## Approach

This analysis tests the hypothesis that the Voynich manuscript's EVA alphabet contains **homophones** -- multiple symbols encoding the same phoneme. If we identify the correct collapse mapping (merging homophones into single characters), the resulting text might exhibit statistical properties matching a known natural language.

**Corpus**: RF1b-e.txt EVA transcription
- **37,724 words** extracted
- **8,476 unique words**
- **188,403 total characters**
- **25 distinct EVA characters** (a-z minus some letters)

---

## 1. Distributional Similarity: Finding Homophones

For each pair of EVA characters, we computed **bigram context similarity** -- the cosine similarity of what characters appear before and after each character. Characters in truly homophonic relationship should have nearly identical distributional contexts.

### Top Homophone Candidates by Context Similarity

| Pair | Left Sim | Right Sim | Combined | Freq1 | Freq2 | Assessment |
|------|----------|-----------|----------|-------|-------|------------|
| **f - p** | 0.978 | 0.984 | **0.981** | 491 | 1,654 | STRONG homophone |
| **k - t** | 0.984 | 0.967 | **0.976** | 10,785 | 6,994 | STRONG homophone |
| **c - s** | 0.980 | 0.930 | **0.955** | 13,096 | 6,997 | STRONG homophone |
| m - r | 0.901 | 0.990 | 0.945 | 1,065 | 7,559 | Possible (right-context dominated) |
| l - r | 0.903 | 0.970 | 0.936 | 10,653 | 7,559 | Possible (right-context dominated) |
| g - r | 0.788 | 0.991 | 0.890 | 165 | 7,559 | Weak (g is rare) |
| g - m | 0.719 | 1.000 | 0.859 | 165 | 1,065 | Weak (both rare-ish) |

### Key Finding: Three Very Strong Homophone Pairs

The distributional evidence strongly supports three homophone pairs:

1. **f/p** (combined 0.981): Nearly identical left AND right contexts. f is 3.4x rarer than p. These are almost certainly the same phoneme.

2. **k/t** (combined 0.976): Very high bilateral similarity. Both are high-frequency. This is surprising -- k and t look quite different in EVA. But distributionally they are interchangeable.

3. **c/s** (combined 0.955): High bilateral similarity. In EVA, these form the first element of digraphs (ch/sh, ck/sk). Their interchangeability confirms that ch and sh may encode the same sound.

### Comparison with Glyph-Based Expectations

| Expected Pair | Context Similarity | Verdict |
|---------------|-------------------|---------|
| i/ii (length variant) | N/A (substring) | Confirmed by word-level analysis |
| e/ee (length variant) | N/A (substring) | Confirmed by word-level analysis |
| ch/sh (glyph-similar) | c-s: 0.955 | **CONFIRMED** |
| d/s | d-s: not in top 25 | **NOT SUPPORTED** -- d and s have different distributions |
| o/a | o-a: not in top 25 | **NOT SUPPORTED** -- o and a are distributionally distinct |
| f/p | 0.981 | **CONFIRMED** |

**Surprise finding**: k-t homophony (0.976) was not predicted from glyph similarity but is the second-strongest signal in the data.

---

## 2. Minimal Pair Analysis

We searched for **minimal pairs** -- words that differ by exactly one substitution. Abundant minimal pairs between two characters suggest they are NOT homophones (they create meaning distinctions), while their absence suggests homophony.

| Pair | Minimal Pairs Found | Example | Interpretation |
|------|---------------------|---------|----------------|
| **o / a** | **494** | chol(359) / chal(57) | **NOT homophones** -- massive number of minimal pairs |
| **ch / sh** | **603** | chey(494) / shey(339) | Ambiguous -- many pairs, but both forms are very frequent |
| **d / s** | **353** | ald(2) / als(6) | **NOT homophones** -- substantial minimal pairs |
| **e / y** | **160** | che(17) / chy(215) | **NOT homophones** -- clear frequency asymmetry in pairs |
| **k / q** | **57** | kaiin(71) / qaiin(2) | Possible -- few pairs, q-forms always much rarer |
| **p / f** | **128** | chep(4) / chef(1) | Compatible with homophony -- pairs exist but are rare relative to corpus |

### Minimal Pair Paradox for ch/sh

The 603 minimal pairs for ch/sh seem to argue against homophony. However, the distributional similarity of c and s is 0.955. This paradox might be explained by:
- ch/sh could be phonetically similar but not identical (e.g., /t_S/ vs /S/)
- The scribe may have had loose rules for when to use each
- The minimal pairs might not represent true meaning differences if the text itself is encoded/constructed

---

## 3. Collapse Mapping Results

### 3a. Minimal Collapse (ii->i, ee->e)

| Metric | Value |
|--------|-------|
| Distinct characters | 25 (unchanged) |
| Unique words | 7,525 (from 8,476, -11.2%) |
| Avg word length | 4.72 (from 4.99) |
| Vowel ratio (aeiou) | 0.347 |

**Top 5 words**: dain (903), ain (746), chey (684), qokey (582), qokain (529)

**Assessment**: This is the least controversial collapse. The reduction from 8,476 to 7,525 unique words (-11.2%) shows that i/ii and e/ee length variants account for ~950 "false" word types. The word-type reduction is moderate, suggesting these ARE largely interchangeable.

### 3b. Moderate Collapse (+ sh->ch, f->p)

| Metric | Value |
|--------|-------|
| Distinct characters | 24 |
| Unique words | 6,824 (-19.5%) |
| Avg word length | 4.72 |
| Vowel ratio | 0.347 |

**Top 5 words**: chey (1168), dain (903), ain (746), chedy (665), qokey (582)

**Assessment**: Merging sh->ch dramatically increases chey to 1,168 occurrences (3.1% of all words). This would make it the dominant function word. No natural language has a single word at >3% unless it's a very common article/particle ("the" in English is ~7%, "de" in French ~3%).

### 3c. Aggressive Collapse (+ q->k, y->i)

| Metric | Value |
|--------|-------|
| Distinct characters | 22 |
| Unique words | 6,757 (-20.3%) |
| Avg word length | 4.72 |
| **Vowel ratio** | **0.445** |

**Top 5 words**: chei (1168), dain (903), ain (746), chedi (665), kokei (582)

**Key result**: The vowel ratio jumps to **0.445**, which is very close to Latin (0.45) and Italian (0.48). This is the most natural-looking vowel ratio of all collapse levels.

**Common word matches**:
- Italian: 2 matches (di, al)
- Hebrew: 2 matches (kol, al)

### 3d. Very Aggressive Collapse (+ ck->k, ph->p, ct->t, d->t)

| Metric | Value |
|--------|-------|
| Distinct characters | 21 |
| Unique words | 6,453 (-23.9%) |
| Avg word length | 4.67 |
| Vowel ratio | 0.450 |

**Top 5 words**: chei (1168), tain (961), ain (746), cheti (709), kokei (582)

**Assessment**: Merging d->t is too aggressive. The minimal pair evidence (353 d/s pairs) shows d is NOT interchangeable with other consonants. This collapse destroys valid distinctions.

---

## 4. Data-Driven Collapse (Automatic Merging)

Using only the distributional similarity data (threshold-based merging of the most similar pairs):

### Threshold 0.95: Merge f->p, t->k, s->c

| Metric | Value |
|--------|-------|
| Distinct characters | 22 |
| Unique words | 6,980 |
| Top word | chey (833) |

This data-driven result merges exactly the three strongest homophone pairs. It reduces the alphabet from 25 to 22 characters. The resulting text has:
- 22 characters (close to Hebrew 22, Latin 23, Italian 21)
- Average word length 4.99
- The digraphs ch/ck/ct all become ch/ck/ck (since s->c merges sh into ch)

### Threshold 0.90: Additionally merge m->r, r->l

| Metric | Value |
|--------|-------|
| Distinct characters | 21 |
| Unique words | 6,336 |
| Top word | ol/chol/chey (all ~830) |

### Threshold 0.80: Additionally merge g->l

| Metric | Value |
|--------|-------|
| Distinct characters | 19 |
| Unique words | 6,032 |

---

## 5. Language Scoring Summary

Composite scores (word length match + character count match + vowel ratio match + common word overlap), scale 0-100:

| Collapse Level | Latin | Italian | German | Arabic | Hebrew |
|----------------|-------|---------|--------|--------|--------|
| Minimal | 51.0 | 52.0 | 59.0 | 29.7 | 29.7 |
| Moderate | 54.0 | 55.0 | 56.0 | 29.7 | 29.7 |
| **Aggressive** | **63.7** | **75.7** | 50.7 | 20.5 | 25.5 |
| Very Aggressive | 60.7 | 73.7 | 46.7 | 20.0 | 25.0 |

**Italian scores highest under aggressive collapse** (y->i, q->k, sh->ch, f->p, ii->i, ee->e).

The rank-frequency correlation with known languages (comparing the shape of the frequency curve, not letter identity):

| Collapse | Latin | Italian | German | Arabic | Hebrew |
|----------|-------|---------|--------|--------|--------|
| Aggressive | 0.985 | 0.980 | 0.937 | 0.953 | 0.964 |

Latin and Italian have the best rank-frequency curve match across all collapse levels.

---

## 6. Morphological Evidence

### Word-initial patterns (prefix-like behavior)

| Initial | Freq | % | Possible interpretation |
|---------|------|---|------------------------|
| o- | 8,643 | 22.9% | Article/preposition prefix? |
| ch- | 6,052 | 16.0% | Very common word-start (digraph) |
| qo- | 5,257 | 13.9% | Prefix combination? (q always followed by o) |
| sh- | 2,952 | 7.8% | If ch/sh homophonic, this merges with ch- |
| ot- | 2,510 | 6.7% | o + t prefix? |
| ok- | 2,441 | 6.5% | o + k prefix? |
| da- | 1,928 | 5.1% | Could be a prefix |

**Key observation**: 'q' almost exclusively appears as 'qo-' at word start (5,257 of 5,430 total q). This is highly non-random and suggests qo- is a functional unit (prefix, article, or first syllable).

### Word-final patterns (suffix-like behavior)

| Final | Freq | % | Possible interpretation |
|-------|------|---|------------------------|
| -y | 15,087 | 40.0% | Dominant ending -- nominal/adjectival? |
| -n | 6,065 | 16.1% | Second most common (often -in, -ain) |
| -l | 5,741 | 15.2% | Third (often -ol, -al) |
| -r | 5,722 | 15.2% | Fourth (often -ar, -or) |
| -s | 1,376 | 3.6% | Possible plural? |
| -m | 1,018 | 2.7% | If m/r homophonic, merges with -r |

**Key observation**: The suffix system is remarkably constrained. Just four endings (-y, -n, -l, -r) account for **86.5%** of all words. This is highly unusual for natural languages (Italian endings: -a, -e, -i, -o, -n cover about 80%, but more evenly distributed).

---

## 7. The ch/sh Question

The ch/sh pair is central to the homophone hypothesis. Evidence:

**For homophony**:
- c and s have distributional similarity 0.955
- sh->ch collapse produces natural-looking word frequencies
- ch and sh share almost all of their combinatorial contexts

**Against homophony**:
- 603 minimal pairs exist (chol/shol, chey/shey, etc.)
- Both forms are very frequent (not one rare variant of the other)
- The minimal pairs include high-frequency words (chey 494 vs shey 339)

**Resolution**: ch and sh may represent a **phonetic near-merger** (like pin/pen in Southern US English) rather than true homophones. The scribe may have inconsistently distinguished /tS/ and /S/, or the distinction may have been regional/dialectal. This is consistent with an Italian/Romance language where 'c' before front vowels and 'sc' were phonetically close.

---

## 8. Conclusions

### Most Likely Homophone Pairs (confidence-ranked)

1. **f / p** -- Confidence: VERY HIGH (distributional similarity 0.981, f is 3.4x rarer)
2. **ii / i / iii** -- Confidence: VERY HIGH (length variants, 11.2% word-type reduction)
3. **ee / e / eee** -- Confidence: VERY HIGH (length variants)
4. **k / t** -- Confidence: HIGH (distributional similarity 0.976, unexpected but consistent)
5. **c / s** (and thus ch / sh) -- Confidence: MODERATE (similarity 0.955, but 603 minimal pairs)
6. **q / k** -- Confidence: MODERATE (q is basically "qo-" prefix form of k)

### Pairs That Are NOT Homophones

1. **o / a** -- 494 minimal pairs, clearly distinct phonemes
2. **d / s** -- 353 minimal pairs, clearly distinct
3. **e / y** -- 160 minimal pairs with strong frequency asymmetry
4. **l / r** -- Though right-context similarity is 0.970, they occupy different word positions

### Best Language Match

**Italian / Romance language** scores highest under aggressive collapse (75.7/100), driven by:
- Vowel ratio 0.445 (close to Italian 0.48 and Latin 0.45)
- Word length 4.72 (close to Italian 5.0)
- 22 distinct characters (close to Italian 21)
- Common word matches: "di", "al"
- Best rank-frequency curve correlation

However, major caveats:
- Only 2 common words matched out of 20 tested
- The word-final distribution (-y at 40%) is unlike any known Romance language
- The morphological patterns (constrained prefix/suffix system) look more like an **agglutinative** or **constructed** notation than natural Italian

### The Deeper Problem

Even the best collapse mapping fails to produce text that looks like natural language in key ways:
1. **Word-final -y at 40%** is far too dominant for any natural language
2. **qo- prefix** at 14% has no natural language parallel
3. **Only 2/20 common words match** any candidate language
4. The **suffix system** (-y, -n, -l, -r = 86.5%) is too constrained

This suggests that even if the underlying language is Romance, the encoding system involves more than simple homophonic substitution. There may be additional layers:
- Null characters (characters that encode nothing)
- Verbose cipher elements (extra characters inserted by rule)
- A syllabary or mixed phonemic/logographic system
- Or the text may not encode natural language at all

### Recommended Next Steps

1. **Null character testing**: Remove candidate null characters (e.g., the -y ending, or the o- in qo-) and re-test
2. **Syllable-level collapse**: Treat common bigrams (ch, sh, qo, ot, ok, ai, etc.) as single units and analyze at the syllable level
3. **Prefix/suffix stripping**: Remove qo-, o-, -y, -in, -ain before language matching
4. **Combined approach**: Apply the f->p, k/t merge, c/s merge, PLUS null removal, then test
