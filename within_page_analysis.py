#!/usr/bin/env python3
"""
Voynich Manuscript: Within-Page Structure Analysis
Tests whether herbal entries follow a systematic template similar to medieval herbals.
"""

import re
import sys
from collections import defaultdict, Counter
import math

INPUT_FILE = r"C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt"
OUTPUT_FILE = r"C:\Users\kazuk\Downloads\voynich_analysis\within_page_structure.md"

# Herbal section pages (Herbal A: f1-f57, Herbal B: f100-f116 approx)
# We identify them by bifolio info in the file
# $I=H means herbal illustration

def parse_transcription(filepath):
    """Parse EVA transcription into pages and lines."""
    pages = {}
    current_page = None
    current_section = None  # Track section type

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            # Page header with metadata
            page_header = re.match(r'^<(f\d+[rv])>\s+<!\s*(.*?)>', line)
            if page_header:
                current_page = page_header.group(1)
                metadata = page_header.group(2)
                pages[current_page] = {
                    'metadata': metadata,
                    'lines': [],
                    'section': 'unknown'
                }
                # Detect section type from metadata
                if '$I=H' in metadata:
                    pages[current_page]['section'] = 'herbal'
                elif '$I=P' in metadata:
                    pages[current_page]['section'] = 'pharma'
                elif '$I=B' in metadata:
                    pages[current_page]['section'] = 'biological'
                elif '$I=S' in metadata:
                    pages[current_page]['section'] = 'star'
                elif '$I=C' in metadata:
                    pages[current_page]['section'] = 'cosmo'
                elif '$I=T' in metadata:
                    pages[current_page]['section'] = 'text'
                elif '$I=Z' in metadata:
                    pages[current_page]['section'] = 'zodiac'
                continue

            # Text line
            line_match = re.match(r'^<(f\d+[rv])\.(\d+),([^>]*)>\s*(.*)', line)
            if line_match and current_page:
                page_id = line_match.group(1)
                line_num = int(line_match.group(2))
                line_type = line_match.group(3)
                text = line_match.group(4)

                if page_id in pages:
                    pages[page_id]['lines'].append({
                        'num': line_num,
                        'type': line_type,
                        'text': text
                    })

    return pages


def extract_words(text):
    """Extract EVA words from a line of text."""
    # Remove markup: {xxx}, @NNN, <->, punctuation
    text = re.sub(r'\{[^}]*\}', '', text)
    text = re.sub(r'@\d+;?', '', text)
    text = re.sub(r'<->', ' ', text)
    text = re.sub(r'[,?\'"]', '', text)
    # Split on dots and spaces
    tokens = re.split(r'[.\s]+', text)
    words = [w.strip() for w in tokens if w.strip() and len(w.strip()) > 0]
    return words


def get_word_prefix(word):
    """Get the prefix category of a word."""
    prefixes = [
        ('qo', 'qo-'),
        ('ch', 'ch-'),
        ('sh', 'sh-'),
        ('cth', 'cth-'),
        ('ckh', 'ckh-'),
        ('ot', 'ot-'),
        ('ok', 'ok-'),
        ('da', 'da-'),
        ('ol', 'ol-'),
        ('or', 'or-'),
        ('ct', 'ct-'),
        ('yk', 'yk-'),
        ('yc', 'yc-'),
        ('yd', 'yd-'),
        ('so', 'so-'),
        ('ko', 'ko-'),
        ('do', 'do-'),
        ('pc', 'pc-'),
        ('tc', 'tc-'),
        ('po', 'po-'),
        ('to', 'to-'),
    ]
    for pfx, label in prefixes:
        if word.startswith(pfx):
            return label
    return 'other'


def get_word_suffix(word):
    """Get the suffix category of a word."""
    suffixes = [
        ('aiin', '-aiin'),
        ('ain', '-ain'),
        ('iin', '-iin'),
        ('am', '-am'),
        ('ol', '-ol'),
        ('or', '-or'),
        ('ar', '-ar'),
        ('al', '-al'),
        ('an', '-an'),
        ('ey', '-ey'),
        ('dy', '-dy'),
        ('chy', '-chy'),
        ('shy', '-shy'),
        ('ty', '-ty'),
        ('ry', '-ry'),
        ('ly', '-ly'),
        ('y', '-y'),
        ('om', '-om'),
        ('os', '-os'),
        ('es', '-es'),
        ('od', '-od'),
    ]
    for sfx, label in suffixes:
        if word.endswith(sfx) and len(word) > len(sfx):
            return label
    return 'other'


def normalize_line_position(line_num, total_lines):
    """Normalize line position to a 0-1 scale, then bin."""
    if total_lines <= 1:
        return 0
    pos = (line_num - 1) / (total_lines - 1)
    # Bin into thirds: beginning, middle, end
    if pos < 0.33:
        return 'beginning'
    elif pos < 0.67:
        return 'middle'
    else:
        return 'end'


