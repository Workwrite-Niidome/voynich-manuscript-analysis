import json
import re
from collections import defaultdict, Counter

# Load folio words
with open('C:/Users/kazuk/Downloads/voynich_analysis/folio_words.json', 'r') as f:
    folio_words = json.load(f)

def folio_sort_key(f):
    num = int(re.search(r'\d+', f).group())
    side = 1 if 'v' in f else 0
    return (num, side)

sorted_folios = sorted(folio_words.keys(), key=folio_sort_key)

def jaccard(set1, set2):
    if not set1 or not set2:
        return 0.0
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union)

def get_vocab(folio_id):
    words = folio_words.get(folio_id, [])
    return set(words)

def get_boundary_words(folio_id, n=5):
    words = folio_words.get(folio_id, [])
    first_w = words[:n] if words else []
    last_w = words[-n:] if words else []
    return first_w, last_w

def boundary_overlap(fid1, fid2, n=5):
    _, last1 = get_boundary_words(fid1, n)
    first2, _ = get_boundary_words(fid2, n)
    s1 = set(last1)
    s2 = set(first2)
    if not s1 or not s2:
        return 0.0
    return len(s1 & s2) / len(s1 | s2)

def calc_avg_jaccard(folio_list):
    overlaps = []
    for i in range(len(folio_list) - 1):
        v1 = get_vocab(folio_list[i])
        v2 = get_vocab(folio_list[i + 1])
        j = jaccard(v1, v2)
        overlaps.append((folio_list[i], folio_list[i+1], j))
    return overlaps

def currier_score(folio_id):
    words = folio_words.get(folio_id, [])
    if not words:
        return None, 0, 0
    a_count = 0
    b_count = 0
    for w in words:
        if w.startswith('qo'): a_count += 1
        if w.endswith('am') or w.endswith('om'): a_count += 1
        if w.startswith('ol'): a_count += 0.5
        if w.endswith('dy') or w.endswith('ey'): b_count += 1
        if w.startswith('sh') and not w.startswith('sho'): b_count += 0.5
        if w.endswith('aiin'): b_count += 0.5
        if w.startswith('dain') or w == 'daiin': b_count += 0.5
    total = a_count + b_count
    if total == 0:
        return 'U', 0, 0
    ratio = a_count / total
    dialect = 'A' if ratio > 0.6 else ('B' if ratio < 0.4 else 'AB')
    return dialect, a_count, b_count

results = []

# ============================================================
# ANALYSIS 1: Current order vocabulary overlap
# ============================================================
results.append("=" * 70)
results.append("ANALYSIS 1: Vocabulary overlap of currently adjacent folios")
results.append("=" * 70)

current_overlaps = []
for i in range(len(sorted_folios) - 1):
    f1 = sorted_folios[i]
    f2 = sorted_folios[i + 1]
    v1 = get_vocab(f1)
    v2 = get_vocab(f2)
    j = jaccard(v1, v2)
    current_overlaps.append((f1, f2, j))

avg_current = sum(x[2] for x in current_overlaps) / len(current_overlaps)
results.append(f"Average Jaccard similarity (current order): {avg_current:.4f}")
results.append(f"Total adjacent pairs: {len(current_overlaps)}")

current_overlaps_sorted = sorted(current_overlaps, key=lambda x: x[2], reverse=True)
results.append("\nTop 10 most similar adjacent pairs:")
for f1, f2, j in current_overlaps_sorted[:10]:
    results.append(f"  {f1} <-> {f2}: {j:.4f}")
results.append("\nBottom 10 least similar adjacent pairs:")
for f1, f2, j in current_overlaps_sorted[-10:]:
    results.append(f"  {f1} <-> {f2}: {j:.4f}")

# ============================================================
# ANALYSIS 2: Q13 reordering test
# ============================================================
results.append("\n" + "=" * 70)
results.append("ANALYSIS 2: Quire 13 reordering test")
results.append("=" * 70)

q13_current = []
for n in range(75, 85):
    for side in ['r', 'v']:
        fid = f'f{n}{side}'
        if fid in folio_words:
            q13_current.append(fid)

q13_proposed_leaf_order = [76, 77, 79, 84, 78, 81, 75, 80, 82, 83]
q13_proposed = []
for n in q13_proposed_leaf_order:
    for side in ['r', 'v']:
        fid = f'f{n}{side}'
        if fid in folio_words:
            q13_proposed.append(fid)

