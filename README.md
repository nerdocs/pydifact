# pydifact

A Python library to parse and serialize UN/EDIFACT interchanges.

## Preamble

This is a port of [metroplex-systems/edifact](https://github.com/metroplex-systems/edifact) to Python. Thanks here at the start to [Craig Duncan](https://github.com/duncan3dc) for this cool piece of software. Porting was like a breeze due to the high code quality there. All credits for the initial code here go to him, I just did the translation to Python(3), some "pythonifications" of the code and little improvements.

### Why another EDIFACT library?

Because I did not find a decent UN/EDIFACT library for Python, so I decided to port one of the available good PHP libraries to Python. Here is the result.

ATM this is a Work In Progress, the API is not stable yet.
Feel free to help.

## Install

As usual, use a virtualenv, and install via pip or pipenv:

```bash
pip install pydifact
```

However, it is not stable yet, so the pypi version, including documentation an dcode examples, could differ from the latest git code. If in doubt, use the git version:
```bash
git clone https://github.com/nerdocs/pydifact.git
cd pydifact
pip install -e .
```


## Usage

To read a message from a file or from a string, take the `SegmentsCollection` class and
iter over the segments:

```python
from pydifact.segmentcollection import SegmentCollection
collection = SegmentCollection.from_file("./tests/data/order.edi")
collection = SegmentCollection.from_str("UNA:+,? 'UNH+1+ORDERS:D:96A:UN:EAN008'")

for segment in collection.segments:
    print('Segment tag: {}, content: {}'.format(
        segment.tag, segment.elements))
```

Or you can create an EDI interchange on the fly:

```python
from pydifact.segmentcollection import SegmentCollection
from pydifact.segments import Segment
collection = SegmentCollection()
collection.add_segment(Segment('QTY', ['12', '3']))
print(collection.serialize())
```

## Limitations

- No support of high-level EDIFACT containers : Interchange (`UNA`+`UNB`→`UNZ`), Messages (`UNH`/`UNT`), and optional functional groups (`UNG`→`UNE`),
- No support for data encoded with something else than *ISO-8859*

## Alternatives

In python ecosystem:

- [python-edifact](https://github.com/FriedrichK/python-edifact) - simpler, IMHO less cleaner code, less flexible. may be faster though (not tested). Seems unmaintained.
- [bots](https://github.com/bots-edi/bots) - huge, with webinterface (bots-monitor), webserver, bots-engine.
- [edicat](https://github.com/notpeter/edicat) - simple, only for separating lines/segments for CLI-piping.


## Development

To develop pydifact, install the dev requirements with `pipenv install --dev`. This installs all the python packages needed for development and testing.

Format all python files using [black](https://black.readthedocs.io).

Happy coding, PR are more than welcome to make this library better, or to add a feature that matches your needs. Nevertheless, don't forget adding tests for every aspect you add in code.

### Testing

pydifact uses [pytest](http://pytest.org) for testing.
Just exec `pytest` within the project folder to execute the unit tests.

There is one test to check the performance of parsing huge files, named `test_huge_message` - you can skip that test by calling

```bash
pytest --ignore tests/test_huge_message.py
```
This is recommended for fast testing.


## License

This library is licensed under the
*MIT* license, see the
[LICENSE file](LICENSE).
