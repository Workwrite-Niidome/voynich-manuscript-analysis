# Voynich Medical Morpheme Analysis: Preparation, Administration, Body, and Temporal Terms

## Source: RF1b-e.txt (EVA transcription, full manuscript)
## Focus: Recipe section f88r-f116v (1,759 lines, 14,254 word tokens)
## Baseline: Herbal section f1r-f57v (9,561 word tokens)

---

## PREVIOUSLY DECODED (Reference)

| Morpheme | Meaning | Confidence | Evidence |
|----------|---------|------------|----------|
| qo- | quantity prefix | HIGH | Dominant recipe prefix, precedes measure words |
| qokeey | drachma (dram) | HIGH | Most common qo- word (296 ms-wide), doubled patterns |
| p- | recipe/take (Recipe) | HIGH | 25 recipe-initial words begin with p-; line-start preference 0.376 |
| +eeo | preparation level (3.8x enriched) | HIGH | Grade system correlation r=-0.954 |
| k root | measure/body | HIGH | 8,259 words, recipe enrichment 1.28x |
| t root | process/time | HIGH | 4,706 words, ot- prefix 43% |
| lk root | dose (7.49x recipe enriched) | HIGH | 1,042 words, 54% recipe section |
| dal | misce (mix) | MEDIUM | 42 recipe occurrences, mid-recipe position |
| dar | da (give) | MEDIUM | 63 recipe occurrences, recipe-final position |
| -am | sentence/clause terminator | HIGH | 735 occurrences, recipe boundary marker |

---

## 1. PREPARATION METHOD MORPHEMES

### 1A. Recipe-Initial Verbs (Imperative Position)

The first word of each recipe body (@P0) occupies the imperative verb slot, equivalent to Latin "Recipe..." or "Tolle..." in medieval formularies. Analysis of 73 recipe-opening words yields three dominant stem families:

| Stem | Count | Example Words | Proposed Latin | Confidence |
|------|-------|---------------|----------------|------------|
| **p-** | 25 (34%) | pcheol, polaiin, poeear, pcheody, pshodaiin, pchedal, pchdar, pshdar | **Recipe** (Take) | HIGH |
| **t-** | 14 (19%) | tcheol, teodal, tsheeor, tolkeey, tolchor, teesody, tchedor | **Tolle/Tere** (Take/Grind) | MEDIUM |
| **k-** | 14 (19%) | kosholdy, kodaiin, kosar, kolches, kolor, koshey | **Coque/Collige** (Cook/Gather) | MEDIUM |
| **f-** | 5 (7%) | folsho, faidaiin, fsheda, folchey | **Fac** (Make) | LOW |
| **s-** | 2 (3%) | sor, sol | **Solve** (Dissolve) | LOW |
| **d-** | 2 (3%) | doreoy, doror | Unknown | LOW |

**Key Finding**: The p- stem accounts for 34% of recipe openings, confirming it as the primary recipe imperative. The t- and k- stems each account for 19%, suggesting two additional preparation actions. The t- stem (process) likely encodes "grind" (tere) or "take" (tolle), while k- (body/measure) likely encodes "cook" (coque) or "gather" (collige).

### 1B. Mid-Recipe Preparation Verbs

Words appearing in instruction positions between ingredients and dosage, with recipe enrichment analysis:

| Morpheme | Recipe Count | Herbal Count | Recipe Enrichment | Proposed Meaning | Confidence |
|----------|-------------|-------------|-------------------|------------------|------------|
| **sar** | 30 | 9 | 2.24x | **solve** (dissolve) or **cola** (strain) | MEDIUM |
| **dol** | 28 | 37 | 0.51x | **tere** (grind/pulverize) | MEDIUM |
| **sal** | 14 | 7 | 1.34x | **cola** (strain) or **cum sale** (with salt) | LOW-MEDIUM |
| **sol** | 14 | 8 | 1.17x | **solve** (dissolve) | LOW-MEDIUM |
| **lor** | 23 | 1 | 15.4x | **lora** (wash/rinse) or structural verb | MEDIUM |
| **tol** | 10 | 14 | 0.48x | **tolle** (take/remove) | LOW-MEDIUM |
| **tor** | 7 | 7 | 0.67x | **torque** (twist/press) or **tolle** variant | LOW |
| **kor** | 7 | 15 | 0.31x | **coque** (boil/cook) | LOW-MEDIUM |

