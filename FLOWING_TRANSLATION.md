# FLOWING TRANSLATION OF VOYNICH PAGES
## Using the Complete Morpheme System

Date: 2026-04-10

---

## MORPHEME SYSTEM REFERENCE

```
WORD = PREFIX + CLASSIFIER + ROOT + GRADE + TERMINAL + SUFFIX

PREFIXES:
  p-   = Take/Recipe instruction
  ch-  = herb_category (aerial plant)
  sh-  = root_category (underground part)
  d-   = grammar/connector
  qo-  = quantity/measure
  cth- = attribute/quality
  ok-  = individual/specific item
  ot-  = alternative/other
  t-   = imperative/command
  s-   = then/next/sequential
  y-   = qualifying/adjective
  k-   = action/operative

CLASSIFIERS:
  c = aerial (leaf, herb)     -> ch = c+h
  s = underground (root)      -> sh = s+h
  k = body/measure            -> kch = k+c+h
  t = process                 -> tch = t+c+h
  p = product/prepared        -> pch = p+c+h
  l = structure/place
  e = botanical
  a = function

ROOT: h = substance/materia

GRADE (after root):
  null   = general
  +e     = specific (dried?)
  +ee    = very specific (powder?)
  +eeo   = preparation (decoction?)
  +eod   = product (confection?)

TERMINAL:
  null = unmarked
  +d   = definite
  +s   = collective/plural

SUFFIX:
  -ol/-or  = subject/this (nominative)
  -am/-m   = end clause (clause-final)
  -y/-dy   = predicate/is
  -aiin    = of (genitive)
  -edy     = B-subject (secondary topic)

FUNCTION WORDS:
  daiin = and
  aiin  = in
  ol    = of/the
  chey  = is (herb-predicate)
  ar    = to/toward
  or    = with
  shey  = which (root-relative)
  dar   = but
  dain  = and/then (variant)
```

---

## 1. FOLIO 47r (GRAPE / Vitis vinifera)

### Raw EVA Text

```
1. pchair.oly.sheaiin.shol.daiin.chdy
2. chokchol.chol.choldy.dair.chad.aiin
3. dor.chol.chy.chaiin.ckhey.chol.dain.okaiin
4. qokcheo.cthey.chokain.chol.daiin.kchdal
5. dain.olshey.chokolg
6. folr.chey.so.chol.shol.aiin.shol.shol.chdy.cholol
7. schesy.kchor.cthaiin.chol.chol.chol.chor.{ckhh}ey
8. sho,keey.chy.tchod.choy.sho.cht,chy,kchar.ctham
9. qokokor.chaiin.okal.chol.daiin.okchokchor,sy
10. shy.otcho.keey.tor.chey.otchy.tchol.dain.dam
11. dsho.cphy.daiin.daiiny
```

### Line-by-Line Morpheme Decomposition

**Line 1: `pchair.oly.sheaiin.shol.daiin.chdy`**
- `pchair` = p(take/recipe) + ch(herb) + a(function) + ir(quality-suffix) -> "Take the herb preparation"
- `oly` = ol(of/the) + y(qualifying) -> "of the"
- `sheaiin` = sh(root) + e(specific) + aiin(genitive) -> "of the specific root"
- `shol` = sh(root) + ol(subject/this) -> "this root"
- `daiin` = "and"
- `chdy` = ch(herb) + dy(predicate) -> "is the herb"

**Flowing: "Take the herb preparation of the specific root -- this root -- and the herb [itself]."**

**Line 2: `chokchol.chol.choldy.dair.chad.aiin`**
- `chokchol` = ch(herb) + ok(individual) + ch(herb) + ol(subject) -> "the individual herb-plant of this"
- `chol` = ch(herb) + ol(subject) -> "this herb"
- `choldy` = ch(herb) + ol(subject) + dy(predicate) -> "is this herb"
- `dair` = d(grammar) + air -> "to/toward it"
- `chad` = ch(herb) + a(function) + d(definite) -> "the functional herb"
- `aiin` = "in"

**Flowing: "The particular herb-plant, this herb, is the herb [used] toward the functional herb part in..."**

**Line 3: `dor.chol.chy.chaiin.ckhey.chol.dain.okaiin`**
- `dor` = d(grammar) + or(with) -> "with"
- `chol` = "this herb"
- `chy` = ch(herb) + y(qualifying) -> "herb-like / herbal"
- `chaiin` = ch(herb) + aiin(genitive) -> "of the herb"
- `ckhey` = ckh(body-herb compound) + ey(specific-predicate) -> "is [of] bodily-herbal [virtue]"
- `chol` = "this herb"
- `dain` = "and then"
- `okaiin` = ok(individual) + aiin(genitive) -> "of the individual [part]"

**Flowing: "With this herb, the herbal [property] of the herb is of bodily virtue; this herb, and then of the individual [part]..."**

**Line 4: `qokcheo.cthey.chokain.chol.daiin.kchdal`**
- `qokcheo` = qo(quantity) + kch(body-measure) + eo(preparation-grade) -> "a measured body-preparation"
- `cthey` = cth(attribute) + ey(specific-predicate) -> "is of the attribute/quality"
- `chokain` = ch(herb) + ok(individual) + ain -> "individual herb ingredient"
- `chol` = "this herb"
- `daiin` = "and"
- `kchdal` = kch(body-measure) + d(definite) + al -> "the definite body-measure/dose"

**Flowing: "A measured body-preparation is of [this] quality: the individual herb ingredient, this herb, and the definite body-dose..."**

