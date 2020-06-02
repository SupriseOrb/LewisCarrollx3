label ToTheDay5:
    if AliceFeltPain:
        a awkward "Sorry honey, I really felt tried now"
        "Alice's eyes were full of exhaustion."
        a guilty "I'm afraid we have to stop our conversation today now"
        "Alice stood up slowly"
        "She looked up at the sky in the night, a bright moon hung in the air, accompanied by twinkling stars, radiating holy light."
        "Alice looks at you again"
        a smile "Good night Honey, have a nice dream"
        "After Alice finished with a smile, she left the dining table and went up the stairs"
        "..."
        scene playerroom night
        "You returned to your room and fell into sleep."
        "...zzz"
        scene black
        jump day5

    if FinishThisBoringDay:
        "You quickly finished dinner and returned to your room"
        scene playerroom night
        with fade
        w "What a terrible day"
        "You lay in bed and fell asleep quickly"
        scene black
        jump day5

        ###for the test
        return
