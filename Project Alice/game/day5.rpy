label day5:
    default ending_points = 0

    scene bg whitley_bedroom
    with fade
    with Dissolve(2)

    play music morning fadein 2.0

    $ day = 5

    show screen Day with Dissolve(2)
    $ renpy.pause(3, hard=True)
    hide screen Day with Dissolve(4)

    "After everything that happened yesterday, the truth was undeniable."
    "Magic killed those people that night. And magic killed Alice's parents."
    "How in the world was I going to put that in an official police report?"
    "And aside from that...how am I going to leave this mansion? I think I understand why that last nanny left. I'm surprised she didn't leave sooner."
    "Even though I know the truth now...I don't think this is the end of the matter."
    "Alice is certainly acting strange, she's obviously dangerous but...there's a different storm inside her."
    "I know there's more to this case than magic." 
    "Maybe today I can learn more about her. That rabbit of hers certainly seems special to her. Maybe there's something there?"
    "I'd better get ready then."

    scene bg dining room

    ##show alice_happy_closemouth

    w "\"So Alice, what do you want to do today?\""

    ##hide alice_happy_closemouth

    a happy "\"Let's play a game of tag!\""

    w "\"I don't know Alice, I was hoping we could take a break today.\""
    "A nice slow day would make it easier to talk to her..."

    a sad "\"You don't want to play with me?\""

    default tag_choice = False
    menu:

        "Ok, if you insist.":
            jump yes_tag

        "What if we don't play a game today?":
            jump no_tag

        "What if we went for a walk around wonderland instead?":
            jump neut_tag


    label yes_tag:
        $ tag_choice = True

        w "\"Ok, if you insist. Tag sounds like it could be fun...\""

        a happy "\"I'm so happy you think so. Let's go now, I can't wait! It's been so long since I've had a good game of tag.\""

        scene black
        with Dissolve(.5)

        jump done_tag_intro

    label no_tag:

        w "\"Yeah, these last few days have been a lot. What if we don't play a game today? Maybe just...\""

        a sad "\"NO, I WANT TO PLAY TAG!\""

        "I threw my hands up to calm her down. After what happened yesterday...I don't think I want Alice mad."

        w "\"I'm sorry, we can play. Please don't get upset with me. I don't want you to be upset.\""

        "Who knows what she's capable of when she's upset."

        a sad closeeyes "\"Okay, I'm sorry, I shouldn't have yelled. I just want to have fun with you. I really enjoy having you around. Please don't Leave me. I get so lonely.\""

        w "\"It's ok, I'm not going anywhere. Let's play your game after you finish eating.\""

        hide alice_sad
        show alice_happy_openmouth

        a happy "\"Yayyy! I can't wait.\""
        hide alice_happy_openmouth

        scene black
        with Dissolve(.5)

        jump done_tag_intro

    label neut_tag:

        w "\"What if we just took a walk around your Wonderland, maybe learn more about what your little rabbit there?\""

        #visual of rabbit moving

        a sad "\"No, I think I want to play tag. My parents used to play with me before...\""

        a happy "\"Well, anyways we should get going. I can't wait to play again.\""

        w "\"Okay...\""

        scene black
        with Dissolve(.5)

        "I'm sure she doesn't want to talk about the fire. But I would like to know more about her relationship with her parents."
        "They seem like they were all very close, but Alice also mentioned them hiding her away...I wonder if that has anything to do with how she's been acting."

        jump done_tag_intro

    label done_tag_intro:

        "Well, this should be interesting."

        jump wonderland_tag

    label wonderland_tag:

        scene wonderland
        ##show  alice_happy_closemouth

        "Again, we were in Wonderland. This time we weren't playing a crazy game of hopscotch, but I couldn't imagine the level of crazy would be any different."
        w "\"This place amazes me everytime.\""

        ##hide alice_happy_closemouth

        a happy "\"I know it's brilliant, isn't it. So are you ready to play?\""

        ##show alice_happy_closemouth

        w "\"Uhh...sure.\""

        ##hide alice_happy_closemouth
        a normal "\"The rules are easy: Whoever's it gets turned into a wolf, and whoevers not it, gets turned into a little rabbit.\""

        a happy "\"You have to catch the rabbit before you turn white. With each minute you don't find the rabbit, you will become more white.\""

        a happy closeopen "\"Luckily the wolf is much bigger than the rabbit and can smell really well. All you have to do is catch the rabbit in your mouth and tag there it.\""

        a normal "\"But if you turn full white, you'll stay a wolf and you won't be able to leave wonderland. Are you ready?\""

        ##show alice_happy_closemouth

        w "\"Wait, what do you mean stay a wolf and never leave wonderland?\""

        ##hide alice_happy_closemouth

        a smile "\"Oh, It's only a game silly, people just say that. I've never seen anyone stay it long enough to become a wolf. It'll be fun. You ready?\""

        default rabbit_first = False
        default is_rabbit = False
        default visit_house = False
        default visit_cat = False
        default wolf_side_won = False

        if tag_choice:
            a happy "\"So, do you want to be the wolf or the rabbit?\""

            ##show alice_happy_closemouth

            w "\"Ummm...\""

            menu:
                "Wolf":
                    jump wolf_choice

                "Rabbit":
                    jump rabbit_choice



        else:
            "\"You go to speak, but before the words can come out-\""

            ##hide alice_happy_closemouth

            a happy "\"Let's play. You'll be it first!\""

            ##show alice_happy_closemouth

            jump wolf

    label wolf_choice:
        w "\"I'll be the wolf first.\""

        jump wolf

    label rabbit_choice:
        w "\"I'll be the rabbit first.\""

        $ rabbit_first = True
        $ is_rabbit = True

        jump rabbit

