# Voynich Manuscript: Suffix Semantic Analysis

## Corpus Statistics
- Total word tokens: 37,824
- Total text lines: 5,420
- Folios with Currier Language A tag: 102; Language B: 72
- Section sizes: herbal=9,954 (26.3%), recipe=14,334 (37.9%), bio=9,171 (24.2%), astro=1,879 (5.0%), other=2,486 (6.6%)

## Suffix Frequencies

| Suffix | Count | % of corpus |
|--------|-------|-------------|
| -y     | 5,186 | 13.7%       |
| -aiin  | 3,277 |  8.7%       |
| -ey    | 2,883 |  7.6%       |
| -edy   | 2,797 |  7.4%       |
| -ol    | 2,794 |  7.4%       |
| -ar    | 2,316 |  6.1%       |
| -eey   | 2,150 |  5.7%       |
| -dy    | 1,884 |  5.0%       |
| -al    | 1,746 |  4.6%       |
| -or    | 1,666 |  4.4%       |
| -ain   | 1,505 |  4.0%       |
| -am    |   644 |  1.7%       |
| -an    |   108 |  0.3%       |

Total suffixed words: ~29,000 out of 37,824 (77% of all tokens carry one of these suffixes).

---

## 1. Section Distribution

The key question: are suffixes section-specific (encoding domain content) or section-independent (encoding grammar)?

### Strongly section-biased suffixes (ratio > 1.5 or < 0.5 in at least 2 sections):

**-edy** (n=2,797): The most dramatically skewed suffix.
- Herbal: 7.7% (expected 26.3%, ratio 0.29) -- massively underrepresented
- Bio: 48.6% (expected 24.2%, ratio 2.01) -- massively overrepresented
- Astro: 1.0% (expected 5.0%, ratio 0.19) -- nearly absent
- Recipe: 40.7% (expected 37.9%, ratio 1.07) -- baseline

**-or** (n=1,666): Herbal-dominant.
- Herbal: 45.5% (expected 26.3%, ratio 1.73) -- strongly overrepresented
- Bio: 14.2% (expected 24.2%, ratio 0.58) -- underrepresented
- Astro: 2.3% (expected 5.0%, ratio 0.47) -- underrepresented

**-ain** (n=1,505): Recipe/Bio preference, avoids herbal/astro.
- Herbal: 14.8% (expected 26.3%, ratio 0.56) -- underrepresented
- Recipe: 49.0% (expected 37.9%, ratio 1.29) -- overrepresented
- Astro: 0.5% (expected 5.0%, ratio 0.11) -- nearly absent

**-y** (n=5,186): Herbal-leaning.
- Herbal: 36.4% (expected 26.3%, ratio 1.38) -- overrepresented
- Recipe: 26.7% (expected 37.9%, ratio 0.70) -- underrepresented

**-ol** (n=2,794): Mild herbal preference.
- Herbal: 34.3% (expected 26.3%, ratio 1.30)

**-al** (n=1,746): Astro preference.
- Astro: 9.0% (expected 5.0%, ratio 1.81)

**-am** (n=644): Astro preference.
- Astro: 7.9% (expected 5.0%, ratio 1.59)

### Section-neutral suffixes:
- **-ar**: fairly even across sections (ratio 0.83-1.35)
- **-dy**: fairly even (ratio 0.81-1.39)
- **-aiin**: mild herbal lean but basically distributed

### Interpretation:
Suffixes are NOT section-neutral. The dramatic section bias of -edy (bio-concentrated), -or (herbal-concentrated), and -ain (astro-avoidant) argues AGAINST pure grammatical function. A grammatical marker (like a case ending) would distribute roughly evenly across topics. These biases suggest suffixes encode semantic content that varies by subject matter.

---

## 2. Position in Herbal Entries

Mapping suffix position to expected entry structure (beginning=name/description, middle=properties, end=preparation).

### Position-biased suffixes:

**Beginning-heavy (mean_pos < 0.46):**
- -dy: mean=0.432, beginning=41.2%
- -y: mean=0.433, beginning=42.1%
- -ar: mean=0.443, beginning=41.7%

**End-heavy (mean_pos > 0.51):**
- -eey: mean=0.526, beginning=36.1%, end=40.9%
- -al: mean=0.526, beginning=30.8%, end=38.5%

**Middle-heavy:**
- -edy: mean=0.456, middle=41.6%, end=25.2%

**Neutral (evenly distributed):**
- -ol: mean=0.495, all thirds ~32%
- -aiin: mean=0.476, fairly even
- -ain: mean=0.501, very even

