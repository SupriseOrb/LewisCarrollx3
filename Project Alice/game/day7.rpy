label day7:

    play music lunch fadein 1.0

    scene bg whitley_bedroom

    "The next morning, I was awakened by Alice pouncing on top of me."
    
    a happy "\"Whitley, wake up, wake up!!!\""
    
    "I was still trying to see through stars, but it was clear she was excited about something."

    "I sat up and yawned."
    
    w "\"I'm up, I'm up!\""
    
    "I was a little slow to get up, though."
    
    "To be perfectly honest, I wasn't ready for whatever new game awaited me for today."

    "Especially after everything I've heard this little girl say."

    a smile "\"Today's the big surprise!\""

    "Oh boy. What did THAT mean?"

    w "\"R-Right. That's right, it's your big surprise!\""

    "I nodded along with her through a forced smile."

    "Today was the day I had to escape Wonderland."

    "But there was still so much I wasn't sure about. And leaving Alice the way she was...."

    "Even after everything she's done, it just didn't feel right. But I needed to at least try to find an exit."

    w "\"A big surprise on my last day here. What a treat, Alice!\""

    "Alice, as expected, gave me a quizzical look. She giggled."

    a confused "\"Last day here? Oh, you're funny!\""

    "Funny...right. As if she would ever just let me waltz out the door anyhow. Well, it was worth a shot."

    "Alice hopped off my bed and twirled around."
    
    a happy "\"Today I want to try a new game with you!\""

    a normal "\"We're gonna play House! I've never played it before, but it looks fun!\""

    a smile "\"So I'll be Daughter and you get to be Mama!\""

    w "\"Me? Don't you want to play as a real grown-up?\""

    "Alice frowned at me."

    a sorrow "\"Being a real grown-up? What's the point of that?\""

    w "\"...\""

    w "\"That's fair.\""

    "Alice pulled on my arm."

    a smile "\"C'mon! We don't have any time to waste!\""

    "I finally started to get up while Alice skipped away, back into the main hall."

    "Once I'd gotten dressed, I left my room and found her downstairs, sitting at the kitchen table."

    scene bg kitchen
    
    "Alice's Mr. Rabbit was seated with her as usual, but another object accompanied her as well."

    "A leather bag, placed primly at her side." 

    a normal "\"It's my first day of school! And you gotta make me my favorite food for lunchtime!\""

    w "\"O-Oh okay-\""

menu:

    "Make pancakes":
        jump day7pancakes

    "Make rabbit stew":
        jump day7lunch

    "Make roast chicken":
        jump day7chicken


label day7pancakes:

    a awkward "\"Mama, stop being silly, that's not my favorite food!\""

    a confused "\"Maybe you should try again.\""

menu:

    "Make rabbit stew":
        jump day7lunch

    "Make roast chicken":
        jump day7wrong

label day7chicken:

    a awkward "\"Mama, stop being silly, that's not my favorite food!\""

    a confused "\"Maybe you should try again.\""

menu:

    "Make pancakes":
        jump day7wrong

    "Make rabbit stew":
        jump day7lunch

label day7wrong:

    a annoyed "\"No, Mama. Now you're just being mean.\""
    
    a confused "\"Make my favorite food!\""

    a unhappy "\"Now, please.\""

menu:

    "Make rabbit stew":
        jump day7lunch

label day7lunch:

    a happy "\"Oooo, that smells sooo good! I can't wait for lunch!\""

    "As I packed the stew into her thermis, I noticed my hands quivering against the cold metal."

    "Her commands were making me more and more nervous."

    "I know I already resolved to see this through..."

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

    "Maybe sneaking away wouldn't be so hard? At the very least, I could plan an escape route."

    "I tip-toed to the door."

    "My hands were so close to the doorknob, I could already feel the smooth brass under my fingertips..."

    "Then-"

    a confused "\"Mama? What are you doing?\""

    "I froze, nails barely brushing the door frame."

    w "\"I thought I'd take a look outside.\""

    "I kept my voice steady, but my heart was pounding out of my chest."

    a unhappy "\"You know...Auntie said something like that too. The nanny that took care of me before.\""

    "I didn't turn to look at her, but there was a tenderness in her voice I hadn't heard before."

    "Something raw. Something she was...embarrassed of?"
    
    a angry "\"She didn't come back. But I'm going to make things different this time.\""

    "With a pop of her familiar magic, the doorknob vanished, swallowed away into the wood."

    " *Pop* *Pop* *Pop* "
    
    "Every door to the outside and every window become fused with the house itself."

    "I had no choice but to face Alice."

    "She was standing now, looking maybe a little too satisfied with herself."

    a happy strange "\"There! Now we have more time together! Which is just perfect because-\""

    jump day7scavengerStart


