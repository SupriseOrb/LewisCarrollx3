label day6:

    default pillowchecked = False

    default gohallway = False

    default wandfound = False

    default mirrorchecked = False

    default translated = False

    default firstgoout = True

    default hr = 6

    default minute = 40

    screen Time:
        if minute < 10:

            text "Time: [hr]:0[minute]" xpos 0.1 ypos 0.1

        else:

            text "Time: [hr]:[minute]" xpos 0.1 ypos 0.1

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

    scene bg bedroom

    play sound "audio/soundeffects/Fast_Footsteps.wav" fadein 2.0

    "I was awakened from the sleep by the noise of rapid footsteps."

    stop sound fadeout 1.0

    "The room was dark and the curtains were drawn."

    " My head was paining... Did I draw the curtains last night?"

    "I picked up the pocket watch I put on the bedside table - it's just 6:00 a.m."

    play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

    "The door of my room was opened by someone."

    show alice

    a "Hi Whitley! Glad to see you sleeping so well last night. Have you seen Mr. Rabbit?"

    hide alice

    w "No... I just wake up. What happened?"

    show alice

    a "It said it wanted to play with you and sneaked away in the early morning. How cunning!"

    hide alice

    menu:

        "What can I do for you?":
            jump day6_option1a

        "It must be very good at playing games":
            jump day6_option1b

    label day6_option1a:

        show alice

        "Alice stamped her feet, she looked anxious"

        a "I have something to do, so I cannot play with you this time. Can you help me find Mr. Rabbit? It might hide somewhere in the house."

        hide alice

        w "Of course. May I have some tips? I’m afraid that I cannot find it."

        show alice

        a "It often leaves hints in the mirror, and important information will be marked out."

        a "Remember, Mr. Rabbit never misses its breakfast, so you'd better find it before that."

        a "Don't worry. Enjoy the game, and everything will be over after tomorrow..."

        jump day6_option1_over

    label day6_option1b:

        show alice

        "Alice stamped her feet, she looked unhappy"

        a "It can only play some simple tricks with the mirror. Everyone should know mirrors could reverse the words!"

        hide alice

        w "Yes, yes. Of course you play games better than it."

        show alice

        a "Obviously. It’ll even mark the important clues for the player, I’m fairer than it too!"

        a "But right now, I have other things to do. I allow you to go play with Mr. Rabbit today."

        a "Remember, Mr. Rabbit never misses its breakfast, so you'd better find it before that."

        a "Don’t worry, enjoy the game, and everything will be over after tomorrow..."

        jump day6_option1_over

    label day6_option1_over:

        hide alice

        w "Wait… What do you mean? Alice? Alice!"

        "Alice left as soon as she finished speaking, and her rapid footsteps faded away."

        jump day6_option2

    label day6_option2:

        scene bg bedroom

        menu:

            "What should I do right now?"

            "Check the pillow" if pillowchecked == False:

                $ pillowchecked = True

                "Nothing found here... Oh God, did I drool last night? I haven't got a deep sleep like this for a while."

                jump day6_option2

            "Check the dressing mirror":

                $ gohallway = True

                jump day6_option2b

            "Get out of the room" if gohallway == True:

                jump day6_option2_over

    label day6_option2b:

        if mirrorchecked == False:

            "There were some mirrored texts recorded on the mirror. They were more like floating in the mirror instead of being written on it."

            "Is this Alice's magic, too?"

            "This reminds me an old gentlemen I met when I was a child. He called himself wizard and taught me a spell."

            "I don't know what this spell does, but maybe I can try it here."

            $ mirrorchecked = True

        menu:

            "Avada Kedavra!":

                if wandfound == False:

                    "Nothing happened, as was expected."

                else:

                    "Nothing happened. Seems like a wand doesn't make me more like a wizard."

                jump day6_option2b

            "Translate the text" if translated == False:

                "I took a while to translate the text and got a couple lines of clues."

                $ translated = True

                jump clues

            "Read the clues" if translated == True:

                jump clues

        label clues:

            centered "{b}{size=+8}Playing Hide and Seek with Mr. Rabbit!{/size}{/b}\n\n\n1. You are the {b}{size=+3}SEEKER{/size}{/b}\n\n2. If you find the hidden Mr. Rabbit, you {b}{size=+3}WIN{/size}{/b}\n\n3. Every choice Mr. Rabbit does is {b}{size=+3}RIGHT{/size}{/b}\n\n4. There is {b}{size=+3}NO{/size}{/b} candy for the winner, just have fun!\n\n5. {b}{size=+3}FOLLOW{/size}{/b} the rules\n\n\n\n{space=1000}-- {font=fonts/Pacifico-Regular.ttf}Mr. Rabbit{/font}"

        jump day6_option2

    label day6_option2_over:

        if firstgoout == True:

            "I looked at my watch, it’s 6:40 a.m. right now."

            "Breakfast time normally started at 7:30 a.m. I hope I can find Mr. Rabbit before that."

            show screen Time

            scene bg hallway

            play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

            "I pushed the door open, but the hallway looked as dark as night."

            "I blinked, the morning sunshine sprinkled on the ground through the window, and everything seemed normal again."

            "There have been more and more delusions recently. I'd better persuade Alice to leave, but right now, I need to find Mr. Rabbit first."

            "I went to the end of the hallway, and it split off into two different directions."

            "On my detective’s honor, I swear I never saw this fork here before."

            $ firstgoout = False

        else:

            scene bg hallway

            play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

            "I pushed the door open and went to the end of the hallway again."

            "The way split off into two different directions."


    label day6_option3:

        "There was a sign on each of the two roads. The left sign had a \"LEFT\" written on it, and the right sign had a \"RIGHT\" written on it."

        "Which way should I go?"

        menu:

            "Road with \"LEFT\" sign (+5min)":

                $ addmin(5)

                "I went to the road chosen and soon came to another fork in the road."

                jump day6_option4

            "Road with \"RIGHT\" sign (+5min)":

                $ addmin(5)

                "I went to the road chosen and soon came to a dead end."

                "I could only go back to the last fork."

                jump day6_option3

            "Back to bedroom":

                play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

                "I went back to the bedroom."

                jump day6_option2

    label day6_option4:

        "The sign \"RIGHT\" was placed in the left way, and the sign \"LEFT\" was placed in the right way."

        "Which way should I go?"

        menu:

            "Road with \"RIGHT\" sign (+5min)":

                "I went to the road chosen and soon came to a dead end."

                "I could only go back to the last fork."

                jump day6_option4

            "Road with \"LEFT\" sign (+5min)":

                $ addmin(5)

                "I went to the road chosen and soon came to another fork in the road."

                jump day6_option5

            "Back to bedroom (+5min)":

                $ addmin(5)

                play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0

                "I went back to the bedroom."

                jump day6_option2

    label day6_option5:

        "nothing yet"

    label breakfast:
    
        show alice

        a "Game is over! Everyone should have breakfast right now!"