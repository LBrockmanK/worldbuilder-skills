---
type: review
title: Review — Additive-Doctrine Discriminator Trial
description: Adversarial review of the Additive-Doctrine Discriminator Trial spec.
tags:
- complete
date: 2026-08-09
timestamp: 2026-08-10T01:21Z
resources:
- "[[2026-08-09-additive-doctrine-discriminator-trial]]"
---

# Review — Additive-Doctrine Discriminator Trial

## Round 1 — digest `708d7c05…`, anchor `340ddff6` (dirty), tokens 43363, 2026-08-09T17:26:52-05:00, 146s

Anchor: 340ddff649383d6d199f035a9373b9b131b9c551 (dirty tree)
Artifact digest: 708d7c053ae1ef678771e52ec633694dadb3df69dadd3a7037df06e13de2243d (sha256 over the exact scoped bytes as delivered)
Scope: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md

1. Arm definitions conflict
   Location: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md:51-74
   Quote: `| Doctrine | current, additive, stopslop (current style + current doctrine) |`
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: escalate
   Body: The matrix defines stopslop as “current style + current doctrine,” but D2 instead applies `style-stopslop.md`. It also never applies `style-current.md` to the current or additive arms, although the referenced trial kit models style and doctrine as separate inputs. Consequently, implementers cannot tell whether the intended prompts are current-style/current-doctrine, current-style/additive-doctrine, and stopslop-style/current-doctrine, or simply base, base+additive, and base+stopslop. This violates the fully specified matrix and unambiguous implementation criteria.

2. Exact models and generation controls are unspecified
   Location: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md:54,76-77
   Quote: `| Model | Sonnet, Opus (same Claude family) |`
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: escalate
   Body: “Sonnet” and “Opus” do not identify exact model versions or dispatch identifiers. Likewise, saying temperature and system prompt are constant does not state their values, the exact system-prompt bytes, other sampling parameters, or whether aliases may move during the trial. Different implementations can therefore run materially different experiments while claiming compliance, and the promised reproduction instructions cannot reproduce the scoped trial.

3. Input-echo scoring units and aggregation are undefined
   Location: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md:83-91
   Quote: `**Input-echo score.** Per-entry trigram Jaccard similarity between
output and source design notes, via \`categorize()\`. Reported as:
- Per-cell mean overlap score (continuous, 0.0–1.0)
- Per-cell echo rate (proportion of entries exceeding the 0.35
  threshold)`
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: escalate
   Body: Each generation produces a complete note, while `categorize()` accepts one output entry. The spec never defines how a note is split into entries, which headings or metadata are excluded, how multiline entries are joined, or how empty/failed parses are handled. It also does not say whether the cell mean and echo rate pool all entries, average per-run statistics equally, or weight runs by entry count. These choices can change both the metric and the 3-of-4 success result.

4. The stopslop arm is not a valid metric-neutral control
   Location: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md:58-60
   Quote: `The stopslop arm serves as a behavioral baseline: a surface-level
change (word choice) that should not move structural metrics. If it
does, the metrics are measuring something other than doctrine effect.`
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: escalate
   Body: Input echo is explicitly a character-trigram lexical-similarity metric, so changing word choice directly changes that metric. Moreover, the referenced stopslop rules alter sentence structure, voice, list length, rhythm, fragmentation, and punctuation—not merely word choice. A stopslop movement therefore does not demonstrate confounding as claimed; it is an expected consequence of the intervention. This faulty diagnostic can cause valid results to be rejected or misinterpreted.

5. Stopslop “indistinguishability” is not operationalized
   Location: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md:112-126
   Quote: `- A sanity check: whether the stopslop arm's metrics fall within the
  current arm's range (expected: yes)`
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: escalate
   Body: The spec does not define the “range”: it could mean the three raw runs in a corresponding cell, the four character×model cell means, confidence bounds, or the global minimum and maximum. It also does not state whether every stopslop cell and both metrics must be in range. D5 then calls this “indistinguishable,” which is not equivalent to falling inside an observed min/max interval. Thus the third success question has no deterministic pass/fail implementation.

