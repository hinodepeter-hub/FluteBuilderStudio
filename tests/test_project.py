from flutebuilder.models.project import Project


def test_create_project():
    project = Project(name="My First Flute")

    assert project.name == "My First Flute"
    assert project.version == "0.1.0"
