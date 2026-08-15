---
type: research
title: Research Audit — Ideal Character Descriptions for AI Roleplay
description: Audit of all prior research, resource reviews, and empirical trials to
  synthesize what the ideal end state for character descriptions looks like, identify
  what is established vs. open, and flag where further research is needed.
tags:
- complete
date: 2026-08-14
timestamp: 2026-08-15T14:31Z
resources:
- "[[2026-07-11-causal-character-writing-for-llm-roleplay-friction-engines-and-trait-word-poisoning]]"
- "[[Anti Slop Research Results]]"
- "[[Worldbuilding Structure Research Results]]"
- "[[2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3]]"
- "[[2026-07-30-resource-review-aeon-s-notebook-decision-engine-and-helpful-default-convergence]]"
- "[[2026-07-17-resource-review-world-forge-multi-agent-world-pipeline]]"
- "[[2026-07-23-writing-doctrine-blind-trial-results-viralys-nadja]]"
- "[[2026-07-31-character-generation-pipeline-v2-input-restructuring-doctrine-additions-and-grader-agent]]"
- "[[2026-08-14-writing-style-trial-ste-100-and-semantic-anchors]]"
- "[[2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step]]"
- "[[2026-08-09-additive-doctrine-discriminator-trial]]"
---

# Research Audit — Ideal Character Descriptions for AI Roleplay

## Goals

Audit all prior research, resource reviews, and empirical trials in
this project to answer: what should an ideal character description for
AI roleplay look like? Identify what is established by evidence, what
is adopted but untested, and where further research is needed —
especially as context for a potential pipeline rework.

## Scope

This audit covers 278 commits of project history, 23 research
documents, 16 specs, 7 empirical trials, 4 ADRs, 3 external resource
reviews, and the current framework and pipeline design. The analysis
synthesizes across all of these; individual source citations are given
where a claim rests on specific evidence.

---

## Part 1: What the Research Establishes

### 1.1 Behavioral concreteness over trait labels

The single strongest finding across all sources. A heavy trait
adjective ("intelligent," "arrogant," "kind") can poison an entire
character card — the model latches onto the label and generates from
statistical associations with that word rather than from the
behavioral context surrounding it. The community term is "trait-word
poisoning."

**Evidence:** Three independent community sources converge on this
([causal character writing research](2026-07-11-causal-character-writing-for-llm-roleplay-friction-engines-and-trait-word-poisoning.md)).
Character Builder v3's design independently confirms it
([Hoplight review](2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md)).
Adopted as an absolute ban in
[ADR 0004](../adr/0004-action-line-style-model.md).

**Status:** Established. Implemented. No trial has contradicted it.

### 1.2 Causal structure: When/Behavior/Because

Character entries that specify a trigger, an observable action, and
the psychological source behind it outperform flat behavioral
descriptions. This is the structural formula for Soul entries.

**Evidence:** Derived from the causal character writing research,
which finds that "causality matters: specify why a behavior happens,
not just that it happens." Implemented in
[framework.md](../../skills/worldbuilder-character/framework.md) as
the standard Soul entry format.

**Status:** Established. Implemented.

### 1.3 Action-line convention as primary style model

Screenwriting action-line convention (present tense, only what is
visible or heard, no internal states, short plain sentences) is the
structural anchor for all character description prose. Chosen because
the spec-to-enactment relationship in screenwriting matches the
spec-to-portrayal relationship in AI roleplay.

**Evidence:** The [anti-slop research](<Anti Slop Research Results.md>)
identified it as the only high-salience reference that structurally
forbids unobservable interior description. Backed by Shaib et al.
(arXiv 2025) on slop taxonomy and Reinhart et al. (PNAS, Feb 2025)
showing that instruction-tuned models' dense Latinate register
persists even when explicitly told to imitate other styles. Decided in
[ADR 0004](../adr/0004-action-line-style-model.md).

**Status:** Established by theoretical argument and external
research. Implemented. The
[writing style trial](../specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md)
found that a human reviewer preferred baseline output over STE-100
and BLUF alternatives, but this is a taste preference for prose
readability — it does not demonstrate that action-line convention
produces better roleplay outcomes when the description is used as a
character card. No trial has tested functional roleplay quality for
any style approach.

