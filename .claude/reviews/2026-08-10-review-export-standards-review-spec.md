---
type: review
title: Review — Export-Standards Review Spec
description: Adversarial review of the export-standards review spec (keywords field
  and extraction reliability map).
tags:
- agent-ready
date: 2026-08-10
timestamp: 2026-08-10T02:57Z
resources: []
---

# Review — Export-Standards Review Spec
## Round 1 — digest `dec998d6…`, anchor `34d74f9d` (dirty), tokens 58687, 2026-08-09T21:33:30-05:00, 193s

Anchor: 34d74f9d1ba7d15156eaaf1d40dcdc2906af276b (dirty tree)
Artifact digest: dec998d66b5f5ac36e588781d8030c25e894c78c0164b026cb1b42768682cf29 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/specs/2026-08-10-export-standards-review-keywords-field-and-extraction-reliability-map.md

1. D1 incorrectly treats location and faction notes as existing lorebook sources
   Location: .claude/specs/2026-08-10-export-standards-review-keywords-field-and-extraction-reliability-map.md:66
   Quote:
   > **Why these three types:** Concept, location, and faction notes
   > are the note types that map to lorebook entries on export.
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The repository’s authoritative ainime export mapping reads concept notes for `loreEntries[]`; it does not export location or faction notes directly. The target-system reference likewise assigns `loreEntries` to `worldbuilder-concept`, even recommending concept notes for major-location lore. Therefore D1 either adds ineffective metadata to two note types or silently introduces a new export-source mapping without specifying entry construction, availability, duplication, or conflict behavior. Narrow D1 to actual lorebook-bound types, or explicitly define and scope the new location/faction export mappings.

2. The structural example names a source that does not exist
   Location: .claude/specs/2026-08-10-export-standards-review-keywords-field-and-extraction-reliability-map.md:91
   Quote:
   > - **Structural:** Value is extracted deterministically from a known
   >   section or frontmatter field. Example: character `name` from the
   >   note's H1 title.
   Type: correctness
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: Character templates have no H1 title, and the current export skill extracts `name` and `lastName` from the filename. The category’s defining example would consequently direct the map toward a nonexistent source and could produce an empty or inconsistent name extraction. Replace it with the actual filename source or explicitly add an H1 requirement, with the latter requiring broader template and export changes.

3. Constructed-field examples contradict the category definition
   Location: .claude/specs/2026-08-10-export-standards-review-keywords-field-and-extraction-reliability-map.md:98
   Quote:
   > - **Constructed:** Value does not exist in any note and must be
   >   generated or configured at export time. Example: `artStyle`
   >   prompts, `calendarConfig.weatherPools`.
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: Both examples have note sources under the referenced export contract: `artStyle` prompts transform the seed’s plain-language art-style reference, while `weatherPools` are derived from seasonal tone and the seed. They therefore also satisfy the stated Derived definition—agent interpretation constrained by note structure. The categories are not mutually exclusive as written. Define precedence based on whether any source material exists, then reclassify these examples consistently.

4. “Every field” includes fields the taxonomy cannot classify
   Location: .claude/specs/2026-08-10-export-standards-review-keywords-field-and-extraction-reliability-map.md:102
   Quote:
   > The map covers every field in the ainime JSON schema
   > (docs/target-system.md) and is maintained alongside the export
   > skill.
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: `docs/target-system.md` also enumerates platform-assigned, generated, and post-export fields that the workflow explicitly does not write, such as `worldId`, generated images, publishing metadata, and UI configuration. These are neither extracted from notes nor necessarily generated or configured “at export time,” so the three categories do not cover the promised universe. Define “export-target field” as fields written by this export workflow, or add a mutually exclusive disposition for platform-managed/out-of-scope fields.

