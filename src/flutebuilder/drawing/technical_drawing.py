from dataclasses import dataclass

from flutebuilder.models.project import Project


@dataclass(slots=True)
class TechnicalDrawing:
    """Represents a technical drawing of a flute project."""

    project: Project

    page_width_mm: float = 297.0
    page_height_mm: float = 210.0
    scale: float = 1.0
    show_dimensions: bool = True