### 1.4 Unresolved tensions over resolved facts

Models shortcut through resolved states. Unresolved tensions —
competing pulls, contradictions the character has not reconciled, open
futures — force the model to find positions fresh each time rather
than collapsing to a default.

**Evidence:** Community sources in the causal character writing
research. Character Builder v3's design principle that "contradictions
must be rooted, not arbitrary" ([Hoplight review](2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md)).

**Status:** Established in principle. Partially implemented (value-
conflict stance field in Pipeline v2 design). Not yet empirically
tested as an isolated variable.

### 1.5 Values must carry costs

A value without a price tag is decoration. Each top value needs a
concrete cost the character has already paid for holding it; lowest
values need proof of absence.

**Evidence:** Adopted from Character Builder v3 via
[Hoplight review](2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md).
Described as "behavioral, stageable, fills a gap" in existing
doctrine.

**Status:** Adopted. Specified in Pipeline v2 design. Not yet
deployed to production.

### 1.6 False beliefs that generate scenes

At least one wrongly-held conviction that the character acts on with
confidence. This is a scene generator — it creates situations where
the character's actions are driven by belief rather than truth.

**Evidence:** Character Builder v3 design principle
([Hoplight review](2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md)).

**Status:** Adopted. Specified in Pipeline v2 as a required doctrine
field. Not yet deployed.

### 1.7 Knowledge boundaries with domain specificity

