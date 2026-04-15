# Voynich Recipe Ingredient Frequencies vs. Antidotarium Nicolai Core Ingredients

## Date: 2026-04-10
## Source: EVA transcription RF1b-e.txt, recipe section f88r-f116v

---

## 1. Recipe Section Statistics

| Metric | Value |
|---|---|
| Total words in recipe section (f88r-f116v) | ~14,210 |
| Unique words | ~4,268 |
| Recipe blocks (by @Lc title markers) | 37 |
| @Lf ingredient label lines | 193 |
| @P0 paragraph text lines | 73 |
| Average @Lf labels per recipe | 5.2 (range: 0-49) |

---

## 2. The @Lf System: Marginal Ingredient Labels

The recipe section uses a distinctive structural feature: **@Lf labels** in the margins alongside paragraph text. This is structurally parallel to how AN manuscripts list ingredients in the margins or as rubrics alongside the recipe text.

### @Lf Labels Ranked by Frequency

| Rank | @Lf Word | Count | In Herbal? | Significance |
|---|---|---|---|---|
| 1 | otaly | 4 | No | Most common label; recipe-only |
| 2 | otory | 3 | No | Recipe-only |
| 3 | otoky | 2 | No | Recipe-only |
| 4 | okol | 2 | Yes | Also in herbal section |
| 5 | otoldy | 2 | Yes | Also in herbal section |
| 6 | okary | 2 | Yes | Also in herbal section |
| 7 | oky | 2 | Yes | Also in herbal section |
| 8 | okeody | 2 | Yes | Also in herbal section |

**Critical observation**: The @Lf labels are almost entirely **unique** (182 unique words out of 193 total). This means each ingredient label appears in only 1-4 recipes across the entire section. This is consistent with an AN-type formulary: most ingredients are named specifically and appear in a modest number of recipes.

However, the @Lf labels do NOT directly correspond to the high-frequency words in the paragraph text. The paragraph text uses a different vocabulary, suggesting the @Lf labels are ingredient NAMES while the paragraph text contains procedural language, quantities, and possibly abbreviated or coded references.

---

## 3. Paragraph-Level Ingredient Identification

### Strategy: Words Before qo- Quantity Markers

In the recipe paragraph text, `qo-` prefixed words function as quantity/measure markers (appearing 1,500+ times). Words immediately before `qo-` words are strong candidates for ingredient names being measured.

### Top 30 "Ingredient Position" Words (non-qo words before qo-words)

| Rank | Voynich Word | Count before qo- | In Herbal? | In @Lf? |
|---|---|---|---|---|
| 1 | chey | 63 | Yes | -- |
| 2 | shey | 56 | Yes | -- |
| 3 | chedy | 49 | Yes | -- |
| 4 | shedy | 37 | Yes | -- |
| 5 | okeey | 31 | Yes | -- |
| 6 | cheey | 29 | Yes | -- |
| 7 | sheey | 25 | Yes | -- |
| 8 | oteey | 22 | Yes | -- |
| 9 | cheody | 17 | Yes | Yes |
| 10 | sheol | 17 | Yes | -- |
| 11 | otedy | 16 | Yes | -- |
| 12 | oteedy | 16 | Yes | -- |
| 13 | chdy | 14 | Yes | -- |
| 14 | okeedy | 14 | Yes | -- |
| 15 | daiin | 13 | Yes | -- |
| 16 | aiin | 13 | Yes | -- |
| 17 | chol | 12 | Yes | -- |
| 18 | lchedy | 12 | Yes | -- |
| 19 | chody | 11 | Yes | -- |
| 20 | sheody | 11 | Yes | -- |

**Critical finding**: ALL of the top 20 ingredient-position words also appear in the herbal section. None are recipe-only. This is the opposite of what we would expect if these were imported spice names (pepper, ginger, cinnamon should be recipe-only, not in the herbal section describing fresh plants).

### Interpretation

These high-frequency "ingredient" words are almost certainly **NOT ingredient names**. They appear too uniformly across the manuscript and have too-regular morphological patterns (-ey, -edy, -eey suffixes). They are more likely:

1. **Function words** (prepositions, conjunctions, articles)
2. **Procedural terms** (take, mix, grind, add)
3. **Quantity/measurement modifiers** (drachm, ounce, handful)
4. **Morphological variants of a small number of stems**

The che-/she-/oke-/ote- stems with -y/-dy/-ey/-eey suffixes form a systematic paradigm, not a list of distinct ingredients.

---

## 4. Recipe-Only Words: Imported Spice Candidates

Words appearing in recipes but NOT in the herbal section are the strongest candidates for imported spices (which have no plant page in a local herbal).

### Top Recipe-Only Words

| Rank | Word | Recipe Count | Notes |
|---|---|---|---|
| 1 | lkaiin | 39 | lka- family, 104 total members |
| 2 | lkain | 24 | Same lka- family |
| 3 | olkeey | 21 | olk- family |
| 4 | lkar | 21 | Same lka- family |
| 5 | otair | 18 | ota- family variant |
| 6 | rain | 16 | rai- family variant |
| 7 | lky | 16 | lk- stem |
| 8 | cheeo | 15 | che- variant |
| 9 | chedar | 14 | Unique compound |
| 10 | chedain | 13 | Unique compound |
| 11 | lshedy | 12 | lsh- family |
| 12 | lshey | 12 | lsh- family |
| 13 | otchedy | 12 | otch- family |
| 14 | okchedy | 12 | okch- family |
| 15 | rar | 11 | Short word |

### The lka- Family as Spice Candidate

The `lka-` stem is particularly interesting:
- **lkaiin** (39), **lkain** (24), **lkar** (21), **lkam** (6), **lkal** (4) = 104 total
- **Entirely absent from herbal section**
- Appears across multiple recipes
- Has the same suffix paradigm (-aiin, -ain, -ar, -am, -al) as other content words

If this is a single ingredient in various grammatical forms, its total frequency of ~104 across the recipe section would make it one of the most commonly referenced substances. In the AN, that frequency level corresponds to **Piper nigrum** (black pepper, ~60 recipes) or **Piper longum/Zingiber** (~45 recipes each).

Similarly, the `lke-` family (lkeey 41, lkeedy 25, lkey 13 = ~170 total) and `lch-` family (lchedy 38, lchey 26 = ~157 total) are largely recipe-concentrated.

---

## 5. Frequency-Rank Matching: Voynich vs. AN

### Methodology

We compare two ranking systems:
- **AN ranking**: Ingredients by number of recipes they appear in
- **Voynich ranking**: Word families by total recipe frequency, filtering for recipe-heavy or recipe-only distribution

### Non-qo Content Word Families in Recipes (by total frequency)

| Rank | Word Family | Recipe Total | Herbal Total | Ratio R:H | AN Candidate |
|---|---|---|---|---|---|
| 1 | che- (chey, chedy, cheey, cheol...) | 1,320 | ~500 | 2.6:1 | Function word family |
| 2 | she- (shey, shedy, sheey, sheol...) | 653 | ~200 | 3.3:1 | Function word family |
| 3 | cho- (chol, chor, chody...) | 526 | ~500 | 1:1 | Function word family |
| 4 | oke- (okeey, okeol, okey...) | 457 | ~100 | 4.6:1 | Possible content |
| 5 | ote- (oteey, oteedy, otedy...) | 382 | ~30 | 12.7:1 | **Strong recipe concentration** |
| 6 | ota- (otaiin, otar, otal...) | 363 | ~80 | 4.5:1 | Possible content |
| 7 | aii- (aiin, aiiin...) | 339 | ~150 | 2.3:1 | Function word |
| 8 | oka- (okaiin, okain, okar...) | 331 | ~100 | 3.3:1 | Possible content |
| 9 | dai- (daiin, dain, dair...) | 314 | ~400 | 0.8:1 | Function word |
| 10 | lke- (lkeey, lkeedy, lkey...) | 170 | ~50 | 3.4:1 | Possible content |
| 11 | lch- (lchedy, lchey...) | 157 | ~20 | 7.9:1 | **Strong recipe concentration** |
| 12 | chc- (chckhy, chcthy...) | 141 | ~30 | 4.7:1 | Possible content |
| 13 | olk- (olkeey, olkaiin...) | 130 | ~20 | 6.5:1 | **Strong recipe concentration** |
| 14 | pch- (pchedy, pcheol...) | 121 | ~20 | 6:1 | **Strong recipe concentration** |
| 15 | lka- (lkaiin, lkain, lkar...) | 104 | 0 | INF | **Recipe-exclusive** |
| 16 | opc- (opchedy, opchey...) | 98 | ~10 | 9.8:1 | **Strong recipe concentration** |
| 17 | alk- (alkain, alkaiin...) | 34 | 0 | INF | **Recipe-exclusive** |
| 18 | lkc- (lkchey, lkchedy...) | 32 | 0 | INF | **Recipe-exclusive** |
| 19 | lsh- (lshedy, lshey...) | 42 | ~5 | 8.4:1 | **Strong recipe concentration** |
| 20 | tsh- (tshey, tshor...) | 31 | ~5 | 6.2:1 | **Strong recipe concentration** |