5. The required map granularity and completeness boundary are unspecified
   Location: .claude/specs/2026-08-10-export-standards-review-keywords-field-and-extraction-reliability-map.md:102
   Quote:
   > The map covers every field in the ainime JSON schema
   > (docs/target-system.md) and is maintained alongside the export
   > skill. When a field's extraction method changes (e.g., from derived
   > to structural because a template gained a new section), the map is
   > updated.
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The spec does not say whether compound fields are classified only at their parent path or at every nested leaf. That matters for objects such as `storyTriggers[]`, `loreEntries[]`, `characters[].spriteSets[]`, and `calendarConfig.weatherPools`, whose children can use different extraction methods. It also supplies no required columns, canonical path notation, document path, or mechanical completeness check. Different implementations can therefore claim full coverage while omitting or collapsing materially different fields. Specify row granularity, identity/path rules, and a completeness validation method.

6. D3 prescribes future target behavior despite being declared non-gating
   Location: .claude/specs/2026-08-10-export-standards-review-keywords-field-and-extraction-reliability-map.md:120
   Quote:
   > - **`first_mes` and `mes_example`** (CCv3): Export-time
   >   constructions. No note captures a "first message" because ainime
   >   generates greetings dynamically. A SillyTavern export would need
   >   to construct these from character behavior + scenario context.
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: “Would need to construct these from character behavior + scenario context” selects a mandatory derivation strategy for a future SillyTavern exporter. The following `system_prompt` entry similarly says target-specific transformation is required. Those are normative implementation decisions, conflicting with D3’s stated role as a non-gating gap assessment. Record the missing sources and candidate strategies without deciding what a future exporter must do.

7. The dead-entry consequence is not enabled by the optional field
   Location: .claude/specs/2026-08-10-export-standards-review-keywords-field-and-extraction-reliability-map.md:147
   Quote:
   > - Dead-entry detection (an entry with no keywords and no always-on
   >   flag can never fire) becomes mechanically checkable once keywords
   >   are explicit.
   Type: consistency
   Severity: minor
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: D1 leaves `keywords` optional and requires derivation when it is absent or empty, so keywords are not made explicit for every source note. Conversely, the completed export already contains a concrete keyword array that can be checked regardless of whether it came from frontmatter or derivation. The new field therefore neither makes source-level detection universally mechanical nor enables output-level detection for the first time. Qualify the claim to explicit-keyword notes or leave dead-entry validation with the separately scoped export-procedure work.

FINDINGS: 0 critical, 6 major, 1 minor, 0 nit

### Adjudication

1. **Accept.** Narrow D1 to concept notes only. Location and faction don't map to lorebook entries in the current ainime export; adding keywords for unmapped types is premature. They can gain the field when an export mapping is defined.
2. **Accept.** Fix the structural example — character name comes from filename, not H1 title.
3. **Accept.** Fix the constructed examples — artStyle and weatherPools do have note sources (seed content). Sharpen the category boundary.
4. **Accept.** Define the map's scope as fields the export workflow writes, not every field in the ainime schema. This naturally excludes platform-managed fields.
5. **Accept.** Add that the map classifies at leaf-field granularity for compound fields.
6. **Accept.** Rephrase D3 to record gaps and candidate strategies without prescribing what future exporters must do.
7. **Accept.** Qualify the dead-entry claim — detection is already possible on export output; explicit keywords make it checkable at the note level for concept notes that use the field.

## Round 2 — digest `27a2e42e…`, anchor `34d74f9d` (dirty), tokens 120754, 2026-08-09T21:48:33-05:00, 284s

Anchor: 34d74f9d1ba7d15156eaaf1d40dcdc2906af276b (dirty tree)
Artifact digest: 27a2e42e2d5ecf89ab69f0163867922f40630306661c06aaed4f8b9662de3404 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/plans/2026-08-10-export-standards-review-implementation.md

