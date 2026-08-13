# Pipeline Quality Trial — Protocol

## Test character

**Kallya.** Reused from the convergence validation experiment and the selection mechanism trial. Design Notes contain 30+ facts across motivations (self-image gap, care-predation coexistence), behaviors (social predation through persuasion, airhead performance, community defense), relationships (Vesper, Rado, Liza/Mir, Maja, Ataraxia, Leif, Nadja, Elara), and internal dynamics (genocide-line revelation, reluctance to admit caring). This density provides enough material for quality differences to manifest across conditions.

Design Notes are in `inputs/design-notes.md`.

## Output section

Soul.

## Pinned parameters

- **Model:** `claude-opus-4-6`
- **Temperature:** `1.0`
- **Runs per condition:** 2

Model and temperature are the same for all conditions and all runs. Each run is scored independently; per-condition means are reported across both runs.

## Conditions

Each condition is cumulative (each adds to the previous):

**Condition 0 — Baseline.** Current Pipeline v2: deslop/deframe preprocessing, routing annotations, 3-variant generation with fact-to-manifestation, synthesis selection. No changes.

**Condition A — Fail-check gate.** Baseline plus a formal divergence gate between variant generation and synthesis. After generating 3 variants for each entry, compute pairwise Jaccard similarity of lowercase character trigrams. If any pair exceeds 0.25, reject the spread and regenerate that entry. Allow 3 additional regeneration attempts (4 total including the original). If all fail the threshold, flag the entry and proceed with the spread whose maximum pairwise Jaccard similarity is lowest. This mechanical gate replaces the existing qualitative divergence check in generation-rules.md for all conditions that include it (A, B, C).

**Condition B — Input restructuring.** Condition A plus three changes to how Design Notes are presented to the generation pipeline:

- S1 (orthogonal organization): Reorganize the preprocessed input by topic cluster (motivations, behaviors, relationships, fears) rather than mirroring the output sections (Background, Body, Soul, Relationships). The model receives thematic bundles and must redistribute facts across output sections.
- S3 (coarser bundling): Merge related bullet points within each topic cluster into paragraph-level blocks. No single-fact bullets; each block contains 2-4 related facts that must be decomposed.
- S6 (distinct builder voice): Add an LLM-driven rewrite pass after deslop/deframe that converts the preprocessed input into compressed clinical shorthand (abbreviated, no articles, no hedging). This is a new preprocessing stage, not a mechanical rule. Any reproduction of input phrasing in the character-voice output becomes immediately detectable.

**Condition C — Decomposition step.** Condition B plus an explicit decomposition phase before variant generation. The model must first produce a redistribution outline: for each input fact, which output section and entry it maps to, and what behavioral manifestation it becomes. The outline is validated for coverage (every input fact appears at least once) before generation proceeds. For this trial, the outline maps all input facts to their target sections, but only facts routed to Soul proceed to variant generation.

## Metrics

Score each entry on five dimensions (1-3 scale):

1. **Staging test** — Does the entry show observable behavior rather than stating an internal quality? (1 = tells: "she is brave"; 2 = mixed: names the quality but includes a behavioral example; 3 = shows: describes what she does, a reader infers the quality)
2. **Specificity** — Is the behavior concrete and particular to this character, or generic? (1 = generic: could describe anyone; 2 = moderate: somewhat particular but common pattern; 3 = specific: this behavior distinguishes this character)
3. **Input echo** — Does the phrasing reproduce Design Notes input? (1 = clear echo: a phrase of 4+ words appears verbatim or near-verbatim from the original Design Notes; 2 = partial overlap: recognizable rewording of input phrasing; 3 = fully transformed: expresses the same fact in unrelated phrasing)
4. **Slop** — Does the entry contain filler, hedging, or cliche phrasing? (1 = sloppy: hedges, qualifiers, or stock phrases dominate; 2 = some filler: one or two weak phrases in otherwise clean prose; 3 = clean: every word earns its place)
5. **Factual fidelity** — Does the entry accurately reflect the Design Notes facts it draws from, without omission, distortion, or invention? (1 = factually wrong or invented: states something unsupported by Design Notes; 2 = partially accurate: the core fact is present but details are altered or missing; 3 = faithful: the fact is preserved and nothing is added)

Additionally, run the existing grader checks (input-echo detection, within-model divergence) mechanically on all conditions, comparing against the original Design Notes (pre-preprocessing), and report rates alongside the human scores. Human echo scoring also uses the original Design Notes as the reference, not any intermediate preprocessed form.

## Blind review procedure

1. Generate output for all four conditions.
2. The generating agent strips condition labels, assigns random letter codes (W, X, Y, Z), and seals the mapping. The human reviewer does not have access to the code-to-condition mapping until all scoring is complete.
3. Randomize entry order within each condition's output.
4. Present all entries to the human reviewer grouped by letter code, with the Design Notes visible for reference.
5. Reviewer scores each entry on all five dimensions before unblinding.
6. Unblind and compute per-condition means.

## Success criteria

A condition is an improvement over baseline if its mean score exceeds the baseline mean by at least 0.3 on any dimension (staging, specificity, slop, or factual fidelity — the four quality dimensions; input echo is reported but not weighted for adoption since the baseline rate is already low) without regressing by more than 0.1 on any other dimension. If multiple conditions improve, adopt the one with the highest sum of per-dimension means (equal weight across all four dimensions). If no condition improves over baseline, the current pipeline stands and the trial is recorded as a negative result. Tie-break: if two conditions produce the same sum, prefer the simpler one (lower condition letter).

## Adoption rule

Improvements that graduate are implemented permanently in the pipeline. Input restructuring changes modify generation-rules.md: S1 and S3 alter the preprocessing instructions; S6 adds a new LLM-driven rewrite stage that runs after deslop/deframe. The fail-check gate is added to the generation flow in the worldbuilder-character skill (generation-rules.md). The decomposition step, if it graduates, is added to generation-rules.md as a required pre-generation phase.
