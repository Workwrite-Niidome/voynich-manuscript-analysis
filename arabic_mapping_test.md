# EVA-to-Arabic Phoneme Mapping Test

## Premise

Test whether EVA characters can be mapped to Arabic phonemes, using the sandhi-derived phonological classes as constraints.

**Sandhi-derived classes** (from n/l/r suffix analysis):
- **Stops** (trigger -l before following word): k, l, r, d, t, e
- **Fricatives** (trigger -n): tsh, ckh, cph, cth, p, y, o, ch, f, sh
- **Vowels** (trigger -r): a, i

**Arabic consonant inventory** (28 consonants):
- Stops: b, t, d, k, q, hamza (+ emphatics T, D)
- Fricatives: f, th, dh, s, z, sh, H, kh, ayn, h (+ emphatics S, Z)
- Nasals: m, n
- Liquids: l, r
- Glides: w, y

---

## 1. Frequency-Based Mapping

### EVA phoneme frequencies (full corpus, 37,682 words)

| Rank | EVA | Freq% | Arabic (medical) | Freq% |
|---:|:---|---:|:---|---:|
| 1 | o | 15.98 | alif | 13.19 |
| 2 | y | 11.12 | lam | 11.54 |
| 3 | ch | 7.04 | mim | 6.59 |
| 4 | e | 6.80 | nun | 6.04 |
| 5 | l | 6.79 | waw | 5.49 |
| 6 | d | 6.68 | ya | 5.49 |
| 7 | k | 6.33 | ra | 4.95 |
| 8 | a | 5.01 | ha | 4.40 |
| 9 | r | 4.82 | ba | 3.85 |
| 10 | ai | 4.26 | ta | 3.85 |
| 11 | n | 3.94 | dal | 3.30 |
| 12 | t | 3.79 | fa | 3.30 |
| 13 | q | 3.45 | ayn | 3.30 |
| 14 | ee | 3.14 | sin | 3.08 |
| 15 | i | 2.71 | qaf | 2.75 |
| 16 | sh | 2.55 | kaf | 2.20 |
| 17 | s | 1.81 | Ha | 2.20 |
| 18 | p | 0.92 | jim | 1.98 |
| 19 | m | 0.68 | shin | 1.65 |
| 20 | cth | 0.57 | kha | 1.65 |

**Assessment**: The frequency distributions are broadly similar in shape (Zipfian), but the top ranks diverge. EVA has two very dominant characters (o at 16%, y at 11%) while Arabic has alif and lam at similar frequencies. The rank correlation is moderate but non-specific -- any language with 20+ characters will show similar broad shapes.

**Critical issue**: EVA has prominent digraph phonemes (ch, sh, ai, ee) that have no direct Arabic analog as single letters. Arabic bigrams like "al" are frequent, but they represent two separate letters, not fused units. The EVA parsing treats "ch" as a single phoneme, which would require mapping to a single Arabic consonant.

---

## 2. Distributional Mapping (Syllable Structure)

Arabic has strict phonotactic constraints:
- Syllable types: CV, CVC, CVV, CVVC, CVCC (final only)
- **No initial consonant clusters** (no CC- onsets)
- Maximum one consonant in onset position

### Test: EVA word-initial patterns

**With broad vowel set (a, i, o, e, y as vowels):**

| Pattern | Count | Percentage | Arabic compatible? |
|:---:|---:|---:|:---:|
| CV | 3,069 | 63.6% | Yes |
| VC | 1,064 | 22.1% | Yes (hamza onset) |
| CC | 562 | 11.6% | **No** |
| VV | 130 | 2.7% | Marginal |

**With sandhi-derived vowel set (a, i only):**

| Pattern | Count | Percentage | Arabic compatible? |
|:---:|---:|---:|:---:|
| CC | 3,976 | 82.4% | **No** |
| CV | 726 | 15.0% | Yes |
| VC | 63 | 1.3% | Yes |
| VV | 60 | 1.2% | Marginal |

**Verdict**: This is the most damaging test for Arabic. If the sandhi analysis is correct that only a and i are vowels, then **82.4% of EVA words begin with consonant clusters**, which is flatly impossible in Arabic. Even with the broad vowel interpretation (o, e, y as vowels), 11.6% CC onsets is higher than Arabic allows (0%).

The sandhi-derived phonological system and Arabic phonotactics are **fundamentally contradictory**. Arabic requires o, e, y to be vowels for syllable structure to work, but the sandhi system classifies them as consonants/fricatives.

---

## 3. Known Word Test