def main():
    print("Parsing transcription...")
    pages = parse_transcription(INPUT_FILE)

    # Separate herbal and other pages
    herbal_pages = {k: v for k, v in pages.items() if v['section'] == 'herbal'}
    pharma_pages = {k: v for k, v in pages.items() if v['section'] == 'pharma'}
    text_pages = {k: v for k, v in pages.items() if v['section'] == 'text'}

    print(f"Total pages: {len(pages)}")
    print(f"Herbal pages: {len(herbal_pages)}")
    print(f"Pharma pages: {len(pharma_pages)}")
    print(f"Text pages: {len(text_pages)}")

    # Count section types
    section_counts = Counter(v['section'] for v in pages.values())
    print(f"Section distribution: {dict(section_counts)}")

    # =========================================================
    # ANALYSIS 1: Line-position word frequency matrix
    # =========================================================
    print("\n=== Analysis 1: Line-position word frequency ===")

    # Collect all words with their line positions (herbal only)
    global_word_counts = Counter()
    word_at_position = defaultdict(lambda: Counter())  # position -> word -> count

    MAX_LINE = 15  # Cap line positions

    for page_id, page in herbal_pages.items():
        total_lines = len(page['lines'])
        for line_info in page['lines']:
            line_pos = min(line_info['num'], MAX_LINE)
            words = extract_words(line_info['text'])
            for w in words:
                global_word_counts[w] += 1
                word_at_position[line_pos][w] += 1

    # Find common words (50+ occurrences for herbal - adjusted from 100)
    common_words = [w for w, c in global_word_counts.most_common() if c >= 50]
    print(f"Words with 50+ occurrences: {len(common_words)}")
    print(f"Top 30: {common_words[:30]}")

    # Build heatmap data
    positions = sorted(word_at_position.keys())
    heatmap = {}
    for w in common_words[:40]:  # Top 40 words
        heatmap[w] = []
        for pos in positions:
            heatmap[w].append(word_at_position[pos].get(w, 0))

    # =========================================================
    # ANALYSIS 2: First-line uniqueness (plant name test)
    # =========================================================
    print("\n=== Analysis 2: First-line word uniqueness ===")

    first_line_words = []
    other_line_words = []
    first_line_unique = 0
    first_line_total = 0

    for page_id, page in herbal_pages.items():
        if not page['lines']:
            continue
        first_words = extract_words(page['lines'][0]['text'])
        other_words = []
        for line_info in page['lines'][1:]:
            other_words.extend(extract_words(line_info['text']))

        for w in first_words:
            first_line_total += 1
            if global_word_counts[w] <= 3:
                first_line_unique += 1

        first_line_words.extend(first_words)
        other_line_words.extend(other_words)

    first_unique_pct = first_line_unique / first_line_total * 100 if first_line_total > 0 else 0
    print(f"First line words: {first_line_total}, unique (<=3 occ): {first_line_unique} ({first_unique_pct:.1f}%)")

    # Compare with other lines
    other_unique = sum(1 for w in other_line_words if global_word_counts[w] <= 3)
    other_unique_pct = other_unique / len(other_line_words) * 100 if other_line_words else 0
    print(f"Other line words: {len(other_line_words)}, unique (<=3 occ): {other_unique} ({other_unique_pct:.1f}%)")

    # =========================================================
    # ANALYSIS 3: Prefix frequency by line position
    # =========================================================
    print("\n=== Analysis 3: Prefix frequency by line position ===")

    target_prefixes = ['ch-', 'qo-', 'sh-', 'cth-', 'ot-', 'ok-', 'da-', 'ol-',
                       'yk-', 'so-', 'ko-', 'do-', 'pc-', 'tc-', 'po-', 'to-']

    prefix_at_position = defaultdict(lambda: Counter())  # pos -> prefix -> count
    total_words_at_position = Counter()  # pos -> total words

    for page_id, page in herbal_pages.items():
        for line_info in page['lines']:
            line_pos = min(line_info['num'], MAX_LINE)
            words = extract_words(line_info['text'])
            total_words_at_position[line_pos] += len(words)
            for w in words:
                pfx = get_word_prefix(w)
                prefix_at_position[line_pos][pfx] += 1

    # Print prefix distribution
    print(f"\n{'Prefix':<8}", end='')
    for pos in positions:
        print(f"L{pos:<4}", end='')
    print()

    for pfx in target_prefixes:
        print(f"{pfx:<8}", end='')
        for pos in positions:
            total = total_words_at_position[pos]
            count = prefix_at_position[pos].get(pfx, 0)
            pct = count / total * 100 if total > 0 else 0
            print(f"{pct:5.1f}", end='')
        print()

    # =========================================================
    # ANALYSIS 4: Suffix frequency by line position
    # =========================================================
    print("\n=== Analysis 4: Suffix frequency by line position ===")

    target_suffixes = ['-aiin', '-ain', '-ol', '-or', '-ar', '-al', '-an',
                       '-ey', '-y', '-am', '-dy', '-chy', '-om']

    suffix_at_position = defaultdict(lambda: Counter())

    for page_id, page in herbal_pages.items():
        for line_info in page['lines']:
            line_pos = min(line_info['num'], MAX_LINE)
            words = extract_words(line_info['text'])
            for w in words:
                sfx = get_word_suffix(w)
                suffix_at_position[line_pos][sfx] += 1

    print(f"\n{'Suffix':<8}", end='')
    for pos in positions:
        print(f"L{pos:<4}", end='')
    print()

    for sfx in target_suffixes:
        print(f"{sfx:<8}", end='')
        for pos in positions:
            total = total_words_at_position[pos]
            count = suffix_at_position[pos].get(sfx, 0)
            pct = count / total * 100 if total > 0 else 0
            print(f"{pct:5.1f}", end='')
        print()

    # =========================================================
    # ANALYSIS 5: Compare herbal vs pharma/recipe line profiles
    # =========================================================
    print("\n=== Analysis 5: Herbal vs Pharma prefix profiles ===")

    pharma_prefix_at_pos = defaultdict(lambda: Counter())
    pharma_total_at_pos = Counter()

    for page_id, page in pharma_pages.items():
        for line_info in page['lines']:
            line_pos = min(line_info['num'], MAX_LINE)
            words = extract_words(line_info['text'])
            pharma_total_at_pos[line_pos] += len(words)
            for w in words:
                pfx = get_word_prefix(w)
                pharma_prefix_at_pos[line_pos][pfx] += 1

    # =========================================================
    # ANALYSIS 6: Cross-page consistency test
    # =========================================================
    print("\n=== Analysis 6: Cross-page consistency ===")

    # For each herbal page, compute its prefix profile vector
    page_profiles = {}

    for page_id, page in herbal_pages.items():
        if len(page['lines']) < 3:
            continue

        profile = {}
        for section_name, line_range in [('beginning', (1, 4)), ('middle', (4, 8)), ('end', (8, 20))]:
            section_words = []
            for line_info in page['lines']:
                if line_range[0] <= line_info['num'] <= line_range[1]:
                    section_words.extend(extract_words(line_info['text']))

            prefix_counts = Counter()
            for w in section_words:
                prefix_counts[get_word_prefix(w)] += 1

            total = len(section_words) if section_words else 1
            for pfx in target_prefixes:
                profile[f"{section_name}_{pfx}"] = prefix_counts.get(pfx, 0) / total

        page_profiles[page_id] = profile

    # Compute variance of profiles across pages
    if page_profiles:
        all_features = list(list(page_profiles.values())[0].keys())
        feature_values = {f: [] for f in all_features}

        for page_id, profile in page_profiles.items():
            for f in all_features:
                feature_values[f].append(profile.get(f, 0))

        print(f"\nFeature consistency (mean +/- std) across {len(page_profiles)} herbal pages:")
        consistency_data = {}
        for f in sorted(all_features):
            vals = feature_values[f]
            mean = sum(vals) / len(vals)
            variance = sum((v - mean) ** 2 for v in vals) / len(vals)
            std = math.sqrt(variance)
            cv = std / mean if mean > 0 else float('inf')
            consistency_data[f] = {'mean': mean, 'std': std, 'cv': cv}
            if mean > 0.01:
                print(f"  {f:<25}: {mean:.4f} +/- {std:.4f} (CV={cv:.2f})")

    # =========================================================
    # ANALYSIS 7: Cluster herbal entries by profile
    # =========================================================
    print("\n=== Analysis 7: Entry clustering ===")

    # Simple k-means-like clustering using prefix distribution in thirds
    # Compute distance matrix between pages
    page_ids = sorted(page_profiles.keys())

    # Use beginning ch- rate, middle qo- rate, end -am rate as clustering features
    cluster_features = ['beginning_ch-', 'beginning_qo-', 'beginning_sh-',
                       'middle_ch-', 'middle_qo-', 'middle_sh-',
                       'end_ch-', 'end_qo-', 'end_sh-']

    def page_vector(page_id):
        return [page_profiles[page_id].get(f, 0) for f in cluster_features]

    def distance(v1, v2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

    # Simple 3-cluster assignment based on dominant beginning prefix
    clusters = {'ch-dominant': [], 'qo-dominant': [], 'sh-dominant': [], 'other': []}
    for pid in page_ids:
        prof = page_profiles[pid]
        ch_rate = prof.get('beginning_ch-', 0)
        qo_rate = prof.get('beginning_qo-', 0)
        sh_rate = prof.get('beginning_sh-', 0)

        max_rate = max(ch_rate, qo_rate, sh_rate)
        if max_rate < 0.05:
            clusters['other'].append(pid)
        elif max_rate == ch_rate:
            clusters['ch-dominant'].append(pid)
        elif max_rate == qo_rate:
            clusters['qo-dominant'].append(pid)
        else:
            clusters['sh-dominant'].append(pid)

    for cname, members in clusters.items():
        print(f"  {cname}: {len(members)} pages")
        if members:
            print(f"    Examples: {members[:5]}")

    # =========================================================
    # ANALYSIS 8: Chi-squared test for position-dependence
    # =========================================================
    print("\n=== Analysis 8: Statistical significance of position dependence ===")

    # For each prefix, test if its distribution across positions is non-uniform
    for pfx in ['ch-', 'qo-', 'sh-', 'cth-', 'ot-', 'da-']:
        observed = []
        expected = []
        total_pfx = sum(prefix_at_position[pos].get(pfx, 0) for pos in positions)
        total_all = sum(total_words_at_position[pos] for pos in positions)

        if total_pfx == 0 or total_all == 0:
            continue

        overall_rate = total_pfx / total_all

        chi2 = 0
        for pos in positions:
            obs = prefix_at_position[pos].get(pfx, 0)
            exp = total_words_at_position[pos] * overall_rate
            if exp > 0:
                chi2 += (obs - exp) ** 2 / exp

        df = len(positions) - 1
        # Approximate p-value using chi2 > 2*df as rough significance
        sig = "***" if chi2 > 3 * df else ("**" if chi2 > 2 * df else ("*" if chi2 > 1.5 * df else "ns"))
        print(f"  {pfx:<8}: chi2={chi2:.1f}, df={df}, {sig}")

    # Same for suffixes
    for sfx in ['-aiin', '-ol', '-ey', '-y', '-am', '-ain']:
        total_sfx = sum(suffix_at_position[pos].get(sfx, 0) for pos in positions)
        total_all = sum(total_words_at_position[pos] for pos in positions)

        if total_sfx == 0 or total_all == 0:
            continue

        overall_rate = total_sfx / total_all

        chi2 = 0
        for pos in positions:
            obs = suffix_at_position[pos].get(sfx, 0)
            exp = total_words_at_position[pos] * overall_rate
            if exp > 0:
                chi2 += (obs - exp) ** 2 / exp

        df = len(positions) - 1
        sig = "***" if chi2 > 3 * df else ("**" if chi2 > 2 * df else ("*" if chi2 > 1.5 * df else "ns"))
        print(f"  {sfx:<8}: chi2={chi2:.1f}, df={df}, {sig}")

    # =========================================================
    # ANALYSIS 9: Detailed per-line profiles for specific pages
    # =========================================================
    print("\n=== Analysis 9: Example page profiles ===")

    example_pages = []
    for pid in sorted(herbal_pages.keys(), key=lambda x: int(re.search(r'\d+', x).group())):
        if len(herbal_pages[pid]['lines']) >= 8:
            example_pages.append(pid)
            if len(example_pages) >= 5:
                break

    for pid in example_pages:
        page = herbal_pages[pid]
        print(f"\n  Page {pid} ({len(page['lines'])} lines):")
        for line_info in page['lines']:
            words = extract_words(line_info['text'])
            prefixes = Counter(get_word_prefix(w) for w in words)
            suffixes = Counter(get_word_suffix(w) for w in words)
            top_pfx = prefixes.most_common(3)
            top_sfx = suffixes.most_common(3)
            print(f"    L{line_info['num']:2d}: {len(words):2d} words | pfx: {top_pfx} | sfx: {top_sfx}")

    # =========================================================
    # ANALYSIS 10: Transition patterns between lines
    # =========================================================
    print("\n=== Analysis 10: Prefix transition patterns ===")

    # For consecutive lines, what prefix follows what prefix?
    transition_counts = defaultdict(Counter)  # dominant_pfx_line_n -> dominant_pfx_line_n+1

    for page_id, page in herbal_pages.items():
        prev_dominant = None
        for line_info in page['lines']:
            words = extract_words(line_info['text'])
            if not words:
                continue
            prefixes = Counter(get_word_prefix(w) for w in words)
            dominant = prefixes.most_common(1)[0][0]
            if prev_dominant is not None:
                transition_counts[prev_dominant][dominant] += 1
            prev_dominant = dominant

    print("\nMost common transitions (from -> to : count):")
    for from_pfx in ['ch-', 'sh-', 'qo-', 'da-', 'ot-', 'other']:
        if from_pfx in transition_counts:
            top = transition_counts[from_pfx].most_common(3)
            print(f"  {from_pfx} -> {top}")

    # =========================================================
    # GENERATE REPORT
    # =========================================================
    print("\n\nGenerating report...")

    report = []
    report.append("# Voynich Manuscript: Within-Page Structure Analysis")
    report.append("")
    report.append("## Research Question")
    report.append("")
    report.append("Does the Voynich herbal text follow a systematic TEMPLATE analogous to medieval")
    report.append("pharmaceutical manuscripts? Standard medieval herbal entries encode:")
    report.append("1. Plant name (line 1)")
    report.append("2. Physical description (lines 2-4)")
    report.append("3. Galenic qualities (lines 4-6)")
    report.append("4. Medical uses (lines 6-8)")
    report.append("5. Preparation method (lines 8-10)")
    report.append("6. Dosage/administration (final lines)")
    report.append("")
    report.append("If the Voynich text has structured pharmaceutical content, prefix and suffix")
    report.append("frequencies should shift systematically with line position.")
    report.append("")
    report.append("---")
    report.append("")
    report.append("## Dataset Summary")
    report.append("")
    report.append(f"- **Total pages parsed**: {len(pages)}")
    report.append(f"- **Herbal pages ($I=H)**: {len(herbal_pages)}")
    report.append(f"- **Pharma pages ($I=P)**: {len(pharma_pages)}")
    report.append(f"- **Text-only pages ($I=T)**: {len(text_pages)}")
    report.append(f"- **Section distribution**: {dict(section_counts)}")
    report.append(f"- **Common words (50+ occurrences)**: {len(common_words)}")
    report.append("")

    # Lines per page distribution for herbal
    lines_per_page = [len(p['lines']) for p in herbal_pages.values()]
    avg_lines = sum(lines_per_page) / len(lines_per_page) if lines_per_page else 0
    report.append(f"- **Average lines per herbal page**: {avg_lines:.1f}")
    report.append(f"- **Range**: {min(lines_per_page)} - {max(lines_per_page)}")
    report.append("")
    report.append("---")
    report.append("")

    # =========================================================
    # Section 1: Word frequency heatmap
    # =========================================================
    report.append("## 1. Line-Position Word Frequency Heatmap")
    report.append("")
    report.append("Frequency of the 30 most common words at each line position (herbal pages only).")
    report.append("Values are raw counts.")
    report.append("")

    # Build table
    header = "| Word |" + "|".join(f" L{p} " for p in positions) + "| Total |"
    separator = "|------|" + "|".join("-----" for _ in positions) + "|-------|"
    report.append(header)
    report.append(separator)

    for w in common_words[:30]:
        total = global_word_counts[w]
        row = f"| {w} |"
        for pos in positions:
            count = word_at_position[pos].get(w, 0)
            row += f" {count} |"
        row += f" {total} |"
        report.append(row)

    report.append("")

    # Highlight patterns
    report.append("### Key Observations from Heatmap")
    report.append("")

    # For each common word, find its peak position
    for w in common_words[:15]:
        counts_by_pos = [(pos, word_at_position[pos].get(w, 0)) for pos in positions]
        peak_pos, peak_count = max(counts_by_pos, key=lambda x: x[1])
        total = global_word_counts[w]
        peak_pct = peak_count / total * 100 if total > 0 else 0
        if peak_pct > 15:  # Significant concentration
            report.append(f"- **{w}** peaks at line {peak_pos} ({peak_pct:.0f}% of occurrences)")
    report.append("")

    # =========================================================
    # Section 2: First-line uniqueness
    # =========================================================
    report.append("## 2. First-Line Word Uniqueness (Plant Name Test)")
    report.append("")
    report.append(f"- **First line**: {first_line_total} words, {first_line_unique} unique (<=3 total occurrences) = **{first_unique_pct:.1f}%**")
    report.append(f"- **Other lines**: {len(other_line_words)} words, {other_unique} unique = **{other_unique_pct:.1f}%**")
    report.append(f"- **Ratio**: First line is **{first_unique_pct/other_unique_pct:.1f}x** more likely to contain rare words" if other_unique_pct > 0 else "")
    report.append("")
    if first_unique_pct > other_unique_pct * 1.5:
        report.append("**CONFIRMED**: First lines contain significantly more rare/unique words,")
        report.append("consistent with line 1 encoding a plant name or identifier.")
    else:
        report.append("**NOT CONFIRMED**: First lines do not show significantly more rare words.")
    report.append("")

    # =========================================================
    # Section 3: Prefix shifts
    # =========================================================
    report.append("## 3. Prefix Frequency by Line Position")
    report.append("")
    report.append("Percentage of words starting with each prefix, at each line position.")
    report.append("If text has structured content, different prefixes should dominate at different positions.")
    report.append("")

    header = "| Prefix |" + "|".join(f" L{p} " for p in positions) + "|"
    separator = "|--------|" + "|".join("-----" for _ in positions) + "|"
    report.append(header)
    report.append(separator)

    prefix_patterns = {}
    for pfx in target_prefixes:
        row = f"| {pfx} |"
        values = []
        for pos in positions:
            total = total_words_at_position[pos]
            count = prefix_at_position[pos].get(pfx, 0)
            pct = count / total * 100 if total > 0 else 0
            values.append(pct)
            row += f" {pct:.1f}% |"
        report.append(row)
        prefix_patterns[pfx] = values

    report.append("")

    # Analyze prefix shifts
    report.append("### Prefix Shift Analysis")
    report.append("")

    for pfx in ['ch-', 'qo-', 'sh-', 'cth-', 'ot-', 'da-']:
        vals = prefix_patterns.get(pfx, [])
        if not vals:
            continue
        peak_idx = vals.index(max(vals))
        trough_idx = vals.index(min(vals))
        peak_pos = positions[peak_idx]
        trough_pos = positions[trough_idx]
        peak_val = max(vals)
        trough_val = min(vals)
        shift_ratio = peak_val / trough_val if trough_val > 0 else float('inf')

        report.append(f"- **{pfx}**: Peak at L{peak_pos} ({peak_val:.1f}%), trough at L{trough_pos} ({trough_val:.1f}%), shift ratio = {shift_ratio:.1f}x")

    report.append("")

    # =========================================================
    # Section 4: Suffix shifts
    # =========================================================
    report.append("## 4. Suffix Frequency by Line Position")
    report.append("")

    header = "| Suffix |" + "|".join(f" L{p} " for p in positions) + "|"
    separator = "|--------|" + "|".join("-----" for _ in positions) + "|"
    report.append(header)
    report.append(separator)

    suffix_patterns = {}
    for sfx in target_suffixes:
        row = f"| {sfx} |"
        values = []
        for pos in positions:
            total = total_words_at_position[pos]
            count = suffix_at_position[pos].get(sfx, 0)
            pct = count / total * 100 if total > 0 else 0
            values.append(pct)
            row += f" {pct:.1f}% |"
        report.append(row)
        suffix_patterns[sfx] = values

    report.append("")

    report.append("### Suffix Shift Analysis")
    report.append("")

    for sfx in ['-aiin', '-ol', '-ey', '-y', '-am', '-ain', '-ar']:
        vals = suffix_patterns.get(sfx, [])
        if not vals:
            continue
        peak_idx = vals.index(max(vals))
        trough_idx = vals.index(min(vals))
        peak_pos = positions[peak_idx]
        trough_pos = positions[trough_idx]
        peak_val = max(vals)
        trough_val = min(vals)
        shift_ratio = peak_val / trough_val if trough_val > 0 else float('inf')

        report.append(f"- **{sfx}**: Peak at L{peak_pos} ({peak_val:.1f}%), trough at L{trough_pos} ({trough_val:.1f}%), shift ratio = {shift_ratio:.1f}x")

    report.append("")

    # =========================================================
    # Section 5: Herbal vs Pharma comparison
    # =========================================================
    report.append("## 5. Herbal vs Pharma Section Comparison")
    report.append("")

    if pharma_pages:
        report.append("Comparing prefix profiles between herbal and pharmaceutical sections.")
        report.append("If sections encode different content types, their profiles should differ.")
        report.append("")

        pharma_positions = sorted(pharma_total_at_pos.keys())
        compare_prefixes = ['ch-', 'qo-', 'sh-', 'da-', 'ot-']

        report.append("### Overall prefix rates (all positions combined)")
        report.append("")
        report.append("| Prefix | Herbal | Pharma | Difference |")
        report.append("|--------|--------|--------|------------|")

        for pfx in compare_prefixes:
            h_total = sum(prefix_at_position[pos].get(pfx, 0) for pos in positions)
            h_all = sum(total_words_at_position[pos] for pos in positions)
            h_rate = h_total / h_all * 100 if h_all > 0 else 0

            p_total = sum(pharma_prefix_at_pos[pos].get(pfx, 0) for pos in pharma_positions)
            p_all = sum(pharma_total_at_pos[pos] for pos in pharma_positions)
            p_rate = p_total / p_all * 100 if p_all > 0 else 0

            diff = p_rate - h_rate
            report.append(f"| {pfx} | {h_rate:.1f}% | {p_rate:.1f}% | {diff:+.1f}% |")

        report.append("")
    else:
        report.append("No pharma pages found with $I=P tag in this transcription file.")
        report.append("")

    # =========================================================
    # Section 6: Cross-page consistency
    # =========================================================
    report.append("## 6. Cross-Page Consistency (Template Test)")
    report.append("")
    report.append("If entries follow a template, the prefix distribution at each position should be")
    report.append("**consistent across pages** (low coefficient of variation).")
    report.append("")
    report.append(f"Analyzed {len(page_profiles)} herbal pages with 3+ lines.")
    report.append("")

    if consistency_data:
        report.append("| Feature | Mean | Std | CV (lower=more consistent) |")
        report.append("|---------|------|-----|---------------------------|")

        low_cv_features = []
        for f in sorted(consistency_data.keys()):
            d = consistency_data[f]
            if d['mean'] > 0.01:
                report.append(f"| {f} | {d['mean']:.4f} | {d['std']:.4f} | {d['cv']:.2f} |")
                if d['cv'] < 1.0:
                    low_cv_features.append((f, d['cv']))

        report.append("")

        if low_cv_features:
            report.append("### Features with CV < 1.0 (consistent across pages)")
            report.append("")
            for f, cv in sorted(low_cv_features, key=lambda x: x[1]):
                report.append(f"- **{f}**: CV = {cv:.2f}")
            report.append("")

    # =========================================================
    # Section 7: Clustering
    # =========================================================
    report.append("## 7. Entry Clustering by Line-Position Profile")
    report.append("")
    report.append("Pages clustered by dominant prefix in the beginning section (lines 1-3).")
    report.append("")

    for cname, members in clusters.items():
        report.append(f"### {cname}: {len(members)} pages")
        if members:
            report.append(f"Pages: {', '.join(members[:20])}")
            if len(members) > 20:
                report.append(f"... and {len(members) - 20} more")

            # Average profile for this cluster
            if members:
                avg_profile = {}
                for f in cluster_features:
                    vals = [page_profiles[pid].get(f, 0) for pid in members if pid in page_profiles]
                    avg_profile[f] = sum(vals) / len(vals) if vals else 0

                report.append("")
                report.append("Average profile:")
                for f in cluster_features:
                    report.append(f"  - {f}: {avg_profile[f]:.3f}")
        report.append("")

    # =========================================================
    # Section 8: Statistical significance
    # =========================================================
    report.append("## 8. Statistical Significance of Position-Dependence")
    report.append("")
    report.append("Chi-squared test: Is each prefix/suffix distributed non-uniformly across line positions?")
    report.append("(*** = highly significant, ** = significant, * = marginal, ns = not significant)")
    report.append("")
    report.append("| Morpheme | Chi-sq | df | Significance |")
    report.append("|----------|--------|----|-------------|")

    for morph_type, morph_list, at_pos in [
        ('prefix', ['ch-', 'qo-', 'sh-', 'cth-', 'ot-', 'da-'], prefix_at_position),
        ('suffix', ['-aiin', '-ol', '-ey', '-y', '-am', '-ain'], suffix_at_position)
    ]:
        for m in morph_list:
            total_m = sum(at_pos[pos].get(m, 0) for pos in positions)
            total_all = sum(total_words_at_position[pos] for pos in positions)
            if total_m == 0 or total_all == 0:
                continue
            overall_rate = total_m / total_all
            chi2 = 0
            for pos in positions:
                obs = at_pos[pos].get(m, 0)
                exp = total_words_at_position[pos] * overall_rate
                if exp > 0:
                    chi2 += (obs - exp) ** 2 / exp
            df = len(positions) - 1
            sig = "***" if chi2 > 3 * df else ("**" if chi2 > 2 * df else ("*" if chi2 > 1.5 * df else "ns"))
            report.append(f"| {m} | {chi2:.1f} | {df} | {sig} |")

    report.append("")

    # =========================================================
    # Section 9: Transition patterns
    # =========================================================
    report.append("## 9. Line-to-Line Prefix Transitions")
    report.append("")
    report.append("What dominant prefix typically follows another? Consistent transitions")
    report.append("would indicate a template-driven sequence.")
    report.append("")
    report.append("| From | Most likely next (count) |")
    report.append("|------|-------------------------|")

    for from_pfx in ['ch-', 'sh-', 'qo-', 'da-', 'ot-', 'ok-', 'other']:
        if from_pfx in transition_counts:
            top = transition_counts[from_pfx].most_common(3)
            top_str = ", ".join(f"{t[0]} ({t[1]})" for t in top)
            report.append(f"| {from_pfx} | {top_str} |")

    report.append("")

    # =========================================================
    # Section 10: Overall verdict
    # =========================================================
    report.append("## 10. Overall Verdict: Does the Text Follow a Template?")
    report.append("")

    # Compute evidence scores
    evidence_for = []
    evidence_against = []

    # Test 1: First-line uniqueness
    if first_unique_pct > other_unique_pct * 1.5:
        evidence_for.append(f"First-line uniqueness: {first_unique_pct:.0f}% vs {other_unique_pct:.0f}% (plant names)")
    else:
        evidence_against.append(f"No first-line uniqueness signal ({first_unique_pct:.0f}% vs {other_unique_pct:.0f}%)")

    # Test 2: Prefix position-dependence
    sig_prefixes = 0
    for pfx in ['ch-', 'qo-', 'sh-', 'cth-', 'ot-', 'da-']:
        vals = prefix_patterns.get(pfx, [])
        if vals:
            shift = max(vals) / min(vals) if min(vals) > 0 else float('inf')
            if shift > 1.5:
                sig_prefixes += 1

    if sig_prefixes >= 3:
        evidence_for.append(f"{sig_prefixes}/6 prefixes show significant position-dependent shifts")
    else:
        evidence_against.append(f"Only {sig_prefixes}/6 prefixes show position-dependent shifts")

    # Test 3: Suffix position-dependence
    sig_suffixes = 0
    for sfx in ['-aiin', '-ol', '-ey', '-y', '-am', '-ain']:
        vals = suffix_patterns.get(sfx, [])
        if vals:
            shift = max(vals) / min(vals) if min(vals) > 0 else float('inf')
            if shift > 1.5:
                sig_suffixes += 1

    if sig_suffixes >= 3:
        evidence_for.append(f"{sig_suffixes}/6 suffixes show significant position-dependent shifts")
    else:
        evidence_against.append(f"Only {sig_suffixes}/6 suffixes show position-dependent shifts")

    # Test 4: Cross-page consistency
    consistent_features = sum(1 for f, cv in low_cv_features) if low_cv_features else 0
    total_features = len([d for d in consistency_data.values() if d['mean'] > 0.01])

    if consistent_features > total_features * 0.5:
        evidence_for.append(f"{consistent_features}/{total_features} features are consistent across pages (CV<1.0)")
    else:
        evidence_against.append(f"Only {consistent_features}/{total_features} features are consistent across pages")

    report.append("### Evidence FOR a template structure:")
    report.append("")
    for e in evidence_for:
        report.append(f"1. {e}")
    report.append("")

    report.append("### Evidence AGAINST a template structure:")
    report.append("")
    for e in evidence_against:
        report.append(f"1. {e}")
    report.append("")

    # Final assessment
    score = len(evidence_for) - len(evidence_against)
    if score >= 2:
        verdict = "STRONG EVIDENCE FOR TEMPLATE"
        desc = ("The Voynich herbal text shows clear signs of a systematic template structure. "
                "Prefix and suffix distributions shift with line position in a pattern consistent "
                "with medieval pharmaceutical entries. The text encodes STRUCTURED CONTENT that "
                "changes throughout each entry, strongly suggesting real pharmaceutical information.")
    elif score >= 0:
        verdict = "MODERATE EVIDENCE FOR TEMPLATE"
        desc = ("Some features of the text are consistent with a template structure, but the "
                "evidence is mixed. The shifts in morpheme frequencies may reflect a loose "
                "organizational pattern rather than a rigid template.")
    else:
        verdict = "WEAK/NO EVIDENCE FOR TEMPLATE"
        desc = ("The Voynich text does not show strong evidence of a systematic template. "
                "Morpheme distributions are relatively uniform across line positions, "
                "inconsistent with a structured pharmaceutical format.")

    report.append(f"### VERDICT: {verdict}")
    report.append("")
    report.append(desc)
    report.append("")

    # Specific template mapping attempt
    report.append("### Tentative Template Mapping (if template exists)")
    report.append("")
    report.append("Based on which morphemes peak at which positions:")
    report.append("")

    # Find peak positions for key prefixes
    template_map = {}
    for pfx in ['ch-', 'qo-', 'sh-', 'cth-', 'ot-', 'da-']:
        vals = prefix_patterns.get(pfx, [])
        if vals:
            peak_idx = vals.index(max(vals))
            template_map[pfx] = positions[peak_idx]

    for pfx, peak in sorted(template_map.items(), key=lambda x: x[1]):
        report.append(f"- **Line {peak}**: {pfx} prefix peaks (possible function: ?)")

    report.append("")
    report.append("---")
    report.append("")
    report.append("*Analysis based on EVA transcription (RF1b-e.txt). Herbal pages identified by $I=H metadata tag.*")

    # Write report
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

    print(f"\nReport written to {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
