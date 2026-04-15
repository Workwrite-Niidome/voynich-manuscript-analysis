"""
Comprehensive analysis of ch- vs sh- words by line position within herbal folios.
Tests hypothesis: ch = description (early lines), sh = preparation/use (later lines)
Also tests: sh frequency vs visual features on 10 blind test folios.
"""

import re
from collections import defaultdict, Counter

def parse_ivtff_with_lines(filepath):
    """Parse IVTFF file preserving line numbers within each folio."""
    folios = defaultdict(list)
    current_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue

            m = re.match(r'<(f\d+[rv]\d?)\.(\d+)', line)
            if m:
                current_folio = m.group(1)
                line_num = int(m.group(2))
            else:
                m2 = re.match(r'<(f\d+[rv]\d?)>\s', line)
                if m2:
                    current_folio = m2.group(1)
                    continue
                else:
                    continue

            if current_folio is None:
                continue

            text = re.sub(r'<[^>]*>', '', line)
            text = re.sub(r'@\d+;', '', text)
            text = re.sub(r'\{[^}]*\}', '', text)
            text = re.sub(r'<%>', '', text)
            text = re.sub(r'<\$>', '', text)
            text = re.sub(r'\[.*?\]', '', text)
            text = re.sub(r'[,?!\-]', '.', text)

            words = [w.strip() for w in text.split('.') if w.strip()]
            words = [w for w in words if len(w) > 0 and re.match(r'^[a-z]+$', w)]

            folios[current_folio].append((line_num, words))

    return folios

def is_herbal(folio):
    m = re.match(r'f(\d+)([rv])', folio)
    if not m: return False
    num = int(m.group(1))
    return 1 <= num <= 57 or 58 <= num <= 66 or num == 87

def is_recipe(folio):
    m = re.match(r'f(\d+)([rv])', folio)
    if not m: return False
    num = int(m.group(1))
    return 88 <= num <= 116

def count_sh_ch(words):
    ch_count = sum(1 for w in words if w.startswith('ch') and not w.startswith('ckh'))
    sh_count = sum(1 for w in words if w.startswith('sh'))
    return ch_count, sh_count