q13_current_overlaps = calc_avg_jaccard(q13_current)
q13_proposed_overlaps = calc_avg_jaccard(q13_proposed)

avg_q13_current = sum(x[2] for x in q13_current_overlaps) / len(q13_current_overlaps) if q13_current_overlaps else 0
avg_q13_proposed = sum(x[2] for x in q13_proposed_overlaps) / len(q13_proposed_overlaps) if q13_proposed_overlaps else 0

results.append(f"Q13 current order avg Jaccard: {avg_q13_current:.4f}")
results.append(f"Q13 proposed order avg Jaccard: {avg_q13_proposed:.4f}")
if avg_q13_current > 0:
    results.append(f"Change: {(avg_q13_proposed - avg_q13_current) / avg_q13_current * 100:+.1f}%")

results.append("\nQ13 Current order pairs (leaf transitions only):")
for f1, f2, j in q13_current_overlaps:
    if f1.endswith('v') and f2.endswith('r'):
        results.append(f"  {f1} -> {f2}: {j:.4f}")

results.append("\nQ13 Proposed order pairs (leaf transitions only):")
for f1, f2, j in q13_proposed_overlaps:
    if f1.endswith('v') and f2.endswith('r'):
        results.append(f"  {f1} -> {f2}: {j:.4f}")

# ============================================================
# ANALYSIS 3: Cross-folio boundary word continuation
# ============================================================
results.append("\n" + "=" * 70)
results.append("ANALYSIS 3: Cross-folio word continuation (boundary overlap)")
results.append("=" * 70)

results.append("\nQ13 boundary overlap (last 10 words -> first 10 words at leaf transitions):")
results.append("Current order:")
for i in range(len(q13_current) - 1):
    if q13_current[i].endswith('v') and q13_current[i+1].endswith('r'):
        bo = boundary_overlap(q13_current[i], q13_current[i+1], 10)
        results.append(f"  {q13_current[i]} -> {q13_current[i+1]}: {bo:.4f}")

current_q13_boundary = []
for i in range(len(q13_current) - 1):
    if q13_current[i].endswith('v') and q13_current[i+1].endswith('r'):
        current_q13_boundary.append(boundary_overlap(q13_current[i], q13_current[i+1], 10))

results.append("Proposed order:")
proposed_q13_boundary = []
for i in range(len(q13_proposed) - 1):
    if q13_proposed[i].endswith('v') and q13_proposed[i+1].endswith('r'):
        bo = boundary_overlap(q13_proposed[i], q13_proposed[i+1], 10)
        results.append(f"  {q13_proposed[i]} -> {q13_proposed[i+1]}: {bo:.4f}")
        proposed_q13_boundary.append(bo)

if current_q13_boundary and proposed_q13_boundary:
    avg_cur_bound = sum(current_q13_boundary) / len(current_q13_boundary)
    avg_prop_bound = sum(proposed_q13_boundary) / len(proposed_q13_boundary)
    results.append(f"\nAvg boundary overlap - Current: {avg_cur_bound:.4f}, Proposed: {avg_prop_bound:.4f}")

# ============================================================
# ANALYSIS 4: Herbal bifolium coherence
# ============================================================
results.append("\n" + "=" * 70)
results.append("ANALYSIS 4: Herbal section bifolium coherence")
results.append("=" * 70)

herbal_bifolia = {
    'Q1': [(1,8), (2,7), (3,6), (4,5)],
    'Q2': [(9,15), (10,14), (11,13)],
    'Q4': [(25,32), (26,31), (27,30), (28,29)],
    'Q5': [(33,40), (34,39), (35,38), (36,37)],
    'Q6': [(41,48), (42,47), (43,46), (44,45)],
}

results.append("\nBifolium coherence (Jaccard between conjugate leaves):")
for quire, bifolia in herbal_bifolia.items():
    results.append(f"\n  {quire}:")
    for outer, inner in bifolia:
        outer_words = set()
        inner_words = set()
        for side in ['r', 'v']:
            outer_words |= get_vocab(f'f{outer}{side}')
            inner_words |= get_vocab(f'f{inner}{side}')
        j = jaccard(outer_words, inner_words)
        results.append(f"    f{outer}/f{inner} bifolium: {j:.4f}")

