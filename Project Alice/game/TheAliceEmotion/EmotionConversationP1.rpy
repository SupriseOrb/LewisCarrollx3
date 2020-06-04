label checkTheSilenceP1:
    $ AliceReaction = ["\"Don't be so mean!\"", "\"I don't want to hear that.\"", "\"I don't like that.\"", "\"That's not very nice.\""]
    $ EmotionLevel =  AliceAngry-1
    if EmotionLevel < 0:
        $ EmotionLevel = 0
    elif EmotionLevel > 3:
        $ EmotionLevel = 3
    $ output = AliceReaction[EmotionLevel]
    if EmotionLevel <= 0:
        a annoyed "\"Don't be so mean!\""
    elif EmotionLevel == 1:
        a annoyed openeyes "[output]"
    elif EmotionLevel == 2:
        a angry "[output]"
    elif EmotionLevel >= 3:
        a unhappy "[output]"
    if AliceAngry==5:
        $ AliceHateU  = True
        jump badEndingSilence
    else:
        ##hide Alice angry
        ##show Alice normal
        ##with dissolve
        return

label checkTheFeeling:
    if AliceUnhappy==3:
        $ AliceFeltSad = True
        jump badEndingUnhappy
    else:
        return


label checkThePain:
    if AliceInPain ==5:
        $ AliceFeltPain = True
        jump badEndingUnhappy
    else:
        return
