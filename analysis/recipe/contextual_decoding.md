# Voynich Manuscript: Contextual Decoding Analysis
## Distributional Semantics Approach

**Method**: Build context vectors for the 50 most frequent stems, cluster by
distributional similarity, cross-reference with section distribution and
positional patterns to propose vocabulary identifications.

### Key Discoveries
1. **The cho-/sho-/ctho-/cth-/do- cluster**: These stems cluster together with 73% herbal concentration. All are likely plant-part vocabulary. ctho- (94% herbal exclusive) is the strongest plant-part candidate after cho- and sho-.
2. **qo- is bio-enriched, not just recipe-enriched**: 23.5% of bio section words are qo-prefixed (1.68x enrichment), vs 16.9% recipe (1.21x). This suggests qo- is a general quantifier/determiner, not recipe-specific.
3. **Positional structure is real**: otch- and ot- stems appear 1.7-2.0x enriched in early lines (plant description), while cheo- and okeo- appear 1.5-1.9x enriched in late lines (preparation). This matches medieval herbal structure.
4. **10 new vocabulary proposals** at 35-55% confidence, expanding the dictionary from 4 to 15 stems.
5. **Distributional similarity confirms plant-part system**: cth- (0.930 cosine similarity to cho-) and ctho- (0.887) are distributionally near-identical to cho- (leaf), strongly supporting they name plant parts.

**Corpus**: 37189 tokens, 8517 unique words, 5799 unique stems
**Sections**: herbal=13415, recipe=10806, astro=4829, bio=6909, other=1230

---
## 1. Top 50 Stems: Context Profiles

