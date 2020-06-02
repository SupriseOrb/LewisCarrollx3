label day7:
    #(Scene: Bedroom)

    "The next morning, I was awakened by Alice pouncing on top of me."
    
    #show Alice
    
    a happy "\"Whitley, wake up, wake up!!!\""
    
    "I was still trying to see through stars, but it was clear she was excited about something."
    
    "I sat up and yawned."
    
    w "\"I'm up, I'm up!\""
    
    "I'm a little slow to get up, though."
    
    "To be perfectly honest, I wasn't ready for whatever new game awaited me for today."

    a normal "\"Today's the big surprise!\""

    "Oh boy. What did THAT mean?"

    w "\"Big surprise?\""

    "Wait a second..."

    "Today is Sunday! I'm supposed to be leaving today!"

    w "\"Oh, today is my last day here...\""

    "The prospect of leaving made my heart feel light, but I knew my work wasn't quite done."

    "There was still so much I wasn't sure about. And leaving Alice the way she was...."

    "Even after everything she's done, it just didn't feel right."

    a confused "\"Last day here? Oh, you're funny!\""

    "Funny...right. As if she would ever just let me waltz out the door anyhow."

    "Alice hopped off my bed and twirled around."
    
    a "\"Today I want to try a new game with you!\""

    a "\"We're gonna play House! I've never played it before, but it looks fun!\""

    a "\"So I'll be Daughter and you get to be Mama!\""

    "\"Me? Don't you want to play as a real grown-up?\""

    "Alice gave me a quizzical look."

    a "\"Being a real grown-up? What's the point of that?\""

    "\"...\""

    "\"That's fair.\""

    "Alice pulled on my arm."

    a "\"C'mon! We don't have any time to waste!\""

    #hide Alice

    "I finally started to get up and Alice skipped away, back into the main hall."

    "Once I'd gotten dressed, I left my room and found her sitting at the kitchen table."

    scene kitchen
    
    "Alice's Mr. Rabbit was seated next to her, but another object accompanied her as well."

    "A leather bag, placed primly at her side."

    a "\"It's my first day of school! And you gotta make me my favorite food for lunchtime!\""

    "\"O-Oh okay-\""

menu:

    "Make pancakes":
        jump day7pancakes

    "Make rabbit stew":
        jump day7lunch

    "Make roast chicken":
        jump day7chicken


label day7pancakes:

    a "\"Mama, stop being silly, that's not my favorite food!\""

    a "\"Maybe you should try again.\""

menu:

    "Make rabbit stew":
        jump day7lunch

    "Make roast chicken":
        jump day7wrong

label day7chicken:

    a "\"Mama, stop being silly, that's not my favorite food!\""

    a "\"Maybe you should try again.\""

menu:

    "Make pancakes":
        jump day7wrong

    "Make rabbit stew":
        jump day7lunch

label day7wrong:

    a "\"No, Mama. Now you're just being mean.\""
    
    a "\"Make my favorite food!\""

    a "\"Now, please.\""

menu:

    "Make rabbit stew":
        jump day7lunch

label day7lunch:

    a "\"Oooo, that smells sooo good! I can't wait for lunch!\""

    "As I packed the stew into her thermis, I noticed my hands quivering against the cold metal."

    "Her commands were making me more and more nervous."

    "I knew I already resolved to see this through..."

    "But would leaving now be so bad?"

    "I looked toward the front door. Freedom."

    "Then I looked at Alice, who was energetically swinging her legs at a table surrounded by vacant chairs."

    menu:

        "Leave":
            jump day7leaveAttempt

        "Stay":
            jump day7stay

label day7leaveAttempt:
    "She looked preoccupied enough with sorting through her \"school bag\"."

    "Maybe sneaking away wouldn't be so hard?"

    "I tip-toed to the door."

    "My hands were so close to the doorknob, I could already feel the smooth brass under my fingertips..."

    "Then-"

    a "\"Mama? What are you doing?\""

    "I froze, nails barely brushing the door frame."

    "\"I thought I'd take a look outside.\""

    "Alice just shook her head."

    a "\"You know...Auntie said something like that too.\""

    "I didn't turn to look at her, but there was a tenderness in her voice I hadn't heard before."

    "Something raw. Something she was...embarrassed of?"

    "\"I'm going to make things different this time.\""

    "With a pop of her familiar magic, the doorknob vanished, swallowed away into the wood."

    " *Pop* *Pop* *Pop* "
    
    "Every door outside and every window become fused with the house itself."

    "I had no choice but to face Alice."

    "She was standing now, looking maybe a little too satisfied with herself."

    a "\"There! Now we have more time together! Which is just perfect because-\""

    jump day7scavengerStart


