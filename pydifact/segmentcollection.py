# Pydifact - a python edifact library
#
# Copyright (c) 2019 Christian González
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import collections
from typing import Callable, List, Optional, Tuple, Union
import datetime
import warnings

from pydifact.api import EDISyntaxError
from pydifact.parser import Parser
from pydifact.segments import Segment
from pydifact.serializer import Serializer
from pydifact.control import Characters
import codecs


class AbstractSegmentsContainer:
    """Represent a collection of EDI Segments for both reading and writing."""

    def __init__(self, extra_header_elements: List[Union[str, List[str]]] = []):
        """
        :param extra_header_elements: a list of elements to be appended at the end
          of the header segment (same format as Segment() constructor *elements).
        """

        # The segments that make up this message
        self.segments = []
        self.characters = Characters()

        self.extra_header_elements = extra_header_elements

        # Flag whether the UNA header is present
        self.has_una_segment = False

    @classmethod
    def from_str(cls, string: str) -> "SegmentCollection":
        """Create a SegmentCollection instance from a string.
        :param string: The EDI content
        """
        segments = Parser().parse(string)

        return cls.from_segments(segments)

    @classmethod
    def from_segments(
        cls, segments: list or collections.Iterable
    ) -> "AbstractSegmentsContainer":
        """Create a new AbstractSegmentsContainer instance from a iterable list of segments.

        :param segments: The segments of the EDI interchange
        :type segments: list/iterable of Segment
        """

        # create a new instance of AbstractSegmentsContainer and return it
        # with the added segments
        return cls().add_segments(segments)

    def get_segments(
        self, name: str, predicate: Callable[[Segment], bool] = None
    ) -> list:
        """Get all the segments that match the requested name.

        :param name: The name of the segments to return
        :param predicate: Optional predicate callable that returns True if the given segment matches a condition
        :rtype: list of Segment
        """
        for segment in self.segments:
            if segment.tag == name and (predicate is None or predicate(segment)):
                yield segment

    def get_segment(
        self, name: str, predicate: Callable[[Segment], bool] = None
    ) -> Optional[Segment]:
        """Get the first segment that matches the requested name.

        :return: The requested segment, or None if not found
        :param name: The name of the segment to return
        :param predicate: Optional predicate that must match on the segments
           to return
        """
        for segment in self.get_segments(name, predicate):
            return segment

        return None

    def add_segments(
        self, segments: List[Segment] or collections.Iterable
    ) -> "AbstractSegmentsContainer":
        """Add multiple segments to the collection. Passing a UNA segment means setting/overriding the control
        characters and setting the serializer to output the Service String Advice. If you wish to change the control
        characters from the default and not output the Service String Advice, change self.characters instead,
        without passing a UNA Segment.

        :param segments: The segments to add
        :type segments: list or iterable of Segments
        """
        for segment in segments:
            self.add_segment(segment)

        return self

    def add_segment(self, segment: Segment) -> "AbstractSegmentsContainer":
        """Append a segment to the collection.

        :param segment: The segment to add
        """
        self.segments.append(segment)
        return self

    def get_header_segment(self) -> Optional[Segment]:
        """Craft and return this container header segment (if any)

        :returns: None if there is no header for that container
        """
        return None

    def get_footer_segment(self) -> Optional[Segment]:
        """Craft and return this container footer segment (if any)
        :returns: None if there is no footer for that container
        """
        return None

    def serialize(self, break_lines: bool = False) -> str:
        """Serialize all the segments added to this object.
        :param break_lines: if True, insert line break after each segment terminator.
        """
        header = self.get_header_segment()
        footer = self.get_footer_segment()
        out = []

        if header:
            out.append(header)
        out += self.segments
        if footer:
            out.append(footer)

        return Serializer(self.characters).serialize(
            out,
            self.has_una_segment,
            break_lines,
        )

    def __str__(self) -> str:
        """Allow the object to be serialized by casting to a string."""
        return self.serialize()


class FileSourcableMixin:
    """
    For backward compatibility

    For v0.2 drop this class and move from_file() to Interchange class.
    """

    @classmethod
    def from_file(cls, file: str, encoding: str = "iso8859-1") -> "FileSourcableMixin":
        """Create a Interchange instance from a file.

        Raises FileNotFoundError if filename is not found.
        :param encoding: an optional string which specifies the encoding. Default is "iso8859-1".
        :param file: The full path to a file that contains an EDI message.
        :rtype: FileSourcableMixin
        """
        # codecs.lookup raises an LookupError if given codec was not found:
        codecs.lookup(encoding)

        with open(file, encoding=encoding) as f:
            collection = f.read()
        return cls.from_str(collection)


class UNAHandlingMixin:
    """
    For backward compatibility

    For v0.2 drop this class and move add_segment() to Interchange class.
    """

    def add_segment(self, segment: Segment) -> "UNAHandlingMixin":
        """Append a segment to the collection. Passing a UNA segment means setting/overriding the control
        characters and setting the serializer to output the Service String Advice. If you wish to change the control
        characters from the default and not output the Service String Advice, change self.characters instead,
        without passing a UNA Segment.

        :param segment: The segment to add
        """
        if segment.tag == "UNA":
            self.has_una_segment = True
            self.characters = Characters.from_str(segment.elements[0])
            return self
        return super().add_segment(segment)