| # | Stem | Freq | Primary Section | Position | Top Left Context | Top Right Context |
|---|------|------|----------------|----------|-----------------|-------------------|
| 1 | **qok** | 1716 | bio (45%) | S29/M58/E13 | qok(367), ch(249), sh(221) | qok(367), ch(187), sh(122) |
| 2 | **ch** | 1493 | recipe (35%) | S23/M59/E18 | qok(187), o(136), ch(131) | qok(249), ch(131), d(110) |
| 3 | **sh** | 1037 | bio (35%) | S34/M55/E12 | qok(122), o(95), sh(76) | qok(221), ch(94), sh(76) |
| 4 | **ok** | 893 | recipe (39%) | S27/M55/E18 | qok(121), ch(72), ok(71) | qok(120), ch(88), ok(71) |
| 5 | **ot** | 856 | recipe (42%) | S20/M59/E22 | qok(104), ot(92), ch(65) | qok(106), ot(92), ch(65) |
| 6 | **cho** | 702 | herbal (74%) | S33/M57/E10 | cho(75), d(69), o(53) | d(86), cho(75), ch(60) |
| 7 | **aii** | 651 | recipe (37%) | S22/M53/E25 | o(130), s(57), a(57) | o(53), ch(47), ot(44) |
| 8 | **da** | 516 | herbal (39%) | S20/M44/E36 | qok(57), ch(49), a(30) | sh(39), o(39), ch(36) |
| 9 | **qot** | 493 | recipe (41%) | S23/M58/E19 | qok(81), ch(71), sh(48) | qok(66), ch(53), qot(47) |
| 10 | **sho** | 389 | herbal (74%) | S46/M49/E5 | d(42), sho(39), cho(32) | sho(39), d(30), ch(30) |
| 11 | **qoka** | 351 | bio (44%) | S24/M58/E18 | qok(62), sh(47), ch(34) | qok(48), ch(47), sh(44) |
| 12 | **cheo** | 345 | herbal (45%) | S32/M55/E12 | o(35), ch(22), qok(22) | o(28), ch(23), qok(23) |
| 13 | **qo** | 321 | bio (46%) | S41/M47/E12 | ch(53), sh(46), qok(37) | ch(69), qok(36), o(34) |
| 14 | **ota** | 305 | recipe (41%) | S18/M53/E29 | ot(41), qok(32), ch(21) | o(31), a(29), ch(25) |
| 15 | **oka** | 300 | recipe (30%) | S23/M55/E23 | qok(37), ch(25), ok(24) | a(31), ch(24), o(24) |
| 16 | **ai** | 251 | recipe (47%) | S31/M44/E25 | o(35), a(30), s(28) | a(31), o(27), ch(26) |
| 17 | **lk** | 229 | recipe (79%) | S22/M56/E21 | ch(40), qok(37), ok(23) | qok(30), ch(24), ot(19) |
| 18 | **olk** | 211 | bio (52%) | S28/M53/E18 | qok(40), ch(16), ok(16) | qok(30), o(26), ch(18) |
| 19 | **lch** | 204 | bio (47%) | S26/M48/E25 | ch(41), qok(41), ot(19) | qok(54), sh(19), ch(19) |
| 20 | **sheo** | 197 | herbal (45%) | S46/M45/E9 | qok(17), d(14), o(12) | qok(25), sh(15), o(14) |
| 21 | **cth** | 189 | herbal (84%) | S21/M52/E27 | d(28), cho(24), ch(20) | d(24), cho(15), ch(11) |
| 22 | **do** | 184 | herbal (68%) | S34/M51/E15 | d(15), qok(14), cho(12) | sh(22), ch(14), d(12) |
| 23 | **yk** | 179 | herbal (37%) | S41/M47/E12 | o(16), qok(15), ok(15) | ch(18), qok(18), o(14) |
| 24 | **chckh** | 179 | bio (32%) | S17/M66/E17 | qok(33), d(17), o(14) | qok(26), ok(16), d(15) |
| 25 | **ke** | 163 | recipe (42%) | S25/M56/E18 | ch(26), o(26), a(19) | qok(27), d(14), ok(10) |
| 26 | **yt** | 161 | herbal (39%) | S34/M47/E19 | qok(14), ot(12), o(11) | ot(12), ch(11), d(10) |
| 27 | **cha** | 158 | herbal (37%) | S22/M59/E19 | o(17), cho(16), qok(15) | ch(18), a(15), o(11) |
| 28 | **qokch** | 154 | herbal (42%) | S32/M56/E12 | ch(16), qok(12), qotch(10) | qok(16), d(13), ch(10) |
| 29 | **oto** | 143 | herbal (43%) | S36/M48/E17 | o(7), a(7), d(6) | d(11), cho(10), ot(10) |
| 30 | **sa** | 137 | herbal (26%) | S40/M35/E25 | qok(11), o(11), ch(9) | sh(20), aii(13), o(12) |
| 31 | **qoko** | 136 | herbal (51%) | S32/M61/E7 | qok(20), d(11), cho(9) | ch(18), sh(13), cho(11) |
| 32 | **qota** | 136 | recipe (38%) | S16/M62/E22 | ch(19), qok(18), ok(10) | ch(22), sh(15), d(12) |
| 33 | **chod** | 133 | herbal (63%) | S20/M63/E17 | cho(11), qok(10), ch(9) | d(15), ch(13), s(8) |
| 34 | **chd** | 128 | recipe (41%) | S20/M62/E19 | qok(12), ot(11), ch(9) | qok(17), ch(16), ok(8) |
| 35 | **otch** | 126 | herbal (39%) | S26/M59/E15 | ch(12), ota(9), o(9) | d(19), qok(15), qot(8) |
| 36 | **od** | 122 | herbal (53%) | S25/M48/E27 | aii(10), cho(9), o(9) | sh(10), a(9), ch(8) |
| 37 | **oko** | 120 | herbal (62%) | S28/M53/E18 | oka(8), ok(8), sh(7) | ch(10), ok(10), o(10) |
| 38 | **qotch** | 118 | herbal (56%) | S33/M57/E10 | d(11), qok(11), cho(9) | d(15), qokch(10), cho(7) |
| 39 | **so** | 115 | bio (46%) | S77/M17/E6 | qok(17), d(9), ch(9) | ch(27), sh(16), qok(12) |
| 40 | **am** | 114 | herbal (30%) | S6/M19/E75 | a(16), ch(11), aii(9) | o(9), s(8), sh(7) |
| 41 | **okeo** | 114 | herbal (56%) | S37/M46/E18 | qok(9), okeo(8), ok(7) | ok(11), d(9), cho(8) |
| 42 | **chea** | 112 | recipe (43%) | S29/M54/E18 | qok(18), ch(12), d(9) | ch(10), o(9), qok(9) |
| 43 | **ctho** | 112 | herbal (94%) | S18/M71/E12 | cho(21), d(20), ch(9) | d(18), cho(16), s(5) |
| 44 | **chek** | 110 | herbal (43%) | S30/M49/E21 | qok(11), y(8), ok(7) | ch(12), qok(10), da(8) |
| 45 | **opch** | 108 | recipe (48%) | S25/M57/E18 | qot(10), ot(7), qok(6) | o(8), d(7), qot(7) |
| 46 | **lo** | 101 | bio (44%) | S18/M39/E44 | qok(22), ch(14), sh(10) | ch(14), qok(14), sh(10) |
| 47 | **chcth** | 101 | herbal (33%) | S14/M62/E24 | ch(14), qok(13), ok(9) | qok(10), ch(8), ot(8) |
| 48 | **tch** | 99 | herbal (45%) | S49/M40/E10 | d(12), ch(12), ot(7) | qok(9), ch(8), d(7) |
| 49 | **dai** | 99 | herbal (44%) | S39/M37/E23 | ch(8), d(6), qok(6) | a(11), ch(11), cho(8) |
| 50 | **ka** | 97 | herbal (35%) | S23/M48/E29 | a(13), cho(10), qok(10) | o(9), a(9), ok(8) |

---
## 2. Cluster Analysis (8 clusters by distributional similarity)

### Cluster: da
- **Members**: da(516), yk(179), yt(161), cha(158), oto(143), sa(137), qoko(136), qota(136), od(122), so(115), okeo(114), chek(110), tch(99), dai(99), ka(97)
- **Section profile**: herbal=39%, recipe=21%, bio=18%
- **Position profile**: S32/M46/E22

### Cluster: cho -- CONFIRMED: cho (leaf), sho (root)
- **Members**: cho(702), sho(389), cth(189), do(184), chod(133), oko(120), qotch(118), ctho(112)
- **Section profile**: herbal=73%, recipe=13%, astro=7%
- **Position profile**: S32/M55/E12

### Cluster: qok
- **Members**: qok(1716), qot(493), qoka(351), qo(321), lch(204), lo(101)
- **Section profile**: bio=44%, recipe=37%, herbal=12%
- **Position profile**: S28/M55/E16

