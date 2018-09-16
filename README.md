## pydifact

A Python library to parse and serialize UN/EDIFACT messages.

#### Preamble

This is a port of [metroplex-systems/edifact](https://github.com/metroplex-systems/edifact) to Python. Thanks here at the start to [Craig Duncan](https://github.com/duncan3dc) for this cool piece of software. Porting was like a breeze due to the high code quality there. All credits for the initial code here go to him, I just did the translation to Python(3), some "pythonifications" of the code and little improvements.

#### Why another EDIFACT library?

Because I did not find a decent UN/EDIFACT library for Python, so I decided to port one of the available good PHP libraries to Python. Here is the result.

ATM this is a Work In Progress, the API is not stable yet.
Feel free to help.

#### Usage

To read a message from a file or from a string, take the `Message` class and
iter over the segments:

```python
from pydifact.Message import Message
message = Message.from_file("./tests/data/order.edi");
message = Message.from_str("UNA:+,? 'UNH+1+ORDERS:D:96A:UN:EAN008'")

for segment in message.segments:
    print('Segment tag: {}, content: {}'.format(
        segment.tag, segment.elements))
```

Or you can create an EDI message:

```python
from pydifact.Segments import Segment
message = Message()
message.add_segment(Segment('QTY', ['12', '3']))
print(message.serialize())
```

#### Testing
pydifact uses unittests for testing.
You can use [nose](https://nose.readthedocs.io/en/latest/) to automate the
tests. Just install the requirements with `pip install -r requirements_dev.txt`
and exec `nosetests` within the project folder.


#### License
This library is licensed under the
![LGPLv3](https://www.gnu.org/graphics/lgplv3-88x31.png) license, see the
[LICENSE file](LICENSE.LGPL.md).
