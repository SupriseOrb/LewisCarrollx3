# Here we can initialize all of our resources.

# character definitions
define w = Character("Whitley")
define a = Character("Alice", image="alice",window_left_padding=150)
define r = Character("Mr. Rabbit", image="bunny",window_left_padding=150)

# The game starts here.

# Alice's Heart
default heart = 0

# Day 3 variables
default Alice_affinity = 10
default beatqueen = False
default time = 5
default watchbook = False
default watchdiary = False


# image definition
image side alice = Image(im.FactorScale("/alice/alice_happy_closemouth.png",0.8,0.8))
image side alice normal = Image(im.FactorScale("/alice/alice_happy_closemouth.png",0.8,0.8))
image side alice happy = Image(im.FactorScale("/alice/alice_happy_openmouth.png",0.8,0.8))
image side alice happy strange= Image(im.FactorScale("/alice/alice_happy_strange.png",0.8,0.8))
image side alice annoyed = Image(im.FactorScale("/alice/alice_annoyed.png",0.8,0.8))
image side alice asleep = Image(im.FactorScale("/alice/alice_asleep.png",0.8,0.8))
image side alice confused = Image(im.FactorScale("/alice/alice_confused.png",0.8,0.8))
image side alice sad = Image(im.FactorScale("/alice/alice_sad.png",0.8,0.8))
image side bunny = Image(im.FactorScale("/bunny/bunny.png",1.2,1.2))
image side bunny normal = Image(im.FactorScale("/bunny/bunny.png",1.2,1.2))
image side bunny angry = Image(im.FactorScale("/bunny/bunny_angry.png",1.2,1.2))
image side bunny confused = Image(im.FactorScale("/bunny/bunny_confused.png",1.2,1.2))
image side bunny depressed = Image(im.FactorScale("/bunny/bunny_depressed.png",1.2,1.2))
image side bunny happy = Image(im.FactorScale("/bunny/bunny_happy.png",1.2,1.2))
image side bunny sad = Image(im.FactorScale("/bunny/bunny_sad.png",1.2,1.2))
image side bunny satisfied = Image(im.FactorScale("/bunny/bunny_satisfied.png",1.2,1.2))
image side bunny winning = Image(im.FactorScale("/bunny/bunny_winning.png",1.2,1.2))
image side bunny ok = Image(im.FactorScale("/bunny/bunny_ok.png",1.2,1.2))

# BGM definition

$ renpy.music.set_volume(2, delay=0, channel='music')

# bg definitions
image black = "#000"

init python:

    import math

    class Shaker(object):

        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }

        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()

            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child

        def __call__(self, t, sizes):

            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor

            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)

        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)

    Shake = renpy.curry(_Shake)

label start:

    stop music

    jump day1

label ending:

    return
