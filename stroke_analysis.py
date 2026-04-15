import re
import math
from collections import Counter, defaultdict

# ============================================================
# EVA Glyph Stroke Decomposition Analysis
# ============================================================

with open("C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

def extract_words(lines):
    words = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"<[^>]+>\s*(.*)", line)
        if m:
            text = m.group(1)
        else:
            continue
        text = re.sub(r"<[^>]*>", "", text)
        text = re.sub(r"@\d+;?", "", text)
        text = re.sub(r"\{[^}]*\}", "", text)
        text = re.sub(r"[,?\*!\'\-]", "", text)
        # Words are separated by dots in EVA transcription
        for w in re.split(r"[\.\s]+", text):
            w = w.strip()
            if w and len(w) > 0 and re.match(r"^[a-zA-Z]+$", w):
                words.append(w)
    return words

all_words = extract_words(lines)
print(f"Total words extracted: {len(all_words)}")
print(f"Unique words: {len(set(all_words))}")

# EVA glyph definitions
EVA_GLYPHS = {
    "ch":  {"components": ["BENCH"], "type": "bench"},
    "sh":  {"components": ["BENCH_alt"], "type": "bench"},
    "ckh": {"components": ["BENCH", "GALLOWS_k"], "type": "gallows_bench"},
    "cth": {"components": ["BENCH", "GALLOWS_t"], "type": "gallows_bench"},
    "cph": {"components": ["BENCH", "GALLOWS_p"], "type": "gallows_bench"},
    "cfh": {"components": ["BENCH", "GALLOWS_f"], "type": "gallows_bench"},
    "k":   {"components": ["GALLOWS_k"], "type": "gallows"},
    "t":   {"components": ["GALLOWS_t"], "type": "gallows"},
    "p":   {"components": ["GALLOWS_p"], "type": "gallows"},
    "f":   {"components": ["GALLOWS_f"], "type": "gallows"},
    "o":   {"components": ["LOOP_o"], "type": "loop"},
    "a":   {"components": ["LOOP_a"], "type": "loop"},
    "e":   {"components": ["LOOP_e"], "type": "loop"},
    "i":   {"components": ["PLUME_i"], "type": "plume"},
    "n":   {"components": ["TAIL_n"], "type": "tail"},
    "r":   {"components": ["TAIL_r"], "type": "tail"},
    "l":   {"components": ["TAIL_l"], "type": "tail"},
    "m":   {"components": ["TAIL_m"], "type": "tail"},
    "s":   {"components": ["TAIL_s"], "type": "tail"},
    "d":   {"components": ["TAIL_d"], "type": "tail"},
    "g":   {"components": ["TAIL_g"], "type": "tail"},
    "y":   {"components": ["FINAL_y"], "type": "final"},
    "q":   {"components": ["INITIAL_q"], "type": "initial"},
}

def tokenize_word(word):
    glyphs = []
    i = 0
    while i < len(word):
        matched = False
        for length in [3, 2, 1]:
            if i + length <= len(word):
                chunk = word[i:i+length]
                if chunk in EVA_GLYPHS:
                    glyphs.append(chunk)
                    i += length
                    matched = True
                    break
        if not matched:
            glyphs.append(word[i])
            i += 1
    return glyphs

def decompose_to_components(word):
    glyphs = tokenize_word(word)
    components = []
    for g in glyphs:
        if g in EVA_GLYPHS:
            components.extend(EVA_GLYPHS[g]["components"])
        else:
            components.append(f"UNKNOWN_{g}")
    return components

def get_type_sequence(word):
    glyphs = tokenize_word(word)
    return [EVA_GLYPHS.get(g, {}).get("type", "unknown") for g in glyphs]

def entropy(counter):
    total = sum(counter.values())
    if total == 0:
        return 0
    h = 0
    for c in counter.values():
        p = c / total
        if p > 0:
            h -= p * math.log2(p)
    return h

def classify_role(glyph):
    if glyph == "q":
        return "INITIAL"
    if glyph == "y":
        return "FINAL"
    if glyph in ("k", "t", "p", "f", "ch", "sh", "ckh", "cth", "cph", "cfh"):
        return "ONSET"
    if glyph in ("o", "a", "e", "i"):
        return "NUCLEUS"
    if glyph in ("n", "r", "l", "m", "s", "d", "g"):
        return "CODA"
    return "UNKNOWN"

# ============================================================
# 1. GLYPH TOKENIZATION
# ============================================================
print("\n" + "="*60)
print("1. EVA GLYPH TOKENIZATION")
print("="*60)

