from dataclasses import dataclass, field

from flutebuilder.common.enums import InstrumentType
from flutebuilder.models.embouchure import Embouchure
from flutebuilder.models.finger_hole import FingerHole
from flutebuilder.models.material import Material


@dataclass(slots=True)
class Instrument:
    """Represents a flute instrument."""

    name: str
    instrument_type: InstrumentType
    material: Material
    total_length_mm: float

    embouchure: Embouchure | None = None
    finger_holes: list[FingerHole] = field(default_factory=list)

    notes: str = ""