### Interpretation:
-y, -dy, -ar tend to appear at the beginning of herbal entries (plant name, physical description zone). -eey and -al lean toward the end (preparation/dosage zone). -edy concentrates in the middle (properties/habitat zone). This positional variation is modest but consistent with suffixes carrying different semantic loads rather than purely grammatical function.

---

## 3. Stem x Suffix Co-occurrence Matrix

### Key findings from the top 30 stems:

1. **Most stems accept nearly ALL suffixes.** The top 7 stems (ch, qok, d, ok, sh, ot, qot) each take 13 out of 13 possible suffixes. Average suffix diversity for stems with >=5 tokens: 5.6 different suffixes.

2. **Despite high diversity, stems show strong suffix preferences:**
   - `d-`: 40% -aiin (713/1779). The stem `d` overwhelmingly prefers -aiin.
   - `q-`: 80% -ol (138/173). Almost exclusively takes -ol.
   - `chckh-`: 69% -y (139/201).
   - `qoke-`: 65% -edy (222/339).
   - `che-`: 36% -ol (155/426).
   - `she-`: 38% -ol (95/248).

3. **Two stem groups emerge based on suffix affinity:**
   - "ol/or-preferring" stems: q, che, she, ch (Language A pattern)
   - "edy/eey-preferring" stems: qoke, lch, ote, sh (Language B pattern)

### Interpretation:
The fact that stems can take many suffixes but show strong preferences is consistent with a system where suffixes modify meaning (like plant-part or preparation-method markers) rather than being rigid grammatical endings. A noun declension system would show more exclusive stem-suffix binding.

---

## 4. Test: Suffixes = Plant Parts

Hypothesis: different suffixes appear on pages with different illustration types (leaf-prominent vs root-prominent).

Baseline leaf/(leaf+root) ratio: 0.325

| Suffix | Leaf | Root | L/(L+R) | Deviation |
|--------|------|------|---------|-----------|
| -an    |   29 |   20 | 0.592   | +0.267 ** |
| -or    |  284 |  435 | 0.395   | +0.070    |
| -ol    |  299 |  584 | 0.339   | +0.014    |
| -y     |  597 | 1163 | 0.339   | +0.014    |
| -aiin  |  326 |  650 | 0.334   | +0.009    |
| -dy    |  146 |  328 | 0.308   | -0.017    |
| -ey    |  154 |  346 | 0.308   | -0.017    |
| -or    |  284 |  435 | 0.395   | +0.070    |
| -eey   |   65 |  165 | 0.283   | -0.042    |
| -ar    |  128 |  333 | 0.278   | -0.047    |
| -al    |   55 |  182 | 0.232   | -0.093 *  |
| -am    |   36 |  115 | 0.238   | -0.087 *  |
| -edy   |   34 |  121 | 0.219   | -0.106 ** |

### Significant deviations:
- **-an**: strongly leaf-associated (0.592 vs baseline 0.325). Small sample (n=49) but dramatic.
- **-edy**: strongly root-associated (0.219 vs baseline 0.325).
- **-al**: root-leaning (0.232).
- **-am**: root-leaning (0.238).
- **-or**: leaf-leaning (0.395).

### Verdict: PARTIALLY SUPPORTED
-edy and -al/-am do show illustration-dependent variation, concentrating on root-heavy pages. -an and -or lean toward leaf pages. However, the deviations are modest (except -an), and many suffixes (-aiin, -ol, -y, -dy) show no meaningful variation. This suggests illustration type has some influence but suffixes do not straightforwardly map to plant parts.

---

## 5. Test: Suffixes = Preparation Methods

Hypothesis: if suffixes encode preparation type, they should shift between herbal (raw descriptions) and recipe (preparations) sections.

| Suffix | Herbal rate | Recipe rate | Ratio (R/H) |
|--------|------------|-------------|-------------|
| -edy   |     2.15%  |     7.94%   | 3.69 ***    |
| -eey   |     2.70%  |     7.95%   | 2.94 ***    |
| -ain   |     2.24%  |     5.15%   | 2.30 ***    |
| -al    |     2.74%  |     4.52%   | 1.65        |
| -ey    |     5.80%  |     7.35%   | 1.27        |
| -ar    |     5.06%  |     6.24%   | 1.23        |
| -ol    |     9.63%  |     7.08%   | 0.73        |
| -y     |    18.95%  |     9.65%   | 0.51 ***    |
| -or    |     7.62%  |     3.73%   | 0.49 ***    |
| -an    |     0.58%  |     0.21%   | 0.36 ***    |
| -aiin  |    10.71%  |     9.45%   | 0.88        |
| -am    |     1.67%  |     1.92%   | 1.15        |
| -dy    |     5.29%  |     4.88%   | 0.92        |

