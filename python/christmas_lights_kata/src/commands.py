from typing import Tuple

class Command:
    def apply(self, grid, start: Tuple[int, int], end: Tuple[int, int]):
        raise NotImplementedError

class TurnOnCommand(Command):
    def apply(self, grid, start, end):
        grid.turn_on_region(start, end)

class TurnOffCommand(Command):
    def apply(self, grid, start, end):
        grid.turn_off_region(start, end)

class ToggleCommand(Command):
    def apply(self, grid, start, end):
        grid.toggle_region(start, end)

def get_command(action: str) -> Command:
    if action == "on":
        return TurnOnCommand()
    elif action == "off":
        return TurnOffCommand()
    elif action == "toggle":
        return ToggleCommand()
    else:
        raise ValueError(f"Unknown action: {action}")
