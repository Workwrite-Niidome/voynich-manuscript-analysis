"""
FALSE POSITIVE RATE ANALYSIS FOR CONSONANT SKELETON REVERSAL (Hypothesis D)
============================================================================
Question: Is the 21.51% match rate for consonant skeleton reversal REAL
or a statistical artifact of short consonant strings?

Method:
1. Calculate actual match rate for Voynich consonant skeletons reversed -> Italian
2. Generate RANDOM consonant strings of same length distribution -> Italian
3. SHUFFLE Voynich words (destroy any linguistic structure) and test
4. Analyze match rates by skeleton LENGTH (short skeletons = high false positive)
5. Semantic coherence check: do matches make botanical/pharmaceutical sense?

If random baseline ~ 15-20%, then 21.51% is NOT significant.
If random baseline ~ 5-10%, then 21.51% IS significant.
"""

import re
import random
import string
from collections import Counter, defaultdict

# ============================================================
# ITALIAN WORD LIST (same as rtl_hypothesis_test.py)
# ============================================================

ITALIAN_COMMON = {
    "il", "lo", "la", "le", "li", "i", "gli", "un", "uno", "una",
    "io", "tu", "lui", "lei", "noi", "voi", "loro", "si", "se",
    "mi", "ti", "ci", "vi", "ne", "che", "chi", "cui", "quale",
    "questo", "questa", "quello", "quella", "ogni",
    "di", "da", "in", "con", "su", "per", "tra", "fra", "a", "e",
    "o", "ma", "al", "del", "nel", "dal", "sul", "col",
    "alla", "della", "nella", "dalla", "sulla",
    "allo", "dello", "nello", "dallo", "sullo",
    "ai", "dei", "nei", "dai", "sui",
    "alle", "delle", "nelle", "dalle", "sulle",
    "non", "no", "come", "dove", "quando", "poi", "ora", "ancora",
    "essere", "avere", "fare", "dire", "dare", "stare", "andare",
    "venire", "potere", "volere", "dovere", "sapere", "vedere",
    "prendere", "mettere", "trovare", "parlare", "portare",
    "ha", "ho", "hai", "hanno", "sono", "sei", "era", "fu",
    "fa", "fai", "fanno", "va", "vai", "sta",
    "acqua", "aria", "terra", "fuoco", "sole", "luna", "stella",
    "cielo", "mare", "monte", "campo", "via", "casa", "porta",
    "mano", "piede", "occhio", "testa", "corpo", "cuore",
    "oro", "argento", "ferro", "rame", "sale", "olio", "vino",
    "pane", "carne", "pesce", "latte", "miele",
    "albero", "foglia", "fiore", "frutto", "radice", "seme",
    "erba", "rosa", "giglio", "salvia", "menta", "rosmarino",
    "donna", "uomo", "re", "regina", "dio", "santo",
    "giorno", "notte", "anno", "mese", "ora", "tempo",
    "parte", "tutto", "cosa", "modo", "nome", "vita", "morte",
    "bene", "male", "forza", "natura", "arte", "opera",
    "libro", "carta", "lettera", "parola", "segno",
    "sangue", "spirito", "anima", "mente",
    "medicina", "rimedio", "cura", "febbre", "dolore", "male",
    "stomaco", "fegato", "polmone", "rene", "bile", "flemma",
    "decotto", "infuso", "unguento", "balsamo", "sciroppo",
    "dose", "goccia", "polvere", "pasta", "succo",
    "toro", "olla", "otto", "testa", "occhi",
    "pietra", "mercurio", "zolfo", "vetro", "cenere",
    "distillare", "calcinare", "dissolvere",
    "elisir", "tintura", "essenza", "quintessenza",
    "grande", "piccolo", "buono", "cattivo", "bello", "brutto",
    "alto", "basso", "lungo", "corto", "largo", "stretto",
    "caldo", "freddo", "secco", "umido", "dolce", "amaro",
    "rosso", "verde", "bianco", "nero", "giallo", "azzurro",
    "primo", "secondo", "terzo", "quarto", "quinto",
    "nuovo", "vecchio", "giovane", "forte", "debole",
    "due", "tre", "quattro", "cinque", "sei", "sette", "otto",
    "nove", "dieci", "cento", "mille",
    "piu", "molto", "poco", "tanto", "quanto", "troppo",
    "sempre", "mai", "qui", "li", "la", "su", "giu",
    "dentro", "fuori", "sopra", "sotto", "prima", "dopo",
    "anche", "solo", "proprio", "altro", "stesso",
    "toro", "olio", "otto", "oro", "olla",
    "al", "da", "de", "do", "ed", "et", "id", "od",
    "sol", "cor", "col", "dar", "dir", "lor",
    "ora", "era", "ira", "are", "ore",
    "oca", "eco", "ode", "uso",
}

