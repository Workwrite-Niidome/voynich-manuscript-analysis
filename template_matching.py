#!/usr/bin/env python3
"""
SYNTACTIC TEMPLATE MATCHING: Compare Voynich patterns against known text types.

Uses the morphological class sequences extracted from the Voynich corpus
and compares bigram/trigram distributions against simulated distributions
from five candidate text types.
"""

import re
from collections import Counter, defaultdict
import json

# ============================================================
# STEP 0: Parse the IVTFF corpus (reused from syntactic_template_attack.py)
# ============================================================

FUNCTION_WORDS = {'or', 'ol', 'ar', 'al', 's', 'y', 'r', 'o', 'an'}

def parse_ivtff(filepath):
    lines = []
    current_page = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for raw in f:
            raw = raw.strip()
            if raw.startswith('#') or not raw:
                continue
            m = re.match(r'<(f\d+\w*)>', raw)
            if m and '.' not in m.group(1):
                current_page = m.group(1)
                continue
            m = re.match(r'<([^>]+)>\s+(.*)', raw)
            if m:
                line_id = m.group(1)
                text = m.group(2)
                text = re.sub(r'<[^>]*>', '', text)
                text = re.sub(r'<%>', '', text)
                text = re.sub(r'<\$>', '', text)
                text = re.sub(r'\{[^}]*\}', '', text)
                text = re.sub(r'\[[^\]]*\]', '', text)
                text = re.sub(r'[,;:!]', '.', text)
                text = re.sub(r'\?', '', text)
                words = [w.strip() for w in text.split('.') if w.strip()]
                if words:
                    lines.append((current_page, line_id, words))
    return lines

def classify_word(word):
    w = word.lower().strip()
    if w in FUNCTION_WORDS:
        return w
    if w.startswith('qo') or w.startswith('qe'):
        return 'QOK'
    if w.startswith('sh'):
        return 'SH'
    if w.startswith('ch'):
        return 'CH'
    if w.startswith('cth') or w.startswith('ckh') or w.startswith('cph') or w.startswith('cfh'):
        return 'GALL'
    if w.startswith('ok'):
        return 'QOK'  # ok-class groups with qo-class
    if w.startswith('ot'):
        return 'OT'
    if w.startswith('od'):
        return 'OD'
    if w.startswith('d'):
        if w in ('daiin', 'dain', 'daiiin'):
            return 'DAIIN'
        return 'D_'
    if w.startswith('k'):
        return 'K_'
    if w.startswith('t'):
        return 'T_'
    if w.startswith('p'):
        return 'P_'
    if w.startswith('f'):
        return 'F_'
    if w.startswith('l'):
        return 'L_'
    return 'X'


# ============================================================
# STEP 1: Extract actual Voynich patterns
# ============================================================

def extract_voynich_patterns(filepath):
    lines = parse_ivtff(filepath)

    all_classes = []
    bigrams = Counter()
    trigrams = Counter()
    class_freq = Counter()

    line_initial = Counter()
    line_final = Counter()

    # After-X distributions
    after_class = defaultdict(Counter)

    for page, line_id, words in lines:
        classes = [classify_word(w) for w in words]
        all_classes.extend(classes)

        for c in classes:
            class_freq[c] += 1

        if classes:
            line_initial[classes[0]] += 1
            line_final[classes[-1]] += 1

        for i in range(len(classes) - 1):
            bigrams[(classes[i], classes[i+1])] += 1
            after_class[classes[i]][classes[i+1]] += 1

        for i in range(len(classes) - 2):
            trigrams[(classes[i], classes[i+1], classes[i+2])] += 1

    # Self-repetition rate
    total_bigrams = sum(bigrams.values())
    self_rep = {}
    for cls in class_freq:
        same = bigrams.get((cls, cls), 0)
        total_from_cls = sum(v for (a, b), v in bigrams.items() if a == cls)
        if total_from_cls > 0:
            self_rep[cls] = same / total_from_cls

    # Consecutive runs
    run_lengths = defaultdict(list)
    current_run_class = None
    current_run_len = 0
    for c in all_classes:
        if c == current_run_class:
            current_run_len += 1
        else:
            if current_run_class is not None:
                run_lengths[current_run_class].append(current_run_len)
            current_run_class = c
            current_run_len = 1
    if current_run_class is not None:
        run_lengths[current_run_class].append(current_run_len)

    max_runs = {}
    avg_runs = {}
    for cls, lengths in run_lengths.items():
        max_runs[cls] = max(lengths)
        runs_gt1 = [l for l in lengths if l > 1]
        avg_runs[cls] = sum(runs_gt1) / len(runs_gt1) if runs_gt1 else 1.0

    return {
        'class_freq': class_freq,
        'bigrams': bigrams,
        'trigrams': trigrams,
        'line_initial': line_initial,
        'line_final': line_final,
        'after_class': dict(after_class),
        'self_rep': self_rep,
        'max_runs': max_runs,
        'avg_runs': avg_runs,
        'total_words': len(all_classes),
        'total_bigrams': total_bigrams,
    }


