# Semitic Root-and-Pattern Morphology Hypothesis: Voynich Manuscript Analysis

## Corpus Statistics
- **Total words extracted**: 37,030 tokens
- **Unique word forms**: 8,850
- **Source**: RF1b-e.txt (EVA transcription, full herbal + other sections)

---

## 1. Consonant Root Extraction

Two scenarios were tested, reflecting the ambiguous status of EVA 'o':

### Scenario A: o = vowel (stripped along with a, e, i)
- **Unique consonant skeletons**: 3,698

| Root | Freq | Example forms |
|------|------|---------------|
| r | 1,097 | ar, air, aiir, or, oar, ear |
| l | 980 | al, ol, el, ail, eal, aeol |
| dn | 978 | daiin (669), dain (147), dan (12) |
| chy | 947 | chey (487), cheey, chy, cheoy |
| n | 851 | aiin (552), ain (128), an (6) |
| qky | 749 | qokey, qokeey, qoky |
| chl | 663 | chol (345), chal (54), cheel, chel |
| chdy | 642 | chody (77), chedy, cheedy |
| ky | 614 | key (33), keey (67), okey, okeey |
| shy | 606 | shey (333), sheey, shy |

### Scenario B: o = consonant (only a, e, i stripped)
- **Unique consonant skeletons**: 5,560

| Root | Freq | Example forms |
|------|------|---------------|
| chy | 878 | chey, cheey, chy |
| dn | 867 | daiin, dain, dan |
| n | 758 | aiin, ain, an |
| qoky | 720 | qokey, qokeey, qoky |
| r | 673 | ar, air, er |
| shy | 569 | shey, sheey, shy |
| qokn | 556 | qokaiin (255), qokain (271) |
| ol | 543 | ol, oal, oel |
| chol | 510 | chol, cheol, choal |
| chdy | 470 | chdy, chedy, cheedy |

### Phonemic Tokenization (digraphs ch, sh, cth, ckh, cph, cfh as single units)
- **Unique phonemic roots (o=vowel)**: 3,699
- **Unique phonemic roots (o=consonant)**: 5,561

---

## 2. Root-Pattern Paradigm Tables

### Key paradigm: Root d-n (phonemic, o=vowel) -- 32 forms

This is the most convincing Semitic-like paradigm in the corpus:

| Word | Pattern | Vowels | Freq |
|------|---------|--------|------|
| daiin | CVVVC | aii | 669 |
| dain | CVVC | ai | 147 |
| daiiin | CVVVVC | aiii | 20 |
| dan | CVC | a | 12 |
| diin | CVVC | ii | 5 |
| deiin | CVVVC | eii | 3 |
| din | CVC | i | 2 |
| dein | CVVC | ei | 1 |

This looks superficially like a Semitic paradigm where different vowel patterns on the same root yield different grammatical forms. However, notice that the "vowel variation" is mostly about the **number of 'i' characters** (ii vs iii vs i), not about qualitatively different vowel patterns (as in Arabic CaCaC/CuCuC/CiCaC).

### Root ch-l (phonemic, o=vowel) -- 18 forms

| Word | Pattern | Vowels | Freq |
|------|---------|--------|------|
| chol | CVC | o | 345 |
| chal | CVC | a | 54 |
| cheel | CVVC | ee | 1 |
| chel | CVC | e | 3 |
| cheol | CVVC | eo | 44 |
| cheeol | CVVVC | eeo | 10 |

This is more interesting -- same root with genuinely different vowel qualities (o/a/e/ee/eo). But note that "chol" and "chal" could also be entirely different words rather than paradigmatic variants.

### Root ch-d-y (phonemic, o=vowel) -- 18 forms

| Word | Pattern | Vowels | Freq |
|------|---------|--------|------|
| chody | CVCC | o | 77 |
| chedy | CVCC | e | 52 |
| cheedy | CVVCC | ee | 9 |
| cheody | CVVCC | eo | 53 |
| chdy | CCC | (none) | 1 |

### Root q-k-n (phonemic, o=vowel) -- 26 forms

| Word | Pattern | Vowels | Freq |
|------|---------|--------|------|
| qokaiin | CVCVVVC | oaii | 255 |
| qokain | CVCVVC | oai | 271 |
| qokan | CVCVC | oa | 8 |
| qokiin | CVCVVC | oii | 2 |
| qokeaiin | CVCVVVVC | oeaii | 1 |

### Roots with 5+ distinct forms (phonemic, o=vowel): **428 roots**
### Roots with 5+ distinct forms (phonemic, o=consonant): **246 roots**

---

## 3. Most Common Vowel Patterns (Top 20)

### With o = vowel (phonemic tokenization)

