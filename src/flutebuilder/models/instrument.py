from dataclasses import dataclass

from flutebuilder.common.enums import InstrumentType
from flutebuilder.models.material import Material


@dataclass(slots=True)
class Instrument:
    """Represents a flute instrument."""

    name: str
    instrument_type: InstrumentType
    material: Material
    total_length_mm: float
    notes: str = ""
