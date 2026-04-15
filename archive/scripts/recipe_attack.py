#!/usr/bin/env python3
"""
Voynich Manuscript Recipe Section Attack
Extract starred recipe entries from f103r-f116v and analyze positional word patterns.
"""

import re
from collections import Counter, defaultdict
import json

ZL_FILE = r"C:\Users\kazuk\Downloads\voynich_analysis\ZL3b-n.txt"

# ============================================================
# STEP 1: Extract all recipe entries (starred paragraphs)
# ============================================================

def extract_recipes(filepath):
    """Extract recipe paragraphs from the recipe section (f103r onward, I=S pages)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find recipe section pages (marked with $I=S for "stars" or text-only/stars pages)
    # Actually, let's just grab f103r through f116v
    in_recipe_section = False
    recipes = []
    current_recipe = []
    current_star = ""
    current_folio = ""

    for i, line in enumerate(lines):
        line = line.strip()

        # Track folio changes
        folio_match = re.match(r'^<(f\d+[rv]\d?)>', line)
        if folio_match:
            current_folio = folio_match.group(1)
            # Recipe section: f103r through f116v
            fnum = re.match(r'f(\d+)', current_folio)
            if fnum:
                num = int(fnum.group(1))
                if 103 <= num <= 116:
                    in_recipe_section = True
                else:
                    in_recipe_section = False
            continue

        if not in_recipe_section:
            continue

        # Track star markers
        if '# Dark star' in line or '# Light star' in line or '# star' in line.lower():
            current_star = line.strip('# ').strip()
            continue

        # Skip comments
        if line.startswith('#'):
            continue

        # Extract text content
        text_match = re.match(r'^<[^>]+>\s+(.*)', line)
        if not text_match:
            continue

        text = text_match.group(1)

        # Check if this line starts a new recipe (has <%>)
        if '<%>' in text:
            # Save previous recipe if any
            if current_recipe:
                recipes.append({
                    'folio': current_recipe[0]['folio'],
                    'star': current_recipe[0].get('star', ''),
                    'lines': current_recipe,
                    'full_text': ' '.join(l['text'] for l in current_recipe)
                })
            current_recipe = []

        # Clean text
        clean = text.replace('<%>', '').replace('<$>', '').strip()
        # Remove editorial marks but keep the preferred readings
        clean = re.sub(r'\[([^:\]]+):[^\]]+\]', r'\1', clean)  # [a:b] -> a
        clean = re.sub(r'\{[^}]+\}', '', clean)  # remove {notes}
        clean = re.sub(r'<[^>]*>', '', clean)  # remove remaining tags
        clean = re.sub(r'<!@\d+;>', '', clean)  # remove @refs
        clean = re.sub(r'\?\?+', '?', clean)  # collapse multiple ?
        clean = clean.replace(',', '.').replace(' ', ' ')

        if clean.strip():
            current_recipe.append({
                'folio': current_folio,
                'star': current_star,
                'text': clean.strip(),
                'has_end': '<$>' in text
            })

        # If line ends recipe
        if '<$>' in text and current_recipe:
            recipes.append({
                'folio': current_recipe[0]['folio'],
                'star': current_recipe[0].get('star', ''),
                'lines': current_recipe,
                'full_text': ' '.join(l['text'] for l in current_recipe)
            })
            current_recipe = []

    # Don't forget last recipe
    if current_recipe:
        recipes.append({
            'folio': current_recipe[0]['folio'],
            'star': current_recipe[0].get('star', ''),
            'lines': current_recipe,
            'full_text': ' '.join(l['text'] for l in current_recipe)
        })

    return recipes


# ============================================================
# STEP 2: Tokenize and analyze word positions
# ============================================================

def tokenize(text):
    """Split recipe text into words, cleaning separators."""
    # Split on dots and spaces
    text = text.replace('.', ' ').replace('-', ' ')
    words = text.split()
    # Remove empty, single-char noise, and uncertain readings
    words = [w.strip() for w in words if w.strip() and len(w.strip()) > 0]
    return words


def analyze_positions(recipes):
    """Analyze which words appear in which positions."""
    position_words = defaultdict(Counter)  # position -> word -> count
    word_positions = defaultdict(Counter)  # word -> position -> count
    first_words = Counter()
    last_words = Counter()
    second_words = Counter()
    third_words = Counter()
    all_words = Counter()

    for recipe in recipes:
        words = tokenize(recipe['full_text'])
        if not words:
            continue

        for i, w in enumerate(words):
            position_words[i][w] += 1
            word_positions[w][i] += 1
            all_words[w] += 1

        first_words[words[0]] += 1
        if len(words) > 1:
            second_words[words[1]] += 1
        if len(words) > 2:
            third_words[words[2]] += 1
        last_words[words[-1]] += 1
        if len(words) > 1:
            # Also second-to-last
            pass

    return {
        'position_words': position_words,
        'word_positions': word_positions,
        'first_words': first_words,
        'second_words': second_words,
        'third_words': third_words,
        'last_words': last_words,
        'all_words': all_words,
    }


# ============================================================
# STEP 3: Find structural patterns
# ============================================================

def find_connector_patterns(recipes):
    """Find words that appear between pairs of other words (connectors like 'of', 'and')."""
    bigrams = Counter()
    trigrams = Counter()
    connector_candidates = defaultdict(Counter)  # word -> (left_word, right_word)

    for recipe in recipes:
        words = tokenize(recipe['full_text'])
        for i in range(len(words) - 1):
            bigrams[(words[i], words[i+1])] += 1
        for i in range(len(words) - 2):
            trigrams[(words[i], words[i+1], words[i+2])] += 1
            connector_candidates[words[i+1]][(words[i], words[i+2])] += 1

    return bigrams, trigrams, connector_candidates


def find_final_position_words(recipes, all_words):
    """Find words that preferentially appear at the end of recipes."""
    final_3_words = Counter()
    non_final_words = Counter()

    for recipe in recipes:
        words = tokenize(recipe['full_text'])
        if len(words) < 4:
            continue
        for w in words[-3:]:
            final_3_words[w] += 1
        for w in words[:-3]:
            non_final_words[w] += 1

    # Find words with high final-preference ratio
    final_preference = {}
    for w in final_3_words:
        total = all_words[w]
        if total >= 3:
            ratio = final_3_words[w] / total
            final_preference[w] = (ratio, final_3_words[w], total)

    return final_preference


def analyze_lk_words(recipes):
    """Analyze the l+k prefix words unique to recipes."""
    lk_contexts = []
    for recipe in recipes:
        words = tokenize(recipe['full_text'])
        for i, w in enumerate(words):
            if re.match(r'lk', w):
                context = {
                    'word': w,
                    'position': i,
                    'total_words': len(words),
                    'relative_position': i / max(len(words), 1),
                    'prev': words[i-1] if i > 0 else None,
                    'next': words[i+1] if i < len(words)-1 else None,
                    'folio': recipe['folio']
                }
                lk_contexts.append(context)
    return lk_contexts


# ============================================================
# STEP 4: Compare with herbal sections
# ============================================================

def extract_section_vocab(filepath, section_type):
    """Extract vocabulary from different sections for comparison."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    herbal_words = Counter()
    recipe_words = Counter()
    current_section = None

    for line in lines:
        line = line.strip()
        if '$I=H' in line:
            current_section = 'herbal'
        elif '$I=S' in line or '$I=T' in line:
            # Check if in recipe range
            folio_match = re.search(r'f(\d+)', line)
            if folio_match and 103 <= int(folio_match.group(1)) <= 116:
                current_section = 'recipe'
            else:
                current_section = 'other'
        elif '$I=P' in line:
            current_section = 'pharma'
        elif line.startswith('<f'):
            pass
        elif line.startswith('#'):
            continue
        else:
            text_match = re.match(r'^<[^>]+>\s+(.*)', line)
            if text_match and current_section:
                text = text_match.group(1)
                text = re.sub(r'<[^>]*>', '', text)
                text = re.sub(r'\[[^\]]*\]', '', text)
                text = re.sub(r'\{[^}]*\}', '', text)
                words = text.replace('.', ' ').replace(',', ' ').replace('-', ' ').split()
                words = [w.strip() for w in words if w.strip() and not w.startswith('%') and not w.startswith('$')]
                if current_section == 'herbal':
                    for w in words:
                        herbal_words[w] += 1
                elif current_section == 'recipe':
                    for w in words:
                        recipe_words[w] += 1

    return herbal_words, recipe_words


