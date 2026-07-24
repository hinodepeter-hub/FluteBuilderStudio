from dataclasses import dataclass
@dataclass(slots=True)
class Measurement:
    name: str
    value: float
    unit: str
