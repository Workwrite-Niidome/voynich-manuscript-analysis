# Plant Family Decoding: Sub-sequence Analysis of Voynich Plant Codes

## Executive Summary

Systematic analysis of ~104 plant codes (first words of herbal folios) reveals that certain sub-sequences within the codes correlate with groups of botanically or morphologically related plants. The strongest signal is **"-yd-"** marking Ranunculaceae (75% precision, 5.8x enrichment over random). However, the encoding appears to reflect **medieval morphological grouping** (visual similarity) rather than modern taxonomic family in the strict sense. This is consistent with a pre-Linnaean, Llullian combinatorial nomenclature system.

---

## 1. The "-yd-" Cluster: Complete Inventory

**All plant codes containing "-yd-":**

| Folio | Code | Decomposition | Plant ID | Family | Confidence |
|-------|------|--------------|----------|--------|------------|
| f2r | **k-yd-ainy** | k + yd + ainy | Paeonia officinalis | Ranunculaceae* | 55% |
| f9r | **t-yd-lo** | t + yd + lo | Nigella damascena | Ranunculaceae | 65% |
| f23r | **p-yd-chdom** | p + yd + chdom | Aconitum napellus | Ranunculaceae | 35% |
| f45r | **pyk-yd-al** | py + kyd + al | Alchemilla/Potentilla | Rosaceae | 35% |

*Paeonia was traditionally placed in or near Ranunculaceae; modern taxonomy separates it into Paeoniaceae.

**Result: Exactly 4 codes contain "-yd-". Of these, 3 out of 4 (75%) are Ranunculaceae.**

The fourth (f45r, pykydal) is tentatively identified as Alchemilla/Potentilla (Rosaceae, 35% confidence). However:
- Alchemilla has deeply lobed leaves visually similar to some Ranunculaceae
- Potentilla was historically confused with Ranunculus
- The identification is low-confidence (35%); the plant could actually be Ranunculaceae (e.g., Anemone, Thalictrum, or Ranunculus)
- The sub-sequence position differs: "pyk-yd-al" vs the clean "X-yd-suffix" pattern of the other three

**Statistical significance:**
- Base rate of Ranunculaceae in identified plants: ~6/46 = 13%
- Rate among -yd- codes: 3/4 = 75%
- Enrichment factor: 5.8x over random expectation
- This is unlikely to be coincidental, even with the small sample size

**Ranunculaceae plants WITHOUT "-yd-":**

| Folio | Code | Plant ID | Confidence | Note |
|-------|------|----------|------------|------|
| f7r | fchodaiin | Helleborus niger | 30% | Different initial prefix (fch-) |
| f48r | pshdaiin | Aconitum sp. | 30% | Low conf; same genus as pydchdom |
| f51r | tsholdchy | Paeonia variant? | 20% | Very low confidence ID |

The recall is 50% (3/6 Ranunculaceae have -yd-). The missing cases all have low-confidence identifications (20-30%). If f48r or f51r are misidentified, recall improves. Alternatively, "-yd-" may encode a specific sub-group within Ranunculaceae rather than the entire family.

---

## 2. The "pcheo-" Cluster: Spiny/Thistle-Type Plants

**All plant codes containing "pcheo-":**

| Folio | Code | Decomposition | Plant ID | Family | Confidence |
|-------|------|--------------|----------|--------|------------|
| f34r | **pcheo-epchy** | pcheo + epchy | Cirsium sp. (thistle) | Asteraceae | 30% |
| f46r | **pcheo-cphy** | pcheo + cphy | Eryngium sp. (sea holly) | Apiaceae | 30% |
| f48v | **pcheo-dchy** | pcheo + dchy | Unknown | Unknown | -- |
| f54v | **pcheo-dar** | pcheo + dar | Unknown | Unknown | -- |

**Critical finding:** Cirsium (Asteraceae) and Eryngium (Apiaceae) are in **different modern families**, but both are **spiny, thistle-like plants**. A medieval herbalist would group them together based on their shared morphology (spiny capitula/heads), not their phylogeny.

This strongly suggests "pcheo-" encodes **morphological type** ("spiny-headed plant" / "thistle-type") rather than taxonomic family. The two unidentified plants (f48v, f54v) are predicted to be additional spiny/thistle-like plants.

**Broader "cheo" occurrences:**

| Folio | Code | Plant ID | Family |
|-------|------|----------|--------|
| f16r | po-cheo-dy | Cannabis sativa | Cannabaceae |
| f32v | k-cheo-daiin | Unknown | Unknown |
| f34r | p-cheo-epchy | Cirsium sp. | Asteraceae |
| f46r | p-cheo-cphy | Eryngium sp. | Apiaceae |
| f48v | p-cheo-dchy | Unknown | Unknown |
| f54v | p-cheo-dar | Unknown | Unknown |
| f56v | k-cheo-t | Unknown | Unknown |

