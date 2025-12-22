# Pydifact - a python edifact library
#
# Copyright (c) 2017-2024 Christian González
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
from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Type, TypeVar

from pydifact.exceptions import EDISyntaxError
from pydifact.control import Characters
from pydifact.parser import Parser
from pydifact.segments import Segment
from pydifact.constants import Element, Elements
from pydifact.serializer import Serializer

T = TypeVar("T", bound="AbstractSegmentsContainer")


class AbstractSegmentsContainer:
    """Abstract base class of subclasses containing collection of segments.

    `AbstractSegmentsContainer` is the superclass of several classes such as
    `RawSegmentCollection` and `Interchange` and contains methods common
    to them.

    **Implementation detail:** Subclasses must set `HEADER_TAG` and
    `FOOTER_TAG`.

    Args:
        extra_header_elements: A list of elements to be appended at the end
            of the header segment (same format as `~pydifact.segments.Segment`
            constructor elements).
        characters: The set of control characters

    Attributes:
        segments: The segments that comprise the container. This does not include the envelope
            (that is, the header and footer) segments. To get the envolope segments, use
            as `get_header_segment` and `get_footer_segment`.

        characters: The control characters (a `~pydifact.control.Characters` object).
    """

    HEADER_TAG: str | None = None
    FOOTER_TAG: str | None = None

    def __init__(
        self,
        extra_header_elements: Elements | None = None,
        characters: Characters | None = None,
    ) -> None:
        self.segments: list[Segment] = []

        # set of control characters
        self.characters = characters or Characters()

        self.extra_header_elements = (
            extra_header_elements if extra_header_elements else []
        )

        # Flag whether the UNA header is present
        self.has_una_segment = False

    @classmethod
    def from_str(
        cls: Type[T],
        string: str,
        parser: Parser | None = None,
        characters: Characters | None = None,
    ) -> T:
        """Create an instance from a string.

        Args:
            string: The EDI content.
            parser: A parser to convert the tokens to segments; defaults to `Parser`.
            characters: The set of control characters.
        """
        if parser is None:
            parser = Parser(characters=characters)

        segments = parser.parse(string)

        return cls.from_segments(segments=segments, characters=parser.characters)

    @classmethod
    def from_segments(
        cls: Type[T],
        segments: Iterable[Segment],
        characters: Characters | None = None,
    ) -> T:
        """Create an instance from a list of segments.

        Args:
            segments: The segments of the EDI interchange (list/iterable of Segment).
            characters: The set of control characters.
        """
        # create a new instance of AbstractSegmentsContainer and return it
        # with the added segments
        res = cls(characters=characters)
        res.add_segments(segments)
        return res

    def get_segments(
        self,
        name: str,
        predicate: Callable[[Segment], bool] | None = None,
    ) -> Iterator[Segment]:
        """Get all segments that match the requested name.

        Args:
            name: The name of the segments to return.
            predicate: Optional callable that accepts a segment as argument.
                Only segments for which the returned value is `True` are returned.

        Yields:
            Segment: Matching segment objects.
        """
        for segment in self.segments:
            if segment.tag == name and (predicate is None or predicate(segment)):
                yield segment

    def get_segment(
        self,
        name: str,
        predicate: Callable[[Segment], bool] | None = None,
    ) -> Segment | None:
        """Get the first segment that matches the requested name.

        Args:
            name: The name of the segment to return.
            predicate: Optional callable that accepts a segment as argument.
                Only segments for which the returned value is `True` are
                considered.

        Returns:
            The requested segment, or None if not found.
        """
        for segment in self.get_segments(name, predicate):
            return segment

        return None

    def split_by(
        self,
        start_segment_tag: str,
    ) -> Iterable["RawSegmentCollection"]:
        """Split the segment collection by tag.

        Assuming the collection contains tags `["A", "B", "A", "A", "B", "D"]`,
        `split_by("A")` would return `[["A", "B"], ["A"], ["A", "B", "D"]]`.
        Everything before the first start segment is ignored, so if no matching start
        segment is found at all, the returned result is empty.

        Args:
            start_segment_tag: The segment tag we want to use as separator.

        Yields:
            Generator of segment collections. The start tag is included in
            each yielded collection.
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

    def add_segments(self, segments: Iterable[Segment]) -> None:
        """Append a list of segments to the collection.

        For the `Interchange` subclass, passing a `UNA` segment means
        setting/overriding the control characters and setting the serializer to output
        the Service String Advice. If you wish to change the control characters from the
        default and not output the Service String Advice, change `characters`
        instead, without passing a `UNA` Segment.

        Args:
            segments: The segments to add.
        """
        for segment in segments:
            self.add_segment(segment)

    def add_segment(self, segment: Segment) -> None:
        """Append a segment to the collection.

        Note: skips segments that are header or footer tags of this segment
        container type.

        Args:
            segment: The segment to add.
        """
        if segment.tag not in (self.HEADER_TAG, self.FOOTER_TAG):
            self.segments.append(segment)

    def get_header_segment(self) -> Segment | None:
        """Craft and return a header segment.

        `get_header_segment` creates and returns an appropriate
        `pydifact.segments.Segment` object that can serve as a header of the
        current object. This is useful, for example, when serializing the current object.

        Although the current object may have been created by reading a string (e.g.
        with `from_str`), `get_header_segment` does not return the header
        segment that was read by the string; that segment would have been useful only
        during reading and it is the job of `from_str` to check it.

        Returns:
            Segment | None: The header segment, or None if not applicable.
        """
        raise NotImplementedError

    def get_footer_segment(self) -> Segment | None:
        """Craft and return a footer segment.

        This is similar to `get_header_segment`, but for the footer segment.
        """
        raise NotImplementedError

    def serialize(self, break_lines: bool = False) -> str:
        """Return the string representation of the object.

        Args:
             break_lines: If `True`, inserts line break after each segment
                terminator. This is forbidden in the EDIFACT specs, but apparently widely
                used.
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

    def validate(self) -> bool:
        """Validate the object.

        Raises an exception if the object is invalid.
        """
        raise NotImplementedError

    def __str__(self) -> str:
        return self.serialize()


