from pathlib import Path

from python.christmas_lights_kata.src.controller import apply_commands, load_instructions
from python.christmas_lights_kata.src.lights import LightGrid
from python.christmas_lights_kata.src.position import LightPosition


def test_turn_on_region_affects_correct_cells():
    grid = LightGrid()
    apply_commands(grid, ["turn on 0,0 through 2,2"])
    assert grid.count_lit() == 9
    for y in range(0, 3):
        for x in range(0, 3):
            assert grid.is_lit(x, y) is True
    for y in [3, grid.height - 1]:
        for x in [3, grid.width - 1]:
            assert grid.is_lit(x, y) is False


def test_turn_off_region_turns_off_only_specified_area():
    grid = LightGrid()
    apply_commands(grid, ["turn on 0,0 through 4,4"])
    apply_commands(grid, ["turn off 1,1 through 2,2"])
    assert grid.count_lit() == 21
    for y in range(1, 3):
        for x in range(1, 3):
            assert grid.is_lit(x, y) is False


def test_toggle_region_flips_state():
    grid = LightGrid()
    apply_commands(grid, ["turn on 0,0 through 1,1"])
    apply_commands(grid, ["toggle 0,0 through 2,2"])
    assert grid.count_lit() == 5
    assert grid.is_lit(0, 0) is False
    assert grid.is_lit(2, 2) is True
