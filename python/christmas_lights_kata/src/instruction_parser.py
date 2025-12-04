import re
from typing import Tuple
from .position import LightPosition
from .action import LightAction

class InstructionParser:
    """
    Parses instruction lines for grid commands. Validates format and coordinates.
    - Only accepts commands in the format: 'turn on x1,y1 through x2,y2', 'turn off ...', or 'toggle ...'.
    - Coordinates must be integers >= 0.
    - Returns (LightAction, LightPosition, LightPosition).
    - Raises ValueError for invalid lines or coordinates.
    """
    _COMMAND_RE = re.compile(r"^(turn\s+(on|off)|toggle)\s+(-?\d+),(-?\d+)\s+through\s+(-?\d+),(-?\d+)$", re.IGNORECASE)

    @staticmethod
    def _validate_coords(x1: int, y1: int, x2: int, y2: int) -> None:
        """Raise ValueError if any coordinate is negative."""
        for val, name in zip([x1, y1, x2, y2], ["x1", "y1", "x2", "y2"]):
            if val < 0:
                raise ValueError(f"Coordinate {name} must be >= 0, got {val}")

    @staticmethod
    def _get_action(action_str: str) -> LightAction:
        """Map a string to a LightAction enum, raising ValueError if unknown."""
        action_str = action_str.lower()
        if action_str == "on":
            return LightAction.TURN_ON
        elif action_str == "off":
            return LightAction.TURN_OFF
        elif action_str == "toggle":
            return LightAction.TOGGLE
        else:
            raise ValueError(f"Unknown action: {action_str}")

    @staticmethod
    def parse(line: str) -> Tuple[LightAction, LightPosition, LightPosition]:
        """
        Parse a command line and return (action, start, end).
        Raises ValueError if the line is invalid or coordinates are not valid integers >= 0.
        """
        line = line.strip()
        if not line:
            raise ValueError("Empty command line")
        m = InstructionParser._COMMAND_RE.match(line)
        if not m:
            raise ValueError(f"Invalid command format: {line!r}")
        action_str = m.group(2) if m.group(2) else "toggle"
        action = InstructionParser._get_action(action_str)
        try:
            x1, y1 = int(m.group(3)), int(m.group(4))
            x2, y2 = int(m.group(5)), int(m.group(6))
        except ValueError:
            raise ValueError("Coordinates must be integers")
        InstructionParser._validate_coords(x1, y1, x2, y2)
        start = LightPosition(x1, y1)
        end = LightPosition(x2, y2)
        return action, start, end
