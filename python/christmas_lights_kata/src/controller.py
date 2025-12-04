from __future__ import annotations

from pathlib import Path
from typing import List

from .commands import get_command
from .instruction_parser import InstructionParser
from .lights import LightGrid
from .position import LightPosition
from .action import LightAction


def apply_commands(grid: LightGrid, commands: List[str]) -> None:
    """
    Apply a list of command lines to the grid.
    """
    for line in commands:
        action, start, end = InstructionParser.parse(line)
        command = get_command(action)
        command.apply(grid, start, end)


def load_instructions(path: Path) -> List[str]:
    """
    Load and filter valid instruction lines from a file.
    """
    return [
        ln
        for ln in path.read_text().splitlines()
        if ln.strip() and not ln.lstrip().startswith("#") and InstructionParser._COMMAND_RE.match(ln.strip())
    ]


def main() -> None:
    """
    Main entry point for running the Christmas Lights Kata.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Run the Christmas Lights Kata")
    parser.add_argument(
        "instructions",
        type=Path,
        help="Path to the instructions.md file (or any file with one command per line)",
    )
    args = parser.parse_args()

    grid = LightGrid()
    commands = load_instructions(args.instructions)
    apply_commands(grid, commands)
    print(f"Lights lit: {grid.count_lit()}")


if __name__ == "__main__":
    main()
