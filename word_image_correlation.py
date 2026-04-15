#!/usr/bin/env python3
"""
Voynich Manuscript: Word-Image Correlation Analysis
Tests whether specific EVA words systematically correlate with visual features of illustrations.
"""

import re
import random
import math
from collections import Counter, defaultdict

# ============================================================
# 1. VISUAL CLASSIFICATION OF HERBAL PAGES
# ============================================================
# Mapping: pdf_page -> folio
# page 3 = f1r, page 4 = f1v, page 5 = f2r, ...
# Each page side (recto/verso) is one PDF page.
#
# Visual features scored from examining each page image:
# root:   0=no root visible, 1=small/thin root, 2=prominent/large root system
# flower: 0=no flowers, 1=small/few flowers, 2=prominent/many flowers
# leaf:   0=simple/oval, 1=lobed, 2=compound/dissected, 3=needle-like
# color:  dominant non-green color accent (green is always present)
# size:   0=small plant (much text space), 1=medium, 2=fills page

HERBAL_PAGES = {
    # folio: {root, flower, leaf, color, size}
    'f1r':  {'root': 0, 'flower': 0, 'leaf': 0, 'color': 'green',  'size': 0},  # pg3: small plant, mostly text, simple leaves
    'f1v':  {'root': 0, 'flower': 1, 'leaf': 0, 'color': 'green',  'size': 1},  # pg4: medium plant, oval leaves, small flower top
    'f2r':  {'root': 1, 'flower': 2, 'leaf': 2, 'color': 'green',  'size': 1},  # pg5: dissected leaves, prominent flowers, small root
    'f2v':  {'root': 0, 'flower': 0, 'leaf': 0, 'color': 'green',  'size': 1},  # pg6: single large round leaf, no flower
    'f3r':  {'root': 2, 'flower': 0, 'leaf': 2, 'color': 'red',    'size': 2},  # pg7: striped red-green dissected leaves, big root
    'f3v':  {'root': 1, 'flower': 2, 'leaf': 1, 'color': 'blue',   'size': 2},  # pg8: lobed leaves, blue flower top, segmented root
    'f4r':  {'root': 1, 'flower': 0, 'leaf': 3, 'color': 'red',    'size': 2},  # pg9: needle-like small leaves, branching, small root
    'f4v':  {'root': 2, 'flower': 1, 'leaf': 0, 'color': 'blue',   'size': 1},  # pg10: bulbous root, trailing leaves, blue flower
    'f5r':  {'root': 0, 'flower': 0, 'leaf': 0, 'color': 'green',  'size': 1},  # pg11: large round leaves, no visible root/flower
    'f5v':  {'root': 1, 'flower': 2, 'leaf': 1, 'color': 'red',    'size': 1},  # pg12: lobed leaves, red flowers, small root
    'f6r':  {'root': 1, 'flower': 1, 'leaf': 2, 'color': 'green',  'size': 2},  # pg13: dissected spiny leaves, seed pods, fibrous root
    'f6v':  {'root': 1, 'flower': 2, 'leaf': 2, 'color': 'blue',   'size': 2},  # pg14: star-shaped spiny leaves with blue-green fruit, root visible
    'f7r':  {'root': 2, 'flower': 0, 'leaf': 0, 'color': 'green',  'size': 2},  # pg15: star rosette of simple leaves, big prominent root
    'f7v':  {'root': 1, 'flower': 1, 'leaf': 0, 'color': 'red',    'size': 1},  # pg16: oval leaves, red-orange fruit, small root
    'f8r':  {'root': 1, 'flower': 0, 'leaf': 0, 'color': 'green',  'size': 2},  # pg17: single huge arrow-shaped leaf, thin root
    'f8v':  {'root': 1, 'flower': 2, 'leaf': 0, 'color': 'red',    'size': 2},  # pg18: oval leaves, red-orange flowers, brown root
    'f9r':  {'root': 2, 'flower': 2, 'leaf': 1, 'color': 'red',    'size': 2},  # pg19: lobed leaves, red branching flowers, prominent root
    'f9v':  {'root': 1, 'flower': 2, 'leaf': 2, 'color': 'blue',   'size': 2},  # pg20: blue prominent flowers, dissected leaves
    'f10r': {'root': 0, 'flower': 1, 'leaf': 0, 'color': 'brown',  'size': 1},  # pg21: broad serrated leaves, blue sunflower, red tubers at base
    'f10v': {'root': 1, 'flower': 2, 'leaf': 0, 'color': 'blue',   'size': 1},  # pg22: drooping blue bell flowers, large oval leaves
    'f11r': {'root': 1, 'flower': 2, 'leaf': 0, 'color': 'blue',   'size': 2},  # pg23: dense dome of small leaves+blue flowers, spreading roots
    'f11v': {'root': 1, 'flower': 1, 'leaf': 0, 'color': 'brown',  'size': 2},  # pg24: artichoke-like scale dome, single blue flower top
    'f13r': {'root': 2, 'flower': 1, 'leaf': 1, 'color': 'brown',  'size': 2},  # pg25: large lobed leaves, bulbous brown root, small flowers
    'f13v': {'root': 1, 'flower': 1, 'leaf': 0, 'color': 'blue',   'size': 1},  # pg26: two plants with rounded leaves, blue flowers, root
    'f14r': {'root': 2, 'flower': 1, 'leaf': 2, 'color': 'red',    'size': 2},  # pg27: deeply dissected leaves, red stem, striped root
    'f14v': {'root': 1, 'flower': 2, 'leaf': 2, 'color': 'green',  'size': 2},  # pg28: compound dissected leaves with seed clusters, curled roots
    'f15r': {'root': 2, 'flower': 2, 'leaf': 1, 'color': 'red',    'size': 2},  # pg29: lobed dandelion-like leaves, large white flower, root
    'f15v': {'root': 1, 'flower': 0, 'leaf': 0, 'color': 'green',  'size': 1},  # pg30: simple three-lobed/clover, thin roots
    'f16r': {'root': 1, 'flower': 2, 'leaf': 2, 'color': 'red',    'size': 2},  # pg31: star/compound leaves (cannabis-like), red flowers, bulbous root
    'f17r': {'root': 1, 'flower': 2, 'leaf': 2, 'color': 'red',    'size': 2},  # pg32: red star flowers, dissected, root
    'f17v': {'root': 1, 'flower': 2, 'leaf': 2, 'color': 'blue',   'size': 1},  # pg33: fern-like leaves, blue flowers, small root
    'f18r': {'root': 2, 'flower': 1, 'leaf': 0, 'color': 'red',    'size': 2},  # pg34: oval leaves on branching stems, red catkins, large root
    'f18v': {'root': 1, 'flower': 1, 'leaf': 0, 'color': 'blue',   'size': 2},  # pg35: oval simple leaves, blue flowers top, root
    'f19r': {'root': 2, 'flower': 1, 'leaf': 1, 'color': 'green',  'size': 2},  # pg36: lobed leaves, prominent root system
    'f19v': {'root': 2, 'flower': 2, 'leaf': 2, 'color': 'blue',   'size': 2},  # pg37: dissected compound leaves, blue flowers, spreading root
    'f20r': {'root': 2, 'flower': 2, 'leaf': 1, 'color': 'red',    'size': 2},  # pg38: round/lobed leaves, root
    'f20v': {'root': 0, 'flower': 2, 'leaf': 0, 'color': 'green',  'size': 1},  # pg39: small compound leaves, many tiny flowers, no root
    'f21r': {'root': 0, 'flower': 2, 'leaf': 2, 'color': 'blue',   'size': 1},  # pg40: compound pinnate leaves, blue flowers, no root visible
    'f22r': {'root': 2, 'flower': 2, 'leaf': 0, 'color': 'red',    'size': 2},  # pg43: round oval leaves, tall inflorescence, prominent root
    'f22v': {'root': 2, 'flower': 1, 'leaf': 0, 'color': 'green',  'size': 2},  # pg44: oval leaves on thick stem, spiny root
    'f23r': {'root': 2, 'flower': 1, 'leaf': 1, 'color': 'blue',   'size': 2},  # pg45: deeply lobed palmate leaves, blue flowers, huge root
    'f23v': {'root': 2, 'flower': 1, 'leaf': 0, 'color': 'green',  'size': 2},  # pg46: round leaves on branching stem, root
    'f24r': {'root': 1, 'flower': 1, 'leaf': 1, 'color': 'green',  'size': 2},  # pg47: lobed leaves, white daisy flower top
    'f24v': {'root': 2, 'flower': 2, 'leaf': 0, 'color': 'blue',   'size': 2},  # pg48: round leaves, blue flowers, prominent root
    'f25r': {'root': 1, 'flower': 0, 'leaf': 0, 'color': 'green',  'size': 1},  # pg49: simple oval leaves on stem, small root
    'f25v': {'root': 2, 'flower': 0, 'leaf': 2, 'color': 'green',  'size': 1},  # pg50: dissected/palmate leaves, mandrake-like root+animal
    'f26r': {'root': 2, 'flower': 1, 'leaf': 0, 'color': 'green',  'size': 2},  # pg51: round scalloped leaves, root system
    'f26v': {'root': 2, 'flower': 1, 'leaf': 2, 'color': 'blue',   'size': 2},  # pg52: large tree-like, compound leaves, prominent root
    'f27r': {'root': 1, 'flower': 2, 'leaf': 0, 'color': 'green',  'size': 1},  # pg53: simple broad leaves, flowers top
    'f27v': {'root': 1, 'flower': 2, 'leaf': 2, 'color': 'red',    'size': 2},  # pg54: compound leaves, red-centered flowers, root
}


