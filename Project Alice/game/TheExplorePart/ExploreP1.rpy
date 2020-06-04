label ExploreRoom:
    scene playerroom noon with Dissolve(2)
    "I was worried about what that bang was, but this gives me a chance to explore more of the house."
    w "\"Let's see what I can find.\""
    play music "audio/BGM/Daily_BGM.wav" fadein 1

$ CheckTheWayOut = True
$ CheckTheDoor = False
$ CheckTheWindow = False
label FirstCheck:
    label check1:
    $ renpy.sound.set_volume(0.5, delay=0, channel='sound')
    while CheckTheWayOut:
        if CheckTheDoor and CheckTheWindow:
            $ CheckTheWayOut = False
            jump check1
        menu:
            "Check the door":
                $ CheckTheDoor = True
                play sound "audio/soundeffects/handle_shake.wav"
                "The door is locked."
                w "\"The door is locked, maybe I can find a key somewhere.\""
                jump FirstCheck
            "Check the window":
                $ CheckTheWindow = True
                play sound "audio/soundeffects/handle_shake.wav"
                "The window is locked."
                w "\"No way out.\""
                jump FirstCheck

    w "\"All the ways out are locked. Maybe I can find something from this room to help get me out.\""

$ TheTimesCheckWardrobe=0
$ ExploreNotDone=True
$ CheckUnderBed=True
label SecondCheck:
    label check2:
    $ renpy.sound.set_volume(1, delay=0, channel='sound')
    while ExploreNotDone:
        menu:
            "Check the desk":
                "There is a name carved on the table, \"Aiden\"."
                "Maybe Aiden used this room."
                jump SecondCheck
            "Check under the bed":
                "I can't see clearly under the bed."
                label check3:
                while CheckUnderBed:
                    menu:
                        "Try to find something by hand":
                            $ getsomething=renpy.random.randint(0,1)
                            if getsomething==1:
                                w"\"I found something!\""
                                play sound "audio/soundeffects/page_turn.wav"
                                "A piece of paper, it looks like a note. It reads:"
                                "*REMINDER*"
                                "I put the false key in the WARDROBE."
                                "Try checking there if you can't find it. Check it again if you have to."
                                "- Aiden"
                                w "\"Oh Aiden, you're a lifesaver.\""
                                $ CheckUnderBed = False
                                jump check2
                            else:
                                "I didn't find anything."
                                jump check3
                        "I don't think I can find anything here.":
                            jump check2
                if CheckUnderBed:
                    jump SecondCheck
                else:
                    "There's nothing here, maybe I should try checking the wardrobe again."
                    jump SecondCheck
            "Check the Wardrobe":
                $ TheTimesCheckWardrobe += 1
                if TheTimesCheckWardrobe == 3:
                    w "\"I found something!\""
                    $ ExploreNotDone = False
                    "There's a secret grid inside the wardrobe!"
                    "There's a key inside the grid."
                    jump leaveTheRoom
                else:
                    "It's empty here."
                    jump SecondCheck
            "Check the Bedstand":
                "There's a notebook on the end table."
                "It doesn't look like Alice's... maybe someone else's?"
                play sound "audio/soundeffects/page_turn.wav"
                "Upon inspection, I found one page had been torn off."
                w "\"I bet the missing page is still in this room somewhere.\""
                jump SecondCheck

label leaveTheRoom:
    w "\"Okay, I got the key!\""
    w "\"I can leave this room and explore more.\""
    jump Part2Start
