# Some variables used in day1
default closeeye = True

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve

label day1:
    $ timer_range = 0
    $ timer_jump = 0
    $ day1has_bone = False
    play music morning
    "With a new day came a new case."
    "I, Detective Whitley Leveret, was in charge of uncovering the Hearts family's case."
    "The Hearts were a prosperous bunch, with two loving parents and an adorable child."
    "However, in this time of civil unrest, the parents disappeared without a trace. Some said they were killed in the protests at night, but rumor has it that they dabbled in black magic..."
    "My goal was to sift through these rumours and find the truth."
    play sound "/audio/soundeffects/fire_burning.wav" fadein 2.0
    "The most prolific rumor though, has been that they burned in a house fire."
    stop sound fadeout 6.0
    "When the firemen arrived, the house was untouched."
    "A huge ornate mansion..."
    "With a single little girl inside."
    "After that night, multiple others were declared missing."
    "The police had already declared the case cold. It happened back in May, but something about it just didn't sit right with me."
    "Where did all those people go? Did the parents have something to do with it? None of the people seemed to have much in common, aside from living in the same area."

    "So today, on December 7th, 1968, I was on my way with these questions in mind to the heart of this mess: to the Hearts' Paris Mansion."

    "I was almost there, but before I arrived, I decided to review the details of the case first."
    play sound "/audio/soundeffects/page_turn.wav" fadein 2.0
    "I took out the familiar letter."
    "\"I'll be going undercover in this case. Once I reach that mansion, I will become the temporary Nanny Whitley, a young college student looking after the orphaned Alice Hearts for some quick cash.\""
    "Apparently, the old nanny left suddenly, giving me an opening to explore the mansion. However, I only had seven days to snoop around before Alice's godparents arrive and clear me out."
    "But I was sure that should be more than enough time."

    scene bg front with Dissolve(2)
    play sound_little "/audio/soundeffects/morning_bird.wav" fadein 3.0

    $ day = 1
    show screen Day with Dissolve(2)
    $ renpy.pause(3, hard=True)
    hide screen Day with Dissolve(4)
    ##play sound_little "/audio/soundeffects/morning_bird.wav" fadein 3.0 fadeout 3
    "The mansion was a very grand mansion in the middle of Grigny, a small town in the suburbs of Paris. A blooming flower in a field full of weeds."
    "Near the mansion gates was a young girl dressed in a simple blue dress and holding onto an overstuffed life-sized white rabbit."
    play sound "/audio/soundeffects/outside_footsteps.wav" fadein 2.0
    "I placed the letter back into my pocket, and exited the car. I hurriedly walked towards the girl, carrying my luggage over the overturned gravel suffering from last night's protest."
    stop sound fadeout 1.0
    stop sound_little fadeout 5.0
    w "\"Hello Alice. I'm Whitley and I'll be taking care of you for the next seven days.\""
    "Alice curtsied, trying to appear like a grown up."
    a normal "\"Hello Ms. Whitley. I am Alice Hearts and this is Mr. Rabbit!\""
    transform imgcenter:
        xalign 0.5 yalign 0.5
    show bunny at imgcenter
    with Dissolve(0.5)
    "She held up the rabbit she was holding."
    hide bunny with Dissolve(0.5)
    "Alice then burst out smiling and tackled me with a hug!"

    a happy "\"Yay, a friend! Are you here to play with me? You must be. I've been soooo bored! Let's go play!\""
    "I was surprised by her cheerfulness. Her circumstances weren't anything I envied."
    "But I suppose, in the end, she's still just a kid."

    menu:
        "Don't play with Alice":
            jump day1c1a1
        "Play with Alice":
            jump day1c1a2


label day1c1a1:
    "I slowly released myself from Alice's embrace and placed my luggage in between us."
    w "\"How about you let me put away my stuff first?\""
    "I looked at the mansion"
    "...And maybe give me time to look around the place."
    a annoyed "\"No! Ms. Whitley has to play with Alice first!\""
    "Alice crumpled her dress and looked down with a sour face."
    a sad "\"No one wants to play with Alice anymore... Auntie left without saying goodbye... and Mom...Dad...they...\""
    "Ah, she looks like she's going to cry. Being in a big mansion without anyone around must be really lonely and the memory of her parents leaving is still fresh."

