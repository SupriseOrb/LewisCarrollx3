label TheChoiceInPart3(numberp3):
    if numberp3 == 1:
        menu:
            "Do some cleaning work here":
                call screen DoTheClean
                w "\"I hope that makes Alice feel happy.\""
                $ ResponceAlice = True
                return
            "Go straight to get the ingredients you need":
               w "\"I don't want to waste my time with those rats.\""
               return

    if numberp3==2:
        menu:
            "Yes":
                $ AliceInPain += 1
                return
            "No":
                $ AliceInPain += 1
                return
            "I don't know":
                "Alice smiled."
                return

    if numberp3==3:
        menu:
            "Yes":
                $ AliceInPain += 1
                return
            "No":
                "Alice smiled"
                return
            "I don't know":
                $ AliceInPain += 1
                return

    if numberp3 ==4:
        menu:
            "Yes":
                "Alice smiled"
                return
            "No":
                $ AliceInPain += 1
                return
            "How about I ask you a question?":
                $ AliceInPain += 2
                "Alice gave me a sour look."
                a angry "\"That's not fair! I asked a question first.\""
                "It looks like Alice wasn't happy about that."
                call checkThePain
                return

    if numberp3 == 5:
        menu:
            "Break the silence and ask Alice something":
                w "\"Can I ask you some quesions, Alice?\""
                "Alice blinked at me, as if she was surprised I still had some left in me."
                "To be honest, I was surprised too. But even after everything, I needed to at least try to get something out of Alice."
                a normal "\"Sure, Ms. Whitley! As long as I know it!"
                "She recovered fast and plastered her signature smile back on."
                jump QuestionForAlice

            "Just finish the dinner and get this day over with":
                    $ FinishThisBoringDay= True
                    return


label QuestionForAlice:
    menu:
        "Ask about Aiden":
            w "\"Can you tell me more about Aiden?\""
            a nervous "\"Aiden?\""
            "Alice's eyes become full of doubt."
            a awkward "\"Who is Aiden?\""
            w "\"??!!\""
            with vpunch
            "Alice suddenly burst out laughing."
            a happy closeopen "\"Haha, got you!\""
            a "Sorry, but you should've seen you face! Haha!"
            "After a while, Alice finally stopped laughing."
            a normal "\"Aiden was our housekeeper\""
            a "\"He worked here long before I was born.\""
            a "\"He took his work very seriously and he only had one style of clothes!\""
            a happy closeeyes "\"He's so very old-fashioned!"
            "Alice put down the cutlery then propped up her chin with her hands."
            a guilty "\"Aiden worked hard but his memory wasn't good. He was always losing things.\""
            a normal "\"So he had a notebook to where he wrote things down so he could remember!\""
            jump AskAliceround2
        "Ask about Luke":
            w "\"Can you tell me more about Luke?\""
            "Alice didn't even bother looking up from her food."
            a guilty "\"No thank you, Ms. Whitley. I don't want to talk about that.\""
            $ AliceInPain +=1
            "Looks like discussing Luke is a minefield with her."

            call checkThePain
            jump AskAliceround2
        "Ask about Miffy":
            w "\"Can you tell me more about Miffy?\""
            "Alice paused with a sudden sadness."
            a sad closeeyes "\"Oh, my Miffy.... She was such a good rabbit.\""
            a guilty "\"She was a gift from my parents for my sixth birthday!\""
            a "\"She was an amazing pet, sometimes it was like she would react to what I said.\""
            a awkward "\"It was like she understood me...\""
            "Her sad smile faded away and she shifted her focus back to her food, viciously cutting into it."
            a unhappy "\"I hate Luke.\""
            jump AskAliceround2

