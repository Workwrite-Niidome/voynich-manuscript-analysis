#!/usr/bin/env python3
"""
Discriminating tests for chol/shol semantics in the Voynich Manuscript.
Tests whether chol means "leaf", "green", "plant", "visible/above-ground".
Tests whether shol means "root", "below-ground", "hidden".
"""

import re
import sys
from collections import defaultdict, Counter
import math

INPUT_FILE = r"C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt"
OUTPUT_FILE = r"C:\Users\kazuk\Downloads\voynich_analysis\chol_discrimination_test.md"

# Known Voynich MS section classifications by illustration type ($I= field)
# H = Herbal, S = Stars/Stellar, B = Biological/Balneological,
# P = Pharmaceutical/Pharmacological, Z = Zodiac, C = Cosmological,
# A = Astronomical, T = Text-only
SECTION_NAMES = {
    'H': 'Herbal', 'S': 'Stars', 'B': 'Biological',
    'P': 'Pharmaceutical', 'Z': 'Zodiac', 'C': 'Cosmological',
    'A': 'Astronomical', 'T': 'Text-only'
}

# Known pages with prominent root illustrations vs leaf-prominent vs flower-prominent
# Based on standard Voynich codicological analysis
# These are well-established categorizations from Voynich research
# Root-prominent herbal pages (large root drawings visible)
ROOT_PROMINENT = {
    'f2r', 'f2v', 'f3r', 'f4r', 'f5r', 'f6r', 'f13r', 'f13v',
    'f14r', 'f15r', 'f16r', 'f17r', 'f22r', 'f25r', 'f25v',
    'f27r', 'f29r', 'f29v', 'f34r', 'f34v', 'f41r', 'f41v',
    'f49r', 'f49v', 'f50r', 'f50v', 'f55r', 'f55v', 'f56r', 'f56v',
    'f90r1', 'f90r2', 'f90v1', 'f90v2', 'f93r', 'f93v', 'f94r', 'f94v',
    'f95r1', 'f95r2', 'f95v1', 'f95v2', 'f96r', 'f96v',
    'f99r', 'f99v', 'f100r', 'f100v', 'f101r', 'f101v',
    'f102r1', 'f102r2', 'f102v1', 'f102v2'
}

# Leaf-prominent (large, detailed leaf structures dominate)
LEAF_PROMINENT = {
    'f1r', 'f1v', 'f4v', 'f5v', 'f6v', 'f7r', 'f7v',
    'f8r', 'f8v', 'f9r', 'f9v', 'f10r', 'f10v', 'f11r', 'f11v',
    'f14v', 'f15v', 'f16v', 'f17v', 'f18r', 'f18v', 'f19r', 'f19v',
    'f20r', 'f20v', 'f21r', 'f21v', 'f22v', 'f23r', 'f23v',
    'f24r', 'f24v', 'f26r', 'f26v', 'f27v', 'f28r', 'f28v',
    'f30r', 'f30v', 'f31r', 'f31v', 'f32r', 'f32v',
    'f33r', 'f33v', 'f34r', 'f34v', 'f35r', 'f35v',
    'f36r', 'f36v', 'f37r', 'f37v', 'f38r', 'f38v',
    'f39r', 'f39v', 'f40r', 'f40v',
    'f42r', 'f42v', 'f43r', 'f43v', 'f44r', 'f44v',
    'f45r', 'f45v', 'f46r', 'f46v', 'f47r', 'f47v',
    'f48r', 'f48v', 'f51r', 'f51v', 'f52r', 'f52v',
    'f53r', 'f53v', 'f54r', 'f54v', 'f57r', 'f57v'
}

# Flower-prominent pages (where flowers dominate over leaves)
FLOWER_PROMINENT = {
    'f3v', 'f9r', 'f22r', 'f23v', 'f26v', 'f28v',
    'f33r', 'f35v', 'f38r', 'f43r', 'f43v',
    'f52r', 'f53v', 'f56v'
}

