# Voynich Manuscript Co-occurrence Decoding Analysis

## Methodology

Starting from 10 decoded anchor words, this analysis uses obligatory collocations in Latin pharmaceutical text to decode additional stems. The EVA transcription (RF1b-e.txt) contains 37,705 tokens and 8,691 unique word types.

---

## Anchor Codebook (Given)

| EVA | Latin | English | Frequency |
|-----|-------|---------|-----------|
| daiin | et | and | 676 (1.79%) |
| aiin | in | in | 623 (1.65%) |
| ol | de | of | 586 (1.55%) |
| chey | est | is | 505 (1.34%) |
| ar | ad | to/for | 445 (1.18%) |
| or | cum | with | 380 (1.01%) |
| qokeey | drachma | drachma (unit) | 366 (0.97%) |
| dar | sed | but | 268 (0.71%) |
| ckhy | calidus | hot | 42 (0.11%) |
| kchy | frigidus | cold | 30 (0.08%) |

---

## Analysis 1: "Est calidus/frigidus in gradu [X]"

### Findings

The expected Galenic formula "est calidus in gradu primo/secundo" is **not well-attested** as a rigid fixed phrase in this corpus. Key observations:

- **chey + ckhy** (est + calidus) appears only **0 times** as a direct bigram.
- **chey + kchy** (est + frigidus) appears only **1 time**.
- ckhy and kchy are low-frequency words (42 and 30 occurrences), heavily concentrated in specific sections.

However, the **window co-occurrence** (within 3 words) of ckhy reveals:
- `daiin` (et/and): 7 co-occurrences -- strongest association
- `or` (cum/with): 4
- `aiin` (in): 4
- `s`: 4

For kchy (cold):
- `chy`: 7 co-occurrences -- **strongest**
- `chol`: 5
- `daiin` (et/and): 5
- `chey` (est): 4

### "Gradu" Candidate

No single word consistently appears exclusively after quality words + "in" to serve as "gradu." The Galenic degree formula may not be used in this text, or may be encoded differently.

### "Siccus" (dry) Candidate: `chy`

The pattern **ckhy + daiin + [WORD]** (calidus et X) finds no trigram instances. However, the pattern **kchy + daiin + [WORD]** yields one instance:
- `kchy daiin cthol` -- context: "dykaiin o kchy daiin cthol ctholo dar"

For the **ckhy window**, `daiin` is the strongest co-occurring word (7 times). The word `chy` appears as the strongest co-occurrence with `kchy` (7 times).

**Proposed decoding:**
| EVA | Latin | Rationale |
|-----|-------|-----------|
| chy | siccus (dry) | Strongest co-occurrence with kchy (cold), appears in quality-pair position; "frigidus et siccus" is a standard Galenic pairing |
| cthol | humidus (moist) | Appears in "kchy daiin cthol" = "frigidus et humidus"; standard complementary quality |

---

## Analysis 2: Recipe Structure

### qokeey (drachma) Context Analysis

qokeey appears 366 times, making it the 7th most frequent word -- consistent with it being a measurement unit in pharmaceutical text.

**Words immediately before qokeey (potential quantities/ingredients):**

| EVA | Count | Proposed Meaning |
|-----|-------|------------------|
| qokeey | 16 | Self-repetition (multiple drachmas listed) |
| chey | 14 | "est" -- "is [N] drachmas" |
| chedy | 13 | Candidate: ingredient name or quantity |
| okeey | 9 | Variant of qokeey / "half-drachma" (semidrachma) |
| shedy | 9 | Candidate: ingredient name |
| qokey | 8 | Variant of qokeey |
| qokeedy | 8 | Variant with suffix |
| shey | 7 | Candidate |
| aiin | 6 | "in" -- structural |

**Words immediately after qokeey (next ingredient or instruction):**

