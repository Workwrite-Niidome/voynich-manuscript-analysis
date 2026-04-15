#!/usr/bin/env python3
"""
Voynich Manuscript n/l/r suffix sandhi analysis - v2 (fixed word extraction).
"""

import re
import math
from collections import Counter, defaultdict


def parse_voynich(filepath):
    lines_data = []
    current_folio = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            folio_match = re.match(r'<(f\d+[rv]\d?)>\s', line)
            if folio_match:
                current_folio = folio_match.group(1)
                continue
            line_match = re.match(r'<(f\d+[rv]\d?)\.(\d+),([^>]+)>\s+(.*)', line)
            if line_match:
                folio = line_match.group(1)
                line_num = int(line_match.group(2))
                line_type = line_match.group(3)
                text = line_match.group(4)
                current_folio = folio
                lines_data.append({
                    'folio': folio, 'line_num': line_num,
                    'line_type': line_type, 'text': text,
                })
    return lines_data


def extract_words(text):
    """Extract clean words from EVA text. Dots are word separators."""
    # Replace <-> with space (line break marker)
    text = text.replace('<->', ' ')
    # Split on dots and whitespace FIRST (these are word separators)
    tokens = re.split(r'[\s.]+', text)
    words = []
    for tok in tokens:
        # Remove annotations
        tok = re.sub(r'\{[^}]+\}', '', tok)
        tok = re.sub(r'@\d+;?', '', tok)
        tok = re.sub(r'[,?!\'"*]', '', tok)
        # Only keep pure EVA character words
        if tok and re.match(r'^[a-z]+$', tok):
            words.append(tok)
    return words


def get_suffix(word):
    if word and word[-1] in ('n', 'l', 'r'):
        return word[-1]
    return None


def get_stem(word):
    if word and word[-1] in ('n', 'l', 'r'):
        return word[:-1]
    return word


def compute_mi(x_counts, y_counts, joint_counts, total):
    mi = 0.0
    for (x, y), count in joint_counts.items():
        p_xy = count / total
        p_x = x_counts[x] / total
        p_y = y_counts[y] / total
        if p_xy > 0 and p_x > 0 and p_y > 0:
            mi += p_xy * math.log2(p_xy / (p_x * p_y))
    return mi


