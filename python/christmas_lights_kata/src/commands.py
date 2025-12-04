from typing import Tuple
from .position import LightPosition
from .action import LightAction

class Command:
    """
    Abstract base class for grid commands. Each command applies an action to a region.
    """
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        """Apply the command to the grid. Must be implemented by subclasses."""
        raise NotImplementedError

class TurnOnCommand(Command):
    """
    Command to turn on lights in a region.
    """
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        if not isinstance(start, LightPosition) or not isinstance(end, LightPosition):
            raise TypeError("start and end must be LightPosition instances")
        grid.turn_on_region(start, end)

class TurnOffCommand(Command):
    """
    Command to turn off lights in a region.
    """
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        if not isinstance(start, LightPosition) or not isinstance(end, LightPosition):
            raise TypeError("start and end must be LightPosition instances")
        grid.turn_off_region(start, end)

class ToggleCommand(Command):
    """
    Command to toggle lights in a region.
    """
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        if not isinstance(start, LightPosition) or not isinstance(end, LightPosition):
            raise TypeError("start and end must be LightPosition instances")
        grid.toggle_region(start, end)

def get_command(action: LightAction) -> Command:
    """
    Factory to get the correct command instance for the given action.
    """
    if action == LightAction.TURN_ON:
        return TurnOnCommand()
    elif action == LightAction.TURN_OFF:
        return TurnOffCommand()
    elif action == LightAction.TOGGLE:
        return ToggleCommand()
    else:
        raise ValueError(f"Unknown action: {action}")
