import re
from collections import defaultdict, Counter
import random

def parse_eva(filepath):
    """Parse EVA transcription, return dict: page -> list of words"""
    page_words = defaultdict(list)
    current_page = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            m = re.match(r'^<(f\d+[rv]\d*)>', line)
            if m:
                current_page = m.group(1)
                continue
            m2 = re.match(r'^<(f\d+[rv]\d*)\.\d+', line)
            if m2:
                current_page = m2.group(1)

            if current_page is None:
                continue

            text = re.sub(r'<[^>]*>', '', line)
            text = re.sub(r'@\d+;?', '', text)
            text = re.sub(r'\{([^}]*)\}', r'\1', text)
            words = re.split(r'[.\s,<>\-]+', text)
            for w in words:
                w = re.sub(r"[^a-z']", '', w.lower())
                if w and len(w) >= 2:
                    page_words[current_page].append(w)

    return page_words

def build_vocab(page_words):
    word_freq = Counter()
    word_pages = defaultdict(set)
    for page, words in page_words.items():
        for w in words:
            word_freq[w] += 1
            word_pages[w].add(page)
    return word_freq, word_pages

def find_mirror_pairs(word_freq, min_freq=5):
    vocab = {w for w, f in word_freq.items() if f >= min_freq}
    pairs = []
    seen = set()
    for w in vocab:
        rev = w[::-1]
        if rev in vocab and rev != w and (rev, w) not in seen:
            pairs.append((w, rev, word_freq[w], word_freq[rev]))
            seen.add((w, rev))
    return sorted(pairs, key=lambda x: -(x[2] + x[3]))

def find_anagram_pairs(word_freq, min_freq=5):
    vocab = {w: f for w, f in word_freq.items() if f >= min_freq}
    anagram_groups = defaultdict(list)
    for w in vocab:
        key = ''.join(sorted(w))
        anagram_groups[key].append(w)
    pairs = []
    for key, group in anagram_groups.items():
        if len(group) >= 2:
            for i in range(len(group)):
                for j in range(i+1, len(group)):
                    w1, w2 = group[i], group[j]
                    pairs.append((w1, w2, word_freq[w1], word_freq[w2]))
    return sorted(pairs, key=lambda x: -(x[2] + x[3]))

def calculate_overlap(w1, w2, word_pages):
    pages1 = word_pages[w1]
    pages2 = word_pages[w2]
    overlap = pages1 & pages2
    union = pages1 | pages2
    jaccard = len(overlap) / len(union) if union else 0
    return len(overlap), len(pages1), len(pages2), len(union), jaccard, overlap, pages1, pages2

def partial_reversal_pairs(word_freq, word_pages, min_freq=5, prefix_len=3):
    vocab = {w: f for w, f in word_freq.items() if f >= min_freq and len(w) >= prefix_len}
    pairs = []
    seen = set()
    for w in vocab:
        reversed_prefix = w[:prefix_len][::-1] + w[prefix_len:]
        if reversed_prefix in vocab and reversed_prefix != w and (reversed_prefix, w) not in seen:
            pairs.append((w, reversed_prefix, word_freq[w], word_freq[reversed_prefix]))
            seen.add((w, reversed_prefix))
    return sorted(pairs, key=lambda x: -(x[2] + x[3]))

# Main
filepath = 'RF1b-e.txt'
page_words = parse_eva(filepath)
word_freq, word_pages = build_vocab(page_words)

all_page_list = list(page_words.keys())
total_pages = len(all_page_list)

print(f"Total unique words: {len(word_freq)}")
print(f"Words with freq >= 5: {sum(1 for f in word_freq.values() if f >= 5)}")
print(f"Words with freq >= 3: {sum(1 for f in word_freq.values() if f >= 3)}")
print(f"Total pages: {total_pages}")
print()

# Monte Carlo test
random.seed(42)
def monte_carlo_test(n1, n2, observed, n_trials=10000):
    count = 0
    for _ in range(n_trials):
        s1 = set(random.sample(all_page_list, min(n1, total_pages)))
        s2 = set(random.sample(all_page_list, min(n2, total_pages)))
        if len(s1 & s2) <= observed:
            count += 1
    return count / n_trials

