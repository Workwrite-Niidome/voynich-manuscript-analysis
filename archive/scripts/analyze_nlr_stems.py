#!/usr/bin/env python3
"""
Deep analysis of n/l/r word-final suffixes in the Voynich manuscript.
"""

import re
from collections import defaultdict, Counter

def parse_voynich(filepath):
    """Parse EVA transcription, return list of (folio, line, word) tuples."""
    words = []
    current_folio = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Detect folio markers
            folio_match = re.match(r'^<(f\d+[rv]\d*)>', line)
            if folio_match and '.' not in folio_match.group(1):
                current_folio = folio_match.group(1)
                continue

            # Parse text lines
            line_match = re.match(r'^<(f\d+[rv]\d*\.\d+)', line)
            if line_match:
                line_id = line_match.group(1)
                folio = re.match(r'(f\d+[rv]\d*)', line_id).group(1)
                current_folio = folio

                # Extract text after the header
                text_part = re.sub(r'^<[^>]+>\s*', '', line)
                # Remove comments
                text_part = re.sub(r'<[^>]*>', '', text_part)
                # Remove special markers
                text_part = re.sub(r'\{[^}]*\}', '', text_part)
                text_part = re.sub(r'@\d+;?', '', text_part)
                text_part = re.sub(r"[',?!]", '', text_part)

                # Split into words
                tokens = re.split(r'[\s.<>\-]+', text_part)
                for token in tokens:
                    token = token.strip()
                    if token and len(token) > 1:
                        words.append((current_folio, line_id, token))

    return words

def get_section(folio):
    """Classify folio into manuscript section."""
    m = re.match(r'f(\d+)', folio)
    if not m:
        return 'unknown'
    num = int(m.group(1))
    if num <= 56:
        return 'herbal_a'
    elif num <= 66:
        return 'astro'
    elif num <= 73:
        return 'herbal_b'
    elif num <= 84:
        return 'bio'
    elif num <= 86:
        return 'cosmo'
    elif num <= 102:
        return 'pharma'
    elif num <= 116:
        return 'recipe'
    else:
        return 'other'