**Line 5: `dain.olshey.chokolg`**
- `dain` = "and then"
- `olshey` = ol(of/the) + sh(root) + ey -> "of the root which"
- `chokolg` = ch(herb) + ok(individual) + ol(subject) + g(?) -> "the individual herb [cluster?]"

**Flowing: "And then of the root which [is] the individual herb cluster."**

**Line 6: `folr.chey.so.chol.shol.aiin.shol.shol.chdy.cholol`**
- `folr` = f(?) + ol(the) + r(quality) -> "the [fine?] quality"
- `chey` = "is [the herb]"
- `so` = s(then/next) + o -> "then"
- `chol` = "this herb"
- `shol` = "this root"
- `aiin` = "in"
- `shol.shol` = "root [and] root" (repetition = emphasis: the roots)
- `chdy` = ch(herb) + dy(predicate) -> "is herbal"
- `cholol` = ch(herb) + ol(subject) + ol(the) -> "this herb of the"

**Flowing: "The quality is [the herb]; then this herb [and] this root -- in the roots, the roots -- is herbal; this herb of the..."**

**Line 7: `schesy.kchor.cthaiin.chol.chol.chol.chor.{ckhh}ey`**
- `schesy` = s(then) + ch(herb) + e(specific) + sy(collective-qualifying) -> "then the specific herbs collectively"
- `kchor` = kch(body-measure) + or(with) -> "with the body-measure"
- `cthaiin` = cth(attribute) + aiin(genitive) -> "of the attribute"
- `chol.chol.chol` = triple repetition -> "herb, herb, herb" (= many herbs / the herbs altogether)
- `chor` = ch(herb) + or(with) -> "with the herb"
- `{ckhh}ey` = ckh(body-herb) + h(substance) + ey -> "is [of] bodily herbal substance"

**Flowing: "Then the specific herbs collectively, with the body-measure of the quality, herb upon herb upon herb, with the herb, is of bodily herbal substance."**

**Line 8: `sho,keey.chy.tchod.choy.sho.cht,chy,kchar.ctham`**
- `sho` = sh(root) + o -> "root-state [extracted root]"
- `keey` = k(action) + ee(powder-grade) + y -> "the powdered action"
- `chy` = "herbal"
- `tchod` = tch(process) + o + d(definite) -> "the definite process"
- `choy` = ch(herb) + o + y -> "herb-state qualifying"
- `sho` = "extracted root"
- `kchar` = kch(body-measure) + ar(to) -> "to the body-measure"
- `ctham` = cth(attribute) + am(clause-end) -> "attribute [end]."

**Flowing: "The extracted root, in powder, herbal, the definite process: the herb-state, the extracted root, to the body-measure of the attribute."**

**Line 9: `qokokor.chaiin.okal.chol.daiin.okchokchor,sy`**
- `qokokor` = qo(quantity) + ok(individual) + ok(individual) + or(with) -> "in quantity, each individual, with"
- `chaiin` = "of the herb"
- `okal` = ok(individual) + al -> "individual portion"
- `chol` = "this herb"
- `daiin` = "and"
- `okchokchor,sy` = ok(individual) + ch(herb) + ok(individual) + ch(herb) + or(with) + sy(collective) -> "individual herbs collectively with"

**Flowing: "In quantity, for each individual of the herb, an individual portion of this herb, and individual herbs collectively with [one another]."**

**Line 10: `shy.otcho.keey.tor.chey.otchy.tchol.dain.dam`**
- `shy` = sh(root) + y(qualifying) -> "root-like / of the root"
- `otcho` = ot(alternative) + ch(herb) + o -> "alternative herb state"
- `keey` = k(action) + ee(powder) + y -> "powdered action"
- `tor` = t(imperative) + or(with) -> "apply with"
- `chey` = "is [the herb]"
- `otchy` = ot(alternative) + ch(herb) + y -> "alternative herbal"
- `tchol` = tch(process) + ol(subject) -> "this process"
- `dain` = "and then"
- `dam` = d(grammar) + am(clause-end) -> "end."

**Flowing: "Of the root, the alternative herb state in powder: apply with the herb; alternatively herbal, this process. And then, end."**

**Line 11: `dsho.cphy.daiin.daiiny`**
- `dsho` = d(grammar) + sh(root) + o -> "grammatical root-state"
- `cphy` = cp(?) + h(substance) + y -> "prepared substance qualifying"
- `daiin` = "and"
- `daiiny` = daiin(and) + y(qualifying) -> "and qualifying / and also"

**Flowing: "The root-state, the prepared substance, and also [the following]."**

### COMPLETE FLOWING TRANSLATION OF f47r

> Take the herb preparation of the specific root -- this root and the herb itself. The particular herb-plant, this herb, is the herb used toward its functional part. With this herb, the herbal property of the herb is of bodily virtue; this herb and of the individual part.
>
> A measured body-preparation is of this quality: the individual herb ingredient, this herb, and the definite body-dose. And then of the root which is the individual herb cluster.
>
> The quality is the herb. Then this herb and this root -- in the roots, the roots -- is herbal. This herb of the specific herbs collectively, with the body-measure of the quality: herb upon herb upon herb, with the herb, is of bodily herbal substance.
>
> The extracted root, in powder, herbal -- the definite process: the herb-state, the extracted root, to the body-measure of the attribute. In quantity, for each individual of the herb, an individual portion of this herb, and individual herbs collectively with one another.
>
> Of the root, the alternative herb state in powder: apply with the herb; alternatively herbal, this process, and then, end. The root-state, the prepared substance, and also...

### Comparison with Dioscorides on Vitis (Grape Vine)

