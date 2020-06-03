label Part3Start:
    play sound "audio/soundeffects/whitley_walk.wav" fadein 1
    scene basement night
    with fade
    with Dissolve(2)
    stop sound fadeout 2
    "I went down to the basement, still trying to parse through that crazy dream Alice put me through."
    play sound "audio/soundeffects/rat_squeak.wav" fadein 2
    "I heard a loud squeak and abruptly realized that she was right. There were some critters down here!"
    "But they weren't cute little mice, they were rats. And they were rats everywhere"
    stop sound fadeout 2
    call TheChoiceInPart3(1)

    play sound "audio/soundeffects/whitley_walk.wav" fadein 1
    "I walked over to a pile of ingredients, but upon closer inspection, it looked like most of them were rotten."
    stop sound fadeout 2
    w "\"Let me see what I can find over here...\""
    w "\"Wait, what was it Alice wanted me to bring her again?\""
    call SelectVeg

    w "\"Okay, everything looks like it's here. Time to go back and give it to Alice.\""
    play sound "audio/soundeffects/whitley_walk.wav" fadein 1
    "I went back upstairs with the ingredients to find Alice."
    stop sound fadeout 2

    scene diningroom night with Dissolve(2)

    a normal "\"Hey, welcome back, Ms. Whitley!\""
    w "\"I found the stuff you asked me to find.\""
    "I handed all the ingredients over to Alice."
    "\"Alice checked every single item carefully.\""
    if finishedMission:
        "Finally, she nodded in satisfaction."
        a happy "\"Good job! Everything is perfect.\""
        "Alice smiled at me."
        a happy closemouth "\"And now I can cook a perfect dinner, just for you!\""
    
    else:
        "Alice frowned and shook her head."
        a awkward "\"No, something isn't right here... These ingredients are wrong.\""
        $ AliceInPain += 1
        a happy "\"But no worries! I'll just have to try my best and figure out what I can do!\""
        "In just a second, a smile was back on Alice's face."

    "Alice turned and left with the ingredients."
    play sound "audio/soundeffects/sit_soft.wav"
    "I wearily sat down on the sofa."
    play sound "audio/soundeffects/cooking.wav" fadein 3
    "With the sound of cooking, I gradually fell asleep."

    show black with Dissolve(1)

    hide black with Dissolve(0.8)

    show black with Dissolve(2)

    "...zzz"

    stop sound fadeout 1

    scene table night with Dissolve(3)

    hide black with Dissolve(3)

    "When I woke up, Alice had already finished preparing dinner."
    "The sumptuousness of dinner exceeded my original imagination."
    "At the dining table, Alice said to me with a smile -"
    a smile "\"It looks like you are really tired today, Ms. Whitley.\""
    "I can't do anything but nod. I really am exhausted."
    a normal "\"Then let's just stop my story, it's dull anyway. Let's talk about something else!\""
    a happy "\"So...um... Oh! What do you think about my magic!\""
    a normal "\"You've been here long enough now! Tell me what you think!\""
    a smile "\"Don't you think it's just the best?\""
    call TheChoiceInPart3(2)

    "Alice grew silent after she heard my answer."
    "After a pause of a couple of seconds, she spoke again."

    a normal "\"That's a great answer.\""
    "Alice suddenly leaned in and grinned wide at me."
    a normal "\"And what about hurting people?\""
    a guilty "\"Do you think that....sometimes, you just can't avoid it?\""
    call TheChoiceInPart3(3)

    "Again, Alice was silent after my answer."
    "For a time, only the sound of chewing and knives and forks hitting plates echoed in the dining room."
    "I felt uncomfortable in my chair as a depressive air loomed over us."
    "I tried to eat the food as fast as possible just to leave this silent table."
    "To my dismay, Alice spoke again before I could finish."

    a smile "\"One more question, Ms. Whitley.\""
    a normal "\"The last one for today, I promise.\""
    "Before I could say anything, she jumped right into it."
    a confused "\"Do you think that power and hurting people are connected somehow?.\""
    call TheChoiceInPart3(4)


    "The atmosphere became cold again."
    if AliceFeltPain:

        jump ToTheDay5

    call TheChoiceInPart3(5)

    jump ToTheDay5