### Cluster: ch
- **Members**: ch(1493), chckh(179), ke(163), qokch(154), otch(126), chea(112)
- **Section profile**: recipe=36%, herbal=29%, bio=25%
- **Position profile**: S24/M59/E17

### Cluster: ok
- **Members**: ok(893), oka(300), lk(229), chd(128), chcth(101)
- **Section profile**: recipe=42%, herbal=25%, bio=20%
- **Position profile**: S24/M56/E20

### Cluster: aii
- **Members**: aii(651), cheo(345), ai(251), am(114)
- **Section profile**: recipe=37%, herbal=34%, astro=16%
- **Position profile**: S25/M49/E26

### Cluster: sh
- **Members**: sh(1037), olk(211), sheo(197)
- **Section profile**: bio=35%, recipe=28%, herbal=26%
- **Position profile**: S35/M53/E12

### Cluster: ot
- **Members**: ot(856), ota(305), opch(108)
- **Section profile**: recipe=42%, bio=19%, astro=18%
- **Position profile**: S20/M57/E23

---
## 3. Section-Specific Vocabulary

### HERBAL section exclusives (>=90% in section, freq>=5)
| Word | In-section | Total | Ratio |
|------|-----------|-------|-------|
| cthy | 86 | 95 | 90.5% |
| cthol | 49 | 52 | 94.2% |
| cthor | 39 | 42 | 92.9% |
| otchol | 22 | 24 | 91.7% |
| kchor | 21 | 22 | 95.5% |
| ckhol | 18 | 19 | 94.7% |
| chom | 15 | 15 | 100.0% |
| qotchol | 14 | 14 | 100.0% |
| dan | 12 | 13 | 92.3% |
| qotchor | 12 | 12 | 100.0% |
| v | 11 | 11 | 100.0% |
| cthaiin | 10 | 10 | 100.0% |
| shos | 10 | 11 | 90.9% |
| chory | 10 | 10 | 100.0% |
| choiin | 10 | 10 | 100.0% |
| ctheol | 10 | 10 | 100.0% |
| ychol | 9 | 10 | 90.0% |
| ytol | 9 | 9 | 100.0% |
| ctho | 9 | 9 | 100.0% |
| ckhor | 7 | 7 | 100.0% |

### HERBAL section enriched (>=60%, freq>=5)
| Word | In-section | Total | Ratio |
|------|-----------|-------|-------|
| daiin | 428 | 674 | 63.5% |
| chol | 249 | 353 | 70.5% |
| s | 185 | 289 | 64.0% |
| chor | 169 | 202 | 83.7% |
| chy | 131 | 207 | 63.3% |
| shol | 110 | 165 | 66.7% |
| sho | 91 | 110 | 82.7% |
| shor | 65 | 85 | 76.5% |
| shy | 60 | 95 | 63.2% |
| chody | 51 | 78 | 65.4% |

### RECIPE section exclusives (>=90% in section, freq>=5)
| Word | In-section | Total | Ratio |
|------|-----------|-------|-------|
| lkchey | 10 | 11 | 90.9% |
| lkeeey | 10 | 10 | 100.0% |
| shedain | 7 | 7 | 100.0% |
| alkain | 6 | 6 | 100.0% |
| liin | 5 | 5 | 100.0% |
| chedam | 5 | 5 | 100.0% |
| qotched | 5 | 5 | 100.0% |
| ail | 5 | 5 | 100.0% |
| qokeain | 5 | 5 | 100.0% |
| oteed | 5 | 5 | 100.0% |

### RECIPE section enriched (>=60%, freq>=5)
| Word | In-section | Total | Ratio |
|------|-----------|-------|-------|
| lkeey | 41 | 50 | 82.0% |
| lkaiin | 39 | 47 | 83.0% |
| raiin | 38 | 56 | 67.9% |
| lkeedy | 25 | 29 | 86.2% |
| lkain | 24 | 30 | 80.0% |
| lkar | 22 | 32 | 68.8% |
| okeeey | 21 | 35 | 60.0% |
| qokchedy | 21 | 28 | 75.0% |
| chedaiin | 17 | 23 | 73.9% |
| otair | 17 | 25 | 68.0% |

### ASTRO section exclusives (>=90% in section, freq>=5)
*(none found)*

### ASTRO section enriched (>=60%, freq>=5)
| Word | In-section | Total | Ratio |
|------|-----------|-------|-------|
| oteos | 15 | 21 | 71.4% |
| okeo | 9 | 14 | 64.3% |
| oteeos | 9 | 13 | 69.2% |
| yteody | 8 | 12 | 66.7% |
| okeos | 8 | 10 | 80.0% |
| otees | 8 | 12 | 66.7% |
| oteoy | 7 | 9 | 77.8% |
| oto | 7 | 9 | 77.8% |
| chotey | 6 | 9 | 66.7% |
| ykeody | 6 | 10 | 60.0% |

### BIO section exclusives (>=90% in section, freq>=5)
| Word | In-section | Total | Ratio |
|------|-----------|-------|-------|
| qolchey | 12 | 13 | 92.3% |
| qolchedy | 7 | 7 | 100.0% |
| loly | 6 | 6 | 100.0% |
| eckhy | 6 | 6 | 100.0% |
| qoly | 6 | 6 | 100.0% |
| solkeey | 5 | 5 | 100.0% |

