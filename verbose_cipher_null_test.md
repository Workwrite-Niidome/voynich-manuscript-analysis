# Verbose Cipher Null Character Hypothesis Test

## Hypothesis

15th-century verbose ciphers inserted meaningless 'null' characters to disguise
the true plaintext. If the Voynich manuscript uses such a system, removing the
null characters should:
1. **Decrease entropy** (remaining chars are more predictable)
2. **Increase mutual information** between adjacent characters
3. **Improve bigram overlap** with known languages
4. **Produce recognizable word patterns**

Historical precedents: Alberti cipher disk (1467), Simonetta cipher (Milan, 1474),
Trithemius Polygraphiae (1508).

---

## Baseline Statistics

- Total words parsed: 37031
- Words ending in -y: 14776 (39.9%)
- Words starting with qo-: 5239 (14.1%)
- Gallows characters (k,t,p,f) as % of all chars: 10.6%

### Word-Final Character Distribution
| Char | Count | Freq% |
|------|-------|-------|
| y | 14776 | 39.9% |
| n | 5976 | 16.1% |
| r | 5677 | 15.3% |
| l | 5648 | 15.3% |
| s | 1324 | 3.6% |
| o | 1086 | 2.9% |
| m | 1000 | 2.7% |
| d | 663 | 1.8% |
| e | 277 | 0.7% |
| g | 153 | 0.4% |
| h | 104 | 0.3% |
| k | 91 | 0.2% |
| t | 69 | 0.2% |
| a | 53 | 0.1% |
| p | 29 | 0.1% |

### Word-Initial Bigram Distribution
| Bigram | Count | Freq% |
|--------|-------|-------|
| ch | 5939 | 16.5% |
| qo | 5239 | 14.5% |
| sh | 2894 | 8.0% |
| ot | 2448 | 6.8% |
| ok | 2390 | 6.6% |
| da | 1862 | 5.2% |
| ol | 1586 | 4.4% |
| ai | 957 | 2.7% |
| ar | 591 | 1.6% |
| yk | 563 | 1.6% |
| or | 560 | 1.6% |
| al | 555 | 1.5% |
| sa | 482 | 1.3% |
| yt | 475 | 1.3% |
| ct | 456 | 1.3% |

---

## Strategy Results

### Original (no removal)
- Total words: 37031
- Unique words: 8851
- Total characters: 188670
- Unique characters: 26
- Mean word length: 5.09
- Median word length: 5
- **Entropy (bits/char): 3.8658**
- **Mutual Information: 1.5914**

**Top 20 characters:**
| Char | Count | Freq% |
|------|-------|-------|
| o | 25113 | 13.3% |
| e | 20534 | 10.9% |
| y | 17466 | 9.3% |
| h | 17283 | 9.2% |
| a | 14549 | 7.7% |
| c | 13121 | 7.0% |
| i | 11933 | 6.3% |
| k | 10800 | 5.7% |
| l | 10668 | 5.7% |
| d | 10492 | 5.6% |
| r | 7571 | 4.0% |
| s | 7011 | 3.7% |
| t | 7008 | 3.7% |
| n | 6189 | 3.3% |
| q | 5435 | 2.9% |
| p | 1655 | 0.9% |
| m | 1065 | 0.6% |
| f | 492 | 0.3% |
| g | 165 | 0.1% |
| x | 43 | 0.0% |

**Top 20 bigrams:**
| Bigram | Count | Freq% |
|--------|-------|-------|
| ch | 11066 | 7.30% |
| he | 7953 | 5.24% |
| ai | 6683 | 4.41% |
| in | 6052 | 3.99% |
| ok | 6041 | 3.98% |
| ol | 5579 | 3.68% |
| ee | 5388 | 3.55% |
| qo | 5304 | 3.50% |
| ey | 5236 | 3.45% |
| dy | 5022 | 3.31% |
| ii | 4811 | 3.17% |
| sh | 4174 | 2.75% |
| ke | 4017 | 2.65% |
| ot | 4005 | 2.64% |
| ho | 3976 | 2.62% |
| ed | 3653 | 2.41% |
| da | 3469 | 2.29% |
| ar | 3411 | 2.25% |
| eo | 3384 | 2.23% |
| al | 3188 | 2.10% |

