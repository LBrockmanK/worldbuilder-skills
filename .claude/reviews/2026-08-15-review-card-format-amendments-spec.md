---
type: review
title: Review — Card Format Amendments Spec
description: Adversarial review of the card format amendments spec (Body appearance
  preamble and Story Beats addon block).
tags:
- human-ready
date: 2026-08-15
timestamp: 2026-08-15T17:19Z
resources: []
---

# Review — Card Format Amendments Spec

## Rounds
## Round 1 — digest `d085fb63…`, anchor `73675fff` (dirty), tokens 68907, 2026-08-15T11:58:04-05:00, 299s

Anchor: 73675fffd56ddfcd3618cbb96290a36b4b18f909 (dirty tree)
Artifact digest: d085fb632ea653adf176683dd2dac96657c20b9d038edf1280cff280c3584910 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md

1. Title: Hidden static features have no valid Q&A path
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:59-64,78-82
   Quote:
   ```
   **What goes in the preamble:** hair, eyes, skin, build, distinguishing
   physical features, default or seasonal clothing. What you would see
   in a portrait.

   **What stays as entries:** physical mannerisms, posture habits, how
   they move or carry themselves — anything that passes the staging test.
   ```
   ```
   Immediate column
   covers the preamble (surface features, first impression), Over Time
   and Hidden columns cover behavioral entries.
   ```
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: The existing Body grid places scars, marks, and other features hidden under clothing in the Hidden column. D1 assigns static distinguishing features to the preamble, but then declares that Hidden produces behavioral entries. A hidden scar is neither immediate nor behavioral, so the proposed workflow cannot represent it without violating one of D1’s rules. Storage format and depth-of-access must be treated as independent dimensions.

2. Title: The preamble example does not use the required sentence format
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:45-54,68-71
   Quote:
   ```
   Body opens with a
   short prose block (1-3 sentences) describing the character's static
   physical appearance
   ```
   ```
   > Pink hair past her shoulders, wavy, with a bow on top. Purple eyes,
   > brown skin. Her spring outfit is a magenta bodice over white puffed
   > sleeves, dark navy skirt with floral embroidery — the outfit changes
   > with the season but the bow stays.
   ```
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The first two punctuated units are noun fragments without finite verbs, not sentences. They also cannot demonstrate the stated active-voice rule. The principal D1 example therefore contradicts the defined preamble format and writing rules.

3. Title: The Body-entry example violates the existing one-sentence format
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:45-48,73-74
   Quote:
   ```
   followed by the existing behavioral entries as
   bullet points.
   ```
   ```
   > - She always has something to write with. A pen at the desk, a
   >   clipboard at the quest board...
   ```
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The existing Body entry contract is one stageable sentence per entry. This bullet contains one sentence followed by a separate fragment and an ellipsis. It therefore does not demonstrate the unchanged behavioral-entry format promised by D1.

4. Title: Story Beats is selected twice and its workflow position is circular
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:90-94,152-156
   Quote:
   ```
   **Session opening:** recommend Story Beats when the character has
   progression-gated events (relationship milestones, story
   involvement), when the target platform supports future storylines or
   alternate greetings, or when the source material provides rich
   scenario data. The user decides.
   ```
   ```
   **Q&A workflow change:** after Voice/Dialogue (or after the last
   selected addon block), ask whether the character has narrative
   milestones, story events, or progression-gated encounters worth
   capturing.
   ```
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: Session opening already decides whether Story Beats is selected, but the later flow asks the selection question again. If Story Beats is the only selected addon, it is itself the “last selected addon block,” making the stated placement circular; if no addon was selected, there is no last selected addon. The flow must instead say when to work through an already-selected Story Beats block, including the sole-addon case.

