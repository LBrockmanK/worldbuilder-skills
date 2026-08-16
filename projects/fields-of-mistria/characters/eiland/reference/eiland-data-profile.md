# Eiland --- Character Data Profile

## Sources

- `fiddle/npcs/eiland.toml` --- NPC profile, gift preferences, visual config
- `fiddle/quests/heart_quests.toml` --- heart event quest definitions
- `fiddle/quests/story_quests.toml` --- story quest involvement
- `fiddle/letters.toml` --- letters sent to/about Eiland
- `fiddle/spouse.toml` --- wedding party composition
- `Eiland.md` --- existing character card

## Identity

- **Name:** Eiland
- **Bio (game text):** "Prettyboy noble with a love of archaelogy and ancient history. Brother to Adeline."
- **Birthday:** Summer 20
- **Tags:** townsfolk, noble, dateable
- **Job:** Archaeologist
- **Affiliation:** Royal Family of Mistria (Baron/Baroness lineage)
- **Aldarian name:** ELND
- **Dateable:** Yes
- **Child:** Astrid (post-marriage; `can_carry_child = false`)

## Family & Household

- **Sister:** Adeline --- co-manages town affairs from the Manor. She handles administration (grants, tax documents, business reviews); he handles archaeology and pitches dessert budgets. She assigns him paperwork he files late; he proposes cookie care packages she vetoes for building materials. As children: she built scale models of Mistria from snow, he played "rampaging dragon." He ate sugar straight from the bag.
- **Great Aunt:** Elsie --- lives at the Manor. Former opera singer in the Capital. Says Eiland "would be a hit at the Capital" on the piano. Offers romance advice he repeats in the same tone he uses for ancient inscriptions.
- **Father:** Baron Wiscar of Mistria --- moved to the Capital after the earthquake. Old friends with Errol. Attends wedding as spouse guest and standing speaker.
- **Mother:** Baroness Linnet of Mistria --- held the lantern while young Eiland traced stele symbols. Helped him research the Caldosian signet ring he found in the Manor basement.
- **Wedding party:** Errol (spouse_party_0), Adeline (spouse_party_1), Wiscar (guest + standing speaker), Linnet (guest)

## Physical Appearance (from portraits + character card)

- **Hair:** Light pink, wavy, short to medium length
- **Eyes:** Dark (uncertain from pixel art)
- **Skin:** Brown
- **Build:** Shown waist-up in portraits
- **Age appearance:** Young adult
- **Spring outfit:** White-lavender jacket with gold chevron embroidery at chest, gold-trimmed collar, purple cape, gold belt at waist

### Seasonal outfits

Six outfits: spring, summer, autumn, winter, beach, wedding

## Portrait Expression Catalog

14 expressions across up to 6 outfits:

| Expression | Outfits available | Usage context | Emotional register |
|---|---|---|---|
| neutral | all 6 | Default conversational mode, presenting information | Measured calm |
| think | all 6 | Considering history, analyzing artifacts, mid-lecture | Absorbed deliberation |
| happy | all 6 | Genuine excitement about discoveries, greeting player | Unguarded enthusiasm |
| wink | 5 (no wedding) | Confident asides, acknowledging Adeline's help | Playful warmth |
| mad | 5 (no wedding) | Determined excitement about pottery, D&D sessions | Intense focus |
| embarrassed | all 6 | Caught mid-lecture, self-conscious about enthusiasm | Core self-awareness |
| sad | 5 (no wedding) | Disappointment (Caldosian ring loss, no clues found) | Genuine deflation |
| ugh | 5 (no wedding) | Tax forms, crude marginalia, Adeline's office search | Mild distaste |
| hope_special | all 6 | Risking emotional vulnerability, romantic confession | Deepest openness |
| gloomy_special | 5 (no wedding) | Fear of adventure ending, potential loss | Suppressed longing |
| neutral_closed | 5 + wedding | Soaking in atmosphere, reflective silence | Contemplative stillness |
| happy_blush | 5 (no wedding) | Romantic moments, proposal, shared joy | Emotional warmth |
| surprised | 5 (no wedding) | Discoveries, unexpected revelations | Genuine startle |
| bashful | all 6 | Acknowledging his gift is "over the top" | Shy self-exposure |
| bath_neutral | beach only | Bathhouse scenes | Relaxed neutral |

**Key expression sequences in dialogue:**
- Archaeological excitement: neutral -> think -> happy -> mad (intense focus)
- Self-conscious retreat: happy -> embarrassed -> sad (caught lecturing)
- Emotional vulnerability: embarrassed -> hope_special -> gloomy_special
- Romantic progression: happy_blush -> hope_special -> embarrassed -> bashful