Dioscorides Book V (De Materia Medica) on Vitis vinifera:
- **Leaves**: Applied topically for headache, inflammation of the stomach; pounded with barley meal for hot inflammation
- **Tendrils**: Drunk in water for dysentery, spitting blood, stomach disorders
- **Juice from vines** (sap, "dakruon"): When cut in spring, the sap heals skin diseases, removes warts
- **Unripe grape** (omphax): Astringent, good for the stomach when applied as plaster
- **Raisins**: Warming, good for the trachea and lungs, applied to swellings
- **Vinegar**: Cooling, astringent

**Points of possible contact:**
- f47r mentions root + herb (vine is both above-ground shoot and root)
- Repeated emphasis on "body-measure" / dosage is consistent with pharmaceutical text
- Reference to "powder" (keey) -- Dioscorides mentions pounding leaves
- Process instructions (take, prepare, apply)

**Points of divergence:**
- No specific body parts or diseases mentioned in the translation
- No recognizable ingredient names
- The repetitive "herb herb herb" does not match the specificity of Dioscorides

**Pharmaceutical coherence: 3/10**
**Similarity to Dioscorides: 2/10**
**Continuous sense: ~25%**
**Remaining gaps: Most words decompose into vague "herb/root/measure" without specific meaning. No dosage numbers, no disease names, no preparation details that couldn't apply to any plant.**

---

## 2. FOLIO 3r (MADDER / Rubia tinctorum)

### Raw EVA Text

```
1.  tsheos.qopal.chol.cthol.daimg
2.  ycheor.chor.dam.qotcham.cham
3.  ochor.qocheor.chol.daiin.cthy
4.  schey.chor.chal.chag.cham.cho
5.  qokol.chololy.s.cham.cthol
6.  ychtaiin.chor.cthom.otaldam
7.  otchol.qodaiin.chom.shom.@152;amo
8.  ysheor.chor.chol.oky.dago
9.  sho.@140;or.sheoldam.otchody.ol
10. y,dar.cholcthom
11. pcheol.{ch'}ol.sols.sheol.shey
12. ok@221;daiin.qokchor.qo.schodam.octhy
13. qokeey.qotshey.qokody.qokshey.cheody
14. chor.qo@152;air.okeey.qokeey
15. tsheoarom.shar.or.chor.olchsy.chom.otchom<->oporar
16. oteol.chol.s.cheol.ekshy.qokeom.qok@221;l.daiin<->soleeg
17. soeom.okeom.yteody.qokeeodal.sam
18. pcheoldom.shodaiin.qopchor.qopol.opcholqoty<->otolom
19. otchor.ol.cheor.qoeor.dair.qoteol.qosaiin<->chor.cthy
20. ycheor.chol.odaiin.chol.s.aiin.okolor.am
```

### Line-by-Line Morpheme Decomposition

**Line 1: `tsheos.qopal.chol.cthol.daimg`**
- `tsheos` = t(imperative) + sh(root) + eo(preparation-grade) + s(collective) -> "Prepare the root preparations collectively"
- `qopal` = qo(quantity) + p(product) + al -> "a quantity of product"
- `chol` = "this herb"
- `cthol` = cth(attribute) + ol(subject) -> "this attribute/quality"
- `daimg` = d(grammar) + aim + g(?) -> "and [compound]"

**Flowing: "Prepare the root preparations collectively, a quantity of product: this herb, this quality, and..."**

**Line 2: `ycheor.chor.dam.qotcham.cham`**
- `ycheor` = y(qualifying) + ch(herb) + e(specific) + or(with) -> "with qualifying specific herb"
- `chor` = ch(herb) + or(with) -> "with the herb"
- `dam` = d(grammar) + am(clause-end) -> "[end clause]"
- `qotcham` = qo(quantity) + tch(process) + am(clause-end) -> "a quantity of process [complete]"
- `cham` = ch(herb) + am(clause-end) -> "herb [clause-end]."

**Flowing: "With the qualifying specific herb, with the herb. A measured process of the herb."**

**Line 3: `ochor.qocheor.chol.daiin.cthy`**
- `ochor` = o + ch(herb) + or(with) -> "with the herb"
- `qocheor` = qo(quantity) + ch(herb) + e(specific) + or(with) -> "with a quantity of specific herb"
- `chol` = "this herb"
- `daiin` = "and"
- `cthy` = cth(attribute) + y(qualifying) -> "of [its] quality"

**Flowing: "With the herb, with a quantity of specific herb, this herb, and its quality."**

**Line 4: `schey.chor.chal.chag.cham.cho`**
- `schey` = s(then) + ch(herb) + ey -> "then the herb is"
- `chor` = "with herb"
- `chal` = ch(herb) + al -> "herb-portion"
- `chag` = ch(herb) + a(function) + g(?) -> "functional herb [compound]"
- `cham` = "herb [clause-end]"
- `cho` = ch(herb) + o -> "herb-state"

**Flowing: "Then the herb is with [other] herb: a herb-portion, the functional herb, the herb in its state."**

**Line 5: `qokol.chololy.s.cham.cthol`**
- `qokol` = qo(quantity) + k(action) + ol(subject) -> "a measured action/amount of this"
- `chololy` = ch(herb) + ol(subject) + ol(the) + y(qualifying) -> "this herb of the qualifying"
- `s` = s(then/next) -> "then"
- `cham` = "herb [end]"
- `cthol` = cth(attribute) + ol(subject) -> "this quality"

**Flowing: "A measured amount, this qualifying herb, then the herb: this quality."**

