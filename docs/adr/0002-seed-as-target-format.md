# ~~Seed document uses target system field format from day one~~

> **Superseded by ADR-0003 (platform decoupling).** The seed document no longer writes ainime-games field names. Seed phase output is platform-agnostic markdown (`seed.md`). The ainime export skill handles field mapping.

---

The seed document is a direct draft of the target system's Setting fields, written in final format from the start of Phase 1. The alternative — an intermediate artifact in a free-form notes format that gets compiled into target format at the end — was rejected because it creates a translation step that adds friction without adding value. Every refinement session advances the actual deliverable rather than an intermediate that has to be converted later. The seed is explicitly framed as a starting point ("seed," not "summary") so users understand the world will grow beyond it — the format commitment does not imply the content is frozen.
