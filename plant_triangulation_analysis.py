import re
from collections import Counter, defaultdict

# Read the transcription file
with open(r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Define target pages (recto + verso)
pages = {
    'f2': ('f2r', 'f2v'),   # Paeonia
    'f3': ('f3r', 'f3v'),   # Rubia
    'f9': ('f9r', 'f9v'),   # Nigella
    'f41': ('f41r', 'f41v'), # Adiantum
    'f47': ('f47r', 'f47v'), # Vitis
}

# Properties
hot_pages = ['f2', 'f3', 'f9']
cold_pages = ['f41', 'f47']
root_pages = ['f2', 'f3']  # Paeonia, Rubia - prominent roots
seed_pages = ['f9']  # Nigella - seed-based
leaf_pages = ['f41', 'f47']  # Adiantum fronds, Vitis leaves

def extract_words(lines, page_ids):
    """Extract all words from given page IDs."""
    words = []
    current_page = None
    for line in lines:
        # Check if line starts a page
        m = re.match(r'^<(f\d+[rv])>', line)
        if m:
            current_page = m.group(1)
            continue
        # Check if line belongs to a target page
        for pid in page_ids:
            if line.startswith(f'<{pid}.'):
                # Extract text after the tag
                text = re.sub(r'^<[^>]+>\s*', '', line.strip())
                # Remove annotations like @NNN;, {xxx}, etc.
                text = re.sub(r'@\d+;', '', text)
                text = re.sub(r'\{[^}]*\}', '', text)
                # Split on delimiters
                tokens = re.split(r'[<>\-\s.,;:]+', text)
                for t in tokens:
                    t = t.strip()
                    if t and len(t) > 0 and not t.startswith('#') and not t.startswith('!'):
                        words.append(t)
    return words

# Extract words for each page
page_words = {}
page_word_sets = {}
page_word_counts = {}

for page_name, page_ids in pages.items():
    words = extract_words(lines, page_ids)
    page_words[page_name] = words
    page_word_sets[page_name] = set(words)
    page_word_counts[page_name] = Counter(words)

# Print page statistics
print("=" * 80)
print("PAGE WORD STATISTICS")
print("=" * 80)
for pname in ['f2', 'f3', 'f9', 'f41', 'f47']:
    plant_names = {'f2': 'Paeonia', 'f3': 'Rubia', 'f9': 'Nigella', 'f41': 'Adiantum', 'f47': 'Vitis'}
    print(f"\n{pname} ({plant_names[pname]}): {len(page_words[pname])} total words, {len(page_word_sets[pname])} unique")
    print(f"  Top 20: {page_word_counts[pname].most_common(20)}")

# ANALYSIS 1: Words on ALL 5 pages (core herbal vocabulary)
print("\n" + "=" * 80)
print("CORE VOCABULARY (words on ALL 5 pages)")
print("=" * 80)
core = page_word_sets['f2'] & page_word_sets['f3'] & page_word_sets['f9'] & page_word_sets['f41'] & page_word_sets['f47']
for w in sorted(core):
    counts = {p: page_word_counts[p][w] for p in ['f2', 'f3', 'f9', 'f41', 'f47']}
    print(f"  {w:20s} counts: {counts}")

# ANALYSIS 2: Words on 4/5 pages
print("\n" + "=" * 80)
print("NEAR-CORE VOCABULARY (words on 4/5 pages)")
print("=" * 80)
all_words = set()
for s in page_word_sets.values():
    all_words |= s
for w in sorted(all_words):
    present_on = [p for p in ['f2', 'f3', 'f9', 'f41', 'f47'] if w in page_word_sets[p]]
    if len(present_on) == 4:
        missing = [p for p in ['f2', 'f3', 'f9', 'f41', 'f47'] if p not in present_on]
        counts = {p: page_word_counts[p].get(w, 0) for p in ['f2', 'f3', 'f9', 'f41', 'f47']}
        print(f"  {w:20s} missing: {missing[0]:5s} counts: {counts}")

# ANALYSIS 3: HOT-only words (on hot pages, NOT on cold pages)
print("\n" + "=" * 80)
print("HOT-ONLY VOCABULARY (on 2+ hot pages, NOT on any cold page)")
print("=" * 80)
hot_union = page_word_sets['f2'] | page_word_sets['f3'] | page_word_sets['f9']
cold_union = page_word_sets['f41'] | page_word_sets['f47']
hot_exclusive = hot_union - cold_union

# Filter: must be on at least 2 hot pages
for w in sorted(hot_exclusive):
    hot_count = sum(1 for p in hot_pages if w in page_word_sets[p])
    if hot_count >= 2:
        present = [p for p in hot_pages if w in page_word_sets[p]]
        counts = {p: page_word_counts[p].get(w, 0) for p in present}
        print(f"  {w:20s} on {hot_count} hot pages: {present} counts: {counts}")

# ANALYSIS 4: COLD-only words
print("\n" + "=" * 80)
print("COLD-ONLY VOCABULARY (on BOTH cold pages, NOT on any hot page)")
print("=" * 80)
cold_both = page_word_sets['f41'] & page_word_sets['f47']
cold_exclusive_both = cold_both - hot_union
for w in sorted(cold_exclusive_both):
    counts = {p: page_word_counts[p].get(w, 0) for p in cold_pages}
    print(f"  {w:20s} counts: {counts}")

# ANALYSIS 5: ROOT-prominent pages only (Paeonia+Rubia, not on leaf pages)
print("\n" + "=" * 80)
print("ROOT VOCABULARY (on BOTH root pages f2+f3, NOT on leaf pages f41+f47)")
print("=" * 80)
root_both = page_word_sets['f2'] & page_word_sets['f3']
leaf_union = page_word_sets['f41'] | page_word_sets['f47']
root_exclusive = root_both - leaf_union
for w in sorted(root_exclusive):
    counts = {'f2': page_word_counts['f2'][w], 'f3': page_word_counts['f3'][w]}
    also_f9 = w in page_word_sets['f9']
    print(f"  {w:20s} f2={counts['f2']}, f3={counts['f3']}, also on f9(Nigella): {also_f9}")

# ANALYSIS 6: SEED page only (Nigella hapax)
print("\n" + "=" * 80)
print("SEED/NIGELLA-SPECIFIC (only on f9, not on any other target page)")
print("=" * 80)
other_union = page_word_sets['f2'] | page_word_sets['f3'] | page_word_sets['f41'] | page_word_sets['f47']
nigella_only = page_word_sets['f9'] - other_union
for w in sorted(nigella_only):
    count = page_word_counts['f9'][w]
    if count >= 1:
        print(f"  {w:20s} count: {count}")

# ANALYSIS 7: Plant-specific hapax (on only 1 page)
print("\n" + "=" * 80)
print("PLANT-SPECIFIC HAPAX (words on ONLY ONE target page)")
print("=" * 80)
for pname in ['f2', 'f3', 'f9', 'f41', 'f47']:
    plant_names = {'f2': 'Paeonia', 'f3': 'Rubia', 'f9': 'Nigella', 'f41': 'Adiantum', 'f47': 'Vitis'}
    others = set()
    for p2 in ['f2', 'f3', 'f9', 'f41', 'f47']:
        if p2 != pname:
            others |= page_word_sets[p2]
    unique = page_word_sets[pname] - others
    print(f"\n  {pname} ({plant_names[pname]}) unique words ({len(unique)}):")
    for w in sorted(unique):
        c = page_word_counts[pname][w]
        print(f"    {w:25s} count: {c}")

# ANALYSIS 8: Degree marking analysis
print("\n" + "=" * 80)
print("DEGREE MARKING ANALYSIS")
print("=" * 80)
print("\nExpected Galenic degrees:")
print("  f2 (Paeonia): Hot 1st, Dry 2nd")
print("  f3 (Rubia): Hot 2nd, Dry 2nd")
print("  f9 (Nigella): Hot 3rd, Dry 1st")
print("  f41 (Adiantum): Cold, Dry")
print("  f47 (Vitis): Cold 1st, Moist 2nd")
print("\nWords shared by f2+f3 (Hot 1st+2nd) but NOT f9 (Hot 3rd):")
f2_f3_not_f9 = (page_word_sets['f2'] & page_word_sets['f3']) - page_word_sets['f9']
for w in sorted(f2_f3_not_f9):
    # Also check if on cold pages
    on_cold = any(w in page_word_sets[p] for p in cold_pages)
    flag = " [also on cold page]" if on_cold else ""
    print(f"  {w:20s} f2={page_word_counts['f2'][w]}, f3={page_word_counts['f3'][w]}{flag}")

print("\nWords on f9 (Hot 3rd) but NOT on f2 or f3:")
f9_not_f2f3 = page_word_sets['f9'] - page_word_sets['f2'] - page_word_sets['f3']
for w in sorted(f9_not_f2f3):
    on_cold = any(w in page_word_sets[p] for p in cold_pages)
    if not on_cold:
        print(f"  {w:20s} count: {page_word_counts['f9'][w]} [hot-exclusive]")
    else:
        print(f"  {w:20s} count: {page_word_counts['f9'][w]}")

# ANALYSIS 9: Dry pages vs Moist pages
print("\n" + "=" * 80)
print("DRY vs MOIST ANALYSIS")
print("=" * 80)
print("Dry pages: f2, f3, f9, f41 (all dry)")
print("Moist page: f47 only")
dry_all = page_word_sets['f2'] & page_word_sets['f3'] & page_word_sets['f9'] & page_word_sets['f41']
dry_not_moist = dry_all - page_word_sets['f47']
print(f"\nWords on ALL 4 dry pages but NOT on f47 (moist):")
for w in sorted(dry_not_moist):
    counts = {p: page_word_counts[p][w] for p in ['f2', 'f3', 'f9', 'f41']}
    print(f"  {w:20s} counts: {counts}")

moist_only = page_word_sets['f47'] - page_word_sets['f2'] - page_word_sets['f3'] - page_word_sets['f9'] - page_word_sets['f41']
print(f"\nWords ONLY on f47 (moist/Vitis): {len(moist_only)} words")
for w in sorted(moist_only):
    if page_word_counts['f47'][w] >= 1:
        print(f"  {w:20s} count: {page_word_counts['f47'][w]}")

# ANALYSIS 10: Stem/morpheme analysis
print("\n" + "=" * 80)
print("STEM/MORPHEME FREQUENCY ANALYSIS")
print("=" * 80)
# Look at common prefixes and suffixes
def get_prefix(word, n=3):
    return word[:n] if len(word) >= n else word

def get_suffix(word, n=3):
    return word[-n:] if len(word) >= n else word

for pname in ['f2', 'f3', 'f9', 'f41', 'f47']:
    plant_names = {'f2': 'Paeonia', 'f3': 'Rubia', 'f9': 'Nigella', 'f41': 'Adiantum', 'f47': 'Vitis'}
    prefixes = Counter(get_prefix(w) for w in page_words[pname])
    suffixes = Counter(get_suffix(w) for w in page_words[pname])
    print(f"\n{pname} ({plant_names[pname]}):")
    print(f"  Top prefixes: {prefixes.most_common(15)}")
    print(f"  Top suffixes: {suffixes.most_common(15)}")

# ANALYSIS 11: Words with specific distributions matching Galenic properties
print("\n" + "=" * 80)
print("GALENIC PROPERTY DISTRIBUTION MATCHING")
print("=" * 80)
print("\nLooking for words matching expected property distributions:")
print()

for w in sorted(all_words):
    present = tuple(p for p in ['f2', 'f3', 'f9', 'f41', 'f47'] if w in page_word_sets[p])

    # Exact match: Hot = f2, f3, f9 only
    if present == ('f2', 'f3', 'f9'):
        total = sum(page_word_counts[p][w] for p in present)
        if total >= 3:
            print(f"  EXACT HOT match: {w:20s} (total count: {total}) {dict((p, page_word_counts[p][w]) for p in present)}")

    # Exact match: Cold = f41, f47 only
    if present == ('f41', 'f47'):
        total = sum(page_word_counts[p][w] for p in present)
        if total >= 2:
            print(f"  EXACT COLD match: {w:20s} (total count: {total}) {dict((p, page_word_counts[p][w]) for p in present)}")

    # Dry = f2, f3, f9, f41 (not f47)
    if set(present) == {'f2', 'f3', 'f9', 'f41'}:
        total = sum(page_word_counts[p][w] for p in present)
        print(f"  EXACT DRY match: {w:20s} (total count: {total}) {dict((p, page_word_counts[p][w]) for p in present)}")

    # Root-prominent = f2, f3 only
    if present == ('f2', 'f3'):
        total = sum(page_word_counts[p][w] for p in present)
        if total >= 2:
            print(f"  ROOT (f2+f3 only): {w:20s} (total count: {total})")

# ANALYSIS 12: Distribution of -aiin/-ain/-am/-om endings
print("\n" + "=" * 80)
print("ENDING DISTRIBUTION ANALYSIS")
print("=" * 80)
endings_to_check = ['aiin', 'ain', 'am', 'om', 'ol', 'or', 'chy', 'dy', 'al', 'ar', 'an', 'ey', 'eey', 'ody', 'dam', 'dain', 'daiin', 'chol', 'chor', 'sho']
for ending in endings_to_check:
    counts_per_page = {}
    for pname in ['f2', 'f3', 'f9', 'f41', 'f47']:
        count = sum(1 for w in page_words[pname] if w.endswith(ending))
        total = len(page_words[pname])
        counts_per_page[pname] = (count, f"{count/total*100:.1f}%")
    print(f"  -{ending:8s}: {counts_per_page}")

print("\nDone.")
