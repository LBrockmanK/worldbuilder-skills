# Writing Style

*Shared reference for all Wide phase documents: world notes, character blueprints, story direction, lore notes, event descriptions, calendar.*

These documents are functional specifications for an AI game master. Every sentence should state something that can be acted on. Clarity outranks style in every case.

Prose guidelines for Export phase outputs (character cards, intro text, etc.) live in the export skill, not here.

These rules govern sentence prose. Where a section mandates a format, such as the Background fact pairs or the relationship entry prefix, the format wins and is reproduced exactly as written.

---

## Style Model

Write behavioral descriptions the way a screenplay writes action lines: present tense, only what can be seen or heard in a scene, no internal states or significance announcements, short plain sentences.

**The staging test:** Can a director stage this sentence? If not, rewrite it.

- Fails: "She carries grief she has never articulated."
- Passes: "She changes the subject and starts wiping down the counter."

For vocabulary, apply Orwell's rule from "Politics and the English Language": shortest Anglo-Saxon word that does the job, active voice, cut every word that can go.

---

## Word Choice

### Use the simplest precise word

If a plain word does the job, use it. Don't reach for a longer or more formal word to sound authoritative.

| Avoid | Use instead |
|---|---|
| perceive, observe | see, notice |
| demonstrate | show |
| melancholic | sad |
| contemplative | thoughtful |
| gregarious | outgoing |
| reticent | quiet, guarded |
| reside | live |
| endeavour | try |
| facilitate | help |
| utilize | use |
| exhibits | shows |
| maintains | keeps, has |

When in doubt: would a plain-spoken person use this word in a work meeting? If not, find the word they would.

### Use "is" and "has": avoid copula avoidance

Use "is" and "has" directly. Don't substitute elaborate constructions.

- Wrong: "The settlement serves as a waypoint for traders."
- Right: "The settlement is a waypoint for traders."
- Wrong: "The building boasts three floors and a cellar."
- Right: "The building has three floors and a cellar."

"Serves as," "stands as," "functions as," "boasts," "features" are circumlocutions. The simple verb is clearer.

### No significance inflation

Don't add statements about importance, legacy, or meaning. If something matters, the facts make that clear without announcement.

- Wrong: "The founding betrayal is a pivotal moment that underscores the community's enduring wound."
- Right: "Three families left after the betrayal. The ones who stayed have never discussed it publicly."

"Pivotal," "enduring," "testament," "underscores," "highlights," "reflects broader": cut them. They add length without adding information.

Vague declaratives are the same move in sentence form: "the stakes are high," "the reasons are structural," "the implications are significant." Each one announces that something matters without saying what it is. Cut the sentence and state the fact it was standing in for.

### Cut filler

Delete phrases that announce importance instead of carrying it, and strip adverbs that pad a claim instead of sharpening it.

- Wrong: "It's worth noting that she essentially runs the kitchen."
- Right: "She runs the kitchen."

Cut these groups outright:

- Throat-clearers: "here's the thing," "it's worth noting," "the truth is," "let me be clear."
- Emphasis crutches: "full stop," "make no mistake," "let that sink in," "I promise."
- Jargon standing in for a plain verb: "navigate," "unpack," "lean into," "deep dive," "circle back."
- Adverbs of degree: "really," "just," "genuinely," "truly," "deeply," "actually," "simply," "honestly."

- Wrong: "She genuinely just wants to help, honestly."
- Right: "She wants to help."

---

## Sentence Structure

### Write positive statements

State what something IS. Don't open with "not X."

- Wrong: "She is not warm or friendly at first."
- Right: "She is guarded with strangers. She is watchful, brief, slow to smile."

Negative constructions give the AI one mode (avoidance) instead of something to generate from. Positive statements give behavioral texture.

### Prefer verbs over nominalizations

Keep actions as verbs. Don't convert them into nouns.

- Wrong: "The implementation of the change resulted in a reduction in complaints."
- Right: "The change cut complaints."

### Keep sentences short enough to parse on first read

One idea per sentence when ideas are distinct. If a sentence has two clauses, check whether the second earns its place or whether it reads cleaner on its own.

### No em-dashes

Em-dashes are not used in spec documents. Use periods instead. When two thoughts are joined by an em-dash, split them into two sentences.

**Hedging clause pattern:**

