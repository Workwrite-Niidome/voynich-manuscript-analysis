"""
Voynich Manuscript Word Structure Reverse Engineering
Treats each word as a multi-digit code number and analyzes positional independence.
"""
import re
import math
import json
from collections import Counter, defaultdict
import numpy as np

def load_words(filepath):
    """Extract clean EVA words from transcription."""
    words = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Skip headers and metadata
            if line.startswith('#') or line.startswith('<f') and '>' not in line:
                continue
            # Extract text after the tag
            m = re.match(r'<[^>]+>\s*(.*)', line)
            if not m:
                continue
            text = m.group(1)
            # Remove comments and annotations
            text = re.sub(r'\{[^}]*\}', '', text)  # remove {ct} etc
            text = re.sub(r'@\d+;?', '', text)  # remove @221 etc
            text = re.sub(r"[',\?\.\-<>!\*]", ' ', text)  # remove punctuation
            # Split into words
            for w in text.split():
                w = w.strip()
                if w and len(w) >= 2 and re.match(r'^[a-z]+$', w):
                    words.append(w)
    return words

def positional_character_analysis(words, max_pos=10):
    """For each character position, compute which characters appear and their frequency."""
    pos_chars = defaultdict(Counter)
    pos_total = Counter()

    for w in words:
        for i, ch in enumerate(w):
            if i < max_pos:
                pos_chars[i][ch] += 1
                pos_total[i] += 1

    results = {}
    for pos in sorted(pos_chars.keys()):
        total = pos_total[pos]
        chars = pos_chars[pos]
        sorted_chars = sorted(chars.items(), key=lambda x: -x[1])
        entropy = -sum((c/total) * math.log2(c/total) for _, c in sorted_chars if c > 0)
        results[pos] = {
            'total_words': total,
            'unique_chars': len(chars),
            'entropy': entropy,
            'distribution': sorted_chars
        }
    return results

def compute_mutual_information(words, max_pos=8):
    """Compute MI(position_i, position_j) for all pairs."""
    max_len = min(max_pos, max(len(w) for w in words))

    # Build joint and marginal distributions
    pos_chars = defaultdict(Counter)
    joint_chars = defaultdict(Counter)

    for w in words:
        for i in range(min(len(w), max_len)):
            pos_chars[i][w[i]] += 1
            for j in range(i+1, min(len(w), max_len)):
                joint_chars[(i,j)][(w[i], w[j])] += 1

    mi_matrix = np.zeros((max_len, max_len))

    for i in range(max_len):
        for j in range(i+1, max_len):
            # Only use words that have both positions
            relevant = [w for w in words if len(w) > max(i, j)]
            if len(relevant) < 50:
                continue

            n = len(relevant)
            pi = Counter(w[i] for w in relevant)
            pj = Counter(w[j] for w in relevant)
            pij = Counter((w[i], w[j]) for w in relevant)

            mi = 0.0
            for (ci, cj), count in pij.items():
                p_ij = count / n
                p_i = pi[ci] / n
                p_j = pj[cj] / n
                if p_ij > 0 and p_i > 0 and p_j > 0:
                    mi += p_ij * math.log2(p_ij / (p_i * p_j))

            mi_matrix[i][j] = mi
            mi_matrix[j][i] = mi

    return mi_matrix, max_len

