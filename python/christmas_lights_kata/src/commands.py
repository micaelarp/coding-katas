from typing import Tuple
from .position import LightPosition
from .action import LightAction

class Command:
    """Base class for grid commands."""
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        raise NotImplementedError

class TurnOnCommand(Command):
    """Turn on lights in a region."""
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        if not isinstance(start, LightPosition) or not isinstance(end, LightPosition):
            raise TypeError("start and end must be LightPosition instances")
        grid.turn_on_region(start, end)

class TurnOffCommand(Command):
    """Turn off lights in a region."""
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        if not isinstance(start, LightPosition) or not isinstance(end, LightPosition):
            raise TypeError("start and end must be LightPosition instances")
        grid.turn_off_region(start, end)

class ToggleCommand(Command):
    """Toggle lights in a region."""
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        if not isinstance(start, LightPosition) or not isinstance(end, LightPosition):
            raise TypeError("start and end must be LightPosition instances")
        grid.toggle_region(start, end)

def get_command(action: LightAction) -> Command:
    if action == LightAction.TURN_ON:
        return TurnOnCommand()
    elif action == LightAction.TURN_OFF:
        return TurnOffCommand()
    elif action == LightAction.TOGGLE:
        return ToggleCommand()
    else:
        raise ValueError(f"Unknown action: {action}")