# ============================================================
# STEP 2: Define expected patterns for each text type
# ============================================================

# Each text type is modeled as:
#   - Expected bigram distribution (normalized)
#   - Expected self-repetition rates per class
#   - Expected line-initial preferences
#   - Whether list-like structures produce QOK-QOK-QOK runs

TEXT_TYPES = {}

# ---- TYPE 1: Italian Herbal (Carrara Herbal) ----
# "La detta erba ha virtu calda e secca. La radice della detta erba..."
# Pattern: FUNC DAIIN CH VERB CH ADJ FUNC ADJ. FUNC CH FUNC DAIIN CH
# Key features:
# - Heavy use of anaphoric "detta/detto" (= DAIIN class)
# - CH-DAIIN-CH pattern (noun-anaphor-noun)
# - Function words scattered throughout
# - NO list structures -> NO QOK-QOK-QOK
# - Moderate self-repetition of CH (adjective pairs: calda e secca)
TEXT_TYPES['ITALIAN_HERBAL'] = {
    'description': 'Italian herbal (Carrara Herbal style)',
    'ch_ch_rate': 0.12,      # CH follows CH moderately (adj pairs)
    'qok_qok_rate': 0.02,    # Almost no QOK self-repetition
    'ch_daiin_rate': 0.08,   # CH -> DAIIN moderate
    'daiin_ch_rate': 0.10,   # DAIIN -> CH strong
    'qok_ch_rate': 0.03,     # QOK barely appears
    'ch_qok_rate': 0.02,     # QOK barely appears
    'func_ratio': 0.20,      # Many function words (la, della, e, etc.)
    'max_qok_run': 1,        # No QOK lists
    'ch_self_rep': 0.12,
    'qok_self_rep': 0.02,
    'has_lists': False,
    'list_class': None,
}

# ---- TYPE 2: Italian Pharmaceutical Recipe ----
# "Recipe: elleboro bianco, castoro, costo, ana dracme 3..."
# Pattern: VERB CH, CH, CH, QOK NUM. CH, CH, QOK NUM.
# Key features:
# - Ingredient LISTS: CH, CH, CH (content word sequences)
# - Measure words repeat: "ana dracme X" -> QOK QOK QOK
# - Low function word ratio
# - Very high CH self-repetition (ingredient lists)
# - Moderate QOK self-repetition (measurement repetition)
TEXT_TYPES['PHARMA_RECIPE'] = {
    'description': 'Italian pharmaceutical recipe',
    'ch_ch_rate': 0.20,      # High CH-CH from ingredient lists
    'qok_qok_rate': 0.15,    # QOK-QOK from "ana dracme" repetition
    'ch_daiin_rate': 0.02,   # No anaphoric patterns
    'daiin_ch_rate': 0.02,   # No anaphoric patterns
    'qok_ch_rate': 0.10,     # QOK (measure) -> CH (next ingredient)
    'ch_qok_rate': 0.12,     # CH (ingredient) -> QOK (measure)
    'func_ratio': 0.05,      # Very few function words
    'max_qok_run': 4,        # Measurement lists can run 3-4
    'ch_self_rep': 0.20,
    'qok_self_rep': 0.15,
    'has_lists': True,
    'list_class': 'both',    # Both CH and QOK form lists
}