ITALIAN_ARCHAIC = {
    "acqua", "aceto", "aglio", "alcuno", "aloe", "amaro",
    "anice", "assenzio", "basilico", "borragine", "camomilla",
    "cannella", "cardamomo", "chiodo", "cipolla", "cocco",
    "comino", "corallo", "crescione", "croco", "dattero",
    "edera", "fico", "finocchio", "garofano", "gelsomino",
    "genziana", "incenso", "iris", "issopo", "lattuga",
    "lauro", "lavanda", "lino", "liquirizia", "malva",
    "mandorla", "maggiorana", "mirra", "mirto", "muschio",
    "noce", "oliva", "origano", "ortica", "pepe",
    "prezzemolo", "rabarbaro", "ruta", "sandalo", "senape",
    "timo", "valeriana", "verbena", "viola", "zafferano",
    "zenzero", "zucca",
    "lo", "la", "li", "le", "lo", "el", "al", "del",
    "cho", "chon", "chosa", "chole", "chome",
    "acque", "olio", "oliva", "ombra", "onda",
}

ITALIAN_WORDS = ITALIAN_COMMON | ITALIAN_ARCHAIC

# ============================================================
# EVA PARSING (from rtl_hypothesis_test.py)
# ============================================================

def parse_ivtff(filepath):
    lines_data = []
    current_folio = None
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            header_match = re.match(r'<(f\d+[rv]\d?)>\s+<!\s*(.*?)>', line)
            if header_match:
                current_folio = header_match.group(1)
                continue
            text_match = re.match(r'<([^>]+)>\s+(.*)', line)
            if text_match:
                text = text_match.group(2)
                text = re.sub(r'<%>', '', text)
                text = re.sub(r'<\$>', '', text)
                text = re.sub(r'<->', ' ', text)
                text = re.sub(r'<[^>]*>', '', text)
                text = re.sub(r'\{[^}]*\}', '', text)
                words = re.findall(r'[a-z]+', text.lower())
                words = [w for w in words if len(w) > 0]
                if words:
                    lines_data.append((current_folio, 0, words))
    return lines_data


def tokenize_eva(word):
    tokens = []
    i = 0
    while i < len(word):
        if i + 3 <= len(word) and word[i:i+3] in ('cth', 'ckh', 'cfh', 'cph'):
            tokens.append(word[i:i+3])
            i += 3
        elif i + 2 <= len(word) and word[i:i+2] in ('ch', 'sh', 'qo'):
            tokens.append(word[i:i+2])
            i += 2
        else:
            tokens.append(word[i])
            i += 1
    return tokens


EVA_VOWELS = {'a', 'e', 'i', 'o', 'y'}
EVA_CONSONANTS = {'d', 'k', 'l', 'r', 'n', 's', 't', 'p', 'f', 'q', 'm',
                   'ch', 'sh', 'cth', 'ckh', 'cfh', 'cph'}

def is_consonant_token(token):
    return token in EVA_CONSONANTS or (len(token) > 1 and token not in EVA_VOWELS)


def extract_consonant_skeleton(word):
    tokens = tokenize_eva(word)
    consonants = [t for t in tokens if is_consonant_token(t)]
    return ''.join(consonants)


# ============================================================
# ITALIAN CONSONANT SKELETON DATABASE
# ============================================================

ITALIAN_VOWELS = set('aeiou')

def build_italian_consonant_skeletons():
    skeletons = defaultdict(list)
    for word in ITALIAN_WORDS:
        skeleton = ''.join(c for c in word if c not in ITALIAN_VOWELS)
        if skeleton:
            skeletons[skeleton].append(word)
    return skeletons


# ============================================================
# TEST 1: ACTUAL VOYNICH MATCH RATE (by skeleton length)
# ============================================================

