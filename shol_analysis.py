"""
Comprehensive analysis of 'shol' in the Voynich Manuscript.
Mirrors the chol analysis methodology, plus cross-correlation with chol.
"""

import re
from collections import defaultdict, Counter
import math

def parse_ivtff(filepath):
    """Parse IVTFF file into structured data: {folio: [list of words]}"""
    folios = defaultdict(list)
    current_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue

            m = re.match(r'<(f\d+[rv]\d?)[\.\s>]', line)
            if m:
                raw = m.group(1)
                current_folio = raw

            m2 = re.match(r'^<(f\d+[rv]\d?)>\s', line)
            if m2:
                current_folio = m2.group(1)
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

            folios[current_folio].extend(words)

    return folios


def get_section(folio):
    m = re.match(r'f(\d+)([rv])', folio)
    if not m:
        return 'unknown'
    num = int(m.group(1))

    if 1 <= num <= 57:
        return 'herbal_a'
    elif 58 <= num <= 66:
        return 'herbal_b'
    elif 67 <= num <= 69:
        return 'astro'
    elif 70 <= num <= 73:
        return 'zodiac'
    elif num == 74:
        return 'astro'
    elif 75 <= num <= 86:
        return 'bio'
    elif num == 87:
        return 'herbal_b'
    elif 88 <= num <= 116:
        return 'recipe'
    else:
        return 'unknown'