**Line 6: `ychtaiin.chor.cthom.otaldam`**
- `ychtaiin` = y(qualifying) + ch(herb) + t(process) + aiin(genitive) -> "of the qualifying herbal process"
- `chor` = "with herb"
- `cthom` = cth(attribute) + om -> "attribute [in/of]"
- `otaldam` = ot(alternative) + al + d(definite) + am(clause-end) -> "the alternative definite [thing], end."

**Flowing: "Of the qualifying herbal process, with the herb, the attribute, the alternative definite [preparation]."**

**Line 7: `otchol.qodaiin.chom.shom.@152;amo`**
- `otchol` = ot(alternative) + ch(herb) + ol(subject) -> "the alternative herb"
- `qodaiin` = qo(quantity) + d(grammar) + aiin(genitive) -> "of a measured [amount]"
- `chom` = ch(herb) + om -> "herb-of"
- `shom` = sh(root) + om -> "root-of"
- `@152;amo` = [glyph] + am(clause-end) + o -> "[special glyph] end"

**Flowing: "The alternative herb, of a measured [amount], of the herb, of the root, [end]."**

**Line 8: `ysheor.chor.chol.oky.dago`**
- `ysheor` = y(qualifying) + sh(root) + e(specific) + or(with) -> "with the qualifying specific root"
- `chor` = "with herb"
- `chol` = "this herb"
- `oky` = ok(individual) + y(qualifying) -> "individual qualifying"
- `dago` = d(grammar) + a + g + o -> "connector [compound]"

**Flowing: "With the qualifying specific root, with the herb, this herb, individually qualifying..."**

**Line 11: `pcheol.{ch'}ol.sols.sheol.shey`**
- `pcheol` = p(take/recipe) + ch(herb) + e(specific) + ol(subject) -> "Take the specific herb"
- `{ch'}ol` = ch(herb) + ol(subject) -> "this herb [variant]"
- `sols` = s(then) + ol(the) + s(collective) -> "then the collective"
- `sheol` = sh(root) + e(specific) + ol(subject) -> "this specific root"
- `shey` = "which [root]"

**Flowing: "Take the specific herb, this herb, then the collective specific root, which..."**

**Line 18: `pcheoldom.shodaiin.qopchor.qopol.opcholqoty`**
- `pcheoldom` = p(take/recipe) + ch(herb) + e(specific) + ol(subject) + d(definite) + om -> "Take the definite specific herb of..."
- `shodaiin` = sh(root) + o + d(grammar) + aiin(genitive) -> "of the root-state"
- `qopchor` = qo(quantity) + p(product) + ch(herb) + or(with) -> "with a quantity of the herbal product"
- `qopol` = qo(quantity) + p(product) + ol(subject) -> "a quantity of this product"
- `opcholqoty` = o + p(product) + ch(herb) + ol(subject) + qo(quantity) + ty -> "the herbal product, this quantity, process"

**Flowing: "Take the definite specific herb of the root-state, with a quantity of the herbal product, a quantity of this product, the herbal product [in] this quantity [for] process."**

### COMPLETE FLOWING TRANSLATION OF f3r

> Prepare the root preparations collectively, a quantity of product: this herb, this quality. With the qualifying specific herb, with the herb; a measured process of the herb.
>
> With the herb, with a quantity of specific herb, this herb and its quality. Then the herb is with other herb: a herb-portion, the functional herb, the herb in its state.
>
> A measured amount, this qualifying herb, then the herb: this quality. Of the qualifying herbal process, with the herb, the attribute, the alternative definite preparation.
>
> The alternative herb, of a measured amount, of the herb, of the root. With the qualifying specific root, with the herb, this herb, individually.
>
> [...lines 9-10 abbreviated...]
>
> Take the specific herb, this herb, then the collective specific root, which... [continues with measurements and quantities of herbal products through line 20]

### Comparison with Dioscorides on Rubia (Madder)

Dioscorides Book III on Rubia tinctorum:
- **Root** is the primary medicinal part (used for dye AND medicine)
- Diuretic, promotes menstruation
- Used for jaundice, sciatica, paralysis
- Applied with honey and vinegar
- The **leaves** are rough, applied for skin conditions
- Root drunk with hydromel (honey-water) for spleen disorders

**Points of possible contact:**
- f3r prominently mentions root (sh- words: sheol, shor, shom, ysheor) -- consistent with Rubia where root is primary
- Multiple recipe-prefix words (pcheol, pcheoldom) suggesting preparation instructions
- Mentions "quantity" (qo-) repeatedly -- dosage-like

**Points of divergence:**
- No specific diseases, organs, or application methods
- No mention of honey, vinegar, hydromel
- No distinguishing features (e.g., the "rough leaves" that are diagnostic for Rubia)
- Translation reads as generic "herb + root + quantity" without specificity

**Pharmaceutical coherence: 3/10**
**Similarity to Dioscorides: 2/10**
**Continuous sense: ~20%**
**Remaining gaps: Same fundamental problem as f47r -- every word decomposes to herb/root/quality/quantity without specific medical content.**

---

## 3. FOLIO 2r (PEONY / Paeonia)

### Raw EVA Text

