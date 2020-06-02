label day4:
    scene playerroom noon
    with fade

    show alice happy
    with dissolve

    "The next day, I was in the playroom. Alice had instructed me to wait here for her. She seemed off today. Even more off than usual."
    "..."
    "The door to the playroom opened."

    A "\"Good Morning, Ms. Whitley.\""
    A "\"I hope you're enjoying your life here.\""
    A "\"I have a question for you. Are you a theist?\""

    menu:
        "Yes":
            jump firstTheistDone
        "No":
            pass

    label firstTheistDone:
    A "Interesting, I like your answer."
    A "Hey Ms. Whitley, do you want to hear my story?"
    
    "I looked at her wide-eyed. Just like that? She was going to tell me what's going on?"
    "Maybe she feels lonely...it must be getting to her."
    "I should get what I can from her, and be careful not to make her mad."

    call TheChoiceInPart1(1)
    if AliceHateU:
        jump End

    show Alice normal
    with dissolve
    A "\"My family used to be the richest in this town. Other families didn't like us much.\""
    A "\"Maybe because my parents didn't really like talking with other people. Why else build a house in a neighborhood it doesn't belong in?"
    A "\"Because of that...I didn't really make any friends. My parents never allowed me to outside.\""
    "Alice lowered her head."
    "But she smiled to herself and looked up at me fairly quickly."
    A "\"But my parents always stayed and played with me. They were so kind.\""
    A "\"They even gave me Miffy, my pet rabbit! Before I met Mr. Rabbit here.\""
    A "\"And she was my best friend.\""
    "..."
    "Alice seemed caught up in her own world now. I was afraid even the smallest word from me would bring her out of this trance."
    "I let her sit beside me and continue."
    A "\"Even so... my life was so boring. It was the same thing everytime! Good things! But...same things...\""
    A "\"I would play with Mr. Rabbit all day, and sometimes Aiden would tell me a good crazy story.\""

    call TheChoiceInPart1(2)
    if AliceHateU:
        jump End

    show Alice normal
    with dissolve
    A "\"Aiden is...was our housekeeper.\""
    A "\"He could do everything! Like driving, cooking, and even pipe repairing! The bathroom got completely FLOODED one time! But Aiden was there to fix it.\""
    A "\"And the most important thing was...he's only one who told me stories about the outside world.\""
    A "\"I loved those stories so much...\""
    "Alice trailed off as an abrupt, palpable melancholy seemed to wash over her."
    "I wondered....maybe something happened to Aiden."
    A "\"My parents liked Aiden a lot. They paid him really well! Maybe because my parents liked how we got along so well.\""
    A "\"...I liked that too.\""
    "Alice suddenly stopped talking."
    "..."
    A "\"I thought my whole life would stay that way...but then, one family showed up at our house and they changed my life.\""
    hide Alice
    with dissolve
    show Alice sad
    with dissolve

    A "\"But now, it's a terrible memory.\""

    "Alice brought her knees up to her chest and buried her face behind them."

    call TheChoiceInPart1(3)

    if AliceHateU:
        jump End

    show Alice normal
    with dissolve
    "Alice continued her story."
    A "\"The Adams family visited our family. They were important people. Rich like my parents.\""
    A "\"That was the first time I met Luke. He's the youngest son of the Adams.\""
    A "\"He was talented. His parents called him brilliant and handsome. And the way he smiled just lit up the room.\""
    "Alice was praising the boy, but she didn't seem very happy about it."
    A "\"But I have never had a chance to talk to him. He always stood behind his parents, just like me.\""
    "Alice shook her head. There was a regretful tone in her voice."
    A "\"And that was the first time... I wanted to be friends with someone other than Miffy.\""
    "..."

    call TheChoiceInPart1(4)

    if AliceHateU:
        jump End

    show Alice normal
    with dissolve
    A "\"So I snuck into my parents study and found spell that would help make him be friends with me.\""
    A "\"The spell said I could become friends with Luke. But it needed something in return.\""
    A "\"I didn't know what, but I...would give up anything to try being friends with Luke.\""
    A "\"So I performed the spell. It was really simple. It wasn't hard at all.\""
    "Alice lowered her head again and sighed slightly."
    A "\"After that, I couldn't find my Miffy that night.\""
    A "\"I looked for her everywhere, I asked everyone I could, but nobody had seen her.\""
    A "\"The next day, Luke came to see me. He was holding Miffy in his arms.\""
    "Alice covered her mouth and sobbed quietly."
    A "\"She was so still...\""
    A "\"He said he found her at his door that morning.\""
    A "\"Oh, I forgot to tell you, the Adams family were staying at a residence away from our house.\""
    "She pointed to a ruin outside the window. A once-beautiful home reduced to debris."
    "In this neighborhood, I hadn't paid it any heed. But looking at it now..."
    "..."
    A "\"It was a guest house. My parents didn't want anyone else staying in our home.\""
    A "\"No matter how many times I think about it...I don't understand how she got all the way over there.\""
    "..."

    call TheChoiceInPart1(5)

    if AliceHateU:
        jump End

    show Alice happy
    with dissolve
    A "\"But you know, Ms. Whitley...Miffy actually helped me and Luke actually meet. We buried Miffy together.\""
    A "\"It was sad, but Luke was really nice. He was kind and gentle, just like I thought! He knew about lots of things, like animals and flowers and sorts of rocks.\""
    A "\"It sounds boring...but the way he talked it about it made it so fun!\""
    A "\"I never felt so happy talking to someone.\""
    A "\"We became really good friends, you know, the inseparable kind.\""
    "It seemed like a happy memory, but there was something behind Alice's eyes. It was something sad...but it was something angry too."
    A "\"One day I was telling my parents about a time I played with Luke, and they got really upset.\""
    A "\"They told me to stay away from Luke. They told me he was bad.\""
    "Alice smiled and raised her head slightly, as if trying to remember something."
    "..."
    call TheChoiceInPart1(6)

    if AliceHateU:
        jump End

    show Alice normal
    with dissolve
    A "\"If I had another chance, I would've listened to my parents'.\""
    w "What do you-"
    with vpunch
    "Suddenly, there was a loud bang from upstairs. I jumped to my feet."
    "Alice was only slightly irritated."
    A "\"Can you stay here? Give me a couple of minutes, I'll be right back. It's just a noise problem.\""
    hide Alice
    with dissolve

    jump ExploreRoom
