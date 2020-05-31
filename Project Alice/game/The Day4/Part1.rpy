label day4:
    scene playerroom morning
    with fade

    show alice happy
    with dissolve

    "Someone is kocking my door"
    "..."
    "The door of my room was opened"

    A "Good Morning, Sweetheart"
    A "I hope you enjoy your life here"
    A "Tell me, Honey, are you a theist ?"

    menu:
        "Yes":
            jump firstTheistDone
        "No":
            pass

    label firstTheistDone:
    A "Interesting, I like your answer."
    A "Hey Sweetyy, do you want to hear my story?"


    call TheChoiceInPart1(1)
    if AliceHateU:
        jump End

    show Alice normal
    with dissolve
    A "My family used to be the richest in this town. Other families didn't like us much."
    A " Maybe because my parents don't want to socialize with others, and that's the reason why this house build in this remote place."
    A "And I have no friend in that time and apperently my parents never allowed me to hang out."
    "Alice lowered her head"
    "But she smiled and looked up at you soon"
    A "But my parents usually stay and play with me, they were so kind"
    A "They even sent me a rabbit as a gift, I called her Miffy and she is my best friend."
    "..."
    A "The daily life was so boring at that time, I played with Miffy all day, and sometime Aiden would tell me some crazy story."

    call TheChoiceInPart1(2)
    if AliceHateU:
        jump End

    show Alice normal
    with dissolve
    A "Aiden is the housekeeper in our family at that time."
    A "and Aiden could do many things, like driving, cooking, and pipe repairing."
    A "And the most important thing was, he is the only one who would tell me the story of the outside world. I love his story so much."
    "Alice's expression became sad because something"
    "Maybe something happened on Aiden"
    A "My parents like Aiden and they paid high salary to Aiden, maybe because my parents like his patient."
    A "So do I."
    "Alice suddenly stopped talking"
    "..."
    A "I was thinking that my rest whole life will stay in this way, but one family showed over in our house and they changed my life."
    hide Alice
    with dissolve
    show Alice sad
    with dissolve

    A " That was a terrible memory for me."

    "Alice looks very sad"

    call TheChoiceInPart1(3)

    if AliceHateU:
        jump End

    show Alice normal
    with dissolve
    A "Adams family visited our family at that time. They were relative to my mother."
    A "That was the first time I met Luck, who was the youngest son in the Addams family."
    A "He was excellent, and the way he smiled was fascinating. "
    "Alice was praising the boy, but Alice didn’t look very happy"
    A "But I have never had a chance to talk to him, he always stands behind his parents, just like me."
    "Alice shook her head, as if regretting"
    A "And that was also the first time it shows over in my head."
    "..."

    call TheChoiceInPart1(4)

    if AliceHateU:
        jump End

    show Alice normal
    with dissolve
    A "It tells me that I could become friend with Luke if I were willing to pay the sacrifice."
    A "Of course I said yes"
    "Alice lowered her head again and sighed slightly."
    A "After that, I found that I can't find my Miffy that night"
    A "I looked for her everywhere, I asked almost everyone, but they all said they did not see her"
    A "The next day, Luke came to see me with Miffy's body. He said it was found at his door in the morning. "
    A "Oh, I forgot to tell you that, Luke and their family weren't live in this house."
    "Alice points to a ruin outside the window"
    "..."
    A "They lived in that house, which is for the guest. My parents didn't want others to live in this house."
    A "So I was curious why she ran so far that night"
    "..."

    call TheChoiceInPart1(5)

    if AliceHateU:
        jump End

    show Alice happy
    with dissolve
    A "Anyway, Miffy became an opportunity for me and Luke to meet, and we buried Miffy together. "
    A "And Luck is as polite and gentile as I thought, and he knows a lot of things, I have never felt so happy talking to a person in that time"
    A "We soon became good friends, you know, the inseparable kind. "
    "Although she is talking some happy memory, she looks angry which is so strange."
    A "But when my parents noticed my relationship with Luke, they told me to stay away from Luke because he approached me with bad intentions."
    "Alice smiled and raised her head slightly, as if trying to remember something"
    "..."
    call TheChoiceInPart1(6)

    if AliceHateU:
        jump End

    show Alice normal
    with dissolve
    A "If you give me another chance, I will listen to my parents' advice."
    A "But then something happened and Luke and his family left here"
    A "He..."
    with vpunch
    "There was a loud voice from the upstairs."
    A "Give me a couple of minutes, Honey. I have to solve the noise problem"
    hide Alice
    with dissolve

    jump ExploreRoom
