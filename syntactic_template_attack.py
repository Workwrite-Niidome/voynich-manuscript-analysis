#!/usr/bin/env python3
"""
SYNTACTIC TEMPLATE EXTRACTION ATTACK on the Voynich Manuscript

Instead of deciphering individual words, we:
1. Classify every word by morphological class (prefix-based)
2. Extract sentence/line templates as sequences of classes
3. Compare template distributions against known text types
4. Identify which language/genre best matches the grammatical skeleton

Uses the IT2a-n.txt (Takahashi) transcription as primary corpus.
"""

import re
from collections import Counter, defaultdict
import json
import math

# ============================================================
# STEP 0: Parse the IVTFF corpus
# ============================================================

def parse_ivtff(filepath):
    """Parse IVTFF format, return list of (page, line_id, words)."""
    lines = []
    current_page = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for raw in f:
            raw = raw.strip()
            if raw.startswith('#') or not raw:
                continue
            # Page header
            m = re.match(r'<(f\d+\w*)>', raw)
            if m and '.' not in m.group(1):
                current_page = m.group(1)
                continue
            # Line with text
            m = re.match(r'<([^>]+)>\s+(.*)', raw)
            if m:
                line_id = m.group(1)
                text = m.group(2)
                # Clean markup
                text = re.sub(r'<[^>]*>', '', text)  # remove tags
                text = re.sub(r'<%>', '', text)       # paragraph markers
                text = re.sub(r'<\$>', '', text)      # end markers
                text = re.sub(r'\{[^}]*\}', '', text) # comments
                text = re.sub(r'\[[^\]]*\]', '', text) # alternatives - remove
                text = re.sub(r'[,;:!]', '.', text)   # normalize separators to .
                text = re.sub(r'\?', '', text)         # remove uncertain markers
                # Split into words (. is the word separator in EVA)
                words = [w.strip() for w in text.split('.') if w.strip()]
                if words:
                    lines.append((current_page, line_id, words))
    return lines


# ============================================================
# STEP 1: Morphological classification
# ============================================================

FUNCTION_WORDS = {'or', 'ol', 'ar', 'al', 's', 'y', 'r', 'o', 'an'}

def classify_word(word):
    """Classify a word into its morphological class."""
    w = word.lower().strip()

    if w in FUNCTION_WORDS:
        return w  # Keep function words as-is

    # Prefix-based classification (order matters - longer prefixes first)
    if w.startswith('qo') or w.startswith('qe'):
        return '[QO]'
    if w.startswith('sh'):
        return '[SH]'
    if w.startswith('ch'):
        return '[CH]'
    if w.startswith('cth') or w.startswith('ckh') or w.startswith('cph') or w.startswith('cfh'):
        return '[CTH]'  # Gallows characters
    if w.startswith('ok'):
        return '[OK]'
    if w.startswith('ot'):
        return '[OT]'
    if w.startswith('od'):
        return '[OD]'
    if w.startswith('d'):
        return '[D]'
    if w.startswith('k'):
        return '[K]'
    if w.startswith('t'):
        return '[T]'
    if w.startswith('p'):
        return '[P]'
    if w.startswith('f'):
        return '[F]'
    if w.startswith('l'):
        return '[L]'

    # Suffix-based sub-classification
    if w.endswith('aiin') or w.endswith('ain'):
        return '[*AIN]'  # any prefix + -aiin ending
    if w.endswith('edy') or w.endswith('eey') or w.endswith('ey'):
        return '[*EY]'
    if w.endswith('chy') or w.endswith('shy') or w.endswith('dy'):
        return '[*Y]'
    if w.endswith('ol') or w.endswith('al'):
        return '[*OL]'

    return '[X]'  # unclassified


