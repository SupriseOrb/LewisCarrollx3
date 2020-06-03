label badEndingSilence:
    stop music fadeout 3
    a awkward  "\"It seems like you really don't care about my story, do you?\""
    w "\"I -\""
    a smile "\"It's okay! We'll just have to say goodnight early, Ms. Whitley.\""
    play music "audio/BGM/Sad_Dark.mp3" fadein 1
    scene black with Dissolve(2)
    with hpunch
    scene badending blood with Dissolve(2)
    show screen Ending("{font=fonts/TheAncient.ttf}{size=+15}{size=+60}Bad Ending{/size}\n\n{space=300}{font=fonts/Cageworld.ttf}- Silent Wonderland{/font}{/size}{/font}") with Dissolve(2)
    $ renpy.pause(3, hard=True)
    pause(5)
    return

label badEndingUnhappy:
    stop music fadeout 3
    "Alice sighed heavily."
    ##a unhappy "\"That's not what I wanted to hear.\""
    a unhappy closemouth "\"I...I feel so sad now...\""
    a "\"I think, Ms. Whitley, you ought to feel this sadness too....\""
    a happy strange "\"COME AND SHARE IT WITH ME.\""
    play music "audio/BGM/Sad_Dark.mp3" fadein 1
    scene black with Dissolve(2)
    with hpunch
    scene badending blood with Dissolve(2)
    show screen Ending("{font=fonts/TheAncient.ttf}{size=+15}{size=+60}Bad Ending{/size}\n\n{space=300}{font=fonts/Cageworld.ttf}- Painful Princess{/font}{/size}{/font}") with Dissolve(2)
    $ renpy.pause(3, hard=True)
    hide screen Ending with Dissolve(4)
    pause(5)
    return

label End:
    if AliceHateU:
        return
    elif AliceUnhappy:
        return
    else:
        jump day5
