#!/usr/bin/env python3
"""
PREFIX x SUFFIX Frame Decoding Analysis for the Voynich Manuscript.
"""

import re
from collections import Counter, defaultdict

EVA_FILE = r"C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt"

def classify_folio(folio):
    m = re.match(r'f(\d+)(r|v)', folio)
    if not m:
        return 'other'
    num = int(m.group(1))
    if 1 <= num <= 56:
        return 'herbal'
    elif 57 <= num <= 66:
        return 'pharma'
    elif 67 <= num <= 73:
        return 'astro'
    elif 75 <= num <= 84:
        return 'bio'
    elif 85 <= num <= 86:
        return 'cosmo'
    elif 88 <= num <= 102:
        return 'recipe'
    elif 103 <= num <= 116:
        return 'stars'
    else:
        return 'other'

PREFIXES = [
    'cth', 'ckh', 'cph', 'cfh',
    'qo', 'ch', 'sh', 'ct',
    'ot', 'ok',
    'p', 't', 'k', 's', 'y', 'd', 'o', 'f'
]

SUFFIXES = [
    'aiin', 'eedy', 'edy', 'eey', 'ain', 'iin',
    'am', 'an', 'al', 'ar', 'ol', 'or',
    'ey', 'dy', 'y',
    'n', 'l', 'r', 'm'
]

def extract_prefix(word):
    for p in PREFIXES:
        if word.startswith(p) and len(word) > len(p):
            return p
    return None

def extract_suffix(word):
    for s in SUFFIXES:
        if word.endswith(s) and len(word) > len(s):
            return s
    return None

def segment_word(word):
    prefix = extract_prefix(word)
    suffix = extract_suffix(word)
    stem_start = len(prefix) if prefix else 0
    stem_end = len(word) - len(suffix) if suffix else len(word)
    if stem_start >= stem_end:
        return prefix, '', suffix
    stem = word[stem_start:stem_end]
    return prefix, stem, suffix

def parse_eva(filepath):
    pages = []
    current_folio = None
    lines_data = []

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            folio_match = re.match(r'<(f\d+[rv]\d?)>', line)
            if folio_match:
                if current_folio and lines_data:
                    pages.append({
                        'folio': current_folio,
                        'section': classify_folio(current_folio),
                        'lines': lines_data
                    })
                current_folio = folio_match.group(1)
                lines_data = []
                continue

            line_match = re.match(r'<(f\d+[rv]\d?\.\d+)', line)
            if line_match:
                folio_from_line = re.match(r'(f\d+[rv]\d?)', line_match.group(1)).group(1)
                if current_folio is None:
                    current_folio = folio_from_line

                # Extract text after the tag
                tag_end = line.find('>') + 1
                text_part = line[tag_end:].strip()

                # Remove inline tags and special markers
                text_part = re.sub(r'<[^>]*>', ' ', text_part)
                text_part = re.sub(r'@\d+;?', '', text_part)
                text_part = re.sub(r'\{[^}]*\}', '', text_part)
                text_part = re.sub(r"[',?!]", '', text_part)

                # Words are separated by dots
                # <-> is a line-internal break, treat as space
                text_part = text_part.replace('<->', '.')

                words = [w.strip() for w in text_part.split('.') if w.strip()]
                # Also split on spaces (some entries have space-separated words)
                final_words = []
                for w in words:
                    for sub in w.split():
                        sub = sub.strip()
                        if sub and re.match(r'^[a-z]+$', sub):
                            final_words.append(sub)
                words = final_words

                if words:
                    lines_data.append(words)

    if current_folio and lines_data:
        pages.append({
            'folio': current_folio,
            'section': classify_folio(current_folio),
            'lines': lines_data
        })

    return pages