def normalized_mutual_information(words, max_pos=8):
    """Compute NMI = MI / min(H(i), H(j)) for better comparison."""
    max_len = min(max_pos, max(len(w) for w in words))

    mi_matrix = np.zeros((max_len, max_len))
    nmi_matrix = np.zeros((max_len, max_len))

    for i in range(max_len):
        for j in range(i+1, max_len):
            relevant = [w for w in words if len(w) > max(i, j)]
            if len(relevant) < 50:
                continue

            n = len(relevant)
            pi = Counter(w[i] for w in relevant)
            pj = Counter(w[j] for w in relevant)
            pij = Counter((w[i], w[j]) for w in relevant)

            hi = -sum((c/n) * math.log2(c/n) for c in pi.values() if c > 0)
            hj = -sum((c/n) * math.log2(c/n) for c in pj.values() if c > 0)

            mi = 0.0
            for (ci, cj), count in pij.items():
                p_ij = count / n
                p_i = pi[ci] / n
                p_j = pj[cj] / n
                if p_ij > 0 and p_i > 0 and p_j > 0:
                    mi += p_ij * math.log2(p_ij / (p_i * p_j))

            mi_matrix[i][j] = mi
            mi_matrix[j][i] = mi

            min_h = min(hi, hj) if min(hi, hj) > 0 else 1
            nmi_matrix[i][j] = mi / min_h
            nmi_matrix[j][i] = mi / min_h

    return mi_matrix, nmi_matrix, max_len

def length_distribution(words):
    """Word length distribution."""
    lengths = Counter(len(w) for w in words)
    return dict(sorted(lengths.items()))

def code_table_reconstruction(words, max_pos=8):
    """For each position, what are the possible values and how many?"""
    # Group by word length
    by_length = defaultdict(list)
    for w in words:
        by_length[len(w)].append(w)

    tables = {}
    for length in sorted(by_length.keys()):
        if length > max_pos or len(by_length[length]) < 20:
            continue
        wlist = by_length[length]
        table = {}
        for pos in range(length):
            chars = Counter(w[pos] for w in wlist)
            table[pos] = {
                'unique_values': len(chars),
                'distribution': sorted(chars.items(), key=lambda x: -x[1])
            }
        tables[length] = {
            'word_count': len(wlist),
            'positions': table
        }
    return tables

def substitution_test(words):
    """Test what happens when you change one position at a time.
    For common words, find all words that differ by exactly one position."""
    word_set = set(words)
    word_freq = Counter(words)

    # Focus on frequent words
    common = [w for w, c in word_freq.most_common(50)]

    results = {}
    for w in common:
        neighbors = defaultdict(list)
        for w2 in word_set:
            if len(w2) == len(w) and w2 != w:
                diffs = [(i, w[i], w2[i]) for i in range(len(w)) if w[i] != w2[i]]
                if len(diffs) == 1:
                    pos, old_ch, new_ch = diffs[0]
                    neighbors[pos].append({
                        'word': w2,
                        'freq': word_freq[w2],
                        'change': f'{old_ch}->{new_ch}'
                    })
        if neighbors:
            results[w] = {
                'freq': word_freq[w],
                'neighbors': {str(k): v for k, v in neighbors.items()}
            }
    return results

def compare_with_natural_languages():
    """Generate reference MI values for natural languages."""
    # English reference text (pharmaceutical terms)
    english_words = [
        "leaf", "root", "bark", "seed", "stem", "herb", "drug", "dose",
        "cold", "warm", "moist", "damp", "heat", "fire", "wind", "rain",
        "chop", "boil", "burn", "cook", "wash", "pour", "soak", "brew",
        "part", "half", "much", "less", "more", "full", "void", "some",
        "head", "hand", "foot", "back", "face", "skin", "bone", "vein",
        "take", "give", "make", "bind", "cure", "heal", "harm", "pain"
    ]
    # Expand by repetition with variations
    expanded = english_words * 20

    mi_eng, nmi_eng, max_len_eng = normalized_mutual_information(expanded, 4)
    return nmi_eng, max_len_eng

