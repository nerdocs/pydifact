# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


[0.2] - UNRELEASED
### CHANGES
- BREAKING CHANGE: Remove SegmentCollection
- BREAKING CHANGE: Remove FileSourcableMixin
- BREAKING CHANGE: Segment() calls *must* provide the tag name now as the first parameter.
- change plugin system from `metaclass` to `__init_subclass__`
- raise ValidationError, not AssertionError, when ServiceAdviceString is not 6 chars long
### ADDED
- massively improve type annotations (thanks Tammo Ippen)
- use code-based structures to validate segments and data elements
- improve error output when EDIFACT syntax errors are found
- Implement automatic detection and validation of EDIFACT syntax version (1 - 4) by examining the UNB segment for proper version control and adherence to version-specific syntax rules.
- provide line numbers/columns in EdiFactSyntaxError exceptions

[0.1.9]
### CHANGES
- BREAKING CHANGE (possibly): Characters can be set up with reserved character now. If anyone used args instead of kwargs, this could lead to problems as the 2nd last parameter now is "reserved". But I suppose this not harm anyone's implementations.

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