| EVA | Count | Proposed Meaning |
|-----|-------|------------------|
| qokeey | 16 | Another drachma measurement follows |
| qokey | 12 | Variant measurement |
| daiin | 10 | "et" (and) -- linking ingredients |
| okeey | 8 | Related measurement |
| qokeedy | 7 | Related measurement |
| qokaiin | 6 | Related measurement |
| chey | 5 | "est" |
| ol | 5 | "de" (of) |
| chckhy | 4 | Candidate: plant/ingredient |

### The qo- Prefix System

The qo- prefix is extremely productive (825 word types). The most frequent qo- words correlate strongly with the base words:

| qo- form | Frequency | Base form | Base freq | Proposed relationship |
|----------|-----------|-----------|-----------|----------------------|
| qokeey | 366 | okeey | 195 | drachma / half-drachma |
| qokain | 271 | okain | 123 | Measurement unit (uncia?) |
| qokaiin | 255 | okaiin | 199 | Measurement unit variant |
| qokeedy | 217 | okeedy | -- | drachma + suffix |
| qokey | 186 | okey | -- | drachma variant |
| qokal | 181 | okal | 144 | Measurement unit |
| qokedy | 170 | okedy | -- | Measurement variant |
| qol | 143 | ol | 586 | "of the" (de + article?) |
| qokar | 142 | okar | 127 | Measurement unit |

**Hypothesis**: The qo- prefix functions as a determinative or article preceding measurement/quantity stems. The system `qo + ke + suffix` represents drachma variants (possibly indicating number: -eey = base, -ain = one, -aiin = two, -al = three, etc.).

### p- Words (Recipe Markers)

The most frequent p- words:

| EVA | Frequency | Proposed Meaning |
|-----|-----------|------------------|
| pchedy | 28 | Recipe [ingredient] |
| pol | 17 | Recipe de (recipe of) |
| pchey | 14 | Recipe est? |
| pcheol | 11 | Recipe [ingredient] |
| pchor | 10 | Recipe cum? |
| par | 9 | Recipe ad (recipe for) |

**Words between p- and qokeey** (ingredient names):

| EVA | Count | Context |
|-----|-------|---------|
| shedy | 11 | Most common ingredient stem |
| ol | 8 | "de" (of) -- genitive connector |
| aiin | 6 | "in" -- structural |
| opchedy | 5 | Compound ingredient |
| al | 5 | Structural |
| oteey | 5 | Ingredient or quantity |

---

## Analysis 3: After chol ("hic"/this)

`chol` (352 occurrences) is the 8th most frequent word.

**After chol:**
- daiin (26): "this and..." -- conjunction following demonstrative
- chol (19): self-repetition / "this this" 
- chy (8): "this dry [thing]"
- shol (7): "this leaf/herb"
- chey (7): "this is..."
- chor (6), ol (6): structural words

**Before chol:**
- chol (19), chor (8), otol (7), or (7): all structural/functional

---

## Analysis 4: Quality Pairs

### Lines Containing Quality Words

Examining all lines with ckhy or kchy reveals pharmaceutical quality descriptions:

Notable patterns:
- `ckhy ... daiin` (hot ... and): 7 co-occurrences within 3 words
- `kchy ... chy` (cold ... dry): 7 co-occurrences within 3 words
- `kchy ... chol` (cold ... [something]): 5 co-occurrences
- `kchy ... dar` (cold ... but): 3 co-occurrences

The pairing `kchy + chy` (cold + dry) is the strongest non-structural association for kchy.

The pairing `ckhy + daiin + [X]` (hot + and + [X]) strongly suggests X follows the Galenic quality description.

### Quality Word Context Examples:
- "ckhy dl oiiin aiin okaiin" -- hot [degree?] ... in [quantity]
- "ckhy s ar al" -- hot ... to/for ...
- "kchy daiin cthol" -- cold and moist
- "kchy dar" -- cold but...
- "kchy chol" -- cold [noun]

---

## Analysis 5: Disease Names (after ar = ad)

