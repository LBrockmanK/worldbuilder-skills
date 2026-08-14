# Pipeline Quality Trial — Results

## Blind Key

| Letter | Condition |
|--------|-----------|
| W | B (input restructuring) |
| X | 0 (baseline) |
| Y | C (decomposition step) |
| Z | A (fail-check gate) |

## Scores (holistic 1-3, blind human review)

### Condition 0 (Baseline) — Letter X

| Entry | Score |
|-------|-------|
| X-1 | 2 |
| X-2 | 2 |
| X-3 | 3 |
| X-4 | 2 |
| X-5 | 2 |
| X-6 | 2 |
| X-7 | 2 |
| X-8 | 2 |
| X-9 | 1 |
| X-10 | 2 |
| X-11 | 1 |
| X-12 | 2 |
| X-13 | 1 |
| X-14 | 2 |
| X-15 | 2 |
| X-16 | 1 |
| X-17 | 2 |
| X-18 | 1 |
| X-19 | 1 |
| X-20 | 1 |
| **Mean** | **1.70** |

### Condition A (Fail-check gate) — Letter Z

| Entry | Score |
|-------|-------|
| Z-1 | 2 |
| Z-2 | 1 |
| Z-3 | 1 |
| Z-4 | 2 |
| Z-5 | 1 |
| Z-6 | 2 |
| Z-7 | 1 |
| Z-8 | 1 |
| Z-9 | 1 |
| Z-10 | 1 |
| Z-11 | 2 |
| Z-12 | 1 |
| Z-13 | 1 |
| Z-14 | 1 |
| Z-15 | 1 |
| Z-16 | 1 |
| Z-17 | 1 |
| Z-18 | 1 |
| Z-19 | 1 |
| Z-20 | 1 |
| **Mean** | **1.10** |

### Condition B (Input restructuring) — Letter W

| Entry | Score |
|-------|-------|
| W-1 | 2 |
| W-2 | 1 |
| W-3 | 1 |
| W-4 | 2 |
| W-5 | 1 |
| W-6 | 2 |
| W-7 | 1 |
| W-8 | 1 |
| W-9 | 1 |
| W-10 | 1 |
| W-11 | 1 |
| W-12 | 1 |
| W-13 | 1 |
| W-14 | 1 |
| W-15 | 2 |
| W-16 | 1 |
| W-17 | 1 |
| W-18 | 1 |
| W-19 | 1 |
| W-20 | 1 |
| **Mean** | **1.10** |

### Condition C (Decomposition step) — Letter Y

| Entry | Score |
|-------|-------|
| Y-1 | 1 |
| Y-2 | 1 |
| Y-3 | 1 |
| Y-4 | 1 |
| Y-5 | 1 |
| Y-6 | 1 |
| Y-7 | 1 |
| Y-8 | 1 |
| Y-9 | 1 |
| Y-10 | 1 |
| Y-11 | 1 |
| Y-12 | 1 |
| Y-13 | 1 |
| Y-14 | 1 |
| Y-15 | 1 |
| Y-16 | 1 |
| Y-17 | 1 |
| Y-18 | 1 |
| Y-19 | 1 |
| Y-20 | 1 |
| **Mean** | **1.00** |

## Summary

| Condition | Mean | vs Baseline |
|-----------|------|-------------|
| 0 (Baseline) | 1.70 | — |
| A (Fail-check gate) | 1.10 | -0.60 |
| B (Input restructuring) | 1.10 | -0.60 |
| C (Decomposition step) | 1.00 | -0.70 |

## Adoption Decision

**Negative result.** No condition improved over baseline. All three experimental conditions degraded quality, with degradation increasing as more pipeline stages were added. The current pipeline stands unchanged.

Per spec D5: no condition exceeded baseline by 0.3 on the quality dimension. Per spec D15 (as amended): individual S-findings (S1, S3, S6) remain open for future separate testing, since this bundled null result cannot establish that each lead is individually ineffective.

## Mechanical Divergence Data

Fail-check (Jaccard similarity) results from `results/divergence-condition-*.json`:
- Condition 0: 1 failure out of 20 entries (entry 6 run 1, Jaccard 0.255)
- Condition A: 0 failures out of 20 entries
- Condition B: 1 failure out of 20 entries
- Condition C: 0 failures out of 20 entries

The mechanical gate did reduce measured divergence failures, but this did not translate to quality improvement.

## Qualitative Observations (from reviewer)

1. **Input quality problem:** Kallya's stored Design Notes are poor and don't reflect the corrected final product. The generation agent modified inputs without oversight, losing nuances (e.g., the old settlement extortion-to-personal-connection arc).
2. **Functional purpose mismatch:** These sheets are functional AI portrayal guidelines, not literary prose. Vague, implication-heavy language with entries that lead in without context is unusable for that purpose. This may conflict with some writing style guidelines.
3. **Em-dash ban not enforced:** All conditions produced heavy em-dash usage despite the prose ban in writing-style.md.
4. **Overwrought prose:** Excessively technical language mixed with overwrought literary phrasing — "none of these sound anything like how a human would type."
5. **Quality degradation pattern:** Each additional pipeline stage added more processing between the source facts and the output, and quality dropped at every stage. More processing did not improve output; it degraded it.