```
1.  kydainy.ypchol.daiin.otchal<->ypchaiin.ckholsy
2.  dorchory<->chkar.s<->shor.cthy.{cto}
3.  qotaiin<->cthey.y<->chor.chy.ydy<->chaiin
4.  {c'o}aiidy<->chtoddy<->cphy.dals<->chotaiin.d
5.  otochor.al<->shodaiin<->chol.dan<->ytchaiin.dan
6.  saiin.daind<->dkol.sor<->ytoldy<->dchol.dchy.cthy
7.  shor.ckhy.daiiny<->chol.dan
8.  kydain.shaiin.qoy.s.shol.fodan<->yksh.olsheey.daiildy
9.  dlssho.kol.sheey.qokey.ykody.so<->cholyky.dain.daiirol
10. q'oky.cholaiin.shol.sheky.daiin<->cthey.keol.saiin.e'a'iin
11. ychain.dal.chy.dalor.shan.dan<->olsaiin.sheey.ckhor
12. okol.chy.chor.cthor.yor.an.chan<->saiin.chety.chyky.sal
13. sho.ykeey.chey.daiin.chcthy
14. ytoail
15. ios.an.on
```

### Line-by-Line Morpheme Decomposition

**Line 1: `kydainy.ypchol.daiin.otchal<->ypchaiin.ckholsy`**
- `kydainy` = k(action) + y(qualifying) + dain(and-then) + y -> "the active qualifying and then qualifying"
- `ypchol` = y(qualifying) + p(product) + ch(herb) + ol(subject) -> "the qualifying herbal product"
- `daiin` = "and"
- `otchal` = ot(alternative) + ch(herb) + al -> "alternative herb-portion"
- `ypchaiin` = y(qualifying) + p(product) + ch(herb) + aiin(genitive) -> "of the qualifying herbal product"
- `ckholsy` = ckh(body-herb) + ol(subject) + sy(collective) -> "these bodily-herbal [items] collectively"

**Flowing: "The active, qualifying -- the qualifying herbal product and the alternative herb-portion -- of the qualifying herbal product, these bodily-herbal items collectively."**

**Line 5: `otochor.al<->shodaiin<->chol.dan<->ytchaiin.dan`**
- `otochor` = ot(alternative) + o + ch(herb) + or(with) -> "with the alternative herb"
- `al` = "portion"
- `shodaiin` = sh(root) + o + d(grammar) + aiin(genitive) -> "of the root-state"
- `chol` = "this herb"
- `dan` = d(grammar) + an -> "then"
- `ytchaiin` = y(qualifying) + tch(process) + aiin(genitive) -> "of the qualifying process"
- `dan` = "then"

**Flowing: "With the alternative herb, a portion of the root-state; this herb, then of the qualifying process, then..."**

**Line 7: `shor.ckhy.daiiny<->chol.dan`**
- `shor` = sh(root) + or(with) -> "with the root"
- `ckhy` = ckh(body-herb) + y(qualifying) -> "bodily-herbal qualifying"
- `daiiny` = daiin(and) + y(qualifying) -> "and qualifying"
- `chol` = "this herb"
- `dan` = "then"

**Flowing: "With the root, bodily-herbal qualifying, and qualifying this herb, then..."**

**Line 8: `kydain.shaiin.qoy.s.shol.fodan<->yksh.olsheey.daiildy`**
- `kydain` = k(action) + y(qualifying) + dain(and-then) -> "active qualifying and-then"
- `shaiin` = sh(root) + aiin(genitive) -> "of the root"
- `qoy` = qo(quantity) + y(qualifying) -> "a qualifying quantity"
- `s` = "then"
- `shol` = "this root"
- `fodan` = f(?) + o + dan -> "... then"
- `yksh` = y(qualifying) + k(action) + sh(root) -> "qualifying active root"
- `olsheey` = ol(the) + sh(root) + ee(powder-grade) + y -> "the powdered root qualifying"
- `daiildy` = daiin(and) + l(structure) + dy(predicate) -> "and is of the structure"

**Flowing: "Active and then of the root, a qualifying quantity, then this root... the qualifying active root, the powdered root, and is of the structure."**

**Line 13: `sho.ykeey.chey.daiin.chcthy`**
- `sho` = sh(root) + o -> "root-state [extracted root]"
- `ykeey` = y(qualifying) + k(action) + ee(powder) + y -> "qualifying powdered action"
- `chey` = "is [the herb]"
- `daiin` = "and"
- `chcthy` = ch(herb) + cth(attribute) + y(qualifying) -> "herb-attribute qualifying"

**Flowing: "The extracted root, in qualifying powder, is the herb, and the qualifying herbal attribute."**

**Line 14: `ytoail`** -- (label text)
- `ytoail` = y(qualifying) + t(imperative) + o + a(function) + il -> "qualifying: apply in function..."

**Line 15: `ios.an.on`** -- (label text)
- Possibly abbreviated notation or abbreviated plant name

### COMPLETE FLOWING TRANSLATION OF f2r

> The active, qualifying herbal product and the alternative herb-portion, of the qualifying herbal product, these bodily-herbal items collectively. With the herbal quality, qualifying, with herb, herbal, qualifying [it] is; of the herb.
>
> With the alternative herb, a portion of the root-state; this herb, then of the qualifying process. In [a solution], and then, the definite, and then the herbal quality, the herb, is qualifying; with this herb, then.
>
> With the root, bodily-herbal, qualifying, and this herb, then. Active, of the root, a quantity, then this root -- the qualifying active root, the powdered root, and is of the structure.
>
> [...]
>
> The extracted root, in qualifying powder, is the herb, and the qualifying herbal attribute.

### Comparison with Dioscorides on Paeonia (Peony)

Dioscorides Book III on Paeonia:
- **Root** is primary medicinal part (both male and female peony)
- Male peony root: 10-12 "acorns" (tubercles) like almonds
- Female peony root: more tuberous roots, like bulbs
- Root drunk promotes menstruation
- Root given to children prevents epilepsy (worn as amulet or drunk)
- **Seeds**: 15 grains drunk in wine for uterine suffocation
- Applied topically for liver and kidney pain
- Dries and is astringent

