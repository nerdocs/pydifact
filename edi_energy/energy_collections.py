from typing import Callable, Generator, Iterable, List, Optional, Tuple, Union

from .energy_segments import IDE, EDISegment, LIN, CCI
from .segmentcollection import AbstractSegmentsContainer


class EnergySegmentsContainer(AbstractSegmentsContainer):

    segments: List[EDISegment]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def get_segments(
    #     self, name: str, predicate: Callable[[EDISegment], bool] = None
    # ) -> Generator[EDISegment, None, None]:
    #     """Get all the segments that match the requested name.

    #     :param name: The name of the segments to return
    #     :param predicate: Optional predicate callable that returns True if the given segment matches a condition
    #     :rtype: list of Segment
    #     """
    #     for segment in self.segments:
    #         if segment.tag == name and (predicate is None or predicate(segment)):
    #             yield segment

    # def get_segment(
    #     self, name: str, predicate: Callable[[EDISegment], bool] = None
    # ) -> Optional[EDISegment]:
    #     """Get the first segment that matches the requested name.

    #     :return: The requested segment, or None if not found
    #     :param name: The name of the segment to return
    #     :param predicate: Optional predicate that must match on the segments
    #        to return
    #     """
    #     super().get_segment(name, predicate)

    def get_first_index(
        self, name: str, predicate: Callable[[EDISegment], bool] = None, flag: str = ""
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

    def split_by(
        self,
        start_segment_tag: str,
        end_segment_tag: Union[str, Tuple[str, Union[str, int]]] = None,
        start_segment_flag: str = "",
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

                # qualifier is given...
                if (
                    start_segment_flag
                    and EDISegment(segment).qualifier == start_segment_flag
                ):

                    if current_list:
                        yield current_list
                    current_list = EnergySegmentsContainer.from_segments([segment])

                elif not start_segment_flag:

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

    @classmethod
    def from_segments(cls, segments: list or Iterable) -> "EnergySegmentsContainer":
        """Create a new EnergySegmentsContainer instance from a iterable list of segments.

        :param segments: The segments of the EDI interchange
        :type segments: list/iterable of Segment
        """

        # create a new instance of EnergySegmentsContainer and return it
        # with the added segments
        return cls().add_segments(segments)


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
