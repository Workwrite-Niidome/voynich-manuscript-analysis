#!/usr/bin/env python3
"""
Dioscorides Bulk Mapping for Voynich Manuscript Herbal Section.
Uses 5 anchor points to fit a linear model: folio_number -> Dioscorides_linear_chapter.
Then predicts the Dioscorides chapter for every herbal folio.
"""

import numpy as np
import re
import json
from collections import Counter

# =============================================================================
# Dioscorides structure
# =============================================================================
DIOSCORIDES_BOOKS = {1: 128, 2: 186, 3: 158, 4: 186, 5: 159}

BOOK_OFFSETS = {}
offset = 0
for book, count in DIOSCORIDES_BOOKS.items():
    BOOK_OFFSETS[book] = offset
    offset += count
TOTAL_CHAPTERS = offset  # 817

def book_chapter_to_linear(book, chapter):
    return BOOK_OFFSETS[book] + chapter

def linear_to_book_chapter(linear):
    linear = max(1, min(TOTAL_CHAPTERS, int(round(linear))))
    for book in sorted(DIOSCORIDES_BOOKS.keys(), reverse=True):
        if linear > BOOK_OFFSETS[book]:
            return (book, linear - BOOK_OFFSETS[book])
    return (1, 1)

# =============================================================================
# 5 Anchor points
# =============================================================================
ANCHORS = {
    2:  ("Paeonia officinalis", 3, 140, 0.55),
    3:  ("Rubia tinctorum", 3, 143, 0.60),
    9:  ("Nigella damascena", 3, 79, 0.65),
    41: ("Adiantum capillus-veneris", 4, 134, 0.60),
    47: ("Vitis vinifera", 5, 1, 0.70),
}

anchor_folios = []
anchor_linear = []
anchor_weights = []
for folio, (name, book, ch, conf) in sorted(ANCHORS.items()):
    lin = book_chapter_to_linear(book, ch)
    anchor_folios.append(folio)
    anchor_linear.append(lin)
    anchor_weights.append(conf)
    print(f"  Anchor: f{folio}r = {name} -> Dioscorides {book}.{ch} -> linear {lin}")

# =============================================================================
# Weighted linear regression
# =============================================================================
x = np.array(anchor_folios, dtype=float)
y = np.array(anchor_linear, dtype=float)
w = np.array(anchor_weights, dtype=float)

W = np.diag(w)
X = np.column_stack([x, np.ones_like(x)])
beta = np.linalg.solve(X.T @ W @ X, X.T @ W @ y)
slope, intercept = beta[0], beta[1]

print(f"\nLinear model: linear_chapter = {slope:.2f} * folio + {intercept:.2f}")
print(f"  At folio 1: predicted chapter = {slope * 1 + intercept:.1f}")
print(f"  At folio 57: predicted chapter = {slope * 57 + intercept:.1f}")

for i, (f, l) in enumerate(zip(anchor_folios, anchor_linear)):
    pred = slope * f + intercept
    print(f"  f{f}r: actual={l}, predicted={pred:.1f}, residual={l-pred:.1f}")