# ============================================================
# 2. PARSE TRANSCRIPTION AND EXTRACT WORDS PER FOLIO
# ============================================================

def parse_transcription(filepath):
    """Parse EVA transcription, return dict of folio -> list of words."""
    folio_words = defaultdict(list)
    current_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Check for folio header
            m = re.match(r'^<(f\d+[rv]\d?)>\s', line)
            if m:
                current_folio = m.group(1)
                # Remove the 'r1', 'r2' etc suffixes for multi-part folios
                # but keep basic r/v
                current_folio = re.sub(r'([rv])\d+$', r'\1', current_folio)
                continue

            # Check for text line
            m = re.match(r'^<(f\d+[rv]\d?)\.\d+', line)
            if m:
                folio_tag = m.group(1)
                current_folio = re.sub(r'([rv])\d+$', r'\1', folio_tag)

                # Extract the text part (after the tag)
                text_part = re.sub(r'^<[^>]+>\s*', '', line)

                # Clean the text
                # Remove editorial marks like @NNN, {xxx}, <->, ?, !, etc.
                text_part = re.sub(r'@\d+;?', '', text_part)
                text_part = re.sub(r'\{[^}]*\}', '', text_part)
                text_part = re.sub(r'<->', ' ', text_part)
                text_part = re.sub(r'[?,!*=]', '', text_part)

                # Split on dots and spaces to get words
                words = re.split(r'[.\s]+', text_part)
                words = [w.strip() for w in words if w.strip() and len(w.strip()) > 0]

                # Filter out purely punctuation/noise
                words = [w for w in words if re.search(r'[a-z]', w)]

                folio_words[current_folio].extend(words)

    return folio_words


