---
type: reference
title: Family — Marriage and Children
description: 'Broad-strokes extraction of spouse.toml and children.toml: marriage
  mechanics, spouse behavior, and child NPC system. No-inference extraction.'
tags:
- human-ready
date: 2026-08-15
timestamp: 2026-08-15T23:19Z
resources:
- projects/fields-of-mistria/source/fiddle/spouse.toml
- projects/fields-of-mistria/source/fiddle/children.toml
---

# Family — Marriage and Children

## Spouse System

### Daily Schedule

All spouses follow a single shared routine:

| Event     | Time  |
|-----------|-------|
| Wake up   | 6:10  |
| Go out    | 11:00 |
| Come home | 19:00 |
| Sleep     | 0:00  |

No per-NPC schedule variation is defined in the data.

### Marriageable Characters

Twelve characters have wedding party data: Adeline, Balor, Caldarus, Celine, Eiland, Hayden, Juniper, March, Reina, Ryis, Seridia, Valen.

### Wedding Parties

Each marriageable character defines a wedding ceremony composition:

- **Spouse party** (up to 2 members): NPCs who stand with the spouse's side.
- **Spouse guests** (optional): additional attendees on the spouse's side.
- **Standing speakers** (1--5): NPCs who give remarks during the ceremony.

Notable social connections visible through party composition:

- Adeline's party includes Celine and Reina; speakers are Wiscar and Linnet.
- Juniper has the largest speaker roster (Celine, Elsie, Dell, Luc, Maple).
- Ryis's guests are Wynne and Darren (also the speakers).
- Balor, Hayden, and March each list a single standing speaker.

## Children System

### Child Pool

Twelve named children exist in the data. The player does not choose; the game assigns from this pool.

| Name    | Sex    | Tone Threshold |
|---------|--------|----------------|
| Ellie   | Female | 18             |
| Sterling| Male   | 12             |
| Tephra  | Female | 15             |
| Rowan   | Male   | 12             |
| Astrid  | Female | 18             |
| Wilder  | Male   | 12             |
| Rune    | Female | 12             |
| Fray    | Female | 12             |
| Cedar   | Male   | 24             |
| Kam     | Male   | 24             |
| Brid    | Female | 15             |
| Torin   | Male   | 12             |

Sex distribution: 7 female, 5 male (total 12, not matching marriageable-character count).

### Tone Threshold

Each child has a `tone_threshold` value (range 12--24). The file defines no explanation of what this governs. Values cluster at 12 (seven children), with 15 (two), 18 (two), and 24 (two) as outliers.

### Commented-Out Offsets

Two commented-out values appear at the end of the file:

- `stork_offset = [0, 3]`
- `cradle_offset = [0, 8]`

These likely relate to child-arrival presentation but are inactive in the data.

## Source Absences

- No gift preferences, dialogue, or personality traits for spouses post-marriage.
- No growth stages, aging, or behavioral data for children.
- No indication of how children are assigned to the player (random, choice, spouse-dependent).
- No interaction or scheduling data for children.
- Spouse schedule has no seasonal or weather variation.
- No data on divorce, separation, or spouse removal.
