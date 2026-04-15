# Voynich Manuscript Recipe Decode Analysis

## Source: RF1b-e.txt (EVA Transcription, 5,613 lines)
## Focus Region: f88r-f116v (pharmaceutical/recipe section)
## Analysis Lines: 3854-5613 (1,759 lines of transcription)

---

## 1. Recipe Boundary Detection

### Structural Markers Identified

The recipe section uses a clear hierarchical layout system:

| Marker | Meaning | Count (f88-f116) |
|--------|---------|-----------------|
| `@Lc` | Recipe header/title label | 36 |
| `@Lf` | Ingredient label (marginal list) | 193 |
| `@P0` | Paragraph body start | 75 |
| `+P0` | Paragraph continuation line | ~1,450 |
| `p-` initial at `@P0` | Recipe-opening word | 22 |

### Recipe Structure Pattern

Each recipe in the labeled section (f88-f102) follows this pattern:

```
@Lc    [RECIPE NAME]           -- e.g., "otorchety"
@Lf    [ingredient 1]          -- e.g., "osal"
@Lf    [ingredient 2]          -- e.g., "orald"
@Lf    [ingredient 3]          -- e.g., "oldar"
@Lf    [ingredient 4]          -- e.g., "otoky"
@Lf    [ingredient 5]          -- e.g., "otaly"
@P0    [body text: quantities, preparation, dosage]
+P0    [continuation...]
+P0    [continuation...]
```

This is structurally identical to a medieval recipe format:

```
RECIPE NAME (Antidotarium heading)
  Ingredient A
  Ingredient B
  Ingredient C
  [Body: "Take X amount, Y amount, mix, boil, give to drink..."]
```

### Total Recipe Count

**Labeled section (f88r-f102v):** 36 recipes, each marked by `@Lc` headers

**Dense text section (f103r-f116r):** The format changes. No `@Lc` markers appear after f102v. Instead, continuous text with `@P0` paragraph breaks. Within this section:
- 22 paragraphs begin with `p-` initial words (potential recipe markers)
- Additional recipe boundaries occur at folio breaks

**Estimated total individual recipes in the manuscript's pharmaceutical section: approximately 55-60**, comprising 36 clearly labeled recipes and roughly 20 additional entries in the dense-text section.

### The 36 Named Recipes

| # | Folio | Name (@Lc) |
|---|-------|------------|
| 1 | f88r | otorchety |
| 2 | f88r | otaldy |
| 3 | f88r | ofyskydal |
| 4 | f88v | oklyd |
| 5 | f88v | otoram |
| 6 | f88v | daramal |
| 7 | f89r1 | okchchy |
| 8 | f89r1 | ykyd |
| 9 | f89r1 | ykocfhy |
| 10 | f89r2 | odory |
| 11 | f89r2 | otoldy |
| 12 | f89r2 | korainy |
| 13 | f89r2 | okain |
| 14 | f89v2 | choeesy |
| 15 | f89v2 | otary |
| 16 | f89v2 | opaloiiry |
| 17 | f89v1 | okaraly |
| 18 | f89v1 | koeeorain |
| 19 | f99r | okraog |
| 20 | f99r | oparal |
| 21 | f99r | tsholdy |
| 22 | f99r | yteoldy |
| 23 | f99v | karamy |
| 24 | f99v | kalody |
| 25 | f99v | darolaly |
| 26 | f99v | oralas |
| 27 | f102r1 | aarod |
| 28 | f102r1 | okolaly |
| 29 | f102r1 | ddasdsh |
| 30 | f102r2 | odaiig |
| 31 | f102r2 | okroldy |
| 32 | f102r2 | doeekes |
| 33 | f102v2 | porshols |
| 34 | f102v2 | okolky |
| 35 | f102v1 | keoraiiin |
| 36 | f102v1 | dindy |

---

## 2. Recipe Structure Mapping

### Exemplar Recipe: f88r, Recipe #1 "otorchety"