6. The referenced generation-dispatch mechanism does not exist
   Location: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md:152-155
   Quote: `Generation dispatch uses the same
agent-dispatch mechanism as the convergence retest's
\`run_detection.py\`.`
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The referenced `run_detection.py` reads existing output files and computes detection results; it contains no generation or agent-dispatch mechanism. Therefore it cannot serve as the specified implementation reference for `run_trial.py`. The spec must identify an actual dispatch interface or explicitly separate externally orchestrated generation from local scoring.

7. Required report representation is unspecified
   Location: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md:103-113
   Quote: `The runner produces a structured JSON report and a human-readable
summary.`
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: No JSON schema is given for raw generation metadata, per-entry scores, the three pairwise comparisons, cell aggregates, cross-arm deltas, sanity-check results, or final decision flags. Precision and rounding are also unspecified. Implementations can consequently emit incompatible reports or retain only aggregates, preventing verification of the success calculation and undermining reproducibility.

8. Outcome actions omit and conflict on reachable result scenarios
   Location: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md:169-179
   Quote: `- **Additive shows consistent directional improvement on one or both
  metrics:** Record as measured evidence supporting the adoption.`
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: escalate
   Body: The action table does not cover consistent worsening, an inconsistent directional result such as 2-of-4, ties, or one metric improving while the other worsens. Its first branch would count that last scenario as supporting evidence regardless of the adverse metric. It also gives no precedence when additive appears to improve but stopslop moves unexpectedly: both the “support adoption” and “investigate before drawing conclusions” actions apply. “No measurable difference” cannot absorb these cases because the spec defines no magnitude threshold and several are measurable non-null outcomes. This violates the requirement to cover all result scenarios.

FINDINGS: 0 critical, 8 major, 0 minor, 0 nit

### Adjudication

1. **Accept.** Arm composition ambiguous — will clarify input stacking per arm.
2. **Accept.** Will pin model version IDs. Temperature/system-prompt values remain plan-level.
3. **Accept.** Will define entry extraction and aggregation.
4. **Accept.** Stopslop reframed from null control to reference delta for non-doctrine change.
5. **Accept.** Subsumed by #4 reframing.
6. **Accept.** Will clarify generation is agent-dispatched; detection is local scoring.
7. **Reject.** JSON schema is plan-level implementation detail. Spec defines what must be reported.
8. **Accept.** Will cover worsening, inconsistent (2-of-4), split metrics, and precedence conflicts.

## Round 2 — digest `9fd33c88…`, anchor `340ddff6` (dirty), tokens 80921, 2026-08-09T17:56:17-05:00, 290s

Anchor: 340ddff649383d6d199f035a9373b9b131b9c551 (dirty tree)
Artifact digest: 9fd33c887a3efac57122cf82e32469f60eadd4229a6565caeb7658f6c3859c04 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md

1. Missing or malformed outputs silently become valid zero-valued cells
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:684-715
   Quote:
   ```python
                   for run in range(1, RUNS_PER_CELL + 1):
                       fname = f"{char}-{arm}-{model_short}-run{run}.md"
                       fpath = os.path.join(out_dir, fname)
                       if not os.path.exists(fpath):
                           print(f"SKIP: {fpath} not found")
                           continue

                       text = _read(fpath)
                       run_texts.append(text)

                       # Input-echo per entry
                       entries = extract_entries(text)
                       overlaps = []
                       for entry in entries:
                           result = categorize(entry, input_notes)
                           overlaps.append(result["overlap"])

                       run_mean = sum(overlaps) / len(overlaps) if overlaps else 0.0
   ```
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: `--detect-only` can analyze an empty or partial directory without failing. Missing runs are skipped, notes with no recognized H2 entries receive a zero echo score, and cells with fewer than two runs receive zero pairwise overlap. The runner then saves those zeros as apparently valid results. A fresh empty directory therefore looks like “no measurable difference” rather than an invalid trial. Require all 36 files, the expected run count per cell, at least one extracted entry per run, and all three pairwise comparisons before producing a report.

