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

import codecs
import datetime
import warnings
from collections.abc import Callable, Iterable
from typing import List, Optional, Tuple, Union

from pydifact.api import EDISyntaxError
from pydifact.control import Characters
from pydifact.parser import Parser
from pydifact.segments import Segment
from pydifact.serializer import Serializer


class AbstractSegmentsContainer:
    """Represent a collection of EDI Segments for both reading and writing.

    You should not instantiate AbstractSegmentsContainer itself, but subclass it use that.

    The segments list in AbstractSegmentsContainer includes header and footer segments too.
    Inheriting envelopes must NOT include these elements in .segments, as get_header_element() and
    get_footer_element() should provide these elements on-the-fly.

    Inheriting classes must set HEADER_TAG and FOOTER_TAG
    """

    HEADER_TAG: str = None
    FOOTER_TAG: str = None

    def __init__(self, extra_header_elements: List[Union[str, List[str]]] = None):
        """
        :param extra_header_elements: a list of elements to be appended at the end
          of the header segment (same format as Segment() constructor *elements).
        """

        # The segments that make up this message
        self.segments = []
        self.characters = Characters()

        self.extra_header_elements = (
            extra_header_elements if extra_header_elements else []
        )

        # Flag whether the UNA header is present
        self.has_una_segment = False

    @classmethod
    def from_str(cls, string: str) -> "AbstractSegmentsContainer":
        """Create an instance from a string.

        This method is intended for usage in inheriting classes, not it AbstractSegmentsContainer itself.
        :param string: The EDI content
        """
        segments = Parser().parse(string)

        return cls.from_segments(segments)

    @classmethod
    def from_segments(
        cls, segments: Union[List, Iterable]
    ) -> "AbstractSegmentsContainer":
        """Create a new AbstractSegmentsContainer instance from a iterable list of segments.

        :param segments: The segments of the EDI interchange
        :type segments: list/iterable of Segment
        """

        # create a new instance of AbstractSegmentsContainer and return it
        # with the added segments
        return cls().add_segments(segments)

    def get_segments(
        self,
        name: str,
        predicate: Callable = None,  # Python3.9+ Callable[[Segment], bool]
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
        self,
        name: str,
        predicate: Callable = None,  # Python3.9+ Callable[[Segment], bool]
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

    def split_by(
        self,
        start_segment_tag: str,
    ) -> Iterable:  # Python3.9+ Iterable["RawSegmentCollection"]
        """Split a segment collection by tag.

        Everything before the first start segment is ignored, so if no matching
        start segment is found at all, returned result is empty.


        :param start_segment_tag:
          the segment tag we want to use as separator

        :return: generator of segment collections. The start tag is included in
          each yielded collection
        """
        current_list = None

        for segment in self.segments:
            if segment.tag == start_segment_tag:
                if current_list:
                    yield current_list
                current_list = RawSegmentCollection.from_segments([segment])
            else:
                if current_list is not None:
                    current_list.add_segment(segment)
                else:
                    continue  # we are not yet inside a group
        if current_list is not None:
            yield current_list

    def add_segments(
        self, segments: Union[List[Segment], Iterable]
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

        Note: skips segments that are header oder footer tags of this segment container type.
        :param segment: The segment to add
        """
        if not segment.tag in (self.HEADER_TAG, self.FOOTER_TAG):
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

    def validate(self):
        """Validates this container.

        This method must be overridden in implementing subclasses, and should make sure that
        the container is implemented correctly.

        It does not return anything and should raise an Exception in case of errors.
        """
        raise NotImplementedError

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

    def validate(self):
        """This is just a stub method, no validation done here."""
        pass


class Message(AbstractSegmentsContainer):
    """
    A message (started by UNH segment, ended by UNT segment)

    Optional features of UNH are not yet supported.

    https://www.stylusstudio.com/edifact/40100/UNH_.htm
    https://www.stylusstudio.com/edifact/40100/UNT_.htm
    """

    HEADER_TAG = "UNH"
    FOOTER_TAG = "UNT"

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
            self.HEADER_TAG,
            self.reference_number,
            [str(i) for i in self.identifier],
            *self.extra_header_elements,
        )

    def get_footer_segment(self) -> Segment:
        return Segment(
            self.FOOTER_TAG,
            str(len(self.segments) + 2),
            self.reference_number,
        )

    def validate(self):
        """Validates the message.

        :raises EDISyntaxError in case of syntax errors in the segments
        """

        pass


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

    HEADER_TAG = "UNB"
    FOOTER_TAG = "UNZ"

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
            self.HEADER_TAG,
            [str(i) for i in self.syntax_identifier],
            self.sender,
            self.recipient,
            ["{:%y%m%d}".format(self.timestamp), "{:%H%M}".format(self.timestamp)],
            self.control_reference,
            *self.extra_header_elements,
        )

    def get_footer_segment(self) -> Segment:
        """:returns a (UNZ) footer segment with correct segment count and control reference.

        It counts either of the number of messages or, if used, of the number of functional groups
        in an interchange (TODO)."""

        # FIXME: count functional groups (UNG/UNE) correctly
        cnt = 0
        for segment in self.segments:
            if segment.tag == Message.HEADER_TAG:
                cnt += 1
        if cnt == 0:
            cnt = len(self.segments)

        return Segment(
            self.FOOTER_TAG,
            str(cnt),
            self.control_reference,
        )

    def get_messages(self) -> List[Message]:
        """parses a list of messages out of the internal segments.

        :raises EDISyntaxError if constraints are not met (e.g. UNH/UNT both correct)

        TODO: parts of this here are better done in the validate() method
        """

        message = None
        last_segment = None
        for segment in self.segments:
            if segment.tag == "UNH":
                if not message:
                    message = Message(segment.elements[0], segment.elements[1])
                    last_segment = segment
                else:
                    raise EDISyntaxError(
                        "Missing UNT segment before new UNH: {}".format(segment)
                    )
            elif segment.tag == "UNT":
                if message:
                    yield message
                    message = None
                    last_segment = segment
                else:
                    raise EDISyntaxError(
                        'UNT segment without matching UNH: "{}"'.format(segment)
                    )
            else:
                if message:
                    message.add_segment(segment)
                last_segment = segment
        if last_segment:
            if not last_segment.tag == "UNT":
                raise EDISyntaxError("UNH segment was not closed with a UNT segment.")

    def add_message(self, message: Message) -> "Interchange":
        segments = (
            [message.get_header_segment()]
            + message.segments
            + [message.get_footer_segment()]
        )
        self.add_segments(i for i in segments if i is not None)
        return self

    @classmethod
    def from_segments(cls, segments: Union[list, Iterable]) -> "Interchange":
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

        # In syntax version 3 the year is formatted using two digits, while in version 4 four digits are used.
        # Since some EDIFACT files in the wild don't adhere to this specification, we just use whatever format seems
        # more appropriate according to the length of the date string.
        if len(unb.elements[3][0]) == 6:
            datetime_fmt = "%y%m%d-%H%M"
        elif len(unb.elements[3][0]) == 8:
            datetime_fmt = "%Y%m%d-%H%M"
        else:
            raise EDISyntaxError("Timestamp of file-creation malformed.")

        datetime_str = "-".join(unb.elements[3])
        timestamp = datetime.datetime.strptime(datetime_str, datetime_fmt)
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

        return interchange.add_segments(segments)

    def validate(self):
        # TODO: proper validation
        pass
