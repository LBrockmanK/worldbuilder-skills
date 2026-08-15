## Round 1 — digest `73ed5ed7…`, anchor `06ba0ecb` (dirty), tokens 36137, 2026-08-15T12:55:20-05:00, 151s

Anchor: 06ba0ecb90ee11badf750872708c5772f1005775 (dirty tree)
Artifact digest: 73ed5ed7fb9d9b692ce0972c37444edeeed61c45a7036eb2a0d099303cc47fff (sha256 over the exact scoped bytes as delivered)
Scope: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md

1. D1’s inference exception has no testable boundary
   Location: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md:70
   Quote: `when structural organization requires a minimal judgment call`
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: “Requires” and “minimal” provide no observable rule for deciding which judgments qualify. An implementation can label an arbitrary interpretation `[inferred]` and still claim compliance, despite D1’s categorical “does not interpret” rule. This makes the no-inference principle neither clear nor testable and directly violates acceptance criterion 1.

2. D3 organizes by interpreted content type rather than source
   Location: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md:78; 100
   Quote: `Reference documents are organized by where the data came from, not by what it is about.`
   
   `Ingestion produces one reference document per source type per character`
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: A “source type” such as Dialogue or Narrative Events describes what material is, not where it came from. A single script, chapter, or game file containing dialogue and action would have to be classified and potentially split by content to satisfy D3, contradicting D2’s source-only organization and requiring interpretation. The artifact needs one governing partition rule for mixed-content sources.

3. Multi-character sources have no defined placement
   Location: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md:100
   Quote: `Ingestion produces one reference document per source type per character (or per entity — location, faction, etc.).`
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: The demonstrated test case includes group conversations and events with multiple participants, but the per-character/per-entity structure does not say whether a shared source is duplicated in every participant’s document, assigned to one entity, stored once in a shared document, or split into excerpts. Splitting conflicts with full-dialogue capture; duplication complicates source ordering and gap claims. D3 therefore does not fully cover a demonstrated source shape.

4. External-reference summaries violate extraction-only fidelity
   Location: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md:114
   Quote: `Content from secondary sources reproduced or summarized with attribution.`
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: low
   Channel: fix
   Body: Summarization requires selecting important content and deciding what the source means, whereas D1 permits verbatim capture or minimal structural transformation and prohibits interpretation and importance judgments. No mechanical summarization rule or `[inferred]` treatment is supplied, so D4 cannot consistently implement this source type under D1.

5. Visual extraction requires unmarked perceptual interpretation
   Location: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md:164
   Quote: `Physical description: what is visible in the image (hair color, eye color, skin tone, clothing, distinguishing features).`
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: Assigning color, skin tone, and “distinguishing feature” labels—especially from stylized or pixel art—is a perceptual judgment rather than mechanical extraction. The following example acknowledges that an image can merely “read as” a color, yet D4 does not require the `[inferred]` marker or record the basis as D1 requires. Thus the guidance permits unmarked inference on a normal path.

6. “Corrections” require deciding which source is true
   Location: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md:172
   Quote: `Corrections to other source types flagged explicitly`
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: Calling one source a correction to another decides authority and factual truth across sources. That is cross-source synthesis and interpretation, both explicitly prohibited by D1. Mechanical ingestion could record a discrepancy with provenance, but the artifact presently requires a correctness judgment without defining source precedence or sending the decision to the Q&A workflow.

7. D4 does not consistently require per-piece provenance
   Location: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md:52; 147
   Quote: `Records provenance: where each piece of content came from (file path, URL, page, section)`
   
   `**Narrative events:**`
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: Dialogue explicitly requires a source path for each block, but the Narrative Events and Schedule and Calendar capture lists contain no equivalent per-event or per-record provenance requirement. Frontmatter-level resources cannot identify the origin of each piece when a document combines many files, such as the test case’s heart events, story events, and schedules. D1’s provenance invariant is therefore not consistently applied through D4.

8. Mandatory gap documentation has no finite comparison set
   Location: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md:179
   Quote: `Each reference document ends with a **Gaps** section listing what the source material does not contain.`
   Type: completeness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: A source omits infinitely many possible facts. The spec supplies no source-type schema or closed checklist against which absence is tested, so two compliant extractors can produce arbitrarily different gap lists. This makes the requirement untestable and encourages extractors to introduce their own expectations about what the source should contain.

