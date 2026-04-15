# Voynich Manuscript: Syllable-Level Cipher Decryption Attempt

**Hypothesis**: Each Voynich word encodes exactly ONE Latin syllable.
**Source text**: RF1b-e.txt (EVA transcription, full manuscript)
**Corpus**: 37,209 tokens, 8,245 distinct types

---

## Step 1: Top 50 Voynich Words by Frequency

| Rank | Word | Count | % |
|------|------|-------|---|
| 1 | daiin | 721 | 1.94% |
| 2 | aiin | 637 | 1.71% |
| 3 | ol | 597 | 1.60% |
| 4 | chey | 515 | 1.38% |
| 5 | ar | 455 | 1.22% |
| 6 | or | 393 | 1.06% |
| 7 | chol | 368 | 0.99% |
| 8 | qokeey | 366 | 0.98% |
| 9 | shey | 346 | 0.93% |
| 10 | chedy | 341 | 0.92% |
| 11 | al | 313 | 0.84% |
| 12 | dar | 287 | 0.77% |
| 13 | qokain | 272 | 0.73% |
| 14 | qokaiin | 255 | 0.69% |
| 15 | shedy | 255 | 0.69% |
| 16 | chy | 228 | 0.61% |
| 17 | qokeedy | 221 | 0.59% |
| 18 | chor | 215 | 0.58% |
| 19 | dy | 211 | 0.57% |
| 20 | okaiin | 202 | 0.54% |

## Step 2: Suffix/Ending Analysis

The Voynich vocabulary shows highly productive morphological patterns:

| Suffix | Total occurrences | Example words |
|--------|-------------------|---------------|
| -aiin | 1,670 | daiin(721), qokaiin(255), okaiin(202), otaiin(151), saiin(125) |
| -edy | 1,449 | chedy(341), shedy(255), qokeedy(221), qokedy(177), otedy(95) |
| -ol | 1,421 | chol(368), shol(176), cheol(160), qol(147), qokol(98) |
| -ey | 1,352 | chey(515), shey(346), qokey(188), otey(125), okey(107) |
| -eey | 1,254 | qokeey(366), okeey(198), cheey(189), oteey(160), sheey(141) |
| -ar | 1,057 | dar(287), otar(152), qokar(146), okar(131), char(79) |
| -hy | 858 | chy(228), chckhy(139), shy(103), cthy(101), chcthy(84) |
| -ain | 796 | qokain(272), dain(173), okain(126), otain(95), sain(68) |
| -al | 775 | dal(190), qokal(183), okal(147), otal(132), qotal(64) |
| -dy | 264 | chdy(109), chody(80), cheody(75) |

## Step 3: qo- Prefix Analysis

The qo- prefix is productive: it attaches to base words that also exist independently.

| qo-word | Count | Base word | Base count | Ratio |
|---------|-------|-----------|------------|-------|
| qokeey | 366 | keey | 76 | 4.8x |
| qokain | 272 | kain | 49 | 5.6x |
| qokaiin | 255 | kaiin | 74 | 3.4x |
| qokeedy | 221 | keedy | 31 | 7.1x |
| qokey | 188 | key | 33 | 5.7x |
| qokal | 183 | kal | 30 | 6.1x |
| qokedy | 177 | kedy | 25 | 7.1x |
| qokar | 146 | kar | 58 | 2.5x |
| qoky | 141 | ky | 19 | 7.4x |

The qo- form is consistently 3-7x more frequent than the base, suggesting it is a default/unmarked form, not a derived one.

## Step 4: Top Bigrams

| Word 1 | Word 2 | Count |
|--------|--------|-------|
| or | aiin | 58 |
| ar | aiin | 33 |
| ar | al | 33 |
| ol | aiin | 32 |
| chol | daiin | 29 |
| chol | chol | 22 |
| ol | chey | 21 |
| ol | chedy | 18 |
| ol | shedy | 16 |
| qokeey | qokeey | 16 |
| qokain | ol | 15 |
| ol | daiin | 15 |
| daiin | chey | 14 |
| chey | qokeey | 14 |
| shey | qokain | 14 |

## Step 5: Frequency-Rank Mapping Hypotheses

Five mapping hypotheses were tested, assigning the top 20 Voynich words to the top 20 Latin pharmaceutical syllables:

| Hypothesis | Mapping key | Bigram score |
|------------|-------------|-------------|
| H1 (pure frequency rank) | daiin=et, aiin=in, ol=de | 454 |
| H2 (daiin=de) | daiin=de, aiin=et, ol=in, chol=fo | 464 |
| H3 (chol=fo, daiin=um) | daiin=um, chol=fo, chey=de | 398 |
| H4 (botanical) | daiin=et, chol=fo, chey=in | 317 |
| H5 (chol=li) | daiin=um, chol=li, chey=in | 393 |

Bigram score = sum of occurrences where the mapped pair forms a valid Latin syllable combination. Higher is better.

