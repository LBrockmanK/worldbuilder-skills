---
type: spec
title: Retool worldbuilder-skills on scraibe base
description: Strip note-taking/vault management from worldbuilder skills; scraibe
  owns file management via OKF. This plugin defines worldbuilding types and deliverables
  only. First live trial of scraibe as a base plugin.
tags:
- human-ready
date: 2026-07-04
timestamp: 2026-07-05T06:54
resources: []
---

# Retool worldbuilder-skills on scraibe base

## Context

Scraibe (okf-enforcement repo) now owns note-taking and vault file management: OKF-enforced frontmatter, document creation via `new_doc.py`, status/tag lifecycle, inbox/triage, audit, indexes, and generated rules. This plugin's early vault logic (worldvault template, setup skill's file scaffolding, per-skill folder conventions) predates scraibe and is fully superseded by it.

Decision trail:
- `okf-enforcement/.claude/specs/2026-07-04-scraibe-skills-design.md` — "Related External Work": pare worldbuilder-skills down to writing/creation guidelines.
- `okf-enforcement/.claude/grillings/2026-07-02-scraibe-deferred-items-grilling.md` — Obsidian vault config template findings: scraibe supersedes this plugin's note-taking logic.

This retool is the first live trial of scraibe as a base plugin for a domain skillset. Friction points in scraibe's extension surface (type registry, enforced paths, setup/migration flow) should be captured as we hit them and fed back to the scraibe repo.

Verified in passing (inbox item, resolved 2026-07-04): scraibe's `defaults/obsidian/` copy of this plugin's Obsidian template was already generalized correctly — `attachmentFolderPath`, `templates.json`, and `workspace.json` (which carried worldbuilder filenames and stale `.tmp` entries) were dropped, and the frontmatter-modified-date plugin was retargeted from `last_modified`/`YYYY-MM-DD HH:mm` to OKF's `timestamp`/`YYYY-MM-DDTHH:mm`. Nothing worldbuilding-specific leaked.

## Decisions

Approved section by section with the user, 2026-07-04. Approach chosen: **preset + craft skills** — the plugin ships an OKF preset and craft knowledge; scraibe owns all file management. Rejected alternatives: pushing worldbuilder types upstream into scraibe (couples scraibe to a domain), and wrapper skills that keep owning creation flow (dual sources of truth, strips nothing).

### Vault layout and OKF preset

A player project after setup:

```
<project>/
  .claude/okf.json      ← written from this plugin's defaults/okf.json
  .claude/rules/        ← generated (generate_rules.py)
  .claude/glossary.md   ← seeded with platform terms ("world info" = lorebook)
  .claude/inbox.md
  .obsidian/            ← scraibe defaults + app.json overlay (attachmentFolderPath)
  Home.md  _bases/  _attachments/   ← chrome, unenforced
  project/              ← enforced: seed.md, plan.md, direction.md
  notes/                ← enforced: all entity notes, flat
```

- Enforced paths: `notes/` and `project/`, full level. Chrome stays at root unenforced (root-level enforcement would force frontmatter onto `Home.md`). `project/` exists because unenforced project docs are how `log.md` rotted.
- Type registry (draft exists at `defaults/okf.json`, JSON round-trip verified): entity types `character` (fields: factions), `location` (region, function, primary-characters), `faction` (members, function), `event` (characters, location, layer), `concept` (layer required, trigger-context), `story` (scope required, up); project types `seed`, `plan`, `direction`, `reference`. Body templates carried verbatim from `_templates/`; event's template is new, codifying the three sections `worldbuilder-event` already mandates (Design Notes, What Happens, Scene Effects).
- Frontmatter mapping: `status: draft` → open status tag; `brief` → universal `description`; `last_updated` → universal `timestamp` (Obsidian modified-date plugin already targets it); `aliases` kept as optional universal. Event's in-world `date:` field is dropped entirely — timing lives in body text ("What Happens" opens with when); the export skill reads bodies and its output is deliberately non-OKF.
- Status tags: scraibe's stock six, unchanged (`human-ready`/`agent-ready` open; `complete`/`deprecated`/`abandoned`/`archived` closed; `priority`/`deferred` behavioral). No invented vocabulary.
- Retired root docs: `log.md` (inbox + git history cover it), `agent-context.md` (generated `rules/` covers it).

