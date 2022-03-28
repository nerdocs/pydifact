from typing import Callable, Generator, Iterable, List, Optional, Tuple, Union

from edi_energy.energy_segments import IDE, EDISegment, LIN, CCI, choose_segment_from_catalog
from pydifact.segmentcollection import AbstractSegmentsContainer, Interchange, Message

from pydifact.control import Characters
from pydifact.segments import Segment
from pydifact.parser import Parser
import codecs

import datetime

# from .energy_segments import EDISegment as Segment

# Segment = EDISegment


class EnergySegmentsContainer(AbstractSegmentsContainer):
    """Represent a collection of EDI@energy segments for both reading and writing.

    You should not instantiate EnergySegmentsContainer itself, but subclass it and use that.

    The segments list in AbstractSegmentsContainer includes header and footer segments too.
    Inheriting envelopes must NOT include these elements in .segments, as get_header_element() and
    get_footer_element() should provide these elements on-the-fly.

    Inheriting classes must set HEADER_TAG and FOOTER_TAG
    """

    segments: List[EDISegment]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_first_index(
        self, name: str, predicate: Callable[[EDISegment], bool] = None
    ) -> int:
        """Get all the segments that match the requested name.

        :param name: The name of the segments to return
        :param predicate: Optional predicate callable that returns True if the given segment matches a condition
        :rtype: list of Segment
        """
        for s, segment in enumerate(self.segments):
            if segment.tag == name and (predicate is None or predicate(segment)):
                return s

        return None

    @classmethod
    def from_file(
        cls, file: str, encoding: str = "iso8859-1"
    ) -> "EnergySegmentsContainer":
        """Create a Interchange instance from a file.

        Method was previously in FileSourcableMixin.

        Raises FileNotFoundError if filename is not found.
        :param encoding: an optional string which specifies the encoding. Default is "iso8859-1".
        :param file: The full path to a file that contains an EDI message.
        :rtype: Interchange
        """
        # codecs.lookup raises an LookupError if given codec was not found:
        codecs.lookup(encoding)

        with open(file, encoding=encoding) as f:
            collection = f.read()
        return cls.from_str(collection)

    @classmethod
    def from_str(cls, string: str) -> "EnergySegmentsContainer":
        """Create an instance from a string.

        This method is intended for usage in inheriting classes, not it AbstractSegmentsContainer itself.
        :param string: The EDI content
        """
        segments = Parser().parse(string)

        return cls.from_segments(segments)

    @classmethod
    def from_segments(cls, segments: list or Iterable) -> "EnergySegmentsContainer":
        """Create a new EnergySegmentsContainer instance from a iterable list of segments.

        :param segments: The segments of the EDI interchange
        :type segments: list/iterable of Segment
        """

        # create a new instance of EnergySegmentsContainer and return it
        # with the added segments
        return cls().add_segments(segments)

    def add_segments(
        self, segments: List[EDISegment] or Iterable
    ) -> "EnergySegmentsContainer":
        """Add multiple EDISegments to the collection.

        Passing a UNA segment means setting/overriding the control
        characters and setting the serializer to output the Service String Advice. If you wish to change the control
        characters from the default and not output the Service String Advice, change self.characters instead,
        without passing a UNA Segment.

        :param segments: The segments to add
        :type segments: list or iterable of Segments
        """
        for segment in segments:
            
            if not isinstance(segment, EDISegment):
                segment = choose_segment_from_catalog(segment)
            self.add_segment(segment)

        return self

    def get_segments(
        self, name: str, predicate: Callable[[EDISegment], bool] = None
    ) -> Generator[EDISegment, None, None]:
        """Get all the segments that match the requested name.

        Parameters
        ----------
        name : str
            The name of the segments to return
        predicate : Callable[[Segment], bool], optional
            Optional predicate callable that returns True if the given segment
            matches a condition, by default None
        flag : str, optional
            qualifier to further evaluate segment, must be with keyword,
            by default "", then all segments with name are returned

        Yields
        ------
        Generator[EDISegment, None, None]
            list of Segment
        """
        return super().get_segments(name, predicate)

    def get_segment(
        self,
        name: str,
        predicate: Callable[
            [EDISegment], bool
        ] = None,  # Python3.9+ Callable[[Segment], bool]
    ) -> Optional[Segment]:
        """Get the first segment that matches the requested name.

        :return: The requested segment, or None if not found
        :param name: The name of the segment to return
        :param predicate: Optional predicate that must match on the segments
           to return
        """
        return super().get_segment(name, predicate)

    def get_first_index(
        self, name: str, predicate: Callable[[Segment], bool] = None
    ) -> Optional[int]:
        """Get the index of the first segment that matches the request.

        :param name: The name of the segments to return
        :param predicate: Optional predicate callable that returns True if the given segment matches a condition
        :rtype: int
        """
        for s, segment in enumerate(self.segments):
            if segment.tag == name and (predicate is None or predicate(segment)):
                return s

        return None

    def split_by(
        self,
        start_segment_tag: str,
        end_segment_tag: Union[str, Tuple[str, Union[str, int]]] = None,
    ) -> Generator["EnergySegmentsContainer", None, None]:
        """Split a segment collection by tag.

        Everything before the first start segment is ignored, so if no matching
        start segment is found at all, returned result is empty.

        If an optional end segment is given, all segments between a start segment and end
        segment are present in the split. Segments between the last segment and the next
        start segment will be ignored.


        :param start_segment_tag:
          the segment tag we want to use as separator

        :return: generator of segment collections. The start tag is included in
          each yielded collection
        """
        current_list = None

        # set parameters for end of split
        if end_segment_tag:
            if isinstance(end_segment_tag, tuple):
                end_segment_qual = end_segment_tag[1]
                end_segment_tag = str(end_segment_tag[0])
            else:
                end_segment_qual = None

        for segment in self.segments:
            if segment.tag == start_segment_tag:
                if current_list:
                    yield current_list
                current_list = EnergySegmentsContainer.from_segments([segment])
            else:
                if current_list is not None:
                    current_list.add_segment(segment)

                else:
                    continue  # we are not yet inside a group

            # yield after last segment and reset list
            if end_segment_tag and segment.tag == end_segment_tag:
                if end_segment_qual:
                    if segment[0] == end_segment_qual:
                        yield current_list
                        current_list = None

        if current_list is not None:
            yield current_list