**Points of possible contact:**
- f2r has heavy root emphasis (shor, shol, shaiin, shodaiin, yksh, olsheey, sho) -- consistent with Paeonia where root is primary
- Mentions "powder" of root (olsheey = powdered root) -- Dioscorides mentions pounding/grinding root
- "Bodily-herbal" (ckhy, ckholsy) -- consistent with body-medicine use
- Product/preparation words (ypchol, ypchaiin) -- consistent with processed preparation

**Points of divergence:**
- No mention of epilepsy, menstruation, children, liver, kidneys
- No wine or specific vehicle mentioned
- No seed vs. root distinction
- No dose numbers

**Pharmaceutical coherence: 3/10**
**Similarity to Dioscorides: 2/10**
**Continuous sense: ~20%**
**Remaining gaps: The root-heavy vocabulary is consistent with Paeonia IF the plant ID is correct, but the translation produces no distinguishing medical content.**

---

## 4. FOLIO 103r (RECIPE PAGE) -- First 15 Lines

### Raw EVA Text

```
1.  pchedal.{ch'}dy.ytechypchy.otey.alshey.qoteey.qotal.shedy.yshdal.@152;ain.okal.dal,@152;y
2.  dain.shek.ch{cphh}dy.daloky.opche@152;y.pcheo'l.chep.ar.otchy.sal.lkeey.sar.ain.okad.che@152;y
3.  yshdain.{ch'}eek.cheoty.chokal.che@152;y.chckhy.or.@221;rol.okaiin.chal.ot.shkar.otar.chal
4.  ychedy.qokedy.okedy.qokeey.okey.chdar.ol.loty.chedar,aly
5.  pocharal.okedar.shedy.oteey.qokey.lkar.sheeky.okalor.shedy.yk???.rkar.otae.okdy
6.  ocheey.dain.shek.okeedy.okey.shedy.qokealdy.shcthy.qotedy.qoto???.ota.???.sein.am
7.  saiin.chey.shs.olshedy.qokeey.okeeody.qaedy.ol.shedy
8.  daroal.okey.che@152;y.okey.rain.okeeey.qoisal.qotar.adchey.ofcho.lt??dy.talkechdy.lo
9.  oteeos.ar.cheal.okeey.shey.lkaiin.shey.lkear.otaiin.she@152;y.otey.l.eedy.okeedaram
10. daiin.al.oain.okeol.chal.okam.chety.shedy.otaiin.shedy.teolshy.oteedy.s,ar.ain
11. dar.ateey.otain.lolshedy.okain.chey.qoreiin.shey.otoy.qokeol.key.@152;a{ikh}yky
12. oain.shey.shckhy.oteey.qokeol.kee@152;y.shar.aiin.ote@152;y
13. pojar.sheor.qotedy.okeey.qokar.checkhy.qokain.chedy.pchdy.tsh@152;y.dalkarol
14. okain.shekain.che@152;y.qokeechy.qoky.shey.lol.s.aiin.chey.chkain.chcthy.qoky
15. qote@152;y.qokeey.shal.qotey.shkaiin
```

### Line-by-Line Morpheme Decomposition

**Line 1: `pchedal.{ch'}dy.ytechypchy.otey.alshey.qoteey.qotal.shedy.yshdal.@152;ain.okal.dal,@152;y`**
- `pchedal` = p(take/recipe) + ch(herb) + e(specific) + d(definite) + al -> "Take the definite specific herb portion"
- `{ch'}dy` = ch(herb) + dy(predicate) -> "is the herb"
- `ytechypchy` = y(qualifying) + t(process) + e + ch(herb) + y + p(product) + ch(herb) + y -> "qualifying process-herb and product-herb qualifying"
- `otey` = ot(alternative) + ey -> "alternatively"
- `alshey` = al + sh(root) + ey -> "portion of the root which"
- `qoteey` = qo(quantity) + t(process) + ee(powder) + y -> "a quantity of powdered process"
- `qotal` = qo(quantity) + t(process) + al -> "a quantity of process portion"
- `shedy` = sh(root) + e(specific) + dy(predicate) -> "is the specific root"
- `yshdal` = y(qualifying) + sh(root) + d(definite) + al -> "the qualifying definite root portion"
- `okal` = ok(individual) + al -> "individual portion"
- `dal` = d(grammar) + al -> "of the"

**Flowing: "Take the definite specific herb portion -- the herb [which] is the qualifying processed herbal product. Alternatively, a portion of the root: a quantity of the powdered process, a quantity of the process-portion. It is the specific root, the qualifying definite root portion, an individual portion of the..."**

**Line 2: `dain.shek.ch{cphh}dy.daloky.opche@152;y.pcheo'l.chep.ar.otchy.sal.lkeey.sar.ain.okad.che@152;y`**
- `dain` = "and then"
- `shek` = sh(root) + e(specific) + k(action) -> "the specific root action/cut"
- `daloky` = d(grammar) + al + ok(individual) + y -> "of the individual qualifying"
- `pcheo'l` = p(take) + ch(herb) + eo(preparation) + l -> "take the herb preparation [in] structure"
- `chep` = ch(herb) + e(specific) + p(product) -> "specific herbal product"
- `ar` = "to/toward"
- `otchy` = ot(alternative) + ch(herb) + y -> "alternative herbal"
- `sal` = s(then) + al -> "then the portion"
- `lkeey` = l(structure) + k(action) + ee(powder) + y -> "structural powdered action"
- `sar` = s(then) + ar(to) -> "then to"
- `ain` = "in"
- `okad` = ok(individual) + a(function) + d(definite) -> "the individual definite function"