label AskAliceround2:
    if AliceFeltPain:
        jump ToTheDay5
    "Maybe I could try asking one more question."
    menu:
        "Ask about the fire":
            w "\"Can you tell me more about the fire?\""
            $ AliceInPain +=1
            call checkThePain
            if HelpAlice:
                a confused "\"...\""
                a angry "\"I already told you, it was an accident.\""
                "Alice became a little moody, fidgeting in her chair."
                a sorrow closeeyes "\"I mean, I did, I did something bad, I know that.\""
                a sorrow openmouth "\"I cursed Luke, but I didn't curse his whole family.\""
                a "\"I only wanted to hurt him. I didn't actually want {i}everyone{/i} to get hurt like that.\""
                a "\"But it doesn't matter. It's not like it's my fault. Everyone said it was an accident.\""
                a sorrow closeeyes "\"It's not my fault he got what he deserved. That he... he...\""
                "That quaint, casual smile of hers was breaking. There was something more to her than wishing violence upon others in her. I'm sure of it."
                "Alice covered her face with her hand and sighed deeply."
                a awkward "\"Do you like making me deal with the stuff again? I don't want to talk about it anymore.\""
                jump AskAliceround3
            else:
                a awkward "\"Sorry, I don't want to talk about that.\""
                "Sounds like this topic is a minefield."
                jump AskAliceround3
        "Ask about Luke's family":
            w "\"Can you tell me more about the Adams family?"
            $ AliceInPain +=1
            if ResponceAlice:
                "Alice slowed down her chewing."
                "She was thinking about something."
                "Then she smiled, like always."
                a normal "\"They were just some rich people who knew us.\""
                a "\"But my parents don't know them at all.\""
                a annoyed openeyes "\"They appeared suddenly and uninvited. Very rude!\""
                a sorrow "\"But they knew about our secret.\""
                a "\"They knew about our magic power.\""
                "Alice used her slender finger to draw a circle in the air, circle become a bird"
                "Alice caressed the bird slowly before letting the bird fly away."
                a guilty "\"So, my parents had to be nice to them. I thought Luke was different...\""
                a angry "\"But, he wasn't.\""
                jump AskAliceround3
            else:
                "Alice continued to eat as if she didn't hear you"
                "Just when I was about to try again, she gave me a curt answer."
                a awkward "\"I don't know them well.\""
                jump AskAliceround3

label AskAliceround3:
    "Dinner is almost done."
    "I have time to ask one more question."
    if AliceAngry<2 and AliceUnhappy<2 and HelpAlice and AliceFeltPain<4:
        "Alice seems to be in a good mood."
        w "\"The last question-\""
        "Alice's eyes were back on me again."
        "She was patiently waiting the final question."
        w "\"What happened after that fire and where are your parents now?\""
        "Alice froze in that moment. I waited."
        "After a while, she finally move a little bit."
        "She put down the tableware."
        a smile "\"Do you still remember the questions I asked you before?\""
        a normal "\"About the connection between power and hurting people?\""
        "Alice traced her finger on the rim of her glass."
        a awkward "\"My parents got killed.\""
        w "\"But how? They have the magic power like you did. Couldn't they protect themselves?\""
        a unhappy "\"Not against themselves.\""
        w "\"I don't understand.\""
        a guilty "\"After the fire, I thought everything would go back to normal.\""
        a confused "\"But then some people came. I don't know why.\""
        a unhappy "\"They came with anger, with fire.\""
        a "\"They blamed my parents for what happened. They wanted to do the same thing to us.\""
        "Slowly, Alice's signature smile vanished. And she looked out into the distance, seemingly at a scene invisible to me."
        a angry "\"Aiden tried to protect us, he gave us time to get away. But it wasn't enough, not before they... they....\""
        "Alice couldn't finish. She sucked in a deep breath and skipped over the morbid part."
        a "\"They called him a \'servant of the Devil\'.\""
        a little angry "\"Why were we called the Devil?\""
        "Alice suddenly stood up and started to walk around the table to my side."
        "She stopped in front of me."
        a unhappy "\"Because they're jealous. That's what is, isn't it, Ms. Whitley?\""
        a "\"It's because they don't have this power.\""
        a unhappy closemouth "\"So they want it gone. Just because we were born with it.\""
        a guilty "\"My parents used all their power to protect me in the fire, but there wasn't any left to protect themselves.\""
        "Alice's eyes brimmed with tears."
        "\"She sat down slowly on a dining chair and buried her face between her arms.\""
        "\"Just like the little girl crying in the closet.\""
        $ AliceFeltPain = True
        return
    else:
        "I started to ask a question, but Alice's expression stopped me."
        "It looks like she's in a bad mood. Maybe next time."
        $ AliceFeltPain=True
        return