**Best result**: H2 (score=464), notable hit: ol+daiin -> "inde" (thence/from there) x15

**Notable from H5**: chol+daiin -> "li+um" = "-lium" (x29) -- but this would make "chol chol" = "li li" which is nonsensical.

## Step 6: f47r (Grape/Vitis Page) Decryption Attempt

f47r text (77 tokens):
```
pchair oly sheaiin shol daiin chdy chokchol chol choldy dair chad aiin
dor chol chy chaiin ckhey chol dain okaiin qokcheo cthey chokain chol
daiin kchdal dain olshey chokolg folr chey so chol shol aiin shol shol
chdy cholol schesy kchor cthaiin chol chol chol chor ey sho keey chy
tchod choy sho cht chy kchar ctham qokokor chaiin okal chol daiin
okchokchor sy shy otcho keey tor chey otchy tchol dain dam dsho cphy
daiin daiiny
```

**Result**: Only 22 of 77 words (29%) are in the top-20 mapping. The decoded fragments are discontinuous and form no recognizable Latin pharmaceutical text under any hypothesis. Unmapped words like "pchair", "chokchol", "choldy", "kchdal" have no syllable assignment.

---

## Step 7: Critical Assessment

### Test 1: Vocabulary Size
- Voynich distinct types: **8,245**
- Expected Latin syllable inventory: **~200-300**
- Ratio: **33x too many types**
- **VERDICT: FAIL** -- Fatal mismatch. A 1:1 syllable cipher cannot produce 8,245 distinct codes for ~250 target syllables.

### Test 2: Hapax Legomena
- Words appearing exactly once: **5,702** (69.2% of all types)
- Words appearing 1-3 times: **7,001** (84.9% of all types)
- A syllable cipher with ~250 targets should have almost zero hapax
- **VERDICT: FAIL** -- 5,702 unique codes is incompatible with ~250 syllables

### Test 3: Frequency Distribution Shape
- Top word frequency: 1.94% (expected: ~3-5%)
- Distribution follows Zipf's law (compatible with natural language)
- **VERDICT: MARGINAL** -- shape OK, absolute values slightly low

### Test 4: Morphological Regularity
- qo- prefix: productive across 20+ word families
- -aiin suffix: productive across 8+ word families  
- -eey, -edy suffixes: similarly productive
- A syllable cipher should NOT show productive morphology
- **VERDICT: FAIL** -- these patterns indicate internal grammar

### Test 5: Bigram Validation
- No hypothesis produces consistently valid Latin words
- f47r decryption is 71% unmapped and unreadable
- **VERDICT: FAIL** -- no mapping yields pharmaceutical Latin

### Test 6: Line Length
- Average words per line: 7.5
- Expected Latin syllables per line: 8-15
- **VERDICT: PASS** -- compatible

---

## Overall Conclusion

**The one-word-one-syllable model is REJECTED.**

The hypothesis fails on 4 of 6 critical tests. The fatal flaw is the vocabulary size: 8,245 distinct Voynich word types cannot be a 1:1 mapping to ~250 Latin syllables. This is a 33x mismatch.

### Why the Model Fails

1. **Too many types**: 8,245 distinct words vs ~250 syllables means most Voynich words have no syllable to map to. Even with generous homophony (multiple codes per syllable), you would need ~33 homophones per syllable on average, which destroys any frequency-based decryption.

2. **Productive morphology**: The qo- prefix and -aiin/-eey/-edy suffixes operate as grammatical morphemes, not as arbitrary cipher codes. The system has internal structure that syllable substitution cannot explain.

3. **Hapax explosion**: 69% of word types appear exactly once. If these were syllable codes, it would mean 5,702 syllables appear only once in the entire text -- impossibly sparse for a ~250-syllable target language.

4. **No readable output**: When the best frequency-ranked mapping is applied to pages with known content (f47r, grape vine), the output is unreadable.

### What the Data Actually Suggests

The Voynich word system most likely encodes at the **word level** or represents a language/notation with its own morphology. The productive prefixes (qo-, o-, sh-, ch-) and suffixes (-aiin, -eey, -edy, -ol, -al, -ar) suggest one of:

- A natural language with agglutinative or fusional morphology
- A constructed notation system with compositional word formation
- A verbose cipher with extensive null characters and homophones (where many different codes map to the same plaintext)
- An entropy-controlled meaningless text with statistical regularities

### Possible Salvage

The syllable model could be partially rescued if:
- The 8,245 types are collapsed into ~250 equivalence classes by treating prefixes/suffixes as non-encoding "noise"
- Only the "core" of each word (after stripping qo-, d-, ch-, sh-, -aiin, -eey, etc.) encodes a syllable
- This would be a **verbose syllable cipher with null padding**, not a simple substitution

This refinement merits separate investigation but represents a fundamentally different model than "one word = one syllable."