def compute_word_frequencies(folio_words, folios):
    """Compute word frequencies for a set of folios."""
    counter = Counter()
    total = 0
    for f in folios:
        if f in folio_words:
            counter.update(folio_words[f])
            total += len(folio_words[f])
    return counter, total


def get_all_words(folio_words, folios):
    """Get vocabulary across specified folios."""
    vocab = set()
    for f in folios:
        if f in folio_words:
            vocab.update(folio_words[f])
    return vocab


# ============================================================
# 3. CORRELATION ANALYSIS
# ============================================================

def point_biserial_correlation(feature_vals, word_freqs, folios):
    """
    Compute point-biserial-like correlation between a continuous feature
    and word frequency (words per total words on that page).

    Returns Pearson r between feature value and word-frequency-rate.
    """
    n = len(folios)
    if n < 3:
        return 0.0

    # Compute mean and std of feature
    f_mean = sum(feature_vals) / n
    f_var = sum((x - f_mean)**2 for x in feature_vals) / n
    if f_var == 0:
        return 0.0
    f_std = math.sqrt(f_var)

    # Word frequency rates
    w_mean = sum(word_freqs) / n
    w_var = sum((x - w_mean)**2 for x in word_freqs) / n
    if w_var == 0:
        return 0.0
    w_std = math.sqrt(w_var)

    # Pearson correlation
    cov = sum((feature_vals[i] - f_mean) * (word_freqs[i] - w_mean) for i in range(n)) / n
    r = cov / (f_std * w_std)
    return r