def bigram_vs_position_analysis(words):
    """Compare character bigram frequencies with positional predictions.
    If positions are independent, P(c2|c1,pos) should equal P(c2|pos)."""
    max_pos = 6

    # For each position pair (i, i+1), compute conditional entropy
    results = {}
    for pos in range(max_pos - 1):
        relevant = [w for w in words if len(w) > pos + 1]
        if len(relevant) < 100:
            continue

        n = len(relevant)

        # H(pos+1 | pos) - conditional entropy
        joint = Counter((w[pos], w[pos+1]) for w in relevant)
        marginal = Counter(w[pos] for w in relevant)

        h_cond = 0.0
        for (c1, c2), count in joint.items():
            p_joint = count / n
            p_c1 = marginal[c1] / n
            if p_joint > 0 and p_c1 > 0:
                h_cond -= p_joint * math.log2(p_joint / p_c1)

        # H(pos+1) - marginal entropy
        marginal2 = Counter(w[pos+1] for w in relevant)
        h_marginal = -sum((c/n) * math.log2(c/n) for c in marginal2.values() if c > 0)

        # If independent, H(pos+1|pos) should be close to H(pos+1)
        independence_ratio = h_cond / h_marginal if h_marginal > 0 else 0

        results[pos] = {
            'H_next': round(h_marginal, 4),
            'H_next_given_current': round(h_cond, 4),
            'independence_ratio': round(independence_ratio, 4),
            'sample_size': n
        }

    return results

def pharmaceutical_dimension_mapping(code_tables):
    """Map positional value counts to pharmaceutical dimensions."""
    pharma_dims = {
        'plant_identity': '50-200+ (large inventory)',
        'plant_part': '5-8 (leaf/root/flower/bark/seed/fruit/resin/whole)',
        'preparation': '6-10 (raw/dried/boiled/ground/distilled/infused/soaked/calcined)',
        'galenic_quality': '4 (hot/cold/dry/moist)',
        'degree': '4 (1st/2nd/3rd/4th)',
        'dosage_form': '5-8 (powder/syrup/pill/plaster/ointment/decoction/electuary)',
        'application': '4-6 (internal/external/inhalation/topical/oral/rectal)',
        'quantity': '3-5 (small/medium/large or specific measures)',
    }
    return pharma_dims

def stem_suffix_analysis(words):
    """Analyze if words decompose into stem + suffix patterns."""
    # Common endings
    suffix_candidates = ['aiin', 'ain', 'iin', 'in', 'al', 'ol', 'ar', 'or',
                         'an', 'am', 'dy', 'ey', 'hy', 'chy', 'shy', 'ty',
                         'air', 'eey', 'ody', 'oly', 'ory']

    suffix_stats = {}
    for suf in suffix_candidates:
        matching = [w for w in words if w.endswith(suf) and len(w) > len(suf)]
        if len(matching) >= 5:
            stems = Counter(w[:-len(suf)] for w in matching)
            suffix_stats[suf] = {
                'count': len(matching),
                'unique_stems': len(stems),
                'top_stems': stems.most_common(10)
            }

    return dict(sorted(suffix_stats.items(), key=lambda x: -x[1]['count']))

def pca_like_analysis(words, max_pos=6):
    """Approximate PCA on character-by-position encoding.
    Use one-hot encoding per position, then compute covariance structure."""
    # Filter to words of a common length
    length_counts = Counter(len(w) for w in words)
    target_len = max(length_counts, key=length_counts.get)

    # Also analyze several common lengths
    results = {}
    for target_len in [3, 4, 5, 6, 7]:
        subset = [w for w in words if len(w) == target_len]
        if len(subset) < 30:
            continue

        # Build character vocabulary per position
        pos_vocab = {}
        for pos in range(target_len):
            chars = sorted(set(w[pos] for w in subset))
            pos_vocab[pos] = {ch: idx for idx, ch in enumerate(chars)}

        # One-hot encode
        total_features = sum(len(v) for v in pos_vocab.values())
        matrix = np.zeros((len(subset), total_features))

        offset = 0
        for pos in range(target_len):
            vocab = pos_vocab[pos]
            for i, w in enumerate(subset):
                matrix[i, offset + vocab[w[pos]]] = 1.0
            offset += len(vocab)

        # Compute correlation matrix and eigenvalues
        if matrix.shape[0] > matrix.shape[1]:
            cov = np.cov(matrix.T)
            eigenvalues = np.linalg.eigvalsh(cov)
            eigenvalues = sorted(eigenvalues, reverse=True)
            eigenvalues = [max(0, e) for e in eigenvalues]  # clip negatives
            total_var = sum(eigenvalues)
            if total_var > 0:
                cumulative = np.cumsum(eigenvalues) / total_var
                n_90 = int(np.searchsorted(cumulative, 0.90)) + 1
                n_95 = int(np.searchsorted(cumulative, 0.95)) + 1
            else:
                n_90 = n_95 = total_features

            results[target_len] = {
                'word_count': len(subset),
                'total_features': total_features,
                'chars_per_position': [len(pos_vocab[p]) for p in range(target_len)],
                'n_components_90pct': n_90,
                'n_components_95pct': n_95,
                'top_eigenvalues': [round(e, 4) for e in eigenvalues[:10]],
                'independence_score': n_90 / target_len  # ratio: if ~1.0, positions are independent
            }

    return results

