# ------------------- Data Elements -------------------
# created from EDED - the EDIFACT data elements directory

# This file is auto-generated. Don't edit it manually.

# Copyright (c) 2017-2025 Christian González
# This file is licensed under the MIT license, see LICENSE file.

from pydifact.syntax.common.types import DataElement


class SyntaxIdentifier(DataElement):
    """Coded identification of the agency controlling the syntax, and of the character repertoire used in an interchange."""

    code: str = "0001"
    title: str = "Syntax identifier"
    repr_line: str = "a4"


class SyntaxVersionNumber(DataElement):
    """Version number of the syntax."""

    code: str = "0002"
    title: str = "Syntax version number"
    repr_line: str = "an1"


class InterchangeSenderIdentification(DataElement):
    """Name or coded identification of the sender of the interchange."""

    code: str = "0004"
    title: str = "Interchange sender identification"
    repr_line: str = "an..35"


class IdentificationCodeQualifier(DataElement):
    """Qualifier referring to the identification code."""

    code: str = "0007"
    title: str = "Identification code qualifier"
    repr_line: str = "an..4"


class InterchangeSenderInternalIdentification(DataElement):
    """Identification (for example, a division, branch or computer system/process) specified by the sender of interchange, to be included if agreed, by the recipient in response interchanges, to facilitate internal routing."""

    code: str = "0008"
    title: str = "Interchange sender internal identification"
    repr_line: str = "an..35"


class InterchangeRecipientIdentification(DataElement):
    """Name or coded identification of the recipient of the interchange."""

    code: str = "0010"
    title: str = "Interchange recipient identification"
    repr_line: str = "an..35"


class InterchangeRecipientInternalIdentification(DataElement):
    """Identification (for example, a division, branch or computer system/process) specified by the recipient of interchange, to be included if agreed, by the sender in response interchanges, to facilitate internal routing."""

    code: str = "0014"
    title: str = "Interchange recipient internal identification"
    repr_line: str = "an..35"


class Date(DataElement):
    """Local date when an interchange or a group was prepared."""

    code: str = "0017"
    title: str = "Date"
    repr_line: str = "n8"


class Time(DataElement):
    """Local time of day when an interchange or a group was prepared."""

    code: str = "0019"
    title: str = "Time"
    repr_line: str = "n4"


class InterchangeControlReference(DataElement):
    """Unique reference assigned by the sender to an interchange."""

    code: str = "0020"
    title: str = "Interchange control reference"
    repr_line: str = "an..14"


class RecipientReferencepassword(DataElement):
    """Reference or password to the recipient's system or to a third party network as specified in the partners' interchange agreement."""

    code: str = "0022"
    title: str = "Recipient reference/password"
    repr_line: str = "an..14"


class RecipientReferencepasswordQualifier(DataElement):
    """Qualifier for the recipient's reference or password."""

    code: str = "0025"
    title: str = "Recipient reference/password qualifier"
    repr_line: str = "an2"


class ApplicationReference(DataElement):
    """Identification of the application area assigned by the sender, to which the messages in the interchange relate e.g. the message type, if all the messages in the interchange are of the same type."""

    code: str = "0026"
    title: str = "Application reference"
    repr_line: str = "an..14"


class ProcessingPriorityCode(DataElement):
    """Code determined by the sender requesting processing priority for the interchange."""

    code: str = "0029"
    title: str = "Processing priority code"
    repr_line: str = "a1"


class AcknowledgementRequest(DataElement):
    """Code requesting acknowledgement for the interchange."""

    code: str = "0031"
    title: str = "Acknowledgement request"
    repr_line: str = "n1"


class InterchangeAgreementIdentifier(DataElement):
    """Identification by name or code of the type of agreement under which the interchange takes place."""

    code: str = "0032"
    title: str = "Interchange agreement identifier"
    repr_line: str = "an..35"


class TestIndicator(DataElement):
    """Indication that the structural level containing the test indicator is a test."""

    code: str = "0035"
    title: str = "Test indicator"
    repr_line: str = "n1"


class InterchangeControlCount(DataElement):
    """The number of messages and packages in an interchange or, if used, the number of groups in an interchange."""

    code: str = "0036"
    title: str = "Interchange control count"
    repr_line: str = "n..6"


class MessageGroupIdentification(DataElement):
    """Identification of the single message type in the group."""

    code: str = "0038"
    title: str = "Message group identification"
    repr_line: str = "an..6"


class ApplicationSenderIdentification(DataElement):
    """Name or coded identification of the application sender (for example, a division, branch or computer system/process)."""

    code: str = "0040"
    title: str = "Application sender identification"
    repr_line: str = "an..35"


class InterchangeSenderInternalSubidentification(DataElement):
    """Sub-level of sender internal identification, when further sub-level identification is required."""

    code: str = "0042"
    title: str = "Interchange sender internal sub-identification"
    repr_line: str = "an..35"


class ApplicationRecipientIdentification(DataElement):
    """Name or coded identification of the application recipient (for example, a division, branch or computer system/process)."""

    code: str = "0044"
    title: str = "Application recipient identification"
    repr_line: str = "an..35"


class InterchangeRecipientInternalSubidentification(DataElement):
    """Sub-level of recipient internal identification, when further sub-level identification is required."""

    code: str = "0046"
    title: str = "Interchange recipient internal sub-identification"
    repr_line: str = "an..35"


class GroupReferenceNumber(DataElement):
    """Unique reference number for the group within an interchange."""

    code: str = "0048"
    title: str = "Group reference number"
    repr_line: str = "an..14"


class ControllingAgencyCoded(DataElement):
    """Code identifying a controlling agency."""

    code: str = "0051"
    title: str = "Controlling agency, coded"
    repr_line: str = "an..3"


class MessageVersionNumber(DataElement):
    """Version number of a message type."""

    code: str = "0052"
    title: str = "Message version number"
    repr_line: str = "an..3"


class MessageReleaseNumber(DataElement):
    """Release number within the current message version number."""

    code: str = "0054"
    title: str = "Message release number"
    repr_line: str = "an..3"


class AssociationAssignedCode(DataElement):
    """Code, assigned by the association responsible for the design and maintenance of the message type concerned, which further identifies the message."""

    code: str = "0057"
    title: str = "Association assigned code"
    repr_line: str = "an..6"


class ApplicationPassword(DataElement):
    """Password to the recipient's division, department or sectional application system/process."""

    code: str = "0058"
    title: str = "Application password"
    repr_line: str = "an..14"


class GroupControlCount(DataElement):
    """The number of messages and packages in the group."""

    code: str = "0060"
    title: str = "Group control count"
    repr_line: str = "n..6"


class MessageReferenceNumber(DataElement):
    """Unique message reference assigned by the sender."""

    code: str = "0062"
    title: str = "Message reference number"
    repr_line: str = "an..14"


class MessageType(DataElement):
    """Code identifying a type of message and assigned by its controlling agency."""

    code: str = "0065"
    title: str = "Message type"
    repr_line: str = "an..6"


class CommonAccessReference(DataElement):
    """Reference serving as a key to relate all subsequent transfers of data to the same business case or file."""

    code: str = "0068"
    title: str = "Common access reference"
    repr_line: str = "an..35"


class SequenceOfTransfers(DataElement):
    """Number assigned by the sender indicating the transfer sequence of a message related to the same topic. The message could be an addition or a change to an earlier transfer related to the same topic."""

    code: str = "0070"
    title: str = "Sequence of transfers"
    repr_line: str = "n..2"


class FirstAndLastTransfer(DataElement):
    """Indication used for the first and last message in a sequence of messages related to the same topic."""

    code: str = "0073"
    title: str = "First and last transfer"
    repr_line: str = "a1"


class NumberOfSegmentsInAMessage(DataElement):
    """The number of segments in a message body, plus the message header segment and message trailer segment."""

    code: str = "0074"
    title: str = "Number of segments in a message"
    repr_line: str = "n..10"


class SyntaxReleaseNumber(DataElement):
    """The number of a syntax release (within an existing syntax version number)."""

    code: str = "0076"
    title: str = "Syntax release number"
    repr_line: str = "an2"


class ServiceCodeListDirectoryVersionNumber(DataElement):
    """Version number of the service code list directory."""

    code: str = "0080"
    title: str = "Service code list directory version number"
    repr_line: str = "an..6"


class SectionIdentification(DataElement):
    """Identification of the separation of sections of a message."""

    code: str = "0081"
    title: str = "Section identification"
    repr_line: str = "a1"


class ActionCoded(DataElement):
    """A code indicating acknowledgement, or rejection (the action taken) of a subject interchange, or part of the subject interchange, or indication of interchange receipt."""

    code: str = "0083"
    title: str = "Action, coded"
    repr_line: str = "an..3"


class SyntaxErrorCoded(DataElement):
    """A code indicating the error detected."""

    code: str = "0085"
    title: str = "Syntax error, coded"
    repr_line: str = "an..3"


class AnticollisionSegmentGroupIdentification(DataElement):
    """To identify uniquely an anti-collision segment group in a message."""

    code: str = "0087"
    title: str = "Anti-collision segment group identification"
    repr_line: str = "an..4"


class SegmentPositionInMessageBody(DataElement):
    """The numerical count position of a specific segment that is within the actual received message body. The numbering starts with, and includes, the UNH or the UIH segment as segment number 1. To identify a segment that contains an error, this is the numerical count position of that segment. To report that a segment is missing, this is the numerical count position of the last segment that was processed before the position where the missing segment was expected to be. A missing segment group is denoted by identifying the first segment in the group as missing."""

    code: str = "0096"
    title: str = "Segment position in message body"
    repr_line: str = "n..6"


class ErroneousDataElementPositionInSegment(DataElement):
    """The numerical count position of the stand-alone or composite data element in error. The segment code and each following stand-alone or composite data element defined in the segment description shall cause the count to be incremented. The segment tag has position number 1."""

    code: str = "0098"
    title: str = "Erroneous data element position in segment"
    repr_line: str = "n..3"


class ErroneousComponentDataElementPosition(DataElement):
    """The numerical count position of the component data element in error. Each component data element position defined in the composite data element description shall cause the count to be incremented. The count starts at 1."""

    code: str = "0104"
    title: str = "Erroneous component data element position"
    repr_line: str = "n..3"


class CodeListDirectoryVersionNumber(DataElement):
    """Version number of the code list directory."""

    code: str = "0110"
    title: str = "Code list directory version number"
    repr_line: str = "an..6"


class MessageTypeSubfunctionIdentification(DataElement):
    """Code identifying a sub-function of a message type."""

    code: str = "0113"
    title: str = "Message type sub-function identification"
    repr_line: str = "an..6"


class MessageSubsetIdentification(DataElement):
    """Coded identification of a message subset, assigned by its controlling agency."""

    code: str = "0115"
    title: str = "Message subset identification"
    repr_line: str = "an..14"


class MessageSubsetVersionNumber(DataElement):
    """Version number of the message subset."""

    code: str = "0116"
    title: str = "Message subset version number"
    repr_line: str = "an..3"


class MessageSubsetReleaseNumber(DataElement):
    """Release number within the message subset version number."""

    code: str = "0118"
    title: str = "Message subset release number"
    repr_line: str = "an..3"


class MessageImplementationGuidelineIdentification(DataElement):
    """Coded identification of the message implementation guideline, assigned by its controlling agency."""

    code: str = "0121"
    title: str = "Message implementation guideline identification"
    repr_line: str = "an..14"


class MessageImplementationGuidelineVersionNumber(DataElement):
    """Version number of the message implementation guideline."""

    code: str = "0122"
    title: str = "Message implementation guideline version number"
    repr_line: str = "an..3"


class MessageImplementationGuidelineReleaseNumber(DataElement):
    """Release number within the message implementation guideline version number."""

    code: str = "0124"
    title: str = "Message implementation guideline release number"
    repr_line: str = "an..3"


class ScenarioIdentification(DataElement):
    """Code identifying scenario."""

    code: str = "0127"
    title: str = "Scenario identification"
    repr_line: str = "an..14"


class ScenarioVersionNumber(DataElement):
    """Version number of a scenario."""

    code: str = "0128"
    title: str = "Scenario version number"
    repr_line: str = "an..3"


class ScenarioReleaseNumber(DataElement):
    """Release number within the scenario version number."""

    code: str = "0130"
    title: str = "Scenario release number"
    repr_line: str = "an..3"


class CharacterEncodingCoded(DataElement):
    """Coded identification of the character encoding used in the interchange."""

    code: str = "0133"
    title: str = "Character encoding, coded"
    repr_line: str = "an..3"


class ServiceSegmentTagCoded(DataElement):
    """Code identifying a service segment."""

    code: str = "0135"
    title: str = "Service segment tag, coded"
    repr_line: str = "an..3"


class ErroneousDataElementOccurrence(DataElement):
    """The numerical occurrence of the repeating stand-alone or composite data element in error. Each occurrence (as indicated by the repetition separator) shall cause the count to be incremented. The count starts at 1."""

    code: str = "0136"
    title: str = "Erroneous data element occurrence"
    repr_line: str = "n..6"


class SecuritySegmentPosition(DataElement):
    """The numerical count position of a specific security segment that is within the actual received security header/trailer segment group pair, identified by its security reference number. The numbering starts with, and includes, the USH segment as segment number 1. To identify a security segment that contains an error, this is the numerical count position of that security segment. To report that a security segment is missing, this is the numerical count position of the last security segment that was processed before the position where the missing security segment was expected to be. A missing security segment group is denoted by identifying the first segment in the security segment group as missing."""

    code: str = "0138"
    title: str = "Security segment position"
    repr_line: str = "n..6"


class InitiatorControlReference(DataElement):
    """A reference assigned by the dialogue initiator."""

    code: str = "0300"
    title: str = "Initiator control reference"
    repr_line: str = "an..35"


class InitiatorReferenceIdentification(DataElement):
    """Organisation code or name assigned by the party that initiated the transaction or dialogue."""

    code: str = "0303"
    title: str = "Initiator reference identification"
    repr_line: str = "an..35"


class ResponderControlReference(DataElement):
    """A reference assigned by the dialogue responder."""

    code: str = "0304"
    title: str = "Responder control reference"
    repr_line: str = "an..35"


class TransactionControlReference(DataElement):
    """A reference assigned by the transaction initiator."""

    code: str = "0306"
    title: str = "Transaction control reference"
    repr_line: str = "an..35"


class DialogueIdentification(DataElement):
    """Code identifying a dialogue."""

    code: str = "0311"
    title: str = "Dialogue identification"
    repr_line: str = "an..14"


class EventTime(DataElement):
    """Time of event."""

    code: str = "0314"
    title: str = "Event time"
    repr_line: str = "an..15"


class SenderSequenceNumber(DataElement):
    """Identification of the sequence number of the message or package within the sender interchange."""

    code: str = "0320"
    title: str = "Sender sequence number"
    repr_line: str = "n..6"


class TransferPositionCoded(DataElement):
    """Indication of the position of a transfer."""

    code: str = "0323"
    title: str = "Transfer position, coded"
    repr_line: str = "a1"


class DuplicateIndicator(DataElement):
    """Indication that the structure is a duplicate of a previously sent structure."""

    code: str = "0325"
    title: str = "Duplicate indicator"
    repr_line: str = "a1"


class ReportFunctionCoded(DataElement):
    """Coded value identifying type of status or error report."""

    code: str = "0331"
    title: str = "Report function, coded"
    repr_line: str = "an..3"


class Status(DataElement):
    """Textual explanation of the reason for the status or error report."""

    code: str = "0332"
    title: str = "Status"
    repr_line: str = "an..70"


class StatusCoded(DataElement):
    """Code identifying the reason for the status or error report."""

    code: str = "0333"
    title: str = "Status, coded"
    repr_line: str = "an..3"


class LanguageCoded(DataElement):
    """Code identifying the language used."""

    code: str = "0335"
    title: str = "Language, coded"
    repr_line: str = "an..3"


class TimeOffset(DataElement):
    """UTC (Universal Co-ordinated Time) offset from event time."""

    code: str = "0336"
    title: str = "Time offset"
    repr_line: str = "n4"


class EventDate(DataElement):
    """Date of event."""

    code: str = "0338"
    title: str = "Event date"
    repr_line: str = "n..8"


class InteractiveMessageReferenceNumber(DataElement):
    """Unique interactive message reference assigned by the sender."""

    code: str = "0340"
    title: str = "Interactive message reference number"
    repr_line: str = "an..35"


class DialogueVersionNumber(DataElement):
    """Version number of a dialogue."""

    code: str = "0342"
    title: str = "Dialogue version number"
    repr_line: str = "an..3"


class DialogueReleaseNumber(DataElement):
    """Release number of a dialogue."""

    code: str = "0344"
    title: str = "Dialogue release number"
    repr_line: str = "an..3"


class SecurityServiceCoded(DataElement):
    """Specification of the security service applied."""

    code: str = "0501"
    title: str = "Security service, coded"
    repr_line: str = "an..3"


class ResponseTypeCoded(DataElement):
    """Specification of the type of response expected from the recipient."""

    code: str = "0503"
    title: str = "Response type, coded"
    repr_line: str = "an..3"


class FilterFunctionCoded(DataElement):
    """Identification of the filtering function used to reversibly map any bit pattern on to a restricted character set."""

    code: str = "0505"
    title: str = "Filter function, coded"
    repr_line: str = "an..3"


class OriginalCharacterSetEncodingCoded(DataElement):
    """Identification of the character set in which the secured EDIFACT structure was encoded when security mechanisms were applied."""

    code: str = "0507"
    title: str = "Original character set encoding, coded"
    repr_line: str = "an..3"


class RoleOfSecurityProviderCoded(DataElement):
    """Identification of the role of the security provider in relation to the secured item."""

    code: str = "0509"
    title: str = "Role of security provider, coded"
    repr_line: str = "an..3"


class SecurityPartyIdentification(DataElement):
    """Identification of a party involved in the security process, according to a defined registry of security parties."""

    code: str = "0511"
    title: str = "Security party identification"
    repr_line: str = "an..1024"


class SecurityPartyCodeListQualifier(DataElement):
    """Identification of the type of identification used to register the security parties."""

    code: str = "0513"
    title: str = "Security party code list qualifier"
    repr_line: str = "an..3"


class SecurityPartyCodeListResponsibleAgencyCoded(DataElement):
    """Identification of the agency in charge of registration of the security parties."""

    code: str = "0515"
    title: str = "Security party code list responsible agency, coded"
    repr_line: str = "an..3"


class DateAndTimeQualifier(DataElement):
    """Specification of the type of date and time."""

    code: str = "0517"
    title: str = "Date and time qualifier"
    repr_line: str = "an..3"


class EncryptionReferenceNumber(DataElement):
    """Reference number to the encrypted EDIFACT structure."""

    code: str = "0518"
    title: str = "Encryption reference number"
    repr_line: str = "an..35"


class SecuritySequenceNumber(DataElement):
    """Sequence number assigned to the EDIFACT structure to which security is applied."""

    code: str = "0520"
    title: str = "Security sequence number"
    repr_line: str = "an..35"


class UseOfAlgorithmCoded(DataElement):
    """Specification of the usage made of the algorithm."""

    code: str = "0523"
    title: str = "Use of algorithm, coded"
    repr_line: str = "an..3"


class CryptographicModeOfOperationCoded(DataElement):
    """Specification of the mode of operation used for the algorithm."""

    code: str = "0525"
    title: str = "Cryptographic mode of operation, coded"
    repr_line: str = "an..3"


class AlgorithmCoded(DataElement):
    """Identification of the algorithm."""

    code: str = "0527"
    title: str = "Algorithm, coded"
    repr_line: str = "an..3"


class AlgorithmCodeListIdentifier(DataElement):
    """Specification of the code list used to identify the algorithm."""

    code: str = "0529"
    title: str = "Algorithm code list identifier"
    repr_line: str = "an..3"


class AlgorithmParameterQualifier(DataElement):
    """Specification of the type of parameter value."""

    code: str = "0531"
    title: str = "Algorithm parameter qualifier"
    repr_line: str = "an..3"


class ModeOfOperationCodeListIdentifier(DataElement):
    """Specification of the code list used to identify the cryptographic mode of operation."""

    code: str = "0533"
    title: str = "Mode of operation code list identifier"
    repr_line: str = "an..3"


class SecurityReferenceNumber(DataElement):
    """Unique reference number assigned by the security originator to a pair of security header and security trailer groups."""

    code: str = "0534"
    title: str = "Security reference number"
    repr_line: str = "an..14"


class CertificateReference(DataElement):
    """Identifies one certificate for a certification authority."""

    code: str = "0536"
    title: str = "Certificate reference"
    repr_line: str = "an..70"


class KeyName(DataElement):
    """Name used to establish a key relationship between the parties."""

    code: str = "0538"
    title: str = "Key name"
    repr_line: str = "an..35"


class ScopeOfSecurityApplicationCoded(DataElement):
    """Specification of the scope of application of the security service defined in the security header."""

    code: str = "0541"
    title: str = "Scope of security application, coded"
    repr_line: str = "an..3"


class CertificateOriginalCharacterSetRepertoireCoded(DataElement):
    """Identification of the character set repertoire used to create the certificate it was signed."""

    code: str = "0543"
    title: str = "Certificate original character set repertoire, coded"
    repr_line: str = "an..3"


class CertificateSyntaxAndVersionCoded(DataElement):
    """Coded identification of the syntax and version used to create the certificate."""

    code: str = "0545"
    title: str = "Certificate syntax and version, coded"
    repr_line: str = "an..3"


class UserAuthorisationLevel(DataElement):
    """Specification of the authorisation level associated with the owner of the certificate."""

    code: str = "0546"
    title: str = "User authorisation level"
    repr_line: str = "an..35"


class ServiceCharacterForSignature(DataElement):
    """Service character used when the signature was computed."""

    code: str = "0548"
    title: str = "Service character for signature"
    repr_line: str = "an..4"


class ServiceCharacterForSignatureQualifier(DataElement):
    """Identification of the type of service character used when the signature was computed."""

    code: str = "0551"
    title: str = "Service character for signature qualifier"
    repr_line: str = "an..3"


class AlgorithmParameterValue(DataElement):
    """Value of a parameter required by the algorithm."""

    code: str = "0554"
    title: str = "Algorithm parameter value"
    repr_line: str = "an..512"


class LengthOfDataInOctetsOfBits(DataElement):
    """A count of the data octets of bits."""

    code: str = "0556"
    title: str = "Length of data in octets of bits"
    repr_line: str = "n..18"


