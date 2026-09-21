# Supported Python versions, read from the classifiers in pyproject.toml.
PYTHON_VERSIONS := $(shell python3 scripts/python_versions.py)

dev:
	uv sync

install:
	uv sync --no-dev

build:
	uv build

upload: build
	uv run twine upload dist/*

test:
	uv run pytest --ignore tests/test_huge_message.py

mypy:
	uv run mypy --pretty pydifact

format:
	uv run ruff format .
	uv run ruff check --fix .

check-format:
	uv run ruff format --check .
	uv run ruff check .

test-extended:
	uv run pytest

# Run the test suite against every supported Python version (as in CI).
test-all:
	for v in $(PYTHON_VERSIONS); do \
		uv run --python $$v --isolated pytest -q --ignore tests/test_huge_message.py || exit 1; \
	done

# Generate EDIFACT directory release syntax data.
# Usage: make generate RELEASE=21a
generate:
	uv run python -m pydifact.generator.runner $(RELEASE)

# Generate service segment syntax data for a given EDIFACT syntax version.
# Usage: make generate-service SYNTAX=4   (or SYNTAX=21A / SYNTAX=40219)
generate-service:
	uv run python -m pydifact.generator.runner service $(SYNTAX)