**Top 20 words:**
| Word | Count |
|------|-------|
| daiin | 669 |
| aiin | 552 |
| ol | 514 |
| chey | 487 |
| ar | 398 |
| qokeey | 367 |
| or | 346 |
| chol | 345 |
| shey | 333 |
| chedy | 324 |
| al | 272 |
| qokain | 271 |
| dar | 255 |
| qokaiin | 255 |
| s | 251 |
| shedy | 248 |
| qokeedy | 218 |
| okaiin | 201 |
| y | 199 |
| chor | 196 |

**Bigram overlap with reference languages (out of 20):**
- Latin: 2/20
- Italian: 3/20
- Hebrew: 2/20
- Arabic: 1/20
---

### Strip final -y
- Total words: 37031
- Unique words: 8138
- Total characters: 174093
- Unique characters: 26
- Mean word length: 4.70
- Median word length: 5
- **Entropy (bits/char): 3.8291**
- **Mutual Information: 1.6228**

**Top 20 characters:**
| Char | Count | Freq% |
|------|-------|-------|
| o | 25113 | 14.4% |
| e | 20534 | 11.8% |
| h | 17283 | 9.9% |
| a | 14549 | 8.4% |
| c | 13121 | 7.5% |
| i | 11933 | 6.9% |
| k | 10800 | 6.2% |
| l | 10668 | 6.1% |
| d | 10492 | 6.0% |
| r | 7571 | 4.3% |
| s | 7011 | 4.0% |
| t | 7008 | 4.0% |
| n | 6189 | 3.6% |
| q | 5435 | 3.1% |
| y | 2889 | 1.7% |
| p | 1655 | 1.0% |
| m | 1065 | 0.6% |
| f | 492 | 0.3% |
| g | 165 | 0.1% |
| x | 43 | 0.0% |

**Top 20 bigrams:**
| Bigram | Count | Freq% |
|--------|-------|-------|
| ch | 11066 | 8.07% |
| he | 7953 | 5.80% |
| ai | 6683 | 4.88% |
| in | 6052 | 4.42% |
| ok | 6041 | 4.41% |
| ol | 5579 | 4.07% |
| ee | 5388 | 3.93% |
| qo | 5304 | 3.87% |
| ii | 4811 | 3.51% |
| sh | 4174 | 3.05% |
| ke | 4017 | 2.93% |
| ot | 4005 | 2.92% |
| ho | 3976 | 2.90% |
| ed | 3653 | 2.67% |
| da | 3469 | 2.53% |
| ar | 3411 | 2.49% |
| eo | 3384 | 2.47% |
| al | 3188 | 2.33% |
| ka | 2975 | 2.17% |
| or | 2573 | 1.88% |

**Top 20 words:**
| Word | Count |
|------|-------|
| daiin | 672 |
| ol | 571 |
| aiin | 557 |
| che | 504 |
| ar | 427 |
| qokee | 382 |
| she | 370 |
| chol | 366 |
| or | 365 |
| ched | 347 |
| al | 310 |
| s | 276 |
| dar | 271 |
| qokain | 271 |
| shed | 270 |
| qokaiin | 255 |
| qokeed | 244 |
| dal | 206 |
| chor | 205 |
| y | 202 |

**Bigram overlap with reference languages (out of 20):**
- Latin: 3/20
- Italian: 4/20
- Hebrew: 2/20
- Arabic: 1/20
---

### Strip qo- prefix
- Total words: 37031
- Unique words: 8385
- Total characters: 178276
- Unique characters: 26
- Mean word length: 4.81
- Median word length: 5
- **Entropy (bits/char): 3.8189**
- **Mutual Information: 1.5289**

**Top 20 characters:**
| Char | Count | Freq% |
|------|-------|-------|
| e | 20534 | 11.5% |
| o | 19916 | 11.2% |
| y | 17466 | 9.8% |
| h | 17283 | 9.7% |
| a | 14549 | 8.2% |
| c | 13121 | 7.4% |
| i | 11933 | 6.7% |
| k | 10800 | 6.1% |
| l | 10668 | 6.0% |
| d | 10492 | 5.9% |
| r | 7571 | 4.2% |
| s | 7011 | 3.9% |
| t | 7008 | 3.9% |
| n | 6189 | 3.5% |
| p | 1655 | 0.9% |
| m | 1065 | 0.6% |
| f | 492 | 0.3% |
| q | 238 | 0.1% |
| g | 165 | 0.1% |
| x | 43 | 0.0% |

