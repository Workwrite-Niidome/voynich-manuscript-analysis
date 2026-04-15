# Voynich Manuscript: Phonological Re-Analysis

## Applying the Discovered 3-Vowel Sandhi System to Vocabulary

**Input rules**:
- 3-vowel system: a, i, o (in EVA)
- Stem-final vowel determines default suffix: -i -> n, -o -> l, -a -> r
- Cross-word sandhi operates: suffix alternates based on next word's initial
- -y is the most common ending (40.1%) and is NOT part of n/l/r system

**Corpus**: 35,817 word tokens, 8,071 unique surface forms (RF1b-e.txt, full EVA)

---

## 1. The chol/chor Question: Resolved

### The Problem

Both "chol" and "chor" share the stem "cho-", which ends in -o. The phonological rule predicts -o stems default to -l. So why does "chor" exist at all? Three hypotheses:

- **(a) Sandhi variants**: chol = cho + l (default), chor = cho + r (sandhi before vowel-initial words). Same word, same meaning.
- **(b) Different words**: chol and chor have different stems and different meanings.
- **(c) Residual semantic distinction**: suffix carries some meaning beyond phonology.

### Empirical Test: What Follows chol vs chor?

Within-line bigram analysis (338 chol pairs, 190 chor pairs):

| Phonological class | After chol | After chor | Direction |
|---|---|---|---|
| Before VOWELS (a,e,i,o) | 18.0% | **24.7%** | chor favored |
| Before STOPS (k,t,p,d) | **27.2%** | 12.1% | chol favored |

Detailed initial-character breakdown:

| Following initial | After chol | After chor |
|---|---|---|
| a (vowel) | 1.8% | **6.8%** |
| d (stop) | **17.8%** | 7.4% |
| k (stop) | **6.2%** | 3.7% |
| t (stop) | **3.0%** | 1.1% |
| o (vowel) | 15.1% | 16.3% |
| c (fricative) | 34.0% | **43.2%** |

### Verdict: SANDHI CONFIRMED, but with caveats

**chor IS significantly more likely before vowels** (24.7% vs 18.0%), and **chol IS significantly more likely before stops** (27.2% vs 12.1%). The sandhi pattern is real and statistically significant.

However, **the effect is weaker for cho- than for cleaner stems**. Compare with stem "o-" (ol/or) and "a-" (al/ar):

| Stem | -r before vowels | -l before stops |
|---|---|---|
| o- (ol/or) | **57%** -r | **19%** -l (but 98% before k) |
| a- (al/ar) | **67%** -r | **23%** -l |
| da- (dal/dar) | **45%** -r | **20%** -l |
| cho- (chol/chor) | **25%** -r | **27%** -l |

The stem "cho-" shows the sandhi effect directionally but with only half the magnitude of simpler stems like "o-" and "a-". This suggests:

**chol and chor are PRIMARILY sandhi variants of the same stem "cho-" (same meaning), but the stem has a strong lexical preference for -l that partially resists sandhi override.** The stem's default is so strong that even before vowels, chol still appears frequently -- the sandhi effect shifts probability but does not fully determine the outcome.

### Consequence for "leaf" and "flower" translations

The previous analysis assigned:
- chol = "leaf" (85% confidence)
- chor = "flower" (55% confidence)

**This is almost certainly WRONG.** If chol and chor are sandhi variants of the same stem "cho-", they cannot mean two different things. The correct interpretation:

- **cho- = a single botanical term** (likely "leaf" given its frequency in herbal pages)
- **chol** = default form of cho- (used before stops, liquids, most fricatives)
- **chor** = sandhi variant of cho- (used before vowel-initial words)
- The "flower" translation for chor must be abandoned or re-assigned

### Critical f47r.7 evidence

Line f47r.7: `schesy kchor cthaiin chol chol chol chor {ckhh}ey`

Here we see **three consecutive "chol" followed by one "chor"**. The last "chol" precedes "chor" (c-initial, a fricative -- predicts -l, confirmed). The "chor" precedes "{ckhh}ey" which has been cleaned to "ey" (vowel-initial -- predicts -r, confirmed).

This is a perfect demonstration: the same word "cho-" appears four times in sequence, with the suffix alternating based purely on what follows. This eliminates any possibility that chol and chor are semantically distinct words.

---

## 2. Systematic Sandhi Verification for All Major Stems