label wolf:
    scene black
    "Alice tagged me and I felt my body start to shift, bones breaking, morphing. The pain was excruciating, the worst I've felt in my life!"
    "I went to scream, but my voice was muffled. I tried again, and this time, I heard a loud growl. I looked around and everything seemed taller than it was."
    "I tried to find Alice, but I turned to see only the trail of a rabbit hopping away."
    "The game has started."

    scene wonderland
    with Dissolve(.5)

    w "\"Alice?\""
    a happy closeopen "\"Catch me if you can!\""
    "Alice's voice fades off into the distance"
    jump game_instructions

label rabbit:
    scene black
    "Alice tagged me and I felt my body start to shift, bones breaking, morphing. The pain was excruciating, the worst I've felt in my life!"
    "I felt myself getting smaller, shrinking. I felt a strong urge to hop around and eat carrots. The urge grew stronger the smaller I got."
    "Finally, the pain eased and I looked up to see a ferocious wolf staring back at me. My instincts told me to run."

    scene wonderland
    with Dissolve(.5)

    show wolf
    a happy "\"Well, Ms. Whitley, how was that?\""

    "I was in a daze."

    w "\"Why did it hurt so much? Why are your teeth so big?\""

    a happy strange "\"The game's started, silly! You better start hopping away now, little rabbit.\""

    a happy "\"The big bad wolf is on the prowl!\""

    hide wolf

    jump game_instructions

label game_instructions:
    "As the rabbit, your goal is to run away from the wolf. As the wolf your goal is to catch the rabbit before you turn full wolf."
    "Choose paths to achieve your goal. As the wolf, you have 10 turns before you turn full wolf. So as the rabbit hop away for as long as you can and you just might survive."
    #implement a smell feature

    default turns_left = 10
    default path_open = False

    jump game_start

label game_start:
    if is_rabbit:
        "You have 1 turn before the wolf comes chasing you, better go fast."
        $ turns_left = 10
        $ turn_find = renpy.random.randint(4,7)

    $ rand_path = renpy.random.randint(1,7)

    if is_rabbit:
        $ rand_path = 8

    "Choose your path."

    menu:
        "Woods":
            jump woods
        "Forest Path":
            jump path
        "Creek":
            jump creek



label woods:
    scene woods
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if path_open:
        "Path is [rand_path]"
    "Turns left: [turns_left] \nI ventured deeper into the woods. Choose:"

    menu:
        "Go deeper into woods":
            jump woods1
        "Go toward the forest path":
            jump path