def chol_family_analysis(words):
    """Deep analysis of 'chol' and related words."""
    word_freq = Counter(words)

    # All words containing 'chol'
    chol_words = {w: word_freq[w] for w in word_freq if 'chol' in w}

    # All 4-letter words starting with ch
    ch_4 = {w: word_freq[w] for w in word_freq if len(w) == 4 and w.startswith('ch')}

    # All words matching ?hol pattern
    xhol = {w: word_freq[w] for w in word_freq if len(w) == 4 and w[1:] == 'hol'}

    # All words matching ch?l pattern
    chxl = {w: word_freq[w] for w in word_freq if len(w) == 4 and w[:2] == 'ch' and w[3] == 'l'}

    # All words matching cho? pattern
    chox = {w: word_freq[w] for w in word_freq if len(w) == 4 and w[:3] == 'cho'}

    # All words matching ?ho? pattern (same nucleus)
    xhox = {w: word_freq[w] for w in word_freq if len(w) == 4 and w[1:3] == 'ho'}

    return {
        'chol_family': dict(sorted(chol_words.items(), key=lambda x: -x[1])),
        'ch__4letter': dict(sorted(ch_4.items(), key=lambda x: -x[1])),
        '_hol_pattern': dict(sorted(xhol.items(), key=lambda x: -x[1])),
        'ch_l_pattern': dict(sorted(chxl.items(), key=lambda x: -x[1])),
        'cho__pattern': dict(sorted(chox.items(), key=lambda x: -x[1])),
        '_ho__pattern': dict(sorted(xhox.items(), key=lambda x: -x[1])[:20]),
    }

def adjacent_position_independence_test(words):
    """For non-adjacent positions, test if they show MORE independence than adjacent ones.
    In natural languages, adjacent positions are highly correlated.
    In a code system, even adjacent positions might be independent."""
    max_pos = 7
    relevant = [w for w in words if len(w) >= max_pos]
    if len(relevant) < 100:
        relevant = [w for w in words if len(w) >= 5]
        max_pos = 5

    n = len(relevant)
    results = {}

    for i in range(max_pos):
        for j in range(i+1, max_pos):
            subset = [w for w in words if len(w) > max(i, j)]
            if len(subset) < 50:
                continue
            ns = len(subset)

            pi = Counter(w[i] for w in subset)
            pj = Counter(w[j] for w in subset)
            pij = Counter((w[i], w[j]) for w in subset)

            hi = -sum((c/ns)*math.log2(c/ns) for c in pi.values() if c > 0)
            hj = -sum((c/ns)*math.log2(c/ns) for c in pj.values() if c > 0)

            mi = 0.0
            for (ci, cj), count in pij.items():
                p_ij_val = count / ns
                p_i_val = pi[ci] / ns
                p_j_val = pj[cj] / ns
                if p_ij_val > 0 and p_i_val > 0 and p_j_val > 0:
                    mi += p_ij_val * math.log2(p_ij_val / (p_i_val * p_j_val))

            min_h = min(hi, hj) if min(hi, hj) > 0 else 1
            nmi = mi / min_h

            distance = j - i
            results[f'({i},{j})'] = {
                'distance': distance,
                'MI': round(mi, 4),
                'NMI': round(nmi, 4),
                'H_i': round(hi, 4),
                'H_j': round(hj, 4),
                'sample': ns
            }

    return results

