# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d3w = Character("Whiteley")
define d3a = Character("Alice")
define d3n = Character("Narrator")
define d3wi = Character("Whiteley inner monologue")
# The game starts here.
default Alice_affinity = 10
default beatqueen = False
default time = 5
default watchbook = False
default watchdiary = False

label start:
    scene bg room
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
label d3_morning:
    
    
    d3n "It’s the third day that you are in Alice’s house. Although you think you have known Alice__________(info from previous day), as a detective, you definitely know there are more to discover.(Reminding players of Goals)"
    
    scene bg attic

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    d3n "The warm sunlight shines on the Whitley’s white, soft, and comfortable quilt through the round windows in front of the bed. However, the walls that are painted in gray sometimes makes you think of interrogation rooms in your office for no reason. It’s 8:00 am, and you sit on your bed, yawning and looking through the window."

    d3wi "What a special day~ People in our town can seldom enjoy such bright and clear sunshines during the winter."

    d3w "I need to wake Alice up and invite her to go outside, enjoying this lovely day. Maybe we can have breakfast in the sunlight.(Whiteley can't help smiling)"
    
    #sound Alice's creaming (No!!!!!)
    d3n "You are shocked by such a high pitch voice. You swiftly grab a coat and run to the second floor, where Alice's room locate."
    
    scene bg Alice_room
    with Dissolve(.5)
    d3n "You sit next to Alice on her bed and touch her head."
    d3w "Calm down, Alice. Everyting will be alright."
    d3w "Alice, crying can’t help with anything. What happened Alice?"
    d3a "Mr.Rabbit is gone, and I can’t find him."
    d3w "Mr.Rabbit? A fluffy toy? I can help you find it later, but don’t cry for now, okay?"
    d3a "No, you don’t understand, and you never will. Mr. Rabbit is the last gift that my parents gave to me. You don’t know how important it is."
    d3w "I know, when I was a kid, I cherished my little cat toy as much as you do. Do you remember the last place you play with it?"
    d3n "Alice is not in a good mood to think about it."
    d3a "I don’t know, and I don’t remember!"
    d3w "Okay, fine, fine. We don’t think about the place. Look outside the window, what a beautiful day. Do you want to join me to have breakfast in the sunlights?"
    d3a "But I want to have breakfast with my Mr. Rabbit.(calm down a little bit, but still sad)"
    d3w "Maybe Mr. Rabbit is waiting for you in the dining room. Let’s take a look."
    d3n "As Alice is washing her face and brushing her teeth, you search Alice’s room and find Mr.Rabbit in a rare huge tea pot in Alice’s toy set. You put Mr.Rabbit on a chair in the dining room."
    
    scene bg dining_rabbit
    with Dissolve(.5)
    
    d3n "You put the last dish on the table, and Alice walks in."
    d3a "Oh, you’re right! Mr.Rabbit is waiting for me. Good morning, Mr.Rabbit!"
    d3n "Alice runs to Mr.Rabbit and hold him in her arm."
    d3w "Actually, I find him in a huge tea pot. Maybe he wants to have a cup of tea."
    d3a "Maybe you are right. Mr.Rabbit wants to have a cup of tea."
    d3n "Alice repeats your word in a weird tone with a smile that makes you want to get away from her."
    d3a "Do you want to join the tea party with me and Mr.Rabbit?"
    
    menu:
        #choice A
        "The wonderful weather makes it hard for you to refuse":
            jump d3_choice1_A
        "You hesitate to play with Alice because you are not interested in it":
            jump d3_choice1_B
            
label d3_choice1_A:
    scene bg Tea_Party
    with Dissolve(.5)
    d3n "Alice takes out her vessels of beautifully decorated tea set with the pattern of flowers and rabbit."
    d3a "I’m your godmother. We are invited to a royal tea party to meet the queen. But our mission is to assassinate the queen to save your parents. Remember to behave gracefully and normally."
    d3wi "It sounds childish but interesting.I’ll follow her anyway since she is just a child."
    d3w "Got it, godmother."
    d3a "Dear Whiteley, what would you like to have? We have sea salt caramel puffs, Pomelo raspberry macaron, Pistachio mousse, and my favorite Lychee Rose Raspberry Tart."
    menu:
        "A.Sea salt caramel":
            jump d3_not_tart
        "B.Pomelo raspberry macaron":
            jump d3_not_tart
        "C.Pistachio mousse":
            jump d3_not_tart
        "D.Lychee rose raspberry tart":
            jump d3_tart
