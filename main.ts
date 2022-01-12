let random = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    for (let index = 0; index < 5; index++) {
        basic.showArrow(ArrowNames.North, 50)
        basic.showArrow(ArrowNames.NorthEast, 50)
        basic.showArrow(ArrowNames.East, 50)
        basic.showArrow(ArrowNames.SouthEast, 50)
        basic.showArrow(ArrowNames.South, 50)
        basic.showArrow(ArrowNames.SouthWest, 50)
        basic.showArrow(ArrowNames.West, 50)
        basic.showArrow(ArrowNames.NorthWest, 50)
    }
    for (let index2 = 0; index2 < 5; index2++) {
        basic.showArrow(ArrowNames.North, 90)
        basic.showArrow(ArrowNames.NorthEast, 90)
        basic.showArrow(ArrowNames.East, 90)
        basic.showArrow(ArrowNames.SouthEast, 90)
        basic.showArrow(ArrowNames.South, 90)
        basic.showArrow(ArrowNames.SouthWest, 90)
        basic.showArrow(ArrowNames.West, 90)
        basic.showArrow(ArrowNames.NorthWest, 90)
    }
    random = randint(1, 8)
    if (random == 1) {
        basic.showArrow(ArrowNames.North)
    } else if (random == 2) {
        basic.showArrow(ArrowNames.North)
        basic.showArrow(ArrowNames.NorthEast)
    } else if (random == 3) {
        basic.showArrow(ArrowNames.North)
        basic.showArrow(ArrowNames.NorthEast)
        basic.showArrow(ArrowNames.East)
    } else if (random == 4) {
        basic.showArrow(ArrowNames.North)
        basic.showArrow(ArrowNames.NorthEast)
        basic.showArrow(ArrowNames.East)
        basic.showArrow(ArrowNames.SouthEast)
    } else if (random == 5) {
        basic.showArrow(ArrowNames.North)
        basic.showArrow(ArrowNames.NorthEast)
        basic.showArrow(ArrowNames.East)
        basic.showArrow(ArrowNames.SouthEast)
        basic.showArrow(ArrowNames.South)
    } else if (random == 6) {
        basic.showArrow(ArrowNames.North)
        basic.showArrow(ArrowNames.NorthEast)
        basic.showArrow(ArrowNames.East)
        basic.showArrow(ArrowNames.SouthEast)
        basic.showArrow(ArrowNames.South)
        basic.showArrow(ArrowNames.SouthWest)
    } else if (random == 7) {
        basic.showArrow(ArrowNames.North)
        basic.showArrow(ArrowNames.NorthEast)
        basic.showArrow(ArrowNames.East)
        basic.showArrow(ArrowNames.SouthEast)
        basic.showArrow(ArrowNames.South)
        basic.showArrow(ArrowNames.SouthWest)
        basic.showArrow(ArrowNames.West)
    } else if (random == 8) {
        basic.showArrow(ArrowNames.North)
        basic.showArrow(ArrowNames.NorthEast)
        basic.showArrow(ArrowNames.East)
        basic.showArrow(ArrowNames.SouthEast)
        basic.showArrow(ArrowNames.South)
        basic.showArrow(ArrowNames.SouthWest)
        basic.showArrow(ArrowNames.West)
        basic.showArrow(ArrowNames.NorthWest)
    } else {
        
    }
    
})
basic.forever(function on_forever() {
    
})
basic.forever(function on_forever2() {
    
})
