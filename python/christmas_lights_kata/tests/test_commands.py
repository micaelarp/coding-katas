from python.christmas_lights_kata.src.commands import TurnOnCommand, TurnOffCommand, ToggleCommand
from python.christmas_lights_kata.src.lights import LightGrid

def test_turn_on_command():
    grid = LightGrid(width=3, height=3)
    cmd = TurnOnCommand()
    cmd.apply(grid, (0, 0), (2, 2))
    for y in range(3):
        for x in range(3):
            assert grid.is_lit(x, y)

def test_turn_off_command():
    grid = LightGrid(width=3, height=3)
    grid.turn_on_region((0, 0), (2, 2))
    cmd = TurnOffCommand()
    cmd.apply(grid, (1, 1), (2, 2))
    for y in range(1, 3):
        for x in range(1, 3):
            assert not grid.is_lit(x, y)

def test_toggle_command():
    grid = LightGrid(width=3, height=3)
    grid.turn_on_region((0, 0), (2, 2))
    cmd = ToggleCommand()
    cmd.apply(grid, (0, 0), (2, 2))
    for y in range(3):
        for x in range(3):
            assert not grid.is_lit(x, y)