label day1c1a2:
    "Maybe if I play with her, I might learn some things that I wouldn't otherwise. After all, she is a primary source of information."
    w "\"Okay, okay. I'll play with you.\""
    a happy "\"Really? Let's go inside so we can play a game!\""
    play sound_sec "/audio/soundeffects/Fast_Footsteps.wav" fadein 2.0
    play sound "/audio/soundeffects/outside_footsteps.wav" fadein 2.0
    stop music fadeout 2.0
    "Alice dragged me into the mansion and took us into the grand foyer. She then scattered some metal pieces and rushed up to me."
    stop sound_sec fadeout 1.0
    stop sound fadeout 1.0
    show black with Dissolve(1)
    scene bg foyer with Dissolve(1)
    hide black with Dissolve(1)
    play music lunch fadein 1.0
    a normal "\"Before we start, you have to close your eyes!\""
    menu:
        "Close eyes all the way":
            show black with Dissolve(1.0)
            hide black with Dissolve(1.0)
            show black with Dissolve(1.5)
            jump day1c2a1
        "Close eyes partially":
            $ closeeye = False
            show black with Dissolve(0.8)
            hide black with Dissolve(0.8)
            show black with Dissolve(1.0)
            hide black with Dissolve(2.0)
            jump day1c2a2

label day1c2a1:
    "I'll do as she said. If I want to get any information out of her, I need Alice to trust me."
    w "\"Closing my eyes.\""
    a happy "\"Hehe, it'll only take a minute!\""
    "I heard a little twinkling and a whooshing wind. My luggage was next to me, but I couldn't feel it anymore. Instead I felt a large wall by my side. I didn't move around, and I couldn't hear Alice moving my luggage away. Something's not right…"
    a normal "\"Are your eyes closed, Ms. Whitley?\""
    w "\"Pfft, yes they are. Don't you trust me Alice?\""
    a happy "\"I do! I do!\""
    "What a cute kid."
    jump day1playr1

label day1c2a2:
    "Something's off about this situation, so I should try to observe my surroundings as best as I can."
    w "\"My eyes are closed.\""
    a happy "\"Okay, here goes!\""
    show bunny at imgcenter with Dissolve(1.0):
        subpixel True
        zoom 1.0
        pause(1.0)
        ease 1.5 zoom 1.200
        pause(0.2)
        ease 1.5 zoom 1.500
        pause(0.2)
        ease 1.5 zoom 1.800
    "I slightly opened my eyes and scanned the room. To my astonishment, Alice's stuffed white rabbit grew bigger and bigger."
    hide bunny with Dissolve(1.0)
    a normal "\"Ms. Whitley, did you close your eyes?\""
    w "\"Of course they're closed Alice.\""
    a happy strange "\"If that's what you say…"
    "Does she know that I didn't close my eyes?"

label day1playr1:
    a normal "\"Okay, you can open your eyes now!\""
    if closeeye == True:
        hide black with Dissolve(2.0)
        show black with Dissolve(1.0)
        hide black with Dissolve(0.8)
    "I opened my eyes fully and was shocked! Everything was just so... so big!"
    "I thought there was a wall beside me, but it was only my luggage. The stuffed white rabbit Alice was carrying was now the size of a small skyscraper."
    "I scanned for the metal pieces Alice laid down earlier and noticed they were now as large as ourselves. Instead of everything becoming larger...maybe we shrunk."
    a happy "\"Hehe, is Ms. Whitley surprised?\""
    w "\"I'm very surprised. Is this part of play time?\""
    a normal "\"Yep! I want to play a game that I used to play with my parents: Osellets.\""
    w "\"Osellets?\""
    a "\"Yep, it's where you have these small metal pieces. See the red one? You throw that one up and then try to catch as many as the other metal pieces and then catch the red piece.\""
    a "\"If the red piece touches the ground, you lose and the other player gets to have a turn.\""
    "So basically Jacks."
    a sad "\"Mom and Dad always played by the old rules, but that's boring. So now we're going to play it my way!\""
    w "\"Oh?\""
    a happy "\"The red piece is going to drop on the floor. Before it drops on the floor, we're going to race to see who can catch all regular pieces!\""
    menu:
        "Tell Alice you're too tiny to play":
            jump day1c3a1
        "Go along with Alice's antics":
            jump day1c3a2