# === 1. MIRROR PAIRS ===
print("=" * 80)
print("1. EXACT MIRROR PAIRS (freq >= 5)")
print("=" * 80)
mirror5 = find_mirror_pairs(word_freq, 5)
print(f"Found {len(mirror5)} mirror pairs\n")
for w1, w2, f1, f2 in mirror5:
    ov, p1, p2, un, jac, ovp, pg1, pg2 = calculate_overlap(w1, w2, word_pages)
    tag = "COMPLEMENTARY!" if jac == 0 else f"overlap={ov}/{un}"
    print(f"  {w1} ({f1}x, {p1}pp) <-> {w2} ({f2}x, {p2}pp) | {tag} | J={jac:.3f}")
    if jac < 0.2:
        print(f"    {w1}: {sorted(pg1)}")
        print(f"    {w2}: {sorted(pg2)}")
    print()

# === 2. ANAGRAM PAIRS ===
print("=" * 80)
print("2. ANAGRAM PAIRS (freq >= 5)")
print("=" * 80)
anagram5 = find_anagram_pairs(word_freq, 5)
print(f"Found {len(anagram5)} anagram pairs\n")
for w1, w2, f1, f2 in anagram5:
    ov, p1, p2, un, jac, ovp, pg1, pg2 = calculate_overlap(w1, w2, word_pages)
    is_mir = w1[::-1] == w2
    tag = " [MIRROR]" if is_mir else ""
    comp = "COMPLEMENTARY!" if jac == 0 else f"overlap={ov}"
    print(f"  {w1} <-> {w2}{tag} ({f1}x/{f2}x) | pp:{p1}/{p2} | {comp} | J={jac:.3f}")
    if jac < 0.2:
        print(f"    {w1}: {sorted(pg1)}")
        print(f"    {w2}: {sorted(pg2)}")
    print()

# === 3. PARTIAL REVERSAL ===
print("=" * 80)
print("3. PARTIAL REVERSAL PAIRS (first 2 chars, freq >= 5, J < 0.15)")
print("=" * 80)
partial2 = partial_reversal_pairs(word_freq, word_pages, 5, 2)
print(f"Found {len(partial2)} total; showing low-overlap:\n")
for w1, w2, f1, f2 in partial2:
    ov, p1, p2, un, jac, ovp, pg1, pg2 = calculate_overlap(w1, w2, word_pages)
    if jac < 0.15:
        print(f"  {w1} <-> {w2} ({f1}x/{f2}x) | pp:{p1}/{p2} | J={jac:.3f}")
        print(f"    {w1}: {sorted(pg1)}")
        print(f"    {w2}: {sorted(pg2)}")
        print()

print("=" * 80)
print("3b. PARTIAL REVERSAL PAIRS (first 3 chars, freq >= 5, J < 0.15)")
print("=" * 80)
partial3 = partial_reversal_pairs(word_freq, word_pages, 5, 3)
print(f"Found {len(partial3)} total; showing low-overlap:\n")
for w1, w2, f1, f2 in partial3:
    ov, p1, p2, un, jac, ovp, pg1, pg2 = calculate_overlap(w1, w2, word_pages)
    if jac < 0.15:
        print(f"  {w1} <-> {w2} ({f1}x/{f2}x) | pp:{p1}/{p2} | J={jac:.3f}")
        print(f"    {w1}: {sorted(pg1)}")
        print(f"    {w2}: {sorted(pg2)}")
        print()

# === 4. ckhy/kchy VERIFICATION ===
print("=" * 80)
print("4. VERIFICATION: ckhy / kchy")
print("=" * 80)
for w in ['ckhy', 'kchy']:
    print(f"  {w}: freq={word_freq.get(w,0)}, pages={sorted(word_pages.get(w,set()))}")
if 'ckhy' in word_pages and 'kchy' in word_pages:
    ov, p1, p2, un, jac, ovp, pg1, pg2 = calculate_overlap('ckhy', 'kchy', word_pages)
    pval = monte_carlo_test(p1, p2, ov)
    print(f"  Overlap: {ov}, Jaccard: {jac:.3f}, p-value: {pval:.4f}")
print()

# === 5. STATISTICAL TESTS ===
print("=" * 80)
print("5. STATISTICAL SIGNIFICANCE (all low-overlap pairs, >= 3 pages each)")
print("=" * 80)

tested = set()
results = []

# Gather all pairs from mirrors and anagrams at freq >= 3
for w1, w2, f1, f2 in find_mirror_pairs(word_freq, 3) + find_anagram_pairs(word_freq, 3):
    key = tuple(sorted([w1, w2]))
    if key in tested:
        continue
    tested.add(key)
    ov, p1, p2, un, jac, ovp, pg1, pg2 = calculate_overlap(w1, w2, word_pages)
    if jac < 0.15 and p1 >= 3 and p2 >= 3:
        is_mir = w1[::-1] == w2
        pval = monte_carlo_test(p1, p2, ov)
        results.append((w1, w2, f1, f2, ov, p1, p2, jac, pval, is_mir, pg1, pg2))