def generate_english_comparison(max_pos=8):
    """Generate MI analysis for English pharmaceutical text for comparison."""
    # A more realistic English word list from a herbal/pharmaceutical context
    eng_words = """
    leaf root bark seed stem herb drug dose body part cold warm moist damp
    heat fire wind rain chop boil burn cook wash pour soak brew take give
    make bind cure heal harm pain head hand foot back face skin bone vein
    drop pill balm salve cream paste juice tonic broth syrup water honey
    blood heart lung liver spleen stomach bowel kidney brain nerve tooth
    fever cough wound swell sting bile gout flux worm rash itch sore boil
    dried fresh whole ground mixed clean sharp sweet sour salt bland pure
    first then next last much less more full half some none each both few
    apply drink rinse bathe inhale swallow chew crush steep grind press
    """.split()

    mi_results = {}
    for i in range(min(4, max_pos)):
        for j in range(i+1, min(5, max_pos)):
            subset = [w for w in eng_words if len(w) > max(i, j)]
            if len(subset) < 20:
                continue
            ns = len(subset)
            pi = Counter(w[i] for w in subset)
            pj = Counter(w[j] for w in subset)
            pij = Counter((w[i], w[j]) for w in subset)

            hi = -sum((c/ns)*math.log2(c/ns) for c in pi.values() if c > 0)
            hj = -sum((c/ns)*math.log2(c/ns) for c in pj.values() if c > 0)

            mi = 0.0
            for (ci, cj), count in pij.items():
                p_ij_val = count / ns
                p_i_val = pi[ci] / ns
                p_j_val = pj[cj] / ns
                if p_ij_val > 0 and p_i_val > 0 and p_j_val > 0:
                    mi += p_ij_val * math.log2(p_ij_val / (p_i_val * p_j_val))

            min_h = min(hi, hj) if min(hi, hj) > 0 else 1
            nmi = mi / min_h
            mi_results[f'({i},{j})'] = {'MI': round(mi, 4), 'NMI': round(nmi, 4)}

    return mi_results

def conditional_entropy_chain(words):
    """Compute H(pos_n | pos_1, pos_2, ..., pos_{n-1}) for increasing n.
    In a code: this should stay roughly constant (each position adds new info).
    In language: later positions become more predictable given earlier ones."""
    results = {}
    for target_len in [4, 5, 6]:
        subset = [w for w in words if len(w) == target_len]
        if len(subset) < 50:
            continue

        n = len(subset)
        chain = []

        for pos in range(target_len):
            if pos == 0:
                # H(pos_0)
                counts = Counter(w[0] for w in subset)
                h = -sum((c/n)*math.log2(c/n) for c in counts.values() if c > 0)
                chain.append(round(h, 4))
            else:
                # H(pos | all previous positions)
                # prefix = w[:pos], current = w[pos]
                joint = Counter((w[:pos], w[pos]) for w in subset)
                prefix_counts = Counter(w[:pos] for w in subset)

                h_cond = 0.0
                for (prefix, ch), count in joint.items():
                    p_joint = count / n
                    p_prefix = prefix_counts[prefix] / n
                    if p_joint > 0 and p_prefix > 0:
                        h_cond -= p_joint * math.log2(p_joint / p_prefix)

                chain.append(round(h_cond, 4))

        results[target_len] = {
            'conditional_entropies': chain,
            'total_entropy': round(sum(chain), 4),
            'entropy_per_position': [round(c, 4) for c in chain],
            'sample_size': n,
            'flatness': round(np.std(chain) / np.mean(chain), 4) if np.mean(chain) > 0 else 0
        }

    return results

