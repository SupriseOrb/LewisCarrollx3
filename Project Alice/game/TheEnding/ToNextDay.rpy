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
        scene playerroom night
        "I returned to my room and instantly fell asleep."
        "...zzz"
        scene black
        jump day5

    if FinishThisBoringDay:
        "I quickly finished dinner and returned to my room, without so much as glancing back at Alice. I really needed a break."
        scene playerroom night
        with fade
        w "\"What a day.\""
        "As soon as my head hit the pillow, I fell asleep."
        scene black
        jump day5

        ###for the test
        return
