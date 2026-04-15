#!/usr/bin/env python3
"""
Multi-plant triangulation analysis for Voynich manuscript encoding.
Uses 5 identified plants to search for encoding patterns.
"""
import re
from collections import Counter, defaultdict

# Read the transcription file
with open("C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Parse all folios
folios = {}
current_folio = None
for line in lines:
    line = line.strip()
    # Detect folio header
    m = re.match(r'^<(f\d+[rv])>', line)
    if m:
        current_folio = m.group(1)
        folios[current_folio] = []
        continue
    # Detect folio text lines
    m = re.match(r'^<(f\d+[rv])\.(\d+),', line)
    if m:
        folio_id = m.group(1)
        if folio_id not in folios:
            folios[folio_id] = []
        # Extract text after the tag
        text_part = re.sub(r'^<[^>]+>\s*', '', line)
        folios[folio_id].append(text_part)

def extract_words(text_lines):
    """Extract clean EVA words from text lines."""
    words = []
    for line in text_lines:
        # Remove annotations like @221; {cto} etc
        clean = re.sub(r'@\d+;?', '', line)
        clean = re.sub(r'\{[^}]+\}', '', clean)
        clean = re.sub(r'<->', ' ', clean)
        clean = re.sub(r'[,?.!]', '', clean)
        tokens = clean.split('.')
        for t in tokens:
            t = t.strip()
            if t and len(t) > 0:
                # Split on spaces too
                for w in t.split():
                    w = w.strip()
                    if w and len(w) > 1:
                        words.append(w)
    return words

# Target folios
targets = {
    'f47r': {'plant': 'Vitis vinifera', 'common': 'grape', 'italian': 'vite/uva', 'confidence': 70},
    'f9r':  {'plant': 'Nigella damascena', 'common': 'love-in-a-mist', 'italian': 'nigella/gittone', 'confidence': 65},
    'f3r':  {'plant': 'Rubia tinctorum', 'common': 'madder', 'italian': 'robbia/rubia', 'confidence': 60},
    'f41r': {'plant': 'Adiantum capillus-veneris', 'common': 'maidenhair fern', 'italian': 'capelvenere/adianto', 'confidence': 60},
    'f2r':  {'plant': 'Paeonia officinalis', 'common': 'peony', 'italian': 'peonia', 'confidence': 55},
}

# Build global word frequency across ALL herbal folios (f1r through f57v approx)
global_freq = Counter()
folio_word_sets = {}
all_herbal_folios = []

for fid in sorted(folios.keys(), key=lambda x: (int(re.search(r'\d+', x).group()), x[-1])):
    num = int(re.search(r'\d+', fid).group())
    # Herbal section is roughly f1-f57
    if num <= 57:
        all_herbal_folios.append(fid)
        words = extract_words(folios[fid])
        folio_word_sets[fid] = words
        for w in words:
            global_freq[w] += 1

# ============================================================
# ANALYSIS 1: First words of each target folio
# ============================================================
print("=" * 80)
print("ANALYSIS 1: First words (heading / title candidates)")
print("=" * 80)
for fid, info in targets.items():
    if fid in folios:
        words = extract_words(folios[fid])
        first_5 = words[:5] if len(words) >= 5 else words
        print(f"\n{fid} ({info['plant']}):")
        print(f"  First 5 words: {first_5}")
        print(f"  Latin: {info['plant']}, Italian: {info['italian']}")

# ============================================================
# ANALYSIS 2: Consonant skeleton matching
# ============================================================
print("\n" + "=" * 80)
print("ANALYSIS 2: Consonant skeleton matching")
print("=" * 80)

# EVA consonant mapping (approximate phonetic values commonly proposed)
# EVA: k, t, p, f, d, s, r, l, n, m, g are consonantal
# EVA: a, e, o, i, y are vocalic
# ch, sh, cth, ckh, etc. are digraphs

def eva_consonant_skeleton(word):
    """Extract consonant skeleton from EVA word."""
    # Remove common prefixes
    w = word
    # Map EVA to approximate consonants
    consonants = []
    i = 0
    while i < len(w):
        if i+2 < len(w) and w[i:i+3] in ('cth', 'ckh', 'cfh', 'cph'):
            consonants.append(w[i:i+3])
            i += 3
        elif i+1 < len(w) and w[i:i+2] in ('ch', 'sh', 'th', 'ph'):
            consonants.append(w[i:i+2])
            i += 2
        elif w[i] in 'ktpfdsrlnmgq':
            consonants.append(w[i])
            i += 1
        else:  # vowel
            i += 1
    return '-'.join(consonants)

def latin_consonant_skeleton(word):
    """Extract consonant skeleton from Latin/Italian word."""
    consonants = []
    for c in word.lower():
        if c not in 'aeiou':
            consonants.append(c)
    return '-'.join(consonants)

# Plant name consonant skeletons
plant_skeletons = {
    'vitis': 'v-t-s',
    'vinifera': 'v-n-f-r',
    'vite': 'v-t',
    'uva': 'v',
    'nigella': 'n-g-l-l',
    'gittone': 'g-t-t-n',
    'rubia': 'r-b',
    'robbia': 'r-b-b',
    'tinctorum': 't-n-c-t-r-m',
    'adiantum': 'd-n-t-m',
    'capelvenere': 'c-p-l-v-n-r',
    'adianto': 'd-n-t',
    'paeonia': 'p-n',
    'peonia': 'p-n',
}

for fid, info in targets.items():
    if fid not in folio_word_sets:
        continue
    words = folio_word_sets[fid]
    unique_words = list(dict.fromkeys(words))  # preserve order, deduplicate

    print(f"\n{fid} ({info['plant']}):")
    plant_name = info['plant'].split()[0].lower()
    plant_skel = latin_consonant_skeleton(plant_name)
    print(f"  Target skeleton ({plant_name}): {plant_skel}")

    # Check all words on this page
    matches = []
    for w in unique_words:
        w_skel = eva_consonant_skeleton(w)
        if w_skel == plant_skel:
            matches.append((w, w_skel))

    if matches:
        print(f"  EXACT skeleton matches: {matches}")
    else:
        # Show closest matches (same number of consonants)
        target_len = len(plant_skel.split('-'))
        close = [(w, eva_consonant_skeleton(w)) for w in unique_words
                 if len(eva_consonant_skeleton(w).split('-')) == target_len and eva_consonant_skeleton(w)]
        print(f"  No exact match. Words with {target_len} consonants: {close[:10]}")

# ============================================================
# ANALYSIS 3: Page-unique words (hapax on page / rare globally)
# ============================================================
print("\n" + "=" * 80)
print("ANALYSIS 3: Page-unique and rare words")
print("=" * 80)

for fid, info in targets.items():
    if fid not in folio_word_sets:
        continue
    words = folio_word_sets[fid]
    word_set = set(words)

    # Find words that appear on this page but rarely elsewhere
    unique_or_rare = []
    for w in word_set:
        total_count = global_freq[w]
        if total_count <= 3:  # appears max 3 times in entire herbal section
            unique_or_rare.append((w, total_count))

    unique_or_rare.sort(key=lambda x: x[1])

    print(f"\n{fid} ({info['plant']} / {info['italian']}):")
    print(f"  Total unique words on page: {len(word_set)}")
    print(f"  Rare words (<=3 occurrences in herbal): {unique_or_rare[:15]}")

# ============================================================
# ANALYSIS 4: Word frequency per page (2nd most common)
# ============================================================
print("\n" + "=" * 80)
print("ANALYSIS 4: Most frequent words per page")
print("=" * 80)

# Common function words to filter
function_words = {'chol', 'chor', 'daiin', 'dain', 'cho', 'sho', 'ol', 'or', 'chy', 'cthy',
                  'chey', 'shol', 'dar', 'dal', 'aiin', 'oky', 'dy', 'shey', 'dor', 'chody',
                  'otchol', 'okaiin', 'chaiin', 'oteol', 'qokeey', 'cheor', 'ycheor', 'am',
                  'al', 'an', 'qo', 'sy', 'ky'}

for fid, info in targets.items():
    if fid not in folio_word_sets:
        continue
    words = folio_word_sets[fid]
    freq = Counter(words)

    # All words by frequency
    all_by_freq = freq.most_common(20)
    # Content words (non-function)
    content_by_freq = [(w, c) for w, c in freq.most_common(30) if w not in function_words]

    print(f"\n{fid} ({info['plant']}):")
    print(f"  Top 10 all: {all_by_freq[:10]}")
    print(f"  Top 10 content: {content_by_freq[:10]}")

# ============================================================
# ANALYSIS 5: Distinctive features per page (TF-IDF like)
# ============================================================
print("\n" + "=" * 80)
print("ANALYSIS 5: TF-IDF distinctive words per page")
print("=" * 80)

import math

total_folios = len(all_herbal_folios)
# Document frequency: how many folios contain each word
doc_freq = defaultdict(int)
for fid in all_herbal_folios:
    if fid in folio_word_sets:
        for w in set(folio_word_sets[fid]):
            doc_freq[w] += 1

for fid, info in targets.items():
    if fid not in folio_word_sets:
        continue
    words = folio_word_sets[fid]
    tf = Counter(words)

    # TF-IDF score
    tfidf = {}
    for w, count in tf.items():
        if doc_freq[w] > 0 and len(w) > 2:
            tfidf[w] = count * math.log(total_folios / doc_freq[w])

    sorted_tfidf = sorted(tfidf.items(), key=lambda x: -x[1])

    print(f"\n{fid} ({info['plant']} / {info['italian']}):")
    print(f"  Top 15 distinctive: {sorted_tfidf[:15]}")

# ============================================================
# ANALYSIS 6: First word comparison across all herbal pages
# ============================================================
print("\n" + "=" * 80)
print("ANALYSIS 6: First words across herbal pages")
print("=" * 80)

first_words = {}
for fid in all_herbal_folios:
    if fid in folio_word_sets and folio_word_sets[fid]:
        first_words[fid] = folio_word_sets[fid][0]

# Count first word patterns
first_word_freq = Counter(first_words.values())
print(f"Most common first words: {first_word_freq.most_common(20)}")
print(f"\nTarget folio first words:")
for fid in targets:
    if fid in first_words:
        print(f"  {fid}: {first_words[fid]} (global first-word count: {first_word_freq[first_words[fid]]})")

# ============================================================
# ANALYSIS 7: Label text (Lp/L0 lines - often plant name labels)
# ============================================================
print("\n" + "=" * 80)
print("ANALYSIS 7: Label text on target pages")
print("=" * 80)

for fid in targets:
    print(f"\n{fid}:")
    for line in lines:
        line = line.strip()
        if line.startswith(f'<{fid}.') and ('Lp' in line or 'L0' in line or 'Lr' in line):
            print(f"  LABEL: {line}")

# ============================================================
# ANALYSIS 8: Specific consonant skeleton search across pages
# ============================================================
print("\n" + "=" * 80)
print("ANALYSIS 8: Broader consonant matching (allowing partial)")
print("=" * 80)

# For each plant, search for words whose consonant skeleton is a subset or superset
def consonants_only(word):
    """Get just the consonant letters from EVA."""
    result = []
    i = 0
    while i < len(word):
        if word[i] in 'ktpfdsrlnmgq':
            result.append(word[i])
            i += 1
        else:
            i += 1
    return ''.join(result)

plant_targets = [
    ('f47r', 'vitis', 'vts'),
    ('f47r', 'vite', 'vt'),
    ('f9r', 'nigella', 'ngll'),
    ('f3r', 'rubia', 'rb'),
    ('f3r', 'robbia', 'rbb'),
    ('f41r', 'adiantum', 'dntm'),
    ('f41r', 'capelvenere', 'kplvnr'),
    ('f2r', 'paeonia', 'pn'),
    ('f2r', 'peonia', 'pn'),
]

# EVA does not have 'v' or 'b' - what might they map to?
# v -> f or ph?  b -> p?
# Let's also check with substitutions
print("\nNote: EVA has no 'v' or 'b' glyphs. Possible mappings:")
print("  v -> f, ph, or ch?")
print("  b -> p?")

substituted_targets = [
    ('f47r', 'vitis(v->f)', 'fts'),
    ('f47r', 'vitis(v->ph)', 'pts'),  # ph written as p in consonant extraction
    ('f9r', 'nigella(g->k)', 'nkll'),
    ('f3r', 'rubia(b->p)', 'rp'),
    ('f3r', 'robbia(b->p)', 'rpp'),
    ('f41r', 'adiantum', 'dntm'),
    ('f2r', 'paeonia', 'pn'),
]

for fid, name, target_cons in substituted_targets:
    if fid not in folio_word_sets:
        continue
    words = folio_word_sets[fid]
    matches = []
    for w in set(words):
        w_cons = consonants_only(w)
        if w_cons == target_cons:
            matches.append(w)
    if matches:
        print(f"\n  {fid} looking for '{name}' ({target_cons}): MATCHES = {matches}")
    else:
        # Partial match - starts with same consonants
        partial = []
        for w in set(words):
            w_cons = consonants_only(w)
            if len(w_cons) >= 2 and len(target_cons) >= 2:
                if w_cons[:2] == target_cons[:2]:
                    partial.append((w, w_cons))
        if partial:
            print(f"\n  {fid} looking for '{name}' ({target_cons}): partial matches = {partial[:10]}")
        else:
            print(f"\n  {fid} looking for '{name}' ({target_cons}): no matches")

# ============================================================
# ANALYSIS 9: f3r distinctive feature - many words ending in 'm'
# ============================================================
print("\n" + "=" * 80)
print("ANALYSIS 9: Morphological patterns per page")
print("=" * 80)

for fid, info in targets.items():
    if fid not in folio_word_sets:
        continue
    words = folio_word_sets[fid]

    # Ending patterns
    endings = Counter()
    for w in words:
        if len(w) >= 2:
            endings[w[-2:]] += 1

    # Beginning patterns
    beginnings = Counter()
    for w in words:
        if len(w) >= 2:
            beginnings[w[:2]] += 1

    print(f"\n{fid} ({info['plant']}):")
    print(f"  Top endings: {endings.most_common(10)}")
    print(f"  Top beginnings: {beginnings.most_common(10)}")

# ============================================================
# ANALYSIS 10: Cross-page word overlap
# ============================================================
print("\n" + "=" * 80)
print("ANALYSIS 10: Vocabulary overlap between target pages")
print("=" * 80)

target_ids = list(targets.keys())
for i in range(len(target_ids)):
    for j in range(i+1, len(target_ids)):
        f1, f2 = target_ids[i], target_ids[j]
        if f1 in folio_word_sets and f2 in folio_word_sets:
            s1, s2 = set(folio_word_sets[f1]), set(folio_word_sets[f2])
            overlap = s1 & s2
            unique1 = s1 - s2
            unique2 = s2 - s1
            print(f"\n{f1} vs {f2}:")
            print(f"  Shared: {len(overlap)} words: {sorted(overlap)[:15]}")
            print(f"  Only {f1}: {len(unique1)} words")
            print(f"  Only {f2}: {len(unique2)} words")

# ============================================================
# ANALYSIS 11: Medieval name forms
# ============================================================
print("\n" + "=" * 80)
print("ANALYSIS 11: Medieval/pharmacopeia name forms")
print("=" * 80)

# In medieval herbals, plants often had different names
# Let's also check: if EVA 'o' is a null/prefix, strip it
medieval_names = {
    'f47r': ['vitis', 'uva', 'vite', 'vid', 'raisin'],
    'f9r': ['nigella', 'gith', 'melanthion', 'cumino nero', 'git'],
    'f3r': ['rubia', 'robbia', 'garanza', 'alizari', 'erba rossa'],
    'f41r': ['adiantum', 'capillus', 'veneris', 'capelvenere', 'politricum'],
    'f2r': ['paeonia', 'peonia', 'rosa', 'regia', 'rosa senza spine'],
}

for fid, names in medieval_names.items():
    if fid not in folio_word_sets:
        continue
    words_on_page = set(folio_word_sets[fid])
    print(f"\n{fid}:")
    for name in names:
        name_cons = ''.join(c for c in name.lower() if c not in 'aeiou ')
        # Search with EVA substitutions: v->f, b->p, g->k, c->k
        eva_cons = name_cons.replace('v', 'f').replace('b', 'p').replace('g', 'k').replace('c', 'k')

        for w in words_on_page:
            w_cons = consonants_only(w)
            if w_cons and eva_cons and w_cons == eva_cons:
                print(f"  '{name}' ({name_cons}->{eva_cons}) matches EVA '{w}' ({w_cons})")
            # Also try with 'o-' prefix stripped
            if w.startswith('o') and len(w) > 2:
                w2_cons = consonants_only(w[1:])
                if w2_cons and eva_cons and w2_cons == eva_cons:
                    print(f"  '{name}' ({name_cons}->{eva_cons}) matches EVA '{w}' (stripped o-: {w2_cons})")

print("\n\nDone.")