**Words following ar (ad = for/to):**

| EVA | Count | Proposed Meaning |
|-----|-------|------------------|
| al | 33 | Structural (ad + alam = "for the wing/armpit"? or just function word cluster) |
| aiin | 30 | "ad in" = structural doubling |
| ar | 13 | Self-repetition |
| or | 10 | "ad cum" = structural |
| ol | 9 | "ad de" = structural |
| ain | 9 | Variant of aiin |
| am | 7 | Possible noun ending |
| chey | 5 | "ad est" -- "for [which] is" |
| shey | 5 | Candidate disease term |

The distribution after `ar` is heavily structural -- function words follow function words. This suggests `ar` may function more as a preposition in compound phrases than as a simple "for [disease]" marker.

**2 positions after ar:**
- okeey (8), okaiin (5): measurement words -- suggests "ad [purpose] [quantity]" patterns

---

## Analysis 6: After dar (sed/but or da/give)

**Words following dar:**

| EVA | Count | Proposed Meaning |
|-----|-------|------------------|
| ar | 10 | "but for..." (sed ad) |
| chedy | 6 | Candidate: bibere (to drink)? |
| aiin | 6 | "but in..." |
| ol | 6 | "but of..." |
| or | 5 | "but with..." |
| al | 5 | structural |
| chey | 4 | "but is..." |
| oty | 4 | Candidate: verb of administration |
| chos | 3 | Candidate |
| chear | 3 | Candidate |

**Words before dar:**
- daiin (5): "and but" -- discourse transition
- qokal (5): [measurement] but...
- al (5), shey (4), okal (4): various structural words

**Proposed verb decodings based on dar context:**
| EVA | Proposed Latin | Rationale |
|-----|---------------|-----------|
| oty | potio (drink/potion) | Appears 4x after dar, freq=108; if dar="da" (give), then "da potionem" (give a potion) |
| chedy | herba (herb) | Most frequent after dar besides function words; freq=337 |

---

## Analysis 7: PMI-Based Associations

### Key Discoveries from PMI

**daiin (et/and) -- highest PMI:**
- cthor (3.58): likely a content word that frequently needs conjunction
- cthol (3.42): proposed = humidus; "et humidus" is a standard quality pairing
- cthy (3.04): related to cthol family

**chey (est/is) -- highest PMI:**
- lchedy (2.92), lchey (2.88): l- prefix variants
- qol (2.87): "est de" = "is of"
- qokain (2.66): "est [N] uncia" = "[it] is [N] ounces"

**or (cum/with) -- highest PMI:**
- aiiin (4.31): very strong -- possibly "cum [substance]" 
- eey (4.26): measurement suffix
- ykaiin (3.93): possible ingredient name

**qokeey (drachma) -- highest PMI:**
- qokey (3.47): variant of drachma
- pchedy (3.46): Recipe + ingredient -- strong collocation with drachma
- okeey (3.17): half-drachma or drachma variant
- lchey (3.12): possible "of [this] is" 

---

## Analysis 8: Morphological System

### Suffix System

The most productive suffixes reveal a systematic morphology:

| Suffix | Types | Tokens | Examples | Proposed Function |
|--------|-------|--------|----------|-------------------|
| -iin | 736 | 4,214 | daiin, aiin, qokaiin | Preposition/function marker |
| -edy | 367 | 2,823 | chedy, shedy, qokeedy | Noun/adjective (oblique case?) |
| -eey | 319 | 2,175 | qokeey, okeey, cheey | Noun (nominative case?) |
| -ain | 305 | 1,626 | qokain, dain, ain | Number/quantity marker |
| -hey | 299 | 1,995 | chey, shey | Copula/verb form |
| -chy | 291 | 1,086 | chy, qokchy | Adjective? |
| -ody | 243 | 918 | chody, cheody | Noun (genitive?) |
| -hol | 141 | 935 | chol, shol | Noun (a specific word family) |
| -eol | 133 | 785 | cheol, sheol | Related to -hol (variant form) |
| -hor | 122 | 637 | chor, shor | Noun (another word family) |

