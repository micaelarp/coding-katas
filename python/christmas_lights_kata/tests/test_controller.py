import sys
import pytest
from python.christmas_lights_kata.src import controller


def test_main_runs_and_reports_lit_lights(tmp_path, capsys):
    """Should report correct number of lit lights for valid instructions."""
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


def test_main_with_invalid_instruction(tmp_path):
    """Should print error and exit for invalid instructions (robust subprocess test)."""
    import subprocess
    import os
    instr = "invalid command"
    instr_path = tmp_path / "instr.md"
    instr_path.write_text(instr)
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    result = subprocess.run([
        sys.executable,
        "-m",
        "python.christmas_lights_kata.src.controller",
        str(instr_path)
    ], capture_output=True, text=True, env=env)
    assert "Error:" in result.stdout
    assert result.returncode == 1
