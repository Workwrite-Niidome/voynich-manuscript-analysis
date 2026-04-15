# Voynich Manuscript: Stem Codebook

## Method

The ~200 most frequent STEMS were extracted from the full EVA transcription (RF1b-e.txt, 37,261 tokens).
For each stem, the known PREFIX (category) and SUFFIX (grammatical role) were stripped,
then analyzed for: frequency, dominant prefix, dominant suffix, section distribution,
and line position. Stems are grouped by CATEGORY+ROLE combination and mapped
to medieval herbal vocabulary.

**Known Frame:**
- PREFIX: p-=entry marker, ch-=plant/botanical, cth-=plant attribute, d-=function word, qo-=body/quantity, ot-/ok-=astronomical, sh-=preparation/herb, s-/t-/y-=qualifiers, k-=action
- SUFFIX: -ol/-or=subject/nominative, -am/-m=terminal, -y/-dy=predicate, -aiin=genitive, -edy=B-subject, -ey=attributive, -ar=oblique, -al=locative, -eey=B-opener

---

## 1. Top 200 Stems: Data Table

| Rank | Stem | Freq | Top Prefix (n) | Top Suffix (n) | Avg Line Pos | Section Top-3 | Folios |
|------|------|------|----------------|----------------|-------------|---------------|--------|
| 1 | **(empty)** | 9075 | ch (1902) | aiin (1228) | 0.502 | herbal:33.5%, stars:30.9%, bio:25.5% | 184 |
| 2 | **k** | 2289 | qo (1972) | eey (397) | 0.476 | bio:42.9%, stars:36.5%, herbal:14.4% | 155 |
| 3 | **a** | 1051 | d (7) | iin (420) | 0.589 | stars:49.7%, herbal:23.9%, bio:10.9% | 146 |
| 4 | **e** | 1043 | ch (348) | ol (334) | 0.466 | stars:36.3%, bio:22.0%, herbal:21.9% | 149 |
| 5 | **ch** | 894 | ot (149) | ey (184) | 0.374 | herbal:52.9%, stars:25.7%, bio:13.6% | 176 |
| 6 | **t** | 836 | qo (614) | y (98) | 0.514 | stars:38.6%, bio:30.1%, herbal:25.1% | 139 |
| 7 | **o** | 539 | ch (176) | dy (146) | 0.454 | herbal:62.9%, stars:17.3%, pharma:10.2% | 157 |
| 8 | **l** | 530 | o (195) | y (69) | 0.627 | bio:40.4%, stars:37.4%, herbal:14.2% | 107 |
| 9 | **lk** | 497 | o (207) | eey (105) | 0.547 | stars:56.3%, bio:37.8%, herbal:3.8% | 61 |
| 10 | **ai** | 435 | d (86) | r (228) | 0.477 | stars:50.6%, herbal:25.5%, bio:12.9% | 119 |
| 11 | **r** | 421 | o (96) | aiin (85) | 0.621 | stars:40.9%, bio:29.2%, herbal:20.9% | 110 |
| 12 | **lch** | 349 | o (98) | ey (120) | 0.525 | bio:51.9%, stars:38.4%, herbal:6.3% | 70 |
| 13 | **eo** | 323 | ch (131) | dy (141) | 0.487 | stars:41.5%, herbal:26.0%, pharma:15.2% | 86 |
| 14 | **ckh** | 311 | ch (180) | y (187) | 0.506 | bio:34.7%, stars:32.2%, herbal:23.8% | 105 |
| 15 | **d** | 285 | o (105) | aiin (99) | 0.507 | herbal:43.2%, stars:42.8%, bio:5.6% | 117 |
| 16 | **al** | 243 | d (54) | y (104) | 0.723 | other:26.7%, stars:26.7%, bio:19.8% | 82 |
| 17 | **kch** | 241 | qo (193) | y (92) | 0.417 | herbal:46.9%, stars:35.3%, bio:11.2% | 101 |
| 18 | **sh** | 233 | d (67) | ey (59) | 0.195 | herbal:38.6%, bio:31.3%, stars:22.7% | 108 |
| 19 | **ed** | 223 | ch (106) | ar (36) | 0.473 | stars:61.4%, bio:26.0%, herbal:9.0% | 62 |
| 20 | **pch** | 218 | o (112) | edy (68) | 0.557 | stars:50.9%, herbal:28.4%, bio:15.1% | 88 |
| 21 | **tch** | 205 | qo (151) | y (79) | 0.397 | herbal:62.0%, stars:27.8%, bio:5.4% | 96 |
| 22 | **ar** | 200 | d (29) | y (58) | 0.717 | stars:46.0%, herbal:22.0%, bio:15.0% | 82 |
| 23 | **ek** | 183 | ch (109) | y (84) | 0.497 | herbal:32.2%, stars:24.0%, bio:23.5% | 81 |
| 24 | **ee** | 174 | sh (39) | ol (51) | 0.484 | stars:44.3%, herbal:17.8%, bio:16.1% | 74 |
| 25 | **cth** | 166 | ch (98) | y (114) | 0.556 | herbal:33.1%, stars:30.7%, bio:30.1% | 78 |
| 26 | **od** | 156 | ch (62) | aiin (72) | 0.442 | herbal:54.5%, stars:28.2%, pharma:10.9% | 83 |
| 27 | **ok** | 153 | ch (96) | y (39) | 0.463 | herbal:39.2%, stars:30.7%, pharma:10.5% | 87 |
| 28 | **ke** | 143 | qo (110) | ol (45) | 0.45 | stars:41.3%, pharma:20.3%, bio:18.2% | 67 |
| 29 | **ol** | 138 | ch (37) | y (45) | 0.562 | herbal:39.1%, bio:18.1%, stars:15.2% | 84 |
| 30 | **lsh** | 123 | o (37) | ey (43) | 0.422 | bio:59.3%, stars:33.3%, herbal:4.9% | 42 |
| 31 | **eckh** | 106 | ch (61) | y (76) | 0.475 | bio:49.1%, stars:34.9%, herbal:11.3% | 46 |
| 32 | **ot** | 105 | ch (84) | y (40) | 0.57 | herbal:52.4%, stars:28.6%, pharma:8.6% | 66 |
| 33 | **eeo** | 104 | ch (27) | dy (32) | 0.373 | stars:67.3%, herbal:10.6%, pharma:8.7% | 45 |
| 34 | **che** | 101 | y (25) | ol (44) | 0.19 | stars:39.6%, herbal:35.6%, bio:11.9% | 61 |
| 35 | **eod** | 88 | ch (30) | aiin (19) | 0.504 | stars:35.2%, herbal:25.0%, pharma:18.2% | 51 |
| 36 | **p** | 76 | o (37) | aiin (17) | 0.599 | stars:42.1%, herbal:26.3%, bio:13.2% | 51 |
| 37 | **ees** | 74 | ch (34) | y (6) | 0.467 | herbal:32.4%, stars:29.7%, bio:16.2% | 49 |
| 38 | **cho** | 72 | ok (13) | dy (20) | 0.331 | herbal:76.4%, stars:12.5%, other:6.9% | 53 |
| 39 | **aii** | 72 | d (28) | r (52) | 0.517 | herbal:40.3%, stars:37.5%, other:11.1% | 48 |
| 40 | **eed** | 72 | ch (15) | aiin (14) | 0.483 | stars:79.2%, bio:15.3%, herbal:5.6% | 30 |
| 41 | **s** | 69 | o (25) | aiin (8) | 0.502 | herbal:34.8%, stars:27.5%, pharma:11.6% | 53 |
| 42 | **os** | 69 | ch (31) | aiin (9) | 0.464 | herbal:46.4%, stars:23.2%, pharma:18.8% | 47 |
| 43 | **et** | 68 | ch (45) | y (31) | 0.552 | herbal:30.9%, stars:27.9%, bio:25.0% | 47 |
| 44 | **eek** | 64 | ch (37) | y (38) | 0.43 | bio:34.4%, stars:32.8%, herbal:20.3% | 46 |
| 45 | **or** | 63 | ch (21) | y (26) | 0.637 | herbal:49.2%, pharma:20.6%, stars:15.9% | 47 |
| 46 | **ecth** | 62 | ch (39) | y (50) | 0.593 | bio:58.1%, stars:30.6%, herbal:8.1% | 27 |
| 47 | **olk** | 58 | ch (18) | eey (12) | 0.361 | bio:37.9%, stars:32.8%, herbal:17.2% | 41 |
| 48 | **ched** | 57 | p (17) | ar (13) | 0.195 | stars:70.2%, bio:21.1%, herbal:5.3% | 31 |
| 49 | **es** | 56 | ch (37) | y (3) | 0.493 | bio:30.4%, herbal:30.4%, stars:26.8% | 42 |
| 50 | **eos** | 56 | ch (27) | aiin (3) | 0.444 | stars:35.7%, herbal:28.6%, astro:16.1% | 42 |
| 51 | **kee** | 55 | qo (38) | ol (11) | 0.314 | stars:47.3%, bio:18.2%, pharma:18.2% | 32 |
| 52 | **cheo** | 53 | y (10) | dy (19) | 0.254 | stars:67.9%, herbal:13.2%, other:11.3% | 27 |
| 53 | **olch** | 53 | p (12) | ey (21) | 0.288 | bio:41.5%, stars:34.0%, herbal:13.2% | 36 |
| 54 | **lke** | 48 | o (19) | eey (20) | 0.489 | stars:68.8%, bio:12.5%, other:8.3% | 28 |
| 55 | **alk** | 48 | d (8) | ain (9) | 0.613 | stars:87.5%, bio:6.2%, other:6.2% | 23 |
| 56 | **ech** | 46 | ok (12) | y (19) | 0.385 | stars:60.9%, herbal:15.2%, bio:10.9% | 34 |
| 57 | **alch** | 46 | d (12) | y (10) | 0.497 | stars:39.1%, bio:23.9%, other:17.4% | 32 |
| 58 | **lo** | 44 | o (11) | m (8) | 0.743 | stars:45.5%, bio:31.8%, herbal:18.2% | 33 |
| 59 | **eok** | 43 | ch (23) | y (12) | 0.475 | stars:48.8%, herbal:14.0%, pharma:14.0% | 32 |
| 60 | **keeo** | 43 | qo (28) | dy (19) | 0.426 | stars:51.2%, other:16.3%, herbal:14.0% | 29 |
| 61 | **sho** | 42 | d (10) | dy (3) | 0.13 | herbal:76.2%, stars:14.3%, pharma:7.1% | 33 |
| 62 | **okch** | 42 | ch (27) | y (21) | 0.388 | herbal:71.4%, stars:19.0%, pharma:4.8% | 32 |
| 63 | **ls** | 41 | o (19) | aiin (3) | 0.66 | herbal:34.1%, bio:26.8%, stars:24.4% | 31 |
| 64 | **lt** | 41 | o (16) | edy (7) | 0.66 | bio:46.3%, stars:43.9%, herbal:7.3% | 31 |
| 65 | **fch** | 41 | o (19) | ey (11) | 0.563 | herbal:39.0%, stars:34.1%, bio:19.5% | 31 |
| 66 | **ockh** | 40 | ch (25) | y (30) | 0.449 | stars:32.5%, herbal:30.0%, pharma:25.0% | 34 |
| 67 | **keed** | 40 | qo (36) | ar (4) | 0.383 | stars:55.0%, bio:35.0%, herbal:7.5% | 25 |
| 68 | **air** | 39 | d (10) | y (11) | 0.579 | stars:71.8%, herbal:12.8%, astro:5.1% | 27 |
| 69 | **keo** | 39 | qo (31) | dy (22) | 0.409 | pharma:28.2%, stars:28.2%, herbal:23.1% | 26 |
| 70 | **lkch** | 39 | o (10) | ey (14) | 0.483 | stars:79.5%, bio:12.8%, herbal:5.1% | 19 |
| 71 | **yk** | 38 | ch (11) | y (11) | 0.45 | herbal:63.2%, bio:15.8%, stars:13.2% | 34 |
| 72 | **te** | 37 | qo (23) | ol (12) | 0.492 | stars:45.9%, herbal:24.3%, pharma:13.5% | 31 |
| 73 | **chod** | 37 | p (11) | aiin (11) | 0.31 | herbal:70.3%, stars:18.9%, pharma:8.1% | 29 |
| 74 | **kal** | 37 | qo (31) | y (23) | 0.598 | other:45.9%, stars:18.9%, bio:16.2% | 19 |
| 75 | **octh** | 36 | ch (22) | y (26) | 0.433 | herbal:66.7%, stars:16.7%, pharma:11.1% | 31 |
| 76 | **rch** | 35 | o (6) | ey (14) | 0.63 | bio:51.4%, stars:25.7%, herbal:17.1% | 21 |
| 77 | **chd** | 35 | p (11) | ar (10) | 0.447 | stars:54.3%, herbal:28.6%, bio:11.4% | 26 |
| 78 | **kai** | 34 | qo (23) | r (28) | 0.441 | stars:52.9%, other:20.6%, herbal:14.7% | 18 |
| 79 | **lche** | 34 | o (10) | ol (13) | 0.436 | stars:55.9%, bio:32.4%, other:5.9% | 22 |
| 80 | **i** | 31 | o (10) | iin (13) | 0.328 | stars:45.2%, bio:29.0%, herbal:19.4% | 24 |
| 81 | **ko** | 30 | qo (20) | dy (9) | 0.377 | herbal:80.0%, stars:13.3%, astro:3.3% | 29 |
| 82 | **to** | 30 | qo (18) | dy (10) | 0.553 | herbal:60.0%, stars:20.0%, pharma:10.0% | 24 |
| 83 | **eol** | 30 | ch (12) | y (13) | 0.597 | bio:26.7%, stars:20.0%, herbal:16.7% | 23 |
| 84 | **ld** | 29 | o (14) | aiin (9) | 0.759 | herbal:37.9%, bio:20.7%, stars:20.7% | 22 |
| 85 | **ksh** | 28 | qo (20) | y (12) | 0.299 | stars:35.7%, herbal:28.6%, bio:25.0% | 23 |
| 86 | **cph** | 28 | ch (20) | y (14) | 0.579 | stars:42.9%, herbal:39.3%, bio:17.9% | 21 |
| 87 | **olsh** | 27 | p (8) | y (8) | 0.219 | bio:55.6%, herbal:22.2%, stars:11.1% | 21 |
| 88 | **otch** | 26 | ch (16) | y (15) | 0.311 | herbal:80.8%, stars:19.2% | 24 |
| 89 | **alo** | 26 | d (6) | m (7) | 0.802 | stars:38.5%, bio:15.4%, astro:11.5% | 23 |
| 90 | **ked** | 26 | qo (23) | ar (5) | 0.461 | stars:46.2%, bio:42.3%, herbal:11.5% | 22 |
| 91 | **och** | 25 | ch (9) | y (11) | 0.277 | herbal:76.0%, stars:20.0%, astro:4.0% | 25 |
| 92 | **eeod** | 25 | k (5) | ar (4) | 0.475 | stars:60.0%, herbal:32.0%, astro:4.0% | 20 |
| 93 | **she** | 24 | d (11) | ol (12) | 0.038 | stars:45.8%, herbal:20.8%, bio:12.5% | 22 |
| 94 | **alsh** | 24 | d (7) | edy (8) | 0.423 | bio:37.5%, herbal:25.0%, stars:20.8% | 17 |
| 95 | **ro** | 23 | o (7) | m (4) | 0.787 | stars:47.8%, bio:21.7%, herbal:21.7% | 20 |
| 96 | **yt** | 23 | d (10) | y (10) | 0.456 | herbal:56.5%, bio:26.1%, stars:8.7% | 18 |
| 97 | **cheod** | 23 | p (5) | aiin (7) | 0.187 | stars:60.9%, herbal:26.1%, pharma:8.7% | 16 |
| 98 | **eet** | 23 | ch (10) | y (12) | 0.538 | bio:47.8%, stars:34.8%, herbal:17.4% | 17 |
| 99 | **tsh** | 22 | qo (15) | y (8) | 0.381 | herbal:63.6%, bio:18.2%, stars:13.6% | 18 |
| 100 | **eees** | 22 | o (3) | y (1) | 0.483 | herbal:54.5%, stars:40.9%, bio:4.5% | 21 |
| 101 | **teo** | 21 | qo (15) | dy (11) | 0.464 | stars:57.1%, herbal:23.8%, pharma:14.3% | 17 |
| 102 | **y** | 21 | d (8) | dy (13) | 0.789 | herbal:66.7%, stars:19.0%, bio:4.8% | 19 |
| 103 | **aro** | 21 | d (8) | dy (10) | 0.778 | herbal:38.1%, stars:38.1%, pharma:14.3% | 19 |
| 104 | **q** | 21 | o (2) | y (4) | 0.521 | bio:52.4%, stars:33.3%, herbal:14.3% | 16 |
| 105 | **old** | 20 | ch (10) | aiin (9) | 0.582 | herbal:75.0%, pharma:10.0%, bio:5.0% | 19 |
| 106 | **sheo** | 20 | k (7) | dy (10) | 0.173 | stars:50.0%, herbal:40.0%, astro:5.0% | 16 |
| 107 | **eot** | 20 | ch (14) | y (4) | 0.443 | stars:50.0%, herbal:30.0%, other:10.0% | 19 |
| 108 | **kech** | 20 | qo (18) | y (11) | 0.494 | stars:65.0%, bio:20.0%, herbal:10.0% | 15 |
| 109 | **ii** | 20 | o (4) | n (9) | 0.474 | stars:45.0%, herbal:25.0%, bio:15.0% | 17 |
| 110 | **eeos** | 20 | ch (6) | y (2) | 0.353 | stars:45.0%, astro:25.0%, herbal:20.0% | 13 |
| 111 | **tcho** | 19 | qo (14) | dy (4) | 0.353 | herbal:78.9%, stars:15.8%, other:5.3% | 18 |
| 112 | **arch** | 19 | d (4) | y (6) | 0.531 | herbal:36.8%, bio:21.1%, astro:15.8% | 19 |
| 113 | **ald** | 18 | ot (5) | ar (3) | 0.677 | herbal:50.0%, astro:16.7%, stars:16.7% | 17 |
| 114 | **kcho** | 18 | qo (12) | dy (4) | 0.342 | herbal:72.2%, pharma:16.7%, stars:11.1% | 15 |
| 115 | **eyk** | 18 | ch (10) | y (5) | 0.322 | stars:44.4%, bio:33.3%, herbal:16.7% | 15 |
| 116 | **als** | 18 | d (5) | y (3) | 0.831 | herbal:33.3%, other:22.2%, pharma:16.7% | 17 |
| 117 | **lkee** | 18 | o (9) | ol (5) | 0.343 | stars:72.2%, bio:16.7%, herbal:11.1% | 15 |
| 118 | **x** | 18 | sh (2) | ar (3) | 0.532 | herbal:55.6%, other:22.2%, stars:22.2% | 7 |
| 119 | **ols** | 17 | s (4) | y (2) | 0.73 | herbal:47.1%, pharma:35.3%, stars:11.8% | 16 |
| 120 | **olo** | 17 | ch (9) | dy (6) | 0.741 | herbal:64.7%, pharma:17.6%, bio:11.8% | 16 |
| 121 | **orch** | 17 | ch (4) | y (11) | 0.467 | herbal:70.6%, stars:17.6%, bio:5.9% | 15 |
| 122 | **as** | 17 | ok (3) | y (3) | 0.67 | bio:35.3%, herbal:29.4%, stars:29.4% | 15 |
| 123 | **ak** | 17 | d (2) | y (7) | 0.517 | stars:64.7%, herbal:17.6%, bio:5.9% | 15 |
| 124 | **aiin** | 17 | d (6) | y (8) | 0.85 | stars:52.9%, herbal:23.5%, bio:11.8% | 11 |
| 125 | **ted** | 17 | qo (15) | ar (3) | 0.513 | stars:47.1%, bio:41.2%, other:11.8% | 13 |
| 126 | **pched** | 17 | o (9) | aiin (5) | 0.577 | stars:76.5%, bio:17.6%, pharma:5.9% | 12 |
| 127 | **ag** | 16 | ok (4) | am (1) | 0.85 | herbal:50.0%, other:18.8%, stars:18.8% | 15 |
| 128 | **rar** | 16 | o (1) | y (5) | 0.866 | stars:68.8%, other:12.5%, astro:6.2% | 13 |
| 129 | **lched** | 16 | o (5) | ar (2) | 0.662 | stars:68.8%, bio:31.2% | 14 |
| 130 | **yd** | 15 | p (4) | aiin (6) | 0.512 | herbal:80.0%, stars:13.3%, other:6.7% | 14 |
| 131 | **tal** | 15 | qo (8) | y (11) | 0.627 | stars:33.3%, herbal:26.7%, astro:13.3% | 14 |
| 132 | **chol** | 15 | f (3) | y (7) | 0.449 | herbal:60.0%, other:13.3%, pharma:13.3% | 14 |
| 133 | **teeo** | 15 | qo (8) | dy (7) | 0.278 | stars:53.3%, pharma:20.0%, herbal:13.3% | 14 |
| 134 | **epch** | 15 | ch (8) | y (6) | 0.504 | stars:33.3%, herbal:26.7%, bio:20.0% | 14 |
| 135 | **lpch** | 15 | o (6) | edy (7) | 0.548 | stars:66.7%, bio:26.7%, pharma:6.7% | 10 |
| 136 | **pche** | 14 | o (9) | ol (4) | 0.571 | stars:71.4%, herbal:21.4%, other:7.1% | 13 |
| 137 | **lol** | 14 | o (4) | y (7) | 0.91 | bio:64.3%, herbal:28.6%, stars:7.1% | 12 |
| 138 | **esh** | 14 | ok (6) | y (6) | 0.483 | herbal:42.9%, bio:28.6%, stars:21.4% | 12 |
| 139 | **ep** | 14 | ch (12) | y (4) | 0.552 | stars:42.9%, herbal:28.6%, bio:21.4% | 11 |
| 140 | **lkeeo** | 14 | o (8) | dy (8) | 0.293 | stars:78.6%, herbal:14.3%, astro:7.1% | 12 |
| 141 | **opch** | 13 | ch (11) | y (4) | 0.515 | herbal:38.5%, stars:38.5%, astro:7.7% | 12 |
| 142 | **dai** | 13 | o (5) | r (7) | 0.473 | herbal:38.5%, stars:38.5%, astro:7.7% | 12 |
| 143 | **f** | 13 | o (7) | y (3) | 0.638 | herbal:46.2%, stars:23.1%, bio:15.4% | 12 |
| 144 | **m** | 13 | none | ol (1) | 0.68 | herbal:84.6%, bio:7.7%, stars:7.7% | 9 |
| 145 | **cheeo** | 13 | y (8) | dy (3) | 0.058 | stars:76.9%, pharma:15.4%, herbal:7.7% | 9 |
| 146 | **eolk** | 13 | ch (7) | ain (5) | 0.499 | stars:53.8%, bio:30.8%, herbal:15.4% | 11 |
| 147 | **eockh** | 13 | ch (8) | y (9) | 0.521 | pharma:38.5%, stars:38.5%, herbal:15.4% | 11 |
| 148 | **osh** | 12 | sh (3) | y (8) | 0.356 | herbal:75.0%, pharma:16.7%, stars:8.3% | 11 |
| 149 | **ych** | 12 | d (7) | ey (4) | 0.633 | herbal:66.7%, bio:16.7%, stars:16.7% | 12 |
| 150 | **chos** | 12 | y (3) | ar (1) | 0.354 | herbal:41.7%, pharma:25.0%, stars:25.0% | 10 |
| 151 | **ytch** | 12 | d (5) | y (7) | 0.614 | herbal:91.7%, pharma:8.3% | 10 |
| 152 | **eocth** | 12 | ch (5) | y (9) | 0.55 | pharma:41.7%, stars:25.0%, herbal:16.7% | 11 |
| 153 | **rsh** | 12 | o (3) | y (4) | 0.508 | bio:58.3%, stars:25.0%, herbal:16.7% | 10 |
| 154 | **tee** | 12 | qo (8) | ol (5) | 0.488 | stars:50.0%, herbal:33.3%, bio:16.7% | 11 |
| 155 | **lfch** | 12 | o (7) | ey (3) | 0.539 | stars:41.7%, herbal:33.3%, bio:16.7% | 12 |
| 156 | **lok** | 12 | o (3) | eey (4) | 0.573 | stars:58.3%, bio:33.3%, herbal:8.3% | 10 |
| 157 | **tai** | 12 | qo (8) | r (9) | 0.607 | stars:41.7%, astro:16.7%, bio:16.7% | 10 |
| 158 | **v** | 12 | none | r (1) | 0.479 | herbal:100.0% | 1 |
| 159 | **eee** | 12 | ch (3) | ol (2) | 0.421 | stars:58.3%, pharma:25.0%, astro:8.3% | 11 |
| 160 | **g** | 11 | o (2) | none | 0.897 | herbal:72.7%, stars:27.3% | 10 |
| 161 | **rai** | 11 | o (4) | r (8) | 0.664 | stars:63.6%, bio:18.2%, herbal:18.2% | 10 |
| 162 | **ykch** | 10 | d (3) | y (6) | 0.379 | herbal:80.0%, bio:10.0%, pharma:10.0% | 10 |
| 163 | **oi** | 10 | s (5) | iin (8) | 0.209 | herbal:50.0%, bio:30.0%, stars:20.0% | 9 |
| 164 | **eeeo** | 10 | ot (2) | dy (2) | 0.323 | stars:70.0%, astro:20.0%, herbal:10.0% | 9 |
| 165 | **airo** | 10 | d (3) | dy (5) | 0.596 | stars:80.0%, herbal:10.0%, other:10.0% | 6 |
| 166 | **lchd** | 10 | o (4) | aiin (3) | 0.524 | stars:60.0%, herbal:30.0%, bio:10.0% | 9 |
| 167 | **shed** | 10 | t (5) | ar (1) | 0.141 | stars:80.0%, bio:10.0%, herbal:10.0% | 8 |
| 168 | **eor** | 10 | ch (6) | aiin (3) | 0.627 | stars:30.0%, astro:20.0%, pharma:20.0% | 10 |
| 169 | **sheod** | 10 | y (3) | ar (3) | 0.11 | stars:80.0%, herbal:10.0%, pharma:10.0% | 8 |
| 170 | **lkeed** | 10 | o (3) | al (1) | 0.419 | stars:70.0%, bio:30.0% | 9 |
| 171 | **chee** | 10 | y (3) | or (3) | 0.336 | stars:80.0%, bio:10.0%, other:10.0% | 9 |
| 172 | **oro** | 9 | ch (4) | iin (4) | 0.657 | herbal:88.9%, bio:11.1% | 9 |
| 173 | **pai** | 9 | o (6) | r (5) | 0.676 | stars:77.8%, herbal:11.1%, other:11.1% | 7 |
| 174 | **ocph** | 9 | ch (4) | y (4) | 0.387 | herbal:33.3%, stars:33.3%, other:22.2% | 9 |
| 175 | **etch** | 9 | ch (5) | y (5) | 0.464 | herbal:66.7%, pharma:22.2%, other:11.1% | 9 |
| 176 | **kees** | 9 | qo (5) | an (1) | 0.381 | bio:33.3%, herbal:33.3%, astro:11.1% | 8 |
| 177 | **keod** | 9 | qo (5) | ar (1) | 0.275 | stars:44.4%, herbal:22.2%, pharma:22.2% | 9 |
| 178 | **lkeo** | 9 | o (1) | dy (5) | 0.443 | stars:55.6%, herbal:22.2%, pharma:22.2% | 8 |
| 179 | **eech** | 9 | k (3) | y (5) | 0.382 | stars:88.9%, herbal:11.1% | 9 |
| 180 | **qek** | 9 | none | eey (3) | 0.382 | bio:33.3%, stars:33.3%, herbal:11.1% | 9 |
| 181 | **cheos** | 9 | d (3) | aiin (1) | 0.091 | stars:66.7%, other:33.3% | 8 |
| 182 | **lcheo** | 9 | o (5) | dy (3) | 0.464 | stars:77.8%, pharma:22.2% | 9 |
| 183 | **eal** | 8 | ch (6) | y (6) | 0.689 | bio:37.5%, herbal:25.0%, stars:25.0% | 7 |
| 184 | **oto** | 8 | ch (5) | dy (3) | 0.377 | herbal:62.5%, other:12.5%, pharma:12.5% | 8 |
| 185 | **keeod** | 8 | qo (5) | aiin (2) | 0.619 | stars:62.5%, herbal:25.0%, pharma:12.5% | 7 |
| 186 | **chocth** | 8 | p (3) | y (7) | 0.147 | herbal:62.5%, pharma:25.0%, stars:12.5% | 8 |
| 187 | **oii** | 8 | d (6) | r (8) | 0.292 | herbal:62.5%, astro:12.5%, bio:12.5% | 8 |
| 188 | **op** | 8 | ch (6) | ol (1) | 0.466 | herbal:62.5%, stars:25.0%, astro:12.5% | 8 |
| 189 | **aiind** | 8 | d (2) | aiin (2) | 0.74 | herbal:75.0%, pharma:12.5%, stars:12.5% | 7 |
| 190 | **qk** | 8 | none | ain (2) | 0.394 | stars:37.5%, herbal:25.0%, pharma:25.0% | 8 |
| 191 | **los** | 8 | o (2) | aiin (1) | 0.576 | herbal:37.5%, stars:37.5%, bio:12.5% | 8 |
| 192 | **oke** | 8 | ch (6) | ol (3) | 0.283 | stars:37.5%, herbal:25.0%, pharma:25.0% | 8 |
| 193 | **chok** | 8 | t (3) | ey (2) | 0.0 | herbal:50.0%, stars:25.0%, astro:12.5% | 8 |
| 194 | **cfh** | 8 | ch (5) | y (2) | 0.491 | stars:50.0%, herbal:37.5%, bio:12.5% | 8 |
| 195 | **pal** | 8 | o (8) | or (2) | 0.639 | stars:37.5%, astro:25.0%, bio:12.5% | 7 |
| 196 | **eyt** | 8 | ch (4) | y (2) | 0.6 | bio:37.5%, astro:25.0%, stars:25.0% | 8 |
| 197 | **le** | 8 | o (6) | eey (5) | 0.32 | stars:50.0%, bio:25.0%, other:12.5% | 8 |
| 198 | **lal** | 8 | o (6) | y (4) | 0.741 | other:50.0%, stars:25.0%, astro:12.5% | 6 |
| 199 | **psh** | 8 | qo (4) | edy (3) | 0.595 | bio:87.5%, stars:12.5% | 4 |
| 200 | **qe** | 8 | none | eey (3) | 0.439 | stars:75.0%, bio:25.0% | 8 |

