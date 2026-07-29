# FluteBuilderStudio v0.3.0-alpha

This release introduces the first implementation of the FluteBuilderStudio project file format.

## ✨ New features

### Project serialization

- Added project serialization to Python dictionaries
- Added deserialization from dictionaries back to Project objects
- Added saving projects to YAML (.fbs) files
- Added loading projects from YAML (.fbs) files

### Project file format

- Introduced the initial `.fbs` project format
- Versioned project structure for future compatibility

### Testing

- Added unit tests for serialization
- Added round-trip serialization tests
- Added save/load tests
- All tests passing

## Project status

Implemented:

- ✅ Core domain models
- ✅ Project serialization
- ✅ YAML project file format
- ✅ Continuous Integration (GitHub Actions)

## Next milestone

**FBS-006 – Technical Drawing**

Planned features:

- flute drawing
- dimensions
- SVG export
- PDF export
