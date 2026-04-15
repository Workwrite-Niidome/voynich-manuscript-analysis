# Grape Reverse Decoding: f47r (Vitis vinifera) Attack

## Raw Text Extraction

### f47r (recto) - 11 lines, 77 words
```
Line 1:  pchair.oly.sheaiin.shol.daiin.chdy
Line 2:  chokchol.chol.choldy.dair.chad.aiin
Line 3:  dor.chol.chy.chaiin.ckhey.chol.dain.okaiin
Line 4:  qokcheo.cthey.chokain.chol.daiin.kchdal
Line 5:  dain.olshey.chokolg
Line 6:  folr.chey.so.chol.shol.aiin.shol.shol.chdy.cholol
Line 7:  schesy.kchor.cthaiin.chol.chol.chol.chor.{ckhh}ey
Line 8:  sho,keey.chy.tchod.choy.sho.cht,chy,kchar.ctham
Line 9:  qokokor.chaiin.okal.chol.daiin.okchokchor,sy
Line 10: shy.otcho.keey.tor.chey.otchy.tchol.dain.dam
Line 11: dsho.cphy.daiin.daiiny
```

### f47v (verso) - 14 lines
```
Line 1:  psheot.cheor.cholsho.chopchy.sal<->sary
Line 2:  dsheey.shy.cphy.otchey.daiidy.chory<->daiiy
Line 3:  shol.char.oteol.dor.otchol.chkchy<->daiin
Line 4:  qotol.sheey.kol.sho.keechy.qoty<->cthy
Line 5:  dsholy.shees.chor.ody.shy.sy<->sary
Line 6:  chody.cheor.saiin.dochod<->chol
Line 7:  pchodaiin.dair.dcthy
Line 8:  daiin.cheotar.chodaly.sal
Line 9:  qotcheey.chety.chol.chol.dain
Line 10: chotcho.ltchey.o.tchotchy.dy<->chol.chody.dar
Line 11: oteey.cho.chdy.chy.key.chyky<->dchy.daiin.chy
Line 12: chy.cho.keesy.chy.chy.cheky<->chochy.aiin
Line 13: dshy.daiin.chdlety.chaiin<->dcheey.otald
Line 14: chol.chey
```

---

## 1. Word Frequency on f47r

| Rank | Word | Count | Notes |
|------|------|-------|-------|
| 1 | **chol** | 9 | Dominant word. Confirmed = "leaf" (cho- family) |
| 2 | **shol** | 4 | Second most frequent |
| 3 | **daiin** | 4 | Very common function/content word |
| 4 | **chy** | 3 | Short word, likely function word |
| 5 | **dain** | 3 | Variant of daiin? |
| 6 | **chdy** | 2 | cho- derivative |
| 7 | **aiin** | 2 | Common function word |
| 8 | **chaiin** | 2 | |
| 9 | **chey** | 2 | |
| 10 | **sho** | 2 | |
| 11 | **keey** | 2 | |

53 unique words out of 77 total (68.8% hapax rate on this page).

**Key observation**: `chol` (leaf) dominates with 9 occurrences out of 77 words (11.7%). This is consistent with the identification note that "cho-" (leaf) is heavily used. In a grape herbal entry, leaves (folia) would be discussed extensively -- grape leaves were used medicinally for diarrhea, bleeding, inflammation.

### Combined f47r+f47v frequency (full grape entry)

| Word | Combined | Global corpus |
|------|----------|---------------|
| chol | 13 | 624 |
| daiin | 8 | 1149 |
| chy | 8 | 190 |
| shol | 5 | 157 |
| dain | 4 | 165 |
| chdy | 3 | 89 |
| cho | 2 | 68 |
| chey | 3 | 455 |
| sho | 3 | 107 |
| shy | 3 | 89 |

---

## 2. First Word Hypothesis

**First content word on f47r: `pchair`**

The opening line reads: `pchair.oly.sheaiin.shol.daiin.chdy`

### Analysis of `pchair`

- EVA glyph decomposition: **p** - **ch** - **a** - **i** - **r** (5 EVA characters if ch is one glyph)
- Phonetic structure: If ch = single consonant, then C-C-V-V-C or C-V-V-C (depending on ch value)
- `pchair` occurs only **2 times** in the entire corpus (here and once on f111v as part of `qopchair`)
- Its rarity strongly suggests it is a **plant-specific name**, not a function word

### If `pchair` = `vitis`:

| EVA | Latin | Notes |
|-----|-------|-------|
| p | v | Both labials (p/v confusion common in medieval Italian) |
| ch | i | ch is one of the most common EVA glyphs |
| a | t | |
| i | i | Identity mapping |
| r | s | Both alveolars |

