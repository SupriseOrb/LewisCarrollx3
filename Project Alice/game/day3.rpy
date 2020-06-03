label day3:
    scene bg whitley_bedroom with Dissolve(2)
    
    play music "audio/day3 music/morning.wav" fadein 1

    $ day += 1

    show screen Day with Dissolve(2)
    pause(3)
    hide screen Day with Dissolve(2)
    
    "{i}This will be the third day since I've been in Alice's house. And something is definitely wrong with this place, there was no way I could deny that.{/i}"
    
    "{i}I had heard of magic before, but this...this was something on an entirely new level.{/i}"
    
    "{i}Maybe those rumors were right? Maybe her parents DID dabble in the dark arts. But what for? Did it have a part in their deaths?{/i}"
    
    "{i}And Alice... She seemed...different.{/i}"
    
    "{i}There's more to this place than meets the eye, and as a detective, I know there is more to discover.{/i}"

    "{i}But for now, I just wanted to enjoy this short moment of peace.{/i}"

    "{i}It was 8:00 am, and I sat on my bed, yawning and looking through the window.{/i}"

    "{i}Warm sunlight shone through the round, bedside windows and onto the bed's white, soft, and comfortable quilt. However, the bedroom's grey walls reminded me of the interrogation rooms back at my workplace.{/i}"
    
    "{i}Right, I still had work to do. But even so..."
    
    w "\"What a special day~. People back in my town can seldom enjoy such bright and clear sunshine during the winter.\""

    w "\"Such nice weather...maybe Alice could open up a bit more today? I'll wake her up and invite her outside to enjoy this lovely day. Maybe we can have breakfast in the sunlight.\""

    w "\"Perhaps I can make her rabbit stew, Lapin a La Cocotte? She mentioned to me once that it was her favorite...\""

    "{i}I couldn't help but smile at the prospect of it. A nice, calming breakfast in the morning sun. A welcome resp--{/i}"
    
    play sound "audio/soundeffects/Alice_scream.wav"
    stop music
    "{i}A sudden, high pitched voice ripped through the air!{/i}"
    play sound "/audio/soundeffects/whitley_run.wav" fadein 1
    "{i}Quickly recovering from the initial shock, I swiftly grabbed a coat and ran up to the second floor, to Alice's room.{/i}"

    stop sound fadeout 1.5
    play sound "/audio/soundeffects/open_bedroom_door.wav" fadein 1 
    show black with Dissolve(1)
    scene bg alice_bedroom with Dissolve(1)
    hide black with Dissolve(1)
    "{i}There stood Alice looking wildly around the room in a state of panic.{/i}"
    w "\"Alice! What happened? Are you hurt?\""
    a sad "\"Mr. Rabbit is gone, and I can't find him!\""
    w "\"Mr. Rabbit? Your fluffy bunny? I can help you find it later, but don't cry for now, okay?\""
    a unhappy "\"No, you don't understand, and you never will. Mr. Rabbit is the last gift that my parents gave me. You don't know how important he is!\""
    "{i}She was absolutely hysterical, she almost hyperventilating.{/i}"
    "{i}I approached her slowly, arms lowered in front of me.{/i}"
    w "\"Okay, okay, calm down. It's going to be fine, everything will be alright.\""
    a sad "\"What if he's lost! Or-or hurt!\""
    w "\"Shh, shh... crying won't help with anything.\""
    w "\"Let's just sit down and think this through.\""
    "{i}At first, Alice just stood there, catching her breath between sobs, but eventually, she dropped herself back on her bed. I sighed in relief.{/i}"
    w "\"You know... when I was a kid, I had a little cat toy that I cherished just as much as you cherish Mr. Rabbit.\""
    "{i}I seated myself next to her and gently touched her head.{/i}"
    w "\"We'd play together all the time. I do understand how much it must hurt you to lose something so important.\""
    "{i}Alice sniffed and nodded.{/i}"
    a sad closeeyes "\"I can't lose him...\""
    w "\"Do you remember the last place you played with him?\""
    "{i}Alice shook her head fervently.{/i}"
    a unhappy "\"I don't know, and I don't remember!\""
    "{i}She was clearly not in a good mood to talk about it.{/i}"
    w "\"Okay, fine, fine. We don't have to think about it.\""
    "{i}I directed her to the window, hoping to cheer her up.{/i}"
    w "\"Look outside, what a beautiful day! Do you want to join me for a little breakfast in the sunlight?\""
    a sorrow "\"But I want to have breakfast with my Mr. Rabbit.\""
    "{i}She had calmed down a bit, but there was still the threat of tears in her eyes.{i}"
    w "\"Maybe Mr. Rabbit is waiting for you in the dining room. Why don't you get ready, and we'll take a look.\""
    "{i}Alice seemed to reluctantly take my suggestion and dragged her feet to the bathroom.{/i}"
    "{i}While she washed her face and brushed her teeth, I searched Alice's room until..."
    transform imgcenter:
        xalign 0.5 yalign 0.5
    show bunny at imgcenter
    with Dissolve(0.5)
    "{i}I found Mr. Rabbit! He was stuffed inside a rare, huge tea pot in Alice's toy set. I carefully took him out then put the fluffy toy on a chair in the dining room.{/i}"
    hide bunny with Dissolve(0.5)

    show black with Dissolve(1)
    scene bg dining_room with Dissolve(1)
    hide black with Dissolve(1)

    "{i}As I placed the last dish on the table, Alice walked in.{/i}"
    "{i}Her smile once she spotted her bunny was absolutely priceless.{/i}"
    a happy "\"Oh, you were right! Mr. Rabbit is waiting for me! Good morning, Mr.Rabbit!"
    play sound "audio/soundeffects/Fast_Footsteps.wav" fadein 1.0
    "{i}She ran to Mr. Rabbit and scooped him up into her arms.{/i}"
    stop sound fadeout 1.0
    w "\"Actually, I found him in a huge tea pot in your room. Maybe he wants to have a cup of tea!\""
    a happy strange "Maybe you're right! Mr. Rabbit wants to have a cup of tea."
    "{i}Alice repeated my words in a weird tone, with a smile that gave me a strange sense of aversion.{/i}"
    "{i}I couldn't describe it...but something about it made me want to run away.{/i}"
    "{i}I blinked and suddenly Alice seemed perfectly normal, with a genuine, beaming expression.{/i}"
    a normal "\"Do you want to join the tea party with me and Mr. Rabbit?\""

    menu:
        "The wonderful weather makes it hard to refuse":
            jump d3_choice1_A
        "Hesitate, not interested in it":
            jump d3_choice1_B

