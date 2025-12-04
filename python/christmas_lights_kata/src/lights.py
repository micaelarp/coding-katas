from __future__ import annotations
from typing import List, Tuple


class ChristmasLights:

    def __init__(self, width: int = 1000, height: int = 1000) -> None:
        self.width = width
        self.height = height
        # Store the grid as a list of lists of booleans (True = on)
        self._grid: List[List[bool]] = [[False for _ in range(width)] for _ in range(height)]

    def _validate(self, x: int, y: int) -> None:
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise ValueError(f"Coordinates ({x},{y}) out of bounds")

    def _region(self, start: Tuple[int, int], end: Tuple[int, int]):
        x1, y1 = start
        x2, y2 = end
        x_start, x_end = sorted((x1, x2))
        y_start, y_end = sorted((y1, y2))
        for y in range(y_start, y_end + 1):
            for x in range(x_start, x_end + 1):
                self._validate(x, y)
                yield y, x

    def turn_on(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        for y, x in self._region(start, end):
            self._grid[y][x] = True

    def turn_off(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        for y, x in self._region(start, end):
            self._grid[y][x] = False

    def toggle(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        for y, x in self._region(start, end):
            self._grid[y][x] = not self._grid[y][x]

    def count_lit(self) -> int:
        return sum(cell for row in self._grid for cell in row)

    def render(self, size: int = 10) -> str:
        lines = []
        for row in self._grid[:size]:
            lines.append("".join("█" if cell else "·" for cell in row[:size]))
        return "\n".join(lines)


class LightGrid:
    def __init__(self, width: int = 1000, height: int = 1000):
        self._lights = ChristmasLights(width, height)
        self.width = width
        self.height = height

    def turn_on_region(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        self._lights.turn_on(start, end)

    def turn_off_region(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        self._lights.turn_off(start, end)

    def toggle_region(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        self._lights.toggle(start, end)

    def count_lit(self) -> int:
        return self._lights.count_lit()

    def render(self, size: int = 10) -> str:
        return self._lights.render(size)

    def is_lit(self, x: int, y: int) -> bool:
        return self._lights._grid[y][x]
