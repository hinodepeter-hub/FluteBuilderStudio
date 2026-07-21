# Domain Model

## Overview

```mermaid
classDiagram

class Project {
    +name
    +author
    +project_version
    +created_at
    +modified_at
}

class Instrument {
    +name
    +type
    +tuning
    +notes
}

class Material {
    +species
    +length_mm
    +outer_diameter_start_mm
    +outer_diameter_end_mm
    +inner_diameter_start_mm
    +inner_diameter_end_mm
    +has_root_end
    +node_positions_mm
}

class Embouchure {
    +type
}

class Hole {
    +position_mm
    +diameter_mm
}

class Measurement {
    +name
    +value
    +unit
}

Project "1" --> "1..*" Instrument
Instrument "1" --> "1" Material
Instrument "1" --> "1" Embouchure
Instrument "1" --> "0..*" Hole
Instrument "1" --> "0..*" Measurement
```

## Design Principles

* Models are independent from the GUI.
* Models are independent from the acoustic engine.
* Models are independent from file storage.
* Models use Python dataclasses.
* Models are fully covered by unit tests.
* Serialization is implemented outside the models.