def main():
    filepath = "C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt"
    lines_data = parse_voynich(filepath)

    # Build flat word list with metadata
    all_words = []
    for ld in lines_data:
        words = extract_words(ld['text'])
        for i, w in enumerate(words):
            all_words.append({
                'word': w, 'folio': ld['folio'],
                'line_num': ld['line_num'],
                'is_line_end': (i == len(words) - 1),
                'is_line_start': (i == 0),
                'line_type': ld['line_type'],
            })

    total_words = len(all_words)
    print(f"Total words extracted: {total_words}")

    # Verify extraction
    wc = Counter(w['word'] for w in all_words)
    print(f"Unique words: {len(wc)}")
    print(f"Top 20 words: {wc.most_common(20)}")

    # NLR words
    nlr_words = [(i, w) for i, w in enumerate(all_words) if get_suffix(w['word'])]
    suffix_counts = Counter(get_suffix(w['word']) for _, w in nlr_words)
    total_nlr = sum(suffix_counts.values())
    print(f"\nWords ending in n/l/r: {total_nlr}")
    baseline_n = suffix_counts['n'] / total_nlr
    baseline_l = suffix_counts['l'] / total_nlr
    baseline_r = suffix_counts['r'] / total_nlr
    print(f"Baseline: n={baseline_n:.1%}, l={baseline_l:.1%}, r={baseline_r:.1%}")

    # ============================================================
    # 1. COMPLETE SANDHI RULE TABLE
    # ============================================================
    print("\n" + "="*80)
    print("1. COMPLETE SANDHI RULE TABLE")
    print("="*80)

    sandhi_data = []
    for idx, w in nlr_words:
        if idx + 1 >= len(all_words):
            continue
        nw = all_words[idx + 1]
        if w['folio'] != nw['folio']:
            continue
        suffix = get_suffix(w['word'])
        stem = get_stem(w['word'])
        next_init = nw['word'][0]
        sandhi_data.append({
            'suffix': suffix, 'next_init': next_init, 'stem': stem,
            'word': w['word'], 'next_word': nw['word'],
            'is_line_end': w['is_line_end'],
            'is_line_start': w['is_line_start'],
        })

    print(f"Pairs analyzed: {len(sandhi_data)}")

    by_next_init = defaultdict(lambda: Counter())
    for sd in sandhi_data:
        by_next_init[sd['next_init']][sd['suffix']] += 1

    sorted_initials = sorted(by_next_init.keys(), key=lambda x: sum(by_next_init[x].values()), reverse=True)

    sandhi_table = []
    print(f"\n{'Next':>6} {'Total':>6} {'P(n)':>8} {'P(l)':>8} {'P(r)':>8} {'Dominant':>10} {'Lift':>8}")
    print("-" * 62)

    for init in sorted_initials:
        counts = by_next_init[init]
        total = sum(counts.values())
        if total < 5:
            continue
        pn = counts['n'] / total
        pl = counts['l'] / total
        pr = counts['r'] / total
        probs = {'n': pn, 'l': pl, 'r': pr}
        baselines = {'n': baseline_n, 'l': baseline_l, 'r': baseline_r}
        dominant = max(probs, key=probs.get)
        lift = probs[dominant] / baselines[dominant]
        print(f"{init:>6} {total:>6} {pn:>8.1%} {pl:>8.1%} {pr:>8.1%} {dominant:>10} {lift:>8.2f}x")
        sandhi_table.append({
            'initial': init, 'total': total,
            'p_n': pn, 'p_l': pl, 'p_r': pr,
            'dominant': dominant, 'lift': lift,
        })

    # ============================================================
    # 2. PHONOLOGICAL CLASS ANALYSIS
    # ============================================================
    print("\n" + "="*80)
    print("2. PHONOLOGICAL CLASS ANALYSIS")
    print("="*80)

    broad_groups = {
        'vowels (a,o,e,i)': ['a', 'o', 'e', 'i'],
        'voiceless stops (k,t,p)': ['k', 't', 'p'],
        'voiced stops (d,g,b)': ['d', 'g', 'b'],
        'fricatives (s,f,c,h)': ['s', 'f', 'c', 'h'],
        'nasals (n,m)': ['n', 'm'],
        'liquids (l,r)': ['l', 'r'],
        'semivowel (y)': ['y'],
        'q-ligature (q)': ['q'],
        'j (j)': ['j'],
    }

    print(f"\n{'Group':>30} {'Total':>6} {'P(n)':>8} {'P(l)':>8} {'P(r)':>8} {'Dominant':>10}")
    print("-" * 75)

    broad_results = []
    for group_name, chars in broad_groups.items():
        combined = Counter()
        for ch in chars:
            if ch in by_next_init:
                combined += by_next_init[ch]
        total = sum(combined.values())
        if total < 5:
            continue
        pn = combined['n'] / total
        pl = combined['l'] / total
        pr = combined['r'] / total
        dominant = max({'n': pn, 'l': pl, 'r': pr}, key={'n': pn, 'l': pl, 'r': pr}.get)
        print(f"{group_name:>30} {total:>6} {pn:>8.1%} {pl:>8.1%} {pr:>8.1%} {dominant:>10}")
        broad_results.append({'group': group_name, 'total': total, 'pn': pn, 'pl': pl, 'pr': pr, 'dominant': dominant})

    # ============================================================
    # 3. STEM + NEXT-WORD INTERACTION
    # ============================================================
    print("\n" + "="*80)
    print("3. STEM + NEXT-WORD INTERACTION")
    print("="*80)

    # Find stems that show alternation
    stem_suffix = defaultdict(lambda: Counter())
    stem_sandhi = defaultdict(lambda: defaultdict(lambda: Counter()))

    for sd in sandhi_data:
        stem_suffix[sd['stem']][sd['suffix']] += 1
        stem_sandhi[sd['stem']][sd['next_init']][sd['suffix']] += 1

    # Stems with >= 10 total and >= 2 suffix types
    alternating = {s: c for s, c in stem_suffix.items()
                   if sum(c.values()) >= 8 and len(c) >= 2}

    print(f"\nAlternating stems (>=8 occurrences, >=2 suffixes):")
    print(f"{'Stem':>15} {'Total':>6} {'n':>5} {'l':>5} {'r':>5} {'Default':>8}")
    print("-" * 50)

    for stem in sorted(alternating, key=lambda s: sum(alternating[s].values()), reverse=True):
        counts = alternating[stem]
        total = sum(counts.values())
        default = counts.most_common(1)[0][0]
        print(f"{stem:>15} {total:>6} {counts.get('n',0):>5} {counts.get('l',0):>5} {counts.get('r',0):>5} {default:>8}")

        # Show sandhi for this stem
        ss = stem_sandhi[stem]
        for init in sorted(ss.keys(), key=lambda x: sum(ss[x].values()), reverse=True):
            sc = ss[init]
            st = sum(sc.values())
            if st < 2:
                continue
            dom = sc.most_common(1)[0][0]
            override = " <<< OVERRIDE" if dom != default else ""
            detail = ', '.join(f"{k}={v}" for k, v in sorted(sc.items()))
            print(f"  before {init}-: {detail} (n={st}){override}")

    # Also check stems with >= 5 occurrences
    print(f"\n\nAll stems >= 5 occurrences:")
    all_stems_5 = {s: c for s, c in stem_suffix.items() if sum(c.values()) >= 5}
    for stem in sorted(all_stems_5, key=lambda s: sum(all_stems_5[s].values()), reverse=True)[:30]:
        counts = all_stems_5[stem]
        total = sum(counts.values())
        default = counts.most_common(1)[0][0]
        n_types = len(counts)
        print(f"  {stem:>15} {total:>5} n={counts.get('n',0):>3} l={counts.get('l',0):>3} r={counts.get('r',0):>3} (default={default}, types={n_types})")

    # ============================================================
    # 4. PAUSE/BOUNDARY MARKING
    # ============================================================
    print("\n" + "="*80)
    print("4. PAUSE/BOUNDARY MARKING")
    print("="*80)

    # Line position analysis
    positions = {
        'line-final': Counter(),
        'non-line-final': Counter(),
        'line-initial': Counter(),
        'non-line-initial': Counter(),
    }

    for w in all_words:
        s = get_suffix(w['word'])
        if s is None:
            continue
        if w['is_line_end']:
            positions['line-final'][s] += 1
        else:
            positions['non-line-final'][s] += 1
        if w['is_line_start']:
            positions['line-initial'][s] += 1
        else:
            positions['non-line-initial'][s] += 1

    print(f"\n{'Position':>20} {'Total':>6} {'P(n)':>8} {'P(l)':>8} {'P(r)':>8}")
    print("-" * 55)
    for pos_name, counts in positions.items():
        total = sum(counts.values())
        if total == 0:
            continue
        print(f"{pos_name:>20} {total:>6} {counts['n']/total:>8.1%} {counts['l']/total:>8.1%} {counts['r']/total:>8.1%}")

    # Folio boundaries
    folio_final = Counter()
    folio_initial = Counter()
    for i, w in enumerate(all_words):
        s = get_suffix(w['word'])
        if s is None:
            continue
        # Folio-final: last word before folio change
        if i < len(all_words) - 1 and all_words[i+1]['folio'] != w['folio']:
            folio_final[s] += 1
        # Folio-initial: first word of a folio
        if i == 0 or all_words[i-1]['folio'] != w['folio']:
            folio_initial[s] += 1

    for label, counts in [('folio-final', folio_final), ('folio-initial', folio_initial)]:
        total = sum(counts.values())
        if total > 0:
            print(f"{label:>20} {total:>6} {counts['n']/total:>8.1%} {counts['l']/total:>8.1%} {counts['r']/total:>8.1%}")

    # Paragraph boundaries
    para_final = Counter()
    para_initial = Counter()
    for i in range(len(lines_data)):
        ld = lines_data[i]
        words = extract_words(ld['text'])
        if not words:
            continue

        # Check if this is a paragraph-initial line
        is_para_start = ld['line_type'].startswith('@P') or ld['line_type'].startswith('*P')
        if is_para_start:
            s = get_suffix(words[0])
            if s:
                para_initial[s] += 1

        # Check if next line is a paragraph start (making this line para-final)
        if i < len(lines_data) - 1:
            next_ld = lines_data[i + 1]
            next_is_para = next_ld['line_type'].startswith('@P') or next_ld['line_type'].startswith('*P')
            next_is_new_folio = next_ld['folio'] != ld['folio']
            if next_is_para or next_is_new_folio:
                s = get_suffix(words[-1])
                if s:
                    para_final[s] += 1

    for label, counts in [('para-final', para_final), ('para-initial', para_initial)]:
        total = sum(counts.values())
        if total > 0:
            print(f"{label:>20} {total:>6} {counts['n']/total:>8.1%} {counts['l']/total:>8.1%} {counts['r']/total:>8.1%}")

    # Label/title lines (=Pt, @L*, etc.)
    label_words = Counter()
    for ld in lines_data:
        if '=P' in ld['line_type'] or '@L' in ld['line_type'] or '*L' in ld['line_type']:
            words = extract_words(ld['text'])
            for w in words:
                s = get_suffix(w)
                if s:
                    label_words[s] += 1

    total_lw = sum(label_words.values())
    if total_lw > 0:
        print(f"{'label/title lines':>20} {total_lw:>6} {label_words['n']/total_lw:>8.1%} {label_words['l']/total_lw:>8.1%} {label_words['r']/total_lw:>8.1%}")

    # ============================================================
    # 5. MUTUAL INFORMATION
    # ============================================================
    print("\n" + "="*80)
    print("5. MUTUAL INFORMATION & STATISTICS")
    print("="*80)

    # MI: suffix vs next_initial
    suffix_c = Counter()
    next_c = Counter()
    joint_sn = Counter()
    for sd in sandhi_data:
        suffix_c[sd['suffix']] += 1
        next_c[sd['next_init']] += 1
        joint_sn[(sd['suffix'], sd['next_init'])] += 1

    mi_next = compute_mi(suffix_c, next_c, joint_sn, len(sandhi_data))
    print(f"MI(suffix, next_initial) = {mi_next:.4f} bits")

    # MI: suffix vs stem
    stem_c = Counter()
    joint_ss = Counter()
    for sd in sandhi_data:
        stem_c[sd['stem']] += 1
        joint_ss[(sd['suffix'], sd['stem'])] += 1

    mi_stem = compute_mi(suffix_c, stem_c, joint_ss, len(sandhi_data))
    print(f"MI(suffix, stem) = {mi_stem:.4f} bits")

    print(f"\nRatio MI(stem)/MI(next): {mi_stem/mi_next:.1f}x")
    print("(stem identity is much stronger predictor than sandhi)")

    # Chi-squared
    top_initials = [init for init in sorted_initials if sum(by_next_init[init].values()) >= 20]
    suffixes = ['n', 'l', 'r']
    col_totals = Counter()
    row_totals = {}
    grand_total = 0
    for init in top_initials:
        row_totals[init] = sum(by_next_init[init].values())
        grand_total += row_totals[init]
        for s in suffixes:
            col_totals[s] += by_next_init[init].get(s, 0)

    chi2 = 0
    for init in top_initials:
        for s in suffixes:
            obs = by_next_init[init].get(s, 0)
            exp = (row_totals[init] * col_totals[s]) / grand_total if grand_total else 0
            if exp > 0:
                chi2 += (obs - exp) ** 2 / exp

    df = (len(top_initials) - 1) * 2
    print(f"\nChi-squared = {chi2:.1f}, df = {df}")
    print(f"Critical value at p<0.001 ~ {df + 3*math.sqrt(2*df):.0f}")
    print(f"Result: {'HIGHLY SIGNIFICANT' if chi2 > df + 3*math.sqrt(2*df) else 'check p-value table'}")

    # Cramers V
    k = min(len(top_initials), 3)
    cramers_v = math.sqrt(chi2 / (grand_total * (k - 1))) if grand_total > 0 and k > 1 else 0
    print(f"Cramer's V = {cramers_v:.3f} (effect size: {'small' if cramers_v < 0.1 else 'medium' if cramers_v < 0.3 else 'large'})")

    # ============================================================
    # 6. MOST COMMON WORD FORMS
    # ============================================================
    print("\n" + "="*80)
    print("6. WORD FREQUENCY ANALYSIS")
    print("="*80)

    for suffix_label, suffix_char in [('-n', 'n'), ('-l', 'l'), ('-r', 'r')]:
        words_with = Counter()
        for w in all_words:
            if get_suffix(w['word']) == suffix_char:
                words_with[w['word']] += 1
        print(f"\nTop 20 {suffix_label} words:")
        for word, count in words_with.most_common(20):
            print(f"  {word}: {count}")

    # ============================================================
    # 7. CROSS-LINE vs WITHIN-LINE COMPARISON
    # ============================================================
    print("\n" + "="*80)
    print("7. CROSS-LINE vs WITHIN-LINE SANDHI")
    print("="*80)

    cross = defaultdict(lambda: Counter())
    within = defaultdict(lambda: Counter())

    for sd in sandhi_data:
        if sd['is_line_end']:
            cross[sd['next_init']][sd['suffix']] += 1
        else:
            within[sd['next_init']][sd['suffix']] += 1

    print(f"\n{'Init':>6} {'Context':>15} {'Total':>6} {'P(n)':>8} {'P(l)':>8} {'P(r)':>8}")
    print("-" * 60)
    for init in ['o', 's', 'd', 'c', 'k', 'p', 'q', 't', 'y', 'a']:
        for label, data in [('within-line', within), ('cross-line', cross)]:
            if init in data:
                c = data[init]
                t = sum(c.values())
                if t >= 5:
                    print(f"{init:>6} {label:>15} {t:>6} {c.get('n',0)/t:>8.1%} {c.get('l',0)/t:>8.1%} {c.get('r',0)/t:>8.1%}")


if __name__ == '__main__':
    main()
