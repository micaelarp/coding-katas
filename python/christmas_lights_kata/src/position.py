from dataclasses import dataclass

@dataclass(frozen=True)
class LightPosition:
    """Immutable position in the grid."""
    x: int
    y: int

    def __str__(self) -> str:
        return f"({self.x},{self.y})"