**Flowing: "And then, the specific root cut of the individual: take the herb preparation, the specific herbal product, toward the alternative herbal, then the portion, the structural powdered action, then to the individual definite function."**

**Line 7: `saiin.chey.shs.olshedy.qokeey.okeeody.qaedy.ol.shedy`**
- `saiin` = s(then) + aiin(in) -> "then in"
- `chey` = "is the herb"
- `shs` = sh(root) + s(collective) -> "roots collectively"
- `olshedy` = ol(the) + sh(root) + e(specific) + dy(predicate) -> "the specific root is"
- `qokeey` = qo(quantity) + k(action) + ee(powder) + y -> "a quantity of powdered action"
- `okeeody` = ok(individual) + ee(powder) + o + dy(predicate) -> "the individual powder-state is"
- `qaedy` = qa(?) + e(specific) + dy(predicate) -> "is specifically [...]"
- `ol` = "of/the"
- `shedy` = "is the specific root"

**Flowing: "Then in the herb, the roots collectively: the specific root is a quantity of powdered action, the individual powder-state is specifically the specific root."**

**Line 13: `pojar.sheor.qotedy.okeey.qokar.checkhy.qokain.chedy.pchdy.tsh@152;y.dalkarol`**
- `pojar` = p(take/recipe) + o + j(?) + ar(to) -> "Take/prepare, to"
- `sheor` = sh(root) + e(specific) + or(with) -> "with the specific root"
- `qotedy` = qo(quantity) + t(process) + e(specific) + dy(predicate) -> "a quantity of specific process is"
- `okeey` = ok(individual) + ee(powder) + y -> "individual powder qualifying"
- `qokar` = qo(quantity) + k(action) + ar(to) -> "a quantity of action toward"
- `checkhy` = ch(herb) + e(specific) + ckh(body) + y -> "specific bodily-herbal"
- `qokain` = qo(quantity) + k(action) + ain -> "a quantity of action in"
- `chedy` = ch(herb) + e(specific) + dy(predicate) -> "is the specific herb"
- `pchdy` = p(product) + ch(herb) + dy(predicate) -> "is the herbal product"
- `dalkarol` = d(grammar) + al + k(action) + ar(to) + ol(the) -> "of the action toward the"

**Flowing: "Prepare with the specific root: a quantity of specific process is individual powder, a quantity of action toward the specific bodily-herbal, a quantity of action in the specific herb, is the herbal product, of the action toward the..."**

### COMPLETE FLOWING TRANSLATION OF f103r (Lines 1-15)

> Take the definite specific herb portion -- the herb which is the qualifying processed herbal product. Alternatively, a portion of the root: a quantity of the powdered process, a quantity of the process-portion. It is the specific root, the qualifying definite root portion, an individual portion.
>
> And then, the specific root cut of the individual: take the herb preparation, the specific herbal product, toward the alternative herbal, then the portion, the structural powdered action, then to the individual definite function.
>
> The qualifying root and then, the specific [herb], the process-herb, the individual herb, the specific [glyph]: the bodily-herbal, with [special glyph], of the individual, the herb portion, the alternative, the root-body [measure], the alternative herb portion.
>
> The qualifying herb is, a quantity of [action] is, the individual is, a quantity of powdered [action], the individual action, the herbal connector of the structural process, the herbal connector portion.
>
> [continues similarly through line 15...]
>
> A quantity of the specific [glyph], a quantity of powdered action, the root portion, a quantity of the process, the root-body of the individual.

### Expected Recipe Pattern vs. Actual

**Expected (from Dioscorides/Antidotarium Nicolai):**
> "Take [specific ingredient] [amount in drams/scruples], [second ingredient] [amount], mix [method], prepare [decoction/powder/confection], give [dose] for [condition]."

**What we actually get:**
> Recursive herb-root-quantity-process without specific ingredients, amounts, methods, or conditions.

**Pharmaceutical coherence: 2/10**
**Recipe-pattern match: 2/10**
**Continuous sense: ~15%**
**Remaining gaps: No ingredient names, no numeric dosages, no specific preparations, no disease indications. The p- prefix (Take/Recipe) does appear where expected, but the rest dissolves into morpheme soup.**

---

## 5. EVALUATION SUMMARY

### Score Table

| Page | Plant ID | Pharma Coherence | Dioscorides Match | Continuous Sense | 
|------|----------|-----------------|-------------------|-----------------|
| f47r | Grape/Vitis | 3/10 | 2/10 | ~25% |
| f3r | Madder/Rubia | 3/10 | 2/10 | ~20% |
| f2r | Peony/Paeonia | 3/10 | 2/10 | ~20% |
| f103r | Recipe | 2/10 | 2/10 | ~15% |

### What Works
1. **Structural detection**: The prefix system (p- for take/recipe, qo- for quantity) does appear to mark real functional positions
2. **ch/sh distribution**: Herbal pages do show ch/sh patterns consistent with above-ground/below-ground plant parts
3. **Function words**: `daiin` (and), `ol` (the/of), `ar` (to) appear in grammatically plausible positions
4. **Grade system**: The -e/-ee/-eeo suffixes do appear to mark something (possibly specificity or processing)

