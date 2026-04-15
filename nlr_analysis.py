#!/usr/bin/env python3
import re, math, random
from collections import Counter, defaultdict

INPUT = "C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt"
OUTPUT = "C:/Users/kazuk/Downloads/voynich_analysis/nlr_information_test.md"

SECTIONS = {
    "herbal_a": list(range(1, 58)),
    "astronomical": list(range(67, 74)),
    "biological": list(range(75, 85)),
    "recipe": list(range(88, 117)),
}

def parse_eva(fp):
    words_all, page_words = [], defaultdict(list)
    with open(fp, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            m = re.match(r"^<f(\d+)[rv]\d?\.\d+[^>]*>\s+(.*)", line)
            if not m: continue
            fnum = int(m.group(1))
            text = m.group(2)
            text = re.sub(r"@\d+;?", "", text)
            text = re.sub(r"\{[^}]*\}", "", text)
            text = re.sub(r"<->", " ", text)
            text = re.sub(r"[,?!]", "", text)
            for tok in text.split("."):
                tok = tok.strip().replace('"''', '"''')
                if tok and re.match(r"^[a-z]+$", tok):
                    words_all.append((fnum, tok))
                    page_words[fnum].append(tok)
    return words_all, page_words

def get_section(fnum):
    for name, folios in SECTIONS.items():
        if fnum in folios: return name
    return "other"

def entropy(seq):
    if not seq: return 0.0
    c = Counter(seq); t = len(seq)
    return -sum((v/t)*math.log2(v/t) for v in c.values() if v > 0)

def cond_entropy(seq, k):
    if len(seq) <= k: return 0.0
    ctx = defaultdict(Counter)
    for i in range(k, len(seq)):
        ctx[tuple(seq[i-k:i])][seq[i]] += 1
    t = len(seq) - k; h = 0.0
    for cc in ctx.values():
        ct = sum(cc.values())
        for v in cc.values():
            p = v / ct
            if p > 0: h -= (ct / t) * p * math.log2(p)
    return h

def calc_mi(x, y):
    n = len(x)
    if n == 0: return 0.0
    xy = Counter(zip(x, y)); xc = Counter(x); yc = Counter(y)
    mi = 0.0
    for (a, b), c in xy.items():
        pxy = c / n; px = xc[a] / n; py = yc[b] / n
        if pxy > 0 and px > 0 and py > 0:
            mi += pxy * math.log2(pxy / (px * py))
    return mi

def pearson(x, y):
    n = len(x)
    if n < 3: return 0
    mx = sum(x) / n; my = sum(y) / n
    sx = math.sqrt(sum((i - mx)**2 for i in x) / n)
    sy = math.sqrt(sum((i - my)**2 for i in y) / n)
    if sx == 0 or sy == 0: return 0
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (n * sx * sy)

def main():
    words_all, page_words = parse_eva(INPUT)
    print(f"Total words: {len(words_all)}")
    nlr_seq, nlr_stem, nlr_folio = [], [], []
    nlr_pages = defaultdict(list)
    for fnum, w in words_all:
        if len(w) >= 2 and w[-1] in "nlr":
            s = w[-1]
            nlr_seq.append(s)
            nlr_stem.append((w[:-1], s))
            nlr_folio.append((fnum, s))
            nlr_pages[fnum].append(s)
    tw = len(words_all); nw = len(nlr_seq)
    ratio = nw / tw if tw else 0
    sc = Counter(nlr_seq)
    maxH = math.log2(3)
    print(f"n/l/r words: {nw} ({ratio:.1%}), dist: {dict(sc)}")
    # 1. Entropy
    h0 = entropy(nlr_seq)
    ck = {k: cond_entropy(nlr_seq, k) for k in range(1, 6)}
    random.seed(42)
    rseq = [random.choice(["n", "l", "r"]) for _ in range(nw)]
    rh0 = entropy(rseq); rck = {k: cond_entropy(rseq, k) for k in range(1, 6)}
    random.seed(42)
    tran = {"n": [("n",0.5),("l",0.3),("r",0.2)], "l": [("n",0.4),("l",0.2),("r",0.4)], "r": [("n",0.45),("l",0.35),("r",0.2)]}
    ns = [random.choice(["n", "l", "r"])]
    for _ in range(nw - 1):
        r = random.random(); cu = 0
        for sym, prob in tran[ns[-1]]:
            cu += prob
            if r < cu: ns.append(sym); break
    nh0 = entropy(ns); nck = {k: cond_entropy(ns, k) for k in range(1, 6)}
    # 2. MI
    stems = [s for s, _ in nlr_stem]
    suffs = [s for _, s in nlr_stem]
    mi = calc_mi(stems, suffs)
    hs = entropy(suffs); hst = entropy(stems)
    nmi = mi / min(hs, hst) if min(hs, hst) > 0 else 0
    sd = defaultdict(Counter)
    for st, sf in nlr_stem: sd[st][sf] += 1
    biased = []
    for st, cc in sd.items():
        t = sum(cc.values())
        if t >= 10: biased.append((st, t, dict(cc), max(cc.values()) / t))
    biased.sort(key=lambda x: -x[3])
    # 3. Section
    ss = defaultdict(list)
    for fn, sf in nlr_folio: ss[get_section(fn)].append(sf)
    sect_stats = {}
    for sec, sq in ss.items():
        if len(sq) < 20: continue
        sect_stats[sec] = {"count": len(sq), "dist": dict(Counter(sq)), "H0": entropy(sq), "H1": cond_entropy(sq, 1), "H2": cond_entropy(sq, 2)}
    # 4. Capacity
    eff = ck[2]
    pcap = []
    for fn in sorted(nlr_pages):
        sq = nlr_pages[fn]; n = len(sq)
        pcap.append((fn, n, n * maxH, n * eff))
    avgsym = sum(x[1] for x in pcap) / len(pcap) if pcap else 0
    avgbit = sum(x[3] for x in pcap) / len(pcap) if pcap else 0
    # 5. Numeric
    vm = {"n": 0, "l": 1, "r": 2}
    numseq = [vm[s] for s in nlr_seq]
    ac = {}
    for lag in [1, 2, 3, 5, 10]:
        if len(numseq) > lag:
            ac[lag] = sum(1 for i in range(len(numseq) - lag) if numseq[i] == numseq[i + lag]) / (len(numseq) - lag)
    inc = sum(1 for i in range(len(numseq) - 1) if numseq[i + 1] > numseq[i])
    dec = sum(1 for i in range(len(numseq) - 1) if numseq[i + 1] < numseq[i])
    eq = sum(1 for i in range(len(numseq) - 1) if numseq[i + 1] == numseq[i])
    pnc, pav = [], []
    for fn in sorted(nlr_pages):
        sq = nlr_pages[fn]
        if len(sq) >= 3: pnc.append(fn); pav.append(sum(vm[s] for s in sq) / len(sq))
    pcorr = pearson(pnc, pav)
    trip = []
    for i in range(0, len(nlr_seq) - 2, 3):
        trip.append(vm[nlr_seq[i]] * 9 + vm[nlr_seq[i + 1]] * 3 + vm[nlr_seq[i + 2]])
    tdist = Counter(trip)
    te = entropy(trip); mte = math.log2(27)
    pmono = {}
    for fn in sorted(nlr_pages):
        sq = nlr_pages[fn]
        if len(sq) < 10: continue
        nums = [vm[s] for s in sq]
        pmono[fn] = sum(nums[-5:]) / 5 - sum(nums[:5]) / 5
    # Build report
    build_report(tw, nw, ratio, sc, maxH, h0, ck, rh0, rck, nh0, nck, mi, hs, hst, nmi, biased, sect_stats, eff, avgsym, avgbit, ac, inc, dec, eq, pcorr, trip, tdist, te, mte, pmono)

def build_report(tw, nw, ratio, sc, maxH, h0, ck, rh0, rck, nh0, nck, mi, hs, hst, nmi, biased, sect_stats, eff, avgsym, avgbit, ac, inc, dec, eq, pcorr, trip, tdist, te, mte, pmono):
    R = []
    def a(s=""): R.append(s)
    d1 = h0 - ck[1]; d5 = h0 - ck[5]
    rd1 = rh0 - rck[1]; nd1 = nh0 - nck[1]
    a("# Voynich Manuscript n/l/r Suffix Information Analysis")
    a()
    a("## Overview")
    a()
    a(f"- **Total words parsed**: {tw}")
    a(f"- **Words ending in n/l/r**: {nw} ({ratio:.1%} of all words)")
    a(f"- **Suffix distribution**: n={sc.get('n',0)} ({sc.get('n',0)/nw:.1%}), l={sc.get('l',0)} ({sc.get('l',0)/nw:.1%}), r={sc.get('r',0)} ({sc.get('r',0)/nw:.1%})")
    a()
    a("---")
    a("## 1. Dual-Channel Hypothesis: Entropy Analysis")
    a()
    a("If the n/l/r suffix sequence carries its own independent message, its entropy")
    a("should decay with context order like natural language (not like random data).")
    a()
    a(f"- **Maximum entropy (uniform ternary)**: {maxH:.4f} bits/symbol")
    a(f"- **H(0) unigram entropy of n/l/r sequence**: {h0:.4f} bits/symbol")
    a()
    a("### Conditional Entropy Decay")
    a()
    a("| Order k | Voynich n/l/r | Random Ternary | NL-like Markov |")
    a("|---------|---------------|----------------|----------------|")
    a(f"| 0 (H0)  | {h0:.4f}        | {rh0:.4f}          | {nh0:.4f}          |")
    for k in range(1, 6):
        a(f"| {k}       | {ck[k]:.4f}        | {rck[k]:.4f}          | {nck[k]:.4f}          |")
    a()
    a("### Entropy Drop Summary")
    a()
    a(f"- **Voynich n/l/r drop H0->H1**: {d1:.4f} bits ({d1/h0*100:.1f}% reduction)")
    a(f"- **Voynich n/l/r drop H0->H5**: {d5:.4f} bits ({d5/h0*100:.1f}% reduction)")
    a(f"- **Random ternary drop H0->H1**: {rd1:.4f} bits")
    a(f"- **NL-like Markov drop H0->H1**: {nd1:.4f} bits")
    a()
    if d1 > 0.05:
        a("**Finding**: The n/l/r sequence shows significant entropy reduction with context,")
        a("indicating sequential structure (not random). Consistent with structured information.")
    else:
        a("**Finding**: The n/l/r sequence shows minimal entropy reduction, near-random.")
        a("This weakens the dual-channel hypothesis.")
    a()
    a("---")
    a("## 2. Mutual Information: Stem vs. Suffix")
    a()
    a(f"- **MI(stem, suffix)**: {mi:.4f} bits")
    a(f"- **H(suffix)**: {hs:.4f} bits")
    a(f"- **H(stem)**: {hst:.4f} bits")
    a(f"- **Normalized MI**: {nmi:.4f}")
    a()
    if nmi < 0.1:
        a("**Finding**: Very low NMI -- suffix is largely **independent** of stem.")
        a("Supports dual-channel: suffix not determined by word identity.")
    elif nmi < 0.3:
        a("**Finding**: Moderate NMI -- partial dependence between stem and suffix.")
        a("Suffix has some stem-related info but also independent component.")
    else:
        a("**Finding**: High NMI -- strong dependence. Against independent channel.")
    a()
    a("### Top 15 Stems by Suffix Bias (freq >= 10)")
    a()
    a("| Stem | Total | n | l | r | Dominant % |")
    a("|------|-------|---|---|---|------------|")
    for st, t, cc, mp in biased[:15]:
        a(f"| {st} | {t} | {cc.get('n',0)} | {cc.get('l',0)} | {cc.get('r',0)} | {mp:.0%} |")
    a()
    if biased:
        ab = sum(x[3] for x in biased) / len(biased)
        a(f"- **Average dominant suffix % across frequent stems**: {ab:.0%}")
        a("  (expected for random: 33%, for fully determined: 100%)")
    a()
    a("---")
    a("## 3. Section-Dependent Entropy Rates")
    a()
    a("| Section | Count | n% | l% | r% | H(0) | H(1) | H(2) | Drop H0->H1 |")
    a("|---------|-------|----|----|----|------|------|------|-------------|")
    for sec in ["herbal_a", "astronomical", "biological", "recipe", "other"]:
        if sec in sect_stats:
            s = sect_stats[sec]; d = s["dist"]; t = s["count"]
            a(f"| {sec} | {t} | {d.get('n',0)/t*100:.0f}% | {d.get('l',0)/t*100:.0f}% | {d.get('r',0)/t*100:.0f}% | {s['H0']:.3f} | {s['H1']:.3f} | {s['H2']:.3f} | {s['H0']-s['H1']:.3f} |")
    a()
    if len(sect_stats) >= 2:
        h1v = [s["H1"] for s in sect_stats.values()]
        h0v = [s["H0"] for s in sect_stats.values()]
        h1r = max(h1v) - min(h1v)
        a(f"- **Range of H(0) across sections**: {max(h0v)-min(h0v):.3f} bits")
        a(f"- **Range of H(1) across sections**: {h1r:.3f} bits")
        if h1r > 0.1:
            a("- **Finding**: Entropy rates differ notably across sections.")
            a("  n/l/r may encode different info per section.")
        else:
            a("- **Finding**: Entropy rates similar across sections (uniform behavior).")
    a()
    a("---")
    a("## 4. Ternary Encoding Capacity")
    a()
    a(f"- **Raw capacity (uniform ternary)**: {maxH:.4f} bits/symbol")
    a(f"- **Effective capacity H(X|X_i-1,X_i-2)**: {eff:.4f} bits/symbol")
    a(f"- **Efficiency**: {eff/maxH*100:.1f}%")
    a()
    a(f"- **Average n/l/r symbols per page**: {avgsym:.1f}")
    a(f"- **Average effective bits per page**: {avgbit:.1f}")
    a(f"- **Total n/l/r symbols**: {nw}")
    a(f"- **Total effective bits in manuscript**: {nw*eff:.0f}")
    a()
    ec = nw * eff / 5
    a(f"- **Equivalent English characters (~5 bits/char)**: ~{ec:.0f}")
    a(f"- **Equivalent English words (~25 bits/word)**: ~{nw*eff/25:.0f}")
    a()
    a("---")
    a("## 5. Numeric / Base-3 Encoding Test")
    a()
    a("### 5a. Autocorrelation (mapping n=0, l=1, r=2)")
    a()
    a("| Lag | Match Rate | Expected (random) |")
    a("|-----|------------|-------------------|")
    for lag in sorted(ac):
        a(f"| {lag} | {ac[lag]:.4f} | 0.3333 |")
    a()
    a(f"- Consecutive increases: {inc}")
    a(f"- Consecutive decreases: {dec}")
    a(f"- Consecutive equals: {eq}")
    a(f"- Inc/Dec ratio: {inc/(dec or 1):.3f} (expected ~1.0)")
    a()
    a("### 5b. Correlation with Page Number")
    a()
    a(f"- **Pearson r(page_number, avg_suffix_value)**: {pcorr:.4f}")
    if abs(pcorr) < 0.1:
        a("- **Finding**: No correlation between suffix values and page position.")
    else:
        a(f"- **Finding**: Correlation detected (r={pcorr:.3f}).")
    a()
    a("### 5c. Triplet Decoding (base-3, 0..26)")
    a()
    a(f"- **Total triplets**: {len(trip)}")
    a(f"- **Triplet entropy**: {te:.3f} bits (max {mte:.3f})")
    a(f"- **Entropy efficiency**: {te/mte*100:.1f}%")
    a()
    inar = sum(1 for v in trip if v < 26)
    a(f"- Values in 0-25 (alphabet range): {inar}/{len(trip)} ({inar/len(trip)*100:.0f}%)")
    a()
    a("Top 10 triplet values:")
    a()
    a("| Value | Count | If A=0 |")
    a("|-------|-------|--------|")
    for v, c in tdist.most_common(10):
        a(f"| {v} | {c} | {chr(65+v) if v<26 else '-'} |")
    a()
    a("### 5d. Within-Page Monotonic Trends")
    a()
    if pmono:
        tv = list(pmono.values())
        ps = sum(1 for t in tv if t > 0.3)
        ng = sum(1 for t in tv if t < -0.3)
        nt = len(tv) - ps - ng
        a(f"- Pages with upward trend: {ps}")
        a(f"- Pages with downward trend: {ng}")
        a(f"- Pages with no clear trend: {nt}")
        if abs(ps - ng) < len(tv) * 0.2:
            a("- **Finding**: No systematic monotonic trends within pages.")
        else:
            a("- **Finding**: Asymmetric monotonic trends detected.")
    a()
    a("---")
    a("## Synthesis and Conclusions")
    a()
    scores = {}
    if d1 > 0.05:
        scores["entropy"] = True
        a(f"1. **Entropy structure**: POSITIVE -- H0->H1 drop = {d1:.4f} bits ({d1/h0*100:.1f}% reduction).")
        a("   Sequential dependencies exist, consistent with structured information.")
    else:
        scores["entropy"] = False
        a("1. **Entropy structure**: NEGATIVE -- near-random sequence.")
    a()
    if nmi < 0.15:
        scores["independence"] = True
        a(f"2. **Independence from stem**: POSITIVE -- NMI = {nmi:.4f}.")
        a("   Suffix largely independent of word identity.")
    else:
        scores["independence"] = False
        a(f"2. **Independence from stem**: NEGATIVE -- NMI = {nmi:.4f}.")
    a()
    if len(sect_stats) >= 2:
        h1v2 = [s["H1"] for s in sect_stats.values()]
        h1r2 = max(h1v2) - min(h1v2)
        if h1r2 > 0.1:
            scores["section"] = True
            a(f"3. **Section variation**: POSITIVE -- H(1) range = {h1r2:.3f} bits.")
        else:
            scores["section"] = False
            a(f"3. **Section variation**: NEGATIVE -- H(1) range = {h1r2:.3f} bits (uniform).")
    a()
    macd = max(abs(r - 1/3) for r in ac.values())
    if macd < 0.05 and abs(pcorr) < 0.1:
        scores["numeric"] = False
        a("4. **Numeric encoding**: NEGATIVE -- no base-3 patterns, no page correlation.")
    else:
        scores["numeric"] = True
        a(f"4. **Numeric encoding**: POSITIVE -- autocorrelation deviation {macd:.4f}, page r={pcorr:.4f}.")
    a()
    sup = sum(1 for v in scores.values() if v)
    a(f"### Overall Assessment ({sup}/{len(scores)} tests support dual-channel)")
    a()
    if sup >= 3:
        a("**Strong support for the dual-channel hypothesis.** The n/l/r suffixes carry")
        a("independent, structured information not determined by the word stem.")
        a(f"Effective capacity: ~{eff:.2f} bits/symbol, ~{nw*eff:.0f} total bits")
        ec = nw * eff / 5
        a(f"(~{ec:.0f} English characters equivalent).")
    elif sup >= 2:
        a("**Moderate support for the dual-channel hypothesis.** Some evidence of")
        a("partially independent information in n/l/r suffixes, but not conclusive.")
        a("The structure may reflect phonotactic/morphological constraints rather")
        a("than a separate encoded message.")
    else:
        a("**Weak or no support for the dual-channel hypothesis.** The n/l/r suffixes")
        a("do not appear to function as an independent information channel.")
    a()
    with open(OUTPUT, "w", encoding="utf-8") as fout:
        fout.write(chr(10).join(R))
    print(f"Report written to: {OUTPUT}")
    print(f"H(0)={h0:.4f} H(1)={ck[1]:.4f} H(2)={ck[2]:.4f} drop={d1:.4f}")
    print(f"MI={mi:.4f} NMI={nmi:.4f} eff={eff:.4f} pcorr={pcorr:.4f}")

if __name__ == "__main__":
    main()
