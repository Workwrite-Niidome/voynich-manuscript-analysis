"""
Sandhi Cross-Validation for the Voynich Manuscript
===================================================
Tests whether n/l/r word-final suffix distributions are conditioned
by the next word's initial character, using rigorous cross-validation.
"""

import re
import random
import numpy as np
from collections import defaultdict, Counter
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

random.seed(42)
np.random.seed(42)

# ── 1. Parse the transcription ───────────────────────────────────────

def parse_transcription(filepath):
    """Parse EVA transcription into folio -> list of (word_pairs) structure."""
    folios = {}  # folio_id -> list of lines of words
    current_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Folio header
            folio_match = re.match(r'^<(f\d+[rv]\d*)>\s', line)
            if folio_match:
                current_folio = folio_match.group(1)
                if current_folio not in folios:
                    folios[current_folio] = []
                continue

            # Text line
            text_match = re.match(r'^<(f\d+[rv]\d*)\.\d+', line)
            if text_match:
                current_folio = text_match.group(1)
                if current_folio not in folios:
                    folios[current_folio] = []

                # Extract text after the tag
                text_part = re.sub(r'^<[^>]+>\s*', '', line)
                # Remove inline comments and special markers
                text_part = re.sub(r'\{[^}]*\}', '', text_part)  # {ct} etc
                text_part = re.sub(r'@\d+;?', '', text_part)     # @221; etc
                text_part = re.sub(r'[<>\[\]!?*,\']', '', text_part)  # punctuation/markup
                text_part = re.sub(r'-', ' ', text_part)          # line breaks -> space

                # Split into words
                words = [w.strip() for w in text_part.split('.') if w.strip()]
                # Also split on spaces (from line-break markers)
                expanded = []
                for w in words:
                    expanded.extend([x for x in w.split() if x])

                # Filter: only keep words that are purely EVA characters
                clean_words = []
                for w in expanded:
                    w = re.sub(r'[^a-z]', '', w)
                    if len(w) >= 2:  # at least 2 chars
                        clean_words.append(w)

                folios[current_folio].append(clean_words)

    return folios


def extract_word_pairs(folios, folio_ids):
    """Extract consecutive word pairs from specified folios."""
    pairs = []
    for fid in folio_ids:
        if fid not in folios:
            continue
        for line_words in folios[fid]:
            for i in range(len(line_words) - 1):
                w1 = line_words[i]
                w2 = line_words[i + 1]
                if w1 and w2:
                    pairs.append((w1, w2))
    return pairs


def extract_within_word_transitions(folios, folio_ids):
    """Extract within-word character transitions (for control test)."""
    transitions = []
    for fid in folio_ids:
        if fid not in folios:
            continue
        for line_words in folios[fid]:
            for w in line_words:
                if len(w) >= 3:
                    for i in range(len(w) - 1):
                        transitions.append((w[i], w[i+1]))
    return transitions


# ── 2. Sandhi analysis functions ─────────────────────────────────────

SUFFIXES = ['n', 'l', 'r']

def compute_sandhi_table(pairs):
    """
    For each next-word initial character, compute P(suffix | next_initial).
    Only considers words ending in n, l, or r.
    Returns: {initial_char: {suffix: count}} and {initial_char: {suffix: probability}}
    """
    counts = defaultdict(lambda: Counter())

    for w1, w2 in pairs:
        last_char = w1[-1]
        if last_char in SUFFIXES:
            first_char = w2[0]
            counts[first_char][last_char] += 1

    probs = {}
    for init_char, suffix_counts in counts.items():
        total = sum(suffix_counts.values())
        if total >= 5:  # minimum threshold
            probs[init_char] = {s: suffix_counts[s] / total for s in SUFFIXES}

    return counts, probs


def get_strongest_triggers(probs):
    """For each initial char, find which suffix is most likely."""
    triggers = {}
    for init_char, p in probs.items():
        best_suffix = max(p, key=p.get)
        triggers[init_char] = (best_suffix, p[best_suffix])
    return triggers


def predict_accuracy(train_probs, test_pairs):
    """
    Given trained probabilities, predict suffix for each test pair
    and measure accuracy.
    """
    correct = 0
    total = 0

    for w1, w2 in test_pairs:
        last_char = w1[-1]
        if last_char not in SUFFIXES:
            continue
        first_char = w2[0]
        if first_char not in train_probs:
            continue

        predicted = max(train_probs[first_char], key=train_probs[first_char].get)
        if predicted == last_char:
            correct += 1
        total += 1

    return correct / total if total > 0 else 0, total


