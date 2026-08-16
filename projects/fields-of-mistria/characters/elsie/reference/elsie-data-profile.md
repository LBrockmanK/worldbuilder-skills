# Elsie — Character Data Profile

## Sources

- `fiddle/npcs/elsie.toml` — NPC profile, gift preferences, visual config
- `fiddle/festivals.toml` — Shooting Star Festival, Spring Festival vendor data
- `fiddle/quests/story_quests.toml` — gossip quest, shooting star festival quest
- `fiddle/quests/fetch_quests.toml` — 7 fetch quests
- `fiddle/letters.toml` — recipe letters, dating follow-up, wedding gift letters
- `t2/Conversations/Bank/Elsie/` — 93 dialogue files (all read)
- Existing character card: `characters/elsie/Elsie.md`

## Identity

- **Name:** Elsie
- **Job title:** Retired Socialite (game data field)
- **Bio context:** Great Aunt to Eiland and Adeline. Former opera singer (prima donna) from the Capital.
- **Birthday:** Summer 2
- **Tags:** townsfolk, noble
- **Dateable:** false
- **Aldarian name:** ELS
- **Journal background color:** [234, 212, 255] (lavender)

## Family & Household

- **Niece:** Adeline — Elsie watches over her, tells her to relax and stop working. "Adeline needs to relax and have more fun!" (adeline_should_relax). Praises her growth: "Adeline has really grown to fill the shoes her mother and father left behind" (adeline_grown). Pushes the player to encourage Adeline to take breaks.
- **Nephew:** Eiland — She has known him since "before he could peek over the keys of a piano" (known_eiland). Proud of his talent: "Eiland is quite a talent at the piano. He'd be a hit at the Capital." (eiland_is_great_at_piano). Visits him at the Museum.
- **NOT a blood relative:** Self-introduced as "Great Aunt. Well, not by blood. Some of us are simply born aunties, you see." (week_one_pt_1; greeting_ari)
- **Baron Wiscar & Baroness Linnet:** Adeline and Eiland's parents. Live in the Capital. "The Baron and Baroness will be so proud to see what Adeline's accomplished in their absence!" (parents_proud). Elsie officiated their wedding by the gazebo.
- **Household dinner companions:** Errol, Eiland, Adeline. "Off to dinner with the youngins and Errol! I do love to see their enthusiasm for Mistria." (travel_to_dinner)

## Physical Appearance (from portraits + character card)

- **Hair:** Lavender-gray, curled
- **Build/carriage:** Carries herself like someone who once commanded a stage
- **Spring outfit:** Pink long-sleeved dress with burgundy trim and belt
- **Summer outfit:** Light blue sleeveless dress with gold shawl at shoulders
- **Autumn outfit:** (data confirms outfit exists; visual description pending)
- **Winter outfit:** Cream-white fur shawl over dark green dress
- **Outfits in data:** spring, summer, autumn, winter (4 total; no beach or wedding variant)

## Portrait Expression Catalog

9 expressions across 4 seasonal outfits:

| Expression | Usage context | Emotional register |
|---|---|---|
| neutral | Default greeting, transitional beats, delivering information | Composed poise |
| think | Reminiscing, processing gossip, considering memories | Reflective pause |
| happy | Genuine delight, praise for others, receiving loved gifts | Warm pleasure |
| wink | Romantic advice, gossip delivery, knowing asides | Performative confidence |
| mad | Emphasis on odd events, mild indignation | Theatrical frustration |
| embarrassed | Receiving emotional compliments, dating tutorial intimacy | Vulnerability beneath composure |
| sad | Concern for Adeline, disappointment | Gentle worry |
| ugh | Receiving disliked gifts, distaste | Clear rejection |
| closed_eyes | (Available in data; specific dialogue triggers limited) | Contentment or reflection |

**Key expression sequences in dialogue:**
- Storytelling performance: neutral -> think -> happy (+ hearts effect)
- Romantic matchmaking: neutral -> wink -> happy
- Concern for family: neutral -> think -> sad -> happy (redirecting to hope)
- Gossip delivery: wink + sparkles_dark

## Animation Cycles

| Cycle | Directions | Outfits | Notes |
|---|---|---|---|
| idle | N, S, E | all 4 | Default standing |
| walk | N, S, E | all 4 | Pauses to idle when speaking |
| blink | S, E | all 4 | |
| sit | N, S, E | all 4 | Seated variant |
| drink | S, E, N | all 4 | Seated; hold 240-360 frames |
| eat | S, E, N | all 4 | Seated; hold 240-360 frames |
| action | N, S, E | all 4 | General action; hold 240-360 frames |
| **sing** | **S only** | **spring, summer, autumn** | **Complex type; unique to Elsie** |
| write | S only | all 4 | Complex type; memoir/journal writing |
| write_sit | S, E | all 4 | Complex type; seated writing variant |
| shocked | S only | spring only | Complex type; rare |

