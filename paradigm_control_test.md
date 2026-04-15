# Paradigm Completeness Control Test: Red Team Analysis

**Date**: 2026-04-06
**Analyst**: Claude Opus 4.6
**Purpose**: Determine whether 87.3% paradigm completeness actually distinguishes the Voynich manuscript from natural languages
**Script**: `paradigm_control_test.py`

---

## The Claim Under Test

The original constructed notation analysis (`constructed_notation_test.md`) reported:

> "Average paradigm completeness: 87.3%"
> "Natural language expected: 30-60%"
> "Fully designed notation expected: 90-100%"
> "STRONGLY SUPPORTS CONSTRUCTED NOTATION."

The 30-60% benchmark for natural language was **never validated on real data**. This analysis tests whether 87.3% is actually unusual.

---

## Method

The Voynich paradigm completeness was measured by:
1. Segmenting all words into PREFIX + ROOT + SUFFIX using a predefined morpheme list
2. Taking the **10 most common prefixes** and **15 most common roots**
3. Building a 10x15 matrix: does prefix P appear with root R anywhere in the corpus?
4. Counting filled cells / total cells = paradigm completeness

We apply the same logic to real and simulated languages.

---

## Results

### Summary Table

| Language/System | Paradigm Completeness | Notes |
|---|---|---|
| English (un/re/pre/dis/over) | **45.0%** | Fusional, limited prefix productivity |
| Latin (pharmaceutical vocabulary) | **77.0%** | Highly productive prefixation |
| Swahili model (Bantu verb paradigm) | **95.3%** | Natural language, near-complete paradigm |
| Turkish model (suffix-only, pseudo-prefixes) | **30.0%** | Algorithm applied to wrong morphology type |
| | | |
| Simulated: 0% gaps | 100.0% | Perfect paradigm |
| Simulated: 10% gaps | 92.7% | |
| Simulated: 20% gaps | 82.7% | |
| Simulated: 30% gaps | 66.7% | |
| Simulated: 40% gaps | 60.0% | |
| Simulated: 50% gaps | 54.0% | |
| Simulated: 60% gaps | 48.7% | |
| Simulated: 70% gaps | 37.3% | |
| | | |
| **VOYNICH MANUSCRIPT** | **87.3%** | Equivalent to ~15% gap rate |

---

### English Control (45.0%)

Applied the test to 5 common English prefixes (un-, re-, pre-, dis-, over-) x 20 common verb roots. English is fusional and has limited prefix productivity, so low completeness is expected and unsurprising. The 30-60% "natural language" benchmark seems calibrated to fusional European languages.

Key finding: `re-` achieves 80% completeness (combines with 16/20 roots). Individual prefix productivity varies enormously: `dis-` achieves only 15%.

### Latin Control (77.0%)

Latin verbal prefixes are genuinely productive. Ten common prefixes (con-, de-, ex-, in-, per-, prae-, pro-, re-, sub-, trans-) were tested against 20 common pharmaceutical/medical verb roots.

| Prefix | Completeness |
|---|---|
| re- | 100% (20/20) |
| con- | 95% (19/20) |
| de- | 85% (17/20) |
| ex- | 85% (17/20) |
| in- | 80% (16/20) |
| pro- | 80% (16/20) |
| sub- | 80% (16/20) |
| per- | 60% (12/20) |
| prae- | 55% (11/20) |
| trans- | 50% (10/20) |

**Average: 77.0%** -- well above the claimed 30-60% ceiling for natural language.

Latin is a natural language. Its high paradigm completeness comes from genuinely productive prefixation where most prefix+root combinations yield real, attested Latin words. If the Voynich encodes a Latin-influenced pharmaceutical vocabulary, 87.3% is completely expected.

### Swahili (Bantu) Model (95.3%)

Swahili verb morphology uses subject prefixes (ni-, u-, a-, tu-, m-, wa-) combined with tense markers (na-, li-, ta-, me-, si-) to create 30 combined prefixes, each of which can attach to virtually any verb root.

**Result: 95.3% paradigm completeness** -- HIGHER than the Voynich.

This is a natural language with naturally near-complete paradigms. In Bantu languages, every person can perform every action in every tense; the paradigm is complete by design of the language itself, not by human construction.

### Turkish Control (30.0%)

Turkish is purely suffixing. When the Voynich segmentation algorithm treats word-initial character sequences as "prefixes," it produces low completeness because the pseudo-prefixes are actually different verb stems, each with its own suffix patterns.

This confirms the algorithm CAN detect the difference between real prefix systems and non-prefix systems. But it cannot distinguish natural prefix-productive languages from constructed ones.

---

## Method Sensitivity Analysis

### Does selecting top-N inflate the score?

We generated a language with a TRUE gap rate of 40% (true completeness: 60.8%) and measured with varying N:

| N_prefix | N_roots | Measured Completeness |
|---|---|---|
| 3 | 15 | 64.4% |
| 5 | 15 | 64.0% |
| 10 | 15 | 62.0% (Voynich method) |
| 15 | 15 | 62.2% |
| 20 | 15 | 63.0% |
| 30 | 15 | 62.2% |

