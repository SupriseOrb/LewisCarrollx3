label TheChoiceInPart2(numberp2):
    if numberp2==1:
        menu:
            "Try to touch the girl":
                "I reached my hand out, but was shocked to find my hand went right through her!"
                "Was this some sort of dream?"
                return
            "Try to call out to her with cool kid talk":
                w "\"What's up, player!\""
                "Still no response."
                "I feel very uncool."
                return
            "Stay silent":
                "I squatted down next to her and listened with her."
                return
    if numberp2==2:
        menu:
            "Rush out":
                stop music
                "I couldn't take it anymore. I slammed open the wardrobe."
                play sound "audio/soundeffects/kick_wardrobe.wav"
                w "\"Now that's enough, you two!\""
                "Upon opening the wardrobe door, an intense light from outside came in."
                image meteor = im.Alpha("white.png",1)

                transform glimmer_grew(start, end):
                    alpha start
                    linear 1.0 alpha end

                show meteor at glimmer_grew(0, 0.4)
                "At that moment, I saw Alice with tears in her eyes, curled up in the closet, and the surprised faces of the two boys outside."
                show meteor at glimmer_grew(0.4, 1)
                "But in the next second, everything went white."
                $ HelpAlice = True
                return
            "Try to comfort Alice":
                "I reached out to try comforting her, but my hand went right through her!"
                "Before I could try something else, the voices from outside started to grow louder and louder."
                "Slowly, I lost consciousness."
                return
            "Do nothing":
                "I tried to lean back and shy away from the situation."
                "But unexpectedly, nothing was behind me!"
                "Again, I was falling and I lost consciousness."
                $ AliceUnhappy += 1
                return
    if numberp2==3:
        menu:
            "Yes. I'm so sorry, Alice.":
                "Alice gave me a strangely bright smile."
                a happy strange "\"It's okay. I'm just happy you were there with me.\""
                return
            "No, what are you talking about.":
                "Alice gave me an eerie grin. There was no lying to her."
                a happy strange "\"Why would you lie to me, Ms. Whitley? Didn't I already tell you? What I say in this house, goes.\""
                $ AliceUnhappy += 1
                call checkTheFeeling from _call_checkTheFeeling
                return

    if numberp2==4:
        menu:
            "So, what happened after that?":
                a happy strange "\"They left.\""
                return
            "I think you should think about what Luke was saying.":
                a angry "\"Think about his words!? The harshest words in the world? You really don't understand, do you, Ms. Whitley?\""
                $ AliceUnhappy += 1
                call checkTheFeeling from _call_checkTheFeeling_1
                return
    if numberp2==5:
        menu:
            "You're not telling the truth.":
                if HelpAlice:
                    w "\"Wait...that doesn't sound right. You were really angry about that, Alice.\""
                    w "\"That house is rubble now. What really happened?\""
                    "Alice stared at me, then suddenly split a cheshire cat grin."
                    a smile "You really know me, Ms. Whitley! And so smart too!"
                    "I waited for an answer, but she said nothing, only stared. She looked like she was calculating something."
                    "Then, she just raised her head slowly and let out a deep sigh."
                    "Finally, her gaze returned to you, and she matter-of-factly said-"
                    play sound_little "audio/soundeffects/fire_burning.wav" fadein 1.0
                    a happy strange "\"I burned it.\""
                    "Alice looked back out at the ruin of the charred house."
                    a unhappy "\"I cursed Luke with the magic I have. The magic Mom and Dad had too.\""
                    stop sound_little fadeout 3.0
                    a "\"And their house burned that night in accident.\""
                    w "\"Did...they...?\""
                    "She shrugged her shoulders."
                    a happy closeeyes "\"Oh, they got out. Just like in those fairy tales! Very exciting.\""
                    a smile "\"But one thing's for sure-\""
                    "Alice suddenly smiled at me."
                    a happy strange "\"They're out of my life for good!\""
                    "She cocked her head and looked me up and down with that eerie smile."
                    a normal "\"Are you starting to regret coming here?\""
                    "I just stared back at her. Here was this sweet, innocent-looking child. And I was absolutely terrified."
                    "She brushed off my lack of response."
                    return
                else:
                    a confused "\"I'm sorry you don't believe me.\""
                    $ AliceUnhappy += 1
                    call checkTheFeeling from _call_checkTheFeeling_2
                    return
            "I'm glad they left.":
                a angry "\"But {i}you{/i} won't! You don't want to leave, do you?\""
                $ AliceUnhappy += 1
                call checkTheFeeling from _call_checkTheFeeling_3
                return

    if numberp2==6:
        menu:
            "I'd rather you do it yourself":
                a angry "Oh, I wish I could too! But I have to get dinner all set!"
                $ AliceUnhappy += 1
                call checkTheFeeling from _call_checkTheFeeling_4
                return
            "Okay, I'll do it":
                a smile "Oh, thank you Ms. Whitley! You are so kind!"
                return
