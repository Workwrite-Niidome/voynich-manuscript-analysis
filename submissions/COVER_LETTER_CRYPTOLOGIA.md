# Cover Letter: Cryptologia

---

**To:** The Editor, *Cryptologia*

**Re:** Manuscript submission -- "Multi-Agent AI Analysis of the Voynich Manuscript: Validated Structural Constraints and the Limits of Computational Decipherment"

---

Dear Editor,

We submit for your consideration a manuscript presenting the results of a systematic computational analysis of the Voynich Manuscript (Beinecke MS 408), conducted over 20+ analysis cycles using the complete EVA transcription (37,779 tokens, 226 folios).

We believe *Cryptologia* is the ideal venue for this work, given the journal's long-standing commitment to historical cryptography and its recent publication of Greshko's analysis of the Naibbe cipher (2025), which bears directly on one of our surviving hypotheses (verbose homophonic cipher).

### Principal contributions

1. **Novel statistical finding: cross-word sandhi.** We report a previously undocumented cross-word suffix dependency in the Voynich text, whereby word-final consonant choice (n/l/r) is systematically conditioned by the following word's initial character. This finding survives 10-fold cross-validation (42.9% vs. 34.7% baseline, all folds above baseline), 1,000-iteration permutation testing (p < 0.001), and cross-split correlation (r = 0.84). The effect operates within lines but collapses across line boundaries, producing a three-layer dependency structure. This result partially refutes Rugg's (2004) simple Cardan grille hoax hypothesis, as such a mechanism cannot produce three-layer cross-word dependencies.

2. **Morphological architecture.** We characterise a 6-layer compositional word structure (prefix + classifier + root + vowel grade + terminal + suffix) with near-zero prefix-suffix coupling (NMI = 0.032), a value outside the range observed in natural languages tested (0.15--0.40 for Latin, Italian, Turkish).

3. **Vowel grade specificity hierarchy.** Vowel grades correlate with lexical specificity at r = -0.954 (R-squared = 0.910), the strongest single statistical relationship found in the text. Recipe-section enrichment increases monotonically with grade level.

4. **Rigorous methodology.** To our knowledge, this is the first Voynich study to employ:
   - Pre-registered blind prediction tests (two rounds of 10 folios each, predictions recorded before illustration examination)
   - A dedicated adversarial red-team cycle with 8 destructive tests
   - Full-scale replication of morpheme-feature associations from 30-page training sets to all 112 herbal pages
   - Complete failure reporting (12+ hypotheses eliminated, 4/5 top morpheme associations failed to replicate)

5. **Honest reporting of failures.** We document all refuted claims, including the failure of sh = underground/root (blind test accuracy 25%), the collapse of cthy = fruit and dchy = tall at full scale, and the systematic failure of negative morpheme predictions. Of 33 hypotheses tested, 10 are validated, 5 remain as hypotheses, and 18 are refuted.

### Relationship to recent literature

The paper engages directly with several works published in *Cryptologia*, including Rugg (2004), Landini (2001), and Greshko (2025). Our analysis of the Naibbe-type verbose homophonic cipher as a surviving hypothesis (25--35% confidence) provides a quantitative framework for evaluating its compatibility with the observed morphological structure.

### Manuscript details

- Word count: approximately 12,000 (including tables and appendices)
- Figures: statistical tables embedded in text
- Supplementary material: 273-file archive (analysis documents, Python scripts, data files) available upon request or via arXiv preprint
- No prior publication; an arXiv preprint may be posted concurrently

The manuscript is not under consideration elsewhere.

We confirm that the analysis was conducted computationally by Claude Opus 4.6 (Anthropic) under the direction and supervision of a human researcher. This represents, to our knowledge, the first systematic multi-agent AI analysis of the Voynich manuscript, and the methodology may be of interest to the journal's readership independently of the specific findings.

We welcome the opportunity to revise the manuscript in response to reviewer feedback.

Respectfully submitted,

[Author name]
[Affiliation]
[Contact email]