---

## 6. Hypothetical Frequency-Rank Mapping

Based on the principle that the most common Voynich recipe ingredient should map to the most common AN ingredient, and filtering for recipe-concentrated word families:

| Voynich Family | Recipe Freq | Recipe-Only? | Hypothetical AN Match | AN Freq (~recipes) |
|---|---|---|---|---|
| lka- | 104 | YES | Piper nigrum (black pepper) | ~60 |
| ote- | 382 | Mostly | Piper longum (long pepper) | ~45 |
| oka- | 331 | Partial | Zingiber (ginger) | ~45 |
| oke- | 457 | Partial | Cinnamomum (cinnamon) | ~40 |
| lke- | 170 | Partial | Crocus (saffron) | ~35 |
| ota- | 363 | Partial | Mel (honey) | ~30 |
| lch- | 157 | Mostly | Rosa (rose) | ~28 |
| olk- | 130 | Mostly | Galanga | ~25 |
| pch- | 121 | Mostly | Nux muscata (nutmeg) | ~22 |
| chc- | 141 | Partial | Caryophyllus (cloves) | ~20 |
| opc- | 98 | Mostly | Cardamomum | ~18 |
| tsh- | 31 | Mostly | Mastix | ~16 |
| alk- | 34 | YES | Opium | ~15 |
| lkc- | 32 | YES | Myrrha (myrrh) | ~14 |
| lsh- | 42 | Mostly | Aloe | ~13 |

**IMPORTANT CAVEAT**: This mapping is purely hypothetical and based solely on frequency ranking. It assumes (1) that word families represent single ingredients, (2) that the manuscript covers approximately the same pharmacopoeia as the AN, and (3) that ingredient frequency distributions are preserved. None of these assumptions can be verified.

---

## 7. Cross-Validation Tests

### 7.1 Honey Test

**Prediction**: The honey-word should:
- Appear frequently in recipes but NEVER in herbal section
- Not be preceded by preparation terms
- Often appear near the END of ingredient lists (as vehicle/binder)

**Candidate: ota- family** (otaiin 81, otar 63, otal 57, otain 56)
- Total recipe frequency: 363
- Herbal frequency: ~80 (FAILS the "never in herbal" test)
- End-of-line analysis: `am` (30), `al` (22), `otam` (12) are common line-enders

**Candidate: lka- family** (lkaiin 39, lkain 24, lkar 21)
- Total: 104
- Herbal frequency: 0 (PASSES)
- But too frequent to be honey alone; more consistent with a primary spice

**Result**: No clear honey candidate emerges. The word `am` appears 39 times in recipes and is notably common at line-ends (30 of 39 occurrences). However, `am` is only 2 characters and appears throughout the manuscript. The words `sam` (recipe: ~20, also in herbal) and `dam` (recipe: ~14, also in herbal) with their -am endings are also candidates for vehicles/binders but cannot be confirmed.

**Alternative interpretation**: If the Voynich recipe section covers a different text than the AN (e.g., a shorter formulary or a text that uses sugar/syrup instead of honey), the honey test may not apply.

### 7.2 Opium Test

**Prediction**: The opium-word should:
- Appear in ~15 recipes, typically at low dose
- Have smaller quantity markers
- Appear in specific recipe types (soporifics/analgesics)

