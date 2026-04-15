import re
from collections import Counter, defaultdict

# Read the file
with open("C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extract words from the transcription
words = []
for line in text.split('\n'):
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    # Check if it's a metadata-only line
    m = re.match(r'^<f\d+[rv]>\s+<', line)
    if m and '.' not in line.split('>')[0]:
        continue
    # Extract the text portion after the tag
    match = re.match(r'<[^>]+>\s+(.*)', line)
    if match:
        content = match.group(1)
    else:
        content = line
    # Remove annotations like @221; {cto} etc
    content = re.sub(r'@\d+;?', '', content)
    content = re.sub(r'\{[^}]*\}', '', content)
    content = re.sub(r'<[^>]*>', '', content)
    content = re.sub(r"['\?,]", '', content)
    # Split on dots and whitespace
    for w in re.split(r'[\s.]+', content):
        w = w.strip()
        if w and len(w) > 0:
            if re.match(r'^[a-z]+$', w):
                words.append(w)

print(f"Total words extracted: {len(words)}")
print(f"Unique words: {len(set(words))}")

# Define EVA vowels
eva_vowels_with_o = set('aeio')
eva_vowels_without_o = set('aei')

# EVA digraphs that likely represent single phonemes
digraphs = ['cth', 'ckh', 'cph', 'cfh', 'sh', 'ch']

def strip_vowels(word, vowels):
    return ''.join(c for c in word if c not in vowels)

def tokenize_eva(word):
    tokens = []
    i = 0
    while i < len(word):
        matched = False
        for dg in digraphs:
            if word[i:i+len(dg)] == dg:
                tokens.append(dg)
                i += len(dg)
                matched = True
                break
        if not matched:
            tokens.append(word[i])
            i += 1
    return tokens

def get_phonemic_root(word, vowels):
    tokens = tokenize_eva(word)
    return tuple(t for t in tokens if t not in vowels)

def get_vowel_pattern(word, vowels):
    return ''.join(c if c in vowels else 'C' for c in word)

def get_phonemic_pattern(word, vowels):
    tokens = tokenize_eva(word)
    return tuple('V' if t in vowels else 'C' for t in tokens)

# =====================================================
# 1. EXTRACT CONSONANT ROOTS
# =====================================================
print("\n" + "="*80)
print("1. CONSONANT ROOT EXTRACTION")
print("="*80)

# Scenario A: o is a vowel (letter-level)
roots_o_vowel = Counter()
root_to_words_ov = defaultdict(set)
for w in words:
    root = strip_vowels(w, eva_vowels_with_o)
    if root:
        roots_o_vowel[root] += 1
        root_to_words_ov[root].add(w)

# Scenario B: o is a consonant (letter-level)
roots_o_cons = Counter()
root_to_words_oc = defaultdict(set)
for w in words:
    root = strip_vowels(w, eva_vowels_without_o)
    if root:
        roots_o_cons[root] += 1
        root_to_words_oc[root].add(w)

print(f"\nScenario A (o=vowel): {len(roots_o_vowel)} unique consonant skeletons")
print(f"Scenario B (o=consonant): {len(roots_o_cons)} unique consonant skeletons")

print("\n--- Top 30 roots (o=vowel) ---")
for root, count in roots_o_vowel.most_common(30):
    forms = sorted(root_to_words_ov[root])[:8]
    print(f"  {root:15s} ({count:4d}x) forms: {', '.join(forms)}")

print("\n--- Top 30 roots (o=consonant) ---")
for root, count in roots_o_cons.most_common(30):
    forms = sorted(root_to_words_oc[root])[:8]
    print(f"  {root:15s} ({count:4d}x) forms: {', '.join(forms)}")

# =====================================================
# PHONEMIC ROOT EXTRACTION
# =====================================================
print("\n" + "="*80)
print("1b. PHONEMIC ROOT EXTRACTION (digraphs as units)")
print("="*80)

phonemic_roots_ov = Counter()
phonemic_root_to_words_ov = defaultdict(set)
phonemic_roots_oc = Counter()
phonemic_root_to_words_oc = defaultdict(set)

for w in words:
    root_ov = get_phonemic_root(w, eva_vowels_with_o)
    root_oc = get_phonemic_root(w, eva_vowels_without_o)
    phonemic_roots_ov[root_ov] += 1
    phonemic_root_to_words_ov[root_ov].add(w)
    phonemic_roots_oc[root_oc] += 1
    phonemic_root_to_words_oc[root_oc].add(w)

print(f"\nWith digraph tokenization:")
print(f"  Unique phonemic roots (o=vowel): {len(phonemic_roots_ov)}")
print(f"  Unique phonemic roots (o=consonant): {len(phonemic_roots_oc)}")

# Root length distribution (phonemic)
phon_root_len_ov = Counter()
phon_root_len_oc = Counter()
for r, c in phonemic_roots_ov.items():
    phon_root_len_ov[len(r)] += c
for r, c in phonemic_roots_oc.items():
    phon_root_len_oc[len(r)] += c

print(f"\nPhonemic root length distribution (o=vowel, weighted by freq):")
for l in sorted(phon_root_len_ov.keys()):
    pct = phon_root_len_ov[l] / len(words) * 100
    print(f"  {l} consonants: {phon_root_len_ov[l]:5d} tokens ({pct:.1f}%)")

print(f"\nPhonemic root length distribution (o=consonant, weighted by freq):")
for l in sorted(phon_root_len_oc.keys()):
    pct = phon_root_len_oc[l] / len(words) * 100
    print(f"  {l} consonants: {phon_root_len_oc[l]:5d} tokens ({pct:.1f}%)")

# Top phonemic roots
print("\n--- Top 25 phonemic roots (o=vowel) ---")
for root, count in phonemic_roots_ov.most_common(25):
    root_str = '-'.join(root)
    forms = sorted(phonemic_root_to_words_ov[root])[:8]
    print(f"  {root_str:20s} ({count:4d}x, {len(phonemic_root_to_words_ov[root])} forms) e.g. {', '.join(forms)}")

print("\n--- Top 25 phonemic roots (o=consonant) ---")
for root, count in phonemic_roots_oc.most_common(25):
    root_str = '-'.join(root)
    forms = sorted(phonemic_root_to_words_oc[root])[:8]
    print(f"  {root_str:20s} ({count:4d}x, {len(phonemic_root_to_words_oc[root])} forms) e.g. {', '.join(forms)}")

# =====================================================
# 2. ROOT-PATTERN PARADIGM TABLES
# =====================================================
print("\n" + "="*80)
print("2. PHONEMIC PARADIGM TABLES (o=vowel, roots with 5+ forms)")
print("="*80)

phon_paradigms = {r: ws for r, ws in phonemic_root_to_words_ov.items() if len(ws) >= 5}
print(f"Roots with 5+ forms: {len(phon_paradigms)}")
for root in sorted(phon_paradigms.keys(), key=lambda r: -len(phon_paradigms[r]))[:20]:
    root_str = '-'.join(root)
    forms = sorted(phon_paradigms[root])
    print(f"\n  Root: {root_str} ({len(forms)} forms)")
    for w in forms[:15]:
        tokens = tokenize_eva(w)
        pat = ''.join('V' if t in eva_vowels_with_o else 'C' for t in tokens)
        vowel_seq = ''.join(t for t in tokens if t in eva_vowels_with_o)
        freq = words.count(w)
        print(f"    {w:20s} pattern: {pat:12s} vowels: {vowel_seq:8s} freq: {freq}")

print("\n" + "="*80)
print("2b. PHONEMIC PARADIGM TABLES (o=consonant, roots with 5+ forms)")
print("="*80)

phon_paradigms_oc = {r: ws for r, ws in phonemic_root_to_words_oc.items() if len(ws) >= 5}
print(f"Roots with 5+ forms: {len(phon_paradigms_oc)}")
for root in sorted(phon_paradigms_oc.keys(), key=lambda r: -len(phon_paradigms_oc[r]))[:15]:
    root_str = '-'.join(root)
    forms = sorted(phon_paradigms_oc[root])
    print(f"\n  Root: {root_str} ({len(forms)} forms)")
    for w in forms[:15]:
        tokens = tokenize_eva(w)
        pat = ''.join('V' if t in eva_vowels_without_o else 'C' for t in tokens)
        vowel_seq = ''.join(t for t in tokens if t in eva_vowels_without_o)
        freq = words.count(w)
        print(f"    {w:20s} pattern: {pat:12s} vowels: {vowel_seq:8s} freq: {freq}")

# =====================================================
# 3. FREQUENCY OF VOWEL PATTERNS
# =====================================================
print("\n" + "="*80)
print("3. VOWEL PATTERN FREQUENCY (Top 25)")
print("="*80)

pattern_freq_ov = Counter()
pattern_freq_oc = Counter()
for w in words:
    tokens = tokenize_eva(w)
    p_ov = ''.join('V' if t in eva_vowels_with_o else 'C' for t in tokens)
    p_oc = ''.join('V' if t in eva_vowels_without_o else 'C' for t in tokens)
    pattern_freq_ov[p_ov] += 1
    pattern_freq_oc[p_oc] += 1

print("\n--- o=vowel (phonemic tokenization) ---")
for pat, count in pattern_freq_ov.most_common(25):
    pct = count / len(words) * 100
    examples = []
    for w in set(words):
        tokens = tokenize_eva(w)
        p = ''.join('V' if t in eva_vowels_with_o else 'C' for t in tokens)
        if p == pat:
            examples.append(w)
        if len(examples) >= 5:
            break
    print(f"  {pat:25s} {count:5d} ({pct:4.1f}%)  e.g. {', '.join(sorted(examples)[:5])}")

print("\n--- o=consonant (phonemic tokenization) ---")
for pat, count in pattern_freq_oc.most_common(25):
    pct = count / len(words) * 100
    examples = []
    for w in set(words):
        tokens = tokenize_eva(w)
        p = ''.join('V' if t in eva_vowels_without_o else 'C' for t in tokens)
        if p == pat:
            examples.append(w)
        if len(examples) >= 5:
            break
    print(f"  {pat:25s} {count:5d} ({pct:4.1f}%)  e.g. {', '.join(sorted(examples)[:5])}")

# =====================================================
# 4. KEY WORD ANALYSIS
# =====================================================
print("\n" + "="*80)
print("4. ANALYSIS OF KEY WORDS")
print("="*80)

test_words = ['chol', 'shol', 'chor', 'cthy', 'daiin', 'dain', 'sho', 'cho',
              'cthol', 'cthor', 'chey', 'shey', 'shody', 'chody', 'chodaiin',
              'shodaiin', 'dar', 'char', 'shar', 'dal', 'chal', 'chom', 'shor',
              'okaiin', 'otaiin', 'qokaiin', 'qotaiin']

for w in test_words:
    freq = words.count(w)
    tokens = tokenize_eva(w)
    root_ov = get_phonemic_root(w, eva_vowels_with_o)
    root_oc = get_phonemic_root(w, eva_vowels_without_o)
    pat_ov = ''.join('V' if t in eva_vowels_with_o else 'C' for t in tokens)
    pat_oc = ''.join('V' if t in eva_vowels_without_o else 'C' for t in tokens)
    print(f"  {w:15s} freq={freq:4d}  tokens={tokens}  root(V)={list(root_ov)}  root(C)={list(root_oc)}")

# Deep analysis of chol family
print("\n--- 'chol' family analysis ---")
chol_family = sorted([w for w in set(words) if 'chol' in w], key=lambda x: -words.count(x))
for w in chol_family[:20]:
    tokens = tokenize_eva(w)
    root = get_phonemic_root(w, eva_vowels_with_o)
    print(f"  {w:20s} freq={words.count(w):4d}  root={'-'.join(root)}")

# =====================================================
# 5. BILITERALISM VS TRILITERALISM
# =====================================================
print("\n" + "="*80)
print("5. ROOT LENGTH DISTRIBUTION (PHONEMIC)")
print("="*80)

# Already printed above, but add comparison
print("\nComparison with Arabic:")
print("  Arabic: ~80% of roots are triconsonantal (3 consonants)")
print("  Voynich (o=vowel):")
for l in sorted(phon_root_len_ov.keys()):
    pct = phon_root_len_ov[l] / len(words) * 100
    print(f"    {l} consonants: {pct:.1f}%")
print("  Voynich (o=consonant):")
for l in sorted(phon_root_len_oc.keys()):
    pct = phon_root_len_oc[l] / len(words) * 100
    print(f"    {l} consonants: {pct:.1f}%")

# Triconsonantal roots analysis
print("\n--- Triconsonantal roots with most forms (o=vowel) ---")
tricons = {r: ws for r, ws in phonemic_root_to_words_ov.items() if len(r) == 3 and len(ws) >= 3}
print(f"  Total triconsonantal roots with 3+ forms: {len(tricons)}")
for root in sorted(tricons.keys(), key=lambda r: -len(tricons[r]))[:20]:
    root_str = '-'.join(root)
    forms = sorted(tricons[root])
    print(f"  {root_str:20s} ({len(forms)} forms): {', '.join(forms[:10])}")

# =====================================================
# SUFFIX ANALYSIS
# =====================================================
print("\n" + "="*80)
print("SUFFIX / ENDING ANALYSIS")
print("="*80)

suffix_counts = Counter()
for w in words:
    if w.endswith('aiin'):
        suffix_counts['-aiin'] += 1
    elif w.endswith('ain'):
        suffix_counts['-ain'] += 1
    if w.endswith('dy'):
        suffix_counts['-dy'] += 1
    if w.endswith('ey'):
        suffix_counts['-ey'] += 1
    if w.endswith('y') and not w.endswith('ey') and not w.endswith('dy'):
        suffix_counts['-y (other)'] += 1
    if w.endswith('ol'):
        suffix_counts['-ol'] += 1
    if w.endswith('or'):
        suffix_counts['-or'] += 1
    if w.endswith('ar'):
        suffix_counts['-ar'] += 1
    if w.endswith('al'):
        suffix_counts['-al'] += 1
    if w.endswith('am'):
        suffix_counts['-am'] += 1
    if w.endswith('an'):
        suffix_counts['-an'] += 1
    if w.endswith('om'):
        suffix_counts['-om'] += 1

print("Common endings:")
for suffix, count in suffix_counts.most_common():
    print(f"  {suffix:12s}: {count:5d} ({count/len(words)*100:.1f}%)")

# =====================================================
# SEMITIC COMPATIBILITY METRICS
# =====================================================
print("\n" + "="*80)
print("SEMITIC COMPATIBILITY METRICS")
print("="*80)

total_unique_words = len(set(words))
total_unique_roots_ov = len(phonemic_roots_ov)
total_unique_roots_oc = len(phonemic_roots_oc)
print(f"\nRoot reuse ratio:")
print(f"  Unique words: {total_unique_words}")
print(f"  Unique phonemic roots (o=V): {total_unique_roots_ov}  ratio: {total_unique_words/total_unique_roots_ov:.2f} words/root")
print(f"  Unique phonemic roots (o=C): {total_unique_roots_oc}  ratio: {total_unique_words/total_unique_roots_oc:.2f} words/root")
print(f"  Arabic typical: ~3-5 words/root in running text")

# Pattern productivity
patterns_per_root = []
for root, ws in phonemic_root_to_words_ov.items():
    if len(ws) >= 2:
        patterns = set()
        for w in ws:
            pat = get_phonemic_pattern(w, eva_vowels_with_o)
            patterns.add(pat)
        patterns_per_root.append(len(patterns))

if patterns_per_root:
    avg_patterns = sum(patterns_per_root) / len(patterns_per_root)
    print(f"\nAvg distinct patterns per root (roots w/ 2+ forms, o=V): {avg_patterns:.2f}")
    print(f"  Max: {max(patterns_per_root)}")
    dist = Counter(patterns_per_root)
    print(f"  Distribution: {dict(sorted(dist.items()))}")

# Do same-root words appear in similar contexts?
print("\n--- Root semantic coherence test ---")
print("(Do words sharing a root appear on the same pages/sections?)")
# Check if root-sharing words cluster on same folios
folio_words = defaultdict(list)
current_folio = ""
for line in text.split('\n'):
    line = line.strip()
    folio_match = re.match(r'<(f\d+[rv])', line)
    if folio_match:
        current_folio = folio_match.group(1)
    if current_folio:
        content = re.sub(r'@\d+;?', '', line)
        content = re.sub(r'\{[^}]*\}', '', content)
        content = re.sub(r'<[^>]*>', '', content)
        content = re.sub(r"['\?,]", '', content)
        for w in re.split(r'[\s.]+', content):
            w = w.strip()
            if w and re.match(r'^[a-z]+$', w):
                folio_words[current_folio].append(w)

# For top roots, show folio distribution
print("\nFolio distribution of top phonemic roots (o=vowel):")
for root, count in phonemic_roots_ov.most_common(10):
    root_str = '-'.join(root)
    root_words = phonemic_root_to_words_ov[root]
    folio_dist = Counter()
    for folio, fwords in folio_words.items():
        for w in fwords:
            if w in root_words:
                folio_dist[folio] += 1
    n_folios = len(folio_dist)
    total_folios = len(folio_words)
    print(f"  {root_str:15s}: appears on {n_folios}/{total_folios} folios ({n_folios/total_folios*100:.0f}%)")
