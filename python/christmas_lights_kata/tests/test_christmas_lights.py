from python.christmas_lights_kata.src.lights import ChristmasLights

def test_christmas_lights_turn_on():
    grid = ChristmasLights(width=3, height=3)
    grid.turn_on((0, 0), (2, 2))
    assert grid.count_lit() == 9

def test_christmas_lights_turn_off():
    grid = ChristmasLights(width=3, height=3)
    grid.turn_on((0, 0), (2, 2))
    grid.turn_off((1, 1), (2, 2))
    assert grid.count_lit() == 5

def test_christmas_lights_toggle():
    grid = ChristmasLights(width=3, height=3)
    grid.toggle((0, 0), (2, 2))
    assert grid.count_lit() == 9
    grid.toggle((0, 0), (2, 2))
    assert grid.count_lit() == 0

