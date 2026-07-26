---
type: research
title: 'Implementation research: standing methodology document conventions'
description: 'Repo conventions for authoring trials/METHODOLOGY.md: existing trial-kit
  file structure and headings, prose wrapping conventions, lint and CI coverage gaps
  over trials/, and the absence of any prior standing methodology document.'
tags:
- human-ready
date: 2026-07-26
timestamp: 2026-07-26T15:51Z
resources: []
---

# Implementation research: standing methodology document conventions

## Goals

Gather the repo conventions needed to author `trials/METHODOLOGY.md` per the [standing writing-assessment methodology spec](../specs/2026-07-26-standing-writing-assessment-methodology-a-b-trial-suite-and-production-self-review-battery.md): what the existing trial kit looks like structurally, how prose in `trials/` is formatted, what lint or CI gates apply, and whether any prior standing methodology document exists.

## Results

**Existing trial kit — `trials/2026-07-writing-doctrine/`.** None of the three prose files carry frontmatter; all are plain repo markdown.

| File | Lines | Headings |
| --- | --- | --- |
| `README.md` | 43 | `# Trial Runner`; `## 1. What this is`; `## 2. Setup`; `## 3. Dispatch`; `## 4. Collect and hand off`; `## 5. Regeneration note` |
| `brief-procedure.md` | 24 | `# Brief Procedure`; `## 1. Pick the character`; `## 2. Run the Q&A`; `## 3. Freeze the brief`; `## 4. Treat the brief as read-only` |
| `rubric.md` | 99 | `# Rubric: Writing-Doctrine Blind Trial`; `## How to score`; `## Scoring table`; `## Results record`; `### Decoded map`; `### Style axis: arms 1-3 vs 4-6`; `### Doctrine axis, additive step`; `### Doctrine axis, tensions step`; `### Interactions` |

**Prose conventions in `trials/`.** Hard-wrapped at roughly 68–74 characters. Heading depth H1/H2, with H3 only in `rubric.md`. Numbered `## N. Title` sections for procedures; markdown tables for scoring; bulleted lists throughout.

**Lint and CI coverage.** `.doodle.toml` scopes its glob to `skills/worldbuilder-setup/SKILL.md` only. CI (`.github/workflows/tests.yml:29-30`) pins `doodle-lint==1.0.0` and runs `doodle --strict skills`. Neither lints `trials/`. No test, build script, or CI step under `.github/workflows/` or `scripts/` references `trials/` at all — the directory is unlinted and untested. Note the standing local-versus-CI gap: local doodle-lint is 0.5.0 while CI pins 1.0.0, so a local pass does not prove CI clean.

**Writing-doctrine files** (referenced by the methodology, not modified by it): `skills/writing-style.md` (218 lines) and `docs/slop-phrases.md` (96 lines), both without frontmatter.

**Prior art.** No `trials/METHODOLOGY.md` exists. Every "methodology" hit in the repo is inside `.claude/` — the inbox, the spec index, the new spec, the 2026-07-25 blind-trial adoption plan, and three research documents. There is no existing standing methodology document to extend or supersede.

## Consolidation

Three implications for the plan:

1. **The document is greenfield but not styleless.** It should match the kit's conventions — no frontmatter, hard wrap at ~72 characters, `## N. Title` numbered sections — so a trial builder reads the standing document and its instance in one idiom.
2. **No automated gate will catch errors in it, and doodle-lint cannot become one.** Because `trials/` is outside both the doodle glob and CI, verification steps in the plan must be explicit structural commands (heading presence, wrap width, required-string greps) rather than an appeal to a lint or test suite that does not cover this path. Extending doodle coverage to `trials/` was considered and rejected on evidence: doodle-lint is a skill linter, not a general prose linter, and it fails any file lacking SKILL.md frontmatter. Run against `docs/slop-phrases.md` it emits `parse/missing-frontmatter` and `desc/too-short` and exits 2. Since `trials/METHODOLOGY.md` deliberately carries no frontmatter, adding it to the lint scope would fail CI on two inapplicable errors. The gap stays open by decision, not oversight.
3. **The 2026-07 kit becomes the first instance.** It stays functionally untouched; the only change it needs is a pointer to the standing document so the relationship is discoverable from either direction.
