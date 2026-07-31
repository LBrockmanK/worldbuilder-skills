# Selection Mechanism Trial

## Goal

Determine which of three selection mechanisms (mechanical rules, judge agent, synthesis) produces the best character note entries when choosing from a 3-variant spread.

## Method

1. Choose one test character with existing Design Notes (Kallya or Nadja from the convergence experiment).
2. Generate the Soul section (minimum 8 entries) **once** using the Pipeline v2 flow to produce 3-variant spreads per entry. This generation step happens exactly one time and produces the SAME variant sets used for every mechanism below — do not regenerate variants per mechanism. Apply all three selection mechanisms (mechanical rules, judge agent, synthesis) to these identical variant sets. This isolates the selection variable from generation variance.
3. Blind the results: strip mechanism labels, randomize entry order within each version.
4. Human reviewer rates each entry on a 1–3 rubric:
   - 3: stageable, specific, no input echo, no slop
   - 2: acceptable but generic or partially echoing input
   - 1: fails staging test, echoes input, or contains slop
5. Unblind and compare mean scores per mechanism.

## Decision rule

Adopt the mechanism with the highest mean score.

- If all three mechanisms score within 0.3 of each other, adopt Mechanism 2 (judge) as the default, for flexibility.
- Otherwise, if exactly two mechanisms tie (within 0.3 of each other, but not all three), prefer the cheaper of the two tied mechanisms.
- Otherwise, adopt the outright highest-scoring mechanism.

## Secondary trial: variant count

After the selection mechanism winner is determined above, test whether 3 variants is the right spread size.

1. Using the winning selection mechanism, repeat Soul-section generation with 2 variants and with 5 variants (in addition to the 3-variant result already scored above).
2. Run each variant count (2, 3, 5) **multiple times** (minimum 2 additional generation runs per count) to control for generation variance — a single run per count is not sufficient to draw a conclusion.
3. Score each run's entries with the same 1–3 rubric used above, blind and randomized as in step 3 of the main method.
4. Compare mean rubric scores across the 2, 3, and 5-variant conditions (averaged across runs per condition) to determine the optimal variant count.

## Output

Write results to `trials/2026-07-selection-mechanism/results/` and update `skills/worldbuilder-character/generation-rules.md` with the chosen mechanism and variant count.