1. D1’s export override is never implemented
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:21
   Quote:
   > **Architecture:** Two independent deliverables — a schema/template change (propagated through the OKF build pipeline) and a reference document (a new markdown file in `docs/`). No code changes to the export skill itself; the skill already derives keywords from aliases and body terms, and the keywords field overrides that derivation when present.
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: The current export skill only instructs derivation from `aliases` and body terms; it never reads a `keywords` field or gives it precedence. Adding the schema field therefore does not implement D1’s required non-empty override behavior. The commit message later claims behavior that no task establishes.

2. The template step targets frontmatter that does not exist
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:58
   Quote:
   > - [ ] **Step 2: Add keywords to the concept note template**
   >
   > In `defaults/templates/concept.md`, add `keywords: []` to the frontmatter after the existing type-specific fields (`layer`, `trigger-context`).
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: `defaults/templates/concept.md` contains only the Markdown body and has no frontmatter, `layer`, or `trigger-context`. Creation-template frontmatter is generated from the OKF `fields` object. Following this instruction literally would put a stray `keywords: []` line in the Markdown body after generated frontmatter rather than update the property skeleton.

3. The generated-preset verification reads the wrong schema key
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:70
   Quote:
   > ```bash
   > python -c "import json; d=json.load(open('defaults/okf.json')); props=d['types']['concept']['properties']; print('keywords' in props, props.get('keywords'))"
   > ```
   >
   > Expected: `True {'type': 'list', 'required': False}`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Generated type definitions use `d['types']['concept']['fields']`, not `properties`. This command raises `KeyError: 'properties'`, so its stated expected evidence cannot be produced.

4. The template check can pass without finding the template line
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:78
   Quote:
   > ```bash
   > grep -n "keywords" defaults/okf.json
   > ```
   >
   > Expected: at least one match showing `keywords: []` in the embedded concept template content.
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Once Step 1 is rebuilt, this grep necessarily matches the schema key `"keywords"` even if the embedded template contains no `keywords: []` line. “At least one match” therefore provides fabricable evidence for the template requirement.

5. Execution refers to a nonexistent approval gate
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:17
   Quote:
   > > **For agentic workers:** REQUIRED SUB-SKILL: Use core-workflow:subagent-driven-development (recommended) or core-workflow:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Execution requires the plan artifact's approval flip (see Approval Gate).
   Type: completeness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The scoped plan has no “Approval Gate” section or defined approval-flip field. The stated prerequisite is consequently impossible to locate or verify.

6. Deterministic seed-section extraction is repeatedly mislabeled as Derived
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:135
   Quote:
   > | `settingSummary` | Derived | seed.md world concept section |
   > | `genre` | Structural | seed.md genre field or section heading |
   > | `inspirations[]` | Derived | seed.md inspirations section |
   > | `tonalInspirations[]` | Derived | seed.md tonal inspirations section |
   > | `keyTropesAndThemes[]` | Derived | seed.md tropes/themes section |
   > | `communityDescription` | Derived | seed.md, distilled for public display |
   > | `introText` | Derived | seed.md opening concept, player-facing |
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The exporter specifies `settingSummary`, `genre`, `communityDescription`, and `introText` as verbatim extraction from named seed sections. The three arrays are deterministic one-entry-per-line conversions from named sections. Under the plan’s own definitions these are Structural, while several listed source names or transformations (“world concept,” “distilled for public display,” “opening concept”) contradict the exporter.

7. `initialStoryArc` is assigned the wrong source and category
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:147
   Quote:
   > | `initialStoryArc` | Derived | story notes (scope: arc) |
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The exporter copies `initialStoryArc` verbatim from the seed’s Opening Situation section. It does not derive it from story notes. The proposed map would document both the wrong source and the wrong extraction category.

8. Story-trigger sources omit intention story notes
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:153
   Quote:
   > | `storyTriggers[].name` | Structural | event note title |
   > | `storyTriggers[].triggerOnDay` | Derived | event note "What Happens" timing |
   > | `storyTriggers[].promptInjection` | Derived | event note scene effects + timing |
   > | `storyTriggers[].recurring` | Derived | event note recurrence indicators |
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The export workflow writes triggers from both recurring event notes and intention story notes with concrete triggers. Restricting every leaf’s source description to event notes leaves a reachable export path undocumented.

