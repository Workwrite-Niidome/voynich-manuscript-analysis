"""
RIGHT-TO-LEFT READING HYPOTHESIS TEST
======================================
Tests four hypotheses about R-to-L reading of the Voynich Manuscript:
  A: Words R-to-L, lines L-to-R (simple word reversal)
  B: Only consonants reversed, vowels stay in place
  C: Boustrophedon (even lines reversed)
  D: Consonant skeleton extraction, reversed, matched against Italian

Uses a comprehensive Italian word list for matching.
"""

import re
from collections import Counter, defaultdict

# ============================================================
# ITALIAN WORD LIST
# ============================================================
# Comprehensive list of common Italian words (articles, prepositions,
# nouns, verbs, adjectives) that could plausibly appear in a 15th-century
# herbal/alchemical/astrological manuscript.

ITALIAN_WORDS = set()

# We'll load from a generated list. For thoroughness, include:
# - All common function words
# - Herbal/medical/alchemical vocabulary
# - Common nouns, verbs, adjectives

ITALIAN_COMMON = {
    # Articles & pronouns
    "il", "lo", "la", "le", "li", "i", "gli", "un", "uno", "una",
    "io", "tu", "lui", "lei", "noi", "voi", "loro", "si", "se",
    "mi", "ti", "ci", "vi", "ne", "che", "chi", "cui", "quale",
    "questo", "questa", "quello", "quella", "ogni",

    # Prepositions & conjunctions
    "di", "da", "in", "con", "su", "per", "tra", "fra", "a", "e",
    "o", "ma", "al", "del", "nel", "dal", "sul", "col",
    "alla", "della", "nella", "dalla", "sulla",
    "allo", "dello", "nello", "dallo", "sullo",
    "ai", "dei", "nei", "dai", "sui",
    "alle", "delle", "nelle", "dalle", "sulle",
    "non", "no", "come", "dove", "quando", "poi", "ora", "ancora",

    # Common verbs (infinitive + common conjugations)
    "essere", "avere", "fare", "dire", "dare", "stare", "andare",
    "venire", "potere", "volere", "dovere", "sapere", "vedere",
    "prendere", "mettere", "trovare", "parlare", "portare",
    "ha", "ho", "hai", "hanno", "sono", "sei", "era", "fu",
    "fa", "fai", "fanno", "va", "vai", "sta",

    # Common nouns
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

    # Medical/herbal terms (15th century)
    "medicina", "rimedio", "cura", "febbre", "dolore", "male",
    "stomaco", "fegato", "polmone", "rene", "bile", "flemma",
    "decotto", "infuso", "unguento", "balsamo", "sciroppo",
    "dose", "goccia", "polvere", "pasta", "succo",
    "toro", "olla", "otto", "testa", "occhi",

    # Alchemical terms
    "pietra", "mercurio", "zolfo", "vetro", "cenere",
    "distillare", "calcinare", "dissolvere",
    "elisir", "tintura", "essenza", "quintessenza",

    # Adjectives
    "grande", "piccolo", "buono", "cattivo", "bello", "brutto",
    "alto", "basso", "lungo", "corto", "largo", "stretto",
    "caldo", "freddo", "secco", "umido", "dolce", "amaro",
    "rosso", "verde", "bianco", "nero", "giallo", "azzurro",
    "primo", "secondo", "terzo", "quarto", "quinto",
    "nuovo", "vecchio", "giovane", "forte", "debole",

    # Numbers
    "due", "tre", "quattro", "cinque", "sei", "sette", "otto",
    "nove", "dieci", "cento", "mille",

    # Additional common words
    "piu", "molto", "poco", "tanto", "quanto", "troppo",
    "sempre", "mai", "qui", "li", "la", "su", "giu",
    "dentro", "fuori", "sopra", "sotto", "prima", "dopo",
    "anche", "solo", "proprio", "altro", "stesso",

    # Words specifically mentioned by Tim Carter Clausen
    "toro", "olio", "otto", "oro", "olla",

    # Additional 2-3 letter words that could match
    "al", "da", "de", "do", "ed", "et", "id", "od",
    "sol", "cor", "col", "dar", "dir", "lor",
    "ora", "era", "ira", "are", "ore",
    "oca", "eco", "ode", "ode", "uso",
}