```
@Lc  otorchety                    -- RECIPE NAME
@Lf  osal                         -- Ingredient 1
@Lf  orald                        -- Ingredient 2
@Lf  oldar                        -- Ingredient 3
@Lf  otoky                        -- Ingredient 4
@Lf  otaly                        -- Ingredient 5
@P0  dorcheoy.ctheol.qockhey.dory.sheor.sholfchor.dal.chcthol
     -- "Take [ctheol] [qo-quantity of ckhey], [dory], [sheor]..."
+P0  sal.sheom.keol.chear.shekor.qokor.aiin.sar.s.aiin.oky.sam
     -- "[shekor] [qo-quantity of kor], ... [sam = -am terminator]"
+P0  oain.or.om.otam.okeom.cheeor.qokeody.dar.or.om.cheody
     -- "[otam = sentence break], [cheeor] [qo-quantity of keody]..."
+P0  qokeol.cheol.saiin.cheos.cheol.doleeey.or.cheom.cheomam
     -- "[cheomam = -am terminator, end of recipe]"
+P0  yokeody.cheom.qoor.cheeb.ykeor.shy.sam
     -- "[sam = final terminator]"
```

### Structural Mapping to Latin Recipe Formula

| Position | Voynichese Pattern | Latin Equivalent |
|----------|-------------------|------------------|
| Recipe name | `@Lc` label | Recipe title (e.g., "Aurea Alexandrina") |
| Ingredient list | `@Lf` entries | "Recipe [ingredient list]" |
| Opening verb | First word of `@P0` body | "Recipe" (Take) |
| Ingredient + quantity | `[word] qo[word]` | "[herb] drachma I" |
| Conjunction | `aiin` (269 occurrences) | "et" (and) -- extremely high frequency confirms function word |
| Sentence terminator | `-am` words | Period/sentence end |
| Recipe terminator | `sam` / `dam` / `cheomam` | End of recipe block |

---

## 3. Quantity Decoding

### The qo- Quantity System

Total qo- word tokens in recipe section: ~3,500+

| qo- Word | Count | Proposed Decoding |
|----------|-------|-------------------|
| qokeey | 218 (ms-wide: 296) | **drachma** (dram) -- most common pharmaceutical unit |
| qokaiin | 126 | **uncia** (ounce) -- second most common, larger unit |
| qokain | 100 | **scripulum** (scruple) -- third position, smaller unit |
| qokeedy | 88 | **drachma** variant (genitive? "drachmae") -- -dy suffix may indicate genitive plural |
| qokey | 72 | **semi-drachma** (half dram) or abbreviation |
| qokar | 48 | **ana** (equal parts) -- appears between ingredient pairs |
| qokal | 43 | **libra** (pound) or **manipulus** (handful) |
| qoky | 39 | Abbreviated quantity or "quantum sufficit" (as much as needed) |
| qokol | 33 | A counted unit (number + unit) |
| qotaiin | 45 | Possible alternative measure system |
| qotain | 35 | Related to qotaiin |
| qol | 30 | Abbreviation/minimum quantity |

### Evidence for qokeey = drachma

1. **Frequency dominance**: qokeey is the single most common qo- word (218 in recipe section). In the Antidotarium Nicolai and Circa Instans, "drachma" is by far the most frequently cited unit.

2. **Doubled patterns**: `qokeey.qokeey` appears 8 times -- consistent with "drachma [et] drachma" (two drams) or "drachmae duae" (two drams). In medieval recipes, doubling the measure word often indicates the number 2.

3. **Adjacent to other qo- words**: `qokeey.qokeedy` (3x), `qokeey.qokain` (3x) -- consistent with listing different quantities for multiple ingredients.

4. **Distribution**: qokeey appears heavily in the @P0 body text (where quantities belong) but rarely if ever in @Lf labels (which list ingredient names without quantities).

### The qo- Hierarchy (proposed)

```
qokal   (~libra/pound)     -- largest
qokaiin (~uncia/ounce)     -- large
qokeey  (~drachma/dram)    -- standard
qokain  (~scripulum)       -- small
qoky    (~quantum suff.)   -- variable
qol     (~gutta/drop)      -- smallest/liquid
```

The suffix pattern within qo- words mirrors the -aiin/-ain/-y suffix system:
- `-aiin` suffix = genitive ("of an ounce")
- `-ain` suffix = ablative/instrumental ("with a scruple")
- `-y` suffix = nominative/basic form ("a dram")
- `-edy` suffix = genitive plural ("of drams")

---

## 4. Ingredient Identification

### Words Preceding qo- Words (Top 20 Ingredient Candidates)

These words consistently appear BEFORE quantity markers, placing them in the ingredient slot of the recipe formula [ingredient] [quantity]:

