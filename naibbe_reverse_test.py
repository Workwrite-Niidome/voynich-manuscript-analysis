#!/usr/bin/env python3
"""
Reverse Naibbe cipher test on Voynich f1r.
Attempt to decode actual EVA text using Greshko's substitution tables.
"""

import re
from collections import defaultdict

# Complete Naibbe tables extracted from github.com/greshko/naibbe-cipher
TABLES_RAW = """unigram_alpha_a,ol
unigram_alpha_b,qokchdy
unigram_alpha_c,chey
unigram_alpha_d,cheey
unigram_alpha_e,chedy
unigram_alpha_f,qokchey
unigram_alpha_g,qokchy
unigram_alpha_h,qokchedy
unigram_alpha_i,shedy
unigram_alpha_l,qokal
unigram_alpha_m,qokar
unigram_alpha_n,daiin
unigram_alpha_o,aiin
unigram_alpha_p,qoky
unigram_alpha_q,qokol
unigram_alpha_r,qokeedy
unigram_alpha_s,qokeey
unigram_alpha_t,qokaiin
unigram_alpha_u,qokain
unigram_alpha_v,qokey
unigram_alpha_x,qokor
unigram_alpha_y,qokdy
unigram_alpha_z,qokeeedy
unigram_beta1_a,or
unigram_beta1_b,okchdy
unigram_beta1_c,okedy
unigram_beta1_d,cheedy
unigram_beta1_e,ar
unigram_beta1_f,okchey
unigram_beta1_g,okchy
unigram_beta1_h,okchedy
unigram_beta1_i,qokedy
unigram_beta1_l,okal
unigram_beta1_m,okar
unigram_beta1_n,dal
unigram_beta1_o,al
unigram_beta1_p,oky
unigram_beta1_q,okol
unigram_beta1_r,okeedy
unigram_beta1_s,okeey
unigram_beta1_t,okaiin
unigram_beta1_u,okain
unigram_beta1_v,okey
unigram_beta1_x,okor
unigram_beta1_y,okdy
unigram_beta1_z,okeeedy
unigram_beta2_a,qol
unigram_beta2_b,otchdy
unigram_beta2_c,lkaiin
unigram_beta2_d,lkain
unigram_beta2_e,dar
unigram_beta2_f,otchey
unigram_beta2_g,otchy
unigram_beta2_h,otchedy
unigram_beta2_i,shey
unigram_beta2_l,otal
unigram_beta2_m,otar
unigram_beta2_n,dain
unigram_beta2_o,ain
unigram_beta2_p,oty
unigram_beta2_q,otol
unigram_beta2_r,oteedy
unigram_beta2_s,oteey
unigram_beta2_t,otaiin
unigram_beta2_u,otain
unigram_beta2_v,otey
unigram_beta2_x,otor
unigram_beta2_y,otdy
unigram_beta2_z,oteeedy
unigram_beta3_a,chdy
unigram_beta3_b,sheckhy
unigram_beta3_c,shckhy
unigram_beta3_d,chor
unigram_beta3_e,dar
unigram_beta3_f,shal
unigram_beta3_g,shar
unigram_beta3_h,shy
unigram_beta3_i,otedy
unigram_beta3_l,saiin
unigram_beta3_m,sain
unigram_beta3_n,dy
unigram_beta3_o,y
unigram_beta3_p,sheody
unigram_beta3_q,shody
unigram_beta3_r,sheol
unigram_beta3_s,shol
unigram_beta3_t,sheey
unigram_beta3_u,sheedy
unigram_beta3_v,shor
unigram_beta3_x,shaiin
unigram_beta3_y,shain
unigram_beta3_z,sheeey
unigram_gamma1_a,chol
unigram_gamma1_b,qotchdy
unigram_gamma1_c,sar
unigram_gamma1_d,chckhey
unigram_gamma1_e,chckhy
unigram_gamma1_f,qotchey
unigram_gamma1_g,qotchy
unigram_gamma1_h,qotchedy
unigram_gamma1_i,raiin
unigram_gamma1_l,qotal
unigram_gamma1_m,qotar
unigram_gamma1_n,dair
unigram_gamma1_o,air
unigram_gamma1_p,qoty
unigram_gamma1_q,qotol
unigram_gamma1_r,qoteedy
unigram_gamma1_s,qoteey
unigram_gamma1_t,qotaiin
unigram_gamma1_u,qotain
unigram_gamma1_v,qotey
unigram_gamma1_x,qotor
unigram_gamma1_y,qotdy
unigram_gamma1_z,qoteeedy
unigram_gamma2_a,cheol
unigram_gamma2_b,olkchdy
unigram_gamma2_c,lchey
unigram_gamma2_d,olkedy
unigram_gamma2_e,lchedy
unigram_gamma2_f,olkchey
unigram_gamma2_g,olkchy
unigram_gamma2_h,olkchedy
unigram_gamma2_i,qotedy
unigram_gamma2_l,olkal
unigram_gamma2_m,olkar
unigram_gamma2_n,dam
unigram_gamma2_o,am
unigram_gamma2_p,olky
unigram_gamma2_q,olkol
unigram_gamma2_r,olkeedy
unigram_gamma2_s,olkeey
unigram_gamma2_t,olkaiin
unigram_gamma2_u,olkain
unigram_gamma2_v,olkey
unigram_gamma2_x,olkor
unigram_gamma2_y,olkdy
unigram_gamma2_z,olkeeedy
suffix_alpha_a,aiin
suffix_alpha_b,l
suffix_alpha_c,eeey
suffix_alpha_d,eeody
suffix_alpha_e,edy
suffix_alpha_f,eam
suffix_alpha_g,g
suffix_alpha_h,eedal
suffix_alpha_i,dy
suffix_alpha_l,es
suffix_alpha_m,ody
suffix_alpha_n,al
suffix_alpha_o,or
suffix_alpha_p,edar
suffix_alpha_q,iin
suffix_alpha_r,eedy
suffix_alpha_s,ar
suffix_alpha_t,y
suffix_alpha_u,eey
suffix_alpha_v,edor
suffix_alpha_x,edo
suffix_alpha_y,oin
suffix_alpha_z,eeaiin
prefix_alpha_a,sh
prefix_alpha_b,dol
prefix_alpha_c,lch
prefix_alpha_d,o
prefix_alpha_e,ch
prefix_alpha_f,shckh
prefix_alpha_g,cph
prefix_alpha_h,qotch
prefix_alpha_i,k
prefix_alpha_l,cth
prefix_alpha_m,l
prefix_alpha_n,opch
prefix_alpha_o,r
prefix_alpha_p,dch
prefix_alpha_q,dl
prefix_alpha_r,t
prefix_alpha_s,lk
prefix_alpha_t,qok
prefix_alpha_u,ot
prefix_alpha_v,qockh
prefix_alpha_x,lpch
prefix_alpha_y,ry
prefix_alpha_z,ols
suffix_beta1_a,eol
suffix_beta1_b,ory
suffix_beta1_c,r
suffix_beta1_d,eeos
suffix_beta1_e,ey
suffix_beta1_f,iiin
suffix_beta1_g,eols
suffix_beta1_h,er
suffix_beta1_i,eody
suffix_beta1_l,eedaiin
suffix_beta1_m,edain
suffix_beta1_n,d
suffix_beta1_o,eos
suffix_beta1_p,as
suffix_beta1_q,als
suffix_beta1_r,daiin
suffix_beta1_s,eeo
suffix_beta1_t,am
suffix_beta1_u,eo
suffix_beta1_v,sy
suffix_beta1_x,eeeos
suffix_beta1_y,eory
suffix_beta1_z,eds
prefix_beta1_a,yt
prefix_beta1_b,qolch
prefix_beta1_c,tsh
prefix_beta1_d,dal
prefix_beta1_e,ok
prefix_beta1_f,rsh
prefix_beta1_g,solch
prefix_beta1_h,oiin
prefix_beta1_i,yk
prefix_beta1_l,ypch
prefix_beta1_m,s
prefix_beta1_n,kch
prefix_beta1_o,lkch
prefix_beta1_p,qoksh
prefix_beta1_q,of
prefix_beta1_r,tch
prefix_beta1_s,or
prefix_beta1_t,pch
prefix_beta1_u,olk
prefix_beta1_v,daly
prefix_beta1_x,f
prefix_beta1_y,sok
prefix_beta1_z,lfch
suffix_beta2_a,air
suffix_beta2_b,oy
suffix_beta2_c,aiiin
suffix_beta2_d,dol
suffix_beta2_e,ol
suffix_beta2_f,daiiin
suffix_beta2_g,saiin
suffix_beta2_h,eaiin
suffix_beta2_i,eor
suffix_beta2_l,edol
suffix_beta2_m,dain
suffix_beta2_n,oiin
suffix_beta2_o,eeedy
suffix_beta2_p,eeod
suffix_beta2_q,edaiiin
suffix_beta2_r,s
suffix_beta2_s,edal
suffix_beta2_t,edaiin
suffix_beta2_u,eeol
suffix_beta2_v,sdy
suffix_beta2_x,ery
suffix_beta2_y,osy
suffix_beta2_z,eda
prefix_beta2_a,olch
prefix_beta2_b,dor
prefix_beta2_c,y
prefix_beta2_d,otsh
prefix_beta2_e,ol
prefix_beta2_f,ly
prefix_beta2_g,ssh
prefix_beta2_h,aly
prefix_beta2_i,qot
prefix_beta2_l,sch
prefix_beta2_m,shcth
prefix_beta2_n,okch
prefix_beta2_o,lt
prefix_beta2_p,qolk
prefix_beta2_q,dary
prefix_beta2_r,qopch
prefix_beta2_s,sol
prefix_beta2_t,od
prefix_beta2_u,p
prefix_beta2_v,sar
prefix_beta2_x,do
prefix_beta2_y,olpch
prefix_beta2_z,om
suffix_beta3_a,ed
suffix_beta3_b,eoy
suffix_beta3_c,aiir
suffix_beta3_d,oly
suffix_beta3_e,ain
suffix_beta3_f,do
suffix_beta3_g,eeam
suffix_beta3_h,eeoy
suffix_beta3_i,o
suffix_beta3_l,edair
suffix_beta3_m,eedar
suffix_beta3_n,eod
suffix_beta3_o,edam
suffix_beta3_p,e
suffix_beta3_q,ols
suffix_beta3_r,eeor
suffix_beta3_s,eed
suffix_beta3_t,ees
suffix_beta3_u,eal
suffix_beta3_v,sd
suffix_beta3_x,ch
suffix_beta3_y,yl
suffix_beta3_z,ady
prefix_beta3_a,ls
prefix_beta3_b,octh
prefix_beta3_c,och
prefix_beta3_d,dar
prefix_beta3_e,qo
prefix_beta3_f,osh
prefix_beta3_g,orch
prefix_beta3_h,qoch
prefix_beta3_i,ych
prefix_beta3_l,ykch
prefix_beta3_m,aiiin
prefix_beta3_n,oly
prefix_beta3_o,ody
prefix_beta3_p,ofch
prefix_beta3_q,es
prefix_beta3_r,ysh
prefix_beta3_s,chcth
prefix_beta3_t,ar
prefix_beta3_u,op
prefix_beta3_v,dyk
prefix_beta3_x,qolsh
prefix_beta3_y,opsh
prefix_beta3_z,daiir
suffix_gamma1_a,dal
suffix_gamma1_b,eeed
suffix_gamma1_c,ail
suffix_gamma1_d,eeeody
suffix_gamma1_e,ear
suffix_gamma1_f,eel
suffix_gamma1_g,ok
suffix_gamma1_h,eedam
suffix_gamma1_i,od
suffix_gamma1_l,daly
suffix_gamma1_m,dor
suffix_gamma1_n,eees
suffix_gamma1_o,dair
suffix_gamma1_p,eoly
suffix_gamma1_q,ealy
suffix_gamma1_r,dam
suffix_gamma1_s,an
suffix_gamma1_t,ary
suffix_gamma1_u,ee
suffix_gamma1_v,aiis
suffix_gamma1_x,dl
suffix_gamma1_y,ry
suffix_gamma1_z,in
prefix_gamma1_a,chckh
prefix_gamma1_b,psh
prefix_gamma1_c,qofch
prefix_gamma1_d,qol
prefix_gamma1_e,dsh
prefix_gamma1_f,qotsh
prefix_gamma1_g,sy
prefix_gamma1_h,ory
prefix_gamma1_i,sal
prefix_gamma1_l,qokch
prefix_gamma1_m,q
prefix_gamma1_n,aiir
prefix_gamma1_o,solk
prefix_gamma1_p,qor
prefix_gamma1_q,air
prefix_gamma1_r,qop
prefix_gamma1_s,ytch
prefix_gamma1_t,rch
prefix_gamma1_u,ckh
prefix_gamma1_v,da
prefix_gamma1_x,dk
prefix_gamma1_y,sk
prefix_gamma1_z,so
suffix_gamma2_a,aly
suffix_gamma2_b,eom
suffix_gamma2_c,esy
suffix_gamma2_d,a
suffix_gamma2_e,dar
suffix_gamma2_f,sairy
suffix_gamma2_g,iir
suffix_gamma2_h,eer
suffix_gamma2_i,m
suffix_gamma2_l,eesy
suffix_gamma2_m,eeal
suffix_gamma2_n,eain
suffix_gamma2_o,aim
suffix_gamma2_p,ais
suffix_gamma2_q,oiiin
suffix_gamma2_r,eear
suffix_gamma2_s,os
suffix_gamma2_t,om
suffix_gamma2_u,eedain
suffix_gamma2_v,eeeo
suffix_gamma2_x,eedo
suffix_gamma2_y,yr
suffix_gamma2_z,alsy
prefix_gamma2_a,al
prefix_gamma2_b,ary
prefix_gamma2_c,olt
prefix_gamma2_d,sair
prefix_gamma2_e,lsh
prefix_gamma2_f,dair
prefix_gamma2_g,dyt
prefix_gamma2_h,qocth
prefix_gamma2_i,olsh
prefix_gamma2_l,ockh
prefix_gamma2_m,d
prefix_gamma2_n,os
prefix_gamma2_o,oksh
prefix_gamma2_p,chcph
prefix_gamma2_q,oiiin
prefix_gamma2_r,otch
prefix_gamma2_s,ksh
prefix_gamma2_t,sor
prefix_gamma2_u,fch
prefix_gamma2_v,soiin
prefix_gamma2_x,x
prefix_gamma2_y,ail
prefix_gamma2_z,chcfh"""