2. D4’s per-model and per-character breakdowns are not implemented
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:788-804
   Quote:
   ```python
       return {
           "additive_vs_current": {
               "echo_delta": round(additive_echo - current_echo, 4),
               "divergence_delta": round(additive_div - current_div, 4),
               "echo_consistent_wins": f"{add_echo_wins}/{combos}",
               "divergence_consistent_wins": f"{add_div_wins}/{combos}",
           },
           "stopslop_vs_current": {
               "echo_delta": round(stopslop_echo - current_echo, 4),
               "divergence_delta": round(stopslop_div - current_div, 4),
           },
           "arm_means": {
               "current": {"echo": round(current_echo, 4), "divergence": round(current_div, 4)},
               "additive": {"echo": round(additive_echo, 4), "divergence": round(additive_div, 4)},
               "stopslop": {"echo": round(stopslop_echo, 4), "divergence": round(stopslop_div, 4)},
           },
       }
   ```
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The summary contains only all-cell arm means, global deltas, and improvement counts. D4 expressly requires separate Sonnet-versus-Opus and Nadja-versus-Kallya breakdowns. The later per-cell table does not calculate those grouped breakdowns. Both the JSON structure and Markdown writer need the required grouped means and deltas, with corresponding tests.

3. D8 has no implementing task
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:891-905
   Quote:
   ```markdown
   - [ ] **Step 8: Run all tests**

   ```bash
   cd trials/2026-08-additive-discriminator && python -m pytest test_runner.py -v
   ```

   Expected: all tests PASS (12 total).

   - [ ] **Step 9: Commit**

   ```bash
   git add trials/2026-08-additive-discriminator/run_trial.py \
          trials/2026-08-additive-discriminator/test_runner.py
   git commit -m "feat: add detection, aggregation, and reporting phase"
   ```
   ```
   Type: completeness
   Severity: major
   Effort-to-fix: large
   Risk-of-fix: medium
   Channel: fix
   Body: The plan ends after producing and committing the report. It never implements D8’s precedence-ordered result handling: recording support, partial support, split, adverse, or null outcomes; updating `.claude/inbox.md`; closing or retaining the revisit trigger; and surfacing adverse evidence as a human decision rather than reversing adoption. This violates the requirement that every D1–D8 decision have an implementing task.

4. Premature rounding can change D5’s directional result
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:701-715,738-740,783-786
   Quote:
   ```python
                       run_entry_overlaps.append({
                           "run": run,
                           "mean_overlap": round(run_mean, 4),
   ```
   ```python
                   run_means = [r["mean_overlap"] for r in run_entry_overlaps]
   ```
   ```python
                       if cells[ak]["echo_mean"] < cells[ck]["echo_mean"]:
                           add_echo_wins += 1
                       if cells[ak]["divergence_mean"] < cells[ck]["divergence_mean"]:
                           add_div_wins += 1
   ```
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: Run means are rounded before cell aggregation, cell means are rounded before arm aggregation, and the rounded cell values determine the 3-of-4 consistency counts. Because D5 intentionally has no minimum effect-size threshold, a real difference below the rounding boundary can become a tie or reverse after compounded rounding. Retain raw values for every calculation and round only serialized/displayed fields.

5. Output filenames discard part of the pinned model identifier
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:29-33,222-225
   Quote:
   ```markdown
   - Model IDs pinned: `claude-sonnet-5`, `claude-opus-4-6` — no aliases.
   ```
   ```python
   def output_path(character: str, doctrine: str, model: str, run: int) -> str:
       """Return the output file path for one generation."""
       model_short = model.replace("claude-", "")
       return os.path.join(OUT_DIR, f"{character}-{doctrine}-{model_short}-run{run}.md")
   ```
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: D6 and the plan’s global naming contract specify `{character}-{doctrine}-{model}-run{n}.md`, with exact model IDs pinned. The implementation instead produces `sonnet-5` and `opus-4-6` filenames. Detection and tests repeat the shortened convention, so the inconsistency is systematic. Use one explicit filename contract everywhere.

