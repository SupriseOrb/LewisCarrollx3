label TheChoiceInPart2(numberp2):
    if numberp2==1:
        menu:
            "Try to touch the girl":
                "Your hand penetrated her body"
                return
            "Try another cool way to say hi":
                W "What's up, player!"
                "Still no responce"
                return
            "Keep silence":
                "You You squat down and listen to the sound like that child"
                return
    if numberp2==2:
        menu:
            "Rush out":
                W "That's enough, you two basterds"
                "With the opening of the wardrobe door, the intense light from outside came in."
                "At that moment, you seemed to see Alice with tears in her face curled up in the closet, and the surprised faces of the two men outside the closet. "
                "But in the next second, your eyes are all white."
                $ HelpAlice = True
                return
            "Try to comfort Alice":
                "Your hand penetrated her body"
                "The sound outside suddenly became unusually loud"
                "Slowly, you lose consciousness."
                return
            "Do nothing":
                "You try to lean back to make you more comfortable to sit."
                "But unexpectedly, nothing is touching your back."
                "You start falling and lose consciousness."
                $ AliceUnhappy += 1
                return
    if numberp2==3:
        menu:
            "Yes, I'm sorry for your experience":
                A "I'm happy to hear you say that, my dear"
                return
            "No, what are you talking about":
                A "Why would you lie to me, my dear"
                $ AliceUnhappy += 1
                call checkTheFeeling
                return

    if numberp2==4:
        menu:
            "So what happened after that":
                A "They left"
                return
            "I think the words of Luke was true":
                A "Do you know that you are speaking the harshest words in the world?"
                $ AliceUnhappy += 1
                call checkTheFeeling
                return
    if numberp2==5:
        menu:
            "This is not like your style, tell me the truth":
                if HelpAlice:
                    "Alice stares at you, then she smiles suddenly"
                    A "Well, you really know me"
                    "Alice's eyebrows frowned, and it looked like she wanted to say something."
                    "But she said nothing, just raised her head slowly and sighed slowly."
                    "Finally her gaze returned to you, and then slowly said"
                    A "I burned it"
                    "Alice looked out at the ruin of the charred house outside the window."
                    A "The Mr.V I mentioned before, it not a thing"
                    A "It is another me, who owned the incredible weird power"
                    A "Just like my parents"
                    "Alice's eyes return to you"
                    A "I cursed Luke"
                    A "And their house burned in that night in accident"
                    A "I'm not sure who survived the fire, but what I know is that they won’t appear in my life anymore."
                    "Alice suddenly smiled"
                    A "Are you a little regretful to pursue this matter to the end?"
                    A "Actually, I prefer the edition that they all leave here safely."
                    A "which sounds like a fairy tale"
                    return
                else:
                    A "I'm sorry for the fact that you don't believe me"
                    $ AliceUnhappy += 1
                    call checkTheFeeling
                    return
            "I am happy that they managed to escape this place":
                A "I also feel sorry for you to stay in this place dear"
                $ AliceUnhappy += 1
                call checkTheFeeling
                return

    if numberp2==5:
        menu:
            "Do it yourself":
                A "I also wish I could, honey, but I have to prepare dinner for us."
                $ AliceUnhappy += 1
                call checkTheFeeling
                return
            "Okay, I will do that":
                A "Oh, thank you my dear, you are so kind"
                return