class ListParameter(DataElement):
    """Specification of the list requested or delivered."""

    code: str = "0558"
    title: str = "List parameter"
    repr_line: str = "an..70"


class ValidationValue(DataElement):
    """Security result corresponding to the security function specified."""

    code: str = "0560"
    title: str = "Validation value"
    repr_line: str = "an..1024"


class ValidationValueQualifier(DataElement):
    """Identification of the type of validation value."""

    code: str = "0563"
    title: str = "Validation value qualifier"
    repr_line: str = "an..3"


class MessageRelationCoded(DataElement):
    """Relationship with another message, past or future."""

    code: str = "0565"
    title: str = "Message relation, coded"
    repr_line: str = "an..3"


class SecurityStatusCoded(DataElement):
    """Identification of the security element (key or certificate, for instance) status."""

    code: str = "0567"
    title: str = "Security status, coded"
    repr_line: str = "an..3"


class RevocationReasonCoded(DataElement):
    """Identification of the reason why the certificate has been revoked."""

    code: str = "0569"
    title: str = "Revocation reason, coded"
    repr_line: str = "an..3"


class SecurityErrorCoded(DataElement):
    """Identifies the security error causing the rejection of the EDIFACT structure."""

    code: str = "0571"
    title: str = "Security error, coded"
    repr_line: str = "an..3"


class CertificateSequenceNumber(DataElement):
    """Specification of a certificate's position within a certification path."""

    code: str = "0572"
    title: str = "Certificate sequence number"
    repr_line: str = "n..4"


class ListParameterQualifier(DataElement):
    """Specification of the type of list parameter."""

    code: str = "0575"
    title: str = "List parameter qualifier"
    repr_line: str = "an..3"


class SecurityPartyQualifier(DataElement):
    """Identification of the role of the security party."""

    code: str = "0577"
    title: str = "Security party qualifier"
    repr_line: str = "an..3"


class KeyManagementFunctionQualifier(DataElement):
    """Specification of the type of key management function."""

    code: str = "0579"
    title: str = "Key management function qualifier"
    repr_line: str = "an..3"


class NumberOfPaddingBytes(DataElement):
    """Count of the number of padding bytes."""

    code: str = "0582"
    title: str = "Number of padding bytes"
    repr_line: str = "n..2"


class SecurityPartyName(DataElement):
    """Name of the security party."""

    code: str = "0586"
    title: str = "Security party name"
    repr_line: str = "an..35"


class NumberOfSecuritySegments(DataElement):
    """The number of security segments in a security header/trailer group pair, plus the USD and USU segments where the security header/trailer group pair is used for encryption."""

    code: str = "0588"
    title: str = "Number of security segments"
    repr_line: str = "n..10"


class PaddingMechanismCoded(DataElement):
    """Padding mechanism or padding scheme applied."""

    code: str = "0591"
    title: str = "Padding mechanism, coded"
    repr_line: str = "an..3"


class PaddingMechanismCodeListIdentifier(DataElement):
    """Specification of the code list used to identify the padding mechanism or padding scheme."""

    code: str = "0601"
    title: str = "Padding mechanism code list identifier"
    repr_line: str = "an..3"


class PackageReferenceNumber(DataElement):
    """Unique package reference number assigned by the sender."""

    code: str = "0800"
    title: str = "Package reference number"
    repr_line: str = "an..35"


class ReferenceIdentificationNumber(DataElement):
    """Reference number to identify a message, message group and/or interchange, which relates to the object."""

    code: str = "0802"
    title: str = "Reference identification number"
    repr_line: str = "an..35"


class ObjectTypeQualifier(DataElement):
    """Qualifier referring to the type of object."""

    code: str = "0805"
    title: str = "Object type qualifier"
    repr_line: str = "an..3"


class ObjectTypeAttribute(DataElement):
    """The attribute applying to the object type."""

    code: str = "0808"
    title: str = "Object type attribute"
    repr_line: str = "an..256"


class ObjectTypeAttributeIdentification(DataElement):
    """Coded identification of the attribute applying to the object type."""

    code: str = "0809"
    title: str = "Object type attribute identification"
    repr_line: str = "an..256"


class LengthOfObjectInOctetsOfBits(DataElement):
    """Count of the number of octets of bits in the object."""

    code: str = "0810"
    title: str = "Length of object in octets of bits"
    repr_line: str = "n..18"


class ReferenceQualifier(DataElement):
    """Code giving specific meaning to a reference identification number."""

    code: str = "0813"
    title: str = "Reference qualifier"
    repr_line: str = "an..3"


class NumberOfSegmentsBeforeObject(DataElement):
    """A count of the number of segments appearing between the UNO segment and the start of the object."""

    code: str = "0814"
    title: str = "Number of segments before object"
    repr_line: str = "n..3"


class EDocumentName(DataElement):
    """Name of a document."""

    code: str = "1000"
    title: str = "Document name"
    repr_line: str = "an..35"


class EDocumentNameCode(DataElement):
    """Code specifying the document name."""

    code: str = "1001"
    title: str = "Document name code"
    repr_line: str = "an..3"


class EMessageTypeCode(DataElement):
    """Code specifying a type of message."""

    code: str = "1003"
    title: str = "Message type code"
    repr_line: str = "an..6"


class EDocumentIdentifier(DataElement):
    """To identify a document."""

    code: str = "1004"
    title: str = "Document identifier"
    repr_line: str = "an..70"


class EMessageSectionCode(DataElement):
    """Code specifying a section of a message."""

    code: str = "1049"
    title: str = "Message section code"
    repr_line: str = "an..3"


class ESequencePositionIdentifier(DataElement):
    """To identify a position in a sequence."""

    code: str = "1050"
    title: str = "Sequence position identifier"
    repr_line: str = "an..10"


class EMessageItemIdentifier(DataElement):
    """To identify an item within a message."""

    code: str = "1052"
    title: str = "Message item identifier"
    repr_line: str = "an..35"


class EMessageSubitemIdentifier(DataElement):
    """To identify a sub-item within a message."""

    code: str = "1054"
    title: str = "Message sub-item identifier"
    repr_line: str = "n..6"


class EVersionIdentifier(DataElement):
    """To identify a version."""

    code: str = "1056"
    title: str = "Version identifier"
    repr_line: str = "an..9"


class EReleaseIdentifier(DataElement):
    """To identify a release."""

    code: str = "1058"
    title: str = "Release identifier"
    repr_line: str = "an..9"


class ERevisionIdentifier(DataElement):
    """To identify a revision."""

    code: str = "1060"
    title: str = "Revision identifier"
    repr_line: str = "an..6"


class EDocumentLineActionCode(DataElement):
    """Code indicating an action associated with a line of a document."""

    code: str = "1073"
    title: str = "Document line action code"
    repr_line: str = "an..3"


class ELineItemIdentifier(DataElement):
    """To identify a line item."""

    code: str = "1082"
    title: str = "Line item identifier"
    repr_line: str = "an..6"


class ECodeListIdentificationCode(DataElement):
    """Code identifying a user or association maintained code list."""

    code: str = "1131"
    title: str = "Code list identification code"
    repr_line: str = "an..17"


class ETravellerReferenceIdentifier(DataElement):
    """To identify a reference to a traveller."""

    code: str = "1145"
    title: str = "Traveller reference identifier"
    repr_line: str = "an..35"


class EAccountName(DataElement):
    """Name of an account."""

    code: str = "1146"
    title: str = "Account name"
    repr_line: str = "an..35"


class EAccountIdentifier(DataElement):
    """To identify an account."""

    code: str = "1147"
    title: str = "Account identifier"
    repr_line: str = "an..35"


class EAccountAbbreviatedName(DataElement):
    """Abbreviated name of an account."""

    code: str = "1148"
    title: str = "Account abbreviated name"
    repr_line: str = "an..17"


class EReferenceCodeQualifier(DataElement):
    """Code qualifying a reference."""

    code: str = "1153"
    title: str = "Reference code qualifier"
    repr_line: str = "an..3"


class EReferenceIdentifier(DataElement):
    """Identifies a reference."""

    code: str = "1154"
    title: str = "Reference identifier"
    repr_line: str = "an..70"


class EDocumentLineIdentifier(DataElement):
    """To identify a line of a document."""

    code: str = "1156"
    title: str = "Document line identifier"
    repr_line: str = "an..6"


class ESequenceIdentifierSourceCode(DataElement):
    """Code specifying the source of a sequence identifier."""

    code: str = "1159"
    title: str = "Sequence identifier source code"
    repr_line: str = "an..3"


class EAccountingJournalName(DataElement):
    """Name of an accounting journal."""

    code: str = "1170"
    title: str = "Accounting journal name"
    repr_line: str = "an..35"


class EAccountingJournalIdentifier(DataElement):
    """To identify an accounting journal."""

    code: str = "1171"
    title: str = "Accounting journal identifier"
    repr_line: str = "an..17"


class EDocumentOriginalsRequiredQuantity(DataElement):
    """Quantity of document originals required."""

    code: str = "1218"
    title: str = "Document originals required quantity"
    repr_line: str = "n..2"


class EDocumentCopiesRequiredQuantity(DataElement):
    """Quantity of document copies required."""

    code: str = "1220"
    title: str = "Document copies required quantity"
    repr_line: str = "n..2"


class EConfigurationLevelNumber(DataElement):
    """To specify a level within a configuration."""

    code: str = "1222"
    title: str = "Configuration level number"
    repr_line: str = "n..2"


class EMessageFunctionCode(DataElement):
    """Code indicating the function of the message."""

    code: str = "1225"
    title: str = "Message function code"
    repr_line: str = "an..3"


class ECalculationSequenceCode(DataElement):
    """Code specifying a calculation sequence."""

    code: str = "1227"
    title: str = "Calculation sequence code"
    repr_line: str = "an..3"


class EActionDescription(DataElement):
    """Free form description of the action to be taken or already taken."""

    code: str = "1228"
    title: str = "Action description"
    repr_line: str = "an..35"


class EActionCode(DataElement):
    """Code specifying the action to be taken or already taken."""

    code: str = "1229"
    title: str = "Action code"
    repr_line: str = "an..3"


class EAllowanceOrChargeIdentifier(DataElement):
    """To identify an allowance or charge."""

    code: str = "1230"
    title: str = "Allowance or charge identifier"
    repr_line: str = "an..35"


class EConsignmentLoadSequenceIdentifier(DataElement):
    """To identify the loading sequence of a consignment or consignments."""

    code: str = "1312"
    title: str = "Consignment load sequence identifier"
    repr_line: str = "n..4"


class EDocumentSourceDescription(DataElement):
    """Free form description of the source of a document."""

    code: str = "1366"
    title: str = "Document source description"
    repr_line: str = "an..70"


class EDocumentStatusCode(DataElement):
    """Code specifying the status of a document."""

    code: str = "1373"
    title: str = "Document status code"
    repr_line: str = "an..3"


class EControllingAgencyIdentifier(DataElement):
    """To identify a controlling agency."""

    code: str = "1476"
    title: str = "Controlling agency identifier"
    repr_line: str = "an..2"


class EConsolidationItemNumber(DataElement):
    """To specify a consignment within a consolidation."""

    code: str = "1490"
    title: str = "Consolidation item number"
    repr_line: str = "n..5"


class EGoodsItemNumber(DataElement):
    """To specify a goods item within a consignment."""

    code: str = "1496"
    title: str = "Goods item number"
    repr_line: str = "an..6"


class EComputerEnvironmentDetailsCodeQualifier(DataElement):
    """Code qualifying computer environment details."""

    code: str = "1501"
    title: str = "Computer environment details code qualifier"
    repr_line: str = "an..3"


class EDataFormatDescription(DataElement):
    """Free form description of the data format."""

    code: str = "1502"
    title: str = "Data format description"
    repr_line: str = "an..35"


class EDataFormatDescriptionCode(DataElement):
    """Code specifying the data format."""

    code: str = "1503"
    title: str = "Data format description code"
    repr_line: str = "an..3"


class EValueListTypeCode(DataElement):
    """Code specifying a type of value list."""

    code: str = "1505"
    title: str = "Value list type code"
    repr_line: str = "an..3"


class EDesignatedClassCode(DataElement):
    """Code specifying a designated class."""

    code: str = "1507"
    title: str = "Designated class code"
    repr_line: str = "an..3"


class EFileName(DataElement):
    """Name of a file."""

    code: str = "1508"
    title: str = "File name"
    repr_line: str = "an..35"


class EComputerEnvironmentName(DataElement):
    """Name of a computer environment."""

    code: str = "1510"
    title: str = "Computer environment name"
    repr_line: str = "an..35"


class EComputerEnvironmentNameCode(DataElement):
    """Code specifying a computer environment."""

    code: str = "1511"
    title: str = "Computer environment name code"
    repr_line: str = "an..3"


class EValueListName(DataElement):
    """Name of a coded or non-coded list of values."""

    code: str = "1514"
    title: str = "Value list name"
    repr_line: str = "an..70"


class EFileFormatName(DataElement):
    """Name of a file format."""

    code: str = "1516"
    title: str = "File format name"
    repr_line: str = "an..17"


class EValueListIdentifier(DataElement):
    """To identify a coded or non-coded list of values."""

    code: str = "1518"
    title: str = "Value list identifier"
    repr_line: str = "an..35"


class EDataSetIdentifier(DataElement):
    """To identify a data set."""

    code: str = "1520"
    title: str = "Data set identifier"
    repr_line: str = "an..35"


class EMessageImplementationIdentificationCode(DataElement):
    """Code identifying an implementation of a message."""

    code: str = "1523"
    title: str = "Message implementation identification code"
    repr_line: str = "an..6"


class EDate(DataElement):
    """To specify a date."""

    code: str = "2000"
    title: str = "Date"
    repr_line: str = "an..14"


class ETime(DataElement):
    """To specify a time."""

    code: str = "2002"
    title: str = "Time"
    repr_line: str = "n4"


class EDateOrTimeOrPeriodFunctionCodeQualifier(DataElement):
    """Code qualifying the function of a date, time or period."""

    code: str = "2005"
    title: str = "Date or time or period function code qualifier"
    repr_line: str = "an..3"


class ETermsTimeRelationCode(DataElement):
    """Code relating terms to a reference date, time or period."""

    code: str = "2009"
    title: str = "Terms time relation code"
    repr_line: str = "an..3"


class EFrequencyCode(DataElement):
    """Code specifying the rate of recurrence."""

    code: str = "2013"
    title: str = "Frequency code"
    repr_line: str = "an..3"


class EDespatchPatternCode(DataElement):
    """Code specifying a despatch pattern."""

    code: str = "2015"
    title: str = "Despatch pattern code"
    repr_line: str = "an..3"


class EDespatchPatternTimingCode(DataElement):
    """Code specifying a set of dates/times within a despatch pattern."""

    code: str = "2017"
    title: str = "Despatch pattern timing code"
    repr_line: str = "an..3"


class EAge(DataElement):
    """To specify the length of time that a person or thing has existed."""

    code: str = "2018"
    title: str = "Age"
    repr_line: str = "n..3"


class EPeriodTypeCodeQualifier(DataElement):
    """Code qualifying the type of the period."""

    code: str = "2023"
    title: str = "Period type code qualifier"
    repr_line: str = "an..3"


class ETimeZoneIdentifier(DataElement):
    """To identify a time zone."""

    code: str = "2029"
    title: str = "Time zone identifier"
    repr_line: str = "an..3"


class ETimeVariationQuantity(DataElement):
    """To specify a time variation."""

    code: str = "2031"
    title: str = "Time variation quantity"
    repr_line: str = "n..3"


class ETimeZoneDifferenceQuantity(DataElement):
    """The difference between two defined time zones."""

    code: str = "2116"
    title: str = "Time zone difference quantity"
    repr_line: str = "n..4"


class EPeriodDetailDescription(DataElement):
    """Free form description of the period detail."""

    code: str = "2118"
    title: str = "Period detail description"
    repr_line: str = "an..35"


class EPeriodDetailDescriptionCode(DataElement):
    """Code specifying the period detail."""

    code: str = "2119"
    title: str = "Period detail description code"
    repr_line: str = "an..3"


class EDateVariationNumber(DataElement):
    """A number to indicate the difference between two dates."""

    code: str = "2148"
    title: str = "Date variation number"
    repr_line: str = "n..5"


class EPeriodTypeCode(DataElement):
    """Code specifying the type of period."""

    code: str = "2151"
    title: str = "Period type code"
    repr_line: str = "an..3"


class EPeriodCountQuantity(DataElement):
    """Count of the number of periods."""

    code: str = "2152"
    title: str = "Period count quantity"
    repr_line: str = "n..3"


class EChargePeriodTypeCode(DataElement):
    """Code specifying a type of a charge period."""

    code: str = "2155"
    title: str = "Charge period type code"
    repr_line: str = "an..3"


class ECheckinTime(DataElement):
    """To specifiy a check-in date and time."""

    code: str = "2156"
    title: str = "Check-in time"
    repr_line: str = "an..10"


class EDaysOfWeekSetIdentifier(DataElement):
    """String data representation of days of the week (Monday = 1)."""

    code: str = "2160"
    title: str = "Days of week set identifier"
    repr_line: str = "an..7"


class EJourneyLegDurationQuantity(DataElement):
    """To specify the elapsed time between departure and arrival for a leg of a journey."""

    code: str = "2162"
    title: str = "Journey leg duration quantity"
    repr_line: str = "an..6"


class EMillisecondTime(DataElement):
    """To specify a time including milliseconds."""

    code: str = "2164"
    title: str = "Millisecond time"
    repr_line: str = "n9"


class EDateOrTimeOrPeriodFormatCode(DataElement):
    """Code specifying the representation of a date, time or period."""

    code: str = "2379"
    title: str = "Date or time or period format code"
    repr_line: str = "an..3"


class EDateOrTimeOrPeriodText(DataElement):
    """The value of a date, a date and time, a time or of a period in a specified representation."""

    code: str = "2380"
    title: str = "Date or time or period text"
    repr_line: str = "an..35"


class EEventTimeReferenceCode(DataElement):
    """Code specifying a time that references an event that will or has occurred."""

    code: str = "2475"
    title: str = "Event time reference code"
    repr_line: str = "an..3"


class EMaintenanceOperationOperatorCode(DataElement):
    """A code identifying the type of party being responsible for a maintenance operation."""

    code: str = "3005"
    title: str = "Maintenance operation operator code"
    repr_line: str = "an..3"


class EMaintenanceOperationPayerCode(DataElement):
    """A code identifying  the type of party paying for a maintenance operation."""

    code: str = "3009"
    title: str = "Maintenance operation payer code"
    repr_line: str = "an..3"


class EPartyFunctionCodeQualifier(DataElement):
    """Code giving specific meaning to a party."""

    code: str = "3035"
    title: str = "Party function code qualifier"
    repr_line: str = "an..3"


class EPartyName(DataElement):
    """Name of a party."""

    code: str = "3036"
    title: str = "Party name"
    repr_line: str = "an..70"


class EPartyIdentifier(DataElement):
    """Code specifying the identity of a party."""

    code: str = "3039"
    title: str = "Party identifier"
    repr_line: str = "an..35"


class EStreetAndNumberOrPostOfficeBoxIdentifier(DataElement):
    """To identify a street and number and/or Post Office box number."""

    code: str = "3042"
    title: str = "Street and number or post office box identifier"
    repr_line: str = "an..256"


class EPartyNameFormatCode(DataElement):
    """Code specifying the representation of a party name."""

    code: str = "3045"
    title: str = "Party name format code"
    repr_line: str = "an..3"


class ECodeListResponsibleAgencyCode(DataElement):
    """Code specifying the agency responsible for a code list."""

    code: str = "3055"
    title: str = "Code list responsible agency code"
    repr_line: str = "an..3"


class ETestMediumCode(DataElement):
    """Code specifying the medium on which a test was or is to be applied."""

    code: str = "3077"
    title: str = "Test medium code"
    repr_line: str = "an..3"


class EOrganisationClassificationCode(DataElement):
    """Code specifying the classification of an organisation."""

    code: str = "3079"
    title: str = "Organisation classification code"
    repr_line: str = "an..3"


class EOrganisationalClassName(DataElement):
    """Name of a class of organisation."""

    code: str = "3082"
    title: str = "Organisational class name"
    repr_line: str = "an..70"


class EOrganisationalClassNameCode(DataElement):
    """Code specifying a class of organisation."""

    code: str = "3083"
    title: str = "Organisational class name code"
    repr_line: str = "an..17"


class ENameAndAddressDescription(DataElement):
    """Free form description of a name and address line."""

    code: str = "3124"
    title: str = "Name and address description"
    repr_line: str = "an..35"


class ECarrierName(DataElement):
    """Name of a carrier."""

    code: str = "3126"
    title: str = "Carrier name"
    repr_line: str = "an..35"


class ECarrierIdentifier(DataElement):
    """To identify a carrier."""

    code: str = "3127"
    title: str = "Carrier identifier"
    repr_line: str = "an..17"


class EAddressTypeCode(DataElement):
    """Code specifying the type of an address."""

    code: str = "3131"
    title: str = "Address type code"
    repr_line: str = "an..3"


class EContactFunctionCode(DataElement):
    """Code specifying the function of a contact (e.g. department or person)."""

    code: str = "3139"
    title: str = "Contact function code"
    repr_line: str = "an..3"


class ECommunicationAddressIdentifier(DataElement):
    """To identify a communication address."""

    code: str = "3148"
    title: str = "Communication address identifier"
    repr_line: str = "an..512"


class ECommunicationMediumTypeCode(DataElement):
    """Code specifying the type of communication medium."""

    code: str = "3153"
    title: str = "Communication medium type code"
    repr_line: str = "an..3"


class ECommunicationMeansTypeCode(DataElement):
    """Code specifying the type of communication address."""

    code: str = "3155"
    title: str = "Communication means type code"
    repr_line: str = "an..3"


class ECityName(DataElement):
    """Name of a city."""

    code: str = "3164"
    title: str = "City name"
    repr_line: str = "an..35"


class EAccountHolderName(DataElement):
    """Name of the holder of an account."""

    code: str = "3192"
    title: str = "Account holder name"
    repr_line: str = "an..35"


class EAccountHolderIdentifier(DataElement):
    """To identify the holder of an account."""

    code: str = "3194"
    title: str = "Account holder identifier"
    repr_line: str = "an..35"


class EAgentIdentifier(DataElement):
    """To identify an agent."""

    code: str = "3197"
    title: str = "Agent identifier"
    repr_line: str = "an..9"


