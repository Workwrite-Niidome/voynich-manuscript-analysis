#!/usr/bin/env python3
"""
Pharmaceutical Encoding Hypothesis Test for the Voynich Manuscript
Tests whether herbal page text encodes PHARMACEUTICAL PROPERTIES rather than visual features.
"""

import re
import json
import math
from collections import Counter, defaultdict
from itertools import combinations

# ============================================================
# DATA EXTRACTION
# ============================================================

def extract_page_words(filepath, target_pages):
    """Extract words from specific pages in EVA transcription."""
    page_words = defaultdict(list)
    current_page = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Page header
            page_match = re.match(r'^<(f\d+[rv]\d*)>', line)
            if page_match and '.' not in line.split('>')[0]:
                current_page = page_match.group(1)
                continue
            # Content line
            if current_page and current_page in target_pages:
                content_match = re.match(r'^<[^>]+>\s+(.*)', line)
                if content_match:
                    text = content_match.group(1)
                    # Clean EVA: remove annotations, line breaks
                    text = re.sub(r'<[^>]*>', '', text)
                    text = re.sub(r'\{[^}]*\}', '', text)
                    text = re.sub(r'@\d+;?', '', text)
                    text = re.sub(r'[,.\-?!\'"]', ' ', text)
                    words = [w.strip() for w in text.split() if w.strip() and len(w.strip()) > 1]
                    page_words[current_page].extend(words)

    return page_words


def extract_all_herbal_pages(filepath):
    """Extract words from all herbal section pages (f1r through f57v approximately)."""
    page_words = defaultdict(list)
    current_page = None
    illustration_type = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            page_match = re.match(r'^<(f\d+[rv]\d*)>\s+<!\s*(.*?)>', line)
            if page_match:
                current_page = page_match.group(1)
                meta = page_match.group(2)
                # $I=H means herbal illustration
                if '$I=H' in meta:
                    illustration_type = 'H'
                else:
                    illustration_type = meta
                continue

            page_match2 = re.match(r'^<(f\d+[rv]\d*)>', line)
            if page_match2 and '.' not in line.split('>')[0]:
                current_page = page_match2.group(1)
                continue

            if current_page:
                content_match = re.match(r'^<[^>]+>\s+(.*)', line)
                if content_match:
                    text = content_match.group(1)
                    text = re.sub(r'<[^>]*>', '', text)
                    text = re.sub(r'\{[^}]*\}', '', text)
                    text = re.sub(r'@\d+;?', '', text)
                    text = re.sub(r'[,.\-?!\'"]', ' ', text)
                    words = [w.strip() for w in text.split() if w.strip() and len(w.strip()) > 1]
                    page_words[current_page].extend(words)

    return page_words


def get_herbal_pages(filepath):
    """Get list of herbal pages ($I=H)."""
    herbal_pages = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            page_match = re.match(r'^<(f\d+[rv]\d*)>\s+<!\s*(.*?)>', line)
            if page_match:
                page = page_match.group(1)
                meta = page_match.group(2)
                if '$I=H' in meta:
                    herbal_pages.append(page)
    return herbal_pages


# ============================================================
# MORPHEME EXTRACTION
# ============================================================

def extract_morphemes(word):
    """Extract prefix, root, and suffix morphemes from EVA word."""
    morphemes = []

    # Common prefixes
    prefixes = ['qo', 'ol', 'ot', 'ok', 'sh', 'ch', 'da', 'so', 'ko']
    for p in prefixes:
        if word.startswith(p):
            morphemes.append(('prefix', p))
            break

    # Common suffixes
    suffixes = ['aiin', 'ain', 'iin', 'in', 'dy', 'ey', 'ar', 'or', 'al', 'ol', 'am', 'om', 'an']
    for s in suffixes:
        if word.endswith(s):
            morphemes.append(('suffix', s))
            break

    # Root patterns
    roots = ['ch', 'sh', 'cth', 'ckh', 'cph', 'cfh', 'od', 'ok', 'ol', 'or', 'ot', 'dar', 'kor', 'dol']
    for r in roots:
        if r in word:
            morphemes.append(('root', r))

    return morphemes


def get_word_set(words):
    return set(words)


