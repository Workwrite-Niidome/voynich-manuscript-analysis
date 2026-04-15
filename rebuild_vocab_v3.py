#!/usr/bin/env python3
"""
v3 - Deep analysis of -y class, -edy morphology, and reading attempts.
"""

import re
from collections import Counter, defaultdict

filepath = r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt'

folio_lang = {}
parsed_lines = []

with open(filepath, 'r', encoding='utf-8') as f:
    current_folio = None
    for raw in f:
        raw = raw.rstrip('\n')
        if raw.startswith('#'):
            continue
        m = re.match(r'^<(f\d+[rv]\d?)>\s+<.*?\$L=(\w).*?>', raw)
        if m:
            current_folio = m.group(1)
            folio_lang[current_folio] = m.group(2)
            continue
        m2 = re.match(r'^<(f\d+[rv]\d?\.\d+(?:,\S+)?)>\s+(.*)', raw)
        if m2:
            parsed_lines.append((current_folio, m2.group(1), m2.group(2)))

def extract_words(text):
    text = re.sub(r'\{[^}]*\}', '', text)
    text = re.sub(r'@\d+;?', '', text)
    text = text.replace('<->', ' ')
    text = text.replace('.', ' ')
    tokens = re.split(r'[^a-z\']+', text.lower())
    return [t for t in tokens if t and re.match(r'^[a-z\']+$', t)]

word_freq = Counter()
word_bigrams = []

for folio, line_id, text in parsed_lines:
    words = extract_words(text)
    for w in words:
        word_freq[w] += 1
    for i in range(len(words) - 1):
        word_bigrams.append((words[i], words[i+1]))

# ============================================
# The -y paradigm in detail
# ============================================

# Classify all word endings
ending_classes = Counter()
for w, f in word_freq.items():
    if w.endswith('aiin') or w.endswith('aiir') or w.endswith('aiil'):
        ending_classes['aiin-class'] += f
    elif w.endswith('ain') or w.endswith('air') or w.endswith('ail'):
        ending_classes['ain-class'] += f
    elif w.endswith('edy'):
        ending_classes['-edy'] += f
    elif w.endswith('eedy'):
        pass  # already counted in -edy
    elif w.endswith('eey'):
        ending_classes['-eey'] += f
    elif w.endswith('ey'):
        ending_classes['-ey'] += f
    elif w.endswith('dy') and not w.endswith('edy'):
        ending_classes['-dy'] += f
    elif w.endswith('y') and not any(w.endswith(s) for s in ['ey', 'dy', 'edy', 'eey']):
        ending_classes['-y(other)'] += f
    elif w.endswith('ol'):
        ending_classes['-ol'] += f
    elif w.endswith('or'):
        ending_classes['-or'] += f
    elif w.endswith('on'):
        ending_classes['-on'] += f
    elif w.endswith('n') and not any(w.endswith(s) for s in ['on', 'in', 'ain', 'aiin']):
        ending_classes['-n(other)'] += f
    elif w.endswith('l') and not w.endswith('ol'):
        ending_classes['-l(other)'] += f
    elif w.endswith('r') and not w.endswith('or'):
        ending_classes['-r(other)'] += f
    else:
        ending_classes['other'] += f

print("=== Word ending classification ===")
for cls, count in ending_classes.most_common():
    print(f"  {cls:>15}: {count:>5} ({100*count/sum(ending_classes.values()):.1f}%)")

# ============================================
# -ey sub-analysis: is it a different suffix from -y?
# ============================================

print("\n=== -ey vs -y (excluding -ey) words ===")
# Check: do -ey words show the same stem+suffix structure as -ol/-or/-on?
# Theory: -ey might be part of the sandhi paradigm too

# Words ending in -ey that also have -el, -er forms
ey_stems = defaultdict(int)
for w, f in word_freq.items():
    if w.endswith('ey') and not w.endswith('eey'):
        ey_stems[w[:-2]] += f

el_stems = defaultdict(int)
er_stems = defaultdict(int)
en_stems = defaultdict(int)
for w, f in word_freq.items():
    if w.endswith('el') and len(w) > 2:
        el_stems[w[:-2]] += f
    if w.endswith('er') and len(w) > 2:
        er_stems[w[:-2]] += f
    if w.endswith('en') and len(w) > 2:
        en_stems[w[:-2]] += f

print("\nStems with both -ey and -el/-er forms:")
for stem in sorted(ey_stems, key=lambda s: -ey_stems[s]):
    ey_f = ey_stems[stem]
    el_f = el_stems.get(stem, 0)
    er_f = er_stems.get(stem, 0)
    en_f = en_stems.get(stem, 0)
    if ey_f >= 10 and (el_f > 0 or er_f > 0):
        print(f"  {stem:>10}: -ey={ey_f:>4} -el={el_f:>4} -er={er_f:>4} -en={en_f:>4}")

# ============================================
# The complete paradigm: -ol/-or/-on vs -ey/-el/-er vs -edy/-eey
# ============================================

print("\n=== FULL PARADIGM TABLE ===")
print("If -ol and -edy are the same morpheme, and n/l/r are sandhi,")
print("then -edy/-edl/-edr and -eey/-eel/-eer should also show sandhi.")
print()

# Count -ed + n/l/r
for ending in ['edn', 'edl', 'edr', 'edy', 'een', 'eel', 'eer', 'eey']:
    count = sum(f for w, f in word_freq.items() if w.endswith(ending))
    print(f"  -{ending}: {count:>5}")

# ============================================
# Attempt reading with full annotation system
# ============================================

print("\n\n=== ANNOTATED READING ATTEMPT ===")