**Pattern: sar contextual evidence**

sar is followed by `aiin` (6x), `ain` (5x), `al` (3x) -- these are connective/structural words, suggesting sar is a TERMINAL action verb (strain/dissolve, then the recipe continues with "and..."). Its 2.24x recipe enrichment supports a pharmaceutical operation.

**Pattern: dol contextual evidence**

dol precedes `shey` (3x), `cheol` (2x), `ol` (2x) -- plant terms follow dol, consistent with "grind [ingredient]". Despite not being recipe-enriched overall (it appears in herbal descriptions too, perhaps as "grind/pound"), its recipe usage is clearly procedural.

### 1C. Preparation Type Compound Morphemes

The opch- family (o + pch = general + preparation-herb) represents compound preparations:

| Morpheme | Recipe | Herbal | Total | Proposed Meaning | Confidence |
|----------|--------|--------|-------|------------------|------------|
| **opchedy** | 20 | 3 | 38 | The defined specific preparation (confectio/electuarium) | MEDIUM |
| **opchey** | 18 | 7 | 38 | A specific preparation (praeparatio specifica) | MEDIUM |
| **opchy** | 10 | 7 | 17 | A preparation (generic) | MEDIUM |
| **opchdy** | 7 | 0 | 15 | The defined preparation (recipe-exclusive!) | MEDIUM-HIGH |
| **opcheol** | 6 | 1 | 7 | The preparation state-subject | LOW |
| **opchedaiin** | 4 | 0 | 5 | The defined preparation entity | LOW |

**opchdy is entirely absent from herbal text** (0 herbal occurrences, 7 recipe), making it the purest recipe-exclusive preparation term. Morpheme decomposition: o(general) + p(preparation) + ch(herb) + d(definite) + y(default) = "the completed/defined herbal preparation."

### 1D. Proposed Preparation Method Mapping

Based on positional analysis and morphological patterns:

| Preparation | Latin | Voynichese | Position Evidence | Confidence |
|------------|-------|------------|-------------------|------------|
| Take/Receive | Recipe | p- initial | 34% of recipe openings | HIGH |
| Grind/Pulverize | Tere | dol / t- initial | "dol shey" = grind root; t-initial recipes | MEDIUM |
| Boil/Cook | Coque | kor / k- initial | k- initial = 19% of recipes | LOW-MEDIUM |
| Dissolve/Strain | Solve/Cola | sar / sal | sar 2.24x enriched, terminal position | MEDIUM |
| Mix | Misce | dal | mid-recipe position, between ingredients | MEDIUM |
| Give | Da | dar | recipe-final position | MEDIUM |
| Make/Prepare | Fac | f- initial | 7% of recipe openings | LOW |
| The preparation | Confectio | opchedy/opchdy | Compound pch- morpheme | MEDIUM |
| Dissolve | Solve | sol | 14 recipe occurrences | LOW |
| Rinse/Wash | Lora/Lava | lor | 23 recipe, 1 herbal (15.4x enriched) | LOW-MEDIUM |

---

## 2. ADMINISTRATION ROUTE MORPHEMES

### 2A. dar + X Patterns (Give + How)

The verb dar (da = give) is followed by words that specify the administration route:

| Pattern | Count | Proposed Reading | Confidence |
|---------|-------|------------------|------------|
| dar aiin | 3 | "give and [continue]" (da et...) | MEDIUM |
| dar al | 3 | "give to/for [purpose]" (da ad...) | LOW-MEDIUM |
| dar chedy | 3 | "give [herb preparation]" (da herbam) | LOW |
| dar am | 2 | "give [terminal]" (da [end of instruction]) | MEDIUM |
| dar ar | 2 | "give [quality/attribute]" (da qualiter) | LOW |

### 2B. X + dar Patterns (What + Give)

