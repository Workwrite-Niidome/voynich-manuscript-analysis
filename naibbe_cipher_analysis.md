# The Naibbe Cipher: Comprehensive Analysis

## A 2025 Decipherment Proposal for the Voynich Manuscript

**Date**: 2026-04-06
**Status**: Extensive web research completed

---

## Executive Summary

The Naibbe cipher, published by Michael A. Greshko in *Cryptologia* (November 26, 2025), is **NOT a decipherment of the Voynich Manuscript**. It is a proof-of-concept demonstration that a historically plausible verbose homophonic substitution cipher, executable entirely by hand with 15th-century materials (dice, playing cards, pen, paper), can encrypt Latin and Italian plaintext into ciphertext that statistically resembles Voynichese. Greshko himself states: "The Naibbe cipher is almost certainly not the way that the manuscript was constructed." Lisa Fagin Davis was **not involved** in this research; she pursues an independent codicological approach.

**Key correction to the prompt**: The user's framing ("published 2025 by Michael Greshko/Lisa Fagin Davis") incorrectly associates Davis with this work. Davis and Greshko are independent researchers with different approaches.

---

## 1. The Complete Naibbe Cipher Proposal

### 1.1 What It Is

A verbose homophonic substitution cipher that maps individual letters in a Latin or Italian plaintext onto multiple distinct strings of Voynichese glyphs. The name "Naibbe" comes from a late 14th-century Italian word for a card game.

### 1.2 Step-by-Step Method

**Step 1: Break plaintext into units**
- Roll a die to determine how to segment a block of plaintext into single letters ("unigrams") and pairs of consecutive letters ("bigrams")
- Example: "gatto" might become "g" | "at" | "to"
- Roughly half the units will be unigrams, half bigrams

**Step 2: Select encryption table**
- Draw a playing card to determine which of **six different substitution tables** to use
- Two variants exist: one using a 78-card tarocchi (tarot) deck from 15th-century Italy, another using a standard 52-card deck
- Tables are "weighted" by corresponding number of cards so that statistical occurrence of output glyphs matches the frequencies observed in the actual VMS

**Step 3: Encode with prefix/suffix structure**
- Each letter maps to one of three positions in the encryption table:
  1. **Unigram encoding** (single letter -> single Voynichese "word")
  2. **Bigram prefix** (first letter of pair -> prefix glyphs)
  3. **Bigram suffix** (second letter of pair -> suffix glyphs)
- Prefixes use one set of characters (modified Zattera slots 0-5) and suffixes use another (modified Zattera slots 6-11), creating natural structural markers
- A unigram can be represented **6 different ways**
- A bigram can be represented **36 different ways** (6 x 6)

### 1.3 Key Design Principles

- The cipher is **verbose**: each plaintext letter becomes an entire Voynichese "word" (typically ~3 glyphs)
- It is **homophonic**: each letter has multiple possible representations, defeating simple frequency analysis
- The **respacing** of plaintext (breaking words into 1-2 letter units) destroys original word boundaries
- Output words obey an **expanded version of the Zattera slot grammar** observed in the real manuscript

### 1.4 Decipherability

The cipher is fully reversible. Because prefixes and suffixes use different glyph sets, a trained reader can identify where prefix ends and suffix begins, then look up the plaintext letters in the appropriate table. The card draw (which table was used) must be recorded or can be determined by context.

---

## 2. Claimed Results and Statistical Properties

### 2.1 What the Naibbe Cipher Successfully Replicates

The paper demonstrates replication of **word-level** properties of Voynich B (the "language" found in biological, astronomical/astrological, and recipe sections):

| Property | Status |
|----------|--------|
| Glyph frequency distribution | Replicated |
| Word length distribution | Replicated |
| Conditional character entropy (h2 ~2, vs natural language 3-4) | Replicated |
| Zipf's law compliance (frequency-rank power law) | Replicated |
| Zattera slot grammar (word-internal structure) | Replicated (by design) |
| Number of unique word types (~4500-4700 in ~20,000 tokens) | Replicated |
| Proportional frequency-rank distribution matching Voynich B | Replicated |
| Absolute frequencies of specific Voynich B word types | Partially replicated |

