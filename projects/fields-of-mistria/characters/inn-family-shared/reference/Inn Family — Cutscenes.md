# Inn Family -- Cutscenes

Source extraction of cutscene data involving Josephine, Hemlock, Luc, and Maple. Directly relevant cutscenes extracted at FULL depth; tangential cutscenes (other characters' Heart Events, Festivals, Wedding) at STRUCTURAL depth.

Sources: `source/t2/Cutscenes/Story Events/`, `source/t2/Cutscenes/Heart Events/`, `source/t2/Cutscenes/Festival Events/`, `source/t2/Cutscenes/Heart Events/Wedding/`

---

## Story Events -- Town Repair (Full Depth)

### repair_the_inn.c.toml

Source: `source/t2/Cutscenes/Story Events/Town Repair/repair_the_inn.c.toml`

#### Part 1: The Proposal

Triggered as gameplay_triggered event. Writes `{ rti = "pre" }`.

Hemlock greets the player. Josephine offers food. Adeline redirects to business -- talking about upgrading the Inn. Hemlock offers drinks; player chooses fruity/bitter/water. Adeline pitches the upgrade: the Inn is travelers' first stop and the hub of social life.

Hemlock hesitates: "we can't really go much bigger than we are, don't have the staff." Josephine declines: "I wouldn't want to put so much of a burden on you two."

Reina bursts in with her own proposal: upgraded kitchen and bar, more dishes, Ryis and Landen helping with redecorating, branded furniture for sale as souvenirs, new soup cauldron. Josephine reviews it: "runners for the tables, new cushions for the chairs, you've really thought of everything." Hemlock: "With a proposal this well thought out, how could we say no?" Josephine: "I'm so proud of you, Reina."

Adeline sets up the Donation Box.

#### Part 1 Follow-ups (refresh = "never", requires rti = "pre")

**Adeline:** "I never expected Jo and Hemlock to decline, they caught me completely off guard. Thank goodness for Reina!"

**Hemlock:** "Lots to do around here before we can start construction, but don't you worry [Ari], we'll be ready as soon as you've collected all the materials!"

**Josephine:** "That daughter of mine! She's grown up into a fine business woman."

**Kids (Dell, Luc, Maple together):** Maple: "Did Reina show you the plans for the Inn? We helped, you know! I proposed the six room Princess Suite!" Luc: "And I suggested the special menu for our bug customers!" Dell: "She told me there wasn't any room for the arena royale though." Maple: "Wait... did my sister use ANY of our ideas?"

**Landen:** Comments on Reina's branded furniture proposal.

**Ryis:** Notes they'll have worked on every building on the street.

#### Part 2: The Construction

Turn-in triggered by Adeline. Writes `{ rti = "post", expires = "4d" }`.

Josephine is surprised the whole town came out. Balor, Landen, Ryis, Celine, Hayden all pitch in. Reina commands the "Dragonguard" (Luc, Maple, Dell) to help decorate the dining room. Balor and Olric do heavy lifting. Hemlock admires the result. Inside: Reina welcomes everyone. Josephine: "It's a dream come true!" Hemlock notices bar is already stocked. Balor asks for a drink. Hemlock: "drinks are on the house for all of you!" Reina excited about the new kitchen. Josephine: "Thank you everyone, I can't tell you how much I'm looking forward to welcoming you all here for many more seasons to come!"

#### Part 2 Follow-ups (refresh = "never", requires rti = "post")

**Balor:** Glad they left his room alone.

**Hemlock:** "Business is right up with the Inn's refurbishment! We're not raising the prices though."

**Josephine:** "The Inn has been in the family for generations, it's so wonderful to see what it's grown into!"

**Maple:** "You know, when I grow up I was planning to go to the Capital to seek my fortune... But the Inn looks so nice now, it's hard to imagine there's a better place to go in all of Aldaria!"

**Reina:** Thanks the player; new kitchen is a dream to work in.

### somethings_bugging_me.c.toml

Source: `source/t2/Cutscenes/Story Events/somethings_bugging_me.c.toml`

Writes `{ sbm = true, expires = "4d" }`. Gameplay triggered.

Luc is excitedly telling Hemlock a story ("whoosh, bzzt, WHAM!"). Hemlock responds: "Oooh, amazing!" Luc asks the player to become an Entomologist. Hemlock explains: "It means someone who studies insects." Luc: "Yeah, that's what I do!" Luc explains bugs in Mistria, Errol agreed to a museum wing. Hemlock: "Until now Luc's been bringing all his finds back to his room...."

Luc asks the player to join him. He gives the player his old Net: "It's brought me lots of luck over the years, but I think it's time... to pass it on to a new generation of bug catchers." Hemlock: "Don't forget to bring any new bugs you find to Errol at the Museum! Please don't bring them here..."

#### Follow-ups (refresh = "never", requires sbm = true)

**Luc:** Excited about the player bug-catching, offers tips anytime.

**Hemlock:** "Little Luc was so excited to see you take up that bug net! It's all he's been able to talk about lately!"

**Reina:** Thanks the player for taking interest in Luc's hobby.

**Errol:** Asks the player to bring specimens to the Museum.

### apiaries_and_terrariums.c.toml

Source: `source/t2/Cutscenes/Story Events/Town Repair/apiaries_and_terrariums.c.toml`

Writes `{ aat = "pre" }`. Gameplay triggered.

Luc announces a letter from the Royal Society of Entomologists congratulating Mistria. Adeline: "It's wonderful to hear that a society from the Capital has taken notice." The Society offers an Apiary and Terrarium program. Reina: "Access to all kinds of fresh, delicious Honey!" Luc explains Terrariums house Bugs that make useful things. He asks the player to ship 20 bugs.

Turn-in (writes `{ aat = "post", expires = "4d" }`): Adeline announces approval. Equipment provided.

#### Follow-ups

**Pre (aat = "pre"):**
- Adeline: "That Luc! I wish I had half his gumption when I was his age."
- Hemlock: "Terrariums huh... On the one hand, that means Luc will be able to keep more bugs. But on the other hand, it means my little guy will be even happier! Seems worth it to me."
- Reina: "I've been helping him write to the Royal Society of Entomologists like every week. He was so tickled when they wrote back calling him a Fellow Scientist!"

**Post (aat = "post"):**
- Luc: Thanks the player, excited about the terrarium.

### lost_and_found.c.toml

Source: `source/t2/Cutscenes/Story Events/Town Repair/lost_and_found.c.toml`

The Dragonguard kids (Maple, Luc, Dell) break into a council meeting. Maple demands to help protect Mistria. Nora asks about Reina's chocolate bar distraction; Hemlock confirms she tried. Luc: "My tummy hurts!" Maple: "Yay!" when allowed to stay. Hemlock: "As long as you're all quiet, okay?" Luc: "You got it, Dad!"

Maple: "Yeah, you really should let us help. Then maybe you won't all look so tired!" Hemlock: "Maple..." Luc: "Noooo problem!" Maple negotiates payment for the Dragonguard.

#### Follow-ups

- Adeline: "Maple successfully negotiated an extra snack for the Dragonguard on town clean-up days. But we negotiated her down from everyone in the Dragonguard getting a patrol pony, so I consider it a win."
- Hemlock: "Those kids! When I told Jo they broke into a council meeting she couldn't stop laughing."

### replenishing_mistrias_food_reserves_2.c.toml (excerpt)

Source: `source/t2/Cutscenes/Story Events/Town Repair/replenishing_mistrias_food_reserves_2.c.toml`

**Josephine follow-up (rmfr2 = "post"):** "Did you hear, [Ari]? Everyone liked those rations so much that we added them to the menu at the Inn! Too bad we didn't come up with a better name for them though..."

**Hemlock** appears in part 2 scene: "Almost there..." and Hayden asks Hemlock to put on a beer reserve to pair. Hemlock: "Way ahead of you, Hayden!"

---

## Heart Events (Structural Depth)

### Balor Heart Events

**balor_four_hearts.c.toml:** Hemlock greets the player at the Inn, directs them to Balor's room upstairs.

**balor_six_hearts.c.toml:** Scene at the Inn bar. Balor orders drinks; Hemlock serves them, offers the rest of the bottle on the house. Hemlock provides drinks throughout the scene.

**balor_eight_hearts.c.toml:** Balor had help from Hemlock and Jo setting up. Maple, Luc and Dell tried to help too ("easy enough to clean up their mess"). Josephine brings food, then interrupts -- Wheedle is downstairs demanding to see Balor about a contract. Josephine: "Balor, surely you're not...?" She and Hemlock keep Wheedle busy. After confrontation: Josephine: "He didn't even pay for his drink!" Hemlock: "If it means we won't see him here again, it's on the house." Josephine: "Balor dear, we're all so proud of you." Hemlock: "You're a true Mistrian, Balor."

Follow-ups: Hemlock reflects on not stepping in ("I know Balor. He needed to handle Wheedle himself."). Josephine angry at Wheedle. Kids (Maple, Luc, Dell): Luc says Balor gave them Chocolate to not interrupt; Dell thinks it would have been more fun with them there.

### Hayden Heart Events

**hayden_six_hearts.c.toml:** Luc and Maple appear, greet Hayden. Play with Henrietta the chicken. Luc: "Cool!" Maple: "Yaaaay! Chicken friend!"

Follow-ups: Luc says Henrietta is good at finding bugs, "We've got competition!" Maple wonders what royal court position to give Henrietta.

**hayden_eight_hearts.c.toml:** Hemlock follow-up (romance path): Hayden buying everyone at the Inn drinks. Luc follow-up: amazed it took so long to get Henrietta into the Dragonguard.

### March Heart Events

**march_six_hearts.c.toml:** March reflects: "Life was hard, even with Jo and Hemlock looking out for us." Hemlock follow-up: his cutlery order at the blacksmith is delayed (March made something).

### Reina Heart Events

**reina_six_hearts.c.toml:** Family tasting scene. Josephine: "Would you listen to these two!" Hemlock: "Let them cook, dear." Josephine allows it if they share. Hemlock introduces Balor. Josephine notes Taliferro's style. Maple tries chocolate cake with chili ganache: "I want a Grilled Cheese..." Hemlock: "Maple, hush!" Maple: "Just make some of the stuff you normally cook, Reina!" Luc: sad about dessert order. Hemlock finds drink "interesting." Josephine: "it does all taste like something Taliferro might serve..."

Follow-ups: Maple wonders about noble food. Hemlock reminisces about "the Hemlock Hooray" (sundae with cake and sparkler). Josephine notices Reina's been thoughtful, asks the player to support her.

**reina_eight_hearts.c.toml:** Aldarian Star cooking competition at the Inn. Hemlock preps drinks, Josephine gets the starchiest tablecloth. Maple: "Me and Luc want to help too!" Reina assigns them silverware cleaning. Luc: "It'll be so clean a bug could eat off it!" Josephine: "Don't worry, dear. I'll check their work." Maple spots judges arriving. Luc greets "Vera." Josephine welcomes judges. Hemlock takes drink orders, mentions Reina's pairing recommendations. After win: Josephine proud, Hemlock: "That's my daughter!" Maple wants to hold the star trophy first, then: "What kind of sham is this?" (no physical trophy). Josephine: "Let us handle it, dear!" Hemlock suggests Reina take a break with the player.

Follow-ups: Hemlock getting reservation inquiries, writes back that people can just drop by. Josephine glad all of Aldaria knows Reina's talent. Luc says it's partly his award for cleaning silverware. Maple drew a trophy picture for Reina and one for the player.

---

## Wedding (Structural Depth)

### wedding_0.c.toml

Source: `source/t2/Cutscenes/Heart Events/Wedding/wedding_0.c.toml`

Josephine is the primary wedding coordinator NPC. She wakes the player on wedding day, reassures them about chores ("Everyone's pitching in"). She set up a room at the Inn for the player to prepare; the fiance uses her room. Elsie compliments Josephine's room setup. Josephine coordinates with Elsie on wardrobe.

Josephine shares personal wedding memories with the player:
- Nervous path: "I had a terrible case of nerves on my wedding day. But the moment I saw Hemlock at the altar... all that just melted away."
- Excited path: "I was full of butterflies on my wedding day too. The minute I saw Hemlock at the altar... my heart just about overflowed."
- "As someone who's watched you change and grow over these many seasons... I just know you'll be so happy."

---

## Festival Events (Structural Depth)

### harvest_festival.c.toml

Source: `source/t2/Cutscenes/Festival Events/harvest_festival.c.toml`

Josephine has two setup variants where she reminds the player about collecting Queen Berries.

Josephine also has a morning variant collecting Queen Berries before heading to prep with Reina.

In all placement variants (no place, third, second, first): Maple wins second/third place. Maple: "I won, I won! How much queenly authority does [place] get me?" Josephine: "It means you get an extra large slice of pie, dear." Maple: "Yay!"

### spring_festival.c.toml

Source: `source/t2/Cutscenes/Festival Events/spring_festival.c.toml`

Josephine is the announcer for all placement results, calling out winners of the Breath of Spring flower competition. She appears in setup, no_place, third_place, second_place, first_place, and first_place_plus variants.

Follow-ups: Josephine says "Nobody does the Spring Festival better than Mistria." Luc: collecting flowers is fun because his favorite insects show up in them. Maple: excited to help with the family booth.

### the_animal_festival.c.toml

Source: `source/t2/Cutscenes/Festival Events/the_animal_festival.c.toml`

Josephine is the turn-in NPC: "Perfect timing, [Ari], we were just about to get the ceremony started!" All four Inn family members appear in can_talk requirement lists for festival eligibility checks.

---

## Source Absences

- No Caldarus, Seridia, Valen, Eiland, Celine, Juniper, or Adeline Heart Event files contained Inn family mentions.
- Children/Delivery and Children/Dream heart event subdirectories contained no Inn family mentions.
- No engagement_tutorial.c.toml mentions of Inn family were found.
