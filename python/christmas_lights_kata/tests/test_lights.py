from pathlib import Path

from python.christmas_lights_kata.src.controller import apply_commands, load_instructions
from python.christmas_lights_kata.src.lights import LightGrid


def test_turn_on_region_affects_correct_cells():
    grid = LightGrid()
    apply_commands(grid, ["turn on 0,0 through 2,2"])
    assert grid.count_lit() == 9
    for y in range(grid.height):
        for x in range(grid.width):
            expected = 0 <= x <= 2 and 0 <= y <= 2
            assert grid.is_lit(x, y) is expected


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


def test_load_instructions_filters_non_commands(tmp_path):
    content = """# This is a comment\n\nturn on 0,0 through 1,1\ninvalid line\n# another comment\nturn off 0,0 through 0,0\n"""
    file_path = tmp_path / "instr.md"
    file_path.write_text(content)
    cmds = load_instructions(Path(file_path))
    # Only the two valid command lines should be returned
    assert cmds == ["turn on 0,0 through 1,1", "turn off 0,0 through 0,0"]


def test_full_instructions_match_expected_result():
    # Use the real instructions file shipped with the kata
    instr_path = Path(__file__).parents[1] / "instructions.md"
    commands = load_instructions(instr_path)
    grid = LightGrid()
    apply_commands(grid, commands)
    assert grid.count_lit() == 230022
