# Generation Rules

*Sub-file for `worldbuilder-character`. Read this when generating Background, Body, Soul, and Relationship entries from Design Notes.*

---

## Preprocessing

Before generating entries, run the deslop/deframe pass on the Design Notes content. This strips meta-vocabulary (builder-level terms like household assignments, narrative function labels) and flags stop-slop patterns. Work from the cleaned copy; preserve the original Design Notes as the permanent builder record.

## Routing annotation

Before generating, annotate each freeform note in Session Notes and Builder Context with which output section(s) it feeds. Record the annotation inline by prepending a tag to the note: `[B]` for Background, `[Bo]` for Body, `[S]` for Soul, `[R]` for Relationships. Notes that feed multiple sections get a combined tag listing each destination, e.g. `[B,S]` or `[B,Bo,R]`. This persists the routing for future agents and makes the annotation visible during generation. Notes that feed multiple sections force synthesis during generation: the model must decompose one input fact into entries across different sections. Notes that feed only one section carry higher echo risk and get extra scrutiny during the multi-option spread.

## Fact-to-manifestation rule

Design Notes state what is true about the character. You write how that truth manifests as observable behavior. Reproduce the semantic content; never reproduce the phrasing.

If the input says "refuses credit," your output describes what refusing credit looks like: the specific gesture, deflection, or subject change. Do not use the phrase "refuses credit."

If the input says "cajoles people closer," your output describes the specific action pattern: how she positions her body, what she says, how people respond. Do not use the word "cajoles."

The input is the fact. Your output is the staged behavior the fact produces. Same meaning, different words, observable action.

## Multi-option spread

For each entry you would produce (each bullet in Background, Body, Soul, Relationships), generate three variant renderings instead of one.

**Rules:**
1. All three variants express the same underlying character fact.
2. Each variant uses genuinely different phrasing, emphasis, or behavioral angle. Three rewrites of the same sentence structure do not count as divergence.
3. After generating three variants, check: could a reader tell them apart without comparing word by word? If not, discard all three and regenerate with deliberate divergence. One retry.
4. Present all three to the selection step (see below).

**What divergence looks like:**
- Variant A focuses on the trigger and what the character does.
- Variant B focuses on the cost or consequence of the behavior.
- Variant C focuses on what an observer would see vs. what is actually happening.

All three pass the staging test, except Background entries (which are factual, not behavioral; see framework.md). All three avoid input phrasing. They differ in which facet of the behavior they foreground.

## Selection

After generating three variants per entry, select the best using the active selection mechanism. The mechanism is determined by the empirical trial (Task 4 of the implementation plan). Until the trial completes, use Mechanism 2 (judge) as the default.

**Mechanism 1. Mechanical rules:** Score each variant against the stop-slop phrase list, input-similarity (string overlap with source Design Notes), and writing-style rules. Select the highest-scoring variant.

**Mechanism 2. Judge (default):** A separate evaluation picks the best of three with a short rationale, guided by the staging test and writing-style rules.

**Mechanism 3. Synthesis:** A final pass takes the strongest elements from all three variants and writes a synthesis. Applied unconditionally during the trial so it can be scored against the other two mechanisms.

**Decision rule:** If all three mechanisms score within 0.3 of each other, adopt Mechanism 2 (judge). Otherwise, if exactly two mechanisms tie, prefer the cheaper one.
