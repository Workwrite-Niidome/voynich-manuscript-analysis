# Plant Code Generation Rule Analysis

## The Core Problem

We concluded that Voynich plant name codes (first words of herbal folios) are "arbitrary codes" with no recoverable pattern. But a 15th-century author could not memorize 200+ arbitrary codes without a generation rule. This document systematically tests every plausible mnemonic or derivation system.

## Anchor Data

| Folio | Code (EVA) | Plant (Latin) | Italian | Dioscorides |
|-------|-----------|---------------|---------|-------------|
| f2r | kydainy | Paeonia officinalis | peonia | III.140 |
| f3r | tsheos | Rubia tinctorum | robbia | III.143 |
| f9r | tydlo | Nigella damascena | nigella/melanzio | III.79 |
| f41r | psheykedaleey | Adiantum capillus-veneris | capelvenere | IV.134 |
| f47r | pchair | Vitis vinifera | vite/uva | V.1 |

---

## TEST 1: Abbreviation of Latin/Italian Names

### 1a. First syllable + last syllable

| Plant | First+Last | Code | Match? |
|-------|-----------|------|--------|
| Pae-o-ni-a | pae+nia = paenia | kydainy | NO |
| Ru-bi-a | ru+bia = rubia | tsheos | NO |
| Ni-gel-la | ni+la = nila | tydlo | NO |
| A-di-an-tum | a+tum = atum | psheykedaleey | NO |
| Vi-tis | vi+tis = vitis | pchair | NO |

**RESULT: No match. Abbreviation does not produce the codes.**

### 1b. Consonant skeleton

| Plant | Consonants | Code consonants (EVA) |
|-------|-----------|----------------------|
| Paeonia | P-N | K-D-N |
| Rubia | R-B | T-SH-S |
| Nigella | N-G-L-L | T-D-L |
| Adiantum | D-N-T-M | P-SH-K-D-L |
| Vitis | V-T-S | P-CH-R |

Nigella (N-G-L-L) vs tydlo (T-D-L): The L matches position, but N->T and G->D are inconsistent with other mappings. No systematic consonant skeleton correspondence.

**RESULT: No match. Consonant skeletons are structurally different.**

### 1c. Name backwards

| Plant | Reversed | Code | Any resemblance? |
|-------|----------|------|-------------------|
| Paeonia | ainoaep | kydainy | Both end in -ainy/-aep. Very weak |
| Rubia | aibur | tsheos | NO |
| Nigella | allegin | tydlo | NO |
| Adiantum | mutnaida | psheykedaleey | NO |
| Vitis | sitiv | pchair | NO |

**RESULT: No match.**

### 1d. First letter of each syllable (acrophonic)

| Plant | Syllable initials | Code |
|-------|------------------|------|
| Pae-o-ni-a | P.O.N.A | kydainy |
| Ru-bi-a | R.B.A | tsheos |
| Ni-gel-la | N.G.L | tydlo |
| A-di-an-tum | A.D.A.T | psheykedaleey |
| Vi-tis | V.T | pchair |

No EVA characters in the codes correspond to these initials under any consistent mapping.

**RESULT: No match.**

---

## TEST 2: Derivation from Dioscorides Chapter Numbers

### 2a. Direct numerical encoding

| Plant | Chapter | Code | Digits in code? |
|-------|---------|------|----------------|
| Paeonia | III.140 | kydainy | 1-4-0? |
| Rubia | III.143 | tsheos | 1-4-3? |
| Nigella | III.79 | tydlo | 7-9? |
| Adiantum | IV.134 | psheykedaleey | 1-3-4? |
| Vitis | V.1 | pchair | 1? |

For this to work, we need a number-to-EVA mapping. Testing: if each EVA glyph = a digit...

Paeonia (140): k=1, y=4, d=0? Then Rubia (143): t=1, sh=4, e=3? But k=1 and t=1 would be the same digit with different glyphs -- this is only plausible if the book number is encoded in the initial character (III=k/t, IV=p, V=p?). Testing:

- Book III plants: kydainy (k-), tsheos (t-), tydlo (t-) -- mixed k and t for same book
- Book IV plants: psheykedaleey (p-) -- p for IV?
- Book V plants: pchair (p-) -- p for V too?

The initial letter does NOT consistently encode the Dioscorides book number.

### 2b. Chapter number as position in alphabet/sequence

If 140 = the 140th word in some list, or maps to a specific syllable combination:
- No known 15th-century numerical cipher uses chapter numbers this way
- The chapter numbers themselves vary between Dioscorides editions
- Different medieval copies had different chapter ordering

**RESULT: No plausible numerical encoding found. Chapter numbers do not map to codes.**

---

## TEST 3: Derivation from a Key Text

### 3a. Pater Noster test

"Pater noster qui es in caelis sanctificetur nomen tuum adveniat regnum tuum fiat voluntas tua sicut in caelo et in terra panem nostrum quotidianum da nobis hodie et dimitte nobis debita nostra sicut et nos dimittimus debitoribus nostris et ne nos inducas in tentationem sed libera nos a malo amen"

If the Nth word encodes the plant at position N:
- Word 1: Pater → f1r? (fachys)
- Word 2: noster → f2r? (kydainy = Paeonia)
- Word 3: qui → f3r? (tsheos = Rubia)

No phonetic resemblance between "noster" and "kydainy", or between "qui" and "tsheos".

### 3b. Psalm-based key

Common cipher psalms: Psalm 51 (Miserere), Psalm 23 (Dominus regit me), Psalm 91, Psalm 119.

For any psalm-based system, we'd need a consistent mapping rule from psalm words to EVA codes. Since there's no phonetic resemblance at the word level (established in Test 1), a psalm key would require an additional layer of encoding -- making memorization HARDER, not easier. This contradicts the premise that a generation rule aids memory.

### 3c. Herbal text as key

The most natural key text would be a known herbal (Dioscorides Latin translation, Macer Floridus, etc.). If the code is the Nth word from the entry for that plant in a known herbal:

- Dioscorides on Paeonia (III.140) begins: "Paeonia quam aliqui glycyside..." 
- No word in typical Dioscorides Paeonia entries resembles "kydainy"

**RESULT: No key text produces the codes. Moreover, a key text cipher adds complexity rather than reducing memorization burden.**

---

## TEST 4: Mnemonic Method of Loci / Property Encoding

### 4a. Positional character = property hypothesis

If each EVA character position encodes a plant property:

| Code | 1st | 2nd | 3rd | 4th+ | Plant |
|------|-----|-----|-----|------|-------|
| kydainy | k | y | d | ainy | Paeonia |
| tsheos | t | sh | e | os | Rubia |
| tydlo | t | y | d | lo | Nigella |
| psheykedaleey | p | sh | e | ykedaleey | Adiantum |
| pchair | p | ch | a | ir | Vitis |

Testing 1st character = plant family:
- k: Paeonia (Ranunculaceae)
- t: Rubia (Rubiaceae), Nigella (Ranunculaceae) -- DIFFERENT families for same initial
- p: Adiantum (Pteridaceae), Vitis (Vitaceae) -- DIFFERENT families for same initial

1st character does NOT encode plant family.

Testing 1st character = growth habit:
- k: Paeonia (perennial herb)
- t: Rubia (perennial climber), Nigella (annual herb) -- DIFFERENT habits
- p: Adiantum (fern), Vitis (woody vine) -- DIFFERENT habits

1st character does NOT encode growth habit.

### 4b. Medical use encoding

- k: Paeonia (epilepsy, gynecology)
- t: Rubia (dye, bladder stones), Nigella (digestion, snakebite)
- p: Adiantum (respiratory), Vitis (diarrhea, inflammation)

No consistent medical-use grouping by initial character.

### 4c. Cross-checking with other codes

