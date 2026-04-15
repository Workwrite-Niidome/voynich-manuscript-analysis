"""Attack the Latin hypothesis - comprehensive analysis."""
import re, math
from collections import Counter

def extract_words(filepath):
    words = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            m = re.search(r'>\s*(.*)', line)
            text = m.group(1) if m else line
            text = re.sub(r'<[^>]*>', '', text)
            text = re.sub(r'<%>', '', text)
            text = re.sub(r'<\$>', '', text)
            text = re.sub(r'@\d+;', '', text)
            text = re.sub(r'\{[^}]*\}', '', text)
            text = re.sub(r'[!?,<>\-]', '', text)
            for w in text.split('.'):
                w = re.sub(r'[^a-zA-Z]', '', w.strip()).lower()
                if w:
                    words.append(w)
    return words

words = extract_words('C:/Users/kazuk/Downloads/voynich_analysis/IT2a-n.txt')
total = len(words)
freq = Counter(words)
print(f"Total words: {total}, Unique: {len(freq)}")

# ATTACK 1: -y problem
print("\n" + "="*60)
print("ATTACK 1: THE -y PROBLEM")
print("="*60)
finals = Counter(w[-1] for w in words)
for ch, c in finals.most_common(15):
    print(f"  -{ch}: {c:5d} ({c/total*100:5.1f}%)")
y_pct = finals.get('y',0)/total*100
print(f"\n-y rate: {y_pct:.1f}%")
print(f"Max Latin final (-s): ~20%")
print(f"RATIO: {y_pct/20:.1f}x the max Latin final letter")

# ATTACK 2: Word length
print("\n" + "="*60)
print("ATTACK 2: WORD LENGTH")
print("="*60)
lens = [len(w) for w in words]
avg = sum(lens)/len(lens)
print(f"Voynich mean word length (EVA chars): {avg:.2f}")
# Collapse digraphs
def collapse(w):
    for d in ['cth','ckh','cph','cfh','ch','sh','th','ph']:
        w = w.replace(d, 'X')
    return w
clens = [len(collapse(w)) for w in words]
cavg = sum(clens)/len(clens)
print(f"After digraph collapse: {cavg:.2f}")
print(f"Latin pharma avg: ~5.5-6.5")
ldist = Counter(lens)
print("\nLength distribution:")
for l in range(1, 13):
    c = ldist.get(l, 0)
    print(f"  {l:2d}: {c:5d} ({c/total*100:5.1f}%) {'#'*int(c/total*200)}")

# ATTACK 3: Consonant-final without y
print("\n" + "="*60)
print("ATTACK 3: CONSONANT-FINAL WITHOUT 'y'")
print("="*60)
vowels = set('aeiou')
cons_all = sum(1 for w in words if w[-1] not in vowels)
print(f"Consonant-final (all): {cons_all/total*100:.1f}%")

non_y = [w for w in words if w[-1] != 'y']
if non_y:
    cons_no_y = sum(1 for w in non_y if w[-1] not in vowels)
    vow_no_y = sum(1 for w in non_y if w[-1] in vowels)
    print(f"Words not ending in y: {len(non_y)}")
    print(f"Consonant-final (no y): {cons_no_y/len(non_y)*100:.1f}%")
    print(f"Vowel-final (no y):     {vow_no_y/len(non_y)*100:.1f}%")
    nf = Counter(w[-1] for w in non_y)
    print("\nFinal chars (excluding y-words):")
    for ch, c in nf.most_common(10):
        t = "V" if ch in vowels else "C"
        print(f"  -{ch} [{t}]: {c:5d} ({c/len(non_y)*100:5.1f}%)")

# ATTACK 4: Function word ratio
print("\n" + "="*60)
print("ATTACK 4: FUNCTION WORD RATIO")
print("="*60)
fw_orig = {'or','ol','ar','al','s','y','r','o','l','d','e'}
fw_strict = {'or','ol','ar','al'}
orig_c = sum(1 for w in words if w in fw_orig)
strict_c = sum(1 for w in words if w in fw_strict)
print(f"Original set {fw_orig}:")
print(f"  {orig_c}/{total} = {orig_c/total*100:.1f}%")
print(f"Strict set {fw_strict}:")
print(f"  {strict_c}/{total} = {strict_c/total*100:.1f}%")
print("\nSingle-char breakdown:")
for s in ['s','y','r','o','l','d','e']:
    print(f"  '{s}': {freq.get(s,0)}")
print(f"\nLatin fw ratio: ~25-35%")
print(f"Italian fw ratio: ~18-22%")

# ATTACK 5: Zipf significance
print("\n" + "="*60)
print("ATTACK 5: ZIPF CORRELATION SIGNIFICANCE")
print("="*60)
r_lat, r_ita, r_occ = 0.9923, 0.9919, 0.9915
def fz(r): return 0.5*math.log((1+r)/(1-r))
zl, zi = fz(r_lat), fz(r_ita)
for n in [10, 15, 20, 30, 50]:
    se = math.sqrt(2.0/(n-3))
    z = abs(zl-zi)/se
    # manual p-value approximation
    # P(Z>z) using approximation
    from math import erfc, sqrt
    p = erfc(z/sqrt(2))
    sig = "SIG" if p < 0.05 else "NOT SIG"
    print(f"  n={n:2d}: z-test={z:.4f}, p={p:.4f} [{sig}]")
print(f"\nDifference r(Latin)-r(Italian) = {r_lat-r_ita:.4f}")
print("All p-values >> 0.05: difference is NOT significant")
