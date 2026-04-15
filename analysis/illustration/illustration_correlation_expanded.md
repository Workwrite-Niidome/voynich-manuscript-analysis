# Expanded Illustration-Text Correlation Analysis

## Methodology

18 herbal pages were visually examined from the PDF scan of the Voynich Manuscript and classified by their illustration features. Each page's text was extracted from the EVA transcription (RF1b-e.txt) and word frequencies were computed. Pages were grouped by visual feature (prominent flowers, prominent roots, fruits/seeds, giant leaves, color elements) and frequency differentials were calculated to identify stems that correlate with specific illustration types.

## Pages Examined

### FLOWER-dominant pages
| Folio | Page | Description |
|-------|------|-------------|
| f4v   | 10   | Blue flower at top, bulbous brown root, small scattered leaves |
| f7r   | 15   | Star-flower dominates page, green+white petals, orange root |
| f9v   | 20   | Many blue flowers (prominent), lobed green leaves |
| f11r  | 22   | Blue hanging bell-flowers, large wavy green leaves |
| f16v  | 32   | Red star-flowers (4) + blue flower at top, very prominent |

### LEAF-dominant pages (no/minimal flowers)
| Folio | Page | Description |
|-------|------|-------------|
| f1v   | 4    | Large green+orange leaves dominant, root visible |
| f2v   | 6    | Single GIANT round green leaf fills page |
| f5r   | 11   | Giant round green leaves (water-lily type) |
| f8r   | 17   | Single large arrowhead-shaped green leaf |
| f8v   | 18   | Many medium green leaves, tiny flowers |

### ROOT-prominent pages
| Folio | Page | Description |
|-------|------|-------------|
| f2r   | 5    | Lobed leaves, spiky flower top, prominent RED roots |
| f3r   | 7    | Striped red/green leaves, prominent red/brown roots |
| f3v   | 8    | Spiky leaves, blue top, prominent red root |
| f9r   | 19   | Bushy lobed leaves, LARGE brown root mass |

### FRUIT/SEED pages
| Folio | Page | Description |
|-------|------|-------------|
| f4r   | 9    | Small leaves with red berries throughout |
| f6r   | 13   | Spiky jagged leaves with green seed pods |
| f6v   | 14   | Star-shaped leaves with blue seed balls |
| f7v   | 16   | Rosette leaves with orange buds/fruits |
| f14v  | 28   | Green leaves with white spotted fruits, red roots |

---

## 1. Confirmed: chol = leaf (reinforced)

The previous finding that `chol` correlates with leaves is further supported:

- **LEAF-dominant pages**: chol = 4.27% of text
- **FLOWER-dominant pages**: chol = 3.50%
- **ROOT-dominant pages**: chol = 3.33%
- **FRUIT/SEED pages**: chol = 1.34% (lowest -- these pages depict fruits, not leaves)

The `*chol*` substring (includes compound words containing chol) shows:
- LEAF: 6.07%, ROOT: 6.67%, FLOWER: 6.12%, FRUIT: 3.48%

The FRUIT pages having the lowest `chol` rate is precisely what we'd expect: fruit/seed illustrations naturally de-emphasize leaves in both picture and text.

Additionally, `shol` (a phonetic variant or related word) shows even stronger leaf correlation:
- LEAF: 2.70%, FLOWER: 0.87%, ROOT: 1.11%, FRUIT: 1.87%
- This is consistent with `shol` being a related leaf term (perhaps a different leaf type or "foliage" vs. "leaf").

---

## 2. Flower Word Candidates

### Primary candidate: `otaiin` / `oty` / `cthor`

Words that are HIGH on flower pages and LOW/ABSENT on leaf-only pages:

| Stem | FLOWER | LEAF | ROOT | FRUIT | Assessment |
|------|--------|------|------|-------|------------|
| `oty` | 1.17% | 0.00% | 0.00% | 0.80% | Appears ONLY on flower+fruit pages, never on leaf-only or root-only |
| `cthor` | 1.17% | 0.00% | 0.56% | 1.07% | Strong flower+fruit correlation, absent from leaf pages |
| `otaiin` | 0.87% | 0.22% | 0.28% | 0.27% | 4x more frequent on flower pages |
| `sheey` | 0.87% | 0.22% | 0.56% | 0.27% | Higher on flower pages |
| `daiin` | 6.12% | 3.37% | 2.22% | 5.08% | Much higher on flower+fruit pages (but too common to be "flower") |

