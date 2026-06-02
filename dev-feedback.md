# Worldbuilder Skills — Development Feedback Log

Issues and suggestions surfaced during real sessions. Intended for the next skill revision pass.

---

## User Info

### Missing: README at repo root

**Date:** 2026-05-31
**Note:** No README.md exists at the repo root. Future users need info and instructions on the tool.

---

## worldbuilder-character

### Anti-pattern: vague meta-commentary in soul/behavioral sections

**Date:** 2026-06-01
**Source:** Vesper (Viralys) session
**Problem:** Phrases like "she hasn't examined this", "she has never named to herself", "runs just below conscious examination" describe what a character *doesn't do* rather than stating the fact directly. These give the LLM nothing to act on and read as hedged narration rather than behavioral specification. The skill's existing guidance ("Write what characters ARE, not what they aren't") covers the principle but the soul section in particular invites this pattern because it deals with things characters suppress or avoid. Good examples of direct alternatives are not yet identified — needs further development.
**Fix needed:** An explicit list of banned phrase patterns in the soul section guidance, with verified direct alternatives.

### Missing: skill must explicitly instruct capturing off-blueprint character decisions

**Date:** 2026-06-01
**Source:** Viralys session, multiple characters
**Problem:** During any character blueprint session, decisions get made about characters who are not the current subject. These decisions — a behavioral detail about Liza, a relationship note about Mairwyn, a friendship note about Maja — will influence those characters' future blueprints. They currently have no home except chat history, which is unreliable.
**Fix needed:** The worldbuilder-character skill (and possibly worldbuilder-world-planning) should include an explicit instruction: before moving to a new character, scan the session for any decisions made about characters without their own note and record them in the relevant cast plan entry. The cast plan entry format should have a standard "Blueprint note (from [source] session):" field so these are clearly flagged as pre-blueprint decisions requiring integration when that character's note is written. This is a skill-level fix — the instruction must live in the skill, not in memory or preference.

**Addendum — tension with "focus on your own perspective" guidance:**
The existing relationships guidance correctly states that each relationship entry should describe the current character's experience of the other person, not the other person's thoughts or worldview. This rule can create a false impression that insights about the other character should simply be discarded. They should not. The two rules operate at different levels:
- The relationship entry stays perspective-focused (unchanged).
- Any insight about the other character derived during that process — whether implicit in the dynamic described or explicitly noted — gets recorded in that character's cast plan entry immediately, as a blueprint note.
Both rules hold simultaneously. The skill should state this explicitly so that "focus on your own perspective" is never used as justification for losing information about another character.

### Skills must be freshly invoked before any note write or edit, not just at session start

**Date:** 2026-06-01
**Source:** Sophie (Viralys) session — context window degradation
**Problem:** Skill sub-files (framework.md, relationships.md, etc.) were loaded at the start of the session. By the time later characters were being written, the guidance had been pushed out of active context by accumulated session work. The writing quality degraded in specific ways that exactly matched loss of the behavioral specificity guidance: vague meta-commentary, unfocused relationship entries, and loss of the When/Behavior/Because discipline.
**Fix needed:** The skill should include an explicit instruction: re-invoke the skill and read all referenced sub-files at the start of any work on a character note, whether that is an initial write or a later edit. Skills should not be assumed to remain in context across a long session. This instruction belongs in the skill itself as a pre-work checklist step, not just as a session-start instruction.

### Anti-pattern: attributing internal perceptions to the wrong character in relationship entries

**Date:** 2026-06-01
**Source:** Sophie/Vesper sync pass (Viralys)
**Problem:** Relationship entries in character notes will sometimes state how the *other* character internally interprets events — e.g., "Sophie pushes back and Vesper hears it as normal grousing" appearing in Sophie's note. This violates the core rule that each entry describes only what *this* character experiences. The other character's internal interpretation is not observable and does not belong in the entry.
**Fix needed:** Add an explicit check to the relationship writing guidance: scan each entry for statements about the other character's internal state (thoughts, interpretations, feelings). If found, move them to that character's note. What the current character can legitimately describe is behavior they observe ("Vesper continues") — not the interpretation behind it ("Vesper hears it as grousing").

### Anti-pattern: "reads" as shorthand for character interpretation

**Date:** 2026-06-01
**Source:** Sophie (Viralys) session
**Problem:** AI defaults to "she reads this as..." or "he reads the situation as..." when describing how a character interprets something. This phrasing is not natural in speech or prose. It sounds like literary criticism rather than characterization.
**Fix needed:** Flag "reads" in this sense as a banned construction. Natural alternatives: "sees", "takes", "interprets", "understands", "takes this to mean". Add to any style guidance in the skill.

### Suggestion: test caveman mode for environment sections

**Date:** 2026-06-01
**Note:** Environment sections in particular tend toward overwriting. Try applying the caveman mode skill to environment writing in a future session and evaluate the result. Do not apply during current session.

### Concept / Inspirations / Design Notes need cleaner organization