9. Calendar classifications invent note sections and misclassify export defaults
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:158
   Quote:
   > | `calendarConfig.seasons[]` | Structural | seed.md or direction.md calendar section |
   > | `calendarConfig.daysPerSeason` | Structural | seed.md or direction.md calendar section |
   > | `calendarConfig.daysOfWeek[]` | Derived | seed.md calendar section |
   > | `calendarConfig.daySegments[]` | Structural | calendar.md default (Morning/Afternoon/Evening/Night) |
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Neither the seed nor direction contract defines the asserted calendar section. The exporter supplies calendar defaults and changes them when the world requires another structure. A value sourced from an export-time default does not meet the plan’s Structural definition of extraction from a note, while `daysOfWeek` is inconsistently labeled Derived despite belonging to the same configuration mechanism.

10. The keyword row explicitly violates mutual exclusivity
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:170
   Quote:
   > | `loreEntries[].keywords[]` | Structural / Derived | concept note `keywords` field (structural) or derived from aliases + body terms (derived fallback) |
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The plan requires every field to appear exactly once with mutually exclusive Structural, Derived, or Constructed categories. This row assigns two categories. If extraction paths need separate treatment, the map needs a defined representation that retains exclusivity rather than a slash category.

11. `enabled` is mapped to a status rule the exporter does not have
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:176
   Quote:
   > | `loreEntries[].enabled` | Structural | concept note status (complete = enabled) |
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The exporter defaults every lore entry to `true` and permits `false` only when an entry should never activate. It does not derive the value from a concept-note status. The proposed source and Structural classification are fabricated.

12. Lore availability uses the wrong day and ignores exporter judgment
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:177
   Quote:
   > | `loreEntries[].availableFromDay` | Structural | concept note `layer` field (surface=0, mid/deep=calculated) |
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The current exporter specifies surface as day 1, not day 0, and defaults mid/deep to days 14/56 while allowing adjustment for world pacing. That adjustment requires interpretation, so the row is also incorrectly labeled as wholly Structural.

13. Character type ignores its deterministic cast-plan source
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:185
   Quote:
   > | `characters[].type` | Derived | character function in narrative |
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The exporter maps the explicit Major/Supporting designation in `project/plan.md` to `"main"` or `"side"`. It does not infer type from narrative function, making this a deterministic Structural mapping under the plan’s taxonomy.

14. The `baseProfile` source omits required inputs and output sections
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:187
   Quote:
   > | `characters[].baseProfile` | Derived | Background + Body sections per card-assembly.md |
   Type: completeness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: `card-assembly.md` also requires behavioral/Soul material, Relationships, Relationship Behavior-derived influence bands, and Future Storylines. Describing the source as only Background plus Body makes the reliability map materially incomplete for the exporter’s most complex field.

15. Appearance is assigned to a section that does not contain the required appearance record
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:188
   Quote:
   > | `characters[].appearance` | Derived | character note Body section (physical description) |
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: The character template defines Body as physical behavioral descriptions, whereas the exporter calls for an Appearance section containing species/type, age presentation, body type, features, and clothing. The current template lacks that section. The plan conceals this extraction gap by equating Body with an appearance description.

16. `spriteSets` is neither leaf-granular nor source-free
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:190
   Quote:
   > | `characters[].spriteSets[]` | Constructed | sprite file references assigned during export |
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: A sprite-set object has distinct `name`, `description`, and `expressions` leaves. Descriptions and prompts are derived from the character’s Appearance material, while names/states involve export decisions; they are not merely file references with no note source. Collapsing them into one Constructed row violates both category accuracy and required leaf granularity.

