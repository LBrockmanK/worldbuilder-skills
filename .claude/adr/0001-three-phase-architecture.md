---
type: adr
title: Three-phase workflow architecture
description: Decision to structure world builder sessions as three sequential phases (Seed, Wide, Export) so every domain is worked broadly before any is finalized.
tags: [complete]
date: 2026-06-15
timestamp: 2026-06-15T17:10
resources: []
---
# Three-phase workflow architecture

World builder sessions follow three sequential phases: Seed → Wide → Export. The alternative — linear document-by-document production (lorebook, then calendar, then characters in sequence) — was rejected because it produces orphaned documents. Characters who don't exist yet can't anchor festival events; locations written before the cast exists don't reflect who actually lives in them. The three-phase structure ensures every domain is worked broadly before any domain is finalized, so documents can inform each other before being locked down.

## Considered Options

**Linear per-domain production**: Write each document type to completion before starting the next. Simpler to understand but creates ordering dependencies — the first documents can't account for decisions made in later ones.

**User-directed navigation**: No enforced order; the user invokes whichever skill they need. Rejected because most users won't know which skill to invoke or what order makes sense.
