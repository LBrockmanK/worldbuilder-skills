---
type: research
title: 'Resource review: Hoplight, a webnovel author''s AI writing guide, and Character
  Builder v3'
description: 'Verdicts on three incoming resources: the Hoplight local-first roleplay-content
  studio (proposed for the export layer), a webnovel author''s guide to writing with
  AI, and a SillyTavern Character Builder v3 preset claiming a research basis.'
tags:
- complete
date: 2026-07-25
timestamp: 2026-07-25T20:29Z
resources:
- https://github.com/Coneja-Chibi/Hoplight
- https://www.reddit.com/r/WritingWithAI/comments/1v66q3e/a_guide_to_writing_with_ai_from_a_webnovel_author/
- https://www.reddit.com/r/SillyTavernAI/comments/1v6acvy/character_builder_v3_decision_engine_v2_built/
- https://aeonsnotebook.substack.com/p/build-a-character-v3-decision-engine
- https://docs.google.com/document/d/13wlOvLIOXNmF3XS7m09fbxFhpUSjOS0lTJB4oOW0Gqk/edit
- https://drive.google.com/file/d/11zvy6JEK0RpGDG5qve9ITJhHZJmS4NLI/view
- https://drive.google.com/file/d/1RMOuY6qmhE8t1cfa_qMP5ZkVw1whdYmz/view
- https://drive.google.com/file/d/1eLsT6CMPPWr4sH7GjnUNa4P2O_0KOu8R/view
---

# Resource review: Hoplight, a webnovel author's AI writing guide, and Character Builder v3

## Goals

Three resources arrived with per-item notes. Each verdict has to answer
the note as an explicit question:

1. **Hoplight** (`https://github.com/Coneja-Chibi/Hoplight`) — note:
   "Inspire or integrate for export layer." Question: should the export
   layer take design input from Hoplight, depend on it, or neither?
2. **A guide to writing with AI, from a webnovel author**
   (r/WritingWithAI, post `1v66q3e`) — no note. Question: does anything
   in it change the writing doctrine, and what does it link to?
3. **Character Builder v3 / Decision Engine v2** (r/SillyTavernAI, post
   `1v6acvy`) — note: "Claims research basis, compare it to our own and
   see what we can learn." Question: is its research basis real, and
   where does it disagree with our character doctrine?

Standing instruction for items 2 and 3: the resources *linked by* the
posts are the primary interest; the discussion itself is secondary.

## Results

### 1. Hoplight — verdict: Inspire (integration real but deferred)

**What it is.** A local-first desktop studio for AI-roleplay content,
written in TypeScript on Bun 1.3+, AGPL-3.0-or-later, by the author of
BunnyMo, TunnelVision and VectHare. It holds characters, lorebooks,
personas, presets and regex sets as plain JSON on local disk and
converts between platform formats. The architecture is hub-and-spoke:
one canonical model in the middle (`specs/formats/canonical-model.md`),
one adapter per platform under `src/formats/`, currently ten codec
folders (agnai, backyard, lumiverse, marinara, novelai, pygmalion,
risu, rolecall, sillytavern, vaud-json). The README states the coupling
rule directly: "Adding a platform is dropping a folder into
`src/formats/`, and the CLI, the editor, the export dialog, and the
Press all gain the format with zero central registration." Its export
room ("The Press") writes SillyTavern V2/V3 JSON, PNG and charx,
RisuAI, RoleCall, Backyard `.byaf`, Agnai, Pygmalion, Lumiverse,
Marinara, Chub, NovelAI lorebooks, and portable CCv3 as the fallback;
it reads the same set back in. It is also an authoring tool, not only a
vault: a Workbench with a conversational "Casting Interview", and a
Binder for lorebooks with activation rules, budgets and health checks.
Slop detection, an agent, prompt evolution and a full interview engine
are listed as planned, not built.

**Verified this session.** `gh repo view` and the GitHub API: AGPL-3.0,
5 stars, 1 fork, repository created 2026-07-18, last push 2026-07-25,
status badge "Active Development". Published releases exist from
v0.1.14 with prebuilt binaries for Windows, macOS arm64/x64 and
linux-x64, so the install path is real and not source-only. `LICENSING.md`
names the project "Vaudeville Studios", so the naming is still in flux.
The roadmap marks the engine and converter and character editing as
done, content types and the studio app as in progress, and the CLI as
work in progress.