def parse_voynich(filepath):
    """Parse EVA transcription into folios with metadata and text."""
    folios = {}
    current_folio = None
    current_section = None

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Folio header with metadata
            header_match = re.match(r'<(f\d+[rv]\d*)>\s+<!\s*(.*?)>', line)
            if header_match:
                current_folio = header_match.group(1)
                meta = header_match.group(2)
                # Extract illustration type
                i_match = re.search(r'\$I=([A-Z]+)', meta)
                section = i_match.group(1) if i_match else 'U'
                folios[current_folio] = {'section': section, 'lines': [], 'words': []}
                current_section = section
                continue

            # Text line
            line_match = re.match(r'<(f\d+[rv]\d*)\.\d+', line)
            if line_match:
                folio_id = line_match.group(1)
                if folio_id not in folios:
                    folios[folio_id] = {'section': current_section or 'U', 'lines': [], 'words': []}
                # Extract text after the marker
                text_match = re.search(r'>\s+(.*)', line)
                if text_match:
                    text = text_match.group(1)
                    folios[folio_id]['lines'].append(text)
                    # Tokenize: split on dots, spaces, dashes
                    words = re.split(r'[.\s<>]+', text)
                    words = [w for w in words if w and not w.startswith('@') and not w.startswith('{') and not w.startswith('!')]
                    folios[folio_id]['words'].extend(words)

    return folios

def count_word_in_folio(words, target):
    """Count standalone occurrences of target word in word list."""
    return sum(1 for w in words if w == target)

def count_word_contains(words, target):
    """Count words containing the target as a substring (for compound words)."""
    return sum(1 for w in words if target in w)

def chi_squared_2x2(a, b, c, d):
    """Chi-squared test for 2x2 contingency table."""
    n = a + b + c + d
    if n == 0:
        return 0, 1.0
    expected_a = (a + b) * (a + c) / n
    expected_b = (a + b) * (b + d) / n
    expected_c = (c + d) * (a + c) / n
    expected_d = (c + d) * (b + d) / n

    chi2 = 0
    for obs, exp in [(a, expected_a), (b, expected_b), (c, expected_c), (d, expected_d)]:
        if exp > 0:
            chi2 += (obs - exp) ** 2 / exp

    # Approximate p-value for 1 df
    # Using simple approximation
    if chi2 < 0.001:
        p = 1.0
    elif chi2 > 10.83:
        p = 0.001
    elif chi2 > 6.63:
        p = 0.01
    elif chi2 > 3.84:
        p = 0.05
    elif chi2 > 2.71:
        p = 0.10
    else:
        p = 0.5

    return chi2, p

def coefficient_of_variation(values):
    """Calculate coefficient of variation."""
    if not values:
        return 0
    mean = sum(values) / len(values)
    if mean == 0:
        return 0
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance) / mean

def mann_whitney_approx(group1, group2):
    """Approximate Mann-Whitney U test (normal approximation)."""
    n1, n2 = len(group1), len(group2)
    if n1 == 0 or n2 == 0:
        return 0, 1.0

    combined = [(v, 'g1') for v in group1] + [(v, 'g2') for v in group2]
    combined.sort(key=lambda x: x[0])

    # Assign ranks (handling ties)
    ranks = {}
    i = 0
    while i < len(combined):
        j = i
        while j < len(combined) and combined[j][0] == combined[i][0]:
            j += 1
        avg_rank = (i + j + 1) / 2  # 1-based
        for k in range(i, j):
            if k not in ranks:
                ranks[k] = []
            ranks[k] = avg_rank
        i = j

    r1 = sum(ranks[i] for i in range(len(combined)) if combined[i][1] == 'g1')
    u1 = r1 - n1 * (n1 + 1) / 2

    mu = n1 * n2 / 2
    sigma = math.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)

    if sigma == 0:
        return u1, 1.0

    z = (u1 - mu) / sigma
    # Approximate two-tailed p-value
    z_abs = abs(z)
    if z_abs > 3.29:
        p = 0.001
    elif z_abs > 2.58:
        p = 0.01
    elif z_abs > 1.96:
        p = 0.05
    elif z_abs > 1.64:
        p = 0.10
    else:
        p = 0.5

    return z, p

