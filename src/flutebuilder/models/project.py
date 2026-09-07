from dataclasses import dataclass, field
from pathlib import Path
from uuid import UUID, uuid4

from flutebuilder.models.instrument import Instrument


@dataclass(slots=True)
class Project:
    """Represents a Flute Builder Studio project."""

    name: str
    project_id: UUID = field(default_factory=uuid4)
    version: str = "0.1.0"
    description: str = ""
    project_path: Path | None = None
    instrument: Instrument | None = None
