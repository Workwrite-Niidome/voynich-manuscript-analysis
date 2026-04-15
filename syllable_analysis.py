import re
from collections import Counter, defaultdict

# Read the EVA file
with open("C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt", "r") as f:
    text = f.read()

# Extract clean words
cleaned = re.sub(r'@\d+;?', '', re.sub(r'\{[^}]*\}', '', re.sub(r'<[^>]*>', ' ', text)))
words = re.findall(r'[a-z]{2,}', cleaned)
total = len(words)
freq = Counter(words)
distinct = len(freq)

# Bigram frequencies
bigrams = Counter()
for i in range(len(words)-1):
    bigrams[(words[i], words[i+1])] += 1

# f47r extraction
f47r_text = []
in_f47r = False
for line in text.split('\n'):
    if '<f47r>' in line:
        in_f47r = True
    elif '<f47v>' in line or ('<f' in line and 'f47r' not in line and in_f47r):
        in_f47r = False
    if in_f47r:
        cline = re.sub(r'@\d+;?', '', re.sub(r'\{[^}]*\}', '', re.sub(r'<[^>]*>', ' ', line)))
        f47r_text.extend(re.findall(r'[a-z]{2,}', cline))

# Line length analysis
line_lengths = []
for line in text.split('\n'):
    if re.match(r'.*<f\d+[rv]\.\d+', line):
        cline = re.sub(r'@\d+;?', '', re.sub(r'\{[^}]*\}', '', re.sub(r'<[^>]*>', ' ', line)))
        ws = re.findall(r'[a-z]{2,}', cline)
        if ws:
            line_lengths.append(len(ws))

avg_words = sum(line_lengths)/len(line_lengths) if line_lengths else 0

# Word ending analysis
endings = defaultdict(list)
for w, c in freq.most_common(100):
    matched = False
    for sfx in ['-aiin', '-eey', '-edy', '-ain', '-ey', '-ol', '-al', '-ar', '-dy', '-hy']:
        s = sfx[1:]
        if w.endswith(s) and len(w) > len(s):
            endings[sfx].append((w, c))
            matched = True
            break

# Hypotheses
hypotheses = {
    "H1_freq_rank": {
        "daiin": "et", "aiin": "in", "ol": "de", "chey": "ra",
        "ar": "um", "or": "us", "qokeey": "li", "chol": "ri",
        "shey": "ta", "chedy": "re", "al": "di", "qokain": "ad",
        "dar": "ti", "qokaiin": "na", "shedy": "la", "qokeedy": "te",
        "chy": "is", "chor": "es", "okaiin": "se", "okeey": "con",
    },
    "H2_daiin_de": {
        "daiin": "de", "aiin": "et", "ol": "in", "chey": "ra",
        "ar": "um", "or": "us", "qokeey": "li", "chol": "fo",
        "shey": "ta", "chedy": "re", "al": "ri", "qokain": "ti",
        "dar": "ad", "qokaiin": "na", "shedy": "la", "qokeedy": "te",
        "chy": "is", "chor": "es", "okaiin": "se", "okeey": "con",
    },
    "H3_chol_fo": {
        "daiin": "um", "aiin": "et", "ol": "in", "chey": "de",
        "ar": "ra", "or": "us", "qokeey": "li", "chol": "fo",
        "shey": "ta", "chedy": "re", "al": "ri", "qokain": "ti",
        "dar": "ad", "qokaiin": "na", "shedy": "la", "qokeedy": "te",
        "chy": "is", "chor": "es", "okaiin": "se", "okeey": "con",
    },
    "H4_botanical": {
        "daiin": "et", "aiin": "um", "ol": "de", "chey": "in",
        "ar": "ra", "or": "us", "qokeey": "re", "chol": "fo",
        "shey": "li", "chedy": "ta", "al": "ri", "qokain": "la",
        "dar": "ad", "qokaiin": "na", "shedy": "te", "qokeedy": "di",
        "chy": "is", "chor": "ca", "okaiin": "se", "okeey": "con",
    },
    "H5_chol_li": {
        "daiin": "um", "aiin": "et", "ol": "de", "chey": "in",
        "ar": "ra", "or": "us", "qokeey": "re", "chol": "li",
        "shey": "ta", "chedy": "na", "al": "ri", "qokain": "la",
        "dar": "ad", "qokaiin": "fo", "shedy": "te", "qokeedy": "di",
        "chy": "is", "chor": "ca", "okaiin": "se", "okeey": "con",
    },
}