def test_voynich_actual(unique_words, italian_skeletons):
    """Test actual Voynich words: extract skeleton, reverse, match Italian."""
    matches_by_length = defaultdict(list)
    total_by_length = defaultdict(int)
    all_matches = []

    for w in unique_words:
        skeleton = extract_consonant_skeleton(w)
        if not skeleton:
            continue
        skel_len = len(skeleton)
        total_by_length[skel_len] += 1
        reversed_skel = skeleton[::-1]
        if reversed_skel in italian_skeletons:
            matches_by_length[skel_len].append((w, skeleton, reversed_skel, italian_skeletons[reversed_skel]))
            all_matches.append((w, skeleton, reversed_skel, italian_skeletons[reversed_skel]))

    return matches_by_length, total_by_length, all_matches


# ============================================================
# TEST 2: RANDOM CONSONANT STRINGS (same length distribution)
# ============================================================

def test_random_strings(skeleton_lengths, italian_skeletons, n_trials=1000):
    """Generate random consonant strings matching Voynich length distribution.

    Uses the EVA consonant alphabet (single-char consonants only for simplicity):
    d, k, l, r, n, s, t, p, f, q, m = 11 consonants
    """
    eva_consonant_chars = list('dklrnstpfqm')

    match_rates = []
    for trial in range(n_trials):
        matches = 0
        total = 0
        for skel_len in skeleton_lengths:
            if skel_len == 0:
                continue
            total += 1
            # Generate random consonant string of this length
            random_skel = ''.join(random.choice(eva_consonant_chars) for _ in range(skel_len))
            reversed_random = random_skel[::-1]
            if reversed_random in italian_skeletons:
                matches += 1
        if total > 0:
            match_rates.append(matches / total)

    return match_rates


def test_random_by_length(skeleton_lengths, italian_skeletons, n_trials=500):
    """Random baseline broken down by skeleton length."""
    eva_consonant_chars = list('dklrnstpfqm')

    # Group lengths
    length_counts = Counter(skeleton_lengths)

    results_by_length = defaultdict(list)  # length -> list of match counts per trial

    for trial in range(n_trials):
        for skel_len, count in length_counts.items():
            if skel_len == 0:
                continue
            matches = 0
            for _ in range(count):
                random_skel = ''.join(random.choice(eva_consonant_chars) for _ in range(skel_len))
                reversed_random = random_skel[::-1]
                if reversed_random in italian_skeletons:
                    matches += 1
            results_by_length[skel_len].append(matches / count)

    return results_by_length


# ============================================================
# TEST 3: SHUFFLED VOYNICH (destroy word-position structure)
# ============================================================

def test_shuffled_voynich(unique_words, italian_skeletons, n_trials=500):
    """Shuffle the CHARACTERS within each Voynich word, preserving length distribution.
    This destroys any internal consonant ordering while keeping the same character frequencies."""
    match_rates = []

    for trial in range(n_trials):
        matches = 0
        total = 0
        for w in unique_words:
            skeleton = extract_consonant_skeleton(w)
            if not skeleton:
                continue
            total += 1
            # Shuffle the skeleton characters
            skel_chars = list(skeleton)
            random.shuffle(skel_chars)
            shuffled_skel = ''.join(skel_chars)
            reversed_shuffled = shuffled_skel[::-1]
            if reversed_shuffled in italian_skeletons:
                matches += 1
        if total > 0:
            match_rates.append(matches / total)

    return match_rates


# ============================================================
# TEST 4: UNREVERSED SKELETON MATCH (control)
# ============================================================

def test_unreversed_skeletons(unique_words, italian_skeletons):
    """Match Voynich skeletons WITHOUT reversing. If reversal is meaningful,
    reversed should match MORE than unreversed."""
    matches = []
    total = 0
    for w in unique_words:
        skeleton = extract_consonant_skeleton(w)
        if not skeleton:
            continue
        total += 1
        if skeleton in italian_skeletons:
            matches.append((w, skeleton, italian_skeletons[skeleton]))
    return matches, total


# ============================================================
# TEST 5: SEMANTIC COHERENCE OF MATCHES
# ============================================================

