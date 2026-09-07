from flutebuilder.common.enums import InstrumentType
from flutebuilder.models.instrument import Instrument
from flutebuilder.models.material import Material
from flutebuilder.models.project import Project


def test_create_project():
    project = Project(name="My First Flute")

    assert project.name == "My First Flute"
    assert project.version == "0.1.0"
    assert project.instrument is None


def test_create_project_with_instrument():
    material = Material(
        species="PVC",
        length_mm=455.0,
        outer_diameter_start_mm=25.0,
        outer_diameter_end_mm=25.0,
        inner_diameter_start_mm=23.0,
        inner_diameter_end_mm=23.0,
    )

    instrument = Instrument(
        name="VF-001",
        instrument_type=InstrumentType.OTHER,
        material=material,
        total_length_mm=455.0,
    )

    project = Project(
        name="VF-001 Project",
        instrument=instrument,
    )

    assert project.name == "VF-001 Project"
    assert project.instrument is instrument
    assert project.instrument.name == "VF-001"
    assert project.instrument.total_length_mm == 455.0
