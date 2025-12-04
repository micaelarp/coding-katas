import re
from typing import Tuple

class InstructionParser:
    """
    Parses instruction lines for grid commands.
    """
    _COMMAND_RE = re.compile(r"^(turn\s+(on|off)|toggle)\s+(\d+),(\d+)\s+through\s+(\d+),(\d+)$", re.IGNORECASE)

    @staticmethod
    def parse(line: str) -> Tuple[str, Tuple[int, int], Tuple[int, int]]:
        """
        Parse a command line and return (action, start, end).
        Raises ValueError if the line is invalid.
        """
        line = line.strip()
        if not line:
            raise ValueError("Empty command line")
        m = InstructionParser._COMMAND_RE.match(line)
        if not m:
            raise ValueError(f"Invalid command format: {line!r}")
        if m.group(2):
            action = m.group(2).lower()
        else:
            action = "toggle"
        x1, y1 = int(m.group(3)), int(m.group(4))
        x2, y2 = int(m.group(5)), int(m.group(6))
        return action, (x1, y1), (x2, y2)
