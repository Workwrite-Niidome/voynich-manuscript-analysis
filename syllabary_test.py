import re
from collections import Counter, defaultdict
import math

# Read the EVA transcription
with open("C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt", "r", encoding="utf-8") as f:
    raw = f.read()

# Extract only text content (remove markup)
def extract_words(text):
    words = []
    for line in text.split("\n"):
        if line.startswith("#") or not line.strip():
            continue
        m = re.match(r'<[^>]+>\s+(.*)', line)
        if m:
            content = m.group(1)
        else:
            continue
        content = re.sub(r'\{[^}]+\}', '', content)
        content = re.sub(r'@\d+;?', '', content)
        content = re.sub(r'[<>\-,?\'"{}]', ' ', content)
        for w in re.split(r'[\s.]+', content):
            w = w.strip()
            if w and len(w) > 0 and re.match(r'^[a-z]+$', w):
                words.append(w)
    return words

words = extract_words(raw)
all_text = ''.join(words)

print(f"Total words extracted: {len(words)}")
print(f"Unique words: {len(set(words))}")
print(f"Total characters: {len(all_text)}")
print(f"Average word length: {sum(len(w) for w in words)/len(words):.2f}")
print()

# ============================================================
# 1. COUNT DISTINCT EVA CHARACTER BIGRAMS
# ============================================================
print("=" * 70)
print("1. DISTINCT EVA CHARACTER BIGRAMS")
print("=" * 70)

bigram_counter = Counter()
for w in words:
    for i in range(len(w) - 1):
        bigram_counter[w[i:i+2]] += 1

print(f"Distinct bigrams (within words): {len(bigram_counter)}")
print()
print("Top 40 most frequent bigrams:")
total_bg = sum(bigram_counter.values())
for bg, cnt in bigram_counter.most_common(40):
    print(f"  {bg}: {cnt} ({cnt/total_bg*100:.2f}%)")
print()

# ============================================================
# 2. BIGRAM-AS-SYLLABLE FREQUENCY MAPPING
# ============================================================
print("=" * 70)
print("2. BIGRAM-AS-SYLLABLE MAPPING TO ITALIAN")
print("=" * 70)

italian_top_syllables = [
    "la", "re", "di", "to", "ta", "ti", "no", "ne", "le", "ri",
    "co", "ra", "na", "te", "se", "si", "ro", "li", "de", "ni"
]

top_20_bigrams = [bg for bg, _ in bigram_counter.most_common(20)]

print(f"\nFrequency-rank mapping (EVA bigram -> Italian syllable):")
for i, (bg, it) in enumerate(zip(top_20_bigrams, italian_top_syllables)):
    cnt = bigram_counter[bg]
    print(f"  Rank {i+1}: EVA '{bg}' ({cnt}) -> Italian '{it}'")

bigram_to_italian = dict(zip(top_20_bigrams, italian_top_syllables))
print()

# ============================================================
# 3. GLYPH COMBINATION INVENTORY
# ============================================================
print("=" * 70)
print("3. GLYPH COMBINATION INVENTORY")
print("=" * 70)

char_counter = Counter(all_text)
print(f"\nDistinct single characters: {len(char_counter)}")
print("Single character frequencies:")
for c, cnt in char_counter.most_common():
    print(f"  '{c}': {cnt} ({cnt/len(all_text)*100:.2f}%)")

single_glyphs = sorted(set(all_text))
print(f"\nSingle glyphs ({len(single_glyphs)}): {single_glyphs}")

print(f"\nDouble combinations (top 30):")
for bg, cnt in bigram_counter.most_common(30):
    print(f"  '{bg}': {cnt}")

trigram_counter = Counter()
for w in words:
    for i in range(len(w) - 2):
        trigram_counter[w[i:i+3]] += 1

print(f"\nDistinct trigrams: {len(trigram_counter)}")
print(f"Triple combinations (top 30):")
for tg, cnt in trigram_counter.most_common(30):
    print(f"  '{tg}': {cnt}")

# Quad-grams
quadgram_counter = Counter()
for w in words:
    for i in range(len(w) - 3):
        quadgram_counter[w[i:i+4]] += 1