class ECountryIdentifier(DataElement):
    """Identification of the name of the country or other geographical entity as defined in ISO 3166-1 and UN/ECE Recommendation 3."""

    code: str = "3207"
    title: str = "Country identifier"
    repr_line: str = "an..3"


class EFirstRelatedLocationName(DataElement):
    """Name of first related location."""

    code: str = "3222"
    title: str = "First related location name"
    repr_line: str = "an..70"


class EFirstRelatedLocationIdentifier(DataElement):
    """To identify a first related location."""

    code: str = "3223"
    title: str = "First related location identifier"
    repr_line: str = "an..35"


class ELocationName(DataElement):
    """Name of the location."""

    code: str = "3224"
    title: str = "Location name"
    repr_line: str = "an..256"


class ELocationIdentifier(DataElement):
    """To identify a location."""

    code: str = "3225"
    title: str = "Location identifier"
    repr_line: str = "an..35"


class ELocationFunctionCodeQualifier(DataElement):
    """Code identifying the function of a location."""

    code: str = "3227"
    title: str = "Location function code qualifier"
    repr_line: str = "an..3"


class ECountrySubdivisionName(DataElement):
    """Name of a country subdivision, such as state, canton, county, prefecture."""

    code: str = "3228"
    title: str = "Country subdivision name"
    repr_line: str = "an..70"


class ECountrySubdivisionIdentifier(DataElement):
    """To identify a country subdivision, such as state, canton, county, prefecture."""

    code: str = "3229"
    title: str = "Country subdivision identifier"
    repr_line: str = "an..9"


class ESecondRelatedLocationName(DataElement):
    """Name of the second related location."""

    code: str = "3232"
    title: str = "Second related location name"
    repr_line: str = "an..70"


class ESecondRelatedLocationIdentifier(DataElement):
    """To identify a second related location."""

    code: str = "3233"
    title: str = "Second related location identifier"
    repr_line: str = "an..35"


class ESampleLocationDescription(DataElement):
    """Free form description of the sample location."""

    code: str = "3236"
    title: str = "Sample location description"
    repr_line: str = "an..35"


class ESampleLocationDescriptionCode(DataElement):
    """Code specifying the sample location."""

    code: str = "3237"
    title: str = "Sample location description code"
    repr_line: str = "an..3"


class ECountryOfOriginIdentifier(DataElement):
    """To identify the country in which the goods have been produced or manufactured, according to criteria laid down for the application of the Customs tariff or quantitative restrictions, or any measure related to trade."""

    code: str = "3239"
    title: str = "Country of origin identifier"
    repr_line: str = "an..3"


class EPostalIdentificationCode(DataElement):
    """Code specifying the postal zone or address."""

    code: str = "3251"
    title: str = "Postal identification code"
    repr_line: str = "an..17"


class EGeographicAreaCode(DataElement):
    """Code specifying a geographical area."""

    code: str = "3279"
    title: str = "Geographic area code"
    repr_line: str = "an..3"


class EInstructionReceivingPartyIdentifier(DataElement):
    """Code specifying the party to receive an instruction."""

    code: str = "3285"
    title: str = "Instruction receiving party identifier"
    repr_line: str = "an..35"


class EAddressComponentDescription(DataElement):
    """Free form description of the component of an address."""

    code: str = "3286"
    title: str = "Address component description"
    repr_line: str = "an..70"


class EPersonCharacteristicCodeQualifier(DataElement):
    """Code qualifying a type of characteristic of a person."""

    code: str = "3289"
    title: str = "Person characteristic code qualifier"
    repr_line: str = "an..3"


class ENationalityName(DataElement):
    """Name of a nationality."""

    code: str = "3292"
    title: str = "Nationality name"
    repr_line: str = "a..35"


class ENationalityNameCode(DataElement):
    """Code specifying the name of a nationality."""

    code: str = "3293"
    title: str = "Nationality name code"
    repr_line: str = "an..3"


class ENameOriginalAlphabetCode(DataElement):
    """Code specifying the alphabet originally used to represent a name."""

    code: str = "3295"
    title: str = "Name original alphabet code"
    repr_line: str = "an..3"


class EAddressPurposeCode(DataElement):
    """Code specifying the purpose of an address."""

    code: str = "3299"
    title: str = "Address purpose code"
    repr_line: str = "an..3"


class EEnactingPartyIdentifier(DataElement):
    """To identify the party enacting an instruction."""

    code: str = "3301"
    title: str = "Enacting party identifier"
    repr_line: str = "an..35"


class EInheritedCharacteristicDescription(DataElement):
    """Free form description of an inherited characteristic."""

    code: str = "3310"
    title: str = "Inherited characteristic description"
    repr_line: str = "an..70"


class EInheritedCharacteristicDescriptionCode(DataElement):
    """Code specifying an inherited characteristic."""

    code: str = "3311"
    title: str = "Inherited characteristic description code"
    repr_line: str = "an..8"


class ENameStatusCode(DataElement):
    """Code specifying the status of a name."""

    code: str = "3397"
    title: str = "Name status code"
    repr_line: str = "an..3"


class ENameComponentDescription(DataElement):
    """Free form description of a name component."""

    code: str = "3398"
    title: str = "Name component description"
    repr_line: str = "an..256"


class ENameComponentUsageCode(DataElement):
    """Code specifying the usage of a name component."""

    code: str = "3401"
    title: str = "Name component usage code"
    repr_line: str = "an..3"


class ENameTypeCode(DataElement):
    """Code specifying the type of name."""

    code: str = "3403"
    title: str = "Name type code"
    repr_line: str = "an..3"


class ENameComponentTypeCodeQualifier(DataElement):
    """Code qualifying the type of a name component."""

    code: str = "3405"
    title: str = "Name component type code qualifier"
    repr_line: str = "an..3"


class EContactName(DataElement):
    """Name of a contact, such as a department or employee."""

    code: str = "3412"
    title: str = "Contact name"
    repr_line: str = "an..256"


class EContactIdentifier(DataElement):
    """To identify a contact, such as a department or employee."""

    code: str = "3413"
    title: str = "Contact identifier"
    repr_line: str = "an..17"


class EInstitutionName(DataElement):
    """Name of an institution."""

    code: str = "3432"
    title: str = "Institution name"
    repr_line: str = "an..70"


class EInstitutionNameCode(DataElement):
    """Code specifying the name of an institution."""

    code: str = "3433"
    title: str = "Institution name code"
    repr_line: str = "an..11"


class EInstitutionBranchIdentifier(DataElement):
    """To identify a branch of an institution."""

    code: str = "3434"
    title: str = "Institution branch identifier"
    repr_line: str = "an..17"


class EInstitutionBranchLocationName(DataElement):
    """Name of the location of a branch of an institution."""

    code: str = "3436"
    title: str = "Institution branch location name"
    repr_line: str = "an..70"


class EPartyTaxIdentifier(DataElement):
    """To identify a number assigned to a party by a tax authority."""

    code: str = "3446"
    title: str = "Party tax identifier"
    repr_line: str = "an..20"


class EBankIdentifier(DataElement):
    """To identify a bank."""

    code: str = "3449"
    title: str = "Bank identifier"
    repr_line: str = "an..17"


class ELanguageName(DataElement):
    """Name of language."""

    code: str = "3452"
    title: str = "Language name"
    repr_line: str = "an..35"


class ELanguageNameCode(DataElement):
    """Code specifying the language name."""

    code: str = "3453"
    title: str = "Language name code"
    repr_line: str = "an..3"


class ELanguageCodeQualifier(DataElement):
    """Code qualifying a language."""

    code: str = "3455"
    title: str = "Language code qualifier"
    repr_line: str = "an..3"


class EOriginatorTypeCode(DataElement):
    """Code specifying the type of originator."""

    code: str = "3457"
    title: str = "Originator type code"
    repr_line: str = "an..3"


class EFrequentTravellerIdentifier(DataElement):
    """To identify a frequent traveller."""

    code: str = "3459"
    title: str = "Frequent traveller identifier"
    repr_line: str = "an..25"


class EGivenName(DataElement):
    """An individual's given name."""

    code: str = "3460"
    title: str = "Given name"
    repr_line: str = "an..70"


class EGateIdentifier(DataElement):
    """To identify a gate."""

    code: str = "3463"
    title: str = "Gate identifier"
    repr_line: str = "an..6"


class EInhouseIdentifier(DataElement):
    """A unique locally assigned identification."""

    code: str = "3465"
    title: str = "In-house identifier"
    repr_line: str = "an..9"


class EAddressStatusCode(DataElement):
    """Code specifying the status of an address."""

    code: str = "3475"
    title: str = "Address status code"
    repr_line: str = "an..3"


class EAddressFormatCode(DataElement):
    """Code specifying the format of an address."""

    code: str = "3477"
    title: str = "Address format code"
    repr_line: str = "an..3"


class EMaritalStatusDescription(DataElement):
    """Free form description of the marital status of a person."""

    code: str = "3478"
    title: str = "Marital status description"
    repr_line: str = "an..35"


class EMaritalStatusDescriptionCode(DataElement):
    """Code specifying the marital status of a person."""

    code: str = "3479"
    title: str = "Marital status description code"
    repr_line: str = "an..3"


class EPersonJobTitle(DataElement):
    """Name of a job title such as rank or rating of crew member."""

    code: str = "3480"
    title: str = "Person job title"
    repr_line: str = "an..35"


class EReligionName(DataElement):
    """Name of a religion."""

    code: str = "3482"
    title: str = "Religion name"
    repr_line: str = "an..35"


class EReligionNameCode(DataElement):
    """Code specifying the name of a religion."""

    code: str = "3483"
    title: str = "Religion name code"
    repr_line: str = "an..3"


class ENationalityCodeQualifier(DataElement):
    """Code qualifying a nationality."""

    code: str = "3493"
    title: str = "Nationality code qualifier"
    repr_line: str = "an..3"


class ESalesChannelIdentifier(DataElement):
    """To identify a sales channel."""

    code: str = "3496"
    title: str = "Sales channel identifier"
    repr_line: str = "an..17"


class EGenderCode(DataElement):
    """Code giving the gender of a person, animal or plant."""

    code: str = "3499"
    title: str = "Gender code"
    repr_line: str = "an..3"


class EFamilyName(DataElement):
    """Family name (synonym surname)."""

    code: str = "3500"
    title: str = "Family name"
    repr_line: str = "an..70"


class EAccessAuthorisationIdentifier(DataElement):
    """To identify an authorisation to access."""

    code: str = "3503"
    title: str = "Access authorisation identifier"
    repr_line: str = "an..9"


class EGivenNameTitleDescription(DataElement):
    """Free form description of a title."""

    code: str = "3504"
    title: str = "Given name title description"
    repr_line: str = "an..9"


class EBenefitCoverageConstituentsCode(DataElement):
    """Code used to identify who is included in the benefit coverage."""

    code: str = "3507"
    title: str = "Benefit coverage constituents code"
    repr_line: str = "an..3"


class EOptionCode(DataElement):
    """Code specifying an option."""

    code: str = "4009"
    title: str = "Option code"
    repr_line: str = "an..3"


class EDeliveryPlanCommitmentLevelCode(DataElement):
    """Code specifying the level of commitment to a delivery plan."""

    code: str = "4017"
    title: str = "Delivery plan commitment level code"
    repr_line: str = "an..3"


class ERelatedInformationDescription(DataElement):
    """Free form description of the related information."""

    code: str = "4018"
    title: str = "Related information description"
    repr_line: str = "an..35"


class EBusinessDescription(DataElement):
    """Free form description of a business."""

    code: str = "4022"
    title: str = "Business description"
    repr_line: str = "an..70"


class EBusinessFunctionCode(DataElement):
    """Code describing the specific business function."""

    code: str = "4025"
    title: str = "Business function code"
    repr_line: str = "an..3"


class EBusinessFunctionTypeCodeQualifier(DataElement):
    """Code qualifying the type of business function."""

    code: str = "4027"
    title: str = "Business function type code qualifier"
    repr_line: str = "an..3"


class EPriorityTypeCodeQualifier(DataElement):
    """Code qualifying the type of priority."""

    code: str = "4035"
    title: str = "Priority type code qualifier"
    repr_line: str = "an..3"


class EPriorityDescription(DataElement):
    """Free form description of a priority."""

    code: str = "4036"
    title: str = "Priority description"
    repr_line: str = "an..35"


class EPriorityDescriptionCode(DataElement):
    """Code specifying a priority."""

    code: str = "4037"
    title: str = "Priority description code"
    repr_line: str = "an..3"


class EAdditionalSafetyInformationDescription(DataElement):
    """Free form description of information relating to additional safety."""

    code: str = "4038"
    title: str = "Additional safety information description"
    repr_line: str = "an..35"


class EAdditionalSafetyInformationDescriptionCode(DataElement):
    """Code specifying information relating to additional safety."""

    code: str = "4039"
    title: str = "Additional safety information description code"
    repr_line: str = "an..3"


class ETradeClassCode(DataElement):
    """Code identifying the class of trade."""

    code: str = "4043"
    title: str = "Trade class code"
    repr_line: str = "an..3"


class ESafetySectionName(DataElement):
    """Name of a safety section."""

    code: str = "4044"
    title: str = "Safety section name"
    repr_line: str = "an..70"


class ESafetySectionNumber(DataElement):
    """To specify a safety section by number."""

    code: str = "4046"
    title: str = "Safety section number"
    repr_line: str = "n..2"


class ECertaintyDescription(DataElement):
    """Free form description of a certainty."""

    code: str = "4048"
    title: str = "Certainty description"
    repr_line: str = "an..35"


class ECertaintyDescriptionCode(DataElement):
    """Code specifying a certainty."""

    code: str = "4049"
    title: str = "Certainty description code"
    repr_line: str = "an..3"


class ECharacteristicRelevanceCode(DataElement):
    """Code specifying the relevance of a characteristic."""

    code: str = "4051"
    title: str = "Characteristic relevance code"
    repr_line: str = "an..3"


class EDeliveryOrTransportTermsDescription(DataElement):
    """Free form description of delivery or transport terms."""

    code: str = "4052"
    title: str = "Delivery or transport terms description"
    repr_line: str = "an..70"


class EDeliveryOrTransportTermsDescriptionCode(DataElement):
    """Code specifying the delivery or transport terms."""

    code: str = "4053"
    title: str = "Delivery or transport terms description code"
    repr_line: str = "an..3"


class EDeliveryOrTransportTermsFunctionCode(DataElement):
    """Code specifying the function of delivery or transport terms."""

    code: str = "4055"
    title: str = "Delivery or transport terms function code"
    repr_line: str = "an..3"


class EQuestionDescription(DataElement):
    """Free form description of a question."""

    code: str = "4056"
    title: str = "Question description"
    repr_line: str = "an..256"


class EQuestionDescriptionCode(DataElement):
    """Code specifying a question."""

    code: str = "4057"
    title: str = "Question description code"
    repr_line: str = "an..3"


class EClauseCodeQualifier(DataElement):
    """Code qualifying the nature of the clause."""

    code: str = "4059"
    title: str = "Clause code qualifier"
    repr_line: str = "an..3"


class EContractAndCarriageConditionCode(DataElement):
    """Code to identify the conditions of contract and carriage."""

    code: str = "4065"
    title: str = "Contract and carriage condition code"
    repr_line: str = "an..3"


class EClauseName(DataElement):
    """Name of the clause."""

    code: str = "4068"
    title: str = "Clause name"
    repr_line: str = "an..70"


class EClauseNameCode(DataElement):
    """Code identification of the clause."""

    code: str = "4069"
    title: str = "Clause name code"
    repr_line: str = "an..17"


class EProvisoCodeQualifier(DataElement):
    """Code qualifying the proviso."""

    code: str = "4071"
    title: str = "Proviso code qualifier"
    repr_line: str = "an..3"


class EProvisoTypeDescription(DataElement):
    """Free form description of the type of proviso."""

    code: str = "4072"
    title: str = "Proviso type description"
    repr_line: str = "an..35"


class EProvisoTypeDescriptionCode(DataElement):
    """Code specifying the type of proviso."""

    code: str = "4073"
    title: str = "Proviso type description code"
    repr_line: str = "an..3"


class EProvisoCalculationDescription(DataElement):
    """Free form description of the proviso calculation."""

    code: str = "4074"
    title: str = "Proviso calculation description"
    repr_line: str = "an..35"


class EProvisoCalculationDescriptionCode(DataElement):
    """Code specifying the proviso calculation."""

    code: str = "4075"
    title: str = "Proviso calculation description code"
    repr_line: str = "an..3"


class EHandlingInstructionDescription(DataElement):
    """Free form description of a handling instruction."""

    code: str = "4078"
    title: str = "Handling instruction description"
    repr_line: str = "an..512"


class EHandlingInstructionDescriptionCode(DataElement):
    """Code specifying a handling instruction."""

    code: str = "4079"
    title: str = "Handling instruction description code"
    repr_line: str = "an..3"


class EInformationCategoryDescription(DataElement):
    """Free form description of the category of information."""

    code: str = "4148"
    title: str = "Information category description"
    repr_line: str = "an..70"


class EInformationCategoryDescriptionCode(DataElement):
    """Code specifying the information category."""

    code: str = "4149"
    title: str = "Information category description code"
    repr_line: str = "an..3"


class EInformationDetailDescription(DataElement):
    """Free form description of the information detail."""

    code: str = "4150"
    title: str = "Information detail description"
    repr_line: str = "an..256"


class EInformationDetailDescriptionCode(DataElement):
    """Code specifying the information detail."""

    code: str = "4151"
    title: str = "Information detail description code"
    repr_line: str = "an..17"


class EInformationDetailsCodeQualifier(DataElement):
    """Code qualifying the information details."""

    code: str = "4153"
    title: str = "Information details code qualifier"
    repr_line: str = "an..3"


class ESpecialConditionCode(DataElement):
    """Code specifying a special condition."""

    code: str = "4183"
    title: str = "Special condition code"
    repr_line: str = "an..3"


class ESpecialRequirementDescription(DataElement):
    """Free form description of a special requirement."""

    code: str = "4184"
    title: str = "Special requirement description"
    repr_line: str = "an..17"


class ESpecialRequirementTypeCode(DataElement):
    """Code specifying a type of special requirement."""

    code: str = "4187"
    title: str = "Special requirement type code"
    repr_line: str = "an..4"


class ETransportChargesPaymentMethodCode(DataElement):
    """Code specifying the payment method for transport charges."""

    code: str = "4215"
    title: str = "Transport charges payment method code"
    repr_line: str = "an..3"


class ETransportServicePriorityCode(DataElement):
    """Code specifying the priority of a transport service."""

    code: str = "4219"
    title: str = "Transport service priority code"
    repr_line: str = "an..3"


class EDiscrepancyNatureIdentificationCode(DataElement):
    """Code specifying the identification used to define the nature of a discrepancy."""

    code: str = "4221"
    title: str = "Discrepancy nature identification code"
    repr_line: str = "an..3"


class EMarkingInstructionsCode(DataElement):
    """Code specifying instructions for marking."""

    code: str = "4233"
    title: str = "Marking instructions code"
    repr_line: str = "an..3"


class EPaymentArrangementCode(DataElement):
    """Code specifying the arrangements for a payment."""

    code: str = "4237"
    title: str = "Payment arrangement code"
    repr_line: str = "an..3"


class EPaymentTermsDescription(DataElement):
    """Free form description of the conditions of payment between the parties to a transaction."""

    code: str = "4276"
    title: str = "Payment terms description"
    repr_line: str = "an..35"


class EPaymentTermsDescriptionIdentifier(DataElement):
    """Identification of the terms of payment between the parties to a transaction (generic term)."""

    code: str = "4277"
    title: str = "Payment terms description identifier"
    repr_line: str = "an..17"


class EPaymentTermsTypeCodeQualifier(DataElement):
    """Code qualifying the type of payment terms."""

    code: str = "4279"
    title: str = "Payment terms type code qualifier"
    repr_line: str = "an..3"


class EChangeReasonDescription(DataElement):
    """Free form description of the reason for change."""

    code: str = "4294"
    title: str = "Change reason description"
    repr_line: str = "an..35"


class EChangeReasonDescriptionCode(DataElement):
    """Code specifying the reason for a change."""

    code: str = "4295"
    title: str = "Change reason description code"
    repr_line: str = "an..3"


class EResponseTypeCode(DataElement):
    """Code specifying the type of acknowledgment required or transmitted."""

    code: str = "4343"
    title: str = "Response type code"
    repr_line: str = "an..3"


class EResponseDescription(DataElement):
    """Free form description of a response."""

    code: str = "4344"
    title: str = "Response description"
    repr_line: str = "an..256"


class EResponseDescriptionCode(DataElement):
    """Code specifying a response."""

    code: str = "4345"
    title: str = "Response description code"
    repr_line: str = "an..3"


class EProductIdentifierCodeQualifier(DataElement):
    """Code qualifying the product identifier."""

    code: str = "4347"
    title: str = "Product identifier code qualifier"
    repr_line: str = "an..3"


class EBankOperationCode(DataElement):
    """Code specifying a bank operation."""

    code: str = "4383"
    title: str = "Bank operation code"
    repr_line: str = "an..3"


class EInstructionDescription(DataElement):
    """Free form description of an instruction."""

    code: str = "4400"
    title: str = "Instruction description"
    repr_line: str = "an..35"


class EInstructionDescriptionCode(DataElement):
    """Code specifying an instruction."""

    code: str = "4401"
    title: str = "Instruction description code"
    repr_line: str = "an..3"


class EInstructionTypeCodeQualifier(DataElement):
    """Code qualifying the type of instruction."""

    code: str = "4403"
    title: str = "Instruction type code qualifier"
    repr_line: str = "an..3"


class EStatusDescription(DataElement):
    """Free form description of a status."""

    code: str = "4404"
    title: str = "Status description"
    repr_line: str = "an..35"


class EStatusDescriptionCode(DataElement):
    """Code specifying a status."""

    code: str = "4405"
    title: str = "Status description code"
    repr_line: str = "an..3"


class ESampleProcessStepCode(DataElement):
    """Code specifying the step in the sample process."""

    code: str = "4407"
    title: str = "Sample process step code"
    repr_line: str = "an..3"


class ETestMethodIdentifier(DataElement):
    """To identify a method of testing."""

    code: str = "4415"
    title: str = "Test method identifier"
    repr_line: str = "an..17"


