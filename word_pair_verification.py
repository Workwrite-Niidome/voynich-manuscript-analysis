"""
WORD PAIR VERIFICATION: Do chol(A) and chedy(B) encode the same Italian word?
==============================================================================
Runs 5 systematic tests on the candidate word pairs:
  1. POSITIONAL TEST - same relative position within lines
  2. CONTEXT TEST - similar left/right neighbors
  3. ILLUSTRATION TEST - co-occurrence on herbal pages with similar plants
  4. FREQUENCY RATIO TEST - proportional to A/B word count ratio (1.45:1)
  5. MORPHOLOGICAL TEST - structural relationship between pair members
"""

import re
from collections import Counter, defaultdict
from itertools import combinations
import math
import json

# ============================================================
# PARSE IVTFF TRANSCRIPTION
# ============================================================

def parse_ivtff(filepath):
    """Parse an IVTFF transcription file into structured data."""
    pages = {}
    current_folio = None
    current_lang = None
    current_illust = None
    current_quire = None

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Folio header line
            header_match = re.match(r'<(f\d+[rv]\d?)>\s+<!\s*(.*?)>', line)
            if header_match:
                current_folio = header_match.group(1)
                attrs = header_match.group(2)
                lang_match = re.search(r'\$L=([AB])', attrs)
                current_lang = lang_match.group(1) if lang_match else None
                illust_match = re.search(r'\$I=(\w+)', attrs)
                current_illust = illust_match.group(1) if illust_match else None
                quire_match = re.search(r'\$Q=(\w+)', attrs)
                current_quire = quire_match.group(1) if quire_match else None

                if current_folio not in pages:
                    pages[current_folio] = {
                        'lang': current_lang,
                        'illust': current_illust,
                        'quire': current_quire,
                        'lines': [],
                        'words': []
                    }
                continue

            # Text line
            text_match = re.match(r'<(f\d+[rv]\d?\.\d+)', line)
            if text_match and current_folio:
                text_part = re.sub(r'<[^>]*>', '', line)
                text_part = re.sub(r'<%>', '', text_part)
                text_part = re.sub(r'<\$>', '', text_part)
                text_part = re.sub(r'<!@\d+;>', '', text_part)
                text_part = re.sub(r'@\d+;?', '', text_part)
                text_part = re.sub(r'\{[^}]*\}', '', text_part)
                text_part = re.sub(r'\[[^\]]*\]', '', text_part)
                text_part = re.sub(r'[<>%$?]', '', text_part)

                words = re.split(r'[.\s,]+', text_part)
                words = [w.strip() for w in words if w.strip() and len(w.strip()) > 0]
                words = [w for w in words if not re.match(r'^[-=+*@#]+$', w) and len(w) > 0]

                pages[current_folio]['lines'].append(words)
                pages[current_folio]['words'].extend(words)

    return pages


# ============================================================
# MAIN ANALYSIS
# ============================================================

