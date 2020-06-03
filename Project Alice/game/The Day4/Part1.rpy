label day4:
    scene black
    scene playerroom morning
    with fade
    with Dissolve(2)

    play music morning fadein 2.0

    $ day = 4

    show screen Day with Dissolve(2)
    $ renpy.pause(3, hard=True)
    hide screen Day with Dissolve(4)

    "The next day, I was in the playroom. Alice had instructed me to wait here for her. She seemed off today. Even more off than usual."
    "..."
    play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0
    "The door to the playroom opened."

    a happy "\"Good Morning, Ms. Whitley.\""
    a smile "\"I hope you're enjoying your life here.\""
    a normal "\"I have a question for you. Are you a theist?\""

    menu:
        "Yes":
            jump firstTheistDone
        "No":
            pass

    label firstTheistDone:
    a smile "Interesting, I like your answer."
    a normal "Hey Ms. Whitley, do you want to hear my story?"
    
    "I looked at her wide-eyed. Just like that? She was going to tell me what's going on?"
    "Maybe she feels lonely...it must be getting to her."
    "I should get what I can from her, and be careful not to make her mad."

    stop music fadeout 3

    call TheChoiceInPart1(1)
    if AliceHateU:
        jump End

    play music "audio/BGM/Sad_Music_Box.mp3" fadein 3
    a awkward "\"My family used to be the richest in this town. Other families didn't like us much.\""
    a guilty "\"Maybe because my parents didn't really like talking with other people. Why else build a house in a neighborhood it doesn't belong in?"
    a awkward "\"Because of that...I didn't really make any friends. My parents never allowed me to outside.\""
    "Alice lowered her head."
    "But she smiled to herself and looked up at me fairly quickly."
    a happy "\"But my parents always stayed and played with me. They were so kind.\""
    a normal "\"They even gave me Miffy, my pet rabbit! Before I met Mr. Rabbit here.\""
    a smile "\"And she was my best friend.\""
    "..."
    "Alice seemed caught up in her own world now. I was afraid even the smallest word from me would bring her out of this trance."
    play sound "audio/soundeffects/sit_soft.wav" fadein 1.0
    "I let her sit beside me and continue."
    a guilty "\"Even so... my life was so boring. It was the same thing everytime! Good things! But...same things...\""
    a "\"I would play with Mr. Rabbit all day, and sometimes Aiden would tell me a good crazy story.\""

    call TheChoiceInPart1(2)
    if AliceHateU:
        jump End

    a guilty "\"Aiden is...was our housekeeper.\""
    a happy "\"He could do everything! Like driving, cooking, and even pipe repairing! The bathroom got completely FLOODED one time! But Aiden was there to fix it.\""
    a happy closeeyes "\"And the most important thing was...he's only one who told me stories about the outside world.\""
    a awkward "\"I loved those stories so much...\""
    "Alice trailed off as an abrupt, palpable melancholy seemed to wash over her."
    "I wondered....maybe something happened to Aiden."
    a happy "\"My parents liked Aiden a lot. They paid him really well! Maybe because my parents liked how we got along so well.\""
    a guilty "\"...I liked that too.\""
    "Alice suddenly stopped talking."
    "..."
    a "\"I thought my whole life would stay in this way, simple but peaceful.\""
    a "\"But there was one family show up, and they ruined my lovely life.\""
    "Alice frowned slightly, and after a while, Alice spoke again."
    a awkward "\"Sorry, honey. It still was a terrible memory for me.\""

    "Alice brought her knees up to her chest and buried her face behind them."

    call TheChoiceInPart1(3)

    if AliceHateU:
        jump End

    "Alice continued her story."
    a normal "\"The Adams family visited our family. They were important people. Rich like my parents.\""
    a guilty "\"That was the first time I met Luke. He's the youngest son of the Adams.\""
    a "\"He was talented. His parents called him brilliant and handsome. And the way he smiled just lit up the room.\""
    "Alice was praising the boy, but she didn't seem very happy about it."
    a awkward "\"But I have never had a chance to talk to him. He always stood behind his parents, just like me.\""
    "Alice shook her head. There was a regretful tone in her voice."
    a guilty "\"And that was the first time... I wanted to be friends with someone other than Miffy.\""
    "..."

    call TheChoiceInPart1(4)

    if AliceHateU:
        jump End

    a smile "\"So I snuck into my parents study and found spell that would help make him be friends with me.\""
    a normal "\"The spell said I could become friends with Luke. But it needed something in return.\""
    a guilty "\"I didn't know what, but I...would give up anything to try being friends with Luke.\""
    a awkward "\"So I performed the spell. It was really simple. It wasn't hard at all.\""
    "Alice lowered her head again and sighed slightly."
    a sorrow "\"After that, I couldn't find my Miffy that night.\""
    a "\"I looked for her everywhere, I asked everyone I could, but nobody had seen her.\""
    a guilty"\"The next day, Luke came to see me. He was holding Miffy in his arms.\""
    "Alice covered her mouth and sobbed quietly."
    a "\"She was so still...\""
    a "\"He said he found her at his door that morning.\""
    a awkward "\"Oh, I forgot to tell you, the Adams family were staying at a residence away from our house.\""
    "She pointed to a ruin outside the window. A once-beautiful home reduced to debris."
    "In this neighborhood, I hadn't paid it any heed. But looking at it now..."
    "..."
    a guilty "\"It was a guest house. My parents didn't want anyone else staying in our home.\""
    a "\"No matter how many times I think about it...I don't understand how she got all the way over there.\""
    "..."

    call TheChoiceInPart1(5)

    if AliceHateU:
        jump End

    a guilty "\"But you know, Ms. Whitley...Miffy actually helped me and Luke actually meet. We buried Miffy together.\""
    a awkward "\"It was sad, but Luke was really nice. He was kind and gentle, just like I thought! He knew about lots of things, like animals and flowers and sorts of rocks.\""
    a normal "\"It sounds boring...but the way he talked it about it made it so fun!\""
    a smile "\"I never felt so happy talking to someone.\""
    a unhappy closemouth "\"We became really good friends, you know, the inseparable kind.\""
    "It seemed like a happy memory, but there was something behind Alice's eyes. It was something sad...but it was something angry too."
    a normal "\"One day I was telling my parents about a time I played with Luke, and they got really upset.\""
    a guilty "\"They told me to stay away from Luke. They told me he was bad.\""
    "Alice smiled and raised her head slightly, as if trying to remember something."
    "..."
    call TheChoiceInPart1(6)

    if AliceHateU:
        jump End

    a awkward "\"If I had another chance, I would've listened to my parents'.\""
    w "What do you-"
    with vpunch
    play sound "audio/soundeffects/wood_bang.wav"
    stop music
    "Suddenly, there was a loud bang from upstairs. I jumped to my feet."
    "Alice was only slightly irritated."
    a unhappy "\"Can you stay here? Give me a couple of minutes, I'll be right back. It's just a noise problem.\""
    jump ExploreRoom