class ETestDescription(DataElement):
    """Free form description of the test."""

    code: str = "4416"
    title: str = "Test description"
    repr_line: str = "an..70"


class ETestAdministrationMethodCode(DataElement):
    """Code specifying the method of the administration of a test."""

    code: str = "4419"
    title: str = "Test administration method code"
    repr_line: str = "an..3"


class ETestReasonName(DataElement):
    """Name of the reason for performing a test."""

    code: str = "4424"
    title: str = "Test reason name"
    repr_line: str = "an..35"


class ETestReasonNameCode(DataElement):
    """Code specifying the name of the reason for performing a test."""

    code: str = "4425"
    title: str = "Test reason name code"
    repr_line: str = "an..17"


class EPaymentGuaranteeMeansCode(DataElement):
    """Code specifying the means of payment guarantee."""

    code: str = "4431"
    title: str = "Payment guarantee means code"
    repr_line: str = "an..3"


class EPaymentChannelCode(DataElement):
    """Code specifying the payment channel."""

    code: str = "4435"
    title: str = "Payment channel code"
    repr_line: str = "an..3"


class EAccountTypeCodeQualifier(DataElement):
    """Code qualifying the type of account."""

    code: str = "4437"
    title: str = "Account type code qualifier"
    repr_line: str = "an..3"


class EPaymentConditionsCode(DataElement):
    """Code specifying the payment conditions."""

    code: str = "4439"
    title: str = "Payment conditions code"
    repr_line: str = "an..3"


class EFreeText(DataElement):
    """Free form text."""

    code: str = "4440"
    title: str = "Free text"
    repr_line: str = "an..512"


class EFreeTextDescriptionCode(DataElement):
    """Code specifying free form text."""

    code: str = "4441"
    title: str = "Free text description code"
    repr_line: str = "an..17"


class EFreeTextFormatCode(DataElement):
    """Code specifying the format of free text."""

    code: str = "4447"
    title: str = "Free text format code"
    repr_line: str = "an..3"


class ETextSubjectCodeQualifier(DataElement):
    """Code qualifying the subject of the text."""

    code: str = "4451"
    title: str = "Text subject code qualifier"
    repr_line: str = "an..3"


class EFreeTextFunctionCode(DataElement):
    """Code specifying the function of free text."""

    code: str = "4453"
    title: str = "Free text function code"
    repr_line: str = "an..3"


class EBackOrderArrangementTypeCode(DataElement):
    """Code specifying a type of back order arrangement."""

    code: str = "4455"
    title: str = "Back order arrangement type code"
    repr_line: str = "an..3"


class ESubstitutionConditionCode(DataElement):
    """Code specifying the conditions under which substitution may take place."""

    code: str = "4457"
    title: str = "Substitution condition code"
    repr_line: str = "an..3"


class EPaymentMeansCode(DataElement):
    """Code identifying a means of payment."""

    code: str = "4461"
    title: str = "Payment means code"
    repr_line: str = "an..3"


class EIntracompanyPaymentIndicatorCode(DataElement):
    """Code indicating an intra-company payment."""

    code: str = "4463"
    title: str = "Intra-company payment indicator code"
    repr_line: str = "an..3"


class EAdjustmentReasonDescriptionCode(DataElement):
    """Code specifying the adjustment reason."""

    code: str = "4465"
    title: str = "Adjustment reason description code"
    repr_line: str = "an..3"


class EPaymentMethodCode(DataElement):
    """Code specifying a method of payment."""

    code: str = "4467"
    title: str = "Payment method code"
    repr_line: str = "an..4"


class EPaymentPurposeCode(DataElement):
    """Code identifying the purpose of a payment."""

    code: str = "4469"
    title: str = "Payment purpose code"
    repr_line: str = "an..4"


class ESettlementMeansCode(DataElement):
    """Code specifying the means of settlement."""

    code: str = "4471"
    title: str = "Settlement means code"
    repr_line: str = "an..3"


class EInformationType(DataElement):
    """Text representation of a type of information."""

    code: str = "4472"
    title: str = "Information type"
    repr_line: str = "an..35"


class EInformationTypeCode(DataElement):
    """Code specifying a type of information."""

    code: str = "4473"
    title: str = "Information type code"
    repr_line: str = "an..4"


class EAccountingEntryTypeName(DataElement):
    """Name of a type of accounting entry."""

    code: str = "4474"
    title: str = "Accounting entry type name"
    repr_line: str = "an..35"


class EAccountingEntryTypeNameCode(DataElement):
    """Code specifying a type of accounting entry."""

    code: str = "4475"
    title: str = "Accounting entry type name code"
    repr_line: str = "an..17"


class EFinancialTransactionTypeCode(DataElement):
    """Code specifying a type of financial transaction."""

    code: str = "4487"
    title: str = "Financial transaction type code"
    repr_line: str = "an..3"


class EDeliveryInstructionCode(DataElement):
    """Code specifying a delivery instruction."""

    code: str = "4493"
    title: str = "Delivery instruction code"
    repr_line: str = "an..3"


class EInsuranceCoverDescription(DataElement):
    """Free form description of the insurance cover."""

    code: str = "4494"
    title: str = "Insurance cover description"
    repr_line: str = "an..35"


class EInsuranceCoverDescriptionCode(DataElement):
    """Code specifying the insurance cover."""

    code: str = "4495"
    title: str = "Insurance cover description code"
    repr_line: str = "an..17"


class EInsuranceCoverTypeCode(DataElement):
    """Code specifying the meaning of the insurance cover."""

    code: str = "4497"
    title: str = "Insurance cover type code"
    repr_line: str = "an..3"


class EInventoryMovementReasonCode(DataElement):
    """Code specifying the reason for an inventory movement."""

    code: str = "4499"
    title: str = "Inventory movement reason code"
    repr_line: str = "an..3"


class EInventoryMovementDirectionCode(DataElement):
    """Code specifying the direction of an inventory movement."""

    code: str = "4501"
    title: str = "Inventory movement direction code"
    repr_line: str = "an..3"


class EInventoryBalanceMethodCode(DataElement):
    """Code specifying the method used to establish an inventory balance."""

    code: str = "4503"
    title: str = "Inventory balance method code"
    repr_line: str = "an..3"


class ECreditCoverRequestTypeCode(DataElement):
    """Code specifying the type of request for credit cover."""

    code: str = "4505"
    title: str = "Credit cover request type code"
    repr_line: str = "an..3"


class ECreditCoverResponseTypeCode(DataElement):
    """Code specifying the type of response to a request for credit cover."""

    code: str = "4507"
    title: str = "Credit cover response type code"
    repr_line: str = "an..3"


class ECreditCoverResponseReasonCode(DataElement):
    """Code specifying the reason for a response to a request for credit cover."""

    code: str = "4509"
    title: str = "Credit cover response reason code"
    repr_line: str = "an..3"


class ERequestedInformationDescription(DataElement):
    """Free form description of the response information requested."""

    code: str = "4510"
    title: str = "Requested information description"
    repr_line: str = "an..35"


class ERequestedInformationDescriptionCode(DataElement):
    """Code specifying the response information requested."""

    code: str = "4511"
    title: str = "Requested information description code"
    repr_line: str = "an..3"


class EMaintenanceOperationCode(DataElement):
    """Code specifying a maintenance operation."""

    code: str = "4513"
    title: str = "Maintenance operation code"
    repr_line: str = "an..3"


class ESealConditionCode(DataElement):
    """Code specifying the condition of a seal."""

    code: str = "4517"
    title: str = "Seal condition code"
    repr_line: str = "an..3"


class EDefinitionIdentifier(DataElement):
    """To identify a definition."""

    code: str = "4519"
    title: str = "Definition identifier"
    repr_line: str = "an..35"


class EPremiumCalculationComponentIdentifier(DataElement):
    """To identify a component affecting premium calculation."""

    code: str = "4521"
    title: str = "Premium calculation component identifier"
    repr_line: str = "an..17"


class EPremiumCalculationComponentValueCategoryIdentifier(DataElement):
    """To identify the value category of a premium calculation component."""

    code: str = "4522"
    title: str = "Premium calculation component value category identifier"
    repr_line: str = "an..35"


class ESealTypeCode(DataElement):
    """To specify a type of seal."""

    code: str = "4525"
    title: str = "Seal type code"
    repr_line: str = "an..3"


class EMonetaryAmount(DataElement):
    """To specify a monetary amount."""

    code: str = "5004"
    title: str = "Monetary amount"
    repr_line: str = "n..35"


class EMonetaryAmountFunctionDescription(DataElement):
    """Free form description of the monetary amount function."""

    code: str = "5006"
    title: str = "Monetary amount function description"
    repr_line: str = "an..70"


class EMonetaryAmountFunctionDescriptionCode(DataElement):
    """Code specifying the monetary amount function."""

    code: str = "5007"
    title: str = "Monetary amount function description code"
    repr_line: str = "an..3"


class EIndexCodeQualifier(DataElement):
    """Code qualifying an index."""

    code: str = "5013"
    title: str = "Index code qualifier"
    repr_line: str = "an..3"


class EMonetaryAmountTypeCodeQualifier(DataElement):
    """Code qualifying the type of monetary amount."""

    code: str = "5025"
    title: str = "Monetary amount type code qualifier"
    repr_line: str = "an..3"


class EIndexTypeIdentifier(DataElement):
    """To identify a type of index."""

    code: str = "5027"
    title: str = "Index type identifier"
    repr_line: str = "an..17"


class EIndexText(DataElement):
    """To specify the value of an index."""

    code: str = "5030"
    title: str = "Index text"
    repr_line: str = "an..35"


class EIndexRepresentationCode(DataElement):
    """Code specifying the representation of an index value."""

    code: str = "5039"
    title: str = "Index representation code"
    repr_line: str = "an..3"


class EContributionCodeQualifier(DataElement):
    """Code qualifying a contribution."""

    code: str = "5047"
    title: str = "Contribution code qualifier"
    repr_line: str = "an..3"


class EContributionTypeDescription(DataElement):
    """Free form description of a type of contribution scheme."""

    code: str = "5048"
    title: str = "Contribution type description"
    repr_line: str = "an..35"


class EContributionTypeDescriptionCode(DataElement):
    """Code specifying a type of contribution scheme."""

    code: str = "5049"
    title: str = "Contribution type description code"
    repr_line: str = "an..3"


class EMonetaryAmountFunctionDetailDescription(DataElement):
    """Free form description of the detail of a monetary amount function."""

    code: str = "5104"
    title: str = "Monetary amount function detail description"
    repr_line: str = "an..70"


class EMonetaryAmountFunctionDetailDescriptionCode(DataElement):
    """Code specifying the detail of a monetary amount function."""

    code: str = "5105"
    title: str = "Monetary amount function detail description code"
    repr_line: str = "an..17"


class EPriceAmount(DataElement):
    """To specify a price."""

    code: str = "5118"
    title: str = "Price amount"
    repr_line: str = "n..15"


class EPriceCodeQualifier(DataElement):
    """Code qualifying a price."""

    code: str = "5125"
    title: str = "Price code qualifier"
    repr_line: str = "an..3"


class EDutyOrTaxOrFeeTypeName(DataElement):
    """Name of a type of duty, tax or fee."""

    code: str = "5152"
    title: str = "Duty or tax or fee type name"
    repr_line: str = "an..35"


class EDutyOrTaxOrFeeTypeNameCode(DataElement):
    """Code specifying a type of duty, tax or fee."""

    code: str = "5153"
    title: str = "Duty or tax or fee type name code"
    repr_line: str = "an..3"


class ETotalMonetaryAmount(DataElement):
    """To specify a total monetary amount."""

    code: str = "5160"
    title: str = "Total monetary amount"
    repr_line: str = "n..20"


class EAllowanceOrChargeIdentificationCode(DataElement):
    """Code specifying the identification of an allowance or charge."""

    code: str = "5189"
    title: str = "Allowance or charge identification code"
    repr_line: str = "an..3"


class ESublineItemPriceChangeOperationCode(DataElement):
    """Code specifying the price change operation for a sub- line item."""

    code: str = "5213"
    title: str = "Sub-line item price change operation code"
    repr_line: str = "an..3"


class EChargeCategoryCode(DataElement):
    """Code specifying the category of charges."""

    code: str = "5237"
    title: str = "Charge category code"
    repr_line: str = "an..3"


class ERateOrTariffClassDescription(DataElement):
    """Free form description of an applicable rate or tariff class."""

    code: str = "5242"
    title: str = "Rate or tariff class description"
    repr_line: str = "an..35"


class ERateOrTariffClassDescriptionCode(DataElement):
    """Code specifying an applicable rate or tariff class."""

    code: str = "5243"
    title: str = "Rate or tariff class description code"
    repr_line: str = "an..9"


class EPercentageTypeCodeQualifier(DataElement):
    """Code qualifying the type of percentage."""

    code: str = "5245"
    title: str = "Percentage type code qualifier"
    repr_line: str = "an..3"


class EPercentageBasisIdentificationCode(DataElement):
    """Code specifying the basis on which a percentage is calculated."""

    code: str = "5249"
    title: str = "Percentage basis identification code"
    repr_line: str = "an..3"


class EChargeUnitCode(DataElement):
    """Code specifying a charge unit."""

    code: str = "5261"
    title: str = "Charge unit code"
    repr_line: str = "an..3"


class ERateTypeIdentifier(DataElement):
    """To identify a type of rate."""

    code: str = "5263"
    title: str = "Rate type identifier"
    repr_line: str = "an..20"


class EServiceTypeCode(DataElement):
    """Code specifying the type of service."""

    code: str = "5267"
    title: str = "Service type code"
    repr_line: str = "an..3"


class EDutyOrTaxOrFeeRateBasisCode(DataElement):
    """Code specifying the basis for a duty or tax or fee rate."""

    code: str = "5273"
    title: str = "Duty or tax or fee rate basis code"
    repr_line: str = "an..12"


class ESupplementaryRateOrTariffCode(DataElement):
    """Code specifying a supplementary rate or tariff."""

    code: str = "5275"
    title: str = "Supplementary rate or tariff code"
    repr_line: str = "an..6"


class EDutyOrTaxOrFeeRate(DataElement):
    """Rate of a duty or tax or fee."""

    code: str = "5278"
    title: str = "Duty or tax or fee rate"
    repr_line: str = "an..17"


class EDutyOrTaxOrFeeRateCode(DataElement):
    """Code specifying a rate of a duty or tax or fee."""

    code: str = "5279"
    title: str = "Duty or tax or fee rate code"
    repr_line: str = "an..7"


class EDutyOrTaxOrFeeFunctionCodeQualifier(DataElement):
    """Code qualifying the function of a duty or tax or fee."""

    code: str = "5283"
    title: str = "Duty or tax or fee function code qualifier"
    repr_line: str = "an..3"


class EUnitPriceBasisQuantity(DataElement):
    """To specify the basis for a unit price."""

    code: str = "5284"
    title: str = "Unit price basis quantity"
    repr_line: str = "n..9"


class EDutyOrTaxOrFeeAssessmentBasisQuantity(DataElement):
    """To specify the basis on which a duty or tax or fee will be assessed."""

    code: str = "5286"
    title: str = "Duty or tax or fee assessment basis quantity"
    repr_line: str = "an..15"


class EDutyOrTaxOrFeeAccountCode(DataElement):
    """Code specifying a duty or tax or fee account."""

    code: str = "5289"
    title: str = "Duty or tax or fee account code"
    repr_line: str = "an..6"


class EDutyOrTaxOrFeeCategoryCode(DataElement):
    """Code specifying a duty or tax or fee category."""

    code: str = "5305"
    title: str = "Duty or tax or fee category code"
    repr_line: str = "an..3"


class ETaxOrDutyOrFeePaymentDueDateCode(DataElement):
    """A code indicating when the duty, tax, or fee payment will be due."""

    code: str = "5307"
    title: str = "Tax or duty or fee payment due date code"
    repr_line: str = "an..3"


class ERemunerationTypeName(DataElement):
    """Name of a type of remuneration."""

    code: str = "5314"
    title: str = "Remuneration type name"
    repr_line: str = "an..35"


class ERemunerationTypeNameCode(DataElement):
    """Code specifying the name of a type of remuneration."""

    code: str = "5315"
    title: str = "Remuneration type name code"
    repr_line: str = "an..3"


class EPriceTypeCode(DataElement):
    """Code specifying the type of price."""

    code: str = "5375"
    title: str = "Price type code"
    repr_line: str = "an..3"


class EPriceChangeTypeCode(DataElement):
    """Code specifying the type of price change."""

    code: str = "5377"
    title: str = "Price change type code"
    repr_line: str = "an..3"


class EProductGroupTypeCode(DataElement):
    """Code specifying the type of product group."""

    code: str = "5379"
    title: str = "Product group type code"
    repr_line: str = "an..3"


class EPriceSpecificationCode(DataElement):
    """Code identifying pricing specification."""

    code: str = "5387"
    title: str = "Price specification code"
    repr_line: str = "an..3"


class EProductGroupName(DataElement):
    """Name of a product code."""

    code: str = "5388"
    title: str = "Product group name"
    repr_line: str = "an..35"


class EProductGroupNameCode(DataElement):
    """Code specifying the name of a product group."""

    code: str = "5389"
    title: str = "Product group name code"
    repr_line: str = "an..25"


class EPriceMultiplierTypeCodeQualifier(DataElement):
    """Code qualifying the type of price multiplier."""

    code: str = "5393"
    title: str = "Price multiplier type code qualifier"
    repr_line: str = "an..3"


class EPriceMultiplierRate(DataElement):
    """To specify the rate of a price multiplier."""

    code: str = "5394"
    title: str = "Price multiplier rate"
    repr_line: str = "n..12"


class ECurrencyExchangeRate(DataElement):
    """To specify the rate at which one specified currency is expressed in another specified currency."""

    code: str = "5402"
    title: str = "Currency exchange rate"
    repr_line: str = "n..12"


class ERateTypeCodeQualifier(DataElement):
    """Code qualifying the type of rate."""

    code: str = "5419"
    title: str = "Rate type code qualifier"
    repr_line: str = "an..3"


class EUnitPriceBasisRate(DataElement):
    """To specify the rate per unit specified in the unit price basis."""

    code: str = "5420"
    title: str = "Unit price basis rate"
    repr_line: str = "n..15"


class EAllowanceOrChargeCodeQualifier(DataElement):
    """Code qualifying an allowance or charge."""

    code: str = "5463"
    title: str = "Allowance or charge code qualifier"
    repr_line: str = "an..3"


class ERelationCode(DataElement):
    """Code specifying a relation."""

    code: str = "5479"
    title: str = "Relation code"
    repr_line: str = "an..3"


class EPercentage(DataElement):
    """To specify a percentage."""

    code: str = "5482"
    title: str = "Percentage"
    repr_line: str = "n..10"


class ESublineIndicatorCode(DataElement):
    """Code indicating a sub-line item."""

    code: str = "5495"
    title: str = "Sub-line indicator code"
    repr_line: str = "an..3"


class ERatePlanCode(DataElement):
    """Code specifying a rate plan."""

    code: str = "5501"
    title: str = "Rate plan code"
    repr_line: str = "an..3"


class ELatitudeDegree(DataElement):
    """To specify  the angular distance, measured in degrees, minutes, and seconds, north or south from the equator."""

    code: str = "6000"
    title: str = "Latitude degree"
    repr_line: str = "an..10"


class ELongitudeDegree(DataElement):
    """To specify the value of longitude i.e. the angular distance east or west on the earth's surface, measured by the angle and expressed in degrees, minutes, and seconds, which the meridian passing through a particular place makes with a standard or prime meridian."""

    code: str = "6002"
    title: str = "Longitude degree"
    repr_line: str = "an..11"


class EHeightMeasure(DataElement):
    """To specify the value of a height dimension."""

    code: str = "6008"
    title: str = "Height measure"
    repr_line: str = "n..15"


class EGeographicalPositionCodeQualifier(DataElement):
    """Code identifying the type of a geographical position."""

    code: str = "6029"
    title: str = "Geographical position code qualifier"
    repr_line: str = "an..3"


class EQuantity(DataElement):
    """Alphanumeric representation of a quantity."""

    code: str = "6060"
    title: str = "Quantity"
    repr_line: str = "an..35"


class EQuantityTypeCodeQualifier(DataElement):
    """Code qualifying the type of quantity."""

    code: str = "6063"
    title: str = "Quantity type code qualifier"
    repr_line: str = "an..3"


class EVarianceQuantity(DataElement):
    """To specify the value of a quantity variance."""

    code: str = "6064"
    title: str = "Variance quantity"
    repr_line: str = "n..15"


class EControlTotalQuantity(DataElement):
    """To specify the value of a control quantity."""

    code: str = "6066"
    title: str = "Control total quantity"
    repr_line: str = "n..18"


class EControlTotalTypeCodeQualifier(DataElement):
    """Code qualifying the type of control of hash total."""

    code: str = "6069"
    title: str = "Control total type code qualifier"
    repr_line: str = "an..3"


class EFrequencyCodeQualifier(DataElement):
    """Code qualifying the frequency."""

    code: str = "6071"
    title: str = "Frequency code qualifier"
    repr_line: str = "an..3"


class EFrequencyRate(DataElement):
    """The number of repetitions in a given time."""

    code: str = "6072"
    title: str = "Frequency rate"
    repr_line: str = "n..9"


class EConfidencePercent(DataElement):
    """To specify the confidence that a true value falls within a certain confidence interval expressed as a percentage."""

    code: str = "6074"
    title: str = "Confidence percent"
    repr_line: str = "n..6"


class EResultRepresentationCode(DataElement):
    """Code specifying the representation of a result."""

    code: str = "6077"
    title: str = "Result representation code"
    repr_line: str = "an..3"


class EResultNormalcyCode(DataElement):
    """Code specifying the degree of conformance to a standard."""

    code: str = "6079"
    title: str = "Result normalcy code"
    repr_line: str = "an..3"


class EDosageDescription(DataElement):
    """Free form description of a dosage."""

    code: str = "6082"
    title: str = "Dosage description"
    repr_line: str = "an..70"


class EDosageDescriptionIdentifier(DataElement):
    """Code identifying a dosage."""

    code: str = "6083"
    title: str = "Dosage description identifier"
    repr_line: str = "an..8"


class EDosageAdministrationCodeQualifier(DataElement):
    """Code qualifying the administration of a dosage."""

    code: str = "6085"
    title: str = "Dosage administration code qualifier"
    repr_line: str = "an..3"