Plants with similar properties and their codes:
- Climbers: Rubia (tsheos), Vitis (pchair), Bryonia/torshor -- all different initials
- Fleshy-rooted: Paeonia (kydainy), Mandragora/pchocthy, Arum/pshol -- mixed
- Blue-flowered: Nigella (tydlo), Borago/tshol, Gentiana/pdrairdy -- mixed

**RESULT: No positional property encoding detected. Characters at each position do not correlate with any botanical property across plants.**

---

## TEST 5: Structural Patterns in the Codes

### 5a. The p- prefix (42% of codes)

Already documented: 42% of codes begin with p-. If p- is a removable prefix (article, classifier), what remains?

| Code | Stripped | Plant |
|------|---------|-------|
| pchair | chair | Vitis |
| pshol | shol | Arum |
| pchocthy | chocthy | Mandragora |
| pchodaiin | chodaiin | Symphytum |
| psheykedaleey | sheykedaleey | Adiantum |
| psheoky | sheoky | Glechoma |
| pchodar | chodar | Arum italicum |

After stripping p-: "chair" for grape, "shol" for arum, "chocthy" for mandrake. These stripped forms still show no phonetic resemblance to plant names. Moreover, non-p- codes (kydainy, tsheos, tydlo) are not more recognizable.

The p- prefix may be a grammatical marker (e.g., "plant" or an article) but removing it does not reveal the generation rule.

### 5b. Clustering by plant property

Sorting codes by plant family to check for clustering:

**Ranunculaceae** (buttercup family):
- kydainy (Paeonia), tydlo (Nigella), pydchdom (Aconitum?), pshdaiin (Aconitum?)
- Codes: k-yd..., t-yd..., p-yd..., p-sh...
- NOTABLE: kydainy and tydlo share the "-yd-" element! And pydchdom also has "-yd-"!

**Lamiaceae** (mint family):
- fcholdy (Mentha?), pchor (Thymus?)
- No shared element

**Asteraceae** (daisy family):
- tshor (Taraxacum?), fshody (Centaurea?), tshdar (Scabiosa?)
- Shared: tsh- appears in tshor and tshdar, but fshody breaks the pattern

### 5c. THE "-yd-" CLUSTER -- A POTENTIAL LEAD

Three Ranunculaceae plants share "-yd-":
- **k-yd-ainy** = Paeonia (Ranunculaceae, formerly Paeoniaceae)
- **t-yd-lo** = Nigella (Ranunculaceae)
- **p-yd-chdom** = Aconitum? (Ranunculaceae)

Additionally, pykydal (f45r, Alchemilla/Potentilla -- Rosaceae, NOT Ranunculaceae) contains -yd-. This weakens but does not destroy the pattern since visual identification is only 35% confidence.

Testing more broadly for shared code elements among related plants:

**Arum-type (Araceae)**:
- pshol (f8r, Arum maculatum)
- pchodar (f28r, Arum italicum)
- Both have p- prefix but different stems

**Thistle-type (Asteraceae/Carduoideae)**:
- pcheoepchy (f34r, Cirsium)
- pcheocphy (f46r, Eryngium -- actually Apiaceae, not Asteraceae)
- These share "pcheo-" prefix! Both are spiny/thistle-like plants.

### 5d. Alphabetical sorting of codes

| Code | Plant candidate |
|------|----------------|
| fachys | Laurus |
| fchaiin | Lamium |
| fchodaiin | Helleborus |
| fcholdy | Mentha |
| foar | Papaver/Datura |
| fshody | Centaurea |
| kchody | Aristolochia |
| kdchody | Fumaria |
| keedey | Angelica |
| kodalchy | Rosmarinus |
| ksor | Symphytum |
| kydainy | Paeonia |
| okeeesy | Plantago |
| pchair | Vitis |
| pchey | Echinops |
| pchocthy | Mandragora |
| pchodaiin | Symphytum |
| pchodar | Arum italicum |
| pchor | Astragalus/Thymus |
| pdrairdy | Gentiana |
| pocheody | Cannabis |
| podaiin | Potentilla/Iris |
| pol | Polygala |
| porory | Chrysanthemum |
| posaiin | Convallaria |
| psheoky | Glechoma |
| psheykedaleey | Adiantum |
| pshol | Arum |
| pshdaiin | Aconitum |
| psheor | Centaurea/Cynara |
| pykydal | Alchemilla |
| pydchdom | Aconitum |
| tarodaiin | Rubia (cult.) |
| tolor | Dipsacus |
| tocphol | Polygonum |
| torshor | Bryonia |
| tshor | Taraxacum |
| tshdar | Scabiosa |
| tsheos | Rubia |
| tshol | Borago |
| tsholdchy | Paeonia variant? |
| tshodpy | Bryonia/Humulus |
| tydlo | Nigella |

