from pydifact.syntax.common import (
    DataElement,
    CompositeDataElement,
    SyntaxVersionNumber,
)
from pydifact.constants import M, C
from pydifact.segments import Segment

__version__ = 1

from .data import partner_identification_codes
from ... import Characters


class ServiceStringAdvice(DataElement):
    code = ""
    repr = "an6"
    title = "Service String Advice"
    description = "Service string advice"


class SyntaxIdentifier(DataElement):
    code = "0001"
    title = "Syntax identifier"
    repr = "a4"
    codes = {
        "UNOA": (
            "UN/ECE level A",
            "Defined in ISO 646 basic code table with exceptions for lowercase "
            "letters, alternative graphic character allocations, "
            "and national/application-oriented allocations.",
        ),
        "UNOB": (
            "UN/ECE level B",
            "Defined in ISO 646 basic code table with exceptions for alternative "
            "graphic character allocations and national/application-oriented "
            "allocations.",
        ),
        "UNOC": (
            "UN/ECE level C",
            "Defined in ISO 8859-1: Information processing - Part 1: Latin alphabet No. 1.",
        ),
        "UNOD": (
            "UN/ECE level D",
            "Defined in ISO 8859-2: Information processing - Part 2: Latin alphabet No. 2.",
        ),
        "UNOE": (
            "UN/ECE level E",
            "Defined in ISO 8859-5: Information processing - Part 5: Latin/Cyrillic alphabet.",
        ),
        "UNOF": (
            "UN/ECE level F",
            "Defined in ISO 8859-7: Information processing - Part 7: Latin/Greek alphabet.",
        ),
    }


class SenderIdentification(DataElement):
    code = "0004"
    repr = "an..35"
    title = "Sender identification"


class IdentificationCodeQualifier(DataElement):
    code = "0007"
    repr = "an..4"
    title = "Identification code qualifier"
    description = "Qualifier referring to the recipient identification code."
    codes = partner_identification_codes


class AddressForReverseRouting(DataElement):
    code = "0008"
    repr = "an..14"
    title = "Address for reverse routing"


class RecipientIdentification(DataElement):
    code = "0010"
    repr = "an..35"
    title = "Recipient identification"
    description = "Code or name as specified in IA"


class RoutingAddress(DataElement):
    code = "0014"
    repr = "an..14"
    title = "Routing address"
    description = "If used, normally coded sub-address for onward routing"


class Date(DataElement):
    code = "0017"
    repr = "n6"
    title = "Date"
    description = "Date in the format YYMMDD"


class Time(DataElement):
    code = "0019"
    repr = "n4"
    title = "Time"
    description = "Time in the format HHMM"


class InterchangeControlReference(DataElement):
    code = "0020"
    repr = "an..14"
    title = "Interchange control reference"
    description = "Unique reference assigned by sender"


class RecipientReferencePassword(DataElement):
    code = "0022"
    repr = "an..14"
    title = "Recipient's reference/password"
    description = "As specified in IA. May be password to recipient's system or to third party network"


class RecipientReferencePasswordQualifier(DataElement):
    code = "0025"
    repr = "an2"
    title = "Recipient's reference/password qualifier"
    description = "If specified in IA"


class ApplicationReference(DataElement):
    code = "0026"
    repr = "an..14"
    title = "Application reference"
    description = "Optional message identification if the interchange contains only one type of message"


class ProcessingPriorityCode(DataElement):
    code = "0029"
    repr = "a1"
    title = "Processing priority code"
    description = "Used if specified in IA"


class AcknowledgementRequest(DataElement):
    code = "0031"
    repr = "n1"
    title = "Acknowledgement request"
    description = (
        "Set = 1 if sender requests acknowledgement, i.e. UNB and UNZ "
        "segments received and identified"
    )


class CommunicationAgreementID(DataElement):
    code = "0032"
    repr = "an..35"
    title = "Communication agreement ID"
    description = (
        "If used, to identify type of communication agreement controlling "
        "the interchange, e.g. Customs or ECE agreement. Code or name as specified in IA"
    )


