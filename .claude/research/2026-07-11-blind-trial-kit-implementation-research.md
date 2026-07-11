---
type: research
title: Blind-trial kit implementation research
description: 'Implementation research for the writing-doctrine blind-trial kit plan:
  current instruction-set inventory, stop-slop rule inventory, additive-principle
  source passages, repo conventions.'
tags:
- human-ready
date: 2026-07-11
timestamp: 2026-07-11T16:42Z
resources:
- '[[2026-07-11-writing-doctrine-blind-trial-kit]]'
- '[[2026-07-11-causal-character-writing-for-llm-roleplay-friction-engines-and-trait-word-poisoning]]'
- https://github.com/hardikpandya/stop-slop/
---

# Blind-trial kit implementation research

## Goals

Context dossier for the implementation plan of the [writing-doctrine blind-trial kit spec](../specs/2026-07-11-writing-doctrine-blind-trial-kit.md). Five questions: (1) which blocks of the shipped character instruction set go into a self-contained packet and which are excluded, (2) the complete stop-slop rule inventory, (3) the source passages for the +additive and +tensions doctrine blocks, (4) repo conventions bearing on a new `trials/` folder, (5) the vault-mechanics invocation for follow-up artifacts.

## 1. Current instruction set inventory

All headings quoted exactly as they appear in the source files. "Include" means the packet needs the content (rewritten as a self-contained instruction, with all cross-file references and vault mechanics stripped); "exclude" means the trial agent must never see it because it concerns vault plumbing, the Q&A flow (already done and frozen in the brief), or downstream work.

### skills/worldbuilder-character/SKILL.md

Headings (H2 unless noted):

- `# Character Blueprint` (H1)
- `## Overview`
- `## Character Note Structure`
- `## Design Notes` — with H3s `### Session Notes` and `### Builder Context`
- `## Session Flow`
- `## Writing Rules`
- `## Background, Body & Soul`
- `## Relationships`
- `## Story Notes`
- `## Intimate Dynamics`
- `## Post-Group Sync Pass`
- `## Self-Check Before Marking Complete`

Include in packets:

- `## Overview` — the "behavioral specification, not description" framing (first paragraph only; the Description-field paragraph is export/cast-navigation mechanics).
- `## Character Note Structure` — the section list (Background, Body, Soul, Relationships, Intimate Dynamics if flagged), minus the table's Design Notes row, the sub-file column, and the entire frontmatter/`new_doc.py`/rename paragraph.
- `## Writing Rules` — all five bolded rules: "Make decisions, don't hedge" (packet variant must drop "ask the user" — the no-questions rule replaces it), "Write plainly. No flair.", "Write what characters ARE, not what they aren't", "The note describes the character's starting state" (drop "create a story note or cut it" → just "cut it"), "Section discipline", plus "Asymmetry in relationships is normal".
- `## Self-Check Before Marking Complete` — only the **Background**, **Body**, **Soul**, **Relationships**, and **Intimate Dynamics (if flagged)** checklist blocks. The Soul block's Because-clause item references Session Notes ("ask the user before writing") — packet variant must rephrase to "trace to the brief; where the brief is silent, decide per these rules and move on".

Exclude from packets:

- `## Design Notes` entirely (builder record; spec says no Design Notes section in trial output).
- `## Session Flow` entirely (Q&A already run and frozen as `brief.md`).
- `## Story Notes` entirely (trial writes only the note body).
- `## Post-Group Sync Pass` (batch mechanics).
- Self-check blocks: **Frontmatter**, **Design Notes**, **Story Notes**, **Pre-Handoff Scan**, **Description** (all vault/flow mechanics).
- All sub-file pointers (`framework.md`, `relationships.md`, `intimate.md`, `writing-style.md`, `worldbuilder-story`) — packets are self-contained, content is inlined instead.

### skills/worldbuilder-character/framework.md

Headings:

- `# Character Framework — Background, Body & Soul` (H1)
- `## Background`
- `## Body`
- `## Soul` — with H3s `### The Formula`, `### Why behavioral descriptions outperform trait labels`, `### Coverage`, `### Contradictions`, `### The Because clause`

