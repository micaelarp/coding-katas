from __future__ import annotations

from pathlib import Path
from typing import List

from .commands import get_command
from .instruction_parser import InstructionParser
from .lights import LightGrid


def apply_commands(grid: LightGrid, commands: List[str]) -> None:
    for line in commands:
        action, start, end = InstructionParser.parse(line)
        command = get_command(action)
        command.apply(grid, start, end)


def load_instructions(path: Path) -> List[str]:
    return [
        ln
        for ln in path.read_text().splitlines()
        if ln.strip() and not ln.lstrip().startswith("#") and InstructionParser._COMMAND_RE.match(ln.strip())
    ]


def main() -> None:
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