# Generate additional Italian words by common patterns
# Italian words commonly end in -o, -a, -e, -i
# Let's also add archaic/dialectal forms
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
    # Old Italian / Tuscan
    "lo", "la", "li", "le", "lo", "el", "al", "del",
    "cho", "chon", "chosa", "chole", "chome",  # old spellings with ch
    "acque", "olio", "oliva", "ombra", "onda",
}

ITALIAN_WORDS = ITALIAN_COMMON | ITALIAN_ARCHAIC

# ============================================================
# PARSER
# ============================================================

def parse_ivtff(filepath):
    """Parse IVTFF transcription, return list of (folio, line_num, words)."""
    lines_data = []
    current_folio = None

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Folio header
            header_match = re.match(r'<(f\d+[rv]\d?)>\s+<!\s*(.*?)>', line)
            if header_match:
                current_folio = header_match.group(1)
                continue

            # Text line
            text_match = re.match(r'<([^>]+)>\s+(.*)', line)
            if text_match:
                line_id = text_match.group(1)
                text = text_match.group(2)

                # Extract line number
                ln_match = re.search(r'\.(\d+)', line_id)
                line_num = int(ln_match.group(1)) if ln_match else 0

                # Clean text: remove markup
                text = re.sub(r'<%>', '', text)
                text = re.sub(r'<\$>', '', text)
                text = re.sub(r'<->', ' ', text)  # treat line breaks as spaces
                text = re.sub(r'<[^>]*>', '', text)
                text = re.sub(r'\{[^}]*\}', '', text)

                # Extract words (EVA characters only)
                words = re.findall(r'[a-z]+', text.lower())
                words = [w for w in words if len(w) > 0]

                if words:
                    lines_data.append((current_folio, line_num, words))

    return lines_data


def get_all_words(lines_data):
    """Extract all words from parsed data."""
    all_words = []
    for folio, line_num, words in lines_data:
        all_words.extend(words)
    return all_words


# ============================================================
# EVA CHARACTER CLASSIFICATION
# ============================================================
# In EVA transcription, multi-character glyphs: ch, sh, cth, ckh, cfh, cph
# Single chars: a, e, i, o, y, d, k, l, r, n, s, t, p, f, q, m

def tokenize_eva(word):
    """Tokenize an EVA word into individual glyph tokens."""
    tokens = []
    i = 0
    while i < len(word):
        # Try longest match first
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


# Vowels and consonants in EVA
EVA_VOWELS = {'a', 'e', 'i', 'o', 'y'}
EVA_CONSONANTS = {'d', 'k', 'l', 'r', 'n', 's', 't', 'p', 'f', 'q', 'm',
                   'ch', 'sh', 'cth', 'ckh', 'cfh', 'cph'}


def is_vowel_token(token):
    return token in EVA_VOWELS


def is_consonant_token(token):
    return token in EVA_CONSONANTS or (len(token) > 1 and token not in EVA_VOWELS)


# ============================================================
# HYPOTHESIS A: Simple word reversal
# ============================================================

def hypothesis_a(words):
    """Reverse every word character-by-character. Count Italian matches."""
    reversed_words = [w[::-1] for w in words]
    matches = []
    for orig, rev in zip(words, reversed_words):
        if rev in ITALIAN_WORDS:
            matches.append((orig, rev))
    return reversed_words, matches


# ============================================================
# HYPOTHESIS B: Reverse only consonant positions, keep vowels in place
# ============================================================

