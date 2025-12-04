from __future__ import annotations
from typing import List, Tuple


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

    def _validate(self, x: int, y: int) -> None:
        """Raise ValueError if coordinates are out of bounds."""
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ValueError(f"Coordinates ({x},{y}) out of bounds")

    def _region(self, start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[int, int]:
        """Yield all (y, x) positions in the rectangular region from start to end inclusive."""
        x1, y1 = start
        x2, y2 = end
        x_start, x_end = sorted((x1, x2))
        y_start, y_end = sorted((y1, y2))
        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                self._validate(x, y)
                yield y, x

    def turn_on(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """Turn on all lights in the region."""
        for y, x in self._region(start, end):
            self._grid[y][x] = True

    def turn_off(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """Turn off all lights in the region."""
        for y, x in self._region(start, end):
            self._grid[y][x] = False

    def toggle(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """Toggle all lights in the region."""
        for y, x in self._region(start, end):
            self._grid[y][x] = not self._grid[y][x]

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

    def turn_on_region(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """Turn on all lights in the region."""
        self._lights.turn_on(start, end)

    def turn_off_region(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """Turn off all lights in the region."""
        self._lights.turn_off(start, end)

    def toggle_region(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """Toggle all lights in the region."""
        self._lights.toggle(start, end)

    def count_lit(self) -> int:
        """Return the number of lights that are on."""
        return self._lights.count_lit()

    def render(self, size: int = 10) -> str:
        """Return a string representation of the grid (for debugging)."""
        return self._lights.render(size)

    def is_lit(self, x: int, y: int) -> bool:
        """Return True if the light at (x, y) is on."""
        return self._lights._grid[y][x]
