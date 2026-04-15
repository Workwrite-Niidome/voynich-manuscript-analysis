#!/usr/bin/env python3
"""Analyze plant code sub-sequences for family encoding patterns."""

from collections import defaultdict

# All first words (plant codes) from herbal folios
plant_codes = {
    'f1r': 'fachys',
    'f1v': 'kchsy',
    'f2r': 'kydainy',
    'f2v': 'kooiin',
    'f3r': 'tsheos',
    'f3v': 'koaiin',
    'f4r': 'kodalchy',
    'f4v': 'pchooiin',
    'f5r': 'kchody',
    'f6r': 'foar',
    'f6v': 'koarysar',
    'f7r': 'fchodaiin',
    'f8r': 'pshol',
    'f9r': 'tydlo',
    'f9v': 'fochor',
    'f10r': 'pchocthy',
    'f10v': 'paiin',
    'f11r': 'tshol',
    'f11v': 'poldchody',
    'f13r': 'torshor',
    'f13v': 'koair',
    'f14r': 'pchodaiin',
    'f14v': 'pdychoiin',
    'f15r': 'tshor',
    'f15v': 'paror',
    'f16r': 'pocheody',
    'f17r': 'fshody',
    'f17v': 'pchodol',
    'f18r': 'pdrairdy',
    'f18v': 'told',
    'f19r': 'pchor',
    'f19v': 'pochaiin',
    'f20r': 'kdchody',
    'f20v': 'faiisar',
    'f21r': 'pchor',
    'f21v': 'toldshy',
    'f22r': 'pol',
    'f22v': 'pysaiinor',
    'f23r': 'pydchdom',
    'f23v': 'podairol',
    'f24r': 'porory',
    'f24v': 'tchodar',
    'f25r': 'fcholdy',
    'f25v': 'poeeaiin',
    'f26r': 'psheoky',
    'f26v': 'pchedar',
    'f27r': 'ksor',
    'f27v': 'fochof',
    'f28r': 'pchodar',
    'f28v': 'kshol',
    'f29r': 'posaiin',
    'f29v': 'kooiin',
    'f30r': 'okeeesy',
    'f31r': 'keedey',
    'f31v': 'podair',
    'f32r': 'fchaiin',
    'f32v': 'kcheodaiin',
    'f33r': 'tshdar',
    'f33v': 'tarar',
    'f34r': 'pcheoepchy',
    'f34v': 'kschdy',
    'f35v': 'parchor',
    'f36r': 'pchadan',
    'f36v': 'pcharosy',
    'f37r': 'tocphol',
    'f37v': 'kshody',
    'f38r': 'tolor',
    'f39v': 'pair',
    'f40r': 'pchey',
    'f41r': 'psheykedaleey',
    'f43r': 'tarodaiin',
    'f43v': 'pdsairy',
    'f44r': 'tshodpy',
    'f44v': 'tsho',
    'f45r': 'pykydal',
    'f45v': 'kosary',
    'f46r': 'pcheocphy',
    'f47r': 'pchair',
    'f47v': 'psheot',
    'f48r': 'pshdaiin',
    'f48v': 'pcheodchy',
    'f49r': 'pchol',
    'f50r': 'psheor',
    'f50v': 'tchy',
    'f51r': 'tsholdchy',
    'f51v': 'poshody',
    'f52r': 'tdokchcfhy',
    'f52v': 'pchor',
    'f53r': 'kdam',
    'f53v': 'tshorshey',
    'f54r': 'podaiin',
    'f54v': 'pcheodar',
    'f55r': 'podaiin',
    'f55v': 'kcheedchdy',
    'f56v': 'kcheot',
    'f57r': 'poeeockhey',
    'f65v': 'cphy',
    'f66v': 'okeodof',
    'f69r': 'tcheeos',
    'f75r': 'kchedykary',
    'f75v': 'pchedar',
    'f76r': 'potchokor',
    'f76v': 'polarar',
    'f79r': 'torain',
}