Include: essentially the whole file. `## Background` (fact-pair format, example/anti-example, coverage list), `## Body` (format, coverage prompts, thin-is-acceptable, example), `## Soul` with all five H3s — the When/Behavior/Because formula ("When [trigger], they [behavior], because [underlying reason]"), the staging test with fail/pass pair, the Because-clause exemption ("may name an internal state if the state is specific"), the 4-row label-vs-behavioral table (Confident/Stubborn/Kind/Nervous), coverage minimums (3–5 psychological entries; irrational behavior with emotional root required; self-image gap; contradiction as separate required entry; 2–3 social entries; speech pattern if distinctive), the irrational-behavior callout, `### Contradictions`.

Exclude/adapt: `### The Because clause` references "the Q&A session capture in Design Notes" and "ask before writing" — the packet variant redirects to the frozen brief and the no-questions rule. That is the only vault-flow dependency in the file.

### skills/worldbuilder-character/relationships.md

Headings:

- `# Relationships` (H1)
- `## Overview`
- `## The 12 Relationship Archetypes`
- `## Coverage Requirements`
- `## Archetype Distribution`
- `## Writing Relationship Entries` — with H3s `### The Fiske relational model lens` and (under a separator) `### Per-entry self-review: internal state check`
- `## Generativity Hierarchy`
- `## Coverage Validation`

Include: `## Overview` (behavioral dynamic not history; incompatible-wants; asymmetry — but the "cross-character capture"/Blueprint-note paragraph is vault mechanics, keep only the perspective-focus half), `## The 12 Relationship Archetypes` (Kin, Authority, Rival, Friction, Obligation, Confidant, Desire, Unease, Ideological Counterpart, Community Thread, Ghost, Charge — each with behavioral signature), `## Coverage Requirements` (major: 8 named, anchors = Kin-or-Ghost + Authority + rivalry-or-friction + Confidant + one further friction source; supporting: 5 named, three anchors), `## Archetype Distribution` (variety goal, once-or-twice repetition limit, Community-Thread-last-resort, 4–5 distinct archetypes), `## Writing Relationship Entries` (2–4 sentences, bullet with bold `**Name — Archetype(s):**` prefix, Mira example; Fiske lens optional but harmless to include), `## Generativity Hierarchy` (love loop, ally collapse callouts), `### Per-entry self-review: internal state check` (minus its two "log as Blueprint note in `project/plan.md`" sentences — displaced content is simply cut in the trial), and `## Coverage Validation` items 1–3 (item 3, cast web check, works because arms have vault read access to the existing cast).

Exclude: the H1 preamble's "open them before continuing" instruction stays (vault read access exists), but every mention of `project/plan.md` Blueprint notes and cast-plan capture goes — trial agents write one file and nothing else.

### skills/worldbuilder-character/intimate.md

Headings:

- `# Intimate Dynamics (Optional Section)` (H1)
- `## Overview`
- `## Format`
- `## Coverage`

Include: all three sections when the trial character is flagged — behavioral-over-labels rationale, bullet/prose format same as Soul, coverage (attraction expression, hesitation and limits, specific dynamic if present), the required friction point, both example entries. Exclude: the Overview's second paragraph ("Exploration questions ... belong in the Q&A session and Design Notes") and third paragraph (project-planning flag mechanics) — the packet just states the conditional: include this section only if the brief flags the character.

### skills/writing-style.md

Headings:

- `# Writing Style` (H1)
- `## Style Model`
- `## Word Choice` — H3s: `### Use the simplest precise word`, `### Use "is" and "has": avoid copula avoidance`, `### No significance inflation`
- `## Sentence Structure` — H3s: `### Write positive statements`, `### Prefer verbs over nominalizations`, `### Keep sentences short enough to parse on first read`, `### No em-dashes`, `### Numbers as numerals`
- `## Content Standards` — H3s: `### Describe behavior, not labels`, `### Make claims verifiable or behavioral`, `### No flair`, `### No -ing padding`, `### Single source of truth`, `### Don't describe one entity in another entity's document`
- `## Structure`
- `## Four Failure Modes`