def main():
    folios = parse_voynich(INPUT_FILE)

    out = []
    out.append("# Chol/Shol Discrimination Tests")
    out.append("")
    out.append("Red-team challenge: discriminate between chol='leaf' vs 'green' vs 'plant' vs 'visible/above-ground'.")
    out.append("")
    out.append(f"**Corpus**: {len(folios)} folios parsed from EVA transcription (RF1b-e.txt)")
    out.append("")

    # Section distribution
    section_counts = Counter(f['section'] for f in folios.values())
    out.append("## Section Distribution")
    out.append("")
    out.append("| Section | Code | Folios |")
    out.append("|---------|------|--------|")
    for code in sorted(section_counts.keys()):
        name = SECTION_NAMES.get(code, 'Unknown')
        out.append(f"| {name} | {code} | {section_counts[code]} |")
    out.append("")

    # ============================================================
    # TEST 1: Green vs Leaf — Section Distribution
    # ============================================================
    out.append("---")
    out.append("## Test 1: Green vs Leaf (Section Distribution)")
    out.append("")
    out.append("**Logic**: If chol means 'green' (a color), it should appear across sections")
    out.append("(green stars, green biological pools, etc.). If it means 'leaf', it should")
    out.append("concentrate in herbal (H) and pharmaceutical (P) sections.")
    out.append("")

    # Count chol (exact and as substring) per section
    section_chol_exact = defaultdict(int)
    section_chol_contains = defaultdict(int)
    section_total_words = defaultdict(int)
    section_shol_exact = defaultdict(int)
    section_shol_contains = defaultdict(int)

    for fid, fdata in folios.items():
        sec = fdata['section']
        words = fdata['words']
        section_total_words[sec] += len(words)
        section_chol_exact[sec] += count_word_in_folio(words, 'chol')
        section_chol_contains[sec] += count_word_contains(words, 'chol')
        section_shol_exact[sec] += count_word_in_folio(words, 'shol')
        section_shol_contains[sec] += count_word_contains(words, 'shol')

    total_chol = sum(section_chol_exact.values())
    total_chol_contains = sum(section_chol_contains.values())

    out.append("### Chol distribution by section (exact match)")
    out.append("")
    out.append("| Section | Folios | chol count | Total words | chol/1000 words | % of all chol |")
    out.append("|---------|--------|-----------|-------------|-----------------|---------------|")

    herbal_pharma_chol = 0
    herbal_pharma_words = 0
    other_chol = 0
    other_words = 0

    for code in sorted(section_counts.keys()):
        name = SECTION_NAMES.get(code, 'Unknown')
        cc = section_chol_exact[code]
        tw = section_total_words[code]
        rate = (cc / tw * 1000) if tw > 0 else 0
        pct = (cc / total_chol * 100) if total_chol > 0 else 0
        out.append(f"| {name} ({code}) | {section_counts[code]} | {cc} | {tw} | {rate:.1f} | {pct:.1f}% |")

        if code in ('H', 'P'):
            herbal_pharma_chol += cc
            herbal_pharma_words += tw
        else:
            other_chol += cc
            other_words += tw

    out.append("")

    hp_pct = (herbal_pharma_chol / total_chol * 100) if total_chol > 0 else 0
    out.append(f"**Herbal+Pharmaceutical chol**: {herbal_pharma_chol}/{total_chol} = **{hp_pct:.1f}%**")
    out.append("")

    # Chi-squared: chol in H+P vs others, controlling for total words
    hp_rate = herbal_pharma_chol / herbal_pharma_words * 1000 if herbal_pharma_words > 0 else 0
    other_rate = other_chol / other_words * 1000 if other_words > 0 else 0

    chi2, p = chi_squared_2x2(
        herbal_pharma_chol, herbal_pharma_words - herbal_pharma_chol,
        other_chol, other_words - other_chol
    )

    out.append(f"**Rate in H+P**: {hp_rate:.1f}/1000 words vs **other sections**: {other_rate:.1f}/1000 words")
    out.append(f"**Chi-squared**: {chi2:.2f}, p {'<' if p < 0.05 else '>'} 0.05 (p ~ {p})")
    out.append("")

    if hp_pct > 80:
        out.append("**VERDICT**: >80% concentration in botanical sections strongly favors **'leaf'** over **'green'**.")
        out.append("A color word would appear in astronomical/zodiac sections describing green-tinted objects.")
    elif hp_pct > 60:
        out.append("**VERDICT**: 60-80% in botanical sections — moderate evidence for 'leaf', but 'plant' or 'green' cannot be excluded.")
    else:
        out.append("**VERDICT**: <60% in botanical sections — 'green' (color) remains plausible.")
    out.append("")

    # ============================================================
    # TEST 2: Leaf vs Plant — Variance across herbal folios
    # ============================================================
    out.append("---")
    out.append("## Test 2: Leaf vs Plant (Variance Across Herbal Folios)")
    out.append("")
    out.append("**Logic**: If chol means 'plant' (the whole organism), every herbal page describes")
    out.append("a plant, so chol should appear uniformly. If chol means 'leaf' specifically, it should")
    out.append("vary: HIGH on leaf-prominent pages, LOW on root-prominent pages.")
    out.append("")

    herbal_folios = {fid: fdata for fid, fdata in folios.items() if fdata['section'] == 'H'}

    # Per-folio chol rate
    folio_chol_rates = {}
    for fid, fdata in herbal_folios.items():
        words = fdata['words']
        if len(words) > 0:
            rate = count_word_contains(words, 'chol') / len(words) * 100
            folio_chol_rates[fid] = rate

    rates = list(folio_chol_rates.values())
    cv = coefficient_of_variation(rates)
    mean_rate = sum(rates) / len(rates) if rates else 0
    variance = sum((x - mean_rate) ** 2 for x in rates) / len(rates) if rates else 0

    out.append(f"**Herbal folios analyzed**: {len(herbal_folios)}")
    out.append(f"**Mean chol rate**: {mean_rate:.2f}% of words per folio")
    out.append(f"**Variance**: {variance:.4f}")
    out.append(f"**Coefficient of Variation (CV)**: {cv:.2f}")
    out.append("")
    out.append("CV interpretation: A 'plant' meaning predicts low CV (<0.5); a 'leaf' meaning predicts high CV (>0.7).")
    out.append("")

    # Compare leaf-prominent vs root-prominent herbal pages
    leaf_rates = [folio_chol_rates[fid] for fid in LEAF_PROMINENT if fid in folio_chol_rates]
    root_rates = [folio_chol_rates[fid] for fid in ROOT_PROMINENT if fid in folio_chol_rates]

    leaf_mean = sum(leaf_rates) / len(leaf_rates) if leaf_rates else 0
    root_mean = sum(root_rates) / len(root_rates) if root_rates else 0

    out.append(f"### Leaf-prominent vs Root-prominent herbal pages")
    out.append("")
    out.append(f"| Category | N folios | Mean chol% | Median |")
    out.append(f"|----------|----------|-----------|--------|")

    leaf_sorted = sorted(leaf_rates)
    root_sorted = sorted(root_rates)
    leaf_median = leaf_sorted[len(leaf_sorted)//2] if leaf_sorted else 0
    root_median = root_sorted[len(root_sorted)//2] if root_sorted else 0

    out.append(f"| Leaf-prominent | {len(leaf_rates)} | {leaf_mean:.2f}% | {leaf_median:.2f}% |")
    out.append(f"| Root-prominent | {len(root_rates)} | {root_mean:.2f}% | {root_median:.2f}% |")
    out.append("")

    if leaf_rates and root_rates:
        z, p = mann_whitney_approx(leaf_rates, root_rates)
        out.append(f"**Mann-Whitney U test (approx)**: z = {z:.2f}, p ~ {p}")

        ratio = leaf_mean / root_mean if root_mean > 0 else float('inf')
        out.append(f"**Leaf/Root ratio**: {ratio:.2f}x")
        out.append("")

        if ratio > 1.5 and p < 0.05:
            out.append("**VERDICT**: Chol frequency significantly higher on leaf-prominent pages.")
            out.append("This discriminates **'leaf'** from **'plant'** — a 'plant' word would be uniform.")
        elif ratio > 1.2:
            out.append("**VERDICT**: Weak trend toward leaf-prominent pages; inconclusive between 'leaf' and 'plant'.")
        else:
            out.append("**VERDICT**: No significant difference — consistent with 'plant' meaning.")
    out.append("")

    # ============================================================
    # TEST 3: Above-ground vs Leaf — Flower pages
    # ============================================================
    out.append("---")
    out.append("## Test 3: Above-Ground vs Leaf (Flower-Prominent Pages)")
    out.append("")
    out.append("**Logic**: If chol means 'above-ground part' (leaves+flowers+stems), it should")
    out.append("remain frequent on pages where flowers dominate but leaves are less prominent.")
    out.append("If chol means 'leaf' specifically, it should be lower on flower-dominant pages.")
    out.append("")

    flower_rates = [folio_chol_rates[fid] for fid in FLOWER_PROMINENT if fid in folio_chol_rates]
    # Non-flower leaf-prominent pages
    leaf_only = LEAF_PROMINENT - FLOWER_PROMINENT
    leaf_only_rates = [folio_chol_rates[fid] for fid in leaf_only if fid in folio_chol_rates]

    flower_mean = sum(flower_rates) / len(flower_rates) if flower_rates else 0
    leaf_only_mean = sum(leaf_only_rates) / len(leaf_only_rates) if leaf_only_rates else 0

    out.append(f"| Category | N folios | Mean chol% |")
    out.append(f"|----------|----------|-----------|")
    out.append(f"| Flower-prominent | {len(flower_rates)} | {flower_mean:.2f}% |")
    out.append(f"| Leaf-only prominent | {len(leaf_only_rates)} | {leaf_only_mean:.2f}% |")
    out.append(f"| Root-prominent | {len(root_rates)} | {root_mean:.2f}% |")
    out.append("")

    if flower_rates and leaf_only_rates:
        z_fl, p_fl = mann_whitney_approx(flower_rates, leaf_only_rates)
        out.append(f"**Flower vs Leaf-only**: z = {z_fl:.2f}, p ~ {p_fl}")

        if flower_mean < leaf_only_mean * 0.7:
            out.append("**VERDICT**: Chol drops significantly on flower pages — favors **'leaf'** over 'above-ground'.")
        elif abs(flower_mean - leaf_only_mean) / max(leaf_only_mean, 0.01) < 0.2:
            out.append("**VERDICT**: Chol similar on flower and leaf pages — consistent with 'above-ground' meaning.")
        else:
            out.append("**VERDICT**: Moderate difference; weakly favors 'leaf' over 'above-ground'.")
    out.append("")

    # ============================================================
    # TEST 4: Co-occurrence / Bigram Analysis
    # ============================================================
    out.append("---")
    out.append("## Test 4: Co-occurrence Analysis (What Appears Next to Chol?)")
    out.append("")
    out.append("**Logic**: If chol means 'leaf', expect modifiers (shape, size descriptors).")
    out.append("If chol means 'green', expect nouns following it. If 'plant', expect general descriptors.")
    out.append("")

    # Collect bigrams: word before chol, word after chol
    before_chol = Counter()
    after_chol = Counter()
    chol_bigrams = Counter()

    for fid, fdata in folios.items():
        words = fdata['words']
        for i, w in enumerate(words):
            if w == 'chol':
                if i > 0:
                    before_chol[words[i-1]] += 1
                if i < len(words) - 1:
                    after_chol[words[i+1]] += 1
                if i > 0:
                    chol_bigrams[f"{words[i-1]} chol"] += 1
                if i < len(words) - 1:
                    chol_bigrams[f"chol {words[i+1]}"] += 1

    out.append("### Most frequent words BEFORE chol (top 20)")
    out.append("")
    out.append("| Word | Count |")
    out.append("|------|-------|")
    for word, count in before_chol.most_common(20):
        out.append(f"| {word} | {count} |")
    out.append("")

    out.append("### Most frequent words AFTER chol (top 20)")
    out.append("")
    out.append("| Word | Count |")
    out.append("|------|-------|")
    for word, count in after_chol.most_common(20):
        out.append(f"| {word} | {count} |")
    out.append("")

    out.append("### Most frequent bigrams involving chol (top 20)")
    out.append("")
    out.append("| Bigram | Count |")
    out.append("|--------|-------|")
    for bigram, count in chol_bigrams.most_common(20):
        out.append(f"| {bigram} | {count} |")
    out.append("")

    # Check if the same words appear after chol vs after shol (discriminating)
    before_shol = Counter()
    after_shol = Counter()

    for fid, fdata in folios.items():
        words = fdata['words']
        for i, w in enumerate(words):
            if w == 'shol':
                if i > 0:
                    before_shol[words[i-1]] += 1
                if i < len(words) - 1:
                    after_shol[words[i+1]] += 1

    out.append("### Comparison: words after chol vs after shol")
    out.append("")
    out.append("If chol and shol are a semantic pair (leaf/root), their collocates should differ.")
    out.append("If they are both generic botanical words, collocates would overlap heavily.")
    out.append("")

    chol_after_set = set(w for w, c in after_chol.most_common(20))
    shol_after_set = set(w for w, c in after_shol.most_common(20))
    overlap = chol_after_set & shol_after_set
    jaccard = len(overlap) / len(chol_after_set | shol_after_set) if (chol_after_set | shol_after_set) else 0

    out.append(f"**Top-20 collocate overlap (Jaccard)**: {jaccard:.2f}")
    out.append(f"**Shared words**: {', '.join(sorted(overlap)) if overlap else 'none'}")
    out.append("")

    if jaccard < 0.3:
        out.append("Low overlap suggests chol and shol occupy different semantic slots (supports leaf/root pair).")
    else:
        out.append("High overlap suggests chol and shol may be variants or have similar general meanings.")
    out.append("")

    # ============================================================
    # TEST 5: Shol Discrimination
    # ============================================================
    out.append("---")
    out.append("## Test 5: Shol Discrimination (Root vs Below-Ground vs Hidden)")
    out.append("")

    # Section distribution of shol
    total_shol = sum(section_shol_exact.values())

    out.append("### Shol distribution by section")
    out.append("")
    out.append("| Section | shol count | Total words | shol/1000 words | % of all shol |")
    out.append("|---------|-----------|-------------|-----------------|---------------|")

    herbal_pharma_shol = 0
    other_shol_count = 0

    for code in sorted(section_counts.keys()):
        name = SECTION_NAMES.get(code, 'Unknown')
        sc = section_shol_exact[code]
        tw = section_total_words[code]
        rate = (sc / tw * 1000) if tw > 0 else 0
        pct = (sc / total_shol * 100) if total_shol > 0 else 0
        out.append(f"| {name} ({code}) | {sc} | {tw} | {rate:.1f} | {pct:.1f}% |")

        if code in ('H', 'P'):
            herbal_pharma_shol += sc
        else:
            other_shol_count += sc

    out.append("")

    # Shol on root-prominent vs leaf-prominent pages
    folio_shol_rates = {}
    for fid, fdata in herbal_folios.items():
        words = fdata['words']
        if len(words) > 0:
            rate = count_word_contains(words, 'shol') / len(words) * 100
            folio_shol_rates[fid] = rate

    root_shol = [folio_shol_rates[fid] for fid in ROOT_PROMINENT if fid in folio_shol_rates]
    leaf_shol = [folio_shol_rates[fid] for fid in LEAF_PROMINENT if fid in folio_shol_rates]

    root_shol_mean = sum(root_shol) / len(root_shol) if root_shol else 0
    leaf_shol_mean = sum(leaf_shol) / len(leaf_shol) if leaf_shol else 0

    out.append(f"### Shol on root-prominent vs leaf-prominent herbal pages")
    out.append("")
    out.append(f"| Category | N folios | Mean shol% |")
    out.append(f"|----------|----------|-----------|")
    out.append(f"| Root-prominent | {len(root_shol)} | {root_shol_mean:.2f}% |")
    out.append(f"| Leaf-prominent | {len(leaf_shol)} | {leaf_shol_mean:.2f}% |")
    out.append("")

    if root_shol and leaf_shol:
        z_s, p_s = mann_whitney_approx(root_shol, leaf_shol)
        out.append(f"**Mann-Whitney U test**: z = {z_s:.2f}, p ~ {p_s}")

        ratio_s = root_shol_mean / leaf_shol_mean if leaf_shol_mean > 0 else float('inf')
        out.append(f"**Root/Leaf ratio for shol**: {ratio_s:.2f}x")
        out.append("")

        if ratio_s > 1.5 and p_s < 0.05:
            out.append("**VERDICT**: Shol significantly higher on root-prominent pages — favors **'root'** meaning.")
        elif ratio_s > 1.2:
            out.append("**VERDICT**: Weak trend; inconclusive.")
        else:
            out.append("**VERDICT**: No significant difference — shol may mean something broader than 'root'.")
    out.append("")

    # ============================================================
    # TEST 6: Compound word analysis
    # ============================================================
    out.append("---")
    out.append("## Test 6: Compound Word Analysis")
    out.append("")
    out.append("Words containing 'chol' as a component (not standalone).")
    out.append("If chol is a morpheme meaning 'leaf', compounds should be interpretable")
    out.append("as leaf-related concepts.")
    out.append("")

    chol_compounds = Counter()
    shol_compounds = Counter()

    for fid, fdata in folios.items():
        for w in fdata['words']:
            if 'chol' in w and w != 'chol':
                chol_compounds[w] += 1
            if 'shol' in w and w != 'shol':
                shol_compounds[w] += 1

    out.append("### Compounds containing 'chol' (top 30)")
    out.append("")
    out.append("| Compound | Count |")
    out.append("|----------|-------|")
    for word, count in chol_compounds.most_common(30):
        out.append(f"| {word} | {count} |")
    out.append("")

    out.append("### Compounds containing 'shol' (top 30)")
    out.append("")
    out.append("| Compound | Count |")
    out.append("|----------|-------|")
    for word, count in shol_compounds.most_common(30):
        out.append(f"| {word} | {count} |")
    out.append("")

    # ============================================================
    # TEST 7: Cross-check chol vs chor/chos/chod (morphological family)
    # ============================================================
    out.append("---")
    out.append("## Test 7: Morphological Family Comparison (cho- words)")
    out.append("")
    out.append("If 'chol' = 'leaf', then 'cho-' is a stem and '-l' a suffix.")
    out.append("Compare distribution of chol vs chor, chos, chod, chok across sections.")
    out.append("")

    cho_words = ['chol', 'chor', 'chos', 'chod', 'chok', 'chom', 'chon', 'choy',
                 'cthol', 'ckhol']

    out.append("| Word | Herbal | Pharma | Astro | Bio | Stars | Zodiac | Cosmo | Text | Total |")
    out.append("|------|--------|--------|-------|-----|-------|--------|-------|------|-------|")

    for target in cho_words:
        counts = {}
        total = 0
        for code in ['H', 'P', 'A', 'B', 'S', 'Z', 'C', 'T']:
            c = 0
            for fid, fdata in folios.items():
                if fdata['section'] == code:
                    c += count_word_in_folio(fdata['words'], target)
            counts[code] = c
            total += c
        if total > 0:
            out.append(f"| {target} | {counts['H']} | {counts['P']} | {counts['A']} | {counts['B']} | {counts['S']} | {counts['Z']} | {counts['C']} | {counts['T']} | {total} |")
    out.append("")

    out.append("If chol has a uniquely herbal-skewed distribution compared to chor/chos,")
    out.append("it supports a leaf-specific meaning rather than being a generic morphological variant.")
    out.append("")

    # ============================================================
    # SUMMARY
    # ============================================================
    out.append("---")
    out.append("## Summary Scorecard")
    out.append("")
    out.append("| Test | Favors 'leaf' | Favors 'green' | Favors 'plant' | Favors 'above-ground' |")
    out.append("|------|---------------|----------------|----------------|----------------------|")

    # Test 1 scoring
    t1_leaf = "YES" if hp_pct > 80 else ("weak" if hp_pct > 60 else "no")
    t1_green = "no" if hp_pct > 70 else "possible"
    out.append(f"| 1. Section distribution ({hp_pct:.0f}% H+P) | {t1_leaf} | {t1_green} | {t1_leaf} | {t1_leaf} |")

    # Test 2 scoring
    if leaf_rates and root_rates:
        ratio = leaf_mean / root_mean if root_mean > 0 else 1
        t2_leaf = "YES" if ratio > 1.5 else ("weak" if ratio > 1.2 else "no")
        t2_plant = "no" if ratio > 1.5 else ("weak" if ratio > 1.2 else "YES")
    else:
        t2_leaf = "N/A"
        t2_plant = "N/A"
    out.append(f"| 2. Leaf vs Root page variance | {t2_leaf} | - | {t2_plant} | - |")

    # Test 3 scoring
    if flower_rates and leaf_only_rates:
        t3_above = "YES" if abs(flower_mean - leaf_only_mean) / max(leaf_only_mean, 0.01) < 0.2 else "no"
        t3_leaf = "no" if t3_above == "YES" else "YES"
    else:
        t3_above = "N/A"
        t3_leaf = "N/A"
    out.append(f"| 3. Flower-page frequency | {t3_leaf} | - | - | {t3_above} |")

    out.append(f"| 4. Co-occurrence patterns | (see analysis above) | | | |")
    out.append(f"| 5. Shol root correlation | (see analysis above) | | | |")
    out.append("")

    # Write output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))

    print(f"Results written to {OUTPUT_FILE}")
    print(f"Total chol (exact): {total_chol}")
    print(f"Total chol (contains): {total_chol_contains}")
    print(f"Total shol (exact): {total_shol}")

if __name__ == '__main__':
    main()
