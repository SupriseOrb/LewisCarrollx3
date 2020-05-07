define e = Character("Whiteley")

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
    # Call screen shakes using keywords "at" or "with".
    # Use None for first argument since it is the relative position of the screen shake if you are using it for backgrounds.
    # Otherwise use (x-position, y-position, x-anchor, y-anchor).
    # Position is calculated relative to the top left.

    # The second argument is the time span of the shaking.
    # The third argument is the intensity of the screen shake.

    # Note that while this is pulled straight from the Ren'Py documentation and was last edited five years ago, it still works.
    # The shaking continues even through dialogue.
    scene bg room at Shake(None, 5.0, dist=20)

    show eileen happy

    e "Change."

    # In order to have the screen shake again, you must call the scene again.
    scene bg room at Shake(None, 5.0, dist=20)

    # You can shake almost everything, even characters.
    # (0.5, 1.0, 0.5, 1.0) puts the character at the center.
    show eileen happy at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)

    e "Now get out of here."


    return
