# Multi-Plant Triangulation Analysis: Voynich Encoding System

## Method
Using 5 plant identifications (ranked by confidence) to test whether EVA text
encodes recognizable plant names, and if so, how.

## 1. Plant Name Comparison Table

| Folio | Plant (Latin) | Italian | Conf. | First EVA word | First line words |
|-------|--------------|---------|-------|----------------|-----------------|
| f47r | Vitis vinifera | vite/uva | 70% | `pchair` | pchair, oly, sheaiin, shol, daiin, chdy |
| f9r | Nigella damascena | nigella/gittone | 65% | `tydlo` | tydlo, choly, cthor, orchey, s, shy, odaiin, sary |
| f3r | Rubia tinctorum | robbia/rubia | 60% | `tsheos` | tsheos, qopal, chol, cthol, daimg |
| f41r | Adiantum capillus-veneris | capelvenere | 60% | `psheykedaleey` | psheykedaleey, oked, shekeeey, opshes... |
| f2r | Paeonia officinalis | peonia | 55% | `kydainy` | kydainy, ypchol, daiin, otchal, ypchaiin, ckholsy |

### Label text (rare in herbal section -- only a few folios have them):
- **f2r**: `ytoail` (label) + `ios.an.on` (additional label)
- **f41v** (verso of f41r): `keesedal` (label)
- No labels on f47r, f9r, f3r

## 2. Consonant Skeleton Test

### Target consonant skeletons (with v->f, b->p, g->k substitutions for EVA):

| Plant name | Raw consonants | EVA-equivalent |
|-----------|---------------|----------------|
| vitis | v-t-s | f-t-s |
| vite | v-t | f-t |
| nigella | n-g-l-l | n-k-l-l |
| rubia | r-b | r-p |
| adiantum | d-n-t-m | d-n-t-m |
| paeonia | p-n | p-n |

### Results: NO exact consonant skeleton matches found.

For each target page, no EVA word had a consonant skeleton matching the
Latin or Italian plant name. This is a **strong negative result** that rules
out simple substitution cipher where plant names appear as single words.

Key observations:
- f47r (grape): No word with consonants (f,t,s) or (f,t)
- f9r (nigella): No word with consonants (n,k,l,l)
- f3r (rubia): No word with consonants (r,p)
- f41r (adiantum): No word with consonants (d,n,t,m) -- only `daiin`=(d,n) as partial
- f2r (peonia): No word with consonants (p,n)

## 3. Phonetic Mapping Tests

Two mapping systems tested (Bax-style and alternative with f->v):

| Folio | EVA 1st word | Bax reading | Alt reading | Target name |
|-------|-------------|------------|------------|-------------|
| f47r | pchair | pkair | pchair | vitis/vite |
| f9r | tydlo | tydlo | tdlo | nigella |
| f3r | tsheos | tseos | tsheos | rubia |
| f41r | psheykedaleey | pseykedaleey | pshekedalee | adiantum |
| f2r | kydainy | kydny | kdn | paeonia |

**Result**: No phonetic mapping produces recognizable plant names from the
first words. Exhaustive search of ALL words on each page also yielded zero
matches with any mapping tested.

## 4. Page-Unique / Rare Words (Best Plant-Name Candidates)

Words appearing only 1-3 times in the entire herbal section, unique to each page:

### f47r (grape) -- 52 unique words, 17 rare:
- `pchair` (p,ch,r) -- unique first word, possible title
- `chad` (ch,d)
- `chokolg` (ch,k,l,g) -- unusual ending -g
- `folr` (f,l,r) -- only word starting with 'f' on this page
- `ctham` (cth,m)
- `tchod` (t,ch,d)
- `schesy` (s,ch,s)

### f9r (nigella) -- 72 unique words, 20 rare:
- `tydlo` (t,d,l) -- unique first word
- `ram` (r,m)
- `toeoky` (t,k)
- `dayty` (d,t)
- `dsholdy` (d,sh,l,d)
- `koraiin` (k,r,n)
- `cfhdosal` (cfh,d,s,l)

### f3r (madder) -- 87 unique words, 20+ rare:
- `tsheos` (t,sh,s) -- first word
- `qopal` (q,p,l) -- second word
- `daimg` (d,m,g) -- unusual ending -g
- `chag` (ch,g)
- `dago` (d,g)
- `oporar` (p,r,r) -- very unusual word
- `cholcthom`, `otchom`, `qokeom`, `soeom`, `okeom` -- many -om endings

### f41r (maidenhair fern) -- 79 unique words, 20+ rare:
- `psheykedaleey` (p,sh,k,d,l) -- long first word
- `opshes` (p,sh,s)
- `chkchod` (ch,k,ch,d)
- `parchdy` (p,r,ch,d)
- `chekeey`, `cheked` -- unique forms
- `qokedy` appears 7 times (most frequent content word!)

### f2r (peony) -- 82 unique words, 20+ rare:
- `kydainy` (k,d,n) -- first word
- `ypchaiin` (p,ch,n)
- `fodan` (f,d,n)
- `dlssho` (d,l,s,sh)
- `dorchory` (d,r,ch,r)
- `ckholsy` (ckh,l,s)

## 5. Key Distinctive Features Per Page

### f3r stands out dramatically with -m/-om endings
- **23 out of 111 words (20.7%)** end in -m or -mo
- Compare: f2r: 0%, f9r: 1.3%, f41r: 0%, f47r: 2.7%
- Words: dam, cham (x3), cthom, chom (x2), shom, qotcham, otaldam, sheoldam,
  schodam, tsheoarom, otchom, qokeom, soeom, okeom, pcheoldom, otolom, sam, am
