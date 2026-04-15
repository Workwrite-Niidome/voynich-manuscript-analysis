#!/usr/bin/env python3
"""
Co-occurrence analysis of Voynich Manuscript EVA transcription.
Uses decoded anchor words to find obligatory collocations and decode new stems.
"""
import re
import math
from collections import Counter, defaultdict

# Read and parse the EVA transcription
def parse_eva(filepath):
    """Extract words from EVA transcription, ignoring metadata."""
    all_words = []
    lines_of_words = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Skip comments, headers, empty lines
            if not line or line.startswith('#') or line.startswith('<!' ):
                continue
            # Extract the text part after the folio reference
            m = re.match(r'<[^>]+>\s+(.*)', line)
            if not m:
                continue
            text = m.group(1)
            # Remove inline comments and special markers
            text = re.sub(r'<[^>]*>', '', text)
            text = re.sub(r'\{[^}]*\}', '', text)  # Remove {ct} etc
            text = re.sub(r'@\d+;?', '', text)  # Remove @222 markers
            # Split on separators
            words = re.split(r'[.\s,<>\-]+', text)
            words = [w.strip() for w in words if w.strip() and len(w.strip()) > 0]
            all_words.extend(words)
            if words:
                lines_of_words.append(words)
    return all_words, lines_of_words

# Decoded anchors
ANCHORS = {
    'daiin': 'et (and)',
    'aiin': 'in (in)',
    'ol': 'de (of)',
    'chey': 'est (is)',
    'ar': 'ad (to/for)',
    'or': 'cum (with)',
    'dar': 'sed (but)',
    'ckhy': 'calidus (hot)',
    'kchy': 'frigidus (cold)',
    'qokeey': 'drachma',
}

def word_freq(words):
    return Counter(words)

def bigram_freq(words):
    c = Counter()
    for i in range(len(words)-1):
        c[(words[i], words[i+1])] += 1
    return c

def trigram_freq(words):
    c = Counter()
    for i in range(len(words)-2):
        c[(words[i], words[i+1], words[i+2])] += 1
    return c

def window_cooccurrence(words, target, window=3):
    """Find words that appear within `window` positions of `target`."""
    positions = [i for i, w in enumerate(words) if w == target]
    cooc = Counter()
    for pos in positions:
        for offset in range(-window, window+1):
            if offset == 0:
                continue
            idx = pos + offset
            if 0 <= idx < len(words):
                cooc[words[idx]] += 1
    return cooc

def pmi(words, w1, w2, wf, bf, N):
    """Pointwise Mutual Information."""
    joint = bf.get((w1, w2), 0) + bf.get((w2, w1), 0)
    if joint == 0:
        return -999
    p_joint = joint / (N - 1)
    p_w1 = wf[w1] / N
    p_w2 = wf[w2] / N
    if p_w1 == 0 or p_w2 == 0:
        return -999
    return math.log2(p_joint / (p_w1 * p_w2))

def after_word(words, target):
    """Get distribution of words appearing immediately after target."""
    c = Counter()
    for i in range(len(words)-1):
        if words[i] == target:
            c[words[i+1]] += 1
    return c

def before_word(words, target):
    """Get distribution of words appearing immediately before target."""
    c = Counter()
    for i in range(1, len(words)):
        if words[i] == target:
            c[words[i-1]] += 1
    return c

def two_after(words, target):
    """Get word appearing 2 positions after target."""
    c = Counter()
    for i in range(len(words)-2):
        if words[i] == target:
            c[words[i+2]] += 1
    return c

def three_after(words, target):
    """Get word appearing 3 positions after target."""
    c = Counter()
    for i in range(len(words)-3):
        if words[i] == target:
            c[words[i+3]] += 1
    return c

def find_pattern(words, pattern_words):
    """Find sequences matching a pattern (list of words, None = wildcard)."""
    results = []
    plen = len(pattern_words)
    for i in range(len(words) - plen + 1):
        match = True
        for j, pw in enumerate(pattern_words):
            if pw is not None and words[i+j] != pw:
                match = False
                break
        if match:
            results.append(words[i:i+plen])
    return results

