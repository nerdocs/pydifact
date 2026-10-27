# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

[Unreleased]

[0.3.0] - 2026-10-27
### Added
- Support for Python 3.14
- `NonConformantEDIWarning` for accepted deviations from the spec; switch off with `warn_non_conformant=False`
- `validate` parameter for `Parser`, `from_str()`, `from_segments()` and `Interchange.from_file()` to skip validation when parsing

### Changed
- An empty mandatory element (e.g. `UNB+…++…`) warns with `NonConformantEDIWarning` instead of raising
  `ValidationError`; a missing element still raises
- The `UNB` date/time of preparation is strict: composite `date:time`, 6-digit date for syntax 1–3, 8-digit for 4;
  wrong length, missing time or the Austrian AEK-style split `date+time` raise `EDISyntaxError` (no warning anymore)
- `Interchange` serializes an 8-digit `UNB` date for syntax version 4
- Update dependencies (dependabot, incl. security fixes)

### Security
- Generator downloads are hardened against Zip Slip and MITM; untrusted XML is parsed with `defusedxml`

### Fixed
- Include the XML syntax definitions in sdist and wheel, so validation works in installed packages
- Validate service segments against the service directory even when an explicit `directory` is passed to `Parser`
- `Segment.__init__` overload signature now matches the implementation (`tag` is positional-only)
- Don't mistake an escaped segment terminator followed by `UNA` in free text for a service string advice
- Malformed input raises `EDISyntaxError` instead of `StopIteration`, `IndexError`, `ValueError` or `AssertionError`
- A reused `Parser` no longer leaks the UNB version of the previous interchange into the next `parse()`
- `Segment.__getitem__` returns `None` for negative out-of-range indices too, instead of raising `IndexError`
- The parser now picks the typed service segment classes (e.g. `syntax.v4.UNBSegment`) matching the UNB syntax version
- `Segment.__eq__` is symmetric between typed segments and generic `Segment`s
- Numeric elements accept a leading minus and a decimal mark (not counted in length); alphabetic elements accept spaces
- Empty segments warn with `NonConformantEDIWarning` instead of Python's `SyntaxWarning`
- `Parser(directory=...)` pointing outside the package raises `ValueError` instead of a misleading warning
- `Interchange.get_messages()` reports "no message found" instead of an unclosed UNH when there is no UNH at all
- `mypy pydifact` is clean and enforced in CI; `Segment.schema`/`CompositeDataElement.schema` have honest types
- `v4.InterchangeSenderInternalSubIdentification` now subclasses `DataElement`; `v1` C080/C082 schemas use tuples
- `DataElement`/`CompositeDataElement.validate()` use explicit checks (no `assert`) and raise `ValidationError`

[0.2.4] - 2026-10-27
- Mistakenly released as a patch version; same content as 0.3.0

[0.2.3]
- Update dependencies (recommendations from dependabot)
- migrate toolchain to uv

[0.2.2] - 2026-04-10
### Fixed
- Fix regression when no segments.xml is present for the used EDIFACT directory. Print a warning instead of raising an exception.

[0.2.1] - 2026-03-28
### Fixed
- don't write trailing empty elements (colons) at end of composite data elements

[0.2.0] - UNRELEASED
### CHANGES
- BREAKING CHANGE: Remove SegmentCollection
- BREAKING CHANGE: Remove FileSourcableMixin
- BREAKING CHANGE: Segment() calls *must* provide the tag name now as the first parameter.
- BREAKING CHANGE: Parser cannot override syntax_version and syntax_identifier anymore. It is determined from the UNB header.
- change plugin system from `metaclass` to `__init_subclass__`
- raise ValidationError, not AssertionError, when ServiceAdviceString is not 6 chars long
- Drop support for Python versions < 3.10 (3.8 was EOL 2024-10-07, 3.9 not much used in Distros.)

### ADDED
- EDED, EDCD, EDMD, EDSD, UNCL, UNSL parsers and zip extraction logic for automated EDI schema generation
- massively improve type annotations (thanks Tammo Ippen)
- use code-based structures to validate segments and data elements
- improve error output when EDIFACT syntax errors are found
- Implement automatic detection and validation of EDIFACT syntax version (1 - 4) by examining the UNB segment for proper version control and adherence to version-specific syntax rules.
- provide line numbers/columns in EdiFactSyntaxError exceptions

[0.1.9]
### CHANGES
- BREAKING CHANGE (possibly): Characters can be set up with reserved character now. If anyone used args instead of kwargs, this could lead to problems as the 2nd last parameter now is "reserved". But I suppose this will not harm anyone's implementations.

### FIXES
- Token creation with the wrong type fixed
- raise Error when "escaped newline" occurs

[0.1.8]
- allow parsing EDI files created with SAGE COALA (with a "header" before the UNA segment)

[0.1.7]
- TODO

[0.1.6] - 2023-04-22
- Fix Parser drops UNA Segments while converting tokens to segments #56
- Apply fixes for Segmentfactory and Pluginmount #54

[0.1.5] - 2022-01-24
- fix compatibility with Python <3.9
 
[0.1.4] - 2021-12-14
- fix compatibility with Python 3.10

[0.1.3] - 2021-11-03
- Fix multi-message interchange parsing (bug #43)
- Fix correct handling of UNT segments (bug #44)
- Add validation to AbstractSegmentsCollection

[0.1.2] - 2021-10-25
- Fix parsing of colon at line endings
- Fix multi-message interchange parsing

[0.1.1] - 2021-06-27
- fix missing pydifact.syntax package

[0.1] - 2021-06-27
- Add a `split_by(tag_name)` helper to manually split segment collections

[0.0.6] - 2021-04-06
- Deprecate SegmentCollection in favour of Interchange
- Add Interchange and Message semantic and featured classes
- Add an optional predicate filter to `get_segment` and `get_segments` methods
- Allow to access AbstractSegmentsContainer elements using `container[i]`

[0.0.5] - 2020-04-29
- corrected pypi details

[0.0.4] - 2020-04-27
- First release