label d3_choice1_B:
    a confused "\"Why can't you play with with me? I never have a chance to go outside and have a tea party. Don't you like the sunshine?\""
    "{i}I just couldn't refuse Alice's request. I decided to play with her{/i}"
    w "\"Fine, let's go outside.\""
    a happy "\"Yay! I'll bring out my tea set!\""
    play sound "audio/soundeffects/Fast_Footsteps.wav" fadein 1.0
    pause(1.5)
    stop sound fadeout 2.0
    pause(2.0)

label d3_choice1_A:
    show black with Dissolve(1)
    scene bg day3_tea party with Dissolve(1)
    hide black with Dissolve(1)
    play music "audio/day3 music/tea party.wav" fadein 1
    "{i}Alice took out her vessels of beautifully decorated tea set pieces adorned with a pattern of flowers and rabbits.{/i}"
    "{i}As she set the table, she described our roles in the game.{/i}"
    a normal "\"I'm your godmother, Countess Le Cœur! We have been invited to a royal tea party to meet the queen. But our mission is to assassinate the queen to save your parents!"
    a happy strange "\"But remember, we're hiding our {i}real{/i} selves! So you have to behave gracefully and normally.\""
    "{i}I couldn't help but chuckle at that. With my training, I should hope I know how to be undercover.{/i}"
    "{i}The game sounded childish, but interesting. I'll follow her anyway since she is just a child. Maybe I could learn more about her this way?{/i}"
    w "\"You got it, godmother.\""
    "{i}Alice settled into her \"Countess\" character.{/i}"
    a normal "\"Dear Whitley, what would you like to have? We have sea salt caramel puffs, Pomelo raspberry macaron, Pistachio mousse, and my favorite Lychee Rose Raspberry Tart.\""
    w "\"I thought your favorite food was Lapin a La Cocotte?\""
    a "\"Not Countess Le Cœur's!\""
    w "\"Ah, right, right. Then I'll have...\""
    menu:
        "A. Sea salt caramel":
            jump d3_not_tart
        "B. Pomelo raspberry macaron":
            jump d3_not_tart
        "C. Pistachio mousse":
            jump d3_not_tart
        "D. Lychee rose raspberry tart":
            jump d3_tart
