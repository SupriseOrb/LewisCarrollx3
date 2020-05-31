# The collection of the choice for the part1:

label TheChoiceInPart1(numberP1):
    if numberP1==1:
        menu:
            "Yes,I do":
                A "Oh, you are so kind Sweetheart!"
                return
            "No, screw you!":
                show alice sad
                A  "Don't be so mean Honey. My story was not that terrible "
                $ AliceAngry +=1
                return
    elif numberP1==2:
        menu:
            "Wait, who is Aiden?":
                return
            "I don't care about your silly childhood":
                $ AliceAngry +=1
                call checkTheSilenceP1
                return
    elif numberP1==3:
        menu:
            "Are you okey?":
                show Alice happy
                A "Yes, my sweetyy, thanks for your concern. I feel better now."
                return
            "Looks someone is almost crying haha":
                $ AliceAngry +=1
                call checkTheSilenceP1
                return
    elif numberP1==4:
        menu:
            "What is it ?":
                A "I named it Mr.Voice, I haven't seen it physically, but I can hear it's a voice in my head."
                return
            "You mean you fell in love with a boy in the first sight?":
                A "Probably, I wish you would have a chance to meet that boy, sweetheart. I bet you would have the feeling with me, which makes you want to own that boy."
                return
            "Who care about your lonely soul?":
                $ AliceAngry +=1
                call checkTheSilenceP1
                return
    elif numberP1==5:
        menu:
            "But why that house was burnt down?":
                A sad "umm..... That's because... some accident happened."
                return
            "Sorry for the Miffy, Alice":
                A normal "Thank you, sweetyy"
                return
            "I wonder the taste of rabbit, haha":
                $ AliceAngry +=1
                call checkTheSilenceP1
                return
    else:
        menu:
            "So did you obey your parents?":
                A "I hope I did."
                return
            "Your parents was right":
                A "I get it now."
                return
            "Finally, someone came to wake up the ugly duckling's dream.":
                $ AliceAngry +=1
                call checkTheSilenceP1
                return