label d3_not_tart:
    d3a "Are you sure? Why not take your godmother’s choice? Oh, dear, godmother’s choice is the best. I’m always doing this for your own good."
    d3a "Mr.Rabbit, I know Whitley will have the same taste as me right? You know that, for sure."
    d3a "I’m so generous to give you a chance. What would you like to have? Pomelo raspberry macaron or Lychee Rose Raspberry Tart?"
    menu:
        "A.Pomelo raspberry macaron":
            jump d3_macaron
        "B.Lychee rose raspberry tart":
            jump d3_tartt
label d3_macaron:
    d3a "Oh, Whitley, why are you so stubborn. Can’t you see that I’m asking you to take the \“Lychee Rose Raspberry Tart\”? I’m really disappointed. You’re not listening to me, and you’re caring about me."
    $Alice_affinity = Alice_affinity- 1
    jump question_alice
label d3_tartt:
    d3a "I’m glad that you pick the right one. Now we have the same flavor for our dessert."
    $Alice_affinity =Alice_affinity+ 1
    jump question_alice

label d3_tart:
    d3a "Excellent! You know, you should always have the same choice as your godmother because I’m always doing this for your own good.(Smile)"
    $Alice_affinity =Alice_affinity+ 1

label question_alice:
    d3n "You are kind of surprised about Alice’s thoughts. You want to see if Alice is just role-playing, or she believes this is the right thing."
    d3w "Alice, isn’t that too extreme to control your child’s thoughts as a godmother?"
    d3a "What are you talking about? I’m not harming you, and isn’t Lychee Rose Raspberry Tart tasty? My mother always gives me the best. I believe my mother’s choice is the best. My mother...my mother...I miss her.\n(Alice become sad and is about to cry)"
    d3w "No, no, my Alice, I’m not blaming you, and you’re right. Oh, don’t cry honey. Let’s keep playing."
    d3a "Yeah! Let’s keep playing. I like that! I’m your godmother\n (Alice suddenly backs to normal and become excited about the game)"
    d3a "Would you like some tea? I remember that my parents sometimes will drink the British tea on such a wonderful day, and they tell me that British tea has a special smell. Here is your choice: Camellia Oleifera, Green tea, and Earl Grey"
    menu:
        "A.Camellia Oleifera":
            jump d3_not_tea
        "B.Green tea":
            jump d3_not_tea
        "C.Earl Grey":
            jump d3_tea
label d3_not_tea:
    d3a "What a pity, Whitley. Don’t you know that Earl Grey is a British tea? It’s a black tea base flavored with oil from the rind of bergamot orange, a citrus fruit with the appearance and flavor somewhere between an orange and a lemon with a little grapefruit and lime thrown in."
    d3a "I can still remember the feeling when my parents made that tea for the first time."
    $Alice_affinity = Alice_affinity- 1
    jump d3_kill_queen
label d3_tea:
    d3a "Earl Grey is definitely the best choice. It’s a black tea base flavored with oil from the rind of bergamot orange, a citrus fruit with the appearance and flavor somewhere between an orange and a lemon with a little grapefruit and lime thrown in."
    d3a "I can still remember the feeling when my parents made that tea for the first time."
    $Alice_affinity =Alice_affinity+ 1
label d3_kill_queen:
    d3n "Alice gracefully lifts the tea cup with her back straight. Her nose slowly closes to the tea cup, and she pretends to smell the fragrance from the tea. Then, she passes the tea cup to you. You unconsciously start to smell the tea cup as well."
    d3a "Mr.Rabbit tells me that the queen is coming in this way. There is a good chance that we can finally save your parents. Don’t you miss your parents? Don’t you want to be together with them again?"
    d3n "Alice heads down, and says to herself."
    d3a "Maybe you would never know what it feels like to lose the comfort and protection from parents."
    d3a "Listen! Mr.Rabbit says that the ugly queen has locked your parents in the attic. The only way you can save them is to kill her. Would you be willing to help me do that?"
    menu:
        "A.Kill the queen":
            jump d3_kill
        "B.Do not Kill the queen, and suggest another way":
            jump d3_not_kill
            
label d3_kill:
    $Alice_affinity = Alice_affinity+ 1
    $beatqueen = True
    d3a "I appreciate your courage. It’s time to prepare for the mission. We need an excuse to meet the queen in person. I’d like to lend you my favorite book: Alice’s Adventure in Wonderland. You can use that to kill the queen by claiming that you have a gift for her."
    d3n "You and Alice successfully save the parents and it’s almost lunch time."
    jump d3_lunch
    
label d3_not_kill:
    $Alice_affinity = Alice_affinity- 1
    d3w "I know it’s hard to live without parents aside. But I still have the hope to live because I’m staying with you. I can’t just kill someone to save our parents. I can’t make it. Why can’t we try to negotiate with the queen?"
    d3a "Ah, what a joke. Do you think the queen is easy to talk with? She only knows the joy of locking someone in the attic and hypocritically says that she wants them to accompany her and don’t leave her alone. You really ruin the game Whitley. I’m done with it!"
    d3n "Alice walks away with the Mr. Rabbit."