label d3_not_tart:
    a confused "\"Are you sure? Why not take your godmother's choice? Oh, dear, godmother's choice is the best. And it's for your own good!\""
    a "\"Mr. Rabbit, I know Whitley will have the same taste as me, right? You know that, for sure.\""
    a annoyed "\"Here's what I'll do! My dear, I'm so generous to give you another chance. What would you like to have? Pomelo raspberry macaron or Lychee Rose Raspberry Tart?\""
    menu:
        "A. Pomelo raspberry macaron":
            jump d3_macaron
        "B. Lychee rose raspberry tart":
            jump d3_tartt
label d3_macaron:
    "{i}I knew I was spoiling her fun, but I wanted to see her reaction. I'm still a detective after all.{/i}"
    "{i}This time, Alice looked annoyed with me indeed.{/i}"
    a angry "\"Oh, Whitley, why are you so stubborn? Can't you see that I'm asking you to take the Lychee Rose Raspberry Tart? I'm really disappointed. You're not listening to me, you're not caring about me!\""
    $Alice_affinity = Alice_affinity- 1
    jump question_alice
label d3_tartt:
    "{i}I gave in and chose the one she wanted. She gave me a pleased grin.{/i}"
    a "\"I'm glad that you pick the right one. Now we both have the same flavor for our dessert!\""
    $Alice_affinity =Alice_affinity+ 1
    jump question_alice

label d3_tart:
    a happy "\"Excellent! You know, you should always have the same choice as your godmother because I'm always doing this for your own good.\""
    "{i}She beamed at me, enthusiastically, and I couldn't help but smile back. Making her happy felt good.{/i}"
    $Alice_affinity =Alice_affinity+ 1

label question_alice:
    "{i}I was a bit curious about what Alice is thinking. The way she was acting surprised me. I wondered if Alice really is just role-playing, or if she believes this is the right thing.{/i}"
    w "\"Alice, isn't that a little too extreme to control your child's thoughts as a godmother?\""
    a asleep "\"What are you talking about? I'm not harming you, and isn't Lychee Rose Raspberry Tart tasty? {i}My{/i} mother's choice were always the best!\""
    a sad closeeyes "\"My mother...my mother...\""
    "{i}Alice started to break character. She set her tea cup down as her eyes brimmed with tears.{/i}"
    a sad "\"I wish she was here.\""
    "{i}I instantly felt guilty.{/i}"
    w "No, no, my Alice, I didn't mean to question you, and you're right. Oh, don't cry honey. Let's keep playing."
    "{i}Alice suddenly snapped her head up, excited about the game again. Her tears were gone and her smile was back.{/i}"
    a happy "\"Yeah! Let's keep playing. I'm your godmother!\""
    a "\"Would you like some tea? I remember that my parents sometimes will drink the British tea on such a wonderful day. They told me British tea has a special smell. Here are your choices: Camellia Oleifera, Green tea, or Earl Grey?"
    menu:
        "A. Camellia Oleifera":
            jump d3_not_tea
        "B. Green tea":
            jump d3_not_tea
        "C. Earl Grey":
            jump d3_tea