def between_words(words, w1, w2, max_gap=5):
    """Find words that appear between w1 and w2."""
    results = []
    for i in range(len(words)):
        if words[i] == w1:
            for j in range(i+1, min(i+max_gap+1, len(words))):
                if words[j] == w2:
                    results.extend(words[i+1:j])
                    break
    return Counter(results)

def main():
    filepath = r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt'
    all_words, lines = parse_eva(filepath)

    N = len(all_words)
    wf = word_freq(all_words)
    bf = bigram_freq(all_words)
    tf = trigram_freq(all_words)

    print(f"Total words: {N}")
    print(f"Unique words: {len(wf)}")
    print(f"\nTop 50 most frequent words:")
    for w, c in wf.most_common(50):
        print(f"  {w}: {c} ({c/N*100:.2f}%)")

    print("\n" + "="*80)
    print("ANALYSIS 1: 'Est calidus/frigidus in gradu [X]'")
    print("Pattern: chey (est) + ckhy/kchy (hot/cold) + ... + aiin (in) + gradu + number")
    print("="*80)

    # What follows ckhy (hot)?
    print("\nWords immediately AFTER ckhy (calidus/hot):")
    after_ckhy = after_word(all_words, 'ckhy')
    for w, c in after_ckhy.most_common(20):
        print(f"  {w}: {c}")

    print("\nWords immediately AFTER kchy (frigidus/cold):")
    after_kchy = after_word(all_words, 'kchy')
    for w, c in after_kchy.most_common(20):
        print(f"  {w}: {c}")

    # What appears 2 positions after ckhy?
    print("\nWords 2 positions AFTER ckhy:")
    two_ckhy = two_after(all_words, 'ckhy')
    for w, c in two_ckhy.most_common(15):
        print(f"  {w}: {c}")

    # Pattern: ckhy + daiin (et) + X  => X = siccus?
    print("\nTrigrams starting with ckhy + daiin:")
    for (a,b,c_), cnt in tf.most_common(5000):
        if a == 'ckhy' and b == 'daiin':
            print(f"  ckhy daiin {c_}: {cnt}")

    print("\nTrigrams starting with kchy + daiin:")
    for (a,b,c_), cnt in tf.most_common(5000):
        if a == 'kchy' and b == 'daiin':
            print(f"  kchy daiin {c_}: {cnt}")

    # chey (est) + ckhy (hot) patterns
    print("\nBigram: chey + ckhy:")
    print(f"  count: {bf.get(('chey','ckhy'), 0)}")
    print("Bigram: chey + kchy:")
    print(f"  count: {bf.get(('chey','kchy'), 0)}")

    # What comes after chey?
    print("\nWords immediately AFTER chey (est):")
    after_chey = after_word(all_words, 'chey')
    for w, c in after_chey.most_common(20):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 2: 'Recipe [X] drachmas [N]'")
    print("Words between p- markers and qokeey (drachma)")
    print("="*80)

    # Find all words starting with 'p' (Recipe markers)
    p_words = [w for w in wf if w.startswith('p') and len(w) > 1]
    print(f"\nAll p- words (potential Recipe markers): {len(p_words)}")
    for w, c in sorted([(w, wf[w]) for w in p_words], key=lambda x: -x[1])[:30]:
        print(f"  {w}: {c}")

    # Words between any p-word and qokeey
    print("\nWords appearing between p- words and qokeey (drachma):")
    p_set = set(p_words)
    ingredient_candidates = Counter()
    for i in range(len(all_words)):
        if all_words[i].startswith('p') and len(all_words[i]) > 1:
            for j in range(i+1, min(i+10, len(all_words))):
                if all_words[j] == 'qokeey' or all_words[j].startswith('qoke'):
                    for k in range(i+1, j):
                        ingredient_candidates[all_words[k]] += 1
                    break
    for w, c in ingredient_candidates.most_common(30):
        print(f"  {w}: {c}")

    # What comes immediately before qokeey?
    print("\nWords immediately BEFORE qokeey:")
    before_qokeey = before_word(all_words, 'qokeey')
    for w, c in before_qokeey.most_common(20):
        print(f"  {w}: {c}")

    # What comes immediately after qokeey?
    print("\nWords immediately AFTER qokeey:")
    after_qokeey = after_word(all_words, 'qokeey')
    for w, c in after_qokeey.most_common(20):
        print(f"  {w}: {c}")

    # All qoke- words (drachma variants?)
    qoke_words = [w for w in wf if w.startswith('qoke')]
    print(f"\nAll qoke- words (drachma-related): {len(qoke_words)}")
    for w in sorted(qoke_words, key=lambda x: -wf[x]):
        print(f"  {w}: {wf[w]}")

    print("\n" + "="*80)
    print("ANALYSIS 3: After chol (hic/this)")
    print("="*80)

    print("\nWords immediately AFTER chol:")
    after_chol = after_word(all_words, 'chol')
    for w, c in after_chol.most_common(25):
        print(f"  {w}: {c}")

    print("\nWords immediately BEFORE chol:")
    before_chol = before_word(all_words, 'chol')
    for w, c in before_chol.most_common(25):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 4: Quality pairs - ckhy + daiin + [WORD]")
    print("Expected: 'calidus et siccus' or 'frigidus et humidus'")
    print("="*80)

    # Find ckhy...daiin...X patterns
    for i in range(len(all_words)-2):
        if all_words[i] == 'ckhy' and all_words[i+1] == 'daiin':
            context = all_words[max(0,i-2):min(len(all_words),i+5)]
            print(f"  Context: {' '.join(context)}")

    print("\nkchy...daiin...X patterns:")
    for i in range(len(all_words)-2):
        if all_words[i] == 'kchy' and all_words[i+1] == 'daiin':
            context = all_words[max(0,i-2):min(len(all_words),i+5)]
            print(f"  Context: {' '.join(context)}")

    # Also check ckhy + X + daiin (if "in gradu" intervenes)
    print("\nckhy window co-occurrence (3):")
    ckhy_cooc = window_cooccurrence(all_words, 'ckhy', 3)
    for w, c in ckhy_cooc.most_common(20):
        print(f"  {w}: {c}")

    print("\nkchy window co-occurrence (3):")
    kchy_cooc = window_cooccurrence(all_words, 'kchy', 3)
    for w, c in kchy_cooc.most_common(20):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 5: After ar (ad = for/to) - disease names")
    print("="*80)

    print("\nWords immediately AFTER ar (ad):")
    after_ar = after_word(all_words, 'ar')
    for w, c in after_ar.most_common(25):
        print(f"  {w}: {c}")

    print("\nWords 2 positions AFTER ar:")
    two_ar = two_after(all_words, 'ar')
    for w, c in two_ar.most_common(20):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 6: After dar (sed/but or da/give) - verbs")
    print("="*80)

    print("\nWords immediately AFTER dar:")
    after_dar = after_word(all_words, 'dar')
    for w, c in after_dar.most_common(25):
        print(f"  {w}: {c}")

    print("\nWords immediately BEFORE dar:")
    before_dar = before_word(all_words, 'dar')
    for w, c in before_dar.most_common(25):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 7: PMI for all anchor words")
    print("="*80)

    anchors = ['daiin', 'aiin', 'ol', 'chey', 'ar', 'or', 'dar', 'ckhy', 'kchy', 'qokeey']

    # Get top-100 words for PMI calculation
    top_words = [w for w, _ in wf.most_common(200)]

    for anchor in anchors:
        print(f"\nHighest PMI with '{anchor}' ({ANCHORS[anchor]}):")
        pmis = []
        for w in top_words:
            if w == anchor:
                continue
            p = pmi(all_words, anchor, w, wf, bf, N)
            if p > -900:
                pmis.append((w, p))
        pmis.sort(key=lambda x: -x[1])
        for w, p in pmis[:15]:
            joint = bf.get((anchor, w), 0) + bf.get((w, anchor), 0)
            print(f"  {w}: PMI={p:.2f} (joint={joint}, freq={wf[w]})")

    print("\n" + "="*80)
    print("ANALYSIS 8: shol (often appears) - potential 'folium/herba'")
    print("="*80)

    print("\nWords immediately AFTER shol:")
    after_shol = after_word(all_words, 'shol')
    for w, c in after_shol.most_common(20):
        print(f"  {w}: {c}")

    print("\nWords immediately BEFORE shol:")
    before_shol = before_word(all_words, 'shol')
    for w, c in before_shol.most_common(20):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 9: chor - frequent word analysis")
    print("="*80)

    print("\nWords immediately AFTER chor:")
    after_chor = after_word(all_words, 'chor')
    for w, c in after_chor.most_common(20):
        print(f"  {w}: {c}")

    print("\nWords immediately BEFORE chor:")
    before_chor = before_word(all_words, 'chor')
    for w, c in before_chor.most_common(20):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 10: qo- prefix words (potential measurement/quantity)")
    print("="*80)

    qo_words = [w for w in wf if w.startswith('qo')]
    print(f"All qo- words: {len(qo_words)}")
    for w in sorted(qo_words, key=lambda x: -wf[x])[:30]:
        print(f"  {w}: {wf[w]}")

    print("\n" + "="*80)
    print("ANALYSIS 11: sho - very frequent word")
    print("="*80)

    print(f"\nsho frequency: {wf.get('sho', 0)}")
    print("\nWords immediately AFTER sho:")
    after_sho = after_word(all_words, 'sho')
    for w, c in after_sho.most_common(20):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 12: ot- prefix words (potential demonstrative/article)")
    print("="*80)

    ot_words = [w for w in wf if w.startswith('ot') and len(w) > 2]
    print(f"All ot- words: {len(ot_words)}")
    for w in sorted(ot_words, key=lambda x: -wf[x])[:20]:
        print(f"  {w}: {wf[w]}")

    print("\n" + "="*80)
    print("ANALYSIS 13: cthy - frequent word after anchors")
    print("="*80)

    print(f"\ncthy frequency: {wf.get('cthy', 0)}")
    print("\nWords immediately BEFORE cthy:")
    before_cthy = before_word(all_words, 'cthy')
    for w, c in before_cthy.most_common(20):
        print(f"  {w}: {c}")

    print("\nWords immediately AFTER cthy:")
    after_cthy = after_word(all_words, 'cthy')
    for w, c in after_cthy.most_common(20):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 14: dain vs daiin distinction")
    print("="*80)

    print(f"\ndain frequency: {wf.get('dain', 0)}")
    print(f"daiin frequency: {wf.get('daiin', 0)}")

    print("\nWords immediately AFTER dain:")
    after_dain = after_word(all_words, 'dain')
    for w, c in after_dain.most_common(15):
        print(f"  {w}: {c}")

    print("\nWords immediately BEFORE dain:")
    before_dain = before_word(all_words, 'dain')
    for w, c in before_dain.most_common(15):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 15: dal - another common word")
    print("="*80)

    print(f"\ndal frequency: {wf.get('dal', 0)}")
    print("\nWords AFTER dal:")
    after_dal = after_word(all_words, 'dal')
    for w, c in after_dal.most_common(15):
        print(f"  {w}: {c}")
    print("\nWords BEFORE dal:")
    before_dal = before_word(all_words, 'dal')
    for w, c in before_dal.most_common(15):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 16: Folio-section specific patterns (pharmaceutical pages)")
    print("Look at f88r-f116v which are traditionally 'pharmaceutical' pages")
    print("="*80)

    # Extract words from pharma folios
    pharma_words = []
    in_pharma = False
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # Check folio markers
            folio_match = re.match(r'<(f\d+[rv])', line)
            if folio_match:
                folio = folio_match.group(1)
                fnum = int(re.match(r'f(\d+)', folio).group(1))
                in_pharma = (88 <= fnum <= 116)
            if not in_pharma:
                continue
            m = re.match(r'<[^>]+>\s+(.*)', line)
            if not m:
                continue
            text = m.group(1)
            text = re.sub(r'<[^>]*>', '', text)
            text = re.sub(r'\{[^}]*\}', '', text)
            text = re.sub(r'@\d+;?', '', text)
            words = re.split(r'[.\s,<>\-]+', text)
            words = [w.strip() for w in words if w.strip()]
            pharma_words.extend(words)

    if pharma_words:
        pharma_wf = word_freq(pharma_words)
        print(f"\nPharma section words: {len(pharma_words)}, unique: {len(pharma_wf)}")
        print("\nTop 30 words in pharma section:")
        for w, c in pharma_wf.most_common(30):
            print(f"  {w}: {c}")

        # qokeey in pharma
        print(f"\nqokeey in pharma: {pharma_wf.get('qokeey', 0)}")
        print(f"qokeey total: {wf.get('qokeey', 0)}")

        # p- words in pharma
        pharma_p = [w for w in pharma_wf if w.startswith('p')]
        print(f"\np- words in pharma section:")
        for w in sorted(pharma_p, key=lambda x: -pharma_wf[x])[:20]:
            print(f"  {w}: {pharma_wf[w]}")
    else:
        print("\nNo pharma section words found in expected folio range.")
        # Try broader search
        print("Searching for qokeey context across all folios...")

    # Find all contexts around qokeey
    print("\n\nAll qokeey contexts (5 words before and after):")
    for i, w in enumerate(all_words):
        if w == 'qokeey':
            start = max(0, i-5)
            end = min(len(all_words), i+6)
            context = all_words[start:end]
            print(f"  [{i}]: {' '.join(context)}")

    print("\n" + "="*80)
    print("ANALYSIS 17: ol (de/of) - genitive marker analysis")
    print("="*80)

    print(f"\nol frequency: {wf.get('ol', 0)}")
    print("\nWords immediately AFTER ol:")
    after_ol = after_word(all_words, 'ol')
    for w, c in after_ol.most_common(20):
        print(f"  {w}: {c}")
    print("\nWords immediately BEFORE ol:")
    before_ol = before_word(all_words, 'ol')
    for w, c in before_ol.most_common(20):
        print(f"  {w}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 18: or (cum/with) usage patterns")
    print("="*80)

    print(f"\nor frequency: {wf.get('or', 0)}")
    print("\nWords immediately AFTER or:")
    after_or = after_word(all_words, 'or')
    for w, c in after_or.most_common(20):
        print(f"  {w}: {c}")
    print("\nWords immediately BEFORE or:")
    before_or = before_word(all_words, 'or')
    for w, c in before_or.most_common(20):
        print(f"  {w}: {c}")

    # Pattern: X or Y (X with Y)
    print("\nX or Y patterns (most common):")
    xory = Counter()
    for i in range(1, len(all_words)-1):
        if all_words[i] == 'or':
            xory[(all_words[i-1], all_words[i+1])] += 1
    for (x,y), c in xory.most_common(20):
        print(f"  {x} or {y}: {c}")

    print("\n" + "="*80)
    print("ANALYSIS 19: Suffix analysis for morphological patterns")
    print("="*80)

    # Group words by suffix
    suffix_groups = defaultdict(list)
    for w in wf:
        if len(w) >= 3:
            suffix_groups[w[-3:]].append(w)

    print("\nMost productive 3-char suffixes:")
    for suffix, words_list in sorted(suffix_groups.items(), key=lambda x: -len(x[1]))[:15]:
        total_freq = sum(wf[w] for w in words_list)
        print(f"  -{suffix}: {len(words_list)} types, {total_freq} tokens")
        for w in sorted(words_list, key=lambda x: -wf[x])[:5]:
            print(f"    {w}: {wf[w]}")

    print("\n" + "="*80)
    print("ANALYSIS 20: Lines containing ckhy or kchy (quality descriptions)")
    print("="*80)

    for line_words in lines:
        line_str = ' '.join(line_words)
        if 'ckhy' in line_words or 'kchy' in line_words:
            print(f"  {line_str}")

if __name__ == '__main__':
    main()