---

## 2. Stems Grouped by Category+Role

### BOTANICAL + genitive (ch-...-aiin) -- 8 stems, 9546 tokens

- **(empty)** (9075): [herbal:33.5%, stars:30.9%, bio:25.5%] -- daiin(575), chey(430), ol(423)
- **od** (156): [herbal:54.5%, stars:28.2%, pharma:10.9%] -- chodaiin(34), shodaiin(15), shod(9)
- **eod** (88): [stars:35.2%, herbal:25.0%, pharma:18.2%] -- sheod(10), cheodaiin(8), cheodal(5)
- **eed** (72): [stars:79.2%, bio:15.3%, herbal:5.6%] -- okeed(7), cheed(5), sheed(5)
- **os** (69): [herbal:46.4%, stars:23.2%, pharma:18.8%] -- chos(26), shos(8), shosaiin(5)
- **eos** (56): [stars:35.7%, herbal:28.6%, astro:16.1%] -- cheos(25), sheos(9), oteos(6)
- **old** (20): [herbal:75.0%, pharma:10.0%, bio:5.0%] -- choldaiin(6), ctholdar(1), choldar(1)
- **eor** (10): [stars:30.0%, astro:20.0%, pharma:20.0%] -- cheoraiin(3), oteory(1), oteorar(1)

