# Writing Style Trial — Results

## Blind Key

| Letter | Condition |
|--------|-----------|
| W | C (BLUF) |
| X | A (STE-100 strict) |
| Y | B (STE-100 loose) |
| Z | 0 (Baseline) |

## Impressions (from reviewer, blind)

**W (BLUF):** Overall writing quality much better, though some contents don't make a ton of sense — possibly attributable to inputs. Content is easier to fix than writing quality later on.

**X (STE-100 strict):** A little worse than W, but more concise which is a bonus. Same content problems.

**Y (STE-100 loose):** Pretty close to W.

**Z (Baseline):** Beside the content issues present throughout, this one reads notably better than all the others.

## Ranking

Z > W = Y > X

Baseline > BLUF = STE-100 loose > STE-100 strict

## Adoption Decision

No condition graduates. The baseline (current writing-style.md) produced the best output. The experimental conditions did not improve over it.

## Observations

The reviewer noted that all conditions have content problems attributable to the inputs rather than the writing style. Writing quality across all conditions was acceptable (unlike the previous pipeline quality trial). Key takeaways:

1. Content is now the main issue, not writing quality. Content is easier to fix than writing quality.
2. A more hands-on human-in-the-loop process throughout generation may handle the content problem better than automated pipeline changes.
3. The Design Notes would change from a direct generation input to more of a record, with human review at each stage.
4. The semantic anchor approach (naming a writing standard) did not outperform the existing ban-list approach in this test, but the gap was small and the direction shows promise.
5. Pending core workflow changes may also affect this area.