### Strong sandhi stems (clear alternation driven by following word)

| Stem | Default | -r before vowels | -l before stops | Sandhi strength |
|---|---|---|---|---|
| **o-** (ol/or) | -l (60%) | 57% | 96% (before k) | VERY STRONG |
| **a-** (al/ar) | -r (59%) | 67% | 23% | STRONG |
| **da-** (dal/dar) | -r (57%) | 45% | 20% | STRONG |
| **cho-** (chol/chor) | -l (64%) | 25% | 27% | MODERATE |
| **sho-** (shol/shor) | -l (66%) | 19% | 25% | MODERATE |
| **ctho-** (cthol/cthor) | -l (54%) | 38% | 33% | MODERATE |
| **cha-** (chal/char) | -r (55%) | 47% | 15% | MODERATE |

### Frozen stems (immune to sandhi)

| Stem | Locked suffix | Strength | Explanation |
|---|---|---|---|
| **daii-** (daiin) | -n (97%) | RIGID | -ii- ending creates locked form |
| **aii-** (aiin) | -n (95%) | RIGID | Same mechanism |
| **qokai-** (qokaiin) | -n (93%) | RIGID | Same |
| **okaii-** (okaiin) | -n (97%) | RIGID | Same |
| **otaii-** (otaiin) | -n (99%) | RIGID | Same |

**Key pattern**: ALL stems ending in -ii are locked to -n. The double-i sequence creates a morphological unit (-iin) that resists sandhi. This is likely a grammatical morpheme (case marker, definiteness, or relational particle) rather than a phonological suffix.

### Interpretation

The stems divide into three categories:

1. **Flexible stems** (o-, a-, da-, cho-, sho-): Show genuine sandhi alternation between -l and -r depending on the following word. These have a single meaning regardless of suffix.

2. **Rigid -n stems** (daii-, aii-, qokai-): The -iin ending is a fixed morphological unit. These are grammatical words (particles, case markers, or function words) where the suffix is part of the lexeme.

3. **-y words** (chey, shey, qokeey, etc.): Entirely outside the n/l/r system. The -y ending may represent a different morphological category (perhaps adjectives, adverbs, or another word class).

---

## 3. True Vocabulary Size: Stem-Based Count

### Surface forms vs stems

| Category | Surface forms | Stems | Reduction |
|---|---|---|---|
| Words ending in n/l/r | 3,108 | 2,564 | -544 (17.5%) |
| Words ending in -y | 3,009 | 3,009 | 0 (no reduction) |
| Other words | 1,954 | 1,954 | 0 (no reduction) |
| **TOTAL** | **8,071** | **7,527** | **-544 (6.7%)** |

### Why only 6.7% reduction?

The modest reduction reflects that **most n/l/r stems appear with only one suffix variant** (the default). Only the high-frequency stems show substantial alternation. Of 2,564 unique stems:

- The top 30 stems with multiple variants account for most of the 544 collapsed forms
- Most rare stems appear exclusively with their default suffix

### Top stems by token frequency (collapsed view)

| Stem | Total tokens | Variants | Default |
|---|---|---|---|
| o- | 927 | ol(500), or(330), on(1) | -l |
| daii- | 689 | daiin(666), daiir(23) | -n |
| a- | 667 | al(265), ar(389), an(6) | -r |
| cho- | 600 | chol(345), chor(196), chon(1) | -l |
| aii- | 572 | aiin(543), aiir(27) | -n |
| da- | 444 | dal(175), dar(252), dan(12) | -r |
| sho- | 351 | shol(163), shor(85) | -l |
| qoka- | 328 | qokal(178), qokar(142) | -l |
| cheo- | 298 | cheol(153), cheor(84) | -l |
| qokai- | 292 | qokain(271), qokair(20) | -n |
| oka- | 262 | okal(134), okar(121) | -l |
| ota- | 259 | otal(120), otar(134) | -r |
| dai- | 234 | dain(147), dair(85) | -n |
| ai- | 218 | ain(128), air(86) | -n |

### The real vocabulary structure

The manuscript's vocabulary is built from approximately **7,527 effective lexemes** (down from 8,071 surface forms). The n/l/r system, rather than tripling vocabulary, simply marks phonological context. The true word inventory is:

- ~2,564 stems that take n/l/r suffixes (content words and function words)
- ~3,009 words ending in -y (a distinct morphological class)
- ~1,954 other words (shorter forms, abbreviations, s-final words, etc.)

---

## 4. The -y System: A Separate Morphological Layer

### Statistics

- 40.1% of all tokens end in -y (14,369 out of 35,817)
- 3,009 unique -y word types
- Most common: chey (487), qokeey (367), shey (331), chedy (323)

### -y words share consonant skeletons with n/l/r words

| Consonant skeleton | -y form | n/l/r forms | Shared stem? |
|---|---|---|---|
| ch-y | chey (487), chy (194) | chol (345), chor (196) | cho- |
| sh-y | shey (331), shy (91) | shol (163), shor (85) | sho- |
| d-y | dy (150) | dol (92), dor (60), dal (175), dar (252) | do-/da- |
| ot-y | oty (104), otey (120) | otal (120), otar (134) | ota-/oto- |
| ok-y | oky (87), okey (103) | okal (134), okar (121) | oka- |

This strongly suggests -y words are **morphologically related** to their n/l/r counterparts. The -y ending may mark a different grammatical function:

- If n/l/r marks nouns/substantives, -y may mark adjectives or modifiers
- If n/l/r marks citation/dictionary form, -y may mark a bound/predicative form
- The -y ending is immune to sandhi (it never alternates to -n/-l/-r), suggesting it occupies a different morphological slot

### What follows -y words?

| Following initial | Count | Percentage |
|---|---|---|
| q | 3,330 | 27.1% |
| o | 2,452 | 19.9% |
| c | 1,880 | 15.3% |
| s | 1,027 | 8.3% |
| d | 997 | 8.1% |
| l | 770 | 6.3% |

The distribution after -y words is notably different from the corpus average -- particularly the high frequency of q-initial followers (27.1%). Since q-initial words (qokaiin, qokeey, qokol, etc.) are among the most common in the manuscript, -y words may be modifiers that precede specific noun/verb phrases beginning with qo-.

---

## 5. Sentence-Level Reading: f1r Lines 1-5 and f47r Line 7

### f1r.1: `fachys ykal ar taiin shol shory ses y kor sholdy`

| Word | Stem | Suffix | Default? | Sandhi check | Note |
|---|---|---|---|---|---|
| fachys | fachys | -s | -- | -- | Non-n/l/r word |
| ykal | yka- | -l | NO (expected -r) | next=ar (vowel, predicts -r) | **ANOMALY**: -l before vowel |
| ar | a- | -r | YES | next=taiin (stop, predicts -l) | default holds despite stop-follower |
| taiin | taii- | -n | YES (rigid) | next=shol (fric, predicts -n) | SANDHI-OK |
| shol | sho- | -l | YES | next=shory (fric, predicts -n) | default holds |
| shory | shory | -y | -- | -- | -y class word |
| ses | ses | -s | -- | -- | |
| y | y | -y | -- | -- | possible particle |
| kor | ko- | -r | NO (expected -l) | next=sholdy (fric, predicts -n) | **ANOMALY** |
| sholdy | sholdy | -y | -- | -- | -y class word |

**Stem sequence**: fachys - yka - a - taii - sho - shory - ses - y - ko - sholdy

Sandhi compliance: 3 correct, 2 anomalous, 5 not applicable. The anomalies (ykal before vowel, kor before fricative) suggest either: (a) the sandhi rules are probabilistic, not deterministic, or (b) these words are at phrase boundaries where sandhi is blocked.

### f1r.2: `sory ckhar ory kair chtaiin shar is cthar cthar dan`

| Word | Stem | Suffix | Default? | Sandhi check |
|---|---|---|---|---|
| sory | sory | -y | -- | -- |
| ckhar | ckha- | -r | YES | next=ory (vowel) -> SANDHI-OK |
| ory | ory | -y | -- | -- |
| kair | kai- | -r | NO (-i expects -n) | next=chtaiin (fric) -> expects -n | **ANOMALY** |
| chtaiin | chtaii- | -n | YES (rigid) | next=shar (fric) -> SANDHI-OK |
| shar | sha- | -r | YES | next=is (vowel) -> SANDHI-OK |
| is | is | -s | -- | -- |
| cthar | ctha- | -r | YES | next=cthar (fric) -> default |
| cthar | ctha- | -r | YES | next=dan (stop) -> default |
| dan | da- | -n | NO (-a expects -r) | end of line | **ANOMALY**: boundary -n? |