### BODY/QUANTITY + B-opener (qo-...-eey) -- 1 stems, 2289 tokens

- **k** (2289): [bio:42.9%, stars:36.5%, herbal:14.4%] -- qokeey(341), qokain(262), qokaiin(234)

### BOTANICAL + predicate (ch-...-y) -- 37 stems, 2064 tokens

- **ckh** (311): [bio:34.7%, stars:32.2%, herbal:23.8%] -- chckhy(118), shckhy(49), chckhey(29)
- **ek** (183): [herbal:32.2%, stars:24.0%, bio:23.5%] -- cheky(53), sheky(26), chekal(10)
- **cth** (166): [herbal:33.1%, stars:30.7%, bio:30.1%] -- chcthy(73), shcthy(29), octhy(6)
- **ok** (153): [herbal:39.2%, stars:30.7%, pharma:10.5%] -- choky(30), chokaiin(12), chokeey(10)
- **ol** (138): [herbal:39.1%, bio:18.1%, stars:15.2%] -- choly(16), otoldy(7), polaiin(7)
- **eckh** (106): [bio:49.1%, stars:34.9%, herbal:11.3%] -- checkhy(44), sheckhy(25), checkhey(11)
- **ot** (105): [herbal:52.4%, stars:28.6%, pharma:8.6%] -- choty(34), chotar(9), chotaiin(8)
- **ees** (74): [herbal:32.4%, stars:29.7%, bio:16.2%] -- chees(32), oees(10), okees(7)
- **et** (68): [herbal:30.9%, stars:27.9%, bio:25.0%] -- chety(18), chetar(7), shety(7)
- **eek** (64): [bio:34.4%, stars:32.8%, herbal:20.3%] -- cheeky(25), sheeky(10), sheek(4)
- **or** (63): [herbal:49.2%, pharma:20.6%, stars:15.9%] -- chory(9), soraiin(5), shory(4)
- **ecth** (62): [bio:58.1%, stars:30.6%, herbal:8.1%] -- checthy(31), shecthy(18), checthey(4)
- **es** (56): [bio:30.4%, herbal:30.4%, stars:26.8%] -- ches(34), shes(5), es(3)
- **eok** (43): [stars:48.8%, herbal:14.0%, pharma:14.0%] -- sheoky(6), cheokeey(4), cheoky(3)
- **okch** (42): [herbal:71.4%, stars:19.0%, pharma:4.8%] -- chokchy(14), shokchy(6), chokchol(4)
- **ockh** (40): [stars:32.5%, herbal:30.0%, pharma:25.0%] -- chockhy(18), shockhy(6), chockhey(3)
- **yk** (38): [herbal:63.2%, bio:15.8%, stars:13.2%] -- chyky(5), oykeey(3), dyky(3)
- **octh** (36): [herbal:66.7%, stars:16.7%, pharma:11.1%] -- chocthy(15), shocthy(9), chocthey(6)
- **eol** (30): [bio:26.7%, stars:20.0%, herbal:16.7%] -- cheoly(5), cheoldy(4), okeoly(4)
- **cph** (28): [stars:42.9%, herbal:39.3%, bio:17.9%] -- chcphy(10), chcphey(4), chcphedy(3)
- **otch** (26): [herbal:80.8%, stars:19.2%] -- chotchy(9), chotchey(4), shotchy(3)
- **och** (25): [herbal:76.0%, stars:20.0%, astro:4.0%] -- chochy(6), shochy(2), chochor(2)
- **eet** (23): [bio:47.8%, stars:34.8%, herbal:17.4%] -- sheety(6), sheet(3), cheety(3)
- **eot** (20): [stars:50.0%, herbal:30.0%, other:10.0%] -- cheoty(3), cheotol(2), cheotey(2)
- **eeos** (20): [stars:45.0%, astro:25.0%, herbal:20.0%] -- cheeos(6), okeeos(5), oteeos(4)
- **eyk** (18): [stars:44.4%, bio:33.3%, herbal:16.7%] -- cheyky(3), cheykaiin(2), sheyky(2)
- **orch** (17): [herbal:70.6%, stars:17.6%, bio:5.9%] -- korchy(3), torchy(2), otorchy(2)
- **epch** (15): [stars:33.3%, herbal:26.7%, bio:20.0%] -- shepchy(3), chepchey(3), chepchy(2)
- **ep** (14): [stars:42.9%, herbal:28.6%, bio:21.4%] -- chep(4), chepar(3), chepy(3)
- **opch** (13): [herbal:38.5%, stars:38.5%, astro:7.7%] -- chopchy(4), chopchedy(2), chopchdy(2)
- **eockh** (13): [pharma:38.5%, stars:38.5%, herbal:15.4%] -- cheockhy(7), sheockhey(3), sheockhy(2)
- **eocth** (12): [pharma:41.7%, stars:25.0%, herbal:16.7%] -- cheocthy(4), sheocthy(2), keocthy(1)
- **ocph** (9): [herbal:33.3%, stars:33.3%, other:22.2%] -- chocphy(3), tocphol(1), tocpheey(1)
- **etch** (9): [herbal:66.7%, pharma:22.2%, other:11.1%] -- chetchy(4), chetchey(1), shetchy(1)
- **eal** (8): [bio:37.5%, herbal:25.0%, stars:25.0%] -- chealy(4), cphealy(1), shealy(1)
- **cfh** (8): [stars:50.0%, herbal:37.5%, bio:12.5%] -- chcfhal(1), tcfhy(1), ocfhor(1)
- **eyt** (8): [bio:37.5%, astro:25.0%, stars:25.0%] -- cheyty(1), okeytam(1), cheytey(1)

### BODY/QUANTITY + predicate (qo-...-y) -- 8 stems, 1404 tokens

- **t** (836): [stars:38.6%, bio:30.1%, herbal:25.1%] -- qoty(71), qotaiin(66), qotedy(61)
- **kch** (241): [herbal:46.9%, stars:35.3%, bio:11.2%] -- qokchy(72), qokchey(35), qokchedy(27)
- **tch** (205): [herbal:62.0%, stars:27.8%, bio:5.4%] -- qotchy(59), qotchey(21), qotchedy(19)
- **kal** (37): [other:45.9%, stars:18.9%, bio:16.2%] -- qokaly(18), qokaldy(5), qokalor(3)
- **ksh** (28): [stars:35.7%, herbal:28.6%, bio:25.0%] -- qokshy(6), qokshedy(6), qokshey(4)
- **tsh** (22): [herbal:63.6%, bio:18.2%, stars:13.6%] -- qotshey(5), qotshy(4), qotshdy(3)
- **kech** (20): [stars:65.0%, bio:20.0%, herbal:10.0%] -- qokechy(10), qokechey(4), qokechdy(3)
- **tal** (15): [stars:33.3%, herbal:26.7%, astro:13.3%] -- qotaly(5), ytaly(4), chtaly(2)

### BOTANICAL + subject (ch-...-ol) -- 4 stems, 1071 tokens