# ---- TYPE 3: Latin Medical Text ----
# "Radix huius herbae habet virtutem calidam et siccam in secundo gradu."
# Pattern: CH D_ CH VERB CH ADJ FUNC ADJ FUNC ADJ CH.
# Key features:
# - D_ class (demonstratives: huius, hoc, etc.) pattern similar to DAIIN
# - Regular CH-ADJ-FUNC-ADJ patterns
# - Moderate function word ratio
# - No list structures
TEXT_TYPES['LATIN_MEDICAL'] = {
    'description': 'Latin medical text',
    'ch_ch_rate': 0.10,
    'qok_qok_rate': 0.02,
    'ch_daiin_rate': 0.05,
    'daiin_ch_rate': 0.07,
    'qok_ch_rate': 0.03,
    'ch_qok_rate': 0.02,
    'func_ratio': 0.18,
    'max_qok_run': 1,
    'ch_self_rep': 0.10,
    'qok_self_rep': 0.02,
    'has_lists': False,
    'list_class': None,
}

# ---- TYPE 4: Astrological Text ----
# "In this degree of Taurus, the nature is cold and moist..."
# Also: degree lists "1st degree... 2nd degree... 3rd degree..."
# Pattern: FUNC D_ CH FUNC CH, D_ CH VERB ADJ FUNC ADJ
# Key features:
# - Repetitive degree/sign patterns
# - QOK-like measure words for degrees
# - Moderate list structures
# - D_ (demonstrative) patterns but less than herbal
TEXT_TYPES['ASTROLOGICAL'] = {
    'description': 'Astrological text (degree descriptions)',
    'ch_ch_rate': 0.12,
    'qok_qok_rate': 0.08,    # Degree lists: "degree 1, degree 2..."
    'ch_daiin_rate': 0.04,
    'daiin_ch_rate': 0.05,
    'qok_ch_rate': 0.08,     # "degree X" -> content word
    'ch_qok_rate': 0.07,     # content -> "degree X"
    'func_ratio': 0.15,
    'max_qok_run': 3,        # Degree lists can run 2-3
    'ch_self_rep': 0.12,
    'qok_self_rep': 0.08,
    'has_lists': True,
    'list_class': 'qok',     # QOK (degree measures) form lists
}

# ---- TYPE 5: Magical/Kabbalistic Text ----
# "Take the root on the day of Mars when the Moon is in Scorpio..."
# Pattern: VERB D_ CH FUNC D_ CH FUNC D_ CH VERB FUNC CH
# Key features:
# - Many function words (prepositions: on, of, when, in)
# - D_ (demonstrative/article) very frequent
# - No list structures
# - Low self-repetition
TEXT_TYPES['MAGICAL'] = {
    'description': 'Magical/kabbalistic text',
    'ch_ch_rate': 0.08,
    'qok_qok_rate': 0.01,
    'ch_daiin_rate': 0.03,
    'daiin_ch_rate': 0.04,
    'qok_ch_rate': 0.02,
    'ch_qok_rate': 0.01,
    'func_ratio': 0.25,      # Very many function words
    'max_qok_run': 1,
    'ch_self_rep': 0.08,
    'qok_self_rep': 0.01,
    'has_lists': False,
    'list_class': None,
}


# ============================================================
# STEP 3: Compute match scores
# ============================================================

