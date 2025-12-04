from typing import Tuple
from .position import LightPosition

class Command:
    """
    Abstract base class for grid commands.
    """
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        """Apply the command to the grid."""
        raise NotImplementedError

class TurnOnCommand(Command):
    """
    Command to turn on lights in a region.
    """
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        grid.turn_on_region(start, end)

class TurnOffCommand(Command):
    """
    Command to turn off lights in a region.
    """
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        grid.turn_off_region(start, end)

class ToggleCommand(Command):
    """
    Command to toggle lights in a region.
    """
    def apply(self, grid: object, start: LightPosition, end: LightPosition) -> None:
        grid.toggle_region(start, end)

def get_command(action: str) -> Command:
    """
    Factory to get the correct command instance for the given action.
    """
    if action == "on":
        return TurnOnCommand()
    elif action == "off":
        return TurnOffCommand()
    elif action == "toggle":
        return ToggleCommand()
    else:
        raise ValueError(f"Unknown action: {action}")
