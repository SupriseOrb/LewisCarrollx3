label badEndingSilence:
    A "\"It seems like you really don't care about my story, do you?\""
    w "\"I -\""
    A "\"It's okay! We'll just have to say goodnight early, Ms. Whitley.\""
    hide Alice
    scene blcak
    with hpunch
    scene badending blood
    return

label badEndingUnhappy:
    "Alice sighed heavily."
    A "\"That's not what I wanted to hear.\""
    A "\"I...I feel so sad now...\""
    A "\"I think, Ms. Whitley, you ought to feel this sadness too....\""
    A "\"COME AND SHARE IT WITH ME.\""
    hide Alice
    scene blcak
    with hpunch
    scene badending blood
    return

label End:
    if AliceHateU:
        return
    elif AliceUnhappy:
        return
    else:
        jump day5
