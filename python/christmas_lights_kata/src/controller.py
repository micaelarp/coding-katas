from __future__ import annotations

import re
from pathlib import Path
from typing import List, Tuple

from .lights import LightGrid

# Regular expression to parse commands like:
#   turn on 887,9 through 959,629
#   toggle 0,0 through 2,2
_COMMAND_RE = re.compile(r"^(turn\s+(on|off)|toggle)\s+(\d+),(\d+)\s+through\s+(\d+),(\d+)$", re.IGNORECASE)


def parse_command(line: str) -> Tuple[str, Tuple[int, int], Tuple[int, int]]:
    """Parse a single command line.

    Returns a tuple ``(action, start, end)`` where ``action`` is one of
    ``"on"``, ``"off"`` or ``"toggle"`` and ``start``/``end`` are ``(x, y)``
    coordinate pairs.
    """
    line = line.strip()
    if not line:
        raise ValueError("Empty command line")
    m = _COMMAND_RE.match(line)
    if not m:
        raise ValueError(f"Invalid command format: {line!r}")
    if m.group(2):
        action = m.group(2).lower()
    else:
        action = "toggle"
    x1, y1 = int(m.group(3)), int(m.group(4))
    x2, y2 = int(m.group(5)), int(m.group(6))
    return action, (x1, y1), (x2, y2)


def apply_commands(grid: LightGrid, commands: List[str]) -> None:
    for line in commands:
        action, start, end = parse_command(line)
        if action == "on":
            grid.turn_on_region(start, end)
        elif action == "off":
            grid.turn_off_region(start, end)
        elif action == "toggle":
            grid.toggle_region(start, end)
        else:
            raise RuntimeError(f"Unsupported action: {action}")


def load_instructions(path: Path) -> List[str]:
    return [
        ln
        for ln in path.read_text().splitlines()
        if ln.strip() and not ln.lstrip().startswith("#") and _COMMAND_RE.match(ln.strip())
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