def compute_correlations(folio_words, herbal_pages, feature_name):
    """
    For each word, compute correlation between its frequency rate and
    the specified visual feature across all herbal pages.
    """
    folios = sorted(herbal_pages.keys())
    # Only use folios that have transcription data
    folios = [f for f in folios if f in folio_words]

    if len(folios) < 5:
        return {}

    # Feature values
    feature_vals = []
    for f in folios:
        if feature_name == 'color_blue':
            feature_vals.append(1 if herbal_pages[f]['color'] == 'blue' else 0)
        elif feature_name == 'color_red':
            feature_vals.append(1 if herbal_pages[f]['color'] == 'red' else 0)
        else:
            feature_vals.append(herbal_pages[f][feature_name])

    # Get vocabulary (words appearing on at least 3 pages)
    word_page_count = defaultdict(int)
    for f in folios:
        for w in set(folio_words[f]):
            word_page_count[w] += 1

    vocab = [w for w, c in word_page_count.items() if c >= 3]

    # For each word, compute frequency rate per page and correlate
    results = {}
    for word in vocab:
        word_rates = []
        for f in folios:
            total = len(folio_words[f])
            if total == 0:
                word_rates.append(0.0)
            else:
                count = folio_words[f].count(word)
                word_rates.append(count / total)

        r = point_biserial_correlation(feature_vals, word_rates, folios)
        results[word] = r

    return results


# ============================================================
# 4. PERMUTATION TEST (NULL MODEL)
# ============================================================

def permutation_test(folio_words, herbal_pages, feature_name, n_perms=1000):
    """
    Shuffle feature assignments and compute max |correlation| each time.
    Returns the distribution of max correlations under the null.
    """
    folios = sorted(herbal_pages.keys())
    folios = [f for f in folios if f in folio_words]

    # Get real correlations
    real_corrs = compute_correlations(folio_words, herbal_pages, feature_name)
    if not real_corrs:
        return [], 0, 0

    real_max = max(abs(v) for v in real_corrs.values())

    # Get the real feature values
    if feature_name == 'color_blue':
        real_features = [1 if herbal_pages[f]['color'] == 'blue' else 0 for f in folios]
    elif feature_name == 'color_red':
        real_features = [1 if herbal_pages[f]['color'] == 'red' else 0 for f in folios]
    else:
        real_features = [herbal_pages[f][feature_name] for f in folios]

    # Word page counts for vocab
    word_page_count = defaultdict(int)
    for f in folios:
        for w in set(folio_words[f]):
            word_page_count[w] += 1
    vocab = [w for w, c in word_page_count.items() if c >= 3]

    # Precompute word rates
    word_rate_matrix = {}
    for word in vocab:
        rates = []
        for f in folios:
            total = len(folio_words[f])
            if total == 0:
                rates.append(0.0)
            else:
                rates.append(folio_words[f].count(word) / total)
        word_rate_matrix[word] = rates

    null_maxes = []
    random.seed(42)

    for _ in range(n_perms):
        shuffled = real_features[:]
        random.shuffle(shuffled)

        max_abs_r = 0
        for word in vocab:
            r = point_biserial_correlation(shuffled, word_rate_matrix[word], folios)
            if abs(r) > max_abs_r:
                max_abs_r = abs(r)

        null_maxes.append(max_abs_r)

    # p-value: fraction of null max >= real max
    p_value = sum(1 for x in null_maxes if x >= real_max) / n_perms

    return null_maxes, real_max, p_value


# ============================================================
# 5. STEM ANALYSIS
# ============================================================

def get_stem(word):
    """Extract approximate stem from EVA word."""
    # Common stems: cho-, sho-, dal-, dar-, etc.
    stems = []
    if word.startswith('cho'):
        stems.append('cho-')
    if word.startswith('sho'):
        stems.append('sho-')
    if word.startswith('dai'):
        stems.append('dai-')
    if word.startswith('dar'):
        stems.append('dar-')
    if word.startswith('cha'):
        stems.append('cha-')
    if word.startswith('sha'):
        stems.append('sha-')
    if word.startswith('qo'):
        stems.append('qo-')
    if word.startswith('ol'):
        stems.append('ol-')
    if word.startswith('ok'):
        stems.append('ok-')
    if word.startswith('ot'):
        stems.append('ot-')
    if word.startswith('cth'):
        stems.append('cth-')
    if word.startswith('che'):
        stems.append('che-')
    if word.startswith('she'):
        stems.append('she-')
    if word.startswith('kor'):
        stems.append('kor-')
    if word.startswith('kol'):
        stems.append('kol-')
    if 'aiin' in word:
        stems.append('-aiin')
    if 'ain' in word and 'aiin' not in word:
        stems.append('-ain')
    if word.endswith('dy'):
        stems.append('-dy')
    if word.endswith('chy'):
        stems.append('-chy')
    if word.endswith('ol'):
        stems.append('*-ol')
    if word.endswith('or'):
        stems.append('*-or')
    if word.endswith('al'):
        stems.append('*-al')
    if word.endswith('ar'):
        stems.append('*-ar')
    return stems