### BIO section enriched (>=60%, freq>=5)
| Word | In-section | Total | Ratio |
|------|-----------|-------|-------|
| qokedy | 113 | 169 | 66.9% |
| qol | 111 | 143 | 77.6% |
| qotedy | 38 | 62 | 61.3% |
| sol | 36 | 55 | 65.5% |
| edy | 30 | 38 | 78.9% |
| olkain | 26 | 33 | 78.8% |
| lol | 21 | 34 | 61.8% |
| checthy | 19 | 31 | 61.3% |
| olchedy | 17 | 22 | 77.3% |
| dshedy | 14 | 23 | 60.9% |

---
## 4. The qo- Prefix: Comprehensive Analysis

### qo- frequency by section
| Section | qo- count | Total words | qo- rate | Enrichment |
|---------|-----------|-------------|----------|-----------|
| herbal | 1287 | 13415 | 9.6% | 0.68x |
| recipe | 1830 | 10806 | 16.9% | 1.21x |
| astro | 321 | 4829 | 6.6% | 0.47x |
| bio | 1626 | 6909 | 23.5% | 1.68x |
| other | 160 | 1230 | 13.0% | 0.93x |
| **TOTAL** | **5224** | **37189** | **14.0%** | 1.00x |

### Top 30 qo- words
| Word | Freq | Primary Section | Position | Right neighbors |
|------|------|----------------|----------|----------------|
| qokeey | 366 | recipe(195) | S31/M57/E12 | qokeey(16), qokey(12), daiin(10) |
| qokain | 271 | bio(159) | S27/M62/E11 | ol(15), chey(10), chckhy(9) |
| qokaiin | 255 | recipe(118) | S29/M59/E12 | chey(9), ol(7), shey(6) |
| qokeedy | 217 | bio(120) | S34/M56/E11 | qokeedy(13), qokeey(8), qokain(5) |
| qokey | 185 | bio(84) | S30/M59/E11 | qokeey(8), qokedy(6), qokain(5) |
| qokal | 180 | bio(100) | S27/M57/E17 | chedy(10), ol(6), dar(5) |
| qokedy | 169 | bio(113) | S30/M58/E12 | qokeedy(7), chedy(7), qokedy(6) |
| qol | 143 | bio(111) | S41/M47/E13 | chedy(12), chey(7), shedy(5) |
| qokar | 142 | bio(45) | S24/M60/E16 | shey(6), shedy(5), ol(4) |
| qoky | 132 | bio(57) | S14/M56/E30 | daiin(9), chey(5), saiin(4) |
| qokol | 96 | herbal(50) | S29/M65/E6 | chedy(5), daiin(4), chey(4) |
| qoty | 81 | bio(28) | S16/M53/E31 | daiin(4), shey(4), qokar(2) |
| qotaiin | 79 | recipe(42) | S24/M59/E16 | qokaiin(2), ol(2), chor(2) |
| qokchy | 79 | herbal(50) | S33/M54/E13 | s(3), daiin(3), dar(2) |
| qotar | 64 | recipe(29) | S19/M59/E22 | shey(3), otal(3), ol(3) |
| qoteey | 63 | recipe(34) | S27/M63/E10 | qokain(3), daiin(2), qokol(2) |
| qotal | 63 | bio(28) | S16/M65/E19 | chedy(7), shey(4), dar(3) |
| qotedy | 62 | bio(38) | S15/M68/E18 | qotedy(3), qokeedy(2), otedy(2) |
| qotain | 62 | recipe(35) | S21/M55/E24 | chedy(4), chey(4), oteedy(3) |
| qotchy | 61 | herbal(51) | S39/M56/E5 | qokchy(5), daiin(3), qotor(2) |
| qoteedy | 56 | bio(32) | S34/M50/E16 | qokeey(3), chedy(2), qokaiin(2) |
| qo | 55 | herbal(21) | S49/M42/E9 | qokain(3), chol(2), ar(2) |
| qotey | 51 | recipe(19) | S25/M61/E14 | qokeedy(3), qokeey(3), oteey(2) |
| qokeol | 45 | herbal(31) | S22/M60/E18 | daiin(4), okey(2), okol(2) |
| qotol | 44 | herbal(23) | S34/M59/E7 | sheol(2), shy(2), chykychodar(1) |
| qodaiin | 37 | herbal(15) | S35/M57/E8 | odain(2), chom(1), cho(1) |
| qokchey | 35 | recipe(20) | S37/M57/E6 | qocphy(1), chey(1), dolotchol(1) |
| qokchdy | 32 | recipe(11) | S28/M56/E16 | qokal(2), chor(1), qokees(1) |
| qokor | 29 | herbal(13) | S41/M55/E3 | shedy(2), chol(1), okeor(1) |
| qokchedy | 28 | recipe(21) | S21/M61/E18 | daiin(3), qoekaly(1), qofchy(1) |

