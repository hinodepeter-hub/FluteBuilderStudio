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