all_glyph_sequences = [tokenize_word(w) for w in all_words]
all_glyphs_flat = [g for seq in all_glyph_sequences for g in seq]
glyph_counts = Counter(all_glyphs_flat)

print(f"\nTotal glyph tokens: {len(all_glyphs_flat)}")
print(f"Unique glyphs: {len(glyph_counts)}")
print("\nTop 30 glyphs by frequency:")
for g, c in glyph_counts.most_common(30):
    gtype = EVA_GLYPHS.get(g, {}).get("type", "unknown")
    print(f"  {g:5s} ({gtype:15s}): {c:6d}  ({100*c/len(all_glyphs_flat):.2f}%)")

# ============================================================
# 2. COMPONENT FREQUENCY
# ============================================================
print("\n" + "="*60)
print("2. STROKE COMPONENT FREQUENCIES")
print("="*60)

all_components = [decompose_to_components(w) for w in all_words]
all_components_flat = [c for comps in all_components for c in comps]
component_counts = Counter(all_components_flat)

print(f"\nTotal stroke components: {len(all_components_flat)}")
print(f"Unique components: {len(component_counts)}")
print("\nComponent frequencies:")
for comp, cnt in component_counts.most_common():
    print(f"  {comp:20s}: {cnt:6d}  ({100*cnt/len(all_components_flat):.2f}%)")

# ============================================================
# 3. ENTROPY ANALYSIS
# ============================================================
print("\n" + "="*60)
print("3. ENTROPY: PER-CHARACTER vs PER-GLYPH vs PER-STROKE")
print("="*60)

char_counts = Counter()
for w in all_words:
    for c in w:
        char_counts[c] += 1

char_entropy = entropy(char_counts)
glyph_entropy = entropy(glyph_counts)
comp_entropy = entropy(component_counts)
avg_strokes = len(all_components_flat) / len(all_glyphs_flat)

print(f"\nRaw EVA character entropy:  {char_entropy:.4f} bits/char")
print(f"EVA glyph entropy:          {glyph_entropy:.4f} bits/glyph")
print(f"Stroke component entropy:   {comp_entropy:.4f} bits/component")
print(f"\nAvg components per glyph:   {avg_strokes:.3f}")
print(f"\nIf strokes independent, predicted glyph entropy:")
print(f"  avg_strokes * stroke_entropy = {avg_strokes:.3f} * {comp_entropy:.4f} = {avg_strokes * comp_entropy:.4f}")
print(f"  Actual glyph entropy:        {glyph_entropy:.4f}")
print(f"  Ratio (actual/predicted):    {glyph_entropy / (avg_strokes * comp_entropy):.4f}")

# ============================================================
# 4. MUTUAL INFORMATION
# ============================================================
print("\n" + "="*60)
print("4. MUTUAL INFORMATION BETWEEN ADJACENT COMPONENTS")
print("="*60)

comp_bigrams = Counter()
for comps in all_components:
    for i in range(len(comps) - 1):
        comp_bigrams[(comps[i], comps[i+1])] += 1

total_bigrams = sum(comp_bigrams.values())
total_unigrams = sum(component_counts.values())

mi_comp = 0
for (c1, c2), count in comp_bigrams.items():
    p_joint = count / total_bigrams
    p_c1 = component_counts[c1] / total_unigrams
    p_c2 = component_counts[c2] / total_unigrams
    if p_joint > 0 and p_c1 > 0 and p_c2 > 0:
        mi_comp += p_joint * math.log2(p_joint / (p_c1 * p_c2))

# MI for adjacent glyphs
glyph_bigrams = Counter()
for seq in all_glyph_sequences:
    for i in range(len(seq) - 1):
        glyph_bigrams[(seq[i], seq[i+1])] += 1

total_gb = sum(glyph_bigrams.values())
total_gu = sum(glyph_counts.values())

mi_glyph = 0
for (g1, g2), count in glyph_bigrams.items():
    p_joint = count / total_gb
    p_g1 = glyph_counts[g1] / total_gu
    p_g2 = glyph_counts[g2] / total_gu
    if p_joint > 0 and p_g1 > 0 and p_g2 > 0:
        mi_glyph += p_joint * math.log2(p_joint / (p_g1 * p_g2))

print(f"\nMI between adjacent components: {mi_comp:.4f} bits")
print(f"MI between adjacent glyphs:     {mi_glyph:.4f} bits")
print(f"\n  MI ~0 => components are independent (Hangul-like)")
print(f"  MI >> 0 => components are correlated (atomic glyphs)")

