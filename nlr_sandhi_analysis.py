#!/usr/bin/env python3
"""
Voynich Manuscript n/l/r suffix sandhi analysis.
Analyzes word-final n/l/r alternation patterns relative to the following word's initial character.
"""

import re
import json
from collections import Counter, defaultdict
import math

def parse_voynich(filepath):
    """Parse EVA transcription, return list of (folio, line_num, words, is_paragraph_start, line_type)."""
    lines_data = []
    current_folio = None
    prev_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Folio header
            folio_match = re.match(r'<(f\d+[rv]\d?)>\s', line)
            if folio_match:
                prev_folio = current_folio
                current_folio = folio_match.group(1)
                continue

            # Content line
            line_match = re.match(r'<(f\d+[rv]\d?)\.(\d+),([^>]+)>\s+(.*)', line)
            if line_match:
                folio = line_match.group(1)
                line_num = int(line_match.group(2))
                line_type = line_match.group(3)
                text = line_match.group(4)

                is_folio_start = (folio != prev_folio and line_num <= 1) or (line_num == 1)
                prev_folio = folio
                current_folio = folio

                lines_data.append({
                    'folio': folio,
                    'line_num': line_num,
                    'line_type': line_type,
                    'text': text,
                    'is_folio_start': is_folio_start,
                })

    return lines_data


def extract_words(text):
    """Extract clean words from a line of EVA text."""
    # Remove annotations like {cto}, @221;, @152;, etc.
    text = re.sub(r'\{[^}]+\}', '', text)
    text = re.sub(r'@\d+;?', '', text)
    text = re.sub(r'<->', ' ', text)  # line breaks within bifolios
    text = re.sub(r'[,?.!\'"]', '', text)
    # Split on dots and spaces
    words = re.split(r'[\s.]+', text)
    # Filter: only keep words with EVA chars
    words = [w for w in words if w and re.match(r'^[a-z]+$', w)]
    return words


def get_suffix_type(word):
    """Check if word ends in n, l, or r. Return the suffix or None."""
    if not word:
        return None
    last = word[-1]
    if last in ('n', 'l', 'r'):
        return last
    return None


def get_stem(word):
    """Get stem by removing final n/l/r."""
    if word and word[-1] in ('n', 'l', 'r'):
        return word[:-1]
    return word