### 2.2 What the Naibbe Cipher Does NOT Replicate

| Property | Status |
|----------|--------|
| Voynich A properties (herbal/pharma sections) | **Incomplete** - acknowledged weakness |
| Line-initial/line-final positional effects | **Not replicated** (Section 4.3 of paper) |
| Paragraph-level patterns | **Not replicated** |
| Word-length autocorrelation (long-long-short-short clustering) | **Incompletely addressed** |
| Token autocorrelation (especially in Stars section) | **Not replicated** |
| Exact word-type coverage | **Only ~30% of unique word types, ~83% of tokens** |
| Line-by-line reuse patterns | **Not replicated** |
| Labels on illustrations | **Problematic** - labels would be mostly single letters |

### 2.3 The Voynich A / Voynich B Problem

This is a critical limitation. Greshko's own paper acknowledges: "the Naibbe cipher's incomplete replication of Voynich B's properties underscores the difficulty of achieving a comprehensive cipher-based model for Voynich manuscript text generation." The cipher was primarily tested against **Voynich B** only; Voynich A (which appears in the herbal and pharmaceutical sections) is not well-replicated.

### 2.4 Plaintext Corpora Used for Testing

Greshko tested the cipher on a combination of period-appropriate texts:
- Dante's *Divina Commedia*
- Book 16 of Pliny's *Natural History*
- Grosseteste's *De sphaera*
- A 14th-century Latin "alchemical herbal"
- Caesar's *De bello Gallico*

---

## 3. Peer Review and Community Reaction

### 3.1 Publication Status

- Published in *Cryptologia*, a peer-reviewed journal specializing in cryptology
- Open-access format
- Python implementation and Excel tools released on GitHub (github.com/greshko/naibbe-cipher) and Zenodo
- Licensed under modified MIT with citation requirement

### 3.2 Expert Reactions

**Rene Zandbergen** (leading Voynich researcher): Cautioned that we should not assume it is the exact method used. Remains unsure whether the text has actual meaning or is a hoax.

**Bruce Schneier** (cryptography expert): Posted the paper on his blog with minimal editorial commentary, letting the community discuss.

**Voynich Ninja forum** (community of dedicated researchers): Multi-page discussion with mixed reception:
- Acknowledged as "the most thought through attempt of replicating the statistics of Voynichese"
- **Verbosity criticism**: ~15 Voynich glyphs needed to encode a 5-letter plaintext word, "feels like too much work"
- **Label problem**: Under this cipher, illustration labels would consist mostly of single encrypted letters, inconsistent with observed VMS labels
- **Type generation**: When tested with simpler sources (Divine Comedy), generates only ~600 word types across 14,000 tokens vs ~3,000 types in equivalent Voynich B sections
- **Positional constraints**: Questions about whether it captures VMS's "strong positionality" (certain words appearing at line beginnings/endings)

**Ray Dillinger** (Schneier blog): Noted Voynichese exhibits "very strong bias about letters appearing in cycles" with limited sequence variation, suggesting hoax or asemic writing rather than enciphered language.

### 3.3 General Scholarly Assessment

The consensus is that the Naibbe cipher is a **useful methodological contribution** and benchmark, not a solution. It demonstrates that the cipher hypothesis remains viable while placing constraints on what kind of cipher could produce Voynichese. It is welcomed as sharpening the questions future studies must address.

---

## 4. Statistical Tests: Comparison with Our Analysis

### 4.1 Tests We Ran vs Tests in the Naibbe Paper

| Our Test | Naibbe Paper Addresses? | Verdict |
|----------|------------------------|---------|
| Entropy analysis | YES - h2 ~2 replicated | Compatible |
| Zipf's law | YES - power law emerges naturally | Compatible |
| Sandhi (cross-word phonological alternation) | NO - not discussed | Unknown |
| Morphological structure (prefix+root+suffix) | PARTIALLY - slot grammar by design | Compatible but trivial (built into cipher) |
| Section-specific vocabulary | NO - not addressed | Unknown |
| Function word paradigm (PREFIX + -aiin) | NO - not addressed | Unknown |
| n/l/r equal distribution | NO - not addressed | Unknown |
| ch/sh opposition | NO - not addressed | Unknown |
| A/B scribe difference | PARTIALLY - acknowledged as limitation | Problematic |