# Top correlated component pairs
print("\nTop 20 most correlated component bigrams (by PMI):")
pmi_list = []
for (c1, c2), count in comp_bigrams.items():
    if count < 10:
        continue
    p_joint = count / total_bigrams
    p_c1 = component_counts[c1] / total_unigrams
    p_c2 = component_counts[c2] / total_unigrams
    pmi = math.log2(p_joint / (p_c1 * p_c2))
    pmi_list.append((c1, c2, pmi, count))

pmi_list.sort(key=lambda x: -x[2])
for c1, c2, pmi, cnt in pmi_list[:20]:
    print(f"  {c1:20s} -> {c2:20s}  PMI={pmi:+.4f}  count={cnt}")

# ============================================================
# 5. POSITIONAL SLOT ANALYSIS (Hangul test)
# ============================================================
print("\n" + "="*60)
print("5. HANGUL ANALOGY: POSITIONAL SLOT ANALYSIS")
print("="*60)

type_sequences = [tuple(get_type_sequence(w)) for w in all_words]
type_seq_counts = Counter(type_sequences)

print("\nTop 30 word type-patterns:")
for seq, cnt in type_seq_counts.most_common(30):
    examples = [w for w, ts in zip(all_words, type_sequences) if ts == seq][:3]
    print(f"  {str(seq):65s}  n={cnt:5d}  ex: {', '.join(examples)}")

# Position-type distribution
max_pos = 12
pos_type_dist = defaultdict(Counter)
for types in [get_type_sequence(w) for w in all_words]:
    for i, t in enumerate(types):
        if i < max_pos:
            pos_type_dist[i][t] += 1

all_types = sorted(set(t for c in pos_type_dist.values() for t in c.keys()))
print(f"\nGlyph type distribution by position:")
print(f"{'Pos':>4s}", end="")
for t in all_types:
    print(f"  {t:>12s}", end="")
print(f"  {'Total':>7s}  {'H':>6s}")

for pos in range(max_pos):
    total = sum(pos_type_dist[pos].values())
    if total < 10:
        continue
    print(f"{pos:4d}", end="")
    for t in all_types:
        cnt = pos_type_dist[pos].get(t, 0)
        pct = 100 * cnt / total if total > 0 else 0
        print(f"  {pct:11.1f}%", end="")
    h = entropy(pos_type_dist[pos])
    print(f"  {total:7d}  {h:6.4f}")

# ============================================================
# 6. BENCH COMPONENT SEMANTIC ANALYSIS
# ============================================================
print("\n" + "="*60)
print("6. BENCH COMPONENT: DISTRIBUTION & SUBSTITUTABILITY")
print("="*60)

bench_glyphs = {"ch", "sh", "ckh", "cth", "cph", "cfh"}
bench_pos_dist = defaultdict(Counter)
bench_examples = defaultdict(list)

for w in all_words:
    glyphs = tokenize_word(w)
    for i, g in enumerate(glyphs):
        if g in bench_glyphs:
            rel_pos = round(i / max(len(glyphs) - 1, 1), 1)
            bench_pos_dist[g][rel_pos] += 1
            if len(bench_examples[g]) < 5:
                bench_examples[g].append(w)

print("\nBench glyph positional distributions:")
for bg in sorted(bench_glyphs):
    total = sum(bench_pos_dist[bg].values())
    if total == 0:
        continue
    positions = sorted(bench_pos_dist[bg].keys())
    dist_str = ", ".join([f"{p:.1f}:{bench_pos_dist[bg][p]}" for p in positions])
    exs = bench_examples.get(bg, [])
    print(f"  {bg:5s} (n={total:5d}): [{dist_str}]")
    print(f"         ex: {', '.join(exs[:3])}")

# Substitution test
word_set = set(all_words)
sub_pairs = set()
for w in all_words:
    glyphs = tokenize_word(w)
    for i, g in enumerate(glyphs):
        if g in bench_glyphs:
            for rep in bench_glyphs:
                if rep != g:
                    new_w = "".join(glyphs[:i] + [rep] + glyphs[i+1:])
                    if new_w in word_set:
                        sub_pairs.add(tuple(sorted([w, new_w])))

print(f"\nBench substitution minimal pairs: {len(sub_pairs)}")
for p in sorted(sub_pairs)[:25]:
    print(f"    {p[0]:20s} <-> {p[1]:20s}")

# ============================================================
# 7. GALLOWS ANALYSIS
# ============================================================
print("\n" + "="*60)
print("7. GALLOWS POSITION DISTRIBUTION")
print("="*60)

gallows_all = {"k", "t", "p", "f", "ckh", "cth", "cph", "cfh"}
gallows_pos = defaultdict(Counter)

for w in all_words:
    glyphs = tokenize_word(w)
    for i, g in enumerate(glyphs):
        if g in gallows_all:
            pos = "initial" if i == 0 else ("final" if i == len(glyphs)-1 else "medial")
            gallows_pos[g][pos] += 1

