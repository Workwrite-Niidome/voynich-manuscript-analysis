import re
from collections import defaultdict, Counter

# Read the file
with open("C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Extract words from EVA transcription
all_words = []
for line in lines:
    line = line.strip()
    # Skip metadata/header lines
    if line.startswith('#'):
        continue
    # Extract the text portion after the folio/line reference
    m = re.match(r'<[^>]+>\s+(.*)', line)
    if not m:
        continue
    text = m.group(1)
    # Skip pure metadata lines
    if text.startswith('<!'):
        continue
    # Remove inline comments {}, @-codes, <->
    text = re.sub(r'\{[^}]*\}', '', text)
    text = re.sub(r'@\d+;?', '', text)
    text = re.sub(r'<->', ' ', text)
    text = re.sub(r'[?,!\*\']', '', text)
    # Split into words by '.' or whitespace
    tokens = re.split(r'[.\s]+', text)
    # Clean each word
    for w in tokens:
        w = w.strip()
        w = re.sub(r'[^a-z]', '', w)
        if w:
            all_words.append(w)

print(f"Total words extracted: {len(all_words)}")

def get_initial(word):
    if len(word) == 0:
        return None
    trigraphs = ['cth', 'ckh', 'cfh', 'cph', 'tsh']
    digraphs = ['ch', 'sh', 'ck', 'ct', 'cf', 'cp', 'qo', 'ts']
    for tg in trigraphs:
        if word.startswith(tg):
            return tg
    for dg in digraphs:
        if word.startswith(dg):
            return dg
    return word[0]

def get_simple_initial(word):
    if len(word) == 0:
        return None
    return word[0]

def get_suffix(word):
    if not word:
        return None
    if word.endswith('r'):
        return 'r'
    elif word.endswith('l'):
        return 'l'
    elif word.endswith('n'):
        return 'n'
    elif word.endswith('y'):
        return 'y'
    elif word.endswith('m'):
        return 'm'
    elif word.endswith('s'):
        return 's'
    else:
        return word[-1]

# Build bigram analysis
suffix_initial_pairs = []
for i in range(len(all_words) - 1):
    w1 = all_words[i]
    w2 = all_words[i+1]
    suf = get_suffix(w1)
    init_simple = get_simple_initial(w2)
    init_full = get_initial(w2)
    if suf and init_simple:
        suffix_initial_pairs.append((suf, init_simple, init_full, w1, w2))

print(f"Total bigram pairs: {len(suffix_initial_pairs)}")

# ============================================================
# ANALYSIS 1: For each initial character, what suffix precedes it?
# ============================================================
print("\n" + "="*80)
print("ANALYSIS 1: PHONOLOGICAL CLASS ASSIGNMENT")
print("What suffix does each word-initial character trigger in the PRECEDING word?")
print("="*80)

init_trigger = defaultdict(Counter)
for suf, init_s, init_f, w1, w2 in suffix_initial_pairs:
    init_trigger[init_s][suf] += 1

init_trigger_digraph = defaultdict(Counter)
for suf, init_s, init_f, w1, w2 in suffix_initial_pairs:
    init_trigger_digraph[init_f][suf] += 1

print("\n--- By first letter of following word ---")
print(f"{'Init':>6} {'Total':>6} {'%-r':>6} {'%-l':>6} {'%-n':>6} {'%-y':>6} {'%-m':>6} {'%-s':>6} {'other':>6} | {'Likely class'}")
print("-" * 90)

init_class_data = {}
for init in sorted(init_trigger.keys()):
    counts = init_trigger[init]
    total = sum(counts.values())
    if total < 20:
        continue
    r_pct = counts['r'] / total * 100
    l_pct = counts['l'] / total * 100
    n_pct = counts['n'] / total * 100
    y_pct = counts['y'] / total * 100
    m_pct = counts['m'] / total * 100
    s_pct = counts['s'] / total * 100
    other_pct = (total - counts['r'] - counts['l'] - counts['n'] - counts['y'] - counts['m'] - counts['s']) / total * 100

    rln_total = counts['r'] + counts['l'] + counts['n']
    if rln_total > 0:
        r_rln = counts['r'] / rln_total * 100
        l_rln = counts['l'] / rln_total * 100
        n_rln = counts['n'] / rln_total * 100
    else:
        r_rln = l_rln = n_rln = 0

    if r_rln > 45:
        cls = "VOWEL (triggers -r)"
    elif l_rln > 40:
        cls = "STOP (triggers -l)"
    elif n_rln > 35:
        cls = "FRICATIVE (triggers -n)"
    else:
        cls = "MIXED"

    init_class_data[init] = {
        'total': total, 'r': counts['r'], 'l': counts['l'], 'n': counts['n'],
        'y': counts['y'], 'r_pct': r_pct, 'l_pct': l_pct, 'n_pct': n_pct,
        'r_rln': r_rln, 'l_rln': l_rln, 'n_rln': n_rln, 'class': cls
    }

    print(f"{init:>6} {total:>6} {r_pct:>5.1f}% {l_pct:>5.1f}% {n_pct:>5.1f}% {y_pct:>5.1f}% {m_pct:>5.1f}% {s_pct:>5.1f}% {other_pct:>5.1f}% | {cls}")

# Digraph-level analysis
print("\n--- By digraph initial of following word ---")
print(f"{'Init':>6} {'Total':>6} {'%-r':>6} {'%-l':>6} {'%-n':>6} {'%-y':>6} {'r/rln':>6} {'l/rln':>6} {'n/rln':>6} | {'Class'}")
print("-" * 100)

digraph_class_data = {}
for init in sorted(init_trigger_digraph.keys(), key=lambda x: -sum(init_trigger_digraph[x].values())):
    counts = init_trigger_digraph[init]
    total = sum(counts.values())
    if total < 15:
        continue
    r_pct = counts['r'] / total * 100
    l_pct = counts['l'] / total * 100
    n_pct = counts['n'] / total * 100
    y_pct = counts['y'] / total * 100

    rln_total = counts['r'] + counts['l'] + counts['n']
    if rln_total > 0:
        r_rln = counts['r'] / rln_total * 100
        l_rln = counts['l'] / rln_total * 100
        n_rln = counts['n'] / rln_total * 100
    else:
        r_rln = l_rln = n_rln = 0

    if r_rln > 45:
        cls = "VOWEL"
    elif l_rln > 40:
        cls = "STOP"
    elif n_rln > 35:
        cls = "FRIC/NASAL"
    else:
        cls = "MIXED"

    digraph_class_data[init] = {
        'total': total, 'r': counts['r'], 'l': counts['l'], 'n': counts['n'],
        'r_rln': r_rln, 'l_rln': l_rln, 'n_rln': n_rln, 'class': cls
    }

    print(f"{init:>6} {total:>6} {r_pct:>5.1f}% {l_pct:>5.1f}% {n_pct:>5.1f}% {y_pct:>5.1f}% {r_rln:>5.1f}% {l_rln:>5.1f}% {n_rln:>5.1f}% | {cls}")

# ============================================================
# ANALYSIS 2: Vowel identification
# ============================================================
print("\n" + "="*80)
print("ANALYSIS 2: VOWEL IDENTIFICATION")
print("Do EVA a, o, e trigger -r (vowel behavior)?")
print("="*80)

for v in ['a', 'o', 'e', 'i', 'y']:
    if v in init_class_data:
        d = init_class_data[v]
        print(f"\n  '{v}' as word-initial (N={d['total']}):")
        print(f"    Preceded by: -r {d['r_pct']:.1f}%, -l {d['l_pct']:.1f}%, -n {d['n_pct']:.1f}%")
        print(f"    Among r/l/n: -r {d['r_rln']:.1f}%, -l {d['l_rln']:.1f}%, -n {d['n_rln']:.1f}%")
        print(f"    Classification: {d['class']}")
    else:
        ct = init_trigger[v]
        total = sum(ct.values())
        print(f"\n  '{v}' as word-initial: {total} occurrences (below threshold)")
        if total > 0:
            print(f"    -r: {ct['r']}, -l: {ct['l']}, -n: {ct['n']}")

# ============================================================
# ANALYSIS 3: Consonant subclasses
# ============================================================
print("\n" + "="*80)
print("ANALYSIS 3: CONSONANT SUBCLASSES")
print("Do EVA consonants form coherent phonological subclasses?")
print("="*80)

classes = defaultdict(list)
for init, data in init_class_data.items():
    classes[data['class']].append((init, data))

for cls_name, members in sorted(classes.items()):
    print(f"\n  {cls_name}:")
    for init, data in sorted(members, key=lambda x: -x[1]['total']):
        print(f"    {init}: r/l/n = {data['r_rln']:.0f}%/{data['l_rln']:.0f}%/{data['n_rln']:.0f}% (N={data['total']})")

# ============================================================
# ANALYSIS 4: Stem-suffix correlation
# ============================================================
print("\n" + "="*80)
print("ANALYSIS 4: STEM-FINAL VOWEL -> SUFFIX CORRELATION")
print("="*80)

stem_suffix = defaultdict(Counter)
for w in all_words:
    suf = get_suffix(w)
    if suf in ('r', 'l', 'n') and len(w) >= 2:
        penult = w[-2]
        stem_suffix[penult][suf] += 1

print(f"\n{'Stem-final':>10} {'Total':>6} {'->r':>6} {'->l':>6} {'->n':>6} | {'%-r':>6} {'%-l':>6} {'%-n':>6}")
print("-" * 70)
for char in sorted(stem_suffix.keys()):
    counts = stem_suffix[char]
    total = sum(counts.values())
    if total < 10:
        continue
    print(f"{char:>10} {total:>6} {counts['r']:>6} {counts['l']:>6} {counts['n']:>6} | {counts['r']/total*100:>5.1f}% {counts['l']/total*100:>5.1f}% {counts['n']/total*100:>5.1f}%")

# ============================================================
# ANALYSIS 5: Word-final character distribution
# ============================================================
print("\n" + "="*80)
print("ANALYSIS 5: WORD-FINAL CHARACTER DISTRIBUTION")
print("="*80)

final_counts = Counter()
for w in all_words:
    if w:
        final_counts[w[-1]] += 1

total_words = sum(final_counts.values())
print(f"\nTotal words: {total_words}")
for char, count in final_counts.most_common(20):
    print(f"  -{char}: {count:>5} ({count/total_words*100:.1f}%)")

# ============================================================
# ANALYSIS 6: The 'y' character analysis
# ============================================================
print("\n" + "="*80)
print("ANALYSIS 6: THE EVA 'y' CHARACTER")
print("="*80)

y_followed_by = Counter()
rln_followed_by = {'r': Counter(), 'l': Counter(), 'n': Counter()}

for i in range(len(all_words) - 1):
    w1 = all_words[i]
    w2 = all_words[i+1]
    init = get_simple_initial(w2)
    suf = get_suffix(w1)
    if suf == 'y':
        y_followed_by[init] += 1
    elif suf in ('r', 'l', 'n'):
        rln_followed_by[suf][init] += 1

print("\nWhat initial characters follow -y words?")
total_y_pairs = sum(y_followed_by.values())
for init, count in y_followed_by.most_common(15):
    print(f"  -y + {init}-: {count:>4} ({count/total_y_pairs*100:.1f}%)")

print("\nComparison: following-initial distribution by preceding suffix")
print(f"{'Init':>6} {'after-r':>8} {'after-l':>8} {'after-n':>8} {'after-y':>8}")
print("-" * 50)
all_inits = set()
for d in [y_followed_by, rln_followed_by['r'], rln_followed_by['l'], rln_followed_by['n']]:
    all_inits.update(d.keys())

total_r = sum(rln_followed_by['r'].values()) or 1
total_l = sum(rln_followed_by['l'].values()) or 1
total_n = sum(rln_followed_by['n'].values()) or 1
total_y_p = sum(y_followed_by.values()) or 1

for init in sorted(all_inits):
    r_p = rln_followed_by['r'][init] / total_r * 100
    l_p = rln_followed_by['l'][init] / total_l * 100
    n_p = rln_followed_by['n'][init] / total_n * 100
    y_p = y_followed_by[init] / total_y_p * 100
    print(f"{init:>6} {r_p:>7.1f}% {l_p:>7.1f}% {n_p:>7.1f}% {y_p:>7.1f}%")

print("\n\nCharacters preceding word-final -y:")
pre_y = Counter()
for w in all_words:
    if len(w) >= 2 and w[-1] == 'y':
        pre_y[w[-2]] += 1

total_pre_y = sum(pre_y.values())
for char, count in pre_y.most_common(15):
    print(f"  {char}y: {count:>4} ({count/total_pre_y*100:.1f}%)")

# ============================================================
# ANALYSIS 7: Word-initial character frequency
# ============================================================
print("\n" + "="*80)
print("ANALYSIS 7: WORD-INITIAL CHARACTER FREQUENCIES")
print("="*80)

init_freq = Counter()
init_freq_digraph = Counter()
for w in all_words:
    init_freq[w[0]] += 1
    init_freq_digraph[get_initial(w)] += 1

print("\nSimple initial (first letter):")
for char, count in init_freq.most_common(20):
    print(f"  {char}-: {count:>5} ({count/total_words*100:.1f}%)")

print("\nDigraph initial:")
for init, count in init_freq_digraph.most_common(25):
    print(f"  {init}-: {count:>5} ({count/total_words*100:.1f}%)")

# ============================================================
# ANALYSIS 8: Suffix choice conditioned on NEXT word initial
# ============================================================
print("\n" + "="*80)
print("ANALYSIS 8: SUFFIX CHOICE CONDITIONED ON NEXT WORD INITIAL")
print("(Only looking at words that end in r, l, or n)")
print("="*80)

next_init_suffix = defaultdict(Counter)
for suf, init_s, init_f, w1, w2 in suffix_initial_pairs:
    if suf in ('r', 'l', 'n'):
        next_init_suffix[init_s][suf] += 1

print(f"\n{'Next init':>10} {'Total':>6} {'%-r':>7} {'%-l':>7} {'%-n':>7} | {'Dominant'}")
print("-" * 60)
for init in sorted(next_init_suffix.keys()):
    counts = next_init_suffix[init]
    total = sum(counts.values())
    if total < 10:
        continue
    r_p = counts['r'] / total * 100
    l_p = counts['l'] / total * 100
    n_p = counts['n'] / total * 100
    dom = max(('r', r_p), ('l', l_p), ('n', n_p), key=lambda x: x[1])
    print(f"{init:>10} {total:>6} {r_p:>6.1f}% {l_p:>6.1f}% {n_p:>6.1f}% | -{dom[0]} ({dom[1]:.0f}%)")

next_init_suffix_dg = defaultdict(Counter)
for suf, init_s, init_f, w1, w2 in suffix_initial_pairs:
    if suf in ('r', 'l', 'n'):
        next_init_suffix_dg[init_f][suf] += 1

print(f"\n{'Next(digraph)':>14} {'Total':>6} {'%-r':>7} {'%-l':>7} {'%-n':>7} | {'Dominant'}")
print("-" * 65)
for init in sorted(next_init_suffix_dg.keys(), key=lambda x: -sum(next_init_suffix_dg[x].values())):
    counts = next_init_suffix_dg[init]
    total = sum(counts.values())
    if total < 8:
        continue
    r_p = counts['r'] / total * 100
    l_p = counts['l'] / total * 100
    n_p = counts['n'] / total * 100
    dom = max(('r', r_p), ('l', l_p), ('n', n_p), key=lambda x: x[1])
    print(f"{init:>14} {total:>6} {r_p:>6.1f}% {l_p:>6.1f}% {n_p:>6.1f}% | -{dom[0]} ({dom[1]:.0f}%)")

# ============================================================
# ANALYSIS 9: Does -y show selectivity or is it unmarked?
# ============================================================
print("\n" + "="*80)
print("ANALYSIS 9: -y SELECTIVITY TEST")
print("If -y is unmarked, it should NOT select for following initials")
print("="*80)

# Chi-square-like comparison: is -y distribution similar to baseline?
baseline = Counter()
for suf, init_s, init_f, w1, w2 in suffix_initial_pairs:
    baseline[init_s] += 1

total_baseline = sum(baseline.values())
print(f"\n{'Init':>6} {'Baseline%':>10} {'After-y%':>10} {'Diff':>8}")
print("-" * 40)
for init in sorted(baseline.keys()):
    if baseline[init] < 20:
        continue
    b_p = baseline[init] / total_baseline * 100
    y_p = y_followed_by.get(init, 0) / total_y_p * 100
    diff = y_p - b_p
    marker = " ***" if abs(diff) > 3 else ""
    print(f"{init:>6} {b_p:>9.1f}% {y_p:>9.1f}% {diff:>+7.1f}%{marker}")

# ============================================================
# ANALYSIS 10: Position of y in words
# ============================================================
print("\n" + "="*80)
print("ANALYSIS 10: EVA 'y' POSITIONAL ANALYSIS")
print("="*80)

y_positions = Counter()
y_word_initial = 0
y_word_final = 0
y_word_medial = 0
y_word_only = 0

for w in all_words:
    for i, c in enumerate(w):
        if c == 'y':
            if len(w) == 1:
                y_word_only += 1
            elif i == 0:
                y_word_initial += 1
            elif i == len(w) - 1:
                y_word_final += 1
            else:
                y_word_medial += 1

print(f"  y as sole character: {y_word_only}")
print(f"  y word-initial: {y_word_initial}")
print(f"  y word-medial: {y_word_medial}")
print(f"  y word-final: {y_word_final}")
print(f"  Total y occurrences: {y_word_only + y_word_initial + y_word_medial + y_word_final}")

print("\n\n=== ANALYSIS COMPLETE ===")