Include (this is the "current" style block, arms 1–3): everything except the H1 preamble's export-phase pointer and the closing pointer to `docs/slop-phrases.md` (a review reference the packet must not name — it is also the rubric's slop-density checklist, so leaking it into packets would coach half the arms). Word-choice table (12 rows), copula rule, significance inflation, positive statements, nominalizations, short sentences, no em-dashes, numerals, behavior-not-labels, verifiable claims, no flair, no -ing padding, single source of truth, entity-boundary rule, structure guidance, and the Four Failure Modes checklist (Latinate vocabulary, negative constructions, labels without behaviors, literary flair).

Format note for the stop-slop swap: the current block's native format is rule + wrong/right example pairs; the spec requires the stop-slop block rewritten into the same shape so form does not leak the arm.

## 2. stop-slop rule inventory

Repo: https://github.com/hardikpandya/stop-slop/ — default branch `main`. Structure: `README.md`, `SKILL.md`, `CHANGELOG.md`, `LICENSE`, and `references/` containing `phrases.md` (2.9 KB), `structures.md` (5.3 KB), `examples.md` (1.7 KB, five before/after pairs). **License: MIT** (stated in README and SKILL.md) — free to derive and rewrite, attribution preserved by the LICENSE terms; note the source in kit-construction records, not in the packets themselves.

SKILL.md core rules (eight):

1. **Cut filler phrases** — throat-clearing openers, emphasis crutches, all adverbs.
2. **Break formulaic structures** — no binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency.
3. **Use active voice** — every sentence needs a human subject doing something; no passive constructions.
4. **Be specific** — no vague declarations, no lazy extremes ("every," "always," "never").
5. **Put the reader in the room** — direct address over distant narration; concrete details over abstractions.
6. **Vary rhythm** — mix sentence lengths; two items beat three; vary paragraph endings; no em dashes.
7. **Trust readers** — facts plainly, no softening or over-justification.
8. **Cut quotables** — rewrite anything that reads like a pull-quote.

SKILL.md also carries a pre-submission Quick Checks list and a 5-dimension 1–10 scoring matrix (Directness, Rhythm, Trust, Authenticity, Density; below 35/50 = revise). The scoring matrix is stop-slop's own evaluation tool, distinct from and not to be confused with this trial's rubric.

`references/phrases.md` — phrase-level bans, seven groups:

1. Throat-clearing openers ("Here's the thing:", "The uncomfortable truth is", "It turns out", "Let me be clear", any "here's what/this/that" construction — 15 listed).
2. Emphasis crutches ("Full stop.", "Let that sink in.", "This matters because", "Make no mistake").
3. Business jargon table, 11 rows (navigate→handle, unpack→explain, lean into→accept, landscape→situation, game-changer, double down, deep dive, take a step back, moving forward, circle back, on the same page).
4. Adverbs — "Kill all adverbs. No -ly words." 15 named offenders (really, just, literally, genuinely, honestly, simply, actually, deeply, truly, fundamentally, inherently, inevitably, interestingly, importantly, crucially) plus filler phrases ("At its core", "In today's [X]", "It's worth noting", "At the end of the day", "When it comes to", "In a world where", "The reality is").
5. Meta-commentary ("Hint:", "Plot twist:", "You already know this, but", "Let me walk you through...", "As we'll see...").
6. Performative emphasis ("creeps in", "I promise") and telling-instead-of-showing ("This is genuinely hard", "actually matters").
7. Vague declaratives ("The reasons are structural", "The stakes are high", "The implications are significant").

`references/structures.md` — structural bans, eleven groups:

1. Binary contrasts (11 patterns: "Not because X. Because Y.", "The answer isn't X. It's Y.", "not just X but also Y", etc.) — state Y directly.
2. Negative listing ("Not a X... Not a Y... A Z.") — state Z.
3. Dramatic fragmentation ("[Noun]. That's it. That's the [thing].").
4. Rhetorical setups ("What if...?", "Here's what I mean:", "Think about it:", "And that's okay.").
5. Formulaic constructions ("By the time X, I was Y.", "X that isn't Y").
6. False agency (7 patterns: "the decision emerges", "the data tells us", "the culture shifts") — name the human actor.
7. Narrator-from-a-distance ("Nobody designed this.", "People tend to...") — put the reader in the room.
8. Passive voice (4 patterns: "X was created", "Mistakes were made") — name the actor, front the sentence with them.
9. Sentence starters to avoid — no Wh- openers (What/When/Where/Which/Who/Why/How), no paragraph-initial "So", no "Look,".
10. Rhythm patterns — no three-item lists (use two or one), don't answer questions immediately, vary paragraph endings, no em-dashes at all, no staccato stacking, no "Not always. Not perfectly." hedge-reassurance.
11. Word patterns — lazy extremes banned (every/always/never/everyone/nobody), all adverbs banned.

Conflicts and overlaps to handle in the packet derivation:

- **Direct conflict with the character-note form:** stop-slop bans sentences starting with Wh- words, but the When/Behavior/Because formula produces "When [trigger], they..." sentences by design, and framework.md's own examples open with "When". The stop-slop packet block must carve out the formula (scope the Wh- rule to non-formula sentences) or the doctrine axis gets contaminated by the style axis. Same issue with "never"/"always" bans vs. behavioral descriptions that legitimately say "she does not lose."
- **Direct conflict #2:** stop-slop rule 5 ("put the reader in the room", direct address, "use 'you'") targets essay prose; character notes are third-person specs. Must be dropped or re-scoped in derivation.
- **Overlap (no conflict):** no-em-dash, active voice, specificity, and plain language all match writing-style.md — these shared rules will make arms 1–3 vs 4–6 differ less than the raw rule counts suggest.
- **Gotcha in the source itself:** `references/examples.md` Example 4's "after" text uses an em-dash ("Speed, quality, cost—pick two.") in a rule set that bans em-dashes entirely. Do not import the examples verbatim; write fresh wrong/right pairs in the current-block format anyway (the spec requires that rewrite for blinding).

## 3. Additive-principles source text

Source: [causal-character-writing reference](2026-07-11-causal-character-writing-for-llm-roleplay-friction-engines-and-trait-word-poisoning.md), sections "New principles not in current doctrine" and "Tensions with current doctrine".

### +Additive block (arms 2, 3, 5, 6) — five principles

**Trait-word poisoning** (principle 1): "A single heavy adjective — 'intelligent,' 'analytical,' 'arrogant,' 'dominant' — can outweigh a whole card of behavioral description and drag output into the trope statistically welded to that word (jargon-spewing robot, UN spokesman, emotionless android). The fix is never a softer adjective: specify the *domain* of competence ('remembers the C99 spec verbatim'), the *drive* behind it, and a cost or flaw it produces. Strongest formulation: the thread's consensus that you cannot use these words *anywhere* in the card — the description can't outvote them."

**Knowledge boundaries** (principle 2): "State what a character knows *and where they have no insight*. Unbounded competence plus an LLM's own knowledge produces omniscient characters (the book nerd who knows thread counts). Per-topic depth beats a global trait."