label day1c3a1:
    w "\"But Alice, how can we catch all the pieces if we're so tiny?\""
    stop music fadeout(3.0)
    "Alice smiled amusingly."
    a happy strange "\"Why don't you try first, Ms. Whitley?\""
    w "\"That doesn't answ-\""
    play music "/audio/BGM/Scary_BGM.wav" fadein 2.0
    a "\"Look the red piece is in the air! The game's already starting.\""
    "I looked up and lo and behold, the red piece was thrown in the air. But who did that? Alice and I weren't near it."
    "I looked back at Alice, who was already next to a regular piece. Once Alice touched the metal piece, it shrunk until it fit in Alice's palm."
    "So that's how we can get the pieces. I looked around for any more pieces, but it seemed like there was only one."
    a "\"I won this round! Teehee! Better luck next time, Ms. Whitley!\""
    jump day1playr2

label day1c3a2:
    w "\"Sounds like a fun game! Let's see who wins.\""
    stop music fadeout(1.0)
    a happy "\"Yeah!\""
    play music "/audio/BGM/Scary_BGM.wav" fadein 2.0
    "I looked for the red piece. It lingered on the ground for a second before shooting up."
    play sound "/audio/soundeffects/whitley_run.wav" fadein 1.5
    "I ran towards the nearest metal piece, stretching out my arm to grasp it."
    stop sound fadeout 2.0
    "Before I could wonder how I was going to catch it, the metal piece mysteriously shrunk to its original size in my palm."
    "I turned around towards Alice and handed her the metal piece. She looked up at me with surprise and awe."
    w "\"Looks like it's my win.\""
    a "\"Wow, you're so fast Ms. Whitley!\""
    a happy strange "\"But can you win in the next round?\""

label day1playr2:
    "Alice threw the metal piece away from us. Once the metal piece settled, it returned to its original size."
    "There was another metal piece a little farther away...when did it get there?"
    "I eyed the red metal piece, ready for the second round to start."
    "Alice tapped my shoulder, but I only glanced at her. I was too focused on the game itself."
    a happy "\"Ms. Whitley, it's question time! What's your favorite food?\""
    $ time = 2
    $ timer_range = 2
    $ timer_jump = 'day1c4a1'
    show screen countdown
    menu:
        "Don't have a favorite food":
            hide screen countdown
            jump day1c4a2
        "Food":
            hide screen countdown
            jump day1c4a3

label day1c4a1:
    "I mulled over many different meals."
    w "\"Well, soupe à l'oignon is good. Ratatouille is also a wonderful dish. Do desserts count?\""
    "Wait, why am I so focused on this one question? We're in the middle of a game."
    "I looked for the red piece, the signal from the start of the round. It was already up in the air and starting its descent. Alice also already had one metal piece."
    play sound "/audio/soundeffects/whitley_walk.wav" fadein 1
    "I walked towards Alice to congratulate her on her soon-to-be victory, when I stumbled across a small metal piece."
    stop sound fadeout 1.5
    "I picked it up and looked up towards Alice who was still running to the second big metal piece before the red piece fell."
    "That's strange. I mulled over the piece, it was much more worn out and cracked than the ones that they were playing with."
    a happy "\"Heehee~ I'm the winner! Looks like you'll have to try harder Ms. Whitley!\""
    "I pocketed the piece and looked up to Alice."
    $ day1has_bone = True
    jump day1playr3

label day1c4a2:
    w "\"I don't have a favorite food.\""
    a confused "\"W-what you must have one!\""
    "I patted Alice's head. I probably do have a favorite food, but I can't be distracted from the game."
    jump day1playr2cont

