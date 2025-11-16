import pydifact.syntax.common.data
import pydifact.syntax.v1.segments
from .. import v1
from ..common import DataElement
from ..common.types import CompositeDataElement
from ...constants import M


class SyntaxIdentifier(DataElement):
    code = "0001"
    title = "Syntax identifier"
    repr = "a4"
    codes = {
        "UNIX": {
            "name": "7 bit",
            "description": "",
        },
        "DINA": {
            "name": "7 bit",
            "description": "",
        },
        "IBMA": {
            "name": "8 bit",
            "description": "",
        },
        "ANSI": {
            "name": "Windows",
            "description": "",
        },
    }


class InterchangeSender(DataElement):
    code = ""
    repr = "an..35"  # TODO
    title = "Interchange sender"


class InterchangeRecipient(DataElement):
    code = ""
    repr = "an..35"  # TODO
    title = "Interchange recipient"


class Date(DataElement):
    code = ""
    repr = "n6"
    title = "Date"
    description = "Date in the format YYMMDD"


class Time(DataElement):
    code = ""
    repr = "n4"
    title = "Time"
    description = "Time in the format HHMM"


class ReferenceNumber(DataElement):
    code = ""
    repr = "an..35"  # TODO
    title = "Reference number"
    description = "Is determined by the sender (internal number of the finding). Must be same as in UNT segment"


class CMedRpt(CompositeDataElement):
    code = ""
    description = "Is determined by the sender (internal number of the finding). Must be same as in UNH segment"

    def validate(self, mandatory: bool = None, repeat: int = None) -> None:
        super().validate(mandatory, repeat)


class CSyntaxIdentifier(v1.CSyntaxIdentifier):
    code = "S001"
    title = "Syntax identifier"
    schema = [
        (SyntaxIdentifier, M, "a4"),
        (pydifact.syntax.common.data.SyntaxVersionNumber, M, "an1"),
    ]


class UNBSegment(pydifact.syntax.v1.segments.UNBSegment):
    """Specific Interchange Header for Austrian MED EDIFACT."""

    schema = [
        (CSyntaxIdentifier, M),
        (InterchangeSender, M),
        (InterchangeRecipient, M),
        (Date, M),
        (Time, M),
    ]


class UNHSegment(v1.UNHSegment):
    """Specific Message Header for Austrian MED EDIFACT.

    Must be in the format `UNH+REFERENZNUMMER+MEDRPT:1:901:UN'`.
    """

    schema = [
        (ReferenceNumber, M),
        (CMedRpt, M),
    ]
