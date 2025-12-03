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

    def apply_line(self, line: str) -> None:
        """Parse a single line like ``turn on 10,20 through 30,40`` or ``toggle 10,20 through 30,40`` and apply it.
        """
        parts = line.strip().split()
        if len(parts) != 5:
            return  # ignora líneas mal formateadas
        if parts[0].lower() == "turn":
            _, sub, start_str, _, end_str = parts
            x1, y1 = map(int, start_str.split(","))
            x2, y2 = map(int, end_str.split(","))
            if sub == "on":
                self.turn_on((x1, y1), (x2, y2))
            elif sub == "off":
                self.turn_off((x1, y1), (x2, y2))
        elif parts[0].lower() == "toggle":
            _, start_str, _, end_str, _ = parts[0], parts[1], parts[2], parts[3], parts[4]
            x1, y1 = map(int, parts[1].split(","))
            x2, y2 = map(int, parts[3].split(","))
            self.toggle((x1, y1), (x2, y2))

    def apply_instructions(self, lines: List[str]) -> None:
        for line in lines:
            self.apply_line(line)

    def count_lit(self) -> int:
        return sum(cell for row in self._grid for cell in row)

    def render(self, size: int = 10) -> str:
        lines = []
        for row in self._grid[:size]:
            lines.append("".join("█" if cell else "·" for cell in row[:size]))
        return "\n".join(lines)


class LightGrid(ChristmasLights):
    def turn_on_region(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        self.turn_on(start, end)

    def turn_off_region(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        self.turn_off(start, end)

    def toggle_region(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        self.toggle(start, end)
