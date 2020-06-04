label day2:

    scene bg whitley_bedroom with Dissolve(2)

    play music morning fadein 1.0

    $ day = 2

    show screen Day with Dissolve(2)
    $ renpy.pause(3, hard=True)
    hide screen Day with Dissolve(4)

    "The warm sunlight greeted me for the new day."

    w "\"Urghh\""

    "A soft groan escaped my lips. I wasn't expecting to be so tired, but I guess that game of magical Jacks was both mentally and physically draining."

    "I rolled off the side of the bed and onto my feet. Time for another day of caretaking and mystery."

    play sound "audio/soundeffects/open_bedroom_door.wav"

    show black with Dissolve(1)

    scene bg hallway with Dissolve(1)

    hide black with Dissolve(1)

    a happy "\"Hi Ms. Whitley!\""

    "I was met with a cheery voice."

    a normal "\"How did you sleep last night? You didn't get any nightmares did you?\""

    w "\"I‒\""

    a happy "\"Come with me, Ms. Whitley! We're going to play again!\""

    play sound_sec "/audio/soundeffects/Fast_Footsteps.wav" fadein 2.0
    play sound_little "/audio/soundeffects/run_concrete.wav" fadein 2.0

    "She dragged me by the hand through the hallway, down the stairs, and outside into the mansion's backyard."

    stop sound_sec fadeout 1.0
    stop sound_little fadeout 1.0

    show black with Dissolve(1)
    scene bg backyard with Dissolve(1)
    hide black with Dissolve(1)

    a normal "\"Here we go!\""

    "On the ground right outside the backyard doors lay a bucket full of white chalk. A very sizeable bucket, I may add. There was enough chalk to draw lines on a new road."

    "Fittingly, there was a large area of concrete in the backyard."

    a smile "\"Huff huff..\""

    "Alice heaved the bucket, which was half her size, towards the center of the concrete."

    a happy "\"Are you ready to play? We are going to have loooooots of fun today too!\""

menu:

    "Play with Alice":
        jump day2play

    "Don't play with Alice":
        a happy "\"That's too bad! You're going to play with me anyways!\""

        "I guess I'm going to play with her regardless of choice."


label day2play:

    w "\"I'm ready!\""

    "Before I even spoke, Alice was already on the ground, tracing boxes and boundaries."

    a normal "\"Un, deux, trois…\""

    "She was numbering the boxes, and I came to realize that we were about to play hopscotch."

    a happy "\"Have you ever played Marelle before, Ms. Whitley?\""

menu:

    "What's Marelle?":

        jump day2c1a1

    "Isn't this hopscotch?":

        jump day2c1a2

label day2c1a1:

    a nervous "\"You don't know what Marelle is?\""

label day2c1a2:

    w "\"Marelle? In my country, we call this hopscotch.\""

    a happy "\"Oh that's interesting! Where are you from? I thought your accent sounded funny!\""

    w "\"Well, that's not the most polite way to ask, but I'm British.\""

    a happy closeopen "\"Then today you learn how we play in France!\""

    "She beamed."

    a guilty "\"The last time I played Marelle was when my parents were alive.\""

    "She seemed to shake away the sudden, sad memory."

    a happy closeopen "\"Anyways, this is going to be fun! Here we go!\""

    "I held my breath, anticipating the unknown."

    stop music fadeout 3

    #(Transition to dream world)

    show black with Dissolve(1)

    a happy "\"We're here!\""

    "I opened my eyes."

    scene bg floating_squares with Dissolve(1)

    hide black with Dissolve(1)

    $ renpy.music.set_volume(0.6, delay=0, channel='music')

    play music "audio/BGM/Game_music.mp3" fadein 2

    "This time, we stood upon a wide concrete square surrounded by complete black."

    "There was another concrete square a few meters in front of us, but that was the only other thing existing in this realm besides us and the ground we were standing on."

    a normal "\"Are you ready to play?\""

    "She looked straight through my eyes. I chuckled."

    w "\"You've asked me this before. I'm ready.\""

    play sound "audio/soundeffects/walk_concrete.wav" fadein 1.0

    "Curious, I walked forward to inspect the other squares. I took a step forward, putting my foot where half of it was on the concrete and half of it was not."

    stop sound fadeout 1.5

    "I almost instantly regretted this decision."

    "The front of my feet lacked any form of surface contact. I lurched backwards on reaction, realizing that anywhere that was not part of the squares dropped into the everlasting black abyss."

    a happy closeopen "\"I'm ready too!\""

    "As soon as she said that she did a running start, ready to make the jump over the divide!"

    w "\"ALICE NO!\""

    "I desperately called after her, but it was too late. She had jumped."

    "Yet, my eyes were graced by something unimaginable."

    "She had done a full frontal somersault, somehow floating and defying gravity all while landing on her two feet on the square in front."

    "She turned around."

    a happy "\"Easy! Your turn, Ms. Whitley!\""

    "She looked at me expectantly."

    "I don't think this is actually how they did it in France."