### Clear section-shifting suffixes:
- **Recipe-heavy**: -edy (3.7x), -eey (2.9x), -ain (2.3x)
- **Herbal-heavy**: -y (0.51x), -or (0.49x), -an (0.36x)
- **Section-neutral**: -aiin, -am, -dy, -ar

### Verdict: PARTIALLY SUPPORTED
The dramatic shifts for -edy, -eey, and -ain between herbal and recipe sections are consistent with preparation/processing encoding. However, this could also reflect the confound with Currier languages (herbal sections are mostly Language A, recipe sections are mostly Language B).

---

## 6. Test: Suffixes = Grammatical Roles

### 6a. Suffix Bigrams (what follows what)

Top 10 most common suffix pairs:
1. -y -> -y: 775 (self-chaining)
2. -edy -> -edy: 527 (strong self-chaining)
3. -aiin -> -y: 479
4. -ol -> -ol: 396 (self-chaining)
5. -y -> -aiin: 366
6. -ey -> -y: 357
7. -ol -> -y: 336
8. -y -> -ol: 312
9. -y -> -ey: 282
10. -ey -> -ey: 279

**Key pattern: suffix self-chaining.** -edy, -ol, -y, -ey, and -eey all strongly chain with themselves. This is unusual for grammatical suffixes (you would not expect "noun noun noun" sequences) but natural for list-like structures (e.g., listing ingredients, plant features, or steps).

### Following-suffix profiles:
- **-aiin** is followed by: -y (21%), -aiin (12%), -ey (10%)
- **-ain** is followed by: -y (21%), -ey (14%), -edy (11%)
- **-edy** is followed by: -edy (23%), -ey (12%), -y (12%)
- **-ol** is followed by: -ol (19%), -y (16%), -aiin (13%)
- **-or** is followed by: -y (21%), -ol (15%), -or (13%)

The -edy suffix is the most self-associative (23% of next-words are also -edy), followed by -ol (19%) and -eey (15%).

### 6b. After daiin/dain (hypothesized "of" particle)

756 bigrams found. What follows daiin/dain:
- [no suffix]: 162 (21.4%)
- -y: 136 (18.0%)
- -ey: 70 (9.3%)
- -ol: 64 (8.5%)
- -aiin: 59 (7.8%)
- -edy: 42 (5.6%)

Top actual words: chey (21), shey (16), daiin (14), cthy (11), chedy (11), chckhy (10), ol (10)

**Key finding**: daiin is followed by -y words disproportionately (18% vs ~14% baseline). The most common post-daiin words are ch-ey, sh-ey (stem+ey pattern), suggesting -ey words may indeed serve as modifiers/adjectives after a particle.

### 6c. Common words BEFORE suffix types

- Before **-edy**: ol (58), shedy (54), qokeedy (53), qokedy (50), chedy (39) -- Note: heavily preceded by other -edy words (self-chaining) and by ol.
- Before **-ol**: chol (66), daiin (58), ol (31), shol (30) -- preceded by other -ol words and by daiin.
- Before **-y**: daiin (112), aiin (71), qokain (57) -- most commonly preceded by function words daiin and aiin.
- Before **-ar**: aiin (36), daiin (33), chey (27) -- preceded by function words.
- Before **-al**: aiin (38), chey (30), daiin (28) -- preceded by function words.

**Pattern**: -y, -ar, -al tend to be preceded by function words (daiin, aiin), suggesting they may serve as head nouns. -edy and -ol tend to be preceded by their own kind, suggesting list/chain behavior.

### 6d. Line-initial vs Line-final Position

| Suffix | Initial | Final | I/(I+F) |
|--------|---------|-------|---------|
| -or    |     421 |   118 | 0.781   |
| -eey   |     287 |    94 | 0.753   |
| -ol    |     470 |   190 | 0.712   |
| -edy   |     302 |   187 | 0.618   |
| -ar    |     393 |   247 | 0.614   |
| -ey    |     297 |   188 | 0.612   |
| -aiin  |     573 |   383 | 0.599   |
| -ain   |     233 |   167 | 0.583   |
| -al    |     199 |   294 | 0.404   |
| -dy    |     254 |   388 | 0.396   |
| -y     |     640 | 1,232 | 0.342   |
| -an    |      12 |    44 | 0.214   |
| -am    |      55 |   471 | 0.105   |

**Dramatic finding**: suffixes split cleanly into line-initial and line-final groups.

**Line-initial** (beginning of clauses/sentences): -or (78%), -eey (75%), -ol (71%)
**Line-final** (end of clauses/sentences): -am (90% final!), -an (79% final), -y (66% final), -dy (60% final)

