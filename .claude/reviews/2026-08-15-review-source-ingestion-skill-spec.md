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