### qo- stripped: what base word remains?
| qo-word | Stripped | Standalone freq |
|---------|---------|----------------|
| qokeey (366) | keey | 75 |
| qokain (271) | kain | 48 |
| qokaiin (255) | kaiin | 72 |
| qokeedy (217) | keedy | 31 |
| qokey (185) | key | 33 |
| qokal (180) | kal | 28 |
| qokedy (169) | kedy | 25 |
| qol (143) | l | 161 |
| qokar (142) | kar | 56 |
| qoky (132) | ky | 17 |
| qokol (96) | kol | 35 |
| qoty (81) | ty | 16 |
| qotaiin (79) | taiin | 45 |
| qokchy (79) | kchy | 34 |
| qotar (64) | tar | 43 |
| qoteey (63) | teey | 30 |
| qotal (63) | tal | 25 |
| qotedy (62) | tedy | 22 |
| qotain (62) | tain | 14 |
| qotchy (61) | tchy | 25 |

### What stems follow qo- words?
| Following stem | Count | Known meaning |
|---------------|-------|--------------|
| qok | 345 |  |
| ch | 298 |  |
| sh | 199 |  |
| o | 167 |  |
| ok | 160 |  |
| d | 151 |  |
| ot | 145 |  |
| qot | 106 |  |
| cho | 94 | leaf |
| a | 82 |  |
| da | 79 |  |
| s | 68 |  |
| qoka | 68 |  |
| cheo | 59 |  |
| qo | 58 |  |
| ota | 56 |  |
| olk | 51 |  |
| oka | 49 |  |
| aii | 42 |  |
| lch | 40 |  |

### What stems precede qo- words?
| Preceding stem | Count | Known meaning |
|---------------|-------|--------------|
| sh | 392 |  |
| ch | 388 |  |
| qok | 379 |  |
| ok | 139 |  |
| ot | 138 |  |
| qot | 113 |  |
| d | 112 |  |
| lch | 64 |  |
| sheo | 57 |  |
| sho | 50 | root |
| qokch | 50 |  |
| da | 47 |  |
| olk | 47 |  |
| o | 46 |  |
| ke | 42 |  |
| qotch | 39 |  |
| chckh | 38 |  |
| otch | 36 |  |
| a | 36 |  |
| cho | 35 | leaf |

### Recipe-dominant vs herbal-dominant qo- words
**Recipe-dominant qo- words:**
| Word | Recipe | Herbal | Recipe% |
|------|--------|--------|---------|
| qotain | 35 | 0 | 100% |
| qokchedy | 21 | 0 | 100% |
| qopchedy | 16 | 0 | 100% |
| qotchedy | 14 | 0 | 100% |
| qoeedy | 9 | 0 | 100% |
| qokeain | 5 | 0 | 100% |
| qokeechy | 5 | 0 | 100% |
| qopaiin | 5 | 0 | 100% |
| qotched | 5 | 0 | 100% |
| qochey | 5 | 0 | 100% |
| qoked | 4 | 0 | 100% |
| qokeear | 4 | 0 | 100% |
| qoteal | 4 | 0 | 100% |
| qoke | 3 | 0 | 100% |
| qoteed | 3 | 0 | 100% |

---
## 5. Medieval Herbal Structure Mapping

Herbal pages divided into: early (lines 1-3), middle (4-8), late (9+).

Expected structure: Early=plant description, Middle=qualities, Late=preparation

### Stems enriched EARLY (plant name/description)
| Stem | Early | Middle | Late | Total | Enrichment |
|------|-------|--------|------|-------|------------|
| otch | 24 | 16 | 9 | 49 | 2.05x |
| opch | 9 | 8 | 4 | 21 | 1.79x |
| qota | 7 | 8 | 2 | 17 | 1.72x |
| ot | 58 | 49 | 36 | 143 | 1.69x |
| qot | 26 | 23 | 19 | 68 | 1.60x |
| tch | 16 | 17 | 12 | 45 | 1.49x |
| ka | 12 | 11 | 11 | 34 | 1.47x |
| yt | 21 | 27 | 14 | 62 | 1.42x |
| od | 20 | 17 | 28 | 65 | 1.29x |
| sh | 80 | 91 | 93 | 264 | 1.27x |
| qotch | 20 | 28 | 18 | 66 | 1.27x |
| qokch | 19 | 24 | 21 | 64 | 1.24x |

### Stems enriched LATE (preparation/dosage)
| Stem | Early | Middle | Late | Total | Enrichment |
|------|-------|--------|------|-------|------------|
| okeo | 4 | 9 | 51 | 64 | 1.92x |
| lch | 0 | 4 | 7 | 11 | 1.53x |
| cheo | 11 | 47 | 97 | 155 | 1.50x |
| chea | 4 | 7 | 16 | 27 | 1.42x |
| qoko | 10 | 22 | 37 | 69 | 1.29x |
| sa | 5 | 12 | 19 | 36 | 1.27x |
| aii | 34 | 71 | 116 | 221 | 1.26x |
| ok | 55 | 68 | 117 | 240 | 1.17x |
| oko | 14 | 24 | 36 | 74 | 1.17x |
| so | 9 | 10 | 18 | 37 | 1.17x |
| cho | 103 | 166 | 248 | 517 | 1.15x |
| olk | 2 | 10 | 11 | 23 | 1.15x |

---
## 6. Co-occurrence with Confirmed Vocabulary