class RawSegmentCollection(AbstractSegmentsContainer):
    """
    A way to analyze arbitrary bunch of edifact segments.

    If you are handling an Interchange or a Message, you may want to prefer
    those classes to RawSegmentCollection, as they offer more features and
    checks.
    """

    def get_header_segment(self) -> Segment | None:
        """This is just a stub method."""
        return None

    def get_footer_segment(self) -> Segment | None:
        """This is just a stub method."""
        return None

    def validate(self):
        """This is just a stub method, no validation done here."""
        pass


class Message(AbstractSegmentsContainer):
    """
    A message (started by UNH_ segment, ended by UNT_ segment)

    Optional features of UNH are not yet supported.

    .. _UNH: https://www.stylusstudio.com/edifact/40100/UNH_.htm
    .. _UNT: https://www.stylusstudio.com/edifact/40100/UNT_.htm
    """

    HEADER_TAG = "UNH"
    FOOTER_TAG = "UNT"

    def __init__(
        self, reference_number: str, identifier: Sequence[str], *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.reference_number = reference_number
        self.identifier = list(identifier)

    @property
    def type(self) -> str:
        return self.identifier[0]

    @property
    def version(self) -> str:
        """
        Gives version number and release number.

        :return: message version, parsable by pkg_resources.parse_version()
        """
        return f"{self.identifier[1]}.{self.identifier[2]}"

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


class Interchange(AbstractSegmentsContainer):
    """An EDIFACT interchange.

    In EDIFACT, the **interchange** is the entire document at the highest level. Except
    for its header (a UNB_ segment) and footer (a UNZ_ segment), it consists of one or
    more **messages**.

    `Interchange` currently does not support functional groups and optional
    features of UNB.

    `Interchange` supports all methods of `AbstractSegmentsContainer` plus
    some additional methods.

    .. _UNB: https://www.stylusstudio.com/edifact/40100/UNB_.htm
    .. _UNZ: https://www.stylusstudio.com/edifact/40100/UNZ_.htm
    """

    HEADER_TAG = "UNB"
    FOOTER_TAG = "UNZ"

    def __init__(
        self,
        sender: Element,
        recipient: Element,
        control_reference: Element,
        syntax_identifier: tuple[str, int],
        timestamp: datetime.datetime | None = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.sender = sender
        self.recipient = recipient
        self.control_reference = control_reference
        self.syntax_identifier = syntax_identifier
        self.timestamp = timestamp or datetime.datetime.now()

    def get_header_segment(self) -> Segment:
        return Segment(
            self.HEADER_TAG,
            [self.syntax_identifier[0], str(self.syntax_identifier[1])],
            self.sender,
            self.recipient,
            [f"{self.timestamp:%y%m%d}", f"{self.timestamp:%H%M}"],
            self.control_reference,
            *self.extra_header_elements,
        )

    def get_footer_segment(self) -> Segment:
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

    def get_messages(self) -> Iterator[Message]:
        """Get list of messages in the interchange.

        Using `get_messages` is optional; interchange segments can be accessed
        directly without going through messages.

        Raises:
             `EDISyntaxError` if the interchange contents are not correct.
        """

        message = None
        last_segment = None
        for segment in self.segments:
            if segment.tag == "UNH":
                if not message:
                    assert isinstance(segment.elements[0], str)
                    assert isinstance(segment.elements[1], list)
                    message = Message(segment.elements[0], segment.elements[1])
                    last_segment = segment
                else:
                    raise EDISyntaxError(
                        f"Missing UNT segment before new UNH: segment{segment}"
                    )
            elif segment.tag == "UNT":
                if message:
                    yield message
                    message = None
                    last_segment = segment
                else:
                    raise EDISyntaxError(
                        f'UNT segment without matching UNH: "{segment}"'
                    )
            else:
                if message:
                    message.add_segment(segment)
                last_segment = segment
        if last_segment:
            if not last_segment.tag == "UNT":
                raise EDISyntaxError("UNH segment was not closed with a UNT segment.")

    def add_message(self, message: Message) -> "Interchange":
        """Append a message to the interchange."""
        segments = (
            [message.get_header_segment()]
            + message.segments
            + [message.get_footer_segment()]
        )
        self.add_segments(i for i in segments if i is not None)
        return self

    @classmethod
    def from_file(
        cls, file: str, encoding: str = "iso8859-1", parser: Parser | None = None
    ) -> "Interchange":
        """Create an Interchange instance from a file.

        Args:
            file : str
                The full path to a file that contains an EDI message.
            encoding : str, default='iso8859-1'
                The encoding to use when reading the file.
            parser : Parser, optional
                A parser to convert the tokens to segments.

        Returns:
            Interchange
                A new Interchange instance created from the file contents.

        Raises:
            FileNotFoundError
                If the specified file is not found.
            LookupError
                If the specified encoding is not recognized.
        """
        # codecs.lookup raises an LookupError if given codec was not found:
        codecs.lookup(encoding)

        with open(file, encoding=encoding) as f:
            collection = f.read()
        return cls.from_str(collection, parser=parser)

    @classmethod
    def from_segments(
        cls, segments: Iterable[Segment], characters: Characters | None = None
    ) -> "Interchange":
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
        if isinstance(unb.elements[3], list) and len(unb.elements[3]) > 0:
            if len(unb.elements[3][0]) == 6:
                datetime_fmt = "%y%m%d-%H%M"
            elif len(unb.elements[3][0]) == 8:
                datetime_fmt = "%Y%m%d-%H%M"
            else:
                raise EDISyntaxError("Timestamp of file-creation malformed.")
        else:
            raise EDISyntaxError("Timestamp of file-creation malformed.")

        if (
            isinstance(unb.elements[0], list)
            and len(unb.elements[0]) == 2
            and unb.elements[0][1].isdecimal()
        ):
            syntax_identifier = (unb.elements[0][0], int(unb.elements[0][1]))
        else:
            raise EDISyntaxError("Syntax identifier malformed.")

        datetime_str = "-".join(unb.elements[3])
        timestamp = datetime.datetime.strptime(datetime_str, datetime_fmt)
        interchange = Interchange(
            syntax_identifier=syntax_identifier,
            sender=unb.elements[1],
            recipient=unb.elements[2],
            timestamp=timestamp,
            control_reference=unb.elements[4],
            characters=characters,
            extra_header_elements=unb.elements[5:],
        )

        if first_segment.tag == "UNA" and isinstance(first_segment.elements[0], str):
            interchange.has_una_segment = True
            interchange.characters = Characters.from_str(first_segment.elements[0])

        interchange.add_segments(segments)
        return interchange

    def add_segment(self, segment: Segment) -> None:
        """Append a segment to the collection.

        Passing a UNA segment means setting/overriding the control
        characters and setting the serializer to output the Service String Advice.
        If you wish to change the control characters from the default and not output
        the Service String Advice, change self.characters instead,
        without passing a UNA Segment.

        Args:
             segment: The segment to add
        """
        if segment.tag == "UNA":
            self.has_una_segment = True
            assert isinstance(segment.elements[0], str)
            self.characters = Characters.from_str(segment.elements[0])
            return
        super().add_segment(segment)

    def validate(self):
        # TODO: proper validation
        pass