def analyze():
    filepath = r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt'
    words_data = parse_voynich(filepath)

    print(f"Total word tokens parsed: {len(words_data)}")

    # Focus on words ending in n, l, or r
    nlr_words = []
    all_words = []
    for folio, line_id, word in words_data:
        all_words.append(word)
        if word[-1] in ('n', 'l', 'r'):
            stem = word[:-1]
            suffix = word[-1]
            if stem:  # non-empty stem
                nlr_words.append((folio, line_id, word, stem, suffix))

    print(f"Words ending in n/l/r: {len(nlr_words)}")

    # Build stem -> suffix frequency mapping
    stem_suffix = defaultdict(Counter)
    stem_words = defaultdict(list)  # store full tuples for context analysis

    for folio, line_id, word, stem, suffix in nlr_words:
        stem_suffix[stem][suffix] += 1
        stem_words[stem].append((folio, line_id, word, suffix))

    # Filter stems with 10+ total occurrences with n/l/r endings
    freq_stems = {}
    for stem, counter in stem_suffix.items():
        total = sum(counter.values())
        if total >= 10:
            freq_stems[stem] = counter

    print(f"Stems with 10+ n/l/r tokens: {len(freq_stems)}")

    # =============================================
    # 1. DEFAULT SUFFIX MAPPING
    # =============================================
    print("\n" + "="*80)
    print("1. DEFAULT SUFFIX MAPPING")
    print("="*80)

    rigid = []  # >90%
    moderate = []  # 70-90%
    flexible = []  # <70%

    stem_info = {}
    for stem, counter in sorted(freq_stems.items(), key=lambda x: -sum(x[1].values())):
        total = sum(counter.values())
        best_suffix = counter.most_common(1)[0]
        pct = best_suffix[1] / total * 100

        info = {
            'stem': stem,
            'total': total,
            'default': best_suffix[0],
            'default_count': best_suffix[1],
            'pct': pct,
            'counter': counter,
        }
        stem_info[stem] = info

        if pct > 90:
            rigid.append(info)
        elif pct >= 70:
            moderate.append(info)
        else:
            flexible.append(info)

    print(f"\nRigid (>90% preference): {len(rigid)}")
    print(f"Moderate (70-90%): {len(moderate)}")
    print(f"Flexible (<70%): {len(flexible)}")

    for label, group in [("RIGID (>90%)", rigid), ("MODERATE (70-90%)", moderate), ("FLEXIBLE (<70%)", flexible)]:
        print(f"\n--- {label} ---")
        for info in sorted(group, key=lambda x: -x['total']):
            parts = ', '.join(f"{s}={c}" for s, c in sorted(info['counter'].items()))
            print(f"  {info['stem']:20s} -> -{info['default']}  ({info['pct']:5.1f}%)  total={info['total']:4d}  [{parts}]")

    # =============================================
    # 2. SEMANTIC CLUSTERING BY DEFAULT SUFFIX
    # =============================================
    print("\n" + "="*80)
    print("2. SEMANTIC CLUSTERING BY DEFAULT SUFFIX")
    print("="*80)

    default_n = [i for i in stem_info.values() if i['default'] == 'n']
    default_l = [i for i in stem_info.values() if i['default'] == 'l']
    default_r = [i for i in stem_info.values() if i['default'] == 'r']

    for label, group in [("-n stems", default_n), ("-l stems", default_l), ("-r stems", default_r)]:
        print(f"\n{label} ({len(group)} stems):")
        for info in sorted(group, key=lambda x: -x['total']):
            print(f"  {info['stem']+'X':20s}  total={info['total']:4d}  pref={info['pct']:.1f}%  [{', '.join(f'{s}={c}' for s,c in sorted(info['counter'].items()))}]")

    # =============================================
    # 3. THE EQUALITY PARADOX
    # =============================================
    print("\n" + "="*80)
    print("3. THE EQUALITY PARADOX")
    print("="*80)

    # Global n:l:r ratio
    global_nlr = Counter()
    for _, _, _, _, suffix in nlr_words:
        global_nlr[suffix] += 1
    total_nlr = sum(global_nlr.values())
    print(f"\nGlobal n:l:r counts: n={global_nlr['n']}, l={global_nlr['l']}, r={global_nlr['r']}")
    print(f"Global n:l:r ratio:  n={global_nlr['n']/total_nlr*100:.1f}%, l={global_nlr['l']/total_nlr*100:.1f}%, r={global_nlr['r']/total_nlr*100:.1f}%")

    # Sum frequencies by default-suffix group (for stems with 10+)
    group_freq = {'n': 0, 'l': 0, 'r': 0}
    group_stem_count = {'n': 0, 'l': 0, 'r': 0}
    for info in stem_info.values():
        group_freq[info['default']] += info['total']
        group_stem_count[info['default']] += 1

    total_grp = sum(group_freq.values())
    print(f"\nTotal tokens in stems with 10+ freq, by default suffix:")
    for s in 'nlr':
        print(f"  Default-{s}: {group_stem_count[s]:3d} stems, {group_freq[s]:5d} tokens ({group_freq[s]/total_grp*100:.1f}%)")

    # Also check ALL stems (including rare ones)
    all_stem_default = {'n': 0, 'l': 0, 'r': 0}
    for stem, counter in stem_suffix.items():
        best = counter.most_common(1)[0][0]
        all_stem_default[best] += sum(counter.values())

    total_all = sum(all_stem_default.values())
    print(f"\nAll stems (including rare), by default suffix:")
    for s in 'nlr':
        print(f"  Default-{s}: {all_stem_default[s]:5d} tokens ({all_stem_default[s]/total_all*100:.1f}%)")

    # Check: how many tokens from default vs non-default
    default_tokens = 0
    nondefault_tokens = 0
    for info in stem_info.values():
        default_tokens += info['default_count']
        nondefault_tokens += info['total'] - info['default_count']
    print(f"\nAmong freq stems: {default_tokens} default tokens, {nondefault_tokens} non-default ({nondefault_tokens/(default_tokens+nondefault_tokens)*100:.1f}% switching)")

    # =============================================
    # 4. FLEXIBLE STEMS ANALYSIS
    # =============================================
    print("\n" + "="*80)
    print("4. FLEXIBLE STEMS ANALYSIS")
    print("="*80)

    # For each flexible stem, analyze by section, following word, folio
    for info in sorted(flexible, key=lambda x: -x['total']):
        stem = info['stem']
        entries = stem_words[stem]
        print(f"\n--- Stem: '{stem}' (total={info['total']}, default=-{info['default']} {info['pct']:.1f}%) ---")

        # By section
        section_suffix = defaultdict(Counter)
        for folio, line_id, word, suffix in entries:
            sec = get_section(folio)
            section_suffix[sec][suffix] += 1

        print("  By section:")
        for sec in sorted(section_suffix.keys()):
            c = section_suffix[sec]
            parts = ', '.join(f"{s}={cnt}" for s, cnt in sorted(c.items()))
            print(f"    {sec:12s}: {parts}")

        # By folio
        folio_suffix = defaultdict(Counter)
        for folio, line_id, word, suffix in entries:
            folio_suffix[folio][suffix] += 1

        # Show folios with mixed suffixes
        mixed_folios = {f: c for f, c in folio_suffix.items() if len(c) > 1}
        if mixed_folios:
            print(f"  Folios with mixed suffixes: {len(mixed_folios)}/{len(folio_suffix)}")
            for f in sorted(mixed_folios.keys()):
                c = mixed_folios[f]
                parts = ', '.join(f"{s}={cnt}" for s, cnt in sorted(c.items()))
                print(f"    {f}: {parts}")

    # Following-word analysis for flexible stems
    print("\n--- Following word patterns for flexible stems ---")
    # Build word sequence
    word_sequence = [(folio, line_id, word) for folio, line_id, word in words_data]

    for info in sorted(flexible, key=lambda x: -x['total'])[:5]:
        stem = info['stem']
        print(f"\nStem '{stem}':")
        # Find this stem's words in sequence and check next word
        next_word_by_suffix = defaultdict(list)
        for i, (folio, line_id, word) in enumerate(word_sequence):
            if word[-1] in 'nlr' and word[:-1] == stem and len(word) > 1:
                suffix = word[-1]
                if i + 1 < len(word_sequence):
                    next_w = word_sequence[i+1][2]
                    next_word_by_suffix[suffix].append(next_w)

        for suffix in sorted(next_word_by_suffix.keys()):
            nexts = next_word_by_suffix[suffix]
            # Show first-char distribution of next words
            first_chars = Counter(w[0] if w else '?' for w in nexts)
            print(f"  -{suffix} ({len(nexts)} tokens) -> next word starts with: {dict(first_chars.most_common(8))}")

    # =============================================
    # 5. KNOWN WORD VERIFICATION
    # =============================================
    print("\n" + "="*80)
    print("5. KNOWN WORD VERIFICATION")
    print("="*80)

    # Check stem "cho"
    if 'cho' in stem_suffix:
        c = stem_suffix['cho']
        total = sum(c.values())
        print(f"\nStem 'cho': total={total}, {dict(c)}")
        if total > 0:
            for s in 'nlr':
                if s in c:
                    print(f"  cho{s}: {c[s]} ({c[s]/total*100:.1f}%)")

    # Check stem "daii"
    if 'daii' in stem_suffix:
        c = stem_suffix['daii']
        total = sum(c.values())
        print(f"\nStem 'daii': total={total}, {dict(c)}")
        if total > 0:
            for s in 'nlr':
                if s in c:
                    print(f"  daii{s}: {c[s]} ({c[s]/total*100:.1f}%)")

    # Also check "dai"
    if 'dai' in stem_suffix:
        c = stem_suffix['dai']
        total = sum(c.values())
        print(f"\nStem 'dai': total={total}, {dict(c)}")
        if total > 0:
            for s in 'nlr':
                if s in c:
                    print(f"  dai{s}: {c[s]} ({c[s]/total*100:.1f}%)")

    # Check what other common stems look like
    print("\n--- Top 30 stems by frequency ---")
    all_stems_sorted = sorted(stem_suffix.items(), key=lambda x: -sum(x[1].values()))[:30]
    for stem, counter in all_stems_sorted:
        total = sum(counter.values())
        best = counter.most_common(1)[0]
        parts = ', '.join(f"{s}={c}" for s, c in sorted(counter.items()))
        print(f"  {stem:20s}  total={total:4d}  default=-{best[0]} ({best[1]/total*100:.1f}%)  [{parts}]")

    # Check grammatical pattern: do -n stems appear before specific words?
    print("\n--- Do -n words appear before different words than -l words (same stem)? ---")
    # For stems that have both -n and -l with decent counts
    for info in stem_info.values():
        c = info['counter']
        if c.get('n', 0) >= 5 and c.get('l', 0) >= 5:
            stem = info['stem']
            print(f"\nStem '{stem}' (n={c['n']}, l={c['l']}):")

            next_after_n = []
            next_after_l = []
            for i, (folio, line_id, word) in enumerate(word_sequence):
                if len(word) > 1 and word[:-1] == stem and word[-1] in ('n', 'l'):
                    if i + 1 < len(word_sequence):
                        next_w = word_sequence[i+1][2]
                        if word[-1] == 'n':
                            next_after_n.append(next_w)
                        else:
                            next_after_l.append(next_w)

            # Show most common next words
            cn = Counter(next_after_n).most_common(5)
            cl = Counter(next_after_l).most_common(5)
            print(f"  After -{stem}n: {cn}")
            print(f"  After -{stem}l: {cl}")

    return stem_info, flexible, rigid, moderate, stem_suffix, nlr_words, words_data, stem_words, global_nlr

if __name__ == '__main__':
    analyze()