menu:

    "Make the jump":

        jump day2jump1

    "Stand your ground":

        jump day2stand

label day2jump1:

    "I got off the ground and steadied my breath."

    w "\"Here goes nothing.\""

    play sound "audio/soundeffects/run_concrete.wav" fadein 1.0

    "I ran as fast as I could and leapt to the next square."

    scene bg floating_squares:
        subpixel True
        center
        linear 0.3 yalign 0.05
        ease 1.5 zoom 2

    pause(1)

    show black with Dissolve (0.5)

    stop sound fadeout 1.5

    pause(2)

    hide black

    play sound "audio/soundeffects/body_fall.wav"

    scene bg floating_squares at center, Shake(None, 1.0, dist=20)
    with Dissolve(1)

    "I couldn't make the jump. Instead, my stomach crashed into the concrete platform and I immediately started falling."

    "I desperately flailed my arms to grab onto anything to stop my momentum. I did not expect anything to grab onto me."

    a normal "\"Up we go.\""

    "Alice pulled me up by the forearm with ease and dropped me onto the new platform."

    "I looked at her, wide-eyed. How did this girl gain monstrous strength all of a sudden?"

    "That's right. I'm in a different world. I have to suspend my beliefs here."

    a smile "\"Wasn't that fun?\""

    "Breathless, I nodded."

    w "\"Y-Yeah, I guess.\""

    "Alice laughed."

    a happy closeopen "\"Hee-hee! I knew you would enjoy this. Let's keep on going.\""

    "There was another platform in front of us. Oh, not again."

menu:

    "Make the jump again":

        jump day2jump2

    "Stand your ground":

        jump day2stand

label day2jump2:

    a sad "\"Why don't you try going first this time.\""

    "No way. I'm not going to do that."

    "Alice looked at me with big, pitiful eyes. I sighed."

    w "\"Just for you.\""

    a happy closeopen "\"Yay! Good luck and don't die!\""

    "I braced myself and made the jump again."

    play sound "audio/soundeffects/run_concrete.wav" fadein 1.0

    scene bg floating_squares:
        subpixel True
        center
        linear 0.3 yalign 0.05
        ease 1.5 zoom 2

    pause(1)

    show black with Dissolve (0.5)

    stop sound fadeout 1.5

    pause(2)

    hide black

    scene bg floating_squares at center, Shake(None, 1.0, dist=20)
    with Dissolve(1)

    play sound "audio/soundeffects/body_fall.wav"

    "*Thud!*"

    "I'm once again hanging on for dear life."

    a annoyed openeyes "\"Awww Ms. Whitley. Do I have to help you every time?\""

    "Once again, I am saved by this little girl."

    a happy "\"This time, there's two choices ahead! Maybe you could go on one, and I could go on the other.\""

    "This is getting ridiculous."

menu:

    "Make the jump again (again)":

        jump day2jump3

    "Stand your ground":

        jump day2stand

label day2jump3:

    "I was breathing heavily at this point."

    w "\"I'll do it, as long as you promise to go to bed early tonight Alice.\""

    a normal "\"Don't be such a stick in the mud! Though, I guess we'll {i}have{/i} to go together this time.\""

    w "\"Thanks... Huh? Did something happen?\""

    a smile "\"Something is about to.\""

    "She pointed towards one of the two platforms in front of us."

    "At first I couldn't see anything, but a glimmer in the corner of my eye caught my attention. The glimmer grew in size, and then I realized what was happening."

    image meteor = im.Alpha("white.png",1)

    transform glimmer_grew(start, end):
        alpha start
        linear 1.0 alpha end

    show meteor at glimmer_grew(0, 0.1)

    "A meteor was about to crash into the platform."

    w "\"Alice we need to get out of here before that meteor comes!\""

    show meteor at glimmer_grew(0.1, 0.2)

    a normal "\"Oh don't worry about it. It won't hit us.\""

    w "\"Even if it didn't, the impact would blast us away!\""

    show meteor at glimmer_grew(0.2, 0.4)

    a happy "\"We're in my world! I'll decide whether or not it will.\""

    show meteor at glimmer_grew(0.4, 1)

    pause(2)

    scene bg floating_squares at center, Shake(None, 2.0, dist=20)
    with Dissolve(2.0)

    hide meteor

    pause(0.5)

    "And just like that, the meteor landed, shattering the entire platform. And just as she said, there was no effect of the impact on us."

    a happy closeeyes "\"See?\""

    a happy "\"Now, are you ready to move on to the next platform?\""