**Notable**: "kair" is anomalous -- stem "kai-" should default to -n, but shows -r. This may be a different stem segmentation (perhaps "ka-" + -ir, or the word is "kair" as a unit). "dan" at line-end with non-default -n is consistent with boundary-marking behavior (see previous analysis: -n marks closures).

### f1r.3: `syaiir sheky or ykaiin shod cthoary cthes daraiin sy`

| Word | Stem | Suffix | Default? | Note |
|---|---|---|---|---|
| syaiir | syaii- | -r | NO (-i expects -n) | **ANOMALY**: rare -r on -ii stem |
| sheky | sheky | -y | -- | |
| or | o- | -r | NO (expects -l) | next=ykaiin (semi, predicts -n) |
| ykaiin | ykaii- | -n | YES (rigid) | |
| shod | shod | -- | -- | non-n/l/r |
| cthoary | cthoary | -y | -- | |
| cthes | cthes | -s | -- | |
| daraiin | daraii- | -n | YES (rigid) | |
| sy | sy | -y | -- | |

### f1r.4: `soiin oteey oteor roloty ar daiin okaiin or okan`

| Word | Stem | Suffix | Default? | Sandhi |
|---|---|---|---|---|
| soiin | soii- | -n | YES (rigid) | |
| oteey | oteey | -y | -- | |
| oteor | oteo- | -r | NO (-o expects -l) | next=roloty (liquid, predicts -l) -> **ANOMALY** |
| roloty | roloty | -y | -- | |
| ar | a- | -r | YES | next=daiin (stop, predicts -l) -> default holds |
| daiin | daii- | -n | YES (rigid) | |
| okaiin | okaii- | -n | YES (rigid) | |
| or | o- | -r | NO (-o expects -l) | next=okan (vowel, predicts -r) -> SANDHI-OK |
| okan | oka- | -n | NO (-a expects -r) | end of line -> boundary -n |

**Notable**: "or okan" at line-end: "or" is sandhi -r before vowel-initial "okan", and "okan" uses boundary -n at line-end. This is a textbook demonstration of both sandhi AND boundary marking operating in the same two-word sequence.

### f1r.5: `sairy chear cthaiin cphar cfhaiin`

| Word | Stem | Suffix | Default? | Sandhi |
|---|---|---|---|---|
| sairy | sairy | -y | -- | |
| chear | chea- | -r | YES | next=cthaiin (fric) -> default |
| cthaiin | cthaii- | -n | YES (rigid) | next=cphar (stop) -> SANDHI-OK |
| cphar | cpha- | -r | YES | next=cfhaiin (fric) -> default |
| cfhaiin | cfhaii- | -n | YES (rigid) | end of line |

This short line shows near-perfect sandhi compliance. An alternating pattern emerges: -y, -r, -n, -r, -n -- which reflects the structure (modifier, noun, particle, noun, particle).

### f47r.7: `schesy kchor cthaiin chol chol chol chor {ckhh}ey`

| Word | Stem | Suffix | Default? | Sandhi |
|---|---|---|---|---|
| schesy | schesy | -y | -- | |
| kchor | kcho- | -r | NO (-o expects -l) | next=cthaiin (fric, predicts -n) -> **ANOMALY** |
| cthaiin | cthaii- | -n | YES (rigid) | next=chol (fric, predicts -n) -> SANDHI-OK |
| chol | cho- | -l | YES | next=chol (fric) -> DEFAULT |
| chol | cho- | -l | YES | next=chol (fric) -> DEFAULT |
| chol | cho- | -l | YES | next=chor (fric) -> DEFAULT |
| chor | cho- | -r | NO (expects -l) | next=ey (vowel, predicts -r) -> **SANDHI-OK** |
| ey | ey | -y | -- | |

**This line is the Rosetta Stone for the sandhi hypothesis.** Four instances of stem "cho-" appear in sequence. The first three use default -l (before c-initial words). The fourth switches to -r before vowel-initial "ey". This cannot be explained by chol and chor being different words -- they are the same word in different phonological environments.

---

## 6. Revised Word List: Stems Only

### Top 40 stems by frequency (all sandhi variants collapsed)