**Top 20 bigrams:**
| Bigram | Count | Freq% |
|--------|-------|-------|
| ch | 11066 | 7.83% |
| he | 7953 | 5.63% |
| ai | 6683 | 4.73% |
| in | 6052 | 4.28% |
| ee | 5388 | 3.81% |
| ol | 5328 | 3.77% |
| ey | 5236 | 3.71% |
| dy | 5022 | 3.56% |
| ii | 4811 | 3.41% |
| sh | 4174 | 2.96% |
| ke | 4017 | 2.84% |
| ho | 3976 | 2.81% |
| ed | 3653 | 2.59% |
| da | 3469 | 2.46% |
| ar | 3411 | 2.41% |
| eo | 3384 | 2.40% |
| al | 3188 | 2.26% |
| ok | 2999 | 2.12% |
| ka | 2975 | 2.11% |
| ot | 2856 | 2.02% |

**Top 20 words:**
| Word | Count |
|------|-------|
| daiin | 708 |
| aiin | 578 |
| ol | 519 |
| chey | 494 |
| keey | 434 |
| ar | 411 |
| or | 356 |
| chol | 346 |
| shey | 334 |
| chedy | 326 |
| kaiin | 325 |
| kain | 318 |
| al | 278 |
| dar | 265 |
| l | 265 |
| s | 255 |
| shedy | 248 |
| keedy | 248 |
| key | 219 |
| y | 214 |

**Bigram overlap with reference languages (out of 20):**
- Latin: 2/20
- Italian: 3/20
- Hebrew: 2/20
- Arabic: 1/20
---

### Strip gallows (k,t,p,f)
- Total words: 36994
- Unique words: 5959
- Total characters: 168715
- Unique characters: 22
- Mean word length: 4.56
- Median word length: 4
- **Entropy (bits/char): 3.6082**
- **Mutual Information: 1.5025**

**Top 20 characters:**
| Char | Count | Freq% |
|------|-------|-------|
| o | 25113 | 14.9% |
| e | 20534 | 12.2% |
| y | 17466 | 10.4% |
| h | 17283 | 10.2% |
| a | 14549 | 8.6% |
| c | 13121 | 7.8% |
| i | 11933 | 7.1% |
| l | 10668 | 6.3% |
| d | 10492 | 6.2% |
| r | 7571 | 4.5% |
| s | 7011 | 4.2% |
| n | 6189 | 3.7% |
| q | 5435 | 3.2% |
| m | 1065 | 0.6% |
| g | 165 | 0.1% |
| x | 43 | 0.0% |
| j | 37 | 0.0% |
| b | 17 | 0.0% |
| v | 14 | 0.0% |
| u | 7 | 0.0% |

**Top 20 bigrams:**
| Bigram | Count | Freq% |
|--------|-------|-------|
| ch | 13106 | 9.95% |
| he | 8020 | 6.09% |
| ai | 6683 | 5.07% |
| in | 6052 | 4.59% |
| ol | 5637 | 4.28% |
| ee | 5562 | 4.22% |
| ey | 5514 | 4.19% |
| qo | 5313 | 4.03% |
| dy | 5030 | 3.82% |
| ii | 4811 | 3.65% |
| oe | 4375 | 3.32% |
| sh | 4174 | 3.17% |
| ho | 4014 | 3.05% |
| ed | 3655 | 2.77% |
| oa | 3613 | 2.74% |
| da | 3476 | 2.64% |
| eo | 3421 | 2.60% |
| ar | 3411 | 2.59% |
| al | 3188 | 2.42% |
| or | 2612 | 1.98% |

**Top 20 words:**
| Word | Count |
|------|-------|
| chey | 753 |
| aiin | 674 |
| daiin | 673 |
| ol | 616 |
| ar | 504 |
| chol | 487 |
| qoeey | 449 |
| chy | 442 |
| chedy | 412 |
| oaiin | 410 |
| or | 407 |
| shey | 391 |
| qoaiin | 368 |
| oeey | 364 |
| qoain | 340 |
| al | 323 |
| oar | 315 |
| chor | 306 |
| cheey | 294 |
| qoeedy | 289 |

**Bigram overlap with reference languages (out of 20):**
- Latin: 3/20
- Italian: 4/20
- Hebrew: 2/20
- Arabic: 1/20
---

### Combined (y + qo + gallows)
- Total words: 36706
- Unique words: 5071
- Total characters: 143774
- Unique characters: 22
- Mean word length: 3.92
- Median word length: 4
- **Entropy (bits/char): 3.5001**
- **Mutual Information: 1.5291**