**Answering the note.** Both halves, separately.

*Inspire — yes, and it mostly confirms rather than changes.* Hoplight's
hub-and-spoke shape is the same decision as
[ADR 0003](../adr/0003-platform-decoupling.md): the canonical model
knows no field names, and only the adapter does. An independent project
arriving at the identical split is the strongest kind of evidence for a
decision we already made, and it costs nothing to bank. The one genuine
design input is the granularity: Hoplight's canonical model is a typed
schema with entity types, ours is prose notes and one hand-written
export skill. That difference is deliberate on our side and should stay
that way, because our Wide-phase notes carry authored prose that no
typed schema wants to hold.

*Integrate — not into the plugin, but a real option downstream.*
Vendoring is off the table on two counts. The license is AGPL-3.0-or-later
and this repo currently ships markdown skills with no `LICENSE` file at
root, which makes any code lift a licensing decision rather than a
technical one. And the architecture does not fit: our export phase is
agent-written prose assembled into `world.json` and packed as
`.sbworld`, with no build script to call a Bun app from.

The option that does fit is Hoplight as a *downstream* converter, and
it bears directly on the open SillyTavern work (inbox item 4). That
item currently reads as "teach the export skill a second target
format". If instead the export skill emits one portable CCv3-shaped
payload, Hoplight fans it out to eleven platforms without us writing a
second exporter at all. That is a materially better shape than adding
targets one at a time. Two things hold it back today: it puts an
external application in the user's path, and the repository is one week
old at v0.1.x. Neither is a reason to drop the idea; both are reasons
not to depend on it yet.

Note also that **ainime-games.com is not in Hoplight's format list**,
so it does nothing for our primary export target. Its value is entirely
on the secondary-target question.

*Against World-Forge.* Inbox item 4 already names World-Forge (MIT) as
its primary reference. These are complementary, not competing.
World-Forge documents what the SillyTavern runtime actually honors,
which is what the mapping study needs first. Hoplight supplies the
field shape as working code.

The sleeper asset here is `specs/formats/`, and it may be worth more to
us than the application. It holds seventeen hand-written format specs,
most of them 20-50KB: `chara-card-v2.md`, `chara-card-v3.md`,
`st-worldinfo.md`, `st-preset.md`, `png-embedding.md`, `charx.md`,
`content-detection.md`, plus the RoleCall, Backyard and Lumiverse
codecs. `canonical-model.md` itself is a short skeleton that names the
content types (`Character`, `Lorebook` plus `LorebookEntry`, `Preset`,
`Persona`, `RegexScript`, `Production`) and states the design rules,
including one worth stealing outright: prompt-bearing fields are
first-class and format-neutral, and an embedded lorebook is a reference
to a canonical Lorebook entity rather than an inline blob, with codecs
inlining or extracting at the boundary. That is precisely the question
inbox item 4's mapping study has to answer for our Wide-phase notes.
Reading those specs is free, carries no license entanglement, and beats
reverse-engineering the card format from scratch.

**Follow-up asked during review: can its workflow raise the standard of
our own export, even though it never touches ainime?** Yes, and this
turned out to be the more useful half of the resource. Our export is an
agent assembling `world.json` by hand from Wide-phase notes, which is
exactly the situation where an unwritten procedure degrades quietly.
Hoplight's export room has one governing idea worth taking whole: it
refuses to be silent. Six borrowings, none of which need code.

*Report every piece, and never omit.* "The Press never fails silently,
and it never lies by omission. Every row is printed, skipped, or
failed, and it tells you which one and why." Our export produces no
report at all. A required export report — every Wide-phase note listed
as exported, partially exported, or skipped, with the reason — is pure
skill prose and would catch the failure mode where a note quietly never
reaches the world.

*Bad news before the run, not after.* Their readiness pass happens
before the lever is pulled, and their own line for it is "A red line in
the Press beats a broken card in someone else's app." For us that is a
pre-assembly check: which required ainime fields have no source note,
and which notes have no target field.

*Show what the target will actually carry.* Each staged item displays
"exactly what the target platform will actually carry", per field. The
analogue is a per-note field map printed before assembly, so the author
sees that a note's third paragraph lands nowhere before the export
happens rather than after.

