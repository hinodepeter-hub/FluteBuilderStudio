from flutebuilder.models.measurement import Measurement


def test_create_measurement():
    measurement = Measurement(
        name="Length",
        value=500.0,
        unit="mm",
    )

    assert measurement.name == "Length"
    assert measurement.value == 500.0
    assert measurement.unit == "mm"