# Categorize Italian words by domain
BOTANICAL_PHARMA = {
    "rosa", "ruta", "salvia", "menta", "rosmarino", "aloe", "anice",
    "basilico", "camomilla", "cannella", "cipolla", "comino", "croco",
    "edera", "fico", "finocchio", "garofano", "gelsomino", "genziana",
    "iris", "issopo", "lattuga", "lauro", "lavanda", "lino", "malva",
    "mandorla", "maggiorana", "mirra", "mirto", "noce", "oliva",
    "origano", "ortica", "pepe", "rabarbaro", "sandalo", "senape",
    "timo", "valeriana", "verbena", "viola", "zafferano", "zenzero",
    "zucca", "borragine", "crescione", "dattero", "muschio",
    "erba", "foglia", "fiore", "frutto", "radice", "seme", "albero",
    "acqua", "olio", "aceto", "miele", "sale", "vino", "latte",
    "medicina", "rimedio", "cura", "febbre", "dolore",
    "decotto", "infuso", "unguento", "balsamo", "sciroppo",
    "dose", "goccia", "polvere", "pasta", "succo",
    "stomaco", "fegato", "polmone", "rene", "bile", "flemma",
    "sangue", "corpo", "testa", "mano", "piede", "occhio", "cuore",
    "elisir", "tintura", "essenza",
    "caldo", "freddo", "secco", "umido", "dolce", "amaro",
    "rosso", "verde", "bianco", "nero", "giallo",
    "sole", "luna", "stella", "terra", "aria", "fuoco",
    "oro", "argento", "ferro", "rame",
    "pietra", "mercurio", "zolfo", "cenere",
    "forte", "debole", "grande", "piccolo",
    "natura", "forza", "spirito", "anima",
}

FUNCTION_WORDS = {
    "il", "lo", "la", "le", "li", "i", "gli", "un", "uno", "una",
    "di", "da", "in", "con", "su", "per", "tra", "fra", "a", "e", "o",
    "ma", "al", "del", "nel", "dal", "sul", "col",
    "alla", "della", "nella", "dalla", "sulla",
    "non", "no", "che", "chi", "cui", "si", "se",
    "io", "tu", "lui", "lei", "noi", "voi", "loro",
    "mi", "ti", "ci", "vi", "ne",
}


def analyze_semantic_coherence(matches):
    """Classify matched Italian words by domain."""
    botanical_matches = []
    function_matches = []
    other_matches = []

    for w, skeleton, rev_skeleton, italian_list in matches:
        for it_word in italian_list:
            if it_word in BOTANICAL_PHARMA:
                botanical_matches.append((w, skeleton, rev_skeleton, it_word))
            elif it_word in FUNCTION_WORDS:
                function_matches.append((w, skeleton, rev_skeleton, it_word))
            else:
                other_matches.append((w, skeleton, rev_skeleton, it_word))

    return botanical_matches, function_matches, other_matches


# ============================================================
# MAIN
# ============================================================