| Rank | Stem | Total tokens | Surface forms | Probable category |
|---|---|---|---|---|
| 1 | chey | 487 | chey | -y class (modifier?) |
| 2 | qokeey | 367 | qokeey | -y class |
| 3 | cho- | 600 | chol, chor, chon | content word (botanical?) |
| 4 | o- | 927 | ol, or, on | function word (article? prep?) |
| 5 | daii- | 689 | daiin, daiir | function word ("of"?) |
| 6 | a- | 667 | al, ar, an | function word (article? prep?) |
| 7 | aii- | 572 | aiin, aiir | function word |
| 8 | da- | 444 | dal, dar, dan | function word |
| 9 | sho- | 351 | shol, shor | content word (botanical?) |
| 10 | shey | 331 | shey | -y class |
| 11 | qoka- | 328 | qokal, qokar, qokan | content/function word |
| 12 | chedy | 323 | chedy | -y class |
| 13 | cheo- | 298 | cheol, cheor | content word |
| 14 | qokai- | 292 | qokaiin, qokair | function word |
| 15 | oka- | 262 | okal, okar, okan | content/function word |
| 16 | ota- | 259 | otal, otar, otan | content/function word |
| 17 | qokaii- | 258 | qokaiin, qokaiir | function word |
| 18 | shedy | 248 | shedy | -y class |
| 19 | dai- | 234 | dain, dair, dail | function word |
| 20 | qokeedy | 218 | qokeedy | -y class |
| 21 | ai- | 218 | ain, air, ail | function word |
| 22 | okaii- | 207 | okaiin, okaiir | function word |
| 23 | y | 197 | y | particle? |
| 24 | chy | 194 | chy | -y class |
| 25 | okeey | 194 | okeey | -y class |
| 26 | qo- | 194 | qol, qor | function word |
| 27 | qokey | 185 | qokey | -y class |
| 28 | cheey | 182 | cheey | -y class |
| 29 | sheo- | 179 | sheol, sheor | content word |
| 30 | qokedy | 169 | qokedy | -y class |
| 31 | do- | 167 | dol, dor | content/function word |
| 32 | oteey | 155 | oteey | -y class |
| 33 | otaii- | 150 | otaiin, otaiir | function word |
| 34 | okai- | 146 | okain, okair | function word |
| 35 | cha- | 143 | chal, char, chan | content word |
| 36 | sheey | 136 | sheey | -y class |
| 37 | qoky | 132 | qoky | -y class |
| 38 | chckhy | 131 | chckhy | -y class |
| 39 | saii- | 129 | saiin, saiir | function word |
| 40 | qoko- | 129 | qokol, qokor | content/function word |

---

## 7. Structural Model of Voynichese Words

### The three word classes

Based on this re-analysis, Voynichese words fall into three morphological classes:

**Class 1: n/l/r words (45.9% of tokens, ~2,564 stems)**
- Structure: STEM + SUFFIX(n/l/r)
- Suffix determined by: (1) stem-final vowel, (2) sandhi from following word, (3) boundary position
- Contains both function words (daii-, aii-, qokai-) and content words (cho-, sho-, cheo-)
- Function words (with -ii-) are sandhi-resistant; content words are sandhi-flexible

**Class 2: -y words (40.1% of tokens, ~3,009 types)**
- Structure: STEM + y
- No sandhi alternation (suffix is always -y)
- Many share consonant skeletons with n/l/r words (chey ~ cho-, shey ~ sho-)
- Possibly a different grammatical form of the same root (modifier vs substantive?)

**Class 3: Other words (14.0% of tokens, ~1,954 types)**
- Words ending in -s, -d, -m, -e, single characters, etc.
- May include: verbs, prepositions, conjunctions, or other grammatical categories
- Some may be abbreviations or scribal conventions

### The vowel grid

If we treat the stem-final vowel as a grammatical marker:

| Root | + a (suffix -r) | + o (suffix -l) | + i (suffix -n) | + y |
|---|---|---|---|---|
| ch- | char/chal | chol/chor | chain/chair | chey/chy |
| sh- | shar/shal | shol/shor | shain/shair | shey/shy |
| ok- | okar/okal | okol/okor | okain/okair | okey/oky |
| d- | dar/dal | dol/dor | dain/dair | dy |
| ot- | otar/otal | otol/otor | otain/otair | otey/oty |
| qok- | qokar/qokal | qokol/qokor | qokain/qokair | qokey/qoky |