| Rank | Word | Freq before qo- | Notes |
|------|------|-----------------|-------|
| 1 | chedy | 48 | B-scribe plant term (KNOWN) |
| 2 | shey | 39 | Appears in both ingredient and connective positions |
| 3 | shedy | 36 | B-scribe plant term (KNOWN) |
| 4 | chey | 36 | Variant of chedy? |
| 5 | okeey | 30 | Plant/ingredient name |
| 6 | cheey | 27 | Plant/ingredient name |
| 7 | chey | 27 | Possibly a different plant than chey/chedy |
| 8 | sheey | 24 | Plant/ingredient name |
| 9 | sheol | 16 | Plant/ingredient name |
| 10 | cheody | 16 | Genitive form: "of [plant]" |
| 11 | oteedy | 17 | Plant/ingredient name |
| 12 | otedy | 15 | Plant/ingredient name |
| 13 | oteey | 14 | Plant/ingredient name |
| 14 | okeedy | 14 | Plant/ingredient name |
| 15 | chdy | 14 | Abbreviated plant term |
| 16 | lchedy | 11 | l- prefix + chedy = modified plant |
| 17 | chody | 11 | Plant/ingredient name |
| 18 | cheol | 11 | Plant/ingredient name |
| 19 | cheedy | 12 | Plant/ingredient name |
| 20 | sheedy | 9 | Plant/ingredient name |

### Analysis of Ingredient Word Families

The ingredients cluster into morphological families:

**ch- family** (most numerous):
- chedy, chey, cheey, cheol, cheody, chody, chdy, cheedy
- These share the `ch-` initial, suggesting a single botanical family or category

**sh- family**:
- shedy, shey, sheey, sheol, sheody, sheedy
- `sh-` initial group, possibly a different plant category

**o- family**:
- okeey, oteey, oteedy, otedy, okeedy
- `o-` prefix may indicate a preparation or form modifier

**l- prefix group**:
- lchedy (39x), lkaiin (39x), lkeey (41x)
- The `l-` prefix consistently modifies base ingredient words
- This may represent "of the [plant]" (article) or a preparation method (e.g., "infusion of")

---

## 5. Preparation Verb Identification

### Words Appearing in Recipe-Body Position (NOT Plant Terms, NOT Quantities)

| Candidate Verb | Count | Position | Proposed Latin | Notes |
|----------------|-------|----------|----------------|-------|
| daiin | 185 | Throughout | **et** (and) | Connective, not a verb -- appears everywhere |
| aiin | 269 | Throughout | **et** / **cum** (and/with) | Function word |
| dal | 42 | Mid-recipe | **misce** (mix) | Appears after ingredient lists |
| dar | 63 | Mid-to-end | **da** (give) or **cola** (strain) | Often near -am terminators |
| sar | ~20 | Final lines | **solve** (dissolve) | End-of-preparation position |
| sal | ~25 | Mid-recipe | **cola** (strain) or **sale** (with salt) | |
| or | 102 | Throughout | **vel** (or) | Conjunction |
| ol | 150 | Throughout | **de** (of/from) | Preposition |
| ar | 158 | Throughout | **ad** (to/for) | Preposition |
| dol | ~30 | Mid-recipe | **tere** (grind) | |
| kor/chor | ~40 | Mid-recipe | **coque** (boil/cook) | |
| tor/tol | ~25 | Beginning | **tolle** (take/remove) | Latin imperative |

### Positional Analysis

**Recipe-initial verbs** (first word of @P0 body):
- Words starting with `t-`: tor, tol, tcheol, tsheeor -- possibly "tolle" (take) or "tere" (grind)
- Words starting with `k-`: kodaiin, kosholdy, kosar, kolor -- possibly "collige" (gather) or "coque" (cook)
- Words starting with `p-`: pcheol, polaiin, poleeol -- the `p-` prefix (KNOWN recipe marker) likely corresponds to "Recipe" (Take)

**Recipe-final verbs** (last words before -am or @Lc):
- `dar` (63x) -- consistently near sentence-final position. Strong candidate for **"da"** (give [to the patient])
- `dal` (42x) -- "da libenter" (give freely) or "da ad libitum"
- `saiin` (48x) -- possibly "signa" (label/mark) or "sero" (in the evening)
- `am` terminator words: sam (14x), dam (14x), ram (7x), oram (5x), cheam (5x)

### Proposed Verb-Stem Assignments