def compute_stem_correlations(folio_words, herbal_pages, feature_name):
    """Compute correlations for stem frequencies."""
    folios = sorted(herbal_pages.keys())
    folios = [f for f in folios if f in folio_words]

    if feature_name == 'color_blue':
        feature_vals = [1 if herbal_pages[f]['color'] == 'blue' else 0 for f in folios]
    elif feature_name == 'color_red':
        feature_vals = [1 if herbal_pages[f]['color'] == 'red' else 0 for f in folios]
    else:
        feature_vals = [herbal_pages[f][feature_name] for f in folios]

    # Count stems per folio
    stem_counts = defaultdict(lambda: [0]*len(folios))
    total_words = []

    for i, f in enumerate(folios):
        total_words.append(len(folio_words[f]))
        for w in folio_words[f]:
            for s in get_stem(w):
                stem_counts[s][i] += 1

    results = {}
    for stem, counts in stem_counts.items():
        # Convert to rates
        rates = [counts[i]/total_words[i] if total_words[i] > 0 else 0 for i in range(len(folios))]
        r = point_biserial_correlation(feature_vals, rates, folios)
        results[stem] = r

    return results


# ============================================================
# MAIN
# ============================================================

def main():
    filepath = r"C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt"
    folio_words = parse_transcription(filepath)

    print(f"Parsed {len(folio_words)} folios")
    print(f"Herbal pages classified: {len(HERBAL_PAGES)}")

    # Check overlap
    overlap = [f for f in HERBAL_PAGES if f in folio_words]
    print(f"Folios with both visual + text data: {len(overlap)}")

    for f in sorted(overlap):
        print(f"  {f}: {len(folio_words[f])} words, root={HERBAL_PAGES[f]['root']}, "
              f"flower={HERBAL_PAGES[f]['flower']}, leaf={HERBAL_PAGES[f]['leaf']}, "
              f"color={HERBAL_PAGES[f]['color']}")

    features = ['root', 'flower', 'leaf', 'color_blue', 'color_red', 'size']

    print("\n" + "="*80)
    print("WORD-FEATURE CORRELATIONS")
    print("="*80)

    all_correlations = {}

    for feat in features:
        print(f"\n--- Feature: {feat} ---")
        corrs = compute_correlations(folio_words, HERBAL_PAGES, feat)
        all_correlations[feat] = corrs

        if not corrs:
            print("  No correlations computed")
            continue

        # Top 10 positive
        sorted_pos = sorted(corrs.items(), key=lambda x: x[1], reverse=True)[:10]
        print(f"  Top 10 POSITIVE correlations (word appears MORE when {feat} is high):")
        for w, r in sorted_pos:
            print(f"    {w:20s}  r = {r:+.4f}")

        # Top 10 negative
        sorted_neg = sorted(corrs.items(), key=lambda x: x[1])[:10]
        print(f"  Top 10 NEGATIVE correlations (word appears LESS when {feat} is high):")
        for w, r in sorted_neg:
            print(f"    {w:20s}  r = {r:+.4f}")

    # ============================================================
    # STEM CORRELATIONS
    # ============================================================
    print("\n" + "="*80)
    print("STEM-FEATURE CORRELATIONS")
    print("="*80)

    for feat in features:
        print(f"\n--- Feature: {feat} ---")
        stem_corrs = compute_stem_correlations(folio_words, HERBAL_PAGES, feat)
        sorted_stems = sorted(stem_corrs.items(), key=lambda x: abs(x[1]), reverse=True)
        print(f"  All stems by |r|:")
        for s, r in sorted_stems:
            print(f"    {s:15s}  r = {r:+.4f}")

    # ============================================================
    # KEY QUESTION: cho- and sho- vs ALL features
    # ============================================================
    print("\n" + "="*80)
    print("KEY QUESTION: cho- and sho- stems vs ALL features")
    print("="*80)

    for stem_prefix in ['cho', 'sho']:
        print(f"\n  === Words starting with '{stem_prefix}' ===")
        for feat in features:
            stem_corrs = compute_stem_correlations(folio_words, HERBAL_PAGES, feat)
            key = f"{stem_prefix}-"
            if key in stem_corrs:
                print(f"    vs {feat:12s}: r = {stem_corrs[key]:+.4f}")

    # Also test 'chol', 'chor', 'shol', 'shor' as individual words
    print("\n  === Individual high-frequency words ===")
    test_words = ['chol', 'chor', 'shol', 'shor', 'daiin', 'dain', 'dar',
                  'chey', 'shey', 'cthy', 'chy', 'ol', 'or', 'qo',
                  'chody', 'shody', 'chodaiin', 'shodaiin', 'okol']

    for w in test_words:
        print(f"\n  Word: '{w}'")
        for feat in features:
            corrs = all_correlations.get(feat, {})
            if w in corrs:
                r = corrs[w]
                print(f"    vs {feat:12s}: r = {r:+.4f}")

    # ============================================================
    # TOP 20 MOST FEATURE-CORRELATED WORDS
    # ============================================================
    print("\n" + "="*80)
    print("TOP 20 MOST FEATURE-CORRELATED WORDS (across all features)")
    print("="*80)

    # Collect all (word, feature, |r|) tuples
    all_tuples = []
    for feat in features:
        for w, r in all_correlations.get(feat, {}).items():
            all_tuples.append((w, feat, r, abs(r)))

    all_tuples.sort(key=lambda x: x[3], reverse=True)

    # Deduplicate by word (keep highest)
    seen_words = set()
    top_unique = []
    for w, feat, r, absr in all_tuples:
        if w not in seen_words:
            seen_words.add(w)
            top_unique.append((w, feat, r))
            if len(top_unique) >= 20:
                break

    print(f"{'Rank':>4}  {'Word':20s}  {'Best Feature':12s}  {'r':>8}")
    print("-" * 52)
    for i, (w, feat, r) in enumerate(top_unique, 1):
        print(f"{i:4d}  {w:20s}  {feat:12s}  {r:+.4f}")

    # ============================================================
    # PERMUTATION TEST
    # ============================================================
    print("\n" + "="*80)
    print("PERMUTATION TEST (Null Model, 1000 shuffles)")
    print("="*80)

    for feat in ['root', 'flower', 'leaf']:
        print(f"\n--- Feature: {feat} ---")
        null_maxes, real_max, p_value = permutation_test(
            folio_words, HERBAL_PAGES, feat, n_perms=1000
        )
        if null_maxes:
            null_mean = sum(null_maxes) / len(null_maxes)
            null_95 = sorted(null_maxes)[int(0.95 * len(null_maxes))]
            print(f"  Real max |r|:        {real_max:.4f}")
            print(f"  Null mean max |r|:   {null_mean:.4f}")
            print(f"  Null 95th pctl:      {null_95:.4f}")
            print(f"  p-value:             {p_value:.4f}")
            if p_value < 0.05:
                print(f"  ** SIGNIFICANT at p<0.05 **")
            elif p_value < 0.10:
                print(f"  * Marginally significant (p<0.10) *")
            else:
                print(f"  Not significant")

    # Also test color features
    for feat in ['color_blue', 'color_red']:
        print(f"\n--- Feature: {feat} ---")
        null_maxes, real_max, p_value = permutation_test(
            folio_words, HERBAL_PAGES, feat, n_perms=1000
        )
        if null_maxes:
            null_mean = sum(null_maxes) / len(null_maxes)
            null_95 = sorted(null_maxes)[int(0.95 * len(null_maxes))]
            print(f"  Real max |r|:        {real_max:.4f}")
            print(f"  Null mean max |r|:   {null_mean:.4f}")
            print(f"  Null 95th pctl:      {null_95:.4f}")
            print(f"  p-value:             {p_value:.4f}")
            if p_value < 0.05:
                print(f"  ** SIGNIFICANT at p<0.05 **")
            elif p_value < 0.10:
                print(f"  * Marginally significant (p<0.10) *")
            else:
                print(f"  Not significant")


if __name__ == '__main__':
    main()
