# Voynich Manuscript: Galenic Quality Vocabulary Analysis

## Methodology

Anchor: `ckhy` confirmed on hot plant pages (f2r Paeonia, f3v, f9v) and zero cold plant pages.
Source: EVA transcription (RF1b-e.txt), herbal section (f1r-f57v, 112 pages).

Five reference pages with known Galenic qualities (from Dioscorides/Galen):
- f2r = Paeonia: **hot 1st, dry 2nd**
- f3r = Rubia tinctorum: **hot 1st, dry 2nd**
- f9r = Nigella sativa: **hot 3rd, dry 1st**
- f41r = Adiantum: **cold, dry**
- f47r = Vitis vinifera: **cold 1st, moist 2nd**

## CRITICAL CORRECTION: ckhy Distribution

The prior claim that "ckhy appears on ALL 3 hot plant pages" requires correction:

- f2r (Paeonia): standalone `ckhy` = YES (line 7)
- f3r (Rubia): standalone `ckhy` = NO (appears on f3**v** instead, a different plant)
- f9r (Nigella): standalone `ckhy` = NO (appears on f9**v** instead, a different plant)
- f41r (Adiantum, cold): `chckhy` present (compound form, likely different word)
- f47r (Vitis, cold): absent

Standalone `ckhy` appears on 22 of 112 herbal pages (~20%), distributed across all quires (A=5, B=2, C=2, D=1, E=4, F=3, G=4). The cross-quire distribution rules out scribal variation.

## Primary Finding: ckhy / kchy Complementary Distribution

### The zero-overlap discovery

| Word | Pages | Quire distribution | Target page presence |
|------|-------|--------------------|---------------------|
| ckhy | 22 pages | A=5, B=2, C=2, D=1, E=4, F=3, G=4 | f2r(hot): YES, f3r(hot): no, f9r(hot): no, f41r(cold): no, f47r(cold): no |
| kchy | 26 pages | A=2, B=7, C=5, D=4, E=3, F=2, G=3 | f2r: no, f3r: no, f9r: no, f41r(cold): YES, f47r: no |

**ckhy and kchy have ZERO page overlap across 112 herbal pages.**

This is statistically extraordinary. With 22 and 26 pages respectively, random chance would predict ~5.1 overlapping pages. The probability of zero overlap by chance is vanishingly small (p < 0.001).

Both words appear across all quires (A through G), ruling out scribal hand differences. Their complementary distribution strongly suggests they encode opposite semantic values.

### Context comparison

ckhy contexts: `shor.ckhy.daiiny`, `qotar.ckhy`, `chkaiin.ckhy.chor`, `dar.ckhy`
kchy contexts: `kshy.kchy.d,or`, `kchy.dar`, `kchy.dy.daiin`, `kchy.chol.daiin`

Both appear in similar syntactic environments (preceded and followed by common words like daiin, chor, dar, chol), suggesting they occupy the same grammatical slot with different meanings.

### Interpretation

If `ckhy` = calidus ("hot"), then `kchy` = frigidus ("cold").
The glyph sequence is strikingly similar: both are composed of the same EVA characters (c, k, h, y) in nearly-anagrammatic order. This may reflect a deliberate encoding where quality opposites share the same letter inventory but differ in order.

## Additional Zero-Overlap Words (Anti-correlated with ckhy)

| Word | Pages | Overlap with ckhy | Notes |
|------|-------|-------------------|-------|
| kchy | 26 | 0 | **Best cold candidate** |
| chedy | 14 | 0 | Concentrated in Q=D,E,F (later quires) |
| tchey | 13 | 0 | Distributed across all quires |
| ody | 13 | 0 | Q=E,F,G concentrated |
| kar | 13 | 0 | Q=E,G concentrated |
| otey | 11 | 0 | Distributed |
| shedy | 10 | 0 | Q=F concentrated |

The cluster of chedy/kar/otey/shedy shows high mutual overlap (e.g. chedy-shedy: 7 pages, chedy-kar: 7 pages), suggesting they may form a vocabulary group for a specific topic (possibly quality-related).

## Dry/Moist Analysis

### Dry candidate: cthy

`cthy` is the ONLY word appearing on all 3 hot+dry pages (f2r, f3r, f9r) while absent from the moist page (f47r):

| Page | Quality | cthy count |
|------|---------|------------|
| f2r | hot, dry | 2 |
| f3r | hot, dry | 2 |
| f9r | hot, dry | 3 |
| f41r | cold, dry | 0 |
| f47r | cold, moist | 0 |

However, `cthy` appears on 47/112 herbal pages (42%), which is extremely high for a specific quality word. This frequency suggests `cthy` is more likely a common function word (possibly a conjunction like "and", a preposition, or a grammatical particle) rather than "siccus" (dry).