def compute_mi(x_counts, y_counts, joint_counts, total):
    """Compute mutual information."""
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

    # Build a flat list of all words with metadata
    all_words_flat = []  # (word, folio, line_num, is_line_start, is_line_end, line_type, is_folio_start)

    for ld in lines_data:
        words = extract_words(ld['text'])
        for i, w in enumerate(words):
            all_words_flat.append({
                'word': w,
                'folio': ld['folio'],
                'line_num': ld['line_num'],
                'is_line_start': (i == 0),
                'is_line_end': (i == len(words) - 1),
                'line_type': ld['line_type'],
                'is_folio_start': ld['is_folio_start'] and i == 0,
            })

    print(f"Total words extracted: {len(all_words_flat)}")

    # Count words ending in n/l/r
    nlr_words = [w for w in all_words_flat if get_suffix_type(w['word'])]
    print(f"Words ending in n/l/r: {len(nlr_words)}")

    suffix_counts = Counter(get_suffix_type(w['word']) for w in nlr_words)
    total_nlr = sum(suffix_counts.values())
    print(f"Baseline: n={suffix_counts['n']/total_nlr:.1%}, l={suffix_counts['l']/total_nlr:.1%}, r={suffix_counts['r']/total_nlr:.1%}")

    # ============================================================
    # 1. COMPLETE SANDHI RULE TABLE
    # ============================================================
    print("\n" + "="*80)
    print("1. COMPLETE SANDHI RULE TABLE")
    print("="*80)

    # For each word ending in n/l/r, find the next word
    sandhi_data = []  # (suffix, next_initial, stem, word, next_word)

    for i in range(len(all_words_flat) - 1):
        w = all_words_flat[i]
        nw = all_words_flat[i+1]
        suffix = get_suffix_type(w['word'])
        if suffix is None:
            continue
        # Only consider within-line or adjacent-line pairs
        # Skip if next word is on a different folio (major break)
        if w['folio'] != nw['folio']:
            continue
        next_initial = nw['word'][0] if nw['word'] else None
        if next_initial is None:
            continue
        stem = get_stem(w['word'])
        sandhi_data.append({
            'suffix': suffix,
            'next_initial': next_initial,
            'stem': stem,
            'word': w['word'],
            'next_word': nw['word'],
            'is_line_end': w['is_line_end'],
            'is_line_start': w['is_line_start'],
        })

    print(f"n/l/r words with a following word (same folio): {len(sandhi_data)}")

    # Group by next_initial
    by_next_init = defaultdict(lambda: Counter())
    for sd in sandhi_data:
        by_next_init[sd['next_initial']][sd['suffix']] += 1

    # Sort by frequency
    sorted_initials = sorted(by_next_init.keys(), key=lambda x: sum(by_next_init[x].values()), reverse=True)

    sandhi_table = []
    print(f"\n{'Next':>6} {'Total':>6} {'P(n)':>8} {'P(l)':>8} {'P(r)':>8} {'Dominant':>10} {'Lift':>8}")
    print("-" * 62)

    baseline_n = suffix_counts['n'] / total_nlr
    baseline_l = suffix_counts['l'] / total_nlr
    baseline_r = suffix_counts['r'] / total_nlr

    for init in sorted_initials:
        counts = by_next_init[init]
        total = sum(counts.values())
        if total < 5:
            continue
        pn = counts['n'] / total if total else 0
        pl = counts['l'] / total if total else 0
        pr = counts['r'] / total if total else 0

        # Find dominant and its lift over baseline
        probs = {'n': pn, 'l': pl, 'r': pr}
        baselines = {'n': baseline_n, 'l': baseline_l, 'r': baseline_r}
        dominant = max(probs, key=probs.get)
        lift = probs[dominant] / baselines[dominant] if baselines[dominant] > 0 else 0

        print(f"{init:>6} {total:>6} {pn:>8.1%} {pl:>8.1%} {pr:>8.1%} {dominant:>10} {lift:>8.2f}x")
        sandhi_table.append({
            'initial': init,
            'total': total,
            'p_n': pn, 'p_l': pl, 'p_r': pr,
            'dominant': dominant, 'lift': lift,
        })

    # ============================================================
    # 2. PHONOLOGICAL CLASS ANALYSIS
    # ============================================================
    print("\n" + "="*80)
    print("2. PHONOLOGICAL CLASS ANALYSIS")
    print("="*80)

    # EVA character phonological hypotheses
    # Based on common EVA-to-phoneme mappings
    eva_classes = {
        # Possible vowels
        'a': 'vowel', 'o': 'vowel', 'e': 'vowel', 'y': 'vowel/semivowel', 'i': 'vowel',
        # Possible stops
        'k': 'stop/velar', 't': 'stop/dental', 'd': 'stop/dental_voiced', 'p': 'stop/labial',
        'g': 'stop/velar_voiced', 'b': 'stop/labial_voiced',
        # Possible fricatives/continuants
        's': 'fricative/alveolar', 'f': 'fricative/labial', 'c': 'affricate/palatal',
        'h': 'fricative/glottal',
        # Liquids/nasals
        'l': 'liquid/lateral', 'r': 'liquid/rhotic', 'n': 'nasal', 'm': 'nasal/labial',
        # Other
        'q': 'stop/uvular_or_ligature', 'j': 'palatal',
    }

    # Group initials by phonological class
    class_groups = defaultdict(list)
    for init in sorted_initials:
        total = sum(by_next_init[init].values())
        if total < 5:
            continue
        cls = eva_classes.get(init, 'unknown')
        class_groups[cls].append(init)

    print("\nSuffix distribution by phonological class of following word:")
    print(f"\n{'Class':>25} {'Chars':>10} {'Total':>6} {'P(n)':>8} {'P(l)':>8} {'P(r)':>8}")
    print("-" * 75)

    class_results = []
    for cls in sorted(class_groups.keys()):
        chars = class_groups[cls]
        combined = Counter()
        for ch in chars:
            combined += by_next_init[ch]
        total = sum(combined.values())
        if total < 10:
            continue
        pn = combined['n'] / total
        pl = combined['l'] / total
        pr = combined['r'] / total
        char_str = ','.join(chars)
        print(f"{cls:>25} {char_str:>10} {total:>6} {pn:>8.1%} {pl:>8.1%} {pr:>8.1%}")
        class_results.append({'class': cls, 'chars': char_str, 'total': total, 'pn': pn, 'pl': pl, 'pr': pr})

    # Broader grouping
    print("\nBroad phonological grouping:")
    broad_groups = {
        'vowels': ['a', 'o', 'e', 'i'],
        'voiceless_stops': ['k', 't', 'p'],
        'voiced_stops': ['d', 'g', 'b'],
        'fricatives': ['s', 'f', 'c', 'h'],
        'nasals': ['n', 'm'],
        'liquids': ['l', 'r'],
        'semivowels': ['y'],
        'other': ['q', 'j'],
    }

    print(f"\n{'Group':>20} {'Total':>6} {'P(n)':>8} {'P(l)':>8} {'P(r)':>8} {'Dominant':>10}")
    print("-" * 62)

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
        print(f"{group_name:>20} {total:>6} {pn:>8.1%} {pl:>8.1%} {pr:>8.1%} {dominant:>10}")
        broad_results.append({'group': group_name, 'total': total, 'pn': pn, 'pl': pl, 'pr': pr, 'dominant': dominant})

    # ============================================================
    # 3. STEM + NEXT-WORD INTERACTION
    # ============================================================
    print("\n" + "="*80)
    print("3. STEM + NEXT-WORD INTERACTION")
    print("="*80)

    # Find top 10 stems
    stem_counter = Counter()
    for sd in sandhi_data:
        stem_counter[sd['stem']] += 1

    top_stems = stem_counter.most_common(20)
    print(f"\nTop 20 stems: {[(s, c) for s, c in top_stems]}")

    # For each top stem, show default suffix and how it changes by next_initial
    print(f"\n{'Stem':>15} {'Default':>10} {'Count':>6}")
    print("-" * 35)

    stem_details = {}
    for stem, count in top_stems[:10]:
        stem_suffixes = Counter()
        stem_sandhi = defaultdict(lambda: Counter())
        for sd in sandhi_data:
            if sd['stem'] == stem:
                stem_suffixes[sd['suffix']] += 1
                stem_sandhi[sd['next_initial']][sd['suffix']] += 1

        total = sum(stem_suffixes.values())
        default_suffix = stem_suffixes.most_common(1)[0][0]
        default_pct = stem_suffixes.most_common(1)[0][1] / total
        print(f"{stem:>15} {default_suffix} ({default_pct:.0%}){total:>6}")

        # Show override cases
        overrides = []
        for init in sorted(stem_sandhi.keys()):
            sc = stem_sandhi[init]
            st = sum(sc.values())
            if st < 3:
                continue
            dominant = sc.most_common(1)[0][0]
            if dominant != default_suffix:
                overrides.append(f"  before {init}-: {dominant} ({sc[dominant]}/{st})")

        if overrides:
            for ov in overrides:
                print(ov)

        stem_details[stem] = {
            'default': default_suffix,
            'default_pct': default_pct,
            'total': total,
            'suffixes': dict(stem_suffixes),
            'sandhi': {k: dict(v) for k, v in stem_sandhi.items()},
        }

    # ============================================================
    # 4. PAUSE/BOUNDARY MARKING (line-final, paragraph, folio)
    # ============================================================
    print("\n" + "="*80)
    print("4. PAUSE/BOUNDARY MARKING")
    print("="*80)

    # Line-final vs non-line-final
    line_final = Counter()
    non_line_final = Counter()
    line_start = Counter()
    non_line_start = Counter()

    for w in all_words_flat:
        s = get_suffix_type(w['word'])
        if s is None:
            continue
        if w['is_line_end']:
            line_final[s] += 1
        else:
            non_line_final[s] += 1
        if w['is_line_start']:
            line_start[s] += 1
        else:
            non_line_start[s] += 1

    print("\nLine-final suffix distribution:")
    tf = sum(line_final.values())
    tnf = sum(non_line_final.values())
    tls = sum(line_start.values())
    tnls = sum(non_line_start.values())

    print(f"{'Position':>20} {'Total':>6} {'P(n)':>8} {'P(l)':>8} {'P(r)':>8}")
    print("-" * 55)
    print(f"{'line-final':>20} {tf:>6} {line_final['n']/tf:>8.1%} {line_final['l']/tf:>8.1%} {line_final['r']/tf:>8.1%}")
    print(f"{'non-line-final':>20} {tnf:>6} {non_line_final['n']/tnf:>8.1%} {non_line_final['l']/tnf:>8.1%} {non_line_final['r']/tnf:>8.1%}")
    print(f"{'line-start':>20} {tls:>6} {line_start['n']/tls:>8.1%} {line_start['l']/tls:>8.1%} {line_start['r']/tls:>8.1%}")
    print(f"{'non-line-start':>20} {tnls:>6} {non_line_start['n']/tnls:>8.1%} {non_line_start['l']/tnls:>8.1%} {non_line_start['r']/tnls:>8.1%}")

    # Folio transitions: words at end of a folio
    folio_final = Counter()
    folio_start_words = Counter()

    # Detect folio changes
    for i, w in enumerate(all_words_flat):
        s = get_suffix_type(w['word'])
        if s is None:
            continue
        if w['is_folio_start']:
            folio_start_words[s] += 1
        # Check if next word is on a different folio
        if i < len(all_words_flat) - 1:
            if all_words_flat[i+1]['folio'] != w['folio'] and w['is_line_end']:
                folio_final[s] += 1

    if sum(folio_final.values()) > 0:
        tff = sum(folio_final.values())
        print(f"\n{'folio-final':>20} {tff:>6} {folio_final['n']/tff:>8.1%} {folio_final['l']/tff:>8.1%} {folio_final['r']/tff:>8.1%}")

    if sum(folio_start_words.values()) > 0:
        tfs = sum(folio_start_words.values())
        print(f"{'folio-start':>20} {tfs:>6} {folio_start_words['n']/tfs:>8.1%} {folio_start_words['l']/tfs:>8.1%} {folio_start_words['r']/tfs:>8.1%}")

    # Paragraph-initial lines (lines with @P0 or *P0 after a gap)
    # Check line_type for paragraph markers
    para_initial = Counter()
    para_types = defaultdict(int)
    for ld in lines_data:
        para_types[ld['line_type']] += 1

    print(f"\nLine types found: {dict(para_types)}")

    # Paragraph-initial: @P0 or *P0 (new paragraph)
    # Lines before paragraph start = last line of previous paragraph
    para_boundary_final = Counter()
    for i in range(len(lines_data) - 1):
        curr = lines_data[i]
        next_l = lines_data[i+1]
        # If next line starts a new paragraph (@P0 or is on new folio)
        is_para_break = next_l['line_type'].startswith('@P') or next_l['line_type'].startswith('*P') or next_l['folio'] != curr['folio']
        if is_para_break:
            words = extract_words(curr['text'])
            if words:
                last_word = words[-1]
                s = get_suffix_type(last_word)
                if s:
                    para_boundary_final[s] += 1

    if sum(para_boundary_final.values()) > 0:
        tpf = sum(para_boundary_final.values())
        print(f"\n{'para-boundary-final':>20} {tpf:>6} {para_boundary_final['n']/tpf:>8.1%} {para_boundary_final['l']/tpf:>8.1%} {para_boundary_final['r']/tpf:>8.1%}")

    # Also: the very last word of each paragraph (before @P or *P type line)
    # And label lines (=Pt, @Lp, @L0 etc.)
    label_final = Counter()
    for ld in lines_data:
        if '=P' in ld['line_type'] or '@L' in ld['line_type']:
            words = extract_words(ld['text'])
            if words:
                last = words[-1]
                s = get_suffix_type(last)
                if s:
                    label_final[s] += 1

    if sum(label_final.values()) > 0:
        tlf = sum(label_final.values())
        print(f"{'label-lines':>20} {tlf:>6} {label_final['n']/tlf:>8.1%} {label_final['l']/tlf:>8.1%} {label_final['r']/tlf:>8.1%}")

    # ============================================================
    # 5. Mutual information: suffix vs next_initial
    # ============================================================
    print("\n" + "="*80)
    print("5. MUTUAL INFORMATION")
    print("="*80)

    suffix_c = Counter()
    next_init_c = Counter()
    joint_c = Counter()

    for sd in sandhi_data:
        suffix_c[sd['suffix']] += 1
        next_init_c[sd['next_initial']] += 1
        joint_c[(sd['suffix'], sd['next_initial'])] += 1

    total_pairs = len(sandhi_data)
    mi = compute_mi(suffix_c, next_init_c, joint_c, total_pairs)
    print(f"MI(suffix, next_initial) = {mi:.4f} bits")

    # MI: suffix vs stem
    stem_c = Counter()
    joint_stem = Counter()
    for sd in sandhi_data:
        stem_c[sd['stem']] += 1
        joint_stem[(sd['suffix'], sd['stem'])] += 1

    mi_stem = compute_mi(suffix_c, stem_c, joint_stem, total_pairs)
    print(f"MI(suffix, stem) = {mi_stem:.4f} bits")

    # ============================================================
    # Chi-squared test for independence
    # ============================================================
    print("\n" + "="*80)
    print("6. STATISTICAL SIGNIFICANCE")
    print("="*80)

    # Chi-squared for suffix vs next_initial (top initials only)
    top_initials = [init for init in sorted_initials if sum(by_next_init[init].values()) >= 20]
    suffixes = ['n', 'l', 'r']

    # Build contingency table
    observed = {}
    row_totals = {}
    col_totals = Counter()
    grand_total = 0

    for init in top_initials:
        observed[init] = {}
        row_totals[init] = 0
        for s in suffixes:
            val = by_next_init[init].get(s, 0)
            observed[init][s] = val
            row_totals[init] += val
            col_totals[s] += val
            grand_total += val

    chi2 = 0
    for init in top_initials:
        for s in suffixes:
            expected = (row_totals[init] * col_totals[s]) / grand_total if grand_total else 0
            if expected > 0:
                chi2 += (observed[init][s] - expected) ** 2 / expected

    df = (len(top_initials) - 1) * (len(suffixes) - 1)
    print(f"Chi-squared = {chi2:.1f}, df = {df}")
    print(f"(For df={df}, critical value at p<0.001 is ~{df + 3*math.sqrt(2*df):.0f})")
    print(f"Result: {'HIGHLY SIGNIFICANT' if chi2 > df + 3*math.sqrt(2*df) else 'check p-value'}")

    # ============================================================
    # Return results for report generation
    # ============================================================
    return {
        'total_words': len(all_words_flat),
        'nlr_words': len(nlr_words),
        'baseline': {'n': baseline_n, 'l': baseline_l, 'r': baseline_r},
        'sandhi_table': sandhi_table,
        'class_results': class_results,
        'broad_results': broad_results,
        'stem_details': stem_details,
        'line_positions': {
            'line_final': dict(line_final),
            'non_line_final': dict(non_line_final),
            'line_start': dict(line_start),
            'folio_final': dict(folio_final),
            'para_boundary': dict(para_boundary_final),
        },
        'mi_next_init': mi,
        'mi_stem': mi_stem,
        'chi2': chi2,
        'df': df,
    }


if __name__ == '__main__':
    results = main()