**Top 20 characters:**
| Char | Count | Freq% |
|------|-------|-------|
| e | 20534 | 14.3% |
| o | 19931 | 13.9% |
| h | 17283 | 12.0% |
| a | 14549 | 10.1% |
| c | 13121 | 9.1% |
| i | 11933 | 8.3% |
| l | 10668 | 7.4% |
| d | 10492 | 7.3% |
| r | 7571 | 5.3% |
| s | 7011 | 4.9% |
| n | 6189 | 4.3% |
| y | 2889 | 2.0% |
| m | 1065 | 0.7% |
| q | 253 | 0.2% |
| g | 165 | 0.1% |
| x | 43 | 0.0% |
| j | 37 | 0.0% |
| b | 17 | 0.0% |
| v | 14 | 0.0% |
| u | 7 | 0.0% |

**Top 20 bigrams:**
| Bigram | Count | Freq% |
|--------|-------|-------|
| ch | 13106 | 12.24% |
| he | 8020 | 7.49% |
| ai | 6683 | 6.24% |
| in | 6052 | 5.65% |
| ee | 5562 | 5.19% |
| ol | 5356 | 5.00% |
| ii | 4811 | 4.49% |
| sh | 4174 | 3.90% |
| ho | 4014 | 3.75% |
| ed | 3655 | 3.41% |
| da | 3476 | 3.25% |
| eo | 3421 | 3.20% |
| ar | 3411 | 3.19% |
| al | 3188 | 2.98% |
| or | 2569 | 2.40% |
| oe | 2494 | 2.33% |
| oa | 2236 | 2.09% |
| od | 1963 | 1.83% |
| oc | 1407 | 1.31% |
| la | 936 | 0.87% |

**Top 20 words:**
| Word | Count |
|------|-------|
| aiin | 1047 |
| che | 903 |
| ol | 859 |
| ar | 765 |
| daiin | 716 |
| ch | 655 |
| al | 641 |
| ee | 611 |
| chol | 580 |
| ched | 536 |
| ain | 530 |
| or | 497 |
| she | 454 |
| oaiin | 413 |
| e | 393 |
| eed | 388 |
| oee | 385 |
| o | 381 |
| l | 345 |
| ed | 344 |

**Bigram overlap with reference languages (out of 20):**
- Latin: 3/20
- Italian: 5/20
- Hebrew: 2/20
- Arabic: 2/20
---

### Strip vowels a,o,e (Simonetta)
- Total words: 36900
- Unique words: 4204
- Total characters: 128474
- Unique characters: 23
- Mean word length: 3.48
- Median word length: 3
- **Entropy (bits/char): 3.6240**
- **Mutual Information: 1.1601**

**Top 20 characters:**
| Char | Count | Freq% |
|------|-------|-------|
| y | 17466 | 13.6% |
| h | 17283 | 13.5% |
| c | 13121 | 10.2% |
| i | 11933 | 9.3% |
| k | 10800 | 8.4% |
| l | 10668 | 8.3% |
| d | 10492 | 8.2% |
| r | 7571 | 5.9% |
| s | 7011 | 5.5% |
| t | 7008 | 5.5% |
| n | 6189 | 4.8% |
| q | 5435 | 4.2% |
| p | 1655 | 1.3% |
| m | 1065 | 0.8% |
| f | 492 | 0.4% |
| g | 165 | 0.1% |
| x | 43 | 0.0% |
| j | 37 | 0.0% |
| b | 17 | 0.0% |
| v | 14 | 0.0% |

**Top 20 bigrams:**
| Bigram | Count | Freq% |
|--------|-------|-------|
| ch | 11066 | 12.08% |
| in | 6052 | 6.61% |
| hy | 5181 | 5.66% |
| dy | 5088 | 5.56% |
| ii | 4813 | 5.26% |
| sh | 4174 | 4.56% |
| hd | 3628 | 3.96% |
| qk | 3148 | 3.44% |
| ky | 2415 | 2.64% |
| hl | 2188 | 2.39% |
| di | 1950 | 2.13% |
| ki | 1685 | 1.84% |
| hr | 1484 | 1.62% |
| kl | 1438 | 1.57% |
| kd | 1343 | 1.47% |
| ty | 1232 | 1.35% |
| qt | 1174 | 1.28% |
| kc | 1171 | 1.28% |
| lk | 1151 | 1.26% |
| tc | 1069 | 1.17% |

