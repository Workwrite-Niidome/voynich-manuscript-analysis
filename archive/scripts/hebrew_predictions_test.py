"""
Test 5 predictions of the Hebrew kol/shel hypothesis against the Voynich corpus.
Uses ZL3b-n.txt (Zandbergen-Landini transliteration) as the primary corpus.
"""

import re
import sys
from collections import Counter, defaultdict
import statistics

# ============================================================
# SECTION CLASSIFICATION (by folio ranges)
# Based on standard Voynich MS section assignments
# ============================================================
SECTION_MAP = {
    'herbal_a': ['f1r','f1v','f2r','f2v','f3r','f3v','f4r','f4v','f5r','f5v',
                 'f6r','f6v','f7r','f7v','f8r','f8v','f9r','f9v','f10r','f10v',
                 'f11r','f11v','f12r','f12v','f13r','f13v','f14r','f14v','f15r','f15v',
                 'f16r','f16v','f17r','f17v','f18r','f18v','f19r','f19v','f20r','f20v',
                 'f21r','f21v','f22r','f22v','f23r','f23v','f24r','f24v','f25r','f25v',
                 'f26r','f26v','f27r','f27v','f28r','f28v','f29r','f29v','f30r','f30v',
                 'f31r','f31v','f32r','f32v','f33r','f33v','f34r','f34v','f35r','f35v',
                 'f36r','f36v','f37r','f37v','f38r','f38v','f39r','f39v','f40r','f40v',
                 'f41r','f41v','f42r','f42v','f43r','f43v','f44r','f44v','f45r','f45v',
                 'f46r','f46v','f47r','f47v','f48r','f48v','f49r','f49v','f50r','f50v',
                 'f51r','f51v','f52r','f52v','f53r','f53v','f54r','f54v','f55r','f55v',
                 'f56r','f56v','f57r','f57v'],
    'astro': ['f67r1','f67r2','f67v2','f67v1','f68r1','f68r2','f68r3','f68v1','f68v2','f68v3',
              'f69r','f69v','f70r1','f70r2','f70v1','f70v2','f71r','f71v','f72r1','f72r2',
              'f72r3','f72v1','f72v2','f72v3','f73r','f73v'],
    'biological': ['f75r','f75v','f76r','f76v','f77r','f77v','f78r','f78v','f79r','f79v',
                   'f80r','f80v','f81r','f81v','f82r','f82v','f83r','f83v','f84r','f84v'],
    'recipe': ['f103r','f103v','f104r','f104v','f105r','f105v','f106r','f106v',
               'f107r','f107v','f108r','f108v','f109r','f109v','f110r','f110v',
               'f111r','f111v','f112r','f112v','f113r','f113v','f114r','f114v',
               'f115r','f115v','f116r','f116v'],
    'herbal_b': ['f87r','f87v','f88r','f88v','f89r1','f89r2','f89v1','f89v2',
                 'f90r1','f90r2','f90v1','f90v2','f93r','f93v','f94r','f94v',
                 'f95r1','f95r2','f95v1','f95v2','f96r','f96v','f99r','f99v',
                 'f100r','f100v','f101r1','f101r2','f101v1','f101v2','f102r1','f102r2','f102v1','f102v2'],
    'cosmo': ['f85r1','f85r2','f85v', 'f86v3','f86v4','f86v5','f86v6'],
}

def get_section(folio):
    """Classify a folio into its section."""
    for section, folios in SECTION_MAP.items():
        if folio in folios:
            return section
    # Fuzzy match: strip variants
    base = folio.rstrip('0123456789').rstrip('rv') if not folio[-1].isdigit() else folio
    for section, folios in SECTION_MAP.items():
        for f in folios:
            if folio.startswith(f) or f.startswith(folio):
                return section
    return 'unknown'

