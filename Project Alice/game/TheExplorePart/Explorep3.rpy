label setTheIngre:
    $ TheVeg = ["Eggplant", "Cucumber", "Cabbage", "Potato"]
    $ TheMeat = ["Pork", "Beef", "Lamb", "Chicken"]
    $ TheSauce = ["Hot Sauce", "BBQ", "Sweet Sour", "Wasabi"]
    $ SelectIngre = renpy. random. randint(0,3)
    $ AnswerIngre1 = SelectIngre
    $ SecltedIngre1 = TheVeg [SelectIngre]
    a happy "First is [SecltedIngre1]"
    $ SelectIngre = renpy. random. randint(0,3)
    $ AnswerIngre2 = SelectIngre
    $ SecltedIngre2 = TheMeat [SelectIngre]
    a smile "and next is [SecltedIngre2]"
    $ SelectIngre = renpy. random. randint(0,3)
    $ AnswerIngre3 = SelectIngre
    $ SecltedIngre3 = TheSauce [SelectIngre]
    a normal "the last is [SecltedIngre3]"
    return


label SelectVeg:
    $ Ingreloop = True
    $ VegRight = False
    while Ingreloop:
        menu:
            "Eggplant":
                if AnswerIngre1 == 0:
                    $ VegRight = True
                    jump CheckIngre1
            "Cucumber":
                if AnswerIngre1 == 1:
                    $ VegRight = True
                    jump CheckIngre1
            "Cabbage":
                if AnswerIngre1 == 2:
                    $ VegRight = True
                    jump CheckIngre1
            "Potato":
                if AnswerIngre1 == 3:
                    $ VegRight = True
                    jump CheckIngre1
        label CheckIngre1:
            "Are you really sure about it?"
            menu:
                "Yes":
                    jump SelectMeat
                "No":
                    jump SelectVeg

label SelectMeat:
    $ MeatRight = False
    while Ingreloop:
        menu:
            "Pork":
                if AnswerIngre2 == 0:
                    $ MeatRight = True
                    jump CheckIngre2
            "Beef":
                if AnswerIngre2 == 1:
                    $ MeatRight = True
                    jump CheckIngre2
            "Lamb":
                if AnswerIngre2 == 2:
                    $ MeatRight = True
                    jump CheckIngre2
            "Chicken":
                if AnswerIngre2 == 3:
                    $ MeatRight = True
                    jump CheckIngre2
        label CheckIngre2:
            "Are you really sure about it?"
            menu:
                "Yes":
                    jump SelectSauce
                "No":
                    jump SelectMeat

label SelectSauce:
    $ SauceRight = False
    while Ingreloop:
        menu:
            "Hot Sauce":
                if AnswerIngre3 == 0:
                    $ SauceRight = True
                    jump CheckIngre3
            "BBQ":
                if AnswerIngre3 == 1:
                    $ SauceRight = True
                    jump CheckIngre3
            "Sweet Sour":
                if AnswerIngre3 == 2:
                    $ SauceRight = True
                    jump CheckIngre3
            "Wasabi":
                if AnswerIngre3 == 3:
                    $ SauceRight = True
                    jump CheckIngre3
        label CheckIngre3:
            "Are you really sure about it?"
            menu:
                "Yes":
                    jump FinishedIngre
                "No":
                    jump SelectSauce


label FinishedIngre:
    if VegRight and MeatRight and SauceRight:
        $ finishedMission = True
    return