print(f"\nDistinct quadgrams: {len(quadgram_counter)}")
print(f"Quad combinations (top 20):")
for qg, cnt in quadgram_counter.most_common(20):
    print(f"  '{qg}': {cnt}")

print()

# ============================================================
# 4. SYLLABIC SEGMENTATION AND DECODING TEST
# ============================================================
print("=" * 70)
print("4. SYLLABIC SEGMENTATION AND DECODING TEST")
print("=" * 70)

# Define syllabic units - ordered longest first for greedy matching
syllabic_units = [
    # 4-char
    'aiin', 'eiin', 'oiin', 'chol', 'chor', 'shor', 'shol', 'dain',
    'chey', 'ched', 'ches', 'chet', 'shey', 'shed', 'shod', 'ckhy',
    'cthy', 'cpho', 'cfho',
    # 3-char
    'chy', 'shy', 'cth', 'cph', 'cfh', 'ckh',
    'ain', 'iin', 'een', 'eey',
    'cho', 'che', 'cha', 'chi',
    'sho', 'she', 'sha', 'shi',
    'dai', 'ota', 'ote', 'oto',
    'qok', 'qot', 'qop', 'qod',
    # 2-char
    'ch', 'sh', 'ck', 'ct', 'cp', 'cf',
    'ai', 'ii', 'ee', 'ey', 'dy',
    'ol', 'or', 'al', 'ar', 'an', 'am',
    'in', 'ok', 'ot', 'qo', 'da',
    'sy', 'hy', 'ho', 'he',
    # 1-char
    'a', 'e', 'i', 'o', 'y', 'd', 'k', 'l', 'm', 'n',
    'p', 'r', 's', 't', 'f', 'g', 'q', 'j', 'h'
]

def segment_word(word):
    units = []
    pos = 0
    while pos < len(word):
        matched = False
        for unit in syllabic_units:
            if word[pos:pos+len(unit)] == unit:
                units.append(unit)
                pos += len(unit)
                matched = True
                break
        if not matched:
            units.append(word[pos])
            pos += 1
    return units

segmented = [(w, segment_word(w)) for w in words]

unit_counter = Counter()
for _, units in segmented:
    for u in units:
        unit_counter[u] += 1

print(f"Distinct syllabic units used: {len(unit_counter)}")
print(f"\nAll syllabic units by frequency:")
for u, cnt in unit_counter.most_common():
    print(f"  '{u}': {cnt}")

print(f"\nSample word segmentations:")
sample_words = ['chol', 'daiin', 'shol', 'chor', 'qokeey', 'otaiin',
                'chodaiin', 'shody', 'cthor', 'dain', 'chey', 'okaiin',
                'chololy', 'shodaiin', 'qotchol', 'ykchy']
for w in sample_words:
    units = segment_word(w)
    print(f"  {w} -> {units} ({len(units)} syllables)")

syllable_counts = [len(units) for _, units in segmented]
avg_syl = sum(syllable_counts) / len(syllable_counts)
print(f"\nAverage syllabic units per word: {avg_syl:.2f}")
print(f"Distribution of syllable counts:")
sc_counter = Counter(syllable_counts)
for sc in sorted(sc_counter.keys()):
    print(f"  {sc} units: {sc_counter[sc]} words ({sc_counter[sc]/len(words)*100:.1f}%)")
print()

# ============================================================
# 5. TEXT DENSITY: WORDS PER PAGE
# ============================================================
print("=" * 70)
print("5. TEXT DENSITY: WORDS PER PAGE")
print("=" * 70)

page_words = defaultdict(list)
current_page = None
for line in raw.split("\n"):
    m = re.match(r'<(f\d+[rv])', line)
    if m:
        current_page = m.group(1)
    m2 = re.match(r'<([^>]+)>\s+(.*)', line)
    if m2:
        tag = m2.group(1)
        page_id = tag.split('.')[0].strip('<')
        if not page_id.startswith('f'):
            continue
        content = m2.group(2)
        content = re.sub(r'\{[^}]+\}', '', content)
        content = re.sub(r'@\d+;?', '', content)
        content = re.sub(r'[<>\-,?\'"{}]', ' ', content)
        for w in re.split(r'[\s.]+', content):
            w = w.strip()
            if w and re.match(r'^[a-z]+$', w):
                page_words[page_id].append(w)

