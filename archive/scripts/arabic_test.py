import re, sys, math
from collections import Counter, defaultdict

try:
    sys.stdout.reconfigure(encoding='utf-8')
except:
    pass

with open('RF1b-e.txt', 'r') as f:
    text = f.read()

words = []
f1r_words = []
in_f1r = False
for line in text.split('\n'):
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    if '<f1r>' in line and '.' not in line.split('>')[0].split('<')[-1]:
        in_f1r = True
    if '<f1v>' in line:
        in_f1r = False
    m = re.match(r'<[^>]+>\s*(.*)', line)
    if m:
        content = m.group(1)
    else:
        continue
    content = re.sub(r'@\d+;?', '', content)
    content = re.sub(r'\{[^}]*\}', '', content)
    content = re.sub(r'<[^>]*>', '', content)
    for w in re.split(r'[.\-\s,?]+', content):
        w = w.strip().strip("'")
        if w and re.match(r'^[a-z]+$', w):
            words.append(w)
            if in_f1r:
                f1r_words.append(w)

def parse_eva(word):
    phonemes = []
    i = 0
    while i < len(word):
        if i+3 <= len(word) and word[i:i+3] in ('cth','ckh','cph','cfh','tsh'):
            phonemes.append(word[i:i+3])
            i += 3
        elif i+2 <= len(word) and word[i:i+2] in ('sh','ch'):
            phonemes.append(word[i:i+2])
            i += 2
        else:
            phonemes.append(word[i])
            i += 1
    return phonemes

# EVA phoneme frequencies
eva_freq = Counter()
for w in words:
    for p in parse_eva(w):
        eva_freq[p] += 1
total_eva = sum(eva_freq.values())

# EVA bigram frequencies
eva_bigrams = Counter()
for w in words:
    ph = parse_eva(w)
    for i in range(len(ph)-1):
        eva_bigrams[(ph[i], ph[i+1])] += 1
total_eva_bg = sum(eva_bigrams.values())

# Arabic bigram frequencies (representative of medical texts)
# These are approximate normalized frequencies for common Arabic bigrams
arabic_common_bigrams = {
    ('a','l'): 5.0, ('l','a'): 3.5, ('a','n'): 2.5, ('w','a'): 2.0,
    ('m','a'): 1.8, ('f','y'): 1.5, ('l','m'): 1.5, ('a','r'): 1.4,
    ('h','a'): 1.3, ('y','a'): 1.2, ('l','y'): 1.2, ('n','a'): 1.1,
    ('a','h'): 1.1, ('m','n'): 1.0, ('r','a'): 1.0, ('b','a'): 0.9,
    ('t','a'): 0.9, ('d','a'): 0.9, ('q','a'): 0.8, ('s','a'): 0.8,
    ('k','a'): 0.7, ('l','l'): 0.7, ('y','n'): 0.7, ('a','t'): 0.7,
    ('sh','a'): 0.6, ('l','h'): 0.6, ('a','d'): 0.6, ('w','l'): 0.5,
    ('n','h'): 0.5, ('r','h'): 0.5, ('a','s'): 0.5, ('kh','a'): 0.4,
}
total_ar_bg = sum(arabic_common_bigrams.values())

# ==========================================
# MAPPING DEFINITIONS
# ==========================================

# MAPPING 1: Pure frequency rank matching
map1 = {
    'o': 'a', 'y': 'l', 'ch': 'm', 'e': 'n', 'l': 'w',
    'd': 'y', 'k': 'r', 'a': 'h', 'r': 'b', 'n': 't',
    't': 'd', 'q': 'f', 'sh': 'ayn', 's': 's', 'i': 'q',
    'p': 'k', 'm': 'H', 'cth': 'j', 'ckh': 'sh', 'cph': 'kh',
    'f': 'S', 'tsh': 'th',
}

# MAPPING 2: Sandhi-class constrained + frequency
map2 = {
    'k': 'q', 'd': 'd', 't': 't', 'l': 'l', 'r': 'r', 'e': 'b',
    'ch': 'kh', 'sh': 'sh', 'o': 'ayn', 'y': 'h', 'cth': 'th',
    'ckh': 'gh', 'cph': 'H', 'p': 'f', 'f': 'z', 'tsh': 'dh',
    'a': 'a', 'i': 'i', 'q': 'w', 'n': 'n', 's': 's', 'm': 'm',
}

