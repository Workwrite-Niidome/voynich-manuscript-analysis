# Email Template: Voynich Researchers

---

## Template (customise the opening paragraph for each recipient)

---

**Subject:** Computational analysis of Voynich MS -- cross-word dependencies and blind prediction tests (arXiv preprint)

---

### Version 1: Lisa Fagin Davis

Dear Dr. Davis,

I am writing to share a computational analysis of the Voynich Manuscript that I believe may be relevant to your codicological work on MS 408. Your identification of five scribal hands and proposed folio reorderings informed several aspects of our analysis, and one of our validated findings -- that conjugate leaf pairs show 19% higher vocabulary coherence than sequential pairs (Jaccard 0.1070 vs. 0.0898) -- directly supports your reordering hypothesis.

[Continue with common body below]

---

### Version 2: Rene Zandbergen

Dear Mr. Zandbergen,

I am writing to share a computational analysis of the Voynich Manuscript conducted on the Takahashi-Zandbergen EVA transcription (RF1b-e.txt). Your transcription work made this analysis possible, and I wanted to bring the results to your attention, as the most comprehensive maintainer of Voynich research at voynich.nu.

[Continue with common body below]

---

### Version 3: Nick Pelling

Dear Mr. Pelling,

I am writing to share a computational analysis of the Voynich Manuscript that I believe intersects with your long-standing work on the manuscript's cipher mechanisms. Our analysis of cross-word suffix dependencies and measurement system paradigms may be relevant to the cipher hypotheses you have explored on Cipher Mysteries.

[Continue with common body below]

---

### Version 4: Michael Greshko

Dear Mr. Greshko,

I am writing to share a computational analysis of the Voynich Manuscript that engages directly with your work on the Naibbe cipher (Cryptologia, 2025). One of our four surviving hypotheses -- verbose homophonic cipher at 25--35% confidence -- is explicitly framed as a "Naibbe-type" mechanism. Our morphological findings provide specific constraints that any Naibbe-type explanation would need to satisfy.

[Continue with common body below]

---

### Common Body

Over 20+ analysis cycles, we conducted a systematic computational analysis of the complete EVA transcription (37,779 tokens, 226 folios), testing 33 hypotheses and producing 273 analytical files. The preprint is available at: [arXiv:XXXX.XXXXX]

I am reaching out because I believe the findings may be useful to the Voynich research community, and I would value your perspective.

**Key validated findings:**

1. A previously unreported cross-word suffix dependency ("sandhi") in which word-final n/l/r choice is conditioned by the following word's initial (10-fold CV: 42.9% vs. 34.7% baseline, p < 0.001). This operates within lines but not across line boundaries.

2. A vowel grade specificity hierarchy with r = -0.954, meaning 91% of the variance in how widely a word appears is explained by its vowel grade.

3. Near-zero prefix-suffix coupling (NMI = 0.032), lower than any natural language tested.

**Key failures (equally important):**

- 4 of 5 morpheme-feature associations failed when scaled from 30-page training sets to all 112 herbal pages
- The sh = underground/root hypothesis was refuted by blind prediction testing (25% accuracy)
- No phonetic recovery was achieved for any anchor plant name
- The manuscript remains undeciphered

**Methodological innovations:**

- Pre-registered blind prediction tests (a first in Voynich studies)
- Adversarial red-team review with 8 destructive tests
- Complete failure reporting alongside successes

The analysis was conducted using Claude Opus 4.6 (Anthropic) under my direction. I am transparent about this and about the limitation that all analysis was performed by the same model, so true multi-agent independence was not achieved.

I would be grateful for any feedback, criticism, or suggestions for further validation. I am particularly interested in:
- Whether the cross-word sandhi pattern has been observed before
- Whether the measurement system paradigm (qo-k) resonates with known pharmaceutical conventions
- Any methodological concerns I may have overlooked

The full 273-file archive is available upon request.

Thank you for your time and for your contributions to Voynich research.

Best regards,

[Name]
[Contact email]

---

## Sending Notes

- Send individually, not as a group email
- Customise the opening paragraph for each recipient as shown above
- Do NOT attach the full paper -- link to arXiv instead (reduces spam filter risk)
- Keep the tone professional and humble; these researchers have decades of experience
- Do not claim decipherment or breakthrough -- the paper explicitly does not
- Be prepared for no response; these researchers receive many Voynich-related emails
- If using a pseudonym for anonymity, consider creating a dedicated academic email address