# Parse tables
unigram_map = {}  # glyph -> list of (table, letter)
prefix_map = {}   # glyph -> list of (table, letter)
suffix_map = {}   # glyph -> list of (table, letter)

for line in TABLES_RAW.strip().split("\n"):
    code, glyphs = line.split(",", 1)
    parts = code.split("_")
    category = parts[0]
    table = parts[1]
    letter = parts[2]

    if category == "unigram":
        unigram_map.setdefault(glyphs, []).append((table, letter))
    elif category == "prefix":
        prefix_map.setdefault(glyphs, []).append((table, letter))
    elif category == "suffix":
        suffix_map.setdefault(glyphs, []).append((table, letter))

# f1r EVA text (cleaned from transcription)
f1r_lines = [
    "fachys ykal ar taiin shol shory ses y kor sholdy",
    "sory ckhar ory kair chtaiin shar is cthar cthar dan",
    "syaiir sheky or ykaiin shod cthoary cthes daraiin sy",
    "soiin oteey oteor roloty ar daiin okaiin or okan",
    "sairy chear cthaiin cphar cfhaiin",
    "ydaraishy",
    "odar shol cphoy oydar shs cfhoaiin shodary",
    "yshey shody okchoy otchol chocthy oschy dain chor kos",
    "daiin shos cfhol shody",
    "dain or teod",
    "ydain cphesaiin ols cphey ytain shoshy cphodal es",
    "oksho kshoy otairin oteol okan shodain sckchy daiin",
    "shoy ckhey kodaiin cphy cphodaiils cthhy sho olain",
    "dain oiin chol odaiin chodain chdy okain an cthy kod",
    "daiin shckhey ckhor char shey kol chol chol kor chal",
    "sho chol shodan kshy kchy dor chodaiin sho keeam",
    "ycho tchey chekain sheopshol dydyd cthy daiy",
    "to shol she kodshey cphealy dar ain dain ckhyds",
    "dchar shcthaiin okaiir chey chy tol cthols dloy",
    "shok chor chey dain ckhey",
    "otol daiiin",
    "cpho shaiin shokcheey chol tshodeesy shey pydeey chy ro dar",
    "ain chol dain cthal dar shear kaiin dar chey cthar",
    "cho kaiin shoaiin okol daiin par cthol daiin ctholdar",
    "ycheey okeey oky daiin okchey kokaiin ochol kchy dal",
    "dcheo shody koechy cthy okchey keey keey dal chtor",
    "sho chol chckh choty chotey",
    "dchaiin",
]