6. `parse_args()` has no test coverage
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:228-236
   Quote:
   ```python
   def parse_args() -> argparse.Namespace:
       parser = argparse.ArgumentParser(description="Additive-doctrine discriminator trial")
       parser.add_argument("--detect-only", action="store_true",
                           help="Skip generation, run detection on existing outputs")
       parser.add_argument("--dry-run", action="store_true",
                           help="Print prompts and exit, no API calls")
       parser.add_argument("--out-dir", default=OUT_DIR,
                           help="Output directory for generated notes")
       return parser.parse_args()
   ```
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: None of the proposed tests calls `parse_args()` or checks its three flags and defaults. A manual dry-run command covers only one happy-path invocation and is not test coverage for the function. This violates the all-functions coverage criterion.

7. `write_summary()` has no test coverage
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:812-853
   Quote:
   ```python
   def write_summary(report: dict, path: str) -> None:
       """Write the human-readable summary report."""
   ```
   Type: completeness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The test plan stops after checking `run_detection()`’s dictionary structure. No test invokes `write_summary()`, checks that a file is created, or validates its tables, deltas, consistency section, and per-cell rows. The final report-producing function is therefore completely uncovered.

8. The final expected test count is wrong
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:522-613,891-897
   Quote:
   ```markdown
   Expected: all tests PASS (12 total).
   ```
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: Task 1 defines seven tests, Task 2 adds two, and Task 3 adds four—three extraction tests and one detection test—for 13 total. The stated expected output cannot match the plan as written.

9. Multiple executable steps omit expected output
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:53-57,316-323,502-508,899-905
   Quote:
   ```markdown
   - [ ] **Step 1: Create the trial directory**

   ```bash
   mkdir -p trials/2026-08-additive-discriminator/out
   ```
   ```
   ```markdown
   - [ ] **Step 9: Commit**

   ```bash
   git add trials/2026-08-additive-discriminator/run_trial.py \
          trials/2026-08-additive-discriminator/test_runner.py
   git commit -m "feat: add detection, aggregation, and reporting phase"
   ```
   ```
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The directory-creation command and all three commit command blocks have no stated expected result or verification. That directly violates the command-output acceptance criterion. Each executable step needs a concrete success condition, such as the directory’s existence or the expected committed paths and commit subject.

10. Pairwise overlap is mislabeled as “divergence mean”
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:722-740,816-823
   Quote:
   ```python
                   # Within-model divergence: pairwise on full note text
                   pairwise_overlaps = []
   ```
   ```python
                   "divergence_mean": round(divergence_mean, 4),
   ```
   ```python
           "| Arm | Echo mean | Divergence mean |",
   ```
   Type: consistency
   Severity: minor
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: The stored value is mean trigram overlap, where higher means less divergence, but both the field and report heading call it divergence. That label invites the opposite interpretation. Name it `pairwise_overlap_mean`/“Mean pairwise overlap,” or transform the value into an actual divergence score and consistently adjust direction checks.

FINDINGS: 0 critical, 9 major, 1 minor, 0 nit

### Adjudication

1. **Accept.** Add validation: require all 36 files, entries per run, pairwise completeness.
2. **Accept.** Add per-model and per-character breakdowns.
3. **Reject.** D8 is human post-trial interpretation; report provides data, human acts per D8's precedence table.
4. **Accept.** Raw floats for computation, round only for display/serialization.
5. **Accept.** Standardize model short names in filenames and global constraint.
6. **Reject.** CLI boilerplate; flags exercised through integration use.
7. **Accept.** Add write_summary() test.
8. **Accept.** Fix test count.
9. **Accept.** Add expected output to directory creation and commit steps.
10. **Accept.** Rename divergence_mean → pairwise_overlap_mean.