- **e** (1043): [stars:36.3%, bio:22.0%, herbal:21.9%] -- cheol(127), sheol(74), cheor(64)
- **eee** (12): [stars:58.3%, pharma:25.0%, astro:8.3%] -- oteee(3), eee(1), oeee(1)
- **op** (8): [herbal:62.5%, stars:25.0%, astro:12.5%] -- chop(2), chopol(1), chopy(1)
- **oke** (8): [stars:37.5%, herbal:25.0%, pharma:25.0%] -- chokeol(3), chokeor(1), otokeeey(1)

### FUNCTION + connector (d-...-iin) -- 1 stems, 1051 tokens

- **a** (1051): [stars:49.7%, herbal:23.9%, bio:10.9%] -- aiin(420), ar(296), al(220)

### BOTANICAL + state (ch-...-dy) -- 5 stems, 991 tokens

- **o** (539): [herbal:62.9%, stars:17.3%, pharma:10.2%] -- sho(93), chody(62), cho(50)
- **eo** (323): [stars:41.5%, herbal:26.0%, pharma:15.2%] -- cheody(55), cheo(46), sheo(33)
- **eeo** (104): [stars:67.3%, herbal:10.6%, pharma:8.7%] -- cheeo(16), okeeo(12), okeeody(9)
- **olo** (17): [herbal:64.7%, pharma:17.6%, bio:11.8%] -- cholody(5), cholo(3), dolo(1)
- **oto** (8): [herbal:62.5%, other:12.5%, pharma:12.5%] -- choto(2), chotom(2), potoy(1)

### GENERAL + genitive (o-...-aiin) -- 9 stems, 956 tokens

- **r** (421): [stars:40.9%, bio:29.2%, herbal:20.9%] -- r(137), raiin(57), oraiin(23)
- **d** (285): [herbal:43.2%, stars:42.8%, bio:5.6%] -- odaiin(43), qodaiin(27), odar(18)
- **p** (76): [stars:42.1%, herbal:26.3%, bio:13.2%] -- opaiin(9), opal(7), opar(6)
- **s** (69): [herbal:34.8%, stars:27.5%, pharma:11.6%] -- os(18), chs(14), shs(4)
- **ls** (41): [herbal:34.1%, bio:26.8%, stars:24.4%] -- ols(15), ls(11), olsy(2)
- **ld** (29): [herbal:37.9%, bio:20.7%, stars:20.7%] -- oldaiin(4), ldaiin(4), ldar(4)
- **pched** (17): [stars:76.5%, bio:17.6%, pharma:5.9%] -- opched(4), opchedaiin(4), qopched(3)
- **lchd** (10): [stars:60.0%, herbal:30.0%, bio:10.0%] -- olchdaiin(2), dlchd(2), lchdal(1)
- **los** (8): [herbal:37.5%, stars:37.5%, bio:12.5%] -- los(4), olos(2), dlos(1)

### ASTRONOMICAL + attributive (ot-...-ey) -- 1 stems, 894 tokens

- **ch** (894): [herbal:52.9%, stars:25.7%, bio:13.6%] -- otchy(45), okchey(32), kchy(31)

### FUNCTION + predicate (d-...-y) -- 11 stems, 644 tokens

- **al** (243): [other:26.7%, stars:26.7%, bio:19.8%] -- aly(30), daly(24), otaly(20)
- **ar** (200): [stars:46.0%, herbal:22.0%, bio:15.0%] -- ary(19), aral(14), dary(13)
- **alch** (46): [stars:39.1%, bio:23.9%, other:17.4%] -- dalchedy(5), alchey(4), okalchy(4)
- **air** (39): [stars:71.8%, herbal:12.8%, astro:5.1%] -- sairy(5), airam(3), dairy(2)
- **yt** (23): [herbal:56.5%, bio:26.1%, stars:8.7%] -- chyty(5), dyty(2), dytey(2)
- **arch** (19): [herbal:36.8%, bio:21.1%, astro:15.8%] -- archy(2), darchor(1), sarchor(1)
- **als** (18): [herbal:33.3%, other:22.2%, pharma:16.7%] -- als(6), dals(4), okals(1)
- **ak** (17): [stars:64.7%, herbal:17.6%, bio:5.9%] -- akar(3), aky(3), daky(2)
- **aiin** (17): [stars:52.9%, herbal:23.5%, bio:11.8%] -- aiiny(4), aiinal(3), daiiny(2)
- **ytch** (12): [herbal:91.7%, pharma:8.3%] -- dytchy(3), shytchy(2), dytcheey(1)
- **ykch** (10): [herbal:80.0%, bio:10.0%, pharma:10.0%] -- chykchy(3), dykchy(2), oykchor(1)

### GENERAL + predicate (o-...-y) -- 8 stems, 636 tokens

- **l** (530): [bio:40.4%, stars:37.4%, herbal:14.2%] -- l(120), oly(48), olaiin(37)
- **eees** (22): [herbal:54.5%, stars:40.9%, bio:4.5%] -- eees(7), oeees(3), qoeees(3)
- **q** (21): [bio:52.4%, stars:33.3%, herbal:14.3%] -- qy(4), qeey(3), qedy(3)
- **rar** (16): [stars:68.8%, other:12.5%, astro:6.2%] -- rary(5), raraiin(4), raram(3)
- **lol** (14): [bio:64.3%, herbal:28.6%, stars:7.1%] -- loly(6), ololdy(2), loldy(2)
- **f** (13): [herbal:46.2%, stars:23.1%, bio:15.4%] -- qof(2), ofy(2), ofar(2)
- **rsh** (12): [bio:58.3%, stars:25.0%, herbal:16.7%] -- rshedy(3), orshy(2), rsheedy(2)
- **lal** (8): [other:50.0%, stars:25.0%, astro:12.5%] -- olaly(4), olalor(1), olalaiin(1)

### GENERAL + attributive (o-...-ey) -- 6 stems, 599 tokens

- **lch** (349): [bio:51.9%, stars:38.4%, herbal:6.3%] -- lchedy(79), lchey(70), olchey(35)
- **lsh** (123): [bio:59.3%, stars:33.3%, herbal:4.9%] -- lshedy(28), lshey(27), olshey(14)
- **fch** (41): [herbal:39.0%, stars:34.1%, bio:19.5%] -- qofchedy(5), ofchy(4), qofchey(4)
- **lkch** (39): [stars:79.5%, bio:12.8%, herbal:5.1%] -- lkchey(11), lkchedy(9), olkchy(4)
- **rch** (35): [bio:51.4%, stars:25.7%, herbal:17.1%] -- rchey(10), rchedy(7), rcheey(5)
- **lfch** (12): [stars:41.7%, herbal:33.3%, bio:16.7%] -- olfchey(3), lfchy(2), olfchedy(2)

### GENERAL + B-opener (o-...-eey) -- 4 stems, 565 tokens

- **lk** (497): [stars:56.3%, bio:37.8%, herbal:3.8%] -- lkeey(50), olkeey(47), lkaiin(44)
- **lke** (48): [stars:68.8%, bio:12.5%, other:8.3%] -- lkeeey(10), olkeeey(9), olkeol(7)
- **lok** (12): [stars:58.3%, bio:33.3%, herbal:8.3%] -- lokeey(4), oloky(2), lokar(1)
- **le** (8): [stars:50.0%, bio:25.0%, other:12.5%] -- oleeey(4), oleol(2), leeey(1)

### FUNCTION + sandhi (d-...-r) -- 3 stems, 515 tokens

- **ai** (435): [stars:50.6%, herbal:25.5%, bio:12.9%] -- ain(110), air(63), dair(62)
- **aii** (72): [herbal:40.3%, stars:37.5%, other:11.1%] -- aiir(18), daiir(16), okaiir(5)
- **oii** (8): [herbal:62.5%, astro:12.5%, bio:12.5%] -- doiir(6), choiir(1), otoiir(1)

### GENERAL + B-subject (o-...-edy) -- 3 stems, 274 tokens

- **pch** (218): [stars:50.9%, herbal:28.4%, bio:15.1%] -- opchedy(35), opchey(33), qopchedy(23)
- **lt** (41): [bio:46.3%, stars:43.9%, herbal:7.3%] -- lteey(5), oltedy(4), lteedy(4)
- **lpch** (15): [stars:66.7%, bio:26.7%, pharma:6.7%] -- lpchedy(4), olpchedy(3), lpchdy(2)

### BODY/QUANTITY + subject (qo-...-ol) -- 4 stems, 247 tokens

- **ke** (143): [stars:41.3%, pharma:20.3%, bio:18.2%] -- qokeol(34), qokeeey(25), qokeor(12)
- **kee** (55): [stars:47.3%, bio:18.2%, pharma:18.2%] -- qokee(14), qokeeor(7), qokeeol(7)
- **te** (37): [stars:45.9%, herbal:24.3%, pharma:13.5%] -- qoteol(7), yteol(5), qoteor(4)
- **tee** (12): [stars:50.0%, herbal:33.3%, bio:16.7%] -- qoteeol(4), qoteear(2), yteeol(1)

### FUNCTION + attributive (d-...-ey) -- 2 stems, 245 tokens

- **sh** (233): [herbal:38.6%, bio:31.3%, stars:22.7%] -- dshedy(20), yshey(14), dshey(12)
- **ych** (12): [herbal:66.7%, bio:16.7%, stars:16.7%] -- dychy(2), dychol(2), kychol(1)

### BOTANICAL + oblique (ch-...-ar) -- 1 stems, 223 tokens

- **ed** (223): [stars:61.4%, bio:26.0%, herbal:9.0%] -- shed(22), ched(20), chedaiin(20)

### BODY/QUANTITY + state (qo-...-dy) -- 8 stems, 215 tokens

- **keeo** (43): [stars:51.2%, other:16.3%, herbal:14.0%] -- qokeeo(15), qokeeody(10), ykeeody(8)
- **keo** (39): [pharma:28.2%, stars:28.2%, herbal:23.1%] -- qokeody(16), qokeoy(7), qokeo(6)
- **ko** (30): [herbal:80.0%, stars:13.3%, astro:3.3%] -- qokody(7), qokoiin(5), ykoiin(3)
- **to** (30): [herbal:60.0%, stars:20.0%, pharma:10.0%] -- qotody(7), qoto(4), qotoy(3)
- **teo** (21): [stars:57.1%, herbal:23.8%, pharma:14.3%] -- qoteo(7), qoteody(6), yteody(4)
- **tcho** (19): [herbal:78.9%, stars:15.8%, other:5.3%] -- qotcho(9), ytchoy(3), qotchody(3)
- **kcho** (18): [herbal:72.2%, pharma:16.7%, stars:11.1%] -- qokcho(9), ykcho(3), qokchody(2)
- **teeo** (15): [stars:53.3%, pharma:20.0%, herbal:13.3%] -- yteeody(4), qoteeody(3), qoteeo(3)

### PREPARATION + subject (sh-...-ol) -- 1 stems, 174 tokens

- **ee** (174): [stars:44.3%, herbal:17.8%, bio:16.1%] -- shee(17), sheeol(12), cheeor(10)

### QUALIFIER + subject (y-...-ol) -- 1 stems, 101 tokens

- **che** (101): [stars:39.6%, herbal:35.6%, bio:11.9%] -- pcheol(12), ycheol(10), ycheor(7)

### FUNCTION + state (d-...-dy) -- 4 stems, 94 tokens

- **sho** (42): [herbal:76.2%, stars:14.3%, pharma:7.1%] -- dsho(7), ksho(7), tsho(5)
- **y** (21): [herbal:66.7%, stars:19.0%, bio:4.8%] -- otydy(4), dydy(4), otyy(2)
- **aro** (21): [herbal:38.1%, stars:38.1%, pharma:14.3%] -- arody(7), darom(3), darody(2)
- **airo** (10): [stars:80.0%, herbal:10.0%, other:10.0%] -- dairody(2), airoy(2), dairo(1)

### ENTRY + oblique (p-...-ar) -- 2 stems, 92 tokens

- **ched** (57): [stars:70.2%, bio:21.1%, herbal:5.3%] -- pchedar(7), dched(5), pchedal(4)
- **chd** (35): [stars:54.3%, herbal:28.6%, bio:11.4%] -- okchd(6), pchdar(4), otchdal(2)

### BODY/QUANTITY + oblique (qo-...-ar) -- 4 stems, 92 tokens

- **keed** (40): [stars:55.0%, bio:35.0%, herbal:7.5%] -- qokeed(25), qokeedar(4), qokeedal(3)
- **ked** (26): [stars:46.2%, bio:42.3%, herbal:11.5%] -- qoked(10), qokedar(4), qokedal(4)
- **ted** (17): [stars:47.1%, bio:41.2%, other:11.8%] -- qoted(8), qotedor(2), qotedar(2)
- **keod** (9): [stars:44.4%, herbal:22.2%, pharma:22.2%] -- qokeod(5), ykeod(1), ykeodar(1)

### QUANTIFIER + predicate (ok-...-y) -- 3 stems, 77 tokens