class EResultValueTypeCodeQualifier(DataElement):
    """Code qualifying the type of a result value."""

    code: str = "6087"
    title: str = "Result value type code qualifier"
    repr_line: str = "an..3"


class EAltitude(DataElement):
    """The height of an object above sea level."""

    code: str = "6096"
    title: str = "Altitude"
    repr_line: str = "n..18"


class ELengthTypeCode(DataElement):
    """Code specifying the type of length."""

    code: str = "6113"
    title: str = "Length type code"
    repr_line: str = "an..3"


class EWidthMeasure(DataElement):
    """To specify the value of a width dimension."""

    code: str = "6140"
    title: str = "Width measure"
    repr_line: str = "n..15"


class EDimensionTypeCodeQualifier(DataElement):
    """Code qualifying the type of the dimension."""

    code: str = "6145"
    title: str = "Dimension type code qualifier"
    repr_line: str = "an..3"


class ERangeMaximumQuantity(DataElement):
    """To specify the maximum value of a range."""

    code: str = "6152"
    title: str = "Range maximum quantity"
    repr_line: str = "n..18"


class ENondiscreteMeasurementName(DataElement):
    """Name of a non-discrete measurement."""

    code: str = "6154"
    title: str = "Non-discrete measurement name"
    repr_line: str = "an..70"


class ENondiscreteMeasurementNameCode(DataElement):
    """Code specifying the name of a non-discrete measurement."""

    code: str = "6155"
    title: str = "Non-discrete measurement name code"
    repr_line: str = "an..17"


class ERangeMinimumQuantity(DataElement):
    """To specify the minimum value of a range."""

    code: str = "6162"
    title: str = "Range minimum quantity"
    repr_line: str = "n..18"


class ERangeTypeCodeQualifier(DataElement):
    """Code qualifying a type of range."""

    code: str = "6167"
    title: str = "Range type code qualifier"
    repr_line: str = "an..3"


class ELengthMeasure(DataElement):
    """To specify the value of a length dimension."""

    code: str = "6168"
    title: str = "Length measure"
    repr_line: str = "n..15"


class ESizeTypeCodeQualifier(DataElement):
    """Code qualifying a type of size."""

    code: str = "6173"
    title: str = "Size type code qualifier"
    repr_line: str = "an..3"


class ESizeMeasure(DataElement):
    """To specify a magnitude."""

    code: str = "6174"
    title: str = "Size measure"
    repr_line: str = "n..15"


class EOccurrencesMaximumNumber(DataElement):
    """To specify the maximum number of occurrences."""

    code: str = "6176"
    title: str = "Occurrences maximum number"
    repr_line: str = "n..7"


class EEditFieldLengthMeasure(DataElement):
    """To specify the length of a field for editing."""

    code: str = "6178"
    title: str = "Edit field length measure"
    repr_line: str = "n..3"


class EDiameterMeasure(DataElement):
    """To specify the value of a diameter dimension."""

    code: str = "6182"
    title: str = "Diameter measure"
    repr_line: str = "n..15"


class ETemperatureTypeCodeQualifier(DataElement):
    """Code qualifying the type of a temperature."""

    code: str = "6245"
    title: str = "Temperature type code qualifier"
    repr_line: str = "an..3"


class ETemperatureDegree(DataElement):
    """To specify the value of a temperature."""

    code: str = "6246"
    title: str = "Temperature degree"
    repr_line: str = "n..15"


class EMeasurementPurposeCodeQualifier(DataElement):
    """Code qualifying the purpose of the measurement."""

    code: str = "6311"
    title: str = "Measurement purpose code qualifier"
    repr_line: str = "an..3"


class EMeasuredAttributeCode(DataElement):
    """Code specifying the attribute measured."""

    code: str = "6313"
    title: str = "Measured attribute code"
    repr_line: str = "an..3"


class EMeasure(DataElement):
    """To specify the value of a measurement."""

    code: str = "6314"
    title: str = "Measure"
    repr_line: str = "an..18"


class EMeasurementSignificanceCode(DataElement):
    """Code specifying the significance of a measurement."""

    code: str = "6321"
    title: str = "Measurement significance code"
    repr_line: str = "an..3"


class EStatisticTypeCodeQualifier(DataElement):
    """Code qualifying the type of a statistic."""

    code: str = "6331"
    title: str = "Statistic type code qualifier"
    repr_line: str = "an..3"


class EExchangeRateCurrencyMarketIdentifier(DataElement):
    """To identify an exchange rate currency market."""

    code: str = "6341"
    title: str = "Exchange rate currency market identifier"
    repr_line: str = "an..3"


class ECurrencyTypeCodeQualifier(DataElement):
    """Code qualifying the type of currency."""

    code: str = "6343"
    title: str = "Currency type code qualifier"
    repr_line: str = "an..3"


class ECurrencyIdentificationCode(DataElement):
    """Code specifying a monetary unit."""

    code: str = "6345"
    title: str = "Currency identification code"
    repr_line: str = "an..3"


class ECurrencyUsageCodeQualifier(DataElement):
    """Code qualifying the usage of a currency."""

    code: str = "6347"
    title: str = "Currency usage code qualifier"
    repr_line: str = "an..3"


class ECurrencyRate(DataElement):
    """To specify the value of the multiplication factor used in expressing currency units."""

    code: str = "6348"
    title: str = "Currency rate"
    repr_line: str = "n..4"


class EUnitsQuantity(DataElement):
    """To specify the number of units."""

    code: str = "6350"
    title: str = "Units quantity"
    repr_line: str = "n..15"


class EUnitTypeCodeQualifier(DataElement):
    """Code qualifying the type of unit."""

    code: str = "6353"
    title: str = "Unit type code qualifier"
    repr_line: str = "an..3"


class EMeasurementUnitName(DataElement):
    """Name of a measurement unit."""

    code: str = "6410"
    title: str = "Measurement unit name"
    repr_line: str = "an..35"


class EMeasurementUnitCode(DataElement):
    """Code specifying the unit of measurement."""

    code: str = "6411"
    title: str = "Measurement unit code"
    repr_line: str = "an..8"


class EClinicalInformationDescription(DataElement):
    """Free form description of an item of clinical information."""

    code: str = "6412"
    title: str = "Clinical information description"
    repr_line: str = "an..70"


class EClinicalInformationDescriptionIdentifier(DataElement):
    """Code identifying an item of clinical information."""

    code: str = "6413"
    title: str = "Clinical information description identifier"
    repr_line: str = "an..17"


class EClinicalInformationTypeCodeQualifier(DataElement):
    """Code qualifying the type of clinical information."""

    code: str = "6415"
    title: str = "Clinical information type code qualifier"
    repr_line: str = "an..3"


class EProcessStagesQuantity(DataElement):
    """Count of the number of process stages."""

    code: str = "6426"
    title: str = "Process stages quantity"
    repr_line: str = "n..2"


class EProcessStagesActualQuantity(DataElement):
    """Count of  the actual number of process stages."""

    code: str = "6428"
    title: str = "Process stages actual quantity"
    repr_line: str = "n..2"


class ESignificantDigitsQuantity(DataElement):
    """Count of the number of significant digits."""

    code: str = "6432"
    title: str = "Significant digits quantity"
    repr_line: str = "n..2"


class EStatisticalConceptIdentifier(DataElement):
    """Free form identification of a statistical concept."""

    code: str = "6434"
    title: str = "Statistical concept identifier"
    repr_line: str = "an..35"


class EPhysicalOrLogicalStateTypeCodeQualifier(DataElement):
    """Code qualifying the type of physical or logical state."""

    code: str = "7001"
    title: str = "Physical or logical state type code qualifier"
    repr_line: str = "an..3"


class EPhysicalOrLogicalStateDescription(DataElement):
    """Free form description of a physical or logical state."""

    code: str = "7006"
    title: str = "Physical or logical state description"
    repr_line: str = "an..70"


class EPhysicalOrLogicalStateDescriptionCode(DataElement):
    """Code specifying a physical or logical state."""

    code: str = "7007"
    title: str = "Physical or logical state description code"
    repr_line: str = "an..3"


class EItemDescription(DataElement):
    """Free form description of an item."""

    code: str = "7008"
    title: str = "Item description"
    repr_line: str = "an..256"


class EItemDescriptionCode(DataElement):
    """Code specifying an item."""

    code: str = "7009"
    title: str = "Item description code"
    repr_line: str = "an..17"


class EItemAvailabilityCode(DataElement):
    """Code specifying the availability of an item."""

    code: str = "7011"
    title: str = "Item availability code"
    repr_line: str = "an..3"


class ECharacteristicDescription(DataElement):
    """Free form description of a characteristic."""

    code: str = "7036"
    title: str = "Characteristic description"
    repr_line: str = "an..35"


class ECharacteristicDescriptionCode(DataElement):
    """A code specifying a characteristic."""

    code: str = "7037"
    title: str = "Characteristic description code"
    repr_line: str = "an..17"


class ESampleSelectionMethodCode(DataElement):
    """Code specifying the selection method for a sample."""

    code: str = "7039"
    title: str = "Sample selection method code"
    repr_line: str = "an..3"


class EPowerTypeDescription(DataElement):
    """Description of the type of power."""

    code: str = "7040"
    title: str = "Power type description"
    repr_line: str = "an..17"


class EPowerTypeCode(DataElement):
    """Code indicating the type of power."""

    code: str = "7041"
    title: str = "Power type code"
    repr_line: str = "an..3"


class ESampleStateCode(DataElement):
    """Code specifying the state of a sample."""

    code: str = "7045"
    title: str = "Sample state code"
    repr_line: str = "an..3"


class ESampleDirectionCode(DataElement):
    """Code specifying the direction in which a sample was taken."""

    code: str = "7047"
    title: str = "Sample direction code"
    repr_line: str = "an..3"


class EClassTypeCode(DataElement):
    """Code specifying the type of class."""

    code: str = "7059"
    title: str = "Class type code"
    repr_line: str = "an..3"


class ETypeOfPackages(DataElement):
    """Description of the form in which goods are presented."""

    code: str = "7064"
    title: str = "Type of packages"
    repr_line: str = "an..35"


class EPackageTypeDescriptionCode(DataElement):
    """Code specifying the type of package."""

    code: str = "7065"
    title: str = "Package type description code"
    repr_line: str = "an..17"


class EPackagingTermsAndConditionsCode(DataElement):
    """Code specifying the packaging terms and conditions."""

    code: str = "7073"
    title: str = "Packaging terms and conditions code"
    repr_line: str = "an..3"


class EPackagingLevelCode(DataElement):
    """Code specifying a level of packaging."""

    code: str = "7075"
    title: str = "Packaging level code"
    repr_line: str = "an..3"


class EDescriptionFormatCode(DataElement):
    """Code specifying the format of a description."""

    code: str = "7077"
    title: str = "Description format code"
    repr_line: str = "an..3"


class EItemCharacteristicCode(DataElement):
    """Code specifying the characteristic of an item."""

    code: str = "7081"
    title: str = "Item characteristic code"
    repr_line: str = "an..3"


class EConfigurationOperationCode(DataElement):
    """Code specifying the configuration operation."""

    code: str = "7083"
    title: str = "Configuration operation code"
    repr_line: str = "an..3"


class ECargoTypeClassificationCode(DataElement):
    """Code specifying the classification of a type of cargo."""

    code: str = "7085"
    title: str = "Cargo type classification code"
    repr_line: str = "an..3"


class EDangerousGoodsFlashpointDescription(DataElement):
    """To describe the flashpoint of dangerous goods."""

    code: str = "7088"
    title: str = "Dangerous goods flashpoint description"
    repr_line: str = "an..8"


class EShippingMarksDescription(DataElement):
    """Free form description of the shipping marks."""

    code: str = "7102"
    title: str = "Shipping marks description"
    repr_line: str = "an..35"


class EShipmentFlashpointDegree(DataElement):
    """To specify the value of the flashpoint of a shipment."""

    code: str = "7106"
    title: str = "Shipment flashpoint degree"
    repr_line: str = "n3"


class ECharacteristicValueDescription(DataElement):
    """Free form description of the value of a characteristic."""

    code: str = "7110"
    title: str = "Characteristic value description"
    repr_line: str = "an..35"


class ECharacteristicValueDescriptionCode(DataElement):
    """Code specifying the value of a characteristic."""

    code: str = "7111"
    title: str = "Characteristic value description code"
    repr_line: str = "an..3"


class EUnitedNationsDangerousGoodsUndgIdentifier(DataElement):
    """The unique serial number assigned within the United Nations to substances and articles contained in a list of the dangerous goods most commonly carried."""

    code: str = "7124"
    title: str = "United nations dangerous goods (UNDG) identifier"
    repr_line: str = "n4"


class ECustomerShipmentAuthorisationIdentifier(DataElement):
    """To identify the authorisation to ship issued by the customer."""

    code: str = "7130"
    title: str = "Customer shipment authorisation identifier"
    repr_line: str = "an..17"


class EProductDetailsTypeCodeQualifier(DataElement):
    """Code qualifying a type of product details."""

    code: str = "7133"
    title: str = "Product details type code qualifier"
    repr_line: str = "an..3"


class EProductName(DataElement):
    """Name identifying a product."""

    code: str = "7134"
    title: str = "Product name"
    repr_line: str = "an..35"


class EProductIdentifier(DataElement):
    """To identify a product."""

    code: str = "7135"
    title: str = "Product identifier"
    repr_line: str = "an..35"


class EProductCharacteristicIdentificationCode(DataElement):
    """Code specifying the identification of a product characteristic."""

    code: str = "7139"
    title: str = "Product characteristic identification code"
    repr_line: str = "an..3"


class EItemIdentifier(DataElement):
    """To identify an item."""

    code: str = "7140"
    title: str = "Item identifier"
    repr_line: str = "an..35"


class EItemTypeIdentificationCode(DataElement):
    """Coded identification of an item type."""

    code: str = "7143"
    title: str = "Item type identification code"
    repr_line: str = "an..3"


class ESpecialServiceDescription(DataElement):
    """Free form description of a special service."""

    code: str = "7160"
    title: str = "Special service description"
    repr_line: str = "an..35"


class ESpecialServiceDescriptionCode(DataElement):
    """Code specifying a special service."""

    code: str = "7161"
    title: str = "Special service description code"
    repr_line: str = "an..3"


class EHierarchicalStructureLevelIdentifier(DataElement):
    """To identify a level within a hierarchical structure."""

    code: str = "7164"
    title: str = "Hierarchical structure level identifier"
    repr_line: str = "an..35"


class EHierarchicalStructureParentIdentifier(DataElement):
    """To identify the next higher level in a hierarchical structure."""

    code: str = "7166"
    title: str = "Hierarchical structure parent identifier"
    repr_line: str = "an..35"


class ELevelNumber(DataElement):
    """Number identifying a level."""

    code: str = "7168"
    title: str = "Level number"
    repr_line: str = "n..3"


class EHierarchicalStructureRelationshipCode(DataElement):
    """Code specifying the relationship between the hierarchical object and an identified object."""

    code: str = "7171"
    title: str = "Hierarchical structure relationship code"
    repr_line: str = "an..3"


class EHierarchyObjectCodeQualifier(DataElement):
    """Code qualifying an object in a hierarchy."""

    code: str = "7173"
    title: str = "Hierarchy object code qualifier"
    repr_line: str = "an..3"


class ERulePartIdentifier(DataElement):
    """To identify a part of a rule."""

    code: str = "7175"
    title: str = "Rule part identifier"
    repr_line: str = "an..7"


class ERiskObjectSubtypeDescription(DataElement):
    """Free form description of the object sub-type of a risk."""

    code: str = "7176"
    title: str = "Risk object sub-type description"
    repr_line: str = "an..70"


class ERiskObjectSubtypeDescriptionIdentifier(DataElement):
    """Code identifying the object sub-type of a risk."""

    code: str = "7177"
    title: str = "Risk object sub-type description identifier"
    repr_line: str = "an..17"


class ERiskObjectTypeIdentifier(DataElement):
    """Code identifying a type of risk object."""

    code: str = "7179"
    title: str = "Risk object type identifier"
    repr_line: str = "an..17"


class EProcessTypeDescription(DataElement):
    """Free form description of a type of process."""

    code: str = "7186"
    title: str = "Process type description"
    repr_line: str = "an..35"


class EProcessTypeDescriptionCode(DataElement):
    """Code specifying a type of process."""

    code: str = "7187"
    title: str = "Process type description code"
    repr_line: str = "an..17"


class ETestMethodRevisionIdentifier(DataElement):
    """To identify the revision of a test method."""

    code: str = "7188"
    title: str = "Test method revision identifier"
    repr_line: str = "an..30"


class EProcessDescription(DataElement):
    """Free form description of a process."""

    code: str = "7190"
    title: str = "Process description"
    repr_line: str = "an..70"


class EProcessDescriptionCode(DataElement):
    """Code specifying a process."""

    code: str = "7191"
    title: str = "Process description code"
    repr_line: str = "an..17"


class EPackageQuantity(DataElement):
    """To specify the number of packages."""

    code: str = "7224"
    title: str = "Package quantity"
    repr_line: str = "n..8"


class EPackagingRelatedDescriptionCode(DataElement):
    """Code specifying information related to packaging."""

    code: str = "7233"
    title: str = "Packaging related description code"
    repr_line: str = "an..3"


class EItemTotalQuantity(DataElement):
    """Count of the total number of items."""

    code: str = "7240"
    title: str = "Item total quantity"
    repr_line: str = "n..15"


class EServiceRequirementCode(DataElement):
    """Code specifying a service requirement."""

    code: str = "7273"
    title: str = "Service requirement code"
    repr_line: str = "an..3"


class ESectorAreaIdentificationCodeQualifier(DataElement):
    """Code qualifying identification of a subject area."""

    code: str = "7293"
    title: str = "Sector area identification code qualifier"
    repr_line: str = "an..3"


class ERequirementOrConditionDescription(DataElement):
    """Free form description of a requirement or condition."""

    code: str = "7294"
    title: str = "Requirement or condition description"
    repr_line: str = "an..35"


class ERequirementOrConditionDescriptionIdentifier(DataElement):
    """Code specifying a requirement or condition."""

    code: str = "7295"
    title: str = "Requirement or condition description identifier"
    repr_line: str = "an..17"


class ESetTypeCodeQualifier(DataElement):
    """Code qualifying the type of set."""

    code: str = "7297"
    title: str = "Set type code qualifier"
    repr_line: str = "an..3"


class ERequirementDesignatorCode(DataElement):
    """Code specifying the requirement designator."""

    code: str = "7299"
    title: str = "Requirement designator code"
    repr_line: str = "an..3"


class ECommodityIdentificationCode(DataElement):
    """Code identifying a commodity for Customs, transport or statistical purposes (generic term)."""

    code: str = "7357"
    title: str = "Commodity identification code"
    repr_line: str = "an..18"


class ECustomsGoodsIdentifier(DataElement):
    """Code identifying the goods for customs."""

    code: str = "7361"
    title: str = "Customs goods identifier"
    repr_line: str = "an..18"


class EProcessingIndicatorDescription(DataElement):
    """Free form description of a processing indicator."""

    code: str = "7364"
    title: str = "Processing indicator description"
    repr_line: str = "an..35"


class EProcessingIndicatorDescriptionCode(DataElement):
    """Code specifying a processing indicator."""

    code: str = "7365"
    title: str = "Processing indicator description code"
    repr_line: str = "an..3"


class ESurfaceOrLayerCode(DataElement):
    """Code specifying the surface or layer of an object."""

    code: str = "7383"
    title: str = "Surface or layer code"
    repr_line: str = "an..3"


class EObjectIdentifier(DataElement):
    """Code specifying the unique identity of an object."""

    code: str = "7402"
    title: str = "Object identifier"
    repr_line: str = "an..35"


class EObjectIdentificationCodeQualifier(DataElement):
    """Code qualifying the identification of an object."""

    code: str = "7405"
    title: str = "Object identification code qualifier"
    repr_line: str = "an..3"


class EHazardousMaterialCategoryName(DataElement):
    """Name of a kind of hazard for a material."""

    code: str = "7418"
    title: str = "Hazardous material category name"
    repr_line: str = "an..35"


class EHazardousMaterialCategoryNameCode(DataElement):
    """Code specifying a kind of hazard for a material."""

    code: str = "7419"
    title: str = "Hazardous material category name code"
    repr_line: str = "an..7"


class EIndexingStructureCodeQualifier(DataElement):
    """Code qualifying an indexing structure."""

    code: str = "7429"
    title: str = "Indexing structure code qualifier"
    repr_line: str = "an..3"


class EAgreementTypeCodeQualifier(DataElement):
    """Code qualifying the type of agreement."""

    code: str = "7431"
    title: str = "Agreement type code qualifier"
    repr_line: str = "an..3"


class EAgreementTypeDescriptionCode(DataElement):
    """Code specifying the type of agreement."""

    code: str = "7433"
    title: str = "Agreement type description code"
    repr_line: str = "an..3"


class EAgreementTypeDescription(DataElement):
    """Free form description of the type of agreement."""

    code: str = "7434"
    title: str = "Agreement type description"
    repr_line: str = "an..70"


class ELevelOneIdentifier(DataElement):
    """To identify the first facet of a sequencing mechanism used to position an item within an indexing structure."""

    code: str = "7436"
    title: str = "Level one identifier"
    repr_line: str = "an..17"


class ELevelTwoIdentifier(DataElement):
    """To identify the second facet of a sequencing mechanism used to position an item within an indexing structure."""

    code: str = "7438"
    title: str = "Level two identifier"
    repr_line: str = "an..17"


class ELevelThreeIdentifier(DataElement):
    """To identify the third facet of a sequencing mechanism used to position an item within an indexing structure."""

    code: str = "7440"
    title: str = "Level three identifier"
    repr_line: str = "an..17"


class ELevelFourIdentifier(DataElement):
    """To identify the fourth facet of a sequencing mechanism used to position an item within an indexing structure."""

    code: str = "7442"
    title: str = "Level four identifier"
    repr_line: str = "an..17"


class ELevelFiveIdentifier(DataElement):
    """To identify the fifth facet of a sequencing mechanism used to position an item within an indexing structure."""

    code: str = "7444"
    title: str = "Level five identifier"
    repr_line: str = "an..17"


class ELevelSixIdentifier(DataElement):
    """To identify the sixth facet of a sequencing mechanism used to position an item within an indexing structure."""

    code: str = "7446"
    title: str = "Level six identifier"
    repr_line: str = "an..17"