```
p-     = "Recipe" (Take) -- recipe opening marker
tor/tol = "tolle" (take/remove) or "tere" (grind)
dal    = "misce" (mix)
dar    = "da" (give)
kor    = "coque" (boil/cook)
sal    = "cola" (strain) or "sale" (with salt)
sar    = "solve" (dissolve)
```

---

## 6. Dosage Pattern

### Words in Recipe-Final Position

The `-am` terminator words cluster at recipe endings:

| Terminal Word | Count | Proposed Meaning |
|--------------|-------|-----------------|
| sam | 14 | "sero" (in the evening) -- dosage timing |
| dam | 14 | "da mane" (give in the morning) -- dosage timing |
| otam | 18 | "ad horam" (at the hour/time) -- timing marker |
| qokam | 12 | Quantity + terminator = dosage amount |
| okam | 7 | "hora" (hour) -- timing reference |
| aram | 8 | "ad aram" or general terminator |
| cham | 6 | Preparation-end marker |
| cheam | 5 | Variant terminator |

### Dosage Pattern Structure

The final 1-2 lines of a recipe typically contain:

```
[verb].dar/dal.[timing-word].[quantity-qo].[body-part?].[terminator-am]
```

Example (f88r, lines 8-11):
```
...qokor.aiin.sar.s.aiin.oky.sam        -- "...qo-amount, and dissolve, and ... sam"
oain.or.om.otam.okeom.cheeor.qokeody... -- "...otam [timing], okeom, [plant] qo-amount..."
qokeol.cheol.saiin...cheomam             -- "...cheomam [end]"
yokeody.cheom.qoor.cheeb.ykeor.shy.sam   -- "...sam [end/evening dose]"
```

The recurring pattern `dar...[word]...am` at recipe ends maps well to Latin:
- **"da bibere"** (give to drink) -- dar = da, [intervening word] = bibere
- **"mane et sero"** (morning and evening) -- dam = mane marker, sam = sero marker

### Proposed Dosage Vocabulary

| Voynichese | Latin | English |
|-----------|-------|---------|
| dar | da | give |
| sam | sero | in the evening |
| dam | [da] mane | in the morning |
| otam | hora/horam | at the hour/per hour |
| dal | da libenter / ad libitum | give freely |
| s.aiin | si (if) + and | conditional dosage |
| oky | omni (every) | every [time period] |

---

## 7. Cross-Reference with Antidotarium Nicolai

### Structural Parallels

The Antidotarium Nicolai (AN) contains ~150 standard recipes, organized as:

| Feature | Antidotarium Nicolai | Voynich Recipe Section |
|---------|---------------------|----------------------|
| Recipe count | ~150 | ~55-60 (partial manuscript) |
| Named recipes | Yes (e.g., "Aurea Alexandrina") | Yes (36 @Lc names) |
| Ingredient list format | Marginal or inline | @Lf marginal labels |
| Quantity system | drachma/uncia/scripulum | qo- prefix system |
| Standard opening | "Recipe..." | p- initial word |
| Closing formula | "da bibere" / dosage | dar...-am pattern |
| Ingredient count per recipe | 3-20+ | 3-8 @Lf entries per @Lc |

### Specific Structural Matches

**Match 1: Recipe naming convention**
- AN names recipes by color, effect, or primary ingredient (e.g., "Aurea" = golden, "Diamargariton" = with pearls)
- Voynich recipe names similarly appear to reference the primary ingredient or preparation

**Match 2: Marginal ingredient lists**
- The AN in many manuscript copies lists ingredients in the margin with quantities in the body text
- The Voynich @Lf//@P0 split mirrors this exactly: marginal labels list ingredients, body text provides quantities and instructions

