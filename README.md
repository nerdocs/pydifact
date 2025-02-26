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

However, it is not stable yet, so the pypi version, including documentation and code examples, could differ from the latest git code. If in doubt, use the git version:
```bash
git clone https://github.com/nerdocs/pydifact.git
cd pydifact
pip install -e .
```


## Usage

To read a full Interchange from a file or string, take the `Interchange` class and
iter over the messages and segments:

```python
from pydifact.segmentcollection import Interchange

interchange = Interchange.from_file("./tests/data/wikipedia.edi")
interchange = Interchange.from_str(
    "UNA:+,? '"
    "UNB+UNOC:1+1234+3333+200102:2212+42'"
    "UNH+42z42+PAORES:93:1:IA'"
    "MSG+1:45'"
    "IFT+3+XYZCOMPANY AVAILABILITY'"
    "ERC+A7V:1:AMD'"
    "UNT+5+42z42'UNZ+2+42'"
)
for message in interchange.get_messages():
    for segment in message.segments:
        print("Segment tag: {}, content: {}".format(segment.tag, segment.elements))
```

You may also want to iterate directly on segments :

```python
from pydifact.segmentcollection import Interchange

interchange = Interchange.from_str(
    "UNA:+,? '"
    "UNB+UNOC:1+1234+3333+200102:2212+42'"
    "UNH+42z42+PAORES:93:1:IA'"
    "MSG+1:45'"
    "IFT+3+XYZCOMPANY AVAILABILITY'"
    "ERC+A7V:1:AMD'"
    "UNT+5+42z42'UNZ+2+42'"
)

for segment in interchange.segments:
    print("Segment tag: {}, content: {}".format(segment.tag, segment.elements))
```

Or you can create an EDI interchange on the fly:

```python
from pydifact.segmentcollection import Interchange
from pydifact.segments import Segment

interchange = Interchange(syntax_identifier=("IBMA",1),
                          sender="MeMyselfAndIrene",
                          recipient="TheOtherOne",
                          control_reference="KLuzs7c6")
interchange.add_segment(Segment("QTY", ["12", "3"]))

print(interchange.serialize())
```

To include or override the Service String Advice segment (`UNA`), just specify it as a regular segment:

```python
interchange.add_segment(Segment("UNA", ":+.? '"))
```

You may also want to parse a « raw » segment bunch which is not an interchange:

```python
from pydifact.segmentcollection import RawSegmentCollection

collection = RawSegmentCollection.from_str("UNH+1+ORDERS:D:96A:UN:EAN008'")

for segment in collection.segments:
    print("Segment tag: {}, content: {}".format(segment.tag, segment.elements))
```


## Limitations

- No support of optional functional groups (`UNG`→`UNE`),

## Alternatives

In python ecosystem:

- [python-edifact](https://github.com/FriedrichK/python-edifact) - simpler, IMHO less cleaner code, less flexible. may be faster though (not tested). Seems unmaintained.
- [bots](https://github.com/bots-edi/bots) - huge, with webinterface (bots-monitor), webserver, bots-engine.
- [edicat](https://github.com/notpeter/edicat) - simple, only for separating lines/segments for CLI-piping.

## Development

### Setup

To develop pydifact, clone the repository and install the dev requirements:

```bash
make dev
# or 
# pip install -e .[dev]
```

This installs all the python packages needed for development and testing.

### Code formatting

Format all python files using [black](https://black.readthedocs.io) before committing.

Happy coding, PR are more than welcome to make this library better, or to add a feature that matches your needs.
Nevertheless, don't forget adding tests for every aspect you add in code.

### Testing

pydifact uses [pytest](http://pytest.org) for testing. There is a shortcut in the Makefile for your convenience:

```bash
make test
```

This is recommended for faster testing.


There are some additional tests to check the performance of parsing huge files - you can include that tests by calling

```bash
make test-extended
```

## Credits
The official formats for UN/EDIFAT provided by UN Secretariat are raw text files located [here](http://www.unece.org/tradewelcome/un-centre-for-trade-facilitation-and-e-business-uncefact/outputs/standards/unedifact/directories/download.html) and html (.htm) files located [here](http://www.unece.org/tradewelcome/un-centre-for-trade-facilitation-and-e-business-uncefact/outputs/standards/unedifact/directories/2011-present.html), similarly for service codes as text and html files located at https://www.gefeg.com/jswg/.


## License

This library is licensed under the
*MIT* license, see the
[LICENSE file](LICENSE).