**Candidate: alk- family** (alkain 6, alkaiin 4, alky 3, alkam 3, alkeedy 3, alkar 3)
- Total: ~34
- Entirely recipe-only (PASSES)
- Appears across a modest number of recipes
- The alk- prefix is distinctive

**Candidate: tsh- family** (tshey 4, tshor 2, tshod 2, tshedy 2)
- Total: ~31
- Mostly recipe-only (PASSES)
- Low individual word frequencies suggest careful/limited use

**Analysis of rare qo-words (potential small-dose markers)**:
The words that precede the RAREST qo-words (those appearing only 1-5 times) are: shey (16), chey (10), shedy (9), chedy (8) -- these are the same high-frequency function words, suggesting that rare quantities can apply to any ingredient, not just dangerous ones.

**Result**: The alk- and tsh- families are plausible opium candidates based on recipe-only distribution and moderate frequency, but there is no way to test the "small dose" prediction without knowing which qo-forms encode smaller quantities.

### 7.3 Spice vs. Herb Distinction

**Prediction**: Words appearing ONLY in recipes = imported spices; words in BOTH = herbs/garden plants.

| Category | Word Families | Count |
|---|---|---|
| Recipe-exclusive (spice candidates) | lka-, alk-, lkc- | 3 families |
| Strongly recipe-concentrated (>6:1 ratio) | ote-, lch-, olk-, pch-, opc-, lsh- | 6 families |
| Moderate recipe concentration (3-6:1) | oke-, oka-, lke-, chc- | 4 families |
| Balanced (function words/herbs) | che-, she-, cho-, aii-, dai- | 5 families |

This yields ~13 recipe-concentrated families that could represent the AN's ~13 imported spice ingredients (pepper black, pepper long, ginger, cinnamon, saffron, galanga, nutmeg, cloves, cardamom, camphor, cassia, scammonia, euphorbium), which is a plausible match.

---

## 8. Structural Parallels with AN

### 8.1 @Lc Titles = Recipe Names
- 37 @Lc titles found
- AN has ~115-150 recipes
- Discrepancy suggests either: (a) the Voynich covers a personal extract of ~37 favorite recipes, or (b) the @Lc markers indicate recipe GROUPS, not individual recipes, or (c) there are additional recipe boundaries not marked by @Lc

### 8.2 @Lf Labels = Ingredient Lists
- 193 @Lf labels, mostly unique
- AN recipes typically list 5-40 ingredients
- Average of 5.2 @Lf per recipe matches the lower end of AN ingredient counts
- This is consistent with simpler recipes or a formulary of common preparations

### 8.3 qo- Words = Quantity Markers
- ~20 distinct qo- forms appear frequently
- AN uses a limited quantity vocabulary: drachm (3 sizes), ounce, pound, "ana" (equal parts), "quantum sufficit"
- The ~20 qo- forms could encode: quantity + unit combinations (e.g., 1 drachm, 2 drachms, half ounce, etc.)

### 8.4 Recipe Paragraph Flow

Examining detailed recipe paragraphs reveals a pattern:
```
[word] qo-word [word] qo-word [word] ... [function words] ... [word] qo-word
```

This is consistent with the AN's ingredient-list format:
```
[ingredient] [quantity] [ingredient] [quantity] [ingredient] [quantity] ...
```

The `qo-` prefix consistently marks the element FOLLOWING an ingredient name, which matches quantity/dose notation.

---

## 9. Word Distribution Across Recipes

### Words Appearing in Most Recipes (non-qo, len >= 3)

| Word | In N Recipes | Total Count | Likely Role |
|---|---|---|---|
| aiin | 26 | 272 | Function word (in/of/the) |
| daiin | 22 | 189 | Function word |
| chol | 19 | 110 | Function word |
| chey | 15 | 205 | Function word or very common ingredient |
| okeol | 15 | 42 | Possibly procedural |
| cheol | 14 | 91 | Function word |
| chor | 14 | 45 | Function word |
| sheey | 14 | 64 | Function word |
| cheody | 13 | 50 | Content word |
| okol | 13 | 33 | Content word |
| dol | 13 | 28 | Content word |
| sheol | 13 | 47 | Content word |

Words appearing in 25+ of 37 recipes cannot be specific ingredients (no single AN ingredient appears in every recipe). These are structural/grammatical words.

