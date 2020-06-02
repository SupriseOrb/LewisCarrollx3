# The collection of the choice for the part1:

label TheChoiceInPart1(numberP1):
    if numberP1==1:
        menu:
            "Yes, I would like to hear your story.":
                a smile "\"Oh, you are so kind, Ms. Whitley!\""
                return
            "Maybe you can tell me some other time?":
                a sad  "\"Don't be so mean! I want to tell it now. It's not that bad, I promise.\""
                $ AliceAngry +=1
                return
    elif numberP1==2:
        menu:
            "Wait, who is Aiden?":
                return
            "This seems painful for you to talk about, maybe you shouldn't...":
                $ AliceAngry +=1
                call checkTheSilenceP1
                return
    elif numberP1==3:
        menu:
            "Are you okay?":
                "Alice sniffed and rubbed her eyes."
                a awkward "Yes. I'm okay. Thank you."
                return
            "Oh, Alice. I told you, crying won't solve anything.":
                $ AliceAngry +=1
                call checkTheSilenceP1
                return
    elif numberP1==4:
        menu:
            "It sounds like it was love at first sight!":
                a smile "\"Probably.\""
                "Alice giggled. It was nice to see her smile for once, but it didn't last long."
                a guilty "\"...I wish you were there to meet that boy with me, Ms. Whitley. I bet you could've told me what I was feeling then.\""
                return
            "It sounds like you were really lonely, even before your parents passed.":
                $ AliceAngry +=1
                call checkTheSilenceP1
                return
    elif numberP1==5:
        menu:
            "How did that house burn down?":
                a sorrow "\"Umm..... That's because... an accident happened.\""
                return
            "I'm sorry about Miffy, Alice":
                a normal "Thank you, Ms. Whitley."
                return
            "You can't do anything about now.":
                $ AliceAngry +=1
                call checkTheSilenceP1
                return
    else:
        menu:
            "So did you obey your parents?":
                a awkward "\"...I wish I did.\""
                return
            "Were your parents right?":
                a guilty "\"I think they were.\""
                return
            "You shouldn't trust strangers.":
                $ AliceAngry +=1
                call checkTheSilenceP1
                return