menu:

    "Make the jump again (again (again))":

        jump day2jump4

    "Stand your ground":

        jump day2stand

label day2jump4:

    play sound "audio/soundeffects/run_concrete.wav" fadein 1.0

    scene bg floating_squares:
        subpixel True
        center
        linear 0.3 yalign 0.05
        ease 1.5 zoom 2

    pause(1)

    show black with Dissolve (0.5)

    stop sound fadeout 1.5

    pause(2)

    hide black

    play sound "audio/soundeffects/body_fall.wav"

    scene bg floating_squares at center, Shake(None, 1.0, dist=20)
    with Dissolve(2.0)

    "Another round of me struggling and Alice making it cleanly to the other side."

    a happy closeopen "\"We made it! We're here!\""

    "I looked around."

    w "\"There's nothing here. Why did we come here?\""

    a normal "\"Because here is the secret base where me and my parents used to play.\""

    "I looked around again and saw nothing."

    show black with Dissolve(0.8)

    hide black with Dissolve(1)

    show black with Dissolve(0.8)

    scene bg grassfield with Dissolve(3)

    hide black with Dissolve(3)

    "But when I blinked, the gray concrete and black sky had changed."

    "Replacing it was a clear sunny sky and a flowing grass field. Towers upon towers of books lay upon this field, many clearly read through and torn apart, but many more unscathed and unopened."

    "Curiously, one of the books was one I recognized in the mansion's library."

    a happy "\"Over here!\""

    "Alice beckoned me to a hole within the sea of books."

    a normal "\"I used to hide here when my parents and I played hide and seek here. I hid with Mr. Rabbit to keep me safe.\""

    w "\"I'm sure a friend like him would keep some nice company.\""

    "Alice smiled."

    a smile "\"He sure does! Here, do you want to hold him?\""

    w "\"I would love to.\""

    transform imgcenter:
        xalign 0.5 yalign 0.5

    show bunny at imgcenter with Dissolve(0.5)

    "Alice handed me the bunny she had carried with her the entire time."

    hide bunny with Dissolve(0.5)

    a happy "\"Make sure you take good care of him! I'm going to go look for a book for us to read.\""

    "Alice ran away while I held Mr. Rabbit."

    show bunny at imgcenter with Dissolve(0.5)

    "I looked at the bunny. It was a very soft and cute bunny. I could now understand why she would hold on to the bunny so much. It represented the only \"family\" she had."

    hide bunny with Dissolve(0.5)

    qb "\"{i}How Charming.{/i}\""

    w "\"Huh? Who said that?\""

    qb "\"{i}You Don't Belong Here.{/i}\""

    show red at glimmer_grew(0, 0.3)

    "Worried, I looked around for Alice. It was then that I noticed the books...were {i}bleeding{/i}."

    "Every single one of the books around me was oozing what I could only think of as blood."

    "I held onto the bunny, trying to keep it safe for Alice."

    w "\"Alice!? ALICE?!\""

    "I called for Alice."

    "But there was only silence."

    show red at glimmer_grew(0.3, 0.5)

    "The blood began flowing across the field, encompassing everything including myself. I was swept away and pulled beneath the surface of the fluid, desperately holding onto Alice's hope."

    "I blacked out."

    show black with Dissolve(1)

    hide black with Dissolve(1)

    scene bg grassfield_red with Dissolve(1):
        subpixel True
        center
        linear 1.0 yoffset 0
        ease 1 zoom 3

    pause(0.5)

    play sound "audio/soundeffects/body_fall.wav"

    scene black with Dissolve(0.2)

    jump day2end

label day2stand:

    w "\"Alice it's too dangerous!\""

    "I yelled at her while beckoning her back. She gave me another pout, but this time, I wasn't having it."

    w "\"Please, come back. This is getting out of hand!\""

    "Her innocent pout screwed into a dark glare."

    a smile "\"You're no fun. This game is over.\""

    scene bg floating_squares at center, Shake(None, 100, dist=20)

    "All of a sudden the realm started rumbling. The ground I was on began shaking and cracking apart."

    w "\"Alice? What is going on?\""

    a happy strange "..."

    scene bg floating_squares:
        subpixel True
        center
        linear 1.0 yoffset 0
        ease 1.0 zoom 3

    pause(1)

    scene black with Dissolve(1)

    "I looked at her for answers, but I received nothing but the same glare as I fell into the pit of despair."

label day2end:

    stop music fadeout 3

    pause(4.5)

    $ renpy.music.set_volume(1, delay=0, channel='music')

    jump day3