Adjacent codes in alphabetical order do NOT correspond to botanically related plants. The codes do not form an ordered botanical classification.

**RESULT: The "-yd-" cluster in Ranunculaceae and "pcheo-" in thistle-types are suggestive but not conclusive. With only 5 anchors at 55-70% confidence, apparent clusters may be coincidental.**

---

## TEST 6: Sound-Based Mnemonics (Substitution Cipher)

### 6a. The critical test: kydainy -> peonia

Attempting to find a letter-for-letter substitution:

```
k y d a i n y
p e o n i a ?
```

Proposed mapping: k->p, y->e, d->o, a->n, i->i, n->a

Wait -- "kydainy" has 7 characters in this decomposition, "peonia" has 6. Let's try treating EVA digraphs as single units:

```
EVA:    k  y  d  a  i  n  y
Target: p  e  o  n  i  a  (extra y?)
```

Mapping attempt A: k=p, y=e, d=o, a=n, i=i, n=a, final y = suffix marker

### 6b. Apply Mapping A to other codes

Testing k=p, y=e, d=o, a=n, i=i, n=a:

**tydlo -> Nigella (melanzio)**
```
t  y  d  l  o
?  e  o  l  o
```
Under Mapping A: t is unmapped, but tydlo -> ?eolo. This doesn't match "nigella" (nikella?) or "melanzio".

**tsheos -> Rubia (robbia)**
```
t  sh  e  o  s
?  ?   ?  ?  ?
```
None of these characters appear in Mapping A (except possibly treating 'e' as from mapping, but 'e' doesn't appear in Mapping A's domain -- 'a' maps to 'n', not 'e').

**MAPPING A FAILS immediately on the second plant.** The k->p, y->e, d->o mapping that makes "kydainy" look like "peonia" does not work for any other code.

### 6c. Systematic substitution search

For each anchor pair, compute ALL possible single-character substitution mappings:

**kydainy <-> peonia:**
- k->p, y->e, d->o, a->n, i->i, n->a (as above, plus extra y)
- Alternative: treat "ai" as a digraph, "ny" as a digraph
  - k->p, y->e, d->o, ai->ni, ny->a? (broken)

**tydlo <-> nigella:**
- t->n, y->i, d->g, l->e, o->l, (missing final -la)
- Or: t->n, y->i, d->g, l->el, o->la (multi-char mapping)

**tsheos <-> robbia:**
- t->r, sh->o, e->b, o->b, s->ia (multi-char, inconsistent)
- Or: t->r, sh->ob, e->b, o->i, s->a (incoherent)

**pchair <-> vitis:**
- p->v, ch->i, a->t, i->i, r->s
- Or: p->v, ch->it, air->is (partial)

**psheykedaleey <-> capelvenere (Italian) or adiantum (Latin):**
- Way too long for simple substitution against either name

### 6d. Cross-consistency check

Mapping from kydainy->peonia: k=p, y=e, d=o
Mapping from tydlo->nigella: t=n, y=i, d=g

CONFLICT: y=e (from Paeonia) vs y=i (from Nigella).
CONFLICT: d=o (from Paeonia) vs d=g (from Nigella).

Mapping from pchair->vitis: p=v, ch=i, a=t, i=i, r=s
Mapping from psheykedaleey->adiantum: p=a? (CONFLICT with p=v above)