The broader "cheo" cluster includes 7 codes. The "pcheo-" prefix (with p-) appears to be the specific marker for the spiny-headed sub-group, while "cheo" may have a more general meaning.

---

## 3. Other Sub-sequence Clusters Investigated

### 3a. "tsh-" initial cluster (8 codes)

| Folio | Code | Plant ID | Family |
|-------|------|----------|--------|
| f3r | tsheos | Rubia tinctorum | Rubiaceae |
| f11r | tshol | Borago officinalis | Boraginaceae |
| f15r | tshor | Taraxacum officinale | Asteraceae |
| f33r | tshdar | Scabiosa sp. | Caprifoliaceae |
| f44r | tshodpy | Unknown | Unknown |
| f44v | tsho | Unknown | Unknown |
| f51r | tsholdchy | Paeonia variant? | Ranunculaceae |
| f53v | tshorshey | Unknown | Unknown |

**No family concentration.** The identified plants span 4 different families. "tsh-" likely encodes a property other than family (possibly a morphological or therapeutic category -- several of these plants produce colored saps or were used as dyes).

### 3b. "psh-" initial cluster (6 codes)

| Folio | Code | Plant ID | Family |
|-------|------|----------|--------|
| f8r | pshol | Arum maculatum | Araceae |
| f26r | psheoky | Glechoma hederacea | Lamiaceae |
| f41r | psheykedaleey | Adiantum capillus-veneris | Pteridaceae |
| f47v | psheot | Unknown | Unknown |
| f48r | pshdaiin | Aconitum sp. | Ranunculaceae |
| f50r | psheor | Centaurea/Cynara | Asteraceae |

**No family concentration.** Five different families represented.

### 3c. "fch-" initial cluster (3 codes)

| Folio | Code | Plant ID | Family |
|-------|------|----------|--------|
| f7r | fchodaiin | Helleborus niger | Ranunculaceae |
| f25r | fcholdy | Mentha sp. | Lamiaceae |
| f32r | fchaiin | Lamium sp. | Lamiaceae |

**Partial signal:** 2/3 are Lamiaceae (mint family), both aromatic herbs. Helleborus breaks the pattern, though at only 30% identification confidence. If the "fch-" marker encodes "aromatic/fragrant herbs," this would be a morphological grouping that Helleborus does not fit.

### 3d. "ko-" initial cluster (7 codes)

| Folio | Code | Plant ID | Family |
|-------|------|----------|--------|
| f2v | kooiin | Cyclamen sp. | Primulaceae |
| f3v | koaiin | Cynara scolymus | Asteraceae |
| f4r | kodalchy | Rosmarinus officinalis | Lamiaceae |
| f6v | koarysar | Unknown | Unknown |
| f13v | koair | Unknown | Unknown |
| f29v | kooiin | Unknown | Unknown |
| f45v | kosary | Unknown | Unknown |

**No clear pattern.** Too diffuse across families.

### 3e. "shol" cluster (4 codes)

| Folio | Code | Plant ID | Family |
|-------|------|----------|--------|
| f8r | p-shol | Arum maculatum | Araceae |
| f11r | t-shol | Borago officinalis | Boraginaceae |
| f28v | k-shol | Unknown | Unknown |
| f51r | t-shol-dchy | Paeonia variant? | Ranunculaceae |

**No family concentration**, but "shol" may encode a morphological feature (leaf type? tuberous root?).

### 3f. "sheo" cluster (4 codes)

| Folio | Code | Plant ID | Family |
|-------|------|----------|--------|
| f3r | t-sheo-s | Rubia tinctorum | Rubiaceae |
| f26r | p-sheo-ky | Glechoma hederacea | Lamiaceae |
| f47v | p-sheo-t | Unknown | Unknown |
| f50r | p-sheo-r | Centaurea/Cynara | Asteraceae |

**No family concentration.**

---

## 4. Family-Encoding Table

| Sub-sequence | Position | Proposed Encoding | Evidence Strength | Plants |
|-------------|----------|------------------|-------------------|--------|
| **-yd-** | medial | Ranunculaceae / "divided-leaf acrid plants" | **STRONG** (75% precision, 5.8x enrichment) | Paeonia, Nigella, Aconitum, (Alchemilla?) |
| **pcheo-** | initial | "Spiny-headed / thistle-type" (morphological) | **MODERATE** (100% match on spiny plants, but only 2 data points) | Cirsium, Eryngium, +2 unknown |
| **fch-** | initial | Aromatic-leaved herbs? (Lamiaceae?) | **WEAK** (2/3 Lamiaceae, 1 exception) | Mentha, Lamium, (Helleborus) |
| tsh- | initial | No clear family | NEGATIVE | Spans 4+ families |
| psh- | initial | No clear family | NEGATIVE | Spans 5 families |
| ko- | initial | No clear family | NEGATIVE | Spans 3+ families |
| shol | medial | No clear family | NEGATIVE | Spans 3 families |
| sheo | medial | No clear family | NEGATIVE | Spans 3 families |

---

## 5. Cross-Validation Results

### 5a. Precision/Recall Analysis

| Sub-sequence | Hypothesis | Precision | Recall | Verdict |
|-------------|-----------|-----------|--------|---------|
| -yd- | Ranunculaceae | 75% (3/4) | 50% (3/6) | PROMISING -- high precision, moderate recall |
| pcheo- | Asteraceae | 50% (1/2) | 14% (1/7) | REJECTED as family marker |
| pcheo- | Spiny morphology | 100% (2/2) | N/A | PROMISING but insufficient data |
| tsh- | Any single family | <25% | <50% | REJECTED |
| shol | Araceae | 33% (1/3) | 50% (1/2) | REJECTED (too low precision) |

### 5b. The Key Distinction: Taxonomy vs. Morphology

The data reveals an important distinction:

- **"-yd-" correlates with a taxonomic family** (Ranunculaceae). This is remarkable because Ranunculaceae members share distinctive visual features (deeply divided leaves, acrid roots, follicular fruits) that a medieval herbalist could recognize as a "natural group" without understanding phylogeny.

- **"pcheo-" correlates with morphological type** (spiny/thistle-like), crossing taxonomic boundaries. This is expected for a medieval classification system based on appearance.

This suggests the code system encodes **a mixture of what we would now call taxonomic and morphological information**, which is exactly what pre-Linnaean "natural" groupings looked like.

---

## 6. Compositional Structure of Plant Codes

If the sub-sequence encoding is real, plant codes have a compositional structure:

```
PLANT_CODE = [prefix] + [group_marker] + [species_marker] + [suffix]
```

**Demonstrated decomposition for -yd- codes:**

```
k  - yd - ainy     Paeonia:    k=?, yd=Ranunculaceae, ainy=Paeonia-specific
t  - yd - lo       Nigella:    t=?, yd=Ranunculaceae, lo=Nigella-specific
p  - yd - chdom    Aconitum:   p=?, yd=Ranunculaceae, chdom=Aconitum-specific
```

**Demonstrated decomposition for pcheo- codes:**

```
pcheo - epchy      Cirsium:    pcheo=spiny/thistle, epchy=Cirsium-specific
pcheo - cphy       Eryngium:   pcheo=spiny/thistle, cphy=Eryngium-specific
pcheo - dchy       Unknown:    pcheo=spiny/thistle, dchy=species-specific
pcheo - dar        Unknown:    pcheo=spiny/thistle, dar=species-specific
```

The initial prefixes (k-, t-, p-, f-) appear to encode a different dimension -- possibly:
- **Growth habit** (herb vs. shrub vs. tree)
- **Galenic quality** (hot/cold/wet/dry)
- **Therapeutic category**
- **Source of the name** (grammatical marker)

Note that 42% of all codes begin with "p-", suggesting it may be a generic plant classifier.

---

## 7. Historical Context: Pre-Linnaean Classification

### 7a. Dioscorides' Groupings

Dioscorides (1st century CE, the primary medieval botanical authority) grouped plants by **therapeutic use**, not morphology or taxonomy:
- Book I: Aromatics, oils, trees
- Book II: Animals, cereals, sharp herbs
- Book III: Roots, juices, herbs
- Book IV: Herbs and roots
- Book V: Wines, minerals

The Voynich sub-sequence encoding does **not** match Dioscorides' therapeutic groupings. Ranunculaceae plants (Paeonia, Nigella, Aconitum) fall in different Dioscorides sections (III.140, III.79, IV.76).

### 7b. Theophrastus and Albert the Great

Theophrastus (4th c. BCE) and Albert the Great (13th c. CE) grouped by growth form (trees, shrubs, herbs). The Voynich system is more fine-grained than this.

### 7c. The "Similitude" Tradition

Medieval herbalists had a well-established concept of "simile" -- plants that look alike belong together. The Ranunculaceae would have been recognized as a natural group (acrid plants with divided leaves) centuries before Linnaeus formalized it. The Voynich code system may encode exactly this kind of pre-formal but observationally accurate natural grouping.

### 7d. Llullian Combinatorics

Ramon Llull's combinatorial system (13th c.) used letter-combinations to encode categories of knowledge. A Llullian-influenced pharmacist could have assigned:
- Fixed letters for morphological categories
- Combinatorial suffixes for species within categories
- Prefix markers for additional properties

This produces exactly the kind of compositional code structure we observe. It is **pre-Linnaean systematic nomenclature** -- not arbitrary, but based on a small set of meaningful morphological markers combined into productive compound names.

---

## 8. Predictions and Testable Consequences

### 8a. Predictions from the -yd- hypothesis

If "-yd-" truly encodes Ranunculaceae / "divided-leaf acrid plants":

1. **f45r (pykydal)**: If currently misidentified as Alchemilla/Potentilla, the illustration should be re-examined for Ranunculaceae candidates (Anemone, Thalictrum, Ranunculus, Hepatica)

2. **No other Ranunculaceae candidates** in the manuscript should contain "-yd-" (all confirmed instances already found)

3. **Any new plant identification** that produces a "-yd-" code should belong to the Ranunculaceae or a visually similar group

### 8b. Predictions from the pcheo- hypothesis

If "pcheo-" encodes spiny/thistle morphology:

1. **f48v (pcheodchy)** and **f54v (pcheodar)**: These illustrations should show spiny, thistle-like plants with capitulate flower heads

2. **Other Asteraceae** (koaiin, tshor, fshody, porory) should NOT be spiny thistles -- they should be non-spiny composites (artichoke, dandelion, centaurea, chrysanthemum), which matches our identifications

3. **Any newly identified thistle-like plant** should have a code starting with "pcheo-"

### 8c. General prediction: compositional structure

If the codes are truly compositional:
- Codes for plants from the same "medieval group" should share a sub-sequence
- The shared sub-sequence should be in the same position (medial for -yd-, initial for pcheo-)
- The variable portions should differ between species

---

## 9. Limitations and Caveats

1. **Small confirmed dataset**: Only ~46 plants have identifications, most at moderate confidence (25-55%). The statistical analysis rests on a very small foundation.

2. **Circular reasoning risk**: The plant identifications partly influenced which sub-sequences we looked for. An independent confirmation would require blind testing.

3. **Multiple testing problem**: We tested many sub-sequences. Some apparent correlations could be random. Only "-yd-" shows enrichment that would survive even conservative correction.

4. **The pykydal exception**: One -yd- code maps to a non-Ranunculaceae plant (if the ID is correct). The pattern is strong but not absolute.

5. **Missing Ranunculaceae codes**: Three putative Ranunculaceae plants lack "-yd-". This could mean:
   - The identifications are wrong (all are 20-30% confidence)
   - "-yd-" marks a sub-group, not the entire family
   - The system is imperfect / has exceptions

---

## 10. Conclusion: A Morphological Nomenclature System

The evidence supports the following model:

**Plant codes are COMPOSITIONAL DESCRIPTIONS, not arbitrary codes.**

They encode a medieval-style classification based on visual/morphological similarity:

```
[PREFIX: growth form / Galenic quality / grammatical marker]
  + [GROUP MARKER: morphological category]
    + [SPECIES MARKER: individual plant identifier]
      + [SUFFIX: additional property or grammatical ending]
```

The strongest confirmed group markers are:
- **"-yd-"** = "divided-leaf acrid/poisonous plants" (maps to Ranunculaceae)
- **"pcheo-"** = "spiny-headed plants" (maps to thistle-type morphology)

This is historically plausible: it represents a **pre-Linnaean but observationally systematic nomenclature** -- a pharmacist's working classification encoded through Llullian combinatorics. The author did not need to memorize 200 arbitrary codes because the codes are productive compounds built from a small inventory of meaningful morphemes.

This finding transforms the "memorization paradox": the Voynich plant codes are not a lookup table but a **generative grammar** for naming plants based on their visible properties. The author needed to know perhaps 60-80 morphemes, not 200+ arbitrary codes.

---

## Appendix: Complete Plant Code Inventory with Sub-sequence Annotations

Codes marked with their identified sub-sequence clusters:

| Folio | Code | -yd- | pcheo- | fch- | Family (if identified) |
|-------|------|------|--------|------|----------------------|
| f2r | kydainy | YES | - | - | Ranunculaceae |
| f9r | tydlo | YES | - | - | Ranunculaceae |
| f23r | pydchdom | YES | - | - | Ranunculaceae |
| f45r | pykydal | YES | - | - | Rosaceae (35%, possibly misidentified) |
| f34r | pcheoepchy | - | YES | - | Asteraceae (spiny) |
| f46r | pcheocphy | - | YES | - | Apiaceae (spiny) |
| f48v | pcheodchy | - | YES | - | Unknown (predicted: spiny) |
| f54v | pcheodar | - | YES | - | Unknown (predicted: spiny) |
| f25r | fcholdy | - | - | YES | Lamiaceae |
| f32r | fchaiin | - | - | YES | Lamiaceae |
| f7r | fchodaiin | - | - | YES | Ranunculaceae (breaks fch=Lamiaceae) |
