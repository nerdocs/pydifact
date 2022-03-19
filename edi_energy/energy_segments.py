from typing import Callable, Union

from ..pydifact.segments import Segment

from ..utils.dev import deprecation_warning


class EDISegment(Segment):

    tag: str

    # tag is not a class attribute in this case, as each Segment instance could have another tag.
    __omitted__ = True

    def __init__(self, segment: Segment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

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

    def get(self):
        pass


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


class RFF(EDISegment):
    """Segment containing the Prüfidentifikator"""

    tag = "RFF"
    name = "Pruefidentifikator"
    qualifier = "Z13"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    @deprecation_warning
    def get_id(self):
        return self.get()

    def get(self):
        return self[0][1]


class DTM(EDISegment):
    """Segment containing the date"""

    tag = "DTM"
    name = "Datum"

    flag_137 = "137"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    @deprecation_warning
    def get(self):
        return self[0][1]


class LOC(EDISegment):
    """Segment containing the MeLo or MaLo"""

    tag = "LOC"
    name = "MeLo_MaLo_ID"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    @deprecation_warning
    def get_id(self):
        return self.get()

    def get(self):
        return self[1]


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
    bk_flag = "Z19"
    name = "EIC-Code"

    def __init__(self, segment: EDISegment):
        for key, val in vars(segment).items():
            setattr(self, key, val)

    @deprecation_warning
    def get_id(self):
        return self.get()

    def get(self):
        return self[2]


def match_qualifier(qualifier: Union[str, int]) -> Callable[[EDISegment], bool]:
    def func(segment: EDISegment) -> bool:
        if not isinstance(segment, EDISegment):
            segment = EDISegment(segment.tag, segment.elements)
        return segment.qualifier == qualifier

    return func
