from typing import NamedTuple

from pydifact.constants import C, M
from pydifact.syntax import v1, v2, v3
from pydifact.syntax.common import (
    CompositeDataElement,
    DataElement,
    SyntaxVersionNumber,
)

from .data import partner_identification_codes

__version__ = 4

from ... import Segment


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


# ------------- Composite Data Elements -------------


class CSyntaxIdentifier(v1.CSyntaxIdentifier):
    code = "S001"
    title = "Syntax identifier"
    schema = [
        (SyntaxIdentifier, M, "a4"),
        (SyntaxVersionNumber, M, "an1"),
        (ServiceCodeListDirectoryVersionNumber, C, "an..6"),
        (CharacterEncoding, C, "an..3"),
    ]


class CInterchangeSender(CompositeDataElement):
    code = "S002"
    title = "Interchange sender"
    schema = [
        (v1.SenderIdentification, M, "an..35"),
        (IdentificationCodeQualifier, C, "an..4"),
        (InterchangeSenderInternalIdentification, C, "an..35"),
        (InterchangeSenderInternalSubIdentification, C, "an..35"),
    ]


class CInterchangeRecipient(CompositeDataElement):
    code = "S003"
    title = "Interchange recipient"
    schema = [
        (InterchangeRecipientIdentification, M, "an..35"),
        (IdentificationCodeQualifier, C, "an..4"),
        (InterchangeRecipientInternalIdentification, C, "an..35"),
        (InterchangeRecipientInternalSubIdentification, C, "an..35"),
    ]


class CDateAndTimeOfPreparation(CompositeDataElement):
    code = "S004"
    schema = [
        (v1.Date, M, "n8"),  # CHANGED n6 to n8!!
        (v1.Time, M, "n4"),
    ]


class CRecipientReferencePassword(CompositeDataElement):
    code = "S005"
    schema = [
        (v1.RecipientReferencePassword, M, "an..14"),
        (v1.RecipientReferencePasswordQualifier, C, "an2"),
    ]


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