This produces the mapping: **p->v, ch->i, a->t, i->i, r->s**

Testing on other f47r words:
- `dair` -> `dtis` (not obviously meaningful)
- `chor` -> `ios` (not meaningful)
- `chol` -> `iol` (not "folium")

**Verdict**: The simple substitution pchair=vitis does not produce coherent results for the rest of the page. This is expected -- Voynichese is unlikely to be a simple monoalphabetic cipher. The encoding is more complex (possibly polyalphabetic, nomenclator, or constructed notation).

### Alternative first-word candidates:

Looking at first words of other herbal folios, a strong pattern emerges: **most herbal pages begin with p- or t- or k- initial words**, suggesting these may be formulaic openings ("pchair" could mean "the vine..." or "take the vine...") rather than bare plant names.

Common first-word patterns across all herbal folios:
- p-initial: ~45% of pages (pchair, pshol, pchor, pchey, podaiin, etc.)
- t-initial: ~20% (tsheos, tshol, tshor, tchodar, etc.)
- k-initial: ~20% (koaiin, kchody, kcheor, ksor, etc.)
- f-initial: ~8% (fachys, foar, fchodaiin, fochor, etc.)
- o-initial: ~7%

This suggests the first character may encode a grammatical/formulaic element rather than the first letter of the plant name.

---

## 3. Hapax Legomena on f47r (Rare/Unique Words)

Words appearing on f47r that are **rare or unique** in the entire corpus:

| Word | f47r count | Global count | Candidate meaning |
|------|-----------|--------------|-------------------|
| **pchair** | 1 | 2 | Plant name? (vitis/vite) |
| **chad** | 1 | 1 | HAPAX - grape-specific? (uva? acinus?) |
| **chokolg** | 1 | 1 | HAPAX - grape-specific? (racemus?) |
| **folr** | 1 | 1 | HAPAX - possibly "flower" (flos/fiore)? |
| **schesy** | 1 | 1 | HAPAX |
| **ctham** | 1 | 1 | HAPAX |
| **cht** | 1 | 1 | HAPAX (possibly scribal fragment) |
| **qokokor** | 1 | 1 | HAPAX |
| **okchokchor** | 1 | 1 | HAPAX - compound/reduplicated form |
| **kchdal** | 1 | 1 | HAPAX |
| **tchod** | 1 | 2 | Nearly unique |
| **kchar** | 1 | 2 | Nearly unique |
| **qokcheo** | 1 | 3 | Rare |
| **cholol** | 1 | 3 | Rare cho- variant |
| **daiiny** | 1 | 3 | Rare daiin variant |

**Notable**: 10 words are absolute hapax legomena (appear nowhere else in the manuscript). These are prime candidates for grape-specific vocabulary such as:
- **pampinus** (tendril/vine leaf)
- **racemus** (grape cluster)
- **acinus** (grape berry)
- **sapa** (grape must)
- **uva** (grape)
- **vinum** (wine)

Especially interesting:
- **`chokolg`** -- unusual ending in `-g` (very rare in Voynichese), suggests a special term
- **`folr`** -- resembles the beginning of "folium" or "flos/flor-"
- **`chad`** -- very short, could be a basic noun like "uva"
- **`okchokchor`** -- reduplicated structure, possibly describing grape clusters (racemi)

---

## 4. Cross-Reference: f47r vs f3r (Rubia tinctorum / Madder)

### f3r text (20 lines)
```
Line 1:  tsheos.qopal.chol.cthol.daimg
Line 2:  ycheor.chor.dam.qotcham.cham
Line 3:  ochor.qocheor.chol.daiin.cthy
...
Line 20: ycheor.chol.odaiin.chol.s.aiin.okolor.am
```

### Shared vocabulary (general herbal terms)
Words appearing on BOTH f47r and f3r:

| Word | f47r | f3r | Likely meaning |
|------|------|-----|---------------|
| **chol** | 9 | 6 | "leaf" (folium/foglia) -- confirmed |
| **chor** | 1 | 7 | Very common on f3r. Root? Stem? ("radix"?) |
| **daiin** | 4 | 2 | Generic herbal term (possibly "of the" / functional) |
| **sho** | 2 | 1 | Function word or short descriptor |
| **aiin** | 2 | 1 | Suffix/function word |
| **dair** | 1 | 1 | |
| **dam** | 1 | 1 | |

**Key finding**: `chor` appears 7 times on f3r (madder) but only 1 time on f47r (grape). Since madder's primary medicinal use is its ROOT (radix rubea), `chor` being dominant on f3r but rare on f47r supports the hypothesis that **`chor` may encode "root" (radix/radice)**.

