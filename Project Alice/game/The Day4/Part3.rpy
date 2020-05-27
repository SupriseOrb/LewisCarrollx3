label Part3Start:
    scene basement night
    with fade
    "You came to the basement"
    "Alice was right, there is indeed some confusion in the environment here"
    "There are rats everywhere"
    call TheChoiceInPart3(1)

    "You come to the pile of ingredients, there are many ingredients here, but most of them are rotten"
    W "Let me see what I can find at here"
    W "Wait, let me think what Alice want me to bring her"
    call SelectVeg

    W "Okey, everything is here, it's time back to give to Alice"
    "You go to find Alice with the ingredients"

    scene diningroom night
    show Alice
    with dissolve

    A "Hey, welcome back my sweetyy"
    W "I find the thing you ask me to find"
    "You hand all the ingredients to Alice"
    "Alice is checking every single item carefully"
    if finishedMission:
        A "Good job Honey, everthing is perfect"
        "Alice smiled at you"
        A "And now I can cook a perfect dinner for you"
    else:
        "Alice frowned and shook her head"
        A "It looks like something was taken wrong"
        $ AliceInPain += 1
        "But no wory, Honey. I will try my best to figue out what I can do"
        "The smile back to Alice's face just in a second"

    hide Alice
    with dissolve
    "Alice turned and left with the ingredients "
    "You sit wearily on the sofa"
    "With the sound of cooking, you gradually fell asleep"

    scene black
    with dissolve

    "...zzz"

    scene table night
    show Alice
    with dissolve

    "When you woke up, Alice had already prepared dinner"
    "The sumptuousness of dinner exceeds your original imagination"
    "At the dining table, Alice said to me with a smile"
    A "It looks like you are really tired today, honey"
    "You nodded your head"
    A "Let's just stop my dull story, let's talk about something else"
    A "So...How do you think about.. um.... How do you think about the magical power"
    A "Do you think having magic is great for people?"
    call TheChoiceInPart3(2)

    "Alice become silence after she heard your answer"
    "After a couple of second"

    A "Your answer is great for me"
    "Alice suddenly said"
    A "How do you think about the violence"
    A "Do you agree that....some violence is unevitable?"
    call TheChoiceInPart3(3)

    "Again, Alice become silence after she heard your answer"
    "For a time, only the sound of knives and forks hitting plates and chewing echoed in the restaurant"
    "The depressed atmosphere makes you feel uncomfortable "
    "you try to eat the food as soon as possible to leave this silent table"

    A "One more question,honey"
    A "The last one for today, I swear"
    "Alice suddenly spoke again"
    A "Do you think that there is a particular connection between power and the violence?"
    call TheChoiceInPart3(4)


    "The atmosphere became cold again."
    if AliceFeltPain:
        jump ToTheDay5

    call TheChoiceInPart3(5)

    jump ToTheDay5
