random = 0

def on_button_pressed_a():
    global random
    for index in range(5):
        basic.show_arrow(ArrowNames.NORTH, 50)
        basic.show_arrow(ArrowNames.NORTH_EAST, 50)
        basic.show_arrow(ArrowNames.EAST, 50)
        basic.show_arrow(ArrowNames.SOUTH_EAST, 50)
        basic.show_arrow(ArrowNames.SOUTH, 50)
        basic.show_arrow(ArrowNames.SOUTH_WEST, 50)
        basic.show_arrow(ArrowNames.WEST, 50)
        basic.show_arrow(ArrowNames.NORTH_WEST, 50)
    for index2 in range(5):
        basic.show_arrow(ArrowNames.NORTH, 90)
        basic.show_arrow(ArrowNames.NORTH_EAST, 90)
        basic.show_arrow(ArrowNames.EAST, 90)
        basic.show_arrow(ArrowNames.SOUTH_EAST, 90)
        basic.show_arrow(ArrowNames.SOUTH, 90)
        basic.show_arrow(ArrowNames.SOUTH_WEST, 90)
        basic.show_arrow(ArrowNames.WEST, 90)
        basic.show_arrow(ArrowNames.NORTH_WEST, 90)
    random = randint(1, 8)
    if random == 1:
        basic.show_arrow(ArrowNames.NORTH)
    elif random == 2:
        basic.show_arrow(ArrowNames.NORTH)
        basic.show_arrow(ArrowNames.NORTH_EAST)
    elif random == 3:
        basic.show_arrow(ArrowNames.NORTH)
        basic.show_arrow(ArrowNames.NORTH_EAST)
        basic.show_arrow(ArrowNames.EAST)
    elif random == 4:
        basic.show_arrow(ArrowNames.NORTH)
        basic.show_arrow(ArrowNames.NORTH_EAST)
        basic.show_arrow(ArrowNames.EAST)
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    elif random == 5:
        basic.show_arrow(ArrowNames.NORTH)
        basic.show_arrow(ArrowNames.NORTH_EAST)
        basic.show_arrow(ArrowNames.EAST)
        basic.show_arrow(ArrowNames.SOUTH_EAST)
        basic.show_arrow(ArrowNames.SOUTH)
    elif random == 6:
        basic.show_arrow(ArrowNames.NORTH)
        basic.show_arrow(ArrowNames.NORTH_EAST)
        basic.show_arrow(ArrowNames.EAST)
        basic.show_arrow(ArrowNames.SOUTH_EAST)
        basic.show_arrow(ArrowNames.SOUTH)
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    elif random == 7:
        basic.show_arrow(ArrowNames.NORTH)
        basic.show_arrow(ArrowNames.NORTH_EAST)
        basic.show_arrow(ArrowNames.EAST)
        basic.show_arrow(ArrowNames.SOUTH_EAST)
        basic.show_arrow(ArrowNames.SOUTH)
        basic.show_arrow(ArrowNames.SOUTH_WEST)
        basic.show_arrow(ArrowNames.WEST)
    elif random == 8:
        basic.show_arrow(ArrowNames.NORTH)
        basic.show_arrow(ArrowNames.NORTH_EAST)
        basic.show_arrow(ArrowNames.EAST)
        basic.show_arrow(ArrowNames.SOUTH_EAST)
        basic.show_arrow(ArrowNames.SOUTH)
        basic.show_arrow(ArrowNames.SOUTH_WEST)
        basic.show_arrow(ArrowNames.WEST)
        basic.show_arrow(ArrowNames.NORTH_WEST)
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