### chol = "leaf" (Arabic: waraq)

**chol** parses as: ch - o - l (3 EVA phonemes)
**waraq** consonantal skeleton: w - r - q (3 Arabic consonants)

In Arabic abjad writing, short vowels are omitted, so waraq is written as w-r-q. The 3-unit match with chol is superficially encouraging.

**Required mapping**: ch -> w, o -> r, l -> q

**Sandhi class check**:
- ch is in **fricative** class -> w is a **glide** (partial match: glides pattern with fricatives in some frameworks)
- o is in **fricative** class -> r is a **liquid** (poor match)
- l is in **stop** class -> q is a **stop** (good match)

**But**: If EVA records vowels (a, i are vowels), then chol = C-V-C structure (1 syllable). Arabic waraq = wa.raq = 2 syllables with 2 vowels. The length mismatch is a problem.

**Cross-check with other words**:
- shol (sh-o-l): would need to map to ?-r-q = "?rq" -- no obvious Arabic match
- chor (ch-o-r): would be w-r-? -- wrq minus final consonant?
- chol appears 353 times -- plausible frequency for "leaf" in an herbal

**Alternative analyses**:
- chol = Arabic "kull" (all/every): ch->k, o->u, l->l. Phonetically possible but semantically wrong for herbal context.
- chol = CVC root pattern (Arabic fu'l, fi'l, etc.): Would need to identify the root consonants.

**Verdict**: The chol -> waraq mapping is **not compelling**. The phonological class assignments create mismatches, and no consistent mapping extends to other common EVA words.

### Other plant terms tested

| Arabic term | Consonantal | EVA candidate | Match? |
|:---|:---|:---|:---:|
| waraq (leaf) | w-r-q | chol (ch-o-l) | Weak |
| jadr (root) | j-dh-r | -- | No candidate |
| zahra (flower) | z-h-r | -- | No candidate |
| bazr (seed) | b-dh-r | -- | No candidate |

---

## 4. Judeo-Arabic Test

Judeo-Arabic (Arabic written in Hebrew script) was the standard for Jewish scholars writing medical and philosophical texts in the medieval Islamic world, including Maimonides' medical works.

### Inventory comparison

| System | Consonant count |
|:---|---:|
| Standard Arabic | 28 |
| Judeo-Arabic (Hebrew consonants) | ~22 |
| EVA core phonemes (>1% frequency) | ~17 |

The Judeo-Arabic reduction from 28 to 22 consonants brings it closer to EVA's count, but still leaves a gap.

### Hebrew-Arabic consonant mergers

| Arabic pair | Hebrew equivalent | Merged? |
|:---|:---|:---:|
| ta + tha | tav | Yes |
| dal + dhal | dalet | Yes |
| dad + zha | tsade/zayin | Yes |
| sin + shin | samekh + shin | **No** (distinct) |
| ayn + ghayn | ayin | Yes |
| ha + kha | he + khet | **No** (distinct) |

These mergers reduce the inventory but don't match EVA's specific phonological class structure.

### Arguments for Judeo-Arabic

1. **Reduced inventory** is closer to EVA
2. **Medical text tradition** (Maimonides, Ibn Zuhr) provides context
3. **Abbreviation conventions** (rashei tevot) could explain short EVA words (s, y, r, ol, ar, al)
4. **Double encoding** (Arabic -> Hebrew script -> cipher) could explain difficulty

### Arguments against Judeo-Arabic

1. **Matres lectionis contradiction**: In Judeo-Arabic, alef/waw/yod mark long vowels. If EVA o and y correspond to waw and yod, they should behave as vowels. But sandhi classifies them as fricatives/consonants.
2. **Syllable structure** still fails -- Arabic phonotactics are preserved in Judeo-Arabic
3. **Morphological patterns** (trilateral roots, broken plurals, Form I-X verbs) should be visible in EVA word structure but are not
4. **ta marbuta** (feminine ending -a/-at) is ubiquitous in Arabic medical texts but has no clear EVA counterpart

**Verdict**: Judeo-Arabic is more plausible than standard Arabic due to reduced inventory, but it still fails the structural tests. The syllable structure problem is not resolved by changing the script.

---

## 5. Five Trial EVA->Arabic Mappings

### F1R first 10 words decoded

**Original**: fachys, ykal, ar, taiin, shol, shory, ses, y, kor, sholdy

