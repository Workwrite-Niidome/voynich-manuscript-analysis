import re
import sys
from collections import Counter

def extract_folio_text(filename, folio_id):
    """Extract all text tokens for a given folio."""
    lines = open(filename, 'r', encoding='utf-8').readlines()
    in_folio = False
    tokens = []
    folio_pattern = re.compile(r'^<' + re.escape(folio_id) + r'[\.\s>]')
    next_folio = re.compile(r'^<f\d+[rv]>\s')
    
    for line in lines:
        line = line.strip()
        if folio_pattern.match(line):
            in_folio = True
        elif in_folio and next_folio.match(line) and not line.startswith('<' + folio_id):
            break
        
        if in_folio and ',' in line:
            # Extract text after the folio identifier
            parts = line.split('>', 1)
            if len(parts) > 1:
                text = parts[-1].strip()
                # Remove annotations like @221; {cto} etc
                text = re.sub(r'@\d+;?', '', text)
                text = re.sub(r'\{[^}]+\}', '', text)
                text = re.sub(r'<->', ' ', text)
                text = re.sub(r'[,?!]', '', text)
                # Split into tokens
                words = [w.strip() for w in text.replace('.', ' ').split() if len(w.strip()) > 1]
                tokens.extend(words)
    return tokens

def count_stems(tokens):
    """Count stem frequencies. A stem is the base form ignoring common suffixes."""
    stem_counter = Counter()
    for token in tokens:
        stem_counter[token] += 1
    return stem_counter

# All herbal folios we examined (pages 3-18 = f1r through f8v, plus f9r-f11v)
folios = [
    'f1r', 'f1v', 'f2r', 'f2v', 'f3r', 'f3v',
    'f4r', 'f4v', 'f5r', 'f5v', 'f6r', 'f6v',
    'f7r', 'f7v', 'f8r', 'f8v', 'f9r', 'f9v',
    'f10r', 'f10v', 'f11r', 'f11v', 'f13r', 'f13v',
    'f14r', 'f14v', 'f15r', 'f15v', 'f16r', 'f16v',
    'f17r', 'f17v', 'f18r', 'f18v', 'f19r', 'f19v',
    'f20r', 'f20v', 'f21r', 'f21v',
    'f22r', 'f22v', 'f23r', 'f23v',
    'f24r', 'f24v', 'f25r', 'f25v',
]

filename = "C:/Users/kazuk/Downloads/voynich_analysis/RF1b-e.txt"

# Print word counts per folio
for folio in folios:
    tokens = extract_folio_text(filename, folio)
    counts = count_stems(tokens)
    
    # Count specific stems of interest
    chol_count = sum(v for k, v in counts.items() if 'chol' in k)
    chor_count = sum(v for k, v in counts.items() if k == 'chor')
    shol_count = sum(v for k, v in counts.items() if k == 'shol')
    daiin_count = sum(v for k, v in counts.items() if 'daiin' in k)
    cthy_count = sum(v for k, v in counts.items() if k == 'cthy')
    dar_count = sum(v for k, v in counts.items() if k == 'dar')
    qo_words = sum(v for k, v in counts.items() if k.startswith('qo'))
    chey_count = sum(v for k, v in counts.items() if k == 'chey')
    shey_count = sum(v for k, v in counts.items() if k == 'shey')
    ol_count = sum(v for k, v in counts.items() if k == 'ol')
    or_count = sum(v for k, v in counts.items() if k == 'or')
    dain_count = sum(v for k, v in counts.items() if k == 'dain')
    sho_count = sum(v for k, v in counts.items() if k == 'sho')
    chy_count = sum(v for k, v in counts.items() if k == 'chy')
    dam_count = sum(v for k, v in counts.items() if k == 'dam' or k == 'cham')
    cham_count = sum(v for k, v in counts.items() if k == 'cham')
    chom_count = sum(v for k, v in counts.items() if k == 'chom')
    cthol_count = sum(v for k, v in counts.items() if k == 'cthol')
    okal_count = sum(v for k, v in counts.items() if k == 'okal' or k == 'okol')
    shody_count = sum(v for k, v in counts.items() if k == 'shody')
    otaiin_count = sum(v for k, v in counts.items() if k == 'otaiin')
    cheey_count = sum(v for k, v in counts.items() if 'cheey' in k or 'eey' in k)
    okeey_count = sum(v for k, v in counts.items() if 'keey' in k)
    dal_count = sum(v for k, v in counts.items() if k == 'dal')
    dol_count = sum(v for k, v in counts.items() if k == 'dol')
    
    total = len(tokens)
    print(f"{folio}\ttotal={total}\tchol*={chol_count}\tchor={chor_count}\tshol={shol_count}\tdaiin*={daiin_count}\tdar={dar_count}\tqo*={qo_words}\tchey={chey_count}\tshey={shey_count}\tdain={dain_count}\tsho={sho_count}\tdam/cham={dam_count}\tchom={chom_count}\tcthol={cthol_count}\t*eey={cheey_count}\tdal={dal_count}\tdol={dol_count}\tshody={shody_count}\totaiin={otaiin_count}")

print("\n\n=== FULL WORD FREQUENCY (all herbal folios combined) ===")
all_tokens = []
for folio in folios:
    all_tokens.extend(extract_folio_text(filename, folio))

total_counts = Counter(all_tokens)
for word, count in total_counts.most_common(80):
    print(f"  {word}: {count}")