**The sing cycle** is distinctive — Elsie is the only NPC with this animation. When active, she cannot be interrupted: "(Elsie is occupied with her singing, you shouldn't interrupt her.)" (singing). Not available in winter, consistent with the opera singer who now sings outdoors in fair weather.

## Gift Preferences

**Loved:** alda feather pendant, cranberry orange scone, crystal rose, jasmine tea, mont blanc, paper, perfect diamond, poached pear, rose, wildberry scone

**Liked:** blackberry jam, blueberry jam, cherry tart, chrysanthemum, cosmos, crystal berry pie, diamond ore, iris, jasmine, lilac, marmalade, moon fruit cake, pomegranate sorbet, quiche, red wine, rosehip jam, rose hip, tulip, white wine, wild berry jam

**Disliked categories:** junk, bugs, weird_gift

**Hated:** praying mantis — "Don't tell little Luc, but I simply can't abide the Praying Mantis. I prefer a romance with a happier ending." (Even her hated gift response references romance.)

**Gift response patterns:**
- Loved jewelry: "The glitter reminds me of the stage lights when I was a prima donna!" (loved_gift_jewelry)
- Loved food: "The kind of refreshment that brings back sweet memories of the Capital." (loved_gift_edible)
- Liked food: "How lovely! This will be perfect for after dinner. If I can wait that long!" (liked_gift_edible)
- Liked flowers: "What a sublime blossom!" (liked_gift_flowers)
- Disliked: "I don't think this is making it into my memoirs." (disliked_gift)
- Birthday: "It's terribly sweet of you to remember my birthday, [Ari]." (birthday_gift)

**Drink preferences by time of day:**
- 6am: green tea
- Noon: green tea, lemonade
- 3pm: wine, white wine, rose wine
- 8pm: wine, white wine, rose wine, absinthe

Pattern: gentle morning tea -> social afternoon wine -> adventurous evening additions (absinthe). The shift from tea to wine tracks her transition from private reflection to social mode. The absinthe at night is distinctly bohemian.

## Quest Involvement

### Shooting Star Festival (story quest)
- **npc_for_icon:** elsie — she is the face of this quest
- Quest description: "Elsie said that I should invite someone to go with me"
- She delivers the Star Brooches and explains the tradition
- Manages the romantic invitation mechanic

### Gossip for Elsie (story quest)
- "Do you have a nose for news? An ear for the exciting? I love Mistria, but I do miss all the gossip of the big city..."
- Player collects gossip from Balor, Juniper, and Dell, then reports to Elsie
- Rewards: 20 renown

### Fetch Quests (7 total)
1. **Snowdrop Anemone** — "lovely flowers that grow by the Western Ruins"; rewards: 3 seeds
2. **Blackberries** (x6) — for blackberry jam; rewards: blackberry jam recipe
3. **Wild Berries** (x6) — for wildberry scones; rewards: wildberry scone recipe
4. **Orange** — for marmalade; rewards: marmalade recipe
5. **Silver Ingot** — for "a personal friend in the Capital, who happens to be a rather famous jeweler"; rewards: 500 gold
6. **Roses** (x12) — "I quite like the flower, but I'm not much of a fan of the actual picking, too many thorns"; rewards: 300 gold
7. **Blueberry Jam** (x3) — "I'm quite partial to Blueberry Jam"; rewards: 1000 gold

Pattern: recipes she shares (jam, scones, marmalade) position her as culinary mentor. Capital connections (jeweler friend) and flower appreciation (roses, snowdrop anemone) reflect her socialite identity.

### Letters Sent
- **Poached Pear Recipe** — triggered by player shipping pears
- **Pomegranate Sorbet Recipe** — triggered by player shipping pomegranates
- **Dating Follow-up** — after dating tutorial cutscene + Deep Woods unlocked, sends picnic set with dating advice
- **Wedding Gifts** — Elsie sends ALL wedding gift letters regardless of which NPC the player marries (12 variants). She collects the gifts from the Inn and delivers them. Community social coordinator role.

## Festival Vendor Role

### Spring Festival
- Elsie runs her own vendor stall (`elsie_spring_festival`) selling cosmetics:
  - Flower crown, flower earrings, spring festival dress, spring festival suit, flower top hat
- Challenge tier-gated: higher tiers unlock more items
- This makes her one of the few non-merchant NPCs with a festival shop role

## Q&A Block Mapping

- **Background:** family structure (non-blood aunt), Capital opera career, Manor residence, household dynamics
- **Body:** portrait descriptions, seasonal outfits, expression catalog, sing animation as physical mannerism
- **Soul:** gift preferences as personality signal (loves roses and paper, hates praying mantis with a romance quip), drink preferences (green tea to absinthe), quest patterns (gossip, recipes, Capital connections)
- **Relationships:** family dynamics, Juniper gossip circuit, Valen visits, community wedding role
- **Voice/Dialogue:** expression usage patterns, gift response personality