Characters need domain-specific competence with stated gaps ("remembers
C99 spec verbatim" not "intelligent"), plus an explicit way of handling
not-knowing (does the character deflect? bluff? ask?).

**Evidence:** Community sources in causal character writing research.
Character Builder v3 reinforces: knowledge boundaries must include a
stated way of handling not-knowing.

**Status:** Established in principle. Partially captured in the Q&A
grilling process. Not a dedicated framework field.

### 1.8 Input-echo as the primary quality problem

The dominant quality problem is not slop, convergence, or style — it
is the generation reproducing input phrasing instead of transforming
semantic content into observable behavior. This finding reoriented the
entire pipeline design.

**Evidence:** The [convergence validation experiment](../specs/2026-07-30-cross-model-convergence-metric-validation-experiment.md)
found input-echo dominated cross-model convergence signal. The
[convergence retest](../../trials/2026-07-convergence-retest/retest-results.md)
graduated input-echo detection (0.7% echo rate after deslop/deframe).
Pipeline v2's fact-to-manifestation rule is the direct response.

**Status:** Established. Mitigation designed (deslop/deframe
preprocessing, fact-to-manifestation transformation). Partially
validated.

### 1.9 Content quality is the bottleneck, not style or pipeline mechanics

The single most important cross-trial finding. Both the
[pipeline quality trial](../specs/2026-08-13-pipeline-quality-trial-fail-check-gate-input-restructuring-and-decomposition-step.md)
and the
[writing style trial](../specs/2026-08-14-writing-style-trial-ste-100-and-semantic-anchors.md)
concluded independently that content problems — attributable to Design
Notes input quality — overshadowed any style or pipeline differences.

**Evidence:** Pipeline quality trial: all experimental conditions
scored below baseline; degradation increased monotonically with
additional processing stages. Reviewer observation: "Kallya's stored
Design Notes are poor and don't reflect the corrected final product."
Writing style trial: reviewer noted "all conditions have content
problems attributable to the inputs rather than the writing style."

**Status:** Established by two independent negative results. No
systematic solution tested yet.

---

## Part 2: What Was Empirically Tested

Seven trials, summarized by outcome. An important caveat applies to
all of them: **no trial in this project has tested actual roleplay
quality.** The trials measured two things:

1. **Human taste preferences** — a reviewer scores or ranks generated
   output by how much they like reading it. This tests prose
   readability, not whether the description produces better AI
   portrayals when used as a character card.
2. **Mechanical pipeline metrics** — input-echo rate, cross-model
   convergence, Jaccard divergence. These test pipeline health, not
   downstream roleplay quality.

Whether any of the principles in Part 1 actually improve roleplay
outcomes — in-character consistency, behavioral adherence, resistance
to trait-word collapse, distinguishable portrayals — has never been
measured. The entire evidence base rests on theoretical argument,
community consensus, and taste testing.

### Taste-tested (human reviewer preference)

- **Synthesis selection (3 variants):** A reviewer preferred synthesis
  output over mechanical-rule and LLM-judge selection output.
  5 variants produced hallucinated scenarios; 2 variants lacked
  enough material.
  ([Selection mechanism trial](../../trials/2026-07-selection-mechanism/results/trial-data.md))
- **Baseline writing style preferred:** A reviewer preferred current
  writing-style.md output over STE-100 strict, STE-100 loose, and
  BLUF output. This does not validate the action-line convention for
  roleplay use — it validates that the reviewer found it more
  pleasant to read.
  ([Writing style trial](../../trials/2026-08-writing-style/results/trial-data.md))
- **Pipeline quality interventions degraded taste:** A reviewer scored
  all experimental conditions below baseline. Quality degraded
  monotonically with additional processing stages.
  ([Pipeline quality trial](../../trials/2026-08-pipeline-quality/results/trial-data.md))

### Mechanically validated (pipeline metrics)

- **Input-echo detection:** Post-deslop/deframe echo rate dropped to
  0.7%. Graduated as prevention mechanism. This validates the
  pipeline fix, not whether low echo produces better roleplay.
  ([Convergence retest](../../trials/2026-07-convergence-retest/retest-results.md))
- **Additive doctrine not discriminative:** No meaningful difference
  in echo or overlap rates across current/additive/stopslop
  conditions. Doctrine setting does not affect pipeline metrics.
  ([Additive doctrine discriminator trial](../../trials/2026-08-additive-discriminator/summary.md))

### Behavioral influence (closest to functional validation)

- **Value-conflict stance entries:** Influenced downstream model
  behavior in 3 of 4 test scenarios. This is the only trial that
  tested whether a description element actually affected AI behavior,
  and only for one specific entry type in isolated scenarios.
  ([Convergence retest](../../trials/2026-07-convergence-retest/retest-results.md))

### Inconclusive / deferred

- **Cross-model convergence as slop detector:** Signal dominated by
  input echo; abandoned as metric after convergence retest.
- **LLM-judge scoring:** Ceiling effect prevents discrimination where
  humans see clear differences (writing doctrine blind trial).
- **Writing doctrine blind trial (2x3 design):** Weak positive for
  stopslop; no doctrine improvements adopted. Methodology contributed
  more than the result — led to the standing trial framework.

---

## Part 3: The Ideal End State

Synthesizing across all established principles, trial results, adopted
practices, and external sources, a character description at its ideal
would have these properties:

### Structure

The card comprises a **Core block** (universal, every character needs
it), plus optional **addon blocks** attached when relevant.

**Core block** uses three information-type rows: Background (facts),
Body (physical), Soul (psychological/social). Two candidate
organizations for these rows:

**Option A — Flat sections with coverage targets.** Each row is a
labeled section with a target entry count:
- Background: formative events, current circumstances, key facts
  (4-8 entries)
- Body: appearance, physical habits, embodied presence (3-5 entries)
- Soul: psychological patterns, social behavior, boundaries/pressures
  (5-8 entries, including required doctrine entries: core want, core
  fear, false belief, value-conflict stance)

**Option B — 3x3 depth-of-access grid.** Cross the three
information-type rows with a depth-of-access progression (Immediate /
Over Time / Hidden-or-Foundational), producing nine cells:

| | Immediate | Over time | Hidden / foundational |
|---|---|---|---|
| **Background** | Known history, visible circumstances | Things they let slip, stories that emerge | Formative wound, what they never tell |
| **Body** | Surface features, first impression, obvious mannerisms | Subtle habits noticed with familiarity | Hidden under clothes — scars, marks, physical tells |
| **Soul** | Social persona, default behavior with strangers | True self that emerges with trust | Motivational engine — core want, fear, false belief, value-conflict stance |

The grid maps to how roleplay unfolds over time (column 1 early,
column 2 as relationship develops, column 3 in depth) and forces
coverage of both information type and access level. The Body row's
progression from "everyone can see" to "hidden under clothes" bridges
naturally into the Intimate Dynamics addon block.

Both options share the same Q&A-into-card workflow: the working sheet
labels entries by section (Option A) or grid cell (Option B), and the
export strips labels and reorganizes for the target platform. No
decision between them yet — the choice should be informed by how the
Q&A workflow plays out in practice.

**Addon blocks:**

- **Relationships** — Named dynamics with specific other characters.
  Relevant for cast-based worldbuilding, not needed for standalone
  characters. Current 12-archetype framework carries forward;
  improvements come from the general shift to Q&A-focused creation.

- **Intimate Dynamics** — Optional, flagged at project planning.
  Current state: three flat coverage areas (attraction expression,
  hesitation/limits, specific dynamic) plus mandatory friction point.
  Candidate improvement: depth-of-access grid matching Core:

  | | Immediate | Over time | Hidden / foundational |
  |---|---|---|---|
  | **Attraction** | How they show interest | Changes with familiarity | What they're drawn to vs. what they perform |
  | **Dynamics** | Default intimate behavior | Shifts as trust builds | Emotional need the dynamic serves |
  | **Boundaries** | Obvious limits, what makes them pull back | Boundaries that relax or firm with trust | Friction point — internal contradiction |

  Hidden column should echo Core Soul x Hidden (if core fear is
  abandonment, it shows in intimate boundaries too). Same flexible
  approach: required minimums on key cells, rest filled if relevant.

- **Voice / Dialogue** — 2-4 example dialogue snippets, each a
  composite showing of the character pulling from multiple Core grid
  cells simultaneously. Prescriptive situation categories (casual,
  conflict, vulnerability, authority, solitary) ensure the character
  is stressed from different angles; which Core content appears in
  each example varies per character. Each snippet includes enough
  scene context to make a standalone scenario field redundant. Style
  contract (perspective, tense, register) emerges from the examples
  rather than being declared as rules. Working sheet notes which Core
  cells each example exercises as a coverage sanity check.
  Corresponds to CCv2/v3 fields (first_mes, mes_example, scenario)
  that the current framework does not produce.

### Content properties

Each of these is supported by research findings:

- **Every entry passes the staging test.** Can a director stage this
  sentence? If not, rewrite. No internal states, no significance
  announcements, no implications the reader must unpack.
- **No trait adjectives anywhere.** Absolute ban. Behavior earns the
  word. Not "she is confident" but "When challenged, she responds with
  certainty, treating doubt as personal insult."
- **Values have been paid for.** Each top value carries a stated cost.
  Lowest values carry proof of absence. A value without a price is
  decoration.
- **At least one false belief** the character acts on with confidence.
  This is a scene generator.
- **Unresolved tensions and competing pulls.** Not resolved facts the
  model can shortcut through. Open futures that force fresh
  positioning.
- **Knowledge boundaries with domain specificity.** Stated competence
  areas, stated gaps, and a stated way of handling not-knowing.
- **Value-conflict stance.** Operating code in the character's own
  words. Which way they go when values collide with morality (role-
  following / compromise / alignment-following). The lever that tips
  them. How guilt manifests behaviorally, if at all.
- **Contrast against at least one cast member** on a named axis. The
  description must establish how this character is distinguishable
  from the rest of the cast.
- **Independent ongoing pressures.** Rent, arguments, missed
  opportunities, unfinished obligations — things that give the
  character action beyond reaction.
- **Dense anchor repetition.** Recurring objects, places, gestures
  that connect across entries give the model multiple activation
  routes.
- **Compressed sensory fragments** carry more weight than paragraphs.
  "Lowering her yukata's collar, one word — run" outperforms
  explanation.

### Style properties

- Present tense, observable/audible only (action-line convention)
- Short declarative sentences, active voice
- Anglo-Saxon vocabulary preference (Orwell co-anchor)
- No meta-vocabulary from the builder abstraction layer
- Fact-to-manifestation transformation: reproduce semantic content,
  never reproduce phrasing from the Design Notes input
- Em-dash ban (noted as unenforced in pipeline quality trial)

### Quality properties

- **Voice is blind-line distinguishable.** Strip the character's name
  from the description; a reader should still know who it is from
  prose alone.
- **Every behavior traces to a Design Notes spec line.** Untraced
  behavior is a finding.
- **Input-echo rate below 1%.** Validated by the convergence retest.
- **Three-variant generation with synthesis selection.** Preferred by
  a reviewer in the selection mechanism trial (taste-tested, not
  functionally validated).
- **Human-in-the-loop content review.** Writing style trial reviewer
  recommended human review at each generation stage, not just at the
  end. Design Notes would shift from direct generation input to a
  reviewed record.

### Token budget

Community research consensus is 900-1500 tokens per character card (up
to 2300 for pairs). No trial in this project has tested this range
against the current framework's output length. This is a gap.

---

## Part 4: What Is Not Yet Established

These are principles adopted or designed but lacking empirical
validation, or questions the research raises but does not answer.

### 4.0 Functional roleplay validation

The most fundamental gap. No trial has measured whether any of the
project's established principles actually improve AI roleplay
outcomes. Every trial measured either human taste preferences for
generated prose or mechanical pipeline metrics. The question "does a
character description written this way produce better portrayals than
one written another way" has never been asked in any controlled
setting.

This matters because taste and function can diverge. A description
that reads well to a human reviewer might not bind model behavior
effectively; a description that looks clunky might produce excellent
portrayals. The community sources in the causal character writing
research claim specific functional effects (trait-word poisoning,
anchor activation, tension-driven fresh positioning), but these are
practitioner reports, not controlled tests.

What functional validation would look like: run roleplay scenarios
against character descriptions written in different styles or with
different content structures, and measure in-character consistency,
behavioral adherence to spec, resistance to convergent defaults, and
voice distinguishability across an extended interaction — not just
whether a human likes reading the description itself.

### 4.1 Content quality improvement

The most consequential open question. Two independent trials found
content is the bottleneck, but no systematic approach to improving
Design Notes quality has been tested. The writing style trial reviewer
suggested a more hands-on human-in-the-loop process throughout
generation. Pipeline v2's structured doctrine fields are designed to
improve input quality, but the pipeline quality trial's negative
result showed that more automated processing is not the answer.

**What further research could address:** What does effective human-in-
the-loop content review look like at each generation stage? What makes
a Design Notes document "good enough" to generate from? Can the Q&A
grilling process be improved to elicit richer, more specific inputs?

### 4.2 Writing style for non-Soul sections

All style trials tested Soul section generation only. Background
(fact pairs), Body (physical behaviors), and Relationships
(archetypal dynamics) have different structural properties and may
respond differently to style rules. The writing style trial spec
noted this as a separate post-trial decision.

### 4.3 Token budget validation

Community consensus (900-1500 tokens) has not been tested against the
current framework's output. The relationship between token count and
roleplay quality — where the diminishing returns kick in — is unknown
for this specific format.

### 4.4 Scenario-class testing

World-Forge's scenario testing matrix (on-script, trigger collision,
near-miss false triggers, off-script pressure, coverage-void probes,
lull/passivity) was adopted in principle but has not been implemented
as a validation gate. No trial has tested whether current output
passes these scenario classes.