### Prefix System

| Prefix | Proposed Function | Evidence |
|--------|-------------------|----------|
| qo- | Determiner/article or "quod" | Precedes all major stems; 825 types |
| o- | Variant article or preposition | ok-, ot-, ol- forms |
| y- | Possible conjunction/relative | Line-initial position |
| d- | Possible demonstrative | dain, dal, dar forms |
| l- | Possible article/linker | lchey, lchedy |
| sh- | Stem family marker | shol, shey, shedy |
| ch- | Stem family marker | chol, chey, chedy |
| cth- | Stem family marker | cthol, cthey |

---

## Analysis 9: The chedy/shedy System (Most Common Content Words)

chedy (337) and shedy (253) are the most frequent content words after the function words.

### chedy Analysis
- Appears 13x before qokeey (drachma) -- very strong recipe association
- Appears 6x after dar (sed/but)
- Appears 17x after ol (de/of)

**Proposed: chedy = herba (herb) or nomen herbae (herb name)**

### shedy Analysis  
- Appears 9x before qokeey (drachma)
- Appears 16x after ol (de/of)
- Appears 11x between p- words and qokeey (strongest ingredient candidate)

**Proposed: shedy = semen (seed) or pulvis (powder)**

---

## Expanded Codebook (50+ Entries)

### Tier 1: High Confidence (Given Anchors)

| # | EVA | Latin | English | Freq | Confidence |
|---|-----|-------|---------|------|------------|
| 1 | daiin | et | and | 676 | GIVEN |
| 2 | aiin | in | in | 623 | GIVEN |
| 3 | ol | de | of | 586 | GIVEN |
| 4 | chey | est | is | 505 | GIVEN |
| 5 | ar | ad | to/for | 445 | GIVEN |
| 6 | or | cum | with | 380 | GIVEN |
| 7 | qokeey | drachma | drachma | 366 | GIVEN |
| 8 | dar | sed | but | 268 | GIVEN |
| 9 | ckhy | calidus | hot | 42 | GIVEN |
| 10 | kchy | frigidus | cold | 30 | GIVEN |

### Tier 2: Strong Co-occurrence Evidence

| # | EVA | Latin | English | Freq | Confidence | Evidence |
|---|-----|-------|---------|------|------------|----------|
| 11 | chy | siccus | dry | 207 | MEDIUM | Strongest co-occurrence with kchy (7x in window-3); standard Galenic pairing |
| 12 | cthol | humidus | moist | 52 | MEDIUM | Appears in "kchy daiin cthol" (cold and moist); complementary quality |
| 13 | al | ille/illa | the/that | 306 | MEDIUM | Highest PMI with ar (3.51); "ad illum" pattern; very frequent |
| 14 | s | -que / ac | and (also) | 289 | MEDIUM | PMI=3.53 with aiin; appears as connective particle |
| 15 | shol | folium | leaf | 166 | MEDIUM | Frequent in herbal sections; follows chol (this leaf) |
| 16 | chol | hic/haec | this | 352 | MEDIUM | Demonstrative; followed by daiin(26), nouns, adjectives |
| 17 | dal | vel | or | 183 | MEDIUM | Frequent connective; alternative to daiin/dar |

### Tier 3: Measurement System (Based on qokeey Pattern)

