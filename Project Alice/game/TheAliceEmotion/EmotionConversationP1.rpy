label checkTheSilenceP1:
    $ AliceReaction = ["\"Don't be so mean!\"", "\"I don't want to hear that.\"", "\"I don't like that.\"", "\"That's not very nice.\""]
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