### What Fails
1. **No semantic content emerges**: Every word decomposes to "herb-substance" or "root-substance" or "body-measure" -- there is no vocabulary for diseases, body parts, colors, tastes, seasons, or specific preparations
2. **No distinguishing content between pages**: f47r (grape) and f3r (madder) produce nearly identical translations despite being completely different plants with different medical uses
3. **No dosage numbers**: Medieval recipes always include numeric quantities; the morpheme system produces no numbers
4. **No verb semantics beyond "take/prepare"**: Real pharmaceutical texts have diverse verbs (boil, pound, strain, apply, drink, wash, anoint)

---

## 6. CRITICAL HONESTY CHECK: The Vagueness Test

### Method

To test whether this morpheme system is genuinely reading content or producing pharmaceutical-sounding output from any input, I will apply the EXACT same system to a **shuffled version** of f47r (words randomly reordered) and check whether it also produces "pharmaceutical-sounding" output.

### Original f47r Line 1
`pchair.oly.sheaiin.shol.daiin.chdy`
-> "Take the herb preparation of the specific root, this root, and the herb."

### Shuffled f47r (random word order from all lines)
`ctham.cholol.chol.dam.kchor.chor`

Applying the same system:
- `ctham` = cth(attribute) + am(clause-end) -> "the attribute, end."
- `cholol` = ch(herb) + ol(subject) + ol(the) -> "this herb of the"
- `chol` = "this herb"
- `dam` = d(grammar) + am(clause-end) -> "end"
- `kchor` = kch(body-measure) + or(with) -> "with the body-measure"
- `chor` = ch(herb) + or(with) -> "with the herb"

**Shuffled translation: "The attribute, end. This herb of the, this herb, end, with the body-measure, with the herb."**

### Another random shuffle
`okaiin.schesy.tchol.folr.shy.qokcheo`

- `okaiin` = ok(individual) + aiin(genitive) -> "of the individual"
- `schesy` = s(then) + ch(herb) + e(specific) + sy(collective) -> "then the specific herbs collectively"
- `tchol` = tch(process) + ol(subject) -> "this process"
- `folr` = f(?) + ol(the) + r(quality) -> "the quality"
- `shy` = sh(root) + y(qualifying) -> "of the root"
- `qokcheo` = qo(quantity) + kch(body) + eo(preparation) -> "a quantity of body-preparation"

**Shuffled translation: "Of the individual, then the specific herbs collectively: this process, the quality of the root, a quantity of body-preparation."**

### Verdict on the Vagueness Test

**THE SHUFFLED TEXT ALSO SOUNDS PHARMACEUTICAL.**

The shuffled version produces output like "the attribute... this herb of the... with the body-measure" which is barely distinguishable from the "real" translation. The only difference is that the original has slightly better clause structure (beginning with `p-` = Take, ending with `-am` = clause-end), while the shuffled version has those markers in random positions.

This means:

| Aspect | Original Order | Shuffled Order | Conclusion |
|--------|---------------|----------------|------------|
| Pharmaceutical vocabulary | Yes | Yes | System always produces this |
| Clause structure | Partially coherent | Broken | Word ORDER may carry real info |
| Specific medical content | None | None | System cannot extract specifics |
| Distinguishable from random | Barely | N/A | SYSTEM IS TOO VAGUE |

### Honest Assessment

**The morpheme system as currently constituted is NOT genuinely reading the text.** It is a mapping where:

1. ~80% of Voynich words contain `ch` or `sh`, which the system maps to "herb" or "root"
2. ~30% of words contain `ol`, mapped to "this/the"
3. ~20% contain `aiin`, mapped to "of/in"
4. Common suffixes (-y, -dy, -am) are mapped to grammatical particles

Since the vast majority of Voynich words are built from these few elements, ANY arrangement of Voynich words will produce "herb/root + this/the + of/in + is/end" -- which will always sound vaguely pharmaceutical when strung together.

**The system captures STRUCTURE (prefix/suffix positions, ch/sh distribution) but not CONTENT (what specific herb, what disease, what dose, what preparation).**

### What Would Constitute Genuine Reading?

A genuine decipherment would need to:
1. Produce DIFFERENT specific content for different plant pages (e.g., "this is astringent, good for dysentery" for grape vs. "this is diuretic, promotes menstruation" for madder)
2. Produce recognizable dose numbers in recipe sections
3. Generate text that does NOT sound pharmaceutical when applied to shuffled input
4. Match at least some specific claims from Dioscorides for identified plants
5. Produce verbs beyond "take" and "is" (e.g., boil, pound, drink, apply)

### Final Rating

| Criterion | Score |
|-----------|-------|
| Is the morpheme system internally consistent? | 7/10 -- yes, the decomposition rules are applied systematically |
| Does it produce readable English? | 3/10 -- barely; most output is tautological ("the herb of the herb") |
| Does it capture real structure? | 5/10 -- prefix/suffix positions do seem to correspond to syntactic slots |
| Does it read CONTENT? | 1/10 -- no specific medical, botanical, or procedural content emerges |
| Is it distinguishable from reading random text? | 2/10 -- only clause boundaries differ |
| Overall decipherment validity | 2/10 -- structural observations are real, but this is not a decipherment |

### The Uncomfortable Truth

The morpheme system successfully identifies that the Voynich manuscript has:
- A small number of recurring elements (ch, sh, ol, aiin, daiin, etc.)
- A possible prefix/suffix structure
- Distribution patterns consistent with an organized text (not random)

But mapping these elements to "herb/root/substance/quality" does not constitute reading the text. It is equivalent to noting that English has articles (the, a) and prepositions (of, in, with) and then "translating" any English text as "the thing of the thing in the thing with the thing" -- which would always be vaguely correct but never informative.

**The Voynich manuscript remains unread.**