label d3_lunch:
    scene bg kitchen
    d3n "You make the lunch for Alice. After eating the lunch, Alice wants to have a break. Before she walks back to her room, she has something to tell you."
    if Alice_affinity < 10 and beatqueen == False:
        d3a "Today, it’s the worst tea party ever in my life. There is no fun in the game. I don’t have anything to tell you indeed."
    if Alice_affinity < 10 and beatqueen == True:
        d3a "Although you don’t listen to me and make the same choice, you help me beat the queen. I want to tell you that I don’t accidentally mention Alice’s Adventure in Wonderland."
    if Alice_affinity > 10 and beatqueen == False:
        d3a "Although you didn’t help me kill the queen, I’m glad that you are willing to play with me. There is a book called “Alice's Adventure in Wonderland”, which is my favorite book. You should read it if you have time."
    if Alice_affinity > 10 and beatqueen == True:
        d3a "I hope I can play the tea party with you again. You’re really a good partner. There is a letter in Alice's Adventure in Wonderland from my parents."
        
    d3n "Alice walks to her bedroom with Mr.Rabbit in her arms."
    d3w "What an eccentric girl. I don’t like the oppressive atmosphere during the tea party, though Alice is just a child. Anyway, there are more important things to do."
    menu:
        "A.Have a break in the attic":
            jump d3_attic
        "B.Search the study room in the house":
            jump d3_study_room
        "C.Check out Alice":
            jump d3_check_alice_1
label d3_attic:
    scene bg attic
    $time -= 1
    d3w "WOW, it’s already 2pm. There isn’t much time left to find the clues of Alice’s parents. I need to hurry up before Alice wakes up."
    d3w "Where should I start?"
    menu:
        "A.Search the study room in the house":
            jump d3_study_room
        "B. Check out Alice":
            jump d3_check_alice_2
            
label d3_check_alice_2:
    $time -= 1
    d3n "Whitley gently opens Alice's door to see if Alice wakes up.It takes for a while for you to open the door."
    d3a "Whiteley? Is that you?\nAlice rolls over and continues sleeping."
    d3n "You close the door, and rushe to the study room."
    d3w "Alice may wake up in several minutes. I need to find something for today."
    jump d3_study_room
label d3_check_alice_1:
    $time -= 1
    d3n "You gently open Alice's door to see if Alice wakes up. It takes for a while for you to open the door."
    d3w "Alice is already asleep. I think I still get some time to search for clues in the study_room."
    
label d3_study_room:
    scene bg study_room
    with Dissolve(0.5)
    d3n "The study room is like a museum where you can experience different cultures and histories, know the warm stories in a small family, and also learn all kinds of knowledge in different fields."
    d3n "You don’t know where to start, but, strangely, there are several books stacked on the table:"
    menu:
        "A.Alice’s Adventure in Wonderland":
            jump d3_wonderland
        "B.War and Peace":
            jump d3_war
        "C.Le Comte de Monte-Cristo":
            jump d3_le
        "D.Little Prince":
            jump d3_prince
        "E.Alice's diary":
            jump d3_diary
label d3_wonderland:
    $watchbook = True
    scene hollow_book
    d3n "Surprisingly, the pages inside the book were hollow to put a small box inside. There is a alpabetical lock on the box."
    python:
        name = renpy.input("It asks \"what is my favorite tea?\"")
        name.upper()
        count = 0
        while name != "EARL GREY":
            count += 1
            name = name.strip()
            name = renpy.input("It asks \"what is my favorite tea?\"")
            name.upper()
            if count == 3:
                print("It’s a black tea base flavored with oil from the rind of bergamot orange, a citrus fruit with the appearance and flavor somewhere between an orange and a lemon with a little grapefruit and lime thrown in.")
        
    d3n "The box is unlocked."
    #scene box open
    d3n "After opening the box, there are several pictures of dessert. There is a note saying that “My mother always bakes desserts for me. I really miss its taste."
    show dessert:
        xalign 0
        yalign 0.5
    
    show dessert2:
        xalign 0.5
        yalign 0.5
    show dessert3:
        xalign 1
        yalign 0.5
    
    d3n "On the back of the picture of Lychee rose raspberry tart, there are words written by Alice's parents"
    
