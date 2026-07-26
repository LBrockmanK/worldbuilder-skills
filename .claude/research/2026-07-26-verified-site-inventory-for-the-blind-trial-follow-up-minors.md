---
type: research
title: Verified site inventory for the blind-trial follow-up minors
description: Line-accurate inventory of the seven follow-up defect sites across writing-style.md,
  slop-phrases.md, relationships.md and framework.md, each checked against current
  file text, plus the lint and test gates that apply to those paths.
tags:
- human-ready
date: 2026-07-26
timestamp: 2026-07-26T16:36Z
resources: []
---

# Verified site inventory for the blind-trial follow-up minors

## Goals

Check each of the seven follow-up minors from the blind-trial adoption reviews against the current file text before planning any edit, and establish which lint or test gates cover the affected paths.

## Results

All seven claims verified against current text. Line numbers as of 2026-07-26.

| # | Site | Claim | Verdict |
| --- | --- | --- | --- |
| 1 | `skills/writing-style.md:72` | Cut filler lead restates the section above and misses two of its four groups | Confirmed both halves |
| 2 | `skills/writing-style.md:82` | "just/actually/honestly/genuinely/truly" mislabelled as adverbs of degree | Confirmed |
| 3 | `docs/slop-phrases.md:55-70` | under-covers the new vague-declarative items | Confirmed, and narrower than stated |
| 4 | `skills/worldbuilder-character/relationships.md:14` | asymmetry guaranteed, complement rule absent | Confirmed |
| 5 | `skills/worldbuilder-character/relationships.md:25` | Kin lacks Charge's resist-protection engine | Confirmed, and worse than stated |
| 6 | `relationships.md:63, :67, :140` | two scans state the same clauses | Confirmed — it is three passages, not two |
| 7 | `skills/worldbuilder-character/framework.md:83-84` | non-competence branch has no Wrong/Right pair | Confirmed |

Detail where the finding differs from the original note:

**Site 3 is narrower than "under-covers".** The gap is specific: `writing-style.md:68` added vague declaratives in sentence form ("the stakes are high", "the reasons are structural", "the implications are significant"). The `Significance inflation` section of `slop-phrases.md` lists single words and phrases only, so those sentence forms have no checklist entry. The Cut filler groups are a separate question and are not part of this gap.

**Site 5 is worse than stated.** Charge produces "conflict when the charge resists protection" and explicitly excludes family ("Not kin — family responsibility is Kin"). So the only archetype covering family protection has no resist-protection engine, and cannot borrow one.

**Site 6 involves three passages, not two.** `:63` already carries the hard cap ("no archetype may appear more than twice") along with the arithmetic; `:67` restates it as "three or more times is wrong"; `:140` restates it again. The original note saw only `:67` and `:140`.

**Trait-rule ownership.** The rule with the competence and non-competence branches lives at `writing-style.md:143`. `framework.md:81` defers to it and supplies the character-specific worked cases, so the missing non-competence example belongs in `framework.md`, not in the rule's own file.

**Gates covering these paths.** `python -m pytest tests -q` passes at 13 tests. CI also runs `doodle --strict skills` pinned at 1.0.0; doodle discovers `SKILL.md` files only, so `writing-style.md`, `relationships.md` and `framework.md` are not linted by it — a local `doodle --strict skills` returns "no issues found" and stays clean regardless of these edits. `docs/` is outside both gates. Local doodle is 0.5.0 against CI's 1.0.0, so a local pass does not prove the 1.0.0-only spellcheck clean.

## Consolidation

Three implications for the plan:

1. **Nothing here is speculative.** Every site has verified text and a known fix shape, so the work is scoped edits rather than investigation.
2. **No automated gate will catch a prose regression in these files.** Verification must be explicit greps for the exact strings added and removed, plus the pytest suite as a no-collateral-damage check.
3. **The `:63` finding changes what "collapse the duplication" means.** With the cap already stated at `:63` and the checklist at `:140`, softening `:67` must avoid restating `:63` rather than merely dropping the numeric threshold.