| Pattern | Count | Proposed Reading | Confidence |
|---------|-------|------------------|------------|
| al dar | 4 | "[functional structure] give" = "to be given" | LOW |
| aiin dar | 3 | "and give" (et da) | MEDIUM |
| otal dar | 2 | "[process-structure] give" = "give by process" | LOW |
| oteey dar | 2 | "[specific process] give" | LOW |
| ol dar | 2 | "[the subject] give" = "give this" | LOW |

### 2C. -am Terminal Administration Words

The -am suffix marks sentence boundaries AND encodes administration/timing context. The stem before -am reveals the type of terminal instruction:

| Terminal | Count | Stem | Decomposition | Proposed Meaning | Confidence |
|----------|-------|------|---------------|------------------|------------|
| **otam** | 18 | ot- | process + measure | "per horam" (at the hour/per cycle) | MEDIUM |
| **dam** | 14 | d- | functional + measure | "da mane" (give in the morning) | MEDIUM |
| **qokam** | 11 | qok- | body-quantity + measure | "quantum" (as much as needed) | MEDIUM |
| **qotam** | 9 | qot- | body-process + measure | "per tempus" (for a time/duration) | LOW-MEDIUM |
| **okam** | 7 | ok- | body-specific + measure | "hora" (at the hour) | LOW-MEDIUM |
| **aram** | 7 | ar- | quality + measure | "ad modum" (in the manner of) | LOW |
| **ram** | 7 | r- | quality + measure | Bare quality-measure terminal | LOW |
| **sam** | 6 | s- | collective + measure | "sero" (in the evening) | MEDIUM |
| **lkam** | 6 | lk- | dose + measure | "dosis" (the dose [amount]) | MEDIUM |
| **cheam** | 6 | che- | specific herb + measure | "herbam" (the herb [accusative]) | LOW |
| **chedam** | 5 | ched- | defined herb + measure | "herbam definitam" | LOW |
| **cham** | 4 | ch- | herb + measure | "herbam" (generic herb terminal) | LOW |
| **alam** | 4 | al- | functional-structure + measure | "ad libitum" (at will) | LOW-MEDIUM |
| **olam** | 4 | ol- | subject + measure | "huic" (to this one) | LOW |
| **sham** | 3 | sh- | root + measure | "radicem" (the root [accusative]) | LOW |

### 2D. Administration Route Summary

Medieval recipes end with instructions like "da bibere" (give to drink), "applica" (apply), "da mane et sero" (give morning and evening). In Voynichese:

| Route | Latin | Voynichese Candidate | Evidence | Confidence |
|-------|-------|---------------------|----------|------------|
| Internal liquid (drink) | bibere | **sar + aiin** or **sal** | sar in terminal position, followed by connective | LOW |
| Internal solid (eat) | manducare | Not clearly differentiated | - | VERY LOW |
| External (apply) | applicare | **lor** (15.4x recipe enriched) | Recipe-exclusive, possibly "wash/apply" | LOW |
| Morning dose | mane | **dam** | 14 occurrences at recipe end | MEDIUM |
| Evening dose | sero | **sam** | 6 occurrences at recipe end | MEDIUM |
| At the hour | ad horam | **otam** | 18 occurrences, most common -am word | MEDIUM |
| As needed | quantum sufficit | **qokam** | qo(quantity) + k(measure) + am(terminal) | MEDIUM |

---

## 3. BODY PART / DISEASE MORPHEMES

### 3A. Herbal Late-Line Analysis (Lines 5+ of Herbal Entries)

In medieval herbals, the first lines describe the plant (appearance, habitat), while later lines describe medical uses (which body part, which disease). Words enriched in lines 5+ vs. lines 1-4 of herbal entries are candidates for body part/disease terms:

| Morpheme | Late Lines (5+) | Early Lines (1-4) | Enrichment | Proposed Domain | Confidence |
|----------|-----------------|-------------------|------------|-----------------|------------|
| **shody** | 21 | 1 | 7.95x | Body/condition term (root-state + definite + default) | MEDIUM |
| **cthaiin** | 13 | 1 | 4.92x | Process-botanical entity -- possibly a treated condition | LOW |
| **chokchy** | 13 | 1 | 4.92x | Herb-body compound -- possibly "for the body of [plant]" | LOW |
| **key** | 11 | 1 | 4.16x | Specific measure (bare k + e + y) -- possibly symptom/sign | LOW |
| **tchol** | 10 | 1 | 3.78x | Process-herb-subject -- possibly "procedure for this [organ]" | LOW |
| **tar** | 8 | 1 | 3.03x | Process-quality -- possibly "fever/heat" (calor) | LOW-MEDIUM |
| **ykeey** | 13 | 2 | 2.95x | Connector + specific measure -- dosage reference | LOW |
| **chear** | 14 | 3 | 2.27x | Herb-quality (specific) -- possibly a plant property | LOW |
| **cheol** | 18 | 4 | 2.27x | Herb-state-subject -- "the herbal [organ/part]" | LOW |
| **qodaiin** | 10 | 2 | 2.27x | Body-functional entity -- possibly "for [patient]" | LOW |
| **otal** | 13 | 3 | 2.11x | Process-structure -- possibly body structure/organ | LOW-MEDIUM |

### 3B. Body Part Morpheme Candidates (from root decomposition)

Based on the established morpheme system where ok- = body-specific prefix and k = body/measure root:

| Morpheme | Total Freq | Recipe | Herbal | Decomposition | Proposed Body Reference | Confidence |
|----------|-----------|--------|--------|---------------|------------------------|------------|
| **okal** | 43 | significant | present | ok(body) + al(structure) | Body structure/organ (generic) | MEDIUM |
| **okain** | varied | present | present | ok(body) + ain(entity) | Body entity/patient | LOW-MEDIUM |
| **okam** | 7 | recipe | - | ok(body) + am(measure) | Body measure/dose timing | LOW |
| **okar** | 48 | significant | present | ok(body) + ar(quality) | Body quality/condition | LOW-MEDIUM |
| **okchey** | 37 | present | present | ok(body) + ch(herb) + ey | Body-relevant specific herb | MEDIUM |
| **okchedy** | 11 | recipe-exclusive | 0 herbal | ok(body) + ch(herb) + edy | Defined body-herb (medicinal) | MEDIUM |
| **otal** | 61 | significant | present | ot(process) + al(structure) | Treated structure/organ | LOW-MEDIUM |
| **otain** | 56 | enriched 6.83x | 5 | ot(process) + ain(entity) | Process entity -- possibly "patient/condition" | MEDIUM |

### 3C. Disease/Condition Candidates

| Morpheme | Evidence | Proposed Meaning | Reasoning | Confidence |
|----------|----------|------------------|-----------|------------|
| **shody** | 7.95x herbal-late enrichment | A root-state condition (morbus) | sh(root/hidden) + o(state) + dy(of-definite) = "of the hidden condition" = disease | LOW-MEDIUM |
| **tar** | 3.03x herbal-late enrichment | Heat/fever (calor/febris) | t(process) + ar(quality) = "processual quality" = temperature/fever | LOW |
| **otal** | 2.11x herbal-late enrichment | Organ/body part treated | ot(process) + al(structure) = "the structure under treatment" | LOW-MEDIUM |
| **chear** | 2.27x herbal-late enrichment | Herbal virtue/property | ch(herb) + e(specific) + ar(quality) = "specific herbal quality" | LOW |
| **chokchy** | 4.92x herbal-late enrichment | Medicinal application | cho(herb-state) + kch(body-herb) + y = "herb-body interaction" | LOW |

---

## 4. TEMPORAL / DOSAGE FREQUENCY MORPHEMES

### 4A. -am Terminal Temporal System

The -am suffix encodes "extent/measure" (from root m = measure terminal). When combined with temporal roots, it produces dosage timing:

| Temporal -am | Count | Decomposition | Proposed Timing | Evidence | Confidence |
|-------------|-------|---------------|-----------------|----------|------------|
| **dam** | 14 | d(functional) + am | **mane** (morning) | Recipe-final position, paired with sam | MEDIUM |
| **sam** | 6 | s(collective) + am | **sero** (evening) | Recipe-final position | MEDIUM |
| **otam** | 18 | ot(process) + am | **ad horam** (at the hour) | Most common -am word; process-time marker | MEDIUM |
| **qotam** | 9 | qo(body) + t(process) + am | **per diem** (per day/daily) | Body-process-measure = daily cycle | LOW-MEDIUM |
| **qokam** | 11 | qo(body) + k(measure) + am | **quantum sufficit** (as needed) | Body-quantity-measure = measured dose | MEDIUM |
| **alam** | 4 | al(structure) + am | **ad libitum** (at will/freely) | Structure-measure = open timing | LOW-MEDIUM |
| **olam** | 4 | ol(subject) + am | **hoc modo** (in this way) | Subject-measure terminal | LOW |
| **lkam** | 6 | lk(dose) + am | **dosis** (the dose itself) | Dose-measure terminal | MEDIUM |

### 4B. Dosage Frequency Patterns

| Pattern | Count | Proposed Meaning | Evidence |
|---------|-------|------------------|----------|
| **qokeey qokeey** | 14 | "drachma [et] drachma" (two drams) | Most common doubled quantity |
| **dam...sam** | varies | "mane et sero" (morning and evening) | Classic medieval posology |
| **otam** + quantity | 2+ | "per horam [quantum]" (per hour, [amount]) | qokaiin otam = "ounce per hour" |
| **oky** | recipe-enriched | **omni** (every) or **quotidie** (daily) | Appears near dosage terminals |
| **oty** | recipe-enriched | **ad tempus** (at the time) | ot(process) + y(default) |
| **otain ar** | 6 bigrams | "at this time [quality]" = scheduled dose | Process-entity + quality |
| **ar al** | 19 bigrams | "to the [structure/organ]" = target body part | Most common structural bigram |

### 4C. Dosage Quantity Hierarchy (Refined)

| Morpheme | Recipe Count | Decomposition | Proposed Unit | Confidence |
|----------|-------------|---------------|---------------|------------|
| qokeey | 218 (recipe) | qo+k+ee+y | drachma (dram) -- standard unit | HIGH |
| qokaiin | 126 | qo+k+aiin | uncia (ounce) -- large unit | MEDIUM |
| qokain | 100 | qo+k+ain | scripulum (scruple) -- small unit | MEDIUM |
| qokeedy | 88 | qo+k+ee+dy | drachma (genitive: "of drams") | MEDIUM |
| qokey | 72 | qo+k+e+y | semidrachma (half-dram) | LOW-MEDIUM |
| qokal | 43 | qo+k+al | libra/manipulus (pound/handful) | LOW |
| qoky | 39 | qo+k+y | quantum sufficit (as needed) | MEDIUM |
| qokol | 33 | qo+k+ol | numerus (counted unit) | LOW |
| lkeey | 41 (recipe) | lk+ee+y | specific dose unit | HIGH (lk 7.49x enriched) |
| lkaiin | 39 (recipe) | lk+aiin | dose entity (dosis) | HIGH |
| olkeey | 21 (recipe-exclusive) | ol+lk+ee+y | "this specific dose" | HIGH |

---

## 5. COMPLETE MEDICAL MORPHEME TABLE

### Tier 1: HIGH Confidence (structural + frequency + cross-validation)

| Morpheme | Function | Medieval Equivalent | Key Evidence |
|----------|----------|--------------------| ------------|
| p- (initial) | Recipe opening imperative | Recipe (Take) | 34% of recipe openings; 0.376 line-position |
| qokeey | Standard quantity unit | drachma | Most common qo- word; doubled patterns qokeey qokeey |
| lk root | Dose/dosage | dosis | 7.49x recipe enrichment; 54% in recipe section |
| dal | Mix | misce | Mid-recipe position between ingredient lists |
| dar | Give (to patient) | da | Recipe-final position; 63 recipe occurrences |
| -am suffix | Terminal/boundary marker | (end of instruction) | 735 occurrences across manuscript |
| opch- compound | Prepared substance | confectio/praeparatio | pch 43.9% recipe section; highest recipe concentration |

### Tier 2: MEDIUM Confidence (positional evidence supports)

