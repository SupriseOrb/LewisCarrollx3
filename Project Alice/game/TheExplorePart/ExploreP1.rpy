label ExploreRoom:
    scene playerroom noon
    show Whitley
    "I was worried about what that bang was, but this gave me a chance to explore more of the house."
    W "\"Let's see what I can find.\""
    hide Whitley
    with dissolve

$ CheckTheWayOut = True
$ CheckTheDoor = False
$ CheckTheWindow = False
label FirstCheck:
    label check1:
    while CheckTheWayOut:
        if CheckTheDoor and CheckTheWindow:
            $ CheckTheWayOut = False
            jump check1
        menu:
            "Check the door":
                $ CheckTheDoor = True
                "The door is locked."
                show Whitley
                W "\"The door is locked, maybe I can find a key somewhere.\""
                hide Whitley
                with dissolve
                jump FirstCheck
            "Check the widow":
                $ CheckTheWindow = True
                "The window is locked."
                show Whitley
                W "\"No way out.\""
                hide Whitley
                with dissolve
                jump FirstCheck

    show Whitley
    W "\"All the ways out are locked, maybe I can find something from this room to get me out this room.\""
    hide Whitley
    with dissolve

$ TheTimesCheckWardrobe=0
$ ExploreNotDone=True
$ CheckUnderBed=True
label SecondCheck:
    label check2:
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
                                W "\"I found something!\""
                                "A piece of paper, it looks like a note. It reads:"
                                "*REMINDER*"
                                "I put the false key in the WARDROBE."
                                "Try checking there if you can't find it. Check it again if you have to."
                                "- Aiden"
                                W "\"Oh Aiden, you're a lifesaver.\""
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
                    W "\"I found something!\""
                    $ ExploreNotDone = False
                    "There's a secret grid inside the wardrobe!"
                    "There's a key inside the grid."
                    jump leaveTheRoom
                else:
                    "It's empty here."
                    jump SecondCheck
            "Check the Bedstand":
                "There's a notebook on the end table."
                "It doesn't look like Alice's...maybe someone else?"
                "Upon inspection, I found one page had been torn off."
                W "\"I bet the missing page is still in this room somewhere.\""
                jump SecondCheck

label leaveTheRoom:
    W "\"Okay, I got the key!\""
    W "\"I can leave this room and explore more.\""
    jump Part2Start
