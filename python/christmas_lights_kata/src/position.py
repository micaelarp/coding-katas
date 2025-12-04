from dataclasses import dataclass

@dataclass(frozen=True)
class LightPosition:
    x: int
    y: int