17. The map includes a field the workflow explicitly does not write
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:191
   Quote:
   > | `characters[].color` | Constructed | UI color assigned during export |
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: `docs/target-system.md` lists `characters[].color` under “Fields We Do Not Write” and says it is set in the platform. Including it contradicts the plan’s own writable-subset boundary.

18. Multiple compound objects are collapsed instead of mapped at leaf granularity
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:167,190,197,203
   Quote:
   > | `calendarConfig.weatherPools` | Derived | seed.md seasonal tone + calendar.md structure |
   >
   > | `characters[].spriteSets[]` | Constructed | sprite file references assigned during export |
   >
   > | `locations` | Constructed | location image references, not from notes |
   >
   > | `artStyle.background.*` | Derived | seed.md art style section |
   > | `artStyle.sprite.*` | Derived | seed.md art style section |
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: These rows use parent objects or wildcards despite the explicit leaf-granularity constraint. They fail to distinguish weather-pool value arrays, location `name`/`prompt` leaves, sprite-set children, and the seven named art-style paths, including `artStyle.background.time_contexts`. Different children have different sources or scope dispositions.

19. Multi-target rows fail to assign one of the required categories
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:213
   Quote:
   > | `system_prompt` | Candidate: direction.md | requires transformation |
   > | `post_history_instructions` | Candidate: direction.md | requires transformation |
   > | `character_book.entries[].keys` | Maps to loreEntries[].keywords | same source |
   > | `character_book.entries[].content` | Maps to loreEntries[].content | same source |
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: D2 requires the multi-target extension to say whether additional fields are Structural, Derived, or Constructed. “Candidate” and “Maps to” are not categories, and the same defect recurs for ST `key`, `content`, and `group`. The section can remain non-gating while still providing the required classification.

20. The completeness verifier cannot verify completeness, uniqueness, granularity, or category validity
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:239
   Quote:
   > fields = re.findall(r'`(\w+(?:\.\w+)*(?:\[\])?)`', ts)
   > mapped = [f for f in fields if f in em]
   > unmapped = [f for f in fields if f not in em and f not in ('worldId', 'id', 'url', 'name')]
   > print(f'Total fields: {len(fields)}, Mapped: {len(mapped)}, Unmapped: {len(unmapped)}')
   > if unmapped:
   >     print('Unmapped:', unmapped[:10])
   >
   > Expected: majority of export-written fields appear in the map. Platform-managed fields (worldId, generated images) correctly excluded.
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The script performs substring presence checks over every backticked token, silently exempts the export-written `name` leaf, truncates diagnostics, and always exits successfully. It does not check “exactly once,” valid category membership, leaf paths, or the writable-field boundary. Applied to the proposed map, it still reports 25 unmapped references, yet the vague “majority” expectation permits completion. This is not non-fabricable evidence for acceptance criterion 2.

FINDINGS: 0 critical, 20 major, 0 minor, 0 nit

### Adjudication

1. **Accept.** Add SKILL.md update step to instruct the export agent to check the keywords field first.
2. **Accept.** Remove template body edit — OKF generates frontmatter from field definitions.
3. **Accept.** Fix verification command: `fields` not `properties`.
4. **Accept.** Remove grep check (template body edit removed per F2).
5. **Reject.** Standard plan header boilerplate — the approval gate is the workflow status flip, not a plan section.
6-18. **Accept (batch).** Restructure Task 2: the plan defines the map format, categories, methodology, and verification — but does not embed classifications. The executor reads the actual export skill, card-assembly.md, calendar.md, and target-system.md to classify each field. This avoids the 13 classification errors found by the reviewer, which all stem from classifying without reading the source files line-by-line. The plan provides the structure and rules; the executor provides the content.
19. **Accept.** Multi-target rows must use the three-category classification.
20. **Accept.** Replace the substring-presence verifier with a proper field-count check.

## Round 3 — digest `43b368f2…`, anchor `34d74f9d` (dirty), tokens 51753, 2026-08-09T21:56:19-05:00, 177s

