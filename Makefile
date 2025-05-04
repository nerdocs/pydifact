dev:
	pip install -e .[dev]

install:
	pip install .

build: dev
	python -m build

upload: build
	twine upload dist/*

test:
	pytest --ignore tests/test_huge_message.py

mypy:
	mypy --pretty pydifact

test-extended:
	pytest

run-isort:
	isort .

check-isort:
	isort . --check