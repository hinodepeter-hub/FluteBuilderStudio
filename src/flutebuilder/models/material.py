from dataclasses import dataclass, field


@dataclass(slots=True)
class Material:
    """Represents raw material for a flute."""

    species: str = ""
    length_mm: float = 0.0

    outer_diameter_start_mm: float = 0.0
    outer_diameter_end_mm: float = 0.0

    inner_diameter_start_mm: float = 0.0
    inner_diameter_end_mm: float = 0.0

    has_root_end: bool = False

    node_positions_mm: list[float] = field(default_factory=list)

    notes: str = ""