### Skill surface (eleven skills → nine, no agents)

- `worldbuilder-setup` → thin adopter, five steps: write `.claude/okf.json` from the preset; copy scraibe Obsidian defaults + chrome overlay; create the three `project/` docs via `new_doc.py`; seed the glossary; `generate_rules.py` + `validate.py`. First act: verify scraibe is installed (hard dependency, no degradation mode). Converges with `scraibe:setup` plugin orchestration via `setup-state.json`.
- `worldbuilder-world-planning` → retired. Cast-planning content (roster design, household architecture, Wide-phase dependency ordering) moves into `worldbuilder-world-foundation` first; routing evaporates into `scraibe:orient`/`scraibe:triage`.
- Six craft skills (character, location, faction, event, concept, story) → strip all plumbing ("Working with Vault Files", frontmatter specs, folder paths); keep doctrine (action-line style, positive statements, starting-state-only, relationship POV, section guidance, self-checks). Schema arrives via generated rules at edit time and `new_doc.py` at creation time. `worldbuilder-event` additionally replaces its frontmatter section with timing-in-body guidance.
- `worldbuilder-world-foundation` and `worldbuilder-story` keep their Phase-1 deliverables (seed, direction), now as typed docs in `project/`.
- `worldbuilder-ingestion` → dissolved. Generic process rules proposed as `scraibe:ingest` updates (friction log #10); "constant lorebook entries are seed material" → one line in `worldbuilder-concept`; card-quality signals already in `worldbuilder-character`; "world info = lorebook" → glossary. Trigger reliability improves: arriving with source material triggers `scraibe:ingest`; the judgments live in the craft skills that fire on the extracted material.
- Linker agent → dropped. Write-side linking absorption into scraibe was the original goal and never completed (friction log #9); handoff includes the linker material as a starting point. Until scraibe grows it, generated rules instruct agents to wikilink entity references as they write.
- `worldbuilder-ainime-export` → least changed: reads `description` instead of `brief`, checks status tags for export readiness (seed `complete`, cast notes closed), keeps `target-system.md`; output remains non-OKF by design.

### Session workflow

- First run: `worldbuilder-setup` (triggered directly or via `scraibe:setup` orchestration) → hands off to `worldbuilder-world-foundation` for the seed conversation.
- Returning sessions: SessionStart summary → `scraibe:triage` if pending work, `scraibe:orient` for briefings, craft skills on demand. Mid-session ideas go to the inbox (capture hook enforces). No worldbuilder session-start skill exists.
- Phases (Seed → Wide → Export) survive as structure in `project/plan.md` (phase table + cast plan) and in craft-skill trigger descriptions — guidance, not a mechanical lock. The export skill owns its own gate via status preflight; audit close-out heuristics nudge notes to `complete`.
- Integrity layers (all scraibe's): `new_doc.py` stamps creation, hooks + scoped rules police edits, `validate.py`/audit catch after-the-fact violations (e.g., player hand-creates a note in Obsidian; next session repairs it).

### Repo changes

Delete: `agents/` (linker, after export to scraibe handoff); `skills/worldbuilder-ingestion/`; `skills/worldbuilder-world-planning/` (after content move); worldvault `_templates/`, stub notes, and `.obsidian/` (except an `app.json` overlay with `attachmentFolderPath`); `dev-feedback.md` (superseded by inbox; user approved).

Add: `defaults/okf.json` (exists as draft); `defaults/templates/*.md` — the six template markdown sources as the human editing surface; `scripts/build-okf.py` regenerating `defaults/okf.json` from them (dies if scraibe adds template file references, friction log #6).

Rewrite: all nine surviving SKILL.md files (light pass for seven, heavy for setup and event); `CONTEXT.md` (new architecture); `README.md` and `CLAUDE.md` (scraibe dependency declared). Untouched: `docs/target-system.md`, `docs/slop-phrases.md`, `docs/agents/`, `memory/`.

### Verification

1. Scratch-project trial: run retooled setup; `okf.json` validates, rules generate, `project/` docs pass `validate.py` clean.
2. Build one character and one event through the craft-skill flow in the scratch project; hooks accept, frontmatter correct, no hand-fixing.
3. Export dry-run against the minimal world (proves `description`/status reads).
4. Leftover sweep: grep surviving skills for retired vocabulary (`world-planning`, `linker`, `ingestion index`, `log.md`, `agent-context.md`, `last_updated`, `brief:`).
5. User check: Bases views render correctly in Obsidian (requires human).

## Scraibe friction log (trial run, 2026-07-04)

Problem points hit while using scraibe as a base, to be delivered to the okf-enforcement repo's inbox:

1. `new_doc.py` prints mixed path separators on Windows (`.claude/specs\2026-...`). Cosmetic.
2. No `research` type in the default registry; scraibe's own vault uses `reflection`/`reference` in a `research/` directory, but the convention is implicit — consuming projects must read scraibe's vault to learn it.
3. SessionStart summary reported inbox items but not the open-document set; triage's fallback (walk `index.md` listings) fails on first use because indexes don't exist yet. Chicken-and-egg on adoption.
4. Historical documents migrated into an enforced path trip OKF-005 on placeholder/example wikilinks (`[[Name]]`, `[[The Valley]]`) inside their bodies; no way to mark content as illustrative.
5. `validate.py` human output garbles em-dashes in the Windows console (codepage). Cosmetic.
6. Type body templates are single-line escaped JSON strings in `okf.json` — unpleasant to author and review for long structured templates (character template is ~850 chars). Template file references would fix this; meanwhile this plugin keeps markdown originals and regenerates the JSON.
7. Field types support text/list/tags/date/datetime but not boolean (event `recurring` had to become body text / text field).
8. `links.py` extracts frontmatter links only from `output`/`superseded-by`; domain link fields (`factions`, `members`, `characters`, `up`) are invisible to backlink analysis. Configurable link-bearing fields would fix this.
9. Lost goal (2026-07-04 design session): the worldbuilder linker agent was meant to be absorbed into scraibe entirely, but scraibe only got read-side link analysis (`links.py`, audit checks). The write side — deterministic forward/back-link insertion, rename-with-link-rewrite, and the LLM post-pass review agent — never landed. This plugin drops its linker on the strength of that absorption, so scraibe needs to pick it up. To prevent redoing work, the linker material (`agents/linker.md` — agent definition, LLM post-pass review flow — and `agents/linker/scripts/`: link-notes.ps1, list-notes.ps1, rename-note.ps1, unresolved-links.ps1) is copied into a self-contained reference directory in the okf-enforcement repo, pointed to by that repo's inbox entry; this repo's copy is then removed during implementation.
10. Proposed `scraibe:ingest` updates (from dissolving `worldbuilder-ingestion`): (a) with multiple overlapping sources, establish precedence before extraction and surface contradictions upfront; (b) when ingested material seeds derivative work, ask the fidelity level (strict vs. inspired-by) before extracting; (c) documents from an earlier version of one's own workflow that don't match current type templates are source material requiring reprocessing, not completed documents.

## Consequences

- Scraibe becomes a hard dependency: without it installed, the plugin does nothing. Declared in README/marketplace metadata; `worldbuilder-setup` checks for it first.
- Parts of the design are contingent on the okf-enforcement repo accepting handoff items: write-side linking (#9), ingest generalizations (#10), template file references (#6). Fallbacks exist for each (rules-driven linking, two-line skill insertions, the build-okf.py step) so the retool does not block on them.
- Player vaults built with the old worldvault template are not auto-migrated by this retool; bringing one forward is a `scraibe:setup` migration run with the worldbuilder registry, and can be designed when one actually needs it.
- The friction log plus linker material gets delivered to okf-enforcement's inbox after spec approval (tracked in this repo's inbox).
- `docs/restructure-notes.md` (now `.claude/specs/restructure-notes.md`) remains accurate for the platform-decoupling decisions but its vault-structure sections are superseded by this spec.