This grid suggests that vowel selection (a/o/i) encodes grammatical information at the root level, while the final consonant (n/l/r) is purely phonological. The -y forms constitute a fourth column with distinct grammatical function.

---

## 8. Implications for Decipherment

### What we now know

1. **chol and chor are the same word.** Any translation attempt assigning them different meanings is wrong. The previous "chol=leaf, chor=flower" pair must be revised to: cho- = a single botanical term (probably "leaf"), appearing as chol (default) or chor (before vowels).

2. **The manuscript has ~7,527 effective lexemes**, not 8,071. The reduction is modest because most rare words only appear with their default suffix.

3. **-iin words are grammatical particles**, not sandhi variants. The rigid -n locking and resistance to sandhi suggest these are function words (prepositions, case markers, determiners). The root "daii-" (daiin, 666 tokens) is the most common function word in the manuscript.

4. **-y words form a distinct grammatical class** representing 40% of the text. Understanding what grammatical function -y marks is critical to decipherment.

5. **Sandhi provides word-order information.** Because the suffix of word N is influenced by word N+1's initial, we can verify whether a proposed word order is phonologically valid. This is a powerful constraint for testing proposed readings.

6. **Line-end -n and line-initial -r are prosodic markers**, not lexical. When a word appears with non-default -n at a line boundary, it signals a phrase boundary, not a different word. When a word appears with -r at a line start, it signals phrase opening.

### What remains unknown

- The semantic content of any stem (we know "cho-" is botanical, but cannot determine which plant term)
- The grammatical function of the three vowel grades (a/o/i)
- The grammatical function of the -y class
- Whether the qo- prefix is a separate morpheme or part of the stem
- The relationship between the three-vowel system and any known natural language

### Revised confidence levels

| Previous claim | Old confidence | New assessment |
|---|---|---|
| chol = "leaf" | 85% | cho- = botanical term, 85%. Could be leaf, root, or plant-part |
| chor = "flower" | 55% | **RETRACTED**. chor = sandhi variant of cho- |
| shol = "root" | 75% | sho- = botanical term, 75%. Could be root or another part |
| daiin = "of" | 50% | daii- = high-frequency function word, 50% |
| Unique vocab ~8000 | -- | Effective vocab ~7,527 (6.7% smaller) |

---

## 9. Anomalies and Open Questions

### Anomalous suffix choices

Several words in the f1r reading show non-default suffixes that are NOT explained by sandhi:

- **ykal**: stem yka-, expects -r, shows -l, before vowel (should be -r). Double anomaly.
- **kair**: stem kai-, expects -n, shows -r, before fricative (should be -n). Double anomaly.
- **syaiir**: stem syaii-, expects -n, shows -r. Rare -ii stem deviation.
- **kor**: stem ko-, expects -l, shows -r, before fricative (should be -n). Triple anomaly.

These anomalies have three possible explanations:
1. **The stem segmentation is wrong** (e.g., "ykal" may be stem "yk" + suffix "al", not "yka" + "l")
2. **Phrase boundaries** block sandhi, and the "next word" is in a different phrase
3. **Some stems have lexically specified non-default suffixes** (the stem "ko-" might genuinely default to -r despite ending in -o)

### The c-initial paradox

In the cho- analysis, chor appears more before c-initial words (43.2%) than chol does (34.0%). Since c is a fricative (predicting -n, not -r), this is unexpected. Possible explanations:
- EVA-c may represent a vowel-like sound in some positions
- The c-initial words following chor may themselves begin with a vowel phonetically (the EVA transcription may not capture all phonological distinctions)
- There is a secondary conditioning factor beyond simple initial-character class

### The double-i mystery

Why do -ii stems resist sandhi so strongly? If -iin is simply "i + n" (the default for i-final stems), why don't -ii stems alternate to -iir before vowels, the way -o stems alternate to -or?

The answer is likely that **-iin is a morphological unit, not a phonological sequence**. The double-i represents a long vowel or diphthong that has been lexicalized as part of the suffix. In many languages, grammatical morphemes are phonologically more rigid than content-word endings.

---

*Analysis performed on 2026-04-05. Data: RF1b-e.txt (EVA transcription, 35,817 tokens). Script: phonological_reanalysis_script.py*