class SegmentCollection(
    FileSourcableMixin, UNAHandlingMixin, AbstractSegmentsContainer
):
    """
    For backward compatibility. Drop it in v0.2

    Will be replaced by Interchange or RawSegmentCollection depending on the need.
    """

    def __init__(self, *args, **kwargs):
        warnings.warn(
            "SegmentCollection is deprecated and will no longer be available in v0.2, "
            "replace it with Interchange or RawSegmentCollection",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)

    @classmethod
    def from_file(cls, *args, **kwargs) -> "SegmentCollection":
        warnings.warn(
            "SegmentCollection.from_file will be removed in v0.2, "
            "Use Interchange class instead",
            DeprecationWarning,
        )
        return super().from_file(*args, **kwargs)

    def add_segment(self, segment: Segment) -> "SegmentCollection":
        if segment.tag == "UNA":
            warnings.warn(
                "SegmentCollection will be removed in v0.2, "
                "For UNA handling, use Interchange class instead",
                DeprecationWarning,
            )
        return super().add_segment(segment)


class RawSegmentCollection(AbstractSegmentsContainer):
    """
    A way to analyze arbitrary bunch of edifact segments.

    Similar to the deprecated SegmentCollection, but lacking from_file() and UNA support.

    If you are handling an Interchange or a Message, you may want to prefer
    those classes to RawSegmentCollection, as they offer more features and
    checks.
    """

    pass


class Message(AbstractSegmentsContainer):
    """
    A message (started by UNH segment, ended by UNT segment)

    Optional features of UNH are not yet supported.

    https://www.stylusstudio.com/edifact/40100/UNH_.htm
    https://www.stylusstudio.com/edifact/40100/UNT_.htm
    """

    def __init__(self, reference_number: str, identifier: Tuple, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reference_number = reference_number
        self.identifier = identifier

    @property
    def type(self) -> str:
        return self.identifier[0]

    @property
    def version(self) -> str:
        """
        Gives version number and release number.

        :return: message version, parsable by pkg_resources.parse_version()
        """
        return "{}.{}".format(self.identifier[1], self.identifier[2])

    def get_header_segment(self) -> Segment:
        return Segment(
            "UNH",
            self.reference_number,
            [str(i) for i in self.identifier],
            *self.extra_header_elements,
        )

    def get_footer_segment(self) -> Segment:
        return Segment(
            "UNT",
            self.reference_number,
            str(len(self.segments)),
        )


class Interchange(FileSourcableMixin, UNAHandlingMixin, AbstractSegmentsContainer):
    """
    An interchange (started by UNB segment, ended by UNZ segment)

    Optional features of UNB are not yet supported.

    Functional groups are not yet supported

    Messages are supported, see get_message() and get_message(), but are
    optional: interchange segments can be accessed without going through
    messages.

    https://www.stylusstudio.com/edifact/40100/UNB_.htm
    https://www.stylusstudio.com/edifact/40100/UNZ_.htm
    """

    def __init__(
        self,
        sender: str,
        recipient: str,
        control_reference: str,
        syntax_identifier: Tuple[str, int],
        delimiters: Characters = Characters(),
        timestamp: datetime.datetime = None,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.sender = sender
        self.recipient = recipient
        self.control_reference = control_reference
        self.syntax_identifier = syntax_identifier
        self.delimiters = delimiters
        self.timestamp = timestamp or datetime.datetime.now()

    def get_header_segment(self) -> Segment:
        return Segment(
            "UNB",
            [str(i) for i in self.syntax_identifier],
            self.sender,
            self.recipient,
            ["{:%y%m%d}".format(self.timestamp), "{:%H%M}".format(self.timestamp)],
            self.control_reference,
            *self.extra_header_elements,
        )

    def get_footer_segment(self) -> Segment:
        return Segment(
            "UNZ",
            str(len(self.segments)),
            self.control_reference,
        )

    def get_messages(self) -> List[Message]:
        message = None
        for segment in self.segments:
            if segment.tag == "UNH":
                if not message:
                    message = Message(segment.elements[0], segment.elements[1])
                else:
                    raise EDISyntaxError(
                        "Missing UNT segment before new UNH: {}".format(segment)
                    )
            elif segment.tag == "UNT":
                if message:
                    yield message
                else:
                    raise EDISyntaxError(
                        'UNT segment without matching UNH: "{}"'.format(segment)
                    )
            else:
                if message:
                    message.add_segment(segment)

    def add_message(self, message: Message) -> "Interchange":
        segments = (
            [message.get_header_segment()]
            + message.segments
            + [message.get_footer_segment()]
        )
        self.add_segments(i for i in segments if i is not None)
        return self

    @classmethod
    def from_segments(cls, segments: list or collections.Iterable) -> "Interchange":
        segments = iter(segments)

        first_segment = next(segments)
        if first_segment.tag == "UNA":
            unb = next(segments)
        elif first_segment.tag == "UNB":
            unb = first_segment
        else:
            raise EDISyntaxError("An interchange must start with UNB or UNA and UNB")
        # Loosy syntax check :
        if len(unb.elements) < 4:
            raise EDISyntaxError("Missing elements in UNB header")

        datetime_str = "-".join(unb.elements[3])
        timestamp = datetime.datetime.strptime(datetime_str, "%y%m%d-%H%M")
        interchange = Interchange(
            syntax_identifier=unb.elements[0],
            sender=unb.elements[1],
            recipient=unb.elements[2],
            timestamp=timestamp,
            control_reference=unb.elements[4],
        )

        if first_segment.tag == "UNA":
            interchange.has_una_segment = True
            interchange.characters = Characters.from_str(first_segment.elements[0])

        return interchange.add_segments(
            segment for segment in segments if segment.tag != "UNZ"
        )