def classify_word_detailed(word):
    """More detailed classification considering both prefix AND suffix."""
    w = word.lower().strip()

    if w in FUNCTION_WORDS:
        return w

    # Determine prefix class
    prefix = ''
    if w.startswith('qo') or w.startswith('qe'):
        prefix = 'QO'
    elif w.startswith('cth') or w.startswith('ckh') or w.startswith('cph') or w.startswith('cfh'):
        prefix = 'G'  # Gallows
    elif w.startswith('sh'):
        prefix = 'SH'
    elif w.startswith('ch'):
        prefix = 'CH'
    elif w.startswith('ok'):
        prefix = 'OK'
    elif w.startswith('ot'):
        prefix = 'OT'
    elif w.startswith('od'):
        prefix = 'OD'
    elif w.startswith('d'):
        prefix = 'D'
    elif w.startswith('k'):
        prefix = 'K'
    elif w.startswith('t'):
        prefix = 'T'
    elif w.startswith('p'):
        prefix = 'P'
    elif w.startswith('f'):
        prefix = 'F'
    elif w.startswith('l'):
        prefix = 'L'
    elif w.startswith('o'):
        prefix = 'O'
    else:
        prefix = 'X'

    # Determine suffix class
    suffix = ''
    if w.endswith('aiin') or w.endswith('aiiin'):
        suffix = 'AIN'
    elif w.endswith('ain') or w.endswith('ain'):
        suffix = 'AIN'
    elif w.endswith('eey') or w.endswith('ey'):
        suffix = 'EY'
    elif w.endswith('edy') or w.endswith('ody'):
        suffix = 'DY'
    elif w.endswith('chy') or w.endswith('shy') or w.endswith('thy'):
        suffix = 'CY'
    elif w.endswith('dy') or w.endswith('ry') or w.endswith('ly'):
        suffix = 'Y'
    elif w.endswith('ol') or w.endswith('al'):
        suffix = 'OL'
    elif w.endswith('or') or w.endswith('ar'):
        suffix = 'OR'
    elif w.endswith('os') or w.endswith('as'):
        suffix = 'OS'
    elif w.endswith('an') or w.endswith('on'):
        suffix = 'AN'
    else:
        suffix = 'X'

    return f'[{prefix}.{suffix}]'


# ============================================================
# STEP 2: Template extraction
# ============================================================

def extract_templates(lines, classifier=classify_word):
    """Convert each line to a template of morphological classes."""
    templates = []
    for page, line_id, words in lines:
        template = tuple(classifier(w) for w in words)
        templates.append((page, line_id, words, template))
    return templates


def get_paragraph_templates(lines, classifier=classify_word):
    """Group lines into paragraphs and extract paragraph-level templates."""
    paragraphs = []
    current_para = []
    current_page = None

    for page, line_id, words in lines:
        # Detect paragraph boundary: *P0 or @P0 markers indicate paragraph start
        is_para_start = '@P' in line_id or '*P' in line_id

        if is_para_start and current_para:
            paragraphs.append(current_para)
            current_para = []

        current_para.extend(words)
        current_page = page

    if current_para:
        paragraphs.append(current_para)

    # Classify each paragraph
    para_templates = []
    for para_words in paragraphs:
        template = tuple(classifier(w) for w in para_words)
        para_templates.append((para_words, template))

    return para_templates


# ============================================================
# STEP 3: Statistical analysis of templates
# ============================================================

def analyze_templates(templates):
    """Analyze template patterns."""
    results = {}

    # Line-level template frequency
    template_counter = Counter()
    for _, _, _, tmpl in templates:
        template_counter[tmpl] += 1

    results['total_lines'] = len(templates)
    results['unique_templates'] = len(template_counter)
    results['most_common_templates'] = template_counter.most_common(30)

    # Bigram patterns (adjacent class pairs)
    bigram_counter = Counter()
    for _, _, _, tmpl in templates:
        for i in range(len(tmpl) - 1):
            bigram_counter[(tmpl[i], tmpl[i+1])] += 1
    results['most_common_bigrams'] = bigram_counter.most_common(40)

    # Trigram patterns
    trigram_counter = Counter()
    for _, _, _, tmpl in templates:
        for i in range(len(tmpl) - 2):
            trigram_counter[(tmpl[i], tmpl[i+1], tmpl[i+2])] += 1
    results['most_common_trigrams'] = trigram_counter.most_common(30)

    # Position analysis: what class appears at position 0, 1, 2, ... in a line?
    position_dist = defaultdict(Counter)
    for _, _, _, tmpl in templates:
        for i, cls in enumerate(tmpl):
            position_dist[i][cls] += 1
    results['position_distributions'] = {
        pos: counter.most_common(10)
        for pos, counter in sorted(position_dist.items())
        if pos < 12
    }

    # Line-initial class distribution
    first_word_dist = Counter()
    for _, _, _, tmpl in templates:
        if tmpl:
            first_word_dist[tmpl[0]] += 1
    results['line_initial'] = first_word_dist.most_common(15)

    # Line-final class distribution
    last_word_dist = Counter()
    for _, _, _, tmpl in templates:
        if tmpl:
            last_word_dist[tmpl[-1]] += 1
    results['line_final'] = last_word_dist.most_common(15)

    # Line length distribution
    length_dist = Counter()
    for _, _, _, tmpl in templates:
        length_dist[len(tmpl)] += 1
    results['line_lengths'] = sorted(length_dist.items())

    # Function word ratio per line
    fw_ratios = []
    for _, _, _, tmpl in templates:
        if tmpl:
            fw_count = sum(1 for c in tmpl if c in FUNCTION_WORDS)
            fw_ratios.append(fw_count / len(tmpl))
    results['avg_function_word_ratio'] = sum(fw_ratios) / len(fw_ratios) if fw_ratios else 0

    return results


