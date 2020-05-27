label TheChoiceInPart3(numberp3):
    if numberp3 == 1:
        menu:
            "Do some cleaning work here":
                call screen DoTheClean
                W "I already do my best, Alice will feel happy about it."
                $ ResponceAlice = True
                return
            "Go straight to get the ingredients you need":
                W "I don't want to waste my time on those rats"
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
                "Alice smiled"
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
            "How do think about this question?":
                $ AliceInPain += 2
                A "I refuse to answer since I asked this question first"
                "It looks like Alice is not happy with your rhetorical question"
                call checkThePain
                return

    if numberp3 == 5:
        menu:
            "Break the silence and ask Alice something":
                W "Can I ask you some quesions? Alice"
                "Alice stares at you, it looks like she was surprised by your sudden problem"
                A "Sure, honey, as long as I known"
                "She recovers fast and put her signal smile on the face again."
                jump QuestionForAlice

            "Just finish the dinner and over this boring day":
                    $ FinishThisBoringDay= True
                    return


label QuestionForAlice:
    menu:
        "Ask about Aiden":
            W "Can you tell me more about Aiden?"
            A "Aiden?"
            "Alice's eyes are full of doubts"
            A "Who is Aiden?"
            W "??!!"
            with vpunch
            A "Haha, got you"
            "Alice suddenly burst out laughing"
            A "Sorry, honey, but your face was funny"
            "After a while, Alice stop her laughing"
            A "Aiden is our homekeeper"
            A "He worked here lond before I was born"
            A "He works very seriously and he only has one style of clothes."
            A "which is very old-fashioned"
            "Alice put down the cutlery in her hand and hold her chin with her hands"
            A "Aiden works hard but his memory was too bad."
            A "So he has one small notebook to record the thing he usually forget, like he usually lost his key."
            jump AskAliceround2
        "Ask about Luke":
            W "Can you tell me more about Luke?"
            A "Sorry, I don't want to talk about this."
            $ AliceFeltPain +=1
            "Luke is the minefield"
            call checkThePain
            jump AskAliceround2
        "Ask about Miffy":
            W "Can you tell me more about Miffy"
            "Alice seems very sad"
            A "Oh, my miffy, my sweetyy"
            A "She was the gift from my parents to my sixth birthday"
            A "She is amazing pet, which could react to my words"
            A "It was like she can understand me"
            A "I hate Luke"
            jump AskAliceround2

label AskAliceround2:
    if AliceFeltPain:
        jump ToTheDay5
    W "Maybe I could ask more question"
    menu:
        "Who is the Mr.V":
            W "So who is the Mr.V?"
            "Alice smiled at me"
            A "You still confused about it?"
            A "Well, actually it just one of my crazy idea"
            A "I can't say who is it, because it never exist"
            A "Or"
            "Alice picked up the tableware again"
            A "Mr. V is created by me, and Mr. V is myself."
            A "And I was tried to speak and comfort myself."
            jump AskAliceround3
        "Ask question about the fire":
            W "Can you tell me more about the fire?"
            $ AliceFeltPain +=1
            call checkThePain
            if HelpAlice:
                A "........"
                A "Okey, I already tould you that fire was an accident"
                "Alice's mood became a little emotional"
                A "I mean, I did, I did something bad, I knew"
                A "I curse Luke, but I didn't curse his family"
                A "I never... thought of hurting anyone"
                A "What I did was.... I..I want he will receive ten times more pain than I did"
                A "And... his body start burning in that night"
                A "And everything... everthing start burning"
                "Alice covered her face with her hand and sighed deeply"
                A "It seems you really like to hear the memory to make me feel pain."
                jump AskAliceround3
            else:
                A "Sorry, I don't want to talk about this topic"
                "This topic is the minefield"
                jump AskAliceround3
        "Ask about Luke's family":
            W "Can you tell me more about the family of Luke?"
            $ AliceFeltPain +=1
            if ResponceAlice:
                "You can see that Alice slow down her chewing speed"
                "She is thinking something"
                "And she smiles like always"
                A "They are some kind of relatives of my mother."
                A "But my mother don't even know them at all"
                A "They appear suddenly, my parents didn't want them to stay at here"
                A "But they got goods on my parents"
                A "which is this magic power"
                "Alice use her slender finger drawa a circle in the air and the circle become a bird"
                "Alice caress the bird slowly and she let the bird fly away"
                jump AskAliceround3
            else:
                "Alice continued to eat as if she didn’t hear you"
                "When you was about to ask questions again"
                A "I don't know them well"
                jump AskAliceround3

label AskAliceround3:
    "The dinner is almost finished"
    "You still one question need to ask"
    if AliceAngry<2 and AliceUnhappy<2 and HelpAlice and AliceFeltPain<4:
        "Alice is in a good mood"
        W "The last question"
        "Alice's eyes back to you again"
        "She is waiting the final question"
        W "Where happened after that fire and where is your parents now?"
        "You clearly see that the movement of Alice was freezing in that moment"
        "After a while, Alice finally move a little bit"
        "She put down the tableware"
        A "Do you still remeber the questions I asked you before?"
        A "the connection between power and the violence"
        "Alice is using her finger hit the table"
        A "My parents got killed"
        W "But how? They have the magic power like you did"
        A "Yes, they did. But their power destoyed them"
        W "I don't understand"
        A "After the fire burned Luke's family"
        A "I thought my life would back to track again"
        A "But some people came, I don't know why they came"
        A "They came with violence, with fire"
        A "They annoyceed that they would purify me and my family for this world"
        "The smiles on Alice's face become defference, become more horror"
        A "They caught Aiden, and hang him immidiately with no defend"
        A "They called Aiden is, the servant of devil"
        A "But Aiden just a housekeeper with bad memory"
        "Alice's tone was full of anger."
        A "They burned his body in front of house"
        A "And the fire started to burn our house"
        A "Why we were called the devil?"
        "Alice stand up and start to walk around in front of you"
        "Suddenly, she stopped in front of you"
        A "Because they don't have this power"
        A "So they want to destoy this power that we born with"
        A "My parents used all their power to protect me in the fire, but they burned to death"
        "You find tears spinning in Alice's eyes"
        "She sat down slowly and buried her face between her arms"
        "You seem to see the little girl crying in the closet"
        $ AliceFeltPain = True
        return
    else:
        "Maybe next time"
        "It looks like Alice is in a bad mood"
        $ AliceFeltPain=True
        return
