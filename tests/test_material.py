from flutebuilder.models.material import Material


def test_create_material():
    material = Material(
        species="Bamboo",
        length_mm=823.0,
        outer_diameter_start_mm=30.0,
        outer_diameter_end_mm=26.0,
    )

    assert material.species == "Bamboo"
    assert material.length_mm == 823.0
    assert material.outer_diameter_start_mm == 30.0