label day7stay:

    $ heart += 1

    "No, I set a goal this morning."

    "I'm not leaving without knowing what I can. I can find a way out after I deal with Alice."

    "I know she's hiding something, something that {i}isn't{/i} magic. How could I call myself a detective without knowing what it is?"

    "I've got to make sure I get what I can from Alice, no matter what she throws at me next."

    "But it's already been seven days. What if her godparents get here sooner than expected?"

    "I'll {i}have{/i} to leave by then. I should let Alice know, and make sure she understands."

    "I walked over to one of the chairs and sat opposite to Alice."

    w "\"So...Alice, this has been...fun, but I'm going to have to go soon, whether I like it or not. But your godparents will be here! And they'll take care of you-\""
    
    a sorrow "\"You want to leave?\""

    "Alice looked at me with a kind of sorrow in her eyes I hadn't seen before."

    "Her expression was genuine, but reluctant, as if she didn't like making it."

    "She must've noticed my surprise because her face quickly returned to that innocent mask again."

    a sad "\"You...really want to leave, Mama?\""

    w "\"...I...\""

    "Alice's lips split into an eerie smile."

    a smile "\"That's okay!\""
    
    a happy strange "\"It doesn't really matter. After all, you won't want to, in a moment!\""

    "I noticed her hand surreptitiously travel to her dress pockets."

    w "\"What do you-?\""

    jump day7scavengerStart

