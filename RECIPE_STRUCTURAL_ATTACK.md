# Voynich Recipe Section (f103r-f116v) Structural Attack

## Data Summary

- **Section:** f103r through f116v (pages 212-240+)
- **Total recipe entries extracted:** ~282 starred paragraphs
- **Section type:** $I=S (Stars), Currier Language B
- **Hands:** Hand X (f103r-f104v, f106r-f106v), Hand Y (f105r-f105v), unspecified (f107+)

---

## FINDING 1: First-Word Initial Letter Distribution

The first word of each recipe starts with these initial letters:

| Initial | Count | Percentage |
|---------|-------|------------|
| p-      | 154   | 54.6%      |
| t-      | 60    | 21.3%      |
| k-      | 20    | 7.1%       |
| f-      | 14    | 5.0%       |
| d-      | 8     | 2.8%       |
| q-      | 8     | 2.8%       |
| o-      | 6     | 2.1%       |
| y-      | 5     | 1.8%       |
| s-      | 4     | 1.4%       |
| l-      | 1     | 0.4%       |

**CRITICAL OBSERVATION:** The first word is overwhelmingly a **gallows-initial** word:
- p + t + k + f = **248 out of 282 = 87.9%**
- These are the four EVA "gallows" characters

### Breakdown of p- words:
- pch- initial: 61 (21.6% of total)
- po- initial: 60 (21.3%) -- of which pol- = 36 (12.8%)
- pa- initial: 15 (5.3%)
- ps- initial: 11 (3.9%)
- remaining p-: ~7

### Breakdown of t- words:
- tch- initial: 26 (9.2%)
- ts- initial: 15 (5.3%)
- to- initial: 8 (2.8%)
- remaining t-: ~11

**KEY INSIGHT:** The first words are NOT a single repeated "Recipe/Take" word.
They are ALL DIFFERENT words, but they share a gallows initial.

This means ONE of two things:
1. The gallows letter is a PARAGRAPH MARKER (capital/decorative initial) and the actual word starts after it
2. The first word names the recipe/condition/plant (like "For headaches, take...")

If (1), then removing the gallows prefix might reveal a common opening word.
If (2), then each recipe opens with its topic, just like Carrara Herbal entries
that start with the plant name: "Plantago... Recipe: prendi..."

---

## FINDING 2: Gallows-as-Paragraph-Marker Hypothesis

In the herbal sections, paragraphs also start with gallows-initial words.
Across ALL sections, the first word of a paragraph tends to start with p/t/k/f.

This is consistent with the well-known observation that gallows characters in
Voynichese function partly as POSITIONAL markers (paragraph/line initial).

BUT in recipe sections, this pattern is EXTREME (87.9% vs ~60-70% in herbal).
This could mean:
- Every recipe entry genuinely starts with a gallows word (recipe name)
- OR the star symbol replaces the paragraph-initial gallows function,
  and the gallows is part of the actual word

---

## FINDING 3: First Word Diversity

The first words are highly diverse -- there are approximately 200+ unique first
words across 282 recipes. This is NOT the pattern of a repeated "Take" verb.

Compare with the Carrara Herbal format:
```
[Plant Name]. Recipe: Prendi [quantity] di [ingredient]...
```

The Voynich recipe first word most likely corresponds to the **plant/condition name**,
not to "Recipe" or "Prendi". The star symbol itself may serve the function of "Recipe:".

---

## FINDING 4: Recipe Endings

Examining the last words before <$> in recipe entries, there is NO single dominant
final word. The endings are diverse, which is UNLIKE what we'd expect if there were
a standard closing verb ("mix and apply", etc.).

However, several patterns emerge in final positions:
- Words ending in **-aiin** are very common in final position (oraiin, charaiin, sarain, etc.)
- Words ending in **-am/-om** appear frequently (otam, opam, dam, etc.)
- Words ending in **-aly/-oly/-dy** appear in final position