### 4.5 Blind-line voice distinguishability

Adopted from World-Forge as a quality criterion but never tested.
Unknown whether the current framework produces descriptions where
characters are distinguishable by prose alone when names are stripped.

### 4.6 Pipeline v2 input restructuring

The seven structured doctrine fields are specified but not deployed.
The deslop/deframe preprocessing works (echo rate 0.7%), but the
full input restructuring — charge-scored memories, routing
annotation, values-with-costs, false belief, contrast declaration —
has not been tested end-to-end. The pipeline quality trial's bundled
S1/S3/S6 conditions failed, but the spec notes this "cannot establish
that each lead is individually ineffective."

### 4.7 Grader agent

Designed as a post-generation quality check using input-aware
convergence detection. Partially validated (convergence retest). Full
integration blocked on pipeline quality trial negative result — needs
a retest strategy.

### 4.8 Value-conflict stance activation

Graduated for behavioral influence (3/4 scenarios), but the Pipeline
v2 spec flagged potential need for fine-tuning rather than prompting
alone (per RoleCDE paper) for consistent activation. Whether
prompting reliably activates it at roleplay time, or whether it only
works as a generation input, is unknown.

### 4.9 Multi-platform export

Export standards review completed a field-gap baseline (extraction
reliability map across CCv3, SillyTavern worldinfo, charx). The
description format affects what export targets can extract. Whether
the ideal description format conflicts with any export target's field
requirements is mapped but not tested.