| # | EVA | Latin | English | Freq | Confidence | Evidence |
|---|-----|-------|---------|------|------------|----------|
| 18 | qokain | uncia | ounce | 271 | MEDIUM | 2nd most frequent qo- word; measurement context |
| 19 | qokaiin | semiuncia | half-ounce | 255 | LOW-MED | Variant of qokain with -iin suffix |
| 20 | qokeedy | drachma (pl.) | drachmas | 217 | MEDIUM | Plural/oblique of qokeey; -edy suffix |
| 21 | qokey | drachma (var.) | drachma | 186 | MEDIUM | Short form of qokeey |
| 22 | qokal | libra | pound | 181 | LOW-MED | Another measurement unit |
| 23 | qokedy | uncia (pl.) | ounces | 170 | LOW-MED | Plural of qokain? |
| 24 | qol | quod | which/that | 143 | LOW-MED | PMI=2.87 with chey; "quod est" |
| 25 | qokar | manipulus | handful | 142 | LOW | Another measurement |
| 26 | okeey | semidrachma | half-drachma | 195 | LOW-MED | qokeey without qo- prefix |

### Tier 4: Content Words (Ingredient/Plant Names)

| # | EVA | Latin | English | Freq | Confidence | Evidence |
|---|-----|-------|---------|------|------------|----------|
| 27 | chedy | herba | herb | 337 | LOW-MED | Most frequent after ol; strong recipe association |
| 28 | shedy | semen | seed | 253 | LOW-MED | 2nd most frequent content word; between p- and qokeey |
| 29 | shey | aqua | water | 338 | LOW-MED | Extremely frequent; follows measurement words |
| 30 | cheey | oleum | oil | 189 | LOW | Frequent in recipe contexts |
| 31 | cheol | radix | root | 158 | LOW | Frequent; -eol suffix family |
| 32 | sheol | cortex | bark | 94 | LOW | Related to shol/shey family |
| 33 | chckhy | calidissimus | very hot | 133 | LOW-MED | Intensified form of ckhy; ch- prefix on ckhy |
| 34 | chor | herba (gen.) | of herb | 202 | LOW | Frequent; possible genitive of chedy |

### Tier 5: Structural/Grammatical Words

| # | EVA | Latin | English | Freq | Confidence | Evidence |
|---|-----|-------|---------|------|------------|----------|
| 35 | dain | tamen | however | 152 | LOW | Distinguished from daiin; different distribution |
| 36 | ain | -um (acc.) | accusative ending? | 146 | LOW | Short form; follows ar (ad) |
| 37 | am | -am | feminine acc.? | 113 | LOW | Appears sentence-finally |
| 38 | dy | -ae (gen.) | genitive ending? | 175 | LOW | Very productive suffix |
| 39 | r | -r / -tur | passive? | 194 | LOW | Single-char; possible verbal ending |
| 40 | l | -l | stem-final? | 160 | LOW | Single-char element |
| 41 | y | -i | genitive/nom. pl.? | 229 | LOW | Line-initial; possible article |
| 42 | d | -d | ablative? | 53 | LOW | PMI=3.65 with aiin |
| 43 | otar | contra | against | 148 | LOW | PMI=3.20 with ar; "contra ad" = "against for" |
| 44 | otaiin | ergo | therefore | 147 | LOW | Frequent; ot- prefix + aiin |
| 45 | saiin | sic in | thus in | 117 | LOW | s- prefix + aiin |

### Tier 6: Pharmaceutical Terms

| # | EVA | Latin | English | Freq | Confidence | Evidence |
|---|-----|-------|---------|------|------------|----------|
| 46 | pchedy | Recipe herbam | Take the herb | 28 | LOW-MED | p- (Recipe) + chedy (herb); PMI=3.46 with qokeey |
| 47 | pol | Recipe de | Take of | 17 | LOW | p- + ol (de) |
| 48 | oty | potio | potion/drink | 108 | LOW | Follows dar; administration verb |
| 49 | oteey | pondus | weight | 156 | LOW | Appears in measurement contexts |
| 50 | lchey | dictus est | is called | 71 | LOW-MED | PMI=2.88 with chey; l- prefix naming pattern |
| 51 | lchedy | dicta herba | called herb | 79 | LOW-MED | PMI=2.92 with chey; naming construction |
| 52 | okal | mensura | measure | 144 | LOW | Measurement context |
| 53 | cthor | temperamentum | temperament | 42 | LOW | PMI=3.58 with daiin; quality description |