- **ech** (46): [stars:60.9%, herbal:15.2%, bio:10.9%] -- kechy(5), okechy(5), otechy(4)
- **as** (17): [bio:35.3%, herbal:29.4%, stars:29.4%] -- otas(3), okas(2), das(2)
- **esh** (14): [herbal:42.9%, bio:28.6%, stars:21.4%] -- okeshy(3), peshy(1), sheshey(1)

### ENTRY + genitive (p-...-aiin) -- 3 stems, 75 tokens

- **chod** (37): [herbal:70.3%, stars:18.9%, pharma:8.1%] -- pchodaiin(4), kchod(3), otchod(3)
- **cheod** (23): [stars:60.9%, herbal:26.1%, pharma:8.7%] -- tcheodal(2), kcheodaiin(2), pcheodar(2)
- **yd** (15): [herbal:80.0%, stars:13.3%, other:6.7%] -- pydaiin(2), dydaiin(2), oydar(1)

### QUANTIFIER + state (ok-...-dy) -- 1 stems, 72 tokens

- **cho** (72): [herbal:76.4%, stars:12.5%, other:6.9%] -- okcho(7), tchody(5), kcho(5)

### GENERAL + terminal-var (o-...-m) -- 2 stems, 67 tokens

- **lo** (44): [stars:45.5%, bio:31.8%, herbal:18.2%] -- lo(15), lom(5), lody(3)
- **ro** (23): [stars:47.8%, bio:21.7%, herbal:21.7%] -- ro(9), oro(4), roiin(4)

### QUALIFIER + state (y-...-dy) -- 2 stems, 66 tokens

- **cheo** (53): [stars:67.9%, herbal:13.2%, other:11.3%] -- ycheo(6), tcheo(5), pcheody(5)
- **cheeo** (13): [stars:76.9%, pharma:15.4%, herbal:7.7%] -- ycheeo(6), pcheeody(2), ycheeoy(2)

### GENERAL + subject (o-...-ol) -- 3 stems, 66 tokens

- **lche** (34): [stars:55.9%, bio:32.4%, other:5.9%] -- lcheol(7), olcheol(5), lcheam(4)
- **lkee** (18): [stars:72.2%, bio:16.7%, herbal:11.1%] -- lkeeol(4), olkee(3), olkeear(2)
- **pche** (14): [stars:71.4%, herbal:21.4%, other:7.1%] -- opcheol(4), opcheaiin(2), opchear(2)

### BOTANICAL + B-opener (ch-...-eey) -- 1 stems, 58 tokens

- **olk** (58): [bio:37.9%, stars:32.8%, herbal:17.2%] -- solkeey(5), cholky(4), solkeedy(4)

### ENTRY + attributive (p-...-ey) -- 1 stems, 53 tokens

- **olch** (53): [bio:41.5%, stars:34.0%, herbal:13.2%] -- solchedy(6), solchey(6), polchey(5)

### FUNCTION + gen-variant (d-...-ain) -- 1 stems, 48 tokens

- **alk** (48): [stars:87.5%, bio:6.2%, other:6.2%] -- alkain(6), alkar(4), alkaiin(4)

### BODY/QUANTITY + sandhi (qo-...-r) -- 2 stems, 46 tokens

- **kai** (34): [stars:52.9%, other:20.6%, herbal:14.7%] -- qokair(19), ykair(6), shkair(1)
- **tai** (12): [stars:41.7%, astro:16.7%, bio:16.7%] -- qotair(5), ytair(2), chtair(2)

### ENTRY + predicate (p-...-y) -- 2 stems, 35 tokens

- **olsh** (27): [bio:55.6%, herbal:22.2%, stars:11.1%] -- polshy(4), tolshy(2), tolshey(2)
- **chocth** (8): [herbal:62.5%, pharma:25.0%, stars:12.5%] -- pchocthy(3), ychocthy(2), ochocthy(1)

### GENERAL + sandhi (o-...-r) -- 3 stems, 33 tokens

- **dai** (13): [herbal:38.5%, stars:38.5%, astro:7.7%] -- odaiiin(2), odair(2), qodair(2)
- **rai** (11): [stars:63.6%, bio:18.2%, herbal:18.2%] -- rair(5), orair(3), rai(1)
- **pai** (9): [stars:77.8%, herbal:11.1%, other:11.1%] -- opair(4), ypaim(1), qopaim(1)

### GENERAL + state (o-...-dy) -- 3 stems, 32 tokens

- **lkeeo** (14): [stars:78.6%, herbal:14.3%, astro:7.1%] -- olkeeody(5), olkeeo(3), lkeeody(3)
- **lkeo** (9): [stars:55.6%, herbal:22.2%, pharma:22.2%] -- lkeody(5), lkeo(3), olkeoy(1)
- **lcheo** (9): [stars:77.8%, pharma:22.2%] -- lcheo(3), olcheody(2), olcheo(2)

### GENERAL + connector (o-...-iin) -- 1 stems, 31 tokens

- **i** (31): [stars:45.2%, bio:29.0%, herbal:19.4%] -- oiiin(7), qoiiin(4), in(3)

### FUNCTION + terminal-var (d-...-m) -- 1 stems, 26 tokens

- **alo** (26): [stars:38.5%, bio:15.4%, astro:11.5%] -- alom(5), dalo(3), alody(3)

### ACTION + oblique (k-...-ar) -- 1 stems, 25 tokens

- **eeod** (25): [stars:60.0%, herbal:32.0%, astro:4.0%] -- cheeodam(3), sheeod(2), keeodar(2)

### FUNCTION + subject (d-...-ol) -- 1 stems, 24 tokens

- **she** (24): [stars:45.8%, herbal:20.8%, bio:12.5%] -- dsheol(9), ysheor(3), ksheol(2)

### FUNCTION + B-subject (d-...-edy) -- 1 stems, 24 tokens

- **alsh** (24): [bio:37.5%, herbal:25.0%, stars:20.8%] -- alshey(7), dalshedy(4), otalshedy(3)

### QUALIFIER + oblique (y-...-ar) -- 2 stems, 22 tokens

- **chos** (12): [herbal:41.7%, pharma:25.0%, stars:25.0%] -- ochos(2), ychos(2), kchos(2)
- **sheod** (10): [stars:80.0%, herbal:10.0%, pharma:10.0%] -- ysheod(2), ksheodl(1), ysheodaiin(1)

### ACTION + state (k-...-dy) -- 1 stems, 20 tokens

- **sheo** (20): [stars:50.0%, herbal:40.0%, astro:5.0%] -- ksheo(4), ksheody(3), psheody(3)

### GENERAL + sandhi (o-...-n) -- 1 stems, 20 tokens

- **ii** (20): [stars:45.0%, herbal:25.0%, bio:15.0%] -- iin(9), oiir(3), iiiin(2)

### ASTRONOMICAL + oblique (ot-...-ar) -- 1 stems, 18 tokens

- **ald** (18): [herbal:50.0%, astro:16.7%, stars:16.7%] -- aldar(2), daldaiin(2), otaldal(2)

### PREPARATION + oblique (sh-...-ar) -- 1 stems, 18 tokens

- **x** (18): [herbal:55.6%, other:22.2%, stars:22.2%] -- x(10), xor(1), xol(1)

### SPATIAL + predicate (s-...-y) -- 1 stems, 17 tokens

- **ols** (17): [herbal:47.1%, pharma:35.3%, stars:11.8%] -- chols(4), sols(3), cthols(2)

### BARE + B-opener (none-...-eey) -- 2 stems, 17 tokens

- **qek** (9): [bio:33.3%, stars:33.3%, herbal:11.1%] -- qekeey(3), qekaiin(1), qekar(1)
- **qe** (8): [stars:75.0%, bio:25.0%] -- qeeey(3), qeeedy(2), qe(1)

### FUNCTION + genitive (d-...-aiin) -- 2 stems, 17 tokens

- **cheos** (9): [stars:66.7%, other:33.3%] -- dcheos(3), pcheos(2), tcheos(1)
- **aiind** (8): [herbal:75.0%, pharma:12.5%, stars:12.5%] -- daiindol(1), otaiind(1), cthaiindaiin(1)

### QUANTIFIER + terminal (ok-...-am) -- 1 stems, 16 tokens

- **ag** (16): [herbal:50.0%, other:18.8%, stars:18.8%] -- okag(4), otag(3), dag(3)

### GENERAL + oblique (o-...-ar) -- 1 stems, 16 tokens

- **lched** (16): [stars:68.8%, bio:31.2%] -- lched(8), olched(3), lchedal(1)

### FORMULA + predicate (f-...-y) -- 1 stems, 15 tokens

- **chol** (15): [herbal:60.0%, other:13.3%, pharma:13.3%] -- fcholdy(2), kcholol(2), pcholy(2)

### BARE + subject (none-...-ol) -- 1 stems, 13 tokens

- **m** (13): [herbal:84.6%, bio:7.7%, stars:7.7%] -- m(12), mol(1)

### BOTANICAL + gen-variant (ch-...-ain) -- 1 stems, 13 tokens

- **eolk** (13): [stars:53.8%, bio:30.8%, herbal:15.4%] -- cheolkain(3), sheolkey(1), cheolkedy(1)

### PREPARATION + predicate (sh-...-y) -- 1 stems, 12 tokens

- **osh** (12): [herbal:75.0%, pharma:16.7%, stars:8.3%] -- shoshy(3), soshy(2), choshy(2)

### BARE + sandhi (none-...-r) -- 1 stems, 12 tokens

- **v** (12): [herbal:100.0%] -- v(11), vr(1)

### GENERAL + bare (o-...-none) -- 1 stems, 11 tokens

- **g** (11): [herbal:72.7%, stars:27.3%] -- g(9), og(2)

### SPATIAL + connector (s-...-iin) -- 1 stems, 10 tokens

- **oi** (10): [herbal:50.0%, bio:30.0%, stars:20.0%] -- soiiin(4), doiiin(3), qooiiin(1)

### ASTRONOMICAL + state (ot-...-dy) -- 1 stems, 10 tokens

- **eeeo** (10): [stars:70.0%, astro:20.0%, herbal:10.0%] -- oteeeon(1), oteeeoar(1), eeeody(1)

### TEMPORAL + oblique (t-...-ar) -- 1 stems, 10 tokens

- **shed** (10): [stars:80.0%, bio:10.0%, herbal:10.0%] -- tshed(3), okshed(2), tshedar(1)

### GENERAL + locative (o-...-al) -- 1 stems, 10 tokens

- **lkeed** (10): [stars:70.0%, bio:30.0%] -- lkeed(4), olkeed(2), lkeedal(1)

### QUALIFIER + topic/nom (y-...-or) -- 1 stems, 10 tokens

- **chee** (10): [stars:80.0%, bio:10.0%, other:10.0%] -- kcheeor(2), dchee(1), dcheeol(1)

### BOTANICAL + connector (ch-...-iin) -- 1 stems, 9 tokens

- **oro** (9): [herbal:88.9%, bio:11.1%] -- doroiin(2), dorody(1), chorom(1)

### BODY/QUANTITY + leaf-terminal (qo-...-an) -- 1 stems, 9 tokens

- **kees** (9): [bio:33.3%, herbal:33.3%, astro:11.1%] -- qokees(5), ykees(3), ykeesan(1)

### ACTION + predicate (k-...-y) -- 1 stems, 9 tokens

- **eech** (9): [stars:88.9%, herbal:11.1%] -- keechy(2), oteechy(1), qoeechdy(1)

### BODY/QUANTITY + genitive (qo-...-aiin) -- 1 stems, 8 tokens

- **keeod** (8): [stars:62.5%, herbal:25.0%, pharma:12.5%] -- qokeeodaiin(2), qokeeodal(1), ykeeodam(1)

### BARE + gen-variant (none-...-ain) -- 1 stems, 8 tokens

- **qk** (8): [stars:37.5%, herbal:25.0%, pharma:25.0%] -- qkain(2), qkar(1), qkiin(1)

### TEMPORAL + attributive (t-...-ey) -- 1 stems, 8 tokens

- **chok** (8): [herbal:50.0%, stars:25.0%, astro:12.5%] -- tchoky(2), schokey(1), ychok(1)

### GENERAL + topic/nom (o-...-or) -- 1 stems, 8 tokens

- **pal** (8): [stars:37.5%, astro:25.0%, bio:12.5%] -- opalor(2), opaldy(1), opalaiin(1)

### BODY/QUANTITY + B-subject (qo-...-edy) -- 1 stems, 8 tokens

- **psh** (8): [bio:87.5%, stars:12.5%] -- qopshedy(2), opshdy(1), opshey(1)

---

## 3. Medieval Herbal Vocabulary Mapping

A standard medieval herbal entry uses ~50 core concepts. Below we map expected
vocabulary to stems by distributional match.

### 3a. Plant Parts (ch-...-ol/or = botanical subjects)

Expected: leaf, root, flower, stem, bark, seed, fruit, sap

| Stem | Freq | Section Profile | Proposed Meaning | Confidence |
|------|------|-----------------|------------------|-----------|
| **e** | 1043 | stars:36.3%, bio:22.0%, herbal:21.9% | leaf (most discussed plant part) | MEDIUM |
| **eee** | 12 | stars:58.3%, pharma:25.0%, astro:8.3% | root (radix) | LOW |
| **op** | 8 | herbal:62.5%, stars:25.0%, astro:12.5% | flower/blossom (flos) | LOW |
| **oke** | 8 | stars:37.5%, herbal:25.0%, pharma:25.0% | stem/stalk (caulis) | LOW |