class TestIndicator(DataElement):
    code = "0035"
    repr = "n1"
    title = "Test indicator"
    description = "Set = 1 if the interchange is a test. Otherwise not used"


class NameAndAddressLine(DataElement):
    code = "3124"
    desc = "Free form name and address description."
    repr = "an..35"


class PartyName(DataElement):
    code = "3036"
    desc = "Name of a party involved in a transaction."
    repr = "an..35"


class PartyNameFormat(DataElement):
    code = "3045"
    desc = "Specification of the representation of a party name."
    repr = "an..3"


# ----------------- Composite Data Elements -----------------


class CSyntaxIdentifier(CompositeDataElement):
    code = "S001"
    title = "Syntax identifier"
    schema = [
        (SyntaxIdentifier, M, "a4"),
        (SyntaxVersionNumber, M, "n1"),
    ]


class PartyNameComposite(CompositeDataElement):
    code = "C080"
    desc = "Identification of a transaction party by name, one to five lines. Party name may be formatted."
    schema = [
        PartyName,
        PartyName,
        PartyName,
        PartyName,
        PartyName,
        PartyNameFormat,
    ]


class PartyIdentificationDetails(CompositeDataElement):
    code = "C082"
    schema = [NameAndAddressLine]


# ------------- Segments -------------


class CInterchangeSender(CompositeDataElement):
    code = "S002"
    title = "Interchange sender"
    schema = [
        (SenderIdentification, M, "an..35"),
        (IdentificationCodeQualifier, C, "an..4"),
        (AddressForReverseRouting, C, "an..14"),
    ]


class CInterchangeRecipient(CompositeDataElement):
    code = "S003"
    title = "Interchange recipient"
    schema = [
        (RecipientIdentification, M, "an..35"),
        (IdentificationCodeQualifier, C, "an..4"),
        (AddressForReverseRouting, C, "an..14"),
    ]


class CDateAndTimeOfPreparation(CompositeDataElement):
    code = "S004"
    schema = [
        (Date, M, "n6"),
        (Time, M, "n4"),
    ]


class CRecipientsReference(CompositeDataElement):
    code = "S005"
    schema = [
        (RecipientReferencePassword, M, "an..14"),
        (RecipientReferencePasswordQualifier, C, "an2"),
    ]


# ------------- Segments -------------


class UNASegment(Segment):
    """Service String Advice."""

    tag = "UNA"
    version = __version__
    schema = [
        (ServiceStringAdvice, C, 1),
    ]

    def __init__(self, characters: Characters | str | None = None):  # noqa
        # in this special case, we need no super class, as we directly set the
        # Character string
        if isinstance(characters, str):
            characters = Characters.from_str(characters)
        else:
            characters = Characters() if characters is None else characters
        self.elements = [characters]
        # provide shortcut handles to the separators
        self.component_separator = characters.component_separator
        self.data_separator = characters.data_separator
        self.decimal_point = characters.decimal_point
        self.escape_character = characters.escape_character
        self.reserved_character = characters.reserved_character
        self.segment_terminator = characters.segment_terminator

    def validate(self) -> None:
        super().validate()


class UNBSegment(Segment):
    """Interchange header.

    To start, identify and specify an interchange."""

    tag = "UNB"
    version = __version__
    schema = [
        (CSyntaxIdentifier, M, 1),
        (CInterchangeSender, M, 1),
        (CInterchangeRecipient, M, 1),
        (CDateAndTimeOfPreparation, M, 1),
        (InterchangeControlReference, M, 1),
        (CRecipientsReference, C, 1),
        (ApplicationReference, C, 1, "an..14"),
        (ProcessingPriorityCode, C, 1, "a1"),
        (AcknowledgementRequest, C, 1, "n1"),
        (CommunicationAgreementID, C, 1, "an..35"),
        (TestIndicator, C, 1, "n1"),
    ]
