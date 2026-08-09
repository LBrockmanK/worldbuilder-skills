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
   Retain the 3-variant spreads from generation (before synthesis) for
   within-model convergence analysis in step 3b.
2. Run input-echo detection on all outputs.
3. Run convergence detection from two sources:
   a. **Cross-model convergence** (same as original experiment): two-judge
      detection (Opus-class, GPT-class) comparing outputs across models.
   b. **Within-model convergence** (new): for each entry's 3-variant spread,
      measure how similar the three variants are before synthesis. Entries
      where the spread failed the divergence check (rule 3 in
      generation-rules.md) or where variants are near-identical despite
      passing are flagged. This signal is free — it comes from the generation
      step and requires no additional model calls.
4. Apply input-aware filtering: remove findings categorized as input-echo
   from both cross-model and within-model findings.
5. Generate corrections for the filtered (post-input-echo-removal)
   cross-model findings. Correction generation is mandatory, not optional —
   the correction-value criterion below cannot be assessed without it.
6. Human-review the filtered findings and their corrections: mark each
   finding true/false positive, and mark each correction as improving or not
   improving the flagged text. Review within-model findings separately —
   mark each as true slop signal or benign (the input legitimately
   constrains output to a narrow range).
7. Assess against five graduation criteria, each with a concrete threshold:

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
   - **Within-model signal value:** among filtered within-model convergence
     findings, the true-positive rate must exceed 50% (i.e. more than half
     of flagged low-divergence entries are genuine slop, not input-forced).
     Report the overlap between within-model and cross-model findings —
     entries flagged by both sources are higher-confidence detections.
     If within-model convergence adds no signal beyond what cross-model
     already catches, note this explicitly; the signal may still justify
     its zero marginal cost.
   - **Consistency:** Kallya and Nadja must reach the same pass/fail verdict
     on each of the four criteria above. If one character passes a
     criterion and the other fails it, consistency fails for that criterion
     — report per-character results, not just an average.

## Decision rule

All five criteria must hold, for both characters, to graduate the mechanism
as a whole. The reviewer may graduate individual detection methods (e.g.
input-echo detection alone, within-model convergence alone, or one judge
pairing) rather than the full mechanism if only some criteria pass.
Within-model convergence may graduate independently of cross-model
detection if it provides reliable signal at zero marginal cost, even if
cross-model detection does not meet its thresholds. If the metric still
does not graduate, document what remains unresolved, including whether the
value-conflict stance pre-check surfaced anything relevant to the
assessment.

## Output

Write results to this directory and update inbox item 9 with the outcome.
