# arXiv Preprint Metadata and Preparation

---

## Submission Metadata

- **Title:** Multi-Agent AI Analysis of the Voynich Manuscript: Validated Structural Constraints and the Limits of Computational Decipherment
- **Authors:** Anonymous (direction and supervision), Claude Opus 4.6 (computational analysis, Anthropic)
- **Primary category:** cs.CL (Computation and Language)
- **Cross-list categories:** cs.AI (Artificial Intelligence), cs.DL (Digital Libraries)
- **Comments:** 40+ pages including appendices; 273-file supplementary archive; two pre-registered blind prediction tests; adversarial red-team review
- **MSC classes:** 94A60 (Cryptography), 68T50 (Natural Language Processing)
- **License:** CC BY 4.0

---

## Abstract

The Voynich Manuscript (Beinecke MS 408, radiocarbon-dated 1404--1438) has resisted decipherment for over a century. We present a systematic computational analysis of its full EVA transcription (37,779 tokens, 8,500 unique types, 226 folios) using iterative hypothesis-generation and adversarial hypothesis-destruction cycles across 20+ analysis cycles, comprising over 273 analytical files, two pre-registered blind prediction tests, a dedicated red-team review, full-scale morpheme validation on 112 herbal pages, pharmaceutical encoding tests, within-page structure analysis, and measurement system validation.

Our methodology introduces blind prediction testing to Voynich studies -- a first in the field. Of 33 hypotheses tested, 18 were eliminated, producing a clear separation between validated structural findings, promising hypotheses, and refuted claims.

Validated findings (survived all tests): (1) cross-word sandhi in suffix selection (10-fold CV, 42.9% vs. 34.7% baseline, p < 0.001, Cramer's V = 0.22); (2) a 6-layer compositional morphological architecture with near-zero prefix-suffix coupling (NMI = 0.032); (3) vowel grade encoding lexical specificity (r = -0.954); (4) within-page template structure with -dy/-ol suffix crossover at line 7--8 (chi-squared < 0.001); (5) 93% unique first words on herbal pages; (6) a qo-k measurement system with doubling, position, and context coherence; (7) ty as a validated predictor of linear-leaved plants (Fisher p = 0.008, OR = 18.0); (8) headache-pair vocabulary sharing at 99th percentile (p < 0.01); (9) 14/15 morpheme substrings with non-random page distributions surviving Bonferroni correction; and (10) 8/8 compound classifier compositionality matches.

Refuted claims include: sh = underground/root (blind test 25%), cthy = fruit (full-scale p = 0.66), dchy = tall (p = 1.0), full-scale word-illustration correlation failure, drachma:ounce ratio mismatch, and pharmaceutical encoding (1/5 tests support). Complete failure reporting is provided for all 18 eliminated hypotheses.

The manuscript remains undeciphered. However, the validated findings constrain the solution space and demonstrate genuine linguistic or notational structure incompatible with simple hoax mechanisms.

**Keywords:** Voynich Manuscript, computational linguistics, historical cryptography, undeciphered writing systems, morphological analysis, AI-assisted analysis, blind prediction testing

---

## Data Availability Statement

All analysis files produced during this investigation are available as a supplementary archive comprising 273 files:

- **Core analysis documents:** 35+ Markdown files documenting findings, hypotheses, and validations
- **Python analysis scripts:** 73 scripts implementing all statistical tests (chi-squared, permutation, cross-validation, Fisher exact, mutual information, correlation analysis)
- **Hypothesis test documents:** 20+ files documenting each tested and eliminated hypothesis
- **Cycle reports:** 12 files documenting the iterative analysis process
- **Blind prediction test records:** Complete pre-registered predictions with scoring
- **Red-team review:** Full adversarial analysis with 8 destructive tests
- **Data files:** Intermediate JSON/TXT outputs from all analyses

The primary corpus (EVA transcription RF1b-e.txt by Takahashi-Zandbergen) is publicly available from voynich.nu.

The supplementary archive is available from the corresponding author upon request. We intend to release it publicly via a permanent repository (e.g., Zenodo) upon acceptance at a peer-reviewed venue.

---

## Full Paper

[The full text of FINAL_PAPER_v3.md should be inserted here for the arXiv submission, with the following modifications:]

1. Replace the author line with: "Anonymous (direction and supervision), Claude Opus 4.6 (computational analysis, Anthropic)"
2. Add the Data Availability Statement above as a new section before References
3. Add the following Acknowledgements section:

### Acknowledgements

This analysis was conducted using Claude Opus 4.6 (1M context) provided by Anthropic. The EVA transcription was produced by Gabriel Takahashi and Rene Zandbergen and is publicly available. The Voynich Manuscript digital facsimile is provided by the Beinecke Rare Book and Manuscript Library at Yale University under a CC0 license.

We acknowledge the extensive prior work of the Voynich research community, particularly the transcription efforts that made this analysis possible, Lisa Fagin Davis's codicological studies, and Jorge Stolfi's foundational structural analyses.

---

## Submission Notes

### For arXiv formatting:
- The paper is written in Markdown and can be converted to LaTeX using pandoc
- All tables should be formatted as LaTeX tables
- Statistical formulas should use standard LaTeX math notation
- The 273-file archive should be referenced as "Supplementary Material" with a note that it will be deposited in a permanent repository

### Recommended conversion command:
```
pandoc FINAL_PAPER_v3.md -o voynich_analysis.tex --template=arxiv_template.tex
```

### Category justification:
- **cs.CL** (primary): The paper presents computational linguistic analysis including morphological decomposition, cross-word dependencies, information-theoretic measures (mutual information, entropy), and distributional semantics
- **cs.AI** (cross-list): The methodology demonstrates AI-assisted scientific investigation with iterative hypothesis generation and destruction
- **cs.DL** (cross-list): The work contributes to digital analysis of historical manuscripts