Anchor: 34d74f9d1ba7d15156eaaf1d40dcdc2906af276b (dirty tree)
Artifact digest: 43b368f2d1d6210b3abb2b874c5600523e101d3b6eb77ae9eba4511cf233c5d0 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/plans/2026-08-10-export-standards-review-implementation.md

1. Architecture omits the planned SKILL.md change
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:21
   Quote: `**Architecture:** Two independent deliverables — a schema/template change (propagated through the OKF build pipeline) and a reference document (a new markdown file in \`docs/\`). No code changes to the export skill itself; the skill already derives keywords from aliases and body terms, and the keywords field overrides that derivation when present.`
   Type: completeness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The architecture lists only the schema/template change and reference document, although Task 1 also modifies `skills/worldbuilder-ainime-export/SKILL.md` to introduce the precedence rule. Saying the skill “already” applies the override also misstates the pre-change state. This directly violates the requirement that the architecture header include the SKILL.md update.

2. Tasks described as independent have an ordering dependency
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:21,108
   Quote: `**Architecture:** Two independent deliverables — a schema/template change (propagated through the OKF build pipeline) and a reference document (a new markdown file in \`docs/\`).`
   
   `- Consumes: \`docs/target-system.md\` (ainime field schema), \`skills/worldbuilder-ainime-export/SKILL.md\` (current derivation logic), \`skills/worldbuilder-ainime-export/card-assembly.md\` (character baseProfile rules), \`skills/worldbuilder-ainime-export/calendar.md\` (calendar/storyTrigger rules).`
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Task 2 classifies fields from the same SKILL.md that Task 1 changes. In particular, the keyword classification depends on reading the new explicit-keyword precedence rule. Parallel “independent” execution can therefore classify the old behavior. The plan must specify that Task 2 reads the post-Task-1 version or otherwise define a stable input snapshot.

3. Commit instructions call the output field `keys[]` instead of `keywords[]`
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:92
   Quote: `Spec D1: explicit lorebook trigger keywords for concept notes.
When present, export uses these as loreEntry keys[] instead of
deriving from note content. Defaults to empty (preserves current
agent-derived behavior). SKILL.md updated with precedence rule.`
   Type: consistency
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Task 1 consistently defines the target as `keywords[]`, but its required commit message claims the export uses `keys[]`. That is a different field and makes the recorded behavior contradict the implementation instructions.

4. Task 1 never verifies the precedence-rule update
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:78
   Quote: `- [ ] **Step 4: Verify the generated preset includes the keywords field**`
   Type: completeness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The only functional verification checks `defaults/okf.json`. The later `git log -1 --stat` proves merely that SKILL.md changed, not that it contains the required non-empty/absent/empty precedence behavior. Task 1 can pass while the SKILL.md edit is missing or incorrect, violating the evidence requirement.

5. The plan excludes IDs that its referenced workflow constructs
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:32
   Quote: `- Map scope: fields the export workflow writes. Platform-managed fields (IDs, generated images, publishing metadata) are out of scope.`
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: The plan’s own source corpus defines exporter-created IDs: SKILL.md gives a generated `loreEntries[].id`, and calendar.md constructs `storyTriggers[].id`. Treating all IDs as platform-managed omits export-written leaf fields while the stated output promises every export-written field. The scope must distinguish exporter-constructed IDs from genuinely platform-assigned IDs.

6. The platform-managed exclusion set changes between sections
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:32,115
   Quote: `- Map scope: fields the export workflow writes. Platform-managed fields (IDs, generated images, publishing metadata) are out of scope.`
   
   `1. \`docs/target-system.md\` — the complete field schema. Identify every field the export workflow writes (skip platform-managed fields: IDs, generated images, UI theme, music, custom prompts).`
   Type: consistency
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The global rule excludes publishing metadata but not UI theme, music, or custom prompts; Task 2 excludes the latter three but omits publishing metadata. The template repeats Task 2’s version. Because none of these lists is marked illustrative, workers cannot determine the authoritative inventory unambiguously.