def main():
    print("=" * 80)
    print("COMPREHENSIVE ANALYSIS OF 'shol' IN THE VOYNICH MANUSCRIPT")
    print("=" * 80)

    corpus_files = {
        'RF': 'C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt',
        'ZL': 'C:/Users/kazuk/Downloads/voynich_analysis/ZL3b-n.txt',
    }

    for name, path in corpus_files.items():
        print(f"\n{'='*70}")
        print(f"CORPUS: {name}")
        print(f"{'='*70}")

        try:
            folios = parse_ivtff(path)
        except Exception as e:
            print(f"  Error parsing {name}: {e}")
            continue

        total_words = sum(len(words) for words in folios.values())
        total_shol = sum(words.count('shol') for words in folios.values())
        total_chol = sum(words.count('chol') for words in folios.values())
        print(f"\nTotal words: {total_words}")
        print(f"Total 'shol': {total_shol}")
        print(f"Total 'chol': {total_chol}")
        print(f"shol frequency: {total_shol/total_words*100:.2f}%")
        print(f"chol frequency: {total_chol/total_words*100:.2f}%")

        # Per-folio analysis
        folio_stats = []
        for folio, words in sorted(folios.items(), key=lambda x: (int(re.search(r'\d+', x[0]).group()), x[0][-1])):
            n_words = len(words)
            n_shol = words.count('shol')
            n_chol = words.count('chol')
            pct_shol = n_shol / n_words * 100 if n_words > 0 else 0
            pct_chol = n_chol / n_words * 100 if n_words > 0 else 0
            section = get_section(folio)
            folio_stats.append((folio, n_words, n_shol, n_chol, pct_shol, pct_chol, section))

        # Section-level aggregation
        section_words = defaultdict(int)
        section_shol = defaultdict(int)
        section_chol = defaultdict(int)
        for folio, nw, ns, nc, ps, pc, section in folio_stats:
            section_words[section] += nw
            section_shol[section] += ns
            section_chol[section] += nc

        print("\n--- SECTION-LEVEL FREQUENCIES: shol vs chol ---")
        print(f"  {'Section':12s} {'shol':>6s} {'shol%':>7s} {'chol':>6s} {'chol%':>7s} {'ratio':>7s}")
        for section in ['herbal_a', 'herbal_b', 'astro', 'zodiac', 'bio', 'recipe']:
            sw = section_words.get(section, 0)
            ss = section_shol.get(section, 0)
            sc = section_chol.get(section, 0)
            if sw > 0:
                ratio = ss/sc if sc > 0 else float('inf')
                print(f"  {section:12s} {ss:6d} {ss/sw*100:6.2f}% {sc:6d} {sc/sw*100:6.2f}% {ratio:6.2f}")

        # HIGH-shol folios
        print("\n--- FOLIOS WITH shol >= 5% (sorted by frequency) ---")
        high_folios = [(f, nw, ns, nc, ps, pc, s) for f, nw, ns, nc, ps, pc, s in folio_stats if ps >= 5.0 and nw >= 10]
        high_folios.sort(key=lambda x: -x[4])
        for folio, nw, ns, nc, ps, pc, section in high_folios:
            print(f"  {folio:10s}: shol={ns:3d}/{nw:3d}={ps:5.1f}%  chol={nc:3d}/{nw:3d}={pc:5.1f}%  [{section}]")

        # ZERO-shol folios
        print("\n--- FOLIOS WITH shol = 0% (>20 words) ---")
        zero_folios = [(f, nw, ns, nc, ps, pc, s) for f, nw, ns, nc, ps, pc, s in folio_stats if ns == 0 and nw >= 20]
        zero_folios.sort(key=lambda x: -x[1])
        for folio, nw, ns, nc, ps, pc, section in zero_folios[:30]:
            print(f"  {folio:10s}: {nw:3d} words, chol={nc} [{section}]")
        print(f"  ... total zero-shol folios (>=20 words): {len(zero_folios)}")

        if name != 'RF':
            continue

        # =====================================================
        # DETAILED ANALYSIS (RF corpus only)
        # =====================================================

        # BIGRAM ANALYSIS
        print("\n--- BIGRAMS: what follows shol ---")
        after_shol = Counter()
        before_shol = Counter()
        for folio, words in folios.items():
            for i, w in enumerate(words):
                if w == 'shol':
                    if i + 1 < len(words):
                        after_shol[words[i+1]] += 1
                    if i > 0:
                        before_shol[words[i-1]] += 1

        print("  Top 20 words AFTER shol:")
        total_after = sum(after_shol.values())
        for w, c in after_shol.most_common(20):
            print(f"    {w:15s}: {c:4d} ({c/total_after*100:.1f}%)")

        print("  Top 20 words BEFORE shol:")
        total_before = sum(before_shol.values())
        for w, c in before_shol.most_common(20):
            print(f"    {w:15s}: {c:4d} ({c/total_before*100:.1f}%)")

        # TTR of after-shol words
        after_shol_types = len(after_shol)
        after_shol_tokens = sum(after_shol.values())
        ttr_shol = after_shol_types / after_shol_tokens if after_shol_tokens > 0 else 0
        print(f"\n  TTR of words after 'shol': {after_shol_types} types / {after_shol_tokens} tokens = {ttr_shol:.3f}")

        # Compare with chol TTR
        after_chol = Counter()
        for folio, words in folios.items():
            for i, w in enumerate(words):
                if w == 'chol':
                    if i + 1 < len(words):
                        after_chol[words[i+1]] += 1
        after_chol_types = len(after_chol)
        after_chol_tokens = sum(after_chol.values())
        ttr_chol = after_chol_types / after_chol_tokens if after_chol_tokens > 0 else 0
        print(f"  TTR of words after 'chol': {after_chol_types} types / {after_chol_tokens} tokens = {ttr_chol:.3f}")

        # "shol daiin" bigram
        shol_daiin = 0
        chol_daiin = 0
        for folio, words in folios.items():
            for i in range(len(words)-1):
                if words[i] == 'shol' and words[i+1] == 'daiin':
                    shol_daiin += 1
                if words[i] == 'chol' and words[i+1] == 'daiin':
                    chol_daiin += 1
        print(f"\n  'shol daiin' count: {shol_daiin}")
        print(f"  'chol daiin' count: {chol_daiin}")

        # BURST REPETITION: shol shol
        print("\n--- BURST REPETITION: shol-shol PAIRS (consecutive) ---")
        pair_count = 0
        triple_count = 0
        for folio, words in folios.items():
            for i in range(len(words)-1):
                if words[i] == 'shol' and words[i+1] == 'shol':
                    pair_count += 1
                    section = get_section(folio)
                    context = words[max(0,i-2):min(len(words),i+4)]
                    print(f"  {folio:8s} [{section}]: {' '.join(context)}")
            for i in range(len(words)-2):
                if words[i] == 'shol' and words[i+1] == 'shol' and words[i+2] == 'shol':
                    triple_count += 1
        print(f"  Total shol-shol pairs: {pair_count}")
        print(f"  Total shol-shol-shol triples: {triple_count}")

        # Compare: chol-chol pairs
        chol_pair = 0
        chol_triple = 0
        for folio, words in folios.items():
            for i in range(len(words)-1):
                if words[i] == 'chol' and words[i+1] == 'chol':
                    chol_pair += 1
            for i in range(len(words)-2):
                if words[i] == 'chol' and words[i+1] == 'chol' and words[i+2] == 'chol':
                    chol_triple += 1
        print(f"  (Compare: chol-chol pairs: {chol_pair}, triples: {chol_triple})")

        # ALTERNATION: chol-shol and shol-chol patterns
        print("\n--- ALTERNATION PATTERNS: chol<->shol ---")
        chol_shol = 0
        shol_chol = 0
        chol_X_shol = 0  # chol [1 word] shol
        shol_X_chol = 0
        for folio, words in folios.items():
            for i in range(len(words)-1):
                if words[i] == 'chol' and words[i+1] == 'shol':
                    chol_shol += 1
                    section = get_section(folio)
                    ctx = words[max(0,i-1):min(len(words),i+3)]
                    print(f"  chol->shol: {folio:8s} [{section}]: {' '.join(ctx)}")
                if words[i] == 'shol' and words[i+1] == 'chol':
                    shol_chol += 1
                    section = get_section(folio)
                    ctx = words[max(0,i-1):min(len(words),i+3)]
                    print(f"  shol->chol: {folio:8s} [{section}]: {' '.join(ctx)}")
            for i in range(len(words)-2):
                if words[i] == 'chol' and words[i+2] == 'shol':
                    chol_X_shol += 1
                if words[i] == 'shol' and words[i+2] == 'chol':
                    shol_X_chol += 1
        print(f"\n  Direct adjacency: chol->shol={chol_shol}, shol->chol={shol_chol}")
        print(f"  With 1 word gap:  chol_X_shol={chol_X_shol}, shol_X_chol={shol_X_chol}")

        # CLUSTERING on high-shol folios
        print("\n--- CLUSTERING: Position gaps on high-shol folios ---")
        for folio, nw, ns, nc, ps, pc, section in high_folios[:15]:
            words = folios[folio]
            positions = [i for i, w in enumerate(words) if w == 'shol']
            if len(positions) > 1:
                gaps = [positions[i+1]-positions[i] for i in range(len(positions)-1)]
                avg_gap = sum(gaps)/len(gaps)
                min_gap = min(gaps)
                print(f"  {folio}: n={ns}, positions={positions[:15]}{'...' if len(positions)>15 else ''}, avg_gap={avg_gap:.1f}, min_gap={min_gap}")

        # =====================================================
        # CROSS-CORRELATION: shol vs chol per folio
        # =====================================================
        print("\n" + "=" * 70)
        print("CROSS-CORRELATION ANALYSIS: shol vs chol")
        print("=" * 70)

        # Calculate Pearson correlation
        shol_pcts = []
        chol_pcts = []
        for folio, nw, ns, nc, ps, pc, section in folio_stats:
            if nw >= 15:  # only folios with enough words
                shol_pcts.append(ps)
                chol_pcts.append(pc)

        n = len(shol_pcts)
        if n > 0:
            mean_s = sum(shol_pcts) / n
            mean_c = sum(chol_pcts) / n
            cov = sum((s-mean_s)*(c-mean_c) for s, c in zip(shol_pcts, chol_pcts)) / n
            std_s = math.sqrt(sum((s-mean_s)**2 for s in shol_pcts) / n)
            std_c = math.sqrt(sum((c-mean_c)**2 for c in chol_pcts) / n)
            if std_s > 0 and std_c > 0:
                corr = cov / (std_s * std_c)
            else:
                corr = 0
            print(f"\n  Pearson correlation (shol% vs chol%, folios with >=15 words): r = {corr:.3f}")
            print(f"  n = {n} folios")
            print(f"  Mean shol%: {mean_s:.2f}, Mean chol%: {mean_c:.2f}")

        # Herbal-only correlation
        shol_h = []
        chol_h = []
        for folio, nw, ns, nc, ps, pc, section in folio_stats:
            if nw >= 15 and section.startswith('herbal'):
                shol_h.append(ps)
                chol_h.append(pc)

        if len(shol_h) > 2:
            n_h = len(shol_h)
            mean_sh = sum(shol_h)/n_h
            mean_ch = sum(chol_h)/n_h
            cov_h = sum((s-mean_sh)*(c-mean_ch) for s, c in zip(shol_h, chol_h)) / n_h
            std_sh = math.sqrt(sum((s-mean_sh)**2 for s in shol_h) / n_h)
            std_ch = math.sqrt(sum((c-mean_ch)**2 for c in chol_h) / n_h)
            if std_sh > 0 and std_ch > 0:
                corr_h = cov_h / (std_sh * std_ch)
            else:
                corr_h = 0
            print(f"\n  HERBAL-ONLY correlation: r = {corr_h:.3f} (n={n_h})")

        # Show folios where BOTH are high
        print("\n--- FOLIOS WHERE BOTH shol AND chol ARE HIGH ---")
        print(f"  {'Folio':10s} {'Words':>5s} {'shol':>5s} {'shol%':>6s} {'chol':>5s} {'chol%':>6s} {'Section'}")
        both_high = [(f, nw, ns, nc, ps, pc, s) for f, nw, ns, nc, ps, pc, s in folio_stats
                     if ps >= 3.0 and pc >= 3.0 and nw >= 15]
        both_high.sort(key=lambda x: -(x[4]+x[5]))
        for folio, nw, ns, nc, ps, pc, section in both_high:
            print(f"  {folio:10s} {nw:5d} {ns:5d} {ps:6.1f} {nc:5d} {pc:6.1f} {section}")

        # Show folios where shol is high but chol is low
        print("\n--- FOLIOS WHERE shol IS HIGH BUT chol IS LOW (root-dominant?) ---")
        shol_dom = [(f, nw, ns, nc, ps, pc, s) for f, nw, ns, nc, ps, pc, s in folio_stats
                    if ps >= 3.0 and pc <= 1.5 and nw >= 15]
        shol_dom.sort(key=lambda x: -x[4])
        for folio, nw, ns, nc, ps, pc, section in shol_dom:
            print(f"  {folio:10s} {nw:5d} {ns:5d} {ps:6.1f} {nc:5d} {pc:6.1f} {section}")

        # Show folios where chol is high but shol is low
        print("\n--- FOLIOS WHERE chol IS HIGH BUT shol IS LOW (leaf-dominant?) ---")
        chol_dom = [(f, nw, ns, nc, ps, pc, s) for f, nw, ns, nc, ps, pc, s in folio_stats
                    if pc >= 3.0 and ps <= 1.5 and nw >= 15]
        chol_dom.sort(key=lambda x: -x[5])
        for folio, nw, ns, nc, ps, pc, section in chol_dom:
            print(f"  {folio:10s} {nw:5d} {ns:5d} {ps:6.1f} {nc:5d} {pc:6.1f} {section}")

        # SPECIFIC CROSS-CHECK: f47r and f56v (known high-chol folios)
        print("\n--- SPECIFIC FOLIOS: Known high-chol folios (f47r, f56v) ---")
        for target in ['f47r', 'f56v', 'f47v', 'f48r', 'f49r', 'f49v', 'f50r', 'f50v']:
            for folio, nw, ns, nc, ps, pc, section in folio_stats:
                if folio == target:
                    print(f"  {folio:10s}: words={nw}, shol={ns}({ps:.1f}%), chol={nc}({pc:.1f}%)")

        # HERBAL-ENRICHMENT: Is shol herbal-enriched like chol?
        print("\n--- HERBAL ENRICHMENT TEST ---")
        herbal_words = sum(nw for f, nw, ns, nc, ps, pc, s in folio_stats if s.startswith('herbal'))
        herbal_shol = sum(ns for f, nw, ns, nc, ps, pc, s in folio_stats if s.startswith('herbal'))
        non_herbal_words = sum(nw for f, nw, ns, nc, ps, pc, s in folio_stats if not s.startswith('herbal'))
        non_herbal_shol = sum(ns for f, nw, ns, nc, ps, pc, s in folio_stats if not s.startswith('herbal'))

        herbal_rate = herbal_shol/herbal_words*100 if herbal_words > 0 else 0
        non_herbal_rate = non_herbal_shol/non_herbal_words*100 if non_herbal_words > 0 else 0
        enrichment = herbal_rate/non_herbal_rate if non_herbal_rate > 0 else float('inf')

        print(f"  Herbal sections: {herbal_shol}/{herbal_words} = {herbal_rate:.2f}%")
        print(f"  Non-herbal sections: {non_herbal_shol}/{non_herbal_words} = {non_herbal_rate:.2f}%")
        print(f"  Herbal enrichment factor: {enrichment:.1f}x")

        # Same for chol
        herbal_chol = sum(nc for f, nw, ns, nc, ps, pc, s in folio_stats if s.startswith('herbal'))
        non_herbal_chol = sum(nc for f, nw, ns, nc, ps, pc, s in folio_stats if not s.startswith('herbal'))
        herbal_rate_c = herbal_chol/herbal_words*100 if herbal_words > 0 else 0
        non_herbal_rate_c = non_herbal_chol/non_herbal_words*100 if non_herbal_words > 0 else 0
        enrichment_c = herbal_rate_c/non_herbal_rate_c if non_herbal_rate_c > 0 else float('inf')
        print(f"\n  (Compare chol:)")
        print(f"  Herbal sections: {herbal_chol}/{herbal_words} = {herbal_rate_c:.2f}%")
        print(f"  Non-herbal sections: {non_herbal_chol}/{non_herbal_words} = {non_herbal_rate_c:.2f}%")
        print(f"  Herbal enrichment factor: {enrichment_c:.1f}x")

        # SAMPLE CONTEXTS
        print("\n--- SAMPLE CONTEXTS (5-word window around shol) ---")
        samples = 0
        for folio, words in sorted(folios.items()):
            for i, w in enumerate(words):
                if w == 'shol' and samples < 40:
                    start = max(0, i-3)
                    end = min(len(words), i+4)
                    context = words[start:end]
                    marker = ['*'+x+'*' if x == 'shol' else x for x in context]
                    section = get_section(folio)
                    print(f"  {folio:8s} [{section:10s}]: {' '.join(marker)}")
                    samples += 1

        # HERBAL FOLIOS RANKED BY shol%
        print("\n--- HERBAL FOLIOS RANKED BY shol% ---")
        herbal_folios = [(f, nw, ns, nc, ps, pc, s) for f, nw, ns, nc, ps, pc, s in folio_stats
                         if s.startswith('herbal') and nw >= 15]
        herbal_folios.sort(key=lambda x: -x[4])
        for folio, nw, ns, nc, ps, pc, section in herbal_folios[:25]:
            print(f"  {folio:10s}: shol={ns:3d}/{nw:3d}={ps:5.1f}%  chol={nc:3d}/{nw:3d}={pc:5.1f}%")

        # TOP 20 BY ABSOLUTE COUNT
        print("\n--- TOP 20 FOLIOS BY ABSOLUTE shol COUNT ---")
        by_count = sorted(folio_stats, key=lambda x: -x[2])
        for folio, nw, ns, nc, ps, pc, section in by_count[:20]:
            print(f"  {folio:10s}: shol={ns:3d} ({ps:.1f}%), chol={nc} ({pc:.1f}%)  [{section}]")

        # RELATED FORMS
        print("\n--- shol AND RELATED sh-FORMS (frequency comparison) ---")
        related_forms = ['shol', 'sho', 'shor', 'shod', 'shody', 'shok',
                         'shol', 'sholdy', 'sholar', 'sholy',
                         'chol', 'cthol', 'dshol', 'kshol', 'oshol',
                         'shols', 'shold']
        form_counts = Counter()
        for words in folios.values():
            for w in words:
                if w in related_forms:
                    form_counts[w] += 1

        for form in sorted(set(related_forms)):
            if form_counts[form] > 0:
                print(f"  {form:12s}: {form_counts[form]:4d}")

        # Words starting with sh-
        print("\n--- TOP 30 WORDS STARTING WITH sh- ---")
        sh_words = Counter()
        for words in folios.values():
            for w in words:
                if w.startswith('sh') and len(w) >= 3:
                    sh_words[w] += 1
        for w, c in sh_words.most_common(30):
            print(f"  {w:15s}: {c:4d}")

        # RECIPE FOLIOS
        print("\n--- RECIPE FOLIOS RANKED BY shol% ---")
        recipe_folios = [(f, nw, ns, nc, ps, pc, s) for f, nw, ns, nc, ps, pc, s in folio_stats
                         if s == 'recipe' and nw >= 15]
        recipe_folios.sort(key=lambda x: -x[4])
        for folio, nw, ns, nc, ps, pc, section in recipe_folios[:15]:
            print(f"  {folio:10s}: shol={ns:3d}/{nw:3d}={ps:5.1f}%  chol={nc:3d}/{nw:3d}={pc:5.1f}%")

        # BIO FOLIOS
        print("\n--- BIO FOLIOS RANKED BY shol% ---")
        bio_folios = [(f, nw, ns, nc, ps, pc, s) for f, nw, ns, nc, ps, pc, s in folio_stats
                      if s == 'bio' and nw >= 15]
        bio_folios.sort(key=lambda x: -x[4])
        for folio, nw, ns, nc, ps, pc, section in bio_folios[:15]:
            print(f"  {folio:10s}: shol={ns:3d}/{nw:3d}={ps:5.1f}%  chol={nc:3d}/{nw:3d}={pc:5.1f}%")

        # FINAL COMPARISON TABLE
        print("\n" + "=" * 70)
        print("SUMMARY COMPARISON: shol vs chol")
        print("=" * 70)
        print(f"  {'Metric':40s} {'shol':>10s} {'chol':>10s}")
        print(f"  {'-'*40} {'-'*10} {'-'*10}")
        print(f"  {'Total occurrences':40s} {total_shol:10d} {total_chol:10d}")
        print(f"  {'Overall frequency':40s} {total_shol/total_words*100:9.2f}% {total_chol/total_words*100:9.2f}%")
        print(f"  {'Herbal enrichment factor':40s} {enrichment:9.1f}x {enrichment_c:9.1f}x")
        print(f"  {'TTR of following word':40s} {ttr_shol:10.3f} {ttr_chol:10.3f}")
        print(f"  {'Consecutive pairs (X X)':40s} {pair_count:10d} {chol_pair:10d}")
        print(f"  {'Consecutive triples (X X X)':40s} {triple_count:10d} {chol_triple:10d}")
        print(f"  {'X daiin bigram count':40s} {shol_daiin:10d} {chol_daiin:10d}")
        print(f"  {'Folios >=5% (>=10 words)':40s} {len(high_folios):10d} {'--':>10s}")

        # chol-shol correlation
        print(f"\n  Per-folio correlation (all): r = {corr:.3f}")
        if len(shol_h) > 2:
            print(f"  Per-folio correlation (herbal only): r = {corr_h:.3f}")


if __name__ == '__main__':
    main()
