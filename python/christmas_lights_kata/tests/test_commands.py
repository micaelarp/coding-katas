from python.christmas_lights_kata.src.commands import TurnOnCommand, TurnOffCommand, ToggleCommand
from python.christmas_lights_kata.src.lights import LightGrid
from python.christmas_lights_kata.src.position import LightPosition
import pytest


def test_turn_on_command():
    """Should turn on all lights in the region."""
    grid = LightGrid(width=3, height=3)
    cmd = TurnOnCommand()
    cmd.apply(grid, LightPosition(0, 0), LightPosition(2, 2))
    for y in range(3):
        for x in range(3):
            assert grid.is_lit(LightPosition(x, y))


def test_turn_off_command():
    """Should turn off only the specified region."""
    grid = LightGrid(width=3, height=3)
    grid.turn_on_region(LightPosition(0, 0), LightPosition(2, 2))
    cmd = TurnOffCommand()
    cmd.apply(grid, LightPosition(1, 1), LightPosition(2, 2))
    for y in range(1, 3):
        for x in range(1, 3):
            assert not grid.is_lit(LightPosition(x, y))


def test_toggle_command():
    """Should toggle all lights in the region."""
    grid = LightGrid(width=3, height=3)
    grid.turn_on_region(LightPosition(0, 0), LightPosition(2, 2))
    cmd = ToggleCommand()
    cmd.apply(grid, LightPosition(0, 0), LightPosition(2, 2))
    for y in range(3):
        for x in range(3):
            assert not grid.is_lit(LightPosition(x, y))


def test_single_point_region():
    """Should work for a region of a single point."""
    grid = LightGrid(width=3, height=3)
    cmd = TurnOnCommand()
    cmd.apply(grid, LightPosition(1, 1), LightPosition(1, 1))
    assert grid.is_lit(LightPosition(1, 1))
    # All other lights remain off
    for y in range(3):
        for x in range(3):
            if (x, y) != (1, 1):
                assert not grid.is_lit(LightPosition(x, y))


def test_inverted_region():
    """Should work for regions where start > end."""
    grid = LightGrid(width=3, height=3)
    cmd = TurnOnCommand()
    cmd.apply(grid, LightPosition(2, 2), LightPosition(0, 0))
    for y in range(3):
        for x in range(3):
            assert grid.is_lit(LightPosition(x, y))


def test_out_of_bounds_region():
    """Should raise ValueError for out-of-bounds coordinates."""
    grid = LightGrid(width=3, height=3)
    cmd = TurnOnCommand()
    with pytest.raises(ValueError):
        cmd.apply(grid, LightPosition(-1, 0), LightPosition(2, 2))
    with pytest.raises(ValueError):
        cmd.apply(grid, LightPosition(0, 0), LightPosition(3, 3))
