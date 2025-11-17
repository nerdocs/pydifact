# ------------------- Composite Data Elements -------------------
# created from EDCD - the EDIFACT composite data elements directory
# This file is auto-generated. Don't edit it manually.

# Copyright (c) 2017-2025 Christian González
# This file is licensed under the MIT license, see LICENSE file.

from pydifact.syntax.common.types import CompositeDataElement, CompositeSchemaEntryList
from .data import *


class CSSyntaxIdentifier(CompositeDataElement):
    """Identification of the agency controlling the syntax, the syntax level and version number, and the service code directory."""

    code: str = "S001"
    title: str = "Syntax identifier"
    schema: CompositeSchemaEntryList = [
        (SyntaxIdentifier, True, "a4"),
        (SyntaxVersionNumber, True, "an1"),
        (ServiceCodeListDirectoryVersionNumber, False, "an..6"),
        (CharacterEncodingCoded, False, "an..3"),
        (SyntaxReleaseNumber, False, "an2"),
    ]


class CSInterchangeSender(CompositeDataElement):
    """Identification of the sender of the interchange."""

    code: str = "S002"
    title: str = "Interchange sender"
    schema: CompositeSchemaEntryList = [
        (InterchangeSenderIdentification, True, "an..35"),
        (IdentificationCodeQualifier, False, "an..4"),
        (InterchangeSenderInternalIdentification, False, "an..35"),
    ]


class CSInterchangeRecipient(CompositeDataElement):
    """Identification of the recipient of the interchange."""

    code: str = "S003"
    title: str = "Interchange recipient"
    schema: CompositeSchemaEntryList = [
        (InterchangeRecipientIdentification, True, "an..35"),
        (IdentificationCodeQualifier, False, "an..4"),
        (InterchangeRecipientInternalIdentification, False, "an..35"),
    ]


class CSDateAndTimeOfPreparation(CompositeDataElement):
    """Date and time of preparation of the interchange."""

    code: str = "S004"
    title: str = "Date and time of preparation"
    schema: CompositeSchemaEntryList = [
        (Date, True, "n8"),
        (Time, True, "n4"),
    ]


class CSRecipientReferencepasswordDetails(CompositeDataElement):
    """Reference or password as agreed between the communicating partners."""

    code: str = "S005"
    title: str = "Recipient reference/password details"
    schema: CompositeSchemaEntryList = [
        (RecipientReferencepassword, True, "an..14"),
        (RecipientReferencepasswordQualifier, False, "an2"),
    ]


class CSApplicationSenderIdentification(CompositeDataElement):
    """Sender identification of for example a division, branch or application computer system/process."""

    code: str = "S006"
    title: str = "Application sender identification"
    schema: CompositeSchemaEntryList = [
        (ApplicationSenderIdentification, True, "an..35"),
        (IdentificationCodeQualifier, False, "an..4"),
    ]


class CSApplicationRecipientIdentification(CompositeDataElement):
    """Recipient identification of for example a division, branch or application computer system/process."""

    code: str = "S007"
    title: str = "Application recipient identification"
    schema: CompositeSchemaEntryList = [
        (ApplicationRecipientIdentification, True, "an..35"),
        (IdentificationCodeQualifier, False, "an..4"),
    ]


class CSMessageVersion(CompositeDataElement):
    """Specification of the version and release numbers of all of the messages of a single type in the group."""

    code: str = "S008"
    title: str = "Message version"
    schema: CompositeSchemaEntryList = [
        (MessageVersionNumber, True, "an..3"),
        (MessageReleaseNumber, True, "an..3"),
        (AssociationAssignedCode, False, "an..6"),
    ]


class CSMessageIdentifier(CompositeDataElement):
    """Identification of the type, version, etc. of the message being interchanged."""

    code: str = "S009"
    title: str = "Message identifier"
    schema: CompositeSchemaEntryList = [
        (MessageType, True, "an..6"),
        (MessageVersionNumber, True, "an..3"),
        (MessageReleaseNumber, True, "an..3"),
        (ControllingAgencyCoded, True, "an..3"),
        (AssociationAssignedCode, False, "an..6"),
        (CodeListDirectoryVersionNumber, False, "an..6"),
        (MessageTypeSubfunctionIdentification, False, "an..6"),
    ]


class CSStatusOfTheTransfer(CompositeDataElement):
    """Statement that the message is one in a sequence of transfers relating to the same topic."""

    code: str = "S010"
    title: str = "Status of the transfer"
    schema: CompositeSchemaEntryList = [
        (SequenceOfTransfers, True, "n..2"),
        (FirstAndLastTransfer, False, "a1"),
    ]


class CSDataElementIdentification(CompositeDataElement):
    """Identification of the position for an erroneous data element. This can be the position of a stand-alone or composite data element in the definition of a segment or a component data element in the definition of a composite data element."""

    code: str = "S011"
    title: str = "Data element identification"
    schema: CompositeSchemaEntryList = [
        (ErroneousDataElementPositionInSegment, True, "n..3"),
    ]


class CSMessageSubsetIdentification(CompositeDataElement):
    """Identification of a message subset by its identifier, version, release and source."""

    code: str = "S016"
    title: str = "Message subset identification"
    schema: CompositeSchemaEntryList = [
        (MessageSubsetIdentification, True, "an..14"),
        (MessageSubsetVersionNumber, False, "an..3"),
        (MessageSubsetReleaseNumber, False, "an..3"),
        (ControllingAgencyCoded, False, "an..3"),
    ]


class CSMessageImplementationGuidelineIdentification(CompositeDataElement):
    """Identification of a message implementation guideline by its identifier, version, release and source."""

    code: str = "S017"
    title: str = "Message implementation guideline identification"
    schema: CompositeSchemaEntryList = [
        (ControllingAgencyCoded, False, "an..3"),
    ]


class CSScenarioIdentification(CompositeDataElement):
    """Identification of a scenario."""

    code: str = "S018"
    title: str = "Scenario identification"
    schema: CompositeSchemaEntryList = [
        (ScenarioIdentification, True, "an..14"),
        (ScenarioVersionNumber, False, "an..3"),
        (ScenarioReleaseNumber, False, "an..3"),
        (ControllingAgencyCoded, False, "an..3"),
    ]


class CSReferenceIdentification(CompositeDataElement):
    """Identification of the reference relating to the object."""

    code: str = "S020"
    title: str = "Reference identification"
    schema: CompositeSchemaEntryList = [
        (ReferenceQualifier, True, "an..3"),
        (ReferenceIdentificationNumber, True, "an..35"),
    ]


class CSObjectTypeIdentification(CompositeDataElement):
    """Identification of the attribute related to the object type."""

    code: str = "S021"
    title: str = "Object type identification"
    schema: CompositeSchemaEntryList = [
        (ObjectTypeQualifier, True, "an..3"),
        (ControllingAgencyCoded, False, "an..3"),
    ]


class CSStatusOfTheObject(CompositeDataElement):
    """Identification of the length and if required the transfer status of the object."""

    code: str = "S022"
    title: str = "Status of the object"
    schema: CompositeSchemaEntryList = [
        (LengthOfObjectInOctetsOfBits, True, "n..18"),
        (NumberOfSegmentsBeforeObject, False, "n..3"),
        (SequenceOfTransfers, False, "n..2"),
        (FirstAndLastTransfer, False, "a1"),
    ]


class CSDateAndorTimeOfInitiation(CompositeDataElement):
    """Date and/or time of event initiation."""

    code: str = "S300"
    title: str = "Date and/or time of initiation"
    schema: CompositeSchemaEntryList = [
        (EventDate, False, "n..8"),
    ]


class CSStatusOfTransferInteractive(CompositeDataElement):
    """Identifies the sequence of the message/package within the sender's interchange and the position in a multi-message and/or package transfer."""

    code: str = "S301"
    title: str = "Status of transfer - interactive"
    schema: CompositeSchemaEntryList = []


class CSDialogueReference(CompositeDataElement):
    """Unique reference for the dialogue between co-operating parties within the interactive EDI transaction."""

    code: str = "S302"
    title: str = "Dialogue reference"
    schema: CompositeSchemaEntryList = [
        (InitiatorControlReference, True, "an..35"),
        (ResponderControlReference, False, "an..35"),
    ]


class CSTransactionReference(CompositeDataElement):
    """Unique reference for the business transaction to which the dialogue belongs."""

    code: str = "S303"
    title: str = "Transaction reference"
    schema: CompositeSchemaEntryList = [
        (TransactionControlReference, True, "an..35"),
    ]


class CSDialogueIdentification(CompositeDataElement):
    """Identification of the dialogue type being used for the interactive EDI transaction."""

    code: str = "S305"
    title: str = "Dialogue identification"
    schema: CompositeSchemaEntryList = [
        (DialogueIdentification, True, "an..14"),
        (DialogueVersionNumber, False, "an..3"),
        (DialogueReleaseNumber, False, "an..3"),
        (ControllingAgencyCoded, False, "an..3"),
    ]


class CSInteractiveMessageIdentifier(CompositeDataElement):
    """Identification of the type, version and details of the message being interchanged."""

    code: str = "S306"
    title: str = "Interactive message identifier"
    schema: CompositeSchemaEntryList = [
        (MessageType, True, "an..6"),
        (MessageVersionNumber, True, "an..3"),
        (MessageReleaseNumber, True, "an..3"),
        (MessageTypeSubfunctionIdentification, False, "an..6"),
        (ControllingAgencyCoded, False, "an..3"),
        (AssociationAssignedCode, False, "an..6"),
    ]


class CSStatusInformation(CompositeDataElement):
    """Reason for status or error report."""

    code: str = "S307"
    title: str = "Status information"
    schema: CompositeSchemaEntryList = [
        (StatusCoded, False, "an..3"),
    ]


class CSSecurityIdentificationDetails(CompositeDataElement):
    """Identification of parties involved in the security process."""

    code: str = "S500"
    title: str = "Security identification details"
    schema: CompositeSchemaEntryList = [
        (SecurityPartyQualifier, True, "an..3"),
        (KeyName, False, "an..35"),
        (SecurityPartyName, False, "an..35"),
        (SecurityPartyName, False, "an..35"),
        (SecurityPartyName, False, "an..35"),
    ]


class CSSecurityDateAndTime(CompositeDataElement):
    """Security related date and time."""

    code: str = "S501"
    title: str = "Security date and time"
    schema: CompositeSchemaEntryList = [
        (DateAndTimeQualifier, True, "an..3"),
        (EventDate, False, "n..8"),
        (EventTime, False, "an..15"),
        (TimeOffset, False, "n4"),
    ]


class CSSecurityAlgorithm(CompositeDataElement):
    """Identification of a security algorithm."""

    code: str = "S502"
    title: str = "Security algorithm"
    schema: CompositeSchemaEntryList = [
        (UseOfAlgorithmCoded, True, "an..3"),
    ]