print(f"Total pages: {len(page_words)}")
word_counts = [len(ws) for ws in page_words.values()]
if word_counts:
    print(f"Words per page: min={min(word_counts)}, max={max(word_counts)}, avg={sum(word_counts)/len(word_counts):.1f}")

print("\nHerbal section pages (sample):")
for page in sorted(page_words.keys())[:20]:
    print(f"  {page}: {len(page_words[page])} words")
print()

# ============================================================
# 6. C-V ALTERNATION PATTERN
# ============================================================
print("=" * 70)
print("6. C-V ALTERNATION PATTERN ANALYSIS")
print("=" * 70)

eva_vowels = set('aeiouy')
eva_consonants = set('cdklmnprstfgqj')

def cv_pattern(word):
    pattern = []
    for c in word:
        if c in eva_vowels:
            pattern.append('V')
        elif c in eva_consonants:
            pattern.append('C')
        else:
            pattern.append('?')
    return ''.join(pattern)

cv_patterns = Counter()
for w in words:
    p = cv_pattern(w)
    cv_patterns[p] += 1

print("Top 30 C-V patterns:")
for p, cnt in cv_patterns.most_common(30):
    example = next((w for w in words if cv_pattern(w) == p), "?")
    print(f"  {p}: {cnt} (e.g., '{example}')")

cv_pair_count = 0
total_pairs = 0
for w in words:
    p = cv_pattern(w)
    for i in range(0, len(p) - 1):
        total_pairs += 1
        if p[i:i+2] == 'CV':
            cv_pair_count += 1

print(f"\nCV pair ratio: {cv_pair_count}/{total_pairs} = {cv_pair_count/total_pairs*100:.1f}%")

h_context = Counter()
for w in words:
    for i, c in enumerate(w):
        if c == 'h':
            prev = w[i-1] if i > 0 else '^'
            nxt = w[i+1] if i < len(w) - 1 else '$'
            h_context[f"{prev}_h_{nxt}"] += 1

print(f"\nContexts of 'h' (top 20):")
for ctx, cnt in h_context.most_common(20):
    print(f"  {ctx}: {cnt}")
print()

# ============================================================
# 7. FREQUENCY-MATCHED DECODING ON HERBAL PAGES
# ============================================================
print("=" * 70)
print("7. FREQUENCY-MATCHED DECODING TEST")
print("=" * 70)

# Check available pages
grape_pages = [p for p in sorted(page_words.keys()) if p.startswith('f4')]
print(f"Pages starting with f4: {grape_pages}")

# Build mapping from most frequent syllabic units to Italian syllables
italian_syllables_extended = [
    "re", "la", "di", "to", "ta", "ti", "no", "ne", "le", "ri",
    "co", "ra", "na", "te", "se", "si", "ro", "li", "de", "ni",
    "me", "al", "lo", "ma", "in", "pa", "en", "un", "so", "an",
    "ca", "per", "che", "con", "del", "il", "io", "da", "er", "es",
    "tu", "do", "po", "ve", "vi", "gi", "mo", "fa", "va", "sa",
    "pi", "fi", "ce", "ci", "mi", "bi", "ge", "su", "or", "uo"
]

top_units = [u for u, _ in unit_counter.most_common(len(italian_syllables_extended))]
unit_to_italian = dict(zip(top_units, italian_syllables_extended))

print(f"\nSyllabic unit -> Italian syllable mapping (top {min(len(top_units), len(italian_syllables_extended))}):")
for u, it in list(unit_to_italian.items())[:30]:
    print(f"  '{u}' -> '{it}'")

# Decode f1r
print(f"\nDecoding attempt on f1r:")
f1r_words = page_words.get('f1r', [])
for w in f1r_words[:20]:
    units = segment_word(w)
    decoded = ''.join(unit_to_italian.get(u, f'[{u}]') for u in units)
    print(f"  {w} -> {units} -> {decoded}")

