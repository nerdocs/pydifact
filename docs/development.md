# Development Guide

## Setting Up Development Environment

1. **Clone the repository**
   ```bash
   git clone https://github.com/nerdocs/pydifact.git
   cd pydifact

2. Install development dependencies
```bash
make dev
# or manually:
pip install -e .[dev]
```

3. Verify installation
```bash
make test
# or pytest directly, should work.
```


## Development Workflow

### Running Tests

pydifact uses [pytest](http://pytest.org) for testing. There is a shortcut in the Makefile for your convenience:

```bash
# Run standard test suite (excludes huge message tests)
make test
```

There are some additional tests to check the performance of parsing huge files - you can include that tests by calling

```bash
# Run all tests including extended ones
make test-extended

# Run with coverage
pytest --cov=pydifact
```

### Code Formatting

All code must be formatted with [black](https://black.readthedocs.io) before committing.

```bash
# Format all Python files
black pydifact tests scripts

# Check formatting without changes
black --check pydifact
```

### Type Checking

```bash
make mypy
```

### Building Documentation

```bash
cd docs
make html
# View at docs/_build/html/index.html
```

## Generating EDIFACT Specifications

The generator downloads official UN/EDIFACT specifications and creates Python classes.

```bash
# Generate classes for a specific EDIFACT version
make generate d24a

# Or run directly as module
python -m scripts.generator.pydifact_generator d24a
```

### Supported Versions

* `d24a` - EDIFACT Directory version D.24A
* `d11b` - EDIFACT Directory version D.11B
Other versions available at service.unece.org

### Clear cache

```bash
make generate --clear-cache

# or as module
python -m scripts.generator.pydifact_generator --clear-cache
```

### Generator Output
Generated files are placed in `pydifact/syntax/<version>/`:
`data.py` - Data element classes
`composite.py` - Composite data element classes
`segments.py` - Segment classes
`messages.py` - Message classes


## Adding New Features

1. Create a feature branch

```bash
git checkout -b feature/my-new-feature
```

2. Write tests (TDD approach)
```bash
# Add tests in tests/
pytest tests/test_my_feature.py
```
3. Implement the feature
* Follow existing code patterns
* Add type hints
* Include docstrings

4. Format and test 
```bash
black pydifact tests
make test
make mypy
```

5. Update documentation
* Add docstrings to new functions/classes
* Update relevant .md files in docs/
* Update CHANGELOG.md

6. Submit pull request

## Release Process
1. Update version in `pydifact/__init__.py`
2. Update CHANGELOG.md
3. Run full test suite: `make test-extended`
4. Build package: `make build`
5. Upload to PyPI: `make upload`

## Getting Help

* Check existing tests for examples
* Review documentation at https://pydifact.readthedocs.io
* Open an issue at https://github.com/nerdocs/pydifact/issues
