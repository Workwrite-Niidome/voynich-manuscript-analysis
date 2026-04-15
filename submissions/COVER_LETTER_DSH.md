# Cover Letter: Digital Scholarship in the Humanities

---

**To:** The Editor, *Digital Scholarship in the Humanities* (Oxford University Press)

**Re:** Manuscript submission -- "Multi-Agent AI Analysis of the Voynich Manuscript: Validated Structural Constraints and the Limits of Computational Decipherment"

---

Dear Editor,

We submit for your consideration a manuscript describing a systematic computational analysis of the Voynich Manuscript (Beinecke MS 408, ca. 1404--1438) using iterative AI-driven hypothesis generation and destruction. We believe *Digital Scholarship in the Humanities* is an appropriate venue given the paper's dual contributions: substantive findings about an important historical artefact, and methodological innovations in AI-assisted textual analysis.

### Computational methodology

The investigation employed Claude Opus 4.6 (Anthropic, 1M token context window) over 20+ analysis cycles following a generate-test-destroy protocol. The complete EVA transcription (37,779 tokens, 8,500 unique types, 226 folios) was analysed, producing 273 files comprising analysis documents, Python scripts, and intermediate data.

Key methodological innovations include:

1. **Iterative hypothesis-destruction.** Each cycle attempted to falsify survivors of previous cycles. Of 33 hypotheses tested, 18 were eliminated with documented evidence, 10 were validated through cross-validation and permutation testing, and 5 remain as promising but unconfirmed hypotheses.

2. **Pre-registered blind prediction testing** -- a first in Voynich studies and, to our knowledge, rare in computational analysis of undeciphered texts. Two rounds of 10 folios each, with all predictions recorded before illustration examination. This protocol revealed that 4 of 5 top morpheme-feature associations, which showed strong chi-squared values on 30-page training sets, failed to replicate at full scale (112 pages).

3. **Adversarial red-team review.** A dedicated analysis cycle attacked all claims with 8 destructive tests, reducing confidence levels by 20--40 percentage points on most claims and identifying circular reasoning chains.

4. **Reproducibility.** All statistical tests (chi-squared, permutation n=1000, 10-fold cross-validation, Fisher exact, Bonferroni correction) are fully specified. All Python scripts and intermediate data files are included in a 273-file supplementary archive.

### Relevance to digital humanities

This work demonstrates both the power and the limitations of large language models as analytical tools for historical texts:

- **Power**: The AI system identified a previously unreported cross-word statistical dependency (chi-squared = 1,404, p ~ 10^-278) and a vowel grade specificity hierarchy (r = -0.954) that had not been found in over a century of study.

- **Limitations**: The same system exhibited confirmation bias (the sh = underground/root claim persisted through multiple cycles before blind testing refuted it), produced inflated statistics from small samples (4/5 morpheme associations failed at full scale), and could not achieve true multi-agent independence (all "agents" shared the same model and training data).

The honest documentation of these failures may be as valuable to the digital humanities community as the positive findings, providing a case study in responsible AI-assisted scholarship.

### Substantive findings

The validated findings include: cross-word suffix dependencies surviving 10-fold cross-validation; a 6-layer compositional morphological architecture; a vowel grade specificity hierarchy; within-page template structure; a measurement system paradigm; and non-random morpheme distributions (14/15 surviving Bonferroni correction across 6,384 possible substrings).

### Manuscript details

- Word count: approximately 12,000 (including tables and appendices)
- Supplementary archive: 273 files (analysis documents, Python scripts, data files)
- Data availability: all analysis scripts and intermediate results available; primary corpus (EVA transcription) is publicly available
- No prior publication; an arXiv preprint may be posted concurrently
- The manuscript is not under consideration elsewhere

Respectfully submitted,

[Author name]
[Affiliation]
[Contact email]