class CSAlgorithmParameter(CompositeDataElement):
    """Parameter required by a security algorithm."""

    code: str = "S503"
    title: str = "Algorithm parameter"
    schema: CompositeSchemaEntryList = [
        (AlgorithmParameterQualifier, True, "an..3"),
        (AlgorithmParameterValue, True, "an..512"),
    ]


class CSListParameter(CompositeDataElement):
    """Identification of a parameter for a list request or delivery"""

    code: str = "S504"
    title: str = "List parameter"
    schema: CompositeSchemaEntryList = [
        (ListParameterQualifier, True, "an..3"),
        (ListParameter, True, "an..70"),
    ]


class CSServiceCharacterForSignature(CompositeDataElement):
    """Identification of the characters used as syntactical service characters when a signature was computed."""

    code: str = "S505"
    title: str = "Service character for signature"
    schema: CompositeSchemaEntryList = [
        (ServiceCharacterForSignatureQualifier, True, "an..3"),
        (ServiceCharacterForSignature, True, "an..4"),
    ]


class CSValidationResult(CompositeDataElement):
    """Result of the application of the security mechanism."""

    code: str = "S508"
    title: str = "Validation result"
    schema: CompositeSchemaEntryList = [
        (ValidationValueQualifier, True, "an..3"),
    ]


class CUTransportMeans(CompositeDataElement):
    """Code and/or name identifying the type of means of transport."""

    code: str = "C001"
    title: str = "Transport means"
    schema: CompositeSchemaEntryList = [
        (ETransportMeansDescriptionCode, False, "an..8"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ETransportMeansDescription, False, "an..17"),
    ]


class CUDocumentmessageName(CompositeDataElement):
    """Identification of a type of document/message by code or name. Code preferred."""

    code: str = "C002"
    title: str = "Document/message name"
    schema: CompositeSchemaEntryList = [
        (EDocumentNameCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EDocumentName, False, "an..35"),
    ]


class CUPowerType(CompositeDataElement):
    """To specify the type of power."""

    code: str = "C003"
    title: str = "Power type"
    schema: CompositeSchemaEntryList = [
        (EPowerTypeCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EPowerTypeDescription, False, "an..17"),
    ]


class CUEventCategory(CompositeDataElement):
    """To specify the event category."""

    code: str = "C004"
    title: str = "Event category"
    schema: CompositeSchemaEntryList = [
        (EEventCategoryDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EEventCategoryDescription, False, "an..70"),
    ]