# =============================================================================
# Dioscorides plant lookup
# =============================================================================
DIOSCORIDES_PLANTS = {
    (1, 1): "Iris germanica (orris root)",
    (1, 5): "Nardostachys (spikenard)",
    (1, 6): "Asarum europaeum (asarabacca)",
    (1, 7): "Valeriana (valerian)",
    (1, 9): "Cyperus rotundus (galingale)",
    (1, 10): "Zingiber (ginger)",
    (1, 12): "Costus (costus root)",
    (1, 13): "Cinnamomum (cinnamon)",
    (1, 15): "Liquidambar (storax)",
    (1, 17): "Boswellia (frankincense)",
    (1, 18): "Pinus (pine resin)",
    (1, 19): "Pistacia terebinthus (terebinth)",
    (1, 20): "Cedrus (cedar)",
    (1, 22): "Juniperus (juniper)",
    (1, 25): "Myrrha (myrrh)",
    (1, 30): "Crocus sativus (saffron)",
    (1, 35): "Helichrysum (everlasting)",
    (1, 40): "Lavandula (lavender)",
    (1, 45): "Thymus vulgaris (thyme)",
    (1, 52): "Rosa (rose)",
    (1, 55): "Olea europaea (olive)",
    (1, 60): "Linum (linseed)",
    (1, 65): "Sesamum (sesame)",
    (1, 70): "Prunus dulcis (almond)",
    (1, 75): "Juglans regia (walnut)",
    (1, 80): "Ficus carica (fig)",
    (1, 85): "Morus nigra (mulberry)",
    (1, 90): "Malus/Pyrus (apple/pear)",
    (1, 95): "Punica granatum (pomegranate)",
    (1, 100): "Phoenix dactylifera (date palm)",
    (1, 105): "Myrtus communis (myrtle)",
    (1, 106): "Laurus nobilis (bay laurel)",
    (1, 110): "Cupressus (cypress)",
    (1, 115): "Salix (willow)",
    (1, 120): "Quercus (oak)",
    (1, 125): "Corylus (hazel)",
    (1, 128): "Platanus (plane tree)",
    (2, 100): "Hordeum (barley)",
    (2, 107): "Triticum (wheat)",
    (2, 120): "Lens culinaris (lentil)",
    (2, 130): "Lupinus (lupin)",
    (2, 140): "Brassica (cabbage)",
    (2, 145): "Beta vulgaris (beet)",
    (2, 150): "Lactuca sativa (lettuce)",
    (2, 155): "Cichorium (chicory)",
    (2, 160): "Asparagus",
    (2, 164): "Cyclamen (sowbread)",
    (2, 170): "Allium sativum (garlic)",
    (2, 175): "Allium cepa (onion)",
    (2, 180): "Sinapis (mustard)",
    (3, 1): "Alkanna tinctoria (alkanet)",
    (3, 3): "Gentiana lutea (gentian)",
    (3, 4): "Aristolochia (birthwort)",
    (3, 5): "Glycyrrhiza glabra (liquorice)",
    (3, 6): "Centaurium (centaury)",
    (3, 8): "Chamaeleon (carline thistle)",
    (3, 12): "Rheum (rhubarb)",
    (3, 13): "Rumex (dock/sorrel)",
    (3, 14): "Cynara/Scolymus (artichoke)",
    (3, 16): "Silybum marianum (milk thistle)",
    (3, 18): "Dipsacus (teasel)",
    (3, 19): "Iris florentina (Florentine iris)",
    (3, 22): "Eryngium (sea holly)",
    (3, 24): "Artemisia vulgaris (mugwort)",
    (3, 25): "Artemisia absinthium (wormwood)",
    (3, 28): "Chrysanthemum",
    (3, 30): "Inula helenium (elecampane)",
    (3, 32): "Arum maculatum (lords-and-ladies)",
    (3, 35): "Asphodelus (asphodel)",
    (3, 38): "Narcissus (daffodil)",
    (3, 40): "Lilium candidum (white lily)",
    (3, 45): "Allium ursinum (ramsons)",
    (3, 48): "Convolvulus (bindweed)",
    (3, 50): "Symphytum (comfrey)",
    (3, 52): "Daucus carota (wild carrot)",
    (3, 55): "Thapsia (deadly carrot)",
    (3, 58): "Anethum graveolens (dill)",
    (3, 62): "Pastinaca sativa (parsnip)",
    (3, 64): "Apium graveolens (celery)",
    (3, 65): "Smyrnium (alexanders)",
    (3, 66): "Petroselinum (parsley)",
    (3, 68): "Ferula communis (giant fennel)",
    (3, 70): "Verbascum (mullein)",
    (3, 72): "Aconitum (aconite)",
    (3, 73): "Conium maculatum (hemlock)",
    (3, 74): "Foeniculum vulgare (fennel)",
    (3, 75): "Rosmarinus officinalis (rosemary)",
    (3, 76): "Achillea millefolium (yarrow)",
    (3, 77): "Marrubium vulgare (horehound)",
    (3, 79): "Nigella/Melanthion (black cumin)",
    (3, 80): "Cuminum cyminum (cumin)",
    (3, 85): "Coriandrum sativum (coriander)",
    (3, 90): "Ruta graveolens (rue)",
    (3, 95): "Origanum vulgare (oregano)",
    (3, 100): "Thymbra (savory)",
    (3, 102): "Mentha (mint)",
    (3, 105): "Calamintha (calamint)",
    (3, 106): "Plantago major (plantain)",
    (3, 110): "Scrophularia (figwort)",
    (3, 112): "Salvia officinalis (sage)",
    (3, 115): "Betonica (betony)",
    (3, 118): "Sideritis (ironwort)",
    (3, 120): "Teucrium chamaedrys (germander)",
    (3, 125): "Ajuga chamaepitys (ground pine)",
    (3, 128): "Ballota nigra (black horehound)",
    (3, 130): "Clinopodium (wild basil)",
    (3, 132): "Ocimum basilicum (basil)",
    (3, 135): "Urtica (nettle)",
    (3, 137): "Galium (bedstraw)",
    (3, 139): "Galium aparine (cleavers)",
    (3, 140): "Paeonia (peony)",
    (3, 141): "Polygonum (knotgrass)",
    (3, 142): "Clematis",
    (3, 143): "Rubia tinctorum (madder)",
    (3, 145): "Crucianella (crosswort)",
    (3, 146): "Eupatorium (agrimony)",
    (3, 148): "Verbena officinalis (vervain)",
    (3, 150): "Sideritis syriaca (mountain tea)",
    (3, 152): "Lychnis (campion)",
    (3, 154): "Hypericum perforatum (St. Johns wort)",
    (3, 156): "Androsaenum (tutsan)",
    (3, 158): "Coris (shrubby savory)",
    (4, 1): "Echinops (globe thistle)",
    (4, 2): "Acanthus (bears breeches)",
    (4, 6): "Cirsium (plume thistle)",
    (4, 8): "Euphorbia (spurge)",
    (4, 15): "Euphorbia lathyris (caper spurge)",
    (4, 20): "Chamaesyce (prostrate spurge)",
    (4, 25): "Heliotropium (heliotrope)",
    (4, 30): "Helleborus niger (black hellebore)",
    (4, 35): "Ephedra (joint pine)",
    (4, 40): "Equisetum (horsetail)",
    (4, 45): "Polygala (milkwort)",
    (4, 50): "Bupleurum (hares ear)",
    (4, 55): "Convolvulus (bindweed)",
    (4, 60): "Verbena (verbena)",
    (4, 65): "Anagallis (pimpernel)",
    (4, 70): "Lithospermum (gromwell)",
    (4, 75): "Mandragora (mandrake)",
    (4, 77): "Aconitum napellus (monkshood)",
    (4, 80): "Hyoscyamus niger (henbane)",
    (4, 82): "Solanum nigrum (nightshade)",
    (4, 85): "Physalis (nightshade family)",
    (4, 90): "Datura stramonium (thorn apple)",
    (4, 95): "Papaver somniferum (opium poppy)",
    (4, 100): "Papaver rhoeas (corn poppy)",
    (4, 110): "Nymphaea (water lily)",
    (4, 115): "Sedum (stonecrop)",
    (4, 120): "Sempervivum (houseleek)",
    (4, 125): "Cotyledon (navelwort)",
    (4, 130): "Saxifraga (saxifrage)",
    (4, 134): "Adiantum (maidenhair fern)",
    (4, 136): "Pteridium (bracken)",
    (4, 138): "Asplenium (spleenwort)",
    (4, 140): "Polypodium (polypody)",
    (4, 145): "Dryopteris (wood fern)",
    (4, 150): "Lycopodium (clubmoss)",
    (4, 160): "Usnea (lichen)",
    (4, 165): "Agaricus (mushroom)",
    (4, 175): "Laminaria (seaweed)",
    (4, 186): "Spongia (sponge)",
    (5, 1): "Vitis vinifera (grape vine)",
    (5, 2): "Vinum (wine varieties)",
    (5, 5): "Gleukos (grape must)",
    (5, 8): "Acetum (vinegar)",
    (5, 10): "Mel (mead)",
    (5, 13): "Oxymeli (oxymel)",
    (5, 20): "Zythos (beer)",
    (5, 25): "Aloe vera (aloe)",
    (5, 30): "Opobalsamon (balsam)",
    (5, 40): "Asphaltum (bitumen)",
    (5, 50): "Sulphur",
    (5, 60): "Cadmia (zinc oxide)",
    (5, 70): "Lithargyros (litharge)",
    (5, 80): "Molybdos (lead)",
    (5, 90): "Cuprum (copper)",
    (5, 100): "Aerugo (verdigris)",
    (5, 110): "Ferrum (iron)",
    (5, 120): "Haematites (hematite)",
    (5, 130): "Gypsum",
    (5, 140): "Calx (lime)",
    (5, 150): "Sal (salt)",
    (5, 159): "Terra Lemnia (Lemnian earth)",
}

