"""
Comprehensive analysis of 'chol' in the Voynich Manuscript.
Uses the RF (Rene Zandbergen) corpus as primary, with IT and ZL for cross-check.
"""

import re
from collections import defaultdict, Counter

def parse_ivtff(filepath):
    """Parse IVTFF file into structured data: {folio: [list of words]}"""
    folios = defaultdict(list)
    current_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue

            # Extract folio identifier from line start
            m = re.match(r'<(f\d+[rv]\d?)[\.\s>]', line)
            if m:
                # Get the base folio (e.g., f1r, f2v, f88r)
                raw = m.group(1)
                # Normalize: strip trailing digits that are part of line number
                # The folio tag is like <f1r.1,@P0> so we already got f1r
                current_folio = raw

            # Also check for folio declaration lines like <f1r>
            m2 = re.match(r'^<(f\d+[rv]\d?)>\s', line)
            if m2:
                current_folio = m2.group(1)
                continue  # This is just the folio header, no text

            if current_folio is None:
                continue

            # Extract text portion (after the tag)
            # Remove IVTFF tags and markers
            text = re.sub(r'<[^>]*>', '', line)  # Remove all tags
            text = re.sub(r'@\d+;', '', text)    # Remove @ codes
            text = re.sub(r'\{[^}]*\}', '', text) # Remove {alternatives}
            text = re.sub(r'<%>', '', text)        # Remove paragraph markers
            text = re.sub(r'<\$>', '', text)       # Remove end markers
            text = re.sub(r'\[.*?\]', '', text)    # Remove [alternatives]
            text = re.sub(r'[,?!\-]', '.', text)   # Normalize separators to dots

            # Split into words
            words = [w.strip() for w in text.split('.') if w.strip()]
            # Filter out single characters and clearly non-word tokens
            words = [w for w in words if len(w) > 0 and re.match(r'^[a-z]+$', w)]

            folios[current_folio].extend(words)

    return folios


def get_section(folio):
    """Classify folio into manuscript section based on standard Voynich quire/section mapping."""
    # Extract folio number and r/v
    m = re.match(r'f(\d+)([rv])', folio)
    if not m:
        return 'unknown'
    num = int(m.group(1))
    side = m.group(2)

    # Standard section assignments (approximate, based on consensus)
    # Herbal A: f1-f57 (quires 1-8), but with exceptions
    # Pharma/Recipe: f88r-f102v (quire 13, 14)
    # Biological/Balneological: f75r-f84v (quire 12)
    # Astronomical/Cosmological: f67r-f73v (quires 10-11)
    # Stars/Zodiac: f70v-f73v
    # Herbal B: f87r and some others

    if 1 <= num <= 11:
        return 'herbal_a'
    elif 12 <= num <= 24:
        # Note: some of these may be missing or rosette
        return 'herbal_a'
    elif 25 <= num <= 56:
        return 'herbal_a'
    elif num == 57:
        return 'herbal_a'
    elif 58 <= num <= 66:
        return 'herbal_b'
    elif 67 <= num <= 69:
        return 'astro'
    elif 70 <= num <= 73:
        return 'zodiac'
    elif num == 74:
        return 'astro'
    elif 75 <= num <= 84:
        return 'bio'
    elif 85 <= num <= 86:
        return 'bio'
    elif num == 87:
        return 'herbal_b'
    elif 88 <= num <= 102:
        return 'recipe'
    elif 103 <= num <= 116:
        return 'recipe'
    else:
        return 'unknown'


