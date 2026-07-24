from flutebuilder.models.embouchure import Embouchure


def test_create_embouchure():
    emb = Embouchure(
        width_mm=10.0,
        length_mm=12.0,
        offset_from_top_mm=25.0,
    )

    assert emb.width_mm == 10.0
    assert emb.length_mm == 12.0
    assert emb.offset_from_top_mm == 25.0