print("=" * 80)
print("NAIBBE CIPHER REVERSE TEST ON VOYNICH f1r")
print("=" * 80)
print()

# Collect all words
all_words = []
for line in f1r_lines:
    words = re.split(r"[\s.]+", line)
    words = [w.strip() for w in words if w.strip()]
    all_words.extend(words)

total_words = len(all_words)
print(f"Total EVA words in f1r: {total_words}")
print()

# --- UNIGRAM MATCHES ---
unigram_results = []
for w in all_words:
    if w in unigram_map:
        matches = unigram_map[w]
        letters = sorted(set(m[1] for m in matches))
        unigram_results.append((w, letters))

print(f"--- UNIGRAM MATCHES ({len(unigram_results)}/{total_words} = {100*len(unigram_results)/total_words:.1f}%) ---")
for w, letters in unigram_results:
    print(f"  {w:15s} -> {'/'.join(letters)}")

# --- BIGRAM MATCHES ---
bigram_results = []
for w in all_words:
    readings = []
    for sp in range(1, len(w)):
        pre = w[:sp]
        suf = w[sp:]
        if pre in prefix_map and suf in suffix_map:
            for pt, pl in prefix_map[pre]:
                for st, sl in suffix_map[suf]:
                    readings.append(f"{pl}{sl}")
    if readings:
        bigram_results.append((w, sorted(set(readings))))