| Rank | Pattern | Count | % | Examples |
|------|---------|-------|---|----------|
| 1 | CVC | 4,201 | 11.3% | dar, kar, kor, chol, shor |
| 2 | CVVC | 1,941 | 5.2% | dain, kair, shear, cheol |
| 3 | CVCC | 1,877 | 5.1% | chedy, chely, qety |
| 4 | VC | 1,834 | 5.0% | ar, es, ey, ol, or |
| 5 | CVCVC | 1,733 | 4.7% | chalor, chepol, qokar |
| 6 | VCVC | 1,589 | 4.3% | okar, oker, okol, otal |
| 7 | CVVVC | 1,464 | 4.0% | daiin, shaiin, cheear |
| 8 | CCVC | 1,250 | 3.4% | tchal, ychoy, ypar |
| 9 | CVCVVC | 1,233 | 3.3% | qokain, qokeey, shodain |
| 10 | VCVVC | 1,065 | 2.9% | okeal, okeol, oteal |
| 11 | CC | 902 | 2.4% | dy, ky, ty |
| 12 | C | 896 | 2.4% | s, r, y |
| 13 | CCC | 834 | 2.3% | kchy, pchy, shfy |
| 14 | CVCVVVC | 797 | 2.2% | qokaiin, chokaiin |
| 15 | VCVVVC | 770 | 2.1% | okaiin, otaiin |
| 16 | CCVVC | 706 | 1.9% | lkaim, tshoar, ycheol |
| 17 | VVVC | 690 | 1.9% | aiin, oees |
| 18 | VCC | 581 | 1.6% | oly, ods, otr |
| 19 | VCCVC | 524 | 1.4% | okchoy, olkor, oydar |
| 20 | CCVCC | 489 | 1.3% | ydoly, ykory, chdoly |

### Comparison with Arabic