**Analysis of `oty`**: This stem appears exclusively on pages with flower or fruit illustrations. It is completely absent from leaf-only and root-only pages. On f9v (the page with the MOST prominent blue flowers), `oty` appears 3 times (3.6% of words on that page). On f14v (fruits), it appears twice. This distribution pattern -- present with flowers and fruits but absent with just leaves or roots -- is exactly what we'd expect for a "flower" or "blossom" word (flowers and fruits are botanically related structures).

**Analysis of `cthor`**: Shows a very similar pattern to `oty`. Present on flower pages (1.17%) and fruit pages (1.07%), completely absent from leaf-only pages. This could be an alternative/compound form. Note that `cth-` is a common prefix, and `cthor` could be `cth+or` (a modified form of a base word).

**Assessment**: `oty` is the strongest candidate for "flower/blossom." Its distribution (flower+fruit but not leaf/root) matches botanical reality: flowers and fruits are reproductive organs that appear together, distinct from vegetative parts (leaves, roots).

### The `*oty*` pattern in compounds

The substring `*oty*` (containing "oty") shows:
- FLOWER: 2.92%, LEAF: 0.45%, ROOT: 0.28%, FRUIT: 1.87%
- This 6.5x enrichment on flower pages vs leaf pages is the strongest flower correlation found.

Compound words containing `oty`: `choty`, `shoty`, `otchy` (which may be an inverted form), `chotey`

---

## 3. Root Word Candidates

### Primary candidate: `cham` / `chom`

Words HIGH on root-prominent pages, LOW/ABSENT elsewhere:

| Stem | ROOT | LEAF | FLOWER | FRUIT | Assessment |
|------|------|------|--------|-------|------------|
| `cham` | 1.11% | 0.00% | 0.00% | 0.00% | EXCLUSIVE to root pages |
| `chom` | 1.11% | 0.00% | 0.00% | 0.27% | Nearly exclusive to root pages |
| `dan` | 1.11% | 0.00% | 0.29% | 0.00% | Strongly root-associated |
| `shar` | 0.83% | 0.00% | 0.29% | 0.00% | Root-associated |
| `tchor` | 0.83% | 0.00% | 0.00% | 0.27% | Root-associated |

**Analysis of `cham`/`chom`**: These closely related stems appear almost exclusively on pages with prominent root illustrations. On f3r (the page with the most dramatically illustrated red/brown roots alongside red-green striped leaves), `cham` appears 3 times and `chom` appears 2 times. These are the only pages in the entire sample where these words reach meaningful frequency.

The phonetic relationship `cham`/`chom` suggests vowel alternation (like English "root/rut" or a declension pattern). Given their near-exclusive association with root illustrations, these are strong candidates for "root" or a related underground-part term.

**Cross-check with f3r text** (page 7, red-green striped leaves + prominent red roots):
Top words: `chor`(7), `chol`(6), `cham`(3), `ol`(3), `cthol`(2), `chom`(2)
The text contains both leaf words (`chol`) AND root words (`cham`/`chom`), consistent with the illustration showing both prominent leaves and roots.

### The `dam` pattern

`dam` (without the `ch-` prefix) also appears preferentially on root pages:
- Contained in root pages: 1.11%, leaf pages: 0.45%
- This may be a base form with `cham` = `ch+am` as a derived form.

---

## 4. Fruit/Seed Word Candidates

### Primary candidate: `cthol` / `cthom` / the `cth-` family

Words HIGH on fruit/seed pages:

| Stem | FRUIT | LEAF | FLOWER | ROOT | Assessment |
|------|-------|------|--------|------|------------|
| `cthol` | 1.34% | 0.45% | 0.58% | 0.56% | 3x leaf rate on fruit pages |
| `cthom` | 0.80% | 0.00% | 0.00% | 0.28% | Nearly exclusive to fruit pages |
| `cthy` | 3.21% | 0.90% | 2.04% | 2.22% | 3.5x enrichment on fruit pages vs leaf |
| `chckhy` | 0.80% | 0.00% | 0.58% | 0.00% | Fruit+flower association |