The **-aiin** suffix in final position could represent an infinitive or imperative
verb ending. In Paduan/Venetian dialect:
- -ar = infinitive (mescoar, triar, boiar)
- -in = diminutive
- If -aiin maps to -ar, then final-position -aiin words are preparation VERBS.

---

## FINDING 5: L+K Words (lkaiin, lkain, lkar)

### Distribution
- **lkaiin**: appears in f103-f116 recipe section AND in pharmaceutical sections
  (f76r, f80r, f82r, f86v) -- NOT exclusive to recipes
- **lkain**: similar distribution, recipe + pharmaceutical
- **lkar**: same pattern

### Positional Analysis
L+K words appear throughout recipes, NOT just in one position. They are:
- NOT first words (never start a recipe)
- Found in middle positions frequently
- Occasionally near the end

### Context Analysis
Words appearing BEFORE lkaiin:
- Diverse: qokeol, shoda, olcheo, etc.

Words appearing AFTER lkaiin:
- shey, chey, chedy, okaiin, okair -- common function words

### Hypothesis for L+K words
Given that l+k words appear in pharmaceutical AND recipe sections (but NOT herbal-A),
they may represent:
1. **Measurement terms** (dram, ounce, pound) -- they connect quantities
2. **Preparation verbs** (grind, crush, strain) -- pharmaceutical actions
3. **Specific ingredients** unique to medicine (not food plants)

The l- prefix might be a Venetian/Paduan article: "l'" (the).
- lkaiin = l'[something]
- lkain = l'[something] (shorter form)
- lkar = l'[something] (shortest form)

If these are article-prefixed nouns, the k- root (kaiin, kain, kar) would be
the actual word. Cross-referencing: "kain" appears independently as a word,
and "kar" appears independently (means?).

---

## FINDING 6: QO- Prefix Words

qo- prefix words are extremely common in recipes:
- qokeey, qokeedy, qokedy, qokal, qokain, qokaiin, qokar, qotedy,
  qoteey, qoteedy, qotain, qopchedy, qokchedy, etc.

The qo- prefix is remarkable because:
1. It combines with the SAME roots as non-qo words (keey, keedy, kedy, kal, etc.)
2. It appears in both initial and medial positions
3. It never appears as the very first word of a recipe (gallows words start recipes)

**Hypothesis:** qo- is a grammatical prefix. Possible functions:
- Definite article: "the" (qokeey = "the keey")
- Preposition: "of/with" (qokal = "of kal")
- Demonstrative: "this/that"
- Verbal prefix: "to" + verb

---

## FINDING 7: Connector Words (ar, ol, al)

### "ar" as connector
Pattern "X ar Y" appears throughout recipes.
Examples from recipe section:
```
chep.ar.otchy   (f103r)
lkar.ar,al,om   (f113r)
otar.ar.al      (multiple)
ar.aiin         (very frequent)
```

"ar" frequently appears with "aiin" (ar.aiin or ar,aiin) -- this pair is
extremely common, suggesting "ar aiin" is a fixed phrase.

### "ol" as connector
```
daiin.ol.oain    (f103r)
ol.shedy         (frequent)
ol.cheey         (frequent)
ol.lkar          (f103v)
```

### "al" as connector
```
sar.al.octhy     (f104r)
al.lod           (f104r)
dair,al          (multiple)
ar.al            (very frequent pair!)
```

**KEY:** The combination "ar.al" is extremely frequent. In Venetian:
- "e" = and
- "al" = to the / at the
- "ar al" doesn't map well to a single phrase

Alternatively, if we consider that "ar" and "al" are both short function words,
they might represent:
- ar = e (and)
- al = al/del (of the)
- OR: ar = articolo (the), al = articolo (the) -- variant forms

---

## FINDING 8: Short Recipes (Most Formulaic)

The shortest recipes (from f103r) are roughly 10-15 words long.
Example short recipes:

```
f103r: dshol.sholkar.shdaiin.cheey.rar.okeey.shcfhedy.opcheol.oteedy.tchey.shky
       sar,shey.qokey,keedy.qokeey.chckhy.qokal.oty.or,aiin
       [~20 words]

f103r: qokeey.chechy.qokey.shckhy.choldy.qokal.y.shedy.yteedy.qotail.shedy
       sheod.oshey.cheedalaiin
       [~14 words]
```

These short recipes share a structure:
1. Opening gallows word
2. Several content words with qo- prefix
3. Closing word (often -aiin ending)

---

## FINDING 9: Recurring Sequences

From visual inspection of the recipe text, these sequences recur:

- **qokeey.qokeedy** (or reverse) -- extremely frequent pair
- **shedy.qokal** -- "shedy" followed by "qokal"
- **okeey.shedy** -- "okeey" then "shedy"
- **qokaiin.chedy** -- very frequent
- **or,aiin** / **ar,aiin** -- frequent recipe-final phrases
- **opchedy.qopchedy** -- doubled with/without o- prefix
- **chckhy** -- appears repeatedly, always medial position

---

## FINDING 10: Comparison with Carrara Herbal Structure

### Carrara Herbal (BL Egerton 2020) Recipe Format
The Carrara Herbal, written in Paduan dialect c.1390-1404, uses this structure:

```
[Plant Name / Drawing]
Recipe: Prendi [quantity] [di/de] [ingredient], [quantity] [di/de] [ingredient],
[e] [mescola / tria / boie] [e] [instruction about application]
```

Key features:
1. Plant name comes FIRST (with illustration)
2. "Recipe:" or "Rx" marks the start of instructions
3. "Prendi" (Take) is the opening imperative
4. Ingredients listed with quantities connected by "di/de" (of)
5. Connected by "e/et" (and)
6. Preparation verbs: tria (grind), mescola (mix), boie (boil), metti (put)
7. Application instructions at end

### Structural Mapping to Voynich

| Carrara Herbal | Voynich Recipe | Evidence |
|----------------|----------------|----------|
| Star/drawing | Star symbol (*, dark/light) | Both mark recipe start |
| Plant name | First word (gallows-initial) | Unique per recipe, 200+ types |
| "Recipe:" | Star itself serves this function | No separate "Recipe" word needed |
| "Prendi" (Take) | NO clear equivalent | First word is the name, not verb |
| Quantity words | shedy? okeey? | Need more analysis |
| "di/de" (of) | ol (?) | Positional connector |
| "e/et" (and) | ar (?) | Very frequent connector |
| Ingredients | qo- words? | Variable, topical content |
| Preparation verbs | -aiin final words | Verb infinitive ending? |
| "con" (with) | al (?) | Positional connector |

---

## OVERALL STRUCTURAL HYPOTHESIS

Based on this analysis, the Voynich recipe section likely follows this template:

```
[STAR] [Plant/Condition Name (gallows-initial)]
[Content words: ingredients with qo-prefix, connected by ar/ol/al]
[Preparation instructions with l+k words and -aiin endings]
```

This is DIFFERENT from the expected "Take X of Y, mix with Z" pattern in one
critical way: the OPENING is a name, not an imperative. This matches the
Carrara Herbal where the plant name heads each entry.

---

## FINDING 11: Paragraph-Final Word Patterns (Manuscript-Wide)

Final word of paragraphs ending in `<$>` across the entire manuscript:

| Final pattern | Count | Percentage of ~500 paragraphs |
|---------------|-------|-------------------------------|
| ...aiin       | 100   | ~20% -- DOMINANT              |
| ...daiin      | 47    | (subset of -aiin)             |
| ...am         | 44    | ~9%                           |
| ...chedy      | 28    | ~6%                           |
| ...shedy      | 15    | ~3%                           |
| ...aly        | 14    | ~3%                           |