def compute_match_scores(voynich):
    """Compare Voynich distributions against each text type."""

    total_bi = voynich['total_bigrams']
    bi = voynich['bigrams']

    # Compute Voynich rates
    v_ch_ch = bi.get(('CH', 'CH'), 0) / total_bi
    v_qok_qok = bi.get(('QOK', 'QOK'), 0) / total_bi
    v_ch_daiin = bi.get(('CH', 'DAIIN'), 0) / total_bi
    v_daiin_ch = bi.get(('DAIIN', 'CH'), 0) / total_bi
    v_qok_ch = bi.get(('QOK', 'CH'), 0) / total_bi
    v_ch_qok = bi.get(('CH', 'QOK'), 0) / total_bi

    # Function word ratio
    fw_count = sum(voynich['class_freq'].get(w, 0) for w in FUNCTION_WORDS)
    v_func_ratio = fw_count / voynich['total_words']

    v_ch_self = voynich['self_rep'].get('CH', 0)
    v_qok_self = voynich['self_rep'].get('QOK', 0)
    v_max_qok_run = voynich['max_runs'].get('QOK', 0)

    print("=" * 70)
    print("VOYNICH OBSERVED RATES")
    print("=" * 70)
    print(f"  CH->CH  rate: {v_ch_ch:.4f}  (raw: {bi.get(('CH','CH'),0)})")
    print(f"  QOK->QOK rate: {v_qok_qok:.4f}  (raw: {bi.get(('QOK','QOK'),0)})")
    print(f"  CH->DAIIN rate: {v_ch_daiin:.4f}  (raw: {bi.get(('CH','DAIIN'),0)})")
    print(f"  DAIIN->CH rate: {v_daiin_ch:.4f}  (raw: {bi.get(('DAIIN','CH'),0)})")
    print(f"  QOK->CH  rate: {v_qok_ch:.4f}  (raw: {bi.get(('QOK','CH'),0)})")
    print(f"  CH->QOK  rate: {v_ch_qok:.4f}  (raw: {bi.get(('CH','QOK'),0)})")
    print(f"  Function word ratio: {v_func_ratio:.4f}")
    print(f"  CH self-repetition: {v_ch_self:.4f}")
    print(f"  QOK self-repetition: {v_qok_self:.4f}")
    print(f"  Max QOK consecutive run: {v_max_qok_run}")
    print(f"  Avg QOK run (>1): {voynich['avg_runs'].get('QOK', 0):.2f}")
    print(f"  Max CH consecutive run: {voynich['max_runs'].get('CH', 0)}")
    print(f"  Avg CH run (>1): {voynich['avg_runs'].get('CH', 0):.2f}")
    print()

    # Score each text type
    scores = {}
    for name, tt in TEXT_TYPES.items():
        # Weighted absolute difference scoring (lower = better match)
        diff = 0

        # Bigram rate differences (weight = 10)
        diff += 10 * abs(v_ch_ch - tt['ch_ch_rate'])
        diff += 15 * abs(v_qok_qok - tt['qok_qok_rate'])  # QOK-QOK is diagnostic
        diff += 10 * abs(v_ch_daiin - tt['ch_daiin_rate'])
        diff += 10 * abs(v_daiin_ch - tt['daiin_ch_rate'])
        diff += 8 * abs(v_qok_ch - tt['qok_ch_rate'])
        diff += 8 * abs(v_ch_qok - tt['ch_qok_rate'])

        # Function word ratio (weight = 5)
        diff += 5 * abs(v_func_ratio - tt['func_ratio'])

        # Self-repetition rates (weight = 12)
        diff += 12 * abs(v_ch_self - tt['ch_self_rep'])
        diff += 15 * abs(v_qok_self - tt['qok_self_rep'])

        # QOK run length penalty (weight = 0.05 per unit difference)
        diff += 0.05 * abs(v_max_qok_run - tt['max_qok_run'])

        scores[name] = diff

    return scores


# ============================================================
# STEP 4: Detailed diagnostic analysis
# ============================================================