**Top 20 words:**
| Word | Count |
|------|-------|
| l | 971 |
| r | 961 |
| chy | 945 |
| diin | 758 |
| qky | 747 |
| chl | 663 |
| chdy | 642 |
| iin | 632 |
| ky | 611 |
| shy | 606 |
| ty | 525 |
| chr | 482 |
| qkdy | 442 |
| kl | 414 |
| shdy | 409 |
| dr | 368 |
| qkl | 368 |
| tl | 360 |
| y | 354 |
| s | 344 |

**Bigram overlap with reference languages (out of 20):**
- Latin: 1/20
- Italian: 2/20
- Hebrew: 2/20
- Arabic: 0/20
---

## Comparative Summary

| Strategy | Words | Unique Words | Unique Chars | Mean WL | Entropy | MI | Latin | Italian | Hebrew | Arabic |
|----------|-------|-------------|-------------|---------|---------|-----|-------|---------|--------|--------|
| Original (no removal) | 37031 | 8851 | 26 | 5.09 | 3.8658 | 1.5914 | 2 | 3 | 2 | 1 |
| Strip final -y | 37031 | 8138 | 26 | 4.70 | 3.8291 | 1.6228 | 3 | 4 | 2 | 1 |
| Strip qo- prefix | 37031 | 8385 | 26 | 4.81 | 3.8189 | 1.5289 | 2 | 3 | 2 | 1 |
| Strip gallows (k,t,p,f) | 36994 | 5959 | 22 | 4.56 | 3.6082 | 1.5025 | 3 | 4 | 2 | 1 |
| Combined (y + qo + gallows) | 36706 | 5071 | 22 | 3.92 | 3.5001 | 1.5291 | 3 | 5 | 2 | 2 |
| Strip vowels a,o,e (Simonetta) | 36900 | 4204 | 23 | 3.48 | 3.6240 | 1.1601 | 1 | 2 | 2 | 0 |

---

## Entropy Analysis

Baseline entropy: 3.8658 bits/char
Baseline MI: 1.5914

| Strategy | Entropy Change | MI Change | Entropy Direction | MI Direction |
|----------|---------------|-----------|-------------------|-------------|
| Strip final -y | -0.0367 | +0.0314 | DECREASE (supports null) | INCREASE (supports null) |
| Strip qo- prefix | -0.0470 | -0.0624 | DECREASE (supports null) | DECREASE (against null) |
| Strip gallows (k,t,p,f) | -0.2576 | -0.0889 | DECREASE (supports null) | DECREASE (against null) |
| Combined (y + qo + gallows) | -0.3657 | -0.0623 | DECREASE (supports null) | DECREASE (against null) |
| Strip vowels a,o,e (Simonetta) | -0.2418 | -0.4313 | DECREASE (supports null) | DECREASE (against null) |

---

## Emerging Patterns After Null Removal

### Emerging Patterns After Strip final -y
- Short common words (len<=3): 20
  - 'ol': 571 occurrences
  - 'che': 504 occurrences
  - 'ar': 427 occurrences
  - 'she': 370 occurrences
  - 'or': 365 occurrences
  - 'al': 310 occurrences
  - 's': 276 occurrences
  - 'dar': 271 occurrences
  - 'dal': 206 occurrences
  - 'y': 202 occurrences
- Word length distribution:
  - len 1: 1311 words (3.5%)
  - len 2: 2976 words (8.0%)
  - len 3: 4891 words (13.2%)
  - len 4: 8325 words (22.5%)
  - len 5: 8700 words (23.5%)
  - len 6: 5531 words (14.9%)
  - len 7: 2871 words (7.8%)
  - len 8: 1254 words (3.4%)
  - len 9: 570 words (1.5%)
  - len 10: 246 words (0.7%)
  - len 11: 135 words (0.4%)
  - len 12: 95 words (0.3%)
  - len 13: 47 words (0.1%)
  - len 14: 35 words (0.1%)
  - len 15: 18 words (0.0%)
  - len 16: 12 words (0.0%)
  - len 17: 3 words (0.0%)
  - len 18: 4 words (0.0%)
  - len 19: 4 words (0.0%)
  - len 20: 1 words (0.0%)
  - len 22: 1 words (0.0%)
  - len 23: 1 words (0.0%)
- Top CV patterns:
  - CCVC: 2623 (7.1%)
  - VC: 2185 (5.9%)
  - CVC: 2107 (5.7%)
  - VCVC: 1614 (4.4%)
  - CCVVC: 1334 (3.6%)
  - CVCVC: 1306 (3.5%)
  - CVVVC: 1243 (3.4%)
  - CCV: 1158 (3.1%)
  - C: 1102 (3.0%)
  - CCCVC: 1084 (2.9%)
  - CVCVVC: 932 (2.5%)
  - VCVVC: 895 (2.4%)
  - VCVVVC: 752 (2.0%)
  - CVVC: 749 (2.0%)
  - VVVC: 704 (1.9%)