7. Multi-target classification has no field inventory or source
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:218
   Quote: `For multi-target sections, classify each additional CCv3/ST field the same way. Use "Candidate source" column since these targets have no implemented exporter.`
   Type: completeness
   Severity: major
   Effort-to-fix: large (reaches beyond the scoped change)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Step 1 names only the ainime schema and exporter documents. It names no CCv3 or ST WorldInfo schema and supplies no enumerated fields, version, or completeness boundary. Consequently, “each additional” has no determinate meaning and two implementers can produce materially different tables while both following the plan.

8. Leaf-field and duplicate-placement rules are under-specified
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:142
   Quote: `- Every field the export workflow writes appears exactly once.
- Compound fields (storyTriggers[], loreEntries[], characters[],
  calendarConfig.weatherPools, artStyle.*, spriteSets[]) are
  classified at leaf-field granularity — each child gets its own row.`
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The plan does not enumerate the required leaf paths or define how dynamic maps such as seasons, day segments, expressions, and time contexts collapse into rows. It also provides separate Adventure and Calendar tables even though `storyTriggers[]` belongs to both source sections, without saying where the single permitted occurrence goes. “Exactly once” is therefore not reproducible.

9. Required output is represented by unresolved placeholders
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:153
   Quote: `## Setting fields

| Field | Category | Source |
|-------|----------|--------|
| ... | ... | ... |`
   Type: completeness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: Every ainime and multi-target table contains `...` placeholders rather than a concrete field inventory or expected rows. Telling the implementer to populate them later does not satisfy the explicit acceptance criterion that the plan contain no placeholders and that every step define concrete instructions and expected output.

10. Completeness verification does not perform the claimed comparison
   Location: .claude/plans/2026-08-10-export-standards-review-implementation.md:220
   Quote: `- [ ] **Step 3: Verify completeness**

Count the fields in the map and compare against target-system.md:`
   
   `table_rows = [l for l in lines if l.startswith('| \`')]`
   
   `multi = [l.strip() for l in table_rows if '/' in l.split('|')[2]]`
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The script never opens `docs/target-system.md`, so no comparison occurs. It counts ainime and multi-target rows together, allowing unrelated rows to satisfy the `30+` threshold; it does not detect missing or duplicate fields; and its category check rejects only slash-delimited values, accepting blanks, misspellings, comma-separated categories, and arbitrary text. It also does not verify Source-column evidence. The reported output can therefore claim completeness and exclusivity for an incomplete or invalid map.

FINDINGS: 0 critical, 10 major, 0 minor, 0 nit

### Adjudication

1. **Accept.** Fix architecture header to mention SKILL.md update.
2. **Accept.** Add ordering note: Task 1 completes before Task 2.
3. **Accept.** Fix commit message: `keywords[]` not `keys[]`.
4. **Accept.** Add SKILL.md verification step (grep for precedence text).
5. **Accept.** Clarify ID scope: exporter-constructed IDs (loreEntries[].id, storyTriggers[].id) are in scope; platform-assigned IDs are not.
6. **Accept.** Unify platform-managed exclusion list between global constraint and Step 1.
7. **Accept.** Add CCv3 and ST worldinfo format spec references for multi-target classification.
8. **Accept in part.** Add storyTriggers placement rule (Adventure section, single occurrence). Full leaf enumeration belongs to the executor's classification work.
9. **Reject.** The `...` rows are a document template showing table structure, not TBD/TODO placeholders. The methodology is concrete: read 4 named source files, classify by 3 defined rules, populate tables. The expected output is specified (30+ rows, single categories, verification script). Classification accuracy requires reading the source files line by line — embedding pre-baked classifications produced 13 errors in round 2. The executor's job is to build the content; the plan's job is to specify the format, rules, and verification.
10. **Accept.** Improve verification script to compare against target-system.md.

