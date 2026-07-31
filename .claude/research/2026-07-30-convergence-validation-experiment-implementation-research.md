---
type: research
title: Convergence validation experiment implementation research
description: 'Implementation research for the cross-model convergence validation
  experiment: trial kit patterns, input locations, model access, detection method
  requirements'
tags:
- complete
date: 2026-07-30
timestamp: 2026-07-30T13:27Z
resources:
- '[[2026-07-30-cross-model-convergence-metric-validation-experiment]]'
---

# Convergence validation experiment implementation research

## Goals

Gather implementation details needed to plan the convergence validation
experiment: trial kit patterns, input file locations, model access
methods, detection method dependencies.

## Results

### Trial kit pattern

The existing trial at `trials/2026-07-writing-doctrine/` establishes
the pattern: `build.py` assembles instruction packets from source
components, agents are dispatched independently (packet + brief, no
shared context), each writes an output note. `README.md` documents the
run procedure. `rubric.md` provides the scoring template.

### Character generation skill structure

`skills/worldbuilder-character/` contains:
- `SKILL.md` — frontmatter and overview; sections worked in order
- `framework.md` — Background, Body, Soul section instructions
- `relationships.md` — 12 relationship archetypes; includes one inline
  self-review check (line 111)
- `intimate.md` — optional conditional section

Supporting doctrine:
- `skills/writing-style.md` — shared Wide-phase writing reference;
  screening test: "Can a director stage this sentence?"
- `docs/slop-phrases.md` — reviewer checklist for slop patterns

### Input locations in Viralys

Base: `D:\Sync\Collective Consciousness\Games\Ainime\WIP\Viralys\`

Per-character inputs (Design Notes section of each note):
- `worldvault/notes/nadja.md` lines 21-45: Session Notes (23-39) +
  Builder Context (40-45)
- `worldvault/notes/kallya.md` lines 21-56: Session Notes (21-50) +
  Builder Context (51-56)

World-level context (no direction.md exists):
- `worldvault/seed.md` — world premise
- `worldvault/agent-context.md` — agent briefing
- `worldvault/worldbuilding-plan.md` — project plan

Cast/roster: `worldvault/notes/` contains 8 character notes.

### Model access

- Claude Opus 4.6, Opus 5: Agent tool with model override or API.
- GPT-5.6 Sol, GPT-5.6 Terra: Codex CLI (confirmed 2026-07-26).

### Detection method dependencies

- Method 1 (exact match): pure Python, no dependencies.
- Method 2 (embedding similarity): embedding model from a third family,
  cosine similarity. Starting threshold 0.92.
- Method 3 (LLM-as-judge): judge model from a third family.

## Consolidation

The experiment follows the existing trial kit pattern with
modifications: one instruction packet assembled from current skill
files (not trial-specific packets), per-character inputs extracted from
Design Notes sections only (finished note content excluded), four model
targets instead of six arm variants. Detection and correction are new
infrastructure not present in the prior trial.
