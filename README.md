# pydifact

A Python library to parse and serialize UN/EDIFACT messages.

## Preamble

This is a port of [metroplex-systems/edifact](https://github.com/metroplex-systems/edifact) to Python. Thanks here at the start to [Craig Duncan](https://github.com/duncan3dc) for this cool piece of software. Porting was like a breeze due to the high code quality there. All credits for the initial code here go to him, I just did the translation to Python(3), some "pythonifications" of the code and little improvements.

### Why another EDIFACT library?

Because I did not find a decent UN/EDIFACT library for Python, so I decided to port one of the available good PHP libraries to Python. Here is the result.

ATM this is a Work In Progress, the API is not stable yet.
Feel free to help.

## Usage

To read a message from a file or from a string, take the `Message` class and
iter over the segments:

```python
from pydifact.message import Message
message = Message.from_file("./tests/data/order.edi")
message = Message.from_str("UNA:+,? 'UNH+1+ORDERS:D:96A:UN:EAN008'")

for segment in message.segments:
    print('Segment tag: {}, content: {}'.format(
        segment.tag, segment.elements))
```

Or you can create an EDI message:

```python
from pydifact.message import Message
from pydifact.segments import Segment
message = Message()
message.add_segment(Segment('QTY', ['12', '3']))
print(message.serialize())
```
## Development

To develop pydifact, install the dev requirements with `pipenv install --dev`. This installs all python packages needed for development and testing.

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