def main():
    filepath = 'C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt'
    folios = parse_ivtff_with_lines(filepath)

    print("=" * 80)
    print("CH- vs SH- LINE POSITION ANALYSIS IN HERBAL FOLIOS")
    print("=" * 80)

    # TEST 1: Line position
    print("\n## TEST 1: Line position of ch- and sh- words")
    print("If ch=description (early) and sh=preparation (late),")
    print("ch- should concentrate early and sh- should concentrate late.\n")

    ch_positions = []
    sh_positions = []
    ch_by_line = Counter()
    sh_by_line = Counter()
    total_by_line = Counter()

    for folio in sorted(folios.keys()):
        if not is_herbal(folio):
            continue
        lines = folios[folio]
        if len(lines) < 3:
            continue

        max_line = max(ln for ln, _ in lines)
        min_line = min(ln for ln, _ in lines)
        line_range = max_line - min_line
        if line_range == 0:
            continue

        for line_num, words in lines:
            frac = (line_num - min_line) / line_range
            ch, sh = count_sh_ch(words)
            total_words = len(words)

            total_by_line[line_num] += total_words
            ch_by_line[line_num] += ch
            sh_by_line[line_num] += sh

            for _ in range(ch):
                ch_positions.append(frac)
            for _ in range(sh):
                sh_positions.append(frac)

    if ch_positions:
        mean_ch = sum(ch_positions) / len(ch_positions)
        print(f"  ch- words: n={len(ch_positions)}, mean position={mean_ch:.3f}")
    if sh_positions:
        mean_sh = sum(sh_positions) / len(sh_positions)
        print(f"  sh- words: n={len(sh_positions)}, mean position={mean_sh:.3f}")

    print(f"\n  If sh=later lines, mean_sh should be > mean_ch")
    print(f"  Difference: {mean_sh - mean_ch:+.3f}")

    # Bin into thirds
    ch_early = sum(1 for p in ch_positions if p < 0.33)
    ch_mid = sum(1 for p in ch_positions if 0.33 <= p < 0.67)
    ch_late = sum(1 for p in ch_positions if p >= 0.67)
    sh_early = sum(1 for p in sh_positions if p < 0.33)
    sh_mid = sum(1 for p in sh_positions if 0.33 <= p < 0.67)
    sh_late = sum(1 for p in sh_positions if p >= 0.67)

    ch_total = len(ch_positions)
    sh_total = len(sh_positions)

    print(f"\n  Position distribution (binned into thirds):")
    print(f"  {'':12s} {'Early':>8s} {'Middle':>8s} {'Late':>8s}")
    print(f"  {'ch- words':12s} {ch_early/ch_total*100:7.1f}% {ch_mid/ch_total*100:7.1f}% {ch_late/ch_total*100:7.1f}%")
    print(f"  {'sh- words':12s} {sh_early/sh_total*100:7.1f}% {sh_mid/sh_total*100:7.1f}% {sh_late/sh_total*100:7.1f}%")

    # By absolute line number
    print(f"\n  ch- vs sh- by absolute line number:")
    print(f"  {'Line':>6s} {'Total':>8s} {'ch-':>6s} {'ch%':>7s} {'sh-':>6s} {'sh%':>7s} {'ch/sh':>8s}")
    for ln in range(1, 25):
        tw = total_by_line[ln]
        ch = ch_by_line[ln]
        sh = sh_by_line[ln]
        if tw >= 50:
            ch_pct = ch/tw*100
            sh_pct = sh/tw*100
            ratio = ch/sh if sh > 0 else float('inf')
            ratio_str = f"{ratio:.2f}" if ratio < 100 else "inf"
            print(f"  {ln:6d} {tw:8d} {ch:6d} {ch_pct:6.1f}% {sh:6d} {sh_pct:6.1f}% {ratio_str:>8s}")

    # Lines 1-3 vs 8+
    ch_13 = sum(ch_by_line[ln] for ln in range(1,4))
    sh_13 = sum(sh_by_line[ln] for ln in range(1,4))
    tw_13 = sum(total_by_line[ln] for ln in range(1,4))
    ch_8p = sum(ch_by_line[ln] for ln in range(8,30))
    sh_8p = sum(sh_by_line[ln] for ln in range(8,30))
    tw_8p = sum(total_by_line[ln] for ln in range(8,30))

    r13 = ch_13/sh_13 if sh_13 else 999
    r8p = ch_8p/sh_8p if sh_8p else 999
    print(f"\n  Lines 1-3:  ch={ch_13} ({ch_13/tw_13*100:.1f}%), sh={sh_13} ({sh_13/tw_13*100:.1f}%), ch/sh={r13:.2f}")
    print(f"  Lines 8+:   ch={ch_8p} ({ch_8p/tw_8p*100:.1f}%), sh={sh_8p} ({sh_8p/tw_8p*100:.1f}%), ch/sh={r8p:.2f}")

    # TEST 2: Recipe vs Herbal
    print("\n\n" + "=" * 80)
    print("## TEST 2: ch/sh RATIO IN RECIPE vs HERBAL sections")
    print("If sh=preparation, sh should be enriched in recipe sections.\n")

    herbal_ch = herbal_sh = herbal_tw = 0
    recipe_ch = recipe_sh = recipe_tw = 0

    for folio in folios:
        for ln, words in folios[folio]:
            ch, sh = count_sh_ch(words)
            tw = len(words)
            if is_herbal(folio):
                herbal_ch += ch; herbal_sh += sh; herbal_tw += tw
            elif is_recipe(folio):
                recipe_ch += ch; recipe_sh += sh; recipe_tw += tw

    h_ratio = herbal_ch/herbal_sh if herbal_sh else 999
    r_ratio = recipe_ch/recipe_sh if recipe_sh else 999
    print(f"  Herbal: ch={herbal_ch} ({herbal_ch/herbal_tw*100:.1f}%), sh={herbal_sh} ({herbal_sh/herbal_tw*100:.1f}%), ch/sh={h_ratio:.2f}")
    print(f"  Recipe: ch={recipe_ch} ({recipe_ch/recipe_tw*100:.1f}%), sh={recipe_sh} ({recipe_sh/recipe_tw*100:.1f}%), ch/sh={r_ratio:.2f}")
    print(f"  sh enrichment in recipe vs herbal: {(recipe_sh/recipe_tw)/(herbal_sh/herbal_tw):.2f}x")

    # TEST 3: Blind test folios
    print("\n\n" + "=" * 80)
    print("## TEST 3: sh- WORD FREQUENCY ON BLIND TEST FOLIOS")
    print("=" * 80)

    blind_folios = ['f20r', 'f22r', 'f26r', 'f28r', 'f29r', 'f31r', 'f33r', 'f34r', 'f36r', 'f38r']

    for bf in blind_folios:
        if bf not in folios:
            print(f"  {bf}: NOT FOUND")
            continue
        all_words = []
        for ln, words in folios[bf]:
            all_words.extend(words)
        tw = len(all_words)
        ch_count = sum(1 for w in all_words if w.startswith('ch') and not w.startswith('ckh'))
        sh_count = sum(1 for w in all_words if w.startswith('sh'))
        sh_words_list = [w for w in all_words if w.startswith('sh')]

        print(f"\n  {bf}: {tw} words, ch={ch_count} ({ch_count/tw*100:.1f}%), sh={sh_count} ({sh_count/tw*100:.1f}%)")
        print(f"    sh-words: {', '.join(sh_words_list[:20])}")
        if all_words:
            print(f"    First word: {all_words[0]}")

    # TEST 4: Herbal folios ranked by sh-
    print("\n\n" + "=" * 80)
    print("## TEST 4: HERBAL FOLIOS RANKED BY sh- WORD PERCENTAGE")
    print("=" * 80)

    folio_sh_stats = []
    for folio in sorted(folios.keys()):
        if not is_herbal(folio):
            continue
        all_words = []
        for ln, words in folios[folio]:
            all_words.extend(words)
        tw = len(all_words)
        if tw < 15:
            continue
        sh_count = sum(1 for w in all_words if w.startswith('sh'))
        ch_count = sum(1 for w in all_words if w.startswith('ch') and not w.startswith('ckh'))
        folio_sh_stats.append((folio, tw, sh_count, ch_count, sh_count/tw*100, ch_count/tw*100))

    folio_sh_stats.sort(key=lambda x: -x[4])

    print(f"\n  TOP 25 herbal folios by sh- %:")
    print(f"  {'Folio':>8s} {'Words':>6s} {'sh-':>5s} {'sh%':>7s} {'ch-':>5s} {'ch%':>7s} {'sh/ch':>7s}")
    for folio, tw, shc, chc, shp, chp in folio_sh_stats[:25]:
        ratio = shc/chc if chc > 0 else 999
        print(f"  {folio:>8s} {tw:6d} {shc:5d} {shp:6.1f}% {chc:5d} {chp:6.1f}% {ratio:6.2f}")

    # TEST 5: Top sh- words with collocates
    print("\n\n" + "=" * 80)
    print("## TEST 5: MOST COMMON sh- WORDS AND COLLOCATES")
    print("=" * 80)

    all_sh_words = Counter()
    sh_after = defaultdict(Counter)

    for folio in folios:
        all_words = []
        for ln, words in folios[folio]:
            all_words.extend(words)
        for i, w in enumerate(all_words):
            if w.startswith('sh'):
                all_sh_words[w] += 1
                if i+1 < len(all_words):
                    sh_after[w][all_words[i+1]] += 1

    print(f"\n  Top 15 sh- words with top-3 following words:")
    for w, c in all_sh_words.most_common(15):
        after_top3 = sh_after[w].most_common(3)
        after_str = ", ".join(f"{aw}({ac})" for aw, ac in after_top3)
        print(f"  {w:15s}: {c:4d}  -> [{after_str}]")

    # TEST 6: First word sh content vs sh- frequency
    print("\n\n" + "=" * 80)
    print("## TEST 6: FIRST WORD sh CONTENT vs sh- FREQUENCY")
    print("=" * 80)

    has_sh_first = []
    no_sh_first = []

    for folio, tw, shc, chc, shp, chp in folio_sh_stats:
        first_words = []
        for ln, words in folios[folio]:
            if ln == 1 and words:
                first_words = words
                break
        if not first_words:
            continue
        first_word = first_words[0]
        if 'sh' in first_word:
            has_sh_first.append((folio, first_word, shp))
        else:
            no_sh_first.append((folio, first_word, shp))

    has_vals = [x[2] for x in has_sh_first]
    no_vals = [x[2] for x in no_sh_first]

    if has_vals and no_vals:
        mean_has = sum(has_vals)/len(has_vals)
        mean_no = sum(no_vals)/len(no_vals)
        print(f"\n  First word contains 'sh': n={len(has_vals)}, mean sh-%={mean_has:.1f}%")
        print(f"  First word no 'sh':       n={len(no_vals)}, mean sh-%={mean_no:.1f}%")
        print(f"  Ratio: {mean_has/mean_no:.2f}x")

        print(f"\n  Folios where first word contains 'sh':")
        for folio, fw, shp in sorted(has_sh_first, key=lambda x: -x[2])[:15]:
            print(f"    {folio:8s} first={fw:20s} sh%={shp:.1f}%")


if __name__ == '__main__':
    main()