def main():
    filepath = "C:/Users/kazuk/Downloads/voynich_analysis/ZL3b-n.txt"
    pages = parse_ivtff(filepath)

    # Separate A and B
    a_pages = {f: d for f, d in pages.items() if d['lang'] == 'A'}
    b_pages = {f: d for f, d in pages.items() if d['lang'] == 'B'}

    a_words_all = []
    b_words_all = []
    for d in a_pages.values():
        a_words_all.extend(d['words'])
    for d in b_pages.values():
        b_words_all.extend(d['words'])

    a_counter = Counter(a_words_all)
    b_counter = Counter(b_words_all)

    total_a = len(a_words_all)
    total_b = len(b_words_all)
    ab_ratio = total_a / total_b

    print("=" * 90)
    print("WORD PAIR VERIFICATION: Testing A/B Code Equivalences")
    print("=" * 90)
    print(f"\nTotal A words: {total_a}")
    print(f"Total B words: {total_b}")
    print(f"A/B word ratio: {ab_ratio:.3f}")

    # Define candidate pairs to test
    candidate_pairs = [
        ('chol', 'chedy'),
        ('chor', 'shedy'),
        ('sho', 'chdy'),
        ('shol', 'qokedy'),
        ('daiin', 'daiin'),  # control: shared word
        ('chol', 'qokedy'),  # alternative pairing
        ('shol', 'shedy'),   # alternative pairing
        ('chor', 'chedy'),   # alternative pairing
        ('or', 'or'),        # control: shared word
        ('ol', 'ol'),        # control: shared word
    ]

    # ================================================================
    # TEST 0: Basic frequency comparison
    # ================================================================
    print(f"\n{'='*90}")
    print("TEST 0: BASIC FREQUENCY TABLE")
    print(f"{'='*90}")
    print(f"{'A_word':<12} {'A_count':>8} {'A_%':>7} | {'B_word':<12} {'B_count':>8} {'B_%':>7} | {'Freq_ratio':>10} {'Expected':>8}")
    print("-" * 90)

    for a_word, b_word in candidate_pairs:
        a_c = a_counter.get(a_word, 0)
        b_c = b_counter.get(b_word, 0)
        a_pct = a_c / total_a * 100
        b_pct = b_c / total_b * 100
        if b_c > 0:
            observed_ratio = a_c / b_c
        else:
            observed_ratio = float('inf')
        expected_ratio = ab_ratio
        ratio_deviation = observed_ratio / expected_ratio if expected_ratio > 0 else 0

        marker = ""
        if 0.5 <= ratio_deviation <= 2.0:
            marker = "OK"
        elif 0.3 <= ratio_deviation <= 3.0:
            marker = "WEAK"
        else:
            marker = "FAIL"

        print(f"{a_word:<12} {a_c:>8} {a_pct:>6.2f}% | {b_word:<12} {b_c:>8} {b_pct:>6.2f}% | {observed_ratio:>10.2f} {expected_ratio:>7.2f} [{marker}]")

    # ================================================================
    # TEST 1: POSITIONAL TEST - Position within line
    # ================================================================
    print(f"\n{'='*90}")
    print("TEST 1: POSITIONAL TEST")
    print("If two words encode the same concept, they should appear at similar")
    print("positions within lines (e.g., both as 1st word, 3rd word, last word).")
    print(f"{'='*90}")

    def get_position_distribution(word, lang_pages, normalize=True):
        """Get distribution of positions where word appears in lines."""
        positions = defaultdict(int)  # position bucket -> count
        total = 0
        for folio, data in lang_pages.items():
            for line in data['lines']:
                if len(line) == 0:
                    continue
                for i, w in enumerate(line):
                    if w == word:
                        # Normalize position to 0-1 range
                        if normalize and len(line) > 1:
                            norm_pos = i / (len(line) - 1)
                        else:
                            norm_pos = i / max(len(line), 1)
                        # Bucket into 5 bins: start, early, mid, late, end
                        if norm_pos <= 0.1:
                            positions['1_START'] += 1
                        elif norm_pos <= 0.3:
                            positions['2_EARLY'] += 1
                        elif norm_pos <= 0.6:
                            positions['3_MID'] += 1
                        elif norm_pos <= 0.9:
                            positions['4_LATE'] += 1
                        else:
                            positions['5_END'] += 1
                        total += 1
        return positions, total

    def get_absolute_position_distribution(word, lang_pages):
        """Get distribution of absolute word positions (1st, 2nd, 3rd...)."""
        positions = Counter()
        total = 0
        for folio, data in lang_pages.items():
            for line in data['lines']:
                for i, w in enumerate(line):
                    if w == word:
                        positions[i+1] += 1
                        total += 1
        return positions, total

    def position_similarity(dist1, total1, dist2, total2):
        """Compute cosine similarity between two position distributions."""
        if total1 == 0 or total2 == 0:
            return 0.0
        all_keys = set(dist1.keys()) | set(dist2.keys())
        v1 = [dist1.get(k, 0) / total1 for k in sorted(all_keys)]
        v2 = [dist2.get(k, 0) / total2 for k in sorted(all_keys)]
        dot = sum(a*b for a, b in zip(v1, v2))
        mag1 = sum(a*a for a in v1) ** 0.5
        mag2 = sum(a*a for a in v2) ** 0.5
        if mag1 == 0 or mag2 == 0:
            return 0.0
        return dot / (mag1 * mag2)

    for a_word, b_word in candidate_pairs:
        a_pos, a_total = get_position_distribution(a_word, a_pages)
        b_pos, b_total = get_position_distribution(b_word, b_pages)
        sim = position_similarity(a_pos, a_total, b_pos, b_total)

        print(f"\n  {a_word}(A) vs {b_word}(B) - Position cosine similarity: {sim:.4f}")
        print(f"    {'Position':<12} {'A_%':>8} {'B_%':>8}")
        all_pos = sorted(set(a_pos.keys()) | set(b_pos.keys()))
        for p in all_pos:
            a_pct = a_pos.get(p, 0) / a_total * 100 if a_total > 0 else 0
            b_pct = b_pos.get(p, 0) / b_total * 100 if b_total > 0 else 0
            print(f"    {p:<12} {a_pct:>7.1f}% {b_pct:>7.1f}%")

    # Also check first-word and last-word frequencies
    print(f"\n  --- FIRST WORD ON LINE frequency ---")
    for a_word, b_word in candidate_pairs:
        a_first = sum(1 for d in a_pages.values() for line in d['lines'] if line and line[0] == a_word)
        b_first = sum(1 for d in b_pages.values() for line in d['lines'] if line and line[0] == b_word)
        a_lines = sum(len(d['lines']) for d in a_pages.values())
        b_lines = sum(len(d['lines']) for d in b_pages.values())
        print(f"    {a_word}(A): {a_first}/{a_lines} = {a_first/a_lines*100:.2f}%  |  {b_word}(B): {b_first}/{b_lines} = {b_first/b_lines*100:.2f}%")

    print(f"\n  --- LAST WORD ON LINE frequency ---")
    for a_word, b_word in candidate_pairs:
        a_last = sum(1 for d in a_pages.values() for line in d['lines'] if line and line[-1] == a_word)
        b_last = sum(1 for d in b_pages.values() for line in d['lines'] if line and line[-1] == b_word)
        a_lines = sum(len(d['lines']) for d in a_pages.values())
        b_lines = sum(len(d['lines']) for d in b_pages.values())
        print(f"    {a_word}(A): {a_last}/{a_lines} = {a_last/a_lines*100:.2f}%  |  {b_word}(B): {b_last}/{b_lines} = {b_last/b_lines*100:.2f}%")

    # ================================================================
    # TEST 2: CONTEXT TEST - Left and right neighbors
    # ================================================================
    print(f"\n{'='*90}")
    print("TEST 2: CONTEXT TEST")
    print("If two words encode the same concept, they should appear in similar")
    print("syntactic contexts (same left/right neighbors or equivalent neighbors).")
    print(f"{'='*90}")

    def get_neighbors(word, lang_pages):
        """Get left and right neighbor word distributions."""
        left = Counter()
        right = Counter()
        total = 0
        for folio, data in lang_pages.items():
            for line in data['lines']:
                for i, w in enumerate(line):
                    if w == word:
                        if i > 0:
                            left[line[i-1]] += 1
                        if i < len(line) - 1:
                            right[line[i+1]] += 1
                        total += 1
        return left, right, total

    for a_word, b_word in candidate_pairs:
        a_left, a_right, a_total = get_neighbors(a_word, a_pages)
        b_left, b_right, b_total = get_neighbors(b_word, b_pages)

        print(f"\n  === {a_word}(A) vs {b_word}(B) ===")
        print(f"  Occurrences: A={a_total}, B={b_total}")

        # Left neighbors
        print(f"\n  Left neighbors (word preceding target):")
        print(f"    {'A_left':<15} {'A_n':>5} {'A_%':>7} | {'B_left':<15} {'B_n':>5} {'B_%':>7}")
        a_top_left = a_left.most_common(10)
        b_top_left = b_left.most_common(10)
        for i in range(max(len(a_top_left), len(b_top_left))):
            a_str = ""
            b_str = ""
            if i < len(a_top_left):
                w, c = a_top_left[i]
                a_str = f"{w:<15} {c:>5} {c/a_total*100:>6.1f}%"
            else:
                a_str = " " * 30
            if i < len(b_top_left):
                w, c = b_top_left[i]
                b_str = f"{w:<15} {c:>5} {c/b_total*100:>6.1f}%"
            else:
                b_str = ""
            print(f"    {a_str} | {b_str}")

        # Right neighbors
        print(f"\n  Right neighbors (word following target):")
        print(f"    {'A_right':<15} {'A_n':>5} {'A_%':>7} | {'B_right':<15} {'B_n':>5} {'B_%':>7}")
        a_top_right = a_right.most_common(10)
        b_top_right = b_right.most_common(10)
        for i in range(max(len(a_top_right), len(b_top_right))):
            a_str = ""
            b_str = ""
            if i < len(a_top_right):
                w, c = a_top_right[i]
                a_str = f"{w:<15} {c:>5} {c/a_total*100:>6.1f}%"
            else:
                a_str = " " * 30
            if i < len(b_top_right):
                w, c = b_top_right[i]
                b_str = f"{w:<15} {c:>5} {c/b_total*100:>6.1f}%"
            else:
                b_str = ""
            print(f"    {a_str} | {b_str}")

        # Compute overlap of neighbor sets
        shared_left = set(a_left.keys()) & set(b_left.keys())
        shared_right = set(a_right.keys()) & set(b_right.keys())
        all_left = set(a_left.keys()) | set(b_left.keys())
        all_right = set(a_right.keys()) | set(b_right.keys())
        left_jaccard = len(shared_left) / len(all_left) if all_left else 0
        right_jaccard = len(shared_right) / len(all_right) if all_right else 0
        print(f"\n  Neighbor overlap: Left Jaccard = {left_jaccard:.3f}, Right Jaccard = {right_jaccard:.3f}")

        # Show shared neighbors with their frequencies
        if shared_left:
            print(f"  Shared left neighbors: {', '.join(sorted(shared_left, key=lambda w: -(a_left[w]+b_left[w])))[:15]}")
        if shared_right:
            print(f"  Shared right neighbors: {', '.join(sorted(shared_right, key=lambda w: -(a_right[w]+b_right[w])))[:15]}")

    # ================================================================
    # TEST 3: ILLUSTRATION TEST - Herbal page co-occurrence
    # ================================================================
    print(f"\n{'='*90}")
    print("TEST 3: ILLUSTRATION TEST")
    print("On herbal pages (same topic), do candidate pairs appear on A vs B pages?")
    print("If chol(A) = chedy(B), chol should dominate A-herbal and chedy B-herbal.")
    print(f"{'='*90}")

    # Get herbal-only pages
    a_herbal = {f: d for f, d in a_pages.items() if d['illust'] == 'H'}
    b_herbal = {f: d for f, d in b_pages.items() if d['illust'] == 'H'}

    a_herbal_words = []
    b_herbal_words = []
    for d in a_herbal.values():
        a_herbal_words.extend(d['words'])
    for d in b_herbal.values():
        b_herbal_words.extend(d['words'])

    a_herbal_counter = Counter(a_herbal_words)
    b_herbal_counter = Counter(b_herbal_words)

    print(f"\nHerbal pages: A={len(a_herbal)} folios ({len(a_herbal_words)} words), B={len(b_herbal)} folios ({len(b_herbal_words)} words)")
    herbal_ratio = len(a_herbal_words) / len(b_herbal_words) if b_herbal_words else 0
    print(f"Herbal A/B word ratio: {herbal_ratio:.3f}")

    print(f"\n{'A_word':<12} {'A_herb':>7} {'A_h%':>7} | {'B_word':<12} {'B_herb':>7} {'B_h%':>7} | {'Ratio':>8} {'Verdict':>8}")
    print("-" * 85)

    for a_word, b_word in candidate_pairs:
        a_c = a_herbal_counter.get(a_word, 0)
        b_c = b_herbal_counter.get(b_word, 0)
        a_pct = a_c / len(a_herbal_words) * 100 if a_herbal_words else 0
        b_pct = b_c / len(b_herbal_words) * 100 if b_herbal_words else 0
        ratio = a_c / b_c if b_c > 0 else float('inf')
        deviation = ratio / herbal_ratio if herbal_ratio > 0 and ratio != float('inf') else 0
        verdict = "OK" if 0.5 <= deviation <= 2.0 else ("WEAK" if 0.3 <= deviation <= 3.0 else "FAIL")
        if ratio == float('inf'):
            verdict = "N/A"
        print(f"{a_word:<12} {a_c:>7} {a_pct:>6.2f}% | {b_word:<12} {b_c:>7} {b_pct:>6.2f}% | {ratio:>8.2f} {verdict:>8}")

    # Per-folio distribution for top candidates
    print(f"\n--- Per-folio word counts for key candidates (herbal pages only) ---")
    key_words = ['chol', 'chedy', 'chor', 'shedy', 'shol', 'qokedy', 'daiin', 'ol', 'or']

    print(f"\n  A-HERBAL folios with most 'chol':")
    a_folio_chol = [(f, Counter(d['words']).get('chol', 0)) for f, d in a_herbal.items()]
    a_folio_chol.sort(key=lambda x: -x[1])
    for f, c in a_folio_chol[:15]:
        if c > 0:
            other_counts = {w: Counter(a_herbal[f]['words']).get(w, 0) for w in key_words}
            print(f"    {f}: chol={c}, {', '.join(f'{k}={v}' for k, v in other_counts.items() if v > 0 and k != 'chol')}")

    print(f"\n  B-HERBAL folios with most 'chedy':")
    b_folio_chedy = [(f, Counter(d['words']).get('chedy', 0)) for f, d in b_herbal.items()]
    b_folio_chedy.sort(key=lambda x: -x[1])
    for f, c in b_folio_chedy[:15]:
        if c > 0:
            other_counts = {w: Counter(b_herbal[f]['words']).get(w, 0) for w in key_words}
            print(f"    {f}: chedy={c}, {', '.join(f'{k}={v}' for k, v in other_counts.items() if v > 0 and k != 'chedy')}")

    # ================================================================
    # TEST 4: FREQUENCY RATIO TEST (detailed)
    # ================================================================
    print(f"\n{'='*90}")
    print("TEST 4: FREQUENCY RATIO TEST (DETAILED)")
    print(f"Expected ratio if same word: {ab_ratio:.3f} (overall) or {herbal_ratio:.3f} (herbal)")
    print("Testing across ALL sections and herbal-only.")
    print(f"{'='*90}")

    # Section-by-section breakdown
    sections = ['H', 'B', 'P', 'S', 'T', 'C', 'A', 'Z']
    section_names = {'H': 'Herbal', 'B': 'Bio', 'P': 'Pharma', 'S': 'Stars',
                     'T': 'Text', 'C': 'Cosmo', 'A': 'Astro', 'Z': 'Zodiac'}

    for a_word, b_word in [('chol', 'chedy'), ('chor', 'shedy'), ('shol', 'qokedy'), ('shol', 'shedy')]:
        print(f"\n  {a_word}(A) vs {b_word}(B) by section:")
        for sec in sections:
            a_sec_words = []
            b_sec_words = []
            for f, d in a_pages.items():
                if d['illust'] == sec:
                    a_sec_words.extend(d['words'])
            for f, d in b_pages.items():
                if d['illust'] == sec:
                    b_sec_words.extend(d['words'])

            if a_sec_words or b_sec_words:
                a_c = Counter(a_sec_words).get(a_word, 0)
                b_c = Counter(b_sec_words).get(b_word, 0)
                if a_c > 0 or b_c > 0:
                    print(f"    {section_names.get(sec, sec):<12}: {a_word}={a_c:>4} (in {len(a_sec_words):>5} words), {b_word}={b_c:>4} (in {len(b_sec_words):>5} words)")

    # ================================================================
    # TEST 5: MORPHOLOGICAL TEST
    # ================================================================
    print(f"\n{'='*90}")
    print("TEST 5: MORPHOLOGICAL TEST")
    print("Analyzing structural relationships between paired words.")
    print(f"{'='*90}")

    # Define morphological decomposition
    prefixes = ['qok', 'qo', 'ch', 'sh', 'ct', 'ck', 'ok', 'ot', 'da', 'ol', 'cp']
    suffixes_list = ['edy', 'eedy', 'ey', 'dy', 'ol', 'or', 'ar', 'ain', 'aiin', 'y', 'o']

    def decompose(word):
        """Decompose a word into prefix + root + suffix."""
        prefix = ""
        suffix = ""
        root = word

        # Try prefixes (longest first)
        for p in sorted(prefixes, key=len, reverse=True):
            if word.startswith(p) and len(word) > len(p):
                prefix = p
                root = word[len(p):]
                break

        # Try suffixes on the root (longest first)
        for s in sorted(suffixes_list, key=len, reverse=True):
            if root.endswith(s) and len(root) > len(s):
                suffix = s
                root = root[:-len(s)]
                break
            elif root == s:
                suffix = s
                root = ""
                break

        return prefix, root, suffix

    print(f"\n{'Word':<15} {'Prefix':<8} {'Root':<8} {'Suffix':<8} | Notes")
    print("-" * 65)
    all_words_to_decompose = set()
    for a_word, b_word in candidate_pairs:
        all_words_to_decompose.add(a_word)
        all_words_to_decompose.add(b_word)

    for w in sorted(all_words_to_decompose):
        p, r, s = decompose(w)
        print(f"{w:<15} {p:<8} {r:<8} {s:<8}")

    # Check if prefix is preserved across pairs
    print(f"\n--- Prefix preservation across pairs ---")
    for a_word, b_word in candidate_pairs:
        a_p, a_r, a_s = decompose(a_word)
        b_p, b_r, b_s = decompose(b_word)
        prefix_match = "SAME" if a_p == b_p else "DIFF"
        suffix_match = "SAME" if a_s == b_s else "DIFF"
        print(f"  {a_word}({a_p}+{a_r}+{a_s}) <-> {b_word}({b_p}+{b_r}+{b_s}) : prefix={prefix_match}, suffix={suffix_match}")

    # ================================================================
    # TEST 6: SYSTEMATIC MAPPING - Build full A<->B mapping table
    # ================================================================
    print(f"\n{'='*90}")
    print("TEST 6: SYSTEMATIC MAPPING TABLE")
    print("If there's a systematic A<->B code mapping, we should find parallel")
    print("morphological patterns: if ch+ol(A) = ch+edy(B), then sh+ol(A) = sh+edy(B)")
    print(f"{'='*90}")

    # If the mapping is: A uses -ol/-or suffix where B uses -edy/-eedy suffix,
    # then we should see parallel pairs across all prefixes

    morpho_pairs_hypothesis = {
        'ol': 'edy',    # chol<->chedy hypothesis
        'or': 'eey',    # alternative
        'ol': 'edy',
    }

    print(f"\n--- Testing hypothesis: A suffix '-ol' = B suffix '-edy' ---")
    print(f"{'A_word':<15} {'A_count':>8} | {'B_word':<15} {'B_count':>8} | {'A/B':>6}")
    print("-" * 65)

    # Find all A words ending in 'ol' and check if B has corresponding 'edy' word
    a_ol_words = [w for w in a_counter if w.endswith('ol') and a_counter[w] >= 3]
    a_ol_words.sort(key=lambda w: -a_counter[w])

    for a_w in a_ol_words[:20]:
        # Construct B equivalent: replace 'ol' with 'edy'
        stem = a_w[:-2]
        b_equivalent = stem + 'edy'
        a_c = a_counter[a_w]
        b_c = b_counter.get(b_equivalent, 0)
        if b_c > 0:
            ratio = a_c / b_c
            print(f"{a_w:<15} {a_c:>8} | {b_equivalent:<15} {b_c:>8} | {ratio:>6.2f}")
        else:
            print(f"{a_w:<15} {a_c:>8} | {b_equivalent:<15} {'(0)':>8} |   N/A")

    print(f"\n--- Testing hypothesis: A suffix '-or' = B suffix '-edy' ---")
    a_or_words = [w for w in a_counter if w.endswith('or') and a_counter[w] >= 3]
    a_or_words.sort(key=lambda w: -a_counter[w])

    for a_w in a_or_words[:20]:
        stem = a_w[:-2]
        b_equivalent = stem + 'edy'
        a_c = a_counter[a_w]
        b_c = b_counter.get(b_equivalent, 0)
        if b_c > 0:
            ratio = a_c / b_c
            print(f"{a_w:<15} {a_c:>8} | {b_equivalent:<15} {b_c:>8} | {ratio:>6.2f}")
        else:
            print(f"{a_w:<15} {a_c:>8} | {b_equivalent:<15} {'(0)':>8} |   N/A")

    # Try all suffix transformations
    print(f"\n--- Testing ALL suffix mappings systematically ---")
    suffix_maps = [
        ('ol', 'edy'), ('ol', 'eedy'), ('ol', 'dy'), ('ol', 'ey'),
        ('or', 'edy'), ('or', 'eedy'), ('or', 'dy'), ('or', 'ey'),
        ('al', 'edy'), ('al', 'eedy'),
        ('y', 'dy'), ('y', 'edy'),
        ('o', 'edy'), ('o', 'dy'),
    ]

    print(f"{'Mapping':<15} {'Pairs_found':>12} {'Avg_A/B_ratio':>14} {'Example':>30}")
    print("-" * 75)

    for a_suf, b_suf in suffix_maps:
        pairs = []
        for a_w in a_counter:
            if a_w.endswith(a_suf) and a_counter[a_w] >= 3:
                stem = a_w[:-len(a_suf)]
                b_w = stem + b_suf
                b_c = b_counter.get(b_w, 0)
                if b_c >= 2:
                    pairs.append((a_w, b_w, a_counter[a_w], b_c))

        if pairs:
            avg_ratio = sum(ac/bc for _, _, ac, bc in pairs) / len(pairs)
            best = max(pairs, key=lambda x: x[2] + x[3])
            print(f"{a_suf}->{b_suf:<10} {len(pairs):>12} {avg_ratio:>14.2f} {best[0]}({best[2]})<->{best[1]}({best[3]})")

    # ================================================================
    # TEST 7: CROSS-REFERENCE WITH PAGE CONTENT
    # ================================================================
    print(f"\n{'='*90}")
    print("TEST 7: PAGE-LEVEL CO-OCCURRENCE PATTERNS")
    print("For each A herbal page with high 'chol', show the corresponding")
    print("B herbal page in the same quire and its vocabulary.")
    print(f"{'='*90}")

    # Group herbal folios by quire
    quire_folios = defaultdict(lambda: {'A': [], 'B': []})
    for f, d in pages.items():
        if d['illust'] == 'H' and d['quire'] and d['lang']:
            quire_folios[d['quire']][d['lang']].append(f)

    print(f"\n--- Herbal pages by quire ---")
    for q in sorted(quire_folios.keys()):
        qf = quire_folios[q]
        if qf['A'] or qf['B']:
            a_list = sorted(qf['A'])
            b_list = sorted(qf['B'])
            print(f"\n  Quire {q}:")
            if a_list:
                print(f"    A: {', '.join(a_list)}")
            if b_list:
                print(f"    B: {', '.join(b_list)}")

            # Show top words for A and B pages in this quire
            a_words_q = []
            b_words_q = []
            for f in a_list:
                if f in pages:
                    a_words_q.extend(pages[f]['words'])
            for f in b_list:
                if f in pages:
                    b_words_q.extend(pages[f]['words'])

            if a_words_q:
                top_a = Counter(a_words_q).most_common(8)
                print(f"    A top words: {', '.join(f'{w}({c})' for w, c in top_a)}")
            if b_words_q:
                top_b = Counter(b_words_q).most_common(8)
                print(f"    B top words: {', '.join(f'{w}({c})' for w, c in top_b)}")

    # ================================================================
    # TEST 8: BIGRAM CONTEXT COMPARISON
    # ================================================================
    print(f"\n{'='*90}")
    print("TEST 8: BIGRAM PATTERNS")
    print("If chol(A) = chedy(B), then 'X chol' bigrams in A should have")
    print("parallel 'X chedy' (or 'Y chedy') bigrams in B.")
    print(f"{'='*90}")

    def get_bigrams_containing(word, lang_pages):
        """Get all bigrams containing the target word."""
        left_bg = Counter()   # (prev_word, target)
        right_bg = Counter()  # (target, next_word)
        for folio, data in lang_pages.items():
            for line in data['lines']:
                for i, w in enumerate(line):
                    if w == word:
                        if i > 0:
                            left_bg[line[i-1]] += 1
                        if i < len(line) - 1:
                            right_bg[line[i+1]] += 1
        return left_bg, right_bg

    for a_word, b_word in [('chol', 'chedy'), ('chor', 'shedy'), ('shol', 'qokedy'), ('daiin', 'daiin')]:
        a_left_bg, a_right_bg = get_bigrams_containing(a_word, a_pages)
        b_left_bg, b_right_bg = get_bigrams_containing(b_word, b_pages)

        print(f"\n  === Bigrams for {a_word}(A) vs {b_word}(B) ===")
        print(f"  Top 'X {a_word}' in A  vs  Top 'X {b_word}' in B:")
        a_top = a_left_bg.most_common(8)
        b_top = b_left_bg.most_common(8)
        for i in range(max(len(a_top), len(b_top))):
            a_str = f"{a_top[i][0]:<12} {a_top[i][1]:>4}" if i < len(a_top) else " " * 17
            b_str = f"{b_top[i][0]:<12} {b_top[i][1]:>4}" if i < len(b_top) else ""
            print(f"    {a_str}  |  {b_str}")

        print(f"  Top '{a_word} X' in A  vs  Top '{b_word} X' in B:")
        a_top = a_right_bg.most_common(8)
        b_top = b_right_bg.most_common(8)
        for i in range(max(len(a_top), len(b_top))):
            a_str = f"{a_top[i][0]:<12} {a_top[i][1]:>4}" if i < len(a_top) else " " * 17
            b_str = f"{b_top[i][0]:<12} {b_top[i][1]:>4}" if i < len(b_top) else ""
            print(f"    {a_str}  |  {b_str}")

    # ================================================================
    # SYNTHESIS
    # ================================================================
    print(f"\n{'='*90}")
    print("SYNTHESIS: WHICH PAIRS SURVIVE?")
    print(f"{'='*90}")

    # Compute composite score for each pair
    print(f"\n{'Pair':<25} {'Pos_sim':>8} {'L_Jacc':>8} {'R_Jacc':>8} {'Freq_dev':>9} {'Score':>7} {'Verdict':<12}")
    print("-" * 90)

    for a_word, b_word in candidate_pairs:
        # Position similarity
        a_pos, a_total = get_position_distribution(a_word, a_pages)
        b_pos, b_total = get_position_distribution(b_word, b_pages)
        pos_sim = position_similarity(a_pos, a_total, b_pos, b_total)

        # Neighbor overlap
        a_left, a_right, a_n = get_neighbors(a_word, a_pages)
        b_left, b_right, b_n = get_neighbors(b_word, b_pages)
        shared_left = set(a_left.keys()) & set(b_left.keys())
        shared_right = set(a_right.keys()) & set(b_right.keys())
        all_left = set(a_left.keys()) | set(b_left.keys())
        all_right = set(a_right.keys()) | set(b_right.keys())
        l_jacc = len(shared_left) / len(all_left) if all_left else 0
        r_jacc = len(shared_right) / len(all_right) if all_right else 0

        # Frequency deviation from expected ratio
        a_c = a_counter.get(a_word, 0)
        b_c = b_counter.get(b_word, 0)
        if b_c > 0:
            obs_ratio = a_c / b_c
            freq_dev = abs(obs_ratio / ab_ratio - 1.0)  # 0 = perfect match
        else:
            freq_dev = 9.99

        # Composite score (higher = more likely equivalent)
        score = pos_sim * 0.3 + (l_jacc + r_jacc) * 0.2 + max(0, 1 - freq_dev) * 0.3

        if a_word == b_word:
            verdict = "CONTROL"
        elif score > 0.5:
            verdict = "STRONG"
        elif score > 0.3:
            verdict = "PLAUSIBLE"
        elif score > 0.15:
            verdict = "WEAK"
        else:
            verdict = "REJECTED"

        print(f"{a_word}(A)={b_word}(B)   {pos_sim:>8.3f} {l_jacc:>8.3f} {r_jacc:>8.3f} {freq_dev:>9.3f} {score:>7.3f} {verdict:<12}")

    # ================================================================
    # WHAT IS X? Cross-reference with plant identifications
    # ================================================================
    print(f"\n{'='*90}")
    print("WHAT ITALIAN WORD COULD X BE?")
    print("If chol(A) = chedy(B) = Italian word X, what constraints do we have?")
    print(f"{'='*90}")

    print(f"""
FREQUENCY ANALYSIS:
  chol appears {a_counter.get('chol',0)} times in A ({a_counter.get('chol',0)/total_a*100:.2f}% of A text)
  chedy appears {b_counter.get('chedy',0)} times in B ({b_counter.get('chedy',0)/total_b*100:.2f}% of B text)

  In 15th-century Italian herbal texts, words at ~2% frequency include:
  - "erba/herba" (herb) - ~1-3% in herbals
  - "foglia/foglie" (leaf/leaves) - ~1-2%
  - "radice" (root) - ~0.5-1.5%
  - "acqua" (water) - ~0.5-2% in pharmaceutical texts
  - "fiore" (flower) - ~0.5-1.5%
  - "seme" (seed) - ~0.3-1%

  The word appears in herbal, pharmaceutical, AND other sections.
  It appears line-internally (not restricted to first/last position).
  It has the prefix 'ch-', which may indicate a grammatical category.

POSITIONAL CONSTRAINTS:
  chol is NOT predominantly first-word or last-word on lines.
  It appears throughout the line, suggesting it's a CONTENT word, not a syntactic marker.

  Most common bigrams suggest it appears after:
""")

    # Show what precedes chol most often
    chol_left, chol_right = get_bigrams_containing('chol', a_pages)
    print("  Words most often BEFORE chol(A):")
    for w, c in chol_left.most_common(10):
        print(f"    {w}: {c} times")
    print("\n  Words most often AFTER chol(A):")
    for w, c in chol_right.most_common(10):
        print(f"    {w}: {c} times")

    # Same for chedy
    chedy_left, chedy_right = get_bigrams_containing('chedy', b_pages)
    print("\n  Words most often BEFORE chedy(B):")
    for w, c in chedy_left.most_common(10):
        print(f"    {w}: {c} times")
    print("\n  Words most often AFTER chedy(B):")
    for w, c in chedy_right.most_common(10):
        print(f"    {w}: {c} times")

    # ================================================================
    # BONUS: Find the BEST pairs using algorithmic matching
    # ================================================================
    print(f"\n{'='*90}")
    print("BONUS: ALGORITHMIC BEST-PAIR DISCOVERY")
    print("Finding A-dominant and B-dominant words with highest composite")
    print("equivalence score (position + context + frequency matching).")
    print(f"{'='*90}")

    # Get A-dominant words (at least 5x more frequent in A relative to corpus size)
    a_dominant = []
    for w in a_counter:
        a_c = a_counter[w]
        b_c = b_counter.get(w, 0)
        if a_c >= 10:
            a_rate = a_c / total_a
            b_rate = b_c / total_b if total_b > 0 else 0
            if b_rate == 0 or a_rate / b_rate >= 3:
                a_dominant.append(w)

    b_dominant = []
    for w in b_counter:
        b_c = b_counter[w]
        a_c = a_counter.get(w, 0)
        if b_c >= 10:
            b_rate = b_c / total_b
            a_rate = a_c / total_a if total_a > 0 else 0
            if a_rate == 0 or b_rate / a_rate >= 3:
                b_dominant.append(w)

    print(f"\nA-dominant words (>=10 occ, >=3x relative freq): {len(a_dominant)}")
    print(f"B-dominant words (>=10 occ, >=3x relative freq): {len(b_dominant)}")

    # Score all combinations
    best_pairs = []
    for a_w in a_dominant:
        a_pos, a_pos_total = get_position_distribution(a_w, a_pages)
        a_left, a_right, a_n = get_neighbors(a_w, a_pages)

        for b_w in b_dominant:
            b_pos, b_pos_total = get_position_distribution(b_w, b_pages)
            b_left, b_right, b_n = get_neighbors(b_w, b_pages)

            # Position similarity
            pos_sim = position_similarity(a_pos, a_pos_total, b_pos, b_pos_total)

            # Neighbor overlap (weighted by frequency)
            shared_l = set(a_left.keys()) & set(b_left.keys())
            shared_r = set(a_right.keys()) & set(b_right.keys())
            all_l = set(a_left.keys()) | set(b_left.keys())
            all_r = set(a_right.keys()) | set(b_right.keys())
            l_j = len(shared_l) / len(all_l) if all_l else 0
            r_j = len(shared_r) / len(all_r) if all_r else 0

            # Frequency match
            a_c = a_counter[a_w]
            b_c = b_counter[b_w]
            obs_r = a_c / b_c if b_c > 0 else 999
            freq_dev = abs(obs_r / ab_ratio - 1.0)

            # Score
            score = pos_sim * 0.3 + (l_j + r_j) * 0.2 + max(0, 1 - freq_dev) * 0.3
            best_pairs.append((a_w, b_w, score, pos_sim, l_j, r_j, freq_dev, a_c, b_c))

    best_pairs.sort(key=lambda x: -x[2])

    print(f"\n--- TOP 30 BEST MATCHED PAIRS ---")
    print(f"{'A_word':<15} {'B_word':<15} {'Score':>6} {'Pos':>6} {'L_J':>6} {'R_J':>6} {'F_dev':>7} {'A_n':>5} {'B_n':>5}")
    print("-" * 90)
    for a_w, b_w, sc, ps, lj, rj, fd, ac, bc in best_pairs[:30]:
        print(f"{a_w:<15} {b_w:<15} {sc:>6.3f} {ps:>6.3f} {lj:>6.3f} {rj:>6.3f} {fd:>7.3f} {ac:>5} {bc:>5}")


if __name__ == '__main__':
    main()