# ============ MAIN ============
if __name__ == '__main__':
    filepath = r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt'
    words = load_words(filepath)

    print(f"Total words extracted: {len(words)}")
    print(f"Unique words: {len(set(words))}")
    print()

    # 1. Length distribution
    print("=" * 60)
    print("WORD LENGTH DISTRIBUTION")
    print("=" * 60)
    ldist = length_distribution(words)
    for length, count in ldist.items():
        pct = count / len(words) * 100
        print(f"  Length {length:2d}: {count:5d} words ({pct:5.1f}%) {'#' * int(pct)}")

    # 2. Positional character analysis
    print("\n" + "=" * 60)
    print("POSITIONAL CHARACTER ANALYSIS")
    print("=" * 60)
    pos_analysis = positional_character_analysis(words)
    for pos, data in pos_analysis.items():
        if data['total_words'] < 50:
            continue
        print(f"\n  Position {pos+1} (n={data['total_words']}):")
        print(f"    Unique chars: {data['unique_chars']}, Entropy: {data['entropy']:.3f} bits")
        top5 = data['distribution'][:8]
        dist_str = ', '.join(f"{ch}:{cnt}({cnt/data['total_words']*100:.1f}%)" for ch, cnt in top5)
        print(f"    Top: {dist_str}")

    # 3. Mutual Information Matrix
    print("\n" + "=" * 60)
    print("MUTUAL INFORMATION MATRIX (raw MI in bits)")
    print("=" * 60)
    mi_matrix, nmi_matrix, max_len = normalized_mutual_information(words)

    header = "     " + "  ".join(f"P{i+1:d}   " for i in range(max_len))
    print(header)
    for i in range(max_len):
        row = f"P{i+1:d}  "
        for j in range(max_len):
            if i == j:
                row += "  --- "
            else:
                row += f"{mi_matrix[i][j]:6.3f}"
        print(row)

    print("\nNORMALIZED MI (MI / min(H_i, H_j)):")
    for i in range(max_len):
        row = f"P{i+1:d}  "
        for j in range(max_len):
            if i == j:
                row += "  --- "
            else:
                row += f"{nmi_matrix[i][j]:6.3f}"
        print(row)

    # 4. Independence test by distance
    print("\n" + "=" * 60)
    print("INDEPENDENCE BY POSITION DISTANCE")
    print("=" * 60)
    indep = adjacent_position_independence_test(words)

    # Group by distance
    by_distance = defaultdict(list)
    for key, val in indep.items():
        by_distance[val['distance']].append(val)

    for dist in sorted(by_distance.keys()):
        items = by_distance[dist]
        avg_nmi = np.mean([x['NMI'] for x in items])
        avg_mi = np.mean([x['MI'] for x in items])
        print(f"  Distance {dist}: avg MI={avg_mi:.4f}, avg NMI={avg_nmi:.4f} (n={len(items)} pairs)")

    # 5. English comparison
    print("\n" + "=" * 60)
    print("ENGLISH COMPARISON (pharmaceutical vocabulary)")
    print("=" * 60)
    eng_mi = generate_english_comparison()
    for key, val in eng_mi.items():
        print(f"  English {key}: MI={val['MI']:.4f}, NMI={val['NMI']:.4f}")

    # 6. Conditional entropy chain
    print("\n" + "=" * 60)
    print("CONDITIONAL ENTROPY CHAIN")
    print("=" * 60)
    ce = conditional_entropy_chain(words)
    for length, data in ce.items():
        print(f"\n  {length}-letter words (n={data['sample_size']}):")
        for i, h in enumerate(data['entropy_per_position']):
            bar = '#' * int(h * 10)
            print(f"    H(P{i+1}|prev) = {h:.4f} bits  {bar}")
        print(f"    Flatness (CV): {data['flatness']:.4f} (lower = more uniform = more code-like)")

    # 7. Code table reconstruction
    print("\n" + "=" * 60)
    print("CODE TABLE RECONSTRUCTION")
    print("=" * 60)
    tables = code_table_reconstruction(words)
    for length, data in tables.items():
        print(f"\n  {length}-letter words (n={data['word_count']}):")
        for pos, pdata in data['positions'].items():
            chars = ', '.join(f"{ch}" for ch, _ in pdata['distribution'][:10])
            print(f"    Pos {pos+1}: {pdata['unique_values']} values [{chars}]")

    # 8. PCA-like dimensionality
    print("\n" + "=" * 60)
    print("DIMENSIONALITY ANALYSIS (PCA)")
    print("=" * 60)
    pca = pca_like_analysis(words)
    for length, data in pca.items():
        print(f"\n  {length}-letter words (n={data['word_count']}):")
        print(f"    Chars per position: {data['chars_per_position']}")
        print(f"    Total features: {data['total_features']}")
        print(f"    Components for 90%: {data['n_components_90pct']}")
        print(f"    Components for 95%: {data['n_components_95pct']}")
        print(f"    Independence score: {data['independence_score']:.2f} (1.0 = fully independent positions)")

    # 9. Substitution test
    print("\n" + "=" * 60)
    print("SUBSTITUTION TEST (single-position changes)")
    print("=" * 60)
    subs = substitution_test(words)
    for w, data in list(subs.items())[:15]:
        print(f"\n  '{w}' (freq={data['freq']}):")
        for pos, neighbors in data['neighbors'].items():
            for nb in neighbors[:3]:
                print(f"    Change pos {int(pos)+1}: -> '{nb['word']}' (freq={nb['freq']}) [{nb['change']}]")

    # 10. chol family
    print("\n" + "=" * 60)
    print("CHOL FAMILY ANALYSIS")
    print("=" * 60)
    chol = chol_family_analysis(words)
    for pattern, data in chol.items():
        print(f"\n  {pattern}:")
        for w, freq in list(data.items())[:10]:
            print(f"    {w}: {freq}")

    # 11. Stem-suffix analysis
    print("\n" + "=" * 60)
    print("STEM-SUFFIX DECOMPOSITION")
    print("=" * 60)
    stems = stem_suffix_analysis(words)
    for suf, data in list(stems.items())[:15]:
        print(f"\n  -{suf} ({data['count']} words, {data['unique_stems']} stems):")
        top = data['top_stems'][:8]
        print(f"    Stems: {', '.join(f'{s}({c})' for s, c in top)}")

    # 12. Pharmaceutical dimension mapping
    print("\n" + "=" * 60)
    print("PHARMACEUTICAL DIMENSION MAPPING")
    print("=" * 60)
    pharma = pharmaceutical_dimension_mapping(tables)
    print("\n  Known pharmaceutical dimensions and expected value counts:")
    for dim, desc in pharma.items():
        print(f"    {dim}: {desc}")

    print("\n  Observed values per position (4-letter words):")
    if 4 in tables:
        for pos, pdata in tables[4]['positions'].items():
            print(f"    Position {pos+1}: {pdata['unique_values']} values")

    print("\n  Observed values per position (5-letter words):")
    if 5 in tables:
        for pos, pdata in tables[5]['positions'].items():
            print(f"    Position {pos+1}: {pdata['unique_values']} values")

    print("\n  Observed values per position (6-letter words):")
    if 6 in tables:
        for pos, pdata in tables[6]['positions'].items():
            print(f"    Position {pos+1}: {pdata['unique_values']} values")

    # 13. Bigram vs position
    print("\n" + "=" * 60)
    print("BIGRAM INDEPENDENCE TEST")
    print("=" * 60)
    bigram = bigram_vs_position_analysis(words)
    for pos, data in bigram.items():
        status = "INDEPENDENT" if data['independence_ratio'] > 0.85 else "DEPENDENT"
        print(f"  P{pos+1}->P{pos+2}: H(next)={data['H_next']:.4f}, H(next|curr)={data['H_next_given_current']:.4f}, ratio={data['independence_ratio']:.4f} [{status}]")

    print("\n\nDone. Writing results file...")
