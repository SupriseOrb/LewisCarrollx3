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

    default minute = 20

    default timetakentowin = 0

    default winningstring = ""

    init python:
        def addmin(value):

            global minute,hr

            if minute + value >= 60:

                hr += 1

                minute = minute + value - 60

            else:

                minute += value

            if hr == 7 and minute >= 30:

                minute = 30

                renpy.jump("breakfast")

            return

    scene bg whitley_bedroom

    show black

    play sound "audio/soundeffects/Fast_Footsteps.wav" fadein 2.0

    "I was awakened from the sleep by the noise of rapid footsteps."

    stop sound fadeout 1.0

    "The room was dark and the curtains were drawn."

    hide black with Dissolve(2)

    "My head was paining... Did I draw the curtains last night?"

    play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

    "The door of my room was opened by someone."

    a "Hi Whitley! Glad to see you sleeping so well last night. Have you seen Mr. Rabbit?"

    w "No... I just wake up. What happened?"

    a annoyed "It said it wanted to play with you and sneaked away in the early morning. How cunning!"

    menu:

        "What should I say?"

        "What can I do for you?":
            jump day6_option1a

        "It must be very good at playing games":
            jump day6_option1b

    label day6_option1a:

        "Alice stamped her feet, she looked anxious."

        a annoyed "I have something to do, so I cannot play with you this time. Can you help me find Mr. Rabbit? It might hide somewhere in the house."

        w "Of course. May I have some tips? I’m afraid that I cannot find it."

        a normal "It often leaves hints in the mirror, and important information will be marked out."

        a "Remember, Mr. Rabbit never misses its breakfast, so you'd better find it before that."

        a happy strange "Don't worry. Enjoy the game, and everything will be over after tomorrow..."

        jump day6_option1_over

    label day6_option1b:

        "Alice stamped her feet, she looked unhappy."

        a annoyed "It can only play some simple tricks with the mirror. Everyone should know mirrors could reverse the words!"

        w "Yes, yes. Of course you play games better than it."

        a annoyed "Obviously. It’ll even mark the important clues for the player, I’m fairer than it too!"

        a normal "But right now, I have other things to do. I allow you to go play with Mr. Rabbit today."

        a "Remember, Mr. Rabbit never misses its breakfast, so you'd better find it before that."

        a happy strange "Don’t worry, enjoy the game, and everything will be over after tomorrow..."

        jump day6_option1_over

    label day6_option1_over:

        hide alice

        w "Wait… What do you mean? Alice? Alice!"

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

            "I picked up the pocket watch I put on the bedside table - it's just 6:20 a.m."

            $ firstoption2 = False

        menu:

            "What should I do right now?"

            "Check the pillow" if pillowchecked == False:

                $ pillowchecked = True

                "Nothing found here... Oh God, did I drool last night? I haven't got a deep sleep like this for a while."

                $ scenechange = False

                jump day6_option2

            "Check the dressing mirror":

                $ gohallway = True

                jump day6_option2b

            "Read the clues" if translated == True:

                call clues

                $ scenechange = False

                jump day6_option2

            "Get out of the room":

                jump day6_option2_over

    label day6_option2b:

        if mirrorchecked == False:

            "There were some strange symbols on the mirror. Pretty familiar... They might be mirrored texts."
            
            "They were more like floating in the mirror instead of being written on it."

            "Is that Alice's magic, too?"

            "This reminds me an old gentlemen I met when I was a child. He called himself wizard and taught me a spell."

            "I don't know what this spell does, but maybe I can try it here."

            $ mirrorchecked = True

        elif translated == False:

            "There were some mirrored texts recorded on the mirror."

        menu:

            "What should I do with the mirror?"

            "Avada Kedavra! (+5min)":

                $ addmin(5)

                if wandfound == False:

                    w "Avada Kedavra!"

                    "Nothing happened, as was expected."

                else:

                    "I waved the wand and pointed it to the mirror."

                    w "Avada Kedavra!"

                    "Nothing happened. Seems like a wand doesn't make me more like a wizard."

                jump day6_option2b

            "ɿoɿɿimɘʜɈʜƨɒmƨ! (+5min)" if wandfound == True:

                $ addmin(5)

                "I waved the wand and pointed it to the mirror."

                w "ɿoɿɿimɘʜɈʜƨɒmƨ!"

                play sound "audio/soundeffects/mirror_crash.wav"

                "*Crack*"

                "The mirror broke! I dodged the pieces of the flying mirror and found out a piece of paper inside the mirror."

                if translated == True:

                    "The rules written on this piece of paper were totally different from the one on the mirror"

                else:

                    "This might be the rule of the game. Mr. Rabbit hided it inside the mirror."

                    "Alice is right, it's a cunning rabbit."

                call real_clues

                if translated == True:

                    "I remembered what Alice told me at the very beginning... Every word was reversed in the mirror, that's true."

                else:

                    "If I found this piece of paper at the beginning, it might be very useful."

                "I saw something else in the mirror, so I reached out and took it."

                jump day6_clue


            "FREIGABE! (+5min)" if wandfound == True:

                $ addmin(5)

                "I waved the wand and pointed it to the mirror."

                w "FREIGABE!"

                "Nothing happened. Maybe this's not the correct spell."

                jump day6_option2b
                

            "Translate the text (+20min)" if translated == False:

                $ addmin(20)

                "I took a while to translate the text and got a couple lines of clues."

                "I wrote the clues down, so I could always check it before making choices."

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

            "This was a music box, seemed a little bit old."

            "I remembered it's Alice's favorite \"treasure,\" but she forgot to take it after moving."

            "This should be the \"candy\" for winning the game with Mr. Rabbit."

            "I put the music box into my bedside table."

            if hr < 7 or hr ==7 and minute <=10:

                "I still have some time before the breakfast. Now I could have a rest and waited for the breakfast."

            else:

                "It's almost 7:30 a.m., so I stayed in the bedroom and waited for the breakfast."

            $ win = True

            "..."

            jump breakfast

    label day6_option2_over:

        if firstgoout == True:

            if translated == False and gohallway == True:

                "I couldn't translate the text in a short time. Maybe it's not wise to do it right now."

            "Breakfast time normally started at 7:30 a.m. I hope I can find Mr. Rabbit before that."

            scene bg hallway

            show black

            play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

            "I pushed the door open, but the hallway looked as dark as night."

            "I blinked, the light of lamps sprinkled on the ground, and everything seemed normal again."

            hide black with Dissolve(2)

            show black with Dissolve(1)

            hide black with Dissolve(1.5)

            "There have been more and more delusions recently. I'd better persuade Alice to leave, but right now, I need to find Mr. Rabbit first."

            play sound "audio/soundeffects/whitley_walk.wav"

            "I went to the end of the hallway, and it split off into two different directions."

            stop sound fadeout 1.8

            "On my detective’s honor, I swear I never saw this fork here before."

            $ firstgoout = False

        else:

            play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

            scene bg hallway

            "I pushed the door open and went to the end of the hallway again."

            play sound "audio/soundeffects/whitley_walk.wav"

            "The way split off into two different directions."

            stop sound fadeout 1.8


    label day6_option3:

        "There was a sign on each of the two roads. The left sign had a \"LEFT\" written on it, and the right sign had a \"RIGHT\" written on it."

        menu:

            "Which way should I go?"

            "Road with \"LEFT\" sign (+5min)":

                $ addmin(5)

                play sound "audio/soundeffects/whitley_walk.wav"

                if firstfirstforkright == False:

                    "The right road lead to a dead end. I could only go this way."

                elif translated == False and firstfirstforkleft == True:

                    "I don't have any clue about where Mr. Rabbit is, but I think my intuition will lead me to the place."

                if firstfirstforkleft == False and translated == False and firstfirstforkright == True:

                    "Fortunately, my intuition gave me the correct answer."

                if firstfirstforkleft == True and translated == True and firstfirstforkright == True:

                    "The clues on the mirrors were strange... I didn't think follow them might be the right choice."

                    "I decided to turn left."

                "I went to the road chosen and soon came to another fork in the road."

                stop sound fadeout 2.0

                if firstfirstforkleft == True and translated == True and firstfirstforkright == True:

                    "Seemed like I was right."

                $ firstfirstforkleft = False

                jump day6_option4

            "Road with \"RIGHT\" sign (+5min)":

                $ addmin(5)

                play sound "audio/soundeffects/whitley_walk.wav"

                if translated == False:

                    "I don't have any clue about where Mr. Rabbit is, so I decide to trust my intuition."

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
                
                "It's strange. Shall I trust what the mirror say this time?"

            else:

                "It's strange. Shall I trust my intuition this time?"

        menu:

            "Which way should I go?"

            "Road on left side with \"RIGHT\" sign (+5min)":

                $ addmin(5)

                play sound "audio/soundeffects/whitley_walk.wav"

                "I went to the road chosen and soon came to a dead end."

                if firstfirstforkright == False and firstsecondforkright == True:

                    "I was confused by the clues I translated from the mirror."

                    "I had made wrong decisions twice."

                    "It told me every choice Mr. Rabbit made was right... Did I understand it wrong?"

                    $ firstsecondforkright = False

                "I could only go back to the last fork."

                stop sound fadeout 2

                jump day6_option4

            "Road on right side with \"LEFT\" sign (+5min)":

                $ addmin(5)

                play sound "audio/soundeffects/whitley_walk.wav"

                "I went to the road chosen and soon came to another fork in the road."

                stop sound fadeout 2

                if firstfirstforkright == True and firstsecondforkright == True and firstsecondforkleft == True:

                    if translated == False:

                        "Ah, my intuition led me to the right way for twice!"

                        "There should be a god stand by me."

                    else:

                        "Obviously, I shouldn't trust what the mirror told me."

                        "Opposite to what mirror said, Mr. Rabbit never make a \"right\" choice"

                $ firstsecondforkleft = False

                jump day6_option5

            "Read the clues" if translated == True:

                call clues

                jump day6_option4

            "Back to bedroom (+5min)":

                $ addmin(5)

                play sound "audio/soundeffects/whitley_walk.wav"

                "I went back to the bedroom."

                jump day6_option2

    label day6_option5:

        "There was one sign on each road, but each sign was written with strange letters."

        "They might be mirrored."

        menu:

            "Which way should I go?"

            "Road with \"TꟻƎ⅃\" sign (+5min)":

                $ addmin(5)

                if firstfirstforkright == False and firstsecondforkright == False and translated == False:

                    "This was a mirrored text for word \"LEFT.\" I'd chosen right way for twice, but they both led me to the dead end."

                    "There's no much time left. I decided to turn left first."

                if translated == True and firstthirdforkleft == True:

                    "I choose not to trust the clues in the mirror. Every choice Mr. Rabbit did should be \"left.\""

                    $ firstthirdforkleft = False

                play sound "audio/soundeffects/whitley_walk.wav"

                "I went to the road chosen, but soon came to a dead end."

                "I could only go back to the last fork."

                stop sound fadeout 2

                jump day6_option5

            "Road with \"THӘIЯ\" sign (+5min)":

                $ addmin(5)

                if firstfirstforkright == True and firstsecondforkright == True and firstthirdforkleft == True:

                    if translated == True:

                        "If every word in the mirror was opposed to their original meaning, I should understand the \"THӘIЯ\" in a opposed way too when it's \"a mirrored text\" also."

                        "Therefore, the \"THӘIЯ\" sign meaned \"LEFT,\" and the \"TꟻƎ⅃\" sign meaned \"RIGHT.\""

                        "When every choice Mr. Rabbit was actually left, this was the only way I need to choose."

                        "A professional detective never make a wrong inference, especially on this simple mirror trick."

                    else:

                        "A professional detective never hesitate. I always follow my heart."

                        "A different one after two continuous same answers. This's so old fashioned."

                        "Ms. Detective never made a wrong choice."

                if firstfirstforkright == False and firstsecondforkright == False and firstthirdforkleft == False:

                    "I finally found the correct way to go. I had made wrong decisions for three times."

                    if minute < 10:

                        "It's [hr]:0[minute] right now. No much time left."

                    else:

                        "It's [hr]:[minute] right now. No much time left."

                play sound "audio/soundeffects/whitley_walk.wav"

                "I went to the road chosen and soon came to the end of the hallway."

                stop sound fadeout 2

                jump day6_option5_over

            "Read the clues" if translated == True:

                call clues

                jump day6_option5

            "Back to bedroom (+10min)":

                $ addmin(10)

                play sound "audio/soundeffects/whitley_walk.wav"

                "I went back to the bedroom."

                jump day6_option2

    label day6_option5_over:

        play sound "audio/soundeffects/open_bedroom_door.wav"

        scene bg empty room

        "There was only one room there, so I opened the door and walked in."

        "After entering the room, I immediately saw Mr. Rabbit."

        "It was prisoned by some... winding thorns? On the floor? Is this a delusion too?"

        r ok "Hey! Mr. Rabbit saw you! Mr. Rabbit saw you!"

        r depressed "Help! Mr. Rabbit accidentally used a wrong spell, please help this poor bunny!"

        w "Don't move! Thorns might hurt you."

        w "Mr. Rabbit, you should know I could just win the game by touching you. How can I help you?"

        r sad "Game doesn't matter! Mr. Rabbit never fears failure! Take the wand!"

        w "The wand?"

        r ok "It's right there! Next to you! On the floor!"

        r normal "Then wave it and say the spell ɿoɿɿimɘʜɈʜƨɒmƨ!"

        w "Say...what?"

        r confused "Nononono. Say the spell FREIGABE! Mr. Rabbit almost made a mistake again!"

    label day6_option6:

        menu:

            "What should I do right now?"

            "Take the wand" if not wandfound:

                $ wandfound = True

                "The wand was left near the door, so I soon found and picked up it."

                r ok "Say the spell!"

                jump day6_option7

            "Catch Mr. Rabbit":

                "This maybe the best timing to finish the game. I thought."

                "I have so many questions last in my mind. I just want to talk with Alice as soon as possible."

                "I pass the wand and walked to Mr. Rabbit. It's motionless, so I could easily touch it."

                jump lose

            "Read the clues" if translated == True:

                call clues

                jump day6_option6

            "Back to bedroom (+15min)":

                $ addmin(15)

                play sound "audio/soundeffects/whitley_walk.wav"

                "I went back to the bedroom."

                jump day6_option2

    label day6_option7a:

            hide screen countdown

            hide image "note.jpg"
       
            $ addmin(5)

            "I waved the magic wand and pointed the winding thorns."

            w "ɿoɿɿimɘʜɈʜƨɒmƨ!"

            "Nothing happened."

            r angry "Nonono! What're you doing!"

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

                "I waved the magic wand and pointed the winding thorns."

                w "FREIGABE!"

                "With a flash of blue light, the thorns disappeared."

                w "You are freed. What should we do next?"

                r satisfied "Oh! Oh! How kind you are, Ms. Whitley! Mr. Rabbit almost thought it could not complete the game today."

                "Mr. Rabbit cried and bounced to me."

                w "Mr. Rabbit?"

                "Mr. Rabbit bounced on my shoe and gave me a weird smile."

                jump lose

            "Catch Mr. Rabbit":

                hide screen countdown

                "I shouldn't waste time on waving the wand. I thought."

                "I have so many questions last in my mind. I just want to talk with Alice as soon as possible."

                "I walked to Mr. Rabbit. It's motionless, so I could easily touch it."

                jump lose

            "Read the clues" if translated == True:

                $ yalign_var = 0.85

                call clues

                jump day6_option7

            "Back to bedroom (+15min)":

                hide screen countdown

                $ option7readingclue = True

                $ addmin(15)

                play sound "audio/soundeffects/whitley_walk.wav"

                r angry "Where do you go! Ms. Whitley! Come back! There's no time left!"

                "I went back to the bedroom."

                jump day6_option2


    label lose:

        r winning "Mr. Rabbit catches ya!"

        w "What do you mean? I should be the seeker..."

        r depressed "You’ve never been the seeker. Poor Ms. Whitley, Mr. Rabbit thought everyone should know things are opposite in the mirror."

        r depressed "Mr. Rabbit is suprised how you reach this room without noitcing it!"

        r confused "Did you find the clues? Did you? Didn't you?"

        r happy "*purrrrr* Whatever! Mr. Rabbit is always right! No one will know Mr. Rabbit's big secret now!"

        "I tried to talk to Mr. Rabbit, but it seemed to be in a state of madness and refused to respond."

        "I had to go back and waited for breakfast in my room."

        jump breakfast

    label breakfast:

        if win == True:

            if hr == 6:

                $ timetakentowin = minute - 20

            else:

                $ timetakentowin = minute + 40

        $ hr = 7

        $ minute = 30

        a happy "It's time! Everyone should have breakfast right now!"

        if win == False:

            r winning "Ms. Whitley is smart! But Mr. Rabbit is smarter than her! Than you! Than everyone!"

            a happy strange "You cunning bunny. Every single clue you left in the mirror was a lie."

            r satisfied "Mr. Rabbit only wants to keep its big secret!"

        else:

            r confused "No, no, no! Mr. Rabbit's mirror! Mr. Rabbit’s biggest secret has been discovered!"

            r sad "Ms. Whitley, how could you possibly do that?"
            
            if timetakentowin == 65:

                r depressed "1 hour and 5 minutes! That's so close! Mr. Rabbit almost won the game!"

            elif timetakentowin == 60:

                r depressed "1 hour! That's so close! Mr. Rabbit almost won the game!"

            elif timetakentowin < 60:

                r depressed "[timetakentowin] minutes! You only used [timetakentowin] minutes to find out Mr. Rabbit's biggest secret?!"

                if timetakentowin == 35:

                    r depressed "Noone can find Mr. Rabbit's secret shorter than you! Noone! Did you play a trick with the time?"

            r depressed "Don’t tell Alice, please! Let it be the secret only for you and Mr. Rabbit."
            
            w "Hey Mr. Rabbit, calm down. We should go for breakfast, right?"

            r confused "Oh dear! It's time for breakfast. Mr. Rabbit shall leave! Mr. Rabbit shall leave!"

            "Mr. Rabbit bounced away nervously."

        play sound "audio/soundeffects/whitley_walk.wav" fadein 1.0

        scene bg dining room

        "I went to the dinning room."

        stop sound fadeout 2

        "While having breakfast, my head became more and more groggy and my vision blurred."

        "I had lots of questions to ask and lots of words to say, but everytime I tried to talk with Alice, I would suddenly forget what to say."

        "Alice noticed my discomfort and advised me to have a rest. This was a good idea, I really need a rest before I find a suitable way to convince her tomorrow."

        play sound "audio/soundeffects/whitley_walk.wav" fadein 1.0

        "I went back to my bedroom."

        stop sound fadeout 2

        scene bg whitley_bedroom

        play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

        "I fell asleep soon."

        hide screen Time

        show black with Dissolve(3.0)

        hide black with Dissolve(2.0)

        jump day7