label day7stay:

    "No, I set a goal this morning."

    "I'm not leaving without knowing what I can."

    "How else will I be able to solve this case?"

    "I've got to make sure I get what I can from Alice, no matter what she throws at me next."

    "But it's already been seven days. What if her godparents get here sooner than expected?"

    "I'll have to leave by then. I should let Alice know, and make sure she understands."

    "I walked over to one of the chairs and sat opposite to Alice."

    "\"So...Alice, this has been...fun, but I'm going to have to go soon, whether I like it or not. But your godparents will be here! And they'll take care of you-\""
    
    a "\"You want to leave?\""

    "Alice looked at me with a kind of sorrow in her eyes I hadn't seen before."

    "Her expression was something raw, something she couldn't help."

    "She must've noticed my surprise because her face quickly returned to that innocent mask again."

    a "\"You...really want to leave, Mama?\""

    "\"...I...\""

    "Alice's lips split into an eerie smile."

    a "\"That's okay!\""
    
    a "\"You won't want to, in a moment!\""

    "\"What do you-?\""

    jump day7scavengerStart

label day7scavengerStart:

    "Alice let out an abrupt gasp!"

    "She fished through her pockets, but whatever she was looking for was nowhere to be found."
    
    "\"Alice?\""
    
    a "\"My family spell! It's torn, it's missing pieces!\""

    "She looked to me with wide, desperate eyes."

    a "\"Help me find it, Mama!\""
    
    a "\"Help me find it, and I promise this will be our last game!\"" 

    "Her words were strained and pleading."

    "Just what was this spell that was so important? I'd never seen her this way..."

    "I took a deep breath."
    
    "\"Okay, I'll help you.\"" 

    a "\"Yay! You look in the parlor and I'll look in the kitchen!\""

    #(Scene: Parlor)

    #(Find pieces of paper)

    "With the last scrap of paper, the spell is complete."

    "I watched in wonder as the paper melded back together in my hands, forming a document as seamless as it was in creation."

    "Then I read the words. And my wonder turned to dread."

    "\"It's a resurrection spell! This...this is...\""

    a "\"You found it?\""
    
    "Alice's soft voice descended from the entryway."

    "I spun to her in a panic, and took two reflexive, albeit clumsy steps back."
    
    "\"Alice, no. You can't use this, i-it isn't right-!\""

    a "\"YOU FOUND IT!!!\""

    "She rushed up to me, and while I tried to conceal the paper quickly, Alice's magic was quicker."

    "My hands were frozen to the spot as Alice happily plucked the spell from my fingers."

    a "\"I'm so happy you found this, Mama! This'll be so much fun!\""
    
    "She gave me a huge grin."

    a "\"Now we can have some real playtime!\""

    "\"Alice, wait!\""

    "With another \"pop\", Alice was gone."

    "\"No, no, no, no- Resurrection spells are dangerous! Alice are you listening!?\""

    "\"They're impossible without a....!\""

    "A realization hammered my heart down to my stomach. I felt the hairs on the back of my neck spring up as a looked at my now free hands."

    "\"...without a sacrifice.\""

    "Suddenly, my hands were bound once more."

    "A magical, red string seized my limbs, and I was knocked off my feet as a force pulled me to the back of the room."

    "My back slammed against the extinguished fireplace, knocking the wind right out of me."

    "As I gasped for air, Alice came skipping up to me."

    a "\"Look, Mama! Mr. Rabbit's got all the ingredients!\""

    "She had scooped up all the ingredients for the spell in her bunny's arms"

    a "\"Bunnies are quick quick quick~!\""

    "Alice carefully placed the ingredients down then summoned a cauldron before her."

    a "\"I had everything already ready! Just like you always taught me.\""

    "\"Don't do this! You don't understand what will happen!\""

    a "\"I do too!\""

    "In a blink, the little girl was in my face, eyebrows scrunched and lips pressed tight."
    
    a "\"I DO know what I'm doing, I promise! I'll show you!\""
    
    "She returned to the cauldron, and that's when I noticed her feet weren't touching the ground."
    
    "The spell was already underway."
    
    a "\"I'll SHOW you!\""

    "\"Alice, stop! I know you want to hurt your parents, but you can't-!\""

    "\"THEY hurt ME!\""
    
    "[The magic grew stronger around her.]"
    
    "\"I'll make them come back and then they'll see. Then they'll be sorry they ever left.\""

    "[Alice's expression, Whitley's pity]"
    
    "\"...Oh...Alice...you don't want to hurt them, do you?\""

    a "\"Yes I do!\""

    "\"No you don't.\""
    
    a "\"They need to know what they did! They need to know I'm-!\""

    a "\"I'm...\""
    
    "\"You just...want answers. Right?\""

    "[the magic dims around her slightly]" 
    
    "[Alice sniffs, clenches her fists]" 
    
    a "\"Why? Why did they lock me away? Why...did they have to go?\""
    
    "[The magic dissipates, and it's just Alice, tears streaming down.]" 
    
    a "\"I wanted to be a good girl. I wanted to make them happy. So why did they treat me that way? They never trusted me with anything!\"" 
    
    a "\"I just want them to tell me WHY!?\""

    "\"Alice, I'm sorry, I don't have the answers you're looking for.\"" 
    
    "[Alice looks away and the magic starts building again]" 
    
    "\"But, I know they were trying their best! They were your parents! And they love you-\""

    a "\"YOU DON'T KNOW THAT!\"" 
    
    "[Magic flares up]"
    
    a "\"You don't know anything about them!\""

    "\"I know about []\""
    
    "[Alice pauses and stares at Whitley]" 
    
    "\"I know...you were friends with him. And you felt like he turned on you.\""

    a "\"He LEFT ME! He was only friends with me because of his-his stupid FAMILY!\""

    "\"-because of his PARENTS.\""
    
    "\"Alice, sometimes parents...don't really know what's best. Sometimes they're bad, and they hurt their family.\"" 
    
    "\"And sometimes...they're good but...just a little lost. They do what they think is best for their family, but it's wrong.\""
    
    "\"Like...they tell you you have to become friends with a stranger...or...\""
    
    a "\"They hide you away.\""

    "[Alice expression]"

    "\"Alice, your parents wanted you to be better than them! They wouldn't want you to do this!\""
    
    "\"Even if they aren't here. Even if they won't get to watch you, they love you so much.\""
    
    "\"And I know it's scary, but they wanted you to have this choice! To make the decision...to be - better.\""

    "[Alice looks at Whitley. Whitley can feel the magic starting to drain them. Alice stares.]"
    
    a "\"I just want them back.\""

    "\"Oh, Alice, I know you do.\" [weakly]"

    a "\"Then how come that can't happen!?\"" 

    "[magic flaring up]"

    a "\"HOW COME YOU GET TO LIVE AND THEY DON'T!? WHY DO I HAVE TO CHOOSE!?\""

    "[Alice looks at Whitley, but Whitley has lost her energy to speak. She simply stares.]"
    "[Alice sees her bunny burning up in all the magic she's using. She finally squeezes her eyes shut and lets out a cry and all the magic dissipates]" 
    "[The house returns to normal. Whitley feels her strength return.]" 
    "[The pages of the spell have disintegrated and all Alice is left with is a scorched rabbit. She hugs it tight.]"
    "[Whitley walks over to Alice and kneels beside her.]"
    "[Alice doesn't look up from her bunny.]"

    a "\"I want to be a good girl, Mom.\""

    "[Whitley puts her hand on Alice's shoulder and leans her head against hers]"

    #Fade out

    #(Scene: living room)

    "[Whitley has her things packed and is ready to leave.]"

    "[Alice tugs on her coat]"
    
    a "\"You really can't stay?\""

    "[Whitley smiles weakly and hugs her]"

    "\"I'm sorry, I really can't. But it's going to be okay. Know why?\"" 
    
    "[Whitley pulls back and looks at her front-on.]"
    
    "\"Because you are a smart and talented little girl who's going to do amazing things.\""
    
    "\"You don't have to be scared anymore. You can do this. You are good enough. All you have to do is remember the people who are here for you.\""
    
    "\"You'll always have a family from now on.\"" 
    
    "[Alice smiles at her. There's a knock at the door. Whitley gets up.]" 
    
    "\"I wonder who that could be?\""

    "[Alice looks at her quizzically. Whitley winks at her and looks through the window.]"

    "\"It looks like someone wants to see you!\""
    
    "[Whitley opens the door to show the little boy from day 4 memory.]"
    
    "[Alice hides behind Whitley instantly and gives the boy a sour look. The boy gulps and steps back.]"
    
    "[She realizes she's scared him and looks at his arm, where she burned him. She looks away.]"
    
    "[Whitley rubs Alice's head.]"
    
    "\"It's okay.\""
    
    "[Whitley looks at the boy]"

    "\"Don't you have something to say?\""

    "[The boy pauses and looks down, shuffling his feet.]" 
    
# WE NEED BOY CHARACTER

    "\"...I-I'm sorry. I'm sorry for making fun of you. It was wrong.\""

    "[Alice expression]"

    a "\"I'm sorry too. I shouldn't have hurt you.\""

    "[Alice's godparents arrive, Whitley bids farewell, Alice plays a game with the boy]"