### 4.2 Detailed Analysis

**Entropy**: The Naibbe cipher produces low conditional entropy (h2 ~2) matching Voynichese. This is because the slot grammar constrains glyph sequences, making the next glyph highly predictable given the previous one. Our entropy findings are compatible with but do not prove the Naibbe model.

**Zipf's Law**: Naibbe ciphertexts automatically approximate power-law frequency distributions. However, as noted in our earlier analysis (NAIBBE_COMPATIBILITY_ANALYSIS.md), any two Zipfian distributions correlate r>0.95 in log-log space regardless of mechanism. This is not strong evidence for or against.

**Sandhi**: The Naibbe paper does not discuss cross-word phonological alternation. Our finding of sandhi-like patterns in Voynichese is **not predicted by the Naibbe cipher**. In a verbose homophonic substitution cipher, each "word" encodes just 1-2 plaintext letters independently. There is no mechanism for the last glyph of one word to influence the first glyph of the next word based on phonological rules. If our sandhi findings are real, they are **problematic for the Naibbe model**.

**Morphological Structure**: The prefix+root+suffix pattern is compatible with Naibbe because it is **built into the cipher by design** (prefix = bigram first letter, suffix = bigram second letter, using different slot ranges). However, this makes it a circular argument: the cipher was designed to produce this structure, so observing it in the VMS doesn't validate the cipher.

**Section-Specific Vocabulary**: Not addressed. In the Naibbe model, vocabulary differences between sections would arise from differences in plaintext content (herbal text uses different Latin words than astronomical text). This is plausible but untested.

**Function Words (PREFIX + -aiin)**: Not addressed. In the Naibbe model, high-frequency "words" like "daiin" and "aiin" would represent common plaintext letters (e, a, i, etc.). The consistent -aiin ending would need to be explained as a coincidence of the substitution tables. This seems difficult.

**n/l/r Equal Distribution**: Not addressed. Our finding that n, l, r have suspiciously equal frequencies would need to be an emergent property of the cipher tables. Not obviously predicted.

**ch/sh Opposition**: Not addressed. The complementary distribution of ch and sh in the VMS would need to arise from the substitution table structure. Potentially explainable if ch and sh encode different letters.

---

## 5. Compatibility with Our Findings

### 5.1 Findings the Naibbe Cipher CAN Explain

1. **Low entropy**: Yes, via constrained slot grammar
2. **Zipfian distribution**: Yes, emerges naturally from verbose homophonic substitution
3. **Word-internal structure (slots)**: Yes, by design
4. **High word-type count**: Yes, via homophonic substitution (36 ways per bigram)

### 5.2 Findings the Naibbe Cipher CANNOT Easily Explain

1. **Sandhi/cross-word alternation**: No mechanism for inter-word phonological influence in a letter-substitution cipher
2. **Function word paradigm**: Why would encrypted single letters consistently end in -aiin?
3. **Section-specific vocabulary shifts**: Plausible only if plaintext content varies by section (untested)
4. **Line-initial effects**: Acknowledged gap in the paper
5. **Voynich A properties**: Acknowledged incomplete replication
6. **Labels**: Single-letter ciphertexts would look nothing like observed labels
7. **Word-length autocorrelation**: Not replicated

### 5.3 Critical Assessment

The Naibbe cipher is the **strongest cipher-hypothesis proposal to date** for the Voynich Manuscript. However, it has significant gaps:

- It is a proof-of-concept, not a decipherment
- It replicates word-level statistics but not line/paragraph/page-level patterns
- It covers only ~30% of Voynich B's unique word types
- It does not address Voynich A at all adequately
- It cannot explain cross-word dependencies (sandhi)
- The verbosity (~15 cipher glyphs per 5-letter word) makes practical manuscript creation implausible