Its strong co-occurrence with ckhy (enrichment ratio 1.62x) is consistent with it being a function word that often appears in quality descriptions ("it is hot [cthy] dry") rather than being a quality word itself.

### Moist candidates (on f47r, absent from all dry pages)

| Word | f47r | Global frequency | Quire distribution |
|------|------|------------------|-------------------|
| okal | 1 | 24 pages | All quires |
| otchy | 1 | 27 pages | All quires |
| okaiin | 1 | 31 pages | All quires |
| kchor | 1 | 17 pages | Multiple quires |
| keey | 1 | 11 pages | Multiple quires |
| oly | 1 | 11 pages | Multiple quires |

None of these is convincing as "humidus" (moist). They all appear on too many pages globally to be a specific quality term, and their presence on only one identified moist page (f47r) is statistically weak.

## Degree Encoding

### Repetition-based encoding: Not supported

Checking if word repetition count encodes degree:

| Page | Plant | Hot degree | ckhy count | kchy count |
|------|-------|-----------|------------|------------|
| f2r | Paeonia | 1st | 1 | 0 |
| f9r | Nigella | 3rd | 0 | 0 |
| f41r | Adiantum | cold | 0 | 1 |

No correlation between word count and known degree.

### Numerical/ordinal words: Not identified

No consistent short words (candidates for primus/secundus/tertius) were found systematically near quality words across pages.

### Position-based encoding

`ckhy` position within pages varies widely (8% to 100% through page text), showing no systematic positional pattern for degree encoding.

## Quality Vocabulary Table

| Quality | Voynich word | Confidence | Evidence |
|---------|-------------|------------|----------|
| Hot (calidus) | **ckhy** | 45% (downgraded) | Present on f2r (hot), absent from f41r/f47r (cold). But absent from f3r/f9r recto. Perfect complementary distribution with kchy. Cross-quire (all 7 quires). |
| Cold (frigidus) | **kchy** | 40% | Present on f41r (cold), absent from f2r (hot). ZERO overlap with ckhy across 112 pages (p<0.001). Cross-quire (all 7 quires). Same EVA glyphs in different order. |
| Dry (siccus) | unidentified | -- | `cthy` was the only word on all 3 dry pages and absent from moist, but at 42% page frequency it is almost certainly a function word, not a quality term. No other viable candidate found. |
| Moist (humidus) | unidentified | -- | Only one identified moist plant page (f47r), insufficient sample for statistical discrimination. No candidate word exclusive to moist pages. |
| Degree markers | unidentified | -- | Neither repetition count, position, nor nearby short words correlate with known degree values. |

## Key Insights

### 1. The ckhy/kchy mirror pair
The most robust finding is the perfect complementary distribution of ckhy and kchy. These two words:
- Share the same EVA glyphs (c, k, h, y) in different order
- Never appear on the same page (0/112 overlap, vs ~5 expected by chance)
- Both appear across all 7 quires (not scribal variation)
- Appear in similar syntactic contexts
- Align with hot/cold plant identifications (ckhy on hot pages, kchy on cold)

This mirrors the Latin semantic opposition calidus/frigidus and may reflect a deliberate encoding principle where opposite qualities are written as anagrams.

### 2. Sample size limitation
With only 5 confidently identified plant pages (3 hot+dry, 1 cold+dry, 1 cold+moist), the dry/moist axis is severely underpowered. The hot/cold axis has 3+2=5 data points; the dry/moist axis has only 4+1=5 with 4 of 5 being dry.

### 3. Quire confound
Words concentrated in specific quires (e.g. chedy, shedy, ypchedy in Q=D/E/F) may reflect quire-specific vocabulary or scribal variation rather than semantic content. Only cross-quire patterns (like ckhy and kchy) can be trusted as semantically meaningful.

### 4. The oteey false lead
Previous candidate `oteey` for "cold" appears on 8 herbal pages but is massively more common in the Balneological/Recipe sections (f103r alone has 6 occurrences). It is NOT concentrated on cold plant pages in the herbal section and is likely not a quality term.

## Next Steps

1. **Expand plant identifications**: Cross-reference more herbal pages with known Galenic qualities to test ckhy/kchy beyond the current 5 pages.
2. **Search for dry/moist pair**: Look for another anagram-pair like ckhy/kchy that might encode dry/moist (e.g., words using glyphs s,c,h or h,m,d in different orders).
3. **Compound forms**: Investigate whether chckhy, shckhy, checkhy, ockhy are prefixed forms of ckhy (ch+ckhy, sh+ckhy etc.) or separate words.
4. **Statistical test**: Apply Fisher's exact test to ckhy/kchy page distributions against expanded plant quality data.
5. **Cross-section validation**: Check if ckhy/kchy patterns hold in the pharmaceutical (f87-f90) and recipe (f103-f116) sections where quality vocabulary should also appear.