class CUMonetaryAmountFunctionDetail(CompositeDataElement):
    """To provide the detail of a monetary amount function."""

    code: str = "C008"
    title: str = "Monetary amount function detail"
    schema: CompositeSchemaEntryList = [
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUInformationCategory(CompositeDataElement):
    """To specify the category of information."""

    code: str = "C009"
    title: str = "Information category"
    schema: CompositeSchemaEntryList = [
        (EInformationCategoryDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EInformationCategoryDescription, False, "an..70"),
    ]


class CUInformationType(CompositeDataElement):
    """To specify the type of information."""

    code: str = "C010"
    title: str = "Information type"
    schema: CompositeSchemaEntryList = [
        (EInformationTypeCode, False, "an..4"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EInformationType, False, "an..35"),
    ]


class CUInformationDetail(CompositeDataElement):
    """To provide the information details."""

    code: str = "C011"
    title: str = "Information detail"
    schema: CompositeSchemaEntryList = [
        (EInformationDetailDescriptionCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EInformationDetailDescription, False, "an..256"),
    ]


class CUProcessingIndicator(CompositeDataElement):
    """Identification of the processing indicator."""

    code: str = "C012"
    title: str = "Processing indicator"
    schema: CompositeSchemaEntryList = [
        (EProcessingIndicatorDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EProcessingIndicatorDescription, False, "an..35"),
    ]


class CUPaymentTerms(CompositeDataElement):
    """Terms of payment information."""

    code: str = "C019"
    title: str = "Payment terms"
    schema: CompositeSchemaEntryList = [
        (EPaymentTermsDescriptionIdentifier, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EPaymentTermsDescription, False, "an..35"),
    ]


class CUEventType(CompositeDataElement):
    """To specify the type of event."""

    code: str = "C030"
    title: str = "Event type"
    schema: CompositeSchemaEntryList = [
        (EEventTypeDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EEventTypeDescription, False, "an..70"),
    ]


class CUCarrier(CompositeDataElement):
    """Identification of a carrier by code and/or by name. Code preferred."""

    code: str = "C040"
    title: str = "Carrier"
    schema: CompositeSchemaEntryList = [
        (ECarrierIdentifier, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ECarrierName, False, "an..35"),
    ]


class CUNationalityDetails(CompositeDataElement):
    """To specify a nationality."""

    code: str = "C042"
    title: str = "Nationality details"
    schema: CompositeSchemaEntryList = [
        (ENationalityNameCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ENationalityName, False, "a..35"),
    ]


class CUBillLevelIdentification(CompositeDataElement):
    """A sequenced collection of facetted codes used for multiple indexing purposes."""

    code: str = "C045"
    title: str = "Bill level identification"
    schema: CompositeSchemaEntryList = [
        (ELevelOneIdentifier, False, "an..17"),
        (ELevelTwoIdentifier, False, "an..17"),
        (ELevelThreeIdentifier, False, "an..17"),
        (ELevelFourIdentifier, False, "an..17"),
        (ELevelFiveIdentifier, False, "an..17"),
        (ELevelSixIdentifier, False, "an..17"),
    ]


class CURemunerationTypeIdentification(CompositeDataElement):
    """Identification of the type of a remuneration."""

    code: str = "C049"
    title: str = "Remuneration type identification"
    schema: CompositeSchemaEntryList = [
        (ERemunerationTypeNameCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ERemunerationTypeName, False, "an..35"),
        (ERemunerationTypeName, False, "an..35"),
    ]


class CUContactDetails(CompositeDataElement):
    """Code and/or name of a contact such as a department or employee. Code preferred."""

    code: str = "C056"
    title: str = "Contact details"
    schema: CompositeSchemaEntryList = [
        (EContactIdentifier, False, "an..17"),
        (EContactName, False, "an..256"),
    ]


class CUNameAndAddress(CompositeDataElement):
    """Unstructured name and address: one to five lines."""

    code: str = "C058"
    title: str = "Name and address"
    schema: CompositeSchemaEntryList = [
        (ENameAndAddressDescription, True, "an..35"),
        (ENameAndAddressDescription, False, "an..35"),
        (ENameAndAddressDescription, False, "an..35"),
        (ENameAndAddressDescription, False, "an..35"),
        (ENameAndAddressDescription, False, "an..35"),
    ]


class CUStreet(CompositeDataElement):
    """Street address and/or PO Box number in a structured address: one to four lines."""

    code: str = "C059"
    title: str = "Street"
    schema: CompositeSchemaEntryList = []


class CUEventIdentification(CompositeDataElement):
    """To identify an event."""

    code: str = "C063"
    title: str = "Event identification"
    schema: CompositeSchemaEntryList = [
        (EEventDescriptionCode, False, "an..35"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EEvent, False, "an..256"),
    ]


class CUCommunicationContact(CompositeDataElement):
    """Communication number of a department or employee in a specified channel."""

    code: str = "C076"
    title: str = "Communication contact"
    schema: CompositeSchemaEntryList = [
        (ECommunicationAddressIdentifier, True, "an..512"),
        (ECommunicationMeansTypeCode, True, "an..3"),
    ]


class CUFileIdentification(CompositeDataElement):
    """To identify a file."""

    code: str = "C077"
    title: str = "File identification"
    schema: CompositeSchemaEntryList = [
        (EFileName, False, "an..35"),
        (EItemDescription, False, "an..256"),
    ]


class CUAccountHolderIdentification(CompositeDataElement):
    """Identification of an account holder by account number and/or account holder name in one or two lines. Number preferred."""

    code: str = "C078"
    title: str = "Account holder identification"
    schema: CompositeSchemaEntryList = [
        (EAccountHolderIdentifier, False, "an..35"),
        (EAccountHolderName, False, "an..35"),
        (EAccountHolderName, False, "an..35"),
        (ECurrencyIdentificationCode, False, "an..3"),
    ]


class CUComputerEnvironmentIdentification(CompositeDataElement):
    """To identify parts of a computer environment."""

    code: str = "C079"
    title: str = "Computer environment identification"
    schema: CompositeSchemaEntryList = [
        (EComputerEnvironmentNameCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EComputerEnvironmentName, False, "an..35"),
        (EVersionIdentifier, False, "an..9"),
        (EReleaseIdentifier, False, "an..9"),
        (EObjectIdentifier, False, "an..35"),
    ]


class CUPartyName(CompositeDataElement):
    """Identification of a transaction party by name, one to five lines. Party name may be formatted."""

    code: str = "C080"
    title: str = "Party name"
    schema: CompositeSchemaEntryList = [
        (EPartyName, True, "an..70"),
        (EPartyName, False, "an..70"),
        (EPartyName, False, "an..70"),
        (EPartyName, False, "an..70"),
        (EPartyName, False, "an..70"),
        (EPartyNameFormatCode, False, "an..3"),
    ]


class CUPartyIdentificationDetails(CompositeDataElement):
    """Identification of a transaction party by code."""

    code: str = "C082"
    title: str = "Party identification details"
    schema: CompositeSchemaEntryList = [
        (EPartyIdentifier, True, "an..35"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUMaritalStatusDetails(CompositeDataElement):
    """To specify the marital status of a person."""

    code: str = "C085"
    title: str = "Marital status details"
    schema: CompositeSchemaEntryList = [
        (EMaritalStatusDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EMaritalStatusDescription, False, "an..35"),
    ]


class CUInstitutionIdentification(CompositeDataElement):
    """Identification of a financial institution by code branch number, or name and name of place. Code or branch number preferred."""

    code: str = "C088"
    title: str = "Institution identification"
    schema: CompositeSchemaEntryList = [
        (EInstitutionNameCode, False, "an..11"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EInstitutionBranchIdentifier, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EInstitutionName, False, "an..70"),
        (EInstitutionBranchLocationName, False, "an..70"),
    ]


class CUAddressDetails(CompositeDataElement):
    """To specify the details of an address."""

    code: str = "C090"
    title: str = "Address details"
    schema: CompositeSchemaEntryList = [
        (EAddressFormatCode, True, "an..3"),
        (EAddressComponentDescription, True, "an..70"),
        (EAddressComponentDescription, False, "an..70"),
        (EAddressComponentDescription, False, "an..70"),
        (EAddressComponentDescription, False, "an..70"),
        (EAddressComponentDescription, False, "an..70"),
    ]


class CUFileDetails(CompositeDataElement):
    """To define details relevant to a file."""

    code: str = "C099"
    title: str = "File details"
    schema: CompositeSchemaEntryList = [
        (EFileFormatName, True, "an..17"),
        (EVersionIdentifier, False, "an..9"),
        (EDataFormatDescriptionCode, False, "an..3"),
        (EDataFormatDescription, False, "an..35"),
    ]


class CUTermsOfDeliveryOrTransport(CompositeDataElement):
    """Terms of delivery or transport code from a specified source."""

    code: str = "C100"
    title: str = "Terms of delivery or transport"
    schema: CompositeSchemaEntryList = [
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EDeliveryOrTransportTermsDescription, False, "an..70"),
        (EDeliveryOrTransportTermsDescription, False, "an..70"),
    ]


class CUReligionDetails(CompositeDataElement):
    """To specify the religion of a person."""

    code: str = "C101"
    title: str = "Religion details"
    schema: CompositeSchemaEntryList = [
        (EReligionNameCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EReligionName, False, "an..35"),
    ]


class CUDocumentmessageIdentification(CompositeDataElement):
    """Identification of a document/message by its number and eventually its version or revision."""

    code: str = "C106"
    title: str = "Document/message identification"
    schema: CompositeSchemaEntryList = [
        (EDocumentIdentifier, False, "an..70"),
        (EVersionIdentifier, False, "an..9"),
        (ERevisionIdentifier, False, "an..6"),
    ]


class CUTextReference(CompositeDataElement):
    """Coded reference to a standard text and its source."""

    code: str = "C107"
    title: str = "Text reference"
    schema: CompositeSchemaEntryList = [
        (EFreeTextDescriptionCode, True, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUTextLiteral(CompositeDataElement):
    """Free text; one to five lines."""

    code: str = "C108"
    title: str = "Text literal"
    schema: CompositeSchemaEntryList = [
        (EFreeText, True, "an..512"),
        (EFreeText, False, "an..512"),
        (EFreeText, False, "an..512"),
        (EFreeText, False, "an..512"),
        (EFreeText, False, "an..512"),
    ]


class CURateDetails(CompositeDataElement):
    """Rate per unit and rate basis."""

    code: str = "C128"
    title: str = "Rate details"
    schema: CompositeSchemaEntryList = [
        (ERateTypeCodeQualifier, True, "an..3"),
        (EUnitPriceBasisRate, True, "n..15"),
        (EUnitPriceBasisQuantity, False, "n..9"),
        (EMeasurementUnitCode, False, "an..8"),
    ]


class CUPriceMultiplierInformation(CompositeDataElement):
    """Price multiplier and its identification."""

    code: str = "C138"
    title: str = "Price multiplier information"
    schema: CompositeSchemaEntryList = [
        (EPriceMultiplierRate, True, "n..12"),
        (EPriceMultiplierTypeCodeQualifier, False, "an..3"),
    ]


class CUValuerange(CompositeDataElement):
    """Measurement value and relevant minimum and maximum values of the measurement range."""

    code: str = "C174"
    title: str = "Value/range"
    schema: CompositeSchemaEntryList = [
        (EMeasurementUnitCode, False, "an..8"),
        (EMeasure, False, "an..18"),
        (ERangeMinimumQuantity, False, "n..18"),
        (ERangeMaximumQuantity, False, "n..18"),
        (ESignificantDigitsQuantity, False, "n..2"),
    ]


class CUQuantityDetails(CompositeDataElement):
    """Quantity information in a transaction, qualified when relevant."""

    code: str = "C186"
    title: str = "Quantity details"
    schema: CompositeSchemaEntryList = [
        (EQuantityTypeCodeQualifier, True, "an..3"),
        (EQuantity, True, "an..35"),
        (EMeasurementUnitCode, False, "an..8"),
    ]


class CUCharge(CompositeDataElement):
    """Identification of a charge by code and/or by name."""

    code: str = "C200"
    title: str = "Charge"
    schema: CompositeSchemaEntryList = [
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EFreightAndOtherChargesDescription, False, "an..26"),
        (EPaymentArrangementCode, False, "an..3"),
        (EItemIdentifier, False, "an..35"),
    ]


class CUPackageType(CompositeDataElement):
    """Type of package by name or by code from a specified source."""

    code: str = "C202"
    title: str = "Package type"
    schema: CompositeSchemaEntryList = [
        (EPackageTypeDescriptionCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ETypeOfPackages, False, "an..35"),
    ]


class CURatetariffClass(CompositeDataElement):
    """Identification of the applicable rate/tariff class."""

    code: str = "C203"
    title: str = "Rate/tariff class"
    schema: CompositeSchemaEntryList = [
        (ERateOrTariffClassDescriptionCode, True, "an..9"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ERateOrTariffClassDescription, False, "an..35"),
        (ESupplementaryRateOrTariffCode, False, "an..6"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ESupplementaryRateOrTariffCode, False, "an..6"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUHazardCode(CompositeDataElement):
    """The identification of the dangerous goods in code."""

    code: str = "C205"
    title: str = "Hazard code"
    schema: CompositeSchemaEntryList = [
        (EHazardIdentificationCode, True, "an..7"),
        (EHazardCodeVersionIdentifier, False, "an..10"),
    ]


class CUIdentificationNumber(CompositeDataElement):
    """The identification of an object."""

    code: str = "C206"
    title: str = "Identification number"
    schema: CompositeSchemaEntryList = [
        (EObjectIdentifier, True, "an..35"),
        (EObjectIdentificationCodeQualifier, False, "an..3"),
        (EStatusDescriptionCode, False, "an..3"),
    ]


class CUIdentityNumberRange(CompositeDataElement):
    """Goods item identification numbers, start and end of consecutively numbered range."""

    code: str = "C208"
    title: str = "Identity number range"
    schema: CompositeSchemaEntryList = [
        (EObjectIdentifier, True, "an..35"),
        (EObjectIdentifier, False, "an..35"),
    ]


class CUMarksLabels(CompositeDataElement):
    """Shipping marks on packages in free text; one to ten lines."""

    code: str = "C210"
    title: str = "Marks & labels"
    schema: CompositeSchemaEntryList = [
        (EShippingMarksDescription, True, "an..35"),
        (EShippingMarksDescription, False, "an..35"),
        (EShippingMarksDescription, False, "an..35"),
        (EShippingMarksDescription, False, "an..35"),
        (EShippingMarksDescription, False, "an..35"),
        (EShippingMarksDescription, False, "an..35"),
        (EShippingMarksDescription, False, "an..35"),
        (EShippingMarksDescription, False, "an..35"),
        (EShippingMarksDescription, False, "an..35"),
        (EShippingMarksDescription, False, "an..35"),
    ]


class CUDimensions(CompositeDataElement):
    """Specification of the dimensions of a transportable unit."""

    code: str = "C211"
    title: str = "Dimensions"
    schema: CompositeSchemaEntryList = [
        (EMeasurementUnitCode, True, "an..8"),
        (ELengthMeasure, False, "n..15"),
        (EWidthMeasure, False, "n..15"),
        (EHeightMeasure, False, "n..15"),
        (EDiameterMeasure, False, "n..15"),
    ]


class CUItemNumberIdentification(CompositeDataElement):
    """Goods identification for a specified source."""

    code: str = "C212"
    title: str = "Item number identification"
    schema: CompositeSchemaEntryList = [
        (EItemIdentifier, False, "an..35"),
        (EItemTypeIdentificationCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUNumberAndTypeOfPackages(CompositeDataElement):
    """Number and type of individual parts of a shipment."""

    code: str = "C213"
    title: str = "Number and type of packages"
    schema: CompositeSchemaEntryList = [
        (EPackageQuantity, False, "n..8"),
        (EPackageTypeDescriptionCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ETypeOfPackages, False, "an..35"),
        (EPackagingRelatedDescriptionCode, False, "an..3"),
    ]


class CUSpecialServicesIdentification(CompositeDataElement):
    """Identification of a special service by a code from a specified source or by description."""

    code: str = "C214"
    title: str = "Special services identification"
    schema: CompositeSchemaEntryList = [
        (ESpecialServiceDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ESpecialServiceDescription, False, "an..35"),
        (ESpecialServiceDescription, False, "an..35"),
    ]


class CUSealIssuer(CompositeDataElement):
    """Identification of the issuer of a seal on equipment either by code or by name."""

    code: str = "C215"
    title: str = "Seal issuer"
    schema: CompositeSchemaEntryList = [
        (ESealingPartyNameCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ESealingPartyName, False, "an..35"),
    ]


class CUHazardousMaterial(CompositeDataElement):
    """To specify a hazardous material."""

    code: str = "C218"
    title: str = "Hazardous material"
    schema: CompositeSchemaEntryList = [
        (EHazardousMaterialCategoryNameCode, False, "an..7"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EHazardousMaterialCategoryName, False, "an..35"),
    ]


class CUMovementType(CompositeDataElement):
    """Description of type of service for movement of cargo."""

    code: str = "C219"
    title: str = "Movement type"
    schema: CompositeSchemaEntryList = [
        (EMovementTypeDescriptionCode, False, "an..3"),
        (EMovementTypeDescription, False, "an..35"),
    ]


class CUModeOfTransport(CompositeDataElement):
    """Method of transport code or name. Code preferred."""

    code: str = "C220"
    title: str = "Mode of transport"
    schema: CompositeSchemaEntryList = [
        (ETransportModeNameCode, False, "an..3"),
        (ETransportModeName, False, "an..17"),
    ]


class CUTransportIdentification(CompositeDataElement):
    """Code and/or name identifying the means of transport."""

    code: str = "C222"
    title: str = "Transport identification"
    schema: CompositeSchemaEntryList = [
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ETransportMeansIdentificationName, False, "an..70"),
        (ETransportMeansNationalityCode, False, "an..3"),
    ]


class CUDangerousGoodsShipmentFlashpoint(CompositeDataElement):
    """Temperature at which a vapor can be ignited as per ISO 1523/73."""

    code: str = "C223"
    title: str = "Dangerous goods shipment flashpoint"
    schema: CompositeSchemaEntryList = [
        (EShipmentFlashpointDegree, False, "n3"),
        (EMeasurementUnitCode, False, "an..8"),
    ]


class CUEquipmentSizeAndType(CompositeDataElement):
    """Code and or name identifying size and type of equipment. Code preferred."""

    code: str = "C224"
    title: str = "Equipment size and type"
    schema: CompositeSchemaEntryList = [
        (EEquipmentSizeAndTypeDescriptionCode, False, "an..10"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EEquipmentSizeAndTypeDescription, False, "an..35"),
    ]


class CUChargeCategory(CompositeDataElement):
    """Identification of a category or a zone of charges."""

    code: str = "C229"
    title: str = "Charge category"
    schema: CompositeSchemaEntryList = [
        (EChargeCategoryCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUMethodOfPayment(CompositeDataElement):
    """Code identifying the method of payment."""

    code: str = "C231"
    title: str = "Method of payment"
    schema: CompositeSchemaEntryList = [
        (ETransportChargesPaymentMethodCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUGovernmentAction(CompositeDataElement):
    """Function: To indicate the requirement for a specific governmental action and/or procedure or which specific procedure is valid for a specific part of the transport and cross-border transactions. (Note the red portion as change in the segment description.)."""

    code: str = "C232"
    title: str = "Government action"
    schema: CompositeSchemaEntryList = [
        (EGovernmentAgencyIdentificationCode, False, "an..3"),
        (EGovernmentInvolvementCode, False, "an..3"),
        (EGovernmentActionCode, False, "an..3"),
        (EGovernmentProcedureCode, False, "an..3"),
    ]


class CUService(CompositeDataElement):
    """To identify a service (which may constitute an additional component to a basic contract)."""

    code: str = "C233"
    title: str = "Service"
    schema: CompositeSchemaEntryList = [
        (EServiceRequirementCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EServiceRequirementCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUUndgInformation(CompositeDataElement):
    """Information on dangerous goods, taken from the United Nations Dangerous Goods classification."""

    code: str = "C234"
    title: str = "Undg information"
    schema: CompositeSchemaEntryList = [
        (EDangerousGoodsFlashpointDescription, False, "an..8"),
    ]


class CUHazardIdentificationPlacardDetails(CompositeDataElement):
    """These numbers appear on the hazard identification placard required on the means of transport."""

    code: str = "C235"
    title: str = "Hazard identification placard details"
    schema: CompositeSchemaEntryList = []


class CUDangerousGoodsLabel(CompositeDataElement):
    """Markings identifying the type of hazardous goods and similar information."""

    code: str = "C236"
    title: str = "Dangerous goods label"
    schema: CompositeSchemaEntryList = [
        (EDangerousGoodsMarkingIdentifier, False, "an..4"),
        (EDangerousGoodsMarkingIdentifier, False, "an..4"),
        (EDangerousGoodsMarkingIdentifier, False, "an..4"),
        (EDangerousGoodsMarkingIdentifier, False, "an..4"),
    ]


class CUEquipmentIdentification(CompositeDataElement):
    """Marks (letters/numbers) identifying equipment."""

    code: str = "C237"
    title: str = "Equipment identification"
    schema: CompositeSchemaEntryList = [
        (EEquipmentIdentifier, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ECountryIdentifier, False, "an..3"),
    ]


class CUTemperatureSetting(CompositeDataElement):
    """The temperature under which the goods are (to be) stored or shipped."""

    code: str = "C239"
    title: str = "Temperature setting"
    schema: CompositeSchemaEntryList = [
        (ETemperatureDegree, False, "n..15"),
        (EMeasurementUnitCode, False, "an..8"),
    ]


class CUCharacteristicDescription(CompositeDataElement):
    """To provide a description of a characteristic."""

    code: str = "C240"
    title: str = "Characteristic description"
    schema: CompositeSchemaEntryList = [
        (ECharacteristicDescriptionCode, True, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ECharacteristicDescription, False, "an..35"),
        (ECharacteristicDescription, False, "an..35"),
    ]


class CUDutytaxfeeType(CompositeDataElement):
    """Code and/or name identifying duty, tax or fee."""

    code: str = "C241"
    title: str = "Duty/tax/fee type"
    schema: CompositeSchemaEntryList = [
        (EDutyOrTaxOrFeeTypeNameCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EDutyOrTaxOrFeeTypeName, False, "an..35"),
    ]


class CUProcessTypeAndDescription(CompositeDataElement):
    """Identification of process type and description."""

    code: str = "C242"
    title: str = "Process type and description"
    schema: CompositeSchemaEntryList = [
        (EProcessTypeDescriptionCode, True, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EProcessTypeDescription, False, "an..35"),
        (EProcessTypeDescription, False, "an..35"),
    ]


class CUDutytaxfeeDetail(CompositeDataElement):
    """Rate of duty/tax/fee applicable to commodities or of tax applicable to services."""

    code: str = "C243"
    title: str = "Duty/tax/fee detail"
    schema: CompositeSchemaEntryList = [
        (EDutyOrTaxOrFeeRateCode, False, "an..7"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EDutyOrTaxOrFeeRate, False, "an..17"),
        (EDutyOrTaxOrFeeRateBasisCode, False, "an..12"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUTestMethod(CompositeDataElement):
    """Specification of the test method employed."""

    code: str = "C244"
    title: str = "Test method"
    schema: CompositeSchemaEntryList = [
        (ETestMethodIdentifier, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ETestDescription, False, "an..70"),
    ]


class CUCustomsIdentityCodes(CompositeDataElement):
    """Specification of goods in terms of customs identity."""

    code: str = "C246"
    title: str = "Customs identity codes"
    schema: CompositeSchemaEntryList = [
        (ECustomsGoodsIdentifier, True, "an..18"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUControl(CompositeDataElement):
    """Control total for checking integrity of a message or part of a message."""

    code: str = "C270"
    title: str = "Control"
    schema: CompositeSchemaEntryList = [
        (EControlTotalTypeCodeQualifier, True, "an..3"),
        (EControlTotalQuantity, True, "n..18"),
        (EMeasurementUnitCode, False, "an..8"),
    ]


class CUItemCharacteristic(CompositeDataElement):
    """To provide the characteristic of the item being described."""

    code: str = "C272"
    title: str = "Item characteristic"
    schema: CompositeSchemaEntryList = [
        (EItemCharacteristicCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUItemDescription(CompositeDataElement):
    """Description of an item."""

    code: str = "C273"
    title: str = "Item description"
    schema: CompositeSchemaEntryList = [
        (EItemDescriptionCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EItemDescription, False, "an..256"),
        (EItemDescription, False, "an..256"),
        (ELanguageNameCode, False, "an..3"),
    ]


class CUQuantityDifferenceInformation(CompositeDataElement):
    """Information on quantity difference."""

    code: str = "C279"
    title: str = "Quantity difference information"
    schema: CompositeSchemaEntryList = [
        (EVarianceQuantity, True, "n..15"),
        (EQuantityTypeCodeQualifier, False, "an..3"),
    ]


class CURange(CompositeDataElement):
    """Range minimum and maximum limits."""

    code: str = "C280"
    title: str = "Range"
    schema: CompositeSchemaEntryList = [
        (EMeasurementUnitCode, True, "an..8"),
        (ERangeMinimumQuantity, False, "n..18"),
        (ERangeMaximumQuantity, False, "n..18"),
    ]


class CUSequenceInformation(CompositeDataElement):
    """Identification of a sequence and source for sequencing."""

    code: str = "C286"
    title: str = "Sequence information"
    schema: CompositeSchemaEntryList = [
        (ESequencePositionIdentifier, True, "an..10"),
        (ESequenceIdentifierSourceCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUProductGroup(CompositeDataElement):
    """To give product group information."""

    code: str = "C288"
    title: str = "Product group"
    schema: CompositeSchemaEntryList = [
        (EProductGroupNameCode, False, "an..25"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EProductGroupName, False, "an..35"),
    ]


class CUTunnelRestriction(CompositeDataElement):
    """To specify a restriction for transport through tunnels."""

    code: str = "C289"
    title: str = "Tunnel restriction"
    schema: CompositeSchemaEntryList = [
        (ETunnelRestrictionCode, False, "an..6"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUTransportService(CompositeDataElement):
    """To identify a transport service."""

    code: str = "C290"
    title: str = "Transport service"
    schema: CompositeSchemaEntryList = [
        (ETransportServiceIdentificationCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ETransportServiceName, False, "an..35"),
        (ETransportServiceDescription, False, "an..256"),
    ]


class CUPatternDescription(CompositeDataElement):
    """Shipment, delivery or production interval pattern and timing."""

    code: str = "C329"
    title: str = "Pattern description"
    schema: CompositeSchemaEntryList = [
        (EFrequencyCode, False, "an..3"),
        (EDespatchPatternCode, False, "an..3"),
        (EDespatchPatternTimingCode, False, "an..3"),
    ]


class CUInsuranceCoverType(CompositeDataElement):
    """To provide the insurance cover type."""

    code: str = "C330"
    title: str = "Insurance cover type"
    schema: CompositeSchemaEntryList = [
        (EInsuranceCoverTypeCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUInsuranceCoverDetails(CompositeDataElement):
    """To provide the insurance cover details."""

    code: str = "C331"
    title: str = "Insurance cover details"
    schema: CompositeSchemaEntryList = [
        (EInsuranceCoverDescriptionCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EInsuranceCoverDescription, False, "an..35"),
        (EInsuranceCoverDescription, False, "an..35"),
    ]


class CUSalesChannelIdentification(CompositeDataElement):
    """Identification of sales channel for marketing data, sales, forecast, planning..."""

    code: str = "C332"
    title: str = "Sales channel identification"
    schema: CompositeSchemaEntryList = [
        (ESalesChannelIdentifier, True, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUInformationRequest(CompositeDataElement):
    """To specify the information requested in a responding message."""

    code: str = "C333"
    title: str = "Information request"
    schema: CompositeSchemaEntryList = [
        (ERequestedInformationDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ERequestedInformationDescription, False, "an..35"),
    ]


class CUExcessTransportationInformation(CompositeDataElement):
    """To provide details of reason for, and responsibility for, use of transportation other than normally utilized."""

    code: str = "C401"
    title: str = "Excess transportation information"
    schema: CompositeSchemaEntryList = [
        (EExcessTransportationReasonCode, True, "an..3"),
        (EExcessTransportationResponsibilityCode, True, "an..3"),
    ]


class CUPackageTypeIdentification(CompositeDataElement):
    """Identification of the form in which goods are described."""

    code: str = "C402"
    title: str = "Package type identification"
    schema: CompositeSchemaEntryList = [
        (EDescriptionFormatCode, True, "an..3"),
        (ETypeOfPackages, True, "an..35"),
        (EItemTypeIdentificationCode, False, "an..3"),
        (ETypeOfPackages, False, "an..35"),
        (EItemTypeIdentificationCode, False, "an..3"),
    ]


class CUPercentageDetails(CompositeDataElement):
    """Percentage relating to a specified basis."""

    code: str = "C501"
    title: str = "Percentage details"
    schema: CompositeSchemaEntryList = [
        (EPercentageTypeCodeQualifier, True, "an..3"),
        (EPercentage, False, "n..10"),
        (EPercentageBasisIdentificationCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUMeasurementDetails(CompositeDataElement):
    """Identification of measurement type."""

    code: str = "C502"
    title: str = "Measurement details"
    schema: CompositeSchemaEntryList = [
        (EMeasuredAttributeCode, False, "an..3"),
        (EMeasurementSignificanceCode, False, "an..3"),
        (ENondiscreteMeasurementNameCode, False, "an..17"),
        (ENondiscreteMeasurementName, False, "an..70"),
    ]


class CUDocumentmessageDetails(CompositeDataElement):
    """Identification of document/message by number, status, source and/or language."""

    code: str = "C503"
    title: str = "Document/message details"
    schema: CompositeSchemaEntryList = [
        (EDocumentIdentifier, False, "an..70"),
        (EDocumentStatusCode, False, "an..3"),
        (EDocumentSourceDescription, False, "an..70"),
        (ELanguageNameCode, False, "an..3"),
        (EVersionIdentifier, False, "an..9"),
        (ERevisionIdentifier, False, "an..6"),
    ]


class CUCurrencyDetails(CompositeDataElement):
    """The usage to which a currency relates."""

    code: str = "C504"
    title: str = "Currency details"
    schema: CompositeSchemaEntryList = [
        (ECurrencyUsageCodeQualifier, True, "an..3"),
        (ECurrencyIdentificationCode, False, "an..3"),
        (ECurrencyTypeCodeQualifier, False, "an..3"),
        (ECurrencyRate, False, "n..4"),
    ]


class CUReference(CompositeDataElement):
    """Identification of a reference."""

    code: str = "C506"
    title: str = "Reference"
    schema: CompositeSchemaEntryList = [
        (EReferenceCodeQualifier, True, "an..3"),
        (EReferenceIdentifier, False, "an..70"),
        (EDocumentLineIdentifier, False, "an..6"),
        (EVersionIdentifier, False, "an..9"),
        (ERevisionIdentifier, False, "an..6"),
    ]


class CUDatetimeperiod(CompositeDataElement):
    """Date and/or time, or period relevant to the specified date/time/period type."""

    code: str = "C507"
    title: str = "Date/time/period"
    schema: CompositeSchemaEntryList = [
        (EDateOrTimeOrPeriodText, False, "an..35"),
        (EDateOrTimeOrPeriodFormatCode, False, "an..3"),
    ]


class CULanguageDetails(CompositeDataElement):
    """To identify a language."""

    code: str = "C508"
    title: str = "Language details"
    schema: CompositeSchemaEntryList = [
        (ELanguageNameCode, False, "an..3"),
        (ELanguageName, False, "an..35"),
    ]


class CUPriceInformation(CompositeDataElement):
    """Identification of price type, price and related details."""

    code: str = "C509"
    title: str = "Price information"
    schema: CompositeSchemaEntryList = [
        (EPriceCodeQualifier, True, "an..3"),
        (EPriceAmount, False, "n..15"),
        (EPriceTypeCode, False, "an..3"),
        (EPriceSpecificationCode, False, "an..3"),
        (EUnitPriceBasisQuantity, False, "n..9"),
        (EMeasurementUnitCode, False, "an..8"),
    ]


class CUSizeDetails(CompositeDataElement):
    """Information about the number of observations."""

    code: str = "C512"
    title: str = "Size details"
    schema: CompositeSchemaEntryList = [
        (ESizeTypeCodeQualifier, False, "an..3"),
        (ESizeMeasure, False, "n..15"),
    ]


class CUSampleLocationDetails(CompositeDataElement):
    """Identification of location within the specimen, from which the sample was taken."""

    code: str = "C514"
    title: str = "Sample location details"
    schema: CompositeSchemaEntryList = [
        (ESampleLocationDescriptionCode, False, "an..3"),
        (ESampleLocationDescription, False, "an..35"),
    ]


class CUTestReason(CompositeDataElement):
    """To identify the reason for the test as specified."""

    code: str = "C515"
    title: str = "Test reason"
    schema: CompositeSchemaEntryList = [
        (ETestReasonNameCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ETestReasonName, False, "an..35"),
    ]


class CUMonetaryAmount(CompositeDataElement):
    """Amount of goods or services stated as a monetary amount in a specified currency."""

    code: str = "C516"
    title: str = "Monetary amount"
    schema: CompositeSchemaEntryList = [
        (EMonetaryAmountTypeCodeQualifier, True, "an..3"),
        (EMonetaryAmount, False, "n..35"),
        (ECurrencyIdentificationCode, False, "an..3"),
        (ECurrencyTypeCodeQualifier, False, "an..3"),
        (EStatusDescriptionCode, False, "an..3"),
    ]


class CULocationIdentification(CompositeDataElement):
    """Identification of a location by code or name."""

    code: str = "C517"
    title: str = "Location identification"
    schema: CompositeSchemaEntryList = [
        (ELocationIdentifier, False, "an..35"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ELocationName, False, "an..256"),
    ]


class CURelatedLocationOneIdentification(CompositeDataElement):
    """Identification the first related location by code or name."""

    code: str = "C519"
    title: str = "Related location one identification"
    schema: CompositeSchemaEntryList = [
        (EFirstRelatedLocationIdentifier, False, "an..35"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EFirstRelatedLocationName, False, "an..70"),
    ]


class CUBusinessFunction(CompositeDataElement):
    """To specify a business reason."""

    code: str = "C521"
    title: str = "Business function"
    schema: CompositeSchemaEntryList = [
        (EBusinessFunctionTypeCodeQualifier, True, "an..3"),
        (EBusinessFunctionCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EBusinessDescription, False, "an..70"),
    ]


class CUInstruction(CompositeDataElement):
    """To specify an instruction."""

    code: str = "C522"
    title: str = "Instruction"
    schema: CompositeSchemaEntryList = [
        (EInstructionTypeCodeQualifier, True, "an..3"),
        (EInstructionDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EInstructionDescription, False, "an..35"),
    ]


class CUNumberOfUnitDetails(CompositeDataElement):
    """Identification of number of units and its purpose."""

    code: str = "C523"
    title: str = "Number of unit details"
    schema: CompositeSchemaEntryList = [
        (EUnitsQuantity, False, "n..15"),
        (EUnitTypeCodeQualifier, False, "an..3"),
    ]


class CUHandlingInstructions(CompositeDataElement):
    """Instruction for the handling of goods, products or articles in shipment, storage etc."""

    code: str = "C524"
    title: str = "Handling instructions"
    schema: CompositeSchemaEntryList = [
        (EHandlingInstructionDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EHandlingInstructionDescription, False, "an..512"),
    ]


class CUPurposeOfConveyanceCall(CompositeDataElement):
    """Description of the purpose of the call of the conveyance."""

    code: str = "C525"
    title: str = "Purpose of conveyance call"
    schema: CompositeSchemaEntryList = [
        (EConveyanceCallPurposeDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EConveyanceCallPurposeDescription, False, "an..35"),
    ]


class CUFrequencyDetails(CompositeDataElement):
    """Number of samples collected per specified unit of measure."""

    code: str = "C526"
    title: str = "Frequency details"
    schema: CompositeSchemaEntryList = [
        (EFrequencyCodeQualifier, True, "an..3"),
        (EFrequencyRate, False, "n..9"),
        (EMeasurementUnitCode, False, "an..8"),
    ]


class CUStatisticalDetails(CompositeDataElement):
    """Specifications related to statistical measurements."""

    code: str = "C527"
    title: str = "Statistical details"
    schema: CompositeSchemaEntryList = [
        (EMeasure, False, "an..18"),
        (EMeasurementUnitCode, False, "an..8"),
        (EMeasuredAttributeCode, False, "an..3"),
        (EMeasurementSignificanceCode, False, "an..3"),
    ]


class CUCommodityrateDetail(CompositeDataElement):
    """Identification of commodity/rates."""

    code: str = "C528"
    title: str = "Commodity/rate detail"
    schema: CompositeSchemaEntryList = [
        (ECommodityIdentificationCode, False, "an..18"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUPackagingDetails(CompositeDataElement):
    """Packaging level and details, terms and conditions."""

    code: str = "C531"
    title: str = "Packaging details"
    schema: CompositeSchemaEntryList = [
        (EPackagingLevelCode, False, "an..3"),
        (EPackagingRelatedDescriptionCode, False, "an..3"),
        (EPackagingTermsAndConditionsCode, False, "an..3"),
    ]


class CUReturnablePackageDetails(CompositeDataElement):
    """Indication of responsibility for payment and load contents of returnable packages."""

    code: str = "C532"
    title: str = "Returnable package details"
    schema: CompositeSchemaEntryList = [
        (EReturnablePackageLoadContentsCode, False, "an..3"),
    ]


class CUDutytaxfeeAccountDetail(CompositeDataElement):
    """Indication of account reference for duties, taxes and/or fees."""

    code: str = "C533"
    title: str = "Duty/tax/fee account detail"
    schema: CompositeSchemaEntryList = [
        (EDutyOrTaxOrFeeAccountCode, True, "an..6"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUPaymentInstructionDetails(CompositeDataElement):
    """Indication of method of payment employed or to be employed."""

    code: str = "C534"
    title: str = "Payment instruction details"
    schema: CompositeSchemaEntryList = [
        (EPaymentConditionsCode, False, "an..3"),
        (EPaymentGuaranteeMeansCode, False, "an..3"),
        (EPaymentMeansCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EPaymentChannelCode, False, "an..3"),
    ]


class CUContractAndCarriageCondition(CompositeDataElement):
    """To identify a contract and carriage condition."""

    code: str = "C536"
    title: str = "Contract and carriage condition"
    schema: CompositeSchemaEntryList = [
        (EContractAndCarriageConditionCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUTransportPriority(CompositeDataElement):
    """To indicate the priority of requested transport service."""

    code: str = "C537"
    title: str = "Transport priority"
    schema: CompositeSchemaEntryList = [
        (ETransportServicePriorityCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUAgreementTypeIdentification(CompositeDataElement):
    """Identification of specific agreement type by code or name."""

    code: str = "C543"
    title: str = "Agreement type identification"
    schema: CompositeSchemaEntryList = [
        (EAgreementTypeCodeQualifier, True, "an..3"),
        (EAgreementTypeDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EAgreementTypeDescription, False, "an..70"),
    ]


class CUIndexIdentification(CompositeDataElement):
    """To identify an index."""

    code: str = "C545"
    title: str = "Index identification"
    schema: CompositeSchemaEntryList = [
        (EIndexCodeQualifier, True, "an..3"),
        (EIndexTypeIdentifier, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUIndexValue(CompositeDataElement):
    """To identify the value of an index."""

    code: str = "C546"
    title: str = "Index value"
    schema: CompositeSchemaEntryList = [
        (EIndexText, True, "an..35"),
        (EIndexRepresentationCode, False, "an..3"),
    ]


class CUMonetaryAmountFunction(CompositeDataElement):
    """To identify the function of a monetary amount."""

    code: str = "C549"
    title: str = "Monetary amount function"
    schema: CompositeSchemaEntryList = [
        (EMonetaryAmountFunctionDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EMonetaryAmountFunctionDescription, False, "an..70"),
    ]


class CURequirementconditionIdentification(CompositeDataElement):
    """To identify the specific rule/condition requirement."""

    code: str = "C550"
    title: str = "Requirement/condition identification"
    schema: CompositeSchemaEntryList = [
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ERequirementOrConditionDescription, False, "an..35"),
    ]


class CUBankOperation(CompositeDataElement):
    """Identification of a bank operation by code."""

    code: str = "C551"
    title: str = "Bank operation"
    schema: CompositeSchemaEntryList = [
        (EBankOperationCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUAllowancechargeInformation(CompositeDataElement):
    """Identification of allowance/charge information by number and/or code."""

    code: str = "C552"
    title: str = "Allowance/charge information"
    schema: CompositeSchemaEntryList = [
        (EAllowanceOrChargeIdentifier, False, "an..35"),
        (EAllowanceOrChargeIdentificationCode, False, "an..3"),
    ]


class CURelatedLocationTwoIdentification(CompositeDataElement):
    """Identification of second related location by code or name."""

    code: str = "C553"
    title: str = "Related location two identification"
    schema: CompositeSchemaEntryList = [
        (ESecondRelatedLocationIdentifier, False, "an..35"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ESecondRelatedLocationName, False, "an..70"),
    ]


class CURatetariffClassDetail(CompositeDataElement):
    """Identification of the applicable rate/tariff class."""

    code: str = "C554"
    title: str = "Rate/tariff class detail"
    schema: CompositeSchemaEntryList = [
        (ERateOrTariffClassDescriptionCode, False, "an..9"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUStatus(CompositeDataElement):
    """To specify a status."""

    code: str = "C555"
    title: str = "Status"
    schema: CompositeSchemaEntryList = [
        (EStatusDescriptionCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EStatusDescription, False, "an..35"),
    ]


class CUStatusReason(CompositeDataElement):
    """To specify the reason for a status."""

    code: str = "C556"
    title: str = "Status reason"
    schema: CompositeSchemaEntryList = [
        (EStatusReasonDescriptionCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EStatusReasonDescription, False, "an..256"),
    ]


class CUPhysicalOrLogicalStateInformation(CompositeDataElement):
    """To give information in coded or clear text form on the physical or logical state."""

    code: str = "C564"
    title: str = "Physical or logical state information"
    schema: CompositeSchemaEntryList = [
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EPhysicalOrLogicalStateDescription, False, "an..70"),
    ]


class CUPriorityDetails(CompositeDataElement):
    """To indicate a priority."""

    code: str = "C585"
    title: str = "Priority details"
    schema: CompositeSchemaEntryList = [
        (EPriorityDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EPriorityDescription, False, "an..35"),
    ]


class CUAccountIdentification(CompositeDataElement):
    """Identification of an account."""

    code: str = "C593"
    title: str = "Account identification"
    schema: CompositeSchemaEntryList = [
        (EAccountIdentifier, True, "an..35"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EAccountAbbreviatedName, False, "an..17"),
        (EAccountName, False, "an..35"),
        (EAccountName, False, "an..35"),
        (ECurrencyIdentificationCode, False, "an..3"),
    ]


class CUAccountingJournalIdentification(CompositeDataElement):
    """Identification of an accounting journal."""

    code: str = "C595"
    title: str = "Accounting journal identification"
    schema: CompositeSchemaEntryList = [
        (EAccountingJournalIdentifier, True, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EAccountingJournalName, False, "an..35"),
    ]


class CUAccountingEntryTypeDetails(CompositeDataElement):
    """Identification of the type of entry included in an accounting journal."""

    code: str = "C596"
    title: str = "Accounting entry type details"
    schema: CompositeSchemaEntryList = [
        (EAccountingEntryTypeNameCode, True, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EAccountingEntryTypeName, False, "an..35"),
    ]


class CUStatusCategory(CompositeDataElement):
    """To specify the category of the status."""

    code: str = "C601"
    title: str = "Status category"
    schema: CompositeSchemaEntryList = [
        (EStatusCategoryCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUErrorPointDetails(CompositeDataElement):
    """Indication of the point of error in a message."""

    code: str = "C701"
    title: str = "Error point details"
    schema: CompositeSchemaEntryList = [
        (EMessageSectionCode, False, "an..3"),
        (EMessageItemIdentifier, False, "an..35"),
        (EMessageSubitemIdentifier, False, "n..6"),
    ]


class CUCodeSetIdentification(CompositeDataElement):
    """To identify a code set."""

    code: str = "C702"
    title: str = "Code set identification"
    schema: CompositeSchemaEntryList = [
        (ESimpleDataElementTagIdentifier, False, "an..4"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUNatureOfCargo(CompositeDataElement):
    """Rough classification of a type of cargo."""

    code: str = "C703"
    title: str = "Nature of cargo"
    schema: CompositeSchemaEntryList = [
        (ECargoTypeClassificationCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUMessageIdentifier(CompositeDataElement):
    """Identification of the message."""

    code: str = "C709"
    title: str = "Message identifier"
    schema: CompositeSchemaEntryList = [
        (EMessageTypeCode, True, "an..6"),
        (EVersionIdentifier, False, "an..9"),
        (EReleaseIdentifier, False, "an..9"),
        (EControllingAgencyIdentifier, False, "an..2"),
        (ERevisionIdentifier, False, "an..6"),
        (EDocumentStatusCode, False, "an..3"),
    ]


class CUArrayCellDetails(CompositeDataElement):
    """To contain the data for a contiguous set of cells in an array."""

    code: str = "C770"
    title: str = "Array cell details"
    schema: CompositeSchemaEntryList = [
        (EArrayCellDataDescription, False, "an..512"),
    ]


class CUPositionIdentification(CompositeDataElement):
    """To identify the position of an object in a structure containing the object."""

    code: str = "C778"
    title: str = "Position identification"
    schema: CompositeSchemaEntryList = [
        (EHierarchicalStructureLevelIdentifier, False, "an..35"),
        (ESequencePositionIdentifier, False, "an..10"),
    ]


class CUArrayStructureIdentification(CompositeDataElement):
    """The identification of an array structure."""

    code: str = "C779"
    title: str = "Array structure identification"
    schema: CompositeSchemaEntryList = [
        (EArrayCellStructureIdentifier, True, "an..35"),
        (EObjectIdentificationCodeQualifier, False, "an..3"),
    ]


class CUValueListIdentification(CompositeDataElement):
    """The identification of a coded or non coded value list."""

    code: str = "C780"
    title: str = "Value list identification"
    schema: CompositeSchemaEntryList = [
        (EValueListIdentifier, True, "an..35"),
        (EObjectIdentificationCodeQualifier, False, "an..3"),
    ]


class CUDataSetIdentification(CompositeDataElement):
    """The identification of a data set."""

    code: str = "C782"
    title: str = "Data set identification"
    schema: CompositeSchemaEntryList = [
        (EDataSetIdentifier, True, "an..35"),
        (EObjectIdentificationCodeQualifier, False, "an..3"),
    ]


class CUFootnoteSetIdentification(CompositeDataElement):
    """The identification of a set of footnotes."""

    code: str = "C783"
    title: str = "Footnote set identification"
    schema: CompositeSchemaEntryList = [
        (EFootnoteSetIdentifier, True, "an..35"),
        (EObjectIdentificationCodeQualifier, False, "an..3"),
    ]


class CUFootnoteIdentification(CompositeDataElement):
    """The identification of a footnote."""

    code: str = "C784"
    title: str = "Footnote identification"
    schema: CompositeSchemaEntryList = [
        (EFootnoteIdentifier, True, "an..35"),
        (EObjectIdentificationCodeQualifier, False, "an..3"),
    ]


class CUStatisticalConceptIdentification(CompositeDataElement):
    """The identification of a statistical concept."""

    code: str = "C785"
    title: str = "Statistical concept identification"
    schema: CompositeSchemaEntryList = [
        (EStatisticalConceptIdentifier, True, "an..35"),
        (EObjectIdentificationCodeQualifier, False, "an..3"),
    ]


class CUStructureComponentIdentification(CompositeDataElement):
    """The identification of a structure component."""

    code: str = "C786"
    title: str = "Structure component identification"
    schema: CompositeSchemaEntryList = [
        (EStructureComponentIdentifier, True, "an..35"),
        (EObjectIdentificationCodeQualifier, False, "an..3"),
    ]


class CUQuestionDetails(CompositeDataElement):
    """To specify a question."""

    code: str = "C811"
    title: str = "Question details"
    schema: CompositeSchemaEntryList = [
        (EQuestionDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EQuestionDescription, False, "an..256"),
    ]


class CUResponseDetails(CompositeDataElement):
    """To specify a response to a question, in code or text."""

    code: str = "C812"
    title: str = "Response details"
    schema: CompositeSchemaEntryList = [
        (EResponseDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EResponseDescription, False, "an..256"),
    ]


class CUSafetySection(CompositeDataElement):
    """To identify the safety section to which information relates."""

    code: str = "C814"
    title: str = "Safety section"
    schema: CompositeSchemaEntryList = [
        (ESafetySectionNumber, True, "n..2"),
        (ESafetySectionName, False, "an..70"),
    ]


class CUAdditionalSafetyInformation(CompositeDataElement):
    """To identify additional safety information."""

    code: str = "C815"
    title: str = "Additional safety information"
    schema: CompositeSchemaEntryList = [
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EAdditionalSafetyInformationDescription, False, "an..35"),
    ]


class CUNameComponentDetails(CompositeDataElement):
    """To specify a name component."""

    code: str = "C816"
    title: str = "Name component details"
    schema: CompositeSchemaEntryList = [
        (ENameComponentTypeCodeQualifier, True, "an..3"),
        (ENameComponentDescription, False, "an..256"),
        (ENameComponentUsageCode, False, "an..3"),
        (ENameOriginalAlphabetCode, False, "an..3"),
    ]


class CUAddressUsage(CompositeDataElement):
    """To describe the usage of an address."""

    code: str = "C817"
    title: str = "Address usage"
    schema: CompositeSchemaEntryList = [
        (EAddressPurposeCode, False, "an..3"),
        (EAddressTypeCode, False, "an..3"),
        (EAddressStatusCode, False, "an..3"),
    ]


class CUPersonInheritedCharacteristicDetails(CompositeDataElement):
    """To specify an inherited characteristic of a person."""

    code: str = "C818"
    title: str = "Person inherited characteristic details"
    schema: CompositeSchemaEntryList = [
        (EInheritedCharacteristicDescriptionCode, False, "an..8"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EInheritedCharacteristicDescription, False, "an..70"),
    ]


class CUCountrySubdivisionDetails(CompositeDataElement):
    """To specify a country subdivision, such as state, canton, county, prefecture."""

    code: str = "C819"
    title: str = "Country subdivision details"
    schema: CompositeSchemaEntryList = [
        (ECountrySubdivisionIdentifier, False, "an..9"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ECountrySubdivisionName, False, "an..70"),
    ]


class CUPremiumCalculationComponent(CompositeDataElement):
    """To identify the component affecting premium calculation."""

    code: str = "C820"
    title: str = "Premium calculation component"
    schema: CompositeSchemaEntryList = [
        (EPremiumCalculationComponentIdentifier, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUTypeOfDamage(CompositeDataElement):
    """To specify the type of damage to an object."""

    code: str = "C821"
    title: str = "Type of damage"
    schema: CompositeSchemaEntryList = [
        (EDamageTypeDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EDamageTypeDescription, False, "an..35"),
    ]


class CUDamageArea(CompositeDataElement):
    """To specify where the damage is on an object."""

    code: str = "C822"
    title: str = "Damage area"
    schema: CompositeSchemaEntryList = [
        (EDamageAreaDescriptionCode, False, "an..4"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EDamageAreaDescription, False, "an..35"),
    ]


class CUTypeOfUnitcomponent(CompositeDataElement):
    """To identify the type of unit/component of an object (e.g. lock, door, tyre)."""

    code: str = "C823"
    title: str = "Type of unit/component"
    schema: CompositeSchemaEntryList = [
        (EUnitOrComponentTypeDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EUnitOrComponentTypeDescription, False, "an..35"),
    ]


class CUComponentMaterial(CompositeDataElement):
    """To identify the material of which a component is composed (e.g. steel, plastics)."""

    code: str = "C824"
    title: str = "Component material"
    schema: CompositeSchemaEntryList = [
        (EComponentMaterialDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EComponentMaterialDescription, False, "an..35"),
    ]


class CUDamageSeverity(CompositeDataElement):
    """To specify the severity of damage to an object."""

    code: str = "C825"
    title: str = "Damage severity"
    schema: CompositeSchemaEntryList = [
        (EDamageSeverityDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EDamageSeverityDescription, False, "an..35"),
    ]


class CUAction(CompositeDataElement):
    """To indicate an action which has been taken or is to be taken (e.g. in relation to a certain object)."""

    code: str = "C826"
    title: str = "Action"
    schema: CompositeSchemaEntryList = [
        (EActionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EActionDescription, False, "an..35"),
    ]


class CUTypeOfMarking(CompositeDataElement):
    """Specification of the type of marking that reflects the method that was used and the conventions adhered to for marking (e.g. of packages)."""

    code: str = "C827"
    title: str = "Type of marking"
    schema: CompositeSchemaEntryList = [
        (EMarkingTypeCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUClinicalInterventionDetails(CompositeDataElement):
    """To specify a clinical intervention."""

    code: str = "C828"
    title: str = "Clinical intervention details"
    schema: CompositeSchemaEntryList = [
        (EClinicalInterventionDescriptionCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EClinicalInterventionDescription, False, "an..70"),
    ]


class CUSublineInformation(CompositeDataElement):
    """To provide an indication that a segment or segment group is used to contain sub-line or sub-line item information and to optionally enable the sub-line to be identified."""

    code: str = "C829"
    title: str = "Sub-line information"
    schema: CompositeSchemaEntryList = [
        (ESublineIndicatorCode, False, "an..3"),
        (ELineItemIdentifier, False, "an..6"),
    ]


class CUProcessIdentificationDetails(CompositeDataElement):
    """To identify the details of a specific process."""

    code: str = "C830"
    title: str = "Process identification details"
    schema: CompositeSchemaEntryList = [
        (EProcessDescriptionCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EProcessDescription, False, "an..70"),
    ]


class CUResultDetails(CompositeDataElement):
    """To specify a value."""

    code: str = "C831"
    title: str = "Result details"
    schema: CompositeSchemaEntryList = [
        (EMeasure, False, "an..18"),
        (EMeasurementSignificanceCode, False, "an..3"),
        (ENondiscreteMeasurementNameCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ENondiscreteMeasurementName, False, "an..70"),
    ]


class CUClinicalInformationDetails(CompositeDataElement):
    """To specify an item of clinical information."""

    code: str = "C836"
    title: str = "Clinical information details"
    schema: CompositeSchemaEntryList = [
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EClinicalInformationDescription, False, "an..70"),
    ]


class CUCertaintyDetails(CompositeDataElement):
    """To specify the certainty."""

    code: str = "C837"
    title: str = "Certainty details"
    schema: CompositeSchemaEntryList = [
        (ECertaintyDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ECertaintyDescription, False, "an..35"),
    ]


class CUDosageDetails(CompositeDataElement):
    """To specify a dosage."""

    code: str = "C838"
    title: str = "Dosage details"
    schema: CompositeSchemaEntryList = [
        (EDosageDescriptionIdentifier, False, "an..8"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EDosageDescription, False, "an..70"),
    ]


class CUAttendeeCategory(CompositeDataElement):
    """To specify the category of the attendee."""

    code: str = "C839"
    title: str = "Attendee category"
    schema: CompositeSchemaEntryList = [
        (EAttendeeCategoryDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EAttendeeCategoryDescription, False, "an..35"),
    ]


class CUAttendanceAdmissionDetails(CompositeDataElement):
    """To specify type of admission."""

    code: str = "C840"
    title: str = "Attendance admission details"
    schema: CompositeSchemaEntryList = [
        (EAdmissionTypeDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EAdmissionTypeDescription, False, "an..35"),
    ]


class CUAttendanceDischargeDetails(CompositeDataElement):
    """To specify type of discharge."""

    code: str = "C841"
    title: str = "Attendance discharge details"
    schema: CompositeSchemaEntryList = [
        (EDischargeTypeDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EDischargeTypeDescription, False, "an..35"),
    ]


class CUOrganisationClassificationDetail(CompositeDataElement):
    """To specify details regarding the class of an organisation."""

    code: str = "C844"
    title: str = "Organisation classification detail"
    schema: CompositeSchemaEntryList = [
        (EOrganisationalClassNameCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EOrganisationalClassName, False, "an..70"),
    ]


class CUMeasurementUnitDetails(CompositeDataElement):
    """To specify a measurement unit."""

    code: str = "C848"
    title: str = "Measurement unit details"
    schema: CompositeSchemaEntryList = [
        (EMeasurementUnitCode, False, "an..8"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EMeasurementUnitName, False, "an..35"),
    ]


class CUPartiesToInstruction(CompositeDataElement):
    """Identify the sending and receiving parties of the instruction."""

    code: str = "C849"
    title: str = "Parties to instruction"
    schema: CompositeSchemaEntryList = [
        (EEnactingPartyIdentifier, True, "an..35"),
        (EInstructionReceivingPartyIdentifier, False, "an..35"),
    ]


class CUStatusOfInstruction(CompositeDataElement):
    """Provides information regarding the status of an instruction."""

    code: str = "C850"
    title: str = "Status of instruction"
    schema: CompositeSchemaEntryList = [
        (EStatusDescriptionCode, True, "an..3"),
        (EPartyName, False, "an..70"),
    ]


class CURiskObjectType(CompositeDataElement):
    """Specification of a type of risk object."""

    code: str = "C851"
    title: str = "Risk object type"
    schema: CompositeSchemaEntryList = [
        (ERiskObjectTypeIdentifier, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CURiskObjectSubtype(CompositeDataElement):
    """To provide identification details for a risk object sub-type."""

    code: str = "C852"
    title: str = "Risk object sub-type"
    schema: CompositeSchemaEntryList = [
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ERiskObjectSubtypeDescription, False, "an..70"),
    ]


class CUErrorSegmentPointDetails(CompositeDataElement):
    """To indicate the exact segment location of an application error within a message."""

    code: str = "C853"
    title: str = "Error segment point details"
    schema: CompositeSchemaEntryList = [
        (ESegmentTagIdentifier, False, "an..3"),
        (ESequencePositionIdentifier, False, "an..10"),
        (ESequenceIdentifierSourceCode, False, "an..3"),
    ]


class CUChargeallowanceAccount(CompositeDataElement):
    """Identification of the account for charge or allowance."""

    code: str = "C878"
    title: str = "Charge/allowance account"
    schema: CompositeSchemaEntryList = [
        (EInstitutionBranchIdentifier, True, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EAccountHolderIdentifier, False, "an..35"),
        (ECurrencyIdentificationCode, False, "an..3"),
    ]


class CUCharacteristicValue(CompositeDataElement):
    """To provide the value of a characteristic."""

    code: str = "C889"
    title: str = "Characteristic value"
    schema: CompositeSchemaEntryList = [
        (ECharacteristicValueDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ECharacteristicValueDescription, False, "an..35"),
        (ECharacteristicValueDescription, False, "an..35"),
    ]


class CUApplicationErrorDetail(CompositeDataElement):
    """Code assigned by the recipient of a message to indicate a data validation error condition."""

    code: str = "C901"
    title: str = "Application error detail"
    schema: CompositeSchemaEntryList = [
        (EApplicationErrorCode, True, "an..8"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CURelationship(CompositeDataElement):
    """Identification and/or description of a relationship."""

    code: str = "C941"
    title: str = "Relationship"
    schema: CompositeSchemaEntryList = [
        (ERelationshipDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (ERelationshipDescription, False, "an..35"),
    ]


class CUMembershipCategory(CompositeDataElement):
    """Identification and/or description of a membership category for a member of a scheme or group."""

    code: str = "C942"
    title: str = "Membership category"
    schema: CompositeSchemaEntryList = [
        (EMembershipCategoryDescriptionCode, True, "an..4"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EMembershipCategoryDescription, False, "an..35"),
    ]


class CUMembershipStatus(CompositeDataElement):
    """Code and/or description of membership status."""

    code: str = "C944"
    title: str = "Membership status"
    schema: CompositeSchemaEntryList = [
        (EMembershipStatusDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EMembershipStatusDescription, False, "an..35"),
    ]


class CUMembershipLevel(CompositeDataElement):
    """Identification of a membership level."""

    code: str = "C945"
    title: str = "Membership level"
    schema: CompositeSchemaEntryList = [
        (EMembershipLevelCodeQualifier, True, "an..3"),
        (EMembershipLevelDescriptionCode, False, "an..9"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EMembershipLevelDescription, False, "an..35"),
    ]


class CUEmploymentCategory(CompositeDataElement):
    """Code and/or description of an employment category."""

    code: str = "C948"
    title: str = "Employment category"
    schema: CompositeSchemaEntryList = [
        (EEmploymentCategoryDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EEmploymentCategoryDescription, False, "an..35"),
    ]


class CUQualificationClassification(CompositeDataElement):
    """Qualification classification description and/or code. This specifies the trade, skill, professional or similar qualification category."""

    code: str = "C950"
    title: str = "Qualification classification"
    schema: CompositeSchemaEntryList = [
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EQualificationClassificationDescription, False, "an..35"),
        (EQualificationClassificationDescription, False, "an..35"),
    ]


class CUOccupation(CompositeDataElement):
    """Description of an occupation."""

    code: str = "C951"
    title: str = "Occupation"
    schema: CompositeSchemaEntryList = [
        (EOccupationDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EOccupationDescription, False, "an..35"),
        (EOccupationDescription, False, "an..35"),
    ]


class CUContributionType(CompositeDataElement):
    """Identification of the type of a contribution to a scheme or group."""

    code: str = "C953"
    title: str = "Contribution type"
    schema: CompositeSchemaEntryList = [
        (EContributionTypeDescriptionCode, True, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EContributionTypeDescription, False, "an..35"),
    ]


class CUAttributeType(CompositeDataElement):
    """Identification of the type of attribute."""

    code: str = "C955"
    title: str = "Attribute type"
    schema: CompositeSchemaEntryList = [
        (EAttributeTypeDescriptionCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EAttributeTypeDescription, False, "an..70"),
    ]


class CUAttributeDetail(CompositeDataElement):
    """Identification of the attribute related to an entity."""

    code: str = "C956"
    title: str = "Attribute detail"
    schema: CompositeSchemaEntryList = [
        (EAttributeDescriptionCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EAttributeDescription, False, "an..256"),
    ]


class CUReasonForChange(CompositeDataElement):
    """Code and/or description of the reason for a change."""

    code: str = "C960"
    title: str = "Reason for change"
    schema: CompositeSchemaEntryList = [
        (EChangeReasonDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EChangeReasonDescription, False, "an..35"),
    ]


class CUFormulaComplexity(CompositeDataElement):
    """Identification of the complexity of a formula."""

    code: str = "C961"
    title: str = "Formula complexity"
    schema: CompositeSchemaEntryList = [
        (EFormulaComplexityCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
    ]


class CUClauseName(CompositeDataElement):
    """Identification of a clause in coded or clear form."""

    code: str = "C970"
    title: str = "Clause name"
    schema: CompositeSchemaEntryList = [
        (EClauseNameCode, False, "an..17"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EClauseName, False, "an..70"),
    ]


class CUProvisoType(CompositeDataElement):
    """Specification of the proviso type in coded or clear form."""

    code: str = "C971"
    title: str = "Proviso type"
    schema: CompositeSchemaEntryList = [
        (EProvisoTypeDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EProvisoTypeDescription, False, "an..35"),
    ]


class CUProvisoCalculation(CompositeDataElement):
    """Specification of the proviso calculation in coded or clear form."""

    code: str = "C972"
    title: str = "Proviso calculation"
    schema: CompositeSchemaEntryList = [
        (EProvisoCalculationDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EProvisoCalculationDescription, False, "an..35"),
    ]


class CUApplicabilityType(CompositeDataElement):
    """Specification of the applicability type in coded or clear form."""

    code: str = "C973"
    title: str = "Applicability type"
    schema: CompositeSchemaEntryList = [
        (EApplicabilityTypeDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EApplicabilityTypeDescription, False, "an..35"),
    ]


class CUBasisType(CompositeDataElement):
    """Specification of the basis in coded or clear form."""

    code: str = "C974"
    title: str = "Basis type"
    schema: CompositeSchemaEntryList = [
        (EBasisTypeDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EBasisTypeDescription, False, "an..35"),
    ]


class CUPeriodDetail(CompositeDataElement):
    """Specification of the period detail in coded or clear form."""

    code: str = "C977"
    title: str = "Period detail"
    schema: CompositeSchemaEntryList = [
        (EPeriodDetailDescriptionCode, False, "an..3"),
        (ECodeListIdentificationCode, False, "an..17"),
        (ECodeListResponsibleAgencyCode, False, "an..3"),
        (EPeriodDetailDescription, False, "an..35"),
    ]


__all__ = [
    "CSSyntaxIdentifier",
    "CSInterchangeSender",
    "CSInterchangeRecipient",
    "CSDateAndTimeOfPreparation",
    "CSRecipientReferencepasswordDetails",
    "CSApplicationSenderIdentification",
    "CSApplicationRecipientIdentification",
    "CSMessageVersion",
    "CSMessageIdentifier",
    "CSStatusOfTheTransfer",
    "CSDataElementIdentification",
    "CSMessageSubsetIdentification",
    "CSMessageImplementationGuidelineIdentification",
    "CSScenarioIdentification",
    "CSReferenceIdentification",
    "CSObjectTypeIdentification",
    "CSStatusOfTheObject",
    "CSDateAndorTimeOfInitiation",
    "CSStatusOfTransferInteractive",
    "CSDialogueReference",
    "CSTransactionReference",
    "CSDialogueIdentification",
    "CSInteractiveMessageIdentifier",
    "CSStatusInformation",
    "CSSecurityIdentificationDetails",
    "CSSecurityDateAndTime",
    "CSSecurityAlgorithm",
    "CSAlgorithmParameter",
    "CSListParameter",
    "CSServiceCharacterForSignature",
    "CSValidationResult",
    "CUTransportMeans",
    "CUDocumentmessageName",
    "CUPowerType",
    "CUEventCategory",
    "CUMonetaryAmountFunctionDetail",
    "CUInformationCategory",
    "CUInformationType",
    "CUInformationDetail",
    "CUProcessingIndicator",
    "CUPaymentTerms",
    "CUEventType",
    "CUCarrier",
    "CUNationalityDetails",
    "CUBillLevelIdentification",
    "CURemunerationTypeIdentification",
    "CUContactDetails",
    "CUNameAndAddress",
    "CUStreet",
    "CUEventIdentification",
    "CUCommunicationContact",
    "CUFileIdentification",
    "CUAccountHolderIdentification",
    "CUComputerEnvironmentIdentification",
    "CUPartyName",
    "CUPartyIdentificationDetails",
    "CUMaritalStatusDetails",
    "CUInstitutionIdentification",
    "CUAddressDetails",
    "CUFileDetails",
    "CUTermsOfDeliveryOrTransport",
    "CUReligionDetails",
    "CUDocumentmessageIdentification",
    "CUTextReference",
    "CUTextLiteral",
    "CURateDetails",
    "CUPriceMultiplierInformation",
    "CUValuerange",
    "CUQuantityDetails",
    "CUCharge",
    "CUPackageType",
    "CURatetariffClass",
    "CUHazardCode",
    "CUIdentificationNumber",
    "CUIdentityNumberRange",
    "CUMarksLabels",
    "CUDimensions",
    "CUItemNumberIdentification",
    "CUNumberAndTypeOfPackages",
    "CUSpecialServicesIdentification",
    "CUSealIssuer",
    "CUHazardousMaterial",
    "CUMovementType",
    "CUModeOfTransport",
    "CUTransportIdentification",
    "CUDangerousGoodsShipmentFlashpoint",
    "CUEquipmentSizeAndType",
    "CUChargeCategory",
    "CUMethodOfPayment",
    "CUGovernmentAction",
    "CUService",
    "CUUndgInformation",
    "CUHazardIdentificationPlacardDetails",
    "CUDangerousGoodsLabel",
    "CUEquipmentIdentification",
    "CUTemperatureSetting",
    "CUCharacteristicDescription",
    "CUDutytaxfeeType",
    "CUProcessTypeAndDescription",
    "CUDutytaxfeeDetail",
    "CUTestMethod",
    "CUCustomsIdentityCodes",
    "CUControl",
    "CUItemCharacteristic",
    "CUItemDescription",
    "CUQuantityDifferenceInformation",
    "CURange",
    "CUSequenceInformation",
    "CUProductGroup",
    "CUTunnelRestriction",
    "CUTransportService",
    "CUPatternDescription",
    "CUInsuranceCoverType",
    "CUInsuranceCoverDetails",
    "CUSalesChannelIdentification",
    "CUInformationRequest",
    "CUExcessTransportationInformation",
    "CUPackageTypeIdentification",
    "CUPercentageDetails",
    "CUMeasurementDetails",
    "CUDocumentmessageDetails",
    "CUCurrencyDetails",
    "CUReference",
    "CUDatetimeperiod",
    "CULanguageDetails",
    "CUPriceInformation",
    "CUSizeDetails",
    "CUSampleLocationDetails",
    "CUTestReason",
    "CUMonetaryAmount",
    "CULocationIdentification",
    "CURelatedLocationOneIdentification",
    "CUBusinessFunction",
    "CUInstruction",
    "CUNumberOfUnitDetails",
    "CUHandlingInstructions",
    "CUPurposeOfConveyanceCall",
    "CUFrequencyDetails",
    "CUStatisticalDetails",
    "CUCommodityrateDetail",
    "CUPackagingDetails",
    "CUReturnablePackageDetails",
    "CUDutytaxfeeAccountDetail",
    "CUPaymentInstructionDetails",
    "CUContractAndCarriageCondition",
    "CUTransportPriority",
    "CUAgreementTypeIdentification",
    "CUIndexIdentification",
    "CUIndexValue",
    "CUMonetaryAmountFunction",
    "CURequirementconditionIdentification",
    "CUBankOperation",
    "CUAllowancechargeInformation",
    "CURelatedLocationTwoIdentification",
    "CURatetariffClassDetail",
    "CUStatus",
    "CUStatusReason",
    "CUPhysicalOrLogicalStateInformation",
    "CUPriorityDetails",
    "CUAccountIdentification",
    "CUAccountingJournalIdentification",
    "CUAccountingEntryTypeDetails",
    "CUStatusCategory",
    "CUErrorPointDetails",
    "CUCodeSetIdentification",
    "CUNatureOfCargo",
    "CUMessageIdentifier",
    "CUArrayCellDetails",
    "CUPositionIdentification",
    "CUArrayStructureIdentification",
    "CUValueListIdentification",
    "CUDataSetIdentification",
    "CUFootnoteSetIdentification",
    "CUFootnoteIdentification",
    "CUStatisticalConceptIdentification",
    "CUStructureComponentIdentification",
    "CUQuestionDetails",
    "CUResponseDetails",
    "CUSafetySection",
    "CUAdditionalSafetyInformation",
    "CUNameComponentDetails",
    "CUAddressUsage",
    "CUPersonInheritedCharacteristicDetails",
    "CUCountrySubdivisionDetails",
    "CUPremiumCalculationComponent",
    "CUTypeOfDamage",
    "CUDamageArea",
    "CUTypeOfUnitcomponent",
    "CUComponentMaterial",
    "CUDamageSeverity",
    "CUAction",
    "CUTypeOfMarking",
    "CUClinicalInterventionDetails",
    "CUSublineInformation",
    "CUProcessIdentificationDetails",
    "CUResultDetails",
    "CUClinicalInformationDetails",
    "CUCertaintyDetails",
    "CUDosageDetails",
    "CUAttendeeCategory",
    "CUAttendanceAdmissionDetails",
    "CUAttendanceDischargeDetails",
    "CUOrganisationClassificationDetail",
    "CUMeasurementUnitDetails",
    "CUPartiesToInstruction",
    "CUStatusOfInstruction",
    "CURiskObjectType",
    "CURiskObjectSubtype",
    "CUErrorSegmentPointDetails",
    "CUChargeallowanceAccount",
    "CUCharacteristicValue",
    "CUApplicationErrorDetail",
    "CURelationship",
    "CUMembershipCategory",
    "CUMembershipStatus",
    "CUMembershipLevel",
    "CUEmploymentCategory",
    "CUQualificationClassification",
    "CUOccupation",
    "CUContributionType",
    "CUAttributeType",
    "CUAttributeDetail",
    "CUReasonForChange",
    "CUFormulaComplexity",
    "CUClauseName",
    "CUProvisoType",
    "CUProvisoCalculation",
    "CUApplicabilityType",
    "CUBasisType",
    "CUPeriodDetail",
]
