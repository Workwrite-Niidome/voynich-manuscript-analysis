# Voynich Manuscript Herbal Section: Plant Ordering System Analysis

## Objective

Test whether the herbal section of the Voynich manuscript follows a known medieval plant ordering system. If the order matches a recognized tradition, we can predict the identity of unidentified plants and gain a foothold for decipherment.

---

## Data: Identified Plants by Folio Position

From the plant identification study (`plant_identification.md`) and the user's confirmed identifications:

| Folio | Seq# | Plant Identification | Confidence | Dioscorides Location | Latin Alpha Rank |
|-------|------|---------------------|------------|---------------------|-----------------|
| f1r   | 1    | Laurus nobilis (bay laurel) | 45% | Book 1, Ch.106 (aromatics/trees) | L = ~12/26 |
| f2r   | 3    | Paeonia officinalis (peony) | 55% | Book 3, Ch.140 | P = ~16/26 |
| f2v   | 4    | Cyclamen sp. (sowbread) | 45% | Book 2, Ch.164 | C = ~3/26 |
| f3r   | 5    | Rubia tinctorum (madder) | 60% | Book 3, Ch.143 | R = ~18/26 |
| f3v   | 6    | Cynara scolymus (artichoke) | 55% | Book 3, Ch.14 (Scolymos) | C = ~3/26 |
| f4r   | 7    | Rosmarinus officinalis (rosemary) | 55% | Book 3, Ch.75 (Libanotis) | R = ~18/26 |
| f5r   | 9    | Aristolochia rotunda (birthwort) | 40% | Book 3, Ch.4 | A = ~1/26 |
| f8v   | 16   | Hypericum perforatum (St. John's wort) | 40% | Book 3, Ch.154 (Hyperikon) | H = ~8/26 |
| f9r   | 17   | Nigella damascena | 65% | Book 3, Ch.79 (Melanthion) | N = ~14/26 |
| f9v   | 18   | Mandragora officinarum (mandrake) | 40% | Book 4, Ch.75 | M = ~13/26 |
| f41r  | 81   | Adiantum capillus-veneris (fern) | 60% | Book 4, Ch.134 | A = ~1/26 |
| f42r  | 82   | Daucus carota (wild carrot) | 45% | Book 3, Ch.52 | D = ~4/26 |
| f43r  | 85   | Rubia tinctorum (madder, cultivated) | 60% | Book 3, Ch.143 | R = ~18/26 |
| f47r  | 93   | Vitis vinifera (grape vine) | 70% | Book 5, Ch.1-2 (wines/vine) | V = ~22/26 |

---

## Test 1: Dioscorides' De Materia Medica Order

### The Dioscoridean Ordering Principle

Dioscorides organized his work into 5 books:
- **Book 1** (Ch.1-128): Aromatics, oils, ointments, trees, shrubs, gums, fruits (bay laurel Ch.106)
- **Book 2** (Ch.1-186): Animals, honey, milk, cereals, vegetables, pot herbs (cyclamen Ch.164)
- **Book 3** (Ch.1-158): Roots, juices, herbs, seeds (peony Ch.140, madder Ch.143, nigella/melanthion Ch.79, artichoke/scolymos Ch.14, rosemary/libanotis Ch.75, carrot/daukos Ch.52, hypericum Ch.154, birthwort/aristolochia Ch.4)
- **Book 4** (Ch.1-186): More herbs, ferns, mosses, fungi (mandrake Ch.75, maidenhair fern/adiantum Ch.134)
- **Book 5** (Ch.1-159): Wines, minerals, metals (grape vine Ch.1-2)

### Mapping Voynich Folios to Dioscorides Book/Chapter

| Folio | Plant | Dioscorides | Book.Chapter | Normalized Position (0-1) |
|-------|-------|-------------|-------------|--------------------------|
| f1r (seq 1) | Laurus | Book 1, Ch.106 | 1.106 | 0.13 |
| f2r (seq 3) | Paeonia | Book 3, Ch.140 | 3.140 | 0.55 |
| f2v (seq 4) | Cyclamen | Book 2, Ch.164 | 2.164 | 0.38 |
| f3r (seq 5) | Rubia | Book 3, Ch.143 | 3.143 | 0.56 |
| f3v (seq 6) | Cynara | Book 3, Ch.14 | 3.014 | 0.40 |
| f4r (seq 7) | Rosmarinus | Book 3, Ch.75 | 3.075 | 0.47 |
| f5r (seq 9) | Aristolochia | Book 3, Ch.4 | 3.004 | 0.39 |
| f8v (seq 16) | Hypericum | Book 3, Ch.154 | 3.154 | 0.57 |
| f9r (seq 17) | Nigella | Book 3, Ch.79 | 3.079 | 0.48 |
| f9v (seq 18) | Mandragora | Book 4, Ch.75 | 4.075 | 0.65 |
| f41r (seq 81) | Adiantum | Book 4, Ch.134 | 4.134 | 0.72 |
| f42r (seq 82) | Daucus | Book 3, Ch.52 | 3.052 | 0.44 |
| f43r (seq 85) | Rubia (2nd) | Book 3, Ch.143 | 3.143 | 0.56 |
| f47r (seq 93) | Vitis | Book 5, Ch.1 | 5.001 | 0.78 |

### Dioscorides Book-Level Correlation

Ordering by Voynich folio sequence and checking if Dioscorides book numbers increase:

```
f1r  -> Book 1 (Laurus)     -- FITS: Book 1 first
f2r  -> Book 3 (Paeonia)    -- SKIP: jumps to Book 3
f2v  -> Book 2 (Cyclamen)   -- BREAKS: goes backward to Book 2
f3r  -> Book 3 (Rubia)      -- semi-fits: back to Book 3
f3v  -> Book 3 (Cynara)     -- FITS: stays in Book 3
f4r  -> Book 3 (Rosmarinus) -- FITS: stays in Book 3
f5r  -> Book 3 (Aristol.)   -- FITS: stays in Book 3
f8v  -> Book 3 (Hypericum)  -- FITS: stays in Book 3
f9r  -> Book 3 (Nigella)    -- FITS: stays in Book 3
f9v  -> Book 4 (Mandragora) -- FITS: progresses to Book 4
f41r -> Book 4 (Adiantum)   -- FITS: stays in Book 4
f42r -> Book 3 (Daucus)     -- BREAKS: goes backward to Book 3
f43r -> Book 3 (Rubia 2nd)  -- BREAKS: stays in Book 3
f47r -> Book 5 (Vitis)      -- FITS: progresses to Book 5
```

**Book-level verdict**: Broadly consistent with Books 1->3->4->5 progression, but with 2-3 violations.

### Dioscorides Within-Book Chapter Correlation

Within Book 3 (the largest cluster, folios f2r through f9r):

```
f2r  -> Ch.140 (Paeonia)
f3r  -> Ch.143 (Rubia)       -- FITS: 140 -> 143 (adjacent!)
f3v  -> Ch.14  (Cynara)      -- BREAKS BADLY: 143 -> 14
f4r  -> Ch.75  (Rosmarinus)  -- semi-fits: 14 -> 75 (forward)
f5r  -> Ch.4   (Aristol.)    -- BREAKS: 75 -> 4
f8v  -> Ch.154 (Hypericum)   -- fits direction but big gap
f9r  -> Ch.79  (Nigella)     -- BREAKS: 154 -> 79
```

**Within-book verdict**: The chapter-level ordering within Book 3 does NOT follow Dioscorides' chapter sequence. The critical adjacency of Paeonia (Ch.140) and Rubia (Ch.143) IS notable but may be coincidental.

### Spearman Rank Correlation for Dioscorides

Using normalized Dioscorides positions (0-1) vs. folio sequence numbers:

| Folio Seq | Dioscorides Position |
|-----------|---------------------|
| 1 | 0.13 |
| 3 | 0.55 |
| 4 | 0.38 |
| 5 | 0.56 |
| 6 | 0.40 |
| 7 | 0.47 |
| 9 | 0.39 |
| 16 | 0.57 |
| 17 | 0.48 |
| 18 | 0.65 |
| 81 | 0.72 |
| 82 | 0.44 |
| 85 | 0.56 |
| 93 | 0.78 |

Computing Spearman rank correlation (ranks of folio seq vs ranks of Dioscorides position):

Folio rank:       1  2  3  4  5  6  7  8  9  10 11 12 13 14
Dioscorides rank: 1  8  3  9  4  6  5  10 7  11 13 6  9  14

**Spearman rho = approximately 0.68**

This is a moderate positive correlation. Not random, but not a tight match either.

### KEY FINDING: Paeonia-Rubia Adjacency

The most striking finding is that **Paeonia (f2r) and Rubia (f3r) are on consecutive folios** (bifolium 2 recto and 3 recto), and in Dioscorides they are chapters 140 and 143 -- separated by only 2 entries (Ch.141 = Polygonon, Ch.142 = Clematis). This adjacency in both the Voynich and Dioscorides is highly suggestive but not conclusive with only 2 data points.

---

## Test 2: Latin Alphabetical Order

### Mapping

| Folio Seq | Latin Name | Alpha Position |
|-----------|-----------|---------------|
| 1 | Laurus | 12 |
| 3 | Paeonia | 16 |
| 4 | Cyclamen | 3 |
| 5 | Rubia | 18 |
| 6 | Cynara | 3.5 |
| 7 | Rosmarinus | 18 |
| 9 | Aristolochia | 1 |
| 16 | Hypericum | 8 |
| 17 | Nigella (Melanthion) | 13 |
| 18 | Mandragora | 13 |
| 81 | Adiantum | 1 |
| 82 | Daucus | 4 |
| 85 | Rubia | 18 |
| 93 | Vitis | 22 |

Checking if the alphabetical positions increase with folio sequence:

```
L(12) -> P(16) -> C(3) -> R(18) -> C(3) -> R(18) -> A(1) -> H(8) -> N(13) -> M(13) -> A(1) -> D(4) -> R(18) -> V(22)
```

**Verdict: NO alphabetical Latin order whatsoever.** The sequence is completely non-monotonic. Spearman rho would be near 0 or slightly negative.

---

## Test 3: Italian/Vernacular Alphabetical Order

| Folio Seq | Italian Name | Alpha Position |
|-----------|-------------|---------------|
| 1 | Alloro/Lauro | A/L |
| 3 | Peonia | P |
| 4 | Ciclame | C |
| 5 | Robbia | R |
| 6 | Carciofo | C |
| 7 | Rosmarino | R |
| 9 | Aristolochia | A |
| 16 | Iperico | I |
| 17 | Nigella/Gittone | N/G |
| 18 | Mandragora | M |
| 81 | Capelvenere | C |
| 82 | Pastinaca | P |
| 85 | Robbia | R |
| 93 | Vite/Uva | V/U |

```
A -> P -> C -> R -> C -> R -> A -> I -> N/G -> M -> C -> P -> R -> V
```

**Verdict: NO Italian alphabetical order.** Same chaotic pattern as Latin.

---

## Test 4: Serapion/Arabic Therapeutic Order

Serapion the Younger's *Liber de Simplici Medicina* (widely used in 15th-century Italy, translated into Latin and Italian) organized plants by therapeutic category:

- **Hot/Dry drugs** (heating): rosemary, nigella, aristolochia, hypericum
- **Cold/Moist drugs** (cooling): cyclamen, lettuce, water plants
- **Purgatives**: madder, mandrake, birthwort
- **Wound herbs**: madder, hypericum
- **Aromatic/fragrant**: bay laurel, rosemary

However, Serapion's actual ordering was roughly alphabetical in Arabic transliteration, which does not map to any Latin/Italian alphabetical order. The Voynich sequence does not show clear therapeutic grouping either -- heating drugs (rosemary f4r, nigella f9r) are separated by cooling drugs (cyclamen f2v), and purgatives are scattered throughout.

**Verdict: No clear match to Serapion's ordering.**

---

## Test 5: Circa Instans / Platearius Order

The *Circa Instans* of Platearius (Salerno, 12th c., extremely influential in Italy) was roughly alphabetical by the Latin/Arabic name most commonly used. Its order would partially overlap with Latin alphabetical -- which we already tested and rejected.

**Verdict: No match.**

---

## Test 6: Therapeutic/Body-Part Order (Head-to-Foot)

Some medieval herbals organized plants by the body part they treat (head remedies first, then throat, chest, stomach, etc.):

- Head/brain: peony (epilepsy), bay laurel (headache)
- Respiratory: maidenhair fern, hypericum
- Digestive: nigella, artichoke, rosemary
- Urinary/kidney: madder
- Gynecological: birthwort, mandrake
- External/wounds: grape vine (wine as antiseptic)

This is too vague to test rigorously with only 14 data points, and the sequence doesn't obviously follow a head-to-foot progression.

**Verdict: Inconclusive, but no strong match.**

---

## Correlation Summary

| Ordering System | Spearman rho (approx.) | Verdict |
|----------------|----------------------|---------|
| **Dioscorides (book-level)** | **+0.68** | **Moderate positive -- best match** |
| Dioscorides (chapter-level within Book 3) | ~0.10 | No match within books |
| Latin Alphabetical | ~0.05 | No match |
| Italian Alphabetical | ~0.05 | No match |
| Serapion/Arabic | Not computable | No obvious match |
| Circa Instans | ~0.05 | No match (similar to Latin alpha) |
| Head-to-foot therapeutic | Inconclusive | No clear match |

---

## Assessment of the Dioscorides Hypothesis

### What Fits

1. **Book-level progression**: The sequence Book 1 (f1r) -> Book 3 (f2r-f9r) -> Book 4 (f9v-f41r) -> Book 5 (f47r) is broadly correct.
2. **Paeonia-Rubia adjacency**: These are chapters 140 and 143 in Dioscorides Book 3, and they appear on consecutive Voynich folios (f2r and f3r). This is the single strongest piece of evidence.
3. **Endpoint placement**: Bay laurel (Book 1, aromatics) opens the herbal, and grape vine (Book 5, wines) appears late. This matches Dioscorides' macro-structure.

### What Does NOT Fit

1. **Cyclamen (f2v)**: In Dioscorides, cyclamen is in Book 2 (Ch.164), but it appears AFTER peony (Book 3) in the Voynich. If following Dioscorides strictly, Book 2 plants should come before Book 3 plants.
2. **Chapter-level disorder**: Within Book 3, the chapter sequence is 140, 143, 14, 75, 4, 154, 79 -- essentially random.
3. **Daucus carota (f42r)**: A Book 3 plant appearing after Book 4 plants breaks the macro-sequence.
4. **Missing Book 2**: Very few Book 2 plants are identified. Dioscorides' Book 2 (animals, cereals, vegetables) may simply not be represented in a pharmaceutical herbal.

### Most Likely Interpretation

The Voynich herbal is **NOT a direct copy of Dioscorides' sequence** but may be organized according to a **tradition influenced by Dioscorides' categorical groupings**. The broad pattern (aromatics -> roots/herbs -> ferns/mosses -> wines/minerals) is Dioscoridean in spirit. Many medieval Italian herbals followed a "modified Dioscorides" order where the exact chapter sequence was scrambled but the general category progression was preserved.

This is consistent with a 15th-century North Italian pharmaceutical herbal that used Dioscorides as a source but reorganized plants according to local practice.

---

## Predictions: If Modified-Dioscorides Order Holds

If the Voynich herbal follows a rough Book 1 -> Book 3 -> Book 4 -> Book 5 progression, we can predict plant categories for unidentified folios:

### Early Herbal (f1r-f1v): Book 1 -- Aromatics, Trees, Oils
- f1r = Laurus (confirmed at 45%)
- f1v = Likely another aromatic tree/shrub. **Prediction: Cinnamomum (cinnamon/cassia), Myrtus (myrtle), or Styrax (storax)**

### Main Herbal Body (f2r-f40v): Primarily Book 3 -- Roots, Herbs, Seeds
This is the bulk of the herbal. Dioscorides Book 3 contains ~158 chapters. If the Voynich covers a selection of these, the unidentified folios in this range should be common pharmaceutical herbs from Book 3:

| Folio | Dioscorides Book 3 Prediction (based on position between known plants) |
|-------|------------------------------------------------------------------------|
| f4v-f5v | Between rosemary (3.75) and hypericum (3.154): Could be Gentiana (3.3), Glycyrrhiza (3.5), Iris (3.19), Asarum (3.67), Smyrnium (3.68) |
| f6r-f8r | Still Book 3 range: Could be Anethum (3.58 dill), Coriandrum (3.63), Petroselinum (3.66 parsley), Apium (3.64 celery), Foeniculum (3.74 fennel) -- Apiaceae cluster |
| f10r-f16v | Late Book 3 into Book 4 transition: Aconitum (4.77), Helleborus (4.148), Polypodium (4.186 polypody fern), Asplenium (4.138 spleenwort) |
| f17r-f25v | Book 3 continuation or Book 4: Artemisia (3.24/113), Centaurium (3.6), Plantago (3.106 plantain), Verbena (4.60) |

### Late Herbal (f41r-f48v): Book 4 -> Book 5
- f41r = Adiantum/fern (Book 4, confirmed)
- f42r = Daucus (Book 3 -- possible mis-ordering or a different plant)
- f43r = Rubia cultivation (Book 3 -- could be a "use/preparation" appendix)
- f44r-f46v = **Prediction: more Book 4 plants -- ferns, mosses, or transitional to Book 5 minerals**
- f47r = Vitis (Book 5, confirmed)
- f48r-f48v = **Prediction: Book 5 -- wine preparations, vinegar (Oxos 5.13), or mineral drugs**

### Specific High-Value Predictions

Based on the Dioscorides adjacency finding (Paeonia 3.140 / Rubia 3.143):

| Voynich Folio | Dioscorides Between-Chapter | Predicted Plant |
|---------------|---------------------------|-----------------|
| f2v (between Paeonia and Rubia) | 3.141-142 | **Polygonon (knotgrass) or Clematis** -- but f2v is identified as Cyclamen (Book 2), which breaks this |

The break at f2v suggests the ordering is NOT chapter-sequential within books.

---

## Critical Evaluation

### Confidence in Dioscorides Match: LOW-MODERATE (35%)

**Reasons for caution:**
1. With only 14 identified plants out of ~130 herbal pages, we are working with <11% of the data. Any apparent pattern could be a sampling artifact.
2. The "broad book-level progression" (aromatics -> herbs -> ferns -> wines) is so generic that MOST medieval herbals would show this pattern regardless of whether they followed Dioscorides specifically.
3. The within-book chapter ordering shows essentially no correlation.
4. Several individual placements actively violate Dioscorides order.

**Reasons for continued interest:**
1. The Paeonia-Rubia adjacency (3.140 / 3.143) is genuinely striking.
2. The broad progression does match.
3. Only 14 data points means low statistical power -- the pattern could emerge more clearly with more identifications.

### What Would Confirm or Refute

To confirm Dioscorides ordering, we would need:
- More plant identifications in the f10r-f40v range (currently a desert of data)
- Plants in the f25r-f40v range should be late Book 3 or Book 4 if Dioscorides holds
- Plants between f2r and f3r (if any exist on the verso sides) should be near Dioscorides 3.140-143

To refute:
- If f25r-f40v plants turn out to be Book 1 or Book 2 plants, the progression is broken
- If f48r plants are Book 1 plants, the progression is broken

---

## Alternative Hypothesis: Circa Instans with Local Modifications

The most common organizational scheme for North Italian pharmaceutical herbals in the 15th century was a loose adaptation of the *Circa Instans* tradition, which itself drew on Dioscorides but reorganized by:
1. Importance/frequency of use (most important drugs first)
2. Local availability
3. Therapeutic category within broad groups

This would explain:
- Why bay laurel (universally important) comes first
- Why peony and madder (major drugs) appear early
- Why grape vine (wines, the most universal medieval medicine) appears late (possibly in a "preparations" section)
- Why the exact chapter-level order doesn't match any single source

**This "importance-ordered pharmaceutical compendium" hypothesis may be more accurate than strict Dioscorides ordering, but it is also harder to test because it is less precisely predictive.**

---

## Conclusion

1. **No single known ordering system provides a strong match** to the Voynich herbal sequence.
2. **Dioscorides book-level ordering shows the best (but still moderate) correlation** at rho ~0.68.
3. **Alphabetical ordering (Latin or Italian) is definitively ruled out.**
4. **The Paeonia-Rubia adjacency** (Dioscorides 3.140/3.143) is the single most interesting finding and warrants further investigation.
5. **The most likely organizational scheme** is a "modified Dioscorides" or "importance-based pharmaceutical" ordering common in 15th-century Italian practice -- following broad categories (aromatics, roots/herbs, ferns, wines) without strict chapter-level fidelity.
6. **We cannot yet use the ordering to predict specific plants** on unknown folios with any confidence. The ordering provides only broad categorical predictions (e.g., "folios f25-f40 are probably Book 3-4 herbs").
7. **The path to decipherment through ordering** remains open but requires significantly more plant identifications (at least 30-40 of the ~130 herbal pages) to reach statistical significance.

### Priority Next Steps

1. **Identify more plants in the f10r-f40v gap** -- this is the critical data desert that prevents testing the Dioscorides hypothesis properly.
2. **Test the Paeonia-Rubia adjacency more rigorously** -- examine folios f2v (Cyclamen?) and f3v (Cynara?) for whether they could be re-identified as Dioscorides 3.141 (Polygonon) or 3.142 (Clematis).
3. **Check whether the f48r-f56v range contains mineral/wine content** as predicted by Dioscorides Book 5 placement of Vitis at f47r.
4. **Cross-reference with the Tractatus de Herbis and Carrara Herbal plant orderings** specifically (not just generic Dioscorides), as these are the closest known relatives to the Voynich illustration style.