class EMembershipTypeCodeQualifier(DataElement):
    """Code qualifying the type of membership."""

    code: str = "7449"
    title: str = "Membership type code qualifier"
    repr_line: str = "an..3"


class EMembershipCategoryDescription(DataElement):
    """Free form description of a membership category."""

    code: str = "7450"
    title: str = "Membership category description"
    repr_line: str = "an..35"


class EMembershipCategoryDescriptionCode(DataElement):
    """Code specifying a membership category."""

    code: str = "7451"
    title: str = "Membership category description code"
    repr_line: str = "an..4"


class EMembershipStatusDescription(DataElement):
    """Free form description of a membership status."""

    code: str = "7452"
    title: str = "Membership status description"
    repr_line: str = "an..35"


class EMembershipStatusDescriptionCode(DataElement):
    """Code specifying a membership status."""

    code: str = "7453"
    title: str = "Membership status description code"
    repr_line: str = "an..3"


class EMembershipLevelCodeQualifier(DataElement):
    """Code qualifying the level of membership."""

    code: str = "7455"
    title: str = "Membership level code qualifier"
    repr_line: str = "an..3"


class EMembershipLevelDescription(DataElement):
    """Free form description of a level of membership."""

    code: str = "7456"
    title: str = "Membership level description"
    repr_line: str = "an..35"


class EMembershipLevelDescriptionCode(DataElement):
    """Code specifying a level of membership."""

    code: str = "7457"
    title: str = "Membership level description code"
    repr_line: str = "an..9"


class EAttendeeCategoryDescription(DataElement):
    """Free form description of a category attendee."""

    code: str = "7458"
    title: str = "Attendee category description"
    repr_line: str = "an..35"


class EAttendeeCategoryDescriptionCode(DataElement):
    """Code specifying a category of attendee."""

    code: str = "7459"
    title: str = "Attendee category description code"
    repr_line: str = "an..3"


class EInventoryTypeCode(DataElement):
    """Code specifying a type of inventory."""

    code: str = "7491"
    title: str = "Inventory type code"
    repr_line: str = "an..3"


class EDamageDetailsCodeQualifier(DataElement):
    """Code qualifying the damage details."""

    code: str = "7493"
    title: str = "Damage details code qualifier"
    repr_line: str = "an..3"


class EObjectTypeCodeQualifier(DataElement):
    """Code qualifying a type of object."""

    code: str = "7495"
    title: str = "Object type code qualifier"
    repr_line: str = "an..3"


class EStructureComponentFunctionCodeQualifier(DataElement):
    """Code qualifying the function of a structure component."""

    code: str = "7497"
    title: str = "Structure component function code qualifier"
    repr_line: str = "an..3"


class EDamageTypeDescription(DataElement):
    """Free form description of the type of damage to an object."""

    code: str = "7500"
    title: str = "Damage type description"
    repr_line: str = "an..35"


class EDamageTypeDescriptionCode(DataElement):
    """Code specifying the type of damage to an object."""

    code: str = "7501"
    title: str = "Damage type description code"
    repr_line: str = "an..3"


class EDamageAreaDescription(DataElement):
    """Free form description of where the damage is on an object."""

    code: str = "7502"
    title: str = "Damage area description"
    repr_line: str = "an..35"


class EDamageAreaDescriptionCode(DataElement):
    """Code specifying where the damage is on an object."""

    code: str = "7503"
    title: str = "Damage area description code"
    repr_line: str = "an..4"


class EUnitOrComponentTypeDescription(DataElement):
    """Free form description of a type of unit or component."""

    code: str = "7504"
    title: str = "Unit or component type description"
    repr_line: str = "an..35"


class EUnitOrComponentTypeDescriptionCode(DataElement):
    """Code specifying a type of unit or component."""

    code: str = "7505"
    title: str = "Unit or component type description code"
    repr_line: str = "an..3"


class EComponentMaterialDescription(DataElement):
    """Free form description of a component material."""

    code: str = "7506"
    title: str = "Component material description"
    repr_line: str = "an..35"


class EComponentMaterialDescriptionCode(DataElement):
    """Code specifying a component material."""

    code: str = "7507"
    title: str = "Component material description code"
    repr_line: str = "an..3"


class EDamageSeverityDescription(DataElement):
    """Free form description of the severity of damage."""

    code: str = "7508"
    title: str = "Damage severity description"
    repr_line: str = "an..35"


class EDamageSeverityDescriptionCode(DataElement):
    """Code specifying the severity of damage."""

    code: str = "7509"
    title: str = "Damage severity description code"
    repr_line: str = "an..3"


class EMarkingTypeCode(DataElement):
    """Code specifying the type of marking."""

    code: str = "7511"
    title: str = "Marking type code"
    repr_line: str = "an..3"


class EStructureComponentIdentifier(DataElement):
    """To identify a component of a structure."""

    code: str = "7512"
    title: str = "Structure component identifier"
    repr_line: str = "an..35"


class EStructureTypeCode(DataElement):
    """Code specifying a type of structure."""

    code: str = "7515"
    title: str = "Structure type code"
    repr_line: str = "an..3"


class EBenefitAndCoverageCode(DataElement):
    """Code used to identify the benefit and coverage."""

    code: str = "7517"
    title: str = "Benefit and coverage code"
    repr_line: str = "an..3"


class ETrafficRestrictionCode(DataElement):
    """Code specifying a traffic restriction."""

    code: str = "8015"
    title: str = "Traffic restriction code"
    repr_line: str = "an..3"


class ETrafficRestrictionApplicationCode(DataElement):
    """Code specifying the application of a restriction to traffic."""

    code: str = "8017"
    title: str = "Traffic restriction application code"
    repr_line: str = "an..3"


class EFreightAndOtherChargesDescription(DataElement):
    """Free form description of freight and other charges."""

    code: str = "8022"
    title: str = "Freight and other charges description"
    repr_line: str = "an..26"


class EFreightAndOtherChargesDescriptionIdentifier(DataElement):
    """Code identifying freight and other charges."""

    code: str = "8023"
    title: str = "Freight and other charges description identifier"
    repr_line: str = "an..17"


class EConveyanceCallPurposeDescription(DataElement):
    """Free form description of the purpose of the conveyance call."""

    code: str = "8024"
    title: str = "Conveyance call purpose description"
    repr_line: str = "an..35"


class EConveyanceCallPurposeDescriptionCode(DataElement):
    """Code specifying the purpose of the conveyance call."""

    code: str = "8025"
    title: str = "Conveyance call purpose description code"
    repr_line: str = "an..3"


class EMeansOfTransportJourneyIdentifier(DataElement):
    """To identify a journey of a means of transport."""

    code: str = "8028"
    title: str = "Means of transport journey identifier"
    repr_line: str = "an..17"


class ETrafficRestrictionTypeCodeQualifier(DataElement):
    """Code qualifying a type of traffic restriction."""

    code: str = "8035"
    title: str = "Traffic restriction type code qualifier"
    repr_line: str = "an..3"


class ETransportStageCodeQualifier(DataElement):
    """Code qualifying a specific stage of transport."""

    code: str = "8051"
    title: str = "Transport stage code qualifier"
    repr_line: str = "an..3"


class EEquipmentTypeCodeQualifier(DataElement):
    """Code qualifying a type of equipment."""

    code: str = "8053"
    title: str = "Equipment type code qualifier"
    repr_line: str = "an..3"


class ETransportModeName(DataElement):
    """Name of a mode of transport."""

    code: str = "8066"
    title: str = "Transport mode name"
    repr_line: str = "an..17"


class ETransportModeNameCode(DataElement):
    """Code specifying the name of a mode of transport."""

    code: str = "8067"
    title: str = "Transport mode name code"
    repr_line: str = "an..3"


class EEquipmentSupplierCode(DataElement):
    """Code specifying the party that is the supplier of the equipment."""

    code: str = "8077"
    title: str = "Equipment supplier code"
    repr_line: str = "an..3"


class EAdditionalHazardClassificationIdentifier(DataElement):
    """To identify an additional hazard classification."""

    code: str = "8078"
    title: str = "Additional hazard classification identifier"
    repr_line: str = "an..7"


class EHazardCodeVersionIdentifier(DataElement):
    """To identify the version number of a hazard code."""

    code: str = "8092"
    title: str = "Hazard code version identifier"
    repr_line: str = "an..10"


class ETransitDirectionIndicatorCode(DataElement):
    """Code specifying the direction of transport."""

    code: str = "8101"
    title: str = "Transit direction indicator code"
    repr_line: str = "an..3"


class ETransportEmergencyCardIdentifier(DataElement):
    """To identify a transport emergency (TREM) card."""

    code: str = "8126"
    title: str = "Transport emergency card identifier"
    repr_line: str = "an..10"


class EEquipmentSizeAndTypeDescription(DataElement):
    """Free form description of the size and type of equipment."""

    code: str = "8154"
    title: str = "Equipment size and type description"
    repr_line: str = "an..35"


class EEquipmentSizeAndTypeDescriptionCode(DataElement):
    """Code specifying the size and type of equipment."""

    code: str = "8155"
    title: str = "Equipment size and type description code"
    repr_line: str = "an..10"


class EOrangeHazardPlacardUpperPartIdentifier(DataElement):
    """To specify the identity number for the upper part of the orange hazard placard required on the means of transport."""

    code: str = "8158"
    title: str = "Orange hazard placard upper part identifier"
    repr_line: str = "an..4"


class EFullOrEmptyIndicatorCode(DataElement):
    """Code indicating whether an object is full or empty."""

    code: str = "8169"
    title: str = "Full or empty indicator code"
    repr_line: str = "an..3"


class ETransportMeansDescription(DataElement):
    """Free form description of the means of transport."""

    code: str = "8178"
    title: str = "Transport means description"
    repr_line: str = "an..17"


class ETransportMeansDescriptionCode(DataElement):
    """Code specifying the means of transport."""

    code: str = "8179"
    title: str = "Transport means description code"
    repr_line: str = "an..8"


class EOrangeHazardPlacardLowerPartIdentifier(DataElement):
    """To specify the identity number for the lower part of the orange hazard placard required on the means of transport."""

    code: str = "8186"
    title: str = "Orange hazard placard lower part identifier"
    repr_line: str = "an4"


class EHazardousCargoTransportAuthorisationCode(DataElement):
    """Code specifying the authorisation for the transportation of hazardous cargo."""

    code: str = "8211"
    title: str = "Hazardous cargo transport authorisation code"
    repr_line: str = "an..3"


class ETransportMeansIdentificationName(DataElement):
    """Name identifying a means of transport."""

    code: str = "8212"
    title: str = "Transport means identification name"
    repr_line: str = "an..70"


class ETransportMeansIdentificationNameIdentifier(DataElement):
    """Identifies the name of the transport means."""

    code: str = "8213"
    title: str = "Transport means identification name identifier"
    repr_line: str = "an..35"


class ETransportMeansChangeIndicatorCode(DataElement):
    """Code indicating a change of means of transport."""

    code: str = "8215"
    title: str = "Transport means change indicator code"
    repr_line: str = "an1"


class EJourneyStopsQuantity(DataElement):
    """To specify the number of stops in a journey."""

    code: str = "8216"
    title: str = "Journey stops quantity"
    repr_line: str = "n..3"


class ETravellerAccompaniedByInfantIndicatorCode(DataElement):
    """Code indicating whether a traveller is accompanied by an infant."""

    code: str = "8219"
    title: str = "Traveller accompanied by infant indicator code"
    repr_line: str = "an1"


class EDangerousGoodsMarkingIdentifier(DataElement):
    """To identify the marking of dangerous goods."""

    code: str = "8246"
    title: str = "Dangerous goods marking identifier"
    repr_line: str = "an..4"


class EEquipmentStatusCode(DataElement):
    """Code specifying the status of equipment."""

    code: str = "8249"
    title: str = "Equipment status code"
    repr_line: str = "an..3"


class EPackingInstructionTypeCode(DataElement):
    """Code specifying a type of packing instruction."""

    code: str = "8255"
    title: str = "Packing instruction type code"
    repr_line: str = "an..3"


class EEquipmentIdentifier(DataElement):
    """To identify equipment."""

    code: str = "8260"
    title: str = "Equipment identifier"
    repr_line: str = "an..17"


class EDangerousGoodsRegulationsCode(DataElement):
    """Code specifying a dangerous goods regulation."""

    code: str = "8273"
    title: str = "Dangerous goods regulations code"
    repr_line: str = "an..3"


class EContainerOrPackageContentsIndicatorCode(DataElement):
    """Code indicating the contents of container or package."""

    code: str = "8275"
    title: str = "Container or package contents indicator code"
    repr_line: str = "an..3"


class ETransportMeansOwnershipIndicatorCode(DataElement):
    """Code indicating the ownership of a means of transport."""

    code: str = "8281"
    title: str = "Transport means ownership indicator code"
    repr_line: str = "an..3"


class ETransportMovementCode(DataElement):
    """Code specifying the transport movement."""

    code: str = "8323"
    title: str = "Transport movement code"
    repr_line: str = "an..3"


class EEquipmentPlanDescription(DataElement):
    """Free form description of the equipment plan."""

    code: str = "8332"
    title: str = "Equipment plan description"
    repr_line: str = "an..26"


class EMovementTypeDescription(DataElement):
    """Free form description of a type of movement."""

    code: str = "8334"
    title: str = "Movement type description"
    repr_line: str = "an..35"


class EMovementTypeDescriptionCode(DataElement):
    """Code specifying a type of movement."""

    code: str = "8335"
    title: str = "Movement type description code"
    repr_line: str = "an..3"


class EPackagingDangerLevelCode(DataElement):
    """Code specifying the level of danger for which the packaging must cater."""

    code: str = "8339"
    title: str = "Packaging danger level code"
    repr_line: str = "an..3"


class EHaulageArrangementsCode(DataElement):
    """Code specifying the arrangement for the haulage of goods."""

    code: str = "8341"
    title: str = "Haulage arrangements code"
    repr_line: str = "an..3"


class EHazardIdentificationCode(DataElement):
    """Code identifying a hazard."""

    code: str = "8351"
    title: str = "Hazard identification code"
    repr_line: str = "an..7"


class EEmergencyProcedureForShipsIdentifier(DataElement):
    """To identify the emergency procedure number for ships transporting dangerous goods. Synonym: EMS Number."""

    code: str = "8364"
    title: str = "Emergency procedure for ships identifier"
    repr_line: str = "an..8"


class EReturnablePackageLoadContentsCode(DataElement):
    """Code specifying the load contents for a returnable package."""

    code: str = "8393"
    title: str = "Returnable package load contents code"
    repr_line: str = "an..3"


class EReturnablePackageFreightPaymentResponsibilityCode(DataElement):
    """Code specifying the responsibility for the freight payment for a returnable package."""

    code: str = "8395"
    title: str = "Returnable package freight payment responsibility code"
    repr_line: str = "an..3"


class EHazardMedicalFirstAidGuideIdentifier(DataElement):
    """To identify a Medical First Aid Guide (MFAG) for hazardous goods."""

    code: str = "8410"
    title: str = "Hazard medical first aid guide identifier"
    repr_line: str = "an..4"


class ETransportMeansNationalityCode(DataElement):
    """Code specifying the nationality of a means of transport."""

    code: str = "8453"
    title: str = "Transport means nationality code"
    repr_line: str = "an..3"


class EExcessTransportationReasonCode(DataElement):
    """Code specifying the reason for excess transportation."""

    code: str = "8457"
    title: str = "Excess transportation reason code"
    repr_line: str = "an..3"


class EExcessTransportationResponsibilityCode(DataElement):
    """Code specifying the responsibility for excess transportation."""

    code: str = "8459"
    title: str = "Excess transportation responsibility code"
    repr_line: str = "an..3"


class ETunnelRestrictionCode(DataElement):
    """A code indicating a restriction for transport through tunnels."""

    code: str = "8461"
    title: str = "Tunnel restriction code"
    repr_line: str = "an..6"


class ETransportServiceIdentificationCode(DataElement):
    """Code identifying a transport service."""

    code: str = "8462"
    title: str = "Transport service identification code"
    repr_line: str = "an..17"


class ETransportServiceName(DataElement):
    """Name of a transport service."""

    code: str = "8463"
    title: str = "Transport service name"
    repr_line: str = "an..35"


class ETransportServiceDescription(DataElement):
    """Free form description of a transport service."""

    code: str = "8464"
    title: str = "Transport service description"
    repr_line: str = "an..256"


class EEmploymentDetailsCodeQualifier(DataElement):
    """Code qualifying the employment details."""

    code: str = "9003"
    title: str = "Employment details code qualifier"
    repr_line: str = "an..3"


class EEmploymentCategoryDescription(DataElement):
    """Free form description of the employment category."""

    code: str = "9004"
    title: str = "Employment category description"
    repr_line: str = "an..35"


class EEmploymentCategoryDescriptionCode(DataElement):
    """Code specifying the employment category."""

    code: str = "9005"
    title: str = "Employment category description code"
    repr_line: str = "an..3"


class EQualificationClassificationDescription(DataElement):
    """Free form description of a qualification classification."""

    code: str = "9006"
    title: str = "Qualification classification description"
    repr_line: str = "an..35"


class EQualificationClassificationDescriptionCode(DataElement):
    """Code specifying a qualification classification."""

    code: str = "9007"
    title: str = "Qualification classification description code"
    repr_line: str = "an..3"


class EOccupationDescription(DataElement):
    """Free form description of an occupation."""

    code: str = "9008"
    title: str = "Occupation description"
    repr_line: str = "an..35"


class EOccupationDescriptionCode(DataElement):
    """Code specifying an occupation."""

    code: str = "9009"
    title: str = "Occupation description code"
    repr_line: str = "an..3"


class EStatusReasonDescription(DataElement):
    """Free form description of the status reason."""

    code: str = "9012"
    title: str = "Status reason description"
    repr_line: str = "an..256"


class EStatusReasonDescriptionCode(DataElement):
    """Code specifying the reason for a status."""

    code: str = "9013"
    title: str = "Status reason description code"
    repr_line: str = "an..3"


class EStatusCategoryCode(DataElement):
    """Code specifying the category of a status."""

    code: str = "9015"
    title: str = "Status category code"
    repr_line: str = "an..3"


class EAttributeFunctionCodeQualifier(DataElement):
    """Code qualifying an attribute function."""

    code: str = "9017"
    title: str = "Attribute function code qualifier"
    repr_line: str = "an..3"


class EAttributeDescription(DataElement):
    """Free form description of an attribute."""

    code: str = "9018"
    title: str = "Attribute description"
    repr_line: str = "an..256"


class EAttributeDescriptionCode(DataElement):
    """Code specifying an attribute."""

    code: str = "9019"
    title: str = "Attribute description code"
    repr_line: str = "an..17"


class EAttributeTypeDescription(DataElement):
    """Free form description of an attribute type."""

    code: str = "9020"
    title: str = "Attribute type description"
    repr_line: str = "an..70"


class EAttributeTypeDescriptionCode(DataElement):
    """Coded specifying an attribute type."""

    code: str = "9021"
    title: str = "Attribute type description code"
    repr_line: str = "an..17"


class EDefinitionFunctionCode(DataElement):
    """Code specifying the function of a definition."""

    code: str = "9023"
    title: str = "Definition function code"
    repr_line: str = "an..3"


class EDefinitionExtentCode(DataElement):
    """Code specifying the extent of a definition."""

    code: str = "9025"
    title: str = "Definition extent code"
    repr_line: str = "an..3"


class EEditMaskFormatIdentifier(DataElement):
    """To identify the format of an edit mask."""

    code: str = "9026"
    title: str = "Edit mask format identifier"
    repr_line: str = "an..35"


class EValueDefinitionCodeQualifier(DataElement):
    """Code qualifying a value definition."""

    code: str = "9029"
    title: str = "Value definition code qualifier"
    repr_line: str = "an..3"


class EEditMaskRepresentationCode(DataElement):
    """Code specifying the representation of the edit mask."""

    code: str = "9031"
    title: str = "Edit mask representation code"
    repr_line: str = "an..3"


class EQualificationApplicationAreaCode(DataElement):
    """Code specifying the application area of a qualification."""

    code: str = "9035"
    title: str = "Qualification application area code"
    repr_line: str = "an..3"


class EQualificationTypeCodeQualifier(DataElement):
    """Code qualifying a type of qualification."""

    code: str = "9037"
    title: str = "Qualification type code qualifier"
    repr_line: str = "an..3"


class EFacilityTypeDescription(DataElement):
    """Free form description of the facility type."""

    code: str = "9038"
    title: str = "Facility type description"
    repr_line: str = "an..70"


class EFacilityTypeDescriptionCode(DataElement):
    """Code specifying the facility type."""

    code: str = "9039"
    title: str = "Facility type description code"
    repr_line: str = "an..3"


class EReservationIdentifier(DataElement):
    """To identify a reservation."""

    code: str = "9040"
    title: str = "Reservation identifier"
    repr_line: str = "an..20"


class EReservationIdentifierCodeQualifier(DataElement):
    """Code qualifying the reservation identifier."""

    code: str = "9043"
    title: str = "Reservation identifier code qualifier"
    repr_line: str = "an..3"


class EBasisCodeQualifier(DataElement):
    """Code qualifying the basis."""

    code: str = "9045"
    title: str = "Basis code qualifier"
    repr_line: str = "an..3"


class EBasisTypeDescription(DataElement):
    """Free form description of the basis type."""

    code: str = "9046"
    title: str = "Basis type description"
    repr_line: str = "an..35"


class EBasisTypeDescriptionCode(DataElement):
    """Code specifying the type of basis."""

    code: str = "9047"
    title: str = "Basis type description code"
    repr_line: str = "an..3"


class EApplicabilityTypeDescription(DataElement):
    """Free form description of the type of applicability."""

    code: str = "9048"
    title: str = "Applicability type description"
    repr_line: str = "an..35"


class EApplicabilityTypeDescriptionCode(DataElement):
    """Code specifying the type of applicability."""

    code: str = "9049"
    title: str = "Applicability type description code"
    repr_line: str = "an..3"


class EApplicabilityCodeQualifier(DataElement):
    """Code qualifying the applicability."""

    code: str = "9051"
    title: str = "Applicability code qualifier"
    repr_line: str = "an..3"


class ERelationshipTypeCodeQualifier(DataElement):
    """Code qualifying a type of relationship."""

    code: str = "9141"
    title: str = "Relationship type code qualifier"
    repr_line: str = "an..3"