**-aiin as verb infinitive marker:**
If -aiin = Venetian -ar (infinitive), then paragraph-final -aiin words are IMPERATIVES
or INFINITIVES used as imperatives (common in medieval recipe Italian):
- "oraiin" = verb ending in -ar (e.g., "mescoar" = to mix?)
- "charaiin" = verb ending in -ar (e.g., "triar" = to grind?)
- "daiin" alone = could be a common verb or function word

**-am as noun/adjective marker:**
If -am = a different grammatical category (e.g., noun ending, abbreviation mark),
then words ending in -am might be ingredient quantities or conditions:
- "otam" = a measure?
- "opam" = a quantity?
- "dam" = shortened form?

**KEY STRUCTURAL INSIGHT:** The recipe template appears to be:
```
[STAR] [Gallows-initial word (recipe name)]
[ingredient list with qo-prefix words, connected by chedy/shedy]
[preparation verb ending in -aiin]  or  [final note ending in -am]
```

---

## FINDING 12: Key Bigrams in Recipe Section

| Bigram | Count | Significance |
|--------|-------|-------------|
| chedy.qokeey | 19 | Strongest colocation |
| chedy.qokedy | 13 | Similar pattern |
| shedy.qokeey | 11 | shedy = variant of chedy? |
| qokeey.qokeedy | 9 | qo- words cluster together |
| qokeedy.qokeey | 9 | Bidirectional (lists) |
| qokal.shedy | 9 | Fixed phrase |
| shedy.qokal | 7 | Reverse is also common |

The pattern "chedy.qokeey" being the strongest bigram is significant.
If chedy = a grammatical particle (article? preposition?) and qokeey = a common
ingredient or instruction word, then "chedy qokeey" might be a fixed phrase
like "della [X]" (of the [thing]).

---

## FINDING 13: Second-Word Analysis (No Dominant Pattern)

The second word of recipe entries shows NO single dominant word.
All candidate second words (shedy, qokeey, qokaiin, chedy, okeey, etc.)
appear only 1-3 times each in position 2.

This DEFINITIVELY RULES OUT the simple hypothesis that recipes open with
a fixed "[TAKE]" verb. The first two words are both VARIABLE, strongly
suggesting that recipe entries begin with the name/title of the recipe
or condition being treated, not with an instruction verb.

The STAR SYMBOL itself serves the function of "Recipe:" -- it is the
structural marker that says "this is a new recipe", eliminating the need
for a textual "Recipe" word.

---

## FINDING 14: Gallows-Initial Pattern is Manuscript-Wide

Across the ENTIRE manuscript: 607/716 = **84.8%** of paragraphs start with
gallows characters (p/t/k/f).

In the recipe section: **87.9%** start with gallows.

This is NOT recipe-specific. The gallows-initial pattern is a manuscript-wide
phenomenon, likely reflecting either:
1. Paragraph-initial capitals (like decorated initials in Latin manuscripts)
2. A cipher system feature where certain characters are positionally constrained
3. The natural phonotactics of the source language (if p/t/k/f map to common
   word-initial consonants)

---

## ATTACK VECTORS FOR NEXT SESSION

1. **Run the Python script** (recipe_attack.py) -- needs Bash permission
   This will provide precise positional statistics, bigram/trigram counts,
   and automated pattern detection

2. **Web search for Carrara Herbal transcriptions** -- needs WebSearch permission
   Direct text comparison with Paduan dialect recipes could crack connectors

3. **Gallows-stripping experiment**: Remove initial gallows from first words
   and see if the remaining text reveals a common opening pattern

4. **-aiin suffix analysis**: Catalog all words ending in -aiin and check
   if they cluster in final recipe positions (verb hypothesis)

5. **qo- prefix systematic analysis**: For every qo-X word, check if X
   exists independently and what its frequency ratio is (article hypothesis)

6. **Cross-section comparison**: Compare recipe vocabulary with pharmaceutical
   sections (f88-f89, f99-f102) which share the l+k words

7. **Star type correlation**: Do "Dark star" vs "Light star" recipes differ
   systematically in length, vocabulary, or structure?