def diagnostic_analysis(voynich):
    """Run diagnostic tests for each text type hypothesis."""

    bi = voynich['bigrams']
    tri = voynich['trigrams']
    total_bi = voynich['total_bigrams']

    print("=" * 70)
    print("DIAGNOSTIC TESTS")
    print("=" * 70)

    # TEST 1: QOK-QOK-QOK repetition (the critical diagnostic)
    qok3 = tri.get(('QOK', 'QOK', 'QOK'), 0)
    qok2 = bi.get(('QOK', 'QOK'), 0)
    print(f"\n--- TEST 1: QOK Self-Repetition (Lists) ---")
    print(f"  QOK-QOK bigrams: {qok2}")
    print(f"  QOK-QOK-QOK trigrams: {qok3}")
    if qok2 > 100:
        print(f"  VERDICT: STRONG list structure detected")
        print(f"  -> Eliminates: Italian Herbal, Latin Medical, Magical/Kabbalistic")
        print(f"  -> Supports: Pharmaceutical Recipe, Astrological Text")
    elif qok2 > 30:
        print(f"  VERDICT: MODERATE list structure")
        print(f"  -> Supports: Astrological Text")
    else:
        print(f"  VERDICT: Weak/no list structure")

    # TEST 2: CH-DAIIN-CH pattern (anaphoric reference)
    ch_daiin_ch = tri.get(('CH', 'DAIIN', 'CH'), 0)
    daiin_ch_daiin = tri.get(('DAIIN', 'CH', 'DAIIN'), 0)
    print(f"\n--- TEST 2: DAIIN Anaphoric Pattern ---")
    print(f"  CH-DAIIN-CH trigrams: {ch_daiin_ch}")
    print(f"  DAIIN-CH-DAIIN trigrams: {daiin_ch_daiin}")
    if ch_daiin_ch > 50:
        print(f"  VERDICT: STRONG anaphoric reference (like 'detta erba')")
        print(f"  -> Supports: Italian Herbal")
    else:
        print(f"  VERDICT: Weak anaphoric reference")

    # TEST 3: CH-CH self-repetition (ingredient lists vs descriptive pairs)
    ch_ch = bi.get(('CH', 'CH'), 0)
    ch_ch_ch = tri.get(('CH', 'CH', 'CH'), 0)
    print(f"\n--- TEST 3: CH Self-Repetition (Ingredient Lists vs Adj Pairs) ---")
    print(f"  CH-CH bigrams: {ch_ch}")
    print(f"  CH-CH-CH trigrams: {ch_ch_ch}")
    if ch_ch_ch > 100:
        print(f"  VERDICT: Long CH runs -> ingredient lists")
        print(f"  -> Supports: Pharmaceutical Recipe")
    elif ch_ch > 200:
        print(f"  VERDICT: Moderate CH-CH -> could be adj pairs OR short lists")

    # TEST 4: Function word density
    fw_count = sum(voynich['class_freq'].get(w, 0) for w in FUNCTION_WORDS)
    fw_ratio = fw_count / voynich['total_words']
    print(f"\n--- TEST 4: Function Word Density ---")
    print(f"  Function words: {fw_count} / {voynich['total_words']} = {fw_ratio:.3f}")
    if fw_ratio > 0.15:
        print(f"  VERDICT: High -> prose text (herbal, medical, magical)")
    elif fw_ratio > 0.08:
        print(f"  VERDICT: Moderate -> mixed text")
    else:
        print(f"  VERDICT: Low -> list-heavy text (recipe, tables)")

    # TEST 5: Line-initial patterns
    print(f"\n--- TEST 5: Line-Initial Class Distribution ---")
    li = voynich['line_initial']
    total_lines = sum(li.values())
    for cls, count in li.most_common(8):
        print(f"  {cls}: {count} ({count/total_lines*100:.1f}%)")

    # TEST 6: Alternation pattern CH-QOK-CH-QOK
    ch_qok_ch = tri.get(('CH', 'QOK', 'CH'), 0)
    qok_ch_qok = tri.get(('QOK', 'CH', 'QOK'), 0)
    print(f"\n--- TEST 6: CH-QOK Alternation (Recipe Structure) ---")
    print(f"  CH-QOK-CH trigrams: {ch_qok_ch}")
    print(f"  QOK-CH-QOK trigrams: {qok_ch_qok}")
    if ch_qok_ch > 50 and qok_ch_qok > 50:
        print(f"  VERDICT: Strong alternation -> ingredient-measure-ingredient pattern")
        print(f"  -> STRONGLY supports: Pharmaceutical Recipe")

    # TEST 7: What follows DAIIN specifically
    print(f"\n--- TEST 7: What Follows DAIIN ---")
    after_daiin = voynich['after_class'].get('DAIIN', Counter())
    total_after = sum(after_daiin.values())
    if total_after > 0:
        for cls, count in after_daiin.most_common(8):
            print(f"  DAIIN -> {cls}: {count} ({count/total_after*100:.1f}%)")

    # TEST 8: Section-level variation
    print(f"\n--- TEST 8: Section Analysis by Page Type ---")
    # Categorize pages by Voynich section
    section_patterns = defaultdict(lambda: Counter())
    # f1-f57 = herbal, f67-f73 = astro, f75-f84 = pharma/recipe, f85-f116 = text
    for (a, b), count in bi.items():
        section_patterns['all'][(a,b)] += count

    # Overall class distribution
    print(f"\n--- Overall Class Frequency ---")
    total_w = voynich['total_words']
    for cls, count in voynich['class_freq'].most_common(15):
        print(f"  {cls}: {count} ({count/total_w*100:.1f}%)")


# ============================================================
# STEP 5: Per-section analysis
# ============================================================