### Emerging Patterns After Strip qo- prefix
- Short common words (len<=3): 18
  - 'ol': 519 occurrences
  - 'ar': 411 occurrences
  - 'or': 356 occurrences
  - 'al': 278 occurrences
  - 'dar': 265 occurrences
  - 'l': 265 occurrences
  - 's': 255 occurrences
  - 'key': 219 occurrences
  - 'y': 214 occurrences
  - 'kal': 203 occurrences
- Word length distribution:
  - len 1: 1196 words (3.2%)
  - len 2: 2692 words (7.3%)
  - len 3: 4361 words (11.8%)
  - len 4: 8382 words (22.6%)
  - len 5: 8982 words (24.3%)
  - len 6: 5597 words (15.1%)
  - len 7: 2949 words (8.0%)
  - len 8: 1503 words (4.1%)
  - len 9: 709 words (1.9%)
  - len 10: 293 words (0.8%)
  - len 11: 134 words (0.4%)
  - len 12: 97 words (0.3%)
  - len 13: 54 words (0.1%)
  - len 14: 35 words (0.1%)
  - len 15: 16 words (0.0%)
  - len 16: 14 words (0.0%)
  - len 17: 6 words (0.0%)
  - len 18: 1 words (0.0%)
  - len 19: 5 words (0.0%)
  - len 20: 2 words (0.0%)
  - len 21: 1 words (0.0%)
  - len 22: 1 words (0.0%)
  - len 23: 1 words (0.0%)
- Top CV patterns:
  - CVC: 2549 (6.9%)
  - CCVC: 2510 (6.8%)
  - VC: 1881 (5.1%)
  - CVVC: 1729 (4.7%)
  - CVVVC: 1700 (4.6%)
  - VCVC: 1530 (4.1%)
  - CCVVC: 1446 (3.9%)
  - CCCVC: 1353 (3.7%)
  - CCVCC: 1098 (3.0%)
  - C: 1081 (2.9%)
  - VCVVC: 1055 (2.8%)
  - CCCC: 778 (2.1%)
  - VCVVVC: 769 (2.1%)
  - VVVC: 747 (2.0%)
  - CC: 672 (1.8%)

### Emerging Patterns After Strip gallows (k,t,p,f)
- Short common words (len<=3): 19
  - 'ol': 616 occurrences
  - 'ar': 504 occurrences
  - 'chy': 442 occurrences
  - 'or': 407 occurrences
  - 'al': 323 occurrences
  - 'oar': 315 occurrences
  - 'oal': 280 occurrences
  - 'dar': 257 occurrences
  - 's': 252 occurrences
  - 'y': 238 occurrences
- Word length distribution:
  - len 1: 1021 words (2.8%)
  - len 2: 3100 words (8.4%)
  - len 3: 5328 words (14.4%)
  - len 4: 9073 words (24.5%)
  - len 5: 9242 words (25.0%)
  - len 6: 5212 words (14.1%)
  - len 7: 2192 words (5.9%)
  - len 8: 1015 words (2.7%)
  - len 9: 389 words (1.1%)
  - len 10: 185 words (0.5%)
  - len 11: 99 words (0.3%)
  - len 12: 66 words (0.2%)
  - len 13: 27 words (0.1%)
  - len 14: 22 words (0.1%)
  - len 15: 8 words (0.0%)
  - len 16: 6 words (0.0%)
  - len 17: 3 words (0.0%)
  - len 18: 3 words (0.0%)
  - len 19: 1 words (0.0%)
  - len 20: 1 words (0.0%)
  - len 21: 1 words (0.0%)
- Top CV patterns:
  - CCVC: 3037 (8.2%)
  - VC: 2456 (6.6%)
  - CVVVC: 2283 (6.2%)
  - CVC: 1896 (5.1%)
  - VVVC: 1882 (5.1%)
  - CVVC: 1846 (5.0%)
  - VVC: 1838 (5.0%)
  - CCVVC: 1595 (4.3%)
  - CCVCC: 994 (2.7%)
  - C: 877 (2.4%)
  - VVVVC: 735 (2.0%)
  - CCC: 729 (2.0%)
  - CVVVVC: 612 (1.7%)
  - CCCVC: 605 (1.6%)
  - VCVC: 526 (1.4%)