| Morpheme | Function | Medieval Equivalent | Key Evidence |
|----------|----------|--------------------| ------------|
| t- (initial) | Grind/take | tere/tolle | 19% of recipe openings |
| k- (initial) | Cook/gather | coque/collige | 19% of recipe openings |
| sar | Dissolve/strain | solve/cola | 30 recipe occurrences, 2.24x enriched; terminal verb |
| dol | Grind/pulverize | tere/contere | 28 recipe occurrences; "dol shey" = grind root |
| lor | Wash/rinse | lava/lora | 23 recipe vs 1 herbal (15.4x enriched!) |
| dam | Morning timing | mane | 14 recipe-terminal occurrences |
| sam | Evening timing | sero | 6 recipe-terminal occurrences |
| otam | Hourly/timed | ad horam | 18 occurrences; most common -am word |
| qokam | As needed | quantum sufficit | qo(body) + k(measure) + am |
| lkam | Dose terminal | dosis (completed) | lk(dose) + am(measure) |
| otain | Condition/patient | aeger/conditio | 56 recipe, 5 herbal (6.83x enriched) |
| oky | Every/daily | omni/quotidie | Recipe-enriched, near dosage terms |
| opchdy | Defined preparation | confectio definita | 7 recipe, 0 herbal (recipe-exclusive) |
| shody | Disease/condition | morbus | 7.95x herbal-late enrichment |

### Tier 3: LOW-MEDIUM Confidence (pattern-consistent but less evidence)

| Morpheme | Function | Medieval Equivalent | Key Evidence |
|----------|----------|--------------------| ------------|
| sal | Strain/salt | cola/sal | 14 recipe occurrences; mid-recipe position |
| sol | Dissolve | solve | 14 recipe occurrences |
| kor | Boil/cook | coque | k root + or(quality); 7 recipe occurrences |
| tol | Take/remove | tolle | 10 recipe occurrences; t root + ol(subject) |
| tor | Press/grind | torque/tere | 7 recipe occurrences; t root + or(quality) |
| f- (initial) | Make/prepare | fac | 5 recipe openings (7%) |
| tar | Fever/heat | calor/febris | 3.03x herbal-late enrichment; t + ar = process-quality |
| okal | Body structure | organum | ok(body) + al(structure) |
| otal | Treated organ | membrum | ot(process) + al(structure) |
| alam | At will | ad libitum | al(structure) + am(measure) |
| chear | Herbal virtue | virtus herbae | ch + ear; 2.27x late-herbal enrichment |
| chokchy | Medicinal use | usus medicinalis | 4.92x late-herbal enrichment |
| ar al | To the organ/part | ad [partem] | 19 bigrams in recipes; most common structural pair |
| qotam | Daily cycle | per diem | qo + t + am; 9 occurrences |

### Tier 4: LOW Confidence (speculative, requires further validation)

| Morpheme | Function | Medieval Equivalent | Key Evidence |
|----------|----------|--------------------| ------------|
| cthaiin | Treated condition | passio | 4.92x late-herbal enrichment |
| tchol | Organ under procedure | Not mapped | 3.78x late-herbal enrichment |
| sham | Root-measure terminal | radicem (accusative) | sh + am; 3 recipe occurrences |
| cheam | Herb-measure terminal | herbam (accusative) | che + am; 6 recipe occurrences |
| sar + aiin | Drink (give to drink) | bibere | sar followed by aiin 6x |
| lor | Apply externally | applicare | 15.4x recipe enrichment, but low absolute count |

---

## 6. RECIPE TEMPLATE (Complete Proposed Reading)

A Voynich recipe, read through the full medical morpheme system:

```
@Lc   [RECIPE NAME]                    -- e.g., "otorchety" (process-body-herb-process-y)
@Lf   [Ingredient A]                   -- e.g., "osal" (general-strain?)
@Lf   [Ingredient B]                   -- e.g., "orald"
@Lf   [Ingredient C]                   -- e.g., "oldar"

@P0   p[verb] [ingredient] qokeey     -- "Take [ingredient A], one dram"
+P0   [ingredient B] qokaiin          -- "[ingredient B], one ounce"
+P0   dal [connecting words]           -- "Mix [together]"
+P0   dol [ingredient] qokain          -- "Grind [ingredient C], one scruple"
+P0   sar aiin sal                      -- "Dissolve and strain"
+P0   dar [al/am] dam / sam             -- "Give in the morning / in the evening"
+P0   olkeey otam                       -- "[This dose] at the hour"
+P0   [final word]-am                   -- [End of recipe]
```

