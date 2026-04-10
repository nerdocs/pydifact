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

test-extended:
	uv run pytest