**RESULT: No consistent single-substitution cipher exists that transforms codes into plant names. Every mapping derived from one anchor produces conflicts when applied to others. This is a DEFINITIVE negative result.**

### 6e. What about sound similarity without exact mapping?

Pronouncing codes with Italian phonology:
- kydainy: "ki-DAI-ni" -- does this SOUND like "pe-O-nia"? Only if you squint at the rhythm (3 syllables, stress on middle). The actual consonants and vowels are entirely different.
- tydlo: "TID-lo" -- vs "ni-GEL-la" -- no phonetic resemblance
- tsheos: "tse-OS" -- vs "ROB-bia" -- no resemblance
- pchair: "p-KHAIR" -- vs "VI-tis" -- no resemblance
- psheykedaleey: "pshey-ke-da-LEE" -- vs "ca-pel-ve-NE-re" -- no resemblance

**RESULT: No sound-based mnemonic. The codes do not sound like the plant names under any phonological system.**

---

## TEST 7: Cross-Validation (The Critical Test)

Since no single-substitution mapping survives cross-validation (Test 6d), and no abbreviation, numerical, key-text, property-encoding, or sound-based system works (Tests 1-6), we must conclude:

**There is no simple generation rule that derives the codes from the plant names.**

---

## REVISED HYPOTHESIS: The Codes Are NOT Derived from Plant Names

If the codes are not derived from plant names, what ARE they? A 15th-century person still needed to remember them. Several alternatives:

### Alternative A: The codes ARE the plant descriptions, not names

The "first word" is not a code for the plant name -- it IS a descriptive word in the manuscript's notation system. Evidence:
- "psheykedaleey" for Adiantum is extremely long -- more like a compound description than a code
- The same plant (Rubia) has different codes on different pages: tsheos (f3r) and tarodaiin (f43r)
- Codes containing "chol" (hypothesized = "leaf") might literally mean "X-leaved" (e.g., fcholdy = "fragrant-leaved"?)

Under this model, the author did NOT need to memorize arbitrary codes. The first word is simply the first word of a description, just as an English herbal might begin "The broad-leaved plant..." The description IS the mnemonic.

### Alternative B: The codes encode properties, not names (systematic nomenclature)

Like a proto-Linnaean system:
- Initial character = major category (p=plant, t=tree/herb, k=root-plant, f=fragrant?)
- Middle section = primary characteristic
- Ending = preparation method or habitat

Evidence for this:
- 42% start with p- (the most common initial, possibly = generic "plant")
- The "-yd-" cluster appears in 3+ Ranunculaceae codes
- "pcheo-" appears in 2 thistle-like plants
- The codes are too structurally diverse for pure arbitrary assignment

Evidence against:
- The sub-sequence sharing test (from nomenclator_analysis.md) found only 1.04x similarity ratio between sharing and non-sharing pairs -- essentially no signal
- Similar plants (two Arums: pshol vs pchodar) have very different codes

### Alternative C: The codes are from a DIFFERENT source language

What if the author was encoding plant names from Arabic, Hebrew, or another non-Latin/Italian language?

- Arabic names for these plants:
  - Paeonia: "faownia" (فاوونيا) or "oud al-salib"
  - Rubia: "fuwwa" (فوة)
  - Nigella: "habbat al-barakah" (حبة البركة) or "shuniz" (شونيز)
  - Adiantum: "kuzbarat al-bi'r" (كزبرة البئر)
  - Vitis: "inab" (عنب) or "karm" (كرم)

Testing Arabic -> EVA:
- kydainy vs "faownia" -- no resemblance
- tydlo vs "shuniz" -- no resemblance
- pchair vs "karm" or "inab" -- no resemblance

Hebrew names show similar non-resemblance.

### Alternative D: The codes are mnemonics based on folio position

If the code encodes WHICH PAGE of a reference work the plant is on:
- kydainy: folio 2r -- does "kydainy" encode "2"? In Roman numerals, 2 = II. No match.
- tsheos: folio 3r -- does "tsheos" encode "3"? No obvious match.

