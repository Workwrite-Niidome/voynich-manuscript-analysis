# Submission Guide

Step-by-step instructions for submitting to each venue.

---

## 1. arXiv (IMMEDIATE -- no peer review required)

### Account Creation
1. Go to https://arxiv.org/user/register
2. Create an account with an institutional or academic email if possible (Gmail is accepted but may trigger manual review)
3. You will need an **endorsement** for cs.CL if you have not published there before:
   - Ask a colleague who has published in cs.CL to endorse you
   - Alternatively, submit to cs.AI (lower endorsement bar) and cross-list to cs.CL
   - If no endorser is available, email arxiv-moderation@cornell.edu explaining your situation
4. Account activation takes 1--3 business days

### Submission Process
1. Convert the paper from Markdown to LaTeX:
   ```
   pandoc FINAL_PAPER_v3.md -o voynich_analysis.tex
   ```
2. Clean up the LaTeX output (tables, math notation, references)
3. Use the standard article documentclass or arxiv's preferred template
4. Package all files into a .tar.gz or .zip:
   - Main .tex file
   - Any figures (if added)
   - References .bib file
5. Go to https://arxiv.org/submit
6. Select primary category: **cs.CL** (Computation and Language)
7. Add cross-list categories: cs.AI, cs.DL
8. Paste the abstract
9. Upload the package
10. Set license to CC BY 4.0
11. Submit and wait for moderation (typically 1--2 business days)

### Anonymity
- arXiv requires author identification (real name linked to account)
- However, you can use a pseudonym in the paper itself
- The account email is not publicly visible
- Consider: arXiv papers are often linked to ORCID -- decide whether to link