This is strong evidence for grammatical function:
- **-am/-an** as sentence/clause terminators (end markers or final particles)
- **-or/-ol/-eey** as sentence/clause openers (topic markers or initial particles)
- **-y/-dy** as clause-final elements (possibly verb forms or predicate markers)

### 6e. Adjective+Noun Hypothesis (-ey/-y before -ol/-or)

- -ey/-y followed by -ol/-or: 747/5,468 = 13.7%
- Baseline rate of -ol/-or in corpus: 11.8%
- Slight elevation but not dramatic enough to confirm adj+noun pattern.

### Verdict: PARTIALLY SUPPORTED
The line-position data provides the strongest grammatical signal. -am is almost exclusively line-final (90%), while -or is predominantly line-initial (78%). This suggests genuine syntactic roles. The self-chaining behavior of -edy and -ol is consistent with list/enumeration structures rather than strict SVO grammar.

---

## 7. A/B Scribe (Currier Language) Suffix Mapping

### Language Distribution

| Suffix | Lang A | A% | Lang B | B% | Shift |
|--------|--------|-----|--------|-----|-------|
| -aiin  |  1,140 | 13.6% | 2,010 | 10.5% | -3.1% |
| -ol    |  1,448 | 17.3% | 1,256 |  6.6% | -10.7% *** |
| -or    |  1,004 | 12.0% |   619 |  3.2% | -8.7% *** |
| -y     |  1,961 | 23.4% | 2,861 | 15.0% | -8.4% *** |
| -edy   |     20 |  0.2% | 2,745 | 14.4% | +14.1% *** |
| -ey    |    551 |  6.6% | 2,199 | 11.5% | +4.9% *** |
| -eey   |    396 |  4.7% | 1,626 |  8.5% | +3.8% *** |
| -ain   |    221 |  2.6% | 1,275 |  6.7% | +4.0% *** |
| -ar    |    471 |  5.6% | 1,682 |  8.8% | +3.2% *** |
| -al    |    382 |  4.6% | 1,196 |  6.3% | +1.7% |
| -dy    |    560 |  6.7% | 1,200 |  6.3% | -0.4% |
| -am    |    175 |  2.1% |   413 |  2.2% | +0.1% |
| -an    |     61 |  0.7% |    44 |  0.2% | -0.5% |

### The A/B Suffix Divide

The most extreme shifts:

**Language A preferences (herbal-dominant):**
- -ol: 17.3% in A vs 6.6% in B (-10.7 point drop)
- -or: 12.0% vs 3.2% (-8.7 points)
- -y: 23.4% vs 15.0% (-8.4 points)

**Language B preferences (recipe/bio-dominant):**
- -edy: 0.2% in A vs 14.4% in B (+14.1 points!) -- virtually absent from A
- -ey: 6.6% vs 11.5% (+4.9 points)
- -ain: 2.6% vs 6.7% (+4.0 points)
- -eey: 4.7% vs 8.5% (+3.8 points)

**Neutral (both languages):**
- -dy: 6.7% vs 6.3% (essentially identical)
- -am: 2.1% vs 2.2% (essentially identical)

### 7c/7d. Testing 1:1 Mapping Hypothesis

Hypothesis: -ol(A) maps to -edy(B), -or(A) maps to -eey(B), etc.

**Stem overlap test:**
- -ol(A) <-> -edy(B): 263 A-stems, 357 B-stems, **110 shared** (42% of A-stems)
- -or(A) <-> -eey(B): 215 A-stems, 236 B-stems, **74 shared** (34%)
- -al(A) <-> -dy(B): 147 A-stems, 411 B-stems, **41 shared** (28%)
- -ar(A) <-> -y(B): 171 A-stems, 876 B-stems, **78 shared** (46%)