**Selection bias inflation: +1.2 percentage points** for the Voynich method (10x15).

Finding: The inflation from top-N selection is **modest** (~1-5 pp) for this simulated case. The method is not dramatically biased by selection, at least in this controlled setting.

### Voynich sensitivity to N

The Voynich score varies substantially with N:

| N_prefix | N_roots | Completeness |
|---|---|---|
| 5 | 10 | 96.0% |
| 5 | 15 | 89.3% |
| 5 | 20 | 85.0% |
| 5 | 30 | 82.0% |
| 10 | 15 | **87.3%** (reported) |
| 10 | 30 | 78.3% |
| 15 | 30 | 77.1% |
| 20 | 30 | 69.8% |

The score drops to **69.8%** with 20 prefixes x 30 roots. The 87.3% figure is real but depends on the specific N chosen. With broader parameters, the Voynich's completeness overlaps heavily with Latin (77%).

---

## Corpus Size Effect

A language with 40% true gaps, measured at different corpus sizes:

| Corpus Size | Measured Completeness | Inflation |
|---|---|---|
| 1,000 | 58.0% | -2.0 pp |
| 5,000 | 62.7% | +2.7 pp |
| 10,000 | 60.0% | +0.0 pp |
| 37,000 | 62.7% | +2.7 pp |
| 100,000 | 62.7% | +2.7 pp |

Corpus size has a modest effect. The Voynich corpus (37,781 words) is large enough that most valid combinations have been observed. This is not a major confound.

---

## Critical Findings

### 1. The 30-60% benchmark is wrong

The claimed "natural language: 30-60%" range appears to be based on fusional European languages (English, German, etc.) where prefix productivity is limited. It does not account for:

- **Latin**: 77% completeness with productive prefixation
- **Bantu languages (Swahili)**: 95%+ completeness with systematic person/tense prefixes
- **Other prefix-productive languages**: Georgian, many Bantu and Austronesian languages

### 2. The Voynich's 87.3% is compatible with natural language

The Voynich falls between Latin (77%) and Swahili (95%). If the Voynich text represents a language or notation system with productive prefixation -- which the analysis assumes it does, since it defines a prefix list -- then 87% is unremarkable. It corresponds to roughly 10-15% lexical gaps, which is normal for productive morphological systems.

### 3. The measurement assumes what it tries to prove

The Voynich test uses a **predefined prefix list** designed to match Voynich morphology. The test then asks: "Do these prefixes combine with common roots?" But the prefixes were identified precisely BECAUSE they frequently appear before roots. This is a form of circular reasoning:

1. Find character sequences that frequently begin words -> call them "prefixes"
2. Find character sequences that frequently follow prefixes -> call them "roots"
3. Check whether prefixes combine with roots -> surprise, they do

Any text with regular word-initial patterns will score high on this test, whether those patterns are true morphological prefixes or just frequent character sequences.

### 4. What WOULD distinguish constructed from natural?

The paradigm completeness test, as designed, cannot distinguish:
- A natural language with productive prefixation (Latin, Swahili)
- A constructed notation with systematic combinatorics

Better discriminators would be:
- **Irregularity patterns**: Natural languages accumulate irregular forms (strong verbs, suppletive plurals). Constructed systems don't. This is testable.
- **Frequency-productivity correlation**: In natural languages, the most frequent morphemes are often the most irregular (be/am/is/are/was/were). In constructed systems, frequency and regularity are independent.
- **Semantic coherence of gaps**: In natural languages, paradigm gaps have semantic reasons (*un-go, *dis-run are blocked because they're semantically odd). In constructed systems, gaps are random or absent.
- **Diachronic evidence**: Natural languages show historical sound changes that create allomorphy (in-/im-/ir-/il- in Latin). Constructed systems show uniform allomorphs.

---

## Verdict

**The claim "87.3% paradigm completeness is incompatible with natural language (30-60%)" is UNFOUNDED.**

- The 30-60% benchmark was never validated and is wrong for prefix-productive languages
- Latin achieves 77% with natural morphology
- Swahili achieves 95% with natural morphology
- The Voynich's 87.3% is consistent with a language that has productive prefixation and 10-15% lexical gaps, which describes many natural languages
- The score drops to 70% with broader N parameters, overlapping with Latin
- The measurement method has modest selection bias but more critically assumes the existence of the morphological categories it then tests for

**87.3% paradigm completeness is evidence that the Voynich has productive prefix morphology. It is NOT evidence that this morphology is artificial rather than natural.**

---

## Files

- Script: `C:\Users\kazuk\Downloads\voynich_analysis\paradigm_control_test.py`
- Report: `C:\Users\kazuk\Downloads\voynich_analysis\paradigm_control_test.md`
- Original claim: `C:\Users\kazuk\Downloads\voynich_analysis\constructed_notation_test.md` (Test 2, line 76)
- Original script: `C:\Users\kazuk\Downloads\voynich_analysis\constructed_notation_test.py`