results.sort(key=lambda x: x[8])
for w1, w2, f1, f2, ov, p1, p2, jac, pval, is_mir, pg1, pg2 in results:
    typ = "MIRROR" if is_mir else "ANAGRAM"
    sig = " *** SIGNIFICANT ***" if pval < 0.05 else ""
    print(f"  [{typ}] {w1} ({f1}x,{p1}pp) <-> {w2} ({f2}x,{p2}pp) | ov={ov} J={jac:.3f} p={pval:.4f}{sig}")
    if pval < 0.1:
        print(f"    {w1}: {sorted(pg1)}")
        print(f"    {w2}: {sorted(pg2)}")
    print()

# === 6. DRY/MOIST SEARCH ===
print("=" * 80)
print("6. DRY/MOIST CANDIDATES")
print("=" * 80)
dry_pages_set = {'f2r', 'f3r', 'f9r', 'f41r'}
moist_pages_set = {'f47r'}

print(f"Dry pages: {sorted(dry_pages_set)}")
print(f"Moist pages: {sorted(moist_pages_set)}")
print()

# Check all anagram/mirror pairs for dry/moist split
print("--- Anagram/mirror pairs with dry/moist separation ---")
all_pairs = find_mirror_pairs(word_freq, 3) + find_anagram_pairs(word_freq, 3)
for w1, w2, f1, f2 in all_pairs:
    p1 = word_pages[w1]
    p2 = word_pages[w2]
    d1 = len(p1 & dry_pages_set)
    m1 = len(p1 & moist_pages_set)
    d2 = len(p2 & dry_pages_set)
    m2 = len(p2 & moist_pages_set)
    if (d1 >= 1 and m2 >= 1 and m1 == 0) or (d2 >= 1 and m1 >= 1 and m2 == 0):
        is_mir = w1[::-1] == w2
        typ = "MIRROR" if is_mir else "ANAGRAM"
        print(f"  [{typ}] {w1} (dry:{d1},moist:{m1}) <-> {w2} (dry:{d2},moist:{m2})")
        print(f"    {w1}: {sorted(p1)}")
        print(f"    {w2}: {sorted(p2)}")
        print()

# Words concentrated on dry pages
print("\n--- Top words on dry pages (>=2 dry, 0 moist, freq>=3) ---")
dry_cands = []
for w, pages in word_pages.items():
    if word_freq[w] >= 3:
        d = len(pages & dry_pages_set)
        m = len(pages & moist_pages_set)
        if d >= 2 and m == 0:
            rev = w[::-1]
            rev_info = f" MIRROR={rev}({word_freq[rev]}x)" if rev in word_freq and word_freq[rev] >= 2 else ""
            dry_cands.append((w, word_freq[w], d, sorted(pages), rev_info))

dry_cands.sort(key=lambda x: -x[1])
for w, freq, d, pages, rev_info in dry_cands[:20]:
    print(f"  {w}: freq={freq}, dry={d}, pages={pages}{rev_info}")

print("\n--- Top words on moist pages (on f47r, 0 dry, freq>=3) ---")
moist_cands = []
for w, pages in word_pages.items():
    if word_freq[w] >= 3:
        d = len(pages & dry_pages_set)
        m = len(pages & moist_pages_set)
        if m >= 1 and d == 0:
            rev = w[::-1]
            rev_info = f" MIRROR={rev}({word_freq[rev]}x)" if rev in word_freq and word_freq[rev] >= 2 else ""
            moist_cands.append((w, word_freq[w], sorted(pages), rev_info))

moist_cands.sort(key=lambda x: -x[1])
for w, freq, pages, rev_info in moist_cands[:20]:
    print(f"  {w}: freq={freq}, pages={pages}{rev_info}")

# === 7. EXPANDED: freq >= 3 mirror pairs ===
print("\n" + "=" * 80)
print("7. ALL MIRROR PAIRS freq >= 3")
print("=" * 80)
mirror3 = find_mirror_pairs(word_freq, 3)
print(f"Found {len(mirror3)} mirror pairs\n")
for w1, w2, f1, f2 in mirror3:
    ov, p1, p2, un, jac, ovp, pg1, pg2 = calculate_overlap(w1, w2, word_pages)
    print(f"  {w1} ({f1}x,{p1}pp) <-> {w2} ({f2}x,{p2}pp) | ov={ov} J={jac:.3f}")
    if jac < 0.2:
        print(f"    {w1}: {sorted(pg1)}")
        print(f"    {w2}: {sorted(pg2)}")
    print()
