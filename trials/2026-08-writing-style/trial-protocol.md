# Writing Style Trial Protocol

## Test character

Nadja. Justification: known-good Design Notes from the convergence retest trial (2026-07), covering motivations, behaviors, relationships, and history with enough complexity to stress-test style differences. Different character from the previous pipeline quality trial (which used Kallya and Nadja jointly).

## Generation parameters

- Model: `claude-opus-4-6`
- Temperature: `1.0`
- Output scope: Soul section only, 1 run per condition
- All conditions use identical Design Notes (`inputs/design-notes.md`), model, and prompt structure. Only the style instruction varies.

## Conditions

Each condition replaces `writing-style.md` entirely for that run. No condition runs with the ban list active alongside the new style instruction.

| Condition | File | Description |
|---|---|---|
| 0 — Baseline | `conditions/style-baseline.md` | Current writing-style.md rules as-is |
| A — STE-100 strict | `conditions/style-ste100-strict.md` | Full ASD-STE-100 rule set: approved words, sentence limits, active voice, no figurative language, maintenance-manual framing |
| B — STE-100 loose | `conditions/style-ste100-loose.md` | Single instruction naming ASD-STE-100 as a semantic anchor, no enumerated rules |
| C — BLUF | `conditions/style-bluf.md` | Bottom Line Up Front structure: behavior first, then context. 3 rules. |

## Review method

Blind the four outputs with random letter codes and a sealed key. The reviewer reads all four and gives a general impression per condition, not per-entry scores. The impression should address: does this read like a functional instruction set an AI could act on? Would you have to rewrite most of it or is it usable as-is?

## Success criteria

The reviewer ranks the four conditions from best to worst and states whether the best condition is good enough to adopt or whether all fail. The absolute quality gate takes precedence: a condition can rank best but still not be good enough to adopt. There is no numerical threshold. If a condition is both clearly better and good enough, it replaces writing-style.md in the generation rules for Soul. Extension to other sections is a separate decision. If multiple conditions are comparable, the simpler one wins.

A graduating condition is adopted exactly as tested, with no untested modifications.