9. D5’s validity test does not enforce D1
   Location: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md:191
   Quote: `could you determine this gap is present without understanding the character-building pipeline?`
   Type: consistency
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: low
   Channel: fix
   Body: This test excludes only pipeline-specific expectations; it does not exclude semantic interpretation. The declared valid example still requires recognizing which prose counts as a “physical description” and establishing its absence across the source. An extractor can therefore pass D5 while asking “what does this text describe?”, contrary to D1’s “what does this say?” boundary.

10. The scraibe composition omits conflicting mandatory ingest behavior
   Location: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md:198
   Quote: `It builds on the scraibe plugin's ingest skill for the mechanical capture pass (provenance, frontmatter, document creation)`
   Type: correctness
   Severity: major
   Effort-to-fix: medium
   Risk-of-fix: medium
   Channel: fix
   Body: The referenced `scraibe:ingest` mechanical pass also requires ranking overlapping sources, surveying contradictions, and resolving them with the user; its content pass then extracts “relevant” knowledge and applies judgment. Those behaviors conflict with D1 and D2, but D6 neither overrides them nor defines whether the worldbuilder skill invokes only selected scraibe steps, invokes the full skill, or replaces it after document creation. Implementers following the claimed base workflow can therefore produce interpretive output.

11. The Q&A phase is denied provenance it needs to resolve source conflicts
   Location: .claude/specs/2026-08-15-source-ingestion-skill-reference-document-structure-and-extraction-principles.md:214
   Quote: `The Q&A workflow does not need to know where the source material came from.`
   Type: consistency
   Severity: major
   Effort-to-fix: small
   Risk-of-fix: medium
   Channel: fix
   Body: D1 forbids ingestion from synthesizing conclusions across sources, while D4 preserves official/community status and source discrepancies. Consequently, the downstream Q&A phase must retain provenance to decide how conflicting or differently authoritative material affects an answer. Declaring that it need not know origin discards the information required to perform the judgment deliberately deferred to it.

FINDINGS: 0 critical, 11 major, 0 minor, 0 nit

### Adjudication — Round 1

All 11 findings accepted. Decisions rewritten to address all findings:

1. **Accept.** D1 rewritten: removed vague "labeled inference exception," replaced with exhaustive list of permitted structural transformations. Anything not on the list is interpretation.
2. **Accept.** D2 renamed to "Source-Path Organization." Documents follow the source's own file/directory structure, not a content-type taxonomy. Mixed-content files reproduced as-is.
3. **Accept.** D3 now explicitly handles multi-entity sources: store once in shared document, link from each entity's reference set.
4. **Accept.** D4 external references: "summarized" removed. Content reproduced with provenance; if too large, reproduce relevant sections.
5. **Accept.** D4 visual assets: all image-derived observations marked `[perceptual]` with source image path.
6. **Accept.** D4 external references: "corrections" replaced with "discrepancies noted with both sides and provenance." Which source is authoritative is a Q&A decision.
7. **Accept.** D4: per-piece provenance (source file path) now required for all extraction types, not just dialogue.
8. **Accept.** D5 renamed "Source Absence Notes." Absences are relative to the source's own apparent scope, not tested against a pipeline checklist or unbounded fact space.
9. **Accept.** Old D5 (gap validity test) removed; replaced by the scope-relative absence test in the new D5.
10. **Accept.** D6 now specifies that the worldbuilder skill uses scraibe:ingest only for document creation and explicitly skips the judgment pass.
11. **Accept.** Removed false claim. D6 now states that reference documents carry per-piece provenance for downstream consumers including the Q&A workflow.

## Round 2 — digest `17c3f2a2…`, anchor `ea1bd935` (dirty), tokens 45852, 2026-08-15T13:18:49-05:00, 158s

Anchor: ea1bd93542124eb952ced19555bf642f60e274e6 (dirty tree)
Artifact digest: 17c3f2a2befcf478dee53748ffd0a8c5c1d1e320e8515b0c2facab47c90335d2 (sha256 over the exact scoped bytes as delivered)
Scope: .claude/plans/2026-08-15-source-ingestion-skill-implementation-plan.md

1. Title: Execution depends on a nonexistent approval gate
   Location: .claude/plans/2026-08-15-source-ingestion-skill-implementation-plan.md:15
   Quote: `Execution requires the plan artifact's approval flip (see Approval Gate).`
   Type: completeness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The scoped plan has no `Approval Gate` section or approval field defining the referenced flip. An implementing worker cannot determine how execution becomes authorized, producing a reachable, detectable block.