### Emerging Patterns After Combined (y + qo + gallows)
- Short common words (len<=3): 33
  - 'che': 903 occurrences
  - 'ol': 859 occurrences
  - 'ar': 765 occurrences
  - 'ch': 655 occurrences
  - 'al': 641 occurrences
  - 'ee': 611 occurrences
  - 'ain': 530 occurrences
  - 'or': 497 occurrences
  - 'she': 454 occurrences
  - 'e': 393 occurrences
- Word length distribution:
  - len 1: 2166 words (5.9%)
  - len 2: 5674 words (15.5%)
  - len 3: 7923 words (21.6%)
  - len 4: 9020 words (24.6%)
  - len 5: 6471 words (17.6%)
  - len 6: 2770 words (7.5%)
  - len 7: 1387 words (3.8%)
  - len 8: 688 words (1.9%)
  - len 9: 270 words (0.7%)
  - len 10: 158 words (0.4%)
  - len 11: 67 words (0.2%)
  - len 12: 56 words (0.2%)
  - len 13: 21 words (0.1%)
  - len 14: 19 words (0.1%)
  - len 15: 6 words (0.0%)
  - len 16: 4 words (0.0%)
  - len 17: 2 words (0.0%)
  - len 18: 1 words (0.0%)
  - len 19: 2 words (0.0%)
  - len 21: 1 words (0.0%)
- Top CV patterns:
  - VC: 3495 (9.5%)
  - CCVC: 2905 (7.9%)
  - VVC: 2748 (7.5%)
  - VVVC: 2212 (6.0%)
  - CCV: 1770 (4.8%)
  - CVC: 1603 (4.4%)
  - CCVVC: 1398 (3.8%)
  - C: 1361 (3.7%)
  - CVVVC: 1300 (3.5%)
  - CC: 980 (2.7%)
  - VV: 968 (2.6%)
  - V: 805 (2.2%)
  - CVVC: 783 (2.1%)
  - CCVV: 764 (2.1%)
  - VVVVC: 744 (2.0%)

### Emerging Patterns After Strip vowels a,o,e (Simonetta)
- Short common words (len<=3): 33
  - 'l': 971 occurrences
  - 'r': 961 occurrences
  - 'chy': 945 occurrences
  - 'qky': 747 occurrences
  - 'chl': 663 occurrences
  - 'iin': 632 occurrences
  - 'ky': 611 occurrences
  - 'shy': 606 occurrences
  - 'ty': 525 occurrences
  - 'chr': 482 occurrences
- Word length distribution:
  - len 1: 3159 words (8.6%)
  - len 2: 6383 words (17.3%)
  - len 3: 10399 words (28.2%)
  - len 4: 9114 words (24.7%)
  - len 5: 4307 words (11.7%)
  - len 6: 2421 words (6.6%)
  - len 7: 644 words (1.7%)
  - len 8: 229 words (0.6%)
  - len 9: 105 words (0.3%)
  - len 10: 69 words (0.2%)
  - len 11: 33 words (0.1%)
  - len 12: 18 words (0.0%)
  - len 13: 5 words (0.0%)
  - len 14: 4 words (0.0%)
  - len 15: 5 words (0.0%)
  - len 16: 3 words (0.0%)
  - len 17: 1 words (0.0%)
  - len 20: 1 words (0.0%)
- Top CV patterns:
  - CCC: 8802 (23.9%)
  - CCCC: 6411 (17.4%)
  - CC: 6115 (16.6%)
  - C: 3159 (8.6%)
  - CCCCC: 2847 (7.7%)
  - CVVC: 1823 (4.9%)
  - CCCCCC: 1812 (4.9%)
  - CCVVC: 1019 (2.8%)
  - CVC: 887 (2.4%)
  - CCVC: 702 (1.9%)
  - VVC: 679 (1.8%)
  - CCCVVC: 430 (1.2%)
  - CCCCCCC: 420 (1.1%)
  - VC: 262 (0.7%)
  - CCCVC: 233 (0.6%)

---

## Positional Analysis of Suspected Nulls

### Position of 'y' in words
- Initial: 1811 (10.4%)
- Medial: 1078 (6.2%)
- Final: 14577 (83.5%)

### Position of 'k' (gallows) in words
- Initial: 1141 (10.6%)
- Medial: 9582 (88.7%)
- Final: 77 (0.7%)