# =============================================================================
# Herbal folios
# =============================================================================
HERBAL_FOLIOS = list(range(1, 12)) + list(range(13, 58))

print("\n" + "="*80)
print("PREDICTED DIOSCORIDES MAPPING FOR ALL HERBAL FOLIOS")
print("="*80)

results = []
for folio in HERBAL_FOLIOS:
    pred_linear = slope * folio + intercept
    pred_linear = max(1, min(TOTAL_CHAPTERS, pred_linear))
    book, chapter = linear_to_book_chapter(pred_linear)

    best_key = None
    best_dist = 999
    for (b, c) in DIOSCORIDES_PLANTS:
        dist = abs(book_chapter_to_linear(b, c) - pred_linear)
        if dist < best_dist:
            best_dist = dist
            best_key = (b, c)

    plant_name = DIOSCORIDES_PLANTS.get(best_key, "Unknown")
    is_anchor = folio in ANCHORS

    results.append({
        'folio': folio,
        'pred_linear': pred_linear,
        'book': book,
        'chapter': chapter,
        'nearest_key': best_key,
        'plant': plant_name,
        'is_anchor': is_anchor,
        'nearest_dist': best_dist,
    })

    anchor_str = " *** ANCHOR ***" if is_anchor else ""
    print(f"  f{folio:2d}r -> linear {pred_linear:6.1f} -> Book {book}, Ch.{chapter:3d} ~= {best_key[0]}.{best_key[1]:3d} {plant_name}{anchor_str}")