label d3_not_tea:
    a happy strange "\"What a pity, Whitley. Don't you know that Earl Grey is a British tea? It's a black tea base flavored with oil from the rind of bergamot orange, a citrus fruit with the appearance and flavor somewhere between an orange and a lemon with a little grapefruit and lime thrown in.\""
    a "\"I still remember the way it tasted when my parents made that tea for me for the first time...\""
    $Alice_affinity = Alice_affinity- 1
    jump d3_kill_queen

label d3_tea:
    a happy "\"Earl Grey is definitely the best choice. It's a black tea base flavored with oil from the rind of bergamot orange, a citrus fruit with the appearance and flavor somewhere between an orange and a lemon with a little grapefruit and lime thrown in.\""
    a "\"I still remember the way it tasted when my parents made that tea for me for the first time...\""
    $Alice_affinity =Alice_affinity+ 1

label d3_kill_queen:
    "{i}Alice gracefully lifted the tea cup with her back straight. Her nose slowly neared the tea cup as she pretended to smell the fragrance from the tea. Then, she passed the tea cup to me. I unconsciously started to smell the tea cup as well.{/i}"
    a normal "\"Mr.Rabbit tells me that the queen is coming in this way. There is a good chance that we can finally save your parents!\""
    a "\"Don't you miss your parents? Don't you want to be together with them again?\""
    "{i}Alice lowered her head. I got the feeling she wasn't talking to her make-believe goddaughter anymore.{/i}"
    a unhappy "Maybe...you'll never have to know what it feels like to lose the comfort and protection from parents."
    stop music
    play music "audio/day3 music/queen.wav" fadeout 1
    a normal "\"Listen! The queen is comming! Mr.Rabbit says that the ugly queen has locked your parents in the attic. The only way you can save them is to kill her. Would you be willing to help me do that?\""
    menu:
        "A. Kill the queen":
            jump d3_kill
        "B. Do not Kill the queen, and suggest another way":
            jump d3_not_kill

label d3_kill:
    $Alice_affinity = Alice_affinity+ 1
    $beatqueen = True
    a "\"I appreciate your courage. It's time to prepare for the mission. We need an excuse to meet the queen in person. I'd like to lend you my favorite book: Alice's Adventure in Wonderland. You can use that to kill the queen by claiming that it's a gift you have for her.\""
    "{i}With that, Alice and I successfully saved the parents from the wicked queen. Before we knew it, it was almost lunch time.{/i}"
    jump d3_lunch

label d3_not_kill:
    stop music fadeout 1
    $Alice_affinity = Alice_affinity- 1
    w "\"I know it's hard to live without parents aside. But I still have the hope to live because I'm staying with you, godmother! I can't just kill someone to save our parents. I couldn't live with myself! Why can't we try to negotiate with the queen?\""
    "{i}Alice lifted her hand to her chin and let out a dainty laugh.{/i}"
    a asleep "\"Ho, what a joke! Do you think the queen is that easy to talk with? She only knows the joy of locking someone in the attic then abandoning them!\""
    "{i}Alice's character was starting to break again.{/i}"
    a annoyed "\"She says that she wants them to accompany her and and that she won't leave them alone. But she always does in the end. She always goes back on her word.\""
    w "\"But maybe if we talk with her-?\""
    a annoyed "\"You can't!\""
    "{i}Alice jumped up in a rage. Now I'd done it.{/i}"
    a angry "\"You really ruin the game Whitley. I'm done with it!\""
    "{i}She huffed at me. She snatched Mr. Rabbit from his place before stomping away.{/i}"

