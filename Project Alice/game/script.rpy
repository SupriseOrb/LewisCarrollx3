screen pac():
    imagemap:
        ground "Test pac.png"

        # shift + D, then choose "Image Location Picker" while playing to figure out pixel positions
        # choose the appropriate image that is being mapped, then click and drag to copy and past rectangles to use for the hotspots
        # note that when hotspots are overlayed, the topmost declared hotspot is the bottom most layer
        hotspot (1, 5, 799, 595) action Jump("exit")
        hotspot (106, 131, 100, 99) action Jump("red")
        hotspot (315, 247, 239, 175) action Jump("yellow")
        hotspot (648, 103, 62, 80) action Jump("blue")


label start:

    "Welcome to the point and click demo."

    "Click on rectangles to produce dialogue."

    jump screenCall

label red:
    hide screen pac

    "You clicked on the red rectangle."

    jump screenCall

label yellow:
    hide screen pac

    "You clicked on the yellow rectangle."

    jump screenCall

label blue:
    hide screen pac

    "You clicked on the blue rectangle."

    jump screenCall

label screenCall:

    call screen pac

label exit:

    "You clicked on something empty, so the game will exit."

    return