class ERelationshipDescription(DataElement):
    """Free form description of a relationship."""

    code: str = "9142"
    title: str = "Relationship description"
    repr_line: str = "an..35"


class ERelationshipDescriptionCode(DataElement):
    """Code specifying a relationship."""

    code: str = "9143"
    title: str = "Relationship description code"
    repr_line: str = "an..3"


class ECompositeDataElementTagIdentifier(DataElement):
    """To identify the tag of a composite data element."""

    code: str = "9146"
    title: str = "Composite data element tag identifier"
    repr_line: str = "an..4"


class EDirectoryStatusIdentifier(DataElement):
    """To identify the status of a directory set."""

    code: str = "9148"
    title: str = "Directory status identifier"
    repr_line: str = "an..3"


class ESimpleDataElementTagIdentifier(DataElement):
    """To identify the tag of a simple data element."""

    code: str = "9150"
    title: str = "Simple data element tag identifier"
    repr_line: str = "an..4"


class ESimpleDataElementCharacterRepresentationCode(DataElement):
    """Code specifying the character representation of a simple data element."""

    code: str = "9153"
    title: str = "Simple data element character representation code"
    repr_line: str = "an..3"


class ESimpleDataElementMaximumLengthMeasure(DataElement):
    """To specify the value of the maximum length of a simple data element."""

    code: str = "9156"
    title: str = "Simple data element maximum length measure"
    repr_line: str = "n..3"


class ESimpleDataElementMinimumLengthMeasure(DataElement):
    """To specify the value of the minimum length of a simple data element."""

    code: str = "9158"
    title: str = "Simple data element minimum length measure"
    repr_line: str = "n..3"


class ECodeSetIndicatorCode(DataElement):
    """Code indicating whether a data element has an associated code set."""

    code: str = "9161"
    title: str = "Code set indicator code"
    repr_line: str = "an..3"


class EDataElementTagIdentifier(DataElement):
    """To identify the tag of a data element."""

    code: str = "9162"
    title: str = "Data element tag identifier"
    repr_line: str = "an..4"


class EGroupIdentifier(DataElement):
    """To identify a group."""

    code: str = "9164"
    title: str = "Group identifier"
    repr_line: str = "an..4"


class ESegmentTagIdentifier(DataElement):
    """To identify the tag of a segment."""

    code: str = "9166"
    title: str = "Segment tag identifier"
    repr_line: str = "an..3"


class EDataRepresentationTypeCode(DataElement):
    """Code specifying a type of data representation."""

    code: str = "9169"
    title: str = "Data representation type code"
    repr_line: str = "an..3"


class EEventTypeDescription(DataElement):
    """Free form description of the event type."""

    code: str = "9170"
    title: str = "Event type description"
    repr_line: str = "an..70"


class EEventTypeDescriptionCode(DataElement):
    """Code specifying an event type."""

    code: str = "9171"
    title: str = "Event type description code"
    repr_line: str = "an..3"


class EEvent(DataElement):
    """Free form description of the event."""

    code: str = "9172"
    title: str = "Event"
    repr_line: str = "an..256"


class EEventDescriptionCode(DataElement):
    """Code specifying an event."""

    code: str = "9173"
    title: str = "Event description code"
    repr_line: str = "an..35"


class EDataElementUsageTypeCode(DataElement):
    """Code specifying the usage type of a data element."""

    code: str = "9175"
    title: str = "Data element usage type code"
    repr_line: str = "an..3"


class EDutyRegimeTypeCode(DataElement):
    """Code specifying a type of duty regime."""

    code: str = "9213"
    title: str = "Duty regime type code"
    repr_line: str = "an..3"


class EValidationResultText(DataElement):
    """To specify the value of a validation result."""

    code: str = "9280"
    title: str = "Validation result text"
    repr_line: str = "an..35"


class EValidationKeyIdentifier(DataElement):
    """To identify the cryptographic key used for the calculation of the validation."""

    code: str = "9282"
    title: str = "Validation key identifier"
    repr_line: str = "an..35"


class EValidationCriteriaCode(DataElement):
    """Code specifying the validation criteria to be applied."""

    code: str = "9285"
    title: str = "Validation criteria code"
    repr_line: str = "an..3"


class ESealingPartyName(DataElement):
    """Name of the sealing party."""

    code: str = "9302"
    title: str = "Sealing party name"
    repr_line: str = "an..35"


class ESealingPartyNameCode(DataElement):
    """Code specifying the name of the sealing party."""

    code: str = "9303"
    title: str = "Sealing party name code"
    repr_line: str = "an..3"


class ETransportUnitSealIdentifier(DataElement):
    """The identification number of a seal affixed to a  transport unit."""

    code: str = "9308"
    title: str = "Transport unit seal identifier"
    repr_line: str = "an..35"


class EApplicationErrorCode(DataElement):
    """Code specifying an application error."""

    code: str = "9321"
    title: str = "Application error code"
    repr_line: str = "an..8"


class EGovernmentProcedureCode(DataElement):
    """Code specifying a government procedure."""

    code: str = "9353"
    title: str = "Government procedure code"
    repr_line: str = "an..3"


class EGovernmentInvolvementCode(DataElement):
    """Code indicating the requirement and status of governmental involvement."""

    code: str = "9411"
    title: str = "Government involvement code"
    repr_line: str = "an..3"


class EGovernmentAgencyIdentificationCode(DataElement):
    """Code identifying a government agency."""

    code: str = "9415"
    title: str = "Government agency identification code"
    repr_line: str = "an..3"


class EGovernmentActionCode(DataElement):
    """Code specifying a type of government action such as inspection, detention, fumigation, security."""

    code: str = "9417"
    title: str = "Government action code"
    repr_line: str = "an..3"


class EServiceLayerCode(DataElement):
    """Code specifying a service layer."""

    code: str = "9419"
    title: str = "Service layer code"
    repr_line: str = "an..3"


class EProcessStageCodeQualifier(DataElement):
    """Code qualifying a stage in a process."""

    code: str = "9421"
    title: str = "Process stage code qualifier"
    repr_line: str = "an..3"


class EValueText(DataElement):
    """To specify a value."""

    code: str = "9422"
    title: str = "Value text"
    repr_line: str = "an..512"


class EArrayCellDataDescription(DataElement):
    """Free form description of the content of an array cell."""

    code: str = "9424"
    title: str = "Array cell data description"
    repr_line: str = "an..512"


class ECodeValueText(DataElement):
    """To specify a code value."""

    code: str = "9426"
    title: str = "Code value text"
    repr_line: str = "an..35"


class EArrayCellStructureIdentifier(DataElement):
    """To identify an array cell structure."""

    code: str = "9428"
    title: str = "Array cell structure identifier"
    repr_line: str = "an..35"


class EFootnoteSetIdentifier(DataElement):
    """To identify a footnote set."""

    code: str = "9430"
    title: str = "Footnote set identifier"
    repr_line: str = "an..35"


class EFootnoteIdentifier(DataElement):
    """To identify a footnote."""

    code: str = "9432"
    title: str = "Footnote identifier"
    repr_line: str = "an..35"


class ECodeName(DataElement):
    """Name of a code."""

    code: str = "9434"
    title: str = "Code name"
    repr_line: str = "an..70"


class EClinicalInterventionDescription(DataElement):
    """Free form description of a clinical intervention."""

    code: str = "9436"
    title: str = "Clinical intervention description"
    repr_line: str = "an..70"


class EClinicalInterventionDescriptionCode(DataElement):
    """Code specifying a clinical intervention."""

    code: str = "9437"
    title: str = "Clinical intervention description code"
    repr_line: str = "an..17"


class EClinicalInterventionTypeCodeQualifier(DataElement):
    """Code qualifying a type of clinical intervention."""

    code: str = "9441"
    title: str = "Clinical intervention type code qualifier"
    repr_line: str = "an..3"


class EAttendanceTypeCodeQualifier(DataElement):
    """Code qualifying a type of attendance."""

    code: str = "9443"
    title: str = "Attendance type code qualifier"
    repr_line: str = "an..3"


class EAdmissionTypeDescription(DataElement):
    """Free form of the type of admission."""

    code: str = "9444"
    title: str = "Admission type description"
    repr_line: str = "an..35"


class EAdmissionTypeDescriptionCode(DataElement):
    """Code specifying the type of admission."""

    code: str = "9445"
    title: str = "Admission type description code"
    repr_line: str = "an..3"


class EDischargeTypeDescription(DataElement):
    """Free form description of the type of discharge."""

    code: str = "9446"
    title: str = "Discharge type description"
    repr_line: str = "an..35"


class EDischargeTypeDescriptionCode(DataElement):
    """Code specifying the type of discharge."""

    code: str = "9447"
    title: str = "Discharge type description code"
    repr_line: str = "an..3"


class EFileGenerationCommandName(DataElement):
    """Name of a file generation command."""

    code: str = "9448"
    title: str = "File generation command name"
    repr_line: str = "an..35"


class EFileCompressionTechniqueName(DataElement):
    """Name of a file compression technique."""

    code: str = "9450"
    title: str = "File compression technique name"
    repr_line: str = "an..35"


class ECodeValueSourceCode(DataElement):
    """Code specifying the source of a code value."""

    code: str = "9453"
    title: str = "Code value source code"
    repr_line: str = "an..3"


class EFormulaTypeCodeQualifier(DataElement):
    """Code qualifying the type of formula."""

    code: str = "9501"
    title: str = "Formula type code qualifier"
    repr_line: str = "an..3"


class EFormulaName(DataElement):
    """Name identifying a formula."""

    code: str = "9502"
    title: str = "Formula name"
    repr_line: str = "an..35"


class EFormulaComplexityCode(DataElement):
    """Code specifying the complexity of a formula."""

    code: str = "9505"
    title: str = "Formula complexity code"
    repr_line: str = "an..3"


class EFormulaSequenceCodeQualifier(DataElement):
    """Code giving specific meaning to a formula sequence."""

    code: str = "9507"
    title: str = "Formula sequence code qualifier"
    repr_line: str = "an..3"


class EFormulaSequenceOperandCode(DataElement):
    """Code specifying a specific type of operand within a formula sequence."""

    code: str = "9509"
    title: str = "Formula sequence operand code"
    repr_line: str = "an..17"


class EFormulaSequenceName(DataElement):
    """Name identifying a formula sequence."""

    code: str = "9510"
    title: str = "Formula sequence name"
    repr_line: str = "an..35"


class EInformationCategoryCode(DataElement):
    """Code specifying the category of the information."""

    code: str = "9601"
    title: str = "Information category code"
    repr_line: str = "an..3"


class EDataCodeQualifier(DataElement):
    """Code qualifying the data."""

    code: str = "9605"
    title: str = "Data code qualifier"
    repr_line: str = "an..3"


class EYesOrNoIndicatorCode(DataElement):
    """Code specifying either a yes or no."""

    code: str = "9607"
    title: str = "Yes or no indicator code"
    repr_line: str = "an..3"


class EAdjustmentCategoryCode(DataElement):
    """Code specifying the general category of adjustment."""

    code: str = "9619"
    title: str = "Adjustment category code"
    repr_line: str = "an..3"


class EPolicyLimitationIdentifier(DataElement):
    """Code specifying a policy limitation."""

    code: str = "9620"
    title: str = "Policy limitation identifier"
    repr_line: str = "an..10"


class EDiagnosisTypeCode(DataElement):
    """Code specifying the type of diagnosis."""

    code: str = "9623"
    title: str = "Diagnosis type code"
    repr_line: str = "an..3"


class ERelatedCauseCode(DataElement):
    """Code specifying a related cause."""

    code: str = "9625"
    title: str = "Related cause code"
    repr_line: str = "an..3"


class EAdmissionSourceCode(DataElement):
    """Code specifying the source of admission."""

    code: str = "9627"
    title: str = "Admission source code"
    repr_line: str = "an..3"


class EProcedureModificationCode(DataElement):
    """Code specifying the procedure modification."""

    code: str = "9629"
    title: str = "Procedure modification code"
    repr_line: str = "an..3"


class EInvoiceTypeCode(DataElement):
    """Code specifying the type of invoice."""

    code: str = "9631"
    title: str = "Invoice type code"
    repr_line: str = "an..3"


class EEventDetailsCodeQualifier(DataElement):
    """Code qualifying the event details."""

    code: str = "9635"
    title: str = "Event details code qualifier"
    repr_line: str = "an..3"


class EEventCategoryDescription(DataElement):
    """Free form description of the event category."""

    code: str = "9636"
    title: str = "Event category description"
    repr_line: str = "an..70"


class EEventCategoryDescriptionCode(DataElement):
    """Code specifying the event category."""

    code: str = "9637"
    title: str = "Event category description code"
    repr_line: str = "an..3"


class EDiagnosisCategoryCode(DataElement):
    """Code specifying a diagnosis category."""

    code: str = "9639"
    title: str = "Diagnosis category code"
    repr_line: str = "an..3"


class EServiceBasisCodeQualifier(DataElement):
    """Code qualifying the basis on which a service is performed."""

    code: str = "9641"
    title: str = "Service basis code qualifier"
    repr_line: str = "an..3"


class ESupportingEvidenceTypeCodeQualifier(DataElement):
    """Code qualifying the type of supporting evidence."""

    code: str = "9643"
    title: str = "Supporting evidence type code qualifier"
    repr_line: str = "an..3"


class EPayerResponsibilityLevelCode(DataElement):
    """Code specifying the level of responsibility of a payer."""

    code: str = "9645"
    title: str = "Payer responsibility level code"
    repr_line: str = "an..3"


class ECavityZoneCode(DataElement):
    """Code specifying the zone of the cavity."""

    code: str = "9647"
    title: str = "Cavity zone code"
    repr_line: str = "an..3"


class EProcessingInformationCodeQualifier(DataElement):
    """Code qualifying the processing information."""

    code: str = "9649"
    title: str = "Processing information code qualifier"
    repr_line: str = "an..3"