print()
print(f"--- BIGRAM MATCHES ({len(bigram_results)}/{total_words} = {100*len(bigram_results)/total_words:.1f}%) ---")
for w, readings in bigram_results[:60]:
    print(f"  {w:15s} -> {', '.join(readings[:10])}")

# --- SUMMARY ---
uni_set = set(w for w, _ in unigram_results)
bi_set = set(w for w, _ in bigram_results)
either_set = uni_set | bi_set

matched_tokens = sum(1 for w in all_words if w in either_set)
unmatched_words = [w for w in all_words if w not in either_set]

print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total tokens:        {total_words}")
print(f"Unigram matches:     {len(unigram_results)} tokens")
print(f"Bigram matches:      {len(bigram_results)} tokens")
print(f"Either (tokens):     {matched_tokens} ({100*matched_tokens/total_words:.1f}%)")
print(f"No match (tokens):   {total_words - matched_tokens} ({100*(total_words-matched_tokens)/total_words:.1f}%)")
print()

# Show unmatched
unique_unmatched = sorted(set(unmatched_words))
print(f"Unmatched unique words ({len(unique_unmatched)}):")
for w in unique_unmatched[:30]:
    print(f"  {w}")

# --- ATTEMPTED LINE-BY-LINE READING ---
print()
print("=" * 80)
print("LINE-BY-LINE READING ATTEMPT (best single reading per word)")
print("=" * 80)