# Known/proposed plant identifications
identifications = {
    'f1r': ('Laurus nobilis', 'Lauraceae', 45),
    'f2r': ('Paeonia officinalis', 'Ranunculaceae', 55),
    'f2v': ('Cyclamen sp.', 'Primulaceae', 45),
    'f3r': ('Rubia tinctorum', 'Rubiaceae', 60),
    'f3v': ('Cynara scolymus', 'Asteraceae', 55),
    'f4r': ('Rosmarinus officinalis', 'Lamiaceae', 55),
    'f5r': ('Aristolochia rotunda', 'Aristolochiaceae', 40),
    'f7r': ('Helleborus niger', 'Ranunculaceae', 30),
    'f8r': ('Arum maculatum', 'Araceae', 40),
    'f9r': ('Nigella damascena', 'Ranunculaceae', 65),
    'f10r': ('Mandragora officinarum', 'Solanaceae', 40),
    'f11r': ('Borago officinalis', 'Boraginaceae', 30),
    'f13r': ('Bryonia dioica', 'Cucurbitaceae', 30),
    'f14r': ('Symphytum officinale', 'Boraginaceae', 35),
    'f15r': ('Taraxacum officinale', 'Asteraceae', 30),
    'f16r': ('Cannabis sativa', 'Cannabaceae', 25),
    'f17r': ('Centaurea sp.', 'Asteraceae', 30),
    'f18r': ('Gentiana sp.', 'Gentianaceae', 30),
    'f20r': ('Fumaria officinalis', 'Papaveraceae', 25),
    'f22r': ('Polygala sp.', 'Polygalaceae', 25),
    'f23r': ('Aconitum napellus', 'Ranunculaceae', 35),
    'f24r': ('Chrysanthemum sp.', 'Asteraceae', 25),
    'f25r': ('Mentha sp.', 'Lamiaceae', 30),
    'f26r': ('Glechoma hederacea', 'Lamiaceae', 25),
    'f27r': ('Symphytum sp.', 'Boraginaceae', 25),
    'f28r': ('Arum italicum', 'Araceae', 35),
    'f29r': ('Convallaria majalis', 'Asparagaceae', 25),
    'f30r': ('Plantago major', 'Plantaginaceae', 30),
    'f31r': ('Angelica sp.', 'Apiaceae', 30),
    'f32r': ('Lamium sp.', 'Lamiaceae', 25),
    'f33r': ('Scabiosa sp.', 'Caprifoliaceae', 25),
    'f34r': ('Cirsium sp.', 'Asteraceae', 30),
    'f37r': ('Polygonum sp.', 'Polygonaceae', 25),
    'f38r': ('Dipsacus sp.', 'Caprifoliaceae', 25),
    'f40r': ('Echinops sp.', 'Asteraceae', 25),
    'f41r': ('Adiantum capillus-veneris', 'Pteridaceae', 60),
    'f43r': ('Rubia tinctorum (cult.)', 'Rubiaceae', 60),
    'f45r': ('Alchemilla/Potentilla', 'Rosaceae', 35),
    'f46r': ('Eryngium sp.', 'Apiaceae', 30),
    'f47r': ('Vitis vinifera', 'Vitaceae', 70),
    'f48r': ('Aconitum sp.', 'Ranunculaceae', 30),
    'f50r': ('Centaurea/Cynara', 'Asteraceae', 25),
    'f51r': ('Paeonia variant?', 'Ranunculaceae', 20),
    'f6r': ('Papaver/Datura', 'Papaveraceae', 25),
}

print("=" * 80)
print("TASK 1: ALL plant codes containing 'yd'")
print("=" * 80)

yd_codes = {}
for folio, code in sorted(plant_codes.items(), key=lambda x: x[0]):
    if 'yd' in code:
        ident = identifications.get(folio, ('Unknown', 'Unknown', 0))
        yd_codes[folio] = (code, ident)
        print(f"  {folio}: {code:20s} -> {ident[0]:30s} ({ident[1]}, {ident[2]}%)")