def main():
    random.seed(42)  # Reproducibility

    filepath = "C:/Users/kazuk/Downloads/voynich_analysis/IT2a-n.txt"

    print("=" * 78)
    print("FALSE POSITIVE RATE ANALYSIS: CONSONANT SKELETON REVERSAL (Hypothesis D)")
    print("=" * 78)

    # Parse Voynich
    lines_data = parse_ivtff(filepath)
    all_words = []
    for _, _, words in lines_data:
        all_words.extend(words)
    unique_words = list(set(all_words))

    print(f"\nTotal Voynich words: {len(all_words)}")
    print(f"Unique Voynich words: {len(unique_words)}")
    print(f"Italian dictionary size: {len(ITALIAN_WORDS)}")

    # Build Italian skeletons
    italian_skeletons = build_italian_consonant_skeletons()
    print(f"Unique Italian consonant skeletons: {len(italian_skeletons)}")

    # Show Italian skeleton length distribution
    it_skel_by_len = defaultdict(int)
    for skel in italian_skeletons:
        it_skel_by_len[len(skel)] += 1
    print(f"\nItalian skeleton distribution by length:")
    for length in sorted(it_skel_by_len):
        print(f"  Length {length}: {it_skel_by_len[length]} unique skeletons")

    # Compute how many possible skeletons exist at each length (11 EVA consonants)
    print(f"\nTheoretical coverage (Italian skeletons / possible strings):")
    for length in sorted(it_skel_by_len):
        possible = 11 ** length  # 11 EVA consonant characters
        # But Italian uses different consonants. Let's use 16 Italian consonants
        # b, c, d, f, g, h, l, m, n, p, q, r, s, t, v, z
        coverage_pct = it_skel_by_len[length] / possible * 100 if possible > 0 else 0
        print(f"  Length {length}: {it_skel_by_len[length]} / {possible} = {coverage_pct:.4f}%")

    # ============================================================
    # TEST 1: ACTUAL VOYNICH MATCH RATE
    # ============================================================
    print("\n" + "=" * 78)
    print("TEST 1: ACTUAL VOYNICH CONSONANT SKELETON REVERSAL -> ITALIAN")
    print("=" * 78)

    matches_by_len, total_by_len, all_matches = test_voynich_actual(unique_words, italian_skeletons)

    total_matched = len(all_matches)
    total_tested = sum(total_by_len.values())
    overall_rate = total_matched / total_tested * 100 if total_tested > 0 else 0

    print(f"\nOverall: {total_matched} / {total_tested} unique words matched = {overall_rate:.2f}%")
    print(f"\nBreakdown by consonant skeleton length:")
    print(f"{'Length':>8} {'Tested':>8} {'Matched':>8} {'Rate':>10}")
    print("-" * 40)
    for length in sorted(total_by_len):
        tested = total_by_len[length]
        matched = len(matches_by_len.get(length, []))
        rate = matched / tested * 100 if tested > 0 else 0
        print(f"{length:>8} {tested:>8} {matched:>8} {rate:>9.2f}%")

    # ============================================================
    # TEST 2: UNREVERSED CONTROL
    # ============================================================
    print("\n" + "=" * 78)
    print("TEST 2: UNREVERSED SKELETON CONTROL (should be LOWER if reversal matters)")
    print("=" * 78)

    unreversed_matches, unreversed_total = test_unreversed_skeletons(unique_words, italian_skeletons)
    unreversed_rate = len(unreversed_matches) / unreversed_total * 100 if unreversed_total > 0 else 0
    print(f"\nUnreversed: {len(unreversed_matches)} / {unreversed_total} = {unreversed_rate:.2f}%")
    print(f"Reversed:   {total_matched} / {total_tested} = {overall_rate:.2f}%")
    diff = overall_rate - unreversed_rate
    print(f"Difference: {diff:+.2f} percentage points")
    if abs(diff) < 2:
        print(">>> VERDICT: Reversal provides NO meaningful improvement over non-reversal.")
        print(">>> This suggests the matches are driven by short skeleton length, not reversal direction.")
    else:
        print(f">>> Reversal {'IMPROVES' if diff > 0 else 'WORSENS'} match rate by {abs(diff):.2f}pp")

    # ============================================================
    # TEST 3: RANDOM CONSONANT STRINGS BASELINE
    # ============================================================
    print("\n" + "=" * 78)
    print("TEST 3: RANDOM CONSONANT STRING BASELINE (500 trials)")
    print("=" * 78)

    # Get skeleton lengths from Voynich
    skeleton_lengths = []
    for w in unique_words:
        skel = extract_consonant_skeleton(w)
        skeleton_lengths.append(len(skel))
    skeleton_lengths = [s for s in skeleton_lengths if s > 0]

    print(f"\nVoynich skeleton length distribution:")
    len_dist = Counter(skeleton_lengths)
    for length in sorted(len_dist):
        print(f"  Length {length}: {len_dist[length]} words ({100*len_dist[length]/len(skeleton_lengths):.1f}%)")

    print("\nRunning 500 random trials...")
    random_rates = test_random_strings(skeleton_lengths, italian_skeletons, n_trials=500)

    mean_random = sum(random_rates) / len(random_rates) * 100
    sorted_rates = sorted(random_rates)
    p5 = sorted_rates[int(0.05 * len(sorted_rates))] * 100
    p95 = sorted_rates[int(0.95 * len(sorted_rates))] * 100
    p99 = sorted_rates[int(0.99 * len(sorted_rates))] * 100
    max_random = max(random_rates) * 100

    print(f"\nRandom baseline match rate:")
    print(f"  Mean:     {mean_random:.2f}%")
    print(f"  5th pct:  {p5:.2f}%")
    print(f"  95th pct: {p95:.2f}%")
    print(f"  99th pct: {p99:.2f}%")
    print(f"  Maximum:  {max_random:.2f}%")
    print(f"\nActual Voynich: {overall_rate:.2f}%")

    if overall_rate > p99:
        z_approx = (overall_rate/100 - mean_random/100) / (max(0.001, (p95/100 - p5/100) / 3.29))
        print(f"\n>>> SIGNIFICANT: Voynich rate ({overall_rate:.2f}%) exceeds 99th percentile ({p99:.2f}%)")
        print(f">>> Approximate z-score: {z_approx:.2f}")
    elif overall_rate > p95:
        print(f"\n>>> MARGINALLY SIGNIFICANT: Voynich rate ({overall_rate:.2f}%) exceeds 95th percentile ({p95:.2f}%)")
    else:
        print(f"\n>>> NOT SIGNIFICANT: Voynich rate ({overall_rate:.2f}%) is within random range ({p5:.2f}% - {p95:.2f}%)")

    # ============================================================
    # TEST 3b: RANDOM BASELINE BY LENGTH
    # ============================================================
    print("\n" + "=" * 78)
    print("TEST 3b: RANDOM BASELINE BY SKELETON LENGTH (500 trials)")
    print("=" * 78)

    random_by_len = test_random_by_length(skeleton_lengths, italian_skeletons, n_trials=500)

    print(f"\n{'Length':>8} {'Voynich%':>10} {'Random Mean%':>13} {'Random 95%':>12} {'Significant?':>14}")
    print("-" * 60)
    for length in sorted(total_by_len):
        voynich_rate = len(matches_by_len.get(length, [])) / total_by_len[length] * 100 if total_by_len[length] > 0 else 0
        if length in random_by_len:
            rand_rates = random_by_len[length]
            rand_mean = sum(rand_rates) / len(rand_rates) * 100
            rand_sorted = sorted(rand_rates)
            rand_p95 = rand_sorted[int(0.95 * len(rand_sorted))] * 100
            sig = "YES ***" if voynich_rate > rand_p95 else "no"
        else:
            rand_mean = 0
            rand_p95 = 0
            sig = "N/A"
        print(f"{length:>8} {voynich_rate:>9.2f}% {rand_mean:>12.2f}% {rand_p95:>11.2f}% {sig:>14}")

    # ============================================================
    # TEST 4: SHUFFLED VOYNICH (character-level shuffle within words)
    # ============================================================
    print("\n" + "=" * 78)
    print("TEST 4: SHUFFLED VOYNICH WORDS (destroy internal consonant order)")
    print("=" * 78)

    print("\nRunning 500 shuffle trials...")
    shuffled_rates = test_shuffled_voynich(unique_words, italian_skeletons, n_trials=500)

    mean_shuffled = sum(shuffled_rates) / len(shuffled_rates) * 100
    sorted_shuffled = sorted(shuffled_rates)
    p5_s = sorted_shuffled[int(0.05 * len(sorted_shuffled))] * 100
    p95_s = sorted_shuffled[int(0.95 * len(sorted_shuffled))] * 100
    p99_s = sorted_shuffled[int(0.99 * len(sorted_shuffled))] * 100

    print(f"\nShuffled Voynich baseline match rate:")
    print(f"  Mean:     {mean_shuffled:.2f}%")
    print(f"  5th pct:  {p5_s:.2f}%")
    print(f"  95th pct: {p95_s:.2f}%")
    print(f"  99th pct: {p99_s:.2f}%")
    print(f"\nActual Voynich: {overall_rate:.2f}%")

    if overall_rate > p99_s:
        print(f">>> SIGNIFICANT vs shuffled: Consonant ORDER matters (not just consonant frequency)")
    else:
        print(f">>> NOT SIGNIFICANT: Shuffled words produce similar match rates")
        print(f">>> This means the matches are driven by consonant FREQUENCY, not ORDER")

    # ============================================================
    # TEST 5: SEMANTIC COHERENCE
    # ============================================================
    print("\n" + "=" * 78)
    print("TEST 5: SEMANTIC COHERENCE OF MATCHES")
    print("=" * 78)

    botanical, function, other = analyze_semantic_coherence(all_matches)
    total_semantic = len(botanical) + len(function) + len(other)

    print(f"\nTotal match instances (word-to-Italian-word pairs): {total_semantic}")
    print(f"  Botanical/Pharmaceutical: {len(botanical)} ({100*len(botanical)/max(1,total_semantic):.1f}%)")
    print(f"  Function words:          {len(function)} ({100*len(function)/max(1,total_semantic):.1f}%)")
    print(f"  Other:                    {len(other)} ({100*len(other)/max(1,total_semantic):.1f}%)")

    print(f"\nSample botanical/pharmaceutical matches:")
    seen = set()
    count = 0
    for w, skel, rev_skel, it_word in botanical:
        key = (w, it_word)
        if key not in seen:
            seen.add(key)
            print(f"  {w} -> [{skel}] -> [{rev_skel}] -> {it_word}")
            count += 1
            if count >= 30:
                break

    # ============================================================
    # TEST 6: KEY CLAIMED EXAMPLES VERIFICATION
    # ============================================================
    print("\n" + "=" * 78)
    print("TEST 6: VERIFICATION OF KEY CLAIMED EXAMPLES")
    print("=" * 78)

    key_claims = [
        ("sory", "rosa", "medicinal plant"),
        ("raiin", "nero", "color in herbal descriptions"),
        ("taor", "ruta", "major medicinal herb"),
        ("dam", "modo", "pharmaceutical term"),
    ]

    for voynich_word, claimed_italian, claimed_meaning in key_claims:
        skeleton = extract_consonant_skeleton(voynich_word)
        reversed_skel = skeleton[::-1]
        it_skel = ''.join(c for c in claimed_italian if c not in ITALIAN_VOWELS)

        # Check if claimed Italian word exists
        in_dict = claimed_italian in ITALIAN_WORDS
        skel_match = reversed_skel == it_skel

        # How many OTHER Italian words share this skeleton?
        other_words = italian_skeletons.get(reversed_skel, [])

        # How many random words would match a skeleton of this length?
        possible_at_length = 11 ** len(skeleton)
        it_skels_at_length = it_skel_by_len.get(len(skeleton), 0)
        random_match_prob = it_skels_at_length / possible_at_length * 100 if possible_at_length > 0 else 0

        print(f"\n  {voynich_word} -> [{skeleton}] -> [{reversed_skel}]")
        print(f"    Claimed: {claimed_italian} ({claimed_meaning})")
        print(f"    Italian skeleton: [{it_skel}], Match: {skel_match}")
        print(f"    In dictionary: {in_dict}")
        print(f"    ALL Italian words with skeleton [{reversed_skel}]: {other_words}")
        print(f"    Random match probability at length {len(skeleton)}: {random_match_prob:.2f}%")
        print(f"    >>> {'CHERRY-PICKED (many alternatives)' if len(other_words) > 3 else 'Reasonably specific' if len(other_words) <= 2 else 'Moderate ambiguity'}")

    # ============================================================
    # FINAL VERDICT
    # ============================================================
    print("\n" + "=" * 78)
    print("FINAL VERDICT")
    print("=" * 78)

    print(f"""
ACTUAL VOYNICH MATCH RATE:     {overall_rate:.2f}%
UNREVERSED CONTROL:            {unreversed_rate:.2f}%
RANDOM BASELINE (mean):        {mean_random:.2f}%
RANDOM BASELINE (95th pct):    {p95:.2f}%
SHUFFLED VOYNICH (mean):       {mean_shuffled:.2f}%
SHUFFLED VOYNICH (95th pct):   {p95_s:.2f}%

REVERSAL IMPROVEMENT:          {diff:+.2f} percentage points vs unreversed
VOYNICH vs RANDOM MEAN:        {overall_rate - mean_random:+.2f} percentage points

CONCLUSION:""")

    is_significant_vs_random = overall_rate > p95
    is_significant_vs_shuffled = overall_rate > p95_s
    reversal_helps = diff > 2.0

    if not is_significant_vs_random:
        print("  The 21.51% match rate is a FALSE POSITIVE.")
        print("  Random consonant strings produce similar match rates.")
        print("  The effect is driven entirely by short consonant skeletons")
        print("  matching many Italian words by chance.")
    elif not reversal_helps:
        print("  The match rate exceeds random, but REVERSAL adds nothing.")
        print("  Unreversed skeletons match just as well.")
        print("  The effect is driven by EVA consonant frequency resembling Italian,")
        print("  not by a specific reversal cipher.")
    elif not is_significant_vs_shuffled:
        print("  The match rate exceeds pure random, but shuffled Voynich matches equally.")
        print("  The effect is driven by Voynich CONSONANT FREQUENCIES (not order).")
        print("  The specific consonant ORDER within Voynich words does not matter.")
    else:
        print("  The match rate is SIGNIFICANTLY above all baselines.")
        print("  Reversal improves matches, and consonant order matters.")
        print("  The consonant skeleton reversal hypothesis CANNOT be dismissed.")
        print("  However, verify the matches make contextual sense before claiming decipherment.")


if __name__ == "__main__":
    main()