### 4.10 The "how a human would type" problem

The pipeline quality trial reviewer observed that output "doesn't
sound anything like how a human would type." This is a distinct
problem from slop — the output may be technically correct (behavioral,
stageable, action-line) but still read as machine-generated functional
prose rather than something a person would naturally write. Whether
this matters for roleplay quality, and if so how to address it, is an
open question.

---

## Part 5: Tensions and Contradictions

### 5.1 Processing depth vs. output quality

The pipeline quality trial showed that more processing stages degrade
quality. But several established principles (deslop/deframe, fact-to-
manifestation transformation, multi-option generation with synthesis)
are themselves processing stages. The tension: some processing is
clearly beneficial (echo rate dropped from measurable to 0.7%), but
adding processing stages monotonically degraded perceived quality in
the one trial that tested it. The resolution may be that beneficial
processing targets a specific known defect (input echo), while
speculative processing ("input restructuring," "decomposition step")
adds overhead without targeting a validated problem.

### 5.2 Functional guidelines vs. natural prose

The pipeline quality trial reviewer called out a mismatch: character
descriptions are "functional AI portrayal guidelines, not literary
prose," and language that leads in without context or relies on
implication is "unusable for that purpose." But the action-line
convention and compressed sensory fragments from the causal character
writing research push toward concision and implication. The ideal
sits somewhere between machine-like instruction lists and literary
prose — behavioral, concrete, and functional, but still readable as
something a person might write.