def main():
    # Parse primary corpus
    print("=" * 80)
    print("COMPREHENSIVE ANALYSIS OF 'chol' IN THE VOYNICH MANUSCRIPT")
    print("=" * 80)

    corpus_files = {
        'RF': 'C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt',
        'IT': 'C:/Users/kazuk/Downloads/voynich_analysis/IT2a-n.txt',
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

        # Total stats
        total_words = sum(len(words) for words in folios.values())
        total_chol = sum(words.count('chol') for words in folios.values())
        print(f"\nTotal words: {total_words}")
        print(f"Total 'chol': {total_chol}")
        print(f"Overall frequency: {total_chol/total_words*100:.2f}%")

        # Per-folio analysis
        folio_stats = []
        for folio, words in sorted(folios.items(), key=lambda x: (int(re.search(r'\d+', x[0]).group()), x[0][-1])):
            n_words = len(words)
            n_chol = words.count('chol')
            if n_words > 0:
                pct = n_chol / n_words * 100
            else:
                pct = 0
            section = get_section(folio)
            folio_stats.append((folio, n_words, n_chol, pct, section))

        # Section-level aggregation
        section_words = defaultdict(int)
        section_chol = defaultdict(int)
        for folio, n_words, n_chol, pct, section in folio_stats:
            section_words[section] += n_words
            section_chol[section] += n_chol

        print("\n--- SECTION-LEVEL FREQUENCIES ---")
        for section in sorted(section_words.keys()):
            sw = section_words[section]
            sc = section_chol[section]
            if sw > 0:
                print(f"  {section:12s}: {sc:4d}/{sw:5d} = {sc/sw*100:.2f}%")

        # HIGH-chol folios (5%+)
        print("\n--- FOLIOS WITH chol >= 5% (sorted by frequency) ---")
        high_folios = [(f, nw, nc, p, s) for f, nw, nc, p, s in folio_stats if p >= 5.0 and nw >= 10]
        high_folios.sort(key=lambda x: -x[3])
        for folio, nw, nc, pct, section in high_folios:
            print(f"  {folio:10s}: {nc:3d}/{nw:3d} = {pct:5.1f}%  [{section}]")

        # ZERO-chol folios (with enough words)
        print("\n--- FOLIOS WITH chol = 0% (>20 words, sorted by word count) ---")
        zero_folios = [(f, nw, nc, p, s) for f, nw, nc, p, s in folio_stats if nc == 0 and nw >= 20]
        zero_folios.sort(key=lambda x: -x[1])
        for folio, nw, nc, pct, section in zero_folios[:30]:
            print(f"  {folio:10s}: {nw:3d} words  [{section}]")
        print(f"  ... total zero-chol folios (>=20 words): {len(zero_folios)}")

        # Only do detailed analysis for RF corpus
        if name != 'RF':
            continue

        # BIGRAM ANALYSIS
        print("\n--- BIGRAMS: what follows chol ---")
        after_chol = Counter()
        before_chol = Counter()
        for folio, words in folios.items():
            for i, w in enumerate(words):
                if w == 'chol':
                    if i + 1 < len(words):
                        after_chol[words[i+1]] += 1
                    if i > 0:
                        before_chol[words[i-1]] += 1

        print("  Top 15 words AFTER chol:")
        for w, c in after_chol.most_common(15):
            print(f"    {w:15s}: {c}")

        print("  Top 15 words BEFORE chol:")
        for w, c in before_chol.most_common(15):
            print(f"    {w:15s}: {c}")

        # CLUSTERING: Does chol appear in bursts?
        print("\n--- CLUSTERING: Does chol appear in bursts or spread evenly? ---")
        for folio, nw, nc, pct, section in high_folios[:10]:
            words = folios[folio]
            positions = [i for i, w in enumerate(words) if w == 'chol']
            if len(positions) > 1:
                gaps = [positions[i+1]-positions[i] for i in range(len(positions)-1)]
                avg_gap = sum(gaps)/len(gaps)
                print(f"  {folio}: positions={positions}, avg_gap={avg_gap:.1f}")

        # CONTEXT: What's the typical sentence-level context?
        print("\n--- SAMPLE CONTEXTS (5-word window around chol) ---")
        samples = 0
        for folio, words in sorted(folios.items()):
            for i, w in enumerate(words):
                if w == 'chol' and samples < 30:
                    start = max(0, i-3)
                    end = min(len(words), i+4)
                    context = words[start:end]
                    marker = ['*'+x+'*' if x == 'chol' else x for x in context]
                    section = get_section(folio)
                    print(f"  {folio:8s} [{section:10s}]: {' '.join(marker)}")
                    samples += 1

        # VARIANT ANALYSIS: chol vs cthol vs shol vs related forms
        print("\n--- chol AND RELATED FORMS (frequency comparison) ---")
        related_forms = ['chol', 'cthol', 'shol', 'dchol', 'kchol', 'ochol',
                         'choly', 'chols', 'chold', 'choldy', 'cholar',
                         'chor', 'char', 'chy', 'cho', 'chod',
                         'ol', 'dol', 'kol', 'sol', 'tol']
        form_counts = Counter()
        for words in folios.values():
            for w in words:
                if w in related_forms:
                    form_counts[w] += 1
                # Also count any word ending in 'ol'

        for form in related_forms:
            if form_counts[form] > 0:
                print(f"  {form:12s}: {form_counts[form]:4d}")

        # Words ending in -ol
        print("\n--- ALL WORDS ENDING IN -ol (top 20) ---")
        ol_words = Counter()
        for words in folios.values():
            for w in words:
                if w.endswith('ol') and len(w) >= 2:
                    ol_words[w] += 1
        for w, c in ol_words.most_common(20):
            print(f"  {w:15s}: {c:4d}")

        # Herbal-specific: which folios are highest?
        print("\n--- HERBAL FOLIOS RANKED BY chol% ---")
        herbal_folios = [(f, nw, nc, p, s) for f, nw, nc, p, s in folio_stats
                         if s.startswith('herbal') and nw >= 15]
        herbal_folios.sort(key=lambda x: -x[3])
        for folio, nw, nc, pct, section in herbal_folios[:20]:
            print(f"  {folio:10s}: {nc:3d}/{nw:3d} = {pct:5.1f}%")

        # Recipe folios
        print("\n--- RECIPE FOLIOS RANKED BY chol% ---")
        recipe_folios = [(f, nw, nc, p, s) for f, nw, nc, p, s in folio_stats
                         if s == 'recipe' and nw >= 15]
        recipe_folios.sort(key=lambda x: -x[3])
        for folio, nw, nc, pct, section in recipe_folios[:20]:
            print(f"  {folio:10s}: {nc:3d}/{nw:3d} = {pct:5.1f}%")

        # CRITICAL: Per-folio chol count for correlation with plant illustration types
        print("\n--- TOP 20 FOLIOS BY ABSOLUTE chol COUNT ---")
        by_count = sorted(folio_stats, key=lambda x: -x[2])
        for folio, nw, nc, pct, section in by_count[:20]:
            print(f"  {folio:10s}: {nc:3d} occurrences ({pct:.1f}%)  [{section}]")

        # PATTERN: chol chol (repeated)
        print("\n--- chol-chol PAIRS (consecutive) ---")
        pair_count = 0
        for folio, words in folios.items():
            for i in range(len(words)-1):
                if words[i] == 'chol' and words[i+1] == 'chol':
                    pair_count += 1
                    section = get_section(folio)
                    context = words[max(0,i-2):min(len(words),i+4)]
                    print(f"  {folio:8s} [{section}]: {' '.join(context)}")
        print(f"  Total chol-chol pairs: {pair_count}")

        # Cross-check: what percentage of EACH folio's vocabulary is chol?
        # And compare with 'daiin' on same folios
        print("\n--- chol vs daiin CORRELATION BY FOLIO ---")
        print(f"  {'Folio':10s} {'Words':>5s} {'chol':>5s} {'chol%':>6s} {'daiin':>5s} {'daiin%':>6s} {'Section'}")
        for folio, nw, nc, pct, section in sorted(folio_stats, key=lambda x: -x[3])[:25]:
            n_daiin = folios[folio].count('daiin')
            d_pct = n_daiin/nw*100 if nw > 0 else 0
            print(f"  {folio:10s} {nw:5d} {nc:5d} {pct:6.1f} {n_daiin:5d} {d_pct:6.1f} {section}")


if __name__ == '__main__':
    main()