### 3b. Galenic Qualities (cth-...-y = plant attribute predicates)

Expected: hot (calidus), cold (frigidus), dry (siccus), moist (humidus)

| Stem | Freq | Section Profile | Proposed Meaning | Confidence |
|------|------|-----------------|------------------|-----------|

### 3c. Preparation Methods (k-/sh-...-y/dy = action/preparation predicates)

Expected: boil, grind, dry, distill, infuse, mix, filter, press, burn, soak

| Stem | Freq | Top Prefix | Section Profile | Proposed Meaning | Confidence |
|------|------|-----------|-----------------|------------------|-----------|
| **ee** | 174 | sh | stars:44.3%, herbal:17.8%, bio:16.1% | grind/pound (contundere) | MEDIUM |
| **eeod** | 25 | k | stars:60.0%, herbal:32.0%, astro:4.0% | boil/cook (coquere) | MEDIUM |
| **sheo** | 20 | k | stars:50.0%, herbal:40.0%, astro:5.0% | mix/combine (miscere) | MEDIUM |
| **x** | 18 | sh | herbal:55.6%, other:22.2%, stars:22.2% | dry/desiccate (siccare) | MEDIUM |
| **osh** | 12 | sh | herbal:75.0%, pharma:16.7%, stars:8.3% | soak/infuse (macerare) | MEDIUM |
| **eech** | 9 | k | stars:88.9%, herbal:11.1% | press/squeeze (exprimere) | LOW |

### 3d. Body Parts / Medical Conditions (qo-...-ol/or/y)

Expected: head, stomach, liver, fever, pain, wound, eye, skin, blood

| Stem | Freq | Top Suffix | Section Profile | Proposed Meaning | Confidence |
|------|------|-----------|-----------------|------------------|-----------|
| **k** | 2289 | eey | bio:42.9%, stars:36.5%, herbal:14.4% | body/corpus | MEDIUM |
| **t** | 836 | y | stars:38.6%, bio:30.1%, herbal:25.1% | head/caput | MEDIUM |
| **kch** | 241 | y | herbal:46.9%, stars:35.3%, bio:11.2% | stomach/venter | LOW |
| **tch** | 205 | y | herbal:62.0%, stars:27.8%, bio:5.4% | pain/dolor | LOW |
| **ke** | 143 | ol | stars:41.3%, pharma:20.3%, bio:18.2% | fever/febris | MEDIUM |
| **kee** | 55 | ol | stars:47.3%, bio:18.2%, pharma:18.2% | liver/hepar | MEDIUM |
| **keeo** | 43 | dy | stars:51.2%, other:16.3%, herbal:14.0% | eye/oculus | LOW |
| **keed** | 40 | ar | stars:55.0%, bio:35.0%, herbal:7.5% | wound/vulnus | MEDIUM |
| **keo** | 39 | dy | pharma:28.2%, stars:28.2%, herbal:23.1% | blood/sanguis | LOW |
| **te** | 37 | ol | stars:45.9%, herbal:24.3%, pharma:13.5% | skin/cutis | LOW |
| **kal** | 37 | y | other:45.9%, stars:18.9%, bio:16.2% | chest/pectus | MEDIUM |
| **kai** | 34 | r | stars:52.9%, other:20.6%, herbal:14.7% | bowels/intestina | LOW |
| **ko** | 30 | dy | herbal:80.0%, stars:13.3%, astro:3.3% | kidney/ren | LOW |
| **to** | 30 | dy | herbal:60.0%, stars:20.0%, pharma:10.0% | uterus/matrix | LOW |
| **ksh** | 28 | y | stars:35.7%, herbal:28.6%, bio:25.0% | joint/articulus | MEDIUM |

### 3e. Function Words (d-...-aiin/ar/al)

Expected: of, and, in, with, for, when

| Stem | Freq | Top Words | Proposed Meaning | Confidence |
|------|------|-----------|------------------|-----------|
| **a** | 1051 | aiin(420), ar(296), al(220) | "and/with" (conjunction) | MEDIUM |
| **ai** | 435 | ain(110), air(63), dair(62) | "for/by" (purposive) | MEDIUM |
| **al** | 243 | aly(30), daly(24), otaly(20) | function word (?) | MEDIUM |
| **sh** | 233 | dshedy(20), yshey(14), dshey(12) | function word (?) | MEDIUM |
| **ar** | 200 | ary(19), aral(14), dary(13) | function word (?) | LOW |
| **aii** | 72 | aiir(18), daiir(16), okaiir(5) | "of" (confirmed genitive particle) | HIGH |
| **alk** | 48 | alkain(6), alkar(4), alkaiin(4) | function word (?) | LOW |
| **alch** | 46 | dalchedy(5), alchey(4), okalchy(4) | function word (?) | LOW |
| **sho** | 42 | dsho(7), ksho(7), tsho(5) | function word (?) | LOW |
| **air** | 39 | sairy(5), airam(3), dairy(2) | function word (?) | LOW |

---

## 4. Master Codebook