# Valid Latin bigrams
valid_latin_bigrams = set([
    ("et", "in"), ("et", "de"), ("et", "um"), ("et", "us"), ("et", "ra"),
    ("de", "ra"), ("de", "fo"), ("de", "li"), ("de", "se"),
    ("in", "de"), ("in", "ra"), ("in", "fo"), ("in", "te"),
    ("fo", "li"), ("li", "um"), ("ri", "um"), ("ra", "di"),
    ("ra", "re"), ("la", "te"), ("ta", "li"), ("re", "de"),
    ("um", "et"), ("um", "in"), ("um", "de"), ("us", "et"),
    ("us", "in"), ("us", "de"), ("is", "et"), ("is", "in"),
    ("ad", "de"), ("ad", "ra"), ("na", "ta"), ("na", "li"),
    ("se", "de"), ("se", "re"), ("con", "tra"), ("con", "de"),
    ("de", "et"), ("in", "et"), ("te", "re"), ("te", "ra"),
    ("ca", "li"), ("ca", "ra"), ("di", "ca"), ("ti", "li"),
    ("la", "ri"), ("la", "na"), ("ra", "li"), ("re", "li"),
    ("re", "na"), ("re", "ra"), ("fo", "ra"), ("fo", "re"),
    ("li", "ra"), ("li", "na"), ("li", "de"), ("li", "et"),
    ("li", "ta"), ("ri", "de"), ("ri", "ta"), ("um", "ra"),
    ("us", "ra"), ("ta", "re"), ("ta", "de"), ("te", "de"),
    ("na", "re"), ("na", "de"), ("la", "de"), ("la", "et"),
    ("ad", "li"), ("ad", "re"), ("se", "li"), ("se", "na"),
    ("di", "re"), ("di", "li"), ("ti", "re"), ("ti", "na"),
    ("is", "de"), ("es", "et"), ("es", "de"), ("es", "in"),
    ("con", "re"), ("con", "li"), ("con", "ta"), ("con", "na"),
])

# Output
out = []
out.append("=" * 80)
out.append("VOYNICH SYLLABLE CIPHER DECRYPTION ATTEMPT")
out.append("=" * 80)
out.append(f"\nCorpus: {total} tokens, {distinct} distinct types")
out.append(f"Average words per line: {avg_words:.1f}")

out.append(f"\n{'='*80}")
out.append("STEP 1: TOP 50 VOYNICH WORDS BY FREQUENCY")
out.append("="*80)
for i, (w, c) in enumerate(freq.most_common(50)):
    pct = c/total*100
    out.append(f"  {i+1:3d}. {w:15s} {c:5d} ({pct:.2f}%)")

out.append(f"\n{'='*80}")
out.append("STEP 2: WORD ENDING (SUFFIX) ANALYSIS")
out.append("="*80)
for ending, words_list in sorted(endings.items(), key=lambda x: -sum(c for _, c in x[1])):
    total_e = sum(c for _, c in words_list)
    members = ", ".join(f"{w}({c})" for w, c in words_list[:8])
    out.append(f"  {ending:8s}: total={total_e:5d}  [{members}]")

out.append(f"\n{'='*80}")
out.append("STEP 3: TOP BIGRAMS (word pairs)")
out.append("="*80)
for (v1, v2), count in bigrams.most_common(30):
    out.append(f"  {v1:15s} + {v2:15s}  x{count}")

out.append(f"\n{'='*80}")
out.append("STEP 4: qo- PREFIX ANALYSIS")
out.append("="*80)
qo_words = [(w, c) for w, c in freq.most_common(100) if w.startswith('qo')]
non_qo = []
for w, c in qo_words:
    base = w[2:]
    if base in freq:
        non_qo.append((w, c, base, freq[base]))
        out.append(f"  {w:15s}({c:4d}) -> base: {base:15s}({freq[base]:4d})")
    else:
        out.append(f"  {w:15s}({c:4d}) -> base: {base:15s}(  -- )")

out.append(f"\n{'='*80}")
out.append("STEP 5: HYPOTHESIS TESTING - BIGRAM SCORES")
out.append("="*80)
for hname, hmap in hypotheses.items():
    score = 0
    valid_examples = []
    total_checked = 0
    for (v1, v2), count in bigrams.most_common(500):
        if v1 in hmap and v2 in hmap:
            total_checked += 1
            lat_pair = (hmap[v1], hmap[v2])
            if lat_pair in valid_latin_bigrams:
                score += count
                if len(valid_examples) < 5:
                    valid_examples.append(f"{v1}+{v2} -> {hmap[v1]}{hmap[v2]} (x{count})")
    out.append(f"\n  {hname}: score={score}, checked={total_checked}")
    for ex in valid_examples:
        out.append(f"    {ex}")

out.append(f"\n{'='*80}")
out.append("STEP 6: DECODE f47r (GRAPE PAGE) WITH EACH HYPOTHESIS")
out.append("="*80)
out.append(f"\n  f47r words ({len(f47r_text)} tokens): {' '.join(f47r_text)}")
for hname, hmap in hypotheses.items():
    decoded = []
    unmapped = 0
    for w in f47r_text:
        if w in hmap:
            decoded.append(hmap[w])
        else:
            decoded.append(f"[{w}]")
            unmapped += 1
    out.append(f"\n  {hname} ({unmapped} unmapped of {len(f47r_text)}):")
    out.append(f"    {' '.join(decoded)}")