label day7scavengerStart:

    "Alice let out an abrupt gasp!"

    "She fished through her pockets, but whatever she was looking for was nowhere to be found."
    
    w "\"Alice?\""
    
    a sorrow "\"My family spell! It's torn, it's missing a piece!\""

    "She looked to me with wide, desperate eyes."

    a sad "\"Help me find it, Mama!\""
    
    a sad "\"Help me find it, and I promise this will be our last game!\"" 

    "Her words were strained and pleading."

    "Just what was this spell that was so important? I'd never seen her this way..."

    "I took a deep breath."
    
    w "\"Okay, I'll help you.\"" 

    a happy "\"Yay, thank you so much! You look in the foyer and I'll look in the kitchen!\""

    scene bg foyer

    "Just as she requested, I went to the foyer. Where this all began. Part of me wished I had never set my dumb, unsuspecting foot in this place."

    "But the part of me that made me become a detective still hungered for answers. Let's see what this spell is all about."

    menu:
        "Check bottom of staircase":
            "I walked over to the foot of both staircases and checked the polished floor around them."
            "Nothing."
            jump searchFoyerUnder

        "Check under stairs":
            "I looked to the curled corners of the staircases. Maybe a paper could've slipped through the cracks?"
            "After searching every crevice I could find, I came up empty."
            "Nothing here."
            jump searchFoyerBottom

        "Check balcony":
            jump foundPiece

    label searchFoyerBottom:
    menu:
        "Check bottom of staircase":
            "I walked over to the foot of both staircases and checked the polished floor around them."
            "Nothing."
            jump searchBalcony
    
        "Check balcony":
            jump foundPiece

    label searchFoyerUnder:
    menu:
        "Check under stairs":
            "I looked to the curled corners of the staircases. Maybe a paper could've slipped through the cracks?"
            "After searching every crevice I could find, I came up empty."
            "Nothing here."
            jump searchBalcony
    
        "Check balcony":
            jump foundPiece

    label searchBalcony:

    "Looks like there's only one other place to check..."

    label foundPiece:
    # Because of the violent protests going on at the time, no one would've batted an eye at the house fire
    # Whitley putting everything together

    "I climbed the stairs to the balcony overlooking the immaculate foyer of the Hearts' mansion."

    "I searched for the spell, flipping up the blood-red carpets that lined the reflective tile and checking between ornate railings and window frames."

    "If I didn't know this place was absolutely bananas, I might consider a nifty real estate opportunity here."

    "Just when I started to consider heading back down to Alice empty-handed, a bright light pierced my vision."

    "I flinched and held my hand up to shield my eyes when I noticed the source of the ray."

    "It was the grand chandelier, hanging majestically like a second sun in the sky. And to my astonishment, it held treasures too."

    "Not the kind you might buy at a jewelry store, but the kind that just might satiate a desire for answers."

    "There, within the many crystals, was an envelope."

    "Could it be the spell?"

    "I wasted no time in finding out. Hastily, I worked the gears by the window to pull the chandelier towards me, along a pulley system fixed to the high ceiling."

    "As soon as it was within arm's reach, I snatched the envelope from its extravagant roost."

    "On the front of the envelope was Alice's name, written out in a handwriting I'd seen before."

    "I opened the letter and pulled out what I was hoping for. The torn piece of paper."

    "But suddenly, I felt a coldness squeeze my heart in place. The words on the page were just that, words, but they oozed a darkness I couldn't comprehend."

    "I didn't even notice my hands starting to tremble just for being {i}near{/i} the symbols."

    "I was about to fling the demonic thing away from me, when my eyes caught lettering on the back. Only this lettering, was different. It was normal."

    "And it was the same handwriting on the front. This time, my hunch was confirmed."

    "It was a letter to Alice...from Aiden."

    "It was short, but reassuring. I had never met the man, but the words spoke succinctly enough for me to understand why Alice was so attached to him."

    "It read: \"My little Alice - \nI know events have been troubling recently. But know that despite whatever happens,\nWe Love You.\""

    "No tricks. No riddles. No games. Just...\"We Love You.\""

    "Just reading those words gave me the courage to hold the paper firm and ward off it's evil energies."

    "I took a closer look at the black lettering."

    "It wasn't an incantation, it looked more like a recipe?"

    "A recipe that makes...."

    "The courage Aiden's old words gave to me was swept away in an instant. For in my hands, I held-"

    w "\"A resurrection spell! This...this is...\""

    a normal "\"You found it?\""

    "Alice's soft voice ascended from the foyer's entryway."

    "I spun to her in a panic, and took two reflexive, albeit clumsy steps back."

    w "\"Alice, no. You can't use this, i-it isn't right-!\""

    a happy "\"YOU FOUND IT!!!\""

    "She squealed in delight. I looked to both my sides for a hasty escape but I was trapped."

    "Perforce, I sprinted to the staircase opposite her, maybe I could escape through-"

    "Suddenly, a step on the stairs fell away, and I was falling."

    "With no time to break my fall, My back slammed against the merciless stone stairs, knocking the wind right out of me."

    "Alice skipped up to me and happily plucked the torn sheet from my fingers."

    a happy strange "\"I'm so happy you found this, Mama! This'll be so much fun!\""
    
    "Reunitied with the missing scrap of paper, the spell was complete."

    "I watched through spotty eyes as the paper melded back together in her hands, forming a document as seamless as it was in creation."
    
    "She gave me a huge grin."

    a smile "\"Now we can have some real playtime!\""

    w "\"Alice, wait!\""

    "With another *pop*, Alice was gone."

    w "\"No, no, no, no- Resurrection spells are dangerous! Alice are you listening!?\""

    w "\"They're impossible without a....!\""

    "A realization hammered my heart down to my stomach. I felt the hairs on the back of my neck spring up as I looked at my now free hands."

    w "\"...without a sacrifice.\""

    "By the time I gathered enough strength to try standing, Alice was back."

    "A magical, red string seized my limbs, and I was pulled to the staircase's metal banister."

    "As I struggled in the string's steadfast grip, Alice waltzed up to me."

    a happy "\"Look, Mama! Mr. Rabbit's got all the ingredients!\""

    "She held out her stuffed toy, and there in her Mr. Rabbit's plush arms, she had placed her \"schoolbag\". Filled to the brim with every ingredient needed for the spell."

    a smile "\"Bunnies are quick quick quick~!\""

    "Alice carefully placed the ingredients down then summoned a cauldron before her."

    a happy strange "\"I had everything already ready! Just like you always taught me.\""

    w "\"Don't do this! You don't understand what will happen!\""

    a confused "\"I do too!\""

    "In a blink, the little girl was in my face, eyebrows scrunched and lips pressed tight."
    
    a unhappy "\"I DO know what I'm doing, I promise! I'll show you!\""
    
    "She returned to the cauldron, and that's when I noticed her feet weren't touching the ground."
    
    "The spell was already underway."
    
    a sorrow openmouth "\"I'll SHOW you!\""

    "She continued on with her cooking."

    "No no no, this can't be happening. Okay, think Whitley."

    "A resurrection spell. All this was leading up to a resurrection spell."

    "But why? The obvious answer is her parents, but despite talking about them nicely, she always had disdain for them when I asked about them directly."

    "So why would she want them back now? Isn't she free now? Unless..."

    "The spell! Anything she cast a spell on, she controlled. She's going to try controlling her parents!"

    w "\"Alice, stop! I know you want to hurt your parents, but you can't-!\""

    a sorrow closeeyes "\"THEY hurt ME!\""
    
    "A spark of ethereal lights flickered at her feet, growing sharper with every second."

    if heart < 5:
        jump day7BadEnd 

    label day7GoodEnd:
    
    a sorrow openmouth "\"I'll make them come back and then they'll see. Then they'll be sorry they ever left.\""

    "Ever...left?"

    "Alice's eyes were locked on the cauldron now, burning with a determination that betrayed no hate."
    
    w "\"...Oh...Alice...you don't want to hurt them, do you?\""

    a sorrow "\"Yes I do!\""

    "She snapped at me, the sparks flaring even brighter."

    w "\"No you don't.\""

    "I stood my ground. Well, as well as I could being tied to a banister."
    
    a sorrow openmouth "\"They need to know what they did! They need to know I'm strong. I can take care of myself!\""

    a sorrow openmouth "\"You know that, don't you Ms. Whitley!? You played with me, you know I'm strong! They need to see that too! That I'm...\""

    a sorrow "\"I'm...\""
    
    "She was losing her words. No, that wasn't it. She was finding new ones. Ones she didn't want to say."

    "I helped her."

    w "\"You just want to hear them say it, right? Hear them explain themselves. You want them to give you answers, don't you Alice.\""
    
    "The sparks at her feet dimmed slightly as she averted her gaze." 

    w "\"It's okay, Alice. It's normal. I know it's hard to think about, but something in you keeps asking.\""

    w "\"But you never get a response. Not even Mr. Rabbit can answer your questions.\""
    
    "Tears crept into her eyes and she sniffed and rubbed her nose."

    "Then she turned to me with clenched fists and a set jaw." 
    
    a sad "\"Why?\""

    a sad "\"Why did they lock me away? Why...did they have to go?\""
    
    "Finally, the magic sparks at her feet dissipated and Alice stood before me. Just a girl with sad eyes and a wet face." 
    
    a sad closeeyes "\"I wanted to be a good girl. I wanted to make them happy. So why did they treat me that way? They never trusted me with anything!\"" 
    
    a sorrow openmouth "\"I just want them to tell me WHY!?\""

    w "\"Alice, I'm sorry, I don't have the answers you're looking for.\"" 
    
    "Alice spun away from me, weeping into her hands. Her magic started building around her again, a vortex that fed off her immense pain." 
    
    "I tried to thwart it, calling out to her."

    w "\"But, I know they were trying their best! They were your parents! And they love you-\""

    a sorrow closeeyes "\"YOU DON'T KNOW THAT!\"" 
    
    "The vortex engulfing her spun even faster, harsh red flames licking at her feet."
    
    a sorrow openmouth "\"You don't know anything about them!\""

    w "\"You-You're right Alice. I don't. But I know about Luke.\"" 
    
    "Alice glared at me so intensely, I thought I might burst into flames too."

    a sad "\"Don't you bring him up. You know how horribly he treated me!\""

    a sorrow closeeyes "\"He LEFT ME! He was only friends with me because of his-his stupid FAMILY!\""

    w "\"-because of his PARENTS.\""
    
    w "\"Alice, sometimes parents...don't really know what's best. Sometimes they're bad, and they hurt their family.\"" 
    
    w "\"And sometimes, they're good but - just a little lost. They do what they think is best for their family, but it's wrong.\""
    
    w "\"Like, they tell you that you have to become friends with a stranger...or...\""
    
    a unhappy "\"They hide you away.\""

    "Alice shook her head, as if trying to shake off unwelcome feelings."

    a sorrow "\"But that doesn't give them an excuse! At the end of it all they still shouldn't have done it!\""

    a sorrow "\"My parents shouldn't have locked me away and Luke's parents shouldn't be bossing him around like that!\""

    "Alice came to a halt. For the first time, she felt the warm touch of true compassion escape her lips. True empathy."

    "Her brow furrowed in confusion, and she backed away from the now violently bubbling cauldron."

    "The spell must've been more than halfway done by now."

    w "\"Alice, listen to me.\""

    w "\"Deep down, you know this is wrong. You know how I know that?\""

    w "\"Because you aren't trying to resurrect Aiden.\""

    "That set her off. Blue sparks exploded around her body and she shattered the tiled floor with a deafening stomp!"

    a sad "\"DON'T SAY HIS NAME!\""
    
    "Still, I carried on."

    w "\"He loved you, Alice.\""

    w "\"He loved you. He played with you, He would tell you the most brilliant stories, and he took care of you. And when the time came, he protected you.\""

    w "\"You know what this spell is, you know what it does. And you don't want to hurt him.\""
    
    w "\"You know he wouldn't want you to do this. What would he think of you now?\""

    w "\"Do you really want him to see you like this?\""

    "Alice stared at the ground, tears dribbling down her red cheeks."

    "The spell was nearing completion. I started to feel its power begin to enervate me. But I needed to say more."

    w "\"Alice, Aiden wanted you to be better than your parents. AIDEN wanted you to be better than them!\""
    
    w "\"I'm sorry they don't get to come back. I'm sorry they don't get to change.\""
    
    w "\" But even if they aren't here. Even if they won't get to watch you, they still love you so much.\""
    
    w "\"And I know it's scary, but they wanted you to have this choice! To make the decision...to be - better.\""

    "Alice's gaze was now locked on my, but my sight was wavering. The magic thread that bound me loosened just enough for me to drop to my knees."
    
    "Alice looked at me with the most desperate eyes."

    a guilty "\"I just want them back.\""

    "I weakly reached an arm out towards her."

    w "\"Oh, Alice, I know you do.\""

    a sorrow openmouth "\"Then how come that can't happen!?\"" 

    "Along with the cauldron's ever-building magic, Alice's own powers flared up around her."

    a sorrow openmouth "\"HOW COME YOU GET TO LIVE AND THEY DON'T!? WHY DO I HAVE TO CHOOSE!?\""

    "She waited for me to answer but I had no words. My heart began to slow, the very blood in my veins eased its pace. Only a thread of energy kept my eyes open."
    
    "I collapsed to the floor."
    
    "Alice squeezed her bunny but then suddenly noticed something wrong."
    
    "Mr. Rabbit was burning up in her arms. The magical vortex surrounding her and the cauldron was out of control."
    
    a sad "\"M-Mr. Rabbit?\""
    
    "He gave her no answer while his right ear continued to scorch."

    "Alice looked at the spell, sitting flipped over on the plush, with Aiden's words face up."

    "She sucked in a huge shakey breath, squeezed her eyes shut, then let out a long, piercing wail."

    "The vortex was instantly extinguished and the cauldron vanished in puff of smoke. Then the foyer was silent."

    "I felt my strength start to return. When I finally pushed myself off the floor to stand, I realized Alice was now on the floor."

    "She was sitting down, hugging a singed Mr. Rabbit." 
    
    "I walked over and quietly knelt beside her. She didn't look up from her bunny. Instead she sighed and spoke with a candid rasp."

    a awkward "\"You were right. I want to be a good girl, Mom.\""

    "I put my hand on Alice's shoulder and leaned my head against hers. We'll be okay."

    scene black
    with Dissolve(.5)

    scene bg living room

    "That afternoon, I had my belongings packed and set by the front door. I was going over my mental checklist when I felt a tiny hand tug on my coat."
    
    a sorrow "\"You really can't stay?\""

    "I weakly smiled then swooped her up in a hug."

    w "\"I'm sorry, I really can't. But it's going to be okay. Know why?\"" 
    
    "I pulled back and gazed at Alice intently."
    
    w "\"Because you are a smart, talented, and kind little girl who's going to do amazing things.\""
    
    w "\"You don't have to be scared anymore. You can do this. All you have to do is remember the people who are here for you.\""
    
    "I put a palm over her heart."

    w "\"And the people who will always be with you.\""

    w "\"You'll always have a family from now on.\"" 
    
    "Alice smiled. A broken, childish smile. It suited her."

    "There was a knock at the door. I got up and put my pointer finger to my chin." 
    
    w "\"I wonder who that could be?\""

    "Alice cocked her head at me. I winked at her then looked through the front door's window."

    w "\"It looks like someone wants to see you!\""
    
    "I pulled open the door to reveal -"

    "Luke!"
    
    "Alice instantly hid behind me and gave the boy a sour look. He gulped and took a step back."
    
    "She must've realized she scared him, since she hid behind me a bit more and looked away."
    
    "Then she noticed his arm. There was still a mark from the fire. Alice stuck a little tighter to me."
    
    "I gently rubbed her head."
    
    w "\"Alice, it's okay.\""
    
    "I looked at the boy."

    w "\"Don't you have something to say?\""

    "The boy paused and threw his gaze downwards, shuffling his feet." 

    l "\"...I-I'm sorry. I'm sorry for making fun of you. It was wrong.\""

    "Alice opened her mouth ever so slightly, then looked up at me. I gave her a reassuring nod."

    "She stepped out from behind me and slowly approached the boy."

    a guilty "\"I'm sorry too. A-About the fire.\""

    a guilty "\"Do you...would you still like to be friends?\""

    "The boy scratched at his burn mark and bit his lip, but didn't step away."

    l "\"Yeah.\""

    "Alice looked at him with wide eyes."

    l "\"But only if you let me talk to you about my rock collection again.\""

    "He give her a small, innocent smirk. Alice had the biggest grin on her face."

    a happy closeopen "\"Of course!!!\""

    "Together they ran off to the playroom."

    "At that moment, there was a knock at the door. That must be..."
    
    "I opened the door to greet two older-looking women. These must be Alice's godparents."

    "One asked-"

    "\"Are you the nanny?\""

    w "\"Yes, that's me. I suppose Alice is all yours now?\""

    "They smiled and nodded."

    w "\"Well, I will warn you, she can be quite the handful\""

    "One of the women boisterously laughed."

    "Godparent 1" "\"Oh shouldn't be too much of a problem. We've got four hands between us!\""

    "The other woman, who seemed to be the more down-to-earth of the two patted my hand."

    "Godparent 2" "\"What she means to say, is we'll take good care of her. Although, I do hope she's used to getting spoiled\""

    "Godparent 2" "\"THIS one over here wouldn't stop yammering on about all the things she wanted to give her.\""

    "The other woman grinned and crossed her arms."

    "Godparent 1" "\"I'd give her the world if I could!\""

    "I smiled. Yeah. Alice will be okay."

    "I bid my farewell, gathered my things, and finally stepped foot outside the mansion. The air out here felt unreal."

    "I took a deep breath."

    "Then I turned around to see Alice meeting her new godparents through the window."

    "They both were bent down, telling her something."

    "Suddenly Alice beamed then sprinted towards them and hugged them both tight. A warm smile graced my lips."

    "Then, Alice returned to her game with Luke."

    "It looks like they had been playing Osellets. Or as I like to call it, Jacks."

    jump day7finaldone

    label day7BadEnd:

    "I tried to tear away from the banister, but Alice's magic was too powerful. Under a loud, sonorous noise, I watched Alice complete spell."

    "Immediately I felt my very lifeforce began to sap towards the cauldron. Alice looked at me with a pitiful smile and glazed eyes."

    a happy strange "\"It's such a shame you won't get to meet them.\""

    label day7finaldone:

    scene black

   