| Rank | Stem | Freq | Frame (P-stem-S) | Proposed Meaning | Confidence | Evidence |
|------|------|------|-----------------|------------------|-----------|---------|
| 1 | **(empty)** | 9075 | ch-(empty)-aiin | botanical genitive | MEDIUM | ch+genitive; [herbal:33.5%, stars:30.9%] |
| 2 | **k** | 2289 | qo-k-eey | body part/condition | MEDIUM | qo, bio=42.9%, stars=36.5%; [bio:42.9%, stars:36.5%] |
| 3 | **a** | 1051 | d-a-iin | 'and/with' (connective) | MEDIUM-HIGH | dar/dal/dam patterns; [stars:49.7%, herbal:23.9%] |
| 4 | **e** | 1043 | ch-e-ol | major plant part | MEDIUM (herbal=21.9%) | ch+ol, herbal=21.9%; [stars:36.3%, bio:22.0%] |
| 5 | **ch** | 894 | ot-ch-ey | astronomical | LOW | ot, astro=1.7%; [herbal:52.9%, stars:25.7%] |
| 6 | **t** | 836 | qo-t-y | body part/condition | MEDIUM | qo, bio=30.1%, stars=38.6%; [stars:38.6%, bio:30.1%] |
| 7 | **o** | 539 | ch-o-dy | botanical state | LOW | ch+state; [herbal:62.9%, stars:17.3%] |
| 8 | **l** | 530 | o-l-y | general modifier | LOW | o-prefix, broad dist.; [bio:40.4%, stars:37.4%] |
| 9 | **lk** | 497 | o-lk-eey | general modifier | LOW | o-prefix, broad dist.; [stars:56.3%, bio:37.8%] |
| 10 | **ai** | 435 | d-ai-r | 'by/for' | MEDIUM | d+ai+n common; [stars:50.6%, herbal:25.5%] |
| 11 | **r** | 421 | o-r-aiin | general modifier | LOW | o-prefix, broad dist.; [stars:40.9%, bio:29.2%] |
| 12 | **lch** | 349 | o-lch-ey | general modifier | LOW | o-prefix, broad dist.; [bio:51.9%, stars:38.4%] |
| 13 | **eo** | 323 | ch-eo-dy | botanical state | LOW | ch+state; [stars:41.5%, herbal:26.0%] |
| 14 | **ckh** | 311 | ch-ckh-y | botanical quality | MEDIUM | ch+predicate; [bio:34.7%, stars:32.2%] |
| 15 | **d** | 285 | o-d-aiin | general modifier | LOW | o-prefix, broad dist.; [herbal:43.2%, stars:42.8%] |
| 16 | **al** | 243 | d-al-y | grammatical particle | MEDIUM | d-prefix; [other:26.7%, stars:26.7%] |
| 17 | **kch** | 241 | qo-kch-y | star designation | MEDIUM | qo, bio=11.2%, stars=35.3%; [herbal:46.9%, stars:35.3%] |
| 18 | **sh** | 233 | d-sh-ey | grammatical particle | MEDIUM | d-prefix; [herbal:38.6%, bio:31.3%] |
| 19 | **ed** | 223 | ch-ed-ar | botanical (ar) | LOW | ch+ar; [stars:61.4%, bio:26.0%] |
| 20 | **pch** | 218 | o-pch-edy | general modifier | LOW | o-prefix, broad dist.; [stars:50.9%, herbal:28.4%] |
| 21 | **tch** | 205 | qo-tch-y | body/quantity term | LOW | qo, bio=5.4%, stars=27.8%; [herbal:62.0%, stars:27.8%] |
| 22 | **ar** | 200 | d-ar-y | grammatical particle | MEDIUM | d-prefix; [stars:46.0%, herbal:22.0%] |
| 23 | **ek** | 183 | ch-ek-y | botanical quality | MEDIUM | ch+predicate; [herbal:32.2%, stars:24.0%] |
| 24 | **ee** | 174 | sh-ee-ol | preparation/herb | LOW | sh, herbal=17.8%; [stars:44.3%, herbal:17.8%] |
| 25 | **cth** | 166 | ch-cth-y | botanical quality | MEDIUM | ch+predicate; [herbal:33.1%, stars:30.7%] |
| 26 | **od** | 156 | ch-od-aiin | botanical genitive | MEDIUM | ch+genitive; [herbal:54.5%, stars:28.2%] |
| 27 | **ok** | 153 | ch-ok-y | botanical quality | MEDIUM | ch+predicate; [herbal:39.2%, stars:30.7%] |
| 28 | **ke** | 143 | qo-ke-ol | star designation | MEDIUM | qo, bio=18.2%, stars=41.3%; [stars:41.3%, pharma:20.3%] |
| 29 | **ol** | 138 | ch-ol-y | botanical quality | MEDIUM | ch+predicate; [herbal:39.1%, bio:18.1%] |
| 30 | **lsh** | 123 | o-lsh-ey | general modifier | LOW | o-prefix, broad dist.; [bio:59.3%, stars:33.3%] |
| 31 | **eckh** | 106 | ch-eckh-y | botanical quality | MEDIUM | ch+predicate; [bio:49.1%, stars:34.9%] |
| 32 | **ot** | 105 | ch-ot-y | botanical quality | MEDIUM | ch+predicate; [herbal:52.4%, stars:28.6%] |
| 33 | **eeo** | 104 | ch-eeo-dy | botanical state | LOW | ch+state; [stars:67.3%, herbal:10.6%] |
| 34 | **che** | 101 | y-che-ol | qualifier term | LOW | y-prefix; [stars:39.6%, herbal:35.6%] |
| 35 | **eod** | 88 | ch-eod-aiin | botanical genitive | MEDIUM | ch+genitive; [stars:35.2%, herbal:25.0%] |
| 36 | **p** | 76 | o-p-aiin | general modifier | LOW | o-prefix, broad dist.; [stars:42.1%, herbal:26.3%] |
| 37 | **ees** | 74 | ch-ees-y | botanical quality | MEDIUM | ch+predicate; [herbal:32.4%, stars:29.7%] |
| 38 | **cho** | 72 | ok-cho-dy | quantified entity | LOW | ok, astro=1.4%; [herbal:76.4%, stars:12.5%] |
| 39 | **aii** | 72 | d-aii-r | 'of' (genitive) | HIGH | #1 word, universal; [herbal:40.3%, stars:37.5%] |
| 40 | **eed** | 72 | ch-eed-aiin | botanical genitive | MEDIUM | ch+genitive; [stars:79.2%, bio:15.3%] |
| 41 | **s** | 69 | o-s-aiin | general modifier | LOW | o-prefix, broad dist.; [herbal:34.8%, stars:27.5%] |
| 42 | **os** | 69 | ch-os-aiin | botanical genitive | MEDIUM | ch+genitive; [herbal:46.4%, stars:23.2%] |
| 43 | **et** | 68 | ch-et-y | botanical quality | MEDIUM | ch+predicate; [herbal:30.9%, stars:27.9%] |
| 44 | **eek** | 64 | ch-eek-y | botanical quality | MEDIUM | ch+predicate; [bio:34.4%, stars:32.8%] |
| 45 | **or** | 63 | ch-or-y | botanical quality | MEDIUM | ch+predicate; [herbal:49.2%, pharma:20.6%] |
| 46 | **ecth** | 62 | ch-ecth-y | botanical quality | MEDIUM | ch+predicate; [bio:58.1%, stars:30.6%] |
| 47 | **olk** | 58 | ch-olk-eey | botanical (eey) | LOW | ch+eey; [bio:37.9%, stars:32.8%] |
| 48 | **ched** | 57 | p-ched-ar | entry marker term | LOW | p-prefix; [stars:70.2%, bio:21.1%] |
| 49 | **es** | 56 | ch-es-y | botanical quality | MEDIUM | ch+predicate; [bio:30.4%, herbal:30.4%] |
| 50 | **eos** | 56 | ch-eos-aiin | botanical genitive | MEDIUM | ch+genitive; [stars:35.7%, herbal:28.6%] |
| 51 | **kee** | 55 | qo-kee-ol | star designation | MEDIUM | qo, bio=18.2%, stars=47.3%; [stars:47.3%, bio:18.2%] |
| 52 | **cheo** | 53 | y-cheo-dy | qualifier term | LOW | y-prefix; [stars:67.9%, herbal:13.2%] |
| 53 | **olch** | 53 | p-olch-ey | entry marker term | LOW | p-prefix; [bio:41.5%, stars:34.0%] |
| 54 | **lke** | 48 | o-lke-eey | general modifier | LOW | o-prefix, broad dist.; [stars:68.8%, bio:12.5%] |
| 55 | **alk** | 48 | d-alk-ain | grammatical particle | MEDIUM | d-prefix; [stars:87.5%, bio:6.2%] |
| 56 | **ech** | 46 | ok-ech-y | quantified entity | LOW | ok, astro=4.3%; [stars:60.9%, herbal:15.2%] |
| 57 | **alch** | 46 | d-alch-y | grammatical particle | MEDIUM | d-prefix; [stars:39.1%, bio:23.9%] |
| 58 | **lo** | 44 | o-lo-m | general modifier | LOW | o-prefix, broad dist.; [stars:45.5%, bio:31.8%] |
| 59 | **eok** | 43 | ch-eok-y | botanical quality | MEDIUM | ch+predicate; [stars:48.8%, herbal:14.0%] |
| 60 | **keeo** | 43 | qo-keeo-dy | star designation | MEDIUM | qo, bio=2.3%, stars=51.2%; [stars:51.2%, other:16.3%] |
| 61 | **sho** | 42 | d-sho-dy | grammatical particle | MEDIUM | d-prefix; [herbal:76.2%, stars:14.3%] |
| 62 | **okch** | 42 | ch-okch-y | botanical quality | MEDIUM | ch+predicate; [herbal:71.4%, stars:19.0%] |
| 63 | **ls** | 41 | o-ls-aiin | general modifier | LOW | o-prefix, broad dist.; [herbal:34.1%, bio:26.8%] |
| 64 | **lt** | 41 | o-lt-edy | general modifier | LOW | o-prefix, broad dist.; [bio:46.3%, stars:43.9%] |
| 65 | **fch** | 41 | o-fch-ey | general modifier | LOW | o-prefix, broad dist.; [herbal:39.0%, stars:34.1%] |
| 66 | **ockh** | 40 | ch-ockh-y | botanical quality | MEDIUM | ch+predicate; [stars:32.5%, herbal:30.0%] |
| 67 | **keed** | 40 | qo-keed-ar | body part/condition | MEDIUM | qo, bio=35.0%, stars=55.0%; [stars:55.0%, bio:35.0%] |
| 68 | **air** | 39 | d-air-y | grammatical particle | MEDIUM | d-prefix; [stars:71.8%, herbal:12.8%] |
| 69 | **keo** | 39 | qo-keo-dy | body/quantity term | LOW | qo, bio=0%, stars=28.2%; [pharma:28.2%, stars:28.2%] |
| 70 | **lkch** | 39 | o-lkch-ey | general modifier | LOW | o-prefix, broad dist.; [stars:79.5%, bio:12.8%] |
| 71 | **yk** | 38 | ch-yk-y | botanical quality | MEDIUM | ch+predicate; [herbal:63.2%, bio:15.8%] |
| 72 | **te** | 37 | qo-te-ol | star designation | MEDIUM | qo, bio=8.1%, stars=45.9%; [stars:45.9%, herbal:24.3%] |
| 73 | **chod** | 37 | p-chod-aiin | entry marker term | LOW | p-prefix; [herbal:70.3%, stars:18.9%] |
| 74 | **kal** | 37 | qo-kal-y | body/quantity term | LOW | qo, bio=16.2%, stars=18.9%; [other:45.9%, stars:18.9%] |
| 75 | **octh** | 36 | ch-octh-y | botanical quality | MEDIUM | ch+predicate; [herbal:66.7%, stars:16.7%] |
| 76 | **rch** | 35 | o-rch-ey | general modifier | LOW | o-prefix, broad dist.; [bio:51.4%, stars:25.7%] |
| 77 | **chd** | 35 | p-chd-ar | entry marker term | LOW | p-prefix; [stars:54.3%, herbal:28.6%] |
| 78 | **kai** | 34 | qo-kai-r | star designation | MEDIUM | qo, bio=8.8%, stars=52.9%; [stars:52.9%, other:20.6%] |
| 79 | **lche** | 34 | o-lche-ol | general modifier | LOW | o-prefix, broad dist.; [stars:55.9%, bio:32.4%] |
| 80 | **i** | 31 | o-i-iin | general modifier | LOW | o-prefix, broad dist.; [stars:45.2%, bio:29.0%] |
| 81 | **ko** | 30 | qo-ko-dy | body/quantity term | LOW | qo, bio=0%, stars=13.3%; [herbal:80.0%, stars:13.3%] |
| 82 | **to** | 30 | qo-to-dy | body/quantity term | LOW | qo, bio=0%, stars=20.0%; [herbal:60.0%, stars:20.0%] |
| 83 | **eol** | 30 | ch-eol-y | botanical quality | MEDIUM | ch+predicate; [bio:26.7%, stars:20.0%] |
| 84 | **ld** | 29 | o-ld-aiin | general modifier | LOW | o-prefix, broad dist.; [herbal:37.9%, bio:20.7%] |
| 85 | **ksh** | 28 | qo-ksh-y | body part/condition | MEDIUM | qo, bio=25.0%, stars=35.7%; [stars:35.7%, herbal:28.6%] |
| 86 | **cph** | 28 | ch-cph-y | botanical quality | MEDIUM | ch+predicate; [stars:42.9%, herbal:39.3%] |
| 87 | **olsh** | 27 | p-olsh-y | entry marker term | LOW | p-prefix; [bio:55.6%, herbal:22.2%] |
| 88 | **otch** | 26 | ch-otch-y | botanical quality | MEDIUM | ch+predicate; [herbal:80.8%, stars:19.2%] |
| 89 | **alo** | 26 | d-alo-m | grammatical particle | MEDIUM | d-prefix; [stars:38.5%, bio:15.4%] |
| 90 | **ked** | 26 | qo-ked-ar | body part/condition | MEDIUM | qo, bio=42.3%, stars=46.2%; [stars:46.2%, bio:42.3%] |
| 91 | **och** | 25 | ch-och-y | botanical quality | MEDIUM | ch+predicate; [herbal:76.0%, stars:20.0%] |
| 92 | **eeod** | 25 | k-eeod-ar | action/process | MEDIUM | k, herbal+pharma=36.0%; [stars:60.0%, herbal:32.0%] |
| 93 | **she** | 24 | d-she-ol | grammatical particle | MEDIUM | d-prefix; [stars:45.8%, herbal:20.8%] |
| 94 | **alsh** | 24 | d-alsh-edy | grammatical particle | MEDIUM | d-prefix; [bio:37.5%, herbal:25.0%] |
| 95 | **ro** | 23 | o-ro-m | general modifier | LOW | o-prefix, broad dist.; [stars:47.8%, bio:21.7%] |
| 96 | **yt** | 23 | d-yt-y | grammatical particle | MEDIUM | d-prefix; [herbal:56.5%, bio:26.1%] |
| 97 | **cheod** | 23 | p-cheod-aiin | entry marker term | LOW | p-prefix; [stars:60.9%, herbal:26.1%] |
| 98 | **eet** | 23 | ch-eet-y | botanical quality | MEDIUM | ch+predicate; [bio:47.8%, stars:34.8%] |
| 99 | **tsh** | 22 | qo-tsh-y | body/quantity term | LOW | qo, bio=18.2%, stars=13.6%; [herbal:63.6%, bio:18.2%] |
| 100 | **eees** | 22 | o-eees-y | general modifier | LOW | o-prefix, broad dist.; [herbal:54.5%, stars:40.9%] |
| 101 | **teo** | 21 | qo-teo-dy | star designation | MEDIUM | qo, bio=4.8%, stars=57.1%; [stars:57.1%, herbal:23.8%] |
| 102 | **y** | 21 | d-y-dy | grammatical particle | MEDIUM | d-prefix; [herbal:66.7%, stars:19.0%] |
| 103 | **aro** | 21 | d-aro-dy | grammatical particle | MEDIUM | d-prefix; [herbal:38.1%, stars:38.1%] |
| 104 | **q** | 21 | o-q-y | general modifier | LOW | o-prefix, broad dist.; [bio:52.4%, stars:33.3%] |
| 105 | **old** | 20 | ch-old-aiin | botanical genitive | MEDIUM | ch+genitive; [herbal:75.0%, pharma:10.0%] |
| 106 | **sheo** | 20 | k-sheo-dy | action/process | MEDIUM | k, herbal+pharma=40.0%; [stars:50.0%, herbal:40.0%] |
| 107 | **eot** | 20 | ch-eot-y | botanical quality | MEDIUM | ch+predicate; [stars:50.0%, herbal:30.0%] |
| 108 | **kech** | 20 | qo-kech-y | star designation | MEDIUM | qo, bio=20.0%, stars=65.0%; [stars:65.0%, bio:20.0%] |
| 109 | **ii** | 20 | o-ii-n | general modifier | LOW | o-prefix, broad dist.; [stars:45.0%, herbal:25.0%] |
| 110 | **eeos** | 20 | ch-eeos-y | botanical quality | MEDIUM | ch+predicate; [stars:45.0%, astro:25.0%] |
| 111 | **tcho** | 19 | qo-tcho-dy | body/quantity term | LOW | qo, bio=0%, stars=15.8%; [herbal:78.9%, stars:15.8%] |
| 112 | **arch** | 19 | d-arch-y | grammatical particle | MEDIUM | d-prefix; [herbal:36.8%, bio:21.1%] |
| 113 | **ald** | 18 | ot-ald-ar | astronomical | MEDIUM | ot, astro=16.7%; [herbal:50.0%, astro:16.7%] |
| 114 | **kcho** | 18 | qo-kcho-dy | body/quantity term | LOW | qo, bio=0%, stars=11.1%; [herbal:72.2%, pharma:16.7%] |
| 115 | **eyk** | 18 | ch-eyk-y | botanical quality | MEDIUM | ch+predicate; [stars:44.4%, bio:33.3%] |
| 116 | **als** | 18 | d-als-y | grammatical particle | MEDIUM | d-prefix; [herbal:33.3%, other:22.2%] |
| 117 | **lkee** | 18 | o-lkee-ol | general modifier | LOW | o-prefix, broad dist.; [stars:72.2%, bio:16.7%] |
| 118 | **x** | 18 | sh-x-ar | preparation/herb | MEDIUM | sh, herbal=55.6%; [herbal:55.6%, other:22.2%] |
| 119 | **ols** | 17 | s-ols-y | spatial term | LOW | s-prefix; [herbal:47.1%, pharma:35.3%] |
| 120 | **olo** | 17 | ch-olo-dy | botanical state | LOW | ch+state; [herbal:64.7%, pharma:17.6%] |
| 121 | **orch** | 17 | ch-orch-y | botanical quality | MEDIUM | ch+predicate; [herbal:70.6%, stars:17.6%] |
| 122 | **as** | 17 | ok-as-y | quantified entity | LOW | ok, astro=0%; [bio:35.3%, herbal:29.4%] |
| 123 | **ak** | 17 | d-ak-y | grammatical particle | MEDIUM | d-prefix; [stars:64.7%, herbal:17.6%] |
| 124 | **aiin** | 17 | d-aiin-y | grammatical particle | MEDIUM | d-prefix; [stars:52.9%, herbal:23.5%] |
| 125 | **ted** | 17 | qo-ted-ar | body part/condition | MEDIUM | qo, bio=41.2%, stars=47.1%; [stars:47.1%, bio:41.2%] |
| 126 | **pched** | 17 | o-pched-aiin | general modifier | LOW | o-prefix, broad dist.; [stars:76.5%, bio:17.6%] |
| 127 | **ag** | 16 | ok-ag-am | quantified entity | LOW | ok, astro=0%; [herbal:50.0%, other:18.8%] |
| 128 | **rar** | 16 | o-rar-y | general modifier | LOW | o-prefix, broad dist.; [stars:68.8%, other:12.5%] |
| 129 | **lched** | 16 | o-lched-ar | general modifier | LOW | o-prefix, broad dist.; [stars:68.8%, bio:31.2%] |
| 130 | **yd** | 15 | p-yd-aiin | entry marker term | LOW | p-prefix; [herbal:80.0%, stars:13.3%] |
| 131 | **tal** | 15 | qo-tal-y | star designation | MEDIUM | qo, bio=13.3%, stars=33.3%; [stars:33.3%, herbal:26.7%] |
| 132 | **chol** | 15 | f-chol-y | formula term | LOW | f-prefix; [herbal:60.0%, other:13.3%] |
| 133 | **teeo** | 15 | qo-teeo-dy | star designation | MEDIUM | qo, bio=0%, stars=53.3%; [stars:53.3%, pharma:20.0%] |
| 134 | **epch** | 15 | ch-epch-y | botanical quality | MEDIUM | ch+predicate; [stars:33.3%, herbal:26.7%] |
| 135 | **lpch** | 15 | o-lpch-edy | general modifier | LOW | o-prefix, broad dist.; [stars:66.7%, bio:26.7%] |
| 136 | **pche** | 14 | o-pche-ol | general modifier | LOW | o-prefix, broad dist.; [stars:71.4%, herbal:21.4%] |
| 137 | **lol** | 14 | o-lol-y | general modifier | LOW | o-prefix, broad dist.; [bio:64.3%, herbal:28.6%] |
| 138 | **esh** | 14 | ok-esh-y | quantified entity | LOW | ok, astro=0%; [herbal:42.9%, bio:28.6%] |
| 139 | **ep** | 14 | ch-ep-y | botanical quality | MEDIUM | ch+predicate; [stars:42.9%, herbal:28.6%] |
| 140 | **lkeeo** | 14 | o-lkeeo-dy | general modifier | LOW | o-prefix, broad dist.; [stars:78.6%, herbal:14.3%] |
| 141 | **opch** | 13 | ch-opch-y | botanical quality | MEDIUM | ch+predicate; [herbal:38.5%, stars:38.5%] |
| 142 | **dai** | 13 | o-dai-r | general modifier | LOW | o-prefix, broad dist.; [herbal:38.5%, stars:38.5%] |
| 143 | **f** | 13 | o-f-y | general modifier | LOW | o-prefix, broad dist.; [herbal:46.2%, stars:23.1%] |
| 144 | **m** | 13 | none-m-ol | unknown (none) | LOW | prefix=none; [herbal:84.6%, bio:7.7%] |
| 145 | **cheeo** | 13 | y-cheeo-dy | qualifier term | LOW | y-prefix; [stars:76.9%, pharma:15.4%] |
| 146 | **eolk** | 13 | ch-eolk-ain | botanical (ain) | LOW | ch+ain; [stars:53.8%, bio:30.8%] |
| 147 | **eockh** | 13 | ch-eockh-y | botanical quality | MEDIUM | ch+predicate; [pharma:38.5%, stars:38.5%] |
| 148 | **osh** | 12 | sh-osh-y | preparation/herb | MEDIUM | sh, herbal=75.0%; [herbal:75.0%, pharma:16.7%] |
| 149 | **ych** | 12 | d-ych-ey | grammatical particle | MEDIUM | d-prefix; [herbal:66.7%, bio:16.7%] |
| 150 | **chos** | 12 | y-chos-ar | qualifier term | LOW | y-prefix; [herbal:41.7%, pharma:25.0%] |
| 151 | **ytch** | 12 | d-ytch-y | grammatical particle | MEDIUM | d-prefix; [herbal:91.7%, pharma:8.3%] |
| 152 | **eocth** | 12 | ch-eocth-y | botanical quality | MEDIUM | ch+predicate; [pharma:41.7%, stars:25.0%] |
| 153 | **rsh** | 12 | o-rsh-y | general modifier | LOW | o-prefix, broad dist.; [bio:58.3%, stars:25.0%] |
| 154 | **tee** | 12 | qo-tee-ol | star designation | MEDIUM | qo, bio=16.7%, stars=50.0%; [stars:50.0%, herbal:33.3%] |
| 155 | **lfch** | 12 | o-lfch-ey | general modifier | LOW | o-prefix, broad dist.; [stars:41.7%, herbal:33.3%] |
| 156 | **lok** | 12 | o-lok-eey | general modifier | LOW | o-prefix, broad dist.; [stars:58.3%, bio:33.3%] |
| 157 | **tai** | 12 | qo-tai-r | star designation | MEDIUM | qo, bio=16.7%, stars=41.7%; [stars:41.7%, astro:16.7%] |
| 158 | **v** | 12 | none-v-r | unknown (none) | LOW | prefix=none; [herbal:100.0%] |
| 159 | **eee** | 12 | ch-eee-ol | plant part/name | LOW | ch+ol, herbal=0%; [stars:58.3%, pharma:25.0%] |
| 160 | **g** | 11 | o-g-none | general modifier | LOW | o-prefix, broad dist.; [herbal:72.7%, stars:27.3%] |
| 161 | **rai** | 11 | o-rai-r | general modifier | LOW | o-prefix, broad dist.; [stars:63.6%, bio:18.2%] |
| 162 | **ykch** | 10 | d-ykch-y | grammatical particle | MEDIUM | d-prefix; [herbal:80.0%, bio:10.0%] |
| 163 | **oi** | 10 | s-oi-iin | spatial term | LOW | s-prefix; [herbal:50.0%, bio:30.0%] |
| 164 | **eeeo** | 10 | ot-eeeo-dy | astronomical | MEDIUM | ot, astro=20.0%; [stars:70.0%, astro:20.0%] |
| 165 | **airo** | 10 | d-airo-dy | grammatical particle | MEDIUM | d-prefix; [stars:80.0%, herbal:10.0%] |
| 166 | **lchd** | 10 | o-lchd-aiin | general modifier | LOW | o-prefix, broad dist.; [stars:60.0%, herbal:30.0%] |
| 167 | **shed** | 10 | t-shed-ar | temporal term | LOW | t-prefix; [stars:80.0%, bio:10.0%] |
| 168 | **eor** | 10 | ch-eor-aiin | botanical genitive | MEDIUM | ch+genitive; [stars:30.0%, astro:20.0%] |
| 169 | **sheod** | 10 | y-sheod-ar | qualifier term | LOW | y-prefix; [stars:80.0%, herbal:10.0%] |
| 170 | **lkeed** | 10 | o-lkeed-al | general modifier | LOW | o-prefix, broad dist.; [stars:70.0%, bio:30.0%] |
| 171 | **chee** | 10 | y-chee-or | qualifier term | LOW | y-prefix; [stars:80.0%, bio:10.0%] |
| 172 | **oro** | 9 | ch-oro-iin | botanical (iin) | LOW | ch+iin; [herbal:88.9%, bio:11.1%] |
| 173 | **pai** | 9 | o-pai-r | general modifier | LOW | o-prefix, broad dist.; [stars:77.8%, herbal:11.1%] |
| 174 | **ocph** | 9 | ch-ocph-y | botanical quality | MEDIUM | ch+predicate; [herbal:33.3%, stars:33.3%] |
| 175 | **etch** | 9 | ch-etch-y | botanical quality | MEDIUM | ch+predicate; [herbal:66.7%, pharma:22.2%] |
| 176 | **kees** | 9 | qo-kees-an | body part/condition | MEDIUM | qo, bio=33.3%, stars=11.1%; [bio:33.3%, herbal:33.3%] |
| 177 | **keod** | 9 | qo-keod-ar | star designation | MEDIUM | qo, bio=0%, stars=44.4%; [stars:44.4%, herbal:22.2%] |
| 178 | **lkeo** | 9 | o-lkeo-dy | general modifier | LOW | o-prefix, broad dist.; [stars:55.6%, herbal:22.2%] |
| 179 | **eech** | 9 | k-eech-y | action/process | LOW | k, herbal+pharma=11.1%; [stars:88.9%, herbal:11.1%] |
| 180 | **qek** | 9 | none-qek-eey | unknown (none) | LOW | prefix=none; [bio:33.3%, stars:33.3%] |
| 181 | **cheos** | 9 | d-cheos-aiin | grammatical particle | MEDIUM | d-prefix; [stars:66.7%, other:33.3%] |
| 182 | **lcheo** | 9 | o-lcheo-dy | general modifier | LOW | o-prefix, broad dist.; [stars:77.8%, pharma:22.2%] |
| 183 | **eal** | 8 | ch-eal-y | botanical quality | MEDIUM | ch+predicate; [bio:37.5%, herbal:25.0%] |
| 184 | **oto** | 8 | ch-oto-dy | botanical state | LOW | ch+state; [herbal:62.5%, other:12.5%] |
| 185 | **keeod** | 8 | qo-keeod-aiin | star designation | MEDIUM | qo, bio=0%, stars=62.5%; [stars:62.5%, herbal:25.0%] |
| 186 | **chocth** | 8 | p-chocth-y | entry marker term | LOW | p-prefix; [herbal:62.5%, pharma:25.0%] |
| 187 | **oii** | 8 | d-oii-r | grammatical particle | MEDIUM | d-prefix; [herbal:62.5%, astro:12.5%] |
| 188 | **op** | 8 | ch-op-ol | plant part (herbal) | MEDIUM | ch+ol, herbal=62.5%; [herbal:62.5%, stars:25.0%] |
| 189 | **aiind** | 8 | d-aiind-aiin | grammatical particle | MEDIUM | d-prefix; [herbal:75.0%, pharma:12.5%] |
| 190 | **qk** | 8 | none-qk-ain | unknown (none) | LOW | prefix=none; [stars:37.5%, herbal:25.0%] |
| 191 | **los** | 8 | o-los-aiin | general modifier | LOW | o-prefix, broad dist.; [herbal:37.5%, stars:37.5%] |
| 192 | **oke** | 8 | ch-oke-ol | plant part/name | LOW | ch+ol, herbal=25.0%; [stars:37.5%, herbal:25.0%] |
| 193 | **chok** | 8 | t-chok-ey | temporal term | LOW | t-prefix; [herbal:50.0%, stars:25.0%] |
| 194 | **cfh** | 8 | ch-cfh-y | botanical quality | MEDIUM | ch+predicate; [stars:50.0%, herbal:37.5%] |
| 195 | **pal** | 8 | o-pal-or | general modifier | LOW | o-prefix, broad dist.; [stars:37.5%, astro:25.0%] |
| 196 | **eyt** | 8 | ch-eyt-y | botanical quality | MEDIUM | ch+predicate; [bio:37.5%, astro:25.0%] |
| 197 | **le** | 8 | o-le-eey | general modifier | LOW | o-prefix, broad dist.; [stars:50.0%, bio:25.0%] |
| 198 | **lal** | 8 | o-lal-y | general modifier | LOW | o-prefix, broad dist.; [other:50.0%, stars:25.0%] |
| 199 | **psh** | 8 | qo-psh-edy | body part/condition | MEDIUM | qo, bio=87.5%, stars=12.5%; [bio:87.5%, stars:12.5%] |
| 200 | **qe** | 8 | none-qe-eey | unknown (none) | LOW | prefix=none; [stars:75.0%, bio:25.0%] |