If our sandhi findings are robust, they represent the **strongest evidence against** any simple substitution cipher model, including Naibbe. Cross-word phonological alternation implies that Voynichese "words" interact with each other at a phonological level, which is incompatible with each word being an independent cipher token encoding 1-2 plaintext letters.

---

## 6. Can We Test It Ourselves?

### 6.1 Resources Available

**YES** - Greshko has released full implementation:
- **GitHub**: github.com/greshko/naibbe-cipher
  - `naibbe.py` / `naibbe_v2.py` - encryption scripts
  - `decrypt_naibbe.py` - decryption script
  - `voynichesque.py` - Voynich-like text generator
  - Jupyter notebooks for interactive exploration
  - Input examples, encrypted samples, decrypted outputs
- **Zenodo**: Extended datasets and Microsoft Excel implementations (10.5281/zenodo.16415087)

### 6.2 What We Could Do

1. **Forward test**: Encrypt known Latin/Italian pharmaceutical texts and compare the output statistics with our EVA transcription statistics
2. **Reverse test**: Attempt to apply the decryption algorithm to actual EVA text (this would require knowing or guessing the correct substitution tables)
3. **Sandhi test**: Generate Naibbe ciphertexts and check whether they exhibit cross-word phonological alternation patterns similar to what we found in real Voynichese
4. **Function word test**: Check whether Naibbe ciphertexts produce anything resembling the -aiin function word paradigm
5. **Positional test**: Check whether Naibbe ciphertexts produce line-initial/line-final effects

### 6.3 Limitations of Testing