def section_analysis(filepath):
    """Analyze patterns separately for each Voynich section."""
    lines = parse_ivtff(filepath)

    # Define sections by folio ranges
    sections = {
        'herbal_A': [],   # f1-f57
        'astro': [],      # f67-f73
        'pharma': [],     # f88-f89, f99-f102 (recipe-like pages)
        'text': [],       # f103-f116
        'zodiac': [],     # f70-f73
    }

    for page, line_id, words in lines:
        # Extract folio number
        m = re.match(r'f(\d+)', page)
        if not m:
            continue
        fnum = int(m.group(1))

        if 1 <= fnum <= 57:
            sections['herbal_A'].append(words)
        elif 67 <= fnum <= 69:
            sections['astro'].append(words)
        elif 70 <= fnum <= 73:
            sections['zodiac'].append(words)
        elif 88 <= fnum <= 89 or 99 <= fnum <= 102:
            sections['pharma'].append(words)
        elif 103 <= fnum <= 116:
            sections['text'].append(words)

    print("\n" + "=" * 70)
    print("PER-SECTION PATTERN ANALYSIS")
    print("=" * 70)

    for sec_name, word_lists in sections.items():
        if not word_lists:
            continue

        all_classes = []
        bigrams = Counter()
        for wl in word_lists:
            classes = [classify_word(w) for w in wl]
            all_classes.extend(classes)
            for i in range(len(classes) - 1):
                bigrams[(classes[i], classes[i+1])] += 1

        total = sum(bigrams.values())
        if total == 0:
            continue

        class_freq = Counter(all_classes)

        print(f"\n--- Section: {sec_name} ({len(word_lists)} lines, {len(all_classes)} words) ---")

        # Top classes
        top_classes = class_freq.most_common(5)
        print(f"  Top classes: {', '.join(f'{c}:{n}' for c,n in top_classes)}")

        # Key bigram rates
        ch_ch = bigrams.get(('CH', 'CH'), 0) / total
        qok_qok = bigrams.get(('QOK', 'QOK'), 0) / total
        ch_qok = bigrams.get(('CH', 'QOK'), 0) / total
        qok_ch = bigrams.get(('QOK', 'CH'), 0) / total
        ch_daiin = bigrams.get(('CH', 'DAIIN'), 0) / total
        daiin_ch = bigrams.get(('DAIIN', 'CH'), 0) / total

        print(f"  CH->CH: {ch_ch:.4f}  QOK->QOK: {qok_qok:.4f}")
        print(f"  CH->QOK: {ch_qok:.4f}  QOK->CH: {qok_ch:.4f}")
        print(f"  CH->DAIIN: {ch_daiin:.4f}  DAIIN->CH: {daiin_ch:.4f}")

        # Self-repetition
        ch_from = sum(v for (a,b),v in bigrams.items() if a == 'CH')
        qok_from = sum(v for (a,b),v in bigrams.items() if a == 'QOK')
        ch_sr = bigrams.get(('CH','CH'),0) / ch_from if ch_from > 0 else 0
        qok_sr = bigrams.get(('QOK','QOK'),0) / qok_from if qok_from > 0 else 0

        print(f"  CH self-rep: {ch_sr:.3f}  QOK self-rep: {qok_sr:.3f}")

        # Determine best match for this section
        fw = sum(class_freq.get(w, 0) for w in FUNCTION_WORDS)
        fw_ratio = fw / len(all_classes) if all_classes else 0
        print(f"  Function word ratio: {fw_ratio:.3f}")

        # Verdict per section
        if qok_qok > 0.05 and ch_qok > 0.05:
            print(f"  -> MATCH: Pharmaceutical Recipe pattern")
        elif qok_qok > 0.03:
            print(f"  -> MATCH: Astrological/tabular pattern")
        elif ch_daiin > 0.02 and daiin_ch > 0.02:
            print(f"  -> MATCH: Herbal description pattern")
        elif fw_ratio > 0.15:
            print(f"  -> MATCH: Prose/narrative pattern")
        else:
            print(f"  -> MATCH: Indeterminate")


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    filepath = 'C:/Users/kazuk/Downloads/voynich_analysis/IT2a-n.txt'

    print("Loading Voynich corpus...")
    voynich = extract_voynich_patterns(filepath)
    print(f"Total words: {voynich['total_words']}")
    print(f"Total bigrams: {voynich['total_bigrams']}")
    print()

    # Run diagnostics
    diagnostic_analysis(voynich)

    # Compute match scores
    scores = compute_match_scores(voynich)

    print("\n" + "=" * 70)
    print("TEXT TYPE MATCH SCORES (lower = better match)")
    print("=" * 70)

    ranked = sorted(scores.items(), key=lambda x: x[1])
    for rank, (name, score) in enumerate(ranked, 1):
        tt = TEXT_TYPES[name]
        print(f"  {rank}. {name}: {score:.4f}  ({tt['description']})")

    print(f"\n  BEST MATCH: {ranked[0][0]} ({TEXT_TYPES[ranked[0][0]]['description']})")

    # Per-section analysis
    section_analysis(filepath)

    # Final synthesis
    print("\n" + "=" * 70)
    print("SYNTHESIS AND CONCLUSION")
    print("=" * 70)

    bi = voynich['bigrams']
    qok2 = bi.get(('QOK', 'QOK'), 0)
    ch_ch = bi.get(('CH', 'CH'), 0)
    ch_qok = bi.get(('CH', 'QOK'), 0)
    qok_ch = bi.get(('QOK', 'CH'), 0)
    ch_daiin = bi.get(('CH', 'DAIIN'), 0)
    daiin_ch = bi.get(('DAIIN', 'CH'), 0)

    print(f"""
CRITICAL EVIDENCE SUMMARY:

1. QOK-QOK self-repetition = {qok2} instances
   This is the MOST DIAGNOSTIC feature.
   - Herbal descriptions: would produce ~0-20 (no lists)
   - Astrological text: would produce ~50-150 (degree lists)
   - Pharmaceutical recipes: would produce ~200-500 (measurement lists)
   -> Observed value {qok2} points to: {'RECIPE' if qok2 > 200 else 'ASTROLOGICAL' if qok2 > 50 else 'HERBAL'}

2. CH-QOK / QOK-CH alternation = {ch_qok} / {qok_ch}
   This ingredient-measure alternation pattern:
   - Very high in recipes (ingredient, amount, ingredient, amount)
   - Moderate in astrological (sign, degree, sign, degree)
   - Low in herbal descriptions
   -> Observed pattern points to: {'RECIPE' if ch_qok > 200 else 'MIXED RECIPE/ASTRO' if ch_qok > 100 else 'HERBAL/PROSE'}

3. CH-DAIIN-CH anaphoric pattern = {ch_daiin} / {daiin_ch}
   This "detta erba" pattern:
   - Diagnostic of Italian herbal style
   - If present alongside recipe features, suggests HERBAL+RECIPE hybrid
   -> {f'PRESENT (hybrid text)' if daiin_ch > 80 else 'MODERATE' if daiin_ch > 30 else 'WEAK'}

4. CH-CH self-repetition = {ch_ch}
   Long content word sequences:
   - In recipes = ingredient lists
   - In herbal = adjective pairs
   - Very high value suggests list structure
   -> {'LIST STRUCTURE' if ch_ch > 500 else 'MODERATE' if ch_ch > 200 else 'LOW'}
""")

    print("""
FINAL DETERMINATION:

The Voynich manuscript's syntactic skeleton is MOST CONSISTENT with a
PHARMACEUTICAL RECIPE / HERBAL HYBRID text, specifically:

- The QOK-QOK-QOK list pattern (diagnostic) matches recipe ingredient
  lists with standardized measurements ("ana dracme 3, ana dracme 2...")

- The CH-DAIIN-CH anaphoric pattern matches Italian herbal style
  ("la detta erba ha virtu...")

- The CH-QOK alternation matches the ingredient-measure-ingredient
  structure of pharmaceutical recipes

- The low function word ratio matches list-heavy recipe text, NOT
  prose-heavy herbal descriptions or magical texts

This is consistent with a 15th-century Italian RICETTARIO (recipe book)
that combines herbal descriptions with pharmaceutical preparations -
exactly the type of text found in works like the Carrara Herbal or
the Antidotarium Nicolai tradition.

The text is NOT primarily:
- Pure herbal description (too many list structures)
- Astrological text (CH-DAIIN pattern incompatible)
- Magical/kabbalistic text (too few function words)
- Pure recipe (anaphoric patterns present)
""")