**Date:** 2026-06-01
**Source:** Sophie (Viralys) session
**Problem:** The three header sections (Concept, Inspirations, Design Notes) have overlapping purposes and Inspirations in particular is being misused as a duplicate of Concept or Design Notes. Inspirations should contain only specific real-world or fictional references that shaped the design — not character summaries, not rephrasings of concept, not meta-commentary. Currently it gets filled with character description when the writer has no strong external references.
**Fix needed:** Clarify definitions in the skill. Concept = narrative function and unique setting contribution. Inspirations = named external references with specific notes on what was drawn from each; explicitly optional and should be left blank rather than filled with generic character summary. Design Notes = meta-commentary for builders, excluded from all exports. Consider merging these under one heading with clear labeled subsections to reduce confusion.

### AI overemphasis on what is unsaid, undone, avoided

**Date:** 2026-06-01
**Source:** Sophie (Viralys) session
**Problem:** Consistent pattern across soul, relationships, and relationship behavior sections: focus on what characters don't say, don't do, haven't examined, keep below the surface. This produces vague, non-actionable content and hedged prose. The behavioral description format (When/Behavior/Because) counteracts this effectively by forcing active behavioral specification.
**Fix needed:** Consider applying the When/Behavior/Because format more broadly — especially to soul and relationship entries, where the problem is most common. Gaps and silences can be good content, but only when there is active behavioral content for them to exist between. This is a significant rethink of the blueprinting process and should be developed carefully before implementing.

### Overuse of em-dashes

**Date:** 2026-06-01
**Source:** Vesper and Sophie (Viralys) session
**Problem:** Consistent overuse of em-dashes throughout character notes, producing choppy prose and a feeling of hedged qualification. 
**Fix needed:** Style guidance should explicitly flag and limit em-dash use. Prefer period-separated sentences.

### Redundancy between sections

**Date:** 2026-06-01
**Source:** Sophie (Viralys) session
**Problem:** Consistent redundancy and overlap between Soul, Behavioral Descriptions, Relationships, and Relationship Behavior. The same information appears in multiple places. When one section is updated and others aren't, inconsistencies will accumulate. The goal should be one source of truth: each piece of information lives in exactly one section.
**Fix needed:** Audit section purposes to eliminate overlap. One proposed direction: remove Behavioral Descriptions as a standalone section and apply its When/Behavior/Because format to Soul and Relationship entries directly. This may improve quality while reducing redundancy. Requires careful rethinking — do not implement until tested.

### Archetype and Role fields should not be in frontmatter

**Date:** 2026-06-01
**Source:** Sophie (Viralys) session
**Problem:** Archetype and Role are not universally used fields and clutter frontmatter. They are better surfaced in the header section immediately below frontmatter, where they are easy for both humans and AI to find when skimming.
**Fix needed:** Move both fields to the header section just below frontmatter. Related questions to resolve: Are notes set up so the AI properly reads the header? Can Obsidian Bases be configured to display the header? If not, reconsider whether these should be frontmatter fields after all.

### Relationship archetype goal is variety, not labeling

**Date:** 2026-06-01
**Source:** Sophie (Viralys) session
**Problem:** Relationship archetypes are being used as the closest available label for each relationship rather than as tools for ensuring behavioral variety across the relationship set. Community Thread in particular is easy to overuse because it fits almost any low-intensity relationship. Unease was applied to nearly half of Sophie's relationships in first draft.
**Fix needed:** The skill should emphasize that the goal is a varied set of archetypes covering different behavioral modes. Each archetype should appear at most once or twice per character. Community Thread should be a last resort. If you find yourself applying the same archetype repeatedly, that is a signal to look for a more specific framing.

### Each character should have at least one out-group relationship

**Date:** 2026-06-01
**Source:** Sophie (Viralys) session
**Note:** In settings with strong social divides, the within-group relationship weighting guidance can be taken too far. Each character should have at least one named relationship that crosses their primary social boundary. This keeps the cast's social web connected and prevents character notes from existing in isolation.

### Appearance section is ainime-export-specific; remove from blueprint

**Date:** 2026-06-01
**Source:** Sophie (Viralys) session
**Problem:** The standalone Appearance section at the end of character notes duplicates content from Body (Foundation). It is a leftover from ainime export card formatting, not a blueprint requirement.
**Fix needed:** Remove the Appearance section from the character blueprint structure. Appearance information belongs in Body. The export skill will derive it from there.

### Storylines belong in story notes, not character notes

**Date:** 2026-06-01
**Source:** Sophie (Viralys) session
**Problem:** The Storylines section places story arc content inside the character note, where it will drift out of sync as the world develops.
**Fix needed:** Remove Storylines from the character blueprint. Each storyline should be a separate story note (type: story, scope: [[character name]]) with a link back to the character note. The character blueprint skill should instruct writers to create story notes rather than a Storylines section.

---

## General / Cross-skill

### Documentation maintenance belongs in CLAUDE.md, not skill instructions

**Date:** 2026-06-01
**Source:** Viralys session general
**Problem:** During a character blueprint session, significant decisions get made about characters who aren't the current subject. If these aren't written down immediately, they live only in chat history and are effectively lost. This is not a skill-specific problem — it applies to any multi-session creative project regardless of which skill pipeline is in use.
**Not a skill fix:** Skills define how and where information is stored. The instruction to capture decisions in real time and keep project files current belongs in CLAUDE.md as a general working principle, so it applies across all projects and all skills.
**Action needed:** Add to CLAUDE.md in a dedicated session — do not edit piecemeal between projects.