*Name what does not fit instead of dropping it.* Their escrow keeps
unmapped fields alive across a round trip; their codec reports carry
`dropped`, `escrowed` and `warnings`, and their CLI can exit non-zero
on drops. Our export is one-way, so escrow itself does not apply, but
the reporting half does: content in a note with no ainime home should
be named in the report, because the author needs to know what the
platform will not carry.

*Check that things can actually fire.* The Binder flags a lorebook
entry with no keys, no always-on flag and no by-meaning mode, because
it can never trigger, and the Press repeats it in red at export. We
have the same class of defect available to us in `loreEntries[]` and
`storyTriggers[]`, and a can-this-ever-fire check is mechanical and
testable.

*Declare the cut order in advance.* "When the budget runs out, priority
decides who gets evicted and order decides where the survivors land.
You set both, and nothing is left to a chance you didn't choose." This
is the sharpest one, and Character Builder v3 independently does the
same thing with its numbered compression priority. Where content
exceeds what an ainime field will hold, our export skill currently
leaves the choice of what to cut to the agent's judgement in the
moment. A declared cut order makes that a decision we own. Their habit
of marking token estimates with a `~` rather than pretending precision
is worth copying at the same time.

**Proposed routing.** Amend inbox item 4 to carry Hoplight as a second
reference and to record the fan-out option, and open a separate line
for the export-procedure borrowings above, which are a change to the
export skill rather than a reference to read. No change to any ADR.

### 2. Webnovel author's AI writing guide — verdict: Inspire (narrowly)

**What it is.** A self-report from u/StrengthSpiritual939, an anonymous
Royal Road author, describing a human-in-the-loop drafting process for
webnovel chapters. The method: write one full novel with no AI at all
to establish a voice; outline the next book; hand-write chapter one;
then for each subsequent chapter send a short prompt plus the entire
prior book to *two* models, put both drafts side by side, and hand-type
the best version in the middle. Supporting rules: never copy-paste from
a model, generate in 800-1500 word chunks, never reuse model-invented
character names without searching them first, and run early work
through AI detectors until it reads as fully human.

**It links to nothing.** The standing instruction was that resources
linked by the posts are the primary interest. This post contains no
external links at all, so the post body is the whole resource. The
comment thread is mostly an ethics argument about disclosure and adds
nothing technical.

**Credibility.** Every claim is unverifiable self-report. The author
declines to name the story specifically to avoid being identified, and
states in the comments that they would deny using AI if asked. Nothing
here is evidence; it is one practitioner's account of what they believe
works. It is worth reading on that basis and no stronger one.

**Answering the implicit question.** Most of it does not transfer.
The guide's whole objective is preserving a human author's prose
fingerprint from human readers. Our skills produce specification prose
that an engine reads, and the reader we are writing for is a model, not
a subscriber. Three specific consequences:

*Worth taking.* The cross-model convergence check is the one genuinely
portable idea: "If both models wrote a sentence exactly the same way,
you probably need to rewrite it, because it's a major red flag for AI
voice." That is a mechanical slop signal that needs no human judgement.
Our blind-trial kit currently scores slop density by hand, which is the
cost that inbox item 2 is stalled on. Generating a section from two
models and flagging the sentences they agree on verbatim is a cheap
approximation of that score. It does not discriminate additive from
non-additive doctrine, so it does not directly unblock item 2, but it
attacks the same cost.

*Worth rejecting explicitly, so it is not proposed again.* Pangram and
GPTZero have no place in our loop. They measure whether prose fools a
human-oriented detector. Our output is a character note read by a
model, where being recognisably machine-written is not a defect. Any
future suggestion to add detector scoring to the trial kit should point
at this line.

*Corroboration only.* Two of the guide's habits are things we already
do, and it is useful to know an independent practitioner converged on
them: feeding a standing character reference and style guide into every
generation, and hand-writing the parts that later generations draw
from. The second is a mild independent argument for the seed and World
Introduction carve-out landed on 2026-07-25, where player-facing prose
is authored rather than generated to a specification.

**Proposed routing.** One new inbox line for the convergence check,
attached to the trial kit. Nothing else.

### 3. Character Builder v3 + Decision Engine v2 — verdict: Inspire (the strongest of the three)