define nvlp = Character("Alice's parents", kind = nvl)
nvl show dissolve
nvlp "Dear Alice,"
nvlp "Maybe this will surprise you. The world of Wonderland is real. Mr.Rabbit is the gift from the White queen. It gives us the power to protect you. Now, we want to give it to you as if we are still staying with you. If you are in danger, use Mr.Rabbit to protect yourself."
nvl clear
nvlp "However, you need a spell to wake Mr.Rabbit up if you want to use it.The spell is ……"
nvl clear
nvl hide dissolve
d3n "Stangely, the words for the spell are torned, and it seems to be taken away by someone."
if watchdiary == False:
    jump d3_study_room
jump d3_end

label d3_diary:
    $watchdiary = True
define nvld = Character("Alice", kind = nvl)
nvl show dissolve
nvld "I don’t know what I have done wrong. I just want to make friends with others, and why my parents will keep me in captivity in the attic. The gray wall makes me scared and I want to get out of here."
nvl clear
nvld "Why are my parents crying? No, I don’t like that. I want them to be happy. I should behave better in the future."
nvl clear
nvld "I don’t want to break my parents’ hearts. I even don’t really know that making friends can make them so sad. I don’t mean that I will leave them. Actually, I really love them. Maybe it’s not the right thing to make friends. I will stay with my parents forever."
nvl clear
nvld "Now, I finally can make new friends. I don’t have to worry about my parents’ feelings.\n\n\n\nBut, but, I miss my mother’s Lychee Rose Raspberry tart. I wish they could come back. Mr. Rabbit can’t replace my parents."
nvl clear
nvl hide dissolve
if watchbook == False:
    jump d3_study_room
jump d3_end
        
label d3_war:
define nvlwar = Character("Introduction",kind = nvl)
nvl show
nvlwar "War and Peace broadly focuses on Napoleon’s invasion of Russia in 1812 and follows three of the most well-known characters in literature: Pierre Bezukhov, the illegitimate son of a count who is fighting for his inheritance and yearning for spiritual fulfillment; Prince Andrei Bolkonsky, who leaves his family behind to fight in the war against Napoleon; and Natasha Rostov, the beautiful young daughter of a nobleman who intrigues both men.\n\nAs Napoleon’s army invades, Tolstoy brilliantly follows characters from diverse backgrounds—peasants and nobility, civilians and soldiers—as they struggle with the problems unique to their era, their history, and their culture. And as the novel progresses, these characters transcend their specificity, becoming some of the most moving—and human—figures in world literature."
nvl clear
nvl hide
jump d3_study_room
    
label d3_le:
define nvlle = Character("Introduction",kind = nvl)
nvl show
nvle "The Count of Monte Cristo (French: Le Comte de Monte-Cristo) is an adventure novel by French author Alexandre Dumas (père) completed in 1844.\n\nOn the day of his wedding to Mercédès, Edmond Dantès, first mate of the Pharaon, is falsely accused of treason, arrested, and imprisoned without trial in the Château d'If, a grim island fortress off Marseille. A fellow prisoner, Abbé Faria, correctly deduces that his jealous rival Fernand Mondego, envious crewmate Danglars, and double-dealing magistrate De Villefort turned him in. Faria inspires his escape and guides him to a fortune in treasure. As the powerful and mysterious Count of Monte Cristo (Italy), he arrives from the Orient to enter the fashionable Parisian world of the 1830s and avenge himself on the men who conspired to destroy him."
nvl clear
nvl hide
jump d3_study_room
    
label d3_prince:
define nvlprince = Character("Introduction",kind = nvl)
nvl show
nvlprince "The Little Prince, French Le Petit Prince, fable and modern classic by French aviator and writer Antoine de Saint-Exupéry that was published with his own illustrations in French as Le Petit Prince in 1943. The simple tale tells the story of a child, the little prince, who travels the universe gaining wisdom. The novella has been translated into hundreds of languages and has sold some 200 million copies worldwide, making it one of the best-selling books in publishing history."
nvl clear
nvl hide
jump d3_study_room
    
label d3_end:
    scene bg living_room
    with Dissolve(0.5)
    d3n "As you keep reading the books, you hear Whitley’s voice.You hurry to return everything back to normal, and lock the door of the study room. You don’t notice that it’s already 5pm."
    
    d3a "Whiteley~Whiteley~Where are you? I can't find you."
    d3w "I'm here honey. On the first floor."
    d3a "Where have you been?"
    d3w "I...I just came back.I went outside to enjoy the sunshine."
    d3a "Oh, really? Fine. I'm hungry now. Can you make dinner for me?"
    
    scene black
    d3n "Alice walks to the second floor. You look at her thin back. Can't speak out anything."
    
    d3n "What a tough day."
    
return
    












label d3_choice1_B:
    d3a "NO"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # This ends the game.

    #return