def parse_corpus(filepath):
    """Parse IVTFF transliteration file into structured data."""
    folios = {}  # folio -> list of words
    current_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            # Skip comments and empty lines
            if line.startswith('#') or not line:
                continue

            # Detect folio headers
            folio_match = re.match(r'^<(f\d+[rv]\d?)>', line)
            if folio_match:
                current_folio = folio_match.group(1)
                if current_folio not in folios:
                    folios[current_folio] = []
                continue

            # Parse text lines
            line_match = re.match(r'^<(f\d+[rv]\d?)\.\d+', line)
            if line_match:
                current_folio = line_match.group(1)
                if current_folio not in folios:
                    folios[current_folio] = []

                # Extract text after the >
                text_part = re.sub(r'^<[^>]+>\s*', '', line)

                # Remove markup: <%>, <$>, <!...>, {@...}, [...], @NNN;
                text_part = re.sub(r'<%>', '', text_part)
                text_part = re.sub(r'<\$>', '', text_part)
                text_part = re.sub(r'<!@?\d*;?>', '', text_part)
                text_part = re.sub(r'<!.*?>', '', text_part)
                text_part = re.sub(r'@\d+;', '', text_part)
                text_part = re.sub(r'\{[^}]*\}', '', text_part)  # remove uncertain readings in braces
                text_part = re.sub(r'\[[^\]]*\]', '', text_part)  # remove alternatives in brackets

                # Split on dots (word separator in EVA)
                words = [w.strip().strip(',').strip('?').strip("'") for w in text_part.split('.')]
                words = [w for w in words if w and len(w) > 0 and not w.startswith('<')]

                folios[current_folio].extend(words)

    return folios


def build_word_sequences(filepath):
    """Parse corpus preserving word order per folio for bigram analysis."""
    sequences = {}  # folio -> ordered list of words
    current_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue

            folio_match = re.match(r'^<(f\d+[rv]\d?)>', line)
            if folio_match:
                current_folio = folio_match.group(1)
                if current_folio not in sequences:
                    sequences[current_folio] = []
                continue

            line_match = re.match(r'^<(f\d+[rv]\d?)\.\d+', line)
            if line_match:
                current_folio = line_match.group(1)
                if current_folio not in sequences:
                    sequences[current_folio] = []

                text_part = re.sub(r'^<[^>]+>\s*', '', line)
                text_part = re.sub(r'<%>', '', text_part)
                text_part = re.sub(r'<\$>', '', text_part)
                text_part = re.sub(r'<!@?\d*;?>', '', text_part)
                text_part = re.sub(r'<!.*?>', '', text_part)
                text_part = re.sub(r'@\d+;', '', text_part)
                text_part = re.sub(r'\{[^}]*\}', '', text_part)
                text_part = re.sub(r'\[[^\]]*\]', '', text_part)

                words = [w.strip().strip(',').strip('?').strip("'") for w in text_part.split('.')]
                words = [w for w in words if w and len(w) > 0 and not w.startswith('<')]
                sequences[current_folio].extend(words)

    return sequences


