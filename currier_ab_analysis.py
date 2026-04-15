"""
Currier A/B Hypothesis Testing for the Voynich Manuscript
=========================================================
Tests four competing hypotheses for the A/B distinction:
1. Dialect split (same language, different phonological conventions)
2. Topic split (same language, different subject matter)
3. Cipher key split (same plaintext language, different encryption)
4. Scribe split (different individuals with different habits)

Uses the ZL (Zandbergen-Landini) IVTFF transcription.
"""

import re
from collections import Counter, defaultdict
from itertools import combinations
import json
import math

# ============================================================
# PARSE IVTFF TRANSCRIPTION
# ============================================================

def parse_ivtff(filepath):
    """Parse an IVTFF transcription file into structured data."""
    pages = {}
    current_folio = None
    current_lang = None
    current_section = None  # $I field: T=text, H=herbal, etc.
    current_illust = None   # $I field

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
                # Extract Currier language
                lang_match = re.search(r'\$L=([AB])', attrs)
                current_lang = lang_match.group(1) if lang_match else None
                # Extract illustration type
                illust_match = re.search(r'\$I=(\w+)', attrs)
                current_illust = illust_match.group(1) if illust_match else None
                # Extract quire
                quire_match = re.search(r'\$Q=(\w+)', attrs)
                current_quire = quire_match.group(1) if quire_match else None

                if current_folio not in pages:
                    pages[current_folio] = {
                        'lang': current_lang,
                        'illust': current_illust,
                        'quire': current_quire if quire_match else None,
                        'lines': [],
                        'words': []
                    }
                continue

            # Text line
            text_match = re.match(r'<(f\d+[rv]\d?\.\d+)', line)
            if text_match and current_folio:
                # Extract text after the tag info
                text_part = re.sub(r'<[^>]*>', '', line)
                text_part = re.sub(r'<%>', '', text_part)
                text_part = re.sub(r'<\$>', '', text_part)
                text_part = re.sub(r'<!@\d+;>', '', text_part)
                text_part = re.sub(r'@\d+;?', '', text_part)
                text_part = re.sub(r'\{[^}]*\}', '', text_part)
                text_part = re.sub(r'\[[^\]]*\]', '', text_part)
                text_part = re.sub(r'[<>%$?]', '', text_part)

                # Split into words (. or , or space or <- -> as separators)
                words = re.split(r'[.\s,]+', text_part)
                words = [w.strip() for w in words if w.strip() and len(w.strip()) > 0]
                # Remove markup artifacts
                words = [w for w in words if not re.match(r'^[-=+*@#]+$', w) and len(w) > 0]

                pages[current_folio]['lines'].append(words)
                pages[current_folio]['words'].extend(words)

    return pages


def get_section_type(folio, illust):
    """Map folio to manuscript section based on folio number and illustration type."""
    # Extract numeric part
    num_match = re.match(r'f(\d+)', folio)
    if not num_match:
        return 'unknown'
    num = int(num_match.group(1))

    if illust == 'H':
        return 'herbal'
    elif illust == 'A':
        return 'astro'
    elif illust == 'B':
        return 'bio'
    elif illust == 'P':
        return 'pharma'
    elif illust == 'S':
        return 'star'
    elif illust == 'T':
        return 'text'
    elif illust == 'Z':
        return 'zodiac'
    elif illust == 'C':
        return 'cosmo'

    # Fallback by folio number
    if num <= 57:
        return 'herbal'
    elif num <= 67:
        return 'astro'
    elif num <= 86:
        return 'bio'
    elif num <= 102:
        return 'pharma'
    else:
        return 'unknown'


# ============================================================
# ANALYSIS FUNCTIONS
# ============================================================

def compute_word_freqs(pages, lang_filter=None, section_filter=None):
    """Compute word frequencies for a subset of pages."""
    counter = Counter()
    total = 0
    for folio, data in pages.items():
        if lang_filter and data['lang'] != lang_filter:
            continue
        if section_filter:
            section = get_section_type(folio, data['illust'])
            if section != section_filter:
                continue
        for w in data['words']:
            counter[w] += 1
            total += 1
    return counter, total


