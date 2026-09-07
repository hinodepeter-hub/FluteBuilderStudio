from flutebuilder.common.enums import InstrumentType
from flutebuilder.models.embouchure import Embouchure
from flutebuilder.models.finger_hole import FingerHole
from flutebuilder.models.instrument import Instrument
from flutebuilder.models.material import Material


def test_create_instrument():
    material = Material(
        species="Phyllostachys edulis",
        length_mm=800.0,
        outer_diameter_start_mm=30.0,
        outer_diameter_end_mm=22.0,
        inner_diameter_start_mm=20.0,
        inner_diameter_end_mm=16.0,
        has_root_end=True,
    )

    instrument = Instrument(
        name="Xiao G4",
        instrument_type=InstrumentType.XIAO,
        material=material,
        total_length_mm=760.0,
        notes="Prototype",
    )

    assert instrument.name == "Xiao G4"
    assert instrument.instrument_type == InstrumentType.XIAO
    assert instrument.material == material
    assert instrument.total_length_mm == 760.0
    assert instrument.notes == "Prototype"
    assert instrument.embouchure is None
    assert instrument.finger_holes == []


def test_create_instrument_with_embouchure_and_finger_holes():
    material = Material(
        species="PVC",
        length_mm=455.0,
        outer_diameter_start_mm=25.0,
        outer_diameter_end_mm=25.0,
        inner_diameter_start_mm=23.0,
        inner_diameter_end_mm=23.0,
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
    ]

    instrument = Instrument(
        name="VF-001",
        instrument_type=InstrumentType.OTHER,
        material=material,
        total_length_mm=455.0,
        embouchure=embouchure,
        finger_holes=finger_holes,
    )

    assert instrument.name == "VF-001"
    assert instrument.embouchure == embouchure
    assert instrument.finger_holes == finger_holes
    assert instrument.finger_holes[0].position_mm == 57.0
    assert instrument.finger_holes[1].diameter_mm == 9.0
    assert instrument.finger_holes[2].diameter_mm == 6.0