### Position of 't' (gallows) in words
- Initial: 1017 (14.5%)
- Medial: 5930 (84.6%)
- Final: 61 (0.9%)

### Position of 'p' (gallows) in words
- Initial: 538 (32.5%)
- Medial: 1094 (66.1%)
- Final: 23 (1.4%)

### Position of 'f' (gallows) in words
- Initial: 130 (26.4%)
- Medial: 343 (69.7%)
- Final: 19 (3.9%)

### Words starting with 'qo-' — what follows?
- Unique stems after qo-: 848
- Top stems:
  - 'keey': 367x (appears independently: 67x)
  - 'kain': 271x (appears independently: 47x)
  - 'kaiin': 255x (appears independently: 70x)
  - 'keedy': 218x (appears independently: 30x)
  - 'key': 186x (appears independently: 33x)
  - 'kal': 179x (appears independently: 24x)
  - 'kedy': 170x (appears independently: 23x)
  - 'kar': 142x (appears independently: 55x)
  - 'l': 134x (appears independently: 131x)
  - 'ky': 133x (appears independently: 16x)
  - 'kol': 95x (appears independently: 33x)
  - 'kchy': 81x (appears independently: 33x)
  - 'taiin': 79x (appears independently: 44x)
  - 'ty': 79x (appears independently: 14x)
  - 'teey': 63x (appears independently: 28x)
  - 'tchy': 62x (appears independently: 24x)
  - 'tar': 62x (appears independently: 40x)
  - 'tedy': 62x (appears independently: 22x)
  - 'tain': 61x (appears independently: 13x)
  - 'tal': 60x (appears independently: 24x)

- qo- stems that also appear as independent words: 467/848 (55.1%)
  - Examples: epchy, tair, teor, keedain, eair, dair, lkshey, pol, kcheody, lcheedy, tolshy, lkeeey, keeam, lchy, kod

---

## Historical Verbose Cipher Comparison

### Alberti System Analysis
In Alberti's system (1467), the encipherer designated specific letters as nulls
that could be freely inserted anywhere. If Voynich 'y' is an Alberti-type null:
- 'y' appears in 17466 positions total
- But it strongly clusters at word-final (83.5%)
- **Verdict**: A true Alberti null would be uniformly distributed. The strong
  positional preference of 'y' suggests it is NOT a random null but has
  structural/grammatical function (suffix, case marker, etc.)

### Simonetta System Analysis
In Simonetta's cipher (Milan, 1474), null vowels were inserted between consonants
to make the ciphertext look like pronounceable words.
If Voynich vowels (a, o, e) are Simonetta-type nulls:
- Removing a/o/e leaves 23 unique chars
- Mean word length drops to 3.48
- Entropy changes to 3.6240 (from 3.8658)
- **Verdict**: Entropy decreased, which is consistent with null removal.
  However, removing 3 of the most common characters drastically reduces text.
  The remaining 'consonant-only' text would need to match a known consonantal
  writing system (Hebrew, Arabic) for this to be viable.

---

## Conclusions

### Key Findings

1. **Strip final -y**: Entropy -0.0367, MI +0.0314
   - Both metrics support -y as null. However, positional clustering
     at word-final suggests grammatical role rather than random padding.
   - After removal, word-final distribution becomes more diverse, which is
     consistent with unmasking a hidden suffix system.

2. **Strip qo- prefix**: Entropy -0.0470
   - 467/848 qo- stems appear as independent words
   - High overlap supports qo- as detachable prefix (article? determiner? null?)

3. **Strip gallows (k,t,p,f)**: Entropy -0.2576
   - Gallows are 10.6% of all characters
   - After removal: 22 unique chars remain

4. **Combined removal**: Entropy -0.3657, MI -0.0623
   - Alphabet size: 22 (from 26)
   - Best language match: Italian (5/20 bigram overlap)

### Overall Verdict

**PARTIALLY SUPPORTED**: The verbose cipher hypothesis shows some promise.
Null removal produces measurable improvements in at least two metrics.

However, the specific findings suggest:
- **-y** behaves more like a grammatical suffix than a random null
- **qo-** behaves like a detachable prefix (article/determiner)
- **Gallows** have strong positional preferences inconsistent with random nulls
- The Voynich text's anomalies are better explained by **agglutinative morphology**
  or a **constructed notation system** than by simple null insertion.
- If nulls exist, they are position-dependent (not freely insertable),
  which would represent a MORE sophisticated cipher than Alberti/Simonetta.
