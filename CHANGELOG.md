Changelog for PYDIFACT


[0.2] - UNRELEASED
- BREAKING CHANGE: Remove SegmentCollection
- BREAKING CHANGE: Remove FileSourcableMixin

[0.1.5] - 2022-01-24
- fix compatibility with Python <3.9
- 
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
