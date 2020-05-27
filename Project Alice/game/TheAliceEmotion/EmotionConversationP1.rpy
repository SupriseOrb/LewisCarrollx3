label checkTheSilenceP1:
    $ AliceReaction = ["Don't be so mean, honey", "Why your words so harsh word, honey", "Hey.Stop saying those sarcasm", "You brock my heart"]
    $ EmotionLevel =  AliceAngry-2
    $ output = AliceReaction[EmotionLevel]
    show Alice angry
    A "[output]"
    if AliceAngry==5:
        $ AliceHateU  = True
        jump badEndingSilence
    else:
        hide Alice angry
        show Alice normal
        with dissolve
        return

label checkTheFeeling:
    if AliceUnhappy==3:
        $ AliceFeltSad = True
        jump badEndingFeeling
    else:
        return


label checkThePain:
    if AliceInPain ==5:
        $ AliceFeltPain = True
        return
    else:
        return