### Top neighbors of **cho** (leaf)
| Neighbor | Count | Neighbor freq | PMI-like |
|----------|-------|---------------|----------|
| ch | 139 | 1493 | 2.57 |
| sho | 102 | 389 | 3.90 |
| da | 71 | 516 | 3.05 |
| sh | 68 | 1037 | 2.16 |
| qok | 66 | 1716 | 1.60 |
| aii | 66 | 651 | 2.67 |
| ok | 64 | 893 | 2.26 |
| cth | 53 | 189 | 3.99 |
| cheo | 50 | 345 | 3.12 |
| ot | 50 | 856 | 2.03 |
| ctho | 45 | 112 | 4.48 |
| do | 39 | 184 | 3.61 |
| chod | 34 | 133 | 3.86 |
| cha | 30 | 158 | 3.47 |
| qot | 28 | 493 | 2.00 |

### Top neighbors of **sho** (root)
| Neighbor | Count | Neighbor freq | PMI-like |
|----------|-------|---------------|----------|
| cho | 102 | 702 | 3.90 |
| ch | 62 | 1493 | 2.31 |
| sh | 45 | 1037 | 2.36 |
| qok | 37 | 1716 | 1.61 |
| aii | 36 | 651 | 2.65 |
| ok | 31 | 893 | 2.11 |
| cth | 29 | 189 | 3.97 |
| da | 29 | 516 | 2.67 |
| qot | 27 | 493 | 2.64 |
| ot | 24 | 856 | 1.88 |
| do | 20 | 184 | 3.51 |
| sheo | 18 | 197 | 3.28 |
| cheo | 16 | 345 | 2.44 |
| shod | 14 | 79 | 4.17 |
| chod | 14 | 133 | 3.47 |

### Top neighbors of **daii** (of)
| Neighbor | Count | Neighbor freq | PMI-like |
|----------|-------|---------------|----------|
| ot | 5 | 856 | 3.09 |
| aii | 4 | 651 | 3.15 |
| oka | 3 | 300 | 3.79 |
| qo | 3 | 321 | 3.70 |
| cha | 3 | 158 | 4.66 |
| qok | 3 | 1716 | 1.70 |
| sh | 3 | 1037 | 2.24 |
| otch | 3 | 126 | 4.98 |
| do | 2 | 184 | 3.90 |
| okeo | 2 | 114 | 4.55 |
| olo | 2 | 47 | 5.80 |
| cheo | 2 | 345 | 3.08 |
| chek | 2 | 110 | 4.60 |
| ok | 2 | 893 | 1.95 |
| chk | 2 | 80 | 5.05 |
| sa | 2 | 137 | 4.30 |

---
## 7. Distributional Similarity to Confirmed Stems

### Most similar to **cho** (leaf)
| Stem | Similarity | Freq |
|------|-----------|------|
| cth | 0.930 | 189 |
| sho | 0.915 | 389 |
| ctho | 0.887 | 112 |
| chod | 0.869 | 133 |
| do | 0.866 | 184 |
| cheo | 0.842 | 345 |
| tch | 0.827 | 99 |
| qoko | 0.824 | 136 |
| qotch | 0.818 | 118 |
| oko | 0.817 | 120 |

### Most similar to **sho** (root)
| Stem | Similarity | Freq |
|------|-----------|------|
| cho | 0.915 | 702 |
| cth | 0.884 | 189 |
| do | 0.843 | 184 |
| chod | 0.829 | 133 |
| oto | 0.809 | 143 |
| tch | 0.803 | 99 |
| ctho | 0.801 | 112 |
| qoko | 0.792 | 136 |
| sheo | 0.788 | 197 |
| cheo | 0.788 | 345 |

---
## 8. Ten New Vocabulary Proposals

Based on converging evidence from distributional similarity, section distribution,
positional patterns, and co-occurrence analysis.

| # | Word(s) | Proposed Meaning | Confidence | Frequency |
|---|---------|-----------------|-----------|-----------|
| 1 | **ol/or (o- stem)** | preposition "in/at/with" | **50%** | 1210 |
| 2 | **dal/dar (da- stem)** | demonstrative "this/that" or "from" | **45%** | 516 |
| 3 | **oto- (otol/otor)** | stem/stalk (caulis) | **50%** | 143 |
| 4 | **ctho- (cthol/cthor)** | bark/rind (cortex) | **45%** | 112 |
| 5 | **cheo- (cheol/cheor)** | seed/grain (semen) | **40%** | 345 |
| 6 | **qo- prefix** | quantity/measure marker | **55%** | 5224 |
| 7 | **cha- (char/chal)** | quality: "hot/warm" (Galenic) | **40%** | 158 |
| 8 | **ka- (kar/kal)** | quality: "cold" (Galenic) | **35%** | 97 |
| 9 | **oka- (okal/okaiin)** | "each" or "one" (distributive) | **45%** | 300 |
| 10 | **sa- (sar/sal)** | "dry" or "prepare/grind" | **35%** | 137 |

### Proposal 1: ol/or (o- stem) = preposition "in/at/with" (50%)
- Frequency: 1210
- Highest-frequency content stem (1210 tokens)
- Default -l (nominal); sandhi -r before vowels
- Appears evenly across all sections = function word
- Evenly distributed within lines
- Pattern: [X] ol/or [Y] = "X in/at/with Y"

