default yalign_var = 0.6
image timebox = "timebox.png"

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign yalign_var xmaximum 300 at alpha_dissolve

screen Time:

    frame at alpha_dissolve:

        xmaximum 340
        ymaximum 300
        xalign 0
        yalign 0
        background "timebox"

        if minute < 10:

            text "{size=+30}{font=fonts/Paris 1920 Script.ttf}[hr] : 0[minute]{/font}{/size}" xpos 0.3 ypos 0.8

        else:

            text "{size=+30}{font=fonts/Paris 1920 Script.ttf}[hr] : [minute]{/font}{/size}" xpos 0.3 ypos 0.8


label day6:

    default pillowchecked = False

    default gohallway = False

    default wandfound = False

    default mirrorchecked = False

    default translated = False

    default firstgoout = True

    default firstoption2 = True

    default scenechange = False

    default firstfirstforkleft = True

    default firstfirstforkright = True

    default firstsecondforkleft = True

    default firstsecondforkright = True

    default firstthirdforkleft = True

    default firstthirdforkright = True

    default option7readingclue = True

    default win = False

    default hr = 6

    default ohr = 0

    default minute = 20
    
    default omin = 0

    default timetakentowin = 0

    default winningstring = ""

    init python:
        def addmin(value):

            global minute,hr

            ohr = hr
            omin = minute

            if minute + value >= 60:

                while hr!=ohr+1 or minute!= omin + value - 60:

                    minute += 1

                    if minute == 60:
                    
                        hr += 1
                        minute = 0
                
                    renpy.pause(0.05)

            else:

                while minute!= omin + value:

                    minute += 1
                
                    renpy.pause(0.05)

            if hr == 7 and minute >= 30:

                minute = 30

                renpy.jump("breakfast")

            return

    scene bg whitley_bedroom

    show black

    play sound "audio/soundeffects/Fast_Footsteps.wav" fadein 2.0

    "The next morning, I was awakened by the noise of rapid footsteps."

    stop sound fadeout 1.0

    "I sat up to see the room was dark and the curtains were drawn."

    hide black with Dissolve(2)

    "My head was hurting... Did I draw the curtains last night?"

    play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

    "Someone opened the bedroom door."

    a "\"Hi Ms. Whitley! Glad to see you slept well last night. Have you seen Mr. Rabbit?\""

    w "\"No... I just wake up. Is he missing?\""

    a annoyed "\"He said he wanted to play with you and snuck away in the early morning. That tricky rabbit!\""

    "She didn't look as worried as she did a few days earlier. Was this part of her game?"

    "What should I say?"

    menu:
        "Do you want to play today?":
            jump day6_option1a

        "He must be very good at playing games.":
            jump day6_option1b

    label day6_option1a:

        "An idea popped in my head. I wondered if Alice would play without her rabbit."

        w "\"Why don't we play instead? Take your mind off it.\""

        "Alice stamped her feet. She looked anxious. She was hiding something for sure."

        a annoyed "\"I don't want to play with you this time. Can you help me find Mr. Rabbit? He's got to be hiding somewhere in the house!\""

        "The stress in her voice wasn't nearly as earnest as last time. Looks like this would be the game today."

        w "\"Of course. May I have some tips? I'm afraid I'm not sure where to start.\""

        a normal "\"He often leaves hints in the mirror, with important information.\""

        a "\"Remember, Mr. Rabbit never misses his breakfast, so you'd better find him before that!\""

        w "\"Alright, I'll start then!\""

        a happy strange "\"Hehe have fun! Everything will be different after tomorrow...\""

        "The words at the end lilted in an ominous way. That doesn't sound good."

        jump day6_option1_over

    label day6_option1b:

        "Alice stamped her feet, she looked unhappy."

        a annoyed "\"Not as good as me! He can only play some simple tricks with the mirror.\""
        
        a "\"But they aren't REALLY tricks. Everyone knows mirrors can reverse the words!\""

        "I laughed to myself. She really loves playing games, doesn't she?"

        w "\"Okay, okay. You're right, of course you play games better than him, Alice.\""

        "Alice crossed her arms and nodded self-righteously."

        a annoyed "\"Obviously. He even marks important clues for the player, I'm fairer than him too!\""

        a normal "\"Anyway, I've got some important things to work on! Why don't you go play with Mr. Rabbit today?\""

        a "\"Remember, Mr. Rabbit never misses his breakfast, so you'd better find him before that!\""

        a happy strange "\"Hehe have fun! Everything will be different after tomorrow...\""

        "The words at the end lilted in an ominous way. That doesn't sound good."

        jump day6_option1_over

    label day6_option1_over:

        hide alice

        w "\"Wait, what do you mean? Alice? Alice!\""

        play sound "audio/soundeffects/Fast_Footsteps.wav" fadein 2.0

        "Alice left as soon as she finished speaking, and her rapid footsteps faded away."

        stop sound fadeout 2.5

        jump day6_option2

    label day6_option2:

        if scenechange == True:
        
            scene bg whitley_bedroom

            stop sound fadeout 1.8

            play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

        $ scenechange = True

        if firstoption2 == True:

            show screen Time

            "I picked up my pocket from the bedside table - It was 6:20 a.m."

            $ firstoption2 = False

        menu:

            "What should I do right now?"

            "Check the pillow" if pillowchecked == False:

                $ pillowchecked = True

                w "\"Nothing here... Oh God, did I drool last night? Wow, Alice was right, guess I did sleep well. It's definitely been a while.\""

                $ scenechange = False

                jump day6_option2

            "Check the vanity mirror":

                $ gohallway = True

                jump day6_option2b

            "Read the clues" if translated == True:

                call clues

                $ scenechange = False

                jump day6_option2

            "Leave the room":

                jump day6_option2_over

    label day6_option2b:

        if mirrorchecked == False:

            "Alice had mentioned the mirror before. And sure enough, there were some strange symbols on the mirror. But it looked familiar...almost like letters, but not quite."
            
            "The symbols seemed to be floating in the mirror rather than being written on it."

            "Is this more of Alice's magic?"

            "Maybe if I try saying the letters backwards, something will happen."
            
            "Although.... There was an old gentlemen I met when I was a child. He called himself wizard and taught me a spell. The lettering here holds some resemblence to it, if you look at it from a certain angle, anyway."

            "It was just a silly spell he made up to have fun with the kids, I don't even remember what it was supposed to do. But maybe I can try it here?"

            $ mirrorchecked = True

        elif translated == False:

            "There was some mirrored text recorded in the mirror."

        menu:

            "What should I do with the mirror?"

            "Avada Kedavra! (+5min)":

                $ addmin(5)

                if wandfound == False:

                    w "\"Avada Kedavra!\""

                    "Nothing happened, as was expected."

                else:

                    "I waved the wand and pointed it to the mirror."

                    w "\"Avada Kedavra!\""

                    "Nothing happened. Seems like a wand doesn't make me more like a wizard."

                jump day6_option2b

            "ɿoɿɿimɘʜɈʜƨɒmƨ! (+5min)" if wandfound == True:

                $ addmin(5)

                "I waved the wand and pointed it to the mirror."

                w "\"ɿoɿɿimɘʜɈʜƨɒmƨ!\""

                $renpy.sound.set_volume(0.1, 0, channel = 'sound')

                play sound "audio/soundeffects/mirror_crash.wav"

                "*Crack*"

                "The mirror broke! I dodged the pieces that flew out of the shattered mirror and found a piece of paper in the debris."

                $renpy.sound.set_volume(1, 1, channel = 'sound')

                if translated == True:

                    "The rules written on this piece of paper were totally different from the one on the mirror."

                else:

                    "This might be the rules to Mr. Rabbit's little game. He hid them inside the mirror."

                    "Alice was right, this is a tricky rabbit for sure."

                call real_clues

                if translated == True:

                    "I remembered what Alice told me at the very beginning... It was true, every word was reversed in the mirror."

                else:

                    "I sighed. If I had found this piece of paper at the beginning, it could've been very useful."

                "I noticed something else in the mirror, so I reached out and took it."

                jump day6_clue


            "FREIGABE! (+5min)" if wandfound == True:

                $ addmin(5)

                "I waved the wand and pointed it to the mirror."

                w "\"FREIGABE!\""

                "Nothing happened. Maybe this's not the correct spell."

                jump day6_option2b
                

            "Translate the text (+20min)" if translated == False:

                $ addmin(20)

                "It took a while to translate the text, but I got a couple lines of clues."

                "I wrote the clues down, so I could check them again if I needed to before making choices."

                $ translated = True

                call clues

                jump day6_option2b

            "Read the clues" if translated == True:

                call clues

                jump day6_option2b

            "Turn back":

                $ scenechange = False

                jump day6_option2

        label clues:

            show image "note.jpg"

            play sound "audio/soundeffects/page_turn.wav"

            centered "{size=+5}{font=fonts/PenStory.ttf}{b}{size=+12}Playing Hide and Seek with Mr. Rabbit!{/size}{/b}\n\n\n1. You are the {b}{size=+3}SEEKER{/size}{/b}\n\n2. If you find the hidden Mr. Rabbit, you {b}{size=+3}WIN{/size}{/b}\n\n3. Every choice Mr. Rabbit does is {b}{size=+3}RIGHT{/size}{/b}\n\n4. There {b}{size=+3}ISN'T{/size}{/b} a candy for the winner, just have fun!\n\n5. {b}{size=+3}FOLLOW{/size}{/b} the rules\n\n\n\n{space=500}-- Mr. Rabbit{/font}{/size}"

            hide image "note.jpg"
           
        return

        label real_clues:

            show image "note.jpg"

            play sound "audio/soundeffects/page_turn.wav"

            centered "{size=+5}{font=fonts/PenStory.ttf}{b}{size=+12}Playing Lie and Truth with Mr. Rabbit!{/size}{/b}\n\n\n1. You are the {b}{size=+3}HIDER{/size}{/b}\n\n2. If you find the hidden Mr. Rabbit, you {b}{size=+3}LOSE{/size}{/b}\n\n3. Every choice Mr. Rabbit does is {b}{size=+3}LEFT{/size}{/b}\n\n4. There {b}{size=+3}IS{/size}{/b} a candy for the winner, just have fun!\n\n5. {b}{size=+3}BREAK{/size}{/b} the rules\n\n\n\n{space=500}-- Mr. Rabbit{/font}{/size}"

            hide image "note.jpg"
           
        return

        label day6_clue:

            "It was a music box, seemed a little old."

            "I remembered Alice mentioned it once as her favorite \"treasure,\" but she forgot to take it with her after moving here."

            "This must be the \"candy\" for winning the game with Mr. Rabbit."

            "I put the music box on my bedside table."

            if hr < 7 or hr ==7 and minute <=10:

                "I still had some time before the breakfast. At least I could take a little rest. God knows I needed it."

            else:

                "It was almost 7:30 a.m., so I stayed in the bedroom and waited for the breakfast."

            $ win = True

            if hr == 6:

                $ timetakentowin = minute - 20

            else:

                $ timetakentowin = minute + 40

            "Time is passing..."

            play sound "audio/soundeffects/clock_ticking.wav" fadein 1.0

            while hr!=7 or minute!=30:

                $ addmin(1)
                
                $ renpy.pause(0.1)

            jump breakfast

    label day6_option2_over:

        if firstgoout == True:

            if translated == False and gohallway == True:

                "I can't translate the text that quickly. Maybe it's not wise to do it right now."

            "Breakfast normally started at 7:30 a.m. I hope I'd better find Mr. Rabbit before that."

            scene bg hallway

            show black

            play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

            "I pushed the door open, but the hallway looked as dark as night."

            "But then I blinked and saw that the light of the lamps were sprinkled on the ground. Everything seemed normal again."

            hide black with Dissolve(2)

            show black with Dissolve(1)

            hide black with Dissolve(1.5)

            "Lately, I've learned I just can't trust my eyes. I think Alice's delusion magic might be getting stronger."
            "I briefly hoped I'll be able to convince Alice to let me leave. But right now, I need to find Mr. Rabbit."

            play sound "audio/soundeffects/whitley_walk.wav"

            "I went to the end of the hallway, where it split into two different directions."

            stop sound fadeout 1.8

            "Okay... On my detective's honor, I swear I never saw this fork here before."

            $ firstgoout = False

        else:

            play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

            scene bg hallway

            "I pushed the door open and went to the end of the hallway."

            play sound "audio/soundeffects/whitley_walk.wav"

            "The way split off into two different directions. Was this fork here before?"

            stop sound fadeout 1.8


    label day6_option3:

        "There was a sign on each of the two roads. The left sign had a \"LEFT\" written on it, and the right sign had a \"RIGHT\" written on it."
        "That seems a little....unnecessary?"

        menu:

            "Which way should I go?"

            "Road with \"LEFT\" sign (+5min)":

                play sound "audio/soundeffects/whitley_walk.wav"

                scene bg hallway:
                    subpixel True
                    truecenter
                    zoom 1.0
                    ease 5.0 zoom 3.8
                    linear 0.5 xalign 0.0
                    ease 3.0

                $ renpy.pause(4)

                show white with Dissolve(2)

                scene bg hallway with Dissolve(2)

                hide white with Dissolve(2)

                $ addmin(5)

                if firstfirstforkright == False:

                    "The right road led me to a dead end. Looks like I have no choice but to go this way."

                elif translated == False and firstfirstforkleft == True:

                    "I don't have any clue where Mr. Rabbit is, but I think my intuition will lead me to the place."

                if firstfirstforkleft == False and translated == False and firstfirstforkright == True:

                    "Fortunately, my intuition gave me the correct answer."

                if firstfirstforkleft == True and translated == True and firstfirstforkright == True:

                    "The clues on the mirrors were strange... I didn't think following them would be the right choice."

                    "I decided to turn left."

                "I went to the road chosen and soon came to another fork in the road."

                stop sound fadeout 2.0

                if firstfirstforkleft == True and translated == True and firstfirstforkright == True:

                    "Seems like that wasn't a bad choice."

                $ firstfirstforkleft = False

                jump day6_option4

            "Road with \"RIGHT\" sign (+5min)":

                play sound "audio/soundeffects/whitley_walk.wav"

                scene bg hallway:
                    subpixel True
                    truecenter
                    zoom 1.0
                    ease 5.0 zoom 3.8
                    linear 0.5 xalign 1.0
                    ease 3.0

                $ renpy.pause(4)

                show white with Dissolve(2)

                scene bg hallway with Dissolve(2)

                hide white with Dissolve(2)

                $ addmin(5)

                if translated == False:

                    "I didn't have a clue where Mr. Rabbit could be, so I decided to trust my intuition."

                elif firstfirstforkright == True:

                    "Every choice Mr. Rabbit made was right, so this must be the right choice."

                    $ firstfirstforkright = False

                "I went to the road chosen, but soon came to a dead end."

                stop sound fadeout 2

                "I could only go back to the last fork."

                jump day6_option3

            "Read the clues" if translated == True:

                call clues

                jump day6_option3

            "Back to bedroom":

                play sound "audio/soundeffects/whitley_walk.wav"

                "I went back to the bedroom."

                jump day6_option2

    label day6_option4:

        "The sign \"RIGHT\" was placed in the left way, and the sign \"LEFT\" was placed in the right way."

        if firstsecondforkright == True and firstsecondforkleft == True:

            if translated == True:
                
                "That's strange. Shall I trust what the mirror said this time?"

            else:

                "That's strange. Shall I trust my intuition this time?"

        menu:

            "Which way should I go?"

            "Road on left side with \"RIGHT\" sign (+5min)":

                play sound "audio/soundeffects/whitley_walk.wav"

                scene bg hallway:
                    subpixel True
                    truecenter
                    zoom 1.0
                    ease 5.0 zoom 3.8
                    linear 0.5 xalign 0.0
                    ease 3.0

                $ renpy.pause(4)

                show white with Dissolve(2)

                scene bg hallway with Dissolve(2)

                hide white with Dissolve(2)

                $ addmin(5)

                "I went to the road chosen and soon came to a dead end."

                if firstfirstforkright == False and firstsecondforkright == True:

                    "I was confused by the clues I translated from the mirror."

                    "I had made the wrong decision twice now."

                    "It told me every choice Mr. Rabbit made was right... Did I understand it wrong?"

                    $ firstsecondforkright = False

                "I could only go back to the last fork."

                stop sound fadeout 2

                jump day6_option4

            "Road on right side with \"LEFT\" sign (+5min)":

                play sound "audio/soundeffects/whitley_walk.wav"

                scene bg hallway:
                    subpixel True
                    truecenter
                    zoom 1.0
                    ease 5.0 zoom 3.8
                    linear 0.5 xalign 1.0
                    ease 3.0

                $ renpy.pause(4)

                show white with Dissolve(2)

                scene bg hallway with Dissolve(2)

                hide white with Dissolve(2)

                $ addmin(5)

                "I went to the road chosen and soon came to another fork in the road."

                stop sound fadeout 2

                if firstfirstforkright == True and firstsecondforkright == True and firstsecondforkleft == True:

                    if translated == False:

                        "Ah, my intuition led me the right way twice now!"

                        "Looks like there is a god looking out for me."

                    else:

                        "Obviously, I shouldn't trust what the mirror told me."

                        "Opposite to what mirror said, it must be that Mr. Rabbit never makes a \"right\" choice."

                $ firstsecondforkleft = False

                jump day6_option5

            "Read the clues" if translated == True:

                call clues

                jump day6_option4

            "Back to bedroom (+5min)":

                play sound "audio/soundeffects/whitley_walk.wav"

                "I went back to the bedroom."

                $ addmin(5)

                jump day6_option2

    label day6_option5:

        "There was one sign on each road, but each sign was written with strange letters."

        "They looked like the text on the mirror. Backward words again?"

        menu:

            "Which way should I go?"

            "Road with \"TꟻƎ⅃\" sign (+5min)":

                if firstfirstforkright == False and firstsecondforkright == False and translated == False:

                    "That looks like the mirrored text for the word \"LEFT.\" I'd chosen right way for twice, but they both led me to a dead end."

                    "There's not much time left. I decided to turn left first."

                if translated == True and firstthirdforkleft == True:

                    "I chose not to trust the clues in the mirror. Every choice Mr. Rabbit did should be \"left.\""

                    $ firstthirdforkleft = False

                play sound "audio/soundeffects/whitley_walk.wav"

                scene bg hallway:
                    subpixel True
                    truecenter
                    zoom 1.0
                    ease 5.0 zoom 3.8
                    linear 0.5 xalign 0
                    ease 3.0

                $ renpy.pause(4)

                show white with Dissolve(2)

                scene bg hallway with Dissolve(2)

                hide white with Dissolve(2)

                $ addmin(5)

                "I went to the road chosen, but soon came to a dead end."

                "I could only go back to the last fork."

                stop sound fadeout 2

                jump day6_option5

            "Road with \"THӘIЯ\" sign (+5min)":

                if firstfirstforkright == True and firstsecondforkright == True and firstthirdforkleft == True:

                    if translated == True:

                        "If every word in the mirror meant the opposite of their original meaning, that means the backward text here must be opposite too."

                        "Therefore, the \"THӘIЯ\" sign must mean \"LEFT,\" and the \"TꟻƎ⅃\" sign means \"RIGHT.\""

                        "So every choice Mr. Rabbit makes is \"LEFT\"!"

                        "I couldn't help but smile at myself. A professional detective never make a wrong inference, especially on a simple mirror trick!"

                    else:

                        "A professional detective never hesitates. I always follow my heart."

                        "I'll go with a different one after two continuous same answers. Never trust a test that's \"B's\" all the way down."

                if firstfirstforkright == False and firstsecondforkright == False and firstthirdforkleft == False:

                    "I finally found the correct way to go, after making the wrong decisions thrice now."

                    "Gee, am I detective or not? Why didn't I figure this out sooner."

                    if minute < 10:

                        "It's [hr]:0[minute] right now. No much time left."

                    else:

                        "It's [hr]:[minute] right now. No much time left."

                play sound "audio/soundeffects/whitley_walk.wav"

                scene bg hallway:
                    subpixel True
                    truecenter
                    zoom 1.0
                    ease 5.0 zoom 3.8
                    linear 0.5 xalign 1.0
                    ease 3.0

                $ renpy.pause(4)

                show white with Dissolve(2)

                $ addmin(5)

                "I went to the road chosen and soon came to the end of the hallway."

                stop sound fadeout 2

                jump day6_option5_over

            "Read the clues" if translated == True:

                call clues

                jump day6_option5

            "Back to bedroom (+10min)":

                play sound "audio/soundeffects/whitley_walk.wav"

                "I went back to the bedroom."

                $ addmin(10)

                jump day6_option2

    label day6_option5_over:

        "There was only one room here, so I opened the door and walked in."

        play sound "audio/soundeffects/open_bedroom_door.wav"

        scene bg empty room with Dissolve(2)

        hide white with Dissolve(2)

        "After entering the room, I immediately saw Mr. Rabbit."

        "But he was imprisoned by some... winding thorns? On the floor? Is this a delusion too?"

        "Suddenly, I heard a voice pipe up from the plush toy!"

        r ok "\"Hey! Mr. Rabbit sees you! Mr. Rabbit sees you!\""

        r depressed "\"Help! Mr. Rabbit accidentally used a wrong spell, please help this poor bunny!\""

        w "\"O-Okay! Don't move! Thorns might hurt you! Or...not? I'm not exactly sure how this would work for a stuffed rabbit.\""

        w "\"Mr. Rabbit, you should know I could just win the game by touching you. How do I get you out?\""

        r sad "\"Game doesn't matter! Mr. Rabbit never fears failure! Take the wand!\""

        w "\"The wand?\""

        r ok "\"It's right there! Next to you! On the floor!\""

        r normal "\"Then wave it and say the spell ɿoɿɿimɘʜɈʜƨɒmƨ!\""

        w "\"Say...what?\""

        r confused "\"Nononono, say ɿoɿɿimɘʜɈʜƨɒmƨ!\"
        
        w "\"Uh, I guess I'll try?\""
        
        r confused "\"Oh nononono waitwaitwait, wrong spell! Say the spell FREIGABE! That was close, Mr. Rabbit almost made a mistake again!\""

    label day6_option6:

        menu:

            "What should I do?"

            "Take the wand" if not wandfound:

                $ wandfound = True

                "I picked up the wand left near the door."

                r ok "\"Say the spell!\""

                jump day6_option7

            "Catch Mr. Rabbit":

                "This might be the quickest way to finish the game. I could step over these thorns no problem."

                "I had so many questions, I just wanted to talk with Alice as soon as possible."

                "I left the wand and walked to Mr. Rabbit, where I could easily touch him past the thorns."

                jump lose

            "Read the clues" if translated == True:

                call clues

                jump day6_option6

            "Back to bedroom (+15min)":

                play sound "audio/soundeffects/whitley_walk.wav"

                "I went back to the bedroom."

                $ addmin(15)

                jump day6_option2

    label day6_option7a:

            hide screen countdown

            hide image "note.jpg"
       
            $ addmin(5)

            "I waved the magic wand and pointed the winding thorns."

            w "\"ɿoɿɿimɘʜɈʜƨɒmƨ!\""

            "Nothing happened."

            r angry "\"Nonono! What're you doing!? Wrong spell, wrong spell!\""

            $ option7readingclue = True

            jump day6_option7

    label day6_option7:

        if translated == True:
            $ yalign_var = 0.65

        if option7readingclue == True:

            $ time = 7
            $ timer_range = 7
            $ timer_jump = 'day6_option7a'

            show screen countdown

            $ option7readingclue = False

        menu:

            "What should I do?"

            "ɿoɿɿimɘʜɈʜƨɒmƨ! (+5min)":

                $ option7readingclue = True

                jump day6_option7a

            "FREIGABE! (+5min)":

                hide screen countdown

                $ addmin(5)

                "I waved the magic wand and pointed it at the winding thorns."

                w "\"FREIGABE!\""

                "With a flash of blue light, the thorns disappeared."

                w "\"You're free now!\""

                r satisfied "\"Oh! Oh! How kind you are, Ms. Whitley! Mr. Rabbit almost thought he would not complete the game today.\""

                "Mr. Rabbit cried and bounced to me."

                w "\"Mr. Rabbit?\""

                "Mr. Rabbit bounced on my shoe. He looked up and I watched his plush twist and turn to give me a weird smile."

                jump lose

            "Catch Mr. Rabbit":

                hide screen countdown

                "I shouldn't waste time on waving the wand."

                "I had so many questions, I just wanted to talk with Alice as soon as possible."

                "I left the wand and walked to Mr. Rabbit, where I could easily touch him past the thorns."

                jump lose

            "Read the clues" if translated == True:

                $ yalign_var = 0.85

                call clues

                jump day6_option7

            "Back to bedroom (+15min)":

                hide screen countdown

                $ option7readingclue = True

                play sound "audio/soundeffects/whitley_walk.wav"

                r angry "\"Where are you going!? Ms. Whitley! Come back! There's no time left!\""

                "I went back to the bedroom."

                $ addmin(15)

                jump day6_option2


    label lose:

        r winning "\"Mr. Rabbit caught ya!\""

        if translated == True:

            w "\"What do you mean? I was the one looking for you!\""

            r depressed "\"Oh, you've never been the seeker! Poor Ms. Whitley, Mr. Rabbit thought everyone knew things are opposite in the mirror.\""

        else:

            r normal "\"Oh Ms. Whitley, didn't you read the rules I left in the mirror?\""

        r depressed "\"Mr. Rabbit is suprised you reached this room without noticing it!\""

        r happy "\"Oh well! Mr. Rabbit is always right! No one will see through Mr. Rabbit's lies now!\""

        "I tried to talk to Mr. Rabbit, but it seemed to be in a state of madness and refused to respond. It was like I wasn't even there."

        play sound "audio/soundeffects/whitley_walk.wav" fadein 1.0

        "I left Mr. Rabbit and waited for breakfast in my room."

        stop sound fadeout 2

        scene bg whitley_bedroom

        play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

        "I sat in front of the mirror, staring at my pocket watch."

        "Time is passing..."

        play sound "audio/soundeffects/clock_ticking.wav" fadein 1.0

        while hr!=7 or minute!=30:

            $ addmin(1)
                
            $ renpy.pause(0.05)

        jump breakfast

    label breakfast:

        stop sound

        play sound "audio/soundeffects/clock_gong.wav" fadein 10.0

        $ hr = 7

        $ minute = 30

        a happy "\"It's time! Let's have breakfast, everyone!\""

        if win == False:

            r winning "\"Ms. Whitley is smart! But Mr. Rabbit is smarter!\""

            a happy strange "\"You cunning bunny. Every single clue you left in that mirror was a lie, wasn't it!\""

            r satisfied "\"Mr. Rabbit only wants to keep his words sincere!\""

        else:

            r confused "\"No, no, no! Mr. Rabbit's mirror! Mr. Rabbit's secret has been discovered!\""

            r sad "\"Ms. Whitley, how could you possibly do that?\""
            
            if timetakentowin == 65:

                r depressed "\"1 hour and 5 minutes! So close, so close! Mr. Rabbit almost won the game!\""

            elif timetakentowin == 60:

                r depressed "\"1 hour! So close, so close! Mr. Rabbit almost won the game!\""

            elif timetakentowin < 60:

                r depressed "\"[timetakentowin] minutes! You only used [timetakentowin] minutes to see through Mr. Rabbit's trap?!\""

                if timetakentowin == 35:

                    r depressed "\"No one can find Mr. Rabbit's secret faster than you! No one! Did you play a trick with the time?\""

            ##r depressed "\"Don't tell Alice, please! Let it be the secret only for you and Mr. Rabbit.\""
            
            w "\"Hey Mr. Rabbit, calm down. Let's go for breakfast, alright?\""

            r confused "\"Oh dear! Ms. Whitley is right! It's time for breakfast. Mr. Rabbit shall leave! Mr. Rabbit shall leave!\""

            "Mr. Rabbit bounced away nervously."

            "But he soon turned back."

            r depressed "\"Mr. Rabbit almost forget it! Here's your prize for winning the game!\""

            "That's a candy wrapped in blue."

            r depressed "\"Mr. Rabbit must leave now!\""

            "He bounced away soon."

            "*clap*"

            a smile "\"Congratulations! Hope you have a wonderful time with Mr. Rabbit, Ms. Whitley.\""

            w "\"Like what you said, it's a tricky bunny who always tell lies.\""

            w "\"But it's fun to have a friend like it, isn't it?\""

            a annoyed openeyes "..."

            a annoyed openeyes "Don't you think lying is a sin?"

            a angry "Misery always accompanies with lies and misery would only bring pain to our lives."

            a confused "Isn't lying a really, really bad thing to do?"

            menu:
                "Yes, you're right":
                
                    a smile "I know you always stand by me, Ms. Whitley."

                    a happy "Now it's Breakfast time! Let's go to the dinning room!"

                "No, it's not":

                    w "Alice, not only misery would accompany with lies."

                    "I stretched forth my hand and showed Alice the candy I won."

                    w "See, this is the happiness I gain from Mr. Rabbit's lie."

                    w "Now I'm sharing this happiness with you."

                    a sad "..."

                    a smile "You're a really good adult, Ms. Whitley"

                    a guilty "I sometimes hope I could meet you earlier."

                    a happy closeopen "But now it's Breakfast time! Let's go to the dinning room!"

                    heart += 1

            play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

            "Alice pushed the door open and went out of my room."

            "I followed her and went out."

        play sound "audio/soundeffects/whitley_walk.wav" fadein 1.0

        scene bg dining room

        "I went to the dinning room."

        stop sound fadeout 2

        "While having breakfast, my head became more and more groggy and my vision blurred."

        "I had lots of questions to ask and lots of words to say, but every time I tried to talk with Alice, I would suddenly forget what to say."

        "Alice noticed my discomfort and advised me to rest. That sounded like a good idea, I really needed a rest...especially if I was going to be ready for whatever awaited me tomorrow."

        play sound "audio/soundeffects/whitley_walk.wav" fadein 1.0

        "I went back to my bedroom."

        stop sound fadeout 2

        scene bg whitley_bedroom

        play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

        "I laid down and soon fell asleep."

        hide screen Time

        show black with Dissolve(3.0)

        hide black with Dissolve(2.0)

        jump day7