def analyze_clause_patterns(templates):
    """Identify clause-like patterns separated by function words."""
    clause_patterns = Counter()

    for _, _, _, tmpl in templates:
        # Split template at function words to find "clause" patterns
        current_clause = []
        for cls in tmpl:
            if cls in FUNCTION_WORDS and current_clause:
                clause_patterns[tuple(current_clause)] += 1
                current_clause = []
            else:
                current_clause.append(cls)
        if current_clause:
            clause_patterns[tuple(current_clause)] += 1

    return clause_patterns.most_common(30)


# ============================================================
# STEP 4: Language/text-type comparison
# ============================================================

def compute_structural_signature(templates):
    """Compute a structural signature for comparison."""
    sig = {}

    all_classes = []
    for _, _, _, tmpl in templates:
        all_classes.extend(tmpl)

    total = len(all_classes)
    class_freq = Counter(all_classes)

    # Function word percentage
    fw_total = sum(class_freq[fw] for fw in FUNCTION_WORDS if fw in class_freq)
    sig['function_word_pct'] = fw_total / total * 100

    # Content word class distribution (normalized)
    content_classes = {k: v for k, v in class_freq.items() if k not in FUNCTION_WORDS}
    content_total = sum(content_classes.values())
    sig['content_class_dist'] = {
        k: v / content_total * 100
        for k, v in sorted(content_classes.items(), key=lambda x: -x[1])[:10]
    }

    # Average line length (in words)
    lengths = [len(tmpl) for _, _, _, tmpl in templates]
    sig['avg_line_length'] = sum(lengths) / len(lengths) if lengths else 0
    sig['median_line_length'] = sorted(lengths)[len(lengths)//2] if lengths else 0

    # Bigram entropy (measure of word-order rigidity)
    bigrams = Counter()
    for _, _, _, tmpl in templates:
        for i in range(len(tmpl) - 1):
            bigrams[(tmpl[i], tmpl[i+1])] += 1
    bg_total = sum(bigrams.values())
    entropy = -sum((c/bg_total) * math.log2(c/bg_total) for c in bigrams.values())
    sig['bigram_entropy'] = entropy

    # First/last word preferences
    first_words = Counter(tmpl[0] for _, _, _, tmpl in templates if tmpl)
    last_words = Counter(tmpl[-1] for _, _, _, tmpl in templates if tmpl)
    fw_total_first = sum(first_words.values())
    fw_total_last = sum(last_words.values())
    sig['first_word_top3'] = [(k, v/fw_total_first*100) for k, v in first_words.most_common(3)]
    sig['last_word_top3'] = [(k, v/fw_total_last*100) for k, v in last_words.most_common(3)]

    return sig


# ============================================================
# STEP 5: Known language structural models
# ============================================================

# Define expected structural patterns for different text types
# Based on linguistic typology

LANGUAGE_MODELS = {
    'Italian_Herbal': {
        'description': 'Italian herbal/pharmaceutical text (e.g., Pseudo-Mesue, Mattioli)',
        'expected_patterns': {
            'word_order': 'SVO with frequent noun phrases',
            'function_word_pct': (15, 25),  # prepositions: di, del, della, con, per, in, a
            'content_heavy_positions': 'Nouns at start, adjectives follow',
            'typical_template': 'NOUN PREP NOUN ADJ VERB PREP NOUN',
            # "Prendi la radice di questa erba e mettila nell'acqua"
            'line_initial_pattern': 'Content word (noun/verb) dominant at line start',
            'clause_structure': 'Head-initial, modifier follows',
        },
        'structural_features': {
            'fw_ratio': (0.15, 0.25),
            'avg_line_len': (6, 12),
            'adj_follows_noun': True,
            'verb_early': True,  # imperative "Prendi..." common in recipes
        }
    },
    'Latin_Herbal': {
        'description': 'Latin herbal/recipe text (e.g., Dioscorides, Circa Instans)',
        'expected_patterns': {
            'word_order': 'SOV tendency with flexible order',
            'function_word_pct': (8, 18),  # Latin has fewer prepositions, uses case
            'typical_template': 'NOUN ADJ PREP NOUN VERB',
            # "Herbam hanc in aqua decoque"
            'line_initial_pattern': 'Noun dominant',
            'clause_structure': 'Verb-final tendency',
        },
        'structural_features': {
            'fw_ratio': (0.08, 0.18),
            'avg_line_len': (5, 10),
            'adj_follows_noun': False,  # Latin adj often precedes
            'verb_final': True,
        }
    },
    'Italian_Astrology': {
        'description': 'Italian astrological text',
        'expected_patterns': {
            'word_order': 'SVO',
            'function_word_pct': (18, 28),
            'typical_template': 'NOUN VERB PREP NOUN CONJ NOUN VERB',
            # "Quando il sole entra nel segno del leone..."
        },
        'structural_features': {
            'fw_ratio': (0.18, 0.28),
            'avg_line_len': (8, 15),
        }
    },
    'Latin_Prayer': {
        'description': 'Latin liturgical/prayer text',
        'expected_patterns': {
            'word_order': 'VSO with vocatives',
            'function_word_pct': (10, 20),
            'typical_template': 'VERB NOUN ADJ PREP NOUN',
            # "Domine Deus omnipotens in caelis..."
        },
        'structural_features': {
            'fw_ratio': (0.10, 0.20),
            'avg_line_len': (5, 10),
        }
    },
    'Occitan_Recipe': {
        'description': 'Occitan/Provencal recipe or medical text',
        'expected_patterns': {
            'word_order': 'SVO like Italian but with more clitics',
            'function_word_pct': (18, 28),
        },
        'structural_features': {
            'fw_ratio': (0.18, 0.28),
            'avg_line_len': (6, 12),
        }
    },
    'Glossolalia_Constructed': {
        'description': 'Constructed/glossolalic text with pseudo-grammar',
        'expected_patterns': {
            'word_order': 'Repetitive, low entropy',
            'function_word_pct': (5, 40),  # wide range
        },
        'structural_features': {
            'fw_ratio': (0.05, 0.40),
            'avg_line_len': (4, 15),
            'high_template_repetition': True,
        }
    }
}


# ============================================================
# STEP 6: Cross-linguistic structural comparison
# ============================================================

def compare_with_reference_texts():
    """
    Compare Voynich structural patterns with known text structural patterns.

    Key structural features of natural languages for comparison:

    ITALIAN (SVO):
    - Prep + NP is very common: "di questa erba", "nella acqua"
    - Function words: di, del, della, con, per, in, a, il, la, le, lo, e, che
    - ~20-25% function words in running text
    - Adjective follows noun: "erba medicinale"
    - Articles precede nouns: "la radice"

    LATIN (flexible, SOV tendency):
    - Case endings instead of prepositions
    - ~10-15% function words (et, in, ad, cum, per)
    - Adjective often precedes: "magna virtus"
    - Verb often at end of clause

    OCCITAN:
    - Similar to Italian but with lo/la/los/las articles
    - "de la" contracts to "de la" or "dela"

    The KEY QUESTION: Does Voynich function word distribution match
    Italian preposition + article patterns, or Latin conjunction patterns?
    """
    pass


# ============================================================
# STEP 7: Detailed word-position analysis
# ============================================================

def analyze_function_word_contexts(lines, classifier=classify_word):
    """Analyze what surrounds each function word."""
    fw_contexts = defaultdict(lambda: {'before': Counter(), 'after': Counter()})

    for page, line_id, words in lines:
        classes = [classifier(w) for w in words]
        for i, (w, c) in enumerate(zip(words, classes)):
            if c in FUNCTION_WORDS:
                if i > 0:
                    fw_contexts[c]['before'][classes[i-1]] += 1
                if i < len(classes) - 1:
                    fw_contexts[c]['after'][classes[i+1]] += 1

    return fw_contexts


def analyze_sentence_boundaries(templates):
    """
    Identify likely sentence boundaries and extract sentence-level templates.
    In continuous text without punctuation, sentences might be delimited by:
    - Line boundaries
    - Repeated function word patterns
    - Paragraph markers
    """
    # For now, treat each paragraph as a sentence unit
    # and each line as a clause
    pass


# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    filepath = "C:/Users/kazuk/Downloads/voynich_analysis/IT2a-n.txt"

    print("=" * 80)
    print("SYNTACTIC TEMPLATE EXTRACTION ATTACK ON THE VOYNICH MANUSCRIPT")
    print("=" * 80)

    # Parse corpus
    lines = parse_ivtff(filepath)
    print(f"\nParsed {len(lines)} lines from corpus")

    # Count total words
    all_words = []
    for _, _, words in lines:
        all_words.extend(words)
    print(f"Total words: {len(all_words)}")
    print(f"Unique words: {len(set(all_words))}")

    # --------------------------------------------------------
    # STEP 1: Simple classification
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("STEP 1: MORPHOLOGICAL CLASSIFICATION")
    print("=" * 80)

    class_counter = Counter()
    for w in all_words:
        cls = classify_word(w)
        class_counter[cls] += 1

    total_w = len(all_words)
    print("\nWord class distribution:")
    for cls, count in class_counter.most_common(20):
        pct = count / total_w * 100
        example_words = [w for w in set(all_words) if classify_word(w) == cls][:5]
        print(f"  {cls:10s}: {count:5d} ({pct:5.1f}%)  examples: {', '.join(example_words[:5])}")

    # Function word ratio
    fw_count = sum(class_counter[fw] for fw in FUNCTION_WORDS)
    print(f"\nFunction word ratio: {fw_count}/{total_w} = {fw_count/total_w*100:.1f}%")

    # --------------------------------------------------------
    # STEP 2: Template extraction
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("STEP 2: LINE TEMPLATE EXTRACTION")
    print("=" * 80)

    templates = extract_templates(lines)
    analysis = analyze_templates(templates)

    print(f"\nTotal lines: {analysis['total_lines']}")
    print(f"Unique line templates: {analysis['unique_templates']}")
    print(f"Template-to-line ratio: {analysis['unique_templates']/analysis['total_lines']:.3f}")
    print("  (1.0 = every line unique, low = highly repetitive)")

    print(f"\nAverage function word ratio per line: {analysis['avg_function_word_ratio']:.3f}")

    print("\nLine length distribution (words per line):")
    for length, count in analysis['line_lengths']:
        bar = '#' * min(count, 50)
        print(f"  {length:2d} words: {count:4d} {bar}")

    print("\n--- Most common LINE TEMPLATES (top 20) ---")
    for tmpl, count in analysis['most_common_templates'][:20]:
        print(f"  {count:3d}x  {' '.join(tmpl)}")

    # --------------------------------------------------------
    # STEP 2b: Class bigrams
    # --------------------------------------------------------
    print("\n--- Most common CLASS BIGRAMS (adjacent word-class pairs) ---")
    for (a, b), count in analysis['most_common_bigrams'][:25]:
        print(f"  {count:4d}x  {a} -> {b}")

    print("\n--- Most common CLASS TRIGRAMS ---")
    for (a, b, c), count in analysis['most_common_trigrams'][:20]:
        print(f"  {count:3d}x  {a} {b} {c}")

    # --------------------------------------------------------
    # STEP 2c: Position analysis
    # --------------------------------------------------------
    print("\n--- POSITIONAL DISTRIBUTION (what class appears at each position?) ---")
    for pos in range(min(10, max(analysis['position_distributions'].keys()) + 1)):
        if pos in analysis['position_distributions']:
            top3 = analysis['position_distributions'][pos][:5]
            formatted = ', '.join(f"{cls}({cnt})" for cls, cnt in top3)
            print(f"  Position {pos}: {formatted}")

    print("\n--- LINE-INITIAL word class ---")
    for cls, count in analysis['line_initial']:
        pct = count / analysis['total_lines'] * 100
        print(f"  {cls:10s}: {count:4d} ({pct:5.1f}%)")

    print("\n--- LINE-FINAL word class ---")
    for cls, count in analysis['line_final']:
        pct = count / analysis['total_lines'] * 100
        print(f"  {cls:10s}: {count:4d} ({pct:5.1f}%)")

    # --------------------------------------------------------
    # STEP 3: Clause patterns
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("STEP 3: CLAUSE PATTERNS (segments between function words)")
    print("=" * 80)

    clause_patterns = analyze_clause_patterns(templates)
    print("\nMost common clause patterns:")
    for pattern, count in clause_patterns[:25]:
        print(f"  {count:3d}x  {' '.join(pattern)}")

    # --------------------------------------------------------
    # STEP 4: Function word context analysis
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("STEP 4: FUNCTION WORD CONTEXT ANALYSIS")
    print("=" * 80)

    fw_contexts = analyze_function_word_contexts(lines)
    for fw in sorted(fw_contexts.keys(), key=lambda x: -sum(fw_contexts[x]['before'].values())):
        total_occ = sum(fw_contexts[fw]['before'].values()) + sum(fw_contexts[fw]['after'].values())
        if total_occ < 20:
            continue
        print(f"\n  Function word '{fw}':")
        print(f"    Preceded by:  {', '.join(f'{c}({n})' for c, n in fw_contexts[fw]['before'].most_common(5))}")
        print(f"    Followed by:  {', '.join(f'{c}({n})' for c, n in fw_contexts[fw]['after'].most_common(5))}")

    # --------------------------------------------------------
    # STEP 5: Structural signature
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("STEP 5: STRUCTURAL SIGNATURE")
    print("=" * 80)

    sig = compute_structural_signature(templates)
    print(f"\n  Function word percentage: {sig['function_word_pct']:.1f}%")
    print(f"  Average line length: {sig['avg_line_length']:.1f} words")
    print(f"  Median line length: {sig['median_line_length']} words")
    print(f"  Bigram entropy: {sig['bigram_entropy']:.2f} bits")
    print(f"  First word top 3: {sig['first_word_top3']}")
    print(f"  Last word top 3: {sig['last_word_top3']}")
    print(f"\n  Content class distribution:")
    for cls, pct in sig['content_class_dist'].items():
        print(f"    {cls:10s}: {pct:5.1f}%")

    # --------------------------------------------------------
    # STEP 6: Language comparison
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("STEP 6: LANGUAGE/TEXT-TYPE STRUCTURAL COMPARISON")
    print("=" * 80)

    voynich_fw_pct = sig['function_word_pct']
    voynich_avg_len = sig['avg_line_length']

    print(f"\n  Voynich function word %: {voynich_fw_pct:.1f}%")
    print(f"  Voynich avg line length: {voynich_avg_len:.1f}")

    for lang, model in LANGUAGE_MODELS.items():
        print(f"\n  --- {lang}: {model['description']} ---")
        fw_range = model['structural_features']['fw_ratio']
        fw_pct_range = (fw_range[0] * 100, fw_range[1] * 100)
        len_range = model['structural_features']['avg_line_len']

        fw_match = fw_pct_range[0] <= voynich_fw_pct <= fw_pct_range[1]
        len_match = len_range[0] <= voynich_avg_len <= len_range[1]

        print(f"    FW% expected: {fw_pct_range[0]:.0f}-{fw_pct_range[1]:.0f}%  "
              f"{'MATCH' if fw_match else 'NO MATCH'}")
        print(f"    Line len expected: {len_range[0]}-{len_range[1]}  "
              f"{'MATCH' if len_match else 'NO MATCH'}")

    # --------------------------------------------------------
    # STEP 7: Detailed template matching
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("STEP 7: DEEP STRUCTURAL PATTERN MATCHING")
    print("=" * 80)

    # Key question: Does the Voynich show PREPOSITIONAL PHRASE structure?
    # In Italian: PREP + ART + NOUN or PREP + NOUN
    # This would manifest as: function_word + content_word pairs

    # Count how often function words are followed by content words vs other function words
    fw_then_content = 0
    fw_then_fw = 0
    content_then_fw = 0
    content_then_content = 0

    for _, _, _, tmpl in templates:
        for i in range(len(tmpl) - 1):
            a_is_fw = tmpl[i] in FUNCTION_WORDS
            b_is_fw = tmpl[i+1] in FUNCTION_WORDS
            if a_is_fw and not b_is_fw:
                fw_then_content += 1
            elif a_is_fw and b_is_fw:
                fw_then_fw += 1
            elif not a_is_fw and b_is_fw:
                content_then_fw += 1
            else:
                content_then_content += 1

    total_transitions = fw_then_content + fw_then_fw + content_then_fw + content_then_content
    print(f"\n  Transition patterns:")
    print(f"    FW -> Content:    {fw_then_content:5d} ({fw_then_content/total_transitions*100:.1f}%)")
    print(f"    FW -> FW:         {fw_then_fw:5d} ({fw_then_fw/total_transitions*100:.1f}%)")
    print(f"    Content -> FW:    {content_then_fw:5d} ({content_then_fw/total_transitions*100:.1f}%)")
    print(f"    Content -> Content: {content_then_content:5d} ({content_then_content/total_transitions*100:.1f}%)")

    # Italian prepositional structure: high FW->Content ratio (preposition + noun)
    # Latin case structure: lower FW->Content, more Content->Content
    print(f"\n  FW->Content / Content->FW ratio: {fw_then_content/content_then_fw:.2f}")
    print(f"    (>1.0 suggests head-initial / prepositional language like Italian)")
    print(f"    (<1.0 suggests head-final / case language like Latin)")

    # --------------------------------------------------------
    # STEP 8: Paragraph-level analysis
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("STEP 8: PARAGRAPH STRUCTURE ANALYSIS")
    print("=" * 80)

    para_templates = get_paragraph_templates(lines)
    print(f"\n  Total paragraphs: {len(para_templates)}")

    para_lengths = [len(pt[1]) for pt in para_templates]
    print(f"  Avg paragraph length: {sum(para_lengths)/len(para_lengths):.1f} words")
    print(f"  Min: {min(para_lengths)}, Max: {max(para_lengths)}, Median: {sorted(para_lengths)[len(para_lengths)//2]}")

    # Paragraph-initial patterns
    para_initial = Counter()
    for words, tmpl in para_templates:
        if tmpl:
            # First 3 classes of paragraph
            para_initial[tmpl[:min(3, len(tmpl))]] += 1

    print("\n  Most common paragraph-opening patterns (first 3 word classes):")
    for pattern, count in para_initial.most_common(15):
        print(f"    {count:3d}x  {' '.join(pattern)}")

    # --------------------------------------------------------
    # STEP 9: Detailed comparison - Extract actual sentence structures
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("STEP 9: SENTENCE STRUCTURE HYPOTHESIS TESTING")
    print("=" * 80)

    # Test hypothesis: Voynich lines follow Italian herbal text pattern
    # Italian herbal: "[Plant name] [preposition] [property/use]"
    # Example: "Questa erba e buona per il mal di testa"
    # Template: NOUN ADJ VERB ADJ PREP ART NOUN PREP NOUN

    # In Voynich terms, if [CH] and [SH] are noun classes, and 'or'/'ol' are prepositions:
    # [CH/SH] or/ol [CH/SH] [D] = "NOUN prep NOUN VERB" (SVO with PP)

    # Count lines matching Italian SVO + PP pattern:
    # Content FW Content (Content)
    svo_pp_count = 0
    for _, _, _, tmpl in templates:
        for i in range(len(tmpl) - 2):
            if (tmpl[i] not in FUNCTION_WORDS and
                tmpl[i+1] in FUNCTION_WORDS and
                tmpl[i+2] not in FUNCTION_WORDS):
                svo_pp_count += 1
                break

    print(f"\n  Lines with Content-FW-Content pattern (PP-like): "
          f"{svo_pp_count}/{len(templates)} ({svo_pp_count/len(templates)*100:.1f}%)")

    # Now test: does Voynich show verb-final tendency (Latin)?
    # Count lines where the last content word could be a verb
    # In Voynich, [D]-class words (daiin, dain, etc.) might be verbs
    d_final = sum(1 for _, _, _, tmpl in templates
                  if tmpl and tmpl[-1].startswith('[D'))
    print(f"  Lines ending with [D]-class (potential verb-final): "
          f"{d_final}/{len(templates)} ({d_final/len(templates)*100:.1f}%)")

    # Lines starting with [D]-class (imperative, like recipe instructions)
    d_initial = sum(1 for _, _, _, tmpl in templates
                    if tmpl and tmpl[0].startswith('[D'))
    print(f"  Lines starting with [D]-class (potential imperative): "
          f"{d_initial}/{len(templates)} ({d_initial/len(templates)*100:.1f}%)")

    # --------------------------------------------------------
    # STEP 10: Most diagnostic patterns
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("STEP 10: MOST DIAGNOSTIC STRUCTURAL FEATURES")
    print("=" * 80)

    # 1. What's the most common 2-word and 3-word "phrase"?
    print("\n  MOST COMMON WORD-CLASS SEQUENCES (potential fixed phrases):")

    # Use detailed classifier for richer patterns
    templates_detailed = extract_templates(lines, classify_word_detailed)

    bigrams_d = Counter()
    trigrams_d = Counter()
    for _, _, _, tmpl in templates_detailed:
        for i in range(len(tmpl) - 1):
            bigrams_d[(tmpl[i], tmpl[i+1])] += 1
        for i in range(len(tmpl) - 2):
            trigrams_d[(tmpl[i], tmpl[i+1], tmpl[i+2])] += 1

    print("\n  Top detailed bigrams:")
    for (a, b), count in bigrams_d.most_common(20):
        print(f"    {count:4d}x  {a} {b}")

    print("\n  Top detailed trigrams:")
    for (a, b, c), count in trigrams_d.most_common(15):
        print(f"    {count:3d}x  {a} {b} {c}")

    # --------------------------------------------------------
    # STEP 11: Currier A vs B comparison
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("STEP 11: SECTION-SPECIFIC ANALYSIS (by page range)")
    print("=" * 80)

    # Herbal pages (f1-f57) vs Astronomical (f67-f73) vs Pharmaceutical (f88-f102)
    herbal_lines = [t for t in templates if t[0] and t[0].startswith('f') and
                    any(t[0].startswith(f'f{i}') for i in range(1, 58))]
    pharma_lines = [t for t in templates if t[0] and
                    any(t[0].startswith(f'f{i}') for i in range(88, 103))]
    astro_lines = [t for t in templates if t[0] and
                   any(t[0].startswith(f'f{i}') for i in range(67, 74))]

    for section_name, section_templates in [
        ('Herbal (f1-f57)', herbal_lines),
        ('Astronomical (f67-f73)', astro_lines),
        ('Pharmaceutical (f88-f102)', pharma_lines)
    ]:
        if not section_templates:
            print(f"\n  {section_name}: No data")
            continue

        section_sig = compute_structural_signature(section_templates)
        print(f"\n  {section_name} ({len(section_templates)} lines):")
        print(f"    FW%: {section_sig['function_word_pct']:.1f}%")
        print(f"    Avg line len: {section_sig['avg_line_length']:.1f}")
        print(f"    Bigram entropy: {section_sig['bigram_entropy']:.2f}")
        print(f"    First word: {section_sig['first_word_top3']}")
        print(f"    Last word: {section_sig['last_word_top3']}")

    # --------------------------------------------------------
    # FINAL SYNTHESIS
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("SYNTHESIS: LANGUAGE/TEXT-TYPE IDENTIFICATION")
    print("=" * 80)

    print("""
    STRUCTURAL EVIDENCE SUMMARY:

    1. FUNCTION WORD RATIO: The ratio of short frequent words (or, ol, ar, al, s, y, r)
       tells us about the language's morphological type.

    2. WORD ORDER: The transition patterns (FW->Content vs Content->FW) reveal
       whether the language uses prepositions (head-initial) or postpositions/case.

    3. LINE-INITIAL PATTERNS: What begins a line/sentence reveals whether the
       language favors Subject-first, Verb-first, or Topic-first structure.

    4. LINE-FINAL PATTERNS: Verb-final patterns suggest Latin/SOV languages.

    5. CLAUSE STRUCTURE: The Content-FW-Content sequences reveal phrase structure.
    """)

    # Score each hypothesis
    scores = {}

    for lang, model in LANGUAGE_MODELS.items():
        score = 0
        fw_range = model['structural_features']['fw_ratio']
        fw_pct_range = (fw_range[0] * 100, fw_range[1] * 100)
        len_range = model['structural_features']['avg_line_len']

        # FW% match (most diagnostic)
        if fw_pct_range[0] <= voynich_fw_pct <= fw_pct_range[1]:
            score += 3
        elif abs(voynich_fw_pct - sum(fw_pct_range)/2) < 10:
            score += 1

        # Line length match
        if len_range[0] <= voynich_avg_len <= len_range[1]:
            score += 2

        # Head-initial test (FW->Content > Content->FW = prepositional)
        is_head_initial = fw_then_content > content_then_fw
        if lang in ('Italian_Herbal', 'Italian_Astrology', 'Occitan_Recipe'):
            if is_head_initial:
                score += 2
        elif lang in ('Latin_Herbal', 'Latin_Prayer'):
            if not is_head_initial:
                score += 2

        scores[lang] = score

    print("\n  HYPOTHESIS SCORES:")
    for lang, score in sorted(scores.items(), key=lambda x: -x[1]):
        model = LANGUAGE_MODELS[lang]
        print(f"    {score}/7  {lang}: {model['description']}")

    best = max(scores.items(), key=lambda x: x[1])
    print(f"\n  BEST MATCH: {best[0]} (score: {best[1]}/7)")


if __name__ == '__main__':
    main()
