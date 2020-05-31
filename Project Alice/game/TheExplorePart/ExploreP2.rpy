init python:

    import random
    class Room():
        def __init__(self):
            self.state=0

        def display(self):
            if self.state == 0:
                ui.imagebutton(idle="apoto.png")
            else:
                ui.imagebutton(idle="apoto2.png",action=[self.click,SetScreenVariable("a",1)])

        def click(self):
            self.state=0

        def random(self):
            self.state=0
            result=random.randint(0,4)
            if result==0:
                self.state=1


    class MyGame():
        def __init__(self):

            self.grid=[]
            for i in range(0,16):
                self.grid.append(Room())

        def display(self):
            ui.grid(4,4,align=(0.5,0.5),spacing=20)
            for room in self.grid:
                room.display()
            ui.close()

        def random(self):
            for room in self.grid:
                room.random()

    mygame=MyGame()

screen DoTheClean:
    default a=1
    default score=0
    python:
        mygame.display()
    textbutton "Leave":
        pos (0.1,0.1) action Return('test')
    timer 2.0:
        action [mygame.random,SetScreenVariable("a",1)]
        repeat True