# MAPPING 3: Judeo-Arabic inspired
map3 = {
    'ch': 'k', 'sh': 'sh', 'k': 'q', 'd': 'd', 't': 't',
    'l': 'l', 'r': 'r', 'o': 'w', 'y': 'y', 'a': 'a',
    'i': 'i', 'e': 'h', 'n': 'n', 's': 's', 'q': 'ayn',
    'p': 'f', 'm': 'm', 'cth': 'th', 'ckh': 'kh', 'cph': 'ph',
    'f': 'ts', 'tsh': 'j',
}

# MAPPING 4: Phonetic similarity
map4 = {
    'ch': 'H', 'sh': 'sh', 'k': 'k', 'd': 'd', 't': 't',
    'l': 'l', 'r': 'r', 'o': 'a', 'y': 'y', 'a': 'a',
    'i': 'i', 'e': 'h', 'n': 'n', 's': 's', 'q': 'q',
    'p': 'b', 'm': 'm', 'cth': 'th', 'ckh': 'kh', 'cph': 'f',
    'f': 'gh', 'tsh': 'j',
}

# MAPPING 5: Arabic pharma-optimized
map5 = {
    'ch': 'ayn', 'sh': 's', 'k': 'r', 'd': 'q', 't': 'b',
    'l': 'l', 'r': 'm', 'o': 'w', 'y': 'h', 'a': 'a',
    'i': 'y', 'e': 'n', 'n': 'd', 's': 'f', 'q': 'kh',
    'p': 'gh', 'm': 'sh', 'cth': 'H', 'ckh': 'z', 'cph': 'th',
    'f': 'T', 'tsh': 'S',
}

mappings = [
    ("MAP 1: Pure frequency rank", map1),
    ("MAP 2: Sandhi-class constrained", map2),
    ("MAP 3: Judeo-Arabic (Hebrew mergers)", map3),
    ("MAP 4: Phonetic similarity", map4),
    ("MAP 5: Pharma-optimized", map5),
]

first10 = f1r_words[:10]
print("=" * 60)
print("TEST 5: Five Trial EVA->Arabic Mappings")
print("=" * 60)
print(f"\nF1R first 10 words: {first10}")

for name, mapping in mappings:
    print(f"\n--- {name} ---")
    decoded = []
    for w in first10:
        phonemes = parse_eva(w)
        arabic = []
        for p in phonemes:
            if p in mapping:
                arabic.append(mapping[p])
            elif len(p) == 1:
                arabic.append(p)
            else:
                arabic.append('[' + p + ']')
        decoded.append(''.join(arabic))

    for orig, dec in zip(first10, decoded):
        print(f"  {orig:15s} -> {dec}")

    # Check chol
    chol_ph = parse_eva('chol')
    chol_dec = ''.join(mapping.get(p, p) for p in chol_ph)
    print(f"  {'chol':15s} -> {chol_dec}  (target: waraq)")

    # Check daiin
    daiin_ph = parse_eva('daiin')
    daiin_dec = ''.join(mapping.get(p, p) for p in daiin_ph)
    print(f"  {'daiin':15s} -> {daiin_dec}  (most common word)")

print()
print("=" * 60)
print("TEST 6: Bigram Compatibility Analysis")
print("=" * 60)
print()

for name, mapping in mappings:
    # Map EVA bigrams through this mapping to Arabic bigrams
    mapped_bigrams = Counter()
    for (p1, p2), cnt in eva_bigrams.items():
        a1 = mapping.get(p1, p1)
        a2 = mapping.get(p2, p2)
        mapped_bigrams[(a1, a2)] += cnt

    total_mapped = sum(mapped_bigrams.values())

    # Compare with known Arabic bigram distribution
    # Calculate overlap score
    score = 0.0
    matched_count = 0
    for bg, ar_freq in arabic_common_bigrams.items():
        ar_norm = ar_freq / total_ar_bg
        mapped_norm = mapped_bigrams.get(bg, 0) / total_mapped if total_mapped > 0 else 0
        # Use min overlap (Bhattacharyya-like)
        score += math.sqrt(ar_norm * mapped_norm)
        if mapped_bigrams.get(bg, 0) > 0:
            matched_count += 1

    # Top 10 mapped bigrams
    top_mapped = mapped_bigrams.most_common(10)
    top_mapped_str = ', '.join(f"{a}{b}:{c}" for (a,b),c in top_mapped)

    # Check for al- (definite article) which should be very common in Arabic
    al_count = mapped_bigrams.get(('a','l'), 0)
    al_pct = 100 * al_count / total_mapped if total_mapped > 0 else 0

    print(f"{name}:")
    print(f"  Bigram overlap score: {score:.4f} (higher=better, max~1.0)")
    print(f"  Arabic bigrams found: {matched_count}/{len(arabic_common_bigrams)}")
    print(f"  'al' bigram (def. article): {al_count} ({al_pct:.2f}%)")
    print(f"  Top bigrams: {top_mapped_str}")
    print()