def hypothesis_b_reverse(word):
    """Reverse consonant characters but keep vowels in their positions."""
    tokens = tokenize_eva(word)

    # Identify consonant positions and their tokens
    consonant_positions = []
    consonant_tokens = []
    for i, t in enumerate(tokens):
        if is_consonant_token(t):
            consonant_positions.append(i)
            consonant_tokens.append(t)

    # Reverse consonant tokens
    consonant_tokens_reversed = consonant_tokens[::-1]

    # Rebuild
    result_tokens = list(tokens)
    for idx, pos in enumerate(consonant_positions):
        result_tokens[pos] = consonant_tokens_reversed[idx]

    return ''.join(result_tokens)


def hypothesis_b(words):
    """Reverse consonants only, keep vowels in place."""
    transformed = [hypothesis_b_reverse(w) for w in words]
    matches = []
    for orig, trans in zip(words, transformed):
        if trans in ITALIAN_WORDS:
            matches.append((orig, trans))
    return transformed, matches


# ============================================================
# HYPOTHESIS C: Boustrophedon (reverse words on even-numbered lines)
# ============================================================

def hypothesis_c(lines_data):
    """Reverse words on even-numbered lines only."""
    all_transformed = []
    all_original = []
    matches = []

    for folio, line_num, words in lines_data:
        for w in words:
            if line_num % 2 == 0:  # Even lines reversed
                trans = w[::-1]
            else:
                trans = w  # Odd lines kept as-is
            all_transformed.append(trans)
            all_original.append(w)
            if trans in ITALIAN_WORDS:
                matches.append((w, trans, f"{folio}.{line_num}", "even" if line_num % 2 == 0 else "odd"))

    return all_transformed, matches


# ============================================================
# HYPOTHESIS D: Consonant skeleton extraction + reversal
# ============================================================

def extract_consonant_skeleton(word):
    """Extract only consonant tokens from an EVA word."""
    tokens = tokenize_eva(word)
    consonants = [t for t in tokens if is_consonant_token(t)]
    return ''.join(consonants)


def build_italian_consonant_skeletons():
    """Build consonant skeletons for all Italian words."""
    italian_vowels = set('aeiou')
    skeletons = defaultdict(list)
    for word in ITALIAN_WORDS:
        skeleton = ''.join(c for c in word if c not in italian_vowels)
        if skeleton:
            skeletons[skeleton].append(word)
    return skeletons


def hypothesis_d(words):
    """Extract consonant skeleton, reverse it, match against Italian skeletons."""
    italian_skeletons = build_italian_consonant_skeletons()

    matches = []
    for w in words:
        skeleton = extract_consonant_skeleton(w)
        reversed_skeleton = skeleton[::-1]
        if reversed_skeleton in italian_skeletons:
            matches.append((w, skeleton, reversed_skeleton, italian_skeletons[reversed_skeleton]))

    return matches


# ============================================================
# BASELINE: Unreversed words that happen to be Italian
# ============================================================

def baseline_check(words):
    """How many unreversed Voynich words are already Italian words?"""
    matches = []
    for w in words:
        if w in ITALIAN_WORDS:
            matches.append(w)
    return matches


# ============================================================
# MAIN
# ============================================================

