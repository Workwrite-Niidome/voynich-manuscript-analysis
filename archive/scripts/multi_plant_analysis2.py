#!/usr/bin/env python3
"""
Multi-plant triangulation analysis for Voynich manuscript encoding.
Uses 5 identified plants to search for encoding patterns.
Fixed word tokenization.
"""
import re
from collections import Counter, defaultdict
import math

# Read the transcription file
with open("C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt", "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

# Parse all folios - properly split words on '.'
folios = {}  # folio_id -> list of lines, each line is list of words
current_folio = None

for line in raw_lines:
    line = line.strip()
    # Detect folio header
    m = re.match(r'^<(f\d+[rv])>\s', line)
    if m:
        current_folio = m.group(1)
        if current_folio not in folios:
            folios[current_folio] = []
        continue
    # Detect folio text lines
    m = re.match(r'^<(f\d+[rv])\.\d+,[^>]+>\s+(.*)', line)
    if m:
        folio_id = m.group(1)
        text = m.group(2)
        if folio_id not in folios:
            folios[folio_id] = []
        # Split on '.' to get individual words
        # Also split on '<->' which is a word boundary marker
        text = text.replace('<->', '.')
        words = []
        for token in text.split('.'):
            token = token.strip()
            # Clean annotations
            token = re.sub(r'@\d+;?', '', token)
            token = re.sub(r'\{[^}]+\}', '', token)
            token = re.sub(r'[,?]', '', token)
            token = token.strip()
            if token and len(token) > 0:
                words.append(token)
        folios[folio_id].append(words)

def get_all_words(folio_id):
    """Get flat list of all words for a folio."""
    if folio_id not in folios:
        return []
    return [w for line in folios[folio_id] for w in line]

def get_line_tag(folio_id):
    """Get tag type for lines (Lp = label, P0 = paragraph)."""
    tags = {}
    for line in raw_lines:
        line = line.strip()
        m = re.match(r'^<(f\d+[rv])\.(\d+),([^>]+)>\s+(.*)', line)
        if m and m.group(1) == folio_id:
            tags[int(m.group(2))] = (m.group(3), m.group(4))
    return tags

# Target folios
targets = {
    'f47r': {'plant': 'Vitis vinifera', 'common': 'grape', 'italian': 'vite/uva', 'confidence': 70},
    'f9r':  {'plant': 'Nigella damascena', 'common': 'love-in-a-mist', 'italian': 'nigella/gittone', 'confidence': 65},
    'f3r':  {'plant': 'Rubia tinctorum', 'common': 'madder', 'italian': 'robbia/rubia', 'confidence': 60},
    'f41r': {'plant': 'Adiantum capillus-veneris', 'common': 'maidenhair fern', 'italian': 'capelvenere/adianto', 'confidence': 60},
    'f2r':  {'plant': 'Paeonia officinalis', 'common': 'peony', 'italian': 'peonia', 'confidence': 55},
}

# Build global word frequency across ALL herbal folios
global_freq = Counter()
folio_word_sets = {}
all_herbal_folios = []
# Document frequency
doc_freq = defaultdict(int)

for fid in sorted(folios.keys(), key=lambda x: (int(re.search(r'\d+', x).group()), x[-1])):
    num = int(re.search(r'\d+', fid).group())
    if num <= 57:
        all_herbal_folios.append(fid)
        words = get_all_words(fid)
        folio_word_sets[fid] = words
        for w in words:
            global_freq[w] += 1
        for w in set(words):
            doc_freq[w] += 1

total_folios = len(all_herbal_folios)

print("=" * 80)
print("MULTI-PLANT TRIANGULATION ANALYSIS")
print("=" * 80)
print(f"\nTotal herbal folios parsed: {total_folios}")
print(f"Total unique words in herbal section: {len(global_freq)}")

# ============================================================
# 1. First words / heading candidates
# ============================================================
print("\n" + "=" * 80)
print("1. FIRST WORDS (heading/title candidates)")
print("=" * 80)

for fid, info in targets.items():
    words = get_all_words(fid)
    first_words = words[:8] if len(words) >= 8 else words
    print(f"\n{fid} ({info['plant']} / {info['italian']}):")
    print(f"  Line 1 words: {folios[fid][0] if folios[fid] else 'N/A'}")
    print(f"  First 8 words: {first_words}")

# ============================================================
# 2. Label text (Lp/L0 lines)
# ============================================================
print("\n" + "=" * 80)
print("2. LABEL TEXT (plant name labels)")
print("=" * 80)

for fid in targets:
    tags = get_line_tag(fid)
    print(f"\n{fid}:")
    for line_num, (tag, text) in sorted(tags.items()):
        if 'L' in tag:
            print(f"  Line {line_num} [{tag}]: {text}")
    # Also check recto/verso pair
    if fid.endswith('r'):
        verso = fid[:-1] + 'v'
        if verso in folios:
            vtags = get_line_tag(verso)
            for line_num, (tag, text) in sorted(vtags.items()):
                if 'L' in tag:
                    print(f"  {verso} Line {line_num} [{tag}]: {text}")

# ============================================================
# 3. Consonant skeleton analysis
# ============================================================
print("\n" + "=" * 80)
print("3. CONSONANT SKELETON MATCHING")
print("=" * 80)

def eva_consonants(word):
    """Extract consonant sequence from EVA word."""
    # In EVA: ch, sh, cth, ckh, cfh, cph are single glyphs (digraphs/trigraphs)
    result = []
    i = 0
    w = word.lower()
    while i < len(w):
        # Trigraphs first
        if i+2 < len(w) and w[i:i+3] in ('cth', 'ckh', 'cfh', 'cph'):
            result.append(w[i:i+3])
            i += 3
        elif i+1 < len(w) and w[i:i+2] in ('ch', 'sh'):
            result.append(w[i:i+2])
            i += 2
        elif w[i] in 'ktpfdsrlnmgq':
            result.append(w[i])
            i += 1
        else:  # vowels: a, e, i, o, y
            i += 1
    return tuple(result)

def latin_consonants(word):
    """Extract consonant letters from Latin/Italian word."""
    return tuple(c for c in word.lower() if c not in 'aeiou')

# Test all words on each target page against various forms of the plant name
print("\nApproach: For each plant, test if any word on its page has a")
print("consonant skeleton matching the plant name (with v->f, b->p, g->k subs)")

for fid, info in targets.items():
    words = get_all_words(fid)
    unique_words = list(dict.fromkeys(words))

    # Plant name variants
    latin_name = info['plant'].split()[0].lower()  # genus
    latin_name2 = info['plant'].split()[1].lower() if len(info['plant'].split()) > 1 else ''
    italian_names = [n.strip() for n in info['italian'].split('/')]

    all_names = [latin_name] + ([latin_name2] if latin_name2 else []) + italian_names

    print(f"\n--- {fid}: {info['plant']} ---")

    for name in all_names:
        cons = latin_consonants(name)
        # Apply substitutions: v->f, b->p, g->k (EVA lacks v, b, g)
        eva_equiv = []
        for c in cons:
            if c == 'v': eva_equiv.append('f')
            elif c == 'b': eva_equiv.append('p')
            elif c == 'g': eva_equiv.append('k')
            elif c == 'x': eva_equiv.append('ks')
            else: eva_equiv.append(c)
        eva_equiv = tuple(eva_equiv)

        print(f"\n  Name: '{name}' -> consonants: {cons} -> EVA equiv: {eva_equiv}")

        matches = []
        partial = []
        for w in unique_words:
            w_cons = eva_consonants(w)
            if w_cons == eva_equiv:
                matches.append((w, w_cons))
            elif len(w_cons) >= 2 and len(eva_equiv) >= 2:
                # Check if consonant sequence contains the target
                w_str = ''.join(w_cons)
                e_str = ''.join(eva_equiv)
                if e_str in w_str or w_str in e_str:
                    partial.append((w, w_cons))
                # Also check first N consonants match
                elif w_cons[:len(eva_equiv)] == eva_equiv:
                    partial.append((w, w_cons, 'prefix'))

        if matches:
            print(f"  EXACT MATCHES: {matches}")
        if partial:
            print(f"  Partial matches: {partial[:8]}")
        if not matches and not partial:
            # Show all words with their consonant skeletons
            print(f"  No matches. Page words:")
            for w in unique_words[:20]:
                print(f"    {w:25s} -> {eva_consonants(w)}")

# ============================================================
# 4. Page-unique / rare words
# ============================================================
print("\n" + "=" * 80)
print("4. PAGE-UNIQUE AND RARE WORDS")
print("=" * 80)

for fid, info in targets.items():
    words = get_all_words(fid)
    word_set = set(words)

    rare = []
    for w in word_set:
        total = global_freq[w]
        if total <= 3 and len(w) > 2:
            rare.append((w, total, eva_consonants(w)))

    rare.sort(key=lambda x: (x[1], x[0]))

    print(f"\n{fid} ({info['plant']}):")
    print(f"  Total words: {len(words)}, Unique: {len(word_set)}")
    for w, cnt, cons in rare[:20]:
        print(f"  [{cnt}x] {w:25s} cons={cons}")

# ============================================================
# 5. Most frequent content words per page
# ============================================================
print("\n" + "=" * 80)
print("5. WORD FREQUENCY PER PAGE")
print("=" * 80)

function_words = {'chol', 'chor', 'daiin', 'dain', 'cho', 'sho', 'ol', 'or',
                  'chy', 'cthy', 'chey', 'shol', 'dar', 'dal', 'aiin', 'dy',
                  'shey', 'dor', 'am', 'al', 'an', 'sy', 's', 'y', 'r', 'd'}

for fid, info in targets.items():
    words = get_all_words(fid)
    freq = Counter(words)
    all_sorted = freq.most_common()
    content = [(w, c) for w, c in all_sorted if w not in function_words and len(w) > 2]

    print(f"\n{fid} ({info['plant']}):")
    print(f"  All words by freq: {all_sorted[:15]}")
    print(f"  Content words: {content[:10]}")

# ============================================================
# 6. TF-IDF distinctive words
# ============================================================
print("\n" + "=" * 80)
print("6. TF-IDF DISTINCTIVE WORDS")
print("=" * 80)

for fid, info in targets.items():
    words = get_all_words(fid)
    tf = Counter(words)

    tfidf = {}
    for w, count in tf.items():
        if doc_freq[w] > 0 and len(w) > 2:
            tfidf[w] = count * math.log(total_folios / doc_freq[w])

    sorted_tfidf = sorted(tfidf.items(), key=lambda x: -x[1])[:15]

    print(f"\n{fid} ({info['plant']}):")
    for w, score in sorted_tfidf:
        print(f"  {w:25s} tf-idf={score:.2f}  (global={global_freq[w]}, docs={doc_freq[w]})")

# ============================================================
# 7. Cross-page vocabulary overlap
# ============================================================
print("\n" + "=" * 80)
print("7. VOCABULARY OVERLAP BETWEEN TARGET PAGES")
print("=" * 80)

target_ids = list(targets.keys())
for i in range(len(target_ids)):
    for j in range(i+1, len(target_ids)):
        f1, f2 = target_ids[i], target_ids[j]
        s1 = set(get_all_words(f1))
        s2 = set(get_all_words(f2))
        shared = s1 & s2
        if shared:
            print(f"  {f1} & {f2}: shared = {shared}")

# Shared across ALL target pages
all_sets = [set(get_all_words(f)) for f in target_ids]
common_all = all_sets[0]
for s in all_sets[1:]:
    common_all &= s
print(f"\n  Words shared by ALL 5 pages: {common_all if common_all else 'NONE'}")

# ============================================================
# 8. Morphological patterns (endings)
# ============================================================
print("\n" + "=" * 80)
print("8. DISTINCTIVE MORPHOLOGICAL PATTERNS PER PAGE")
print("=" * 80)

for fid, info in targets.items():
    words = get_all_words(fid)
    endings_3 = Counter(w[-3:] for w in words if len(w) >= 3)
    endings_2 = Counter(w[-2:] for w in words if len(w) >= 2)

    print(f"\n{fid} ({info['plant']}):")
    print(f"  Endings (3-char): {endings_3.most_common(8)}")
    print(f"  Endings (2-char): {endings_2.most_common(8)}")

    # Distinctive endings for this page vs global
    page_total = len(words)
    for ending, count in endings_3.most_common(8):
        # Count this ending globally
        global_ending_count = sum(1 for fid2 in all_herbal_folios
                                  for w in get_all_words(fid2) if len(w) >= 3 and w[-3:] == ending)
        ratio = count / max(global_ending_count, 1)
        if ratio > 0.3:  # This page has >30% of all uses
            print(f"    '{ending}' is distinctive: {count}/{global_ending_count} ({ratio:.1%} of all uses)")

# ============================================================
# 9. f3r special: words ending in -m/-am/-om
# ============================================================
print("\n" + "=" * 80)
print("9. SPECIAL: f3r -m ENDINGS (possible Latin -um/-am inflection?)")
print("=" * 80)

f3r_words = get_all_words('f3r')
m_words = [w for w in f3r_words if w.endswith('m') or w.endswith('mo')]
print(f"f3r words ending in -m or -mo: {m_words}")
print(f"Count: {len(m_words)} out of {len(f3r_words)} total words")

# Compare with other pages
for fid in ['f2r', 'f9r', 'f41r', 'f47r']:
    ws = get_all_words(fid)
    m_count = sum(1 for w in ws if w.endswith('m'))
    print(f"  {fid}: {m_count}/{len(ws)} words end in -m")

# ============================================================
# 10. Attempt: strip common prefixes/suffixes, compare cores
# ============================================================
print("\n" + "=" * 80)
print("10. WORD CORE EXTRACTION (stripping common affixes)")
print("=" * 80)

# Common EVA prefixes: qo-, o-, y-, d-, s-, p-
# Common EVA suffixes: -aiin, -ain, -dy, -y, -ol, -or, -al, -ar
# The "core" might encode the plant name

prefixes = ['qo', 'ot', 'ok', 'sh', 'ch']
suffixes = ['aiin', 'ain', 'dy', 'ody', 'ey', 'eey', 'ol', 'or', 'al', 'ar', 'am', 'dam']

def strip_affixes(word):
    """Strip common EVA prefixes and suffixes to get core."""
    w = word
    for p in sorted(prefixes, key=len, reverse=True):
        if w.startswith(p) and len(w) > len(p) + 2:
            w = w[len(p):]
            break
    for s in sorted(suffixes, key=len, reverse=True):
        if w.endswith(s) and len(w) > len(s) + 1:
            w = w[:-len(s)]
            break
    return w

for fid, info in targets.items():
    words = get_all_words(fid)
    unique_words = list(dict.fromkeys(words))

    print(f"\n{fid} ({info['plant']}):")
    cores = Counter()
    for w in words:
        core = strip_affixes(w)
        if core != w and len(core) >= 2:
            cores[core] += 1

    print(f"  Top cores: {cores.most_common(15)}")

    # Check if any core matches plant name consonants
    latin_name = info['plant'].split()[0].lower()
    name_cons = tuple(c for c in latin_name if c not in 'aeiou')
    # With substitutions
    eva_name = tuple('f' if c == 'v' else 'p' if c == 'b' else 'k' if c == 'g' else c for c in name_cons)

    for core, cnt in cores.most_common(15):
        core_cons = eva_consonants(core)
        if core_cons == eva_name:
            print(f"  *** MATCH: core '{core}' matches '{latin_name}' ({core_cons} == {eva_name})")

# ============================================================
# 11. Label on f2r: "ytoail / ios.an.on"
# ============================================================
print("\n" + "=" * 80)
print("11. f2r LABEL ANALYSIS: 'ytoail' and 'ios an on'")
print("=" * 80)

print("f2r label text: ytoail / ios.an.on")
print("If f2r = Paeonia officinalis (peony):")
print("  'ytoail' consonants:", eva_consonants('ytoail'))
print("  Could 'ytoail' encode 'peonia'? p->? n->? ")
print("  'ios' could be a fragment")
print()
print("Note: Labels in the Voynich are often in a different hand/system")
print("They may use a simpler cipher or even be in plain (garbled) text")
print()
# Check if 'ios' appears elsewhere
ios_count = global_freq.get('ios', 0)
print(f"'ios' appears {ios_count} times in herbal section")
# Check labels across all folios
print("\nAll labels in herbal section:")
for line in raw_lines:
    line = line.strip()
    m = re.match(r'^<(f\d+[rv])\.\d+,([^>]*L[^>]*)>\s+(.*)', line)
    if m:
        fid = m.group(1)
        num = int(re.search(r'\d+', fid).group())
        if num <= 57:
            print(f"  {fid} [{m.group(2)}]: {m.group(3)}")

# ============================================================
# 12. Comprehensive word-by-word dump for each target
# ============================================================
print("\n" + "=" * 80)
print("12. COMPLETE WORD LISTS FOR TARGET FOLIOS")
print("=" * 80)

for fid, info in targets.items():
    print(f"\n--- {fid}: {info['plant']} ({info['italian']}) ---")
    for i, line_words in enumerate(folios.get(fid, [])):
        print(f"  Line {i+1}: {line_words}")

# ============================================================
# 13. Attempt phonetic mapping test
# ============================================================
print("\n" + "=" * 80)
print("13. PHONETIC MAPPING TEST")
print("=" * 80)

# If we hypothesize specific EVA->sound mappings, what would the first words read as?
# Common proposals (Bax 2014, others):
# k -> /k/, t -> /t/, p -> /p/, f -> /f/, d -> /d/
# ch -> /k/ or /tʃ/, sh -> /ʃ/ or /s/
# o -> /o/ or null, a -> /a/, e -> /e/, i -> /i/, y -> /j/ or /i/
# r -> /r/, l -> /l/, n -> /n/ (from 'aiin'='n' hypothesis)
# s -> /s/

# Bax-style mapping
bax = {
    'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'y': 'y',
    'k': 'k', 't': 't', 'p': 'p', 'f': 'f', 'd': 'd',
    'ch': 'k', 'sh': 's', 'cth': 'kt', 'ckh': 'kk',
    'cfh': 'kf', 'cph': 'kp',
    'r': 'r', 'l': 'l', 'n': 'n', 'm': 'm', 'g': 'g',
    's': 's', 'q': 'k',
}

# Alternative: ch -> /tʃ/, sh -> /ʃ/
alt = {
    'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'y': '',
    'k': 'k', 't': 't', 'p': 'p', 'f': 'v', 'd': 'd',
    'ch': 'ch', 'sh': 'sh', 'cth': 'th', 'ckh': 'kh',
    'cfh': 'fh', 'cph': 'ph',
    'r': 'r', 'l': 'l', 'n': 'n', 'm': 'm', 'g': 'g',
    's': 's', 'q': 'q',
}

def apply_mapping(word, mapping):
    """Apply a sound mapping to an EVA word."""
    result = []
    i = 0
    w = word.lower()
    while i < len(w):
        matched = False
        # Try longest match first
        for length in [3, 2, 1]:
            chunk = w[i:i+length]
            if chunk in mapping:
                result.append(mapping[chunk])
                i += length
                matched = True
                break
        if not matched:
            result.append(w[i])
            i += 1
    return ''.join(result)

# Special mapping where aiin -> n, ain -> n, iin -> n
def apply_mapping_v2(word, mapping):
    """Apply mapping with aiin/ain -> n substitution first."""
    w = word.lower()
    w = w.replace('aiin', 'N')  # capital N as placeholder
    w = w.replace('ain', 'N')
    w = w.replace('iin', 'N')
    result = []
    i = 0
    while i < len(w):
        if w[i] == 'N':
            result.append('n')
            i += 1
            continue
        matched = False
        for length in [3, 2, 1]:
            chunk = w[i:i+length]
            if chunk in mapping:
                result.append(mapping[chunk])
                i += length
                matched = True
                break
        if not matched:
            result.append(w[i])
            i += 1
    return ''.join(result)

print("\nFirst word of each target page, decoded with two mappings:")
print("(aiin/ain -> n applied in both)")

for fid, info in targets.items():
    words = get_all_words(fid)
    if not words:
        continue
    first_word = words[0]
    bax_reading = apply_mapping_v2(first_word, bax)
    alt_reading = apply_mapping_v2(first_word, alt)

    print(f"\n  {fid} ({info['plant']}):")
    print(f"    EVA:     {first_word}")
    print(f"    Bax:     {bax_reading}")
    print(f"    Alt(v):  {alt_reading}")
    print(f"    Target:  {info['plant']} / {info['italian']}")

# Try ALL words on page with both mappings, see if any look like the plant name
print("\n\nSearching all words for phonetic similarity to plant names:")

for fid, info in targets.items():
    words = list(dict.fromkeys(get_all_words(fid)))
    plant_names = [info['plant'].split()[0].lower()]
    plant_names += [n.strip().lower() for n in info['italian'].split('/')]

    print(f"\n--- {fid}: looking for {plant_names} ---")
    for w in words:
        bax_r = apply_mapping_v2(w, bax)
        alt_r = apply_mapping_v2(w, alt)

        for pname in plant_names:
            # Check if the decoded word starts with the same 3+ chars as plant name
            if len(bax_r) >= 3 and len(pname) >= 3:
                if bax_r[:3] == pname[:3]:
                    print(f"  Bax match: '{w}' -> '{bax_r}' ~ '{pname}'")
                if alt_r[:3] == pname[:3]:
                    print(f"  Alt match: '{w}' -> '{alt_r}' ~ '{pname}'")
            # Also check if decoded word contains plant name
            if len(pname) >= 4 and pname[:4] in bax_r:
                print(f"  Bax contains: '{w}' -> '{bax_r}' contains '{pname[:4]}'")
            if len(pname) >= 4 and pname[:4] in alt_r:
                print(f"  Alt contains: '{w}' -> '{alt_r}' contains '{pname[:4]}'")

print("\n\nDone.")
