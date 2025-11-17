from pydifact.syntax.common.types import DataElement


class SyntaxIdentifier(DataElement):
    code = "0001"
    repr = "a4"
    title = "Syntax identifier"


class SyntaxVersionNumber(DataElement):
    code = "0002"
    repr = "n1"
    title = "Syntax version number"


class SenderIdentification(DataElement):
    code = "0004"
    repr = "an..35"
    title = "Sender identification"


class IdentificationCodeQualifier(DataElement):
    code = "0007"
    repr = "an..4"
    title = "Identification code qualifier"
    description = "Code used to identify the type of identification code"


class AddressForReverseRouting(DataElement):
    code = "0008"
    repr = "an..14"
    title = "Address for reverse routing"


class RecipientIdentification(DataElement):
    code = "0010"
    repr = "an..35"
    title = "Recipient identification"


class RoutingAddress(DataElement):
    code = "0014"
    repr = "an..14"
    title = "Routing address"
    description = "Address of the recipient of the interchange"


class Date(DataElement):
    """YYMMDD"""

    code = "0017"
    repr = "n6"
    title = "Date"
    description = "Date of the interchange (YYMMDD)"


class Time(DataElement):
    """HHMM"""

    code = "0019"
    repr = "n4"
    title = "Time"
    description = "Time of the interchange (HHMM)"


class InterchangeControlReference(DataElement):
    code = "0020"
    repr = "an..14"
    title = "Interchange control reference"
    description = "Unique reference assigned by sender"


class RecipientsReferencePassword(DataElement):
    code = "0022"
    repr = "an..14"
    title = "Recipients reference password"


class RecipientsReferencePasswordQualifier(DataElement):
    code = "0025"
    repr = "an2"
    title = "Recipients reference password qualifier"


class ApplicationReference(DataElement):
    code = "0026"
    repr = "an..14"
    title = "Application reference"


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
    description = "Set = 1 if interchange is a test. Otherwise not used."


class InterchangeControlCount(DataElement):
    code = "0036"
    repr = "n..6"
    title = "Interchange control count"
    description = "Number of functional groups in the interchange. One of these counts shall appear."


class FunctionalGroupIdentification(DataElement):
    """Identifies the one message type in the functional group."""

    code = "0038"
    repr = "an..6"
    title = "Functional group identification"


class FunctionalGroupReferenceNumber(DataElement):
    """Unique reference number assigned by sender's division, department etc."""

    code = "0048"
    repr = "an..14"
    title = "Functional group reference number"


class ControllingAgency(DataElement):
    """Code to identify the agency controlling the specification, maintenance and publication of the message type."""

    code = "0051"
    repr = "an..2"
    title = "Controlling agency"


class ApplicationPassword(DataElement):
    """Password to recipient's division, department or sectional system (if required)."""

    code = "0058"
    repr = "an..14"
    title = "Application password"
