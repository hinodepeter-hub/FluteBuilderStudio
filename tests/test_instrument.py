from flutebuilder.common.enums import InstrumentType
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