# Build the vocabulary
# Function words: stems locked to -n (>90%, freq >= 20)
func_words = {
    'daiin': 'OF/GEN',     # genitive "of"
    'aiin': 'AND/CONJ',    # conjunction
    'saiin': 'PREP',       # preposition
    'okaiin': 'EACH',      # distributive
    'qokaiin': 'Q-EACH',   # q+distributive
    'otaiin': 'OT-FUNC',   # function
    'qotaiin': 'Q-OT-FUNC',
    'kaiin': 'K-FUNC',
    'raiin': 'R-FUNC',
    'chaiin': 'CH-FUNC',
    'taiin': 'T-FUNC',
    'lkaiin': 'LK-FUNC',
    'ytaiin': 'YT-FUNC',
    'ykaiin': 'YK-FUNC',
    'chodaiin': 'LEAF-OF',
    'qodaiin': 'Q-OF',
    'dain': 'THIS',        # demonstrative
    'ain': 'DET',          # determiner
    'okain': 'EACH-DET',
    'otain': 'OT-DET',
    'qokain': 'Q-EACH-DET',
    'qotain': 'Q-OT-DET',
}

# Also add sandhi variants of function words
func_stems_strict = {
    'daii': 'OF',
    'aii': 'AND',
    'saii': 'PREP',
    'okaii': 'EACH',
    'qokaii': 'Q-EACH',
    'otaii': 'OT-FUNC',
    'kaii': 'K-FUNC',
    'raii': 'R-FUNC',
    'chaii': 'CH-FUNC',
    'taii': 'T-FUNC',
}

# Plant vocabulary
plant_parts = {
    'cho': 'LEAF',
    'sho': 'ROOT',
    'ctho': 'BARK',
    'oto': 'STEM',
}

# Color/quality prefixes
prefixes = {
    'ok': 'ok',     # each/measure?
    'qok': 'qok',   # q+ok
    'ot': 'ot',     # stem/stalk?
    'qo': 'qo',     # q-prefix
    'da': 'da',     # demonstrative base
    'che': 'che',    # extended leaf?
    'she': 'she',    # extended root?
}

def deep_annotate(word):
    """Full annotation."""
    # Direct function word match (with sandhi variants)
    if word in func_words:
        return f"[{func_words[word]}]"

    # Check if it's a sandhi variant of a function word
    stem_suffix = None
    if len(word) >= 2 and word[-1] in 'nlr':
        stem = word[:-1]
        suffix = word[-1]
        if stem in func_stems_strict:
            return f"[{func_stems_strict[stem]}-{suffix}]"

    # Plant parts with sandhi
    if len(word) >= 2 and word[-1] in 'nlr':
        stem = word[:-1]
        suffix = word[-1]
        if stem in plant_parts:
            return f"[{plant_parts[stem]}:{suffix}]"

    # -y ending words
    if word.endswith('y'):
        base = word[:-1]
        if base in plant_parts:
            return f"[{plant_parts[base]}.CIT]"
        # -edy
        if word.endswith('edy'):
            base2 = word[:-3]
            if base2 + 'o' in plant_parts:
                return f"[{plant_parts[base2+'o']}.B]"
            return f"{base2}[edy]"
        if word.endswith('eey'):
            base2 = word[:-3]
            return f"{base2}[eey]"
        return word

    # Bare stems
    if word in plant_parts:
        return f"[{plant_parts[word]}]"

    # Default: show stem+suffix
    if len(word) >= 2 and word[-1] in 'nlr':
        return f"{word[:-1]}[-{word[-1]}]"

    return word

# Read f1r lines 1-3
print("--- f1r lines 1-3 ---")
for folio, line_id, text in parsed_lines:
    if folio == 'f1r' and any(f'f1r.{i},' in line_id for i in [1,2,3]):
        words = extract_words(text)
        raw_line = ' '.join(words)
        ann_line = ' '.join(deep_annotate(w) for w in words)
        print(f"\n  RAW: {raw_line}")
        print(f"  ANN: {ann_line}")

# Read f47r lines 5-8
print("\n--- f47r lines 5-8 ---")
for folio, line_id, text in parsed_lines:
    if folio == 'f47r' and any(f'f47r.{i},' in line_id for i in [5,6,7,8]):
        words = extract_words(text)
        raw_line = ' '.join(words)
        ann_line = ' '.join(deep_annotate(w) for w in words)
        print(f"\n  RAW: {raw_line}")
        print(f"  ANN: {ann_line}")

# ============================================
# Extra: What percentage of words can we now classify?
# ============================================
print("\n\n=== VOCABULARY COVERAGE ===")
classified = 0
total = 0
for w, f in word_freq.items():
    total += f
    ann = deep_annotate(w)
    if ann.startswith('[') and ann.endswith(']'):
        classified += f

print(f"Words classifiable: {classified}/{total} ({100*classified/total:.1f}%)")

# Function words alone
func_total = 0
for w, f in word_freq.items():
    ann = deep_annotate(w)
    if 'FUNC' in ann or 'OF' in ann or 'AND' in ann or 'PREP' in ann or 'EACH' in ann or 'DET' in ann or 'THIS' in ann:
        func_total += f
print(f"Function words: {func_total} ({100*func_total/total:.1f}%)")

plant_total = 0
for w, f in word_freq.items():
    ann = deep_annotate(w)
    if 'LEAF' in ann or 'ROOT' in ann or 'BARK' in ann or 'STEM' in ann:
        plant_total += f
print(f"Plant vocabulary: {plant_total} ({100*plant_total/total:.1f}%)")