# Compare: conjugate leaves vs sequential leaves
results.append("\nConjugate vs Sequential comparison (Herbal):")
conj_scores = []
seq_scores = []
for quire, bifolia in herbal_bifolia.items():
    for outer, inner in bifolia:
        outer_words = set()
        inner_words = set()
        for side in ['r', 'v']:
            outer_words |= get_vocab(f'f{outer}{side}')
            inner_words |= get_vocab(f'f{inner}{side}')
        conj_scores.append(jaccard(outer_words, inner_words))

for n in range(1, 56):
    for side_pair in [('v', 'r')]:
        f1 = f'f{n}v'
        f2 = f'f{n+1}r'
        if f1 in folio_words and f2 in folio_words:
            v1 = get_vocab(f1)
            v2 = get_vocab(f2)
            seq_scores.append(jaccard(v1, v2))

results.append(f"  Avg conjugate leaf similarity: {sum(conj_scores)/len(conj_scores):.4f}")
results.append(f"  Avg sequential leaf similarity: {sum(seq_scores)/len(seq_scores):.4f}")

# ============================================================
# ANALYSIS 5: Currier A/B by bifolium
# ============================================================
results.append("\n" + "=" * 70)
results.append("ANALYSIS 5: Currier A/B dialect distribution")
results.append("=" * 70)

results.append("\nHerbal section dialect by folio:")
for n in range(1, 57):
    for side in ['r', 'v']:
        fid = f'f{n}{side}'
        if fid in folio_words and len(folio_words[fid]) > 5:
            d, a, b = currier_score(fid)
            if d:
                results.append(f"  {fid}: {d} (A={a:.1f}, B={b:.1f})")

results.append("\nDialect by bifolium in Q4 (Davis: scribes alternate by bifolium):")
for outer, inner in [(25,32), (26,31), (27,30), (28,29)]:
    outer_all = []
    inner_all = []
    for side in ['r', 'v']:
        outer_all.extend(folio_words.get(f'f{outer}{side}', []))
        inner_all.extend(folio_words.get(f'f{inner}{side}', []))

    # Score combined words
    def score_words(words):
        a = 0; b = 0
        for w in words:
            if w.startswith('qo'): a += 1
            if w.endswith('am') or w.endswith('om'): a += 1
            if w.endswith('dy') or w.endswith('ey'): b += 1
            if w.endswith('aiin'): b += 0.5
        total = a + b
        if total == 0: return 'U'
        return 'A' if a/total > 0.6 else ('B' if a/total < 0.4 else 'AB')

    do = score_words(outer_all)
    di = score_words(inner_all)
    results.append(f"  f{outer}/f{inner}: outer={do}, inner={di}")

# ============================================================
# ANALYSIS 6: Broader reordering - Pharma quires Q15 and Q17
# ============================================================
results.append("\n" + "=" * 70)
results.append("ANALYSIS 6: Pharma quire order test (Q15 vs Q17)")
results.append("=" * 70)

q15_folios = []
for n in [87, 88, 89, 90]:
    for side in ['r', 'v']:
        fid = f'f{n}{side}'
        if fid in folio_words:
            q15_folios.append(fid)

q17_folios = []
for n in [93, 94, 95, 96]:
    for side in ['r', 'v']:
        fid = f'f{n}{side}'
        if fid in folio_words:
            q17_folios.append(fid)

# Current: Q15 then Q17
# Proposed reversal: Q17 then Q15
if q15_folios and q17_folios:
    # Transition similarity Q15->Q17 vs Q17->Q15
    current_trans = jaccard(get_vocab(q15_folios[-1]), get_vocab(q17_folios[0]))
    reversed_trans = jaccard(get_vocab(q17_folios[-1]), get_vocab(q15_folios[0]))
    results.append(f"Q15->Q17 transition Jaccard: {current_trans:.4f}")
    results.append(f"Q17->Q15 transition Jaccard: {reversed_trans:.4f}")
    results.append(f"Better order: {'Reversed (Q17->Q15)' if reversed_trans > current_trans else 'Current (Q15->Q17)'}")

# ============================================================
# ANALYSIS 7: Five scribes vs two (vocabulary clustering)
# ============================================================
results.append("\n" + "=" * 70)
results.append("ANALYSIS 7: Five scribes - vocabulary clustering test")
results.append("=" * 70)

# Davis: Scribe 1 = Q1-Q3, then alternating by bifolium starting Q4
# Get vocabulary profiles for different quire groups
q1_3_words = Counter()
for n in range(1, 24):
    for side in ['r', 'v']:
        fid = f'f{n}{side}'
        if fid in folio_words:
            q1_3_words.update(folio_words[fid])