print("\nGallows position (initial/medial/final):")
for g in sorted(gallows_pos.keys()):
    total = sum(gallows_pos[g].values())
    dist = {pos: f"{100*cnt/total:.1f}%" for pos, cnt in gallows_pos[g].items()}
    print(f"  {g:5s} (n={total:5d}): {dist}")

# ============================================================
# 8. WORD STRUCTURE TEMPLATES
# ============================================================
print("\n" + "="*60)
print("8. WORD STRUCTURE TEMPLATES")
print("="*60)

def fits_single_syllable(roles):
    i = 0
    if i < len(roles) and roles[i] == "INITIAL":
        i += 1
    while i < len(roles) and roles[i] == "ONSET":
        i += 1
    nc = 0
    while i < len(roles) and roles[i] == "NUCLEUS":
        i += 1
        nc += 1
    if nc == 0:
        return False
    while i < len(roles) and roles[i] == "CODA":
        i += 1
    if i < len(roles) and roles[i] == "FINAL":
        i += 1
    return i == len(roles)

def fits_multi_syllable(roles):
    i = 0
    syl = 0
    if i < len(roles) and roles[i] in ("INITIAL", "FINAL"):
        i += 1
    while i < len(roles):
        while i < len(roles) and roles[i] == "ONSET":
            i += 1
        nc = 0
        while i < len(roles) and roles[i] == "NUCLEUS":
            i += 1
            nc += 1
        if nc == 0:
            if i < len(roles) and roles[i] == "FINAL":
                i += 1
            break
        syl += 1
        while i < len(roles) and roles[i] == "CODA":
            i += 1
        if i < len(roles) and roles[i] == "FINAL":
            if i + 1 < len(roles) and roles[i+1] in ("ONSET", "NUCLEUS", "INITIAL"):
                i += 1
            elif i == len(roles) - 1:
                i += 1
                break
    return i == len(roles) and syl > 0

role_sequences = []
for w in all_words:
    glyphs = tokenize_word(w)
    roles = [classify_role(g) for g in glyphs]
    role_sequences.append(tuple(roles))

role_seq_counts = Counter(role_sequences)
total_w = len(all_words)

print("\nTop 30 role-sequences:")
cumulative = 0
for seq, cnt in role_seq_counts.most_common(30):
    cumulative += cnt
    examples = [w for w, rs in zip(all_words, role_sequences) if rs == seq][:3]
    print(f"  {str(seq):70s}  {cnt:5d} ({100*cnt/total_w:.1f}%)  cum={100*cumulative/total_w:.1f}%  ex: {', '.join(examples)}")

single_fit = sum(1 for r in role_sequences if fits_single_syllable(r))
multi_fit = sum(1 for r in role_sequences if fits_multi_syllable(r))
print(f"\nSingle-syllable fit (I? O* N+ C* F?): {single_fit}/{total_w} ({100*single_fit/total_w:.1f}%)")
print(f"Multi-syllable fit:                    {multi_fit}/{total_w} ({100*multi_fit/total_w:.1f}%)")

non_fit = [(w, r) for w, r in zip(all_words, role_sequences) if not fits_multi_syllable(r)]
print(f"\nNon-fitting words: {len(non_fit)}")
for w, r in non_fit[:15]:
    print(f"  {w:25s} -> {r}")

# ============================================================
# 9. SLOT INVENTORIES
# ============================================================
print("\n" + "="*60)
print("9. COMBINATORIAL: SLOT INVENTORIES")
print("="*60)

slot_inv = defaultdict(Counter)
for w in all_words:
    glyphs = tokenize_word(w)
    roles = [classify_role(g) for g in glyphs]
    if fits_single_syllable(roles):
        for g, r in zip(glyphs, roles):
            slot_inv[r][g] += 1

for slot in ["INITIAL", "ONSET", "NUCLEUS", "CODA", "FINAL"]:
    inv = slot_inv[slot]
    total = sum(inv.values())
    if total == 0:
        continue
    items = sorted(inv.items(), key=lambda x: -x[1])
    print(f"\n  {slot} (total={total}, unique={len(inv)}):")
    for g, c in items:
        print(f"    {g:5s}: {c:6d} ({100*c/total:.1f}%)")

sizes = {}
for slot in ["INITIAL", "ONSET", "NUCLEUS", "CODA", "FINAL"]:
    sizes[slot] = len(slot_inv[slot])