for li, line in enumerate(f1r_lines[:10], 1):
    words = re.split(r"[\s.]+", line)
    words = [w.strip() for w in words if w.strip()]
    decoded = []
    for w in words:
        # Prefer unigram
        if w in unigram_map:
            letters = sorted(set(m[1] for m in unigram_map[w]))
            decoded.append(letters[0].upper())
        else:
            # Try bigram
            found = False
            for sp in range(1, len(w)):
                pre = w[:sp]
                suf = w[sp:]
                if pre in prefix_map and suf in suffix_map:
                    pl = sorted(set(m[1] for m in prefix_map[pre]))[0]
                    sl = sorted(set(m[1] for m in suffix_map[suf]))[0]
                    decoded.append(f"{pl}{sl}".upper())
                    found = True
                    break
            if not found:
                decoded.append(f"[{w}]")

    print(f"Line {li:2d}: {' '.join(decoded)}")
    print(f"  EVA:  {line}")
    print()

# --- COMMON WORD ANALYSIS ---
print("=" * 80)
print("COMMON VOYNICH WORDS vs NAIBBE TABLES")
print("=" * 80)
common = ["daiin", "chol", "shol", "dain", "chor", "aiin", "ain", "ol", "or", "ar",
          "chey", "shey", "cthy", "shy", "dal", "dar", "dy", "y", "air", "dair",
          "shor", "shar", "chdy", "sheey", "am", "dam"]
for w in common:
    readings = []
    if w in unigram_map:
        for t, l in unigram_map[w]:
            readings.append(f"U({t})={l}")
    for sp in range(1, len(w)):
        pre = w[:sp]
        suf = w[sp:]
        if pre in prefix_map and suf in suffix_map:
            for pt, pl in prefix_map[pre]:
                for st, sl in suffix_map[suf]:
                    readings.append(f"B({pt},{st})={pl}{sl}")
    if readings:
        print(f"  {w:12s} -> {'; '.join(readings[:8])}")
    else:
        print(f"  {w:12s} -> [no match]")