Words appearing in 8-15 recipes are plausible high-frequency ingredients (pepper appears in ~60/150 = 40% of AN recipes; 40% of 37 = ~15 recipes).

---

## 10. Common Bigrams (Ingredient + Quantity Patterns)

| Bigram | Count | Interpretation |
|---|---|---|
| chey qokeey | 12 | [ingredient?] [quantity] |
| chedy qokeey | 10 | [ingredient?] [same quantity] |
| shey qokain | 6 | [ingredient?] [different quantity] |
| qokeey qokeey | 14 | [quantity] [quantity] -- repeated dose? |
| qokeey qokeedy | 8 | [quantity1] [quantity2] -- compound dose? |
| ar al | 13 | Function word pair |
| or aiin | 20 | Function word pair |
| ar aiin | 12 | Function word pair |

The pattern `qokeey qokeey` (14 occurrences) could represent the AN's `ana` (equal parts) notation, where the same quantity marker is repeated to indicate identical doses for multiple ingredients.

---

## 11. Key Findings and Limitations

### What the Data Shows

1. **Structural parallel confirmed**: The Voynich recipe section has a clear [ingredient] + [qo-quantity] repeating pattern that mirrors the AN's [ingredient] + [quantity] format.

2. **Recipe-exclusive word families exist**: The lka-, alk-, and lkc- families appear only in recipes, never in the herbal section. These are strong candidates for imported spice names.

3. **The lka- family is the strongest spice candidate**: With 104 occurrences, entirely recipe-exclusive, and regular morphological paradigm, this is the most likely candidate for a high-frequency AN ingredient like black pepper or ginger.

4. **~13 recipe-concentrated word families** could correspond to the AN's ~13 primary imported spice ingredients.

5. **Function words dominate**: The most frequent words (aiin, daiin, chol, chey, shey) appear across nearly all recipes and are clearly structural, not ingredient-specific.

6. **qo- words form a system of ~20 quantity markers**, consistent with the AN's limited set of measurement terms.

### What Cannot Be Determined

1. **Specific ingredient identity**: Without a bilingual key or confirmed decipherment of even one word, all mappings are hypothetical.

2. **Whether word families = single ingredients**: The che-/she-/oke- paradigm could represent different ingredients with shared morphology, or different forms of the same word.

3. **The text's actual source**: While structurally compatible with the AN, the Voynich recipes could represent any medieval pharmaceutical formulary.

4. **Honey identification**: No word cleanly passes all honey-test criteria (frequent, recipe-only, line-final, no preparation terms).

5. **Opium identification**: Moderate candidates exist (alk-, tsh-) but cannot be verified without dose-size information.

### Confidence Assessment

| Finding | Confidence |
|---|---|
| Recipe section contains ingredient lists with quantities | High (structural) |
| qo- prefix marks quantities/measures | High (positional) |
| lka- family = imported spice (absent from herbal) | Moderate |
| ~13 recipe-concentrated families = AN spice set | Speculative |
| Any specific ingredient identification | Very Low |
| Frequency-rank mapping to specific AN ingredients | Very Low |

---

## 12. Recommendations for Further Analysis

1. **Cross-reference with Circa Instans**: The ~270 simples in the Circa Instans could be compared with the ~182 unique @Lf labels. If the count matches better, the @Lf system may encode individual simples rather than compound recipe names.

2. **Co-occurrence analysis**: Which @Lf labels appear together? In the AN, certain ingredient combinations are stereotypical (the "three peppers" always appear together; spica nardi + crocus are frequent pairs). The Voynich co-occurrence data is sparse (most @Lf words are unique) but the `okary` label co-occurs with 8 other labels, suggesting it may be a common base ingredient.

3. **Folio-level analysis**: Different sections of f88r-f116v may correspond to different recipe categories (theriac-type, electuary, syrup, etc.). Vocabulary shifts between sections could reveal categorical boundaries.

4. **The `l-` prefix hypothesis**: Words beginning with `l` (lka-, lke-, lch-, lsh-, lkc-) are disproportionately recipe-concentrated. The `l-` prefix may be a morphological marker for a specific category (e.g., "the [ingredient]" as a definite article, or a preparation state like "powdered").