label d3_lunch:
    stop music fadeout 1
    play music "audio/day3 music/lunch.wav" fadeout 1
    show black with Dissolve(1)
    scene bg kitchen with Dissolve(1)
    hide black with Dissolve(1)

    "{i}I made lunch for Alice. After eating the lunch, Alice wanted to have a break. Before she walked back to her room, though, she had something to tell me.{/i}"
    if Alice_affinity < 10 and beatqueen == False:
        $heart -= 5
        a annoyed "\"Today was the worst tea party ever in my life. I didn't have any fun at all so I don't have anymore to say to you, indeed!\""
        "{i}I scratched my head. What was that about? Nothing more to say to me? Was she hiding something?{/i}"
    if Alice_affinity < 10 and beatqueen == True:
        $heart += 1
        a normal "\"Although you didn't listen to me and make the same choice, you did help me beat the queen. I want to tell you that...Alice's Adventure in Wonderland really {i}is{/i} a good book.\""
    if Alice_affinity > 10 and beatqueen == False:
        $heart += 1
        a normal "\"Although you didn't help me kill the queen, I'm glad that you are willing to play with me. There's a book called \"Alice's Adventure in Wonderland\", and it's my favorite! You should read it if you have time.\""
    if Alice_affinity > 10 and beatqueen == True:
        $heart += 5
        a happy "\"I hope I can have another tea party with you again. You're really a good partner! For playing with me so well, I let you have a little secret! There's a letter in \"Alice's Adventure in Wonderland\" from my parents.\""

    "{i}Alice returned to her bedroom with Mr.Rabbit in her arms.{/i}"
    
    "{i}What an eccentric girl. I didn't like the oppressive atmosphere during the tea party, though Alice is just a child."
    "{i}But I can't think of her antics right now. I have some time for myself now.{/i}"
    stop music fadeout 2
    menu:
        "A. Have a break in the attic":
            jump d3_attic
        "B. Search the study room in the house":
            play sound "audio/soundeffects/whitley_walk.wav" fadein 1.0
            pause(1.0)
            jump d3_study_room
        "C. Check on Alice":
            jump d3_check_alice_1
label d3_attic:
    play sound "audio/soundeffects/whitley_walk.wav" fadein 1.0
    show black with Dissolve(1)
    play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0
    scene bg whitley_bedroom with Dissolve(1)
    hide black with Dissolve(1)
    $time -= 1
    "{i}I climbed up to the attic. It was cozy and looked like a comfortable spot to take a short rest.{/i}"
    "{i}The mansion was grand, but sometimes the sheer openness of its rooms almost felt exposing. I felt a little safer in here.{/i}"
    "{i}I set myself down and closed my eyes for a quick nap.{/i}"
    "{i}WOW, it's already 2pm. There isn't much time left to find the clues of Alice's parents. I need to hurry up before Alice wakes up too.{/i}"
    "{i}Where should I start?{/i}"
    menu:
        "A. Search the study room in the house":
            play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0
            pause(1.5)
            play sound "audio/soundeffects/whitley_walk.wav" fadein 1.0
            pause(1.0)
            jump d3_study_room
        "B. Check on Alice":
            jump d3_check_alice_2

label d3_check_alice_2:
    play sound "audio/soundeffects/whitley_walk.wav" fadein 1.0
    show black with Dissolve(1)
    $time -= 1
    play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0
    scene bg alice_bedroom with Dissolve(1)
    hide black with Dissolve(1)
    "{i}I gently pushed on Alice's door and slowly opened it, peeking inside to see if she was up.{/i}"
    a confused "\"Whiteley? Is that you?\""
    "{i}I threw one hand over my mouth and held my breath.{/i}"
    "{i}Alice groaned then rolled over and continued sleeping.{/i}"
    play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0
    "{i}I gingerly closed the door, and rushed off to the study room.{/i}"
    play sound "audio/soundeffects/whitley_run.wav" fadein 1.0
    "{i}Alice might wake up in a few minutes, but I still have time to find something for today.{/i}"
    jump d3_study_room
label d3_check_alice_1:
    play sound "audio/soundeffects/whitley_walk.wav" fadein 1.0
    show black with Dissolve(1)
    $time -= 1
    play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0
    scene bg alice_bedroom with Dissolve(1)
    hide black with Dissolve(1)
    "{i}I gently pushed on Alice's door and slowly opened it, peeking inside to see if she was up.{/i}"
    "{i}It looked like Alice was already asleep. I think I still have some time to search for clues in the study room.{/i}"
    play sound "audio/soundeffects/whitley_walk.wav" fadein 1.0