The Naibbe cipher is explicitly **not** the actual cipher used (if any). Therefore:
- We cannot decrypt the VMS using Naibbe tables
- We can only test whether the cipher *class* (verbose homophonic substitution) is plausible
- A negative result (Naibbe output doesn't match our findings) doesn't disprove the cipher hypothesis in general, only this specific implementation

---

## 7. Lisa Fagin Davis: Current Position

### 7.1 Who She Is

- Executive Director of the Medieval Academy of America
- Teaches at Yale University, Simmons University School of Library and Information Science, and Rare Book School (University of Virginia)
- One of the world's foremost Voynich manuscript scholars

### 7.2 Her Approach: Codicology, Not Cryptography

Davis explicitly focuses on the **physical manuscript** rather than attempting decipherment. Key quote: "You are an expert cryptologist. I am an expert codicologist... We are all better off when we stay in our respective lanes."

She states: researchers "cannot read a book whose pages are out of order," positioning structural work as foundational.

### 7.3 Key Research Findings

- **Five scribes hypothesis** (2020): Concluded the manuscript was written by five different hands, not one. The interaction between hands suggests the manuscript is misbound and has been for centuries.
- **Materiality research** (2024-2025): Using X-ray fluorescence imaging, multispectral imaging, and Latent Semantic Analysis to reconstruct the original folio ordering based on waterstains, paint transfer, and ink composition.
- **Singulion hypothesis**: Proposes that some quires (particularly Q20) consisted of single bifolios rather than traditional nested gatherings.
- **XRF analysis**: Confirmed Marci's marginalia uses zinc-heavy ink; Voynich applied sulfur-based reagents to reveal Sinapius's annotations.
- **Earlier annotations**: Identified Roman letters likely from an early deciphering attempt.

### 7.4 Upcoming Book

Yale University Press will publish a photofacsimile of the Voynich Manuscript with interpretive essays, as the first volume in "Yale Studies in Materials and Texts."

### 7.5 Position on Decipherment

Davis is **agnostic** about whether the text is meaningful. She does not assume it is readable. She dismisses DNA testing as currently unproductive ("There is literally nothing to compare the DNA to!"). She has **not commented publicly on the Naibbe cipher** in any sources found.

---

## 8. Implications for Our Research

### 8.1 The Naibbe Cipher Does Not Invalidate Our Findings

The Naibbe cipher is:
- A proof-of-concept, not a solution
- Focused on word-level statistics only
- Explicitly incomplete in replicating all VMS properties
- Unable to explain several patterns we identified (sandhi, function words, line effects)

### 8.2 Our Findings That Remain Unexplained by Any Current Theory

1. **Sandhi patterns**: Cross-word phonological alternation is not predicted by any substitution cipher model
2. **Function word paradigm**: The systematic PREFIX + -aiin pattern lacks a cipher-based explanation
3. **n/l/r equipartition**: The suspiciously equal distribution of these three glyphs
4. **Section-specific vocabulary shifts**: Consistent with either meaningful content or elaborate hoax

### 8.3 What We Should Do Next

1. **Download and run the Naibbe cipher** from GitHub against our EVA corpus
2. **Test sandhi in Naibbe output**: This is the critical discriminator. If Naibbe ciphertext does NOT show sandhi, it strengthens our linguistic hypothesis.
3. **Test function word emergence**: See if any Naibbe configuration produces -aiin-like paradigms
4. **Compare with Davis's five-scribe hypothesis**: Do our Currier A/B findings align with her five-scribe identification?

---

## 9. Overall Assessment

| Criterion | Rating |
|-----------|--------|
| Scholarly rigor | HIGH - peer-reviewed, open-source, honest about limitations |
| Is it a decipherment? | NO - explicitly stated by the author |
| Does it produce readable text from the VMS? | NO |
| Does it prove the VMS is a cipher? | NO - proves only that a cipher *could* produce VMS-like output |
| Does it refute our findings? | NO - does not address most of our key findings |
| Is it compatible with our findings? | PARTIALLY - compatible with entropy/Zipf, incompatible with sandhi |
| Should we take it seriously? | YES - the strongest cipher-model proposal to date |
| Does it change our conclusions? | NO - but it provides a useful comparison benchmark |

The Naibbe cipher is best understood as establishing a **lower bound** on what a substitution cipher can achieve in replicating Voynichese. It shows that word-level statistics can be replicated by cipher, but the many properties it fails to replicate (line effects, sandhi, function words, labels, Voynich A) suggest that if the VMS is a cipher, it must be considerably more sophisticated than the Naibbe model, or that the VMS contains genuine linguistic structure that no substitution cipher can fully capture.

---

## Sources

- [Greshko (2025) - Full paper in Cryptologia](https://www.tandfonline.com/doi/full/10.1080/01611194.2025.2566408)
- [Michael Greshko's project page](https://www.michaelgreshko.com/naibbe-cipher)
- [GitHub: Naibbe cipher implementation](https://github.com/greshko/naibbe-cipher)
- [Sci.News coverage](https://www.sci.news/othersciences/linguistics/voynich-manuscript-cipher-14466.html)
- [Newsweek coverage](https://www.newsweek.com/voynich-manuscript-15th-century-book-cards-dice-cipher-naibbe-11316017)
- [Live Science coverage](https://www.livescience.com/archaeology/mysterious-voynich-manuscript-may-be-a-cipher-a-new-study-suggests)
- [Archaeology Magazine coverage](https://archaeologymag.com/2026/01/voynich-manuscript-may-be-a-cipher/)
- [The Art Newspaper coverage](https://www.theartnewspaper.com/2026/01/07/can-a-new-cipher-help-to-explain-the-mysterious-voynich-manuscript)
- [The Wild Hunt coverage (tarot connection)](https://wildhunt.org/2026/01/reading-the-unreadable-a-new-study-proposes-cipher-and-tarot-connection.html)
- [Schneier on Security blog discussion](https://www.schneier.com/blog/archives/2025/12/substitution-cipher-based-on-the-voynich-manuscript.html)
- [Voynich Ninja forum discussion](https://www.voynich.ninja/thread-4848-page-4.html)
- [Cipher Mysteries: Lisa Fagin Davis materiality research](https://ciphermysteries.com/2025/10/11/lisa-fagin-davis-the-materiality-of-the-voynich-manuscript)
- [Beinecke Library: Lisa Fagin Davis and the Voynich](https://beinecke.library.yale.edu/voynich-manuscript-lisa-fagin-davis)
- [Lisa Fagin Davis - Wikipedia](https://en.wikipedia.org/wiki/Lisa_Fagin_Davis)