def compute_baseline_accuracy(pairs):
    """Baseline: always predict the most common suffix overall."""
    suffix_counts = Counter()
    for w1, w2 in pairs:
        if w1[-1] in SUFFIXES:
            suffix_counts[w1[-1]] += 1

    if not suffix_counts:
        return 0
    most_common = suffix_counts.most_common(1)[0][0]
    total = sum(suffix_counts.values())
    return suffix_counts[most_common] / total


def correlation_between_splits(probs_a, probs_b):
    """Compute correlation of suffix probabilities between two splits."""
    common_chars = set(probs_a.keys()) & set(probs_b.keys())
    if len(common_chars) < 3:
        return float('nan'), float('nan'), len(common_chars)

    vals_a = []
    vals_b = []
    for ch in sorted(common_chars):
        for s in SUFFIXES:
            vals_a.append(probs_a[ch].get(s, 0))
            vals_b.append(probs_b[ch].get(s, 0))

    r, p = stats.pearsonr(vals_a, vals_b)
    return r, p, len(common_chars)


# ── 3. Within-word control analysis ─────────────────────────────────

def compute_within_word_sandhi(folios, folio_ids):
    """
    Control test: look at within-word transitions.
    For chars at position i that are n/l/r, check distribution
    conditioned on char at position i+1.
    """
    counts = defaultdict(lambda: Counter())

    for fid in folio_ids:
        if fid not in folios:
            continue
        for line_words in folios[fid]:
            for w in line_words:
                if len(w) < 3:
                    continue
                # Look at internal positions (not the last char)
                for i in range(len(w) - 2):  # exclude last char
                    ch = w[i]
                    next_ch = w[i + 1]
                    if ch in SUFFIXES:
                        counts[next_ch][ch] += 1

    probs = {}
    for next_char, suffix_counts in counts.items():
        total = sum(suffix_counts.values())
        if total >= 5:
            probs[next_char] = {s: suffix_counts[s] / total for s in SUFFIXES}

    return counts, probs


# ── 4. Main cross-validation ────────────────────────────────────────