q4_6_words = Counter()
for n in range(25, 49):
    for side in ['r', 'v']:
        fid = f'f{n}{side}'
        if fid in folio_words:
            q4_6_words.update(folio_words[fid])

q1_3_top = set([w for w, c in q1_3_words.most_common(50)])
q4_6_top = set([w for w, c in q4_6_words.most_common(50)])

overlap = q1_3_top & q4_6_top
results.append(f"Top-50 vocabulary overlap Q1-3 vs Q4-6: {len(overlap)}/50 = {len(overlap)/50:.1%}")
results.append(f"Shared words: {sorted(overlap)}")

# Check if Q4 bifolia show vocabulary segregation (scribe alternation)
results.append("\nQ4 bifolium vocabulary segregation test:")
for outer, inner in [(25,32), (26,31), (27,30), (28,29)]:
    outer_words = Counter()
    inner_words = Counter()
    for side in ['r', 'v']:
        outer_words.update(folio_words.get(f'f{outer}{side}', []))
        inner_words.update(folio_words.get(f'f{inner}{side}', []))

    outer_unique = set(outer_words.keys()) - set(inner_words.keys())
    inner_unique = set(inner_words.keys()) - set(outer_words.keys())
    shared = set(outer_words.keys()) & set(inner_words.keys())
    total = len(outer_unique) + len(inner_unique) + len(shared)
    results.append(f"  f{outer}/f{inner}: shared={len(shared)}, outer_unique={len(outer_unique)}, inner_unique={len(inner_unique)}, segregation={1 - len(shared)/total:.2%}")

# ============================================================
# ANALYSIS 8: Dioscorides ordering test with proposed reordering
# ============================================================
results.append("\n" + "=" * 70)
results.append("ANALYSIS 8: Dioscorides ordering correlation")
results.append("=" * 70)

# Check if plant_order_analysis data exists
import os
if os.path.exists('C:/Users/kazuk/Downloads/voynich_analysis/plant_order_analysis.md'):
    results.append("(Referencing prior Dioscorides ordering analysis)")
    results.append("The Dioscorides ordering hypothesis assumed current folio sequence = original.")
    results.append("If bifolia are misordered, any correlation found would be WEAKENED by noise.")
    results.append("Reordering should either:")
    results.append("  a) Improve correlation (supporting both Davis and Dioscorides hypotheses)")
    results.append("  b) Have no effect (reordering is irrelevant to plant ordering)")
    results.append("  c) Worsen correlation (one hypothesis is wrong)")

# Test: within herbal section, is vocabulary more coherent when
# we group by bifolium rather than by sequential folio?
results.append("\nHerbal section: bifolium-grouped vs sequential coherence")

bifolium_coherence = []
sequential_coherence = []

for quire, bifolia in herbal_bifolia.items():
    for outer, inner in bifolia:
        # Bifolium coherence: how similar are the two leaves of same bifolium?
        ow = set()
        iw = set()
        for side in ['r', 'v']:
            ow |= get_vocab(f'f{outer}{side}')
            iw |= get_vocab(f'f{inner}{side}')
        if ow and iw:
            bifolium_coherence.append(jaccard(ow, iw))

        # Sequential coherence: how similar are the outer leaf and its sequential neighbor?
        seq_neighbor = f'f{outer+1}r'
        if seq_neighbor in folio_words:
            nw = get_vocab(seq_neighbor) | get_vocab(f'f{outer+1}v')
            if ow and nw:
                sequential_coherence.append(jaccard(ow, nw))

if bifolium_coherence and sequential_coherence:
    avg_bif = sum(bifolium_coherence) / len(bifolium_coherence)
    avg_seq = sum(sequential_coherence) / len(sequential_coherence)
    results.append(f"  Avg bifolium coherence: {avg_bif:.4f}")
    results.append(f"  Avg sequential coherence: {avg_seq:.4f}")
    if avg_bif > avg_seq:
        results.append("  -> Bifolium grouping shows HIGHER coherence than sequential order")
        results.append("  -> Supports Davis: bifolia were written as units, current sequence is disrupted")
    else:
        results.append("  -> Sequential order shows higher coherence")
        results.append("  -> Current binding may preserve original sequence better than bifolium theory suggests")

# Print all results
output = "\n".join(results)
print(output)

# Save to file
with open('C:/Users/kazuk/Downloads/voynich_analysis/reorder_raw_results.txt', 'w') as f:
    f.write(output)

print("\n\nResults saved to reorder_raw_results.txt")