label woods1:
    scene woods
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if is_rabbit:
        "Turns left: [turns_left] \nAt this point, I was surrounded by trees. I could still make out a small path to my left, but I could also see a clearing coming up on my right. Choose:"

        menu:
            "Even deeper into woods":
                jump woods2
            "Toward forested path":
                jump path1

    "Turns left: [turns_left] \nAt this point, I was surrounded by trees. I could still make out a small path to my left, but I could also see a clearing coming up on my right. Choose:"

    menu:
        "Even deeper into woods":
            jump woods2
        "Toward forest path":
            jump path1
        "Head to clearing":
            jump cat

label woods2:
    scene woods
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if rand_path == 1:
        jump wolf_tag_ending

    if is_rabbit:
        "Turns left: [turns_left] \nThe woods seemed like they might end soon, but they continued on. I saw a clearing on my right, but something told me not to go there. I could still make out a small path to my left, but barely. Choose:"

        menu:
            "Towards end of woods":
                jump woods3
            "Toward forest path":
                jump path2
    else:
        "Turns left: [turns_left] \nThe woods seemed like they might end soon, but they continued on. I saw a clearing on my right. I could still make out a small path to my left, but barely. Choose:"

        menu:
            "Towards end of woods":
                jump woods3
            "Toward forest path":
                jump path2
            "Head to clearing":
                jump cat


label woods3:
    scene woods
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if rand_path == 7:
        jump wolf_tag_ending
    "Turns left: [turns_left] \nI reached the end of the woods where I noticed a warning sign posted above the path foward. The path to my left was out of sight, but a nearby sign suggested its presence. Choose:"

    menu:
        "Go back":
            jump woods2
        "Toward forest path":
            jump path2

label path:
    scene path
    with Dissolve(.5)

    $ turns_left -= 1

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    "Turns left: [turns_left] \nI walked onto a forest path. There was an area of thicker woods on my right, and a creek on my left. Choose:"

    menu:
        "Deeper down path":
            jump path1
        "Towards woods":
            jump woods
        "Head to creek":
            jump creek

label path1:
    scene path
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    "Turns left: [turns_left] \nI went down the path and was met by a crossroads. A path to a creek was on my left, and an area lined with trees to the right. Choose:"

    menu:
        "Continue down path":
            jump path2
        "Head towards creek":
            jump creek1
        "Head to forested area":
            jump woods1

label path2:
    scene path
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if rand_path == 2:
        jump wolf_tag_ending
    "Turns left: [turns_left] \nI was halfway down the path when I was met with another divide. I saw what seemed to be a house not too far to the left, and another covered path that led into the woods. Choose:"

    menu:
        "Continue straight":
            jump path3
        "Towards house":
            jump house
        "Go to woods":
            jump woods2

label path3:
    scene path
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if rand_path == 5:
        jump wolf_tag_ending
    "Turns left: [turns_left] \nI was almost at the end of the path. I saw a river to my left, but the area was covered in mist. Yet again, there was a path to the woods. Choose:"

    menu:
        "Go back":
            jump path2
        "Toward woods":
            jump woods3
        "Continue to end of path":
            jump path4
        "Go into mist":
            jump river2

label path4:
    scene path
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if rand_path == 6:
        jump wolf_tag_ending
    "Turns left: [turns_left] \nI was almost to the end of the path when something didn't feel right. Choose:"

    menu:
        "Go back":
            jump path3
        "GO BACK":
            jump path3
        "GO BACK!!!":
            jump path3

label creek:
    scene creek
    with Dissolve(.5)

    $ turns_left -= 1

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    "Turns left: [turns_left] \nI walked into a creek and noticed there was an open path on my right. Choose:"

    menu:
        "Continue further down creek":
            jump creek1
        "Go to path":
            jump path



label creek1:
    scene creek
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    "Turns left: [turns_left] \nI continued further into the creek and saw a house coming up. There was an open path on your right, but it was harder to make out. I also saw a river coming up on my left. Choose:"

    menu:
        "Head to the house":
            jump house
        "Go to path":
            jump path1
        "Go to river":
            jump river


label house:
    scene house
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if rand_path == 3:
        jump wolf_tag_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if visit_house:
        menu:
            "Go to path on right":
                jump path2
            "Go past house towards a river":
                jump river

    "Turns left: [turns_left] \nI arrived at a house. It was huge, but severely run down. Choose:"
    menu:
        "Explore house.":
            jump house2
        "Go to path on right":
            jump path2
        "Go past house towards a river":
            jump river

label house2:
    scene inside house
    with Dissolve(.5)

    "I approached the house. I walked up to the door, but found it was stuck. I noticed an open window nearby and hopped through. Inside, there was a broken table among other debris. Looked like it had been ransacked."
    "In the far corner I saw what looked to be a small piece of paper. I approached it. It had ancient text written all over it. Instantly you felt something come over me."
    "I'm not sure how...but I felt like the ancient text had somehow inscribed itself in my mind."

    $ visit_house = True
    jump house

label river:
    scene river
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    "Turns left: [turns_left] \nThe current looked weak. However, something prevented me from turning around."
    menu:
        "Continue foward":
            jump river2

label river2:
    scene river
    with Dissolve(.5)

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if rand_path == 4:
        jump wolf_tag_ending

    "Turns left: [turns_left] \nI arrived at the end of the river. I saw a path on my left and a trail leading back to a house. Choose:"
    menu:
        "Head back towards the house.":
            jump house
        "Go to path on right":
            jump path3

label cat:
    scene cat
    with Dissolve(.5)

    if visit_cat:
        menu:
            "Go further towards the ends of the woods":
                jump woods3

    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    "Turns left: [turns_left] \nI headed toward the clearing. Along the way I stopped. I noticed a cat sitting amongst the trees branches. Choose:"
    menu:
        "Talk to the mysterious cat":
            jump cat1
        "Go further towards the ends of the woods":
            jump woods3

label cat1:
    scene cat
    with Dissolve(.5)
    $ visit_cat = True

    c "\"Hello there, wolf.\""
    w "\"Did you see a bunny run by here?\""
    c "\"Hmm, perhaps. You should find Alice, and you better find her quick. Don't want to end up stuck here. We are all mad here.\""
    w "\"Mad?\""
    c "\"Alice is especially mad, all the time she's spent her. Well, with what happened to her parents, who wouldn't be?\""
    w "\"What do you know about that?\""
    c "\"Oh, no one knows the WHOLE truth except that it was horrible. No one except Alice and that rabbit of hers. That dreaded rabbit should've stayed in his home.\""
    w "\"What are talking about, what do you mean?\""
    c "\"Time's running out you know. Go find Alice and maybe her little friend Mr. Rabbit will lead you to the answers you are searching for.\""

    jump cat


label wolf_ending:
    "Time is up."
    "Alice popped up in front of me."
    show bunny_satisfied
    a annoyed openeyes "\"Wow, you aren't very good at this, are you? You do realize the point is to tag me, silly! Well luckily, Mr. Rabbit can stop the curse."
    w "\"Curse?! Tht was real?\""
    a happy closeopen "\"Yes, of course! I didn't want to scare you off, but the game is cursed indeed. It's more fun that way! But thanks to Mr. Rabbit here, all is well."
    "Alice grabbed Mr. Rabbit and touched the both of us."
    hide bunny_satisfied
    "Poof!"
    "We both returned to our human states."
    show alice_happy_openmouth
    a "\"What a shame, if you had tagged me you could've been the rabbit too! But I guess you'll have to wait 'til next time.\""
    hide alice_happy_openmouth

    jump tag_end

label wolf_tag_ending:
    $ ending_points += 1
    show bunny
    "I spotted a small white rabbit. Alice! I sprinted forward and grabbed it in my mouth."
    scene black
    hide bunny
    "Poof!"
    scene wonderland
    "I felt my body return to normal, much less painful this time."
    "I saw Alice standing in front of me."

    show alice_happy_openmouth

    a "\"Shoot! Now I'm it. You ready?\""

    ##show alice_happy_closemouth

    w "\"Gimmie a minute, I am still recovering from being a wolf.\""

    ####hide alice_happy_closemouth

    a smile "\"Well, now you're a rabbit!\""
    "Alice grabbed Mr. rabbit and touched me."
    scene black
    "Can I please get a break..."
    scene wonderland

    $ wolf_side_won = True

    $ is_rabbit = True
    jump game_start

label wolf_dist:
    if (turns_left - turn_find) == 1:
        "Run, Alice is almost there."
    if (turns_left - turn_find) == 2:
        "Hurry, Alice is near by."
    if (turns_left - turn_find) == 3:
        "Alice has found your trail."
    return

label rabbit_ending:
    "I felt fear creep over my shoulder. I hopped to the side slightly to spot the drool of a ferocious wolf pooling up beside me. Then I felt a drop plop on my head."
    scene black
    with Dissolve(.3)
    "I felt my body begin morphing back to normal, my limbs growing, stretching out."
    scene wonderland
    a happy closeopen "\"Yay! I caught ya!\""

    if rabbit_first:
        a happy "\"That was fun. I do like being the wolf, but now you get to be it!\""
        $ is_rabbit = False
        jump wolf

    if wolf_side_won:
        a normal "\"That was fun. Looks like we both won as the wolf. It's a lot more fun being the ferocious predator right?\""
        ##show alice_happy_closemouth
        w "\"Uh yeah sure. But I don't think I liked those deep cravings I felt. I might be a vegaterian now, to be honest.\""
        ##hide alice_happy_closemouth
        a happy closeeyes "\"Wolves are so cute, though. They just have to eat, that's all! I do love how big and strong I feel as a wolf.\""
        a happy "\"Mr. Rabbit makes me strong too, don't you?\""
        "She snuggled her plush happily. Something tells me there's more to Mr. Rabbit than meets the eyes..."
        a normal "\"Well? What did you think of the game?\""
        ##show alice_happy_closemouth
        w "\"Uh...it was fun? Exciting to say the least.\""
        ##hide alice_happy_closemouth
        jump tag_end

    ##show alice_happy_closemouth

    w "\"Darn, you're much better than me at this game.\""

    ##hide alice_happy_closemouth

    a happy "\"Well, I have played it more and this was your first time. I am sure you'll do better next time!\""
    ##show alice_happy_closemouth

    w "\"Yeah, next time.\""

    "I did not care for the prospect of that."
    
    jump tag_end

label write_texts:
    "I wrote down the texts. The symbols were foreign to me, but something about it felt...dark. Very dark. Suddenly, the words began to shift on the paper."
    "I watched in amazement and dread. Something bad is happening."
    "I jumped up to run and grab a lighter. I ignited the paper and tossed it away."
    "The way those words warped and the meaning behind them felt so demonic. Why was something so evil in Wonderland?"
    return

label tag_end:
    w "\"Well, that was something wasn't it.\""
    a happy closeopen "\"Yup! I'm tired.\""
    w "\"Then let's head back. How about I make you dinner?\""
    a smile "\"Okay! I've got a strange craving for meat, probably just a side effect of the game.\""
    w "\"Don't tell me there are side effects?!\""
    a happy closeopen "\"Home we go!\""
    scene black
    with Dissolve(.5)

    scene bg dinning room
    a happy "\"Wow, thanks so much for dinner. That steak was yummy.\""
    w "\"Well I'm glad you liked it. It's been a long day, we should get some rest.\""

    if visit house:
        menu:
            "Write down texts.":
                call write_texts

    scene bg whitley_bedroom
    with Dissolve(.5)

    if wolf_side_won:
        "\"Well, today was certainly interesting. All this magic and chaos is taking it's toll, but after succeeding in a wolf's body...I think I can manage.\""
    else:
        "\"Oh god, Alice is really scaring me. I need to find a way... out? But I can't leave her all alone. Right?\""

    jump day6





    # This ends the game.

    return