def jaccard(set1, set2):
    """Jaccard similarity between two sets."""
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0


def compute_ch_sh_ratio(words):
    """Compute ch/(ch+sh) ratio for a word list."""
    ch_count = sum(1 for w in words if 'ch' in w and 'sh' not in w)
    sh_count = sum(1 for w in words if 'sh' in w and 'ch' not in w)
    both = sum(1 for w in words if 'ch' in w and 'sh' in w)
    total = ch_count + sh_count + both
    if total == 0:
        return None
    return (ch_count + both * 0.5) / total


def word_length_stats(words):
    """Compute word length statistics."""
    lengths = [len(w) for w in words]
    if not lengths:
        return 0, 0
    mean = sum(lengths) / len(lengths)
    var = sum((l - mean) ** 2 for l in lengths) / len(lengths)
    return mean, var ** 0.5


def entropy(counter, total):
    """Shannon entropy of a frequency distribution."""
    h = 0
    for count in counter.values():
        if count > 0:
            p = count / total
            h -= p * math.log2(p)
    return h


def hapax_ratio(counter):
    """Fraction of vocabulary that appears exactly once."""
    hapax = sum(1 for c in counter.values() if c == 1)
    return hapax / len(counter) if counter else 0


def bigram_freqs(pages, lang_filter=None):
    """Compute word bigram frequencies."""
    counter = Counter()
    total = 0
    for folio, data in pages.items():
        if lang_filter and data['lang'] != lang_filter:
            continue
        for line in data['lines']:
            for i in range(len(line) - 1):
                bg = (line[i], line[i+1])
                counter[bg] += 1
                total += 1
    return counter, total


# ============================================================
# MAIN ANALYSIS
# ============================================================