5. Title: The calendar boundary does not cover one-time scheduled events
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:120-126
   Quote:
   ```
   - Story Beats vs. calendar events: calendar events are recurring
     scheduled occurrences (festivals, weekly gatherings). Story Beats
     are one-time or progression-gated narrative moments.
   ```
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: Existing export rules also place one-time narrative events with concrete calendar days into `storyTriggers[]` with `recurring: false`. Such an event is both one-time and scheduled, so it satisfies D2’s Story Beats definition while remaining a calendar trigger under existing content. D2 needs an explicit discriminator for dated one-time events and must say whether character-specific material coexists with, links to, or replaces the calendar trigger.

6. Title: The SillyTavern mapping drops required trigger conditions
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:96-102,128-131
   Quote:
   ```
   - A trigger/condition note (what relationship state, story progress,
     or situation makes this scenario available)
   ```
   ```
   - SillyTavern: Story Beat scenario prose maps to alternate greetings
     (each beat becomes an opening message establishing that scenario)
   ```
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: high (alters shared state, interfaces, or persisted data)
   Channel: fix
   Body: The mapping exports only scenario prose and gives no destination or degradation rule for the required title and trigger/condition. An alternate greeting is available as an opening message and cannot by itself enforce a relationship or story-progress gate. The export contract therefore loses the semantics that make these scenarios “triggerable.”

7. Title: Story Beats cannot directly satisfy ainime Future Storylines rules
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:128-150
   Quote:
   ```
   - ainime: Story Beat entries map to the future storylines section
   ```
   ```
   > Adeline takes the player on a walking tour of Mistria to check on
   > everyone. Landen warns her not to push herself; she deflects. She
   > admits enjoying the company but offers the player an exit. At the
   > end, her first instinct is to return to her desk — the player can
   > suggest a meal at the Inn instead.
   ```
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: high (alters shared state, interfaces, or persisted data)
   Channel: fix
   Body: The existing ainime assembler requires Future Storylines to be phrased as possibilities and forbids scripted outcomes. D2’s example instead states a definite sequence through “At the end.” The spec provides no transformation from definite scenario prose into the exporter’s possibility-style engine format, so its ainime mapping is not implementable without violating existing export rules.

8. Title: The Story Beats example violates its observable staging rule
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:104-109,141-142
   Quote:
   ```
   - Prose follows the action-line convention (present tense, observable)
   - Staging test applies to the scenario description
   ```
   ```
   > first. The evening is administrative and warm and entirely her idea
   > of a good time.
   ```
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: “Warm” and “entirely her idea of a good time” are authorial interpretations rather than observable action or speech. A director cannot stage that sentence without inventing manifestations beyond the text. The example therefore fails the two rules it is supposed to demonstrate.

9. Title: Story Beats contradicts the existing story-note ownership boundary
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:84-88
   Quote:
   ```
   Add Story Beats as an addon block. It is included when the character
   has triggerable narrative scenarios worth specifying — not required
   for every character.
   ```
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: The current `worldbuilder-character/SKILL.md` explicitly says story possibilities live in separate intention-scoped story notes, not in character notes. Adding narrative scenarios to the character card creates two conflicting authoritative destinations. The amendment must revise that section and define the boundary between a character-local Story Beat and a separate story note.

10. Title: Both new formats contradict the all-bullets working-document contract
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:45-51,96-102
   Quote:
   ```
   Add an appearance preamble to the Body section. Body opens with a
   short prose block (1-3 sentences) describing the character's static
   physical appearance, followed by the existing behavioral entries as
   bullet points.

   **Preamble rules:**
   - Descriptive prose, not bulleted entries
   ```
   ```
   **Entry format: labeled prose blocks.** Each entry has:
   ```
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: Both `card-format.md` and `worldbuilder-character/SKILL.md` currently require entries under section headings to be bullet points. D1 introduces non-bulleted Body content, while D2 introduces labeled prose blocks, but the amendment does not reconcile either working-document rule. Implementing only the named Body and addon sections would leave contradictory instructions active.

