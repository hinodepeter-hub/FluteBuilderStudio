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
