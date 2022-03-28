from abc import abstractmethod
from typing import Callable, Union

from pydifact.segments import Segment

from utils.dev import deprecation_warning


class EDISegment(Segment):

    tag: str

    # tag is not a class attribute in this case, as each Segment instance could have another tag.
    __omitted__ = True

    def __init__(self, segment: Union[Segment, str], *args, **kwargs):
        """Constructs an EDISegment instance from a low level Segment instance or given tag and elements

        Parameters
        ----------
        segment : Segment, str
            a Segment instance or a tag, then the elements for this segment must be provided as well

        Exapmle
        -------
        >>> s = Segment("A", "1", "a")
        >>> edi_segment = EDISegment(s)

        or directly with a tag and data elements:
        >>> edi_segment = EDISegment("A", "1", "a")


        """

        if isinstance(segment, Segment):
            for key, val in vars(segment).items():
                setattr(self, key, val)
            return

        super().__init__(segment, *args, **kwargs)

    @property
    def qualifier(self):
        """qualifier aka first value after segment tag

        e.g.
        PIA segment: ['5', ['7-20:3.0.0', 'SRW']],
        QTY segment: [['220', '19813.277']],
        """
        return self[0][0] if isinstance(self[0], list) else self[0]

    # TODO add id interface
    # def get_id():
    #     pass

    def matches(self, qualifier) -> bool:
        return self.qualifier == qualifier

    @abstractmethod
    def get(self):
        """Return the underlying value of this segment.

        Must be implemented in any inheriting classes.
        """

    @classmethod
    def __predicate(cls, obj: "EDISegment") -> bool:
        """Sample implementaion of a predicate.

        Optional predicate callable that returns True if the given segment
        matches a condition. E.g. this segment class may have a qualifier Z13
        which is defined in a class attribute qual_Z13 = "Z13"

        """
        return obj.qualifier == cls.qual_Z13


class UNB(EDISegment):
    """Header Segment"""

    tag = "UNB"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    def get(self):
        return self[1][0]

    @property
    def sender(self):
        return self[1][0]

    @property
    def recipient(self):
        return self[2][0]

    @property
    def date(self):
        return self[3][0]

    @property
    def ref_id(self):
        return self[4]


class UNT(EDISegment):
    """UNT service segment

    Closes a Message and contains the segment count of this message as well as
    the control reference.

    Parameters
    ----------
    EDISegment : _type_
        _description_

    """

    tag = "UNT"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    def get(self) -> str:
        """segment count of this message

        Returns
        -------
        str
            stored segment count
        """
        return self[0]

    @property
    def segment_count(self):
        return self.get()

    @segment_count.setter
    def segement_count(self, val):
        if type(val) not in (str, int):
            raise ValueError(
                f"Cannot set {type(val)} as segment count, only str or int allowed."
            )

        if isinstance(val, int):
            val = str(val)

        self[0] = val


class IDE(EDISegment):
    tag = "IDE"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    def get(self):
        return self[0][1]


class NAD(EDISegment):
    """tag = NAD"""

    tag = "NAD"
    flag_balancing_group = "ZEU"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    @deprecation_warning
    def get_id(self):
        return self.get()

    def get(self):
        return self[1][0]

    @classmethod
    def is_zeu(cls, obj: EDISegment) -> bool:
        return obj.qualifier == cls.flag_balancing_group


class RFF(EDISegment):
    """Segment containing the Prüfidentifikator"""

    tag = "RFF"
    name = "Pruefidentifikator"
    qual_Z13 = "Z13"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    @deprecation_warning
    def get_id(self):
        return self.get()

    def get(self):
        return self[0][1]

    @classmethod
    def is_Z13(cls, obj: EDISegment) -> bool:
        return obj.qualifier == cls.qual_Z13


class DTM(EDISegment):
    """Segment containing the date"""

    tag = "DTM"
    name = "Datum"

    qual_137 = "137"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    @deprecation_warning
    def get(self):
        return self[0][1]

    @classmethod
    def is_137(cls, obj: EDISegment) -> bool:
        return obj.qualifier == cls.qual_137


class LOC(EDISegment):
    """Segment containing the MeLo or MaLo"""

    tag = "LOC"
    name = "MeLo_MaLo_ID"
    qual_172 = "172"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    @deprecation_warning
    def get_id(self):
        return self.get()

    def get(self):
        return self[1]

    @classmethod
    def is_172(cls, obj: EDISegment) -> bool:
        return obj.qualifier == cls.qual_172


class PIA(EDISegment):
    """Segment containing the OBIS-Code or equal"""

    tag = "PIA"
    name = "OBIS_Code"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    @deprecation_warning
    def get_id(self):
        return self.get()

    def get(self):
        return self[1][0]


class LIN(EDISegment):
    tag = "LIN"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    @deprecation_warning
    def get_id(self):
        pass

    def get(self):
        pass


class CCI(EDISegment):
    """Segment containing the EIC-Code or equal"""

    tag = "CCI"
    name = "EIC-Code"
    qual_balancing_group = "Z19"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    @deprecation_warning
    def get_id(self):
        return self.get()

    def get(self):
        return self[2]

    @classmethod
    def is_Z19(cls, obj: EDISegment) -> bool:
        return obj.qualifier == cls.qual_balancing_group


BASE_SEGMENT = EDISegment
# BASE_SEGMENT = Segment

implemented_segment_types = (
    UNB,
    UNT,
    IDE,
    NAD,
    RFF,
    DTM,
    LOC,
    PIA,
    LIN,
    CCI
)


SEGMENTS_CATALOG = dict(zip(list(s.tag for s in implemented_segment_types),implemented_segment_types))

def choose_segment_from_catalog(segment: Segment) -> EDISegment:
    """looks for matching tag in segment catalog and constructs a new instance

    If the given tag is not implemented an EDISegment instance is returned.

    Parameters
    ----------
    segment : Segment
        Segment to use

    Returns
    -------
    EDISegment
        instance from catalog class or EDISegment
    """
    class_to_use = SEGMENTS_CATALOG[segment.tag] if segment.tag in SEGMENTS_CATALOG.keys() else BASE_SEGMENT
    return class_to_use(segment)

def match_qualifier(qualifier: Union[str, int]) -> Callable[[EDISegment], bool]:
    def func(segment: EDISegment) -> bool:
        if not isinstance(segment, EDISegment):
            segment = EDISegment(segment.tag, segment.elements)
        return segment.qualifier == qualifier

    return func