- This could indicate Latin -um/-am case endings, or a morphological feature
  of the plant description

### f41r dominated by -edy/-dy endings
- **32 out of 95 words (33.7%)** end in -dy
- The word `qokedy` appears 7 times (highest frequency content word)
- Cluster of related forms: okedy, chekedy, qotedy, ypchedy, chedy

### f2r has distinctive -an endings
- `dan` appears 4 times (highly distinctive; TF-IDF = 9.66)
- Multiple -an words: dan, chan, shan, an

### f47r: heavy use of `chol` (9 times) and compound words
- `chokchol`, `cholol`, `okchokchorsy` -- elaborate compounds

## 6. Vocabulary Overlap Analysis

Words shared between ALL 5 target pages: **only `daiin`**

This confirms `daiin` is a high-frequency function word (probably "of", "the",
or a grammatical particle), not a plant-specific term.

Shared between pairs (function words only):
- f47r-f9r: 15 shared words (mostly function words)
- f47r-f2r: 13 shared words
- f9r-f2r: 16 shared words
- f41r shares very few words with other pages (only 3-4 shared with each)

**f41r has the most distinctive vocabulary** -- almost no overlap with other
herbal pages. This may reflect:
1. A different scribal hand (Currier B language?)
2. Different subject matter encoding
3. A different section of the manuscript

## 7. Critical Assessment: Is The Plant Name Encoded?

### Hypothesis 1: Plant name as single word -- REJECTED
No word on any target page has a consonant structure matching the expected
plant name under any reasonable substitution cipher.

### Hypothesis 2: Plant name as first word -- INCONCLUSIVE/UNLIKELY
The first words (pchair, tydlo, tsheos, psheykedaleey, kydainy) show no
phonetic resemblance to their putative plant names under any tested mapping.

### Hypothesis 3: Plant name is described, not named -- POSSIBLE
The text may describe plant properties rather than name plants. Evidence:
- f3r's heavy -m endings could be Latin descriptive adjectives (-um/-am)
- f41r's repetitive `qokedy` could describe a property of the fern
- No recognizable plant name words found anywhere on these pages

### Hypothesis 4: The encoding is not a simple substitution -- SUPPORTED
The complete failure of consonant skeleton matching rules out:
- Simple monoalphabetic substitution
- Simple polyalphabetic with known period
- Direct phonetic encoding of Latin/Italian plant names

What remains possible:
- Nomenclator system (plant names encoded as arbitrary codewords)
- Steganographic system (meaningful content hidden in word structure)
- Constructed/artificial language with no simple mapping to natural languages
- The plant identifications may be incorrect

## 8. The f2r Label: A Possible Rosetta Stone?

f2r has actual label text: `ytoail` and `ios.an.on`

If f2r = Paeonia (peony):
- `ytoail` -- consonants (t,l). Does not match "peonia" (p,n)
- `ios` -- only appears once in entire herbal section
- `an.on` -- could be Latin/Italian fragments?

The label `ios.an.on` is intriguing because it looks more like natural language
fragments than typical Voynichese. However, it does not obviously encode "peonia"
or "paeonia" either.

### f41v label: `keesedal`
- Consonants: (k,s,d,l)
- If f41 = Adiantum: target consonants (d,n,t,m) -- no match
- If encoding "capelvenere": target (k,p,l,f,n,r) -- partial k- match only

## 9. Morphological Signature Theory

Each page has a distinctive morphological "fingerprint":

| Folio | Dominant ending | Distinctive feature |
|-------|----------------|-------------------|
| f3r | -m, -om, -am | 20.7% of words end in -m |
| f41r | -edy, -dy | 33.7% end in -dy; `qokedy` x7 |
| f2r | -an, -aiin | `dan` x4 distinctive |
| f47r | -ol | `chol` x9 dominates |
| f9r | -aiin, -thy | more diverse endings |

This suggests the Voynich text may use **morphological suffixes** that vary
by topic/context, not by plant name. The -m endings on f3r might relate to
madder's use as a dye (processing instructions?), while -dy on f41r might
relate to the fern's delicate structure.

## 10. Conclusions

### What we learned:
1. **Plant names are NOT encoded as recognizable single words** under any
   simple substitution system. This is the strongest finding.

2. **Each page has distinctive morphological patterns** (ending distributions)
   that differentiate it from other pages, suggesting the text does encode
   page-specific content -- it is not random or meaningless.

3. **The vocabulary overlap is minimal** between pages dealing with different
   plants, which is consistent with genuine botanical descriptions.

4. **f41r is linguistically distinct** from the other 4 pages, sharing almost
   no vocabulary. This aligns with the Currier A/B language distinction.

5. **The encoding system, if present, operates at a deeper level** than simple
   letter-for-letter substitution. Possible models include:
   - A nomenclator (table of arbitrary codewords for common terms)
   - An agglutinative constructed notation
   - A syllabary-based system where EVA "words" are syllable sequences

### What this means for decipherment:
The triangulation approach cannot crack the Voynich because the encoding
(if it exists) does not preserve the phonetic structure of plant names at
the word level. Any successful decipherment will need to either:
- Identify the codebook/nomenclator if one was used
- Determine sub-word-level mappings (syllable or morpheme level)
- Accept that the text may describe plants without naming them