### Supplementary Data
- arXiv has a 50MB upload limit; the 273-file archive likely exceeds this
- Upload the paper to arXiv; host the archive separately:
  - **Zenodo** (https://zenodo.org): free, DOI-minted, permanent. Best option.
  - **GitHub**: create a public repository with the archive
  - **Figshare** (https://figshare.com): free, DOI-minted
- Reference the external archive URL in the Data Availability section

---

## 2. Cryptologia (Taylor & Francis)

### Journal Information
- Publisher: Taylor & Francis
- ISSN: 0161-1194 (print), 1558-1586 (online)
- Focus: historical and mathematical cryptology
- Impact factor: niche journal, but THE venue for historical cryptography
- Turnaround: 3--6 months typical

### Submission Portal
1. Go to https://www.tandfonline.com/action/authorSubmission?journalCode=ucry20
2. Create a Taylor & Francis account
3. Select "Submit a Manuscript"
4. Follow the ScholarOne submission workflow

### Formatting Requirements
- LaTeX or Word format (LaTeX preferred)
- Taylor & Francis template: https://www.tandf.co.uk/journals/authors/style/layout/style_UCRY.pdf
- Double-spaced, 12pt font
- References in numbered format (journal style)
- Tables and figures at end of document or inline (check current author guidelines)
- No page limit specified, but 12,000 words is at the upper end; consider trimming

### Cover Letter
- Use COVER_LETTER_CRYPTOLOGIA.md (convert to plain text or PDF)
- Address to "The Editor" unless you can identify the current editor-in-chief

### Anonymity
- Cryptologia uses single-blind review (reviewers know author identity)
- You can request double-blind if available
- Author name appears on the submission but can be a pseudonym if legally permissible

### Post-Submission
- Expect 2--3 reviewers
- Be prepared for revisions (R&R is the most common outcome for Voynich papers)
- Reviewers will likely include Voynich scholars who may be sceptical -- the honest failure reporting should help

---

## 3. Digital Scholarship in the Humanities (Oxford University Press)

### Journal Information
- Publisher: Oxford University Press
- ISSN: 2055-7671 (online)
- Focus: computational approaches to humanities research
- Impact factor: ~1.5 (moderate for digital humanities)
- Turnaround: 4--8 months

### Submission Portal
1. Go to https://academic.oup.com/dsh/pages/General_Instructions
2. Submit via ScholarOne: https://mc.manuscriptcentral.com/dsh
3. Create account if needed

### Formatting Requirements
- Word or LaTeX format
- OUP house style for references
- Abstract max 250 words (current paper abstract needs trimming)
- Main text should be under 10,000 words (trim appendices to supplementary)
- Supplementary material uploaded separately

### Cover Letter
- Use COVER_LETTER_DSH.md

### Anonymity
- DSH uses double-blind review
- Remove all author-identifying information from the manuscript
- Replace author references with "[Author]" or "[removed for review]"
- Do not reference your own arXiv preprint in the submitted version (link would identify you)

---

## 4. Nature

### Journal Information
- Publisher: Springer Nature
- Impact factor: ~64 (among the highest in science)
- Acceptance rate: ~8%
- Turnaround: initial editorial decision in 1--2 weeks (most rejections are desk rejections)

### Submission Process
1. Go to https://mts-nature.nature.com/
2. Create a Springer Nature account
3. Submit as an "Article" (not Letter or Brief Communication)
4. Select subject: "Mathematics and computing" > "Computer science"

### Formatting Requirements
- Main text: max 5,000 words (SIGNIFICANT trimming required from current 12,000)
- Methods section: separate, no word limit
- Extended data: up to 10 figures/tables
- Supplementary information: no limit
- References: max 50 (current paper has 12 -- this is fine)
- Abstract: max 150 words (current abstract needs trimming)
- The paper would need substantial restructuring for Nature format

### Cover Letter
- Use COVER_LETTER_NATURE.md
- Nature cover letters should be under 1 page
- Suggest 2--3 potential reviewers (but not people you've contacted)

### Anonymity
- Nature uses single-blind review
- Author identity is known to reviewers
- Consider using a pseudonym if anonymity is critical

### Realistic Expectations
- Desk rejection is highly likely (~92% of submissions)
- If desk-rejected, try Nature Communications (broader scope, higher acceptance)
- The "AI methodology" angle is the strongest hook for Nature editors

---

## 5. Wikipedia

### Editing Guidelines
1. Create a Wikipedia account at https://en.wikipedia.org/wiki/Special:CreateAccount
   - Use a pseudonymous username (standard practice)
   - Do not use a username that suggests affiliation with the research
2. Wait a few days and make some minor edits to other articles first (establishes good faith)
3. Read WP:RS (Reliable Sources) and WP:NPOV (Neutral Point of View)

### Adding the Section
1. Navigate to https://en.wikipedia.org/wiki/Voynich_manuscript
2. Click "Edit" on the relevant section (likely "Theories" or "Analysis")
3. Add the section from WIKIPEDIA_DRAFT.md, converting to wikitext markup
4. Use `<ref>` tags for citations
5. Preview, then submit with an edit summary like: "Add section on 2026 AI structural analysis (arXiv:XXXX.XXXXX)"

### Important Wikipedia Policies
- **WP:SELFCITE**: Citing your own work is permitted but must be used sparingly and transparently
- **WP:COI**: If you have a conflict of interest (you are the author), you should:
  - Disclose your COI on the article's Talk page
  - Propose the edit on the Talk page first and let other editors add it
  - Do NOT add the section directly if you are the paper's author
- **WP:RSPRIMARY**: An arXiv preprint is a primary source. Wikipedia prefers secondary sources (news coverage, review papers). Consider waiting until the press release generates coverage.
- **WP:WEIGHT**: The section should be proportional to the significance of the work. Start small.

### Recommended Approach
1. Post the arXiv preprint and press release first
2. Wait for any media coverage or academic discussion
3. Then propose the Wikipedia edit on the article's Talk page, citing both the preprint AND any secondary coverage
4. Let other editors decide whether to include it

---

## 6. Reddit

### Posting Guidelines

#### r/voynich
- Subreddit: https://www.reddit.com/r/voynich/
- Small but knowledgeable community (~5k members)
- Tolerant of new research but sceptical of "solution" claims
- Post as a text post (not link post) using REDDIT_POST.md
- Flair appropriately if flair options exist

#### r/cryptography
- Subreddit: https://www.reddit.com/r/cryptography/
- Larger community (~200k members)
- More technically oriented
- Cross-post from r/voynich or adapt the post to emphasise cryptographic methodology

#### Additional subreddits to consider:
- r/linguistics -- for the morphological findings
- r/ArtificialIntelligence -- for the AI methodology angle
- r/history -- for the historical context

### Anonymity on Reddit
- Create a new Reddit account with a pseudonymous username
- Do not link to any personal social media
- Do not reveal identifying information in comments
- Reddit accounts are essentially anonymous by default

### Timing
- Post after the arXiv preprint is live (so you can link to it)
- Post on a weekday morning (US time) for maximum visibility
- Engage with comments within the first 2--3 hours

---

## 7. Email to Researchers

### Preparation
1. Create a dedicated email address for this research if anonymity is desired
   - ProtonMail or Tutanota for privacy
   - Or a university/institutional email if available
2. Post the arXiv preprint first (so you have a link to share)
3. Send emails individually, not as a group

### Timing
- Send 1--2 days after the arXiv preprint goes live
- Send on a weekday (Tuesday--Thursday is optimal)
- Space out the emails by a few hours to avoid appearing like spam

### Finding Contact Information
- **Lisa Fagin Davis**: Medieval Academy of America; search her institutional page
- **Rene Zandbergen**: Contact via voynich.nu
- **Nick Pelling**: Contact via ciphermysteries.com
- **Michael Greshko**: Search for his academic/institutional email or contact via journal

### Use the templates in EMAIL_VOYNICH_RESEARCHERS.md

---

## 8. Overall Submission Timeline

### Recommended Order

| Step | Action | When |
|------|--------|------|
| 1 | Create arXiv account, prepare LaTeX version | Day 1--3 |
| 2 | Upload supplementary archive to Zenodo | Day 2--3 |
| 3 | Submit to arXiv | Day 3 |
| 4 | arXiv preprint goes live | Day 4--6 |
| 5 | Send emails to researchers | Day 5--7 |
| 6 | Post to Reddit | Day 5--7 |
| 7 | Issue press release | Day 7--10 |
| 8 | Submit to Cryptologia | Day 7--14 |
| 9 | Submit to DSH (if Cryptologia desk-rejects) | Day 14--21 |
| 10 | Submit to Nature (long shot) | Day 7--14 (parallel) |
| 11 | Propose Wikipedia edit (after media coverage) | Day 30+ |

### Dual Submission Policy
- arXiv is a preprint server, not a journal -- posting there does NOT prevent journal submission
- Cryptologia, DSH, and Nature all accept papers with arXiv preprints
- Do NOT submit to both Cryptologia and DSH simultaneously (one at a time)
- Nature can be submitted in parallel with Cryptologia (different publisher, different scope)

### Anonymity Checklist
- [ ] Pseudonymous arXiv account (or decide to use real name)
- [ ] Pseudonymous Reddit account
- [ ] Pseudonymous Wikipedia account
- [ ] Dedicated email address for researcher correspondence
- [ ] No personal identifying information in the paper text
- [ ] No links between pseudonym and real identity on social media
- [ ] Consider: arXiv requires real name on account but allows pseudonym in paper
- [ ] Note: journal submission (Cryptologia, DSH, Nature) typically requires real name for peer review

---

## 9. Format Conversion Notes

### Markdown to LaTeX
```bash
pandoc FINAL_PAPER_v3.md -o voynich_analysis.tex --standalone
```

### Markdown to Word (for DSH)
```bash
pandoc FINAL_PAPER_v3.md -o voynich_analysis.docx
```

### Markdown to PDF (for email attachments)
```bash
pandoc FINAL_PAPER_v3.md -o voynich_analysis.pdf --pdf-engine=xelatex
```

### Key conversion issues to watch for:
- Tables may need manual cleanup in LaTeX
- Mathematical notation (chi-squared, correlation coefficients) should use proper LaTeX math mode
- The pipe-delimited Markdown tables may not convert cleanly -- verify all tables
- References should be converted to BibTeX format for LaTeX submissions