11. Title: The completion-checklist no-change claim is false
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:167-171
   Quote:
   ```
   - The worldbuilder-character SKILL.md session flow gains a Story
     Beats step after Voice/Dialogue
   - The SKILL.md session opening gains a Story Beats addon decision
   - The completion checklist's "selected addon blocks completed" item
     already covers Story Beats without modification
   ```
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The current checklist’s parenthetical explicitly enumerates Relationships, Intimate Dynamics, and Voice / Dialogue “as determined in session opening.” It does not include Story Beats. Leaving the closed list unchanged makes the newly selected block invisible to the finalization gate.

12. Title: Consequences omits the character template and generated preset
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:161-173
   Quote:
   ```
   ## Consequences

   - Body section in card-format.md gains a preamble definition before
     the entry format specification
   - The addon blocks list grows from three (Relationships, Intimate
     Dynamics, Voice/Dialogue) to four (adding Story Beats)
   ```
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: `defaults/templates/character.md` currently seeds Body with only a bullet placeholder and has no Story Beats heading. It must change for new notes to use either decision. Repository policy then requires regenerating `defaults/okf.json`, which embeds that template. Neither required file appears in Consequences, violating the complete-file-enumeration criterion.

13. Title: Consequences omits the exporter instructions that must consume the new schema
   Location: .claude/specs/2026-08-15-card-format-amendments-body-appearance-preamble-and-story-beats-addon.md:172-173
   Quote:
   ```
   - Export mapping documentation (extraction-reliability-map.md) needs
     entries for the new block's platform fields
   ```
   Type: completeness
   Severity: major
   Effort-to-fix: large (reaches beyond the scoped change)
   Risk-of-fix: high (alters shared state, interfaces, or persisted data)
   Channel: fix
   Body: Updating the reliability map alone does not change export behavior. `skills/worldbuilder-ainime-export/SKILL.md` still reads appearance from a separate Appearance section, and `skills/worldbuilder-ainime-export/card-assembly.md` still reads Future Storylines from a Storylines section under different writing rules. Both files require modification to consume the Body preamble and Story Beats block. Their omission means the stated export mapping would not ship.

FINDINGS: 0 critical, 13 major, 0 minor, 0 nit

### Adjudication — Round 1

All 13 findings accepted and fixed in the spec:

1. **Accept.** Fixed: preamble now covers all static appearance regardless of depth; hidden static features (scars, marks) explicitly included; grid note revised to say preamble covers static appearance at all depths while grid guides behavioral entries only.
2. **Accept.** Fixed: format changed from "1-3 sentences" to "short descriptive prose (sentences or descriptive clauses)." Example rewritten with proper sentence structure.
3. **Accept.** Fixed: Body entry example trimmed to one sentence.
4. **Accept.** Fixed: removed duplicate selection question from Q&A workflow change. Now says "when Story Beats is selected at session opening, work through the block after Voice/Dialogue."
5. **Accept.** Fixed: calendar distinction now explicitly handles dated one-time events — the calendar entry records the date, the Story Beat carries the narrative.
6. **Accept.** Fixed: SillyTavern export mapping now notes that trigger conditions are degraded to narrative framing within the greeting text when the platform cannot mechanically enforce them.
7. **Accept.** Fixed: ainime export mapping now specifies transformation from definite scenario descriptions to possibility-style framing.
8. **Accept.** Fixed: both example entries rewritten to pass staging test — removed "warm and entirely her idea of a good time" and scripted sequence language.
9. **Accept.** Fixed: added "Boundary with story notes" section defining the distinction — Story Beats are character-local hooks; story notes are full arc documents with their own lifecycle. Added to Consequences: SKILL.md Story Notes section must acknowledge the boundary.
10. **Accept.** Fixed: both D1 and D2 now include explicit working-document convention notes acknowledging the non-bullet format as a recognized exception. Added to Consequences: card-format.md working-document conventions section must be updated.
11. **Accept.** Fixed: Consequences now includes "completion checklist parenthetical must add Story Beats to the enumerated addon blocks."
12. **Accept.** Fixed: Consequences now includes `defaults/templates/character.md` and `defaults/okf.json` regeneration requirement.
13. **Accept.** Fixed: Consequences now includes `skills/worldbuilder-ainime-export/SKILL.md` and `card-assembly.md` as files requiring modification.

