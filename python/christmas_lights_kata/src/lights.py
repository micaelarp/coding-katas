from __future__ import annotations
from typing import List
from .position import LightPosition


class ChristmasLights:
    """
    Represents a grid of Christmas lights that can be turned on, off, or toggled.
    """

    def __init__(self, width: int = 1000, height: int = 1000) -> None:
        """Initialize the grid with all lights off."""
        self.width: int = width
        self.height: int = height
        # Store the grid as a list of lists of booleans (True = on)
        self._grid: List[List[bool]] = [[False for _ in range(width)] for _ in range(height)]

    def _validate(self, pos: LightPosition) -> None:
        """Raise ValueError if coordinates are out of bounds."""
        if not (0 <= pos.x < self.width and 0 <= pos.y < self.height):
            raise ValueError(f"Coordinates ({pos.x},{pos.y}) out of bounds")

    def _region(self, start: LightPosition, end: LightPosition):
        """Yield all (y, x) positions in the rectangular region from start to end inclusive."""
        x_start, x_end = sorted((start.x, end.x))
        y_start, y_end = sorted((start.y, end.y))
        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                pos = LightPosition(x, y)
                self._validate(pos)
                yield pos

    def turn_on(self, start: LightPosition, end: LightPosition) -> None:
        """Turn on all lights in the region."""
        for pos in self._region(start, end):
            self._grid[pos.y][pos.x] = True

    def turn_off(self, start: LightPosition, end: LightPosition) -> None:
        """Turn off all lights in the region."""
        for pos in self._region(start, end):
            self._grid[pos.y][pos.x] = False

    def toggle(self, start: LightPosition, end: LightPosition) -> None:
        """Toggle all lights in the region."""
        for pos in self._region(start, end):
            self._grid[pos.y][pos.x] = not self._grid[pos.y][pos.x]

    def count_lit(self) -> int:
        """Return the number of lights that are on."""
        return sum(cell for row in self._grid for cell in row)

    def render(self, size: int = 10) -> str:
        """Return a string representation of the grid (for debugging)."""
        lines: List[str] = []
        for row in self._grid[:size]:
            lines.append("".join("█" if cell else "·" for cell in row[:size]))
        return "\n".join(lines)


class LightGrid:
    """
    Facade for ChristmasLights, exposing only region-based operations and safe inspection for tests.
    """

    def __init__(self, width: int = 1000, height: int = 1000) -> None:
        self._lights: ChristmasLights = ChristmasLights(width, height)
        self.width: int = width
        self.height: int = height

    def turn_on_region(self, start: LightPosition, end: LightPosition) -> None:
        """Turn on all lights in the region."""
        self._lights.turn_on(start, end)

    def turn_off_region(self, start: LightPosition, end: LightPosition) -> None:
        """Turn off all lights in the region."""
        self._lights.turn_off(start, end)

    def toggle_region(self, start: LightPosition, end: LightPosition) -> None:
        """Toggle all lights in the region."""
        self._lights.toggle(start, end)

    def count_lit(self) -> int:
        """Return the number of lights that are on."""
        return self._lights.count_lit()

    def render(self, size: int = 10) -> str:
        """Return a string representation of the grid (for debugging)."""
        return self._lights.render(size)

    def is_lit(self, pos: LightPosition) -> bool:
        """Return True if the light at pos is on."""
        self._lights._validate(pos)
        return self._lights._grid[pos.y][pos.x]
