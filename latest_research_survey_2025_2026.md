# Voynich Manuscript: Comprehensive Research Survey (2024-2026)

**Compiled**: 2026-04-10
**Scope**: All significant research developments from 2024 through early 2026
**Purpose**: Evaluate new findings against our own analysis; identify untried approaches

---

## TABLE OF CONTENTS

1. [Peer-Reviewed Publications](#1-peer-reviewed-publications)
2. [Preprints and Working Papers](#2-preprints-and-working-papers)
3. [Codicological and Material Science Findings](#3-codicological-and-material-science-findings)
4. [AI and Machine Learning Approaches](#4-ai-and-machine-learning-approaches)
5. [Independent Researcher Claims](#5-independent-researcher-claims)
6. [Conferences and Community Activity](#6-conferences-and-community-activity)
7. [Expert Consensus and Skepticism](#7-expert-consensus-and-skepticism)
8. [Compatibility with Our Findings](#8-compatibility-with-our-findings)
9. [Untried Approaches and Gaps](#9-untried-approaches-and-gaps)
10. [Assessment Summary Table](#10-assessment-summary-table)

---

## 1. PEER-REVIEWED PUBLICATIONS

### 1.1 Greshko, "The Naibbe Cipher" (Cryptologia, November 2025)

**Citation**: Greshko, Michael A. "The Naibbe cipher: a substitution cipher that encrypts Latin and Italian as Voynich Manuscript-like ciphertext." *Cryptologia* (2025). DOI: [10.1080/01611194.2025.2566408](https://www.tandfonline.com/doi/full/10.1080/01611194.2025.2566408)

**Claim**: A verbose homophonic substitution cipher, executable by hand with 15th-century materials (playing cards and dice), can produce ciphertext that statistically mimics the Voynich Manuscript. Named after "naibbe," a late 14th-century Italian card game.

**Peer-reviewed**: Yes (Cryptologia, Taylor & Francis).

**Methodology**:
- Roll a die to segment plaintext (Latin or Italian) into unigrams and bigrams
- Draw a playing card to select one of six substitution tables (alpha, beta1-3, gamma1-2)
- Each plaintext letter maps to an entire EVA "word" (unigram encoding) or a prefix/suffix pair (bigram encoding)
- Tables are weighted so output glyph frequencies match actual VMS statistics
- Uses either 78-card tarocchi deck or 52-card standard deck (both historically attested in 15th-century Italy)
- Prefix glyphs occupy Zattera slots 0-5; suffix glyphs occupy slots 6-11

**Key properties reproduced**:
- Glyph frequency distributions
- Word length distributions
- Positional glyph constraints (Zattera slot grammar)
- Word-level entropy
- Many "word grammar" rules of Voynichese

**What it does NOT claim**: Greshko explicitly states this is NOT a solution. He does not assert the Naibbe cipher is how the VMS was created, nor does he assert the VMS is even a ciphertext. It is a proof-of-concept that the "ciphertext hypothesis" remains viable.

**Expert reception**:
- Bruce Schneier featured it on his security blog (December 2025) without additional commentary
- Reader Ray Dillinger (cryptographer) noted the cipher elegantly explains Voynichese's low information density (~0.33 bits/letter vs ~1.25 for English)
- Dillinger himself still favors the hoax hypothesis based on the expensive materials used
- Voynich community experts welcomed it as "a useful benchmark, not a definitive answer"

**Open source**: Code at [github.com/greshko/naibbe-cipher](https://github.com/greshko/naibbe-cipher); data at Zenodo

**Compatibility with our findings**: **HIGH**. Our nomenclator model is structurally similar -- both propose that each "word" encodes a sub-word unit of plaintext. The Naibbe cipher is a pure homophonic substitution, while our model proposes a code/cipher hybrid (nomenclator). The Naibbe cipher does NOT explain the prefix-category structure (ch-/sh-/qo-) that we identified as semantic code categories. However, the Naibbe cipher's slot grammar alignment (Zattera slots) is compatible with our morphological analysis.

**Novel approaches we haven't tried**: Testing our own nomenclator model's output against Naibbe-generated mock text to see if they produce distinguishable statistics.

---

### 1.2 Ponnaluri, "The Voynich Manuscript was written in a single, natural language" (Cryptologia, November 2024)

**Citation**: Ponnaluri, Raj V. "The Voynich Manuscript was written in a single, natural language." *Cryptologia* 49(6) (2024). DOI: [10.1080/01611194.2024.2414128](https://www.tandfonline.com/doi/full/10.1080/01611194.2024.2414128)

**Claim**: Comprehensive analysis of word types, tokens, ranks, characters, placement, and frequencies demonstrates there is NO evidence for Currier's "two languages" or two dialects. The text was written in a single natural language.

**Peer-reviewed**: Yes (Cryptologia).

**Methodology**: Statistical comparison of word type distributions, token frequencies, character placement patterns, and rank-frequency curves across the entire manuscript, comparing Currier A and B sections.

**Compatibility with our findings**: **MODERATE**. Our analysis identified multiple scribes (confirmed by glyph z-test, z=8.8) but did not necessarily claim multiple languages. This paper strengthens the view that scribal variation is orthographic, not linguistic -- which is consistent with our nomenclator model (same code system, different handwriting).

---

### 1.3 Brewer & Lewis, "Voynich Manuscript, Dr Johannes Hartlieb and the Encipherment of Women's Secrets" (Social History of Medicine, 2024)

**Citation**: Brewer, Keagan, and Michelle L. Lewis. "Voynich Manuscript, Dr Johannes Hartlieb and the Encipherment of Women's Secrets." *Social History of Medicine* 37(3):559 (2024). DOI: [10.1093/shm/hkae007](https://academic.oup.com/shm/article-abstract/37/3/559/7633883)

**Claim**: The manuscript is a medieval gynecological guide. The "Rosettes" nine-part illustration depicts the medieval understanding of the uterus (seven chambers) and vagina (two openings), illustrating "coitus and conception." The naked women with objects are consistent with gynecological instruction.

**Peer-reviewed**: Yes (Oxford Academic).

**Methodology**:
- Visual analysis of illustrations, especially the Rosettes and balneological (bathing) sections
- Historical contextualization via Johannes Hartlieb (Bavarian physician, fl. 1430s-1468)
- Hartlieb documented that gynecological knowledge was deliberately enciphered to prevent women from controlling reproduction
- Carbon dating (1404-1438) aligns with Hartlieb's period and geographic context (Bavaria/Northern Italy)

**Compatibility with our findings**: **MODERATE**. Our pharmaceutical/herbal identification does not exclude gynecological content -- medieval herbals frequently included sections on women's health, contraception, and fertility. The "code to hide dangerous knowledge" motivation aligns with our nomenclator hypothesis (why would someone encode herbal recipes unless the knowledge was itself sensitive?). However, the Rosettes interpretation as reproductive anatomy conflicts with other interpretations (astronomical, cartographic).

**Novel approaches we haven't tried**: Systematic comparison of VMS illustrations with known medieval gynecological manuscripts (e.g., Muscio's Gynaecea, Trotula manuscripts).

---

### 1.4 Ardic, "Syllable-letter structure in the ATA (Voynich) Manuscript" (Turk Kulturu, 2025)

**Citation**: Ardic, Ahmet. Published in *Turk Kulturu* (Turkish Culture journal), 2025.

**Claim**: The VMS text is Old Turkish (specifically Pecheneg Turkish), written phonetically. Over 1,000 words have been read. Syllable-letter structures align with Ottoman tughra writing direction (bottom-to-top).

**Peer-reviewed**: Published in a Turkish-language journal (peer review status of that specific journal unclear in mainstream Western academic context).

**Methodology**: Phonetic mapping of VMS glyphs to Turkish phonemes; identification of phonetic harmony patterns; word-image pairing analysis for plant names and proper nouns; use of /P/ in place of /B/ and /F/ as evidence for Pecheneg dialect.

**Compatibility with our findings**: **LOW**. Our quantitative Turkish vowel harmony test yielded 58% (chance level), which we cited as a rejection of the Turkic hypothesis. Ardic's work predates our analysis and uses a different (qualitative) methodology. However, the fact that Ardic has been refining his readings since 2017 and claims 1,000+ words merits at least a critical review of his specific glyph-to-phoneme mappings.

---

## 2. PREPRINTS AND WORKING PAPERS

### 2.1 Compression-Based Hypothesis (Preprints.org, September 2025)

**Citation**: "Voynich Manuscript Decryption: A Novel Compression-Based Hypothesis and Computational Framework." Preprints.org, 2025. [https://www.preprints.org/manuscript/202509.0403](https://www.preprints.org/manuscript/202509.0403)

**Claim**: The VMS text is NOT an encoding of natural language but represents a compressed data stream analogous to LZ77 compression + Huffman coding.

**Peer-reviewed**: No (preprint).

**Methodology**:
- Treats Voynich transliterations as an encoded bitstream
- Systematically tests decompression parameters
- Uses Shannon entropy as a fitness metric to identify outputs resembling natural language
- Proposes the manuscript's low redundancy and specific word structure are artifacts of compression, not features of an unknown language

**Compatibility with our findings**: **LOW-MODERATE**. The compression hypothesis would explain the low character entropy (~3.8 bits vs 4.0 for plaintext) that we observed. However, LZ77-style compression was not conceptualized until the 20th century. The authors argue for a "functionally similar" antecedent, which is speculative. Our nomenclator model already explains the entropy gap through code/cipher mixing without invoking anachronistic technology.

**Novel approaches we haven't tried**: Running actual decompression algorithms on the VMS bitstream is computationally novel, even if historically implausible.

---

### 2.2 "The Voynich Codex Decoded: Statistical Symbolism and Scroll-Wide Logic" (arXiv, April 2025)

**Citation**: arXiv:2505.02261, April 14, 2025. [https://arxiv.org/abs/2505.02261](https://arxiv.org/abs/2505.02261)

**Claim**: The VMS is a non-verbal esoteric system rooted in initiatory tradition, decoded via mathematical rhythm (Fibonacci grouping, prime clustering, golden ratio segmentation) and symbolic alignment with Hermetic, Islamic, and alchemical knowledge systems.

**Peer-reviewed**: No (arXiv preprint).

**Methodology**: Fibonacci grouping, prime number clustering, golden ratio segmentation, symbolic alignment. Validated via Boolean framework and chi-squared tests across ten structural tests.

**Compatibility with our findings**: **VERY LOW**. This approach abandons phonetic/linguistic interpretation entirely and proposes a symbolic/mathematical reading. While creative, it does not explain the word-level statistical properties that match natural language encoding (Zipf's law, word entropy ~10 bits). Our work specifically rejected non-linguistic readings based on Hurst exponent (0.78-0.99) and MI (0.445 bits).

---

### 2.3 "Unlocking the Voynich Cipher via the New Algorithmic Coding Hypothesis" (ResearchGate, September 2025)

**Citation**: ResearchGate, September 10, 2025. [https://www.researchgate.net/publication/395381163](https://www.researchgate.net/publication/395381163)

**Claim**: Same team/approach as 2.1 above (compression-based hypothesis). The VMS text is a compressed data stream; unusual statistical properties are artifacts of encoding rather than features of an unknown language.

**Peer-reviewed**: No.

**Compatibility with our findings**: Same as 2.1.

---

### 2.4 Padua Botanical Garden / Cortuso Hypothesis (Academia.edu, 2025)

**Citation**: Multiple papers on Academia.edu, most recent October 2025. "The solution to the Voynich Manuscript (12Oct25) 10th draft."

**Claim**: The VMS is a coded botanical catalogue from Renaissance Italy, authored by or under Giacomo Antonio Cortuso, prefect of the Padua Botanical Garden (1545-1603). Voynich "words" are positional codewords encoding plant morphology: first token = roots, second = stems, third = leaves.

**Peer-reviewed**: No (Academia.edu self-published).

**Methodology**:
- Statistical correlation with Padua's botanical inventory (Spearman rho=0.92, Kendall tau=0.91, chi-sq=6.74, p<0.01)
- Iterative codebook derivation
- Blind predictive validation (80-100% accuracy across 35 folios)
- Maps word position to morphological description (roots, stems, leaves)

**Compatibility with our findings**: **MODERATE-HIGH on structure, LOW on dating**. The positional encoding idea (word position = semantic category) resonates with our prefix-category system (ch-=plants, sh-=preparations, qo-=quantities). However, the Cortuso attribution (1545-1603) is FATAL -- carbon dating places the vellum at 1404-1438, over a century earlier. Even if the text were added later to old vellum, the ink analysis confirms 15th-century materials. The morphological encoding approach is worth examining, but the authorship claim is incompatible with physical evidence.

**Novel approaches we haven't tried**: Systematic positional decoding where each word's position within a line carries semantic weight (e.g., position 1 = root description, position 2 = stem description).

---

## 3. CODICOLOGICAL AND MATERIAL SCIENCE FINDINGS

### 3.1 Lazarus Project Multispectral Imaging (Released September 2024)

**Source**: Lisa Fagin Davis, [Manuscript Road Trip blog](https://manuscriptroadtrip.wordpress.com/2024/09/08/multispectral-imaging-and-the-voynich-manuscript/); images captured 2014 by The Lazarus Project team (Michael Phelps, Gregory Heyworth, Chet Van Duzer, Ken Boydston, Roger Easton), released 2024.

**Key findings**:
- Three columns of lettering discovered on the opening folio (f1r), previously invisible
- Two columns contain Roman alphabet letters; one contains Voynichese characters
- Likely an early decryption attempt, NOT part of the original text
- Handwriting analysis identifies Johannes Marcus Marci (Prague doctor, owned MS 1662-1665) as the likely author of these annotations
- Marci appears to have been attempting substitution cipher decryption using two different approaches
- Jacobus Sinapius signature in bottom margin of f1r now clearly readable (previously chemically treated by Wilfrid Voynich in 1912)

**Peer-reviewed**: Blog publication with academic rigor; images publicly available.

**Compatibility with our findings**: **HIGH**. The discovery that Marci attempted substitution cipher decryption in the 17th century confirms the manuscript was perceived as enciphered text (not gibberish) by historical owners. The Sinapius signature strengthens Prague provenance chain.

**Novel approaches we haven't tried**: We have not analyzed the specific Roman letter sequences Marci wrote to see if they constitute a meaningful partial decryption or a failed attempt.

---

### 3.2 Lisa Fagin Davis, Codicological Analysis (2024-2025)

**Source**: Davis, Lisa Fagin. "Voynich Codicology," [Manuscript Road Trip](https://manuscriptroadtrip.wordpress.com/2025/01/19/voynich-codicology/) (January 2025); presentation "The Materiality of the Voynich Manuscript" at University of Toronto Centre for Medieval Studies (discussed October 2025 at [Cipher Mysteries](https://ciphermysteries.com/2025/10/11/lisa-fagin-davis-the-materiality-of-the-voynich-manuscript)).

**Key findings**:

1. **Five scribes identified** (expanding on Currier's original two "hands"), with scribal work in the Botanical section organized by BIFOLIUM, not by quire or folio sequence -- described as "utterly atypical" in Davis's experience of hundreds of medieval manuscripts.

2. **Evidence of rebinding**: Water damage patterns in upper margins show inconsistent progression across current folio sequence, proving spill occurred before the current binding order. 17th-century folio numbers were added atop stains. Early quire numbers suggest rebinding within ~100 years of writing.

3. **Quire 9 reconfigured**: Sewing was in the wrong valley-fold; astronomical diagrams make more visual sense in a reconstructed original configuration.

4. **Material chronology proposed**: Early 1400s writing/binding -> later 1400s water damage -> disbinding and drying -> rebinding with misordered bifolia -> 1600s foliation -> leaf loss -> modern conservation.

**Peer-reviewed**: Academic presentation at University of Toronto; blog publication with detailed evidence.

**Compatibility with our findings**: **HIGH**. The five-scribe finding aligns with our glyph shape z-test (z=8.8) confirming multiple scribes. The rebinding evidence is critical -- it means the CURRENT folio order may NOT be the original order, which has implications for any sequential decryption attempt. Our ink composition clustering (3 clusters, 14 change points) may partially reflect scribal changes that correspond to Davis's bifolium-level organization.

**Novel approaches we haven't tried**: Reordering folios according to Davis's reconstructed original sequence and re-running statistical analyses to see if patterns become clearer.

---

## 4. AI AND MACHINE LEARNING APPROACHES

### 4.1 Anonymous LLM Team (2026, Unverified)

**Source**: [Infinity Explorers](https://www.infinityexplorers.com/voynich-manuscript-decoded-ai-message-2026/) (2026)

**Claim**: A custom-trained LLM, trained for 14 months on "every known ancient language, proto-language, cipher system, and undeciphered script," has decoded significant portions of the VMS. The decoded text describes astronomical events, genetic manipulation, and a warning ending in 2040. The manuscript's language is identified as a "constructed language built from mathematical principles."

**Peer-reviewed**: No. The team withheld names and institutional affiliation.

**Expert response**: Linguist Dr. Ella Marchetti (UCL) called it "pattern-matching dressed up as decryption" and noted LLMs generate "convincing-sounding outputs that are statistically plausible but semantically meaningless."

**Methodology**: Custom transformer model trained on multilingual historical corpus. No details on architecture, training data, or evaluation metrics publicly released.

**Compatibility with our findings**: **VERY LOW**. The "genetic manipulation" and "2040 warning" claims are sensationalist and have zero support from the manuscript's content or context. LLMs cannot "decode" ciphers -- they pattern-match on training data. Without the actual model, methodology, and outputs being available for scrutiny, this is not credible research.

---

### 4.2 Zelinka et al., Softcomputing Alphabet Comparison (Applied Soft Computing, 2023)

**Citation**: Zelinka, I., Lara, G., Windsor, G., Lozi, R. "Softcomputing in identification of the origin of Voynich manuscript by comparison with ancient dialects." *Applied Soft Computing* (2023). [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1568494623002351)

**Claim**: Deep learning networks and classical methods can measure visual similarity between Voynich glyphs and other alphabets. Initial results suggest similarity to ancient Indian dialects.

**Peer-reviewed**: Yes (Elsevier journal).

**Methodology**: Supercomputer-based processing; collecting alphabets from many languages/dialects; measuring visual similarity of individual characters; deep learning comparison.

**Compatibility with our findings**: **LOW**. Visual similarity of glyphs does not establish linguistic relationship. Many scripts share visual features coincidentally (e.g., Korean hangul resembles some Latin letters). Our stroke decomposition analysis focused on internal structure rather than cross-script comparison. The Indian dialect suggestion conflicts with all provenance evidence pointing to Northern Italy.

**Novel approaches we haven't tried**: Running our glyph shape data through a pre-trained OCR/handwriting recognition model to see if any known script gets high confidence matches.

---

### 4.3 Kondrak & Hauer, Hebrew Hypothesis via AI (University of Alberta, 2018, cited through 2025)

**Claim**: Algorithmic language identification using 400 languages concluded Hebrew was the most likely source language. Alphagram-based decipherment found 80%+ of decoded words in a Hebrew dictionary.

**Peer-reviewed**: Original 2018 paper was peer-reviewed.

**Compatibility with our findings**: **LOW**. The alphagram hypothesis (letters rearranged within words) is not historically attested as a cipher technique. The 80% dictionary match is misleading -- Hebrew dictionary coverage is very broad and short common words match many languages. Our analysis identified Italian/Romance grammatical patterns (d- prefix system), not Hebrew.

---

## 5. INDEPENDENT RESEARCHER CLAIMS

### 5.1 Tim Carter Clausen / "The Decipherist" (January-February 2026)

**Source**: [thedecipherist.com](https://thedecipherist.com/articles/voynich_manuscript/)

**Claim**: The VMS is a 15th-century Italian Jewish rabbi's personal reference book containing herbal medicine, astronomical calculations, ritual purity laws, and recipes. Written in Judeo-Italian using a personal cipher based on Hebrew cursive script, read right-to-left.

**Peer-reviewed**: No.

**Methodology**:
- Symbol analysis: Loop ligature identified as pronunciation marker (analogous to Hebrew dagesh)
- Visual plant identification: 73+ plants cataloged; 22 "very high confidence"
- Right-to-left reading: Produces Italian words like TORO (bull), OLIO (oil), OTTO (eight), ORO (gold)
- 10-woman pregnancy wheel (f134) interpreted as Talmudic 10-month gestation
- Research conducted with assistance from Claude (Anthropic)

**Verification status**:
- No independent Hebrew expert review
- No comprehensive alphabet or systematic decryption
- Circular reasoning risk: plant drawings confirm plant ID, which confirms Italian vocabulary
- Self-assessed at "~85% solved" with substantial untranslated content remaining

**Compatibility with our findings**: **MODERATE**. The Judeo-Italian hypothesis partially aligns with our Italian grammatical skeleton finding. Right-to-left reading is interesting but we did not test it. The Hebrew cursive script basis is plausible for 15th-century Northern Italy (significant Jewish communities in Venice, Verona, Padua). However, the lack of systematic methodology and the use of AI (Claude) for research assistance rather than quantitative analysis weakens the claim.

**Novel approaches we haven't tried**: Testing right-to-left reading of EVA transcriptions. Comparing VMS glyph shapes to Hebrew cursive forms from 15th-century Italian Jewish manuscripts.

---

### 5.2 Procedurally Generated Mnemonic Scaffold Theory (2026)

**Source**: [rocsite.com](https://rocsite.com/rocsite-voynich/)

**Claim**: The VMS text is NOT language or cipher but a procedurally generated mnemonic scaffold created by university physicians in Northern Italy (~1420 CE). The text generates "memorable nonsense syllables" to help recall botanical and medical knowledge. Text follows rules without carrying meaning.

**Peer-reviewed**: No.

**Methodology**: Not fully accessible (site returned 403 on fetch attempt). Based on search results, the theory explains Zipfian distribution and other linguistic properties as emergent from procedural generation rules.

**Compatibility with our findings**: **LOW**. Our Hurst exponent analysis (0.78-0.99) and mutual information measurements (0.445 bits) indicate the text has long-range correlations and internal structure beyond what procedural generation would typically produce. However, the "mnemonic scaffold" concept is interesting -- it would explain why the text has language-like properties without being translatable.

---

### 5.3 "Dai" Anchor Method (ResearchGate, 2025)

**Source**: Multiple papers on ResearchGate/Academia.edu (2025)

**Claim**: The recurring trigram "dai" serves as an anchor to unlock surrounding content, revealing the manuscript as an encoded compendium of botanical, astronomical, and spiritual knowledge.

**Peer-reviewed**: No.

**Compatibility with our findings**: **LOW-MODERATE**. "daiin" (which contains "dai") is the most frequent word in our analysis. We identified it as potentially encoding a function word (Italian "di" or preposition). Using it as a "crib" for surrounding decryption is methodologically sound (classic cryptanalytic technique) but the claimed translations require independent verification.

---

## 6. CONFERENCES AND COMMUNITY ACTIVITY

### 6.1 2026 International Conference on the Voynich Manuscript

**Organizer**: Medieval Academy of America / University of Malta
**Date**: Wednesday, December 9, 2026
**Format**: Online
**Website**: [https://www.um.edu.mt/events/voynich2026/](https://www.um.edu.mt/events/voynich2026/)
**Contact**: voynich2026@um.edu.mt

**Research areas sought**:
- History of the Voynich Manuscript (historical approaches, ciphers)
- Natural Language Processing techniques
- Artificial Intelligence and Machine Learning techniques
- Image processing of manuscript folios
- Interdisciplinary Digital Humanities approaches

**Critical policy**: "Proposed 'solutions' will not be accepted." Papers must present methodology and analysis, not claim definitive decipherment.

**AI policy**: Generative AI use for writing content is strictly prohibited (grammar assistance permitted).

**Submission deadlines**:
- Abstract: June 30, 2026 (750 words max)
- Full paper: August 31, 2026 (5-9 pages)
- Video presentation: November 9, 2026

**Publication**: CEUR-ART open-access proceedings.

**Relevance to our work**: Our computational analyses (entropy decay, nomenclator separation, prefix-suffix MI, Turkic rejection) would be appropriate for this venue. The "no solutions" policy means methodological contributions are preferred -- which is exactly what our statistical findings represent.

---

### 6.2 Voynich Manuscript Day 2024 & 2025

**Source**: [voynich.ninja](https://www.voynich.ninja/thread-4349.html) (2024 videos); [voynich.ninja](https://www.voynich.ninja/thread-4603.html) (2025 announcement)

Annual community events with researcher presentations. The 2024 event videos are publicly available. Details on specific presentations not fully retrieved.

---

## 7. EXPERT CONSENSUS AND SKEPTICISM

### 7.1 Current State of the Field

As of April 2026, there is **NO community-accepted decipherment** of the Voynich Manuscript -- neither partial nor complete. This is the unanimous position of:

- Lisa Fagin Davis (Medieval Academy of America)
- Claire Bowern (Yale University, linguistics)
- The Voynich Ninja community
- Cipher Mysteries blog (Nick Pelling)
- Bruce Schneier's security community

### 7.2 What IS Broadly Accepted

1. **The manuscript is genuine** -- not a modern forgery (carbon dating 1404-1438; ink analysis confirms 15th-century materials; multispectral imaging confirms no modern additions)
2. **Multiple scribes** -- at least 2 (Currier), possibly 5 (Davis)
3. **The text has linguistic properties** -- Zipf's law, word entropy ~10 bits, long-range correlations
4. **Northern Italian provenance is likely** -- stylistic analysis, historical chain of custody
5. **Simple substitution cipher has been ruled out** -- frequency analysis does not match any known language

### 7.3 What Remains Contentious

1. **Natural language vs. constructed language vs. gibberish** -- all three positions have active defenders
2. **Whether the text carries meaning at all** -- Timm & Schinner's "self-citation" stochastic process model remains credible
3. **The specific language** -- Italian, Latin, Hebrew, Turkish, and others all have advocates
4. **Whether it is a cipher, code, or something else entirely**

### 7.4 Expert Quotes

- **Dr. Ella Marchetti (UCL)** on AI decipherment: "Pattern-matching dressed up as decryption... LLMs are well-known for generating convincing-sounding outputs that are statistically plausible but semantically meaningless."
- **Lisa Fagin Davis** on Cheshire's proto-Romance theory: "This is just more aspirational, circular, self-fulfilling nonsense."
- **Ray Dillinger** (cryptographer) on information density: "Voynichese has ridiculously low information density -- ~0.33 bits per letter vs ~1.25 for English."
- **Nick Pelling** (Cipher Mysteries): Remains cautious about whether the Naibbe cipher proves anything about the actual manuscript.

---

## 8. COMPATIBILITY WITH OUR FINDINGS

### 8.1 What New Research SUPPORTS Our Model

| Our Finding | Supporting New Research |
|---|---|
| Nomenclator (code+cipher hybrid) | Naibbe cipher shows homophonic substitution can produce VMS-like text from Italian/Latin |
| Italian/Romance grammatical skeleton | Ponnaluri (2024) confirms single language; Naibbe cipher works on Italian plaintext |
| Multiple scribes | Davis (2025) identifies 5 scribes with unprecedented bifolium-level organization |
| Manuscript is genuine, not hoax | Multispectral imaging (2024) confirms no modern additions; Davis confirms medieval authenticity |
| Pharmaceutical/herbal content | Brewer & Lewis (2024) add gynecological dimension (consistent with medieval herbal tradition) |
| Text encodes meaningful information | Ponnaluri (2024): single natural language; Bowern: dismisses gibberish hypothesis |

### 8.2 What New Research CHALLENGES Our Model

| Our Finding | Challenging New Research |
|---|---|
| Nomenclator model (65% code / 35% cipher) | Naibbe cipher achieves similar statistics with PURE cipher (no code component needed) |
| d- prefix = Italian prepositions | Not directly tested or confirmed by any external study |
| ch-=plants, sh-=preparations, qo-=quantities | Positional encoding hypothesis (Cortuso) offers alternative: position in line, not prefix, carries semantic category |
| Turkic hypothesis rejected at 58% | Ardic (2025) claims 1,000+ words read; refining phonetic mappings since 2017 |
| Constructed language rejected (MI=0.445) | Anonymous LLM team (2026, unverified) claims constructed language |

### 8.3 Critical Gap: Our Nomenclator vs. Naibbe Cipher

The single most important finding for our work is the Naibbe cipher. Both models explain how plaintext becomes VMS-like text, but they make different predictions:

| Property | Our Nomenclator | Naibbe Cipher |
|---|---|---|
| Each VMS "word" encodes... | Either a code word (plant name, preparation) or 1 cipher word (preposition, conjunction) | 1-2 plaintext LETTERS |
| Original word boundaries | Partially preserved (code words = concepts) | Completely destroyed |
| Prefix categories (ch-/sh-/qo-) | Semantic (plant, preparation, quantity) | Artifact of substitution tables (no semantic meaning) |
| Why text seems repetitive | Code words for same concept recur | Same letter encoded differently each time via random table selection |
| Testable prediction | Code words should cluster by illustration type | No clustering expected by illustration type |

**Key test**: If VMS words starting with "ch-" appear disproportionately on botanical pages vs. astronomical pages, our model is supported over Naibbe. If distribution is uniform, Naibbe is favored.

---

## 9. UNTRIED APPROACHES AND GAPS

### 9.1 Approaches Found in Recent Research That We Have NOT Tried

1. **Right-to-left reading** (Clausen 2026): We have not tested R-to-L reading of EVA transcriptions. Given the Judeo-Italian hypothesis and confirmed Jewish communities in 15th-century Northern Italy, this is worth a systematic test.

2. **Folio reordering per Davis's codicology** (Davis 2025): The manuscript was rebound with misordered bifolia. Reordering according to Davis's reconstructed sequence might reveal sequential patterns invisible in the current order.

3. **Marci's decryption annotations analysis** (MSI 2024): The three columns of Roman letters on f1r, identified as Marci's decryption attempt, have not been analyzed for whether they constitute meaningful partial ciphertext/plaintext pairs.

4. **Naibbe cipher reverse-engineering**: Using Greshko's open-source code to attempt actual decryption of VMS text by brute-forcing table assignments and dice rolls across short passages.

5. **Decompression framework** (Preprint 2025): Treating EVA text as a compressed bitstream and testing decompression parameters. Historically implausible but computationally testable.

6. **Visual glyph comparison via deep learning** (Zelinka 2023): Running VMS glyphs through pre-trained handwriting recognition models to get probabilistic script family identification.

7. **Gynecological manuscript comparison** (Brewer & Lewis 2024): Systematic comparison of VMS illustrations with known medieval gynecological manuscripts.

8. **Positional semantic decoding** (Cortuso hypothesis): Testing whether word position within a line correlates with botanical morphological categories.

### 9.2 Methodological Gaps in the Field

1. **No systematic cross-validation**: No study has tested its decryption against holdout pages and had results verified by independent scholars.

2. **No Bayesian model comparison**: No study has formally compared the posterior probabilities of competing hypotheses (cipher vs. code vs. constructed language vs. gibberish) using the same statistical framework.

3. **No comprehensive glyph-to-phoneme mapping evaluation**: Multiple competing mappings exist (Ardic's Turkish, Kondrak's Hebrew, Clausen's Judeo-Italian, various Latin/Italian proposals) but no study has systematically evaluated all of them against the same validation criteria.

4. **Limited use of modern NLP**: Transformer models have NOT been seriously applied to the VMS for pattern detection (not "translation," but structural analysis). The anonymous 2026 LLM claim is not credible research.

5. **No formal information-theoretic comparison across hypotheses**: While individual entropy measurements exist, no study has computed the full information-theoretic profile (entropy at all orders, mutual information between all position pairs, transfer entropy) and compared it across proposed source languages.

---

## 10. ASSESSMENT SUMMARY TABLE

| Research | Year | Peer-Reviewed | Credibility | Aligns With Our Work | Novel for Us |
|---|---|---|---|---|---|
| Greshko, Naibbe Cipher | 2025 | Yes (Cryptologia) | HIGH | Partial (supports cipher hypothesis, challenges nomenclator) | Reverse-engineering test |
| Ponnaluri, Single Language | 2024 | Yes (Cryptologia) | HIGH | Yes (single language, not two) | Statistical methodology |
| Brewer & Lewis, Gynecological | 2024 | Yes (Oxford Academic) | MODERATE | Partial (content interpretation) | Illustration comparison |
| Davis, Codicology | 2024-25 | Academic presentation | HIGH | Yes (scribes, rebinding) | Folio reordering |
| MSI / Lazarus Project | 2024 | Data release | HIGH | Yes (cipher attempt evidence) | Marci annotation analysis |
| Zelinka et al., Softcomputing | 2023 | Yes (Elsevier) | MODERATE | Low (visual similarity) | DL glyph comparison |
| Ardic, Old Turkish | 2025 | Partial (Turkish journal) | LOW-MODERATE | Low (Turkish rejected) | Review specific mappings |
| Compression Hypothesis | 2025 | No (preprint) | LOW | Low (anachronistic) | Decompression test |
| arXiv Symbolic Decoding | 2025 | No (preprint) | VERY LOW | No (non-linguistic) | None |
| Cortuso / Padua Botanical | 2025 | No (Academia.edu) | LOW | Partial (positional encoding) | Position-based decoding |
| Clausen, Judeo-Italian | 2026 | No | LOW-MODERATE | Partial (Italian, Jewish context) | R-to-L reading test |
| Mnemonic Scaffold | 2026 | No | LOW | Low (procedural generation) | None |
| Anonymous LLM "Decoded" | 2026 | No | VERY LOW | No | None |
| Voynich Conference 2026 | 2026 | N/A | N/A | N/A | Submission opportunity |

---

## CONCLUSIONS

### The Field in 2026

The Voynich manuscript research landscape as of 2026 is characterized by:

1. **One genuinely significant peer-reviewed contribution**: Greshko's Naibbe cipher, which for the first time demonstrates a historically plausible mechanism that reproduces VMS statistical properties. This does not solve the manuscript but raises the bar for all future cipher hypotheses.

2. **Important codicological advances**: Davis's five-scribe identification and rebinding evidence fundamentally change how we should approach sequential analysis of the text.

3. **Valuable physical evidence**: The 2024 multispectral imaging release provides new data (Marci's decryption attempts, Sinapius signature) that has not been fully exploited.

4. **A proliferation of unverified claims**: The accessibility of AI tools and self-publishing platforms has produced a wave of "solution" claims, none of which have survived peer review or independent verification.

5. **An upcoming venue for serious work**: The December 2026 conference explicitly excludes "solutions" and welcomes methodological contributions -- an ideal target for our statistical findings.

### Priority Actions

1. **Test ch-/sh-/qo- prefix distribution by page type** to distinguish our nomenclator model from the Naibbe cipher model
2. **Analyze Marci's f1r annotations** from multispectral images for partial decryption information
3. **Test right-to-left reading** as a systematic alternative
4. **Consider folio reordering** per Davis's codicological findings before further sequential analysis
5. **Evaluate submission** to the December 2026 Voynich conference (abstract deadline: June 30, 2026)

---

## SOURCES

### Peer-Reviewed Publications
- [Greshko, "The Naibbe cipher" (Cryptologia 2025)](https://www.tandfonline.com/doi/full/10.1080/01611194.2025.2566408)
- [Ponnaluri, "Single natural language" (Cryptologia 2024)](https://www.tandfonline.com/doi/full/10.1080/01611194.2024.2414128)
- [Brewer & Lewis, "Women's Secrets" (Social History of Medicine 2024)](https://academic.oup.com/shm/article-abstract/37/3/559/7633883)
- [Zelinka et al., Softcomputing (Applied Soft Computing 2023)](https://www.sciencedirect.com/science/article/pii/S1568494623002351)

### Preprints
- [Compression-Based Hypothesis (Preprints.org 2025)](https://www.preprints.org/manuscript/202509.0403)
- [Voynich Codex Decoded (arXiv 2025)](https://arxiv.org/abs/2505.02261)
- [Algorithmic Coding Hypothesis (ResearchGate 2025)](https://www.researchgate.net/publication/395381163)

### Codicological Research
- [Davis, Multispectral Imaging (Manuscript Road Trip 2024)](https://manuscriptroadtrip.wordpress.com/2024/09/08/multispectral-imaging-and-the-voynich-manuscript/)
- [Davis, Voynich Codicology (Manuscript Road Trip 2025)](https://manuscriptroadtrip.wordpress.com/2025/01/19/voynich-codicology/)
- [Davis, "Materiality" presentation (Cipher Mysteries 2025)](https://ciphermysteries.com/2025/10/11/lisa-fagin-davis-the-materiality-of-the-voynich-manuscript)
- [Voynich Manuscript scans (Art Newspaper 2024)](https://www.theartnewspaper.com/2024/09/25/voynich-manuscript-scans-reveal-early-decoding-attempt)

### News Coverage of Naibbe Cipher
- [Archaeology Magazine (2026)](https://archaeologymag.com/2026/01/voynich-manuscript-may-be-a-cipher/)
- [Live Science (2026)](https://www.livescience.com/archaeology/mysterious-voynich-manuscript-may-be-a-cipher-a-new-study-suggests)
- [Art Newspaper (2026)](https://www.theartnewspaper.com/2026/01/07/can-a-new-cipher-help-to-explain-the-mysterious-voynich-manuscript)
- [Newsweek (2026)](https://www.newsweek.com/voynich-manuscript-15th-century-book-cards-dice-cipher-naibbe-11316017)
- [IFLScience (2026)](https://www.iflscience.com/is-this-how-the-voynich-manuscript-was-made-a-new-cipher-offers-fascinating-clues-81786)
- [Schneier on Security (2025)](https://www.schneier.com/blog/archives/2025/12/substitution-cipher-based-on-the-voynich-manuscript.html)
- [Sci.News (2026)](https://www.sci.news/othersciences/linguistics/voynich-manuscript-cipher-14466.html)
- [Greshko's project page](https://www.michaelgreshko.com/naibbe-cipher)

### Independent Researchers
- [Clausen / The Decipherist (2026)](https://thedecipherist.com/articles/voynich_manuscript/)
- [Ardic, Turkish hypothesis](https://www.turkicresearch.com/files/articles/17.pdf)
- [Cortuso hypothesis (Academia.edu 2025)](https://www.academia.edu/144430098/The_solution_to_the_Voynich_Manuscript_12Oct25_10th_draft)

### Expert Commentary
- [Language Log (2024)](https://languagelog.ldc.upenn.edu/nll/?p=65930)
- [Schneier blog + comments (2025)](https://www.schneier.com/blog/archives/2025/12/substitution-cipher-based-on-the-voynich-manuscript.html)

### Community and Conferences
- [2026 Voynich Conference CFP (Medieval Academy)](https://www.themedievalacademyblog.org/call-for-papers-the-voynich-manuscript/)
- [Voynich.ninja forum](https://voynich.ninja/)
- [Voynich.nu reference site](https://voynich.nu/)
- [Cipher Mysteries blog](https://ciphermysteries.com/)
- [Voynich Revisionist blog](https://voynichrevisionist.com/)

### Open-Source Code and Data
- [Greshko Naibbe cipher code (GitHub)](https://github.com/greshko/naibbe-cipher)
