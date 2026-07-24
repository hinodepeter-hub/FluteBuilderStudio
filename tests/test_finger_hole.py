from flutebuilder.models.finger_hole import FingerHole


def test_create_finger_hole():
    hole = FingerHole(
        index=1,
        position_mm=100.0,
        diameter_mm=8.0,
    )

    assert hole.index == 1
    assert hole.position_mm == 100.0
    assert hole.diameter_mm == 8.0