print(f"\nTotal codes with 'yd': {len(yd_codes)}")
ranunc_count = sum(1 for _, (_, ident) in yd_codes.items() if 'Ranunculaceae' in ident[1])
print(f"Of these, Ranunculaceae: {ranunc_count}")

print("\n" + "=" * 80)
print("TASK 2: Systematic sub-sequence analysis")
print("=" * 80)

# Check key sub-sequences
interesting = [
    'yd', 'cheo', 'pcheo', 'sheo', 'shol', 'chol', 'chor',
    'tsh', 'psh', 'kch', 'fch', 'pch',
    'cho', 'sho', 'dai', 'ody', 'dch',
    'ol', 'or', 'ar', 'dy', 'ey',
    'eed', 'osa', 'ora', 'aro',
    'pshe', 'oche', 'oda', 'pod', 'por',
    'she', 'che',
]

for sub in interesting:
    matching = []
    for folio, code in plant_codes.items():
        if sub in code:
            matching.append(folio)

    if len(matching) >= 3:
        families = defaultdict(list)
        for f in matching:
            if f in identifications:
                fam = identifications[f][1]
                families[fam].append(f)
            else:
                families['Unknown'].append(f)

        total_known = sum(len(v) for k, v in families.items() if k != 'Unknown')
        unknown_count = len(families.get('Unknown', []))

        # Check for family concentration
        dominant_families = [(fam, fols) for fam, fols in families.items()
                          if fam != 'Unknown' and len(fols) >= 2]

        if dominant_families or len(matching) <= 8:
            print(f"\n  '{sub}' in {len(matching)} codes ({total_known} identified, {unknown_count} unknown):")
            for f in sorted(matching):
                ident = identifications.get(f, ('?', '?', 0))
                code = plant_codes[f]
                # Highlight the sub-sequence position
                pos = code.find(sub)
                marked = code[:pos] + '[' + sub + ']' + code[pos+len(sub):]
                print(f"    {f}: {marked:25s} {ident[0]:30s} [{ident[1]}]")

            for fam, fols in dominant_families:
                pct = len(fols) / total_known * 100 if total_known > 0 else 0
                print(f"    >> {fam}: {len(fols)}/{total_known} identified ({pct:.0f}%)")


print("\n" + "=" * 80)
print("TASK 3: 'pcheo-' cluster")
print("=" * 80)

for folio, code in sorted(plant_codes.items()):
    if 'pcheo' in code:
        ident = identifications.get(folio, ('Unknown', 'Unknown', 0))
        print(f"  {folio}: {code:20s} -> {ident[0]:30s} ({ident[1]})")

# Also check broader 'cheo'
print("\nBroader 'cheo' occurrences:")
for folio, code in sorted(plant_codes.items()):
    if 'cheo' in code:
        ident = identifications.get(folio, ('Unknown', 'Unknown', 0))
        print(f"  {folio}: {code:20s} -> {ident[0]:30s} ({ident[1]})")


print("\n" + "=" * 80)
print("TASK 4: Family-encoding table (families with 2+ plants)")
print("=" * 80)

family_plants = defaultdict(list)
for folio, (plant, family, conf) in identifications.items():
    if conf >= 20:
        family_plants[family].append((folio, plant_codes.get(folio, '?'), plant, conf))

