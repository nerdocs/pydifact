# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Commands

```bash
uv run pytest                                # all tests (add --run-extended for huge-file tests)
uv run pytest tests/test_parser.py::test_x   # single test
uv run ruff format . && uv run ruff check --fix .   # format + import sorting (required before commit)
uv run mypy pydifact                         # type checking
uv run bandit -q -r pydifact                 # security lint (see `# nosec` markers)
make generate RELEASE=24a                    # regenerate directory data (dev tool, see docs/generator.rst)
make generate-service SYNTAX=4               # regenerate service segment data
```

## Architecture

pydifact is a UN/EDIFACT parser and serializer:

```
raw string → Tokenizer → Token stream → Parser → Segment stream → SegmentCollection
```

### Core (`pydifact/`)

- `tokenizer.py` / `token.py` – raw string → `Token` objects; handles escape characters.
- `parser.py` – `Token` stream → `Segment` objects. Detects `UNA` for control characters, reads `UNB` for syntax
  version/directory.
- `segments.py` – `Segment` (tag + elements). `SegmentFactory` picks typed subclasses from `Segment.plugins`;
  subclasses with a `tag` attribute auto-register via `__init_subclass__` (`__omitted__ = True` opts out).
  `Segment.validate()` is XML-driven, definitions cached with `@lru_cache`.
- `serializer.py` – `Segment` list → EDI string, incl. `UNA` and escaping.
- `control/characters.py` – the 6 EDIFACT control characters; default `:+.? '`.
- `segmentcollection.py` – `AbstractSegmentsContainer` → `RawSegmentCollection` (no envelope), `Message`
  (UNH/UNT), `Interchange` (UNB/UNZ, main entry point: `from_file()`, `from_str()`, `get_messages()`).
- `constants.py` – `Element = str | list[str]`, `Elements = list[Element]`, defaults (`EDI_DEFAULT_DIRECTORY = "d24a"`).

### Syntax definitions (`pydifact/syntax/`)

- `common.py` – `DataElement`, `CompositeDataElement`, type/length assertions.
- `v1/` … `v4/` – typed service segment classes (`UNB`, `UNH`, …) per syntax version.
- `service/v100` … `v402/` – XML service segment definitions per syntax release.
- `d21a/`, `d23a/`, `d24a/` – XML message directories (segments, elements, codes, message structures).

### Generator (`pydifact/generator/`)

Dev-only tool (excluded from mypy) that downloads UNECE directory zips and generates the XML data above.
Parses untrusted XML via `defusedxml`; stdlib `ElementTree` is only used to build XML (`# nosec B405`).

## Tests

`tests/data/*.edi` holds sample interchanges; `tests/messagetypes/` and `tests/segments/` cover typed messages
and segments.