**This fails too.**

---

## FINAL ASSESSMENT

### What we can definitively rule out:

1. Simple substitution cipher from Latin plant names
2. Simple substitution cipher from Italian plant names
3. Abbreviation of plant names (any method)
4. Numerical encoding of Dioscorides chapter numbers
5. Key text derivation (psalms, prayers, herbal texts)
6. Sound-based mnemonic resemblance
7. Acrophonic encoding
8. Reversed plant names
9. Arabic or Hebrew plant name encoding

### What remains possible but unproven:

1. **Descriptive compound words** -- the codes are descriptions in the manuscript's own notation, not codes for external names. The author memorized the notation system, not a table of codes.

2. **Property-based systematic nomenclature** -- weak evidence from "-yd-" (Ranunculaceae) and "pcheo-" (thistles), but not statistically significant with our small confirmed anchor set.

3. **A completely unknown source language or dialect** -- if the plant names come from a language not yet tested (a specific Italian dialect, a Romani vocabulary, a trade jargon), we cannot test this without knowing the language.

4. **Multi-layer encoding** -- the plant names are first translated to a source language, then encoded through a substitution, making single-step decoding impossible.

### The Memorization Paradox -- Resolution

The premise was: "a 15th-century person couldn't memorize 200 arbitrary codes." But this assumes the codes are arbitrary. Our evidence actually suggests they are NOT arbitrary -- they are **compositional descriptions** within a consistent notation system. Just as a pharmacist doesn't "memorize" the word "broad-leaved" but constructs it from productive morphemes, the Voynich author may have constructed these "codes" from a small set of meaningful morphological units (prefixes, stems, suffixes) that combine productively.

The true "codebook" may not be 200 entries mapping code->plant, but rather:
- ~15-20 prefix morphemes (p-, t-, k-, f-, o-, sh-, ch-, etc.)
- ~30-50 stem morphemes (-yd-, -chol-, -cheo-, -shol-, etc.)
- ~10-15 suffix morphemes (-aiin, -dy, -ol, -or, -ey, -os, etc.)

This gives 15 x 40 x 12 = 7,200 possible combinations from only ~80 memorized units -- far more manageable than 200 arbitrary codes, and consistent with the manuscript's vocabulary size.

### The "-yd-" Finding: Worth Further Investigation

The one genuinely suggestive pattern:
- **kydainy** (Paeonia) -- Ranunculaceae
- **tydlo** (Nigella) -- Ranunculaceae  
- **pydchdom** (Aconitum?) -- Ranunculaceae (if identification is correct)
- **pykydal** (f45r) -- identification uncertain (35%)

If "-yd-" truly marks Ranunculaceae, this would be evidence for Alternative B (systematic nomenclature). To test this:
- We would need MORE confirmed plant identifications in Ranunculaceae
- We would need to verify that NO non-Ranunculaceae plants contain "-yd-"
- Current data is insufficient to confirm or deny this

### The "pcheo-" Finding

- **pcheoepchy** (f34r, Cirsium/thistle)
- **pcheocphy** (f46r, Eryngium/globe thistle)
- Both are spiny, compound-headed plants

If "pcheo-" encodes "spiny-headed", this is a property description, not a plant name. This supports Alternative A/B.

### Practical Implications for Decipherment

The most productive path forward is NOT to search for a code->name mapping, but rather:

1. **Decompose the morphological system**: Identify which sub-word elements carry meaning by looking at distributional patterns across ALL herbal first words

2. **Use confirmed anchors to assign meanings to morphemes**: If "-yd-" = Ranunculaceae, and "k-" vs "t-" vs "p-" encode different properties, each new identification narrows the morpheme meanings

3. **Accept that first words are DESCRIPTIONS, not NAMES**: This means the "code generation rule" is not a lookup table but a productive grammar -- the same grammar used throughout the rest of the text

This reframing dissolves the memorization paradox entirely: the author didn't need a code table because the first word is simply the first word of a description written in the manuscript's own language/notation system.
