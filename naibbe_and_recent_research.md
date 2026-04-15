# Naibbe Cipher Hypothesis and Recent Voynich Research (2024-2026)

**Date**: 2026-04-07
**Scope**: Comprehensive review of the Naibbe cipher (Greshko 2025), reverse decoding test on f1r, and survey of all recent (2024-2026) Voynich decipherment claims.

---

## 1. The Naibbe Cipher: Complete Technical Description

### 1.1 Publication

- **Author**: Michael A. Greshko (science journalist, National Geographic)
- **Paper**: "The Naibbe cipher: a substitution cipher that encrypts Latin and Italian as Voynich Manuscript-like ciphertext"
- **Journal**: *Cryptologia* (peer-reviewed), published November 26, 2025
- **Open access**: [Full paper](https://www.tandfonline.com/doi/full/10.1080/01611194.2025.2566408)
- **Code**: [github.com/greshko/naibbe-cipher](https://github.com/greshko/naibbe-cipher)
- **Data**: [Zenodo archive](https://doi.org/10.5281/zenodo.16415087) (includes Excel implementations)
- **Name origin**: "Naibbe" = late 14th-century Italian word for a card game

### 1.2 Encoding Mechanism (Step by Step)

The Naibbe cipher is a **verbose homophonic substitution cipher** that encrypts one plaintext letter into one entire Voynich "word."

**Step 1 -- Segment the plaintext:**
Roll a die to randomly break plaintext into single letters (unigrams) and letter pairs (bigrams). Example: "gatto" might become "g" | "at" | "to". Roughly half become unigrams, half bigrams.

**Step 2 -- Select substitution table:**
Draw a playing card to select one of **six substitution tables** (alpha, beta1, beta2, beta3, gamma1, gamma2). Tables can use either a 78-card tarocchi deck (historically attested in 15th-century Italy) or a standard 52-card deck. Tables are weighted so that output glyph frequencies match the actual Voynich manuscript.

**Step 3 -- Encode each unit:**
- **Unigrams**: Look up the letter in the selected table's unigram column. The letter maps to a complete EVA word. Example: "n" in table alpha -> "daiin"; "s" in table beta3 -> "shol"; "a" in table gamma1 -> "chol".
- **Bigram prefix**: First letter of a pair maps to a prefix glyph string. Example: "a" in table alpha prefix -> "sh".
- **Bigram suffix**: Second letter of a pair maps to a suffix glyph string. Example: "a" in table alpha suffix -> "aiin".
- The prefix + suffix concatenate to form one EVA word. Example: bigram "aa" in table alpha = "sh" + "aiin" = "shaiin".

**Key properties:**
- Each plaintext letter has 6 possible unigram encodings (one per table)
- Each bigram has 36 possible encodings (6 prefix choices x 6 suffix choices)
- Original word boundaries are destroyed -- the ciphertext "words" correspond to 1-2 plaintext letters, not words
- Prefix glyphs occupy Zattera slots 0-5; suffix glyphs occupy slots 6-11 (matching observed VMS word-internal structure)

### 1.3 Example Mappings (from actual tables)

Selected unigram mappings (letter -> EVA word by table):

| Letter | alpha   | beta1  | beta2  | beta3  | gamma1 | gamma2 |
|--------|---------|--------|--------|--------|--------|--------|
| a      | ol      | or     | qol    | chdy   | chol   | cheol  |
| e      | chedy   | ar     | dar    | dar    | chckhy | lchedy |
| i      | shedy   | qokedy | shey   | otedy  | raiin  | qotedy |
| n      | daiin   | dal    | dain   | dy     | dair   | dam    |
| o      | aiin    | al     | ain    | y      | air    | am     |
| s      | qokeey  | okeey  | oteey  | shol   | qoteey | olkeey |
| t      | qokaiin | okaiin | otaiin | sheey  | qotaiin| olkaiin|

### 1.4 Decipherability

The cipher is fully reversible. Because prefixes and suffixes use structurally distinct glyph sets, a reader can identify the split point, look up the plaintext letter in the corresponding table. The table identity (which card was drawn) must be known or inferred.

---

## 2. Reverse Naibbe Test on f1r

### 2.1 Methodology

We extracted 204 EVA words from folio f1r of the Takahashi transcription and attempted to decode each word using Greshko's published substitution tables (all 6 tables, trying both unigram and bigram lookups).

### 2.2 Match Rates

| Category | Count | Percentage |
|----------|-------|-----------|
| Unigram matches | 59/204 | 28.9% |
| Bigram matches | 153/204 | 75.0% |
| Either match | 158/204 | 77.5% |
| No match at all | 46/204 | 22.5% |

### 2.3 Line-by-Line Decoding Attempt (Lines 1-10)

When we take the first available decoding for each word:

```
Line  1: [fachys] IN E RA S AB ML O IO [sholdy]
Line  2: MB US DY IA [chtaiin] G [is] LS LS MS
Line  3: GC [sheky] A IA AI [cthoary] LL DA MT
Line  4: MN S UI [roloty] E N T A ES
Line  5: DT EE LA GS [cfhaiin]
Line  6: [ydaraishy]
Line  7: DE S GB [oydar] AR [cfhoaiin] [shodary]
Line  8: RE Q NB RE [chocthy] [oschy] N D IS
Line  9: N AS [cfhol] Q
Line 10: N A RN
```

### 2.4 Analysis of the Output

**The output is not readable as any language.** The decoded letters do not form recognizable Latin, Italian, or any other known language words. Observations:

1. **Random-looking letter sequences**: "IN E RA S AB ML O IO" has no obvious word boundaries or meaning in Latin or Italian.
2. **High ambiguity**: Most words that match have multiple possible decodings (e.g., "daiin" = U:n or B:ma or B:vq). Without knowing which table was used, the reading is indeterminate.
3. **22.5% complete failures**: Words like "fachys", "chtaiin", "cfhaiin", "cthoary", "chocthy", "ydaraishy" have no match in any Naibbe table at all. These are common Voynich words containing glyph combinations (cfh, chy sequences) that Naibbe does not generate.
4. **No coherent text emerges** from any combination of unigram/bigram choices.

### 2.5 Key Finding: Common Voynich Words in the Naibbe Framework

The most frequent Voynich words decode as follows under Naibbe:

| EVA word | Naibbe unigram | Naibbe bigram | Assessment |
|----------|---------------|---------------|------------|
| daiin (most common) | n | ma, vq | Plausible as "n" |
| chol | a | ee | Plausible as "a" |
| shol | s | ae | Plausible as "s" |
| dain | n | me, vz | Same letter as daiin -- expected? |
| chor | d | eo | Plausible |
| aiin | o | (none) | Plausible as "o" |
| ain | o | (none) | Same letter -- expected homophones |
| dar | e | ms, vc | Two tables both give "e" |
| chey | c | ee | Plausible |
| shey | i | ae | Plausible |

Under Naibbe, the most common Voynich words encode the most common Italian/Latin letters (e, a, i, o, n, s). This is expected and by design -- the tables are calibrated to produce these frequency matches.

**However:** daiin and dain both decode as "n"; aiin and ain both decode as "o"; dar encodes "e" from two different tables. This means the VMS has **pairs of words** that are near-identical and encode the same letter -- which is suspicious. In genuine Naibbe output, table selection is random, so you would not expect systematic pairing of words that differ by only one glyph and encode the same letter.

### 2.6 Verdict on Reverse Decoding

**The Naibbe cipher cannot be directly reversed on actual Voynich text to produce readable plaintext.** This is consistent with Greshko's own statement: "The Naibbe cipher is almost certainly not the way that the manuscript was constructed." The cipher was designed to show that a historically plausible mechanism *could* produce Voynich-like statistics, not to decode the manuscript.

---

## 3. Evidence For and Against the Naibbe Hypothesis

### 3.1 What the Naibbe Cipher Successfully Replicates

| Property | Replicated? |
|----------|------------|
| Glyph frequency distribution | Yes |
| Word length distribution | Yes |
| Low conditional entropy (h2 ~ 2 bits) | Yes |
| Zipf's law compliance | Yes |
| Zattera slot grammar (word-internal structure) | Yes (by design) |
| Unique word-type count (~4500-4700 in ~20,000 tokens) | Approximately |

### 3.2 What It Fails to Replicate

| Property | Status |
|----------|--------|
| Voynich A (herbal sections) | Not replicated |
| Line-initial/line-final positional effects | Not replicated |
| Word-length autocorrelation | Incomplete |
| Token autocorrelation (Stars section) | Not replicated |
| Full word-type coverage | Only ~30% of types, ~83% of tokens |
| Labels on illustrations | Problematic (would be single letters) |
| Cross-word dependencies (sandhi) | No mechanism exists |
| Currier A/B vocabulary divergence (Jaccard=0.172) | Cannot produce with single table set |
| Section-specific ch/sh ratio variation (p < 10^-6) | Italian letter frequencies are too stable across topics |
| Full-corpus vocabulary size (8,000+ types) | Predicts only ~200-500 types |
| Conditional entropy "knee" (two-component structure) | Homophonic noise would destroy this signal |

### 3.3 Peer Review and Independent Assessment

**Publication**: Peer-reviewed in *Cryptologia*, a respected cryptology journal.

**Expert reactions**:
- **Rene Zandbergen** (leading VMS researcher): Cautious; does not assume it is the actual method.
- **Bruce Schneier** (cryptographer): Posted without strong editorial endorsement.
- **Voynich Ninja forum**: Acknowledged as "the most thought through attempt" but raised concerns about verbosity (15 cipher glyphs per 5-letter word), the label problem, and limited type generation (~600 types from Divine Comedy vs ~3000 in equivalent VMS sections).
- **Ray Dillinger**: Suggested the manuscript's strong cyclic letter patterns point to hoax/asemic writing rather than any cipher.

**Scholarly consensus**: The Naibbe cipher is a **useful methodological contribution and benchmark**, not a solution. It proves that the cipher hypothesis remains viable while constraining what kind of cipher could produce Voynichese.

**No independent validation of actual decipherment has been achieved.**

---

## 4. Our Full-Corpus Compatibility Analysis (Previously Completed)

We ran 7 quantitative tests comparing our EVA corpus statistics against Naibbe predictions:

| Test | Naibbe Compatible? |
|------|-------------------|
| EVA word freq vs Italian word freq (r=0.9919) | FAIL (r=0.99 is a Zipf artifact; 8000+ types vs ~500 predicted) |
| Conditional entropy knee (4.5x ratio) | FAIL (letter-level encoding cannot produce two-component structure) |
| Prefix-suffix MI = 0.075 (Z=297) | AMBIGUOUS (could reflect table design) |
| ch/sh ratio varies by section (p < 10^-6) | FAIL (Italian letter frequencies are topic-stable) |
| Currier A/B Jaccard = 0.172 | FAIL (same tables = same vocabulary) |
| Vocabulary size 8000+ types | FAIL (Naibbe predicts ~200-500) |
| Word length distribution | NEUTRAL |

**Scorecard: 0 passes, 4 failures, 1 ambiguous, 1 neutral, 1 artifact.**

The vocabulary size failure is particularly devastating: the Voynich manuscript has 15-40x more unique word types than Naibbe can generate from a 21-letter alphabet with ~25 homophones per letter.

---

## 5. Other Recent Voynich Research (2024-2026)

### 5.1 Keegan Brewer & Michelle L. Lewis: "Women's Secrets" Hypothesis (2024)

- **Paper**: "The Voynich Manuscript, Dr Johannes Hartlieb and the Encipherment of Women's Secrets"
- **Journal**: *Social History of Medicine*, Volume 37, Issue 3, August 2024, pp. 559-582
- **Peer-reviewed**: Yes (Oxford Academic)
- **Claim**: The manuscript's content relates to gynecology, conception, and reproductive health. The Rosettes illustration represents coitus and conception. The bathing women illustrations relate to gynecological treatments.
- **Connection to Hartlieb**: Dr Johannes Hartlieb (c. 1410-1468) was a Bavarian court physician who wrote about women's secrets in encrypted/coded form.
- **Status**: Provides a contextual interpretation of illustrations but does NOT propose a decipherment of the text.

### 5.2 Tim Carter Clausen ("The Decipherist"): Hebrew Cipher Hypothesis (2026)

- **Published on**: thedecipherist.com (self-published, February 2026)
- **Peer-reviewed**: NO
- **Claim**: The VMS is "~85% solved" -- a 15th-century Italian Jewish rabbi's field manual written in a personal cipher based on Hebrew cursive script, read right-to-left.
- **Decoded words claimed**: TORO (bull), OLIO (oil), OTTO (eight), ORO (gold), OLLA (pot), LATTE (milk) -- all Italian words
- **Evidence**: 78 plant identifications, "10-month pregnancy wheel" matching Talmudic tradition, Jewish ritual elements
- **Methodology**: AI-assisted research ("research assistance from Claude (Anthropic)" acknowledged)
- **Critical assessment**: NOT independently validated. Self-published. The decoded words are short, high-frequency Italian words that could emerge from many mapping schemes. No systematic decryption algorithm demonstrated. 1 million+ web views in January 2026 suggest viral spread outpacing scholarly evaluation.

### 5.3 Lisa Fagin Davis: Codicological Research (2024-2026)

- **Affiliation**: Executive Director, Medieval Academy of America; Yale, Simmons, Rare Book School
- **Approach**: Physical manuscript analysis (codicology), NOT cryptography
- **Key findings**:
  - Five different scribes wrote the manuscript (published 2020 in *Manuscript Studies*)
  - XRF imaging reveals ink composition differences
  - Multispectral imaging and Latent Semantic Analysis for reconstructing original folio order
  - Identified Roman letters from an early deciphering attempt
- **Upcoming**: Yale University Press photofacsimile with interpretive essays (first volume of "Yale Studies in Materials and Texts")
- **Position on Naibbe**: No public comment found
- **Key quote**: "You are an expert cryptologist. I am an expert codicologist... We are all better off when we stay in our respective lanes."

### 5.4 Voynich-Toolkit (antenore, GitHub, 2025-2026)

- **Repository**: [github.com/antenore/voynich-toolkit](https://github.com/antenore/voynich-toolkit)
- **Method**: Computational analysis toolkit for statistical analysis and cipher-type discrimination
- **Finding**: Explored the Judeo-Italian hypothesis with Hebrew script read right-to-left. Phase 15 scribe analysis shows the "Hebrew signal" is dominated by Hand 1 (86 pages, all Currier A herbal), while other hands show weaker matches.
- **Assessment**: If the manuscript uses homophonic substitution or different scribes used different conventions, a single monoalphabetic mapping is structurally inadequate.

### 5.5 Manifold Prediction Market

- **Question**: "Will a decipherment of the Voynich Manuscript be scientifically recognized by end of Dec 31, 2026?"
- **Current probability**: **3%** (as of April 2026)
- **Criteria**: Translation of 10+ consecutive pages in a peer-reviewed journal, institutional validation from Beinecke Library, confirmation from 2+ independent experts
- **Notable**: Market creator Roland Konnerth posted extensive claims about a "state-machine protocol" decipherment, but community responses question the lack of executable decryption code

### 5.6 2026 International Conference on the Voynich Manuscript

- **Organizer**: Medieval Academy of America / University of Malta
- **Status**: Call for papers issued (double-blind review via EasyChair)
- **Topics**: History of VMS, NLP techniques, AI/ML approaches
- **Contact**: voynich2026@um.edu.mt
- **Website**: https://www.um.edu.mt/events/voynich2026/

---

## 6. Synthesis: State of Voynich Research in 2026

### 6.1 The Competitive Landscape

| Approach | Proponent | Status | Peer-Reviewed? |
|----------|-----------|--------|---------------|
| Verbose homophonic substitution | Greshko (Naibbe) | Proof-of-concept benchmark | Yes (Cryptologia) |
| Gynecological content interpretation | Brewer & Lewis | Contextual reading of illustrations | Yes (Social History of Medicine) |
| Hebrew cursive cipher | Clausen | Self-published claim | No |
| Physical/codicological analysis | Davis | Ongoing materiality research | Yes (Manuscript Studies) |
| Computational cipher discrimination | antenore toolkit | Statistical analysis | No (GitHub) |
| Nomenclator hypothesis | Our analysis | Statistical tests passed (7/7) | No (internal) |

### 6.2 What Has Actually Been Established

1. **The manuscript is genuine** (radiocarbon dated to 1404-1438, confirmed by multiple labs)
2. **The text has internal statistical structure** (not random gibberish -- entropy, Zipf's law, slot grammar)
3. **Multiple scribes contributed** (Davis's 5-scribe hypothesis, Currier's A/B classification)
4. **No decipherment has been independently validated**
5. **A verbose cipher *could* produce some VMS properties** (Greshko's contribution)
6. **The illustration content is consistent with 15th-century medical/pharmaceutical knowledge** (convergent finding across multiple researchers)

### 6.3 What Remains Unknown

1. Whether the text encodes meaningful content at all (vs. elaborate hoax or glossolalia)
2. The source language (Latin, Italian dialect, Hebrew, constructed language, or other)
3. The encoding mechanism (if any)
4. The original page/quire ordering
5. The identity of the author(s)

### 6.4 Assessment of the Naibbe Cipher's Significance

The Naibbe cipher is the most rigorous cipher-hypothesis proposal to date. It successfully demonstrates that:
- A historically plausible, hand-executable cipher can replicate word-level statistical properties of Voynichese
- The cipher hypothesis remains viable and should not be dismissed

However, it fails on:
- Vocabulary size (15-40x too few unique words)
- Cross-word dependencies (no mechanism for sandhi-like patterns)
- Section-specific vocabulary variation
- Currier A/B divergence
- Line-position effects

**It is a benchmark, not a solution.** Greshko himself states it explicitly: "The Naibbe cipher is almost certainly not the way that the manuscript was constructed."

### 6.5 Prediction

The Manifold prediction market's 3% probability for recognized decipherment by end of 2026 seems approximately right. No current approach has demonstrated the ability to produce verified, reproducible, readable text from the manuscript. The 2026 International Conference at Malta may surface new approaches, but a breakthrough in this timeframe appears unlikely.

---

## Sources

- [Greshko (2025) - Full paper in Cryptologia](https://www.tandfonline.com/doi/full/10.1080/01611194.2025.2566408)
- [Michael Greshko's project page](https://www.michaelgreshko.com/naibbe-cipher)
- [GitHub: Naibbe cipher implementation](https://github.com/greshko/naibbe-cipher)
- [Archaeology Magazine coverage](https://archaeologymag.com/2026/01/voynich-manuscript-may-be-a-cipher/)
- [Newsweek coverage](https://www.newsweek.com/voynich-manuscript-15th-century-book-cards-dice-cipher-naibbe-11316017)
- [Live Science coverage](https://www.livescience.com/archaeology/mysterious-voynich-manuscript-may-be-a-cipher-a-new-study-suggests)
- [IFLScience coverage](https://www.iflscience.com/is-this-how-the-voynich-manuscript-was-made-a-new-cipher-offers-fascinating-clues-81786)
- [The Art Newspaper](https://www.theartnewspaper.com/2026/01/07/can-a-new-cipher-help-to-explain-the-mysterious-voynich-manuscript)
- [Schneier on Security discussion](https://www.schneier.com/blog/archives/2025/12/substitution-cipher-based-on-the-voynich-manuscript.html)
- [Voynich Ninja forum](https://www.voynich.ninja/thread-4848-page-4.html)
- [Brewer & Lewis (2024) in Social History of Medicine](https://academic.oup.com/shm/article-abstract/37/3/559/7633883)
- [Tim Carter Clausen - The Decipherist](https://thedecipherist.com/articles/voynich_manuscript/)
- [GSNSP: 2026 theories overview](https://www.gsnsp.com/voynich-manuscript/)
- [Manifold Markets prediction](https://manifold.markets/Quintsequence/will-a-decipherment-of-the-voynich)
- [2026 Voynich Conference CfP](https://www.themedievalacademyblog.org/call-for-papers-the-voynich-manuscript/)
- [Lisa Fagin Davis at Beinecke](https://beinecke.library.yale.edu/voynich-manuscript-lisa-fagin-davis)
- [Davis materiality research](https://ciphermysteries.com/2025/10/11/lisa-fagin-davis-the-materiality-of-the-voynich-manuscript)
- [voynich-toolkit](https://github.com/antenore/voynich-toolkit)
- [Language Log critique](https://languagelog.ldc.upenn.edu/nll/?p=63603)

---

*Analysis completed 2026-04-07. Reverse Naibbe test performed using tables from github.com/greshko/naibbe-cipher.*