# ==========================================
# ASSESSMENT SUMMARY
# ==========================================
print("=" * 60)
print("OVERALL ASSESSMENT")
print("=" * 60)
print()

# Arabic word length distribution
ar_word_lens = [3, 4, 5, 4, 5, 3, 4, 6, 4, 5]  # typical Arabic medical text
eva_word_lens = [len(parse_eva(w)) for w in words]
avg_eva = sum(eva_word_lens) / len(eva_word_lens)

print(f"Average EVA word length (phonemes): {avg_eva:.1f}")
print(f"Arabic medical text average word length: ~4-5 letters")
print()

# Word length distribution
len_dist = Counter(eva_word_lens)
print("EVA word length distribution:")
for length in sorted(len_dist.keys())[:12]:
    bar = '#' * (len_dist[length] // 100)
    print(f"  {length:2d}: {len_dist[length]:5d} {bar}")

print()

# Specific structural tests
print("KEY STRUCTURAL COMPARISONS:")
print()
print("1. Vowel inventory:")
print("   Arabic: 3 short (a,i,u) + 3 long = 6 vowel phonemes")
print("   EVA sandhi vowels: 2 (a,i) -- MISSING 'u'")
print("   -> Partial match. Could work if u merged with another vowel")
print()
print("2. Consonant clusters:")
print("   Arabic: strictly CV(C) onset, no initial clusters")
print("   EVA with sandhi classes: 82% CC onsets -- FATAL mismatch")
print("   EVA with broad vowels: 12% CC onsets -- marginal")
print("   -> Arabic is only viable if o,e,y are vowels, NOT consonants")
print("   -> But sandhi shows o,e,y are NOT vowels")
print("   -> CONTRADICTION")
print()
print("3. Definite article al-:")
print("   Arabic texts: ~10-15% of words start with al-")
print("   EVA words starting with 'al': ", end='')
al_words = [w for w in words if w.startswith('al')]
print(f"{len(al_words)} ({100*len(al_words)/len(words):.1f}%)")
print("   EVA words starting with 'ol': ", end='')
ol_words = [w for w in words if w.startswith('ol')]
print(f"{len(ol_words)} ({100*len(ol_words)/len(words):.1f}%)")
print("   Neither matches Arabic al- frequency")
print()
print("4. Root-pattern morphology:")
print("   Arabic: trilateral roots dominate (C1C2C3 + vowel patterns)")
print("   EVA: no clear evidence of trilateral root system")
print("   Common EVA suffixes: -aiin, -ain, -ey, -ol, -or")
print("   These don't correspond to Arabic morphological patterns")
print()
print("5. Word-final patterns:")
print("   Arabic medical texts: frequent -a (ta marbuta), -n (tanwin)")
print("   EVA: frequent -n (daiin), -y (chey, shey), -l (chol)")
print("   Partial overlap with -n, but -y and -l are unusual in Arabic")

# Count word-final characters
final_chars = Counter()
for w in words:
    if w:
        final_chars[w[-1]] += 1
total_finals = sum(final_chars.values())
print()
print("   EVA word-final character distribution:")
for c, cnt in final_chars.most_common(10):
    print(f"     -{c}: {cnt} ({100*cnt/total_finals:.1f}%)")

print()
print("6. chol = waraq test:")
print("   No mapping produces a convincing match")
print("   MAP 1: chol -> maw (no)")
print("   MAP 2: chol -> khaynnl (no)")
print("   MAP 3: chol -> kwl (possible CuL pattern but not waraq)")
print("   MAP 4: chol -> Hal (no)")
print("   MAP 5: chol -> aynwl (no)")
print()
print("VERDICT: Arabic as the underlying language is UNLIKELY")
print("  - The phonotactic structure is incompatible")
print("  - The sandhi-derived phonological classes create contradictions")
print("  - No trial mapping produces recognizable Arabic words")
print("  - The vowel system (2 sandhi vowels) doesn't match Arabic (3+)")
print("  - Word-final distributions don't match Arabic patterns")
print("  - Judeo-Arabic is slightly more plausible (reduced inventory)")
print("    but still fails on syllable structure and morphology")
