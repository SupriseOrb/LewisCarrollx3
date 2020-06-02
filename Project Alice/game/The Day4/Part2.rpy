label Part2Start:
    "When I opened the door and took my first step outside it, to my horror, my feet didn't find ground!"
    "I tried to regain my balance, but quickly found myself reeling back and falling into an abyss."
    with vpunch
    scene black
    show Whitley
    W "\"Ugh... Where am I?\""
    W "\"Why is it so dark?\""
    "Suddenly my eyes caught a girl in the darkness, squatting right in front of me. But she was focused on something else..."
    "I couldn't see her face clearly, but she looked as though she was expecting something"
    W "\"Uhh hello, what are we doing down here? What is this place?\""
    "She didn't respond to me. She didn't even seem to care that I spoke."

    call TheChoiceInPart2(1)

    hide Whitley
    "As my eyes slowly adapted to the dark environment, I realized I was in a closet."
    "The little girl in front of me was peeking outside through a small gap between the closet doors."
    "Suddenly, there was a voice from outside, two people talking with their feet shuffling over the wooden floor"
    "As the sound got closer, I could sense excitement rising in the girl. She pushed herself closer to the gap, desperate to see."

    "???" "\"Aren't you supposed to be with Alice today, Luke?\""

    W "\"Luke? The boy Alice mentioned before?\""
    W "\"So this girl.....\""
    "I looked at the girl hiding in the closet." 
    W "\"Alice?\""
    "I tried to get a closer look, but this closet was pitch black."

    "Luke" "\"Not right now. It's her nap time, thank God.\""
    "???" "\"I thought you enjoyed playing with the Hearts' little princess.\""
    "Luke" "\"Are you kidding me? If it weren't for Dad, I wouldn't even be talking to that freak.\""
    "The other, older boy let out a hearty laugh."
    "???" "\"But I thought you {i}liked{/i} her! You're always talking and laughing when you're with her.\""
    "Luke wasn't amused by the boy's mocking tone."
    "Luke" "\"Leave me alone! I'm already tired of Dad making me smile at her every day, I don't need you making fun of me.\""

    "I watched the little girl sink down, shoulders slackened, head bowed."

    "Luke" "\"You wouldn't believe how stupid she is. She always asks the silliest questions.\""
    "Luke" "\"There are better things to talk about than dumb tea parties and rabbits.\""
    "Luke" "\"And she'll get angry at you for no reason, just because you aren't playing her game right or something ridiculous like that.\""
    "???" "\"Hey, Dad said you have to be friends with her, be careful how much you badmouth her.\""
    "Luke" "\"Friends? I'm like her {i}babysitter.{/i}\""
    "Luke" "\"All she wants is attention.\""
    "Luke" "\"Anyone could be her \'friend\', as long as you can put up with her stupid stories.\""

    "I heard the girl begin to softly cry."
    "Her shoulders trembled slightly as she tried to cover her mouth to stifle the sobs."
    "But the tears soon overflowed, streaking over her cupped hands before dripping to the floor."
    "The two people outside continued on their chat, laughing loudly from time to time."

    call TheChoiceInPart2(2)

    with vpunch
    scene playerroom night
    with fade
    show Alice normal
    "I looked up to see Alice standing in front of me. It was nighttime already? When did it get so late?"
    A "\"...I guess you already saw the part of the story that's next, hm Ms. Whitley?\""
    call TheChoiceInPart2(3)

    A "\"Luke was tricking me. The whole time. I thought he was my only real friend, but this whole time..."
    A "\"He thought I was annoying. I never really mattered to him.\""
    A "\"I'm sorry for showing you the story like that...\""
    A "\"But these memories are always hard to say.\""
    call TheChoiceInPart2(4)

    A "\"After that, I ran back to my parents crying. They took care of me that day.\""
    A "\"After that...I knew Mom and Dad were the only people who cared about.\""
    "Alice gave me a vacant grin."
    A "\"and I don't need anyone else to be my friends.\""
    "She said it so casually, as if it was the only truth in the world."
    "Alice..."
    A "\"The Adams family were asking my parents for money, you know.\""
    A "\"But my parents kept turning them away, so they thought maybe they could get through to them...from me.\""
    "Alice giggled to herself."
    A "\"Sillies. They got kicked out that night.\""
    call TheChoiceInPart2(5)

    A "\"Anyway, let's get dinner started!\""
    A "\"There are some things in the basement we need first, though.\""
    call setTheIngre
    A "\"But there are some critters down there, like mice.\""
    A "\"I hope it's okay that I stay up here and you go get those things for me! Oh and you could do some cleaning while you're at it!\""
    call TheChoiceInPart2(6)

    jump Part3Start
