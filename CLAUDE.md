# worldbuilder-skills

Workflow skills for building and realizing player world visions for the ainime-games.com world builder platform. Currently housed in the Sunmist Valley project during development; will be extracted to a standalone `worldbuilder-skills` repo.

## Agent skills

### Issue tracker

Issues tracked in GitHub Issues (LBrockmanK/worldbuilder-skills). See `docs/agents/issue-tracker.md`.

### Triage labels

Default mattpocock label vocabulary — no overrides. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context. `CONTEXT.md` and `.claude/adr/` at the repo root. See `docs/agents/domain.md`.

### Session memory

Project state, architecture decisions, and feedback are tracked in `memory/`. Read `memory/MEMORY.md` at the start of every session to load current context. Write new memories there — not to any external Claude memory directory.
