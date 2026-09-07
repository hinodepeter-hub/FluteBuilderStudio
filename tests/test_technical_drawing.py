from flutebuilder.drawing.technical_drawing import TechnicalDrawing
from flutebuilder.models.project import Project


def test_create_technical_drawing():
    project = Project(name="VF-001")

    drawing = TechnicalDrawing(project)

    assert drawing.project is project
    assert drawing.page_width_mm == 297.0
    assert drawing.page_height_mm == 210.0
    assert drawing.scale == 1.0
    assert drawing.show_dimensions is True


def test_create_scaled_technical_drawing():
    project = Project(name="VF-001")

    drawing = TechnicalDrawing(
        project=project,
        scale=2.0,
        show_dimensions=False,
    )

    assert drawing.project is project
    assert drawing.scale == 2.0
    assert drawing.show_dimensions is False