def main():
    filepath = "C:/Users/kazuk/Downloads/voynich_analysis/ZL3b-n.txt"

    print("=" * 80)
    print("HEBREW KOL/SHEL HYPOTHESIS: 5 PREDICTIONS TESTED ON VOYNICH CORPUS")
    print("=" * 80)
    print()

    folios = parse_corpus(filepath)
    sequences = build_word_sequences(filepath)

    # Build global word list and counts
    all_words = []
    for folio, words in folios.items():
        all_words.extend(words)

    total_words = len(all_words)
    word_counts = Counter(all_words)

    print(f"Corpus: {len(folios)} folios, {total_words} total word tokens")
    print(f"Unique word types: {len(word_counts)}")
    print()

    # Count chol and shol
    # Note: in EVA, "chol" and "shol" are exact tokens
    chol_count = word_counts.get('chol', 0)
    shol_count = word_counts.get('shol', 0)
    print(f"chol count: {chol_count} ({100*chol_count/total_words:.3f}%)")
    print(f"shol count: {shol_count} ({100*shol_count/total_words:.3f}%)")
    print()

    # Also check variants
    chol_variants = {k: v for k, v in word_counts.items() if 'chol' in k}
    shol_variants = {k: v for k, v in word_counts.items() if 'shol' in k}
    print(f"Words containing 'chol': {dict(sorted(chol_variants.items(), key=lambda x: -x[1])[:15])}")
    print(f"Words containing 'shol': {dict(sorted(shol_variants.items(), key=lambda x: -x[1])[:15])}")
    print()

    # Top 30 words for reference
    print("Top 30 most frequent words:")
    for w, c in word_counts.most_common(30):
        print(f"  {w:20s} {c:5d}  ({100*c/total_words:.2f}%)")
    print()

    # ==================================================================
    # PREDICTION 1: chol is universally distributed across folios
    # ==================================================================
    print("=" * 80)
    print("PREDICTION 1: chol (=kol 'all') should appear on virtually every folio")
    print("              with roughly constant per-folio frequency")
    print("=" * 80)

    folios_with_chol = 0
    folios_with_words = 0
    chol_rates = []

    for folio, words in sorted(folios.items()):
        if len(words) < 3:  # skip near-empty folios
            continue
        folios_with_words += 1
        count = words.count('chol')
        rate = count / len(words) if len(words) > 0 else 0
        if count > 0:
            folios_with_chol += 1
            chol_rates.append(rate)

    print(f"Folios with >= 3 words: {folios_with_words}")
    print(f"Folios containing chol: {folios_with_chol} ({100*folios_with_chol/folios_with_words:.1f}%)")

    if chol_rates:
        mean_rate = statistics.mean(chol_rates)
        stdev_rate = statistics.stdev(chol_rates) if len(chol_rates) > 1 else 0
        cv = stdev_rate / mean_rate if mean_rate > 0 else float('inf')
        print(f"Among folios with chol: mean rate = {mean_rate:.4f}, stdev = {stdev_rate:.4f}, CV = {cv:.2f}")

    # Compare with a known high-frequency function word for reference
    daiin_count = word_counts.get('daiin', 0)
    folios_with_daiin = sum(1 for f, ws in folios.items() if len(ws) >= 3 and 'daiin' in ws)
    print(f"\nReference: 'daiin' (most common word) appears in {folios_with_daiin}/{folios_with_words} folios")

    if folios_with_chol / folios_with_words > 0.5:
        print("\n>> RESULT: chol appears in >50% of folios. CONSISTENT with universal distribution.")
        p1_pass = True
    else:
        print(f"\n>> RESULT: chol appears in only {100*folios_with_chol/folios_with_words:.0f}% of folios.")
        if folios_with_chol / folios_with_words > 0.3:
            print(">> WEAK PASS: moderately distributed but not truly universal.")
            p1_pass = True
        else:
            print(">> FAIL: chol is NOT universally distributed.")
            p1_pass = False
    print()

    # ==================================================================
    # PREDICTION 2: Words before shol vs after shol have different distributions
    # ==================================================================
    print("=" * 80)
    print("PREDICTION 2: shol (=shel 'of') should connect different noun classes")
    print("              words BEFORE shol vs AFTER shol should differ")
    print("=" * 80)

    before_shol = Counter()
    after_shol = Counter()

    for folio, words in sequences.items():
        for i, w in enumerate(words):
            if w == 'shol':
                if i > 0:
                    before_shol[words[i-1]] += 1
                if i < len(words) - 1:
                    after_shol[words[i+1]] += 1

    print(f"\nTotal shol occurrences with context: before={sum(before_shol.values())}, after={sum(after_shol.values())}")
    print(f"\nTop 15 words BEFORE shol (possessed/modified noun):")
    for w, c in before_shol.most_common(15):
        print(f"  {w:20s} {c:3d}")

    print(f"\nTop 15 words AFTER shol (possessor noun):")
    for w, c in after_shol.most_common(15):
        print(f"  {w:20s} {c:3d}")

    # Measure distributional difference using Jaccard distance of top-20 sets
    before_set = set(w for w, _ in before_shol.most_common(20))
    after_set = set(w for w, _ in after_shol.most_common(20))

    intersection = before_set & after_set
    union = before_set | after_set
    jaccard = len(intersection) / len(union) if union else 0

    print(f"\nJaccard similarity of top-20 before/after: {jaccard:.3f}")
    print(f"Overlap words: {intersection}")

    if jaccard < 0.5:
        print("\n>> RESULT: Before-shol and after-shol distributions are DIFFERENT.")
        print(">> PASS: Consistent with genitive marker connecting different word classes.")
        p2_pass = True
    else:
        print("\n>> RESULT: Before-shol and after-shol distributions are SIMILAR.")
        print(">> FAIL: Not consistent with genitive marker.")
        p2_pass = False
    print()

    # ==================================================================
    # PREDICTION 3: chol-shol bigram should be rare (<10% of chol occurrences)
    # ==================================================================
    print("=" * 80)
    print("PREDICTION 3: chol followed by shol should be <10% of chol occurrences")
    print("              (Hebrew prefers 'kol ha-[noun]' over 'kol shel')")
    print("=" * 80)

    chol_total = 0
    chol_shol_bigram = 0
    chol_next = Counter()

    for folio, words in sequences.items():
        for i, w in enumerate(words):
            if w == 'chol':
                chol_total += 1
                if i < len(words) - 1:
                    next_w = words[i+1]
                    chol_next[next_w] += 1
                    if next_w == 'shol':
                        chol_shol_bigram += 1

    pct = 100 * chol_shol_bigram / chol_total if chol_total > 0 else 0
    print(f"\nTotal chol: {chol_total}")
    print(f"chol followed by shol: {chol_shol_bigram} ({pct:.1f}%)")
    print(f"\nTop 15 words following chol:")
    for w, c in chol_next.most_common(15):
        print(f"  {w:20s} {c:3d}  ({100*c/chol_total:.1f}%)")

    if pct < 10:
        print(f"\n>> RESULT: chol-shol bigram is {pct:.1f}% of chol. PASS (<10% threshold).")
        p3_pass = True
    else:
        print(f"\n>> RESULT: chol-shol bigram is {pct:.1f}% of chol. FAIL (>=10%).")
        p3_pass = False
    print()

    # ==================================================================
    # PREDICTION 4: shol frequency should NOT vary dramatically across sections
    # ==================================================================
    print("=" * 80)
    print("PREDICTION 4: shol (=shel 'of') should have stable frequency across sections")
    print("              (unlike 'di' which might vary)")
    print("=" * 80)

    section_words = defaultdict(int)
    section_shol = defaultdict(int)
    section_chol = defaultdict(int)

    for folio, words in folios.items():
        section = get_section(folio)
        section_words[section] += len(words)
        section_shol[section] += words.count('shol')
        section_chol[section] += words.count('chol')

    print(f"\n{'Section':<15} {'Words':>7} {'shol':>6} {'shol%':>8} {'chol':>6} {'chol%':>8}")
    print("-" * 55)

    shol_rates_by_section = {}
    for section in sorted(section_words.keys()):
        n = section_words[section]
        if n < 10:
            continue
        s = section_shol[section]
        c = section_chol[section]
        sr = 100 * s / n
        cr = 100 * c / n
        shol_rates_by_section[section] = sr
        print(f"{section:<15} {n:>7} {s:>6} {sr:>7.3f}% {c:>6} {cr:>7.3f}%")

    if len(shol_rates_by_section) >= 2:
        rates = list(shol_rates_by_section.values())
        rates_nonzero = [r for r in rates if r > 0]
        if rates_nonzero:
            max_r = max(rates_nonzero)
            min_r = min(rates_nonzero)
            ratio = max_r / min_r if min_r > 0 else float('inf')
            mean_r = statistics.mean(rates)
            stdev_r = statistics.stdev(rates) if len(rates) > 1 else 0
            cv_r = stdev_r / mean_r if mean_r > 0 else float('inf')
            print(f"\nshol rate: min={min_r:.3f}%, max={max_r:.3f}%, ratio={ratio:.1f}x, CV={cv_r:.2f}")

            if ratio < 3.0:
                print(">> RESULT: shol frequency is STABLE across sections (ratio < 3x). PASS.")
                p4_pass = True
            elif ratio < 5.0:
                print(">> RESULT: shol varies moderately (ratio 3-5x). WEAK PASS.")
                p4_pass = True
            else:
                print(f">> RESULT: shol varies dramatically ({ratio:.1f}x). FAIL.")
                p4_pass = False
        else:
            print(">> Cannot evaluate: no non-zero shol rates.")
            p4_pass = False
    else:
        print(">> Cannot evaluate: too few sections.")
        p4_pass = False
    print()

    # ==================================================================
    # PREDICTION 5: Is there a ~1-2% frequency word that could be Hebrew "lo" (negation)?
    # ==================================================================
    print("=" * 80)
    print("PREDICTION 5: Hebrew 'lo' (not) should appear as ~1-2% frequency word")
    print("              appearing before verbs (in syntactically negative positions)")
    print("=" * 80)

    # Find all words in the 0.5-3% frequency range
    candidates = []
    for w, c in word_counts.most_common():
        pct = 100 * c / total_words
        if 0.3 <= pct <= 3.0:
            candidates.append((w, c, pct))

    print(f"\nWords in 0.3-3.0% frequency range (candidates for 'lo'):")
    print(f"{'Word':<20} {'Count':>6} {'Freq%':>7}")
    print("-" * 35)
    for w, c, pct in candidates[:30]:
        print(f"{w:<20} {c:>6} {pct:>6.2f}%")

    # For the most promising candidates, check what follows them
    # A negation word should frequently precede the same words (verbs)
    print(f"\n\nDistributional analysis of top candidates:")
    print("(A negation marker should have high entropy after it - many different verbs)")

    for w, c, pct in candidates[:10]:
        followers = Counter()
        for folio, words in sequences.items():
            for i, word in enumerate(words):
                if word == w and i < len(words) - 1:
                    followers[words[i+1]] += 1

        n_followers = sum(followers.values())
        unique_followers = len(followers)
        top3 = followers.most_common(3)
        top3_str = ", ".join(f"{fw}({fc})" for fw, fc in top3)

        # Check if it appears in diverse positions (not just paragraph-initial)
        print(f"\n  {w} (n={c}, {pct:.2f}%): {unique_followers} unique followers, top3: {top3_str}")

    # Specific check: "or" is interesting - short, common, could be negation
    # Also check "ol", "al", "os" etc.
    short_candidates = [(w, c, 100*c/total_words) for w, c in word_counts.items()
                        if len(w) <= 3 and 0.3 <= 100*c/total_words <= 3.0]
    short_candidates.sort(key=lambda x: -x[2])

    print(f"\n\nShort words (1-3 chars) in target frequency range:")
    for w, c, pct in short_candidates[:20]:
        print(f"  {w:<10} {c:>6} {pct:>6.2f}%")

    # Check specifically "ol" which phonetically resembles Hebrew "lo" reversed
    # and "or" which could encode various things
    print(f"\n>> ANALYSIS: The question is whether any high-frequency short word")
    print(f">> functions as a negation marker. This requires deeper syntactic analysis")
    print(f">> than corpus statistics alone can provide. INCONCLUSIVE.")
    p5_pass = None

    print()

    # ==================================================================
    # SUMMARY
    # ==================================================================
    print("=" * 80)
    print("SUMMARY OF ALL 5 PREDICTIONS")
    print("=" * 80)

    results = [
        ("P1: chol universally distributed", p1_pass),
        ("P2: before/after shol differ", p2_pass),
        ("P3: chol-shol bigram <10%", p3_pass),
        ("P4: shol stable across sections", p4_pass),
        ("P5: negation word ~1-2%", p5_pass),
    ]

    for name, result in results:
        if result is True:
            status = "PASS"
        elif result is False:
            status = "FAIL"
        else:
            status = "INCONCLUSIVE"
        print(f"  {name:<45} {status}")

    passed = sum(1 for _, r in results if r is True)
    failed = sum(1 for _, r in results if r is False)
    inconclusive = sum(1 for _, r in results if r is None)
    print(f"\n  PASSED: {passed}  FAILED: {failed}  INCONCLUSIVE: {inconclusive}")
    print()


if __name__ == '__main__':
    main()
