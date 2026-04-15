"""
Extract word frequencies per herbal folio from EVA transcription.
Identify high-frequency words (100+ occurrences across herbal section).
"""
import re
import json
from collections import Counter, defaultdict

# Read the transcription
with open(r'C:\Users\kazuk\Downloads\voynich_analysis\RF1b-e.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Parse folios and their text
herbal_folios = []
current_folio = None
current_is_herbal = False
folio_texts = defaultdict(list)

for line in lines:
    line = line.strip()
    # Check for folio header
    header_match = re.match(r'<(f\d+[rv]\d?)>\s+<!(.*)>', line)
    if header_match:
        current_folio = header_match.group(1)
        attrs = header_match.group(2)
        current_is_herbal = '$I=H' in attrs
        if current_is_herbal:
            herbal_folios.append(current_folio)
        continue

    # Check for folio start without header (just folio marker)
    folio_start = re.match(r'<(f\d+[rv]\d?)>', line)
    if folio_start:
        current_folio = folio_start.group(1)
        continue

    # Extract text content from lines
    if current_folio and current_is_herbal:
        # Lines look like: <f1v.1,@P0>  text here
        text_match = re.match(r'<[^>]+>\s+(.*)', line)
        if text_match:
            text = text_match.group(1)
            # Clean up EVA markup
            text = re.sub(r'<[^>]*>', '', text)  # remove tags
            text = re.sub(r'\{[^}]*\}', '', text)  # remove uncertain readings
            text = re.sub(r'@\d+;?', '', text)  # remove special chars
            text = re.sub(r'[,.\-?!\'"]', ' ', text)  # punctuation to space
            # Extract words
            words = [w.strip() for w in text.split() if w.strip() and len(w.strip()) > 0]
            folio_texts[current_folio].extend(words)

# Count total word frequencies across all herbal pages
total_counts = Counter()
per_folio_counts = {}

for folio in herbal_folios:
    words = folio_texts[folio]
    per_folio_counts[folio] = Counter(words)
    total_counts.update(words)

# High-frequency words (100+)
high_freq = {w: c for w, c in total_counts.items() if c >= 100}

print(f"Total herbal folios: {len(herbal_folios)}")
print(f"Total words in herbal section: {sum(total_counts.values())}")
print(f"Unique words: {len(total_counts)}")
print(f"Words with 100+ occurrences: {len(high_freq)}")
print()
print("HIGH-FREQUENCY WORDS (100+ occurrences):")
print("=" * 50)
for word, count in sorted(high_freq.items(), key=lambda x: -x[1]):
    # Count how many folios contain this word
    folio_presence = sum(1 for f in herbal_folios if word in per_folio_counts[f])
    print(f"  {word:20s}  {count:5d} occurrences  in {folio_presence:3d}/{len(herbal_folios)} folios")

# Also check words with 50+ for near-misses
print()
print("NEAR-MISS WORDS (50-99 occurrences):")
print("=" * 50)
near_miss = {w: c for w, c in total_counts.items() if 50 <= c < 100}
for word, count in sorted(near_miss.items(), key=lambda x: -x[1]):
    folio_presence = sum(1 for f in herbal_folios if word in per_folio_counts[f])
    print(f"  {word:20s}  {count:5d} occurrences  in {folio_presence:3d}/{len(herbal_folios)} folios")

# Save per-folio word frequency data for correlation analysis
output = {
    'herbal_folios': herbal_folios,
    'high_freq_words': sorted(high_freq.keys()),
    'per_folio_counts': {f: dict(per_folio_counts[f]) for f in herbal_folios},
    'total_counts': dict(total_counts)
}

with open(r'C:\Users\kazuk\Downloads\voynich_analysis\herbal_word_data.json', 'w') as f:
    json.dump(output, f, indent=2)

print()
print("Data saved to herbal_word_data.json")

# ch/sh analysis
print()
print("CH vs SH MORPHEME ANALYSIS:")
print("=" * 50)
ch_words = {w: c for w, c in total_counts.items() if 'ch' in w and c >= 50}
sh_words = {w: c for w, c in total_counts.items() if 'sh' in w and c >= 50}
print(f"Words containing 'ch' with 50+ occurrences: {len(ch_words)}")
for w, c in sorted(ch_words.items(), key=lambda x: -x[1])[:20]:
    print(f"  {w:20s}  {c}")
print(f"\nWords containing 'sh' with 50+ occurrences: {len(sh_words)}")
for w, c in sorted(sh_words.items(), key=lambda x: -x[1])[:20]:
    print(f"  {w:20s}  {c}")

# Per-folio ch/sh ratio
print()
print("PER-FOLIO ch-count vs sh-count:")
for folio in herbal_folios[:10]:
    words = folio_texts[folio]
    ch_count = sum(1 for w in words if 'ch' in w)
    sh_count = sum(1 for w in words if 'sh' in w)
    total = len(words)
    print(f"  {folio}: total={total}, ch={ch_count}, sh={sh_count}, ch/sh={ch_count/max(sh_count,1):.2f}")