def get_morpheme_profile(words):
    """Get frequency distribution of morphemes for a word list."""
    profile = Counter()
    for w in words:
        morphemes = extract_morphemes(w)
        for mtype, mval in morphemes:
            profile[f"{mtype}:{mval}"] += 1
    # Normalize
    total = sum(profile.values()) or 1
    return {k: v/total for k, v in profile.items()}


# ============================================================
# SIMILARITY METRICS
# ============================================================

def jaccard_similarity(set1, set2):
    if not set1 and not set2:
        return 0.0
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union)


def cosine_similarity(profile1, profile2):
    all_keys = set(profile1.keys()) | set(profile2.keys())
    dot = sum(profile1.get(k, 0) * profile2.get(k, 0) for k in all_keys)
    mag1 = math.sqrt(sum(v**2 for v in profile1.values())) or 1
    mag2 = math.sqrt(sum(v**2 for v in profile2.values())) or 1
    return dot / (mag1 * mag2)


def group_avg_similarity(page_words, group, metric='jaccard'):
    """Average pairwise similarity within a group of pages."""
    if len(group) < 2:
        return 0.0
    sims = []
    for p1, p2 in combinations(group, 2):
        if p1 in page_words and p2 in page_words:
            if metric == 'jaccard':
                s = jaccard_similarity(set(page_words[p1]), set(page_words[p2]))
            else:
                pr1 = get_morpheme_profile(page_words[p1])
                pr2 = get_morpheme_profile(page_words[p2])
                s = cosine_similarity(pr1, pr2)
            sims.append(s)
    return sum(sims)/len(sims) if sims else 0.0


def between_group_similarity(page_words, group1, group2, metric='jaccard'):
    """Average pairwise similarity between two groups."""
    sims = []
    for p1 in group1:
        for p2 in group2:
            if p1 in page_words and p2 in page_words:
                if metric == 'jaccard':
                    s = jaccard_similarity(set(page_words[p1]), set(page_words[p2]))
                else:
                    pr1 = get_morpheme_profile(page_words[p1])
                    pr2 = get_morpheme_profile(page_words[p2])
                    s = cosine_similarity(pr1, pr2)
                sims.append(s)
    return sum(sims)/len(sims) if sims else 0.0


# ============================================================
# PERMUTATION TEST
# ============================================================

def permutation_test(page_words, group1, group2, metric='jaccard', n_perms=10000):
    """Test if within-group similarity is significantly higher than between-group."""
    import random

    within1 = group_avg_similarity(page_words, group1, metric)
    within2 = group_avg_similarity(page_words, group2, metric)
    between = between_group_similarity(page_words, group1, group2, metric)

    observed_diff = ((within1 + within2) / 2) - between

    all_pages = list(group1) + list(group2)
    n1 = len(group1)
    count_extreme = 0

    for _ in range(n_perms):
        random.shuffle(all_pages)
        perm_g1 = all_pages[:n1]
        perm_g2 = all_pages[n1:]
        w1 = group_avg_similarity(page_words, perm_g1, metric)
        w2 = group_avg_similarity(page_words, perm_g2, metric)
        b = between_group_similarity(page_words, perm_g1, perm_g2, metric)
        perm_diff = ((w1 + w2) / 2) - b
        if perm_diff >= observed_diff:
            count_extreme += 1

    p_value = count_extreme / n_perms
    return observed_diff, p_value


# ============================================================
# MAIN TESTS
# ============================================================

