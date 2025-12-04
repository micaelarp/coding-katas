from dataclasses import dataclass

@dataclass(frozen=True)
class LightPosition:
    """
    Immutable value object representing a position in the grid.
    Used for all grid operations to ensure clarity and domain consistency.
    """
    x: int
    y: int

    def __str__(self) -> str:
        return f"({self.x},{self.y})"