### 5.3 Directive vs. descriptive specifications

World-Forge review established that specs must be "directive, not just
descriptive" — they must bind behavior, not merely describe it. The
current framework is descriptive (here is how the character behaves)
rather than directive (here is how you must portray this character).
Whether a more directive framing improves roleplay quality is
untested.

### 5.4 Exemplars vs. rules

The anti-slop research found that before/after exemplars are "the
strongest lever" for vocabulary suppression — named style models alone
cannot suppress content-activated vocabulary. But the current
framework operates entirely through rules (writing-style.md, slop-
phrases.md) with no exemplars. Whether adding exemplars to the
generation pipeline would improve output quality is untested.

---

## Consolidation

The research base is internally consistent on fundamentals:
behavioral concreteness, causal structure, trait-word ban, action-
line convention. These principles are established by theoretical
argument, community practitioner consensus, and external research —
not by controlled testing of roleplay outcomes.

The trials measured two things: whether a human reviewer preferred
one style of generated prose over another, and whether mechanical
pipeline metrics improved. The generation mechanism (3-variant
synthesis) and input-echo prevention (deslop/deframe) graduated on
these measures, while additional pipeline complexity and alternative
style approaches did not. But no trial measured whether any of these
choices produce better AI roleplay portrayals — the question the
entire project exists to answer.

Two independent trials found that **content quality — the richness
and specificity of what goes into Design Notes — is the primary
constraint on output quality**, not style rules or pipeline
mechanics. This reframes the pipeline rework question: the highest-
leverage intervention may not be a better generation pipeline but a
better process for producing and reviewing the input that feeds it.

The ideal end state for character descriptions is well-specified in
structure, content properties, and style. What is missing is:

1. **Functional validation** — whether these principles actually
   improve roleplay outcomes, not just prose readability
2. **A content quality solution** — the identified bottleneck has no
   tested fix
3. **Validation of adopted-but-untested principles** — token budget,
   scenario testing, blind-line distinguishability, exemplar-based
   guidance

**Further research candidates, ranked by expected impact:**

1. Functional roleplay validation — test whether descriptions written
   to these principles produce measurably better AI portrayals than
   alternatives (the foundational question, never asked)
2. How to systematically improve Design Notes quality (the content
   bottleneck)
3. Whether exemplars in the generation pipeline improve output
   quality (the anti-slop research's strongest lever, never tested)
4. Token budget validation against actual output and roleplay quality
5. Directive vs. descriptive framing for character specifications
6. Blind-line voice distinguishability testing on current output
7. Individual testing of Pipeline v2 input restructuring leads (the
   bundled test failed, but individual leads may be effective)