## Animation Cycles

Unique cycles reflecting his archaeologist role:
- **magnify** --- examining artifacts with magnifying glass (south, east)
- **pickaxe** --- excavation work (east only)
- **trowel** --- careful digging (east only)
- **write / write_sit** --- research documentation (south only)
- **read_sit** --- studying texts (south only)
- **princely_pose** --- distinctive noble stance (south, spring only)
- **brush** --- artifact cleaning (east only)
- Standard: idle, walk, blink, sit, drink, eat, kiss, action, sleep, bath_swim, shocked

## Gift Preferences

**Loved:** Caldosian chocolate cake, coconut cream pie, glowberry cookies, golden cheesecake, golden cookies, ice cream sundae, mont blanc, pumpkin pie, spell fruit parfait, strawberry shortcake

**Liked:** apple pie, berries and cream, candied lemon peel, candied strawberries, caramelized moon fruit, caramel candy, cherry cobbler, cherry tart, chocolate, crystal berry pie, sour lemon cake, lemon pie, peaches and cream, pomegranate sorbet, pudding, roasted rice tea, strawberries and cream, sweet sesame balls, wildberry pie, wintergreen ice cream

**Disliked categories:** junk, bugs, weird gifts

**Hated:** frog

**Pattern:** Overwhelmingly sweet. Every loved and liked gift is a dessert, pastry, or sweet treat (plus roasted rice tea). The sweet tooth is referenced in dialogue: sugar straight from the bag as a child, cookie care packages, pumpkin pie season, beer paired with chocolate chip cookies, museum snack bar proposal, using up Adeline's honey for tea.

**Drink preferences by time of day:**
- 6am: black tea, water
- Noon: green tea, latte
- 4pm: wine
- Midnight: milk

Pattern: quiet morning tea -> social afternoon -> evening wine -> comfort midnight milk.

## Gossip

- **Line:** "eiland_gossip"
- **Portrait:** happy
- **Effect:** hearts

## Quest Involvement

### Heart Quests (progression-gated)
1. **The Stele** (2 hearts) --- meet at Manor grounds, discover Dragonsworn Greaves in stele compartment
2. **The Ruins** (4 hearts) --- meet at Western Ruins, find Dragonsworn Helmet
3. **The Manor** (6 hearts) --- search the Manor house, find Dragonsworn Cloak in Elsie's wardrobe
4. **The Glade** (8 hearts) --- walk in Deep Woods, find Dragonsworn Cuisses and Cuirass in Grove of Rest; relationship fork (best friend / dating)
5. **Ten Hearts** --- proposal scene at original stele; Legacy Stele gift

### Story Quests
- **Unlocking the Mines Pt 1** --- Eiland asks player to discuss reopening the Mines at the Museum
- **Unlocking the Mines Pt 2** --- Meet Errol and Eiland at Mines entrance
- **The Water Tablet** --- player finds tablet in Mines, brings it to Eiland for translation
- **The Dragonsworn Tablet** --- requires both Eiland and Juniper 8-heart events; Eiland helps solve the mystery

## Letters

- **The Stele invitation** (2 hearts): invites player to see archaeological site on Manor grounds
- **The Ruins invitation** (4 hearts): new text translated, believes more armor at Western Ruins
- **The Manor invitation** (6 hearts): search has taken "unexpected turn," meet at Manor
- **The Glade invitation** (8 hearts): no lead yet, wants to walk in Deep Woods; alt hint letter if Deep Woods not unlocked
- **The Glade hint**: suggests exploring deeper mine levels
- **Player birthday** (4+ hearts, neutral): sends Caldosian chocolate cake
- **Player birthday** (8+ hearts, best friend): sends golden cheesecake, "most indulgent birthday cake"
- **Player birthday** (8+ hearts, romantic): sends golden cheesecake, "if you'd like to share the sweetness, you know where to find me"
- **Breakup letter**: "perhaps we got ourselves swept up in the romance that accompanies all major archeologic discoveries"
- **Wedding gifts** (from Elsie): desk, chair, artifact shelf
- **Unlocking the Mines**: asks player to meet at Museum about reopening

## Q&A Block Mapping

- **Background:** family structure, role in town, noble lineage, earthquake context, childhood signet ring story
- **Body:** portrait descriptions, seasonal outfits, expression catalog as physical mannerism proxy, animation cycles as activity evidence
- **Soul:** gift preferences as personality signal (all sweets), knowledge boundaries, archaeological passion
- **Relationships:** family dynamics, Errol mentorship, Juniper friction
- **Voice/Dialogue:** expression usage patterns as speech-to-visual mapping