**Match 3: Recipe length distribution**
- AN recipes range from 3-line simple recipes to 20+ line complex compounds
- Voynich recipes range from 3 lines (@Lc + 1 @Lf + 1 @P0) to 20+ lines (e.g., f88v recipe #4 with 21 continuation lines)
- The distribution curve is similar

**Match 4: The quantity cascade**
- AN recipes typically list the most common ingredient first with "drachma" quantities, then less common ingredients with "scripulum" or "uncia"
- Voynich recipes show qokeey (proposed drachma) appearing first, with qokaiin and qokain appearing later in the recipe body

### Important Caveats

1. The Voynich recipe section (f88-f116) only partially overlaps with the "pharmaceutical" folios as conventionally defined. Folios f103-f116 lack the @Lc label structure entirely and may represent a different text type (continuous prose rather than structured recipes).

2. The dense text section (f103-f116) has dramatically more text per page and fewer structural breaks, suggesting it may be **commentary or instructions** rather than recipe listings -- analogous to the expository sections of the AN that discuss properties, indications, and administration methods.

3. The 36 labeled recipes (f88-f102) represent the clearest parallel to the AN recipe format. The count of ~36 named compounds is consistent with a partial copy or an abbreviated pharmaceutical reference.

---

## 8. Summary of Proposed Decoding Framework

### Core Vocabulary Assignments (Confidence-Ranked)

**HIGH CONFIDENCE** (structural position + frequency consistent):
- `aiin` = "et" (and) -- function word, highest frequency
- `qokeey` = "drachma" (dram) -- dominant quantity word
- `p-` initial = "Recipe" (take) -- recipe opening marker
- `-am` suffix = sentence/clause terminator
- `@Lc` labels = recipe names
- `@Lf` entries = ingredient names

**MEDIUM CONFIDENCE** (positional evidence supports):
- `dar` = "da" (give) -- recipe-final position
- `dal` = "misce" (mix) -- mid-recipe position
- `qokaiin` = "uncia" (ounce) -- second-rank quantity
- `qokain` = "scripulum" (scruple) -- third-rank quantity
- `sam` = "sero" (evening) -- dosage timing
- `dam` = "mane" (morning) -- dosage timing
- `or` = "vel" (or) -- conjunction
- `ol` = "de" (of/from) -- preposition
- `chedy/shedy` = plant terms -- confirmed B-scribe botanical vocabulary

**SPECULATIVE** (requires further validation):
- `qokar` = "ana" (equal parts)
- `tor/tol` = "tolle/tere" (take/grind)
- `kor` = "coque" (boil)
- `sal` = "cola" (strain)
- `l-` prefix = article or preparation modifier
- `qokeedy` = genitive plural of drachma ("drachmarum")

### Recipe Template (Proposed Reading)

A Voynich recipe in the labeled section, read through this framework:

```
[RECIPE NAME]
  [Ingredient A]
  [Ingredient B]  
  [Ingredient C]
  
  Take [Ingredient A] [1 dram], [Ingredient B] [1 ounce],
  [Ingredient C] [1 scruple], and mix.
  Grind and strain. Give [in the evening / in the morning].
```

### Critical Limitation

This analysis identifies STRUCTURAL patterns and POSITIONAL roles for Voynichese words. It does NOT decrypt the underlying language. The actual phonetic or semantic values of individual words remain unknown. What we can say is:

1. The text is organized as pharmaceutical recipes
2. The structural organization mirrors 12th-15th century Latin/Italian recipe collections
3. The qo- prefix system encodes quantities in a systematic way
4. The p- prefix marks recipe openings
5. The -am suffix marks clause/sentence boundaries
6. The @Lc/@Lf/@P0 hierarchy preserves the layout conventions of medieval pharmaceutical manuscripts

This structural analysis is consistent with -- but does not prove -- the hypothesis that the Voynich manuscript's pharmaceutical section contains genuine medical recipes encoded in an unknown script or cipher.

---

## Appendix: Statistical Summary

| Metric | Value |
|--------|-------|
| Total lines in recipe section | 1,759 |
| Total word tokens | 13,575 |
| Unique word forms | 4,151 |
| Named recipes (@Lc) | 36 |
| Ingredient labels (@Lf) | 193 |
| Paragraph blocks (@P0) | 75 |
| qo- quantity words (tokens) | ~3,500+ |
| -am terminator words | ~180 |
| p- initial paragraphs | 22 |
| Folios covered | f88r, f88v, f89r1, f89r2, f89v1, f89v2, f90r1, f90r2, f90v1, f90v2, f93r, f93v, f94r, f94v, f95r1, f95r2, f95v1, f95v2, f96r, f96v, f99r, f99v, f100r, f100v, f101r, f101v, f102r1, f102r2, f102v1, f102v2, f103r, f103v, f104r, f104v, f105r, f105v, f106r, f106v, f107r, f107v, f108r, f108v, f111r, f111v, f112r, f112v, f113r, f113v, f114r, f114v, f115r, f115v, f116r, f116v |
