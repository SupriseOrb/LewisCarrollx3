label ExploreRoom:
    scene playerroom noon
    show Whitley
    W "Finally, let see what I can do now"
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
                W "The door is locked, maybe can find the key somewhere"
                hide Whitley
                with dissolve
                jump FirstCheck
            "Check the widow":
                $ CheckTheWindow = True
                "The window is locked."
                show Whitley
                W "No way out."
                hide Whitley
                with dissolve
                jump FirstCheck

    show Whitley
    W "All the ways out are locked, maybe I can find something from this room to get me out this room"
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
                "There is a name carved on the table, Aiden"
                "Maybe the room used to be Aiden's room"
                jump SecondCheck
            "Check under the bed":
                "Can't see clearly under the bed"
                label check3:
                while CheckUnderBed:
                    menu:
                        "Try to find something by hand":
                            $ getsomething=renpy.random.randint(0,1)
                            if getsomething==1:
                                W "I find something!"
                                "You find a paper, it seems like a note"
                                "The REMINDER"
                                "I put the false key in the WARDROBE"
                                "Try to check a couple of times"
                                "Aiden"
                                W "Oh, I love you so much, Aiden"
                                $ CheckUnderBed = False
                                jump check2
                            else:
                                "Find nothing"
                                jump check3
                        "I don't think I can find things here":
                            jump check2
                if CheckUnderBed:
                    jump SecondCheck
                else:
                    "There is nothing here, maybe I should check the Wardrobe more than once"
                    jump SecondCheck
            "Check the Wardrobe":
                $ TheTimesCheckWardrobe += 1
                if TheTimesCheckWardrobe == 3:
                    W "I find something!"
                    $ ExploreNotDone = False
                    "You find a secret grid in the Wardrobe"
                    "There is a key inside"
                    jump leaveTheRoom
                else:
                    "It's empty here"
                    jump SecondCheck
            "Check the Bedstand":
                "There is a notebook on the bedstand"
                "It seems belong to the last room user"
                "There is one page was torn off"
                W "Maybe I can check the bed to find that page"
                jump SecondCheck

label leaveTheRoom:
    W "Okey, I got the key"
    W "I can leave this room now."
    jump Part2Start