### Exemplar: f88r Recipe #1 "otorchety" (re-read)

```
otorchety                               -- RECIPE: [process-body-herb-process] preparation
  osal                                  -- Ingredient: [general-strain/salt]
  orald                                 -- Ingredient: [state-quality-structure-definite]
  oldar                                 -- Ingredient: [subject-give-quality]
  otoky                                 -- Ingredient: [process-body-measure-default]
  otaly                                 -- Ingredient: [process-structure-default]

  doreoy ctheol qockhey dory sheor sholfchor dal chcthol
  -- "[verb] [process-herb-state-subject] [qo-body-herb-specific-y = quantity] [...]
      [root-state-quality] [root-subject-herb-quality] dal(mix) [herb-process-herb-subject]"
  
  sal sheom keol chear shekor qokor aiin sar s aiin oky sam
  -- "sal(strain) [root-state-measure] [measure-state-subject] [herb-quality]
      [root-measure-quality] qo(quantity)-kor(cook) and sar(dissolve) and [every] sam(evening)"
```

---

## 7. STRUCTURAL OBSERVATIONS

### The Verb Position System

Medieval Latin pharmaceutical texts have a rigid word order for imperatives:
1. **Recipe** (Take) -- always first
2. **Ingredient + Quantity** -- listed in pairs
3. **Preparation verb** (misce, tere, coque, cola) -- mid-recipe
4. **Administration** (da bibere, applica) -- near end
5. **Timing** (mane et sero, ad horam) -- final

The Voynich recipe section follows this EXACT order:
1. **p-** words open recipes (34% of @P0 lines)
2. **[word] qo[word]** pairs fill the body
3. **dal, dol, sar, sal** appear mid-recipe
4. **dar** appears near recipe end
5. **dam, sam, otam** appear as final -am terminators

### The s-/d- Morning/Evening Pair

The proposal that dam = mane (morning) and sam = sero (evening) is supported by:
- Both appear exclusively at recipe-terminal positions
- dam (14x) is more frequent than sam (6x), consistent with "morning dose" being more commonly prescribed
- The d-/s- contrast maps to the functional/collective terminal distinction: d = definite/specific time (morning = start of day), s = collective/general time (evening = end of day)

### The lor Enigma

lor (23 recipe, 1 herbal, 15.4x enrichment) is one of the most recipe-specific non-qo words. Its decomposition l(structure) + o(state) + r(quality) = "structural-state-quality" is ambiguous. In context, it is followed by aiin (4x = "and"), cheo (2x = "herbal state"), suggesting it is a PROCESS that produces a result. Candidate meanings:
- **Lava** (wash) -- consistent with l(structure) = the physical washing action
- **Liqua** (liquefy) -- l(structure) in liquid form
- **Lora** (steep/soak) -- preparation by soaking

---

## 8. CONFIDENCE SUMMARY

| Category | HIGH | MEDIUM | LOW-MEDIUM | LOW |
|----------|------|--------|------------|-----|
| Preparation methods | 1 (p-) | 3 (sar, dol, lor) | 5 (sal, sol, kor, tol, tor) | 2 (f-, mor) |
| Administration routes | 0 | 2 (dam, sam) | 2 (otam, qokam) | 3 |
| Body/disease terms | 0 | 2 (otain, shody) | 3 (okal, otal, tar) | 3 |
| Temporal/frequency | 0 | 4 (dam, sam, otam, oky) | 2 (qotam, alam) | 1 |
| Dosage units | 3 (qokeey, lk, olkeey) | 3 (qokaiin, qokain, qoky) | 2 | 0 |
| Preparation compounds | 2 (opch-, opchdy) | 2 (opchedy, opchey) | 0 | 0 |
| **TOTAL** | **6** | **16** | **14** | **9** |

Total morphemes catalogued: 45 medical/pharmaceutical terms.

---

*Generated from RF1b-e.txt EVA transcription. Analysis based on positional statistics, recipe enrichment ratios, morphological decomposition, and comparison with medieval Latin/Italian pharmaceutical formulary structure.*