# ============================================================
# MAIN ANALYSIS
# ============================================================

def main():
    print("=" * 80)
    print("VOYNICH RECIPE SECTION STRUCTURAL ATTACK")
    print("=" * 80)

    recipes = extract_recipes(ZL_FILE)
    print(f"\nExtracted {len(recipes)} recipe entries from the starred section")

    # Show first few recipes for verification
    print("\n--- FIRST 5 RECIPES ---")
    for i, r in enumerate(recipes[:5]):
        words = tokenize(r['full_text'])
        print(f"\n  Recipe {i+1} [{r['folio']}] ({r['star']}):")
        print(f"    Words ({len(words)}): {' | '.join(words[:10])}{'...' if len(words) > 10 else ''}")

    # Positional analysis
    print("\n" + "=" * 80)
    print("POSITIONAL ANALYSIS")
    print("=" * 80)

    analysis = analyze_positions(recipes)

    print("\n--- POSITION 1 (most likely 'TAKE' / 'Recipe') ---")
    for word, count in analysis['first_words'].most_common(20):
        pct = count / len(recipes) * 100
        print(f"  {word:20s}  {count:3d} ({pct:.1f}%)")

    print("\n--- POSITION 2 ---")
    for word, count in analysis['second_words'].most_common(15):
        pct = count / len(recipes) * 100
        print(f"  {word:20s}  {count:3d} ({pct:.1f}%)")

    print("\n--- POSITION 3 ---")
    for word, count in analysis['third_words'].most_common(15):
        pct = count / len(recipes) * 100
        print(f"  {word:20s}  {count:3d} ({pct:.1f}%)")

    print("\n--- LAST WORD (preparation verb?) ---")
    for word, count in analysis['last_words'].most_common(20):
        pct = count / len(recipes) * 100
        print(f"  {word:20s}  {count:3d} ({pct:.1f}%)")

    # Overall vocabulary
    print("\n--- TOP 30 RECIPE WORDS ---")
    total_words = sum(analysis['all_words'].values())
    for word, count in analysis['all_words'].most_common(30):
        pct = count / total_words * 100
        print(f"  {word:20s}  {count:4d} ({pct:.2f}%)")

    print(f"\n  Total words: {total_words}")
    print(f"  Unique words: {len(analysis['all_words'])}")

    # Connector analysis
    print("\n" + "=" * 80)
    print("CONNECTOR / FUNCTION WORD ANALYSIS")
    print("=" * 80)

    bigrams, trigrams, connectors = find_connector_patterns(recipes)

    print("\n--- TOP BIGRAMS ---")
    for (w1, w2), count in bigrams.most_common(20):
        print(f"  {w1:15s} {w2:15s}  {count:3d}")

    # Analyze specific connector candidates: ar, ol, al
    print("\n--- 'ar' AS CONNECTOR (X ar Y patterns) ---")
    ar_patterns = []
    for recipe in recipes:
        words = tokenize(recipe['full_text'])
        for i, w in enumerate(words):
            if w == 'ar' and i > 0 and i < len(words) - 1:
                ar_patterns.append((words[i-1], 'ar', words[i+1]))
    for pattern in ar_patterns[:15]:
        print(f"  {pattern[0]:15s} ar {pattern[2]:15s}")
    print(f"  Total 'X ar Y' patterns: {len(ar_patterns)}")

    print("\n--- 'ol' AS CONNECTOR (X ol Y patterns) ---")
    ol_patterns = []
    for recipe in recipes:
        words = tokenize(recipe['full_text'])
        for i, w in enumerate(words):
            if w == 'ol' and i > 0 and i < len(words) - 1:
                ol_patterns.append((words[i-1], 'ol', words[i+1]))
    for pattern in ol_patterns[:15]:
        print(f"  {pattern[0]:15s} ol {pattern[2]:15s}")
    print(f"  Total 'X ol Y' patterns: {len(ol_patterns)}")

    print("\n--- 'al' AS CONNECTOR (X al Y patterns) ---")
    al_patterns = []
    for recipe in recipes:
        words = tokenize(recipe['full_text'])
        for i, w in enumerate(words):
            if w == 'al' and i > 0 and i < len(words) - 1:
                al_patterns.append((words[i-1], 'al', words[i+1]))
    for pattern in al_patterns[:15]:
        print(f"  {pattern[0]:15s} al {pattern[2]:15s}")
    print(f"  Total 'X al Y' patterns: {len(al_patterns)}")

    # Final position analysis
    print("\n" + "=" * 80)
    print("FINAL-POSITION PREFERENCE (possible preparation verbs)")
    print("=" * 80)

    final_pref = find_final_position_words(recipes, analysis['all_words'])
    sorted_final = sorted(final_pref.items(), key=lambda x: (-x[1][0], -x[1][1]))
    print(f"\n  Words appearing predominantly in last 3 positions (ratio, final_count, total):")
    for word, (ratio, final_ct, total) in sorted_final[:25]:
        bar = '#' * int(ratio * 20)
        print(f"  {word:20s}  ratio={ratio:.2f}  final={final_ct:3d}  total={total:3d}  {bar}")

    # l+k word analysis
    print("\n" + "=" * 80)
    print("L+K PREFIX WORD ANALYSIS")
    print("=" * 80)

    lk_contexts = analyze_lk_words(recipes)

    # Count l+k word types
    lk_words = Counter(ctx['word'] for ctx in lk_contexts)
    print(f"\n  Total l+k occurrences: {len(lk_contexts)}")
    print(f"\n  l+k word types:")
    for word, count in lk_words.most_common():
        print(f"    {word:20s}  {count:3d}")

    # Position distribution
    print(f"\n  Relative position distribution (0=start, 1=end):")
    position_bins = Counter()
    for ctx in lk_contexts:
        bin_val = round(ctx['relative_position'], 1)
        position_bins[bin_val] += 1
    for pos in sorted(position_bins.keys()):
        bar = '#' * position_bins[pos]
        print(f"    {pos:.1f}: {position_bins[pos]:3d} {bar}")

    # Context words
    print(f"\n  Words BEFORE l+k words:")
    prev_words = Counter(ctx['prev'] for ctx in lk_contexts if ctx['prev'])
    for w, c in prev_words.most_common(10):
        print(f"    {w:20s}  {c:3d}")

    print(f"\n  Words AFTER l+k words:")
    next_words = Counter(ctx['next'] for ctx in lk_contexts if ctx['next'])
    for w, c in next_words.most_common(10):
        print(f"    {w:20s}  {c:3d}")

    # Section comparison
    print("\n" + "=" * 80)
    print("RECIPE vs HERBAL VOCABULARY COMPARISON")
    print("=" * 80)

    herbal_words, recipe_section_words = extract_section_vocab(ZL_FILE, 'comparison')

    # Words unique to recipes (not in herbal)
    recipe_only = set(recipe_section_words.keys()) - set(herbal_words.keys())
    recipe_only_freq = {w: recipe_section_words[w] for w in recipe_only if recipe_section_words[w] >= 3}
    sorted_recipe_only = sorted(recipe_only_freq.items(), key=lambda x: -x[1])

    print(f"\n  Words found ONLY in recipes (freq >= 3):")
    for word, count in sorted_recipe_only[:30]:
        print(f"    {word:20s}  {count:3d}")

    # Words with dramatically different frequency
    print(f"\n  Words with DRAMATIC frequency shift (recipe vs herbal):")
    for word in analysis['all_words']:
        r_count = recipe_section_words.get(word, 0)
        h_count = herbal_words.get(word, 0)
        r_total = sum(recipe_section_words.values()) or 1
        h_total = sum(herbal_words.values()) or 1
        r_pct = r_count / r_total * 100
        h_pct = h_count / h_total * 100
        if r_pct > 0.5 and h_pct > 0.1 and (r_pct / max(h_pct, 0.01) > 3 or h_pct / max(r_pct, 0.01) > 3):
            direction = "RECIPE>>HERBAL" if r_pct > h_pct else "HERBAL>>RECIPE"
            print(f"    {word:20s}  recipe={r_pct:.2f}%  herbal={h_pct:.2f}%  {direction}")

    # Recipe structure template extraction
    print("\n" + "=" * 80)
    print("RECIPE STRUCTURE TEMPLATES")
    print("=" * 80)

    print("\n  Abstracting recipes into templates...")
    print("  (FIRST = position 1 word, then structural skeleton)")

    # Group recipes by first word
    by_first = defaultdict(list)
    for r in recipes:
        words = tokenize(r['full_text'])
        if words:
            by_first[words[0]].append(r)

    print(f"\n  Recipes grouped by first word:")
    for first_word, recipe_list in sorted(by_first.items(), key=lambda x: -len(x[1])):
        if len(recipe_list) >= 2:
            print(f"\n    '{first_word}' ({len(recipe_list)} recipes):")
            for r in recipe_list[:3]:
                words = tokenize(r['full_text'])
                print(f"      [{r['folio']}] {' '.join(words[:8])}...")

    # Analyze recipe lengths
    print("\n" + "=" * 80)
    print("RECIPE LENGTH DISTRIBUTION")
    print("=" * 80)

    lengths = [len(tokenize(r['full_text'])) for r in recipes]
    length_counter = Counter(lengths)
    for length in sorted(length_counter.keys()):
        bar = '#' * length_counter[length]
        print(f"  {length:3d} words: {length_counter[length]:3d} recipes {bar}")

    avg_len = sum(lengths) / max(len(lengths), 1)
    print(f"\n  Average recipe length: {avg_len:.1f} words")
    print(f"  Min: {min(lengths)}, Max: {max(lengths)}")

    # Carrara Herbal comparison structure
    print("\n" + "=" * 80)
    print("CARRARA HERBAL (BL Egerton 2020) STRUCTURAL COMPARISON")
    print("=" * 80)
    print("""
  The Carrara Herbal (Paduan dialect, late 14th century) uses this recipe format:

  TYPICAL STRUCTURE:
    Recipe/Prendi [quantity] [de/di] [ingredient], [quantity] [de/di] [ingredient],
    [e] [verb: mescola/tria/fa/metti] [e] [verb] [e] [instruction]

  KEY PADUAN/VENETIAN RECIPE VOCABULARY:
    Recipe/Prendi    = "Take" (opening imperative)
    de/di            = "of" (connector)
    e/et             = "and" (connector)
    onze/once        = "ounces" (measure)
    drame            = "drams" (measure)
    libra/libre      = "pounds" (measure)
    tria/trida       = "grind" (imperative)
    mescola/meseda   = "mix" (imperative)
    bolle/boi        = "boil" (imperative)
    metti/meta       = "put" (imperative)
    fa               = "make" (imperative)
    con              = "with" (connector)

  MAPPING HYPOTHESIS (Voynich -> Paduan):
    If first-position word = "Recipe/Prendi" then most common first word = ?
    If 'ar' = "and/e" then it connects ingredients
    If 'ol' = "of/de" then it marks quantities
    If 'al' = "with/con" then it marks accompaniments
    If l+k words = verbal prefix for preparation instructions
    """)

    # Build the hypothesis mapping
    print("\n" + "=" * 80)
    print("HYPOTHESIS: STRUCTURAL MAPPING")
    print("=" * 80)

    # What's the most common first word?
    top_first = analysis['first_words'].most_common(1)[0]
    print(f"\n  Most common FIRST word: '{top_first[0]}' ({top_first[1]} times, {top_first[1]/len(recipes)*100:.1f}%)")
    print(f"  -> HYPOTHESIS: '{top_first[0]}' = 'Recipe' or 'Prendi' (Take)")

    # Check if there's a clear second-most
    if len(analysis['first_words']) > 1:
        second_first = analysis['first_words'].most_common(5)
        print(f"\n  Top 5 first words (possible recipe openings):")
        for w, c in second_first:
            print(f"    '{w}' = {c} times ({c/len(recipes)*100:.1f}%)")

    # qo- prefix words
    print("\n\n--- QO- PREFIX ANALYSIS ---")
    qo_words = Counter()
    for recipe in recipes:
        words = tokenize(recipe['full_text'])
        for w in words:
            if w.startswith('qo'):
                qo_words[w] += 1
    print(f"  qo- prefix words in recipes:")
    for w, c in qo_words.most_common(20):
        # Check if corresponding word without qo- exists
        without_qo = w[2:]
        without_count = analysis['all_words'].get(without_qo, 0)
        print(f"    {w:20s}  {c:3d}    (without qo-: '{without_qo}' = {without_count})")

    # Word-pair analysis (X.Y where both appear together repeatedly)
    print("\n" + "=" * 80)
    print("REPEATED WORD PAIRS (possible fixed phrases)")
    print("=" * 80)

    for (w1, w2), count in bigrams.most_common(30):
        print(f"  {w1:15s} {w2:15s}  {count:3d}")

    # Short recipes (most formulaic, easiest to crack)
    print("\n" + "=" * 80)
    print("SHORTEST RECIPES (most formulaic)")
    print("=" * 80)

    sorted_by_length = sorted(recipes, key=lambda r: len(tokenize(r['full_text'])))
    for r in sorted_by_length[:15]:
        words = tokenize(r['full_text'])
        print(f"\n  [{r['folio']}] ({len(words)} words):")
        print(f"    {' '.join(words)}")

    # RECURRENCE: Find recurring word sequences
    print("\n" + "=" * 80)
    print("RECURRING SEQUENCES (length 3+)")
    print("=" * 80)

    all_sequences = Counter()
    for recipe in recipes:
        words = tokenize(recipe['full_text'])
        for length in range(3, 6):
            for i in range(len(words) - length + 1):
                seq = tuple(words[i:i+length])
                all_sequences[seq] += 1

    recurring = {seq: count for seq, count in all_sequences.items() if count >= 3}
    # Filter out subsequences
    sorted_recurring = sorted(recurring.items(), key=lambda x: (-len(x[0]), -x[1]))
    print(f"\n  Sequences appearing 3+ times:")
    shown = set()
    for seq, count in sorted_recurring[:30]:
        seq_str = ' '.join(seq)
        # Skip if this is a subsequence of something already shown
        is_sub = False
        for s in shown:
            if seq_str in s:
                is_sub = True
                break
        if not is_sub:
            print(f"    {seq_str:50s}  {count:3d}")
            shown.add(seq_str)


if __name__ == '__main__':
    main()