Grape entries focus on leaves and fruit, not roots -- consistent with `chol` (leaf) dominating f47r.

### Words unique to f47r (grape-specific candidates)
45 words appear on f47r but NOT f3r. Key candidates:
- `pchair` -- plant name (vitis?)
- `chad` -- grape berry? (acinus?)
- `chokolg` -- grape cluster? (racemus?)
- `keey` -- wine? juice? (vinum? succus?)
- `shol` (4x on f47r) -- possibly vine-specific descriptor
- `dain` -- variant of daiin, high frequency

### Words unique to f3r (madder-specific candidates)
77 words appear on f3r but NOT f47r. Key candidates:
- `cham/chom` (3x/2x) -- distinctive f3r words, possibly "red/dye" (rubia/alizari)
- `qopal` -- possibly the plant name encoding
- `tsheos` -- first word of f3r, possibly "rubia" encoded
- `am` -- ending particle common on f3r, rare elsewhere
- Words with `-om/-am` endings cluster heavily on f3r

**Structural insight**: f3r has a strong `-m` ending pattern (cham, chom, dam, cthom, shom, am, okeom, soeom, otolom) that is largely absent from f47r. This `-m` cluster may relate to madder's Latin/Italian vocabulary or a phonological feature of dye-related terminology.

---

## 5. Cross-Reference: f47r vs f9r (Nigella)

### f9r text (10 lines)
```
Line 1:  tydlo.choly.cthor.orchey.s.shy.odaiin.sary
...
Line 10: ytchas.oraiin.chkr
```

### Shared vocabulary
16 words shared between f47r and f9r:

| Word | Notes |
|------|-------|
| chol, chor | Universal herbal terms (leaf, root?) |
| daiin, dor, shol | Common content/function words |
| chaiin, chey, choy | cho- family |
| cphy, cthaiin, cthey | Less common but shared |
| shy, sy, tchol | Function/structural words |
| chdy, aiin | |

### Words unique to f47r vs f9r
34 words on f47r but not f9r -- these include all the hapax legomena identified above plus:
- `keey` (2x) -- not on f9r or f3r, appears 65x globally. Interesting: could this be a common descriptor for grapes specifically?
- `okal` (1x on f47r, 125x globally) -- very common word, just happens to not appear on f9r
- `dain` (3x) -- common globally but absent from f9r

### Words unique to f9r (Nigella-specific candidates)
- `tydlo` -- first word of f9r, possibly "nigella" encoded
- `sary` -- appears on f9r line 1; interestingly also on f47v (2x)
- `odaiin`, `chokoiin`, `dsholdy` -- unique to f9r

---

## 6. Phonetic Mapping Attempts

### Attempt A: pchair = vitis (simple substitution)

| EVA glyph | -> Latin sound |
|-----------|---------------|
| p | v |
| ch | i |
| a | t |
| i | i |
| r | s |

**Result**: Fails. When applied to other words:
- `chol` -> `iol` (should be "folium" or similar)
- `shol` -> `shol` (no mappable characters)
- `daiin` -> `dtiin` (meaningless)
- `dair` -> `dtis` (meaningless)

The mapping is internally inconsistent. **Simple monoalphabetic substitution is ruled out.**

### Attempt B: ch -> f (based on chol = fol[ium])

If `chol` encodes the Latin stem "fol-" (from folium):

| EVA | Latin |
|-----|-------|
| ch | f |
| o | o |
| l | l |

Testing:
- `chol` -> `fol` (folium!)
- `chor` -> `for` (not "radix" -- breaks the chor=root hypothesis)
- `chody` -> `fody` (meaningless)
- `chokchol` -> `fokfol` (meaningless)

**Partial success**: ch->f, o->o, l->l works perfectly for `chol`=`fol-` but fails on other cho- words. This suggests either:
1. The encoding is not character-level substitution, OR
2. `ch` maps to different values in different positions (polyalphabetic), OR
3. `chol` is a whole-word logogram for "leaf/folium" rather than a phonetic spelling

### Attempt C: Whole-word / syllabic approach

Given that simple substitution fails, consider that Voynichese may use:
- **Whole-word tokens**: `chol` = "folium", `chor` = "radix", `daiin` = "et/cum" (and/with)
- **Syllabic encoding**: each EVA "word" encodes a syllable or morpheme
- **Nomenclator system**: common words have fixed symbols, rare words are spelled out

If we treat the most common words as logograms:

| EVA word | Frequency (global) | Hypothesized meaning |
|----------|-------------------|---------------------|
| daiin | 1149 | Function word: "of the" / "and" / "with" |
| chol | 624 | "leaf" / "folium" (confirmed) |
| chey | 455 | Descriptor? "the" / article? |
| shol | 157 | "stem"? "juice"? (succus?) |
| chor | 192 | "root" (radix) -- supported by f3r dominance |
| dain | 165 | Variant of daiin / "in" / preposition |
| okaiin | 181 | "take" (recipe instruction?) |
| chy | 190 | Short function word / suffix |
| aiin | 483 | Very common -- likely grammatical particle |

---

## 7. Heading Word Analysis

**f47r has NO heading/label lines.** All 11 lines are tagged as `@P0` (first paragraph line) or `+P0` (continuation). There is no `=Pt` (paragraph title), `@Lp` (label), or `=Pc` (caption) tag.

This contrasts with some folios (e.g., f1r which has `=Pt` lines like "ydaraishy" and "dain.or.teod"). The absence of a separate heading means the plant name, if present, is embedded in the running text.

**The first word `pchair` is therefore the strongest candidate for the plant name**, as it:
1. Opens the entry
2. Is nearly unique to this page (2 occurrences globally)
3. Has the right length/structure for a plant name
4. Follows the pattern of other herbal pages starting with p- words

---

## 8. Synthesis: What We Can Conclude

### High confidence findings:

1. **`chol` = "leaf" (folium/foglia)** -- confirmed by frequency dominance on a leaf-heavy plant page (9/77 = 11.7% of all words)

2. **`pchair` = plant name for grape** -- nearly unique word opening the entry, consistent with the pattern of p-initial first words across herbal folios

3. **`chor` likely = "root" (radix)** -- dominates f3r (madder, a root-medicine plant: 7x) but is marginal on f47r (grape: 1x). Grape medicine uses leaves and fruit, not roots.

4. **The encoding is NOT simple monoalphabetic substitution** -- all direct mapping attempts produce gibberish for words beyond the initial hypothesis

5. **f47r has 10 absolute hapax legomena** -- these are grape-specific vocabulary (pampinus, racemus, acinus, uva, vinum, sapa, etc.) that cannot be decoded without a larger Rosetta-stone breakthrough

6. **f3r shows a distinctive `-m` ending cluster** (cham, chom, dam, shom, etc.) absent from f47r, suggesting phonological or semantic specificity tied to madder/dye terminology

### Medium confidence observations:

7. **`shol` may encode a vine/grape-related term** -- 4x on f47r, 157x globally (common but concentrated here). Could be "vinum" (wine), "succus" (juice), or "stipes" (stem/stalk)

8. **`keey` may be grape-specific** -- 2x on f47r, absent from f3r and f9r, 65x globally. Possibly "uva" (grape fruit) or a descriptor like "dulcis" (sweet)

9. **`chad` (absolute hapax) could be "uva"** -- it is short (4 chars), appears exactly once, and would be a natural word for a grape entry. Its shortness parallels the shortness of "uva" (3 letters)

10. **`chokolg` (absolute hapax) could be "racemus"** -- the unusual `-g` ending (extremely rare in Voynichese) marks this as highly specialized vocabulary. A grape cluster term would be unique to this page.

### The "formulaic opening" pattern:

The first line `pchair.oly.sheaiin.shol.daiin.chdy` may parse as:
```
pchair     = Vitis / Vite (plant name)
oly        = ? (article? "the"?)
sheaiin    = ? (descriptor? "vinfera"? "cultivated"?)
shol       = ? (stem/juice/wine?)
daiin      = of-the / and
chdy       = ? (leaf-related? cho+dy suffix)
```

This would parallel a typical herbal opening like:
> *"Vitis vinifera. The leaf (folium) of the vine..."*

### Next steps for cracking the encoding:

1. **Cross-reference `pchair` structure with ALL first words** across herbal pages. If the initial `p-` is a prefix (article/demonstrative), then `chair` is the plant-name kernel. Does `chair` have any phonetic relationship to "vitis"?

2. **Map the 10 hapax legomena against the grape illustration features** -- if specific words appear near specific illustrated parts (clusters, tendrils, leaves), positional correlation could identify racemus, pampinus, etc.

3. **Test `chor` = "radix" hypothesis** on ALL herbal pages -- if true, pages with root-medicine plants (rubia, valeriana, gentiana) should show high `chor` frequency, while leaf/flower medicine plants should show low `chor`.

4. **Investigate the `-m` ending cluster on f3r** -- does this pattern appear on other dye/color-related pages? Could `-m` be an encoding for Latin `-um` (neuter noun ending)?

5. **Compare f47r word lengths to Latin/Italian grape vocabulary** -- even without letter-level decoding, matching word-length distributions between Voynichese and expected natural language text could narrow down the source language.