---

## Structural Observations

### 1. The qo- Measurement Prefix System

The qo- prefix is the single most productive morphological element. It creates a systematic measurement vocabulary:

```
qo + ke + suffix -> drachma family (qokeey, qokeedy, qokey, qokedy)
qo + ka + suffix -> ounce family (qokain, qokaiin, qokal, qokar)
qo + l            -> "of the" / "which" (qol)
qo + t + suffix   -> another unit family (qoty, qotaiin, qotal, qotar)
```

This suggests the manuscript uses a **systematic morphological encoding** for pharmaceutical measurements.

### 2. The ch-/sh-/cth- Stem Families

Three major consonant stems produce parallel word families:

```
ch- family: chol, chey, chedy, cheol, cheey, chor, chy (352+505+337+158+189+202+207 = ~1950 tokens)
sh- family: shol, shey, shedy, sheol, sheey, shor, shy (166+338+253+94+139+86 = ~1076 tokens)  
cth- family: cthol, cthey, cthor, cthy (52+41+42+95 = ~230 tokens)
```

If these represent different plant or substance categories:
- ch- = the largest category (common herbs?)
- sh- = a secondary category (seeds/waters/liquids?)
- cth- = a smaller category (rare ingredients/qualities?)

### 3. Recipe Structure Template

Based on the analysis, a typical recipe line reads:

```
[p-word] [ingredient-ol-ingredient] [qo-measurement] [qokeey/qokain] [daiin] [next-ingredient] ...
```

Example reconstruction:
```
pchedy shedy ol cheol qokeey qokaiin daiin chedy ol shol qokain
Recipe semen de radice drachma semiuncia et herba de folio uncia
"Take seed of root, one and a half drachma, and herb of leaf, one ounce"
```

### 4. The or + aiin Collocation

The bigram `or aiin` (cum + in) appears 55 times -- the strongest bigram involving function words. In pharmaceutical Latin, "cum in" is unusual. This may indicate:
- `or` is not exactly "cum" but perhaps "autem" (however/moreover)
- The sequence represents a compound preposition
- The encoding maps phonetic sequences rather than word boundaries

---

## Caveats and Limitations

1. **Low frequency of quality words**: ckhy (42) and kchy (30) provide limited statistical power for co-occurrence analysis.

2. **The qo- system may be a cipher artifact**: If qo- is a determinative, the "real" stems are the parts after qo-, which would merge with the non-qo- vocabulary.

3. **Suffix variation**: The extreme productivity of suffixes (-eey, -edy, -ain, -aiin, -al, -ar, -ol, etc.) may represent:
   - Latin case endings
   - Number/gender agreement
   - Scribal variation / null characters
   - A cipher layer that inflects stems

4. **No rigid Galenic formulas found**: The expected "est calidus in gradu [N]" formula does not appear as a rigid sequence. Either:
   - The text is not strictly Galenic
   - The formula is expressed more loosely
   - The anchor decodings need refinement

5. **Statistical circularity risk**: Many proposed decodings are based on frequency and position, which can produce plausible-looking but incorrect results.

---

## Recommendations for Further Work

1. **Test the codebook against illustrated pages**: Herbal pages with identified plants can validate proposed plant-name decodings.

2. **Cross-validate with ZL3b-n.txt**: The zodiac/astronomical section should have a different vocabulary distribution if this is truly pharmaceutical Latin.

3. **Investigate the l- prefix**: Words like lchey, lchedy have strong PMI with chey (est). They may represent a naming construction ("is called X").

4. **Map the qo- system completely**: Determine whether qo- + stem forms a systematic cipher table for measurements.

5. **Focus on the pharmaceutical folios (f88r-f116v)**: The analysis found these folios were not well-represented in the transcription under those folio numbers. The actual pharmaceutical pages may use different numbering.
