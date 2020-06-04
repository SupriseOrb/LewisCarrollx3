label Part2Start:
    "When I opened the door and took my first step outside it, to my horror, my feet didn't find ground!"
    "I tried to regain my balance, but quickly found myself reeling back and falling into an abyss."
    with vpunch
    scene black
    w "\"Ughh... Where am I?\""
    w "\"Why is it so dark?\""
    "Suddenly my eyes caught a girl in the darkness, squatting right in front of me. But she was focused on something else..."
    "I couldn't see her face clearly, but she looked as though she was expecting something."
    w "\"Uhh hello, what are we doing down here? What is this place?\""
    "She didn't respond to me."

    call TheChoiceInPart2(1)
    "As my eyes slowly adapted to the dark environment, I realized I was in a closet."
    "The little girl in front of me was peeking outside through a small gap between the closet doors."
    "Suddenly, there was a voice from outside, two people talking with their feet shuffling over the wooden floor"
    "As the sound got closer, I could sense excitement rising in the girl. She pushed herself closer to the gap, desperate to see."

    q "\"Aren't you supposed to be with Alice today, Luke?\""

    w "\"Luke? The boy Alice mentioned before?\""
    w "\"So this girl.....\""
    "I looked at the girl hiding in the closet."
    w "\"Alice?\""
    "I tried to get a closer look, but the closet was pitch black."

    l "\"Not right now. It's her nap time, thank God.\""
    q "\"I thought you enjoyed playing with the Hearts' little princess.\""
    l "\"Are you kidding me? If it weren't for Dad, I wouldn't even be talking to that freak.\""
    "The other, older boy let out a hearty laugh."
    q "\"But I thought you {i}liked{/i} her! You're always talking and laughing when you're with her.\""
    "Luke wasn't amused by the boy's mocking tone."
    l "\"Leave me alone! I'm already tired of Dad making me smile at her every day. I don't need you making fun of me.\""

    "I watched the little girl sink down, shoulders slackened, head bowed."

    l "\"You wouldn't believe how stupid she is. She always asks the silliest questions.\""
    l "\"There are better things to talk about than dumb tea parties and rabbits.\""
    l "\"And she'll get angry at you for no reason, just because you aren't playing her game right or something ridiculous like that.\""
    q "\"Hey, Dad said you have to be friends with her. Be careful how much you badmouth her.\""
    l "\"Friends? I'm like her {i}babysitter{/i}.\""
    l "\"All she wants is attention.\""
    l "\"Anyone could be her \'friend\', as long as you can put up with her stupid stories.\""

    "The girl began to softly cry."
    "Her shoulders trembled slightly as she tried to cover her mouth to stifle the sobs."
    "But the tears soon overflowed, streaking over her cupped hands before dripping to the floor."
    "The two people outside continued on their chat, laughing loudly from time to time."

    call TheChoiceInPart2(2)

    with vpunch
    scene playerroom night
    with fade
    "I looked up to see Alice standing in front of me. It was nighttime already? When did it get so late?"
    a smile "\"...I guess you already saw the part of the story that's next, hm Ms. Whitley?\""
    call TheChoiceInPart2(3)

    a happy strange "\"Luke was tricking me. The whole time. I thought he was my only real friend, but this whole time..."
    a smile "\"He thought I was annoying. I never really mattered to him.\""
    a guilty "\"I'm sorry for showing you the story like that...\""
    a awkward "\"But these memories are always hard to say.\""
    call TheChoiceInPart2(4)

    a unhappy "\"After that, I ran back to my parents crying. They took care of me that day.\""
    a unhappy closemouth "\"I knew Mom and Dad were the only people who cared about me.\""
    "Alice gave me a vacant grin."
    a smile "\"And I don't need anyone else.\""
    "She said it so casually, as if it was the only truth in the world."
    "Alice..."
    a angry "\"The Adams family were constantly asking my parents for money, you know.\""
    a confused "\"But my parents kept turning them away, so they thought maybe they could get through to them... through me.\""
    "Alice giggled to herself."
    a happy strange "\"Sillies. They got kicked out that night.\""
    call TheChoiceInPart2(5)

    a smile "\"Anyway, let's get dinner started!\""
    a normal "\"There are some things in the basement we need first, though.\""
    call setTheIngre
    a sad closeeyes "\"But there are some critters down there, like mice.\""
    a normal "\"I hope it's okay that I stay up here and you go get those things for me! Oh and you could do some cleaning while you're at it!\""
    call TheChoiceInPart2(6)

    jump Part3Start
