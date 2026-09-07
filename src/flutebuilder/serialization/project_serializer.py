import yaml
from pathlib import Path
from uuid import UUID

from flutebuilder.models.embouchure import Embouchure
from flutebuilder.models.finger_hole import FingerHole
from flutebuilder.models.instrument import Instrument
from flutebuilder.models.material import Material
from flutebuilder.models.project import Project


def material_to_dict(material: Material) -> dict:
    """Convert a Material instance into a serializable dictionary."""

    return {
        "species": material.species,
        "length_mm": material.length_mm,
        "outer_diameter_start_mm": material.outer_diameter_start_mm,
        "outer_diameter_end_mm": material.outer_diameter_end_mm,
        "inner_diameter_start_mm": material.inner_diameter_start_mm,
        "inner_diameter_end_mm": material.inner_diameter_end_mm,
        "has_root_end": material.has_root_end,
        "node_positions_mm": material.node_positions_mm,
        "notes": material.notes,
    }


def dict_to_material(data: dict) -> Material:
    """Convert a dictionary into a Material instance."""

    return Material(
        species=data["species"],
        length_mm=data["length_mm"],
        outer_diameter_start_mm=data["outer_diameter_start_mm"],
        outer_diameter_end_mm=data["outer_diameter_end_mm"],
        inner_diameter_start_mm=data["inner_diameter_start_mm"],
        inner_diameter_end_mm=data["inner_diameter_end_mm"],
        has_root_end=data["has_root_end"],
        node_positions_mm=data["node_positions_mm"],
        notes=data["notes"],
    )


def embouchure_to_dict(embouchure: Embouchure) -> dict:
    """Convert an Embouchure instance into a serializable dictionary."""

    return {
        "width_mm": embouchure.width_mm,
        "length_mm": embouchure.length_mm,
        "offset_from_top_mm": embouchure.offset_from_top_mm,
    }


def dict_to_embouchure(data: dict) -> Embouchure:
    """Convert a dictionary into an Embouchure instance."""

    return Embouchure(
        width_mm=data["width_mm"],
        length_mm=data["length_mm"],
        offset_from_top_mm=data["offset_from_top_mm"],
    )


def finger_hole_to_dict(finger_hole: FingerHole) -> dict:
    """Convert a FingerHole instance into a serializable dictionary."""

    return {
        "index": finger_hole.index,
        "position_mm": finger_hole.position_mm,
        "diameter_mm": finger_hole.diameter_mm,
    }


def dict_to_finger_hole(data: dict) -> FingerHole:
    """Convert a dictionary into a FingerHole instance."""

    return FingerHole(
        index=data["index"],
        position_mm=data["position_mm"],
        diameter_mm=data["diameter_mm"],
    )


def instrument_to_dict(instrument: Instrument) -> dict:
    """Convert an Instrument instance into a serializable dictionary."""

    return {
        "name": instrument.name,
        "instrument_type": instrument.instrument_type.value,
        "material": material_to_dict(instrument.material),
        "total_length_mm": instrument.total_length_mm,
        "embouchure": (
            embouchure_to_dict(instrument.embouchure)
            if instrument.embouchure is not None
            else None
        ),
        "finger_holes": [
            finger_hole_to_dict(hole)
            for hole in instrument.finger_holes
        ],
        "notes": instrument.notes,
    }


def dict_to_instrument(data: dict) -> Instrument:
    """Convert a dictionary into an Instrument instance."""

    from flutebuilder.common.enums import InstrumentType

    return Instrument(
        name=data["name"],
        instrument_type=InstrumentType(data["instrument_type"]),
        material=dict_to_material(data["material"]),
        total_length_mm=data["total_length_mm"],
        embouchure=(
            dict_to_embouchure(data["embouchure"])
            if data["embouchure"] is not None
            else None
        ),
        finger_holes=[
            dict_to_finger_hole(hole)
            for hole in data["finger_holes"]
        ],
        notes=data["notes"],
    )


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
            "instrument": (
                instrument_to_dict(project.instrument)
                if project.instrument is not None
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
        instrument=(
            dict_to_instrument(project["instrument"])
            if project.get("instrument") is not None
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