for fam, plants in sorted(family_plants.items(), key=lambda x: -len(x[1])):
    if len(plants) >= 2:
        print(f"\n  {fam} ({len(plants)} plants):")
        codes = []
        for folio, code, plant, conf in sorted(plants, key=lambda x: -x[3]):
            print(f"    {folio}: {code:20s} -> {plant:30s} ({conf}%)")
            codes.append(code)

        # Find shared sub-sequences among family members
        if len(codes) >= 2:
            shared = defaultdict(int)
            for code in codes:
                seen = set()
                for length in [2, 3, 4, 5]:
                    for i in range(len(code) - length + 1):
                        sub = code[i:i+length]
                        if sub not in seen:
                            seen.add(sub)
                            shared[sub] += 1

            family_shared = {sub: cnt for sub, cnt in shared.items()
                           if cnt >= 2 and len(sub) >= 2}
            if family_shared:
                # Check exclusivity
                best_markers = []
                for sub, cnt in sorted(family_shared.items(), key=lambda x: (-len(x[0]), -x[1])):
                    other_count = 0
                    total_other = 0
                    for f2, c2 in plant_codes.items():
                        if f2 not in [p[0] for p in plants]:
                            total_other += 1
                            if sub in c2:
                                other_count += 1
                    in_pct = cnt / len(codes) * 100
                    out_pct = other_count / max(total_other, 1) * 100
                    if in_pct > out_pct * 1.5 and len(sub) >= 3:
                        best_markers.append((sub, cnt, len(codes), other_count, total_other))

                if best_markers:
                    print(f"    Distinctive sub-sequences:")
                    for sub, cnt, total, out_cnt, out_total in best_markers[:5]:
                        print(f"      '{sub}': {cnt}/{total} in-family vs {out_cnt}/{out_total} outside")


print("\n" + "=" * 80)
print("TASK 5: Cross-validation matrix")
print("=" * 80)

# Test specific hypotheses
hypotheses = [
    ('yd', 'Ranunculaceae'),
    ('pcheo', 'Asteraceae'),
    ('tsh', 'Rubiaceae'),  # test
    ('shol', 'Araceae'),   # test
    ('chod', 'Boraginaceae'),  # test
]

print("\nHypothesis testing:")
print(f"{'Sub-seq':10s} {'Hyp. Family':20s} {'In-fam':8s} {'Out-fam':8s} {'Precision':10s} {'Recall':10s}")
print("-" * 70)

for sub, hyp_family in hypotheses:
    # All codes containing the sub-sequence
    codes_with = [f for f, c in plant_codes.items() if sub in c]

    # Of those, how many are the hypothesized family?
    true_pos = 0
    false_pos = 0
    for f in codes_with:
        if f in identifications:
            if hyp_family in identifications[f][1]:
                true_pos += 1
            else:
                false_pos += 1

    # How many of the family DON'T have the sub-sequence (false negatives)?
    false_neg = 0
    total_family = 0
    for f, (_, fam, _) in identifications.items():
        if hyp_family in fam:
            total_family += 1
            if f not in codes_with:
                false_neg += 1

    precision = true_pos / (true_pos + false_pos) * 100 if (true_pos + false_pos) > 0 else 0
    recall = true_pos / total_family * 100 if total_family > 0 else 0

    identified_with = true_pos + false_pos
    print(f"'{sub:8s}' {hyp_family:20s} {true_pos}/{identified_with:<5d}    {false_pos}/{identified_with:<5d}    {precision:6.1f}%     {recall:6.1f}%")


print("\n" + "=" * 80)
print("ADDITIONAL: Check for -yd- plants that could be Ranunculaceae")
print("=" * 80)

# Ranunculaceae includes: Aconitum, Actaea, Adonis, Anemone, Aquilegia,
# Caltha, Clematis, Consolida, Delphinium, Eranthis, Helleborus,
# Hepatica, Nigella, Paeonia (formerly), Pulsatilla, Ranunculus, Thalictrum, Trollius

# Check -yd- codes that are unidentified or low confidence
for folio, code in sorted(plant_codes.items()):
    if 'yd' in code:
        ident = identifications.get(folio, None)
        if ident is None:
            print(f"  {folio}: {code} -> UNIDENTIFIED - could be Ranunculaceae?")
        elif 'Ranunculaceae' not in ident[1]:
            print(f"  {folio}: {code} -> {ident[0]} ({ident[1]}, {ident[2]}%) - NOT Ranunculaceae")
            print(f"    Could this actually be Ranunculaceae? Check illustration.")