label day1c4a3:
    w "\"Food.\""
    "One of the worst answers, but I had to keep my focus on the red piece."
    jump day1playr2cont

label day1playr2cont:
    play sound "/audio/soundeffects/whitley_run.wav" fadein 1
    "Once the red piece was thrown into the air by some mysterious force, I sprinted towards the two pieces."
    stop sound fadeout 1.5
    "I caught one before I launched myself to the other one, capturing it too. I triumphantly turned around to Alice."
    w "\"Guess I'm too fast for little Alice?\""
    "Alice stomped towards me, ready to throw a tantrum."
    a annoyed "\"Ms. Whitley, you didn't answer my question properly!\""
    w "\"Well, I wasn't the one trying to trick my opponent into forgetting that we're in a game.\""
    "Alice puffed up her cheeks and crossed her arms."

label day1playr3:
    "I was so absorbed in the game that I forgot I was here to recover the truth. Curse my competitive streak, or maybe it was something about Alice's nature that enticed me to play? Well, she did {i}force{/i} me to play."
    "But now let's see if I can get some information out of her."
    w "\"Since you asked me a question, why don't you answer a question of mine?\""
    a sorrow "\"Hmm, I don't know~ After all, Ms. Whitley didn't answer my question properly.\""
    "Alice tried to appear casual, but her eyes were trained on the now three metal pieces on the floor as well as the red piece that was about to be thrown upwards."
    "She was distracted from me. Time to ask a crucial question now while her emotional guard is down."
    menu:
        "What's your favorite game?":
            jump day1c5a1
        "What's your favorite food?":
            jump day1c5a2
        "What are you up to?":
            jump day1c5a3

label day1c5a1:
    "She really likes to play, so maybe I should ask what's her favorite game. It might give me insight into what she's like or how life was with her parents."
    w "\"You seem to enjoy plaing, so do you have a favorite game?\""
    "Alice turned eerily and smiled at me."
    a happy strange "\"It's a surprise for the seventh day.\""
    "The seventh day? That's the day I leave and her godparents arrive. But that doesn't give me much else. Maybe it has something to do with food?"
    jump day1playr3cont

label day1c5a2:
    "Let's turn the same question on to her. After all, maybe she already has an answer and was hoping I would ask her too."
    w "\"Hmm, do you have a favorite food?\""
    "Alice looked at me with hungry eyes."
    a happy "\"Lapin a La Cocotte! My parents' rabbit stew was the best.\""
    "Well, I didn't expect that. A big white rabbit plushie, rabbit stew... I wonder if she has some sort of affection for rabbits."
    jump day1playr3cont

label day1c5a3:
    "I wonder if there's deeper meaning to everything Alice has done today."
    w "\"What are you up to?\""
    "For just a second, Alice froze and her smile disappeared."
    a annoyed "\"What do you mean Ms. Whitley? I'm just trying to win this game.\""
    "I should drop the subject. It looked like she wouldn't want to talk anymore."
    jump day1playr3cont

label day1playr3cont:
    a annoyed "\"Whitleeeey~ Are you even trying? You didn't even pay attention in the last round!\""
    "Alice dropped all three metal pieces in front of me."
    w "\"Oh, is the round over? Sorry about that, I wanted to learn more about you.\""
    "Which is technically not a lie even if I have ulterior motives."
    w "\"To make it up to you, let's play another round. I bet I'll win.\""
    "Alice nodded her head side to side."
    a sad "\"We can't play another round. I only have three metal pieces. I lost the other ones.\""
    if day1has_bone:
        "I clutched the broken metal bone in my pocket. For some reason, it feels like a bad idea to say I have another one in my hand."
        w "\"That's too bad.\""
        "Alice sadly smiled at Whitley."
        a happy strange "\"Yeah...if only there was another one.\""
        jump day1end
    w "\"Don't worry about it. It was a fun three rounds! And you're the winner of the day because you won the most important last round!\""
    a happy "\"Hehe, I'm the winner!\""