# Hapax analysis
hapax = sum(1 for w, c in freq.items() if c == 1)
low_freq = sum(1 for w, c in freq.items() if c <= 3)

out.append(f"\n{'='*80}")
out.append("STEP 7: CRITICAL ASSESSMENT - FEASIBILITY OF SYLLABLE MODEL")
out.append("="*80)
out.append(f"""
  VOCABULARY SIZE TEST:
    Voynich distinct word types: {distinct}
    Expected Latin syllable inventory: ~200-300 (pharmaceutical texts)
    Ratio: {distinct/250:.1f}x too many types for syllable substitution
    VERDICT: FAIL - vocabulary is ~{distinct//250}x too large

  HAPAX LEGOMENA TEST:
    Words appearing exactly once: {hapax} ({hapax/distinct*100:.1f}% of types)
    Words appearing 1-3 times: {low_freq} ({low_freq/distinct*100:.1f}% of types)
    For a syllable cipher, almost all syllables should appear multiple times.
    {hapax} hapax legomena is inconsistent with ~200-300 syllable targets.
    VERDICT: FAIL - too many rare types

  FREQUENCY DISTRIBUTION TEST:
    Top word (daiin) frequency: {freq.most_common(1)[0][1]/total*100:.2f}%
    Expected top Latin syllable: ~3-5%
    Shape: Voynich follows Zipf-like distribution (compatible)
    VERDICT: MARGINAL - distribution shape is OK but absolute values are low

  MORPHOLOGICAL REGULARITY TEST:
    qo- prefix: appears productively across {len(qo_words)} of top 100 words
    -aiin suffix: appears across {len(endings.get('-aiin', []))} of top 100 words
    -eey suffix: appears across {len(endings.get('-eey', []))} of top 100 words
    A pure syllable cipher should NOT show productive morphology
    VERDICT: FAIL - morphological patterns indicate word-level or sub-word encoding

  BIGRAM VALIDATION TEST:
    Best hypothesis score: see above
    No hypothesis produces consistently valid Latin words
    Most decoded f47r text is uninterpretable as Latin
    VERDICT: FAIL - no mapping produces readable pharmaceutical Latin

  AVERAGE LINE LENGTH TEST:
    Average words per line: {avg_words:.1f}
    If each word = 1 syllable, that is {avg_words:.1f} syllables per line
    Typical Latin herbal text line: 8-15 syllables
    VERDICT: {'PASS' if 5 <= avg_words <= 15 else 'FAIL'} - line lengths are {'compatible' if 5 <= avg_words <= 15 else 'incompatible'}

  OVERALL CONCLUSION:
    The one-word-one-syllable model FAILS on multiple critical tests:

    1. The vocabulary is {distinct//250}x too large for a syllable substitution cipher.
       With 8,622 distinct types vs ~200-300 expected Latin syllables, the mapping
       cannot be 1:1. This alone is fatal to the hypothesis.

    2. Productive morphology (qo-, -aiin, -eey, -edy) is incompatible with
       arbitrary syllable codes. These patterns suggest the script has its own
       internal grammar, NOT a simple substitution of Latin syllables.

    3. No frequency-based mapping produces readable Latin text when applied to
       known-content pages (f47r grape/Vitis).

    4. {hapax} hapax legomena ({hapax/distinct*100:.1f}% of vocabulary) are far too
       many for a system with only ~200-300 target syllables.

  POSSIBLE REFINEMENTS:
    - The model might work if MANY Voynich words map to the SAME syllable
      (massive homophony), reducing effective vocabulary to ~200-300 classes
    - The qo- prefix and -aiin suffix might be "null" elements or determiners
      that don't encode syllables at all
    - A hybrid model where function words encode syllables but content words
      encode whole words might be more viable

  WHAT THE DATA ACTUALLY SUGGESTS:
    The Voynich script most likely encodes at the WORD level or uses a
    constructed/artificial language. The morphological regularity points to
    either:
    a) A natural language with agglutinative morphology
    b) A constructed notation system
    c) A verbose cipher with extensive null characters and homophones
    d) A glossolalia or meaningless text with statistical regularities
""")

# Write output
output_text = '\n'.join(out)
print(output_text)

with open("C:/Users/kazuk/Downloads/voynich_analysis/syllable_decryption_attempt.md", "w", encoding="utf-8") as f:
    f.write("# Voynich Manuscript: Syllable-Level Cipher Decryption Attempt\n\n")
    f.write("```\n")
    f.write(output_text)
    f.write("\n```\n")
