#!/usr/bin/env python3
"""
Detailed root analysis: ch/sh minimal pair, compound root decomposition,
grade paradigm tables, and classifier analysis.
"""
import re
from collections import defaultdict, Counter

with open(r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Parse words with folio info
folio_words = {}
current_folio = None
all_words = []

def classify_folio(folio):
    f = folio.lower().replace('f','')
    num_match = re.match(r'(\d+)', f)
    if not num_match:
        return 'unknown'
    num = int(num_match.group(1))
    if num <= 57: return 'herbal'
    elif num <= 67: return 'pharma'
    elif num <= 73: return 'astro'
    elif num <= 84: return 'bio'
    elif num <= 86: return 'cosmo'
    elif num <= 98: return 'stars'
    elif num <= 116: return 'recipe'
    return 'other'

folio_sections = {}
for line in lines:
    line = line.strip()
    folio_match = re.match(r'<(f\d+[rv]\d?)>', line)
    if folio_match:
        current_folio = folio_match.group(1)
        folio_words.setdefault(current_folio, [])
        folio_sections[current_folio] = classify_folio(current_folio)
        continue
    line_match = re.match(r'<[^>]+>\s+(.*)', line)
    if line_match and current_folio:
        text = line_match.group(1)
        text = re.sub(r'\{[^}]*\}', '', text)
        text = re.sub(r'@\d+;?', '', text)
        text = re.sub(r'<[^>]*>', '', text)
        text = re.sub(r"['\?\*!,]", '', text)
        words = re.split(r'[\s.]+', text)
        words = [w.strip() for w in words if w.strip()]
        folio_words[current_folio].extend(words)
        for w in words:
            all_words.append((w, current_folio))

# ============================================================
# 1. ch/sh MINIMAL PAIR ANALYSIS
# ============================================================
print("=" * 80)
print("ch/sh MINIMAL PAIR: Words differing only in ch vs sh")
print("=" * 80)

word_freq = Counter(w for w, _ in all_words)

# Find ch-words and check if sh-variant exists
ch_words = {w: c for w, c in word_freq.items() if 'ch' in w and 'sh' not in w and 'tch' not in w and 'kch' not in w and 'lch' not in w and 'pch' not in w}

pairs = []
for w, c in sorted(ch_words.items(), key=lambda x: -x[1]):
    # Try replacing ch with sh
    sh_variant = w.replace('ch', 'sh', 1)
    if sh_variant in word_freq:
        pairs.append((w, c, sh_variant, word_freq[sh_variant]))

print(f"\nFound {len(pairs)} ch/sh minimal pairs")
print(f"\n{'ch-word':>20} {'freq':>6}  {'sh-word':>20} {'freq':>6}  {'ratio':>6}")
print("-" * 70)
for w1, c1, w2, c2 in pairs[:30]:
    ratio = c1 / c2 if c2 > 0 else 999
    print(f"{w1:>20} {c1:>6}  {w2:>20} {c2:>6}  {ratio:>6.1f}x")

# Section distribution of ch-only vs sh-only words
print("\n\nSection distribution of ch-only vs sh-only words:")
ch_section = Counter()
sh_section = Counter()
for w, folio in all_words:
    sec = folio_sections.get(folio, 'unknown')
    # Words where ch is the primary root (starts with ch or has ch after prefix)
    if w.startswith('ch') or (len(w) > 2 and w[1:3] == 'ch'):
        ch_section[sec] += 1
    if w.startswith('sh') or (len(w) > 2 and w[1:3] == 'sh'):
        sh_section[sec] += 1

print(f"\n{'Section':>10} {'ch-words':>10} {'sh-words':>10} {'ch/sh':>8}")
for sec in ['herbal','pharma','astro','bio','cosmo','stars','recipe']:
    c1 = ch_section.get(sec, 0)
    c2 = sh_section.get(sec, 0)
    ratio = c1 / c2 if c2 > 0 else 999
    print(f"{sec:>10} {c1:>10} {c2:>10} {ratio:>8.1f}x")

# ============================================================
# 2. COMPOUND ROOT DECOMPOSITION
# ============================================================
print("\n" + "=" * 80)
print("COMPOUND ROOT DECOMPOSITION")
print("=" * 80)

# If h is the universal root, then:
# ch = c + h, sh = s + h, kch = k + c + h, etc.
# The classifier before h determines the type

compound_roots = {
    'ch': 'c+h (aerial substance)',
    'sh': 's+h (underground substance)',
    'ckh': 'c+k+h (botanical-body substance)',
    'cth': 'c+t+h (botanical-process substance)',
    'kch': 'k+c+h (body-botanical substance)',
    'tch': 't+c+h (process-botanical substance)',
    'pch': 'p+c+h (preparation-botanical substance)',
    'lch': 'l+c+h (structural-botanical substance)',
    'lsh': 'l+s+h (structural-underground substance)',
}

print("\nCompound root frequencies and distributions:")
print(f"\n{'Root':<6} {'Decomp':<35} {'Total':>6}")
print("-" * 55)
for root, decomp in compound_roots.items():
    total = sum(1 for w, _ in all_words if root in w)
    print(f"{root:<6} {decomp:<35} {total:>6}")

# ============================================================
# 3. THE 5 SIMPLE ROOTS (non-h roots)
# ============================================================
print("\n" + "=" * 80)
print("SIMPLE ROOTS: k, t, l, r, p (non-h roots)")
print("=" * 80)

# For these roots, look at words where they appear WITHOUT any h-compound
simple_roots = ['k', 't', 'l', 'r', 'p']
for sr in simple_roots:
    # Count words where this root appears but NOT as part of any h-compound
    standalone_count = 0
    in_compound = 0
    examples = Counter()

    for w, _ in all_words:
        has_sr = False
        in_compound_flag = False

        # Check for standalone occurrence
        for m in re.finditer(re.escape(sr), w):
            pos = m.start()
            end = m.end()
            # Check if this is part of a compound with h
            context = w[max(0,pos-2):min(len(w),end+3)]
            if 'ch' in context or 'sh' in context or 'kh' in context or 'th' in context or 'ph' in context:
                in_compound_flag = True
            else:
                has_sr = True

        if has_sr and not in_compound_flag:
            standalone_count += 1
            examples[w] += 1
        elif in_compound_flag:
            in_compound += 1

    print(f"\n{sr}: standalone={standalone_count}, in_h_compound={in_compound}")
    print(f"  Top standalone words: {', '.join(f'{w}({c})' for w, c in examples.most_common(8))}")

# ============================================================
# 4. FULL GRADE PARADIGM for each root
# ============================================================
print("\n" + "=" * 80)
print("GRADE PARADIGMS: Stem forms for each root")
print("=" * 80)

# For roots ch, sh, k, t - find all stem forms
# Look for patterns like: root, root+e, root+ee, root+eo, root+eeo, root+eod
# With optional terminal d, s

stem_patterns = {
    'ch': [
        ('ch (bare)', r'\bch[ydlrsnm]'),
        ('che (+e)', r'\bche[ydlrsnm]'),
        ('chee (+ee)', r'\bchee[ydlrsnm]'),
        ('cheo (+eo)', r'\bcheo[dlrsnm]'),
        ('cheeo (+eeo)', r'\bcheeo'),
        ('cheod (+eod)', r'\bcheod'),
        ('cho (+o)', r'\bcho[dlrsnmky]'),
        ('chod (+od)', r'\bchod'),
    ],
    'sh': [
        ('sh (bare)', r'\bsh[ydlrsnm]'),
        ('she (+e)', r'\bshe[ydlrsnm]'),
        ('shee (+ee)', r'\bshee[ydlrsnm]'),
        ('sheo (+eo)', r'\bsheo[dlrsnm]'),
        ('sheeo (+eeo)', r'\bsheeo'),
        ('sheod (+eod)', r'\bsheod'),
        ('sho (+o)', r'\bsho[dlrsnmky]'),
        ('shod (+od)', r'\bshod'),
    ],
}

for root_name, patterns in stem_patterns.items():
    print(f"\n{root_name} paradigm:")
    for label, pat in patterns:
        matches = []
        for w, _ in all_words:
            if re.search(pat, w):
                matches.append(w)
        mc = Counter(matches)
        total = len(matches)
        top = ', '.join(f'{w}({c})' for w, c in mc.most_common(5))
        print(f"  {label:>20}: {total:>5}  [{top}]")

# ============================================================
# 5. CLASSIFIER ANALYSIS (what precedes the root)
# ============================================================
print("\n" + "=" * 80)
print("CLASSIFIER ANALYSIS: What character class precedes 'h' in each root?")
print("=" * 80)

# The key question: is the character before 'h' a classifier?
# ch: c before h
# sh: s before h
# In ckh: c,k before h
# In cth: c,t before h

# Count words by their initial consonant cluster leading to h
h_words = Counter()
for w, _ in all_words:
    # Find all 'h' positions
    for i, c in enumerate(w):
        if c == 'h':
            # What precedes h?
            prefix = w[:i]
            # Get just the consonants right before h
            cons_before = ''
            j = i - 1
            while j >= 0 and w[j] not in 'aeiouy':
                cons_before = w[j] + cons_before
                j -= 1
            if cons_before:
                h_words[cons_before] += 1

print(f"\nConsonant clusters before 'h':")
print(f"{'Cluster':>10} {'Count':>8} {'Interpretation':>30}")
print("-" * 55)
for cluster, count in h_words.most_common(20):
    print(f"{cluster:>10} {count:>8}")

# ============================================================
# 6. TERMINAL MARKER ANALYSIS
# ============================================================
print("\n" + "=" * 80)
print("TERMINAL MARKER ANALYSIS")
print("=" * 80)

# What is the last character of each word?
final_char = Counter()
for w, _ in all_words:
    if w:
        final_char[w[-1]] += 1

print("\nWord-final character distribution:")
for ch, cnt in final_char.most_common():
    pct = cnt / len(all_words) * 100
    print(f"  {ch}: {cnt:>6} ({pct:.1f}%)")

# Word-final 2-char combinations
final_2 = Counter()
for w, _ in all_words:
    if len(w) >= 2:
        final_2[w[-2:]] += 1

print("\nWord-final 2-char combinations (top 20):")
for ch, cnt in final_2.most_common(20):
    pct = cnt / len(all_words) * 100
    print(f"  {ch}: {cnt:>6} ({pct:.1f}%)")

# ============================================================
# 7. RECIPE vs HERBAL: Which roots are enriched?
# ============================================================
print("\n" + "=" * 80)
print("RECIPE vs HERBAL ENRICHMENT")
print("=" * 80)

roots_to_check = ['ch', 'sh', 'k', 't', 'l', 'r', 'lk', 'kch', 'tch', 'cth', 'ckh', 'lch', 'pch', 'lsh', 'cph', 'p']

herbal_total = sum(1 for _, f in all_words if folio_sections.get(f) == 'herbal')
recipe_total = sum(1 for _, f in all_words if folio_sections.get(f) == 'recipe')

print(f"\nHerbal words: {herbal_total}, Recipe words: {recipe_total}")
print(f"\n{'Root':<8} {'Herbal':>8} {'H%':>6} {'Recipe':>8} {'R%':>6} {'Enrich':>8}")
print("-" * 55)

for root in roots_to_check:
    h_count = 0
    r_count = 0
    for w, f in all_words:
        sec = folio_sections.get(f, '')
        if root in w:
            if sec == 'herbal':
                h_count += 1
            elif sec == 'recipe':
                r_count += 1
    h_pct = h_count / herbal_total * 100 if herbal_total > 0 else 0
    r_pct = r_count / recipe_total * 100 if recipe_total > 0 else 0
    enrich = r_pct / h_pct if h_pct > 0 else 0
    print(f"{root:<8} {h_count:>8} {h_pct:>5.1f}% {r_count:>8} {r_pct:>5.1f}% {enrich:>7.2f}x")

# ============================================================
# 8. BIO SECTION ANALYSIS (which roots dominate?)
# ============================================================
print("\n" + "=" * 80)
print("BIO SECTION ROOT PROFILE")
print("=" * 80)

bio_total = sum(1 for _, f in all_words if folio_sections.get(f) == 'bio')
print(f"Bio section words: {bio_total}")

bio_roots = Counter()
for w, f in all_words:
    if folio_sections.get(f) != 'bio':
        continue
    for root in roots_to_check:
        if root in w:
            bio_roots[root] += 1

print(f"\n{'Root':<8} {'Count':>8} {'% of bio':>10}")
print("-" * 30)
for root, cnt in bio_roots.most_common():
    pct = cnt / bio_total * 100
    print(f"{root:<8} {cnt:>8} {pct:>9.1f}%")
