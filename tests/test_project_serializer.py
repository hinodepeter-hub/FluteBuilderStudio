from flutebuilder.models.project import Project
from flutebuilder.serialization.project_serializer import (
    dict_to_project,
    project_to_dict,
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