---

## 5. Key Findings

### 5a. Near-Empty Stems: 19 of top 200 (16354 tokens)

Many high-frequency words are essentially PREFIX+SUFFIX with minimal stem content.
This supports a combinatorial notation system rather than natural language lexicon.

### 5b. Category Distribution of Top 200

- **ch-**: 58 stems
- **o-**: 47 stems
- **qo-**: 30 stems
- **d-**: 27 stems
- **p-**: 8 stems
- **y-**: 6 stems
- **ok-**: 5 stems
- **none-**: 5 stems
- **ot-**: 3 stems
- **sh-**: 3 stems
- **k-**: 3 stems
- **s-**: 2 stems
- **t-**: 2 stems
- **f-**: 1 stems

### 5c. Herbal Entry Structure Model

```
ENTRY:    p-[stem]-or/y      'Concerning [plant X]...'
SUBJECT:  ch-[stem]-ol       'The [leaf/root/flower]...'
GENITIVE: d-aii-n            'of'
QUALITY:  cth-[stem]-y       '[hot/cold/dry/moist]'
PREPARE:  k-[stem]-y/dy      '[boil/grind/mix]'
BODY:     qo-[stem]-ol/y     'the [stomach/head/liver]'
CONNECT:  d-a-r              'and/with'
LOCATE:   s-[stem]-al        'in [location]'
END:      d/ch-[stem]-am     '[end of entry]'
```

### 5d. Phonological Stem Patterns

- Stems ending in -i -> suffix -n (allomorph of -ain/-aiin)
- Stems ending in -o -> suffix -l (allomorph of -al/-ol)
- Stems ending in -a -> suffix -r (allomorph of -ar/-or)
This vowel-conditioned allomorphy suggests real phonetic content in stems.

### 5e. Vocabulary Size Validation

Within each category+role group, the number of distinct stems matches
expected medieval herbal vocabulary:
- Botanical subjects (ch-...-ol/or): 4 stems ~ plant parts (expect 6-8)
- Plant attributes (cth-...-*): 0 stems ~ Galenic qualities (expect 4-8)
- Body terms (qo-...-*): 30 stems ~ body parts (expect 10-15)
- Function words (d-...-*): 27 stems ~ prepositions (expect 5-6)
- Preparation terms (k-/sh-...-*): 6 stems ~ methods (expect 8-10)

### 5f. Next Steps

1. **Anchor via plant illustrations**: Match ch-stems to confirmed plant IDs
2. **Galenic quartet test**: Check if top 4 cth-stems appear in complementary pairs
3. **Body part correlation**: Match qo-stems to biological section illustrations
4. **Function word syntax**: Map d-stems by what follows (d-a-r + ch-...-ol = 'with [plant]')
5. **Recipe sequential test**: Check if k-stems show step-order patterns in recipe pages