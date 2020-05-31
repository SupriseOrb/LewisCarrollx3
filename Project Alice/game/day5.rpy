define c = Character("Cheshire Cat")


label day5:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alice_stock

    # These display lines of dialogue.

    "Well, Alice is certainly acting strange. Maybe today I can learn more about her or that rabbit of hers. Better get ready then."

    #visual indication of getting ready.
    #visual idinication of making breakfast.

    w "Alice what do you want to do today?"
    a "Let's play a game of tag."
    w "I don’t know Alice, I was hoping we could take a break today."
    a "You don’t want to play with me?"

    default tag_choice = False
    menu:

        "Ok, if you insist.":
            jump yes_tag

        "What if don't play a game today?":
            jump no_tag

        "What if we went for a walk around wonderland instead?":
            jump neut_tag


    label yes_tag:
        $ tag_choice = True

        w "Ok, if you insist. Tag sounds like it could be fun..."

        a "I'm so happy you think so. Let's go now, I can't wait! It's been so long since I've had a good game of tag."

        jump done_tag_intro

    label no_tag:

        w "Yeah, these last few days have been a lot. What if we don't play a game today? Maybe just..."

        a "NO, I WANT TO PLAY TAG!"

        #visual of angery alice, stood up
        #visual of whitney worried

        w "I'm sorry, we can play. Please don't get upset with me. I don't want you to be upset."

        "Who knows what she's capable of when she is upset"

        a "Ok, im sorry i shouldn't have yelled. I just want to have fun with you. I really enjoy having you around. Please don’t Leave me. I get so lonely."

        w "It's ok, I'm not going anywhere. Let's play your game after you finish eating."

        a "Yeaaaa, I can't wait."

        jump done_tag_intro

    label neut_tag:

        w "What if we just took a walk around wonderland, maybe learn more about what your little rabbit there?"

        #visual of rabbit moving

        a "No, i think I want to play tag. My parents used to play with me before… Well, anyways we should get going. I can’t wait to play again."

        w "Ok...?"

        "what does she mean 'before'?"

        jump done_tag_intro

    label done_tag_intro:

        "Well this should be interesting."

        #black screen

        jump wonderland_tag

    label wonderland_tag:
        #visual of characters in wonderland
        w "This place amazes me everytime."

        a "I know it's the coolest. So are you ready to play?"
        w "Uhh… sure."
        a "The rules are simple: Whoever’s it gets turned into a wolf, and whoevers not it, gets turned into a little rabbit."

        a "You have to catch the rabbit before you turn white. With each minute you don’t find the rabbit, you will become more white."

        a "Luckily the wolf is much bigger than the rabbit and can smell really well. Simply catch the rabbit in your mouth and tag there it."

        a "But if you turn full white, you’ll stay a wolf and not be able to leave wonderland. So you ready?"

        w "What do you mean stay a wolf and never leave wonderland?"

        a "Its just a game silly, people just say that. I’ve never seen anyone stay it long enough to become a wolf. It’ll be fun. You ready?"

        default rabbit_first = False
        default is_rabbit = False
        default visit_house = False
        default visit_cat = False
        default wolf_side_won = False

        if tag_choice:
            a "So, do you want to be the wolf or the rabbit?"

            w "Ummm..."

            menu:
                "Wolf":
                    jump wolf_choice

                "Rabbit":
                    jump rabbit_choice



        else:
            "You go to speak, but before the words can come out."

            a "Let’s play. You’ll be it first"

            jump wolf

    label wolf_choice:
        w "I'll be the wolf first."

        jump wolf

    label rabbit_choice:
        w "I'll be the rabbit first."

        $ rabbit_first = True
        $ is_rabbit = True

        jump rabbit

label wolf:
    "Alice tags you and you feel your body shifting, bones breaking, morphing. The pain is excruciating, the worst you’ve felt in your life."
    "You go to scream, but your voice is muffled. You try again and hear a loud growl. You look around, everything seems taller than it was. You try to find Alice, but turn to only see the trail of a rabbit hoping away."
    "The game has started."
    #wolf appears on screen for whitney, rabbit for alice
    jump game_instructions

label rabbit:
    "Alice tags you and you feel your body shifting, bones breaking, morphing. The pain is excruciating, the worst you’ve felt in your life."
    "You feel yourself getting smaller, shrinking. You feel a strong urge to hop around and eat carrots. The urge grows stronger the smaller you get."
    "Finally, the pain eases and you look up to see a ferocious wolf staring at you. Your intstincts tell you to run."

    a "Hello Whitney, how was that?"

    w "Why did it hurt so much? Why are your teeth so big?"

    a "The game's started. You better start hoping away now little rabbit."
    #wolf appears on screen for whitney, rabbit for alice

    jump game_instructions

label game_instructions:
    "As the rabbit your goal is to runnaway from the wolf. As the wolf your goal is to catch the rabbit before you turn full wolf. Choose paths to achieve your goal. As the wolf, you have 10 turns before you turn full wolf. So as the rabbit hop away for as long as you can and you just might survive."
    #implement a smell feature

    default turns_left = 10
    default path_open = True

    jump game_start

label game_start:
    if is_rabbit:
        "You have 1 turn before the wolf comes chasing you, better go fast."
        $ turns_left = 10
        $ turn_find = renpy.random.randint(4,10)

    $ rand_path = renpy.random.randint(1,7)

    if is_rabbit:
        $ rand_path = 8

    "Choose your path."

    menu:
        "Woods":
            jump woods
        "Forested Path":
            jump path
        "Creek":
            jump creek



label woods:
    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if path_open:
        "Path is [rand_path]"
    "Turns left: [turns_left] \nYou fallow deeper into the woods. Choose:"

    menu:
        "Deeper into woods":
            jump woods1
        "Toward forested path":
            jump path

label woods1:
    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit:
        "Turns left: [turns_left] \nAt this point your surrounded by trees. You can still make out a small path to yout left, but see a clearing coming up on your right. Choose:"

        menu:
            "Even deeper into woods":
                jump woods2
            "Toward forested path":
                jump path1

    "Turns left: [turns_left] \nAt this point your surrounded by trees. You can still make out a small path to yout left, but see a clearing coming up on your right. Choose:"

    menu:
        "Even deeper into woods":
            jump woods2
        "Toward forested path":
            jump path1
        "Head to clearing":
            jump cat

label woods2:
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
        "Turns left: [turns_left] \nThe woods almost seem to end, but continue on. You see a clearing on your right, but something tells you not to go there. You can still make out a small path to your left, but barely. Choose:"

        menu:
            "Towards end of woods":
                jump woods3
            "Toward forested path":
                jump path2
    else:
        "Turns left: [turns_left] \nThe woods almost seem to end, but continue on. You see a clearing on your right. You can still make out a small path to your left, but barely. Choose:"

        menu:
            "Towards end of woods":
                jump woods3
            "Toward forested path":
                jump path2
            "Head to clearing":
                jump cat


label woods3:
    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if rand_path == 7:
        jump wolf_tag_ending
    "Turns left: [turns_left] \nYou reach the end of the woods, a sign of danger is posted above the path foward. The path to your left is out of sight, but a sign says its there. Choose:"

    menu:
        "Go back":
            jump woods2
        "Toward forested path":
            jump path2

label path:
    $ turns_left -= 1

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    "Turns left: [turns_left] \nYou walk into a forest path. There is an area of thicker woods on your right, and a creek on your left. Choose:"

    menu:
        "Deeper down path":
            jump path1
        "Towards woods":
            jump woods
        "Head to creek":
            jump creek

label path1:
    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    "Turns left: [turns_left] \nYou go down the path and are met at a crossroads. A path to a creek is on your left, and a path covered in forest on your right. Choose:"

    menu:
        "Continue down path":
            jump path2
        "Head towards creek":
            jump creek1
        "Head to forested area":
            jump woods1

label path2:
    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if rand_path == 2:
        jump wolf_tag_ending
    "Turns left: [turns_left] \nYou are halfway down the path when you are met with another divide. You see what seems to be a house not too far left, and another covered path that leads into the woods. Choose:"

    menu:
        "Continue straight":
            jump path3
        "Towards house":
            jump house
        "Go to woods":
            jump woods2

label path3:
    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if rand_path == 5:
        jump wolf_tag_ending
    "Turns left: [turns_left] \nYour almost at the end of the path. You see a river to your left, but the area is covered in mist. Yet again there is a path to the woods. Choose:"

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
    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if rand_path == 6:
        jump wolf_tag_ending
    "Turns left: [turns_left] \nYou are almost at the end of the path, something doesn't feel right. Choose:"

    menu:
        "Go back":
            jump path3
        "GO BACK":
            jump path3
        "GO BACK!!!":
            jump path3

label creek:
    $ turns_left -= 1

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    "Turns left: [turns_left] \nYou walk into a creek, there is an open path on your right. Choose:"

    menu:
        "Continue further down creek":
            jump creek1
        "Go to path":
            jump path



label creek1:
    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    "Turns left: [turns_left] \nYou continue further into the creek and see a house coming up. There is an open path on your right, but harder to make out. You also see a river coming up on your left. Choose:"

    menu:
        "Head to the house":
            jump house
        "Go to path":
            jump path1
        "Go to river":
            jump river


label house:
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

    "Turns left: [turns_left] \nYou arrive at a house, it's big and worn down. Choose:"
    menu:
        "Explore house.":
            jump house2
        "Go to path on right":
            jump path2
        "Go past house towards a river":
            jump river

label house2:
    "You approach the house. You walk up and try to get through the door, but lack the facilites to open it. The window is open near the front door you hop in. Inside you see a broken table, the house looks ransacked."
    "In the far corner you see what looks to be a small piece of paper. You approach it. It has ancient text written all over it. Instantly you feel something come over you. The ancient text inscribes itself in your mind."

    $ visit_house = True
    jump house

label river:
    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    "Turns left: [turns_left] \nThe current is weak. However, something is preventing you from turning around."
    menu:
        "Continue foward":
            jump river2

label river2:
    $ turns_left -= 1

    if turns_left <= 0 and is_rabbit == False:
        jump wolf_ending

    if is_rabbit:
        call wolf_dist

    if is_rabbit and (turn_find == turns_left):
        jump rabbit_ending

    if rand_path == 4:
        jump wolf_tag_ending

    "Turns left: [turns_left] \nYou arrive at the end of the river. You see the a path on your left and a trail leading back to a house. Choose:"
    menu:
        "Head back towards the house.":
            jump house
        "Go to path on right":
            jump path3

label cat:
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

    "Turns left: [turns_left] \nYou head towards the clearing. Along the way you stop. You see a cat sitting amongst the trees. Choose:"
    menu:
        "Talk to the mysterious cat":
            jump cat1
        "Go further towards the ends of the woods":
            jump woods3

label cat1:
    $ visit_cat = True

    c "Hello there wolf."
    w "Did you see a bunny run by here?"
    c "Hmm, perhaps. You will find Alice, and you better find her quick. Don't want to end up stuck here. We are all mad here."
    w "Mad?"
    c "Alice is especially mad, all the time she's spent her. With what happened to her parents, who wouldn't be."
    w "What happened to them?"
    c "No one really knows, except that it was horrible. That rabbit of hers, that dreaded rabbit should've stayed in his home."
    w "What do you mean? What does any of this mean?"
    c "There's no time now. Go find Alice and maybe the rabbit will lead you to the answers you are searching for."

    jump cat


label wolf_ending:
    "Time is up."
    "Alice pops up in front of you."
    a "Wow, you really stink at tag don't ya. You do realize the point is to tag me. Well luckly, Mr. Rabbit can stop the curse."
    w "Curse?!"
    a "Yeah, I didn't want to scare you off, but the game is cursed. However, thanks to Mr. Rabbit here all is well."
    "Alice grabs Mr. Rabbit and touches the both of you."
    "Poof."
    "You both return into your human state."
    a "Well if you had tagged me you could've been the rabbit to, but I guess you will have to wait until next time."


    jump tag_end

label wolf_tag_ending:
    "You see a small white rabbit. You run up and grab it in your mouth."
    "Poof."
    "You feel your body return to normal, much less painful this time."
    "You see Alice in front of you."
    a "Dang, it now I'm it. You ready?"
    w "Gimmie a minute, I am still recovering from being a wolf."
    a "Well now you're a rabbit."
    "Alice grabs Mr. rabbit and touches you."

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
    "You feel a fear creep over your shoulder. You do a slight hop to the side to see the drool of a ferocious wolf pooling up beside you. You feel a drop on your head."
    "Darkness."
    "You feel your body morphing back to normal. Your limbs growing, stretching out."
    a "I caught ya."

    if rabbit_first:
        a "So you wanna be the wolf now. That was fun. I do like being the wolf though."
        $ is_rabbit = False
        jump wolf

    if wolf_side_won:
        a "Dang, we both won as the wolf. It is a lot more fun being the predator right?"
        w "Uh yeah sure. I don't like the deep cravings I feel. I think I'm going vegaterian now."
        a "Wolves are so cute. Murderous intent and all. I do love the power I feel as a wolf."
        a "Mr. Rabbit makes me so strong, don't ya think?"
        w "Uh yeah sure..."
        jump tag_end

    w "Dang it. You are much better than me at this game."
    a "Well, I have played it more and this was your first time. I am sure you will do better next time."
    w "Yeah, next time."
    jump tag_end


label tag_end:
    "end"
    jump day6




    # This ends the game.

    return
