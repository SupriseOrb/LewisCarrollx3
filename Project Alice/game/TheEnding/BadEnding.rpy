label badEndingSilence:
    A "Looks like you are really not interested in my story"
    A "Maybe I have to say Goodnight to you, my dear."
    hide Alice
    scene blcak
    with hpunch
    scene badending blood
    return

label badEndingUnhappy:
    "Alice sighed heavily"
    A "Your reaction really disappointed me"
    A "I feel so sad now"
    A "And I think my friend, which is you should share this sad feeling with me"
    A "COME OVER HERE"
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
