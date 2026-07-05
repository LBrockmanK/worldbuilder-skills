---
type: adr
title: Screenwriting action-line convention as primary writing style model
description: Decision to adopt the screenwriting action-line convention as the primary style model for behavioral descriptions, with Orwell's rules retained as a vocabulary co-anchor.
tags: [complete]
date: 2026-06-15
timestamp: 2026-06-15T17:10
resources: []
---
# Screenwriting action-line convention as primary writing style model

Behavioral descriptions in Wide phase documents are written using the screenwriting action-line convention as the primary style model: present tense, only what can be seen or heard, no internal states, no significance announcements, short plain sentences.

The decision came out of a systematic research pass on the AI writing quality problem. The core finding was that rule-enumeration (slop-phrase blacklists, vocabulary tables) fails because the instruction-tuned model generates new slop as fast as rules ban old forms. A named positive model well-represented in training data is more durable than any rule list.

The action-line convention was selected over the alternatives because it is the only candidate that makes behavioral concreteness its defining structural constraint rather than an add-on. Action lines forbid internal states by definition — characters are shown through observable action. This directly addresses vague interiority, the hardest and most persistent failure mode. Orwell addresses vocabulary but not behavioral concreteness. Hemingway produces atmospheric, melodramatic output when used as a "write like X" prompt. Behavioral psychology operational definitions are a better structural match but are low-salience in training data and invoke inconsistently.

George Orwell's rules from "Politics and the English Language" are retained as a vocabulary co-anchor: shortest Anglo-Saxon word that does the job, active voice, cut every unnecessary word.

## Implications

- Soul, Body, and Relationship entries are subject to the staging test: can a director stage this sentence? If not, rewrite it.
- The Because clause earns a limited exemption from the staging test. It may name an internal state if the state is specific enough to act on.
- "Write like X" alone is insufficient — PNAS (2025) evidence shows the instruction-tuned Latinate register persists through style-imitation prompts. The named model is the spine; few-shot exemplars are the correct suppressor of residual vocabulary. Exemplars are deferred.

## Considered options

**George Orwell as primary:** Excellent vocabulary anchor; the essay is highly salient in training data. Rejected as primary because Orwell's rules address word choice and sentence length but say nothing about converting interior states into observable behavior — the most persistent failure mode.

**Hemingway as primary:** High salience, plain vocabulary, short sentences. Rejected because the iceberg theory (deliberate omission of meaning) is wrong for specification writing, and empirically, "write like Hemingway" prompts produce atmospheric output ("The breach came quietly, like the fall of night") rather than suppressing flair.

**Behavioral psychology operational definitions as primary:** Best structural match for the interiority problem. Rejected because low training-data salience makes "write like an ABA operational definition" invoke inconsistently compared to the screenwriting convention.