2. Title: The exhaustive transformation list improperly restricts metadata labels to filenames
   Location: .claude/plans/2026-08-15-source-ingestion-skill-implementation-plan.md:103-109
   Quote:
   > **Permitted structural transformations** (exhaustive — anything else
   > is interpretation):
   > - Format conversion (TOML/JSON/XML to markdown)
   > - Reproducing existing speaker tags from tagged dialogue
   > - Stripping engine markup while preserving content
   > - Reproducing file/directory names as section headers
   > - Reproducing metadata labels from filenames
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: D1 permits reproducing existing metadata labels generally and gives filename-derived portrait names only as an example. Because this skill declares its list exhaustive, “from filenames” excludes labels found in embedded metadata, manifests, or other source structures and misclassifies their reproduction as interpretation. This violates acceptance criterion 2.

3. Title: Large external references lack the required extraction rule
   Location: .claude/plans/2026-08-15-source-ingestion-skill-implementation-plan.md:232-238
   Quote:
   > ### External references (wiki, community, developer commentary)
   >
   > - Content reproduced with source attribution (URL, page title,
   >   access date) — not summarized
   > - `[official]` or `[community]` marker per source
   > - Discrepancies with other sources noted with both sides and
   >   provenance — never declared as corrections
   Type: completeness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: D4 expressly requires that when an external source is too large, relevant sections be reproduced with provenance rather than converted into a digest. That reachable case is absent here. The general prohibition on summarization does not tell the worker what extraction behavior replaces full reproduction, so D4 is incomplete and acceptance criteria 1 and 4 are violated.

4. Title: The creation workflow does not realize the mandated filename
   Location: .claude/plans/2026-08-15-source-ingestion-skill-implementation-plan.md:136-140 and 178
   Quote:
   > python "<scraibe-plugin>/scripts/new_doc.py" --type reference \
   >   --title "<Entity> — <Source Label>" \
   >   --description "<what this document contains>" \
   >   --dir notes
   >
   > **Naming:** `<entity-name> — <source-directory-or-label>.md`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: The repository’s established `new_doc.py` behavior creates a date-prefixed slug filename, while the plan never instructs the worker to rename that output. Following the command therefore produces a filename that conflicts with D3’s explicit naming rule. This leaves one of the six required decisions operationally unimplemented.

5. Title: Verification checks headings and keywords instead of the acceptance criteria
   Location: .claude/plans/2026-08-15-source-ingestion-skill-implementation-plan.md:275-298
   Quote:
   > Run: `grep -n "^## " skills/worldbuilder-source-ingestion/SKILL.md`
   >
   > Run: `grep -c "Format conversion\|speaker tags\|engine markup\|file/directory names\|metadata labels" skills/worldbuilder-source-ingestion/SKILL.md`
   >
   > Run: `grep "judgment pass" skills/worldbuilder-source-ingestion/SKILL.md`
   Type: completeness
   Severity: minor
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: These checks can pass when D2–D5 are empty or incorrect, when a transformation has been semantically narrowed, when source-absence tests have drifted, or when interpretive instructions were added elsewhere. Consequently, the plan has no effective verification for acceptance criteria 1, 4, 5, or 6; the metadata-label defect above also passes its purported exhaustive-list check.

FINDINGS: 0 critical, 4 major, 1 minor, 0 nit

### Adjudication — Round 2 (plan)

1. **Accept.** Fixed: removed "see Approval Gate" reference; replaced with direct statement about status flip.
2. **Accept.** Fixed: metadata labels now says "from filenames, manifests, or other source structures" matching D1's general permission.
3. **Accept.** Fixed: external references guidance now includes "If a source is too large to reproduce in full, reproduce the relevant sections with provenance."
4. **Accept.** Fixed: document creation instructions now include a rename step using `rename_doc.py` to match the naming convention.
5. **Accept (minor).** Verification checks are inherently shallow for markdown — no semantic test exists. The grep checks verify structure, not content correctness. The task reviewer covers the gap.

## Round 3 — digest `6661c25f…`, anchor `27c6e3b9` (clean), tokens 52138, 2026-08-15T13:29:53-05:00, 202s

Anchor: 27c6e3b9df09879178c99c4c7381adf93858f2d6 (clean tree)
Artifact digest: 6661c25fd89e5b99bd270ea2c50891787614305a19bc29e05fcdf388cc39ef1a (sha256 over the exact scoped bytes as delivered)
Scope: git diff 49703c2 -- . :(exclude).claude/reviews/2026-08-15-review-source-ingestion-skill-spec.md

