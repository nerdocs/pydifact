# FIXME: deprecated

from pydifact.constants import M, C
from pydifact.syntax import v1, v2, v3
from pydifact.syntax.common.types import DataElement
from .codes import partner_identification_codes
from ... import Segment

__version__ = 4


class SyntaxIdentifier(v1.SyntaxIdentifier):
    code = "0001"
    repr = "a4"


class IdentificationCodeQualifier(v1.IdentificationCodeQualifier):
    codes = partner_identification_codes


class InterchangeSenderInternalIdentification(DataElement):
    code = "0008"
    repr = "an..35"
    title = "Interchange sender internal identification"


class InterchangeRecipientIdentification(DataElement):
    code = "0010"
    repr = "an..35"
    title = "Interchange recipient identification"


class InterchangeRecipientInternalIdentification(DataElement):
    code = "0014"
    repr = "an..35"
    title = "Interchange recipient internal identification"


class InterchangeControlReference(DataElement):
    code = "0020"
    repr = "an..14"
    title = "Interchange control reference"
    description = "Unique reference assigned by sender"


class ProcessingPriorityCode(DataElement):
    code = "0029"
    repr = "a1"


class AcknowledgementRequest(DataElement):
    code = "0031"
    repr = "n1"


class InterchangeAgreementIdentifier(DataElement):
    code = "0032"
    repr = "an..35"
    title = "Interchange agreement identifier"
    description = "If used, to identify type of interchange controlling the interchange, e.g. Customs or ECE agreement. Code or name as specified in IA"


class TestIndicator(DataElement):
    code = "0035"
    repr = "n1"


class InterchangeSenderInternalSubIdentification:
    code = "0042"
    repr = "an..35"
    title = "Interchange sender internal sub-identification"


class InterchangeRecipientInternalSubIdentification(DataElement):
    code = "0046"
    repr = "an..35"
    title = "Interchange recipient internal sub-identification"


class ControllingAgency(DataElement):
    code = "0051"
    repr = "an..3"


class MessageVersionNumber(DataElement):
    code = "0052"
    repr = "an..3"


class MessageReleaseNumber(DataElement):
    code = "0054"
    repr = "an..3"


class MessageType(DataElement):
    code = "0065"
    repr = "an..6"


class FirstAndLastTransfer(DataElement):
    code = "0073"
    repr = "a1"


class SectionIdentification(DataElement):
    code = "0081"
    repr = "a1"


class Action(DataElement):
    code = "0083"
    repr = "an..3"


class SyntaxError(DataElement):
    code = "0085"
    repr = "an..3"


class MessageTypeSubFunctionIdentification(DataElement):
    code = "0113"
    repr = "an..6"


class CharacterEncoding(DataElement):
    code = "0133"
    repr = "an..3"


class ServiceSegmentTag(DataElement):
    code = "0135"
    repr = "an..3"


class TransferPosition(DataElement):
    code = "0323"
    repr = "a1"


class DuplicateIndicator(DataElement):
    code = "0325"
    repr = "a1"


class MessageAuthenticationCodeQualifier(DataElement):
    code = "0343"
    repr = "an..3"


class MessageAuthenticationCode(DataElement):
    code = "0345"
    repr = "an..35"


class ServiceCodeListDirectoryVersionNumber(DataElement):
    code = "0080"
    repr = "an..6"


# ------------- Segments -------------


class UNASegment(Segment):
    """Service String Advice."""

    version = __version__


class UNBSegment(v3.UNBSegment):
    """Interchange header."""

    tag = "UNB"
    version = __version__
    schema = [
        (CSyntaxIdentifier, M, 1),
        (CInterchangeSender, M, 1),
        (CInterchangeRecipient, M, 1),
        (CDateAndTimeOfPreparation, M, 1),
        (InterchangeControlReference, M, 1),
        (CRecipientReferencePassword, C, 1),
        (v1.ApplicationReference, C, 1, "an..14"),
        (v1.ProcessingPriorityCode, C, 1, "a1"),
        (v1.AcknowledgementRequest, C, 1, "n1"),
        (InterchangeAgreementIdentifier, C, 1, "an..35"),
    ]