**Unresolved states** (principle 3): "A resolved fact ('became a DSA member') is a shortcut the model can cheat through; an unresolved tension ('can't commit because…') forces the model to *find* the character's position each time, which is what produces liveliness. Deliberately leave the character's direction open — multiple supported futures, none chosen. Related to but distinct from the existing starting-state rule: that rule bans future events; this one says the *present* should contain live, competing pulls." (This principle is what the rubric's Liveliness criterion reads for.)

**Specification boundary** (principle 4): "For every detail: does it matter for behavior, or can the model fill it in? Specifying locks it and costs tokens; leaving it open lets the model average — which is fine when the average is fine. The current 'make decisions, don't hedge' rule governs what you write; this governs what you deliberately don't."

**Life in motion** (principle 8): "Rent going up, arguments with parents, missed opportunities, the option of rejecting the player entirely. Independent ongoing pressure is what gives the model 'action' beyond reacting to the user."

Not in the additive block (for the record): implicit encoding (7), names carry weight (9), battle-testing (10), and card-to-greeting ramp (11) were not selected by the spec's additive list; token discipline and Egri mapping are confirmations, not changes.

### +Tensions block (arms 3, 6) — two resolutions, both switched ON

**Emotional-memory-hook exemption** (principle 6 + tension 1): the hook is "a compressed, specific, unresolved sensory fragment ('the last thing she remembers of her mother: lowering her yukata's collar, one word — run') [that] carries more weight than a paragraph of explanation, because dramatic-moment patterns are dense in training data." The tension as recorded: "writing-style.md prescribes screenplay action lines — observable, plain, no flair. The emotional-memory-hook technique argues a few dense cinematic fragments are the highest-leverage tokens in a card. These are reconcilable (hooks are still observable and concrete — a collar, one word — not Latinate abstraction), but the style doctrine as written would likely flag them." The arms-3/6 block states the exemption: a small number of compressed sensory fragments may break plainness when concrete and unresolved.

**Anchor repetition** (principle 5 + tension 2): "Densely interconnecting a character's anchors (the mentor linked to the sword, the pottery, the clothing, the loneliness) gives the model multiple activation routes to the same material — 'more connections make her more reachable,' stability under pressure. The sources deliberately repeat key anchors at several points in the card." The tension: "framework.md treats cross-section redundancy as misplacement; the hairball model treats deliberate anchor repetition as grounding. Possible resolution: no *content* duplication, but anchors may be *referenced* from multiple entries." The arms-3/6 block allows anchor repetition across sections (per the spec: "anchor repetition across sections is allowed"), overriding the section-discipline redundancy clause for anchors specifically.

Note the block-stacking implication: the tensions block *modifies* rules present in the shared doctrine (plain-style rule; section discipline). The packet build must apply the tension text as an explicit stated exemption after the base rule, identical wording in arms 3 and 6, so the only diff between arm pairs is the presence of these two exemption paragraphs.

### Third tension, deliberately not in any packet

"Positive-statement rule vs. prompt-level bans" — the reference already resolves it in favor of existing doctrine ("keep the doctrine, note the disagreement"), so it is not a trial variable. But note: the stop-slop packets themselves are full of negative instructions (bans); that is instruction-to-the-writer, not note content, and does not violate the write-what-characters-ARE rule.

## 4. Repo conventions

- **Root layout:** `CLAUDE.md`, `CONTEXT.md`, `README.md`, `defaults/`, `docs/`, `scripts/`, `skills/`, `tests/`, `.claude/`, `.claude-plugin/`, `.superpowers/`. **No `trials/` folder exists** — `trials/2026-07-writing-doctrine/` is a fresh top-level directory with no naming precedent to follow or collide with.
- **.gitignore** is two lines: `__pycache__/` and `*.pyc`. Nothing would ignore trial markdown; the whole kit will be tracked.
- **Model-neutrality rule, exact CLAUDE.md wording:** "**Shipped content is model-neutral:** never name a specific AI model in templates, stub notes, or skill instructions that reach end users — 'for future agents', never a product name. Some users run these skills with other models." The kit leaves the repo, so packets, README, brief-procedure, and rubric all count as shipped content. Watch the derivation sources: framework.md says "LLMs default to writing rational, helpful-assistant-style characters" — "LLM" is fine (not a product name), but the stop-slop repo's own docs mention a specific vendor's products in their implementation notes; none of that may survive into the packets.
- **Writing doctrine applies to the kit's own prose:** CLAUDE.md — "Skill prose follows the plugin's own writing doctrine: plain, concrete, no filler — `skills/writing-style.md`; phrase-level review checklist in `docs/slop-phrases.md`." The README/brief-procedure/rubric should pass the plugin's own style bar.
- **docs/slop-phrases.md structure** (rubric's slop-density source): six groups, ~35 phrases/patterns total — Interpretive narration (4 pattern families), Soul section hedging (10), Vague interiority (5), Significance inflation (10), Copula avoidance (6), AI vocabulary (2 families: "gap", "register"). Each group has a Fix line. Header states: "Review reference for character note output. Not a skill instruction — agents do not load this file." — which is exactly the trial posture: evaluator-side only, never packet-side.
- **Tests/tooling:** `tests/test_generate_templates.py` is stdlib `unittest`, run directly via `python tests/test_generate_templates.py` — no pytest, no runner config. `scripts/` holds `build-okf.py` and `generate_templates.py`: python3 shebang, stdlib-only (`io`, `json`, `os`, `sys`), `ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` pattern, `newline='\n'` on writes. Local python is 3.14.3. No test convention applies to pure-markdown deliverables. If the plan wants a one-shot shuffle/seal script for key generation (random packet→arm assignment + base64), matching this style in `scripts/` is the precedent — though a one-time build can also just do the shuffle at kit-construction time without shipping a script. Note the spec's rerun caveat implies rebuilds happen; a small script makes reshuffles reproducible.
- **Generated-file rule:** only `defaults/okf.json` is generated-do-not-hand-edit. Nothing similar constrains `trials/`.
- **CONTEXT.md vocabulary** applies (Wide phase, character note, cast plan, etc.) — trial docs should use it.

## 5. Vault mechanics for follow-up artifacts

Confirmed working invocation (used to create this document):

```
python "C:\Users\cpnbe\.claude\plugins\marketplaces\local-desktop-app-uploads\okf-enforcement\scripts\new_doc.py" --type research --title "Blind-trial kit implementation research" --description "..." --dir .claude/research
```

It prints the created path (`.claude/research/2026-07-11-blind-trial-kit-implementation-research.md`), stamps full frontmatter (type, title, description, tags with `human-ready` default status, date, timestamp, empty resources), and generates a date-prefixed slug filename. Same pattern with `--type plan --dir .claude/plans` for the implementation plan and `--type spec --dir .claude/specs [--status human-ready]` for specs. The results-return artifact named by the spec ("Results return as a reflection document in this vault") would use `--type reflection` — the parent marketplace rules list `reflection` as a type; this repo's `.claude/rules/okf-claude.md` type list shows adr/grilling/plan/reference/reflection/research/spec, so reflection is available here too. Documents in `trials/` itself are NOT vault documents — `trials/` is outside `.claude/`, carries no OKF frontmatter obligation, and new_doc.py is not used for kit files.

## Consolidation

The kit build is mostly assembly, with four points of real work:

1. **Packet skeleton.** One shared skeleton covering: role framing (Overview), note structure (Background/Body/Soul/Relationships/±Intimate Dynamics), section rules (framework.md + relationships.md + intimate.md content inlined, vault plumbing stripped, brief-instead-of-Q&A rewires), writing rules (SKILL.md block), a style block (the swap axis), doctrine blocks (the add axis), a no-questions rule, an output rule (single file `out/note-<n>.md`, no rule-naming in output), and a trimmed self-check. The exclusion list is well defined: Design Notes, Session Flow, Story Notes, Post-Group Sync, description field, frontmatter/`new_doc.py`, `project/plan.md` Blueprint-note capture, and the slop-phrases pointer.
2. **stop-slop derivation.** MIT-licensed, safe to derive. Eight core rules expand through two reference files into ~18 phrase/structure groups. Must be rewritten into rule + wrong/right format (spec requirement), scoped for character-note context (drop reader-direct-address; carve out the When/Behavior/Because formula from the Wh-opener ban; reconcile the lazy-extremes ban with behavioral phrasing), and scrubbed of the upstream repo's product-name mentions (model-neutrality).
3. **Doctrine block wording.** The five additive principles and two tension exemptions have precise source passages (section 3 above); the tensions must be phrased as explicit exemptions layered on base rules so arms differ only by those paragraphs.
4. **Blinding mechanics.** Shuffle at build, base64 key with do-not-open warning, neutral packet names, no self-identifying output. Optional small stdlib-python script in `scripts/` for a reproducible shuffle/seal follows existing script conventions (python3, stdlib-only, ROOT pattern).

Main risks found: style-axis contamination of the doctrine axis via the Wh-opener conflict with the Because formula; blinding leakage via format differences between style blocks (spec already mandates format parity); shared-rule overlap shrinking the real style-axis delta; and the upstream examples file being internally inconsistent (em-dash in a no-em-dash rule set) — write fresh examples.