label day1end:
    stop music fadeout 2.0
    "Well, all in all, I was glad we were done with the game. I don't think I could have handled it any more."
    play music lunch fadein 2.0
    a normal "\"Ms. Whitley, I'm tired, carry me to bed!\""
    w "\"Okay, okay. Whatever you wish for your highness.\""
    a happy "\"Hehe~\""
    "I picked up Alice and froze. There were two uncertainties: 1)  I didn't know where Alice's bedroom was and 2) how were we going to move around if we were still tiny compared to the house."
    "I panicked internally, thinking about all the stairs I had to scale and the tall bed that would be impossible to climb. Alice pulled at my shirt, trying to get my attention."
    a confused "\"Why aren't you moving. My bedroom is that way.\""
    "I looked in the direction Alice was pointing towards and to my amazement, everything looked normal. I didn't know when we returned to our original human size, but I'm glad that's one question answered."
    play sound "/audio/soundeffects/whitley_walk.wav" fadein 1 
    "I followed Alice's pointing figure and we soon arrived at her bedroom where I tucked her in for bed. I got up and tried to leave the room, but Alice tugged on my shirt again."
    stop sound fadeout 0.5
    pause(0.5)
    play sound "/audio/soundeffects/open_bedroom_door.wav" fadein 1 
    show black with Dissolve(1)
    scene bg alice_bedroom with Dissolve(1)
    hide black with Dissolve(1)
    a sad "\"Won't you stay? I don't want to sleep by myself.\""
    menu:
        "Stay and sleep with Alice":
            jump day1c6a1
        "Go to your own room.":
            jump day1c6a2

label day1c6a1:
    "Now that someone's here, she probably doesn't want to be alone for a single moment."
    w "\"Just for tonight, okay? You're a big girl, so you should be able to sleep by yourself.\""
    a happy "\"Yay!\""
    "Alice scooted and gave me space where I tucked in. The bed was nice and cozy, the right environment for the tired Alice to fall asleep instantly."
    "I couldn't fall asleep as easily because the protests from outside were still going strong. Seems like the police and college students are clashing again."
    a asleep "\"...Whitley don't go...\""
    w "\"Huh?\""
    w "\"I guess Alice is sleeping talking.\""
    a "\"...stay...meet my parents...zzz.\""
    "Well that doesn't make sense. Alice's parents are gone, so there's no way I can meet them. Poor kid, she probably misses them very much."
    "Mhmm, seems like I'm tuckered out for the day. I hope the next few days will be just as peaceful and playful as today."
    stop music fadeout 3.0
    show black with Dissolve(2)
    pause(3)
    jump day2

label day1c6a2:
    w "\"I'm sorry Alice. I still have to unpack. Besides, you're a big kid now, you should be able to sleep by yourself.\""
    a sad "\"...okay.\""
    "Alice retracted her hand and slumped back into her bed. I'm sorry Alice, but I need some time to myself...to figure out what's going on."
    a happy "\"Before you go, take that with you.\""
    "Alice points to a red envelope on the dresser."
    a asleep openmouth "\"A thank-you for playing with me today. I hope you like it...zzz\""
    "I took the red envelope, investigating it to make sure there was nothing harmful."
    w "\"Thank you Ali-- Oh, it looks like you're asleep already. Well, good night Alice. Sweet dreams.\""
    play sound "/audio/soundeffects/open_bedroom_door.wav" fadein 1
    show black with Dissolve(1)
    scene bg hallway with Dissolve(1)
    hide black with Dissolve(1)
    play sound "/audio/soundeffects/page_turn.wav"
    "I closed the door behind me and opened up the envelope. Inside was a drawing of Alice...me and to other figures who appear to be her parents."
    show home at truecenter with Dissolve(1)
    "A cute drawing if only it wasn't for the red string. Alice was holding onto it while it wrapped all around her parents and me."
    hide home with Dissolve(1)
    "I folded the drawing and placed it into my coat pocket."
    "Hopefully the next six days will be less eventful so I can do some actual work."
    stop music fadeout 3.0
    show black with Dissolve(2)
    pause(3)
    jump day2