Substantial overlap exists, but the cross-language suffix distributions for shared stems show NO preferential mapping. When -ol stems from Language A appear in Language B, their B suffixes are:
- -edy: 2,247 (not dominant -- it ranks #1 but only because -edy is the most common B suffix overall)
- -ey: 1,711
- -aiin: 1,483
- -y: 1,418
- -eey: 1,296

The distribution is broad, not concentrated on -edy as the mapping hypothesis would predict.

### Detailed stem evidence:

The stem `ch` (the most common) shows:
- In A: -or=175, -ol=255, -ey=82, -y=106
- In B: -ey=397, -edy=324, -eey=136, -dy=92, -ol=95, -y=97

`qoke` (an extreme case):
- In A: -ol=33, -or=11, -eey=3 (only 49 A tokens)
- In B: -edy=222, -ol=15, -eey=25 (290 B tokens)

Here qoke shows -ol(A) -> -edy(B) quite clearly. But for most stems, the mapping is much messier.

### Verdict: COMPLEX REALITY

The A/B suffix divide is real and dramatic. -edy is essentially a Language B creation (0.2% -> 14.4%). -ol and -or are Language A features that survive in reduced form in B. However, a clean 1:1 mapping (ol=edy, or=eey) is NOT supported. Instead:

1. Some stems (like qoke) do show clear mapping
2. Most stems show broad suffix redistribution across languages
3. -dy and -am are language-neutral, suggesting they encode something independent of the A/B orthographic system

---

## 8. Suffix Flexibility Analysis

### Key finding: extreme suffix promiscuity

- Average suffix diversity for stems with >=5 tokens: **5.6 different suffixes**
- The top 7 stems each accept ALL 13 suffixes
- Even highly-specialized stems like `q` (80% -ol) still accept 7 suffixes

### Dominance patterns:

| Stem | Dominant suffix | Dominance % | Total tokens |
|------|----------------|-------------|-------------|
| q    | -ol            | 80%         | 173         |
| chckh | -y            | 69%         | 201         |
| qoke | -edy           | 65%         | 339         |
| d    | -aiin          | 40%         | 1,779       |
| che  | -ol            | 36%         | 426         |
| she  | -ol            | 38%         | 248         |
| lch  | -edy           | 38%         | 212         |
| ch   | -ey            | 23%         | 2,135       |

The most common stems show dominance of only 14-23%, meaning the suffix is more like a variable modifier than a fixed inflection.

---

## Synthesis: What Do the Suffixes Actually Encode?

### Evidence summary by hypothesis:

| Hypothesis | Section dist | Position | Plant parts | Prep methods | Grammar | A/B scribe |
|------------|-------------|----------|-------------|-------------|---------|-----------|
| Plant parts | Mixed | Weak | Partial | N/A | N/A | N/A |
| Preparation | Partial | Weak | N/A | Partial | N/A | Confounded |
| Grammar | Mixed | Weak | N/A | N/A | **Strong** | Mixed |
| Orthographic variant | N/A | N/A | N/A | N/A | N/A | **Strong** |

### Conclusions:

**1. The suffixes encode AT LEAST two independent dimensions simultaneously:**

**Dimension 1: Syntactic position (grammatical).**
The line-position data is the strongest signal in the entire analysis. -am is a line-terminator (90% final), -or/-ol are line-openers (78%/71% initial), -y is clause-final (66% final). This is a genuine grammatical signal that operates ACROSS both languages and all sections.

**Functional grouping by syntactic role:**
- **Clause-initial**: -or, -eey, -ol, -edy, -ar, -ey, -aiin
- **Clause-final**: -am, -an, -y, -dy, -al

**Dimension 2: Orthographic dialect (Currier language).**
The A/B split accounts for most of the section distribution findings, since sections correlate with language. The mapping is NOT 1:1 but follows a pattern where:
- Language A uses: -ol, -or, -y (and -an) heavily
- Language B uses: -edy, -eey, -ey, -ain heavily
- Both use: -dy, -am, -aiin, -ar at similar rates

The language-neutral suffixes (-dy, -am, -aiin) likely represent shared core grammatical elements, while the language-specific suffixes represent dialect variation in encoding the same underlying concepts.

**2. What suffixes are NOT:**
- They are not purely plant-part markers (illustration correlation is weak)
- They are not purely preparation-method markers (section shifts are confounded with language)
- They are not 1:1 orthographic variants between scribes (the mapping is too messy)

**3. Most likely interpretation:**
The Voynich suffix system is a **hybrid grammatical-semantic encoding** where:
- The final consonant cluster (-m, -n, -r, -l, -y) encodes syntactic role (sentence position)
- The vowel pattern before the consonant (-o-, -a-, -e-, -ee-, -ai-) encodes something else, possibly semantic class or phonological information
- The Currier Language A/B difference reflects genuine dialectal or scribal variation in how vowel patterns are written, but the consonantal endings remain functionally equivalent across both systems

This explains why -am and -dy are language-neutral (the grammatical ending is what matters), while -ol vs -edy and -or vs -eey differ (the vowel encoding varies by scribe).

**4. The -am puzzle:**
-am stands out as the most positionally constrained suffix (90% line-final) and the most section-neutral and language-neutral. It likely functions as a sentence/clause terminator or period-equivalent. Its frequency (644) is much lower than other suffixes, consistent with a structural marker appearing once per clause rather than on every content word.