# Try herbal pages
for test_page in ['f47r', 'f47v', 'f25r', 'f25v', 'f2r']:
    if test_page in page_words:
        print(f"\nDecoding attempt on {test_page}:")
        for w in page_words[test_page][:15]:
            units = segment_word(w)
            decoded = ''.join(unit_to_italian.get(u, f'[{u}]') for u in units)
            print(f"  {w} -> {units} -> {decoded}")
        break
print()

# ============================================================
# ENTROPY ANALYSIS
# ============================================================
print("=" * 70)
print("ENTROPY ANALYSIS OF SYLLABIC UNITS")
print("=" * 70)

total_units_count = sum(unit_counter.values())
unit_entropy = -sum((cnt/total_units_count) * math.log2(cnt/total_units_count) for cnt in unit_counter.values())
max_entropy = math.log2(len(unit_counter))
print(f"Syllabic unit unigram entropy: {unit_entropy:.2f} bits")
print(f"Max possible entropy ({len(unit_counter)} units): {max_entropy:.2f} bits")
print(f"Efficiency: {unit_entropy/max_entropy*100:.1f}%")

# Character-level entropy for comparison
char_total = sum(char_counter.values())
char_entropy = -sum((cnt/char_total) * math.log2(cnt/char_total) for cnt in char_counter.values())
print(f"\nCharacter-level entropy: {char_entropy:.2f} bits")
print(f"Syllabic unit entropy: {unit_entropy:.2f} bits")
print(f"Ratio (unit/char): {unit_entropy/char_entropy:.2f}")

# Bigram entropy of syllabic units
unit_bigram_counter = Counter()
for _, units in segmented:
    for i in range(len(units) - 1):
        unit_bigram_counter[(units[i], units[i+1])] += 1

unit_bigram_total = sum(unit_bigram_counter.values())
if unit_bigram_total > 0:
    unit_bigram_entropy = -sum((cnt/unit_bigram_total) * math.log2(cnt/unit_bigram_total)
                               for cnt in unit_bigram_counter.values())
    conditional_entropy = unit_bigram_entropy - unit_entropy
    entropy_drop = unit_entropy - conditional_entropy
    print(f"\nSyllabic unit bigram entropy: {unit_bigram_entropy:.2f} bits")
    print(f"Conditional entropy (H2-H1): {conditional_entropy:.2f} bits")
    print(f"Entropy drop (H1 - conditional): {entropy_drop:.2f} bits")
    print(f"(Natural language syllable entropy drop: ~1.0-1.5 bits)")

print()

# ============================================================
# SUMMARY
# ============================================================
print("=" * 70)
print("SUMMARY: SYLLABARY/ABUGIDA HYPOTHESIS ASSESSMENT")
print("=" * 70)

avg_wl = sum(len(w) for w in words) / len(words)
avg_wpp = sum(word_counts) / len(word_counts) if word_counts else 0
cv_ratio = cv_pair_count / total_pairs * 100

print(f"""
KEY METRICS:
- Distinct character bigrams: {len(bigram_counter)}
  -> Italian has ~200-300 common syllables
  -> {"CLOSE to Italian syllable count" if 150 <= len(bigram_counter) <= 350 else "NOT matching Italian syllable count (" + str(len(bigram_counter)) + ")"}

- Distinct syllabic units (greedy segmentation): {len(unit_counter)}
  -> Average units per word: {avg_syl:.1f}
  -> Italian words average 2.5-3.0 syllables
  -> {"MATCHES Italian" if 2.0 <= avg_syl <= 4.0 else "DOES NOT MATCH Italian"}

- Average word length: {avg_wl:.2f} characters
  -> Italian words average ~5.0 characters
  -> {"MATCHES" if 4.5 <= avg_wl <= 5.5 else "CLOSE" if 4.0 <= avg_wl <= 6.0 else "DOES NOT MATCH"}

- Words per page: avg {avg_wpp:.0f}
  -> Medieval herbal entry: ~100-300 words per page

- CV alternation ratio: {cv_ratio:.1f}%
  -> Pure CV syllabary: ~50%
  -> {"SUPPORTS" if 35 <= cv_ratio <= 55 else "DOES NOT SUPPORT"} syllabary hypothesis

- Syllabic unit entropy: {unit_entropy:.2f} bits (of {max_entropy:.2f} max)
""")