def main():
    filepath = "C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt"

    # Our 5 anchor plant pages
    anchor_pages = ['f2r', 'f3r', 'f9r', 'f41r', 'f47r']

    # Extract words
    all_page_words = extract_all_herbal_pages(filepath)
    anchor_words = {p: all_page_words[p] for p in anchor_pages if p in all_page_words}

    # Get herbal pages
    herbal_pages = get_herbal_pages(filepath)

    results = {}

    print("=" * 70)
    print("PHARMACEUTICAL ENCODING HYPOTHESIS TEST")
    print("=" * 70)

    # Print word counts for anchor pages
    print("\n--- Anchor Page Word Counts ---")
    for p in anchor_pages:
        words = anchor_words.get(p, [])
        print(f"  {p}: {len(words)} words, {len(set(words))} unique")

    # ============================================================
    # TEST 1: ADMINISTRATION ROUTE
    # ============================================================
    print("\n" + "=" * 70)
    print("TEST 1: ADMINISTRATION ROUTE GROUPING")
    print("=" * 70)

    # Internal liquid (decoction drunk): Paeonia(f2r), Adiantum(f41r), Vitis(f47r)
    internal_liquid = ['f2r', 'f41r', 'f47r']
    # Seeds/inhalation: Nigella(f9r)
    seeds_inhalation = ['f9r']
    # External application: Vitis(f47r), Rubia(f3r)
    external_app = ['f47r', 'f3r']

    print("\nInternal liquid group (f2r, f41r, f47r):")
    il_sim_j = group_avg_similarity(anchor_words, internal_liquid, 'jaccard')
    il_sim_c = group_avg_similarity(anchor_words, internal_liquid, 'cosine')
    print(f"  Jaccard avg: {il_sim_j:.4f}")
    print(f"  Cosine avg:  {il_sim_c:.4f}")

    print("\nExternal application group (f47r, f3r):")
    ea_sim_j = group_avg_similarity(anchor_words, external_app, 'jaccard')
    ea_sim_c = group_avg_similarity(anchor_words, external_app, 'cosine')
    print(f"  Jaccard avg: {ea_sim_j:.4f}")
    print(f"  Cosine avg:  {ea_sim_c:.4f}")

    # Compare: internal liquid vs all others
    others = ['f3r', 'f9r']
    between_j = between_group_similarity(anchor_words, internal_liquid, others, 'jaccard')
    between_c = between_group_similarity(anchor_words, internal_liquid, others, 'cosine')
    print(f"\nInternal-liquid within vs between:")
    print(f"  Within Jaccard:  {il_sim_j:.4f}")
    print(f"  Between Jaccard: {between_j:.4f}")
    print(f"  Ratio: {il_sim_j/between_j:.2f}x" if between_j > 0 else "  Ratio: N/A")
    print(f"  Within Cosine:   {il_sim_c:.4f}")
    print(f"  Between Cosine:  {between_c:.4f}")
    print(f"  Ratio: {il_sim_c/between_c:.2f}x" if between_c > 0 else "  Ratio: N/A")

    # Unique vocabulary for seeds/inhalation (Nigella f9r)
    nigella_words = set(anchor_words.get('f9r', []))
    other_words = set()
    for p in ['f2r', 'f3r', 'f41r', 'f47r']:
        other_words |= set(anchor_words.get(p, []))
    nigella_unique = nigella_words - other_words
    print(f"\nNigella (f9r) unique words (not in other anchors): {len(nigella_unique)}")
    print(f"  Examples: {list(nigella_unique)[:15]}")

    results['test1'] = {
        'internal_liquid_jaccard': il_sim_j,
        'internal_liquid_cosine': il_sim_c,
        'between_jaccard': between_j,
        'between_cosine': between_c,
        'nigella_unique_count': len(nigella_unique)
    }

    # ============================================================
    # TEST 2: GALENIC QUALITY GROUPING
    # ============================================================
    print("\n" + "=" * 70)
    print("TEST 2: GALENIC QUALITY GROUPING (Hot vs Cold)")
    print("=" * 70)

    hot_plants = ['f2r', 'f3r', 'f9r']   # Paeonia, Rubia, Nigella
    cold_plants = ['f41r', 'f47r']         # Adiantum, Vitis

    hot_within_j = group_avg_similarity(anchor_words, hot_plants, 'jaccard')
    hot_within_c = group_avg_similarity(anchor_words, hot_plants, 'cosine')
    cold_within_j = group_avg_similarity(anchor_words, cold_plants, 'jaccard')
    cold_within_c = group_avg_similarity(anchor_words, cold_plants, 'cosine')
    hc_between_j = between_group_similarity(anchor_words, hot_plants, cold_plants, 'jaccard')
    hc_between_c = between_group_similarity(anchor_words, hot_plants, cold_plants, 'cosine')

    print(f"\nHot plants within-group (f2r, f3r, f9r):")
    print(f"  Jaccard: {hot_within_j:.4f}")
    print(f"  Cosine:  {hot_within_c:.4f}")
    print(f"\nCold plants within-group (f41r, f47r):")
    print(f"  Jaccard: {cold_within_j:.4f}")
    print(f"  Cosine:  {cold_within_c:.4f}")
    print(f"\nHot-Cold between-group:")
    print(f"  Jaccard: {hc_between_j:.4f}")
    print(f"  Cosine:  {hc_between_c:.4f}")

    # Pharmaceutical hypothesis predicts: within > between
    hot_cold_signal = ((hot_within_j + cold_within_j) / 2) - hc_between_j
    print(f"\nWithin - Between (Jaccard): {hot_cold_signal:.4f}")
    print(f"  {'SUPPORTS' if hot_cold_signal > 0 else 'CONTRADICTS'} pharmaceutical grouping")

    # Permutation test
    obs_diff, p_val = permutation_test(anchor_words, hot_plants, cold_plants, 'jaccard', 5000)
    print(f"\nPermutation test (5000 perms):")
    print(f"  Observed diff: {obs_diff:.4f}")
    print(f"  p-value: {p_val:.4f}")
    print(f"  {'Significant' if p_val < 0.05 else 'Not significant'} at alpha=0.05")

    results['test2'] = {
        'hot_within_j': hot_within_j,
        'cold_within_j': cold_within_j,
        'between_j': hc_between_j,
        'signal': hot_cold_signal,
        'p_value': p_val
    }

    # ============================================================
    # TEST 3: BODY SYSTEM GROUPING
    # ============================================================
    print("\n" + "=" * 70)
    print("TEST 3: BODY SYSTEM GROUPING")
    print("=" * 70)

    head_related = ['f9r', 'f47r']     # Nigella=headache, Vitis=headache
    kidney_urinary = ['f3r', 'f41r']   # Rubia=urinary, Adiantum=kidney stones
    nervous = ['f2r']                   # Paeonia=epilepsy (singleton)

    head_sim_j = group_avg_similarity(anchor_words, head_related, 'jaccard')
    head_sim_c = group_avg_similarity(anchor_words, head_related, 'cosine')
    kidney_sim_j = group_avg_similarity(anchor_words, kidney_urinary, 'jaccard')
    kidney_sim_c = group_avg_similarity(anchor_words, kidney_urinary, 'cosine')

    print(f"\nHead-related (f9r, f47r): Jaccard={head_sim_j:.4f}, Cosine={head_sim_c:.4f}")
    print(f"Kidney/urinary (f3r, f41r): Jaccard={kidney_sim_j:.4f}, Cosine={kidney_sim_c:.4f}")

    # Compare to non-matching pairs
    non_matching_pairs = [('f2r', 'f9r'), ('f2r', 'f47r'), ('f3r', 'f9r'), ('f3r', 'f47r'), ('f2r', 'f41r')]
    non_match_sims = []
    for p1, p2 in non_matching_pairs:
        if p1 in anchor_words and p2 in anchor_words:
            s = jaccard_similarity(set(anchor_words[p1]), set(anchor_words[p2]))
            non_match_sims.append(s)
            print(f"  Non-matching pair ({p1}, {p2}): Jaccard={s:.4f}")

    avg_non_match = sum(non_match_sims) / len(non_match_sims) if non_match_sims else 0
    avg_match = (head_sim_j + kidney_sim_j) / 2
    print(f"\nAvg matching body-system: {avg_match:.4f}")
    print(f"Avg non-matching:        {avg_non_match:.4f}")
    print(f"  {'SUPPORTS' if avg_match > avg_non_match else 'CONTRADICTS'} body-system grouping")

    results['test3'] = {
        'head_jaccard': head_sim_j,
        'kidney_jaccard': kidney_sim_j,
        'avg_matching': avg_match,
        'avg_non_matching': avg_non_match
    }

    # ============================================================
    # TEST 4: PREPARATION METHOD
    # ============================================================
    print("\n" + "=" * 70)
    print("TEST 4: PREPARATION METHOD GROUPING")
    print("=" * 70)

    decoction = ['f2r', 'f41r', 'f3r']  # Root/plant decoction
    seed_powder = ['f9r']                 # Seeds chewed/inhaled
    applied = ['f47r']                    # Leaves/juice applied

    dec_sim_j = group_avg_similarity(anchor_words, decoction, 'jaccard')
    dec_sim_c = group_avg_similarity(anchor_words, decoction, 'cosine')
    print(f"\nDecoction group (f2r, f41r, f3r): Jaccard={dec_sim_j:.4f}, Cosine={dec_sim_c:.4f}")

    # Decoction vs non-decoction
    dec_vs_other_j = between_group_similarity(anchor_words, decoction, ['f9r', 'f47r'], 'jaccard')
    print(f"Decoction vs others: Jaccard={dec_vs_other_j:.4f}")
    print(f"Ratio (within/between): {dec_sim_j/dec_vs_other_j:.2f}x" if dec_vs_other_j > 0 else "N/A")

    # Look for shared "preparation" vocabulary within decoction group
    dec_shared = set(anchor_words.get('f2r', [])) & set(anchor_words.get('f41r', [])) & set(anchor_words.get('f3r', []))
    print(f"\nWords shared by ALL decoction plants: {len(dec_shared)}")
    print(f"  {sorted(dec_shared)[:20]}")

    # Words shared by decoction plants but NOT in seed/applied plants
    other_all = set(anchor_words.get('f9r', [])) | set(anchor_words.get('f47r', []))
    dec_exclusive = dec_shared - other_all
    print(f"Decoction-exclusive shared words: {len(dec_exclusive)}")
    print(f"  {sorted(dec_exclusive)[:20]}")

    results['test4'] = {
        'decoction_within_j': dec_sim_j,
        'decoction_vs_other_j': dec_vs_other_j,
        'decoction_shared_words': len(dec_shared),
        'decoction_exclusive_words': len(dec_exclusive)
    }

    # ============================================================
    # TEST 5: sh- MORPHEME AND DOSAGE INTENSITY
    # ============================================================
    print("\n" + "=" * 70)
    print("TEST 5: sh- MORPHEME vs GALENIC DEGREE (Dosage Intensity)")
    print("=" * 70)

    # Galenic degrees (higher = more intense):
    # Nigella: Hot 3rd -> 3
    # Rubia: Hot 2nd -> 2
    # Paeonia: Hot 1st -> 1  (but Dry 2nd, so average ~1.5)
    # Adiantum: Cold, Dry -> 1
    # Vitis: Cold 1st, Moist 2nd -> 1

    galenic_intensity = {
        'f9r': 3,    # Nigella Hot 3rd
        'f3r': 2,    # Rubia Hot 2nd
        'f2r': 1.5,  # Paeonia Hot 1st, Dry 2nd
        'f41r': 1,   # Adiantum Cold, Dry
        'f47r': 1,   # Vitis Cold 1st
    }

    plant_names = {
        'f2r': 'Paeonia',
        'f3r': 'Rubia',
        'f9r': 'Nigella',
        'f41r': 'Adiantum',
        'f47r': 'Vitis'
    }

    sh_frequencies = {}
    for page in anchor_pages:
        words = anchor_words.get(page, [])
        total = len(words) or 1
        sh_count = sum(1 for w in words if w.startswith('sh'))
        sh_freq = sh_count / total
        sh_frequencies[page] = sh_freq
        print(f"  {page} ({plant_names[page]}): sh-words={sh_count}/{total}, freq={sh_freq:.4f}, intensity={galenic_intensity[page]}")

    # Calculate Spearman rank correlation
    pages_sorted = sorted(anchor_pages)
    intensities = [galenic_intensity[p] for p in pages_sorted]
    sh_freqs = [sh_frequencies[p] for p in pages_sorted]

    # Spearman correlation (rank-based)
    def spearman_corr(x, y):
        n = len(x)
        def rank(vals):
            sorted_vals = sorted(enumerate(vals), key=lambda t: t[1])
            ranks = [0] * n
            for r, (i, v) in enumerate(sorted_vals):
                ranks[i] = r + 1
            return ranks
        rx = rank(x)
        ry = rank(y)
        d_sq = sum((a - b) ** 2 for a, b in zip(rx, ry))
        return 1 - (6 * d_sq) / (n * (n**2 - 1))

    rho = spearman_corr(intensities, sh_freqs)
    print(f"\nSpearman correlation (intensity vs sh-freq): rho = {rho:.4f}")
    print(f"  {'SUPPORTS' if rho > 0.3 else 'WEAK/CONTRADICTS'} sh- as dosage/intensity marker")

    # Also check other key morphemes
    print("\n--- Other morpheme frequencies by Galenic intensity ---")
    for morpheme_prefix in ['ch', 'qo', 'ot', 'ok', 'da', 'ol', 'cth', 'ckh']:
        freqs = {}
        for page in anchor_pages:
            words = anchor_words.get(page, [])
            total = len(words) or 1
            count = sum(1 for w in words if w.startswith(morpheme_prefix))
            freqs[page] = count / total

        vals = [freqs[p] for p in pages_sorted]
        r = spearman_corr(intensities, vals)
        print(f"  {morpheme_prefix:4s}-: rho={r:+.4f}  {'<-- correlates with intensity' if abs(r) > 0.7 else ''}")

    results['test5'] = {
        'sh_frequencies': sh_frequencies,
        'spearman_rho': rho
    }

    # ============================================================
    # TEST 6: ALL-PAIRS SIMILARITY MATRIX
    # ============================================================
    print("\n" + "=" * 70)
    print("TEST 6: FULL SIMILARITY MATRIX (Anchor Pages)")
    print("=" * 70)

    print("\nJaccard similarity matrix:")
    print(f"{'':>8}", end='')
    for p in anchor_pages:
        print(f"{p:>8}", end='')
    print()

    for p1 in anchor_pages:
        print(f"{p1:>8}", end='')
        for p2 in anchor_pages:
            if p1 == p2:
                print(f"{'1.000':>8}", end='')
            else:
                s = jaccard_similarity(set(anchor_words.get(p1, [])), set(anchor_words.get(p2, [])))
                print(f"{s:>8.4f}", end='')
        print()

    print("\nMorpheme cosine similarity matrix:")
    profiles = {p: get_morpheme_profile(anchor_words.get(p, [])) for p in anchor_pages}
    print(f"{'':>8}", end='')
    for p in anchor_pages:
        print(f"{p:>8}", end='')
    print()

    for p1 in anchor_pages:
        print(f"{p1:>8}", end='')
        for p2 in anchor_pages:
            if p1 == p2:
                print(f"{'1.000':>8}", end='')
            else:
                s = cosine_similarity(profiles[p1], profiles[p2])
                print(f"{s:>8.4f}", end='')
        print()

    # ============================================================
    # TEST 7: K-MEANS CLUSTERING OF ALL HERBAL PAGES
    # ============================================================
    print("\n" + "=" * 70)
    print("TEST 7: K-MEANS CLUSTERING OF ALL HERBAL PAGES")
    print("=" * 70)

    herbal_words = {p: all_page_words[p] for p in herbal_pages if p in all_page_words and len(all_page_words[p]) > 5}

    print(f"\nHerbal pages with >5 words: {len(herbal_words)}")

    # Build morpheme profiles for all herbal pages
    all_morpheme_keys = set()
    herbal_profiles = {}
    for p in herbal_words:
        prof = get_morpheme_profile(herbal_words[p])
        herbal_profiles[p] = prof
        all_morpheme_keys |= set(prof.keys())

    all_morpheme_keys = sorted(all_morpheme_keys)

    # Convert to vectors
    def profile_to_vec(profile):
        return [profile.get(k, 0) for k in all_morpheme_keys]

    vectors = {p: profile_to_vec(herbal_profiles[p]) for p in herbal_profiles}

    # Simple k-means
    import random

    def kmeans(vectors_dict, k, max_iter=100):
        pages = list(vectors_dict.keys())
        vecs = [vectors_dict[p] for p in pages]
        n = len(vecs)
        dim = len(vecs[0])

        # Initialize centroids randomly
        random.seed(42)
        indices = random.sample(range(n), min(k, n))
        centroids = [list(vecs[i]) for i in indices]

        assignments = [0] * n

        for iteration in range(max_iter):
            # Assign
            new_assignments = []
            for v in vecs:
                dists = []
                for c in centroids:
                    d = sum((a-b)**2 for a, b in zip(v, c))
                    dists.append(d)
                new_assignments.append(dists.index(min(dists)))

            if new_assignments == assignments:
                break
            assignments = new_assignments

            # Update centroids
            for ci in range(k):
                members = [vecs[j] for j in range(n) if assignments[j] == ci]
                if members:
                    centroids[ci] = [sum(m[d] for m in members)/len(members) for d in range(dim)]

        clusters = defaultdict(list)
        for i, p in enumerate(pages):
            clusters[assignments[i]].append(p)

        return dict(clusters), centroids

    # Try k=3 (pharmaceutical categories: hot-internal, cold-external, head-related?)
    for k in [3, 4, 5]:
        clusters, centroids = kmeans(vectors, k)
        print(f"\n--- k={k} clustering ---")
        for ci in sorted(clusters.keys()):
            members = clusters[ci]
            # Check which anchor pages are in this cluster
            anchor_in = [p for p in members if p in anchor_pages]
            anchor_labels = [f"{p}={plant_names[p]}" for p in anchor_in]
            print(f"  Cluster {ci}: {len(members)} pages")
            print(f"    Anchors: {anchor_labels if anchor_labels else 'none'}")
            print(f"    Pages: {members[:10]}{'...' if len(members) > 10 else ''}")

            # Top morphemes in cluster centroid
            top_morph = sorted(range(len(all_morpheme_keys)),
                             key=lambda i: centroids[ci][i], reverse=True)[:5]
            top_labels = [(all_morpheme_keys[i], f"{centroids[ci][i]:.3f}") for i in top_morph]
            print(f"    Top morphemes: {top_labels}")

    # ============================================================
    # TEST 8: SHARED VOCABULARY ANALYSIS BY CATEGORY
    # ============================================================
    print("\n" + "=" * 70)
    print("TEST 8: CATEGORY-SPECIFIC SHARED VOCABULARY")
    print("=" * 70)

    # For each pharmaceutical grouping, find words that appear in ALL members
    # but NOT in non-members
    categories = {
        'Hot (f2r,f3r,f9r)': (['f2r', 'f3r', 'f9r'], ['f41r', 'f47r']),
        'Cold (f41r,f47r)': (['f41r', 'f47r'], ['f2r', 'f3r', 'f9r']),
        'Internal liquid (f2r,f41r,f47r)': (['f2r', 'f41r', 'f47r'], ['f3r', 'f9r']),
        'Head-related (f9r,f47r)': (['f9r', 'f47r'], ['f2r', 'f3r', 'f41r']),
        'Kidney/urinary (f3r,f41r)': (['f3r', 'f41r'], ['f2r', 'f9r', 'f47r']),
    }

    for cat_name, (in_group, out_group) in categories.items():
        in_sets = [set(anchor_words.get(p, [])) for p in in_group]
        out_sets = [set(anchor_words.get(p, [])) for p in out_group]

        if in_sets:
            shared_in = in_sets[0]
            for s in in_sets[1:]:
                shared_in &= s
        else:
            shared_in = set()

        out_all = set()
        for s in out_sets:
            out_all |= s

        exclusive = shared_in - out_all

        print(f"\n{cat_name}:")
        print(f"  Shared by all in-group: {len(shared_in)} words")
        print(f"  Exclusive to category:  {len(exclusive)} words")
        if exclusive:
            print(f"  Exclusive words: {sorted(exclusive)[:15]}")

    # ============================================================
    # TEST 9: SUFFIX DISTRIBUTION BY PHARMACEUTICAL CATEGORY
    # ============================================================
    print("\n" + "=" * 70)
    print("TEST 9: SUFFIX PATTERNS BY PHARMACEUTICAL CATEGORY")
    print("=" * 70)

    suffix_patterns = ['aiin', 'ain', 'dy', 'ey', 'ar', 'or', 'al', 'ol', 'am', 'om', 'an', 'in']

    print(f"\n{'Page':>8} {'Plant':>10}", end='')
    for suf in suffix_patterns:
        print(f" -{suf:>5}", end='')
    print()

    for page in anchor_pages:
        words = anchor_words.get(page, [])
        total = len(words) or 1
        print(f"{page:>8} {plant_names[page]:>10}", end='')
        for suf in suffix_patterns:
            count = sum(1 for w in words if w.endswith(suf))
            freq = count / total
            print(f" {freq:>6.3f}", end='')
        print()

    # Check if -am/-om suffixes correlate with body system (head?)
    # Check if -aiin suffix correlates with preparation type
    print("\n--- Suffix correlation with Galenic intensity ---")
    for suf in suffix_patterns:
        freqs_list = []
        for page in anchor_pages:
            words = anchor_words.get(page, [])
            total = len(words) or 1
            count = sum(1 for w in words if w.endswith(suf))
            freqs_list.append(count / total)
        ints = [galenic_intensity[p] for p in anchor_pages]
        r = spearman_corr(ints, freqs_list)
        marker = ''
        if abs(r) > 0.7:
            marker = ' <-- STRONG'
        elif abs(r) > 0.5:
            marker = ' <-- moderate'
        print(f"  -{suf:>5}: rho={r:+.4f}{marker}")

    # ============================================================
    # TEST 10: WORD LENGTH DISTRIBUTION BY GALENIC QUALITY
    # ============================================================
    print("\n" + "=" * 70)
    print("TEST 10: WORD LENGTH vs GALENIC QUALITY")
    print("=" * 70)

    for page in anchor_pages:
        words = anchor_words.get(page, [])
        if words:
            avg_len = sum(len(w) for w in words) / len(words)
            print(f"  {page} ({plant_names[page]:>10}): avg_word_len={avg_len:.2f}, intensity={galenic_intensity[page]}")

    avg_lens = [sum(len(w) for w in anchor_words.get(p, [])) / (len(anchor_words.get(p, [])) or 1) for p in anchor_pages]
    ints = [galenic_intensity[p] for p in anchor_pages]
    r = spearman_corr(ints, avg_lens)
    print(f"\n  Spearman(intensity, word_length): rho={r:+.4f}")
    print(f"  {'SUPPORTS' if abs(r) > 0.5 else 'DOES NOT SUPPORT'} word-length encoding complexity")

    # ============================================================
    # SYNTHESIS
    # ============================================================
    print("\n" + "=" * 70)
    print("SYNTHESIS: OVERALL ASSESSMENT")
    print("=" * 70)

    # Count supporting vs contradicting tests
    supports = 0
    contradicts = 0

    # Test 1: Administration route
    if il_sim_j > between_j:
        supports += 1
        print("  Test 1 (Admin Route):      SUPPORTS  (within > between)")
    else:
        contradicts += 1
        print("  Test 1 (Admin Route):      CONTRADICTS")

    # Test 2: Galenic quality
    if hot_cold_signal > 0:
        supports += 1
        print("  Test 2 (Galenic Quality):  SUPPORTS  (hot-cold separation)")
    else:
        contradicts += 1
        print("  Test 2 (Galenic Quality):  CONTRADICTS")

    # Test 3: Body system
    if avg_match > avg_non_match:
        supports += 1
        print("  Test 3 (Body System):      SUPPORTS  (matching > non-matching)")
    else:
        contradicts += 1
        print("  Test 3 (Body System):      CONTRADICTS")

    # Test 4: Preparation method
    if dec_sim_j > dec_vs_other_j:
        supports += 1
        print("  Test 4 (Preparation):      SUPPORTS  (decoction group cohesive)")
    else:
        contradicts += 1
        print("  Test 4 (Preparation):      CONTRADICTS")

    # Test 5: sh- morpheme
    if rho > 0.3:
        supports += 1
        print(f"  Test 5 (sh- intensity):    SUPPORTS  (rho={rho:.3f})")
    else:
        contradicts += 1
        print(f"  Test 5 (sh- intensity):    CONTRADICTS (rho={rho:.3f})")

    print(f"\n  Score: {supports}/5 tests support pharmaceutical encoding")
    print(f"  Verdict: {'PROMISING - warrants deeper investigation' if supports >= 3 else 'INCONCLUSIVE' if supports >= 2 else 'DOES NOT SUPPORT pharmaceutical encoding'}")

    return results


if __name__ == '__main__':
    results = main()
