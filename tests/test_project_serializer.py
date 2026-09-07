from flutebuilder.common.enums import InstrumentType
from flutebuilder.models.embouchure import Embouchure
from flutebuilder.models.finger_hole import FingerHole
from flutebuilder.models.instrument import Instrument
from flutebuilder.models.material import Material
from pathlib import Path
from flutebuilder.models.project import Project
from flutebuilder.serialization.project_serializer import (
    dict_to_project,
    project_to_dict,
    save_project,
    load_project,
)


def test_project_to_dict():
    project = Project(name="My First Project")

    data = project_to_dict(project)

    assert isinstance(data, dict)
    assert data["version"] == 1
    assert data["project"]["name"] == "My First Project"


def test_project_round_trip():
    original = Project(name="My First Project")

    data = project_to_dict(original)
    loaded = dict_to_project(data)

    assert loaded.name == original.name
    assert loaded.project_id == original.project_id
    assert loaded.version == original.version
    assert loaded.description == original.description
    assert loaded.project_path == original.project_path

def test_save_project(tmp_path: Path):
    project = Project(name="Demo")

    filename = tmp_path / "demo.fbs"

    save_project(project, filename)

    assert filename.exists()


def test_save_and_load_project(tmp_path: Path):
    original = Project(name="Demo Project")

    filename = tmp_path / "demo.fbs"

    save_project(original, filename)
    loaded = load_project(filename)

    assert loaded.name == original.name
    assert loaded.project_id == original.project_id
    assert loaded.version == original.version
    assert loaded.description == original.description
    assert loaded.project_path == original.project_path


def test_project_with_instrument_roundtrip():
    material = Material(
        species="PVC",
        length_mm=455.0,
        outer_diameter_start_mm=25.0,
        outer_diameter_end_mm=25.0,
        inner_diameter_start_mm=23.0,
        inner_diameter_end_mm=23.0,
        has_root_end=False,
    )

    embouchure = Embouchure(
        width_mm=10.0,
        length_mm=8.0,
        offset_from_top_mm=0.0,
    )

    finger_holes = [
        FingerHole(index=1, position_mm=57.0, diameter_mm=9.0),
        FingerHole(index=2, position_mm=107.0, diameter_mm=9.0),
        FingerHole(index=3, position_mm=157.0, diameter_mm=6.0),
        FingerHole(index=4, position_mm=207.0, diameter_mm=6.0),
        FingerHole(index=5, position_mm=260.0, diameter_mm=5.0),
    ]

    instrument = Instrument(
        name="VF-001",
        instrument_type=InstrumentType.OTHER,
        material=material,
        total_length_mm=455.0,
        embouchure=embouchure,
        finger_holes=finger_holes,
        notes="PVC notched flute",
    )

    project = Project(
        name="VF-001",
        description="PVC notched flute prototype",
        instrument=instrument,
    )

    restored = dict_to_project(project_to_dict(project))

    assert restored.name == "VF-001"
    assert restored.description == "PVC notched flute prototype"

    assert restored.instrument is not None
    assert restored.instrument.name == "VF-001"
    assert restored.instrument.instrument_type == InstrumentType.OTHER
    assert restored.instrument.total_length_mm == 455.0
    assert restored.instrument.notes == "PVC notched flute"

    assert restored.instrument.material.species == "PVC"
    assert restored.instrument.material.length_mm == 455.0
    assert restored.instrument.material.outer_diameter_start_mm == 25.0
    assert restored.instrument.material.outer_diameter_end_mm == 25.0
    assert restored.instrument.material.inner_diameter_start_mm == 23.0
    assert restored.instrument.material.inner_diameter_end_mm == 23.0
    assert restored.instrument.material.has_root_end is False

    assert restored.instrument.embouchure is not None
    assert restored.instrument.embouchure.width_mm == 10.0
    assert restored.instrument.embouchure.length_mm == 8.0
    assert restored.instrument.embouchure.offset_from_top_mm == 0.0

    assert len(restored.instrument.finger_holes) == 5

    assert restored.instrument.finger_holes[0].index == 1
    assert restored.instrument.finger_holes[0].position_mm == 57.0
    assert restored.instrument.finger_holes[0].diameter_mm == 9.0

    assert restored.instrument.finger_holes[4].index == 5
    assert restored.instrument.finger_holes[4].position_mm == 260.0
    assert restored.instrument.finger_holes[4].diameter_mm == 5.0


def test_load_legacy_project_without_instrument():
    data = {
        "version": 1,
        "project": {
            "project_id": "12345678-1234-5678-1234-567812345678",
            "name": "Legacy Project",
            "version": "0.1.0",
            "description": "Legacy project format",
            "project_path": None,
        },
    }

    restored = dict_to_project(data)

    assert restored.name == "Legacy Project"
    assert restored.version == "0.1.0"
    assert restored.description == "Legacy project format"
    assert restored.project_path is None
    assert restored.instrument is None

