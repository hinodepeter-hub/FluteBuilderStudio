import yaml
from pathlib import Path
from uuid import UUID

from flutebuilder.models.project import Project


def project_to_dict(project: Project) -> dict:
    """Convert a Project instance into a serializable dictionary."""

    return {
        "version": 1,
        "project": {
            "project_id": str(project.project_id),
            "name": project.name,
            "version": project.version,
            "description": project.description,
            "project_path": (
                str(project.project_path)
                if project.project_path is not None
                else None
            ),
        },
    }


def dict_to_project(data: dict) -> Project:
    """Convert a dictionary into a Project instance."""

    project = data["project"]

    return Project(
        name=project["name"],
        project_id=UUID(project["project_id"]),
        version=project["version"],
        description=project["description"],
        project_path=(
            Path(project["project_path"])
            if project["project_path"] is not None
            else None
        ),
    )


def save_project(project: Project, filename: str) -> None:
    """Save a Project to a .fbs (YAML) file."""

    data = project_to_dict(project)

    with open(filename, "w", encoding="utf-8") as file:
        yaml.safe_dump(
            data,
            file,
            sort_keys=False,
            allow_unicode=True,
        )

def load_project(filename: str) -> Project:
    """Load a Project from a .fbs (YAML) file."""

    with open(filename, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return dict_to_project(data)