### Fix verification (2026-08-09)

All accepted findings from rounds 1 and 2 verified as implemented in
the spec, plan, and code:

**Round 1 (spec):**
- F1: D2 table specifies per-arm overlay composition (current=none, additive=doctrine, stopslop=style)
- F2: D1 pins `claude-sonnet-5`, `claude-opus-4-6`
- F3: D3 defines entry extraction (## sections, exclude frontmatter/H1/subheadings), aggregation (equal-weight run means), and reporting granularity
- F4+F5: D1 reframes stopslop as reference delta for non-doctrine change, not a null control
- F6: D6 separates generation (Claude API calls) from detection (imports from existing scripts)
- F8: D8 covers consistent improvement (both/one metric), split result, consistent worsening, inconsistent (2-of-4), null result, and precedence between stopslop comparison and primary outcomes

**Round 2 (plan/code):**
- F1: `run_detection()` validates all 36 files present + at least one extracted entry per run (`FileNotFoundError`/`ValueError`)
- F2: `_compute_summary()` computes `per_model` and `per_character` breakdowns with per-arm echo and pairwise overlap means
- F4: Raw floats through all computation; `round()` only on serialized `pairwise_overlaps` list in cell data
- F5: Global constraint pins `model_short` convention; filenames and keys consistent
- F7: `test_write_summary_creates_file()` verifies file creation and required sections
- F8: Test count matches implementation (14 tests, all passing)
- F9: Step 1 and commit steps have expected output and verification commands
- F10: Field renamed `pairwise_overlap_mean` throughout code and summary

## Round 3 — digest `9aa136be…`, anchor `c72c1a58` (dirty), tokens 54312, 2026-08-09T20:17:12-05:00, 252s

Anchor: c72c1a58bf3108ea8b409146fd480694f3af3b68 (dirty tree)
Artifact digest: 9aa136be9cf5f7efc416db1c2896998e84acb21dcd8e734118e06e9d0849a721 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md, .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md

1. Title: D8 does not deterministically classify all reachable outcomes
   Location: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md:213-230
   Quote:
   > - **Consistent improvement on one metric, neutral on the other:**
   > - **Inconsistent direction (2 of 4 cells):** Record as a null result
   > - **No measurable difference (deltas near zero across all cells):**
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Neutral” and “near zero” have no numerical definitions, while “inconsistent” covers only exactly 2 of 4 directional wins. Reachable tie-heavy cases—such as one improving cell and three exact ties, or one metric consistently improving while the other is 2/4—cannot be assigned unambiguously among partial support and null. This violates the requirements that D8 cover every reachable scenario and that the trial contain no ambiguous implementation choices. Define mutually exclusive states for each metric, including equality/ties, then map every two-metric combination in precedence order.

2. Title: The stated consequence contradicts the worsening outcome
   Location: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md:240-243
   Quote:
   > - Produces a reproducible, mechanically-scored comparison that either
   >   strengthens or leaves unchanged the additive-doctrine adoption's
   >   evidence base.
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: D8 explicitly allows “measured evidence against the adoption,” which weakens its evidence base even if the adoption is not automatically reversed. The consequence claims only strengthening or no change is possible, contradicting that reachable outcome and violating cross-section consistency.

3. Title: The spec and plan disagree on the output filename’s model component
   Location: .claude/specs/2026-08-09-additive-doctrine-discriminator-trial.md:184-185; .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:33
   Quote:
   > - `out/` — generated notes, named
   >   `{character}-{doctrine}-{model}-run{n}.md`.
   >
   > - Output naming: `{character}-{doctrine}-{model_short}-run{n}.md` where model_short strips the `claude-` prefix (e.g., `sonnet-5`, `opus-4-6`).
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The spec names the field `model`, naturally referring to the pinned full IDs, while the plan mandates a stripped `model_short`. A reproducer following the spec can create filenames that detection will not recognize. The spec must explicitly adopt the plan’s `model_short` convention.

4. Title: Pairwise-overlap deltas are mislabeled as divergence deltas
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:893-901
   Quote:
   > "divergence_delta": additive_div - current_div,
   >
   > "divergence_delta": stopslop_div - current_div,
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: `additive_div`, `current_div`, and `stopslop_div` are means of `pairwise_overlap_mean`, so their differences are pairwise-overlap deltas, not divergence deltas. The distinction reverses the intuitive sign: a negative overlap delta means greater divergence, whereas a negative “divergence delta” suggests less divergence. This also violates the required `pairwise_overlap_mean` naming consistency. Rename the keys and report labels to pairwise-overlap deltas, or actually transform overlap into a defined divergence measure before labeling it divergence.

5. Title: The summary-writer test does not cover required breakdown output
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:657-668
   Quote:
   > "per_model": {},
   > "per_character": {},
   >
   > assert "Arm means" in content
   > assert "Cross-arm deltas" in content
   > assert "Consistency" in content
   > assert "Per-cell detail" in content
   Type: completeness
   Severity: minor
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The fixture leaves both breakdown mappings empty, and the assertions never require the “Per-model breakdown” or “Per-character breakdown” sections or any rendered values. The test therefore passes if required breakdown formatting is removed or broken. Populate both mappings and assert their headings and representative model/character rows.

6. Title: Runtime dependencies and prompt inputs are not reproducibly pinned
   Location: .claude/plans/2026-08-09-additive-doctrine-discriminator-trial-implementation.md:23, 49-50, 299-303
   Quote:
   > **Tech Stack:** Python 3.10+, `anthropic` SDK for generation, stdlib only for detection (imports from existing `scripts/detect_input_echo.py`).
   >
   > - Consumes: source markdown files listed above (read at runtime).
   >
   >     pip install anthropic
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The plan permits any Python version from 3.10 onward and installs whichever `anthropic` release is current. It also reads mutable prompt sources at runtime without pinning their revisions or recording their hashes in the report. Consequently, the same documented procedure can execute against different client behavior or different prompt bytes. That fails the requirement for a reproducible trial with pinned choices. Pin the execution dependency versions and record or verify the exact source-file hashes used by each run.

FINDINGS: 0 critical, 5 major, 1 minor, 0 nit

### Adjudication

1. **Reject.** D8 is human-interpretive by design (consistent with round 2 F3 rejection). With n=3 per cell, defining "near zero" or "neutral" numerically would imply a precision the trial doesn't support. The human reads the deltas and applies judgment.
2. **Accept.** Consequences section should acknowledge the worsening possibility that D8 explicitly allows.
3. **Accept.** Spec D6 should use `{model_short}` to match the plan and actual filenames.
4. **Accept.** Summary-level delta keys should be renamed from `divergence_delta` to `pairwise_overlap_delta` — the round 2 rename was incomplete.
5. **Accept.** Test fixture should populate breakdowns and assert their output.
6. **Reject.** Trial is a specific executed experiment, not a reusable protocol. Source files are git-versioned; runtime pinning adds no value to a completed one-shot trial.

### Fix verification (2026-08-09)

Round 3 accepted findings verified as implemented:

- F2: Spec consequences section now reads "strengthens, leaves unchanged, or provides evidence against"
- F3: Spec D6 filename template updated to `{model_short}` with definition
- F4: `divergence_delta` renamed to `pairwise_overlap_delta` in `_compute_summary()` return dict and `write_summary()` table header/cells; report.json and summary.md regenerated
- F5: Test fixture `per_model` and `per_character` populated; assertions added for breakdown section headings

All 14 tests passing. Report and summary regenerated with corrected key names.

### Review closed

Three rounds completed (document cadence cap reached). Residual
findings: F1 and F6 rejected with recorded reasons. No unresolved
accepted findings remain. Review complete.