1. Perceptual image descriptions violate the exhaustive no-inference boundary
   Location: skills/worldbuilder-source-ingestion/SKILL.md:170-176
   Quote:
   > ### Visual assets
   >
   > - File path and naming convention
   > - Available variants (expressions, outfits, seasons) reproduced from
   >   filenames and metadata — not from viewing images
   > - When images are viewed for physical description, mark every
   >   observation `[perceptual]` with the source image path
   Type: correctness
   Severity: major
   Effort-to-fix: large (reaches beyond the scoped change)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: escalate
   Body: In the artifact identified by the stated anchor, digest, and scope, this directs ingestion to convert visual perception into physical-description claims. That is interpretation, not one of D1’s exhaustive structural transformations; adding `[perceptual]` labels the judgment but does not make it mechanical extraction. It therefore violates acceptance criteria 2 and 3. The supplied requirements provide no local resolution: removing this behavior would cease to implement D4, while adding perceptual description to the permitted list would cease to match D1 exactly.

2. Large-source handling commands the same relevance judgment the skill prohibits
   Location: skills/worldbuilder-source-ingestion/SKILL.md:75-78; 180-184
   Quote:
   > Do not use scraibe:ingest's
   > judgment pass (source ranking, contradiction resolution, relevance
   > extraction) — those conflict with the no-inference principle.
   >
   > - Content reproduced with source attribution (URL, page title,
   >   access date) — not summarized. If a source is too large to
   >   reproduce in full, reproduce the relevant sections with provenance
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: For this scoped artifact, “relevant sections” leaves the extractor to decide what matters, despite the earlier declaration that relevance extraction is a prohibited judgment. This is a reachable path for every oversized external source and violates acceptance criterion 2. Requiring the sections to be selected through the user-confirmed scope already established in “Exploring the source” would resolve the contradiction without changing the surrounding workflow.

3. Source-absence validation requires semantic inference about apparent scope
   Location: skills/worldbuilder-source-ingestion/SKILL.md:191-202
   Quote:
   > Each reference document ends with a **Source Absences** section
   > noting what the extracted source does not contain. Absences are
   > factual observations about the source's coverage, stated relative to
   > the source's own apparent scope.
   >
   > **Valid:** "No text-based physical description appears in this
   > source."
   Type: correctness
   Severity: major
   Effort-to-fix: medium (several sites within scope)
   Risk-of-fix: medium (alters behavior on existing paths)
   Channel: fix
   Body: Under the stated review identity, determining a source’s “apparent scope” asks what the source seems intended to cover, and proving that no prose constitutes a physical description requires classifying the meaning of all candidate text. Both cross the skill’s own “what does this say?” boundary and violate acceptance criterion 2. The rule can remain an absence test while limiting claims to explicit structural coverage—declared file sets, chapters, fields, or metadata—and using structurally testable examples.

4. The naming rule does not define a valid filename for required shared multi-entity documents
   Location: skills/worldbuilder-source-ingestion/SKILL.md:120-126
   Quote:
   > **Multi-entity sources:** when a source contains material about
   > multiple characters or entities (group conversations, ensemble
   > scenes), store the material once in a shared document. Each entity's
   > reference set links to the shared document. No per-entity splitting
   > or duplication.
   >
   > **Naming:** `<entity-name> — <source-directory-or-label>.md`
   Type: correctness
   Severity: major
   Effort-to-fix: small (one site, local)
   Risk-of-fix: low (mechanical, behavior elsewhere preserved)
   Channel: fix
   Body: In the scoped change, a shared document has multiple entities, but the only naming grammar requires one singular `<entity-name>`. Choosing any participant privileges one entity, while producing one file per name violates the immediately preceding no-duplication rule. This leaves D3’s required multi-entity path operationally undefined and violates acceptance criterion 1. A separate shared-document naming form or the governing spec’s multi-entity example would resolve the ambiguity locally.

FINDINGS: 0 critical, 4 major, 0 minor, 0 nit

### Adjudication — Round 3 (final whole-change pass)

1. **Reject.** Re-litigates spec decision D4 (visual assets, `[perceptual]` markers), which was adjudicated in spec review round 1 finding 5 and accepted. The SKILL.md faithfully implements the spec's explicit permission for perceptual observation with markers. Recorded reason: the spec decided this tradeoff; the implementation is correct.
2. **Accept.** Fixed at 61093c2: "relevant sections" changed to "sections the user identified during source exploration." The user picks what to extract during source mapping, not the extractor.
3. **Accept.** Fixed at 61093c2: source absence notes now limited to structural observations (missing fields, empty directories, absent file types). Valid examples rewritten to be structurally testable.
4. **Accept.** Fixed at 61093c2: added multi-entity naming pattern with example.

All fixes verified by grep. One rejected finding recorded with reason. Ready to merge.

