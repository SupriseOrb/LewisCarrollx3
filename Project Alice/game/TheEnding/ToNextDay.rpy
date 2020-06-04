label ToTheDay5:
    if AliceFeltPain:
        a awkward "\"Sorry Ms. Whitley, I really feel tired right now...\""
        "Alice's eyes were full of exhaustion."
        a guilty "\"I think I'm done for today...\""
        "Alice stood up slowly."
        "She looked up at the night sky where a bright moon hung in the air, accompanied by twinkling stars, radiating a holy light."
        "Alice looked at me again."
        a smile "\"Good night Ms. Whitley, sweet dreams.\""
        "Alice finished with a smile, then she left the dining table and went upstairs."
        "..."
        $ persistent.heart +=1
        play sound "audio/soundeffects/whitley_walk.wav" fadein 1
        show black with Dissolve(1)
        scene playerroom night with Dissolve(1)
        hide black with Dissolve(1)
        stop sound fadeout 2
        "I returned to my room and instantly fell asleep."
        "...zzz"

        stop music fadeout(3)
        show black with Dissolve(3)
        pause(3)
        $ renpy.music.set_volume(1, delay=0, channel='music')
        jump day5

    if FinishThisBoringDay:
        "I quickly finished dinner and returned to my room, without so much as glancing back at Alice. I really needed a break."
        play sound "audio/soundeffects/whitley_walk.wav" fadein 1
        show black with Dissolve(1)
        scene playerroom night with Dissolve(1)
        hide black with Dissolve(1)
        stop sound fadeout 2
        w "\"What a day.\""
        "As soon as my head hit the pillow, I fell asleep."

        stop music fadeout(3)
        show black with Dissolve(3)
        pause(3)
        $ renpy.music.set_volume(1, delay=0, channel='music')
        jump day5

        ###for the test
        return
