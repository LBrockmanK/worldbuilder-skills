# Codex CLI generation reference

Invocation pattern for generating character notes via GPT models using
the Codex CLI (`codex exec`).

## Command

```bash
codex exec -m <model> -s workspace-write "<prompt>"
```

Or with prompt on stdin (preferred for long prompts):

```bash
cat inputs/packet.md inputs/nadja-inputs.md inputs/world-context.md inputs/roster.md | \
  codex exec -m <model> -s workspace-write -
```

## Models

- `gpt-5.6-sol` — GPT-5.6 Sol
- `gpt-5.6-terra` — GPT-5.6 Terra

## Key flags

- `-m <MODEL>` — model override (bypasses config.toml default)
- `-s workspace-write` — sandbox mode allowing file writes in the workspace
- `-s read-only` — for review-only tasks (used by adversarial review)
- `-` as prompt arg — read prompt from stdin
- `-c key=value` — override config.toml values

## Prompt delivery

The prompt travels on stdin, not argv — a multi-line argv element is
mangled by the .cmd shim layer on Windows (observed in
review_dispatch.py). `codex exec` reads stdin to EOF as its prompt.

## Source

Adapted from `fleet/scripts/review_dispatch.py` (adversarial review
wrapper) and `codex exec --help`.