- Wrong: "She is guarded with strangers — watchful, brief, slow to smile — and opens up only when she feels safe."
- Right: "She is guarded with strangers. She is watchful, brief, slow to smile. She opens up only when she feels safe."

**Mid-sentence interruption pattern:**

- Wrong: "He runs the market — has for twenty years — and knows every trader by name."
- Right: "He has run the market for twenty years. He knows every trader by name."

### Numbers as numerals

Write 27, not twenty-seven. Write day 8, not the eighth day.

---

## Content Standards

### Describe behavior, not labels

Name what something *does*, not what it *is* in the abstract.

- Label: "She tends to be evasive."
- Behavior: "She deflects personal questions by turning them back on the asker."

Labels give the AI a category to file under. Behaviors give it something to enact.

**Heavy trait adjectives are banned outright.** "Intelligent," "analytical," "arrogant," "dominant," "majestic," "bustling," and words of that weight may not appear anywhere in a note. One of them outvotes a page of behavioral description and pulls the subject toward the stock type welded to that word. A softer adjective is not the fix. Replace the label with the behavior that earned it. Where the trait is a competence, name three things: the domain the subject is competent in, the drive behind that competence, and a cost or flaw the competence produces. Where it is not a competence, write what happens that makes people reach for the word, and what it costs.

### Make claims verifiable or behavioral

A spec claim should be something that can be checked against the world or enacted in a scene. Abstract claims are weak. Concrete claims are strong.

- Weak: "The region has a troubled history."
- Strong: "Three of the four founding families lost someone in the flood of Year 12."

Ask: what would the AI do differently in a scene because of this statement? If the answer is "nothing specific," the statement is probably too abstract.

### Decide what not to specify

For each detail, ask whether it changes behavior. Specify the details that lock behavior and leave the rest unwritten. This governs which facts you decline to write at all, which is a different question from what you commit to when you do write one.

- Wrong: "The house was pale green with a red door on the third street past the mill, and the family kept a gray cart horse named Birch." None of it changes how anyone behaves.
- Right: "The house was cramped and the walls were thin." That fact alone explains why she can't sleep with a door closed.

### No flair

Metaphor, evocative language, and atmospheric color belong in prose outputs. In spec documents they are noise. State the thing directly.

- Wrong: "Her silence stretches like frost across the room."
- Right: "She goes quiet when this subject comes up and doesn't re-engage until it passes."

### No -ing padding

Don't tack present participle phrases onto sentences to add apparent depth.

- Wrong: "He keeps to himself, reflecting his distrust of outsiders and underscoring the community's broader insularity."
- Right: "He keeps to himself. He doesn't trust outsiders. Most of the community is the same way."

Each thought is its own sentence.

### Single source of truth

Each fact lives in one place. Other documents reference it by naming it, not by restating it.

Don't describe a character in a location note because they're connected to that location. Name the connection; keep the description in the character's own document. Don't paraphrase what another note says. Link to it by name.

### Don't describe one entity in another entity's document

A character note describes that character's experience. A location note describes the location. A relationship entry describes what *this* character feels, thinks, and does. It is not a description of the other party.

- Wrong (in Mira's notes): "Jonas is a quiet, solitary man who keeps to himself."
- Right (in Mira's notes): "She trusts Jonas more than she admits, and resents that she does."

The description of Jonas belongs in Jonas's own notes.

---

## Structure

Structure is expected in spec documents. Use headers, bullets, and tables where they help clarity and scanning. Don't use them decoratively.

Use bullets for discrete parallel items. Use prose for reasoning, relationships, or anything where the connection between ideas matters.

---

## Four Failure Modes

Check for all four before finalizing any document.

**1. Latinate or formal vocabulary.**
Scan for -tion, -ity, -ence, -ance endings and formal synonyms. Replace with plain equivalents.

**2. Negative constructions.**
Search for "not," "never," "without," "lacks," "no X" in descriptions. Rewrite as positive behavioral statements.

**3. Labels without behaviors.**
Any word or phrase that names a quality without showing how it manifests. What does the character *do* because they are "ambitious"? That's the statement worth keeping.

**4. Literary flair.**
Metaphor, atmospheric construction, or evocative phrasing in a spec context. Say the thing directly.

For a phrase-level review checklist of known slop patterns, see `docs/slop-phrases.md` at the plugin root (review reference, not skill instruction).