__all__ = [
    "SyntaxIdentifier",
    "SyntaxVersionNumber",
    "InterchangeSenderIdentification",
    "IdentificationCodeQualifier",
    "InterchangeSenderInternalIdentification",
    "InterchangeRecipientIdentification",
    "InterchangeRecipientInternalIdentification",
    "Date",
    "Time",
    "InterchangeControlReference",
    "RecipientReferencepassword",
    "RecipientReferencepasswordQualifier",
    "ApplicationReference",
    "ProcessingPriorityCode",
    "AcknowledgementRequest",
    "InterchangeAgreementIdentifier",
    "TestIndicator",
    "InterchangeControlCount",
    "MessageGroupIdentification",
    "ApplicationSenderIdentification",
    "InterchangeSenderInternalSubidentification",
    "ApplicationRecipientIdentification",
    "InterchangeRecipientInternalSubidentification",
    "GroupReferenceNumber",
    "ControllingAgencyCoded",
    "MessageVersionNumber",
    "MessageReleaseNumber",
    "AssociationAssignedCode",
    "ApplicationPassword",
    "GroupControlCount",
    "MessageReferenceNumber",
    "MessageType",
    "CommonAccessReference",
    "SequenceOfTransfers",
    "FirstAndLastTransfer",
    "NumberOfSegmentsInAMessage",
    "SyntaxReleaseNumber",
    "ServiceCodeListDirectoryVersionNumber",
    "SectionIdentification",
    "ActionCoded",
    "SyntaxErrorCoded",
    "AnticollisionSegmentGroupIdentification",
    "SegmentPositionInMessageBody",
    "ErroneousDataElementPositionInSegment",
    "ErroneousComponentDataElementPosition",
    "CodeListDirectoryVersionNumber",
    "MessageTypeSubfunctionIdentification",
    "MessageSubsetIdentification",
    "MessageSubsetVersionNumber",
    "MessageSubsetReleaseNumber",
    "MessageImplementationGuidelineIdentification",
    "MessageImplementationGuidelineVersionNumber",
    "MessageImplementationGuidelineReleaseNumber",
    "ScenarioIdentification",
    "ScenarioVersionNumber",
    "ScenarioReleaseNumber",
    "CharacterEncodingCoded",
    "ServiceSegmentTagCoded",
    "ErroneousDataElementOccurrence",
    "SecuritySegmentPosition",
    "InitiatorControlReference",
    "InitiatorReferenceIdentification",
    "ResponderControlReference",
    "TransactionControlReference",
    "DialogueIdentification",
    "EventTime",
    "SenderSequenceNumber",
    "TransferPositionCoded",
    "DuplicateIndicator",
    "ReportFunctionCoded",
    "Status",
    "StatusCoded",
    "LanguageCoded",
    "TimeOffset",
    "EventDate",
    "InteractiveMessageReferenceNumber",
    "DialogueVersionNumber",
    "DialogueReleaseNumber",
    "SecurityServiceCoded",
    "ResponseTypeCoded",
    "FilterFunctionCoded",
    "OriginalCharacterSetEncodingCoded",
    "RoleOfSecurityProviderCoded",
    "SecurityPartyIdentification",
    "SecurityPartyCodeListQualifier",
    "SecurityPartyCodeListResponsibleAgencyCoded",
    "DateAndTimeQualifier",
    "EncryptionReferenceNumber",
    "SecuritySequenceNumber",
    "UseOfAlgorithmCoded",
    "CryptographicModeOfOperationCoded",
    "AlgorithmCoded",
    "AlgorithmCodeListIdentifier",
    "AlgorithmParameterQualifier",
    "ModeOfOperationCodeListIdentifier",
    "SecurityReferenceNumber",
    "CertificateReference",
    "KeyName",
    "ScopeOfSecurityApplicationCoded",
    "CertificateOriginalCharacterSetRepertoireCoded",
    "CertificateSyntaxAndVersionCoded",
    "UserAuthorisationLevel",
    "ServiceCharacterForSignature",
    "ServiceCharacterForSignatureQualifier",
    "AlgorithmParameterValue",
    "LengthOfDataInOctetsOfBits",
    "ListParameter",
    "ValidationValue",
    "ValidationValueQualifier",
    "MessageRelationCoded",
    "SecurityStatusCoded",
    "RevocationReasonCoded",
    "SecurityErrorCoded",
    "CertificateSequenceNumber",
    "ListParameterQualifier",
    "SecurityPartyQualifier",
    "KeyManagementFunctionQualifier",
    "NumberOfPaddingBytes",
    "SecurityPartyName",
    "NumberOfSecuritySegments",
    "PaddingMechanismCoded",
    "PaddingMechanismCodeListIdentifier",
    "PackageReferenceNumber",
    "ReferenceIdentificationNumber",
    "ObjectTypeQualifier",
    "ObjectTypeAttribute",
    "ObjectTypeAttributeIdentification",
    "LengthOfObjectInOctetsOfBits",
    "ReferenceQualifier",
    "NumberOfSegmentsBeforeObject",
    "EDocumentName",
    "EDocumentNameCode",
    "EMessageTypeCode",
    "EDocumentIdentifier",
    "EMessageSectionCode",
    "ESequencePositionIdentifier",
    "EMessageItemIdentifier",
    "EMessageSubitemIdentifier",
    "EVersionIdentifier",
    "EReleaseIdentifier",
    "ERevisionIdentifier",
    "EDocumentLineActionCode",
    "ELineItemIdentifier",
    "ECodeListIdentificationCode",
    "ETravellerReferenceIdentifier",
    "EAccountName",
    "EAccountIdentifier",
    "EAccountAbbreviatedName",
    "EReferenceCodeQualifier",
    "EReferenceIdentifier",
    "EDocumentLineIdentifier",
    "ESequenceIdentifierSourceCode",
    "EAccountingJournalName",
    "EAccountingJournalIdentifier",
    "EDocumentOriginalsRequiredQuantity",
    "EDocumentCopiesRequiredQuantity",
    "EConfigurationLevelNumber",
    "EMessageFunctionCode",
    "ECalculationSequenceCode",
    "EActionDescription",
    "EActionCode",
    "EAllowanceOrChargeIdentifier",
    "EConsignmentLoadSequenceIdentifier",
    "EDocumentSourceDescription",
    "EDocumentStatusCode",
    "EControllingAgencyIdentifier",
    "EConsolidationItemNumber",
    "EGoodsItemNumber",
    "EComputerEnvironmentDetailsCodeQualifier",
    "EDataFormatDescription",
    "EDataFormatDescriptionCode",
    "EValueListTypeCode",
    "EDesignatedClassCode",
    "EFileName",
    "EComputerEnvironmentName",
    "EComputerEnvironmentNameCode",
    "EValueListName",
    "EFileFormatName",
    "EValueListIdentifier",
    "EDataSetIdentifier",
    "EMessageImplementationIdentificationCode",
    "EDate",
    "ETime",
    "EDateOrTimeOrPeriodFunctionCodeQualifier",
    "ETermsTimeRelationCode",
    "EFrequencyCode",
    "EDespatchPatternCode",
    "EDespatchPatternTimingCode",
    "EAge",
    "EPeriodTypeCodeQualifier",
    "ETimeZoneIdentifier",
    "ETimeVariationQuantity",
    "ETimeZoneDifferenceQuantity",
    "EPeriodDetailDescription",
    "EPeriodDetailDescriptionCode",
    "EDateVariationNumber",
    "EPeriodTypeCode",
    "EPeriodCountQuantity",
    "EChargePeriodTypeCode",
    "ECheckinTime",
    "EDaysOfWeekSetIdentifier",
    "EJourneyLegDurationQuantity",
    "EMillisecondTime",
    "EDateOrTimeOrPeriodFormatCode",
    "EDateOrTimeOrPeriodText",
    "EEventTimeReferenceCode",
    "EMaintenanceOperationOperatorCode",
    "EMaintenanceOperationPayerCode",
    "EPartyFunctionCodeQualifier",
    "EPartyName",
    "EPartyIdentifier",
    "EStreetAndNumberOrPostOfficeBoxIdentifier",
    "EPartyNameFormatCode",
    "ECodeListResponsibleAgencyCode",
    "ETestMediumCode",
    "EOrganisationClassificationCode",
    "EOrganisationalClassName",
    "EOrganisationalClassNameCode",
    "ENameAndAddressDescription",
    "ECarrierName",
    "ECarrierIdentifier",
    "EAddressTypeCode",
    "EContactFunctionCode",
    "ECommunicationAddressIdentifier",
    "ECommunicationMediumTypeCode",
    "ECommunicationMeansTypeCode",
    "ECityName",
    "EAccountHolderName",
    "EAccountHolderIdentifier",
    "EAgentIdentifier",
    "ECountryIdentifier",
    "EFirstRelatedLocationName",
    "EFirstRelatedLocationIdentifier",
    "ELocationName",
    "ELocationIdentifier",
    "ELocationFunctionCodeQualifier",
    "ECountrySubdivisionName",
    "ECountrySubdivisionIdentifier",
    "ESecondRelatedLocationName",
    "ESecondRelatedLocationIdentifier",
    "ESampleLocationDescription",
    "ESampleLocationDescriptionCode",
    "ECountryOfOriginIdentifier",
    "EPostalIdentificationCode",
    "EGeographicAreaCode",
    "EInstructionReceivingPartyIdentifier",
    "EAddressComponentDescription",
    "EPersonCharacteristicCodeQualifier",
    "ENationalityName",
    "ENationalityNameCode",
    "ENameOriginalAlphabetCode",
    "EAddressPurposeCode",
    "EEnactingPartyIdentifier",
    "EInheritedCharacteristicDescription",
    "EInheritedCharacteristicDescriptionCode",
    "ENameStatusCode",
    "ENameComponentDescription",
    "ENameComponentUsageCode",
    "ENameTypeCode",
    "ENameComponentTypeCodeQualifier",
    "EContactName",
    "EContactIdentifier",
    "EInstitutionName",
    "EInstitutionNameCode",
    "EInstitutionBranchIdentifier",
    "EInstitutionBranchLocationName",
    "EPartyTaxIdentifier",
    "EBankIdentifier",
    "ELanguageName",
    "ELanguageNameCode",
    "ELanguageCodeQualifier",
    "EOriginatorTypeCode",
    "EFrequentTravellerIdentifier",
    "EGivenName",
    "EGateIdentifier",
    "EInhouseIdentifier",
    "EAddressStatusCode",
    "EAddressFormatCode",
    "EMaritalStatusDescription",
    "EMaritalStatusDescriptionCode",
    "EPersonJobTitle",
    "EReligionName",
    "EReligionNameCode",
    "ENationalityCodeQualifier",
    "ESalesChannelIdentifier",
    "EGenderCode",
    "EFamilyName",
    "EAccessAuthorisationIdentifier",
    "EGivenNameTitleDescription",
    "EBenefitCoverageConstituentsCode",
    "EOptionCode",
    "EDeliveryPlanCommitmentLevelCode",
    "ERelatedInformationDescription",
    "EBusinessDescription",
    "EBusinessFunctionCode",
    "EBusinessFunctionTypeCodeQualifier",
    "EPriorityTypeCodeQualifier",
    "EPriorityDescription",
    "EPriorityDescriptionCode",
    "EAdditionalSafetyInformationDescription",
    "EAdditionalSafetyInformationDescriptionCode",
    "ETradeClassCode",
    "ESafetySectionName",
    "ESafetySectionNumber",
    "ECertaintyDescription",
    "ECertaintyDescriptionCode",
    "ECharacteristicRelevanceCode",
    "EDeliveryOrTransportTermsDescription",
    "EDeliveryOrTransportTermsDescriptionCode",
    "EDeliveryOrTransportTermsFunctionCode",
    "EQuestionDescription",
    "EQuestionDescriptionCode",
    "EClauseCodeQualifier",
    "EContractAndCarriageConditionCode",
    "EClauseName",
    "EClauseNameCode",
    "EProvisoCodeQualifier",
    "EProvisoTypeDescription",
    "EProvisoTypeDescriptionCode",
    "EProvisoCalculationDescription",
    "EProvisoCalculationDescriptionCode",
    "EHandlingInstructionDescription",
    "EHandlingInstructionDescriptionCode",
    "EInformationCategoryDescription",
    "EInformationCategoryDescriptionCode",
    "EInformationDetailDescription",
    "EInformationDetailDescriptionCode",
    "EInformationDetailsCodeQualifier",
    "ESpecialConditionCode",
    "ESpecialRequirementDescription",
    "ESpecialRequirementTypeCode",
    "ETransportChargesPaymentMethodCode",
    "ETransportServicePriorityCode",
    "EDiscrepancyNatureIdentificationCode",
    "EMarkingInstructionsCode",
    "EPaymentArrangementCode",
    "EPaymentTermsDescription",
    "EPaymentTermsDescriptionIdentifier",
    "EPaymentTermsTypeCodeQualifier",
    "EChangeReasonDescription",
    "EChangeReasonDescriptionCode",
    "EResponseTypeCode",
    "EResponseDescription",
    "EResponseDescriptionCode",
    "EProductIdentifierCodeQualifier",
    "EBankOperationCode",
    "EInstructionDescription",
    "EInstructionDescriptionCode",
    "EInstructionTypeCodeQualifier",
    "EStatusDescription",
    "EStatusDescriptionCode",
    "ESampleProcessStepCode",
    "ETestMethodIdentifier",
    "ETestDescription",
    "ETestAdministrationMethodCode",
    "ETestReasonName",
    "ETestReasonNameCode",
    "EPaymentGuaranteeMeansCode",
    "EPaymentChannelCode",
    "EAccountTypeCodeQualifier",
    "EPaymentConditionsCode",
    "EFreeText",
    "EFreeTextDescriptionCode",
    "EFreeTextFormatCode",
    "ETextSubjectCodeQualifier",
    "EFreeTextFunctionCode",
    "EBackOrderArrangementTypeCode",
    "ESubstitutionConditionCode",
    "EPaymentMeansCode",
    "EIntracompanyPaymentIndicatorCode",
    "EAdjustmentReasonDescriptionCode",
    "EPaymentMethodCode",
    "EPaymentPurposeCode",
    "ESettlementMeansCode",
    "EInformationType",
    "EInformationTypeCode",
    "EAccountingEntryTypeName",
    "EAccountingEntryTypeNameCode",
    "EFinancialTransactionTypeCode",
    "EDeliveryInstructionCode",
    "EInsuranceCoverDescription",
    "EInsuranceCoverDescriptionCode",
    "EInsuranceCoverTypeCode",
    "EInventoryMovementReasonCode",
    "EInventoryMovementDirectionCode",
    "EInventoryBalanceMethodCode",
    "ECreditCoverRequestTypeCode",
    "ECreditCoverResponseTypeCode",
    "ECreditCoverResponseReasonCode",
    "ERequestedInformationDescription",
    "ERequestedInformationDescriptionCode",
    "EMaintenanceOperationCode",
    "ESealConditionCode",
    "EDefinitionIdentifier",
    "EPremiumCalculationComponentIdentifier",
    "EPremiumCalculationComponentValueCategoryIdentifier",
    "ESealTypeCode",
    "EMonetaryAmount",
    "EMonetaryAmountFunctionDescription",
    "EMonetaryAmountFunctionDescriptionCode",
    "EIndexCodeQualifier",
    "EMonetaryAmountTypeCodeQualifier",
    "EIndexTypeIdentifier",
    "EIndexText",
    "EIndexRepresentationCode",
    "EContributionCodeQualifier",
    "EContributionTypeDescription",
    "EContributionTypeDescriptionCode",
    "EMonetaryAmountFunctionDetailDescription",
    "EMonetaryAmountFunctionDetailDescriptionCode",
    "EPriceAmount",
    "EPriceCodeQualifier",
    "EDutyOrTaxOrFeeTypeName",
    "EDutyOrTaxOrFeeTypeNameCode",
    "ETotalMonetaryAmount",
    "EAllowanceOrChargeIdentificationCode",
    "ESublineItemPriceChangeOperationCode",
    "EChargeCategoryCode",
    "ERateOrTariffClassDescription",
    "ERateOrTariffClassDescriptionCode",
    "EPercentageTypeCodeQualifier",
    "EPercentageBasisIdentificationCode",
    "EChargeUnitCode",
    "ERateTypeIdentifier",
    "EServiceTypeCode",
    "EDutyOrTaxOrFeeRateBasisCode",
    "ESupplementaryRateOrTariffCode",
    "EDutyOrTaxOrFeeRate",
    "EDutyOrTaxOrFeeRateCode",
    "EDutyOrTaxOrFeeFunctionCodeQualifier",
    "EUnitPriceBasisQuantity",
    "EDutyOrTaxOrFeeAssessmentBasisQuantity",
    "EDutyOrTaxOrFeeAccountCode",
    "EDutyOrTaxOrFeeCategoryCode",
    "ETaxOrDutyOrFeePaymentDueDateCode",
    "ERemunerationTypeName",
    "ERemunerationTypeNameCode",
    "EPriceTypeCode",
    "EPriceChangeTypeCode",
    "EProductGroupTypeCode",
    "EPriceSpecificationCode",
    "EProductGroupName",
    "EProductGroupNameCode",
    "EPriceMultiplierTypeCodeQualifier",
    "EPriceMultiplierRate",
    "ECurrencyExchangeRate",
    "ERateTypeCodeQualifier",
    "EUnitPriceBasisRate",
    "EAllowanceOrChargeCodeQualifier",
    "ERelationCode",
    "EPercentage",
    "ESublineIndicatorCode",
    "ERatePlanCode",
    "ELatitudeDegree",
    "ELongitudeDegree",
    "EHeightMeasure",
    "EGeographicalPositionCodeQualifier",
    "EQuantity",
    "EQuantityTypeCodeQualifier",
    "EVarianceQuantity",
    "EControlTotalQuantity",
    "EControlTotalTypeCodeQualifier",
    "EFrequencyCodeQualifier",
    "EFrequencyRate",
    "EConfidencePercent",
    "EResultRepresentationCode",
    "EResultNormalcyCode",
    "EDosageDescription",
    "EDosageDescriptionIdentifier",
    "EDosageAdministrationCodeQualifier",
    "EResultValueTypeCodeQualifier",
    "EAltitude",
    "ELengthTypeCode",
    "EWidthMeasure",
    "EDimensionTypeCodeQualifier",
    "ERangeMaximumQuantity",
    "ENondiscreteMeasurementName",
    "ENondiscreteMeasurementNameCode",
    "ERangeMinimumQuantity",
    "ERangeTypeCodeQualifier",
    "ELengthMeasure",
    "ESizeTypeCodeQualifier",
    "ESizeMeasure",
    "EOccurrencesMaximumNumber",
    "EEditFieldLengthMeasure",
    "EDiameterMeasure",
    "ETemperatureTypeCodeQualifier",
    "ETemperatureDegree",
    "EMeasurementPurposeCodeQualifier",
    "EMeasuredAttributeCode",
    "EMeasure",
    "EMeasurementSignificanceCode",
    "EStatisticTypeCodeQualifier",
    "EExchangeRateCurrencyMarketIdentifier",
    "ECurrencyTypeCodeQualifier",
    "ECurrencyIdentificationCode",
    "ECurrencyUsageCodeQualifier",
    "ECurrencyRate",
    "EUnitsQuantity",
    "EUnitTypeCodeQualifier",
    "EMeasurementUnitName",
    "EMeasurementUnitCode",
    "EClinicalInformationDescription",
    "EClinicalInformationDescriptionIdentifier",
    "EClinicalInformationTypeCodeQualifier",
    "EProcessStagesQuantity",
    "EProcessStagesActualQuantity",
    "ESignificantDigitsQuantity",
    "EStatisticalConceptIdentifier",
    "EPhysicalOrLogicalStateTypeCodeQualifier",
    "EPhysicalOrLogicalStateDescription",
    "EPhysicalOrLogicalStateDescriptionCode",
    "EItemDescription",
    "EItemDescriptionCode",
    "EItemAvailabilityCode",
    "ECharacteristicDescription",
    "ECharacteristicDescriptionCode",
    "ESampleSelectionMethodCode",
    "EPowerTypeDescription",
    "EPowerTypeCode",
    "ESampleStateCode",
    "ESampleDirectionCode",
    "EClassTypeCode",
    "ETypeOfPackages",
    "EPackageTypeDescriptionCode",
    "EPackagingTermsAndConditionsCode",
    "EPackagingLevelCode",
    "EDescriptionFormatCode",
    "EItemCharacteristicCode",
    "EConfigurationOperationCode",
    "ECargoTypeClassificationCode",
    "EDangerousGoodsFlashpointDescription",
    "EShippingMarksDescription",
    "EShipmentFlashpointDegree",
    "ECharacteristicValueDescription",
    "ECharacteristicValueDescriptionCode",
    "EUnitedNationsDangerousGoodsUndgIdentifier",
    "ECustomerShipmentAuthorisationIdentifier",
    "EProductDetailsTypeCodeQualifier",
    "EProductName",
    "EProductIdentifier",
    "EProductCharacteristicIdentificationCode",
    "EItemIdentifier",
    "EItemTypeIdentificationCode",
    "ESpecialServiceDescription",
    "ESpecialServiceDescriptionCode",
    "EHierarchicalStructureLevelIdentifier",
    "EHierarchicalStructureParentIdentifier",
    "ELevelNumber",
    "EHierarchicalStructureRelationshipCode",
    "EHierarchyObjectCodeQualifier",
    "ERulePartIdentifier",
    "ERiskObjectSubtypeDescription",
    "ERiskObjectSubtypeDescriptionIdentifier",
    "ERiskObjectTypeIdentifier",
    "EProcessTypeDescription",
    "EProcessTypeDescriptionCode",
    "ETestMethodRevisionIdentifier",
    "EProcessDescription",
    "EProcessDescriptionCode",
    "EPackageQuantity",
    "EPackagingRelatedDescriptionCode",
    "EItemTotalQuantity",
    "EServiceRequirementCode",
    "ESectorAreaIdentificationCodeQualifier",
    "ERequirementOrConditionDescription",
    "ERequirementOrConditionDescriptionIdentifier",
    "ESetTypeCodeQualifier",
    "ERequirementDesignatorCode",
    "ECommodityIdentificationCode",
    "ECustomsGoodsIdentifier",
    "EProcessingIndicatorDescription",
    "EProcessingIndicatorDescriptionCode",
    "ESurfaceOrLayerCode",
    "EObjectIdentifier",
    "EObjectIdentificationCodeQualifier",
    "EHazardousMaterialCategoryName",
    "EHazardousMaterialCategoryNameCode",
    "EIndexingStructureCodeQualifier",
    "EAgreementTypeCodeQualifier",
    "EAgreementTypeDescriptionCode",
    "EAgreementTypeDescription",
    "ELevelOneIdentifier",
    "ELevelTwoIdentifier",
    "ELevelThreeIdentifier",
    "ELevelFourIdentifier",
    "ELevelFiveIdentifier",
    "ELevelSixIdentifier",
    "EMembershipTypeCodeQualifier",
    "EMembershipCategoryDescription",
    "EMembershipCategoryDescriptionCode",
    "EMembershipStatusDescription",
    "EMembershipStatusDescriptionCode",
    "EMembershipLevelCodeQualifier",
    "EMembershipLevelDescription",
    "EMembershipLevelDescriptionCode",
    "EAttendeeCategoryDescription",
    "EAttendeeCategoryDescriptionCode",
    "EInventoryTypeCode",
    "EDamageDetailsCodeQualifier",
    "EObjectTypeCodeQualifier",
    "EStructureComponentFunctionCodeQualifier",
    "EDamageTypeDescription",
    "EDamageTypeDescriptionCode",
    "EDamageAreaDescription",
    "EDamageAreaDescriptionCode",
    "EUnitOrComponentTypeDescription",
    "EUnitOrComponentTypeDescriptionCode",
    "EComponentMaterialDescription",
    "EComponentMaterialDescriptionCode",
    "EDamageSeverityDescription",
    "EDamageSeverityDescriptionCode",
    "EMarkingTypeCode",
    "EStructureComponentIdentifier",
    "EStructureTypeCode",
    "EBenefitAndCoverageCode",
    "ETrafficRestrictionCode",
    "ETrafficRestrictionApplicationCode",
    "EFreightAndOtherChargesDescription",
    "EFreightAndOtherChargesDescriptionIdentifier",
    "EConveyanceCallPurposeDescription",
    "EConveyanceCallPurposeDescriptionCode",
    "EMeansOfTransportJourneyIdentifier",
    "ETrafficRestrictionTypeCodeQualifier",
    "ETransportStageCodeQualifier",
    "EEquipmentTypeCodeQualifier",
    "ETransportModeName",
    "ETransportModeNameCode",
    "EEquipmentSupplierCode",
    "EAdditionalHazardClassificationIdentifier",
    "EHazardCodeVersionIdentifier",
    "ETransitDirectionIndicatorCode",
    "ETransportEmergencyCardIdentifier",
    "EEquipmentSizeAndTypeDescription",
    "EEquipmentSizeAndTypeDescriptionCode",
    "EOrangeHazardPlacardUpperPartIdentifier",
    "EFullOrEmptyIndicatorCode",
    "ETransportMeansDescription",
    "ETransportMeansDescriptionCode",
    "EOrangeHazardPlacardLowerPartIdentifier",
    "EHazardousCargoTransportAuthorisationCode",
    "ETransportMeansIdentificationName",
    "ETransportMeansIdentificationNameIdentifier",
    "ETransportMeansChangeIndicatorCode",
    "EJourneyStopsQuantity",
    "ETravellerAccompaniedByInfantIndicatorCode",
    "EDangerousGoodsMarkingIdentifier",
    "EEquipmentStatusCode",
    "EPackingInstructionTypeCode",
    "EEquipmentIdentifier",
    "EDangerousGoodsRegulationsCode",
    "EContainerOrPackageContentsIndicatorCode",
    "ETransportMeansOwnershipIndicatorCode",
    "ETransportMovementCode",
    "EEquipmentPlanDescription",
    "EMovementTypeDescription",
    "EMovementTypeDescriptionCode",
    "EPackagingDangerLevelCode",
    "EHaulageArrangementsCode",
    "EHazardIdentificationCode",
    "EEmergencyProcedureForShipsIdentifier",
    "EReturnablePackageLoadContentsCode",
    "EReturnablePackageFreightPaymentResponsibilityCode",
    "EHazardMedicalFirstAidGuideIdentifier",
    "ETransportMeansNationalityCode",
    "EExcessTransportationReasonCode",
    "EExcessTransportationResponsibilityCode",
    "ETunnelRestrictionCode",
    "ETransportServiceIdentificationCode",
    "ETransportServiceName",
    "ETransportServiceDescription",
    "EEmploymentDetailsCodeQualifier",
    "EEmploymentCategoryDescription",
    "EEmploymentCategoryDescriptionCode",
    "EQualificationClassificationDescription",
    "EQualificationClassificationDescriptionCode",
    "EOccupationDescription",
    "EOccupationDescriptionCode",
    "EStatusReasonDescription",
    "EStatusReasonDescriptionCode",
    "EStatusCategoryCode",
    "EAttributeFunctionCodeQualifier",
    "EAttributeDescription",
    "EAttributeDescriptionCode",
    "EAttributeTypeDescription",
    "EAttributeTypeDescriptionCode",
    "EDefinitionFunctionCode",
    "EDefinitionExtentCode",
    "EEditMaskFormatIdentifier",
    "EValueDefinitionCodeQualifier",
    "EEditMaskRepresentationCode",
    "EQualificationApplicationAreaCode",
    "EQualificationTypeCodeQualifier",
    "EFacilityTypeDescription",
    "EFacilityTypeDescriptionCode",
    "EReservationIdentifier",
    "EReservationIdentifierCodeQualifier",
    "EBasisCodeQualifier",
    "EBasisTypeDescription",
    "EBasisTypeDescriptionCode",
    "EApplicabilityTypeDescription",
    "EApplicabilityTypeDescriptionCode",
    "EApplicabilityCodeQualifier",
    "ERelationshipTypeCodeQualifier",
    "ERelationshipDescription",
    "ERelationshipDescriptionCode",
    "ECompositeDataElementTagIdentifier",
    "EDirectoryStatusIdentifier",
    "ESimpleDataElementTagIdentifier",
    "ESimpleDataElementCharacterRepresentationCode",
    "ESimpleDataElementMaximumLengthMeasure",
    "ESimpleDataElementMinimumLengthMeasure",
    "ECodeSetIndicatorCode",
    "EDataElementTagIdentifier",
    "EGroupIdentifier",
    "ESegmentTagIdentifier",
    "EDataRepresentationTypeCode",
    "EEventTypeDescription",
    "EEventTypeDescriptionCode",
    "EEvent",
    "EEventDescriptionCode",
    "EDataElementUsageTypeCode",
    "EDutyRegimeTypeCode",
    "EValidationResultText",
    "EValidationKeyIdentifier",
    "EValidationCriteriaCode",
    "ESealingPartyName",
    "ESealingPartyNameCode",
    "ETransportUnitSealIdentifier",
    "EApplicationErrorCode",
    "EGovernmentProcedureCode",
    "EGovernmentInvolvementCode",
    "EGovernmentAgencyIdentificationCode",
    "EGovernmentActionCode",
    "EServiceLayerCode",
    "EProcessStageCodeQualifier",
    "EValueText",
    "EArrayCellDataDescription",
    "ECodeValueText",
    "EArrayCellStructureIdentifier",
    "EFootnoteSetIdentifier",
    "EFootnoteIdentifier",
    "ECodeName",
    "EClinicalInterventionDescription",
    "EClinicalInterventionDescriptionCode",
    "EClinicalInterventionTypeCodeQualifier",
    "EAttendanceTypeCodeQualifier",
    "EAdmissionTypeDescription",
    "EAdmissionTypeDescriptionCode",
    "EDischargeTypeDescription",
    "EDischargeTypeDescriptionCode",
    "EFileGenerationCommandName",
    "EFileCompressionTechniqueName",
    "ECodeValueSourceCode",
    "EFormulaTypeCodeQualifier",
    "EFormulaName",
    "EFormulaComplexityCode",
    "EFormulaSequenceCodeQualifier",
    "EFormulaSequenceOperandCode",
    "EFormulaSequenceName",
    "EInformationCategoryCode",
    "EDataCodeQualifier",
    "EYesOrNoIndicatorCode",
    "EAdjustmentCategoryCode",
    "EPolicyLimitationIdentifier",
    "EDiagnosisTypeCode",
    "ERelatedCauseCode",
    "EAdmissionSourceCode",
    "EProcedureModificationCode",
    "EInvoiceTypeCode",
    "EEventDetailsCodeQualifier",
    "EEventCategoryDescription",
    "EEventCategoryDescriptionCode",
    "EDiagnosisCategoryCode",
    "EServiceBasisCodeQualifier",
    "ESupportingEvidenceTypeCodeQualifier",
    "EPayerResponsibilityLevelCode",
    "ECavityZoneCode",
    "EProcessingInformationCodeQualifier",
]
