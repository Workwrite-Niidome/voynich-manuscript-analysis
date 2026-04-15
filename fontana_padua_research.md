# Giovanni Fontana, the Padua-Venice Milieu, and the Voynich Manuscript

## Research compiled 2026-04-06

---

## 1. Giovanni Fontana's Cipher System

### Biography

Giovanni Fontana (c. 1395 - c. 1455), also known as Johannes de Fontana, was a Venetian-born physician and engineer. He attended the University of Padua, receiving his degree in arts in 1418 and medicine in 1421. He is a near-exact contemporary of whoever created the Voynich manuscript (vellum radiocarbon-dated 1404-1438).

### The Two Cipher Manuscripts

Fontana produced two major works written partly or entirely in cipher:

1. **Bellicorum instrumentorum liber** (Book of War Machines, 1420s, Venice) -- Held at the Bayerische Staatsbibliothek, Munich (Cod. icon. 242). Contains ~140 illustrations of siege engines, fountains, pumps, defensive towers, battering rams, a rocket-powered craft, the first known depiction of a magic lantern, scaling ladders, alchemical furnaces, clockwork, and robotic automata. Captions are partly in cipher.

2. **Secretum de thesauro experimentorum ymaginationis hominum** (Secret of the Treasure-Room of Experiments in Man's Imagination, c. 1430) -- Held at the Bibliotheque nationale de France (BNF NAL 635). Describes mnemonic machines and memory techniques, written in cipher. Contains the famous "mnemonic snake" diagram.

Both manuscripts use the **same cipher**, and the plaintext is **Latin**.

### How the Cipher Works

Fontana's cipher is a **mnemonic substitution cipher** -- designed to be easy to remember, not to be cryptographically strong.

**Vowels:** Each vowel is represented by a circle with directional tickmarks:
- Outer vowels (a, i, u) have tickmarks facing east/west
- Inner vowels (e, o) have tickmarks facing north/south

**Consonants use three strategies:**
- **Mirroring:** Letters b, d, p, q (morphologically similar in Latin script) are rendered as horizontally mirrored forms with extended strokes and directional tickmarks
- **Stroke-counting:** Letters h, k, m, n attach multiple strokes to circles, reflecting the stroke count in the actual letter
- **Loop/shape modification:** The letter s closes loops; t adds a crossbar to a looped shape

**Key characteristics:**
- The system is extremely regular and systematic
- It was designed to be **memorizable** rather than secure
- It is essentially a monoalphabetic substitution cipher (one cipher symbol per letter)
- However, some sources describe it as **homophonic** (multiple cipher symbols per letter), which would make it more sophisticated than simple substitution

The best scholarly edition is Battisti and Battisti's (1984) "Le Macchine Cifrate di Giovanni Fontana," which includes full Latin decipherments with modern Italian translations.

### Structural Comparison with the Voynich

| Feature | Fontana | Voynich |
|---------|---------|---------|
| Cipher type | Simple substitution (mnemonic) | Unknown (resists all decipherment attempts) |
| Regularity | Extremely regular, systematic design | Irregular; does not show single-designer regularity |
| Script basis | Circles + lines + tickmarks | Unique glyphs, some resembling shorthand |
| Plaintext | Latin | Unknown |
| Breakability | Trivially breakable (minutes) | Unbroken after 100+ years |
| Purpose of encoding | Mnemonic demonstration / professional showcase | Unknown |
| Illustration style | Shows superior 3D mechanical understanding | Muddled human joints, flat perspectives |

**Critical difference:** Fontana's cipher is regular enough that its design principles are immediately apparent. The Voynich script's irregularity suggests it is NOT a cipher designed by a single person using the same mnemonic principles. Voynich researchers have noted that if the Voynich were a simple cipher like Fontana's, it would have been broken long ago.

---

## 2. Fontana and the Voynich: Proposed Connections

### Evidence FOR a Connection

1. **Exact temporal overlap:** Fontana was active 1418-1455; Voynich vellum dates 1404-1438
2. **Same geographic origin:** Both associated with the Padua-Venice region of Northern Italy
3. **Both use cipher:** Both are encoded manuscripts from the same time and place
4. **Illustration similarities:** Some illustrations in Fontana's books "slightly resemble" Voynich illustrations -- both contain fantastical devices, water-related imagery, and bathing/fountain scenes
5. **Shared intellectual milieu:** Both emerge from the University of Padua's medical and natural philosophical tradition
6. **Interest in mnemonics:** Fontana's explicit interest in mnemonic systems may parallel a mnemonic design in the Voynich

### Evidence AGAINST Fontana as Author

1. **Different cipher systems:** Fontana's cipher is NOT the Voynich script. The two systems share no glyphs or structural principles
2. **Different complexity:** Fontana's is trivially breakable; the Voynich has resisted all cryptanalysis
3. **All Fontana's works are accounted for:** Fontana helpfully provided lists of his writings, and historians believe they have all been identified
4. **Different illustration quality:** Fontana shows better understanding of 3D mechanics than the Voynich artist
5. **Different content focus:** Fontana wrote about engineering and warfare; the Voynich focuses on botany, pharmacy, and cosmology

### Scholarly Consensus

Fontana is considered a **contextual parallel** rather than a candidate author. He demonstrates that cipher manuscripts were being produced in the exact time and place associated with the Voynich, and he establishes a plausible cultural milieu. But the Voynich is considerably more sophisticated (or at least more opaque) than anything Fontana produced.

The Voynich.ninja forum discussion raises an interesting point: the difference may reflect not different motivations but different **levels of cryptographic knowledge**. The Voynich author may have possessed "cutting edge knowledge of ciphers" compared to Fontana's amateur mnemonics.

---

## 3. Padua's Intellectual Milieu (1400-1450)

### The University of Padua

Founded in 1222, the University of Padua was one of Europe's premier centers for medicine, natural philosophy, and astronomy in the 15th century. Its medical school was structured in five chairs:
- Theoretical medicine
- Practical medicine
- Anatomy and surgery
- Botany
- Semeiotic (diagnosis/symptom interpretation)

### Key Figures at Padua (Voynich period)

**Giovanni Fontana** (arts 1418, medicine 1421): Physician, engineer, cipher-maker

**Nicholas of Cusa** (studied at Padua 1417-1423): The great German polymath overlapped with Fontana at Padua for several years. Nicholas studied mathematics, astronomy, and physics there, and became friends with the mathematician-astronomer **Paolo Toscanelli** (1397-1482). Nicholas later developed his own Lullian-influenced combinatorial method (*ars generalis coniecturandi*) with wheel charts resembling Llull's. There is no documented direct connection between Fontana and Nicholas, but their simultaneous presence at Padua (1417-1421) is remarkable.

**The Carrara Court:** Francesco II 'il Novello' da Carrara (r. 1390-1405) was the last prince of Padua before Venetian conquest in 1405. He commissioned the **Carrara Herbal** and cultivated an image as a "physician prince" who ensured the health of his city.

### The Carrara Herbal (BL Egerton MS 2020)

This extraordinary manuscript was commissioned in the late 14th century (under Carrara rule, before 1405) and represents the Paduan pharmaceutical tradition that the Voynich may also belong to.

**Key features:**
- Contains an illustrated, vernacular (Paduan dialect) translation of the pharmacopoeia of **Ibn Sarabi** (Serapion the Younger), a 13th-century Arabic pharmaceutical text
- Illustrations are **naturalistic and three-dimensional** -- showing true plant habits, not schematic diagrams
- Decorated with Carrara family heraldry
- Attests to the integration of Arabic medicine at Padua
- Written in Italian (not Latin), for practical use

**Connection to the Voynich:** The Carrara Herbal demonstrates that:
1. Padua had a tradition of producing illustrated pharmaceutical manuscripts
2. Arabic medical knowledge was being translated and adapted
3. Vernacular (non-Latin) language was used in practical medical texts
4. Naturalistic plant illustration was practiced in the region
5. The patron class valued pharmaceutical knowledge

However, the Carrara Herbal's plants are identifiable and its text is readable -- the opposite of the Voynich's mysterious plants and undeciphered text.

---

## 4. Ramon Llull's Influence in Italy

### Llull's Ars Magna and Combinatorial Method

Ramon Llull (1232-1316) designed a method of combining philosophical and religious attributes using rotating discs inscribed with letters and symbols. His **Ars Magna** (Great Art) was a combinatorial system that generated propositions by mechanically combining fundamental categories.

### 15th-Century Italian Reception

Llull's ideas were actively developed in 15th-century Italy:

1. **Giovanni Fontana** himself is cited as developing Llull's combinatorial ideas further
2. **Nicholas of Cusa** (at Padua 1417-1423) developed *ars generalis coniecturandi* with wheel charts closely resembling Llull's
3. **Giordano Bruno** (16th c.) later used Lullian rotating figures for artificial memory systems

### Pseudo-Lullian Alchemy

A massive corpus of **143 alchemical texts** circulated under Llull's name, none of which are actually by him. The most important is the **Testamentum** (dated c. 1332):

- Of 13 known manuscripts of the *Testamentum novissimum*, **all but one are in Italy**
- Manuscripts exist in **Padua** (Biblioteca Universitaria 2087) and **Milan** (Archivio di Sant'Ambrogio)
- The texts feature elaborate **alchemical diagrams** using combinatorial/geometric principles
- **Christophorus Parisiensis**, likely from Venice, was an enthusiastic follower of pseudo-Lullian alchemy in the second half of the 15th century

### Could the Voynich Be Pseudo-Lullian?

This is a speculative but intriguing hypothesis:

**Supporting evidence:**
- The Voynich's cosmological diagrams (rosettes, circular arrangements) superficially resemble Lullian combinatorial wheels
- The pharmaceutical section's organized structure could reflect a combinatorial approach to recipe construction
- Pseudo-Lullian manuscripts were concentrated in exactly the same region and period (Northern Italy, 15th century)
- The Lullian tradition explicitly valued **systematic notation** and **combinatorial generation** of knowledge
- The Voynich's "constructed" feel (its vocabulary seems rule-generated, not natural) aligns with combinatorial principles

**Weaknesses:**
- No known pseudo-Lullian text uses an invented script
- Pseudo-Lullian alchemical texts are in Latin with standard cipher elements, not constructed scripts
- The Voynich's botanical content is not typical of the pseudo-Lullian corpus (which focuses on transmutation, not pharmacy)

---

## 5. Venice-Padua Pharmaceutical Culture

### The Theriac Trade

Theriac (treacle) was the most complex and prestigious pharmaceutical product of the medieval and early modern world:

- **Theriac Andromachus** contained **55 components** requiring 40 days of preparation and **12 years of maturation**
- Ingredients included four vipers cooked in sal ammoniac with nine herbs and Attic wine, plus 50+ additional herbs
- Venice regulated theriac production from **1258** onward
- By the 15th century, Venice controlled theriac distribution throughout Europe
- Competing cities included Padua, Milan, Genoa, Bologna, Constantinople, and Cairo
- Production was **public** ("with much pomp and ceremony") to prevent fraud
- The College of Apothecaries of Venice maintained a **reference collection of recipes** for comparison

### Apothecary Notation Systems

Medieval pharmaceutical notation used:
- **Standard abbreviations:** Special symbols for ounce (looks like a flat-topped "3"), scruple (backwards "e"), dram (derived from yogh)
- **Latin abbreviations:** "ss" for *semis* (half), "Rx" for recipe (take)
- **Weight system:** The apothecaries' system used drachms as the primary unit
- **Scribal shorthand:** Medieval shorthand expanded from ~140 symbols to 14,000 by the Carolingian period

### Proprietary Encoding

**No direct evidence** has been found of proprietary cipher systems used by Venetian apothecary guilds. However:

- Apothecaries were expected to **adapt recipes** based on ingredient availability and guild custom -- suggesting some flexibility and local variation
- The **public manufacture** requirement for theriac implies that secrecy around high-value recipes was a recognized concern
- The **Nuovo Ricettario Fiorentino** (1499) was the first attempt to standardize pharmaceutical formulations across a city
- The fact that Venice maintained a reference collection of competitor cities' recipes suggests concern about recipe theft/verification

### The Question of Trade Secrets

While no cipher system has been documented for apothecary guilds specifically, the context is suggestive:
- Apothecaries occupied a position "between the more prestigious intellectual professions and the trades associated with commerce and craftsmanship"
- Recipe knowledge was a major competitive advantage
- Theriac could sell for enormous sums (Sir John Paston acquired "pots of Genoa treacle" in 1466 with certification they were unopened)
- The motivation to protect proprietary knowledge was strong, even if the methods are undocumented

---

## 6. The Voynich's Provenance and Italian Connection

### The Documented Chain

| Period | Owner | Notes |
|--------|-------|-------|
| 1404-1438 | Unknown creator | Vellum dates to this period |
| ? | Unknown | Gap of ~150 years |
| c. 1599 | **Rudolf II** of Habsburg | Purchased for 600 ducats/Rheinische Gulden |
| After 1608 | **Jacobus Horcicky de Tepenec** | Rudolf's court pharmacist and botanist; signature on f1r (UV-visible) |
| Before 1646 | **Georg Baresch** | Prague alchemist; called it "uselessly taking up space" |
| c. 1646-1665 | **Johannes Marcus Marci** | Rector of Charles University, Prague |
| 1665+ | **Athanasius Kircher** | Jesuit polymath in Rome |
| 1866-1912 | Jesuit Collegium Romanum | In the library |
| 1912 | **Wilfrid Voynich** | Purchased from Jesuits |
| 1969+ | **Yale University** (Beinecke Library) | Donated by H.P. Kraus |

### The Rudolf II Purchase

The crucial link is Karl Widemann, an Augsburg doctor and collector of Paracelsus manuscripts, who sold a collection of manuscripts to Rudolf in 1599 for 500 silver thaler (recorded elsewhere as 600 gold florin). Widemann's house had previously belonged to **Leonhard Rauwolf**, a botanist-physician who traveled the Orient collecting herbs -- a tantalizing but unproven connection.

### The John Dee Hypothesis (Debunked)

Wilfrid Voynich proposed in 1921 that John Dee brought the manuscript to Prague and sold it to Rudolf II. This has been **thoroughly discredited**:
- Researcher Rafal Prinke demonstrated "none of it can be substantiated"
- Dee's meticulous diaries do not mention such a sale
- The manuscript is now believed to have reached Prague through Widemann, not Dee

### Italian Connection: The Evidence

**Physical evidence for Northern Italian origin:**
1. **Radiocarbon dating:** Vellum from 1404-1438
2. **Swallowtail (Ghibelline) crenellations:** The castle drawing uses architectural features "found predominantly in what is now Northern Italy," closely associated with the Scaliger family near Verona
3. **Alchemical herbal tradition:** The Voynich's plant images resemble ~70 known alchemical herbals, of which **all but two were made in the Veneto area** (the Padua-Venice region)
4. **Script characteristics:** Sergio Toresella identified "a North Italian humanistic hand" in the script
5. **Cipher resemblances:** Voynichese symbols resemble those used in "north Italian ciphers, shorthand, and astrological symbols"

**Toresella's Assessment:** The Voynich comes from "Northern Italy, around 1460" (though the vellum dating suggests the actual text may be slightly earlier).

**Mixed Alpine Character:** The manuscript shows both Italian and German influences:
- Color annotations suggest the scribe's mother language was German
- Zodiac cycle shows similarities to German manuscripts (1400-1500)
- The overall character is described as "Alpine" -- the border zone between Italy and the German-speaking world, which includes the Veneto, Trentino, and Friuli regions

### The Jacobus Horcicky Connection

Jacobus Horcicky de Tepenec (1575-1622), Rudolf II's court **pharmacist and botanist**, is the first positively identified owner after Rudolf. This is significant because:
- He was a pharmaceutical specialist -- exactly the kind of person who would find a pharmaceutical manuscript valuable
- His signature on f1r confirms he possessed it
- He was also Rudolf's **Imperial Distiller** and curator of his botanical gardens
- Lisa Fagin Davis's UV/IR analysis solidified the manuscript's passage through his hands

The fact that a court pharmacist owned the manuscript strengthens the hypothesis that its content is pharmaceutical.

---

## 7. Synthesis: The Padua-Venice Pharmaceutical Hypothesis

### What the Evidence Suggests

The convergence of evidence points strongly to the Padua-Venice region:

1. **The vellum** dates to 1404-1438
2. **The architectural details** point to Northern Italy (Verona/Scaliger region)
3. **The herbal tradition** matches the Veneto's unique alchemical herbal corpus
4. **The script** is identified as North Italian humanistic
5. **The cipher tradition** matches 15th-century North Italian practices (Fontana being the prime example)
6. **The pharmaceutical content** aligns with Padua's status as Europe's premier medical university
7. **The pseudo-Lullian tradition** was concentrated in Italy, with manuscripts in Padua itself
8. **The Carrara Herbal** demonstrates Padua's tradition of illustrated pharmaceutical manuscripts
9. **The first named owner** (Horcicky) was a court pharmacist and botanist
10. **The theriac trade** demonstrates Venice's intense pharmaceutical commerce and recipe competition

### Fontana's Role as Context

Giovanni Fontana is not the Voynich's author, but he is invaluable as a **contextual witness**:
- He proves that cipher manuscripts were being produced at Padua in exactly this period
- He shows that medical graduates had interests in both cryptography and mnemonics
- He demonstrates that the intellectual milieu supported the combination of pharmaceutical knowledge, cipher use, and mnemonic design
- His relatively simple cipher establishes a **baseline** -- the Voynich goes far beyond anything Fontana attempted

### The Naibbe Cipher (2025 Research)

A 2025 study by Greshko proposed the "Naibbe cipher" -- a verbose homophonic substitution cipher using dice throws and playing card draws to determine encryption tables. When applied to Latin or Italian plaintext, it produces ciphertexts with statistical properties matching the Voynich. Key points:
- Named after a medieval Italian card game
- Uses only materials available in 15th-century Europe
- Breaks text into single/double letter groups before substitution
- Introduces randomness via dice (breaking) and cards (table selection)
- **Proof of concept**, not a claimed solution
- Demonstrates that the Voynich's statistics are compatible with a 15th-century Italian cipher system

### Open Questions

1. **How did the manuscript get from Northern Italy to Prague?** The Widemann/Rauwolf connection is suggestive but unproven. The ~150-year gap (1438-1599) remains dark.

2. **Was there a tradition of constructed pharmaceutical notation?** No direct evidence exists, but the combination of (a) secret recipe competition, (b) established cipher use at Padua, and (c) Lullian combinatorial methods creates a plausible context.

3. **What was the purpose of the encoding?** Possibilities include:
   - Trade secret protection (apothecary competition)
   - Professional demonstration (like Fontana's cipher-as-portfolio)
   - Mnemonic system (personal notation for pharmaceutical knowledge)
   - Combinatorial generation (Lullian-inspired recipe construction)
   - Some combination of the above

4. **Who was the author?** The profile that emerges is:
   - Educated at or near the University of Padua
   - Trained in medicine/pharmacy and familiar with Arabic pharmaceutical tradition
   - Knowledgeable about cryptographic methods beyond simple substitution
   - Possibly influenced by Lullian combinatorial thinking
   - Working in or near the Veneto between 1404 and ~1440
   - Possibly bilingual (Italian/German), suggesting the Alpine borderland

---

## Sources

### Giovanni Fontana and Cipher
- [Fontana's Cipher Design -- Voynich Portal](https://voynichportal.com/2020/07/20/fontanas-cipher-design/)
- [Fontana Cipher Manuscripts -- Philip Neal / Voynich Sources](http://philipneal.net/voynichsources/fontana_cipher_manuscripts/)
- [Review of "Le Macchine Cifrate di Giovanni Fontana" -- Cipher Mysteries](https://ciphermysteries.com/2008/12/06/review-of-le-macchine-cifrate-di-giovanni-fontana)
- [Why did Giovanni Fontana write his book in cipher? -- Voynich Ninja](https://www.voynich.ninja/thread-3439.html)
- [Giovanni Fontana (engineer) -- Wikipedia](https://en.wikipedia.org/wiki/Giovanni_Fontana_(engineer))
- [Giovanni Fontana -- History-Computer](https://history-computer.com/people/giovanni-fontana-biography-history-and-inventions/)

### Carrara Herbal and Padua
- [Medicine and Humanism in Late Medieval Italy: The Carrara Herbal in Padua -- Routledge](https://www.routledge.com/Medicine-and-Humanism-in-Late-Medieval-Italy-The-Carrara-Herbal-in-Padua/Kyle/p/book/9780367879846)
- [The Carrara Herbal -- Blog](https://carraraherbal.home.blog/)
- [Origin and development of modern medicine at Padua -- PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3963738/)

### Ramon Llull and Pseudo-Lullian Alchemy
- [Charissime Fili: Pseudo-Lullian Diagrams -- Academia.edu](https://www.academia.edu/43084422/Charissime_Fili_The_Transmission_of_Alchemical_Science_from_the_Manuscript_to_the_Press_the_Pseudo_Lullian_Diagrams)
- [Pseudo-Lull Theorica Testamentum -- TextManuscripts](https://www.textmanuscripts.com/medieval/lull-theorica-testamentum-61038)
- [Ramon Llull -- Britannica](https://www.britannica.com/biography/Ramon-Llull)

### Venice-Padua Pharmaceutical Culture
- [Venetian Treacle and Medicines Regulation -- PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1884566/)
- [Apothecary in 15th Century Italy -- Enionline](https://www.enionline.it/en/apothecary-15th-century-italy/)
- [Apothecaries' Symbols in Medical Recipes](https://www.textpartnership.net/docs/dox/medical.html)

### Voynich Provenance and Origin
- [Voynich MS History -- voynich.nu](https://www.voynich.nu/history.html)
- [Voynich MS Origin -- voynich.nu](https://voynich.nu/origin.html)
- [What if Sergio Toresella was right all along -- Cipher Mysteries](https://ciphermysteries.com/2019/06/18/what-if-sergio-toresella-was-sort-of-right-all-along)
- [Voynich Manuscript -- Wikipedia](https://en.wikipedia.org/wiki/Voynich_manuscript)
- [Jacobus Sinapius -- Wikipedia](https://en.wikipedia.org/wiki/Jacobus_Sinapius)

### Naibbe Cipher (2025)
- [The Naibbe Cipher -- Cryptologia / Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/01611194.2025.2566408)
- [Voynich Manuscript may be a cipher -- Archaeology Magazine](https://archaeologymag.com/2026/01/voynich-manuscript-may-be-a-cipher/)
- [Cards and Dice May Be Key -- Newsweek](https://www.newsweek.com/voynich-manuscript-15th-century-book-cards-dice-cipher-naibbe-11316017)
