# Convergence Metric Retest

## Goal

Determine whether the convergence metric graduates after the Pipeline v2
changes (input restructuring, multi-option generation, input-aware detection).

## Pre-check: value-conflict stance effectiveness

Before the full retest, test whether the value-conflict stance entries
(spec 3.1(f)) actually influence model behavior.

1. For each of Kallya and Nadja, write 2-3 dilemma scenarios where the
   character's operating code conflicts with the "correct" (conventionally
   decent) action.
2. Run each scenario twice against the generated character: once with the
   stance entry present in the character notes, once with it removed.
3. Compare the two responses per scenario for whether the character's choice,
   and the stated lever/guilt behavior, follow the stance entry's declared
   direction (role-following / role-compromise / alignment-compromise /
   alignment-following) or default back to the alignment-consistent choice
   regardless.
4. Record the result per scenario. If the stance entry shows no measurable
   effect on model behavior in a majority of scenarios for a character, note
   this explicitly and flag it for the graduation assessment below — the
   entry may still carry documentation value even if the model does not act
   on it at inference time. Do not block the full retest on this outcome.

## Method

1. Generate character notes for Kallya and Nadja using the Pipeline v2 flow
   with at least 3 models, split so both cross-provider and within-family
   comparisons are possible: either 2 Claude + 1 GPT, or 1 Claude + 2 GPT.
2. Run input-echo detection on all outputs.
3. Run two-judge convergence detection (same judges as the original
   experiment: Opus-class, GPT-class).
4. Apply input-aware filtering: remove findings categorized as input-echo.
5. Generate corrections for the filtered (post-input-echo-removal) findings.
   Correction generation is mandatory, not optional — the correction-value
   criterion below cannot be assessed without it.
6. Human-review the filtered findings and their corrections: mark each
   finding true/false positive, and mark each correction as improving or not
   improving the flagged text.
7. Assess against four graduation criteria, each with a concrete threshold:

   - **Precision:** true-positive rate among filtered findings must exceed
     the original experiment's baseline of 61%. The original run cleared 61%
     but was judged not to meet the bar because the true positives were
     dominated by input-echo rather than genuine slop; Pipeline v2's
     input-aware filtering exists specifically to correct that. A pass
     requires precision above 61% on findings that survive input-echo
     filtering.
   - **Cross-provider signal:** the convergence rate for cross-provider pairs
     (Claude+GPT) must differ from the convergence rate for within-family
     pairs (Claude+Claude, or GPT+GPT if the model mix allows it) by at
     least 10 percentage points. Report both rates and the delta explicitly.
   - **Correction value:** among filtered true-positive findings, corrections
     must be marked "improving" more often than "not improving" (i.e. > 50%
     of reviewed corrections improve the text). This criterion fails if
     corrections were not generated.
   - **Consistency:** Kallya and Nadja must reach the same pass/fail verdict
     on each of the three criteria above. If one character passes a
     criterion and the other fails it, consistency fails for that criterion
     — report per-character results, not just an average.

## Decision rule

All four criteria must hold, for both characters, to graduate the mechanism
as a whole. The reviewer may graduate individual detection methods (e.g.
input-echo detection alone, or one judge pairing) rather than the full
mechanism if only some criteria pass. If the metric still does not graduate,
document what remains unresolved, including whether the value-conflict
stance pre-check surfaced anything relevant to the assessment.

## Output

Write results to this directory and update inbox item 9 with the outcome.