def main():
    filepath = "C:/Users/kazuk/Downloads/voynich_analysis/ZL3b-n.txt"
    pages = parse_ivtff(filepath)

    print("=" * 80)
    print("CURRIER A/B HYPOTHESIS TESTING")
    print("=" * 80)

    # ---- Basic statistics ----
    a_pages = {f: d for f, d in pages.items() if d['lang'] == 'A'}
    b_pages = {f: d for f, d in pages.items() if d['lang'] == 'B'}
    none_pages = {f: d for f, d in pages.items() if d['lang'] is None}

    a_words_all = []
    b_words_all = []
    for d in a_pages.values():
        a_words_all.extend(d['words'])
    for d in b_pages.values():
        b_words_all.extend(d['words'])

    a_vocab = set(a_words_all)
    b_vocab = set(b_words_all)

    print(f"\n--- BASIC COUNTS ---")
    print(f"Currier A pages: {len(a_pages)}")
    print(f"Currier B pages: {len(b_pages)}")
    print(f"Unlabeled pages: {len(none_pages)}")
    print(f"A total words: {len(a_words_all)}")
    print(f"B total words: {len(b_words_all)}")
    print(f"A vocabulary size: {len(a_vocab)}")
    print(f"B vocabulary size: {len(b_vocab)}")
    print(f"Shared vocabulary: {len(a_vocab & b_vocab)}")
    print(f"A-only vocabulary: {len(a_vocab - b_vocab)}")
    print(f"B-only vocabulary: {len(b_vocab - a_vocab)}")
    print(f"Vocabulary Jaccard: {jaccard(a_vocab, b_vocab):.4f}")

    # ---- Word length ----
    a_len_mean, a_len_std = word_length_stats(a_words_all)
    b_len_mean, b_len_std = word_length_stats(b_words_all)
    print(f"\n--- WORD LENGTH ---")
    print(f"A mean length: {a_len_mean:.2f} +/- {a_len_std:.2f}")
    print(f"B mean length: {b_len_mean:.2f} +/- {b_len_std:.2f}")

    # ---- Entropy ----
    a_counter = Counter(a_words_all)
    b_counter = Counter(b_words_all)
    a_entropy = entropy(a_counter, len(a_words_all))
    b_entropy = entropy(b_counter, len(b_words_all))
    print(f"\n--- WORD-LEVEL ENTROPY ---")
    print(f"A entropy: {a_entropy:.3f} bits")
    print(f"B entropy: {b_entropy:.3f} bits")

    # ---- Hapax ----
    a_hapax = hapax_ratio(a_counter)
    b_hapax = hapax_ratio(b_counter)
    print(f"\n--- HAPAX RATIO ---")
    print(f"A hapax ratio: {a_hapax:.3f}")
    print(f"B hapax ratio: {b_hapax:.3f}")

    # ---- Key diagnostic words ----
    print(f"\n--- KEY DIAGNOSTIC WORD FREQUENCIES ---")
    diagnostic_words = ['daiin', 'chol', 'chedy', 'shedy', 'ol', 'or', 'ar',
                        'qokeedy', 'qokedy', 'shol', 'chor', 'shor',
                        'okaiin', 'otaiin', 'dain', 'aiin', 'ain',
                        'lchedy', 'lkeedy', 'qokeey', 'okedy', 'otedy',
                        'cheol', 'sheol', 'chey', 'shey',
                        'cthy', 'shy', 'chy', 'dy', 'ry',
                        'dar', 'dal', 'dan',
                        'oteedy', 'okeedy', 'ykeedy', 'lkeedy']

    print(f"{'Word':<12} {'A_count':>8} {'A_%':>8} {'B_count':>8} {'B_%':>8} {'Ratio':>8}")
    print("-" * 60)
    for w in diagnostic_words:
        a_c = a_counter.get(w, 0)
        b_c = b_counter.get(w, 0)
        a_pct = a_c / len(a_words_all) * 100 if a_words_all else 0
        b_pct = b_c / len(b_words_all) * 100 if b_words_all else 0
        ratio = (a_pct / b_pct) if b_pct > 0 else float('inf')
        print(f"{w:<12} {a_c:>8} {a_pct:>7.2f}% {b_c:>8} {b_pct:>7.2f}% {ratio:>8.2f}")

    # ---- Top words unique to each ----
    print(f"\n--- TOP 30 A-DOMINANT WORDS (by A/B frequency ratio) ---")
    a_dominant = []
    for w in a_vocab:
        a_c = a_counter[w]
        b_c = b_counter.get(w, 0)
        if a_c >= 5:  # minimum frequency
            a_pct = a_c / len(a_words_all)
            b_pct = b_c / len(b_words_all) if b_words_all else 0.0001
            ratio = a_pct / b_pct if b_pct > 0 else a_pct / (1/len(b_words_all))
            a_dominant.append((w, a_c, b_c, ratio))
    a_dominant.sort(key=lambda x: -x[3])
    print(f"{'Word':<15} {'A_count':>8} {'B_count':>8} {'Ratio':>8}")
    for w, ac, bc, r in a_dominant[:30]:
        print(f"{w:<15} {ac:>8} {bc:>8} {r:>8.1f}")

    print(f"\n--- TOP 30 B-DOMINANT WORDS (by B/A frequency ratio) ---")
    b_dominant = []
    for w in b_vocab:
        b_c = b_counter[w]
        a_c = a_counter.get(w, 0)
        if b_c >= 5:
            b_pct = b_c / len(b_words_all)
            a_pct = a_c / len(a_words_all) if a_words_all else 0.0001
            ratio = b_pct / a_pct if a_pct > 0 else b_pct / (1/len(a_words_all))
            b_dominant.append((w, a_c, b_c, ratio))
    b_dominant.sort(key=lambda x: -x[3])
    print(f"{'Word':<15} {'A_count':>8} {'B_count':>8} {'Ratio':>8}")
    for w, ac, bc, r in b_dominant[:30]:
        print(f"{w:<15} {ac:>8} {bc:>8} {r:>8.1f}")

    # ============================================================
    # TEST 1: A/B vs SECTION CROSS-TABULATION
    # ============================================================
    print(f"\n{'='*80}")
    print("TEST 1: A/B vs SECTION TYPE CROSS-TABULATION")
    print("If A/B = section split, they should be perfectly correlated.")
    print("If they cross-cut, A/B is independent of section type.")
    print(f"{'='*80}")

    section_lang = defaultdict(lambda: {'A': 0, 'B': 0, 'None': 0})
    section_lang_folios = defaultdict(lambda: {'A': [], 'B': [], 'None': []})

    for folio, data in pages.items():
        section = get_section_type(folio, data['illust'])
        lang = data['lang'] if data['lang'] else 'None'
        section_lang[section][lang] += len(data['words'])
        section_lang_folios[section][lang].append(folio)

    print(f"\n{'Section':<12} {'A_words':>10} {'B_words':>10} {'None':>10} {'A_folios':>10} {'B_folios':>10}")
    print("-" * 65)
    for section in sorted(section_lang.keys()):
        counts = section_lang[section]
        folio_counts = section_lang_folios[section]
        print(f"{section:<12} {counts['A']:>10} {counts['B']:>10} {counts['None']:>10} {len(folio_counts['A']):>10} {len(folio_counts['B']):>10}")

    # List specific folios where A and B cross within a section
    print(f"\n--- CROSS-CUTTING: Sections with BOTH A and B folios ---")
    for section in sorted(section_lang.keys()):
        fc = section_lang_folios[section]
        if fc['A'] and fc['B']:
            print(f"\n  {section}:")
            print(f"    A folios ({len(fc['A'])}): {', '.join(sorted(fc['A'])[:10])}{'...' if len(fc['A']) > 10 else ''}")
            print(f"    B folios ({len(fc['B'])}): {', '.join(sorted(fc['B'])[:10])}{'...' if len(fc['B']) > 10 else ''}")

    # ============================================================
    # TEST 2: ch/sh RATIO BY LANGUAGE AND SECTION
    # ============================================================
    print(f"\n{'='*80}")
    print("TEST 2: ch/sh RATIO BY LANGUAGE AND SECTION")
    print("If ch/sh correlates with A/B independently of section, it's linguistic.")
    print("If ch/sh correlates with section independently of A/B, it's topical.")
    print(f"{'='*80}")

    for section in sorted(section_lang.keys()):
        for lang in ['A', 'B']:
            words = []
            for folio, data in pages.items():
                if data['lang'] == lang and get_section_type(folio, data['illust']) == section:
                    words.extend(data['words'])
            if len(words) > 50:
                ratio = compute_ch_sh_ratio(words)
                if ratio is not None:
                    print(f"  {section:<12} {lang}: ch/(ch+sh) = {ratio:.3f}  (n={len(words)} words)")

    # Overall by language only
    print(f"\n  Overall:")
    for lang in ['A', 'B']:
        words = a_words_all if lang == 'A' else b_words_all
        ratio = compute_ch_sh_ratio(words)
        print(f"    {lang}: ch/(ch+sh) = {ratio:.3f}")

    # ============================================================
    # TEST 3: CIPHER KEY SPLIT - FREQUENCY-MATCHED WORD PAIRS
    # ============================================================
    print(f"\n{'='*80}")
    print("TEST 3: CIPHER KEY SPLIT - FREQUENCY-MATCHED WORD PAIRS")
    print("If A and B use different cipher keys, the SAME plaintext word")
    print("maps to DIFFERENT EVA words. We look for A-dominant / B-dominant")
    print("word pairs with similar frequency and distribution shape.")
    print(f"{'='*80}")

    # Find word pairs: one A-dominant, one B-dominant, similar total frequency
    a_dom_candidates = [(w, ac, bc) for w, ac, bc, r in a_dominant[:50] if ac >= 10]
    b_dom_candidates = [(w, ac, bc) for w, ac, bc, r in b_dominant[:50] if bc >= 10]

    print(f"\n--- POTENTIAL CIPHER PAIRS (A-word <-> B-word with similar frequency) ---")
    print(f"{'A_word':<15} {'A_freq':>6} {'B_word':<15} {'B_freq':>6} {'Freq_ratio':>10} {'Struct_sim':>10}")
    print("-" * 75)

    pairs_found = []
    for a_word, a_ac, a_bc in a_dom_candidates:
        a_freq = a_ac  # frequency in A
        for b_word, b_ac, b_bc in b_dom_candidates:
            b_freq = b_bc  # frequency in B
            # Similar frequency (within 2x)
            freq_ratio = max(a_freq, b_freq) / min(a_freq, b_freq) if min(a_freq, b_freq) > 0 else 999
            if freq_ratio <= 2.0:
                # Structural similarity: same length? similar character composition?
                len_diff = abs(len(a_word) - len(b_word))
                struct_sim = 1.0 / (1.0 + len_diff)
                pairs_found.append((a_word, a_freq, b_word, b_freq, freq_ratio, struct_sim))

    pairs_found.sort(key=lambda x: x[4])
    for a_w, af, b_w, bf, fr, ss in pairs_found[:25]:
        print(f"{a_w:<15} {af:>6} {b_w:<15} {bf:>6} {fr:>10.2f} {ss:>10.2f}")

    # ============================================================
    # TEST 4: MORPHOLOGICAL SYSTEM COMPARISON
    # ============================================================
    print(f"\n{'='*80}")
    print("TEST 4: MORPHOLOGICAL SYSTEM COMPARISON")
    print("If A/B are dialects, they should share the SAME morphological rules")
    print("but with different phonological realizations.")
    print("If A/B are different languages, morphological rules differ.")
    print(f"{'='*80}")

    # Analyze prefix and suffix distributions
    def get_prefix_suffix(word, prefixes=['ch', 'sh', 'qo', 'ok', 'ot', 'da', 'ol', 'or', 'ct', 'cp']):
        for p in sorted(prefixes, key=len, reverse=True):
            if word.startswith(p) and len(word) > len(p):
                return p, word[len(p):]
        return None, word

    def suffix_analysis(words):
        suffixes = Counter()
        for w in words:
            if len(w) >= 2:
                suffixes[w[-1]] += 1
                suffixes[w[-2:]] += 1
        return suffixes

    print(f"\n--- PREFIX DISTRIBUTION ---")
    prefixes_to_check = ['ch', 'sh', 'qo', 'ok', 'ot', 'da', 'ol', 'ct', 'cp', 'qok', 'cth', 'ckh']
    print(f"{'Prefix':<10} {'A_%':>8} {'B_%':>8} {'Ratio_A/B':>10}")
    print("-" * 40)
    for pfx in prefixes_to_check:
        a_c = sum(1 for w in a_words_all if w.startswith(pfx))
        b_c = sum(1 for w in b_words_all if w.startswith(pfx))
        a_pct = a_c / len(a_words_all) * 100
        b_pct = b_c / len(b_words_all) * 100
        ratio = a_pct / b_pct if b_pct > 0 else float('inf')
        print(f"{pfx:<10} {a_pct:>7.2f}% {b_pct:>7.2f}% {ratio:>10.2f}")

    print(f"\n--- SUFFIX DISTRIBUTION (last character) ---")
    a_suffix = Counter(w[-1] for w in a_words_all if w)
    b_suffix = Counter(w[-1] for w in b_words_all if w)
    all_suffixes = set(a_suffix.keys()) | set(b_suffix.keys())
    print(f"{'Suffix':<10} {'A_%':>8} {'B_%':>8} {'Ratio_A/B':>10}")
    print("-" * 40)
    for s in sorted(all_suffixes):
        a_pct = a_suffix.get(s, 0) / len(a_words_all) * 100
        b_pct = b_suffix.get(s, 0) / len(b_words_all) * 100
        ratio = a_pct / b_pct if b_pct > 0 else float('inf')
        if a_pct > 0.5 or b_pct > 0.5:
            print(f"{s:<10} {a_pct:>7.2f}% {b_pct:>7.2f}% {ratio:>10.2f}")

    print(f"\n--- SUFFIX DISTRIBUTION (last 2 characters) ---")
    a_suffix2 = Counter(w[-2:] for w in a_words_all if len(w) >= 2)
    b_suffix2 = Counter(w[-2:] for w in b_words_all if len(w) >= 2)
    all_suffixes2 = set(a_suffix2.keys()) | set(b_suffix2.keys())
    print(f"{'Suffix':<10} {'A_%':>8} {'B_%':>8} {'Ratio_A/B':>10}")
    print("-" * 40)
    for s in sorted(all_suffixes2, key=lambda x: -(a_suffix2.get(x,0) + b_suffix2.get(x,0))):
        a_pct = a_suffix2.get(s, 0) / len(a_words_all) * 100
        b_pct = b_suffix2.get(s, 0) / len(b_words_all) * 100
        ratio = a_pct / b_pct if b_pct > 0 else float('inf')
        if a_pct > 0.3 or b_pct > 0.3:
            print(f"{s:<10} {a_pct:>7.2f}% {b_pct:>7.2f}% {ratio:>10.2f}")

    # ============================================================
    # TEST 5: POSITIONAL PATTERNS (FIRST/LAST WORD ON LINE)
    # ============================================================
    print(f"\n{'='*80}")
    print("TEST 5: POSITIONAL PATTERNS")
    print("If A/B have the same syntax, first-word and last-word distributions")
    print("should be similar (just with different vocabulary).")
    print("If syntax differs, positional patterns differ.")
    print(f"{'='*80}")

    for lang, lang_pages in [('A', a_pages), ('B', b_pages)]:
        first_words = Counter()
        last_words = Counter()
        total_lines = 0
        for data in lang_pages.values():
            for line in data['lines']:
                if line:
                    first_words[line[0]] += 1
                    last_words[line[-1]] += 1
                    total_lines += 1

        print(f"\n  {lang} - Top 10 LINE-INITIAL words (n={total_lines} lines):")
        for w, c in first_words.most_common(10):
            print(f"    {w:<15} {c:>5} ({c/total_lines*100:.1f}%)")

        print(f"  {lang} - Top 10 LINE-FINAL words:")
        for w, c in last_words.most_common(10):
            print(f"    {w:<15} {c:>5} ({c/total_lines*100:.1f}%)")

    # ============================================================
    # TEST 6: WITHIN-SECTION JACCARD (A-herbal vs B-herbal etc.)
    # ============================================================
    print(f"\n{'='*80}")
    print("TEST 6: WITHIN-SECTION JACCARD COMPARISONS")
    print("If A/B is purely a TOPIC split, then A-herbal vs B-herbal")
    print("should have HIGH Jaccard (same topic, same language).")
    print("If A/B is a LANGUAGE/CIPHER split, Jaccard stays low even")
    print("within the same section type.")
    print(f"{'='*80}")

    for section in ['herbal', 'bio', 'pharma', 'star', 'astro', 'text']:
        a_words_sec = []
        b_words_sec = []
        for folio, data in pages.items():
            sec = get_section_type(folio, data['illust'])
            if sec == section:
                if data['lang'] == 'A':
                    a_words_sec.extend(data['words'])
                elif data['lang'] == 'B':
                    b_words_sec.extend(data['words'])

        if a_words_sec and b_words_sec:
            a_set = set(a_words_sec)
            b_set = set(b_words_sec)
            j = jaccard(a_set, b_set)
            print(f"  {section:<12}: A({len(a_set):>4} types, {len(a_words_sec):>5} tokens) vs B({len(b_set):>4} types, {len(b_words_sec):>5} tokens) -> Jaccard = {j:.4f}")

    # Also compare same-language across sections
    print(f"\n  --- Same language, different sections ---")
    for lang in ['A', 'B']:
        section_vocabs = {}
        for folio, data in pages.items():
            if data['lang'] == lang:
                sec = get_section_type(folio, data['illust'])
                if sec not in section_vocabs:
                    section_vocabs[sec] = set()
                section_vocabs[sec].update(data['words'])

        for s1, s2 in combinations(sorted(section_vocabs.keys()), 2):
            if len(section_vocabs[s1]) > 20 and len(section_vocabs[s2]) > 20:
                j = jaccard(section_vocabs[s1], section_vocabs[s2])
                print(f"  {lang}-{s1} vs {lang}-{s2}: Jaccard = {j:.4f}")

    # ============================================================
    # TEST 7: BIGRAM/COLLOCATIONS
    # ============================================================
    print(f"\n{'='*80}")
    print("TEST 7: WORD BIGRAM COMPARISON")
    print("If A/B share the same GRAMMAR, the most frequent bigrams should")
    print("show parallel structure (function_word + content_word patterns).")
    print(f"{'='*80}")

    a_bg, a_bg_total = bigram_freqs(pages, 'A')
    b_bg, b_bg_total = bigram_freqs(pages, 'B')

    print(f"\n  Top 15 A bigrams (n={a_bg_total}):")
    for bg, c in a_bg.most_common(15):
        print(f"    {bg[0]:<12} {bg[1]:<12} {c:>5} ({c/a_bg_total*100:.2f}%)")

    print(f"\n  Top 15 B bigrams (n={b_bg_total}):")
    for bg, c in b_bg.most_common(15):
        print(f"    {bg[0]:<12} {bg[1]:<12} {c:>5} ({c/b_bg_total*100:.2f}%)")

    # ============================================================
    # TEST 8: CHARACTER-LEVEL COMPARISON
    # ============================================================
    print(f"\n{'='*80}")
    print("TEST 8: CHARACTER-LEVEL FREQUENCY COMPARISON")
    print("If A/B use different cipher keys, character frequencies should differ.")
    print("If A/B are dialects, most characters should have similar frequencies,")
    print("with only a few systematic shifts.")
    print(f"{'='*80}")

    a_chars = Counter(''.join(a_words_all))
    b_chars = Counter(''.join(b_words_all))
    a_total_chars = sum(a_chars.values())
    b_total_chars = sum(b_chars.values())

    all_chars = sorted(set(a_chars.keys()) | set(b_chars.keys()))
    print(f"\n{'Char':<6} {'A_%':>8} {'B_%':>8} {'Ratio':>8} {'Diff':>8}")
    print("-" * 45)
    char_diffs = []
    for ch in all_chars:
        a_pct = a_chars.get(ch, 0) / a_total_chars * 100
        b_pct = b_chars.get(ch, 0) / b_total_chars * 100
        ratio = a_pct / b_pct if b_pct > 0 else float('inf')
        diff = abs(a_pct - b_pct)
        char_diffs.append((ch, a_pct, b_pct, ratio, diff))

    char_diffs.sort(key=lambda x: -x[4])
    for ch, ap, bp, r, d in char_diffs:
        if ap > 0.3 or bp > 0.3:
            print(f"{ch:<6} {ap:>7.2f}% {bp:>7.2f}% {r:>8.2f} {d:>7.2f}%")

    # ============================================================
    # SYNTHESIS
    # ============================================================
    print(f"\n{'='*80}")
    print("SYNTHESIS: HYPOTHESIS EVALUATION")
    print(f"{'='*80}")

    print("""
HYPOTHESIS 1: DIALECT SPLIT
  Prediction: Same morphological system, different phonological realizations
  - ch/sh alternation should be the MAIN difference
  - Prefix/suffix systems should be IDENTICAL
  - Character frequencies should be similar except for ch<->sh
  Evidence: [see prefix/suffix/character tables above]

HYPOTHESIS 2: TOPIC SPLIT
  Prediction: Same language, different subject-matter vocabulary
  - Within-section Jaccard (A-herbal vs B-herbal) should be HIGH
  - Function words should be shared; content words differ
  - A/B should correlate strongly with section type
  Evidence: [see Test 1 cross-tabulation and Test 6 within-section Jaccard]

HYPOTHESIS 3: CIPHER KEY SPLIT
  Prediction: Same plaintext, different EVA mappings
  - LOW Jaccard (confirmed: 0.172)
  - Frequency-matched word pairs should exist (A-word X has same freq as B-word Y)
  - Character frequencies should differ substantially
  - Morphological patterns should differ (different cipher = different surface patterns)
  Evidence: [see Test 3 cipher pairs and Test 8 character frequencies]

HYPOTHESIS 4: SCRIBE SPLIT
  Prediction: Same language and content, different handwriting conventions
  - Should correlate with PHYSICAL folios (consecutive runs)
  - Vocabulary differences should be minor (spelling variants only)
  - Function word frequencies should be nearly identical
  Evidence: [see folio distribution in Test 1]
""")


if __name__ == '__main__':
    main()
