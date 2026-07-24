from dataclasses import dataclass
@dataclass(slots=True)
class FingerHole:
    index: int
    position_mm: float
    diameter_mm: float