# =============================================================================
# Folio grouping by book
# =============================================================================
print("\n" + "="*80)
print("FOLIO GROUPING BY PREDICTED DIOSCORIDES BOOK")
print("="*80)

book_folios = {}
for r in results:
    b = r['book']
    if b not in book_folios:
        book_folios[b] = []
    book_folios[b].append(r['folio'])

book_descriptions = {
    1: "Aromatics, oils, trees, shrubs, gums, fruits",
    2: "Animals, honey, cereals, vegetables",
    3: "Roots, juices, herbs, seeds (core herbal)",
    4: "More herbs, ferns, mosses, fungi",
    5: "Wines, minerals, metals",
}

for book in sorted(book_folios.keys()):
    folios = book_folios[book]
    desc = book_descriptions.get(book, "")
    flist = ", ".join(f"f{f}r" for f in folios)
    print(f"\n  Book {book}: {desc}")
    print(f"  Folios ({len(folios)}): {flist}")

# =============================================================================
# Parse EVA and compute word frequencies by book
# =============================================================================
eva_path = "C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt"
with open(eva_path, 'r', encoding='utf-8') as f:
    eva_text = f.read()

folio_texts = {}
current_folio = None
for line in eva_text.split('\n'):
    m = re.match(r'<f(\d+)([rv])>', line)
    if m:
        current_folio = (int(m.group(1)), m.group(2))
        if current_folio not in folio_texts:
            folio_texts[current_folio] = []
        continue

    if current_folio and current_folio[0] in HERBAL_FOLIOS:
        clean = re.sub(r'<[^>]+>', '', line)
        clean = re.sub(r'@\d+;?', '', clean)
        clean = re.sub(r'\{[^}]+\}', '', clean)
        clean = re.sub(r'[,\.\?\!]', ' ', clean)
        words = clean.split()
        all_words = [w.strip() for w in words if w.strip() and len(w.strip()) > 1 and w.strip().isalpha()]
        folio_texts[current_folio].extend(all_words)

