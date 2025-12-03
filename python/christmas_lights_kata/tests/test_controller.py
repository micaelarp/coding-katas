import sys
import pytest
from python.christmas_lights_kata.src import controller


def test_parse_command_success():
    line = "turn on 10,20 through 30,40"
    action, start, end = controller.parse_command(line)
    assert action == "on"
    assert start == (10, 20)
    assert end == (30, 40)


def test_parse_command_invalid_raises():
    with pytest.raises(ValueError):
        controller.parse_command("invalid command line")


def test_main_runs_and_reports_lit_lights(tmp_path, capsys):
    instr = "turn on 0,0 through 0,0\nturn on 1,1 through 1,1"
    instr_path = tmp_path / "instr.md"
    instr_path.write_text(instr)

    original_argv = sys.argv
    sys.argv = ["controller", str(instr_path)]
    try:
        controller.main()
    finally:
        sys.argv = original_argv

    captured = capsys.readouterr()
    assert "Lights lit: 2" in captured.out