label d3_study_room:
    stop sound fadeout 1.0
    show black with Dissolve(1)
    play sound "audio/soundeffects/open_bedroom_door.wav" fadein 1.0
    play music "audio/BGM/Library.wav" fadein 5.0
    scene bg library with Dissolve(1)
    hide black with Dissolve(1)
    "{i}I don't know what I was expecting entering the study room, but as soon as I opened its doors, I was in absolute awe.{/i}" 
    "{i}The study room was like a private museum, where you could experience different cultures and histories, know the warm stories in a small family, and learn all kinds of knowledge in different fields.{/i}"
    "{i}I didn't know where to start, but, strangely, several books stacked on a nearby table caught my eye.{/i}"
label d3_library_choice:
    menu:
        "A. Alice's Adventure in Wonderland":
            jump d3_wonderland
        "B. War and Peace":
            jump d3_war
        "C. Little Prince":
            jump d3_prince
        "D. Alice's diary":
            jump d3_diary
label d3_wonderland:
    $watchbook = True
    show hollow book at truecenter with Dissolve(1)
    "{i}I opened the book but surprisingly, the pages inside the book were hollow! A small box sat inside the square hole. There was an alpabetical lock on the box.{/i}"
    python:
        name = renpy.input("It asks \"what is my favorite tea?\"(ALL UPPERCASELETTER)")
        name.upper()
        count = 0
        while name != "EARL GREY":
            count += 1
            name = name.strip()
            name = renpy.input("It asks \"what is my favorite tea?\"(ALL UPPERCASELETTER)")
            name.upper()
    play sound "audio/soundeffects/unlock.wav"
    "{i}The box unlocked!{/i}"
    hide hollow book at truecenter with Dissolve(1)
    play sound "audio/soundeffects/page_turn.wav"
    "{i}After opening the box, I found several pictures of various desserts. I picked up a note that read, \"My mother always baked desserts for me. I really miss the taste.\"{/i}"
    show lychee with Dissolve(1):
        xalign 0.5
        yalign 0.5

    "{i}On the back of the picture of Lychee rose raspberry tart, I found there were words written by Alice's parents.{/i}"
    hide lychee with Dissolve(1)
    define nvlp = Character("Alice's parents", kind = nvl)
    nvl show dissolve
    nvlp "Dear Alice,"
    nvlp "Maybe this will surprise you. The world of your beloved Wonderland is real. Mr. Rabbit is a gift from the White Queen. It gives us the power to protect you."
    nvlp "Now, we want to give it to you, so that we will always stay by your side. When you are in danger, use Mr. Rabbit to protect yourself."
    nvl clear
    nvlp "You can even wake Mr. Rabbit, should you ever require his companionship!"
    nvlp "However, you need a spell to wake him. The spell is ......"
    nvl clear
    nvl hide dissolve
    "{i}Strangely, the words for the spell are torn. It looked like someone ripped that portion off.{/i}"
    if watchdiary == False:
        jump d3_library_choice
    jump d3_end

    label d3_diary:
    play sound "audio/soundeffects/page_turn.wav"
    "{i}I picked up the journal with Alice's name embellished across the top. I flipped to a random page and started skimming.{/i}"
    $watchdiary = True
    define nvld = Character("Alice", kind = nvl)
    nvl show dissolve
    nvld "I don't know what I've done wrong. I just want to make friends with others! Why do Mom and Dad keep me here in the attic? I hate these grey walls."
    nvld "It don't like this place. I hear noises outside a lot. I'm scared and I want to get out of here."
    nvl clear
    nvld "Why are my parents crying? No, I don't like that. I want them to be happy. I should behave better in the future."
    nvl clear
    nvld "I don't want to break my parents' hearts. I don't even really know why making friends can make them so sad. It doesn't mean that I'm leaving them."
    nvld "Maybe it's not the right thing to make friends. Maybe my parents are all I should have. I will stay with my parents forever."
    nvl clear
    nvld "I can finally make new friends. Shouldn't I be happy? I don't have to worry about my parents' feelings.\n\n\nBut, but, I miss my mother's Lychee Rose Raspberry tart. I wish I could taste it one more time. Mr. Rabbit can't replace my parents."
    nvl clear
    nvl hide dissolve
    if watchbook == False:
        jump d3_library_choice
    jump d3_end

    label d3_war:
    play sound "audio/soundeffects/page_turn.wav"
    define nvlwar = Character("Introduction",kind = nvl)
    nvl show
    nvlwar "War and Peace broadly focuses on Napoleon's invasion of Russia in 1812 and follows three of the most well-known characters in literature: Pierre Bezukhov, the illegitimate son of a count who is"
    nvlwar "fighting for his inheritance and yearning for spiritual fulfillment; Prince Andrei Bolkonsky, who leaves his family behind to fight in the war against Napoleon; and Natasha Rostov, the beautiful young daughter of"
    nvlwar "a nobleman who intrigues both men.As Napoleon's army invades, Tolstoy brilliantly follows characters from diverse backgrounds—peasants and nobility, civilians and soldiers—as they struggle with the"
    nvlwar "problems unique to their era, their history, and their culture. And as the novel progresses, these characters transcend their specificity, becoming some of the most moving—and human—figures in"
    nvlwar "world literature."
    nvl clear
    nvl hide
    jump d3_library_choice

    label d3_prince:
    play sound "audio/soundeffects/page_turn.wav"
    define nvlprince = Character("Introduction",kind = nvl)
    nvl show
    nvlprince "The Little Prince, French Le Petit Prince, fable and modern classic by French aviator and writer Antoine de Saint-Exupéry that was published with his own illustrations in French as Le Petit Prince in 1943."
    nvlprince "The simple tale tells the story of a child, the little prince, who travels the universe gaining wisdom. The novella has been translated into hundreds of languages and has sold some 200 million copies "
    nvlprince "worldwide, making it one of the best-selling books in publishing history."
    nvl clear
    nvl hide
    jump d3_library_choice

    label d3_end:
        stop music fadeout 2.0
        play sound "audio/soundeffects/open_bedroom_door.wav"
        show black with Dissolve(1)
        pause(0.5)
        play sound "audio/soundeffects/chain_lock.wav"
        pause(1.0)
        play sound "audio/soundeffects/whitley_run.wav"
        scene bg living room with Dissolve(1)
        hide black with Dissolve(1)
        "{i}As I kept scouring the books, I heard Alice's voice. Hurriedly, I put everything back in place and locked the door to the study room behind me.{/i}"
        stop sound fadeout 1.0
        "{i}I glanced down at my pocket watch. It's already 5pm!{/i}"
        "{i}Alice's singsongy voice chimed through the hallways.{/i}"
        a "\"Whitley~ Whitley~Where are you? I can't find you.\""
        w "\"I'm here, honey. On the first floor.\""
        "{i}She appeared in the hall's entrance, hands on her hips.{/i}"
        a awkward "\"Where have you been?\""
        w "\"I...I just came back. I went outside to enjoy the sunshine.\""
        "{i}I hitched a thumb over my shoulder, towards the patio where the sun was starting to set.{/i}"
        a normal "\"Oh, really? Fine. I'm hungry now. Can you make dinner for me?\""

        show black with Dissolve(1)
        scene bg dining_room with Dissolve(1)
        hide black with Dissolve(1)
        "{i}After dinner, Alice retreated up to the second floor as usual. As I watched her go, I couldn't help but think of what I found in the study room.{/i}"
        "{i}I wanted to say something to her, but the way she used magic made her dangerous. Making senseless comments wasn't the way to go.{/i}"
        "{i}Still...this was bad. She's keeping things bottled up. I wonder if I'll ever be able to get through to her.{/i}"

        "{i}What a tough day.{/i}"

        stop music fadeout 3
        show black with Dissolve(3)
        pause(3)
        
        jump day4 