def main():
    filepath = r"C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt"
    folios = parse_transcription(filepath)

    all_folio_ids = sorted(folios.keys())
    print(f"Total folios parsed: {len(all_folio_ids)}")

    # Count total word pairs
    all_pairs = extract_word_pairs(folios, all_folio_ids)
    print(f"Total word pairs: {len(all_pairs)}")

    nlr_pairs = [(w1, w2) for w1, w2 in all_pairs if w1[-1] in SUFFIXES]
    print(f"Word pairs ending in n/l/r: {len(nlr_pairs)}")

    # Overall suffix distribution
    suffix_dist = Counter(w1[-1] for w1, w2 in nlr_pairs)
    total_nlr = sum(suffix_dist.values())
    print(f"\nOverall suffix distribution:")
    for s in SUFFIXES:
        print(f"  {s}: {suffix_dist[s]} ({suffix_dist[s]/total_nlr*100:.1f}%)")

    baseline = compute_baseline_accuracy(all_pairs)
    print(f"\nBaseline accuracy (majority class): {baseline:.4f}")

    # Determine section for stratification
    def get_section(fid):
        """Rough section assignment based on folio number."""
        num = re.search(r'f(\d+)', fid)
        if num:
            n = int(num.group(1))
            if n <= 11: return 'A'  # Herbal A
            elif n <= 25: return 'B'  # Herbal B
            elif n <= 56: return 'C'  # Pharmaceutical/Balneo
            elif n <= 84: return 'D'  # Astrological
            elif n <= 102: return 'E'  # Biological
            else: return 'F'  # Stars/Recipes
        return 'X'

    sections = defaultdict(list)
    for fid in all_folio_ids:
        sections[get_section(fid)].append(fid)

    print(f"\nSections: {dict((k, len(v)) for k, v in sections.items())}")

    results = {}

    # ════════════════════════════════════════════════════════════════
    # TEST 1: 50/50 split cross-validation
    # ════════════════════════════════════════════════════════════════
    print("\n" + "="*70)
    print("TEST 1: 50/50 SPLIT CROSS-VALIDATION")
    print("="*70)

    # Stratified random split
    set_a = []
    set_b = []
    for sec, fids in sections.items():
        shuffled = list(fids)
        random.shuffle(shuffled)
        mid = len(shuffled) // 2
        set_a.extend(shuffled[:mid])
        set_b.extend(shuffled[mid:])

    pairs_a = extract_word_pairs(folios, set_a)
    pairs_b = extract_word_pairs(folios, set_b)

    print(f"\nSet A: {len(set_a)} folios, {len(pairs_a)} word pairs")
    print(f"Set B: {len(set_b)} folios, {len(pairs_b)} word pairs")

    # Train on A, test on B
    _, probs_a = compute_sandhi_table(pairs_a)
    _, probs_b = compute_sandhi_table(pairs_b)

    triggers_a = get_strongest_triggers(probs_a)
    triggers_b = get_strongest_triggers(probs_b)

    acc_ab, n_ab = predict_accuracy(probs_a, pairs_b)
    acc_ba, n_ba = predict_accuracy(probs_b, pairs_a)

    print(f"\nTrain A -> Test B: accuracy = {acc_ab:.4f} (n={n_ab})")
    print(f"Train B -> Test A: accuracy = {acc_ba:.4f} (n={n_ba})")
    print(f"Average: {(acc_ab + acc_ba)/2:.4f}")
    print(f"Baseline (majority): {baseline:.4f}")
    print(f"Lift over baseline: {((acc_ab+acc_ba)/2 - baseline)*100:.2f} pp")

    # Correlation
    r, p, n_common = correlation_between_splits(probs_a, probs_b)
    print(f"\nCorrelation between Set A and Set B probabilities:")
    print(f"  Pearson r = {r:.4f}, p = {p:.2e}, common initials = {n_common}")

    # Trigger agreement
    common_triggers = set(triggers_a.keys()) & set(triggers_b.keys())
    agree = sum(1 for ch in common_triggers if triggers_a[ch][0] == triggers_b[ch][0])
    print(f"\nStrongest trigger agreement:")
    print(f"  Common initial chars: {len(common_triggers)}")
    print(f"  Same strongest suffix: {agree}/{len(common_triggers)} ({agree/len(common_triggers)*100:.1f}%)")

    print(f"\n  Detailed trigger comparison (top initials):")
    print(f"  {'Init':<6} {'Set A best':<12} {'P(A)':<8} {'Set B best':<12} {'P(B)':<8} {'Match'}")
    for ch in sorted(common_triggers):
        sa, pa = triggers_a[ch]
        sb, pb = triggers_b[ch]
        match = "YES" if sa == sb else "NO"
        print(f"  {ch:<6} {sa:<12} {pa:<8.3f} {sb:<12} {pb:<8.3f} {match}")

    results['split_50_50'] = {
        'acc_ab': acc_ab, 'acc_ba': acc_ba,
        'avg': (acc_ab+acc_ba)/2,
        'correlation_r': r, 'correlation_p': p,
        'trigger_agreement': agree/len(common_triggers) if common_triggers else 0
    }

    # ════════════════════════════════════════════════════════════════
    # TEST 2: Permutation test (1000 shuffles)
    # ════════════════════════════════════════════════════════════════
    print("\n" + "="*70)
    print("TEST 2: PERMUTATION TEST (1000 shuffles)")
    print("="*70)

    # Real accuracy (average of both directions)
    real_acc = (acc_ab + acc_ba) / 2

    # Shuffle suffixes and measure accuracy
    n_perms = 1000
    perm_accs = []

    # Collect all pairs that end in n/l/r for permutation
    all_nlr_suffixes = [w1[-1] for w1, w2 in all_pairs if w1[-1] in SUFFIXES]

    for perm_i in range(n_perms):
        # Shuffle suffix assignments across ALL pairs
        shuffled_suffixes = list(all_nlr_suffixes)
        random.shuffle(shuffled_suffixes)

        # Rebuild pairs with shuffled suffixes
        idx = 0
        pairs_a_shuf = []
        for w1, w2 in pairs_a:
            if w1[-1] in SUFFIXES:
                if idx < len(shuffled_suffixes):
                    new_w1 = w1[:-1] + shuffled_suffixes[idx]
                    pairs_a_shuf.append((new_w1, w2))
                    idx += 1
                else:
                    pairs_a_shuf.append((w1, w2))
            else:
                pairs_a_shuf.append((w1, w2))

        pairs_b_shuf = []
        for w1, w2 in pairs_b:
            if w1[-1] in SUFFIXES:
                if idx < len(shuffled_suffixes):
                    new_w1 = w1[:-1] + shuffled_suffixes[idx]
                    pairs_b_shuf.append((new_w1, w2))
                    idx += 1
                else:
                    pairs_b_shuf.append((w1, w2))
            else:
                pairs_b_shuf.append((w1, w2))

        _, probs_a_s = compute_sandhi_table(pairs_a_shuf)
        _, probs_b_s = compute_sandhi_table(pairs_b_shuf)

        acc1, _ = predict_accuracy(probs_a_s, pairs_b_shuf)
        acc2, _ = predict_accuracy(probs_b_s, pairs_a_shuf)
        perm_accs.append((acc1 + acc2) / 2)

    perm_accs = np.array(perm_accs)
    p_value = np.mean(perm_accs >= real_acc)

    print(f"\nReal cross-validated accuracy: {real_acc:.4f}")
    print(f"Permutation mean accuracy: {np.mean(perm_accs):.4f} +/- {np.std(perm_accs):.4f}")
    print(f"Permutation 95th percentile: {np.percentile(perm_accs, 95):.4f}")
    print(f"Permutation 99th percentile: {np.percentile(perm_accs, 99):.4f}")
    print(f"Permutation max: {np.max(perm_accs):.4f}")
    print(f"p-value (real >= permuted): {p_value:.4f}")
    print(f"Times permutation beat real: {np.sum(perm_accs >= real_acc)}/{n_perms}")

    results['permutation'] = {
        'real_acc': real_acc,
        'perm_mean': float(np.mean(perm_accs)),
        'perm_std': float(np.std(perm_accs)),
        'perm_95': float(np.percentile(perm_accs, 95)),
        'p_value': float(p_value)
    }

    # ════════════════════════════════════════════════════════════════
    # TEST 3: 10-fold cross-validation
    # ════════════════════════════════════════════════════════════════
    print("\n" + "="*70)
    print("TEST 3: 10-FOLD CROSS-VALIDATION")
    print("="*70)

    # Shuffle all folios and split into 10 folds
    all_shuffled = list(all_folio_ids)
    random.shuffle(all_shuffled)

    k = 10
    fold_size = len(all_shuffled) // k
    folds = []
    for i in range(k):
        start = i * fold_size
        end = start + fold_size if i < k - 1 else len(all_shuffled)
        folds.append(all_shuffled[start:end])

    fold_accs = []
    fold_correlations = []
    fold_trigger_agreements = []

    for i in range(k):
        test_fids = folds[i]
        train_fids = [fid for j in range(k) for fid in folds[j] if j != i]

        train_pairs = extract_word_pairs(folios, train_fids)
        test_pairs = extract_word_pairs(folios, test_fids)

        _, train_probs = compute_sandhi_table(train_pairs)
        _, test_probs = compute_sandhi_table(test_pairs)

        acc, n_test = predict_accuracy(train_probs, test_pairs)
        fold_accs.append(acc)

        r_fold, _, n_com = correlation_between_splits(train_probs, test_probs)
        fold_correlations.append(r_fold)

        # Trigger agreement
        tr_train = get_strongest_triggers(train_probs)
        tr_test = get_strongest_triggers(test_probs)
        common = set(tr_train.keys()) & set(tr_test.keys())
        if common:
            ag = sum(1 for c in common if tr_train[c][0] == tr_test[c][0]) / len(common)
        else:
            ag = 0
        fold_trigger_agreements.append(ag)

        print(f"  Fold {i+1}: acc={acc:.4f}, r={r_fold:.4f}, trigger_agree={ag:.3f} (n_test={n_test})")

    mean_acc = np.mean(fold_accs)
    std_acc = np.std(fold_accs)
    mean_r = np.nanmean(fold_correlations)
    mean_ta = np.mean(fold_trigger_agreements)

    print(f"\n10-fold CV accuracy: {mean_acc:.4f} +/- {std_acc:.4f}")
    print(f"10-fold CV correlation: {mean_r:.4f}")
    print(f"10-fold CV trigger agreement: {mean_ta:.4f}")
    print(f"Baseline (majority): {baseline:.4f}")
    print(f"Lift: {(mean_acc - baseline)*100:.2f} pp")

    results['cv_10fold'] = {
        'mean_acc': float(mean_acc),
        'std_acc': float(std_acc),
        'mean_correlation': float(mean_r),
        'mean_trigger_agreement': float(mean_ta),
        'fold_accs': [float(x) for x in fold_accs]
    }

    # ════════════════════════════════════════════════════════════════
    # TEST 4: CONTROL -- Within-word transitions
    # ════════════════════════════════════════════════════════════════
    print("\n" + "="*70)
    print("TEST 4: CONTROL -- WITHIN-WORD vs BETWEEN-WORD TRANSITIONS")
    print("="*70)

    # Between-word analysis (already done, use full data)
    _, between_probs = compute_sandhi_table(all_pairs)

    # Within-word analysis
    _, within_probs = compute_within_word_sandhi(folios, all_folio_ids)

    # Measure entropy (lower = more predictable = stronger conditioning)
    def mean_entropy(probs_dict):
        entropies = []
        for ch, p in probs_dict.items():
            vals = [p.get(s, 0.001) for s in SUFFIXES]
            total = sum(vals)
            vals = [v/total for v in vals]
            ent = -sum(v * np.log2(v) for v in vals if v > 0)
            entropies.append(ent)
        return np.mean(entropies) if entropies else 0

    between_entropy = mean_entropy(between_probs)
    within_entropy = mean_entropy(within_probs)

    # Maximum possible entropy for 3 categories
    max_entropy = np.log2(3)

    print(f"\nMean conditional entropy (lower = more predictive):")
    print(f"  Between-word (sandhi): {between_entropy:.4f}")
    print(f"  Within-word (control): {within_entropy:.4f}")
    print(f"  Maximum possible:      {max_entropy:.4f}")
    print(f"  Entropy reduction (between vs max): {(1 - between_entropy/max_entropy)*100:.1f}%")
    print(f"  Entropy reduction (within vs max):  {(1 - within_entropy/max_entropy)*100:.1f}%")

    # Cross-validate within-word too
    within_fold_accs = []
    for i in range(k):
        test_fids = folds[i]
        train_fids = [fid for j in range(k) for fid in folds[j] if j != i]

        _, train_within = compute_within_word_sandhi(folios, train_fids)

        # For within-word, "predict" the n/l/r at internal positions
        test_transitions = extract_within_word_transitions(folios, test_fids)
        correct = 0
        total = 0
        for ch, next_ch in test_transitions:
            if ch not in SUFFIXES:
                continue
            if next_ch not in train_within:
                continue
            predicted = max(train_within[next_ch], key=train_within[next_ch].get)
            if predicted == ch:
                correct += 1
            total += 1

        acc = correct / total if total > 0 else 0
        within_fold_accs.append(acc)

    within_mean = np.mean(within_fold_accs)
    within_std = np.std(within_fold_accs)

    # Also compute within-word baseline
    all_within = extract_within_word_transitions(folios, all_folio_ids)
    within_suffix_counts = Counter(ch for ch, _ in all_within if ch in SUFFIXES)
    within_total = sum(within_suffix_counts.values())
    within_baseline = max(within_suffix_counts.values()) / within_total if within_total > 0 else 0

    print(f"\nWithin-word 10-fold CV accuracy: {within_mean:.4f} +/- {within_std:.4f}")
    print(f"Within-word baseline (majority): {within_baseline:.4f}")
    print(f"Within-word lift: {(within_mean - within_baseline)*100:.2f} pp")
    print(f"\nBetween-word 10-fold CV accuracy: {mean_acc:.4f} +/- {std_acc:.4f}")
    print(f"Between-word baseline (majority): {baseline:.4f}")
    print(f"Between-word lift: {(mean_acc - baseline)*100:.2f} pp")

    if mean_acc - baseline > within_mean - within_baseline + 0.02:
        control_verdict = "Between-word shows STRONGER conditioning than within-word -- consistent with sandhi"
    elif abs((mean_acc - baseline) - (within_mean - within_baseline)) <= 0.02:
        control_verdict = "Between-word and within-word show SIMILAR conditioning -- could be transcription artifact"
    else:
        control_verdict = "Within-word shows STRONGER conditioning -- likely NOT sandhi, possibly transcription artifact"

    print(f"\nControl test verdict: {control_verdict}")

    results['control'] = {
        'between_entropy': float(between_entropy),
        'within_entropy': float(within_entropy),
        'between_cv_acc': float(mean_acc),
        'within_cv_acc': float(within_mean),
        'between_lift': float(mean_acc - baseline),
        'within_lift': float(within_mean - within_baseline),
        'verdict': control_verdict
    }

    # ════════════════════════════════════════════════════════════════
    # TEST 5: Effect size -- Cramer's V
    # ════════════════════════════════════════════════════════════════
    print("\n" + "="*70)
    print("TEST 5: EFFECT SIZE -- Cramer's V (suffix x next_initial)")
    print("="*70)

    # Build contingency table: suffix (n/l/r) x next_initial (top chars)
    between_counts, _ = compute_sandhi_table(all_pairs)

    # Get top initial chars by frequency
    init_totals = {ch: sum(c.values()) for ch, c in between_counts.items() if sum(c.values()) >= 10}
    top_initials = sorted(init_totals, key=init_totals.get, reverse=True)[:15]

    # Build contingency table
    table = []
    for s in SUFFIXES:
        row = []
        for ch in top_initials:
            row.append(between_counts[ch].get(s, 0))
        table.append(row)

    table = np.array(table)
    chi2, p_chi, dof, expected = stats.chi2_contingency(table)
    n_total = table.sum()
    k_min = min(table.shape) - 1
    cramers_v = np.sqrt(chi2 / (n_total * k_min)) if n_total * k_min > 0 else 0

    print(f"\nContingency table: {len(SUFFIXES)} suffixes x {len(top_initials)} initial chars")
    print(f"Chi-squared = {chi2:.2f}, df = {dof}, p = {p_chi:.2e}")
    print(f"Cramer's V = {cramers_v:.4f}")

    if cramers_v < 0.1:
        effect_label = "negligible"
    elif cramers_v < 0.3:
        effect_label = "small"
    elif cramers_v < 0.5:
        effect_label = "medium"
    else:
        effect_label = "large"
    print(f"Effect size: {effect_label}")

    results['effect_size'] = {
        'chi2': float(chi2),
        'p_value': float(p_chi),
        'cramers_v': float(cramers_v),
        'effect_label': effect_label
    }

    # ════════════════════════════════════════════════════════════════
    # FINAL VERDICT
    # ════════════════════════════════════════════════════════════════
    print("\n" + "="*70)
    print("FINAL VERDICT")
    print("="*70)

    # Criteria for "survives":
    # 1. CV accuracy significantly above baseline
    # 2. Permutation p < 0.05
    # 3. Correlation across splits > 0.5
    # 4. Between-word conditioning stronger than within-word

    cv_pass = mean_acc > baseline + 0.02
    perm_pass = results['permutation']['p_value'] < 0.05
    corr_pass = results['split_50_50']['correlation_r'] > 0.5
    control_pass = (mean_acc - baseline) > (within_mean - within_baseline)

    print(f"\n  1. CV accuracy above baseline (+2pp)?     {'PASS' if cv_pass else 'FAIL'} (lift = {(mean_acc-baseline)*100:.2f}pp)")
    print(f"  2. Permutation test p < 0.05?             {'PASS' if perm_pass else 'FAIL'} (p = {results['permutation']['p_value']:.4f})")
    print(f"  3. Cross-split correlation > 0.5?         {'PASS' if corr_pass else 'FAIL'} (r = {results['split_50_50']['correlation_r']:.4f})")
    print(f"  4. Between > within-word conditioning?    {'PASS' if control_pass else 'FAIL'}")
    print(f"  5. Effect size:                           {effect_label} (V = {cramers_v:.4f})")

    n_pass = sum([cv_pass, perm_pass, corr_pass, control_pass])

    if n_pass == 4 and cramers_v >= 0.3:
        verdict = "STRONG SUPPORT -- Sandhi hypothesis survives rigorous cross-validation"
    elif n_pass >= 3:
        verdict = "MODERATE SUPPORT -- Pattern replicates but with caveats"
    elif n_pass >= 2:
        verdict = "WEAK SUPPORT -- Some replication but not fully convincing"
    else:
        verdict = "REJECTED -- Pattern does not replicate; likely overfitting"

    print(f"\n  OVERALL: {verdict}")

    results['verdict'] = verdict
    results['n_pass'] = n_pass

    return results


if __name__ == '__main__':
    results = main()
