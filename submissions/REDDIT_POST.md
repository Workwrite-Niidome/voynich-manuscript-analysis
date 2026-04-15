# Reddit Post

**Target subreddits:** r/voynich, r/cryptography

---

## Post Title

We ran the most extensive computational analysis of the Voynich Manuscript ever attempted (33 hypotheses, 273 files, 2 blind tests). Here's what we found -- and what we got wrong.

---

## Post Body

Hi everyone,

Over 20+ analysis cycles, we systematically analysed the complete EVA transcription of the Voynich Manuscript (37,779 tokens, 226 folios) using AI-assisted hypothesis generation and destruction. The full paper is on arXiv: [arXiv:XXXX.XXXXX]

I want to be upfront: **we did not decode the manuscript.** But we found some things that survived serious attempts to debunk them, and we're sharing everything -- including the failures -- because this community values rigour over hype.

### What survived rigorous testing (10 validated findings):

1. **Cross-word sandhi.** Word-final n/l/r is conditioned by the next word's initial. This survives 10-fold cross-validation (42.9% vs 34.7% baseline), 1000-iteration permutation testing (p < 0.001), and cross-split correlation (r = 0.84). It works within lines but collapses across line boundaries. This is, to our knowledge, previously unreported.

2. **Vowel grade = specificity.** r = -0.954. Words with more complex vowel patterns appear on fewer pages. 91% of the variance explained. Strongest statistical finding in the entire project.

3. **6-layer word structure.** PREFIX + CLASSIFIER + ROOT + VOWEL GRADE + TERMINAL + SUFFIX, with near-zero prefix-suffix coupling (NMI = 0.032 -- lower than any natural language we tested).

4. **93% first-word uniqueness** on herbal pages. Line 1 almost certainly encodes a plant name/identifier.

5. **-dy/-ol suffix crossover** across line positions: -dy dominates early lines, -ol dominates late lines, they swap at line 7-8. Strong evidence of structured content.

6. **ty = thin/linear leaves** (Fisher p = 0.008, OR = 18.0). The only morpheme-feature association that survived full-scale validation on all 112 herbal pages.

7. **qo-k measurement system.** A systematic paradigm (qokeey/qokey/qoky/qokam etc.) with position, doubling, and context coherence. "qokal ... dar" appears 5 times -- possibly "[spoonful] [give]."

### What we got wrong (this is equally important):

- **sh = underground/root: REFUTED.** Blind test accuracy 25%. We believed this for multiple cycles before testing it properly.
- **cthy = fruit: REFUTED.** Chi-squared = 60.44 on a 9-page training set. Full-scale (112 pages): p = 0.661. The "signal" was selection bias.
- **dchy = tall: REFUTED.** Based on 4 word occurrences across 3 pages. At full scale: p = 1.0.
- **4 of 5 top morpheme associations failed at full scale.** This is a cautionary tale about small-N linguistic studies.
- **Negative predictions fail systematically.** If a morpheme is absent, we cannot predict that a feature is absent. The system is partial-descriptor at best.

### What the manuscript probably is (post-red-team confidence):

| Hypothesis | Confidence |
|-----------|-----------|
| Constructed pharmaceutical notation | 35-45% |
| Verbose homophonic cipher (Naibbe-type) | 25-35% |
| Unknown natural language | 10-20% |
| Sophisticated hoax (line-aware) | 15-25% |

### Implications for Rugg's hoax theory:

The three-layer sandhi pattern is difficult to produce with a simple Cardan grille. However, a line-aware grille has not been tested against sandhi -- this is an open experiment for anyone who wants to try.

### Methodological notes:

- We introduced **blind prediction testing** to Voynich studies (predictions recorded before looking at illustrations). This was the single most valuable methodological decision.
- A dedicated **red-team cycle** attacked all claims with 8 destructive tests. Confidence levels dropped 20-40 points.
- All 273 files (scripts, analysis, data) are available.
- The AI doing the analysis was Claude Opus 4.6. We are explicit about this and about the limitation that all "agents" shared the same model and biases.

### What we think would actually crack this:

The barrier is not computation. It's domain expertise. Someone who knows 15th-century Northern Italian pharmaceutical practice -- the Antidotarium Nicolai, the Circa Instans, Carrara Herbal conventions -- would recognise the ~200 stem meanings that statistics alone cannot determine.

Happy to answer questions and receive criticism. The whole point of posting here is to invite scrutiny from people who know this manuscript better than we do.

Paper: [arXiv:XXXX.XXXXX]

---

## Notes for posting:

- Post to r/voynich first, then cross-post to r/cryptography
- Flair: "Research" or "Analysis" if available
- Be prepared for scepticism -- the Voynich community has seen many overblown claims
- Engage with comments respectfully; do not oversell findings
- If someone points out a flaw, acknowledge it -- the paper already documents extensive failures