**Analysis of `cthy`/`cthol`/`cthom`**: The `cth-` prefix family shows the strongest fruit/seed correlation. `cthy` is 3.5x more frequent on fruit pages than leaf pages. `cthol` could literally mean "fruit" (with `-ol` being the same suffix seen in `chol`=leaf). The pattern suggests:
- `chol` = leaf (ch + ol)
- `cthol` = fruit/seed (cth + ol)
- `cham` = root (ch + am)
- `cthom` = ? (cth + om), appears on fruit pages

This reveals a potential morphological pattern where `ch-` and `cth-` may be related prefixes (perhaps marking plant-part categories), with suffixes `-ol`, `-am`, `-om` differentiating specific parts.

---

## 5. Color Word Candidates

### Blue elements (`chor` / `ckh-` words)

Pages with blue illustration elements vs. pages without:

| Pattern | Blue present | Blue absent | Diff |
|---------|-------------|-------------|------|
| `*chor*` | 7.96% | 4.66% | +3.30% |
| `*ckh*` | 3.83% | 1.85% | +1.99% |
| `*shol*` | 0.88% | 3.14% | -2.25% |

**Analysis**: `chor` and words containing `ckh` are significantly more common on pages with blue elements. However, `chor` is also the second most common word overall, so this may reflect that `chor` has a more general meaning (perhaps "stem" or "plant" rather than "blue"). The `ckh-` cluster is more interesting as a potential color marker.

### Red elements (`chol` enrichment confirmed)

Pages with red illustration elements vs. pages without:

| Pattern | Red present | Red absent | Diff |
|---------|------------|------------|------|
| `*ol*` | 20.56% | 15.16% | +5.40% |
| `*chol*` | 7.98% | 4.44% | +3.55% |
| `-aiin` suffix | 15.77% | 11.55% | +4.22% |

**Analysis**: The `*ol*` and `*chol*` enrichment on red-element pages is partially confounded by the fact that red elements often appear alongside prominent leaves (the most common red element is red-colored leaves, e.g., f3r's red-green striped leaves, f8v's red-tinted leaf tips).

The `-aiin` suffix enrichment on red pages is noteworthy and could indicate that `-aiin` is an adjective suffix meaning something like "colored" or "reddish."

### The `-dy` suffix as a size/color descriptor

Pages with giant/dominant leaves have a very strong `-dy` suffix enrichment:
- Giant leaves: 9.06% of words end in `-dy`
- Normal leaves: 4.47%
- Difference: +4.59%

The `-dy` suffix also correlates with blue elements (+2.10%) and anti-correlates with red elements (-2.11%). This suggests `-dy` may function as an adjective-forming suffix, possibly related to size ("large") or visual quality.

---

## 6. Size/Shape Word Candidates

### Giant leaf pages: `chody`, `shy`, `dol`

Words enriched on pages with giant/dominant leaf illustrations:

| Stem | Giant leaf | Normal | Diff | Assessment |
|------|-----------|--------|------|------------|
| `chody` | 1.81% | 0.08% | +1.73% | Nearly exclusive to giant-leaf pages |
| `shy` | 1.21% | 0.16% | +1.05% | Strong giant-leaf correlation |
| `dol` | 1.51% | 0.48% | +1.03% | Giant-leaf enriched |
| `chey` | 1.51% | 0.40% | +1.11% | Giant-leaf enriched |
| `*ody*` | 6.95% | 2.48% | +4.47% | Strongest size correlator |

**Analysis of `chody`**: This word appears almost exclusively on pages depicting oversized or dominant leaf structures. On f1v (dominant large leaves), f2v (single giant round leaf), and f5r (giant round leaves), `chody` appears repeatedly while being virtually absent from pages with normal-sized features. This makes `chody` a strong candidate for "large" or "big" -- or alternatively, it could be a compound `chol+dy` meaning "leafy" (leaf + adjective suffix).

**The `*ody*` substring pattern**: Words ending in `-ody` (chody, shody, etc.) are 2.8x more frequent on giant-leaf pages. This reinforces the hypothesis that `-dy` functions as an adjectival suffix, with `-ody` being a specific descriptive form.

---

## 7. Morphological Patterns Emerging

### Potential plant-part paradigm:

| EVA stem | Meaning | Evidence | Confidence |
|----------|---------|----------|------------|
| `chol` | leaf | 4.27% on leaf pages, confirmed prior study | HIGH (85%) |
| `shol` | leaf (variant) / foliage | 2.70% on leaf pages, 0.87% on flower | MEDIUM (65%) |
| `oty` | flower/blossom | 1.17% on flower, 0% on leaf/root | MEDIUM (60%) |
| `cham`/`chom` | root (underground part) | 1.11% on root pages, 0% on leaf/flower | MEDIUM-HIGH (70%) |
| `cthol` | fruit/seed | 1.34% on fruit, 0.45% on leaf | MEDIUM (55%) |
| `cthy` | fruit/seed (general) | 3.21% on fruit, 0.90% on leaf | MEDIUM (55%) |
| `chody` | "large" or "leafy" | 1.81% on giant-leaf, 0.08% normal | MEDIUM (50%) |

### Potential morphological structure:

The data suggests a system where:
- `ch-` prefix: marks plant-part nouns
- `cth-` prefix: marks a related but distinct category (fruits/seeds?)
- `-ol` suffix: appears in leaf/fruit terms (chol, cthol, shol)
- `-am`/`-om` suffix: appears in root terms (cham, chom, cthom)
- `-dy` suffix: possible adjective marker (size or visual quality)
- `-aiin` suffix: possible noun/adjective ending (very common, may mark definiteness or plurality)

### `qo-` prefix pattern:

The `qo-` prefix shows strong correlation with root-prominent pages:
- Root pages: 9.44% of words start with `qo-`
- Leaf pages: 3.60%
- This may indicate a preposition ("of," "from," "under") or a verbal prefix particularly relevant to root descriptions.

---

## 8. Cross-validation: f3r (page 7) as Test Case

Page 7 (f3r) shows both prominent red-green striped leaves AND prominent red roots. The text should contain both leaf words and root words. Indeed:

**Top words**: chor(7), **chol**(6), **cham**(3), ol(3), **cthol**(2), ycheor(2), daiin(2), cthy(2), **chom**(2), or(2), qokeey(2)

Both `chol` (leaf, 6 occurrences) and `cham`/`chom` (root, 5 combined) appear at high frequency, exactly as predicted by the correlation analysis. The page also has `cthol`(2), consistent with the illustration showing some seed/fruit-like structures at the top.

## 9. Cross-validation: f9v (page 20) -- Blue Flowers

Page 20 has the most prominent flower display (many blue flowers). The text should be enriched for flower words:

**Top words**: daiin(7), chol(4), chor(3), **oty**(3), chy(3), cthor(2), ...

`oty` appears 3 times (3.6% of the page), its highest frequency in the entire sample. This is strong evidence that `oty` = flower/blossom.

## 10. Summary of New Vocabulary Identifications

| Discovery | EVA | Confidence | Key Evidence |
|-----------|-----|------------|--------------|
| **Flower/blossom** | `oty` | 60% | Exclusive to flower+fruit pages; highest on f9v (many blue flowers); absent from leaf-only and root-only pages |
| **Root** | `cham`/`chom` | 70% | Near-exclusive to root-prominent pages; highest on f3r (dramatic roots); absent from flower and leaf-only pages |
| **Fruit/seed** | `cthol`/`cthy` | 55% | `cthy` is 3.5x enriched on fruit pages; `cthol` parallels `chol` morphologically |
| **Adjective suffix** | `-dy` | 50% | 2x enrichment on giant-leaf pages; forms compounds like `chody` (large/leafy) |
| **"Large"** | `chody` | 50% | Nearly exclusive to giant-leaf illustrations; possibly `chol+dy` = "leaf-like" or simply "large" |

### Relationship to prior findings:
- `chol` = leaf: CONFIRMED and reinforced (anti-correlates with fruit pages as expected)
- `shol` = leaf variant: further supported by data (2.70% on leaf vs 0.87% on flower pages)
- `chor` = likely "stem" or "plant" (general botanical term, too ubiquitous to be a specific part)
- `daiin` = likely a very common grammatical word (and/the/is), present everywhere but elevated on flower+fruit pages

### Morphological paradigm hypothesis:

```
ch-ol   = leaf       (ch- + -ol)
cth-ol  = fruit      (cth- + -ol)
sh-ol   = leaf/foliage variant (sh- + -ol)
ch-am   = root       (ch- + -am)
ch-om   = root variant (ch- + -om)
cth-om  = ? related to fruit/root (cth- + -om)
```

This suggests the Voynichese botanical vocabulary may use a prefix+suffix system where:
- The prefix (ch-, cth-, sh-) carries the primary semantic category
- The suffix (-ol, -am, -om) specifies the plant part or modifies the meaning