class EDIEnergyMessage(Message, EnergySegmentsContainer):
    """
    A message (started by UNH segment, ended by UNT segment)

    Optional features of UNH are not yet supported.

    `UNH <https://www.stylusstudio.com/edifact/40100/UNH_.htm>`
    `UNT <https://www.stylusstudio.com/edifact/40100/UNT_.htm>`

    """

    def __init__(
        self,
        reference_number: str = "",
        identifier: Tuple = (),
        extra_header_elements: List[Union[str, List[str]]] = None,
        *args,
        **kwargs
    ):
        super().__init__(
            extra_header_elements=extra_header_elements,
            reference_number=reference_number,
            identifier=identifier,
            *args,
            **kwargs
        )

    @classmethod
    def from_message(cls, message: Message):
        edi_message = EDIEnergyMessage()

        for key, val in vars(message).items():
            setattr(edi_message, key, val)

        return edi_message

    def validate(self):
        """Validates the message.

        :raises EDISyntaxError in case of syntax errors in the segments
        """

        pass


class EDIEnergyInterchange(EnergySegmentsContainer, Interchange):
    """
    An interchange (started by UNB segment, ended by UNZ segment)

    Optional features of UNB are not yet supported.

    Functional groups are not yet supported

    Messages are supported, see get_message() and get_message(), but are
    optional: interchange segments can be accessed without going through
    messages.

    `UNB <https://www.stylusstudio.com/edifact/40100/UNB_.htm>`
    `UNZ <https://www.stylusstudio.com/edifact/40100/UNZ_.htm>`
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
        extra_header_elements: List[Union[str, List[str]]] = None,
    ):
        super().__init__(
            extra_header_elements=extra_header_elements,  # if extra_header_elements else [],  # param of AbstractSegmentContainer
            sender=sender,  # inputs of Interchange
            recipient=recipient,
            control_reference=control_reference,
            syntax_identifier=syntax_identifier,
            delimiters=delimiters,
            timestamp=timestamp,
        )

    @classmethod
    def from_interchange(cls, interchange: Interchange) -> "EDIEnergyInterchange":
        """Create an instance from an existing Interchange instance

        Parameters
        ----------
        interchange : Interchange
            object to create instance from

        Returns
        -------
        EDIEnergyInterchange
            new object with equal attributes
        """
        edi_interchange = EDIEnergyInterchange("", "", "", ("", 0))
        for key, val in vars(interchange).items():
            setattr(edi_interchange, key, val)
        return edi_interchange

    def get_messages(self) -> Generator[EDIEnergyMessage, None, None]:
        """Yields the unterlying messages of this interchange.

        Returns
        -------
        _type_
            _description_

        Yields
        ------
        Generator[Message, None, None]
            _description_
        """
        for m in super().get_messages():
            yield EDIEnergyMessage.from_message(m)

    def add_message(self, message: EDIEnergyMessage) -> "EDIEnergyInterchange":
        """Add an EDIenergy message instance to the interchange.

        Parameters
        ----------
        message : EDIEnergyMessage
            message to append

        Returns
        -------
        EDIEnergyInterchange
            self
        """
        return super().add_message(message)

    def add_segment(self, segment: Segment) -> "EDIEnergyInterchange":
        """Append a segment to the collection.

        Passing a UNA segment means setting/overriding the control
        characters and setting the serializer to output the Service String Advice. If you wish to change the control
        characters from the default and not output the Service String Advice, change self.characters instead,
        without passing a UNA Segment.

        Parameters
        ----------
        segment : Segment
            The segment to add

        Returns
        -------
        EDIEnergyInterchange
            self
        """
        return super().add_segment(segment)

    @classmethod
    def from_segments(cls, segments: Union[list, Iterable]) -> "EDIEnergyInterchange":
        """Create an instance from a list of segments.

        Parameters
        ----------
        segments : Union[list, Iterable]
            to create interchange from

        Returns
        -------
        EDIEnergyInterchange

        """
        # cast segments to edi segments
        segments = [choose_segment_from_catalog(s) for s in segments]
        # create base interchange from edi segments and set inherited attributes
        return cls.from_interchange(Interchange.from_segments(segments))

    @classmethod
    def from_file(
        cls, file: str, encoding: str = "iso8859-1"
    ) -> "EDIEnergyInterchange":
        """Creates an instance of EDIEnergyInterchange from a given file.

        Parameters
        ----------
        file : str
            _description_
        encoding : str, optional
            _description_, by default "iso8859-1"

        Returns
        -------
        EDIEnergyInterchange

        """

        return super().from_file(file, encoding)

    def validate(self):
        # TODO: proper validation
        pass


class LINGroup(EnergySegmentsContainer):
    START_TAG = LIN.tag

    @classmethod
    def from_segments(cls, segments: list or Iterable) -> "LINGroup":
        """Create a new instance from a iterable list of segments.

        :param segments: The segments of the EDI interchange
        :type segments: list/iterable of Segment
        """

        # create a new instance of and return it
        # with the added segments
        return cls().add_segments(segments)


class IDEGroup(EnergySegmentsContainer):
    START_TAG = IDE.tag

    @classmethod
    def from_segments(cls, segments: list or Iterable) -> "IDEGroup":
        """Create a new instance from a iterable list of segments.

        :param segments: The segments of the EDI interchange
        :type segments: list/iterable of Segment
        """

        # create a new instance of and return it
        # with the added segments
        return cls().add_segments(segments)


class CCIGroup(EnergySegmentsContainer):
    START_TAG = CCI.tag
    pass
