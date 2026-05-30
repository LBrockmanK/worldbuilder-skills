---
name: feedback-agent-references
description: Vault template and skill content must never name a specific AI model; use model-agnostic phrasing instead
metadata:
  type: feedback
---

Never refer to "Claude" (or any specific AI model name) inside worldvault template files, stub notes, or skill instructions that will be used by end-users. Some users will run these skills with a different model.

**Why:** The worldbuilder-skills set is model-agnostic. Naming a specific model locks users in and creates confusion when they use a different agent.

**How to apply:** Replace "For future Claude:" blockquotes in note templates and stub notes with "For future agents:" or equivalent model-neutral phrasing. This applies to: `_templates/*.md`, `worldbuilding-plan.md`, `log.md`, `seed.md`, and any skill output that gets written into user vaults.
