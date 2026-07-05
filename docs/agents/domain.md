# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root — single-context repo
- **`.claude/adr/`** — read ADRs that touch the area you're about to work in

If any of these files don't exist, **proceed silently**. Don't flag their absence; don't suggest creating them upfront. The producer skill (`/grill-with-docs`) creates them lazily when terms or decisions actually get resolved.

## File structure

Single-context repo:

```
/
├── CLAUDE.md
├── CONTEXT.md
├── .claude/
│   ├── adr/            ← architectural decision records
│   │   ├── 0001-three-phase-architecture.md
│   │   ├── 0002-seed-as-target-format.md  (superseded by 0003)
│   │   └── 0003-platform-decoupling.md
│   ├── specs/          ← scraibe-managed vault (specs, plans, research)
│   └── plans/
├── defaults/
│   ├── okf.json        ← the OKF preset shipped to player projects (generated)
│   ├── okf.base.json   ← preset source; template bodies referenced by file
│   └── templates/      ← markdown template sources, one per typed note
├── scripts/
│   └── build-okf.py    ← regenerates defaults/okf.json from the sources
├── docs/
│   ├── agents/         ← agent configuration (this file and siblings)
│   └── target-system.md  ← ainime field reference (export skill uses this)
└── skills/
    └── worldbuilder-*/   ← individual skill directories
        └── SKILL.md
```

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a test name), use the term as defined in `CONTEXT.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal — either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/grill-with-docs`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0001 (three-phase architecture) — but worth reopening because…_