theoretical = (sizes.get("INITIAL", 0) + 1) * (sizes.get("ONSET", 0) + 1) * max(sizes.get("NUCLEUS", 1), 1) * (sizes.get("CODA", 0) + 1) * (sizes.get("FINAL", 0) + 1)
print(f"\nTheoretical combinations: {theoretical}")
print(f"Actual unique single-syllable words: {len(set(w for w, r in zip(all_words, role_sequences) if fits_single_syllable(r)))}")

# ============================================================
# 10. SECTION-BASED COMPONENT DISTRIBUTION
# ============================================================
print("\n" + "="*60)
print("10. SECTION-BASED COMPONENT DISTRIBUTION")
print("="*60)

current_page = ""
page_words = defaultdict(list)
for line in lines:
    line = line.strip()
    m = re.match(r"<(f\d+[rv])", line)
    if m:
        current_page = m.group(1)
        continue
    if current_page:
        m2 = re.match(r"<[^>]+>\s*(.*)", line)
        if m2:
            text = m2.group(1)
            text = re.sub(r"<[^>]*>", "", text)
            text = re.sub(r"@\d+;?", "", text)
            text = re.sub(r"\{[^}]*\}", "", text)
            text = re.sub(r"[,?\.\*!\'\-]", "", text)
            for w in text.split():
                w = w.strip()
                if w:
                    page_words[current_page].append(w)

sections = defaultdict(list)
for page, words in page_words.items():
    m = re.match(r"f(\d+)", page)
    if m:
        num = int(m.group(1))
        if num <= 57:
            sections["herbal"].extend(words)
        elif 67 <= num <= 73:
            sections["astro"].extend(words)
        elif 75 <= num <= 84:
            sections["bio"].extend(words)
        elif 87 <= num <= 102:
            sections["pharma"].extend(words)
        elif 103 <= num <= 116:
            sections["recipe"].extend(words)
        else:
            sections["other"].extend(words)

print("\nBench-glyph frequency by section:")
print(f"{'Section':>10s}  {'Words':>6s}", end="")
for bg in sorted(bench_glyphs):
    print(f"  {bg:>6s}", end="")
print()
for section in sorted(sections.keys()):
    words = sections[section]
    if not words:
        continue
    all_g = [g for w in words for g in tokenize_word(w)]
    total = len(all_g)
    gc = Counter(all_g)
    print(f"{section:>10s}  {total:6d}", end="")
    for bg in sorted(bench_glyphs):
        cnt = gc.get(bg, 0)
        print(f"  {100*cnt/total:5.2f}%", end="")
    print()

print("\nGallows frequency by section:")
print(f"{'Section':>10s}  {'Words':>6s}", end="")
for gg in sorted({"k", "t", "p", "f"}):
    print(f"  {gg:>6s}", end="")
for gc2 in sorted({"ckh", "cth", "cph", "cfh"}):
    print(f"  {gc2:>6s}", end="")
print()
for section in sorted(sections.keys()):
    words = sections[section]
    if not words:
        continue
    all_g = [g for w in words for g in tokenize_word(w)]
    total = len(all_g)
    gc = Counter(all_g)
    print(f"{section:>10s}  {total:6d}", end="")
    for gg in sorted({"k", "t", "p", "f"}):
        cnt = gc.get(gg, 0)
        print(f"  {100*cnt/total:5.2f}%", end="")
    for gc2 in sorted({"ckh", "cth", "cph", "cfh"}):
        cnt = gc.get(gc2, 0)
        print(f"  {100*cnt/total:5.2f}%", end="")
    print()

# ============================================================
# 11. CONDITIONAL ENTROPY
# ============================================================
print("\n" + "="*60)
print("11. CONDITIONAL ENTROPY: GLYPH TYPE GIVEN POSITION")
print("="*60)

all_types_flat = [t for w in all_words for t in get_type_sequence(w)]
uncond_h = entropy(Counter(all_types_flat))

total_all = sum(sum(pos_type_dist[p].values()) for p in range(max_pos))
cond_h = 0
for pos in range(max_pos):
    pt = sum(pos_type_dist[pos].values())
    if pt < 10:
        continue
    weight = pt / total_all
    cond_h += weight * entropy(pos_type_dist[pos])

print(f"\nH(glyph_type) unconditional:          {uncond_h:.4f} bits")
print(f"H(glyph_type | position) conditional: {cond_h:.4f} bits")
print(f"Information gain from position:       {uncond_h - cond_h:.4f} bits")
print(f"Reduction:                            {100*(uncond_h - cond_h)/uncond_h:.1f}%")
print(f"\n  High reduction => position determines type (syllabic/Hangul-like)")
print(f"  Low reduction => position irrelevant (alphabetic)")

print("\n\nANALYSIS COMPLETE.")