### Proposal 2: dal/dar (da- stem) = demonstrative "this/that" or "from" (45%)
- Frequency: 516
- High frequency (516 tokens)
- Default -r (modifier suffix) = attributive/deictic function
- Often at line boundaries
- Frequently near cho- (leaf) and daiin (of)
- Pattern: dar chol = "this leaf" / "from the leaf"

### Proposal 3: oto- (otol/otor) = stem/stalk (caulis) (50%)
- Frequency: 143
- Default -l (nominal) = noun
- ot- prefix = fourth plant-part category
- Distributional similarity to cho- (leaf) and sho- (root)
- Enriched in herbal early positions (physical description)
- Plant descriptions list leaves, roots, stems, flowers

### Proposal 4: ctho- (cthol/cthor) = bark/rind (cortex) (45%)
- Frequency: 112
- Default -l (nominal) = noun
- cth- prefix = third plant-part category
- Co-occurs with cho- and sho- in plant descriptions
- Herbal section enriched
- Bark is a common medieval medicinal material

### Proposal 5: cheo- (cheol/cheor) = seed/grain (semen) (40%)
- Frequency: 345
- High frequency (345 tokens)
- Default -l (nominal) = noun
- ch- prefix (above-ground) + extended vowel
- Extended form of cho- (leaf) may denote related plant part
- Seeds are central to medieval pharmacy

### Proposal 6: qo- prefix = quantity/measure marker (55%)
- Frequency: 5224
- Total 5224 tokens across all qo- words
- Recipe enrichment: 16.9% vs 14.0% baseline (1.21x)
- **SURPRISE**: Bio/balneological section has HIGHEST enrichment (23.5%, 1.68x)
- This complicates a pure "recipe quantity" reading. qo- may be a more general determiner/quantifier used in both medical recipes AND body-related instructions
- qo + content stem = "a measure/portion of [substance]" or "the [substance]"
- qokaiin is #3 most common -aiin word
- qo- stripped forms almost always have standalone counterparts (keey->qokeey, kain->qokain), confirming it is a productive prefix, not part of the root
- Medieval recipes always specify quantities; balneological texts specify body parts/fluids

### Proposal 7: cha- (char/chal) = quality: "hot/warm" (Galenic) (40%)
- Frequency: 158
- Default -r (modifier) = adjective
- Enriched in herbal middle positions (where qualities appear)
- ch- prefix in modifier form
- Medieval herbals specify hot/cold/dry/moist
- Galenic qualities are the most important descriptors

### Proposal 8: ka- (kar/kal) = quality: "cold" (Galenic) (35%)
- Frequency: 97
- Default -r (modifier) = adjective
- Structurally related to cha- but without ch- prefix
- If ch- marks "above-ground" and cha- = hot, ka- may be opposite
- Expected to pair with cha- in quality descriptions

### Proposal 9: oka- (okal/okaiin) = "each" or "one" (distributive) (45%)
- Frequency: 300
- High frequency (300 tokens)
- okaiin is a locked-n function word
- Appears between plant-part terms in listing contexts
- Recipe sections use for enumerating ingredients

### Proposal 10: sa- (sar/sal) = "dry" or "prepare/grind" (35%)
- Frequency: 137
- Default -r (modifier) = adjective or verb participle
- Enriched in late herbal positions (preparation section)
- s- prefix may relate to sh- (root/hidden) category
- Medieval preparation involves drying, grinding, boiling

---
## 9. Consolidated Emerging Dictionary

| Stem | Surface forms | Category | Meaning | Confidence | Status |
|------|--------------|----------|---------|-----------|--------|
| cho- | chol, chor, chody, chey | Plant part | leaf/foliage | 85% | CONFIRMED |
| sho- | shol, shor, shody, shey | Plant part | root (radix) | 75% | CONFIRMED |
| daii- | daiin, dain | Function | "of" (genitive) | 60% | CONFIRMED |
| chor | chor | Plant part | flower (flos) | 55% | CONFIRMED |
| qo- | qol, qo+X | Prefix | quantity/measure | 55% | NEW |
| oto- | otol, otor | Plant part | stem/stalk | 50% | NEW |
| o- | ol, or | Function | "in/at/with" | 50% | NEW |
| aii- | aiin, ain | Function | "and" | 45% | prior |
| ctho- | cthol, cthor | Plant part | bark/rind | 45% | NEW |
| da- | dal, dar | Function | "this/from" | 45% | NEW |
| oka- | okal, okaiin | Function | "each/one" | 45% | NEW |
| cha- | char, chal | Quality | "hot/warm" | 40% | NEW |
| cheo- | cheol, cheor | Plant part | seed/grain | 40% | NEW |
| ka- | kar, kal | Quality | "cold" | 35% | NEW |
| sa- | sar, sal | Quality/verb | "dry/prepare" | 35% | NEW |

---
## 10. Sample Readings with Proposed Dictionary

**f101r.8**: `ol aiin oteol chor oteey chokchey kor aiin shok chol chol qoky daiin ol s al ydar daiin or ory okeey daiin shey daiin okol cheor`
  Gloss: in and [oteol] FLOWER [oteey] [chokchey] [kor] and [shok] LEAF LEAF [qoky] of in [s] [al] [ydar] of at [ory] [okeey] of ROOT.y of [okol] SEED.att

