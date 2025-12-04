from typing import Tuple

class Command:
    def apply(self, grid, start: Tuple[int, int], end: Tuple[int, int]):
        raise NotImplementedError

class TurnOnCommand(Command):
    def apply(self, grid, start, end):
        for y in range(start[1], end[1]+1):
            for x in range(start[0], end[0]+1):
                grid._grid[y][x] = True

class TurnOffCommand(Command):
    def apply(self, grid, start, end):
        for y in range(start[1], end[1]+1):
            for x in range(start[0], end[0]+1):
                grid._grid[y][x] = False

class ToggleCommand(Command):
    def apply(self, grid, start, end):
        for y in range(start[1], end[1]+1):
            for x in range(start[0], end[0]+1):
                grid._grid[y][x] = not grid._grid[y][x]

def get_command(action: str) -> Command:
    if action == "on":
        return TurnOnCommand()
    elif action == "off":
        return TurnOffCommand()
    elif action == "toggle":
        return ToggleCommand()
    else:
        raise ValueError(f"Unknown action: {action}")