**What it is.** A SillyTavern character-authoring system by u/Tasty_Living4077
(Substack: The Miscellany of Aeon), published 2026-07-25. The Reddit
post is an announcement; the Substack post is a 4KB overview; the
system itself is four linked documents, all retrieved this session:
*The Decision Engine* (v2, 10KB), *How to Build a Character* (v3,
29KB), *Character Forge* (the builder prompt, 7KB), and a worked
example codex (31KB). The author is a novelist by trade who states they
designed the system in collaboration with a model. The sample card is
login-gated on botbooru and could not be retrieved.

It has two halves.

*The Decision Engine* is a **runtime** mechanic. A prefill opens a think
stage and rolls two dice (`{{random:steady,steady,steady,steady,impulse,impulse,reckless}}`
plus a world die). The engine, installed once in the preset and
mirrored in each card's `system_prompt`, then forces a three-option
spread at every choice point: BASELINE (the character's un-softened
standard move), PIVOT (a task, an NPC, a subject change, or silence),
and FRICTION (a selfish or escalating move aimed at the top of the want
stack). A FAIL CHECK rejects spreads where all three options resolve to
the same decision. The roll picks the winner: steady takes
baseline or pivot, impulse takes friction inside a BOLD domain,
reckless takes friction that crosses into a CAUTIOUS one. Execution
rules follow, of which the sharpest is that the prose must render the
chosen move in its true register rather than "launder a dark choice
into a warm one".

*How to Build a Character v3* is the **authoring** half: a seven-slot
profile (Core, Inner, Surface, Context, Bounds, Friction, People) that
feeds the engine's two read blocks, compressed into a chara_card_v2
card with a defined cut-from-the-bottom priority order, plus a lorebook
sourced from scored memories.

**Answering the note, part one: is the research basis real?** Yes,
substantially — the problem is citation hygiene, not invention.

The v3 guide closes with a "Research receipts" table mapping each
design element to a grounding, and the author says the additions come
from "thirteen papers, July 2026 deep read". The receipts name sources
by nickname only. There is not one title, author, year, DOI or link in
any of the four documents, so nothing in the table is checkable as
written. That is a real defect and it is why the claim deserved
testing.

Tested against the arXiv API this session, most of the nicknames
resolve to real and topically apt papers:

| Nickname in the receipts | Resolves to | arXiv |
|---|---|---|
| Generative Agents | Generative Agents: Interactive Simulacra of Human Behavior | 2304.03442 |
| PsyMem | PsyMem: Fine-grained psychological alignment and Explicit Memory Control for Advanced Role-Playing LLMs | 2505.12814 |
| RoleCDE | RoleCDE: Benchmarking and Mitigating Role-Alignment Trade-offs in Role-Playing Agents | 2606.01552 |
| Interpolative Decoding | Interpolative Decoding: Exploring the Spectrum of Personality Traits in LLMs | 2512.19937 |
| HumanLLM | HumanLLM (two candidates: Towards Personalized Understanding and Simulation of Human Nature; Benchmarking and Improving LLM Anthropomorphism via Human Cognitive Patterns) | 2601.15793 / 2601.10198 |
| ReverieMem | probably Staying In Character: Perspective-Bounded Memory For Book-Based Role-Playing Agents (matched on the term; the title does not carry the name) | 2606.25632 |
| LifeChoice | probably Character is Destiny: Can Role-Playing Language Agents Make Persona-Driven Decisions? (LifeChoice is that paper's benchmark) | 2404.12138 |

Five names did not resolve on the queries tried: SCOPE, SPeCtrum,
Profile Axes, SRI, and PCL / Chain-of-Persona. That is not evidence
they are invented. The documents give no titles, so every query was a
guess at what the nickname refers to, and a failed guess proves
nothing. DPO and TKI appear in passing and are a well-known training
method and a well-known conflict-mode instrument respectively, used
correctly in context.

Where the papers do resolve, the fit is close rather than decorative.
RoleCDE is a benchmark for exactly the role-alignment trade-off their
"alignment gravity" claim describes. Interpolative Decoding treats
personality traits as continuous positions, which is precisely what
their dials are. The perspective-bounded memory paper matches their
knowledge-bounds slot. This is someone who read in the right places.

What remains unverified is every *number*. "Stated motivations turn a
~65% decision-maker into a ~90% one", "+25-30 points", "demographics
explain ~1.5% of behavior", "Context alone approximately equals full
profile" — each is attached to a nickname with no figure or table
reference. Those are the claims that would justify restructuring our
own doctrine, and they are the claims we cannot check without reading
the papers. Treat the design ideas as worth taking on their own merits
and the statistics as unconfirmed.

One correction for the record: an automated citation pass early in this
review reported thirteen of fourteen sources as unfindable. That result
was wrong. Its arXiv lookups all failed on an unfollowed 301 redirect,
so its negatives carried no information, and it separately flagged the
documents' July 2026 dating as impossible, which is an artifact of its
own knowledge cutoff rather than a fact about the documents. The table
above comes from re-running the lookups directly.

**Answering the note, part two: what can we learn?** More than I
expected. Taking the transferable items in descending order of value to
us.

*Role-value decoupling — the finding, corrected.* Their framing is
"alignment gravity": models keep a character's surface traits and
erode the motive fields, so a stated code degrades toward a helpful
narrator **as a conversation runs**. Their counter is a GUARD block in
`post_history_instructions` re-injecting the two most at-risk motive
sentences close to generation.

Reading the paper they cite for it does not support the over-time part.
RoleCDE ([arXiv:2606.01552](https://arxiv.org/abs/2606.01552)) measures
role-playing agents against roughly 8k role profiles and 24k dilemma
instances, and reports a "Role Value Decoupling" phenomenon in which
agents "systematically default to alignment- and morality-consistent
decisions rather than role-specific values when the two conflict, even
under explicit role conditioning". That is a **static, per-decision**
bias, and the paper explicitly reports it as "largely invariant to
dilemma difficulty". There is no measurement of erosion over the course
of a session anywhere in it. The decay narrative is the community
author's extrapolation, not the finding.

Two further corrections that matter for what we do with it. The
mitigation RoleCDE demonstrates is **fine-tuning**, not prompting, so
the GUARD block is an untested invention rather than a validated
counter. And PsyMem
([arXiv:2505.12814](https://arxiv.org/abs/2505.12814)), cited for the
memory machinery, is likewise a training result: it trains a model to
align responses with explicit memory. Neither paper licenses a claim
about what a well-written static profile can achieve through prompting
alone.

The corrected finding is still worth having, and it is better news for
us than the decay version, because a per-decision bias is an
authoring-time problem. At any moment where a character's values
collide with conventional morality, the model will tend to pick
conventional morality regardless of how the profile is written. Our
doctrine has nothing that pre-answers that collision. Their answer is
the Value-Conflict stance: declare which way the character goes
(role-following, role-compromise, alignment-compromise,
alignment-following), name the specific lever that tips them the other
way, and state how guilt shows behaviorally if it shows at all. That is
expressible in a static note, it needs no injection surface, and it is
exactly what their dilemma test checks for. Given that the paper's own
mitigation was fine-tuning, we should expect a partial effect and treat
it as something to test rather than assume.

*Values carry costs.* Their want stack requires that each of the top
three values carries one sentence of what it has already cost the
character or someone else, on the rule that "a value that has never
been paid for is decoration". They pair it with naming the two lowest
values and one act proving the character does not hold them. This is
the single best idea in the document for us, because it needs no
runtime support, it is a behavioral and stageable requirement in
exactly the sense
[skills/writing-style.md](../../skills/writing-style.md) demands, and
it fills a real gap: our doctrine requires a contradiction and an
irrational behavior with a root, but nothing forces a value to have
been *paid for*. It also has teeth against the failure our own trials
keep finding, which is notes that assert a disposition without evidence
of it.

*The dilemma test as a ship gate.* Before a full build ships, the
author writes one dilemma putting the character's top value against
common decency, then checks that the profile answers it without the
author deciding. If they had to decide, the motive fields are
underwritten. The second half is better still: run the same dilemma
past the character this one was declared to be built *against*, and
confirm the answers differ rather than the accents. This is
squarely the family of audit patterns inbox item 6 is already
collecting, and it is more actionable than most of them because it
produces a pass/fail from a single written scenario.

*Contrast declaration.* Every character records which existing
character it is built against and on which axis, and that axis is what
convergence testing presses. Our
[relationships.md](../../skills/worldbuilder-character/relationships.md)
governs distribution of archetypes within one character's relationship
set, but nothing in our doctrine asks whether two characters in a cast
are actually distinguishable. Cheap to adopt, and it targets the
sameness failure directly.

*Scored memories routed by charge.* Memories get a poignancy score out
of ten, and the score decides where the memory goes: 9-10 become
situational lorebook entries written as the live nerve, 6-8 become
problem or place entries, 1-5 become flavor. The
[2026-07-11 reference](2026-07-11-causal-character-writing-for-llm-roleplay-friction-engines-and-trait-word-poisoning.md)
already flagged emotional memory hooks as a delta with an unresolved
tension against our plainness rule. This adds the part that was
missing: a rule for deciding which memories earn the expensive
treatment. It maps onto our own surface/mid/deep layer classification,
which currently has no charge-based criterion.

*False beliefs.* Their knowledge-boundary slot requires at least one
belief the character holds wrongly and acts on with confidence, plus a
stated in-character way of handling not knowing. Our
[framework.md](../../skills/worldbuilder-character/framework.md) has
knowledge boundaries but not the false belief, and the false belief is
the part that generates scenes.

*Independent confirmation of the trait-word ban.* Their dials are the
Big Five plus Honesty-Humility, and every dial must cash out in two
concrete behavioral anchors: "counts the till twice and locks the door
herself," never "conscientious". Arriving from a completely different
direction at the same rule as our trait-adjective ban is worth banking.
So is their reason for keeping the Enneagram builder-only and never
surfacing it, and their warning that stacking more than one typology
"over-constrains toward convergence".

**What we should not take.** The engine half does not transfer.
It depends on prefill support, a `{{random:}}` macro, preset
installation and probability-fired lorebook entries, none of which our
target platform gives us, and it spends tokens on a deliberation trace
every single turn. Their friction lives in the inference loop; ours
lives in the specification, and on a platform we do not control that is
the correct side to be on. Their typology vocabulary (Enneagram, Big
Five, HEXACO) should stay out on our own grounds even though they use
it carefully. And their cards are explicitly "thick on tokens", which
is a different economy from ours.

**Presentation caveat.** The documents are written in a register our
own doctrine would fail: flourish, aphorism, and second-person
instruction throughout. That is a comment on their prose, not their
design, and the design is the part worth mining.

**Proposed routing.** Two inbox lines: one for the character-doctrine
candidates (values-with-costs, false belief, contrast declaration,
charge-scored memory routing, explicit operating code), one attaching
the dilemma test to the existing methodology thread in item 6. The
portrayal-decay question is the largest of them and is the one that may
deserve promotion beyond an inbox line.

## Consolidation

Three resources, three Inspire verdicts, but of very different weight.
Hoplight confirms an architecture decision we already made and hands us
a free format-spec library for the SillyTavern thread. The webnovel
guide yields one portable idea out of a post that is mostly about a
problem we do not have. Character Builder v3 is the substantial one: it
exposes a gap in our doctrine we had not named, and offers four or five
concrete devices that survive translation to our platform.

An earlier draft of this document called portrayal decay over a long
session the most valuable finding of the three and proposed promoting
it beyond an inbox line. Reading RoleCDE directly retired that. The
decay-over-time story is the community author's extrapolation; the
measured finding is a static per-decision bias toward conventional
morality at value conflicts, and that is an authoring-time problem with
an authoring-time answer. It belongs with the other doctrine
candidates, not in a spec of its own.

What survives from that thread as a genuine gap is narrower and
sharper: **we never grade behavior, only notes.** Every check we run
reads the note. Nothing plays the character and grades the transcript.
That limitation is the same one behind the trial's inverted ranking.

**Decided 2026-07-25 (Kevin): live play testing is out of scope, and
this is not a deferral.** Side-by-side play comparison carries too many
uncontrolled variables and too much cost to be worth running at this
stage, and the variance it would add would swamp whatever signal it
produced. The gap is accepted rather than closed. The intended source
of behavioral evidence is uncontrolled user feedback once outputs are
live, which is not a trial arm and should not be treated as one. So
automated assessment stays confined to what can be read off the note
and off paired generations of it, and any future proposal to grade play
transcripts starts by revisiting this decision rather than assuming the
gap is still open.

Two things across the batch turn out to point the same way, and neither
was what the resource was nominally about. Hoplight's real gift is not
its converter but its refusal to export silently, and the Character
Builder's is not its dice engine but its insistence that a claim about
a character is worthless until something has been paid for it. Both are
arguments for making the implicit explicit at the moment of writing.

Already applied this session, at the user's request and outside this
document's routing: two lines to the fleet inbox recording that the
Reddit access ladder has shifted and that `reddit_read.py` fails
silently against the new login wall.

## Routing

All six blocks were approved and applied on 2026-07-25; they are kept
here as the record of what was written. Two were revised before
applying. Block 3 was rewritten after the trial's inverted ranking was
raised: it now leads with automated assessment as the standing weakness
rather than with the convergence trick, and carries the
validate-against-existing-human-ranks requirement and the
same-family-models caveat. Block 5 replaced a withdrawn
portrayal-decay line after RoleCDE was read directly.

### 1. Amend inbox item 4 (SillyTavern export target) — add Hoplight

Replace the existing `2026-07-16T05:45` line with:

```
- 2026-07-16T05:45: SillyTavern as a second export target — Export phase was designed for multiple frontends. First step is a mapping study: which Wide-phase note types feed a V3 card vs the tiered lorebooks, and what carries the chat-preset role. Primary reference: World-Forge (MIT) — Notes_On_functionality.md / Notes_Quick_Reference.md for ST runtime behavior, templates/ + tools/validate_export.py for target formats; see the resource review (item 8). Second reference added 2026-07-25: Hoplight (AGPL-3.0, github.com/Coneja-Chibi/Hoplight) ships seventeen hand-written format specs under specs/formats/ (chara-card-v2.md, chara-card-v3.md, st-worldinfo.md, st-preset.md, png-embedding.md, charx.md), which is field-shape reference material the mapping study can read for free with no license entanglement — World-Forge tells us what the ST runtime honors, Hoplight tells us the field shape. Also evaluate the larger option it opens: rather than teaching the export skill a second target, emit one portable CCv3-shaped payload and let Hoplight fan it out to eleven platforms. Blocked on maturity, not merit — the repo was one week old at v0.1.x when reviewed. See [research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md](research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md) item 1. [tier: opus]
```

### 2. Amend inbox item 6 (trial methodology audit patterns) — add the dilemma test

Replace the existing `2026-07-25T17:20` line about World-Forge audit
patterns with:

```
- 2026-07-25T17:20: Add the World-Forge audit patterns to the trial methodology: scenario classes, cold-read author/grader separation, counterfactual probe / not-binding verdict, blind-line voice test. Carried from the 2026-07-24 fold-in line, which the blind-trial adoption plan closed without covering these - they are trial-methodology improvements rather than writing doctrine, so folding them in alongside doctrine edits would have mixed two unrelated changes. Source: the World-Forge resource review. Added 2026-07-25 from the Character Builder v3 review: the dilemma test, which is the same family and cheaper than most of the above. Write one scenario putting the character's top value against common decency, then check the note answers it without the author deciding; if the author had to decide, the motive content is underwritten. Second half is the anti-convergence probe: run the same dilemma past the character this one was declared to be built against and confirm the answers differ, not just the accents. See [research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md](research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md) item 3. [tier: opus]
```

### 3. New line — cross-model convergence as a slop signal

```
- 2026-07-25T14:45: Candidate cheap slop metric for the blind-trial kit: generate the same section from two different models and flag sentences they produce identically or near-identically as slop. From a webnovel author's AI writing guide (r/WritingWithAI 1v66q3e), where the rule is that cross-model agreement on a sentence marks it as the model's voice rather than the author's. The rubric at trials/2026-07-writing-doctrine/rubric.md currently scores Slop density by hand against docs/slop-phrases.md, which is the cost inbox item 2 is stalled on; this does not discriminate additive from non-additive doctrine, so it does not unblock that item directly, but it attacks the same cost. Explicitly rejected from the same source: AI detectors (Pangram, GPTZero) — they measure whether prose fools a human-oriented detector, which is irrelevant to a note written for a model to read. See [research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md](research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md) item 2. [tier: sonnet]
```

### 4. New line — character-doctrine candidates from Character Builder v3

```
- 2026-07-25T14:45: Character-doctrine candidates from the Character Builder v3 review, in descending order of confidence. (a) Values carry costs: each top-ranked value carries one sentence of what it has already cost the character or someone else, on the rule that a value never paid for is decoration; pairs with naming the lowest values and one act proving they are not held. Behavioral, stageable, needs no runtime support, and fills a real gap next to our required-contradiction rule. (b) At least one false belief the character holds wrongly and acts on with confidence, extending the knowledge-boundaries rule at framework.md:86, plus a stated in-character way of handling not knowing. (c) Contrast declaration: record which existing character this one is built against and on which axis; nothing in our doctrine currently asks whether two characters in a cast are distinguishable. (d) Charge-scored memory routing: score formative memories by emotional charge and let the score decide which layer they land in, which supplies the missing criterion for the surface/mid/deep classification and closes the open memory-hook tension in the 2026-07-11 reference. (e) State the operating code explicitly in the character's own unlaundered words rather than leaving it implied by behavior. Each needs testing against our own stop-slop and trait-adjective rules before fold-in. See [research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md](research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md) item 3. [tier: opus]
```

### 5. Replaces the withdrawn portrayal-decay line — amend inbox item 4(e)

The portrayal-decay line proposed earlier is withdrawn; reading RoleCDE
showed the decay premise was the community author's extrapolation
rather than the paper's finding. What remains is a doctrine candidate,
so it replaces entry (e) in the character-doctrine line applied above.
Replace `(e) State the operating code explicitly in the character's own
unlaundered words rather than leaving it implied by behavior.` with:

```
(e) Value-conflict stance. RoleCDE (arXiv:2606.01552, ~8k role profiles and ~24k dilemma instances) reports "Role Value Decoupling": agents systematically default to alignment- and morality-consistent decisions rather than role-specific values when the two conflict, even under explicit role conditioning, and the effect is largely invariant to dilemma difficulty. This is a static per-decision bias, not the drift-over-a-session story the source document tells, and our doctrine pre-answers nothing at that collision. Candidate rule: state the operating code in the character's own unlaundered words, declare which way they go when it meets conventional decency (role-following / role-compromise / alignment-compromise / alignment-following), name the specific lever that tips them the other way, and state how guilt shows behaviorally if it shows at all. Caveat carried deliberately: RoleCDE's demonstrated mitigation is fine-tuning, not prompting, so expect a partial effect and treat the rule as something the dilemma test has to verify rather than something assumed to work. The dilemma test routed to the trial-methodology line is exactly that check.
```

### 6. New line — export procedure borrowings from Hoplight

```
- 2026-07-25T15:25: Raise the standard of the ainime export procedure using Hoplight's export room as the model, independent of whether Hoplight is ever adopted as a converter. Our export is an agent hand-assembling world.json from Wide-phase notes with no report and no pre-flight, which is where an unwritten procedure degrades quietly. Six borrowings, all skill prose rather than code. (1) An export report that never omits: every Wide-phase note listed as exported, partially exported, or skipped, with the reason ("The Press never fails silently, and it never lies by omission"). (2) A pre-assembly readiness check: which required ainime fields have no source note, which notes have no target field, reported before assembly rather than after. (3) A per-note field map showing what the target will actually carry, so content that lands nowhere is visible before export. (4) Name what does not fit instead of dropping it — we are one-way so escrow itself does not apply, but their dropped/escrowed/warnings reporting does. (5) A can-this-ever-fire check over loreEntries[] and storyTriggers[], modelled on their dead-entry rule (an entry with no keys, no always-on flag and no by-meaning mode can never trigger); mechanical and testable. (6) A declared cut order for when content exceeds what a field holds, instead of leaving the choice to the agent in the moment — "priority decides who gets evicted and order decides where the survivors land"; Character Builder v3 independently does the same with a numbered compression priority. Mark token estimates with ~ rather than implying precision. Needs a plan before implementation; touches skills/worldbuilder-ainime-export/. See [research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md](research/2026-07-25-resource-review-hoplight-a-webnovel-author-s-ai-writing-guide-and-character-builder-v3.md) item 1. [tier: opus]
```