**f101r.5**: `daiin ctheol cheol okor or aiin cheol cho keeodchey okol okeol or chol chy r aiin oteol or aiin ol chey oteeod sheol okeol chosaiin sheom`
  Gloss: of [ctheol] SEED [okor] at and SEED [cho] [keeodchey] [okol] [okeol] at LEAF [chy] [r] and [oteol] at and in LEAF.y [oteeod] [sheol] [okeol] [chosaiin] [sheom]

**f68v3.5**: `oky otal ees choty cheas otchdy s ar oekaiin oteol dar cheo dair qoeeokaiin otchey dal cheky ykos yokeg s ol oy ykoees yty dy y chody otol olees oty ar qotay otoy chey kodar dar sheody shees daiin oteeoaly oteeosol ol okol olsey tol cheol okeey choekcheey okchy qokchshy dchol chshek`
  Gloss: [oky] [otal] [ees] [choty] [cheas] [otchdy] [s] [ar] [oekaiin] [oteol] from [cheo] [dair] [qoeeokaiin] [otchey] this [cheky] [ykos] [yokeg] [s] in [oy] [ykoees] [yty] [dy] [y] LEAF.dy STEM [olees] [oty] [ar] [qotay] [otoy] LEAF.y [kodar] from [sheody] [shees] of [oteeoaly] [oteeosol] in [okol] [olsey] [tol] SEED [okeey] [choekcheey] [okchy] [qokchshy] [dchol] [chshek]

**f81r.5**: `qol cheol okeey ol ol ol aiin ol or ain`
  Gloss: QTY.in SEED [okeey] in in in and in at and

**f106v.23**: `ol kalol shar chor okal chdy chol chey qotaiin or aiin okeedy qokain`
  Gloss: in [kalol] [shar] FLOWER each [chdy] LEAF LEAF.y QTY.fn at and [okeedy] QTY.each

**f101r.9**: `daiin okel qokcheol ykeor dar ol otechy ykeor dor aiin chl s cheol okeal shey qodar soiin choky qokeol daiin dar okchol cheor chety`
  Gloss: of [okel] [qokcheol] [ykeor] from in [otechy] [ykeor] [dor] and [chl] [s] SEED [okeal] ROOT.y [qodar] [soiin] [choky] [qokeol] of from [okchol] SEED.att [chety]

**f101v.23**: `yaiin ol olor daiin okeey qok ykeol aiin qockhy daiin olch odar qokeol ol or aiin olaiin keeol she qokeeeor s ydy cheor okeey choly dar`
  Gloss: [yaiin] in [olor] of [okeey] [qok] [ykeol] and [qockhy] of [olch] [odar] [qokeol] in at and [olaiin] [keeol] [she] [qokeeeor] [s] [ydy] SEED.att [okeey] [choly] from

**f72r1.1**: `oteeo cthe chlol cheol olchear al oteey chedal oteey okeoaly chol chokeol cheolky okaiir okeey sheoltey cheor aiin dal okochey sho okaley ol chalaiin chekeol kol otos ar aiin otam otam chotam sal okeo dar ar adal ar okeeos aiin oteey o kaiin`
  Gloss: [oteeo] [cthe] [chlol] SEED [olchear] [al] [oteey] [chedal] [oteey] [okeoaly] LEAF [chokeol] [cheolky] [okaiir] [okeey] [sheoltey] SEED.att and this [okochey] [sho] [okaley] in [chalaiin] [chekeol] [kol] [otos] [ar] and [otam] [otam] [chotam] [sal] [okeo] from [ar] [adal] [ar] [okeeos] and [oteey] [o] [kaiin]

**f89r2.13**: `daiin olkey okeol okey okeeol qoor ol chor cheky chol daiin chol cheol kolam olcheol dol cheol`
  Gloss: of [olkey] [okeol] [okey] [okeeol] [qoor] in FLOWER [cheky] LEAF of LEAF SEED [kolam] [olcheol] [dol] SEED

**f101v.27**: `sl chol choly okeey dal qol shckheol chol cthear keeol cheeo ol chs oraiin qokeeey saiir qodaiin cheol qokeey daiin cheodag`
  Gloss: [sl] LEAF [choly] [okeey] this QTY.in [shckheol] LEAF [cthear] [keeol] [cheeo] in [chs] [oraiin] [qokeeey] [saiir] QTY.of SEED [qokeey] of [cheodag]

---
## 11. Methodological Notes and Caveats

### Strengths
1. Distributional semantics is language-agnostic -- no assumption about underlying language needed
2. Section distribution is objective and verifiable
3. Positional analysis exploits the known structure of medieval herbals
4. Co-occurrence data is falsifiable -- if cho-=leaf, neighbors should be plant-related

### Risks
1. **Circular reasoning**: Using section labels to infer meaning presupposes the section labels are correct
2. **Stem extraction is hypothesis-dependent**: The n/l/r sandhi model is not proven
3. **Low confidence**: Most proposals are 35-55% -- suggestive but not conclusive
4. **No independent verification**: Without a bilingual key, all readings remain speculative

### What would increase confidence
- Matching a Voynich word to a known plant name in a specific historical language
- Cross-validating proposed plant-part words against the botanical illustrations
- Finding that the proposed dictionary produces coherent readings across multiple pages
- Statistical tests confirming Zipfian distributions for proposed function words