## Round 2 — digest `f55dc308…`, anchor `73675fff` (dirty), tokens 56571, 2026-08-15T12:17:55-05:00, 159s

Anchor: 73675fffd56ddfcd3618cbb96290a36b4b18f909 (dirty tree)
Artifact digest: f55dc308530015d462bacc20e7a61379f47b015bb0484645ba2616e1c4683d7e (sha256 over the exact scoped bytes as delivered)
Scope: .claude/plans/2026-08-15-card-format-amendments-implementation-plan.md

1. D1 and D2 omit the normative meta-vocabulary prohibition
   Location: .claude/plans/2026-08-15-card-format-amendments-implementation-plan.md:59-66,81-86
   Quote:
   > **Appearance preamble:** Body opens with short descriptive prose
   > (sentences or descriptive clauses) covering the character's static
   > physical appearance. The preamble is exempt from the staging test.
   > Orwell co-anchor and trait-word ban apply. Content: hair, eyes,
   > skin, build, distinguishing physical features, default or seasonal
   > clothing, and hidden static features (scars, marks, tattoos) when
   > relevant — everything about what this person looks like, regardless
   > of depth-of-access.
   >
   > Optional. Included when the character has triggerable narrative
   > scenarios worth specifying. Labeled prose blocks — each entry has a
   > short title, a trigger/condition note, and 2-4 sentences of scenario
   > prose following the action-line convention. Staging test applies.
   > Orwell co-anchor applies. Condition notes are factual, not
   > prose-styled.
   Type: completeness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Both D1 and D2 normatively prohibit builder-layer meta-vocabulary, but neither proposed definition carries that rule. The global writing-style constraint does not supply it, and the existing Body/Soul rules also lack it. Consequently, implementing the plan as written loses a normative rule from both decisions despite the plan claiming to consume them verbatim.

2. Story Beats omit required scenario-content coverage
   Location: .claude/plans/2026-08-15-card-format-amendments-implementation-plan.md:81-86
   Quote:
   > Optional. Included when the character has triggerable narrative
   > scenarios worth specifying. Labeled prose blocks — each entry has a
   > short title, a trigger/condition note, and 2-4 sentences of scenario
   > prose following the action-line convention. Staging test applies.
   > Orwell co-anchor applies. Condition notes are factual, not
   > prose-styled.
   Type: completeness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: D2 requires every scenario’s 2–4 sentences to describe the setup, the key action or exchange, and what the event reveals about the character. The proposed authoritative definition reduces this to unspecified “scenario prose,” and no later task restores those required components. Cards produced from the implemented format could therefore satisfy the plan while failing D2.

3. Session Flow’s exhaustive addon order remains stale
   Location: .claude/plans/2026-08-15-card-format-amendments-implementation-plan.md:125-135
   Quote:
   > - [ ] **Step 5: Update SKILL.md session flow — addon blocks**
   >
   > In the Addon blocks subsection, after the Voice / Dialogue paragraph, add:
   >
   > ```markdown
   > **Story Beats:** When selected at session opening, work through Story
   > Beats after Voice / Dialogue (or after the last selected addon
   > block). Ask about narrative milestones, story events, or
   > progression-gated encounters. Work through them in approximate
   > narrative order. See `card-format.md` for entry format, writing
   > rules, and distinctions from other sections.
   > ```
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The existing subsection begins with an exhaustive ordered list ending at Voice / Dialogue. This step only appends a new explanatory paragraph and does not update that list to include Story Beats. The resulting SKILL.md would simultaneously say to process selected addons in a three-block order and separately describe a fourth block, leaving the executable workflow internally contradictory.