| Mapping | fachys | ykal | ar | taiin | shol | shory |
|:---|:---|:---|:---|:---|:---|:---|
| MAP 1 (freq rank) | Shmls | lrhw | hb | dhqqt | aynaw | aynabl |
| MAP 2 (sandhi) | zakhhs | hqal | ar | taiin | shaynl | shaynrh |
| MAP 3 (Judeo-Ar) | tsakys | yqal | ar | taiin | shwl | shwry |
| MAP 4 (phonetic) | ghaHys | ykal | ar | taiin | shal | shary |
| MAP 5 (pharma) | Taaynhf | hral | am | bayyd | swl | swmh |

### chol under each mapping

| Mapping | chol -> | Resembles waraq? |
|:---|:---|:---:|
| MAP 1 | maw | No |
| MAP 2 | khaynl | No |
| MAP 3 | kwl | No (but valid CuL pattern) |
| MAP 4 | Hal | No |
| MAP 5 | aynwl | No |

### daiin (most frequent word, 676 occurrences) under each mapping

| Mapping | daiin -> | Plausible Arabic? |
|:---|:---|:---:|
| MAP 1 | yhqqt | No |
| MAP 2 | daiin | (identity -- coincidence of mapping) |
| MAP 3 | daiin | (identity) |
| MAP 4 | daiin | (identity) |
| MAP 5 | qayyd | Marginal (qayd = "binding"?) |

**None of the five mappings produces recognizable Arabic pharmaceutical vocabulary.**

---

## 6. Bigram Compatibility

For each trial mapping, EVA bigrams were transformed to Arabic bigrams and compared against known Arabic bigram frequency distributions.

| Mapping | Overlap score | Arabic bigrams found | "al" bigram % |
|:---|---:|---:|---:|
| MAP 1 (freq rank) | 0.355 | 32/32 | 0.26% |
| MAP 2 (sandhi) | 0.257 | 26/32 | 2.43% |
| MAP 3 (Judeo-Arabic) | 0.301 | 29/32 | 2.43% |
| MAP 4 (phonetic) | **0.446** | 28/32 | **6.66%** |
| MAP 5 (pharma) | 0.280 | 29/32 | 2.43% |

MAP 4 (phonetic similarity) scores highest, primarily because it preserves several identity mappings (k->k, d->d, etc.) and maps o->a, producing the "al" bigram at 6.66%. However, Arabic texts typically show "al" at 10-15%, so even the best mapping underperforms.

**Note**: An overlap score of 0.446 is not strong. Random mappings between similarly-sized alphabets typically score 0.15-0.25, so MAP 4's score is above chance but far below what would indicate a genuine match (which should be >0.7).

---

## Overall Verdict

### Quantitative summary

| Test | Arabic compatibility | Score |
|:---|:---|:---:|
| Frequency distribution | Broadly similar (non-specific) | Neutral |
| Syllable structure (sandhi vowels) | 82% CC onsets -- impossible | **FAIL** |
| Syllable structure (broad vowels) | 12% CC onsets -- marginal | Weak |
| Known word (chol = waraq) | No convincing mapping | **FAIL** |
| Morphological patterns | No trilateral roots visible | **FAIL** |
| Definite article al- | 1.5-4.3% vs expected 10-15% | **FAIL** |
| Vowel inventory | 2 vs 3+ needed | Weak |
| Bigram overlap | Best score 0.446 (needs >0.7) | **FAIL** |
| Judeo-Arabic reduced inventory | 22 vs EVA ~17 -- closer | Weak+ |
| Word-final distribution | -y at 39% has no Arabic analog | **FAIL** |

### Structural contradictions

The fundamental problem is that the sandhi-derived phonological classes and Arabic phonotactics are **mutually exclusive**:

1. Sandhi says o, y, e are **consonants** (fricative class)
2. Arabic requires o, y, e to be **vowels** for syllable structure to work
3. No resolution exists that satisfies both constraints simultaneously

### Conclusion

**Arabic (including Judeo-Arabic) is unlikely to be the underlying language of the Voynich manuscript.** The evidence against is structural and systematic, not merely a matter of finding the right substitution cipher. The phonological class system derived from sandhi analysis is incompatible with Arabic's strict CV syllable requirements at the most basic level.

The one partial positive -- that MAP 3 (Judeo-Arabic) produces "kwl" for chol, which has an Arabic CuL morphological pattern -- is too weak and isolated to overcome the systematic failures across all other tests.

If Arabic is somehow involved, it would have to be through a mechanism far more complex than simple character substitution -- perhaps a nomenclator, abbreviation system, or steganographic encoding that completely obscures the source language's phonotactic structure. But such a system would also explain why the text doesn't look like *any* natural language under simple substitution.