def main():
    pages = parse_eva(EVA_FILE)
    print(f"Parsed {len(pages)} pages")
    print(f"Sections: {Counter(p['section'] for p in pages)}")

    sections = ['herbal', 'pharma', 'astro', 'bio', 'cosmo', 'recipe', 'stars', 'other']

    # Collect all words with metadata
    all_words = []
    for page in pages:
        section = page['section']
        for line_idx, line_words in enumerate(page['lines']):
            for word_idx, word in enumerate(line_words):
                prefix, stem, suffix = segment_word(word)
                all_words.append({
                    'word': word,
                    'folio': page['folio'],
                    'section': section,
                    'line_pos': word_idx / max(len(line_words) - 1, 1) if len(line_words) > 1 else 0.5,
                    'is_first': word_idx == 0,
                    'is_last': word_idx == len(line_words) - 1,
                    'line_len': len(line_words),
                    'prefix': prefix,
                    'stem': stem,
                    'suffix': suffix,
                })

    print(f"Total word tokens: {len(all_words)}")
    section_totals = Counter(e['section'] for e in all_words)

    # === 1. PREFIX ANALYSIS ===
    print("\n" + "=" * 80)
    print("1. PREFIX MEANINGS BY DISTRIBUTIONAL EVIDENCE")
    print("=" * 80)

    prefix_counts = Counter(e['prefix'] for e in all_words if e['prefix'])
    prefix_section = defaultdict(Counter)
    prefix_position = defaultdict(list)
    prefix_line_start = defaultdict(int)
    prefix_line_end = defaultdict(int)
    prefix_total = defaultdict(int)

    for e in all_words:
        if e['prefix']:
            prefix_section[e['prefix']][e['section']] += 1
            prefix_position[e['prefix']].append(e['line_pos'])
            prefix_total[e['prefix']] += 1
            if e['is_first']:
                prefix_line_start[e['prefix']] += 1
            if e['is_last']:
                prefix_line_end[e['prefix']] += 1

    print(f"\n{'Prefix':>6} {'Total':>6} | " + " | ".join(f"{s:>7}" for s in sections))
    print("-" * 100)

    for p, count in prefix_counts.most_common(18):
        if count < 50:
            continue
        line_parts = []
        for s in sections:
            pct = prefix_section[p][s] / count * 100 if count > 0 else 0
            line_parts.append(f"{pct:>6.1f}%")
        print(f"{p:>6} {count:>6} | " + " | ".join(line_parts))

    print(f"\n{'Prefix':>6} {'Count':>6} {'AvgPos':>7} {'Start%':>7} {'End%':>7}")
    for p, count in prefix_counts.most_common(18):
        if count < 50:
            continue
        avg_pos = sum(prefix_position[p]) / len(prefix_position[p])
        start_pct = prefix_line_start[p] / prefix_total[p] * 100
        end_pct = prefix_line_end[p] / prefix_total[p] * 100
        print(f"{p:>6} {count:>6} {avg_pos:>7.3f} {start_pct:>6.1f}% {end_pct:>6.1f}%")

    # Section over/under representation
    print("\nPrefix section RATIO (observed/expected, >1.5 = overrepresented, <0.5 = underrepresented):")
    for p, count in prefix_counts.most_common(18):
        if count < 100:
            continue
        overrep = []
        underrep = []
        for s in sections:
            expected = section_totals[s] / len(all_words)
            observed = prefix_section[p][s] / count if count > 0 else 0
            ratio = observed / expected if expected > 0 else 0
            if ratio > 1.5:
                overrep.append(f"{s}({ratio:.1f}x)")
            elif ratio < 0.5 and section_totals[s] > 100:
                underrep.append(f"{s}({ratio:.1f}x)")
        print(f"  {p:>6}: OVER={','.join(overrep) if overrep else 'none':30s} UNDER={','.join(underrep) if underrep else 'none'}")

    # === 2. SUFFIX ANALYSIS ===
    print("\n" + "=" * 80)
    print("2. SUFFIX MEANINGS BY POSITIONAL EVIDENCE")
    print("=" * 80)

    suffix_counts = Counter(e['suffix'] for e in all_words if e['suffix'])
    suffix_section = defaultdict(Counter)
    suffix_line_start = defaultdict(int)
    suffix_line_end = defaultdict(int)
    suffix_total = defaultdict(int)

    for e in all_words:
        if e['suffix']:
            suffix_section[e['suffix']][e['section']] += 1
            suffix_total[e['suffix']] += 1
            if e['is_first']:
                suffix_line_start[e['suffix']] += 1
            if e['is_last']:
                suffix_line_end[e['suffix']] += 1

    print(f"\n{'Suffix':>6} {'Count':>6} {'Start%':>7} {'End%':>7} {'I/(I+F)':>7} {'Role':>20}")
    for s, count in suffix_counts.most_common(17):
        if count < 30:
            continue
        start_pct = suffix_line_start[s] / suffix_total[s] * 100
        end_pct = suffix_line_end[s] / suffix_total[s] * 100
        i_ratio = suffix_line_start[s] / max(suffix_line_start[s] + suffix_line_end[s], 1)

        # Determine role
        if i_ratio > 0.7:
            role = "CLAUSE OPENER"
        elif i_ratio < 0.3:
            role = "CLAUSE TERMINATOR"
        elif end_pct > start_pct * 1.3:
            role = "clause-final"
        elif start_pct > end_pct * 1.3:
            role = "clause-initial"
        else:
            role = "neutral/medial"

        print(f"{s:>6} {count:>6} {start_pct:>6.1f}% {end_pct:>6.1f}% {i_ratio:>7.3f} {role:>20}")

    # === 3. PREFIX x SUFFIX MATRIX ===
    print("\n" + "=" * 80)
    print("3. PREFIX x SUFFIX CO-OCCURRENCE MATRIX (counts)")
    print("=" * 80)

    ps_matrix = defaultdict(Counter)
    for e in all_words:
        if e['prefix'] and e['suffix']:
            ps_matrix[e['prefix']][e['suffix']] += 1

    top_p = [p for p, _ in prefix_counts.most_common(12) if prefix_counts[p] >= 100]
    top_s = [s for s, _ in suffix_counts.most_common(13) if suffix_counts[s] >= 50]

    print(f"\n{'':>6} | " + " | ".join(f"{s:>5}" for s in top_s))
    print("-" * (8 + 8 * len(top_s)))
    for p in top_p:
        cells = [f"{ps_matrix[p][s]:>5}" for s in top_s]
        print(f"{p:>6} | " + " | ".join(cells))

    # === 4. HERBAL PAGE VALIDATION ===
    print("\n" + "=" * 80)
    print("4. CONTEXTUAL VALIDATION")
    print("=" * 80)

    # 4a. First words of herbal pages
    herbal_first = []
    for page in pages:
        if page['section'] == 'herbal' and page['lines'] and page['lines'][0]:
            herbal_first.append(page['lines'][0][0])

    print(f"\nHerbal pages first-word analysis ({len(herbal_first)} pages):")
    fp = Counter(extract_prefix(w) for w in herbal_first if extract_prefix(w))
    fs = Counter(extract_suffix(w) for w in herbal_first if extract_suffix(w))
    print(f"  First-word prefixes: {fp.most_common(8)}")
    print(f"  First-word suffixes: {fs.most_common(8)}")

    # ch-...-ol in first position vs anywhere
    ch_ol_first = sum(1 for w in herbal_first if extract_prefix(w) == 'ch' and extract_suffix(w) == 'ol')
    print(f"  ch-...-ol as first word: {ch_ol_first}/{len(herbal_first)} ({ch_ol_first/max(len(herbal_first),1)*100:.1f}%)")

    # 4b. Recipe section
    recipe_lines = []
    for page in pages:
        if page['section'] == 'recipe':
            for line in page['lines']:
                recipe_lines.append(line)

    p_start = sum(1 for l in recipe_lines if l and extract_prefix(l[0]) == 'p')
    am_end = sum(1 for l in recipe_lines if l and extract_suffix(l[-1]) == 'am')
    print(f"\nRecipe lines ({len(recipe_lines)} total):")
    print(f"  p- prefix starting lines: {p_start} ({p_start/max(len(recipe_lines),1)*100:.1f}%)")
    print(f"  -am suffix ending lines: {am_end} ({am_end/max(len(recipe_lines),1)*100:.1f}%)")

    # 4c. Paragraph-initial words by section
    for sec_name in ['herbal', 'recipe', 'bio', 'stars', 'pharma']:
        firsts = []
        for page in pages:
            if page['section'] == sec_name and page['lines'] and page['lines'][0]:
                firsts.append(page['lines'][0][0])
        if not firsts:
            continue
        pf = Counter(extract_prefix(w) for w in firsts if extract_prefix(w))
        print(f"\n  {sec_name} page-initial prefixes ({len(firsts)} pages): {pf.most_common(5)}")

    # === 5. STEM CROSS-SECTION ANALYSIS ===
    print("\n" + "=" * 80)
    print("5. STEM STABILITY: SAME STEM, DIFFERENT PREFIX -> SECTION SHIFT?")
    print("=" * 80)

    stem_contexts = defaultdict(list)
    for e in all_words:
        if e['prefix'] and e['suffix'] and e['stem']:
            stem_contexts[e['stem']].append(e)

    test_stems = ['ol', 'ar', 'e', 'or']
    for ts in test_stems:
        if ts not in stem_contexts or len(stem_contexts[ts]) < 20:
            continue
        contexts = stem_contexts[ts]
        prefix_sec = defaultdict(Counter)
        for c in contexts:
            prefix_sec[c['prefix']][c['section']] += 1

        print(f"\nStem '{ts}' ({len(contexts)} tokens):")
        print(f"  {'Prefix':>6} {'Total':>6} | " + " | ".join(f"{s:>7}" for s in sections))
        for p in sorted(prefix_sec, key=lambda x: sum(prefix_sec[x].values()), reverse=True)[:8]:
            total = sum(prefix_sec[p].values())
            if total < 5:
                continue
            parts = [f"{prefix_sec[p][s]/total*100:>6.1f}%" for s in sections]
            print(f"  {p:>6} {total:>6} | " + " | ".join(parts))

    # === 6. -am TERMINATOR VALIDATION ===
    print("\n" + "=" * 80)
    print("6. -am TERMINATOR DEEP CHECK")
    print("=" * 80)

    am_words = [e for e in all_words if e['suffix'] == 'am']
    am_final = sum(1 for e in am_words if e['is_last'])
    print(f"-am total: {len(am_words)}, line-final: {am_final} ({am_final/max(len(am_words),1)*100:.1f}%)")

    am_prefixes = Counter(e['prefix'] for e in am_words if e['prefix'])
    print(f"-am prefixes: {am_prefixes.most_common(10)}")

    # What follows -am within a line?
    am_next = Counter()
    for i, e in enumerate(all_words[:-1]):
        if e['suffix'] == 'am' and not e['is_last']:
            am_next[all_words[i+1]['suffix']] += 1
    print(f"Suffix following -am (within line): {am_next.most_common(5)}")

    # === 7. -ol/-or OPENER VALIDATION ===
    print("\n" + "=" * 80)
    print("7. -ol/-or OPENER: WHAT ENDS THE PREVIOUS LINE?")
    print("=" * 80)

    for target in ['ol', 'or', 'eey']:
        target_initial = [(i, e) for i, e in enumerate(all_words) if e['suffix'] == target and e['is_first']]
        prev_suffixes = Counter()
        for i, e in target_initial:
            if i > 0 and all_words[i-1]['is_last'] and all_words[i-1]['suffix']:
                prev_suffixes[all_words[i-1]['suffix']] += 1
        print(f"\n  -{target} line-initial ({len(target_initial)} instances):")
        print(f"    Previous line ends with: {prev_suffixes.most_common(5)}")

    # === 8. qo- IN BIO/STARS: WHAT MAKES IT PEAK? ===
    print("\n" + "=" * 80)
    print("8. qo- PREFIX DEEP ANALYSIS: BIO/STARS PEAK")
    print("=" * 80)

    qo_words_by_section = defaultdict(Counter)
    for e in all_words:
        if e['prefix'] == 'qo':
            qo_words_by_section[e['section']][e['word']] += 1

    for sec in ['herbal', 'bio', 'stars']:
        if sec in qo_words_by_section:
            print(f"\n  qo- words in {sec} (top 10): {qo_words_by_section[sec].most_common(10)}")

    # qo- suffix distribution by section
    qo_suffix_sec = defaultdict(Counter)
    for e in all_words:
        if e['prefix'] == 'qo' and e['suffix']:
            qo_suffix_sec[e['section']][e['suffix']] += 1

    print(f"\n  qo- suffix distribution by section:")
    for sec in ['herbal', 'bio', 'stars', 'recipe']:
        if sec in qo_suffix_sec:
            total = sum(qo_suffix_sec[sec].values())
            top = qo_suffix_sec[sec].most_common(5)
            print(f"    {sec}: {[(s, f'{c/total*100:.0f}%') for s, c in top]}")

    # === 9. cth- HERBAL EXCLUSIVITY ===
    print("\n" + "=" * 80)
    print("9. cth- PREFIX: HERBAL EXCLUSIVITY")
    print("=" * 80)

    cth_by_section = Counter()
    cth_words = Counter()
    cth_suffixes = Counter()
    for e in all_words:
        if e['prefix'] == 'cth':
            cth_by_section[e['section']] += 1
            cth_words[e['word']] += 1
            if e['suffix']:
                cth_suffixes[e['suffix']] += 1

    print(f"  cth- section distribution: {cth_by_section.most_common()}")
    print(f"  cth- top words: {cth_words.most_common(10)}")
    print(f"  cth- suffixes: {cth_suffixes.most_common()}")

    # cth- positional data in herbal
    cth_herbal = [e for e in all_words if e['prefix'] == 'cth' and e['section'] == 'herbal']
    if cth_herbal:
        avg_pos = sum(e['line_pos'] for e in cth_herbal) / len(cth_herbal)
        first_pct = sum(1 for e in cth_herbal if e['is_first']) / len(cth_herbal) * 100
        print(f"  cth- in herbal: avg_pos={avg_pos:.3f}, first_word={first_pct:.1f}%")

if __name__ == '__main__':
    main()