4. The ainime `appearance` mapping is not migrated to the Body preamble
   Location: .claude/plans/2026-08-15-card-format-amendments-implementation-plan.md:248-250
   Quote:
   > - [ ] **Step 4: Update card-assembly.md — Body preamble in export**
   >
   > In `skills/worldbuilder-ainime-export/card-assembly.md`, in the section that assembles the character prose (around line 21 where "Who they are at a glance" is constructed), add a note that the Body preamble provides the physical appearance description and is included verbatim in the assembled prose.
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: This only routes the preamble into assembled `baseProfile` prose. The current export SKILL still maps the nonexistent “Appearance section” to `characters[].appearance`; Task 2’s SKILL change covers only Story Beats. Thus the dedicated appearance field remains sourced from an obsolete section, violating the consequence that the ainime export consume the Body preamble.

5. The extraction map and SillyTavern mapping are entirely omitted
   Location: .claude/plans/2026-08-15-card-format-amendments-implementation-plan.md:202-210
   Quote:
   > ### Task 2: Template, Preset, and Export Updates (downstream consumers)
   >
   > **Files:**
   > - Modify: `defaults/templates/character.md:21-25` (Body section)
   > - Modify: `defaults/templates/character.md` (add Story Beats heading)
   > - Generated: `defaults/okf.json` (via `python scripts/build-okf.py`)
   > - Modify: `skills/worldbuilder-ainime-export/card-assembly.md:91-101` (Future Storylines)
   > - Modify: `skills/worldbuilder-ainime-export/card-assembly.md:21` (Body prose)
   > - Modify: `skills/worldbuilder-ainime-export/SKILL.md` (Story Beats export mapping)
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The governing spec requires `extraction-reliability-map.md` to gain mappings for the new platform fields and defines Story Beats as the source for SillyTavern alternate greetings. The repository contains `docs/extraction-reliability-map.md`, including a currently stale `alternate_greetings[]` row, but the plan neither updates it nor explicitly defers it. No other task implements or defers the SillyTavern half of D2’s export mapping.

6. Two declared line ranges extend past EOF and one mislabels most of its range
   Location: .claude/plans/2026-08-15-card-format-amendments-implementation-plan.md:40-44
   Quote:
   > - Modify: `skills/worldbuilder-character/card-format.md:113-142` (working-document conventions)
   > - Modify: `skills/worldbuilder-character/SKILL.md:32-41` (session opening)
   > - Modify: `skills/worldbuilder-character/SKILL.md:44-69` (session flow)
   > - Modify: `skills/worldbuilder-character/SKILL.md:123-126` (story notes)
   > - Modify: `skills/worldbuilder-character/SKILL.md:137-150` (completion checklist)
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: `card-format.md` ends at line 141, and its Working document conventions section begins at line 139; lines 113–137 are Section-scoped writing rules. `SKILL.md` ends at line 149, so its `137-150` range also points beyond EOF. These references fail the explicit line-accuracy criterion and can misdirect implementation edits.

FINDINGS: 0 critical, 6 major, 0 minor, 0 nit

### Adjudication — Round 2 (plan)

1. **Accept.** Fixed: added "No meta-vocabulary from the builder abstraction layer" to both the Body preamble and Story Beats definitions.
2. **Accept.** Fixed: Story Beats scenario prose now explicitly requires "the setup (where and when), the key action or exchange, and what the event reveals about the character."
3. **Accept.** Fixed: Step 5 now updates the ordered addon processing list to include Story Beats after Voice/Dialogue, not just appends a paragraph.
4. **Accept.** Fixed: Step 6 (export SKILL.md) now includes updating the appearance field source to reference the Body preamble.
5. **Partial accept.** extraction-reliability-map already deferred to inbox (separate concern — file doesn't exist or needs broader scope). SillyTavern export skill does not exist in the project yet (inbox item #1 is the mapping study) — no file to update. The card-format.md definition captures the mapping intent for when that skill is built.
6. **Accept.** Fixed: line ranges corrected to match actual file lengths.