In Arabic, the dominant patterns for triliteral roots are:
- **CaCaC** (fa'ala): basic verb form
- **CaCiC**: active participle
- **CuCuC** (fu'ul): plural pattern
- **CiCaC**: verbal noun
- **maCCuC**: passive participle

The Voynich top pattern **CVC** (11.3%) corresponds structurally to Arabic CaC (a biconsonantal pattern), not CaCaC. The second most common is **CVVC** (5.2%), which matches Arabic CaCiC or similar. However, the Voynich patterns are dominated by **variable-length vowel sequences** (ii, iii, ee, eee) rather than by qualitatively different vowel patterns, which is NOT how Arabic morphology works.

---

## 4. Analysis of Key Words

### The "chol" Problem

| Word | Freq | Phonemic root (o=V) | Phonemic root (o=C) |
|------|------|---------------------|---------------------|
| chol | 345 | ch-l (2 consonants) | ch-o-l (3 consonants) |
| shol | 164 | sh-l (2 consonants) | sh-o-l (3 consonants) |
| chor | 196 | ch-r (2 consonants) | ch-o-r (3 consonants) |
| cthol | 52 | cth-l (2 consonants) | cth-o-l (3 consonants) |

If 'o' is a vowel, then "chol" has root ch-l = only **2 consonants** (biconsonantal). This is too short for a standard Semitic triconsonantal root.

If 'o' is a consonant, then "chol" has root ch-o-l = **3 consonants** (triconsonantal). This fits Semitic structure. But then it has NO vowels at all, meaning the word itself is a bare root -- possible in Semitic (like Arabic imperatives), but unusual for a running text to consist mostly of bare roots.

### The "chol" family (o=vowel analysis)

| Word | Freq | Root |
|------|------|------|
| chol | 345 | ch-l |
| otchol | 24 | t-ch-l |
| kchol | 22 | k-ch-l |
| choly | 21 | ch-l-y |
| qokchol | 17 | q-k-ch-l |
| dchol | 16 | d-ch-l |
| tchol | 15 | t-ch-l |

This suggests prefixing (ot-, k-, qok-, d-, t-) on a base "chol" -- which is more consistent with **agglutinative** morphology (prefix + stem) than Semitic root-and-pattern morphology. In Arabic, you don't typically stack different consonantal prefixes onto a root; instead you change the internal vowel pattern.

### Systematic prefix/suffix patterns

| Ending | Count | % of corpus |
|--------|-------|-------------|
| -ey | 5,061 | 13.7% |
| -y (other) | 4,965 | 13.4% |
| -dy | 4,750 | 12.8% |
| -aiin | 3,787 | 10.2% |
| -ol | 3,272 | 8.8% |
| -ar | 2,695 | 7.3% |
| -or | 2,005 | 5.4% |
| -al | 1,980 | 5.3% |
| -ain | 1,617 | 4.4% |
| -am | 735 | 2.0% |

These endings are extremely productive and consistent. Nearly 40% of all words end in -y, -ey, or -dy. Over 10% end in -aiin. This is more characteristic of **suffixal morphology** than Semitic internal vowel ablaut.

---

## 5. Biliteralism vs. Triliteralism

### Phonemic Root Length Distribution

#### o = vowel
| Consonants | Tokens | % |
|-----------|--------|---|
| 0 | 131 | 0.4% |
| 1 | 4,613 | **12.5%** |
| 2 | 13,406 | **36.2%** |
| 3 | 12,364 | **33.4%** |
| 4 | 4,775 | 12.9% |
| 5+ | 1,741 | 4.7% |

#### o = consonant
| Consonants | Tokens | % |
|-----------|--------|---|
| 0 | 23 | 0.1% |
| 1 | 2,919 | 7.9% |
| 2 | 7,893 | **21.3%** |
| 3 | 10,976 | **29.6%** |
| 4 | 8,857 | **23.9%** |
| 5+ | 6,362 | 17.2% |

### Comparison with Arabic
- **Arabic**: ~80% of roots are triconsonantal (3 consonants)
- **Voynich (o=vowel)**: Peak at **2 consonants** (36.2%), with 3 consonants close behind (33.4%)
- **Voynich (o=consonant)**: Peak at **3 consonants** (29.6%), but much more evenly distributed

### Assessment

**(a) Biconsonantal root system?**
If o=vowel, the system is heavily biconsonantal (36.2% of tokens). This does not match any known natural Semitic language, though the theoretical "Proto-Semitic biconsonantal substratum" hypothesis exists. However, 12.5% monoconsonantal roots (e.g., just "r" or "l") is far too high for any morphological system -- these are likely function words or suffixes incorrectly parsed as standalone words.

**(b) A different morphological system that resembles Semitic?**
The data more strongly suggests an **agglutinative** system with:
- A small set of stem morphemes (ch-l, sh-l, d-n, etc.)
- Productive prefixes (o-, qo-, ot-, ok-, y-, s-, d-, k-, t-, p-)
- Productive suffixes (-y, -ey, -dy, -aiin, -ain, -ol, -or, -al, -ar, -am)
- Limited internal vowel variation (mostly "ee" expansion, not qualitative ablaut)

This is structurally different from Semitic morphology, which changes internal vowels while keeping prefixes/suffixes relatively fixed.

**(c) EVA transcription errors masking consonants?**
This is possible. If some EVA "vowels" (particularly sequences like 'ii', 'iii', 'ee', 'eee') actually encode consonants or consonant clusters, the root analysis would shift. The extreme length variability of vowel sequences (ii vs iii vs iiii) is suspicious -- it might represent different consonantal glyphs rather than true vowel length.

---

## 6. Judeo-Arabic Pharmaceutical Texts in 15th-Century Italy

### Historical Evidence

There is strong historical evidence for Judeo-Arabic medical/pharmaceutical manuscripts in the Italian context:

1. **The Sicilian Codex of David ben Shalom** (15th century): A Jewish physician in Sicily compiled three major medical texts in Judeo-Arabic (Arabic written in Hebrew characters), including works by Avicenna and al-Majusi. This demonstrates active transmission of Arabic medical knowledge through Jewish intermediaries in Italy.

2. **Hebrew Herbal Codex Parisinus 1199** (15th century, Northern Italy): A herbal manuscript from northern Italy where plant descriptions were translated from Latin sources but adapted for a Jewish audience. Each entry gives plant names in Hebrew and Latin with pharmaceutical preparation details.

3. **Cairo Genizah Pharmaceutical Lists** (11th-14th centuries): Extensive materia medica lists in Judeo-Arabic document the drugs held and sold by Jewish pharmacists, establishing a long tradition of Judeo-Arabic pharmaceutical notation.

4. **Cross-cultural medical exchange**: The 15th century saw rich cultural exchanges among Latin, Jewish, and Arabic medical traditions, particularly in Sicily and southern Italy, with Jewish physicians serving as key intermediaries between Arabic and Latin medical knowledge.

### Relevance to the Voynich Hypothesis

A Judeo-Arabic pharmaceutical notation system would:
- Use a **Semitic morphological base** (Arabic root system)
- Be written in **non-Arabic script** (Hebrew characters, or potentially a novel cipher script)
- Include **technical abbreviations** and shorthand for pharmaceutical preparations
- Be produced by a bilingual community familiar with both Arabic and European medical traditions

However, true Judeo-Arabic retains full Arabic morphology (triconsonantal roots, standard verb forms, etc.) simply written in Hebrew script. The Voynich word structure does NOT look like abbreviated Arabic -- the root lengths are wrong (too short), the vowel patterns are wrong (quantitative variation rather than qualitative ablaut), and the suffix system is too regular and productive.

### Recent Scholarly Work

A 2025 study published on Zenodo ("Structural Convergence Between the Voynich Manuscript and Arabic Root Morphology") claims quantitative evidence for convergence between Voynich word families and Arabic root systems (Spearman rho ~ 0.82). However, this measures statistical correlation of family sizes, not direct morphological correspondence.

---

## Verdict: Is the Voynich Morphology Semitic?

### Evidence FOR Semitic-like morphology:
1. Words clearly decompose into consonant-skeleton + vowel-pattern
2. Some roots show multiple vowel patterns (ch-l: chol/chal/chel/cheol)
3. Root reuse ratio (2.39 words/root) is in the ballpark of Semitic (3-5)
4. The phoneme inventory has Semitic-like characteristics (rich consonants, few vowels)
5. Historical plausibility (Judeo-Arabic medical texts existed in 15th-century Italy)

### Evidence AGAINST Semitic-like morphology:
1. **Root length is wrong**: Dominant root length is 2 consonants (36.2%), not 3 (Arabic standard). Even treating o as consonant gives a flat distribution, not the sharp triconsonantal peak of Arabic.
2. **Vowel variation is quantitative, not qualitative**: daiin/daiiin/dain differ in number of i's, not in vowel quality. Arabic paradigms use CaCaC/CuCuC/CiCaC (different vowels), not CaCiC/CaCiiC/CaCiiiC (same vowels, different lengths).
3. **The suffix system is too productive**: Nearly 40% of words end in -y/-ey/-dy, and 10% end in -aiin. This looks agglutinative, not Semitic.
4. **Prefix stacking**: Words like qo-k-chol suggest stacking of functional prefixes onto a stem, which is more agglutinative than Semitic.
5. **The top roots are too common**: r, l, n as standalone "roots" (covering 8% of the corpus) are more likely grammatical particles than true lexical roots.
6. **Root distribution across folios**: Top roots appear on 60-94% of all folios, meaning they are ubiquitous function words, not content-specific lexical items.

### Most Likely Interpretation

The Voynich text appears to use a **prefix-stem-suffix agglutinative structure** that superficially resembles Semitic root-and-pattern morphology but differs in fundamental ways:

- **Semitic**: Root is an abstract consonantal skeleton; meaning is carried by the root; grammatical function is carried by the vowel pattern
- **Voynich**: Stem is a concrete syllable (chol, sho, dar); prefixes and suffixes carry grammatical/semantic modification; internal vowel variation is limited and mostly quantitative

The system is more reminiscent of:
- A **constructed language** with a small morpheme inventory
- A **notation system** with systematic abbreviation conventions
- An **agglutinative natural language** (Turkish, Hungarian) rather than a Semitic one
- Or a system where EVA transcription obscures the true phonological structure

The Judeo-Arabic pharmaceutical hypothesis remains historically plausible but morphologically unsupported by this analysis. The word structure does not match Arabic (even abbreviated or vernacular Arabic) at the level of root-and-pattern morphology.

---

## Sources

- [Course in medieval medical manuscripts in Judeo-Arabic (Primo Levi Center)](https://primolevicenter.org/printed-matter/course-in-medieval-medical-manuscripts-in-judeo-arabic/)
- [Early Modern Judaeo-Arabic Medical Manuscripts (Woolf Institute, Cambridge)](https://www.woolf.cam.ac.uk/blog/early-modern-judaeo-arabic-medical-manuscripts)
- [Medieval Mediterranean Pharmacology (NCBI)](https://www.ncbi.nlm.nih.gov/books/NBK606146/)
- [The Jewish Presence in Arabic Writings on Medicine and Pharmacology (Chipman, 2013)](https://compass.onlinelibrary.wiley.com/doi/10.1111/rec3.12063)
- [Cairo Genizah Pharmaceutical Lists (PubMed)](https://pubmed.ncbi.nlm.nih.gov/17113257/)
- [Hebrew Herbal: Already Verified (Academia.edu)](https://www.academia.edu/121231930/)
- [Structural Convergence Between Voynich and Arabic Root Morphology (Zenodo, 2025)](https://zenodo.org/records/17409830)
- [On the Biradical Origins of the Semitic Triradical Root System](https://www.sigmatica.org/1-on-the-biradical-origins-of-the-semitic-triradical-root-system.html)
- [Crux of the MATTR: Voynichese Morphological Complexity (CEUR-WS)](https://ceur-ws.org/Vol-3313/paper9.pdf)
- [Judeo-Arabic (Wikipedia)](https://en.wikipedia.org/wiki/Judeo-Arabic)