folio_book_map = {}
for r in results:
    folio_book_map[r['folio']] = r['book']

book_word_counts = {}
book_total_words = {}
for (fnum, side), words in folio_texts.items():
    if fnum in folio_book_map:
        book = folio_book_map[fnum]
        if book not in book_word_counts:
            book_word_counts[book] = Counter()
            book_total_words[book] = 0
        book_word_counts[book].update(words)
        book_total_words[book] += len(words)

print("\n" + "="*80)
print("WORD FREQUENCY ANALYSIS BY PREDICTED DIOSCORIDES BOOK")
print("="*80)

for book in sorted(book_word_counts.keys()):
    total = book_total_words[book]
    top20 = book_word_counts[book].most_common(20)
    print(f"\n  Book {book} ({book_descriptions.get(book, '')}):")
    print(f"  Total words: {total}")
    print(f"  Top 20: {', '.join(f'{w}({c})' for w,c in top20)}")

# Cross-book comparison
print("\n" + "="*80)
print("CROSS-BOOK VOCABULARY DIFFERENCES")
print("="*80)

all_books = sorted(book_word_counts.keys())
for i, b1 in enumerate(all_books):
    for b2 in all_books[i+1:]:
        set1 = set(book_word_counts[b1].keys())
        set2 = set(book_word_counts[b2].keys())
        shared = set1 & set2
        only1 = set1 - set2
        only2 = set2 - set1
        jaccard = len(shared) / len(set1 | set2) if (set1 | set2) else 0
        print(f"\n  Book {b1} vs Book {b2}:")
        print(f"    Shared: {len(shared)}, Only B{b1}: {len(only1)}, Only B{b2}: {len(only2)}")
        print(f"    Jaccard: {jaccard:.3f}")

        top_b1_only = sorted(only1, key=lambda w: book_word_counts[b1][w], reverse=True)[:10]
        top_b2_only = sorted(only2, key=lambda w: book_word_counts[b2][w], reverse=True)[:10]
        if top_b1_only:
            freqs1 = ', '.join(f'{w}({book_word_counts[b1][w]})' for w in top_b1_only)
            print(f"    Top B{b1}-only: {freqs1}")
        if top_b2_only:
            freqs2 = ', '.join(f'{w}({book_word_counts[b2][w]})' for w in top_b2_only)
            print(f"    Top B{b2}-only: {freqs2}")

# =============================================================================
# Output full table
# =============================================================================
print("\n" + "="*80)
print("FULL PREDICTION TABLE")
print("="*80)
print("| Folio | Pred.Lin | Book | Ch. | Nearest Known Entry | Note |")
print("|-------|----------|------|-----|---------------------|------|")
for r in results:
    conf = "ANCHOR" if r['is_anchor'] else f"d={r['nearest_dist']:.0f}"
    print(f"| f{r['folio']}r | {r['pred_linear']:.1f} | {r['book']} | {r['chapter']} | {r['plant']} | {conf} |")