def main():
    filepath = "C:/Users/kazuk/Downloads/voynich_analysis/IT2a-n.txt"

    print("=" * 70)
    print("RIGHT-TO-LEFT READING HYPOTHESIS TEST")
    print("=" * 70)

    # Parse
    lines_data = parse_ivtff(filepath)
    all_words = get_all_words(lines_data)
    unique_words = list(set(all_words))

    word_freq = Counter(all_words)

    print(f"\nTotal words: {len(all_words)}")
    print(f"Unique words: {len(unique_words)}")
    print(f"Italian dictionary size: {len(ITALIAN_WORDS)}")

    # ---- BASELINE ----
    print("\n" + "=" * 70)
    print("BASELINE: Unreversed Voynich words matching Italian")
    print("=" * 70)

    baseline_matches = baseline_check(all_words)
    baseline_unique = baseline_check(unique_words)
    baseline_freq = Counter(baseline_matches)

    print(f"Total token matches: {len(baseline_matches)} / {len(all_words)} ({100*len(baseline_matches)/len(all_words):.2f}%)")
    print(f"Unique type matches: {len(baseline_unique)} / {len(unique_words)} ({100*len(baseline_unique)/len(unique_words):.2f}%)")
    print(f"\nTop 20 baseline matches (word: count):")
    for w, c in sorted(baseline_freq.items(), key=lambda x: -x[1])[:20]:
        print(f"  {w}: {c}")

    # ---- HYPOTHESIS A: Simple word reversal ----
    print("\n" + "=" * 70)
    print("HYPOTHESIS A: Simple word reversal (each word reversed char-by-char)")
    print("=" * 70)

    rev_words, a_matches = hypothesis_a(all_words)
    _, a_unique_matches = hypothesis_a(unique_words)
    a_freq = Counter(rev for _, rev in a_matches)

    print(f"Total token matches: {len(a_matches)} / {len(all_words)} ({100*len(a_matches)/len(all_words):.2f}%)")
    print(f"Unique type matches: {len(a_unique_matches)} / {len(unique_words)} ({100*len(a_unique_matches)/len(unique_words):.2f}%)")
    print(f"\nTop 20 Hypothesis A matches (original -> reversed = Italian: count):")
    # Get top by frequency
    a_match_dict = {}
    for orig, rev in a_matches:
        if rev not in a_match_dict:
            a_match_dict[rev] = orig
    for rev, c in sorted(a_freq.items(), key=lambda x: -x[1])[:20]:
        print(f"  {a_match_dict[rev]} -> {rev}: {c}")

    # ---- HYPOTHESIS B: Consonant reversal only ----
    print("\n" + "=" * 70)
    print("HYPOTHESIS B: Reverse consonants only, vowels stay in place")
    print("=" * 70)

    b_words, b_matches = hypothesis_b(all_words)
    _, b_unique_matches = hypothesis_b(unique_words)
    b_freq = Counter(trans for _, trans in b_matches)

    print(f"Total token matches: {len(b_matches)} / {len(all_words)} ({100*len(b_matches)/len(all_words):.2f}%)")
    print(f"Unique type matches: {len(b_unique_matches)} / {len(unique_words)} ({100*len(b_unique_matches)/len(unique_words):.2f}%)")
    print(f"\nTop 20 Hypothesis B matches (original -> transformed = Italian: count):")
    b_match_dict = {}
    for orig, trans in b_matches:
        if trans not in b_match_dict:
            b_match_dict[trans] = orig
    for trans, c in sorted(b_freq.items(), key=lambda x: -x[1])[:20]:
        print(f"  {b_match_dict[trans]} -> {trans}: {c}")

    # ---- HYPOTHESIS C: Boustrophedon ----
    print("\n" + "=" * 70)
    print("HYPOTHESIS C: Boustrophedon (even lines reversed)")
    print("=" * 70)

    c_words, c_matches = hypothesis_c(lines_data)
    c_freq = Counter(trans for _, trans, _, _ in c_matches)
    c_unique_from_even = set()
    c_unique_from_odd = set()
    for orig, trans, loc, direction in c_matches:
        if direction == "even":
            c_unique_from_even.add(trans)
        else:
            c_unique_from_odd.add(trans)

    print(f"Total token matches: {len(c_matches)} / {len(all_words)} ({100*len(c_matches)/len(all_words):.2f}%)")
    print(f"  From even lines (reversed): {sum(1 for _,_,_,d in c_matches if d=='even')}")
    print(f"  From odd lines (as-is): {sum(1 for _,_,_,d in c_matches if d=='odd')}")
    print(f"Unique Italian words from even-line reversals: {len(c_unique_from_even)}")
    print(f"Unique Italian words from odd-line as-is: {len(c_unique_from_odd)}")
    print(f"\nTop 20 Hypothesis C matches:")
    for trans, c in sorted(c_freq.items(), key=lambda x: -x[1])[:20]:
        print(f"  {trans}: {c}")

    # ---- HYPOTHESIS D: Consonant skeleton reversal ----
    print("\n" + "=" * 70)
    print("HYPOTHESIS D: Consonant skeleton extracted, reversed, matched")
    print("=" * 70)

    d_matches = hypothesis_d(all_words)
    d_unique = hypothesis_d(unique_words)
    d_skeleton_freq = Counter((skel, rev_skel) for _, skel, rev_skel, _ in d_matches)

    print(f"Total token matches: {len(d_matches)} / {len(all_words)} ({100*len(d_matches)/len(all_words):.2f}%)")
    print(f"Unique type matches: {len(d_unique)} / {len(unique_words)} ({100*len(d_unique)/len(unique_words):.2f}%)")
    print(f"\nTop 20 Hypothesis D matches (word -> skeleton -> reversed -> Italian):")
    # Group by skeleton
    d_examples = {}
    for w, skel, rev_skel, italian_list in d_matches:
        key = (skel, rev_skel)
        if key not in d_examples:
            d_examples[key] = (w, italian_list)
    for (skel, rev_skel), c in sorted(d_skeleton_freq.items(), key=lambda x: -x[1])[:20]:
        w, italian_list = d_examples[(skel, rev_skel)]
        print(f"  {w} -> [{skel}] -> [{rev_skel}] -> {italian_list[:3]}: {c}")

    # ---- SUMMARY ----
    print("\n" + "=" * 70)
    print("SUMMARY COMPARISON")
    print("=" * 70)

    results = {
        "Baseline (unreversed)": (len(baseline_matches), len(baseline_unique)),
        "Hypothesis A (word reversal)": (len(a_matches), len(a_unique_matches)),
        "Hypothesis B (consonant reversal)": (len(b_matches), len(b_unique_matches)),
        "Hypothesis C (boustrophedon)": (len(c_matches), len(set(t for _,t,_,_ in c_matches))),
        "Hypothesis D (skeleton reversal)": (len(d_matches), len(d_unique)),
    }

    print(f"\n{'Hypothesis':<40} {'Token matches':>15} {'Unique matches':>15}")
    print("-" * 70)
    for name, (tokens, uniques) in results.items():
        print(f"{name:<40} {tokens:>10} ({100*tokens/len(all_words):5.2f}%) {uniques:>8} ({100*uniques/len(unique_words):5.2f}%)")

    # ---- Tim Carter Clausen specific words ----
    print("\n" + "=" * 70)
    print("TIM CARTER CLAUSEN SPECIFIC CLAIMS")
    print("=" * 70)

    tcc_words = {"toro", "olio", "otto", "oro", "olla"}
    print("\nSearching for these words in reversed Voynich text:")
    for target in sorted(tcc_words):
        # What Voynich word would produce this when reversed?
        source = target[::-1]
        count = word_freq.get(source, 0)
        print(f"  '{source}' reversed = '{target}': appears {count} times in corpus")
        # Also check if target itself appears (palindromes)
        if target == source:
            print(f"    (palindrome - same word)")

    # Check "ol" -> "lo" and "al" -> "la" specifically
    print(f"\n  'ol' -> 'lo' (Italian article): {word_freq.get('ol', 0)} occurrences")
    print(f"  'al' -> 'la' (Italian article): {word_freq.get('al', 0)} occurrences")
    print(f"  'or' -> 'ro': {word_freq.get('or', 0)} occurrences")
    print(f"  'ar' -> 'ra': {word_freq.get('ar', 0)} occurrences")
    print(f"  'oro' (palindrome = Italian 'gold'): {word_freq.get('oro', 0)} occurrences")


if __name__ == "__main__":
    main()
