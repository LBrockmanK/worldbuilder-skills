---
name: feedback-show-artifacts
description: Design approval needs the concrete artifact AND full prose explanation — no one-line option chips or unexplained summaries
metadata:
  type: feedback
---

When asking for design approval: show the actual artifact (draft file contents, exact paths), and explain each decision in full prose — complete sentences with reasoning. Do not compress design decisions into one-line multiple-choice option descriptions; a single line is not an explanation.

**Why:** During the 2026-07-04 retool design review the user rejected two approval prompts in a row: first a prose summary with no artifact ("you need to actually show me what you're talking about, or at least tell me what file it is"), then an artifact with one-line option chips ("a prose description is fine, but a single line is not an explanation. Use your words").

**How to apply:** For design reviews, write the section as real explanatory prose around the artifact and ask the approval question in plain text in the message body. Avoid the structured-question widget for design approvals; its option format truncates reasoning. Content shown between tool calls can render as collapsed/nested subsections in the desktop app and go unseen — put review material in the main (final) chat block. Never link a file that doesn't exist on disk yet; write the draft artifact to disk first so the link resolves. Related: [[project-restructure]].
