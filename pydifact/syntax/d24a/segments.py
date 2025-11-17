# ------------------- Segments -------------------
# created from EDSD - the EDIFACT segments directory
# This file is auto-generated. Don't edit it manually.

# Copyright (c) 2017-2025 Christian González
# This file is licensed under the MIT license, see LICENSE file.

from pydifact import Segment
from pydifact.syntax.common.types import SegmentSchema
from .data import *
from .composite import *


class DataElementErrorIndicationSegment(Segment):
    """To identify an erroneous stand-alone, composite or component data element, and to identify the nature of the error."""
    tag: str = "UCD"
    schema: SegmentSchema = {
        "syntax_error_coded": (SyntaxErrorCoded, False, "an..3"),
        "data_element_identification": (CSDataElementIdentification, False, 1),
    }


class GroupResponseSegment(Segment):
    """To identify a group in the subject interchange and to indicate acknowledgement or rejection (action taken) of the UNG and UNE segments, and to identify any error related to these segments. It can also identify errors related to the USA, USC, USD, USH, USR, UST, or USU security segments when they appear at the group level. Depending on the action code, it may also indicate the action taken on the messages and packages within that group."""
    tag: str = "UCF"
    schema: SegmentSchema = {
        "group_reference_number": (GroupReferenceNumber, False, "an..14"),
        "application_sender_identification": (CSApplicationSenderIdentification, False, 1),
        "application_recipient_identification": (CSApplicationRecipientIdentification, False, 1),
        "action_coded": (ActionCoded, False, "an..3"),
        "syntax_error_coded": (SyntaxErrorCoded, False, "an..3"),
        "service_segment_tag_coded": (ServiceSegmentTagCoded, False, "an..3"),
        "data_element_identification": (CSDataElementIdentification, False, 1),
        "security_reference_number": (SecurityReferenceNumber, False, "an..14"),
        "security_segment_position": (SecuritySegmentPosition, False, "n..6"),
    }


class InterchangeResponseSegment(Segment):
    """To identify the subject interchange, to indicate interchange receipt, to indicate acknowledgement or rejection (action taken) of the UNA, UNB and UNZ segments, and to identify any error related to these segments. It can also identify errors related to the USA, USC, USD, USH, USR, UST, or USU security segments when they appear at the interchange level. Depending on the action code, it may also indicate the action taken on the groups, messages, and packages within that interchange."""
    tag: str = "UCI"
    schema: SegmentSchema = {
        "interchange_control_reference": (InterchangeControlReference, False, "an..14"),
        "interchange_sender": (CSInterchangeSender, False, 1),
        "interchange_recipient": (CSInterchangeRecipient, False, 1),
        "action_coded": (ActionCoded, False, "an..3"),
        "syntax_error_coded": (SyntaxErrorCoded, False, "an..3"),
        "service_segment_tag_coded": (ServiceSegmentTagCoded, False, "an..3"),
        "data_element_identification": (CSDataElementIdentification, False, 1),
        "security_reference_number": (SecurityReferenceNumber, False, "an..14"),
        "security_segment_position": (SecuritySegmentPosition, False, "n..6"),
    }


class MessagepackageResponseSegment(Segment):
    """To identify a message or package in the subject interchange, and to indicate that message's or package's acknowledgement or rejection (action taken), and to identify any error related to the UNH, UNT, UNO, and UNP segments. It can also identify errors related to the USA, USC, USD, USH, USR, UST, or USU security segments when they appear at the message or package level."""
    tag: str = "UCM"
    schema: SegmentSchema = {
        "message_reference_number": (MessageReferenceNumber, False, "an..14"),
        "message_identifier": (CSMessageIdentifier, False, 1),
        "action_coded": (ActionCoded, False, "an..3"),
        "syntax_error_coded": (SyntaxErrorCoded, False, "an..3"),
        "service_segment_tag_coded": (ServiceSegmentTagCoded, False, "an..3"),
        "data_element_identification": (CSDataElementIdentification, False, 1),
        "package_reference_number": (PackageReferenceNumber, False, "an..35"),
        "reference_identification": (CSReferenceIdentification, False, 99),
        "security_reference_number": (SecurityReferenceNumber, False, "an..14"),
        "security_segment_position": (SecuritySegmentPosition, False, "n..6"),
    }


class SegmentErrorIndicationSegment(Segment):
    """To identify either a segment containing an error or a missing segment, and to identify any error related to the complete segment."""
    tag: str = "UCS"
    schema: SegmentSchema = {
        "segment_position_in_message_body": (SegmentPositionInMessageBody, False, "n..6"),
        "syntax_error_coded": (SyntaxErrorCoded, False, "an..3"),
    }


class AnticollisionSegmentGroupHeaderSegment(Segment):
    """To head, identify and specify an anti-collision segment group. """
    tag: str = "UGH"
    schema: SegmentSchema = {
    }


class AnticollisionSegmentGroupTrailerSegment(Segment):
    """To end and check the completeness of an anti-collision segment group."""
    tag: str = "UGT"
    schema: SegmentSchema = {
    }


class InteractiveInterchangeHeaderSegment(Segment):
    """To head and identify an interchange. """
    tag: str = "UIB"
    schema: SegmentSchema = {
        "syntax_identifier": (CSSyntaxIdentifier, False, 1),
        "dialogue_reference": (CSDialogueReference, False, 1),
        "transaction_reference": (CSTransactionReference, False, 1),
        "scenario_identification": (CSScenarioIdentification, False, 1),
        "dialogue_identification": (CSDialogueIdentification, False, 1),
        "interchange_sender": (CSInterchangeSender, False, 1),
        "interchange_recipient": (CSInterchangeRecipient, False, 1),
        "date_andor_time_of_initiation": (CSDateAndorTimeOfInitiation, False, 1),
        "duplicate_indicator": (DuplicateIndicator, False, "a1"),
        "test_indicator": (TestIndicator, False, "n1"),
    }


class InteractiveMessageHeaderSegment(Segment):
    """To head, identify and specify a message. """
    tag: str = "UIH"
    schema: SegmentSchema = {
        "interactive_message_identifier": (CSInteractiveMessageIdentifier, False, 1),
        "interactive_message_reference_number": (InteractiveMessageReferenceNumber, False, "an..35"),
        "dialogue_reference": (CSDialogueReference, False, 1),
        "status_of_transfer__interactive": (CSStatusOfTransferInteractive, False, 1),
        "date_andor_time_of_initiation": (CSDateAndorTimeOfInitiation, False, 1),
        "test_indicator": (TestIndicator, False, "n1"),
    }


class InteractiveStatusSegment(Segment):
    """To report the status of the dialogue. Note: To avoid endless loops, the UIR segment is not used to respond to a UIR received with syntax errors."""
    tag: str = "UIR"
    schema: SegmentSchema = {
        "report_function_coded": (ReportFunctionCoded, False, "an..3"),
        "status_information": (CSStatusInformation, False, 9),
        "dialogue_reference": (CSDialogueReference, False, 1),
        "date_andor_time_of_initiation": (CSDateAndorTimeOfInitiation, False, 1),
        "interactive_message_reference_number": (InteractiveMessageReferenceNumber, False, "an..35"),
        "package_reference_number": (PackageReferenceNumber, False, "an..35"),
        "syntax_error_coded": (SyntaxErrorCoded, False, "an..3"),
        "segment_position_in_message_body": (SegmentPositionInMessageBody, False, "n..6"),
        "data_element_identification": (CSDataElementIdentification, False, 1),
    }


class InteractiveMessageTrailerSegment(Segment):
    """To end and check the completeness of a message. """
    tag: str = "UIT"
    schema: SegmentSchema = {
        "interactive_message_reference_number": (InteractiveMessageReferenceNumber, False, "an..35"),
        "number_of_segments_in_a_message": (NumberOfSegmentsInAMessage, False, "n..10"),
    }


class InteractiveInterchangeTrailerSegment(Segment):
    """To end and check the completeness of an interchange. """
    tag: str = "UIZ"
    schema: SegmentSchema = {
        "dialogue_reference": (CSDialogueReference, False, 1),
        "interchange_control_count": (InterchangeControlCount, False, "n..6"),
        "duplicate_indicator": (DuplicateIndicator, False, "a1"),
    }


class InterchangeHeaderSegment(Segment):
    """To identify an interchange. """
    tag: str = "UNB"
    schema: SegmentSchema = {
        "syntax_identifier": (CSSyntaxIdentifier, False, 1),
        "interchange_sender": (CSInterchangeSender, False, 1),
        "interchange_recipient": (CSInterchangeRecipient, False, 1),
        "date_and_time_of_preparation": (CSDateAndTimeOfPreparation, False, 1),
        "interchange_control_reference": (InterchangeControlReference, False, "an..14"),
        "recipient_referencepassword_details": (CSRecipientReferencepasswordDetails, False, 1),
        "application_reference": (ApplicationReference, False, "an..14"),
        "processing_priority_code": (ProcessingPriorityCode, False, "a1"),
        "acknowledgement_request": (AcknowledgementRequest, False, "n1"),
        "interchange_agreement_identifier": (InterchangeAgreementIdentifier, False, "an..35"),
        "test_indicator": (TestIndicator, False, "n1"),
    }


class GroupTrailerSegment(Segment):
    """To end and check the completeness of a group. """
    tag: str = "UNE"
    schema: SegmentSchema = {
        "group_control_count": (GroupControlCount, False, "n..6"),
        "group_reference_number": (GroupReferenceNumber, False, "an..14"),
    }


class GroupHeaderSegment(Segment):
    """To head, identify and specify a group of messages and/or packages, which may be used for internal routing and which may contain one or more message types and/or packages."""
    tag: str = "UNG"
    schema: SegmentSchema = {
        "message_group_identification": (MessageGroupIdentification, False, "an..6"),
        "application_sender_identification": (CSApplicationSenderIdentification, False, 1),
        "application_recipient_identification": (CSApplicationRecipientIdentification, False, 1),
        "date_and_time_of_preparation": (CSDateAndTimeOfPreparation, False, 1),
        "group_reference_number": (GroupReferenceNumber, False, "an..14"),
        "controlling_agency_coded": (ControllingAgencyCoded, False, "an..3"),
        "message_version": (CSMessageVersion, False, 1),
        "application_password": (ApplicationPassword, False, "an..14"),
    }


class MessageHeaderSegment(Segment):
    """To head, identify and specify a message. """
    tag: str = "UNH"
    schema: SegmentSchema = {
        "message_reference_number": (MessageReferenceNumber, False, "an..14"),
        "message_identifier": (CSMessageIdentifier, False, 1),
        "common_access_reference": (CommonAccessReference, False, "an..35"),
        "status_of_the_transfer": (CSStatusOfTheTransfer, False, 1),
        "message_subset_identification": (CSMessageSubsetIdentification, False, 1),
        "scenario_identification": (CSScenarioIdentification, False, 1),
    }


class ObjectHeaderSegment(Segment):
    """To head, identify and specify an object. """
    tag: str = "UNO"
    schema: SegmentSchema = {
        "package_reference_number": (PackageReferenceNumber, False, "an..35"),
        "reference_identification": (CSReferenceIdentification, False, 99),
        "object_type_identification": (CSObjectTypeIdentification, False, 99),
        "status_of_the_object": (CSStatusOfTheObject, False, 1),
        "dialogue_reference": (CSDialogueReference, False, 1),
        "status_of_transfer__interactive": (CSStatusOfTransferInteractive, False, 1),
        "date_andor_time_of_initiation": (CSDateAndorTimeOfInitiation, False, 1),
        "test_indicator": (TestIndicator, False, "n1"),
    }


class ObjectTrailerSegment(Segment):
    """To end and check the completeness of an object. """
    tag: str = "UNP"
    schema: SegmentSchema = {
        "length_of_object_in_octets_of_bits": (LengthOfObjectInOctetsOfBits, False, "n..18"),
        "package_reference_number": (PackageReferenceNumber, False, "an..35"),
    }


class SectionControlSegment(Segment):
    """To separate header, detail and summary sections of a message. Note: To be used by message designers only when required to avoid ambiguities."""
    tag: str = "UNS"
    schema: SegmentSchema = {
        "section_identification": (SectionIdentification, False, "a1"),
    }


class MessageTrailerSegment(Segment):
    """To end and check the completeness of a message. """
    tag: str = "UNT"
    schema: SegmentSchema = {
        "number_of_segments_in_a_message": (NumberOfSegmentsInAMessage, False, "n..10"),
        "message_reference_number": (MessageReferenceNumber, False, "an..14"),
    }


class InterchangeTrailerSegment(Segment):
    """To end and check the completeness of an interchange. """
    tag: str = "UNZ"
    schema: SegmentSchema = {
        "interchange_control_count": (InterchangeControlCount, False, "n..6"),
        "interchange_control_reference": (InterchangeControlReference, False, "an..14"),
    }


class SecurityAlgorithmSegment(Segment):
    """To identify a security algorithm, the technical usage made of it, and to contain the technical parameters required."""
    tag: str = "USA"
    schema: SegmentSchema = {
        "security_algorithm": (CSSecurityAlgorithm, False, 1),
        "algorithm_parameter": (CSAlgorithmParameter, False, 9),
    }


class SecuredDataIdentificationSegment(Segment):
    """To contain details related to the AUTACK. """
    tag: str = "USB"
    schema: SegmentSchema = {
        "response_type_coded": (ResponseTypeCoded, False, "an..3"),
        "security_date_and_time": (CSSecurityDateAndTime, False, 1),
        "interchange_sender": (CSInterchangeSender, False, 1),
        "interchange_recipient": (CSInterchangeRecipient, False, 1),
    }


class CertificateSegment(Segment):
    """To convey the public key and the credentials of its owner. """
    tag: str = "USC"
    schema: SegmentSchema = {
        "certificate_reference": (CertificateReference, False, "an..70"),
        "security_identification_details": (CSSecurityIdentificationDetails, False, 2),
        "certificate_syntax_and_version_coded": (CertificateSyntaxAndVersionCoded, False, "an..3"),
        "filter_function_coded": (FilterFunctionCoded, False, "an..3"),
        "original_character_set_encoding_coded": (OriginalCharacterSetEncodingCoded, False, "an..3"),
        "user_authorisation_level": (UserAuthorisationLevel, False, "an..35"),
        "service_character_for_signature": (CSServiceCharacterForSignature, False, 5),
        "security_date_and_time": (CSSecurityDateAndTime, False, 4),
        "security_status_coded": (SecurityStatusCoded, False, "an..3"),
        "revocation_reason_coded": (RevocationReasonCoded, False, "an..3"),
    }


class DataEncryptionHeaderSegment(Segment):
    """To specify size (i.e. length of data in octets of bits) of encrypted data following the segment terminator of this segment."""
    tag: str = "USD"
    schema: SegmentSchema = {
        "length_of_data_in_octets_of_bits": (LengthOfDataInOctetsOfBits, False, "n..18"),
        "encryption_reference_number": (EncryptionReferenceNumber, False, "an..35"),
        "number_of_padding_bytes": (NumberOfPaddingBytes, False, "n..2"),
    }


class SecurityMessageRelationSegment(Segment):
    """To specify the relation to earlier security messages, such as response to a particular request, or request for a particular answer."""
    tag: str = "USE"
    schema: SegmentSchema = {
        "message_relation_coded": (MessageRelationCoded, False, "an..3"),
    }


class KeyManagementFunctionSegment(Segment):
    """To specify the type of key management function and the status of a corresponding key or certificate."""
    tag: str = "USF"
    schema: SegmentSchema = {
        "key_management_function_qualifier": (KeyManagementFunctionQualifier, False, "an..3"),
        "list_parameter": (CSListParameter, False, 1),
        "security_status_coded": (SecurityStatusCoded, False, "an..3"),
        "certificate_sequence_number": (CertificateSequenceNumber, False, "n..4"),
        "filter_function_coded": (FilterFunctionCoded, False, "an..3"),
    }


class SecurityHeaderSegment(Segment):
    """To specify a security mechanism applied to a EDIFACT structure (i.e.: either message/package, group or interchange)."""
    tag: str = "USH"
    schema: SegmentSchema = {
        "security_service_coded": (SecurityServiceCoded, False, "an..3"),
        "security_reference_number": (SecurityReferenceNumber, False, "an..14"),
        "scope_of_security_application_coded": (ScopeOfSecurityApplicationCoded, False, "an..3"),
        "response_type_coded": (ResponseTypeCoded, False, "an..3"),
        "filter_function_coded": (FilterFunctionCoded, False, "an..3"),
        "original_character_set_encoding_coded": (OriginalCharacterSetEncodingCoded, False, "an..3"),
        "role_of_security_provider_coded": (RoleOfSecurityProviderCoded, False, "an..3"),
        "security_identification_details": (CSSecurityIdentificationDetails, False, 2),
        "security_sequence_number": (SecuritySequenceNumber, False, "an..35"),
        "security_date_and_time": (CSSecurityDateAndTime, False, 1),
    }


class SecurityListStatusSegment(Segment):
    """To specify the status of security objects, such as keys or certificates to be delivered in a list, and the corresponding list parameters."""
    tag: str = "USL"
    schema: SegmentSchema = {
        "security_status_coded": (SecurityStatusCoded, False, "an..3"),
        "list_parameter": (CSListParameter, False, 9),
    }


class SecurityResultSegment(Segment):
    """To contain the result of the security mechanisms. """
    tag: str = "USR"
    schema: SegmentSchema = {
        "validation_result": (CSValidationResult, False, 2),
    }


class SecurityTrailerSegment(Segment):
    """To establish a link between security header and security trailer segment groups."""
    tag: str = "UST"
    schema: SegmentSchema = {
        "security_reference_number": (SecurityReferenceNumber, False, "an..14"),
        "number_of_security_segments": (NumberOfSecuritySegments, False, "n..10"),
    }


class DataEncryptionTrailerSegment(Segment):
    """To provide a trailer for the encrypted data. """
    tag: str = "USU"
    schema: SegmentSchema = {
        "length_of_data_in_octets_of_bits": (LengthOfDataInOctetsOfBits, False, "n..18"),
        "encryption_reference_number": (EncryptionReferenceNumber, False, "an..35"),
    }


class SecurityReferencesSegment(Segment):
    """To refer to the secured EDIFACT structure and its associated date and time."""
    tag: str = "USX"
    schema: SegmentSchema = {
        "interchange_control_reference": (InterchangeControlReference, False, "an..14"),
        "interchange_sender": (CSInterchangeSender, False, 1),
        "interchange_recipient": (CSInterchangeRecipient, False, 1),
        "group_reference_number": (GroupReferenceNumber, False, "an..14"),
        "application_sender_identification": (CSApplicationSenderIdentification, False, 1),
        "application_recipient_identification": (CSApplicationRecipientIdentification, False, 1),
        "message_reference_number": (MessageReferenceNumber, False, "an..14"),
        "message_identifier": (CSMessageIdentifier, False, 1),
        "package_reference_number": (PackageReferenceNumber, False, "an..35"),
        "security_date_and_time": (CSSecurityDateAndTime, False, 1),
    }


class SecurityOnReferencesSegment(Segment):
    """To identify the applicable header, and to contain the security result and/or to indicate the possible cause of security rejection for the referred value."""
    tag: str = "USY"
    schema: SegmentSchema = {
        "security_reference_number": (SecurityReferenceNumber, False, "an..14"),
        "validation_result": (CSValidationResult, False, 2),
        "security_error_coded": (SecurityErrorCoded, False, "an..3"),
    }


class AddressSegment(Segment):
    """To specify an address. """
    tag: str = "ADR"
    schema: SegmentSchema = {
        "address_usage": (CUAddressUsage, False, 1),
        "address_details": (CUAddressDetails, False, 1),
        "city_name": (ECityName, False, "an..35"),
        "postal_identification_code": (EPostalIdentificationCode, False, "an..17"),
        "country_identifier": (ECountryIdentifier, False, "an..3"),
        "country_subdivision_details": (CUCountrySubdivisionDetails, False, 5),
        "location_identification": (CULocationIdentification, False, 5),
    }


class AgreementIdentificationSegment(Segment):
    """To specify the agreement details. """
    tag: str = "AGR"
    schema: SegmentSchema = {
        "agreement_type_identification": (CUAgreementTypeIdentification, False, 1),
        "service_layer_code": (EServiceLayerCode, False, "an..3"),
    }


class AdjustmentDetailsSegment(Segment):
    """To identify the reason for an adjustment. """
    tag: str = "AJT"
    schema: SegmentSchema = {
        "adjustment_reason_description_code": (EAdjustmentReasonDescriptionCode, False, "an..3"),
        "line_item_identifier": (ELineItemIdentifier, False, "an..6"),
    }


class AllowanceOrChargeSegment(Segment):
    """To identify allowance or charge details. """
    tag: str = "ALC"
    schema: SegmentSchema = {
        "allowance_or_charge_code_qualifier": (EAllowanceOrChargeCodeQualifier, False, "an..3"),
        "allowancecharge_information": (CUAllowancechargeInformation, False, 1),
        "settlement_means_code": (ESettlementMeansCode, False, "an..3"),
        "calculation_sequence_code": (ECalculationSequenceCode, False, "an..3"),
        "special_services_identification": (CUSpecialServicesIdentification, False, 1),
    }


class AdditionalInformationSegment(Segment):
    """To indicate that special conditions due to the origin, customs preference, fiscal or commercial factors are applicable."""
    tag: str = "ALI"
    schema: SegmentSchema = {
        "country_of_origin_identifier": (ECountryOfOriginIdentifier, False, "an..3"),
        "duty_regime_type_code": (EDutyRegimeTypeCode, False, "an..3"),
        "special_condition_code": (ESpecialConditionCode, False, "an..3"),
        "special_condition_code1": (ESpecialConditionCode, False, "an..3"),
        "special_condition_code2": (ESpecialConditionCode, False, "an..3"),
        "special_condition_code3": (ESpecialConditionCode, False, "an..3"),
        "special_condition_code4": (ESpecialConditionCode, False, "an..3"),
    }


class ApplicabilitySegment(Segment):
    """To specify the applicability. """
    tag: str = "APP"
    schema: SegmentSchema = {
        "applicability_code_qualifier": (EApplicabilityCodeQualifier, False, "an..3"),
        "applicability_type": (CUApplicabilityType, False, 1),
        "party_identification_details": (CUPartyIdentificationDetails, False, 1),
    }


class AdditionalPriceInformationSegment(Segment):
    """To provide information concerning pricing related to class of trade, price multiplier, and reason for change."""
    tag: str = "APR"
    schema: SegmentSchema = {
        "trade_class_code": (ETradeClassCode, False, "an..3"),
        "price_multiplier_information": (CUPriceMultiplierInformation, False, 1),
        "reason_for_change": (CUReasonForChange, False, 1),
    }


class MonetaryAmountFunctionSegment(Segment):
    """To provide details of the function of a monetary amount."""
    tag: str = "ARD"
    schema: SegmentSchema = {
        "monetary_amount_function": (CUMonetaryAmountFunction, False, 1),
        "monetary_amount_function_detail": (CUMonetaryAmountFunctionDetail, False, 8),
    }


class ArrayInformationSegment(Segment):
    """To contain the data in an array. """
    tag: str = "ARR"
    schema: SegmentSchema = {
        "position_identification": (CUPositionIdentification, False, 1),
        "array_cell_details": (CUArrayCellDetails, False, 1),
    }


class ArrayStructureIdentificationSegment(Segment):
    """To identify the structure of an array. """
    tag: str = "ASI"
    schema: SegmentSchema = {
        "array_structure_identification": (CUArrayStructureIdentification, False, 1),
        "party_identification_details": (CUPartyIdentificationDetails, False, 1),
        "status_description_code": (EStatusDescriptionCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


class AttributeSegment(Segment):
    """To identify a specific attribute. """
    tag: str = "ATT"
    schema: SegmentSchema = {
        "attribute_function_code_qualifier": (EAttributeFunctionCodeQualifier, False, "an..3"),
        "attribute_type": (CUAttributeType, False, 1),
        "attribute_detail": (CUAttributeDetail, False, 5),
    }


class AuthenticationResultSegment(Segment):
    """To specify results of the application of an authentication procedure."""
    tag: str = "AUT"
    schema: SegmentSchema = {
        "validation_result_text": (EValidationResultText, False, "an..35"),
        "validation_key_identifier": (EValidationKeyIdentifier, False, "an..35"),
    }


class BasisSegment(Segment):
    """To describe the foundation or starting point. """
    tag: str = "BAS"
    schema: SegmentSchema = {
        "basis_code_qualifier": (EBasisCodeQualifier, False, "an..3"),
        "basis_type": (CUBasisType, False, 1),
    }


class BeginningOfMessageSegment(Segment):
    """To indicate the type and function of a message and to transmit the identifying number. 010    C002 DOCUMENT/MESSAGE NAME                      C    1 1001  Document name code                        C      an..3 1131  Code list identification code             C      an..17 3055  Code list responsible agency code         C      an..3 1000  Document name                             C      an..35 020    C106 DOCUMENT/MESSAGE IDENTIFICATION            C    1 1004  Document identifier                       C      an..70 1056  Version identifier                        C      an..9 1060  Revision identifier                       C      an..6"""
    tag: str = "BGM"
    schema: SegmentSchema = {
        "message_function_code": (EMessageFunctionCode, False, "an..3"),
        "response_type_code": (EResponseTypeCode, False, "an..3"),
        "document_status_code": (EDocumentStatusCode, False, "an..3"),
        "language_name_code": (ELanguageNameCode, False, "an..3"),
    }


class StructureIdentificationSegment(Segment):
    """A segment used to convey an indexing structure mechanism which identifies the positioning of a group or item."""
    tag: str = "BII"
    schema: SegmentSchema = {
        "indexing_structure_code_qualifier": (EIndexingStructureCodeQualifier, False, "an..3"),
        "bill_level_identification": (CUBillLevelIdentification, False, 1),
        "item_identifier": (EItemIdentifier, False, "an..35"),
    }


class BusinessFunctionSegment(Segment):
    """To provide information related to the processing and purpose of a financial message."""
    tag: str = "BUS"
    schema: SegmentSchema = {
        "business_function": (CUBusinessFunction, False, 1),
        "geographic_area_code": (EGeographicAreaCode, False, "an..3"),
        "financial_transaction_type_code": (EFinancialTransactionTypeCode, False, "an..3"),
        "bank_operation": (CUBankOperation, False, 1),
        "intracompany_payment_indicator_code": (EIntracompanyPaymentIndicatorCode, False, "an..3"),
    }


class CharacteristicValueSegment(Segment):
    """To provide the value of a characteristic. """
    tag: str = "CAV"
    schema: SegmentSchema = {
        "characteristic_value": (CUCharacteristicValue, False, 1),
    }


class CreditCoverDetailsSegment(Segment):
    """To request a credit cover, reply to that request and disclose the reason for the reply."""
    tag: str = "CCD"
    schema: SegmentSchema = {
        "credit_cover_request_type_code": (ECreditCoverRequestTypeCode, False, "an..3"),
        "credit_cover_response_type_code": (ECreditCoverResponseTypeCode, False, "an..3"),
        "credit_cover_response_reason_code": (ECreditCoverResponseReasonCode, False, "an..3"),
    }


class CharacteristicclassIdSegment(Segment):
    """To identify and describe a specific characteristic and its relevance for subsequent business processes."""
    tag: str = "CCI"
    schema: SegmentSchema = {
        "class_type_code": (EClassTypeCode, False, "an..3"),
        "measurement_details": (CUMeasurementDetails, False, 1),
        "characteristic_description": (CUCharacteristicDescription, False, 1),
        "characteristic_relevance_code": (ECharacteristicRelevanceCode, False, "an..3"),
    }


class PhysicalOrLogicalStateSegment(Segment):
    """To describe a physical or logical state. 010    7001 PHYSICAL OR LOGICAL STATE TYPE CODE QUALIFIER                                  M    1 an..3"""
    tag: str = "CDI"
    schema: SegmentSchema = {
        "physical_or_logical_state_information": (CUPhysicalOrLogicalStateInformation, False, 1),
    }


class CodeSetIdentificationSegment(Segment):
    """To identify a code set and to give its class and maintenance operation."""
    tag: str = "CDS"
    schema: SegmentSchema = {
        "code_set_identification": (CUCodeSetIdentification, False, 1),
        "designated_class_code": (EDesignatedClassCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


class CodeValueDefinitionSegment(Segment):
    """To provide information related to a code value. """
    tag: str = "CDV"
    schema: SegmentSchema = {
        "code_value_text": (ECodeValueText, False, "an..35"),
        "code_name": (ECodeName, False, "an..70"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
        "code_value_source_code": (ECodeValueSourceCode, False, "an..3"),
        "requirement_designator_code": (ERequirementDesignatorCode, False, "an..3"),
    }


class ComputerEnvironmentDetailsSegment(Segment):
    """To give a precise definition of all necessary elements belonging to the configuration of a computer system like hardware, firmware, operating system, communication (VANS, network type, protocol, format) and application software. 010    1501 COMPUTER ENVIRONMENT DETAILS CODE QUALIFIER                                  M    1 an..3"""
    tag: str = "CED"
    schema: SegmentSchema = {
        "computer_environment_identification": (CUComputerEnvironmentIdentification, False, 1),
        "file_generation_command_name": (EFileGenerationCommandName, False, "an..35"),
    }


class ClinicalInformationSegment(Segment):
    """To describe an item of clinical information. """
    tag: str = "CIN"
    schema: SegmentSchema = {
        "clinical_information_type_code_qualifier": (EClinicalInformationTypeCodeQualifier, False, "an..3"),
        "clinical_information_details": (CUClinicalInformationDetails, False, 1),
        "certainty_details": (CUCertaintyDetails, False, 1),
    }


class ClauseIdentificationSegment(Segment):
    """To identify a clause in a treaty, law and/or contract."""
    tag: str = "CLA"
    schema: SegmentSchema = {
        "clause_code_qualifier": (EClauseCodeQualifier, False, "an..3"),
        "clause_name": (CUClauseName, False, 1),
    }


class ClinicalInterventionSegment(Segment):
    """To specify a clinical intervention such as treatments and investigations."""
    tag: str = "CLI"
    schema: SegmentSchema = {
        "clinical_intervention_type_code_qualifier": (EClinicalInterventionTypeCodeQualifier, False, "an..3"),
        "clinical_intervention_details": (CUClinicalInterventionDetails, False, 1),
    }


class CompositeDataElementIdentificationSegment(Segment):
    """To identify a composite data element and to give its class and maintenance operation."""
    tag: str = "CMP"
    schema: SegmentSchema = {
        "composite_data_element_tag_identifier": (ECompositeDataElementTagIdentifier, False, "an..4"),
        "designated_class_code": (EDesignatedClassCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


class ConsignmentInformationSegment(Segment):
    """To identify one consignment. """
    tag: str = "CNI"
    schema: SegmentSchema = {
        "consolidation_item_number": (EConsolidationItemNumber, False, "n..5"),
        "documentmessage_details": (CUDocumentmessageDetails, False, 1),
        "consignment_load_sequence_identifier": (EConsignmentLoadSequenceIdentifier, False, "n..4"),
    }


class ControlTotalSegment(Segment):
    """To provide control total. """
    tag: str = "CNT"
    schema: SegmentSchema = {
        "control": (CUControl, False, 1),
    }


class ComponentDetailsSegment(Segment):
    """To provide component details of an object (e.g. product, container) such as its type and the material of which it is composed. 010    C823 TYPE OF UNIT/COMPONENT                     C    1 7505  Unit or component type description code   C      an..3 1131  Code list identification code             C      an..17 3055  Code list responsible agency code         C      an..3 7504  Unit or component type description        C      an..35"""
    tag: str = "COD"
    schema: SegmentSchema = {
        "component_material": (CUComponentMaterial, False, 1),
    }


class CommunicationContactSegment(Segment):
    """To identify a communication number of a department or a person to whom communication should be directed."""
    tag: str = "COM"
    schema: SegmentSchema = {
        "communication_contact": (CUCommunicationContact, False, 3),
    }


class ContributionDetailsSegment(Segment):
    """To specify details about membership contributions."""
    tag: str = "COT"
    schema: SegmentSchema = {
        "contribution_code_qualifier": (EContributionCodeQualifier, False, "an..3"),
        "contribution_type": (CUContributionType, False, 1),
        "instruction": (CUInstruction, False, 1),
        "ratetariff_class": (CURatetariffClass, False, 1),
        "reason_for_change": (CUReasonForChange, False, 1),
    }


class ChargePaymentInstructionsSegment(Segment):
    """To identify a charge. """
    tag: str = "CPI"
    schema: SegmentSchema = {
        "charge_category": (CUChargeCategory, False, 1),
        "method_of_payment": (CUMethodOfPayment, False, 1),
        "payment_arrangement_code": (EPaymentArrangementCode, False, "an..3"),
    }


class ConsignmentPackingSequenceSegment(Segment):
    """To identify the sequence in which physical packing is presented in the consignment, and optionally to identify the hierarchical relationship between packing layers."""
    tag: str = "CPS"
    schema: SegmentSchema = {
        "hierarchical_structure_level_identifier": (EHierarchicalStructureLevelIdentifier, False, "an..35"),
        "hierarchical_structure_parent_identifier": (EHierarchicalStructureParentIdentifier, False, "an..35"),
        "packaging_level_code": (EPackagingLevelCode, False, "an..3"),
    }


class AccountIdentificationSegment(Segment):
    """To provide account identification information. """
    tag: str = "CPT"
    schema: SegmentSchema = {
        "account_type_code_qualifier": (EAccountTypeCodeQualifier, False, "an..3"),
        "account_identification": (CUAccountIdentification, False, 1),
    }


class CustomsStatusOfGoodsSegment(Segment):
    """To specify goods in terms of customs identities, status and intended use."""
    tag: str = "CST"
    schema: SegmentSchema = {
        "goods_item_number": (EGoodsItemNumber, False, "an..6"),
        "customs_identity_codes": (CUCustomsIdentityCodes, False, 1),
        "customs_identity_codes1": (CUCustomsIdentityCodes, False, 1),
        "customs_identity_codes2": (CUCustomsIdentityCodes, False, 1),
        "customs_identity_codes3": (CUCustomsIdentityCodes, False, 1),
        "customs_identity_codes4": (CUCustomsIdentityCodes, False, 1),
    }


class ContactInformationSegment(Segment):
    """To identify a person or a department to whom communication should be directed."""
    tag: str = "CTA"
    schema: SegmentSchema = {
        "contact_function_code": (EContactFunctionCode, False, "an..3"),
        "contact_details": (CUContactDetails, False, 1),
    }


class CurrenciesSegment(Segment):
    """To specify currencies used in the transaction and relevant details for the rate of exchange."""
    tag: str = "CUX"
    schema: SegmentSchema = {
        "currency_details": (CUCurrencyDetails, False, 1),
        "currency_details1": (CUCurrencyDetails, False, 1),
        "currency_exchange_rate": (ECurrencyExchangeRate, False, "n..12"),
        "exchange_rate_currency_market_identifier": (EExchangeRateCurrencyMarketIdentifier, False, "an..3"),
    }


class DamageSegment(Segment):
    """To specify damage including action taken. """
    tag: str = "DAM"
    schema: SegmentSchema = {
        "damage_details_code_qualifier": (EDamageDetailsCodeQualifier, False, "an..3"),
        "type_of_damage": (CUTypeOfDamage, False, 1),
        "damage_area": (CUDamageArea, False, 1),
        "damage_severity": (CUDamageSeverity, False, 1),
        "action": (CUAction, False, 1),
    }


class DefinitionFunctionSegment(Segment):
    """To specify a definition function. """
    tag: str = "DFN"
    schema: SegmentSchema = {
        "definition_function_code": (EDefinitionFunctionCode, False, "an..3"),
        "definition_extent_code": (EDefinitionExtentCode, False, "an..3"),
        "definition_identifier": (EDefinitionIdentifier, False, "an..35"),
    }


class DangerousGoodsSegment(Segment):
    """To identify dangerous goods. """
    tag: str = "DGS"
    schema: SegmentSchema = {
        "dangerous_goods_regulations_code": (EDangerousGoodsRegulationsCode, False, "an..3"),
        "hazard_code": (CUHazardCode, False, 1),
        "undg_information": (CUUndgInformation, False, 1),
        "dangerous_goods_shipment_flashpoint": (CUDangerousGoodsShipmentFlashpoint, False, 1),
        "packaging_danger_level_code": (EPackagingDangerLevelCode, False, "an..3"),
        "emergency_procedure_for_ships_identifier": (EEmergencyProcedureForShipsIdentifier, False, "an..8"),
        "hazard_medical_first_aid_guide_identifier": (EHazardMedicalFirstAidGuideIdentifier, False, "an..4"),
        "transport_emergency_card_identifier": (ETransportEmergencyCardIdentifier, False, "an..10"),
        "hazard_identification_placard_details": (CUHazardIdentificationPlacardDetails, False, 1),
        "dangerous_goods_label": (CUDangerousGoodsLabel, False, 1),
        "packing_instruction_type_code": (EPackingInstructionTypeCode, False, "an..3"),
        "transport_means_description_code": (ETransportMeansDescriptionCode, False, "an..8"),
        "tunnel_restriction": (CUTunnelRestriction, False, 1),
    }


class DirectoryIdentificationSegment(Segment):
    """To identify a directory and to give its release, status, controlling agency, language and maintenance operation."""
    tag: str = "DII"
    schema: SegmentSchema = {
        "version_identifier": (EVersionIdentifier, False, "an..9"),
        "release_identifier": (EReleaseIdentifier, False, "an..9"),
        "directory_status_identifier": (EDirectoryStatusIdentifier, False, "an..3"),
        "controlling_agency_identifier": (EControllingAgencyIdentifier, False, "an..2"),
        "language_name_code": (ELanguageNameCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


class DimensionsSegment(Segment):
    """To specify dimensions. """
    tag: str = "DIM"
    schema: SegmentSchema = {
        "dimension_type_code_qualifier": (EDimensionTypeCodeQualifier, False, "an..3"),
        "dimensions": (CUDimensions, False, 1),
    }


class DocumentLineIdentificationSegment(Segment):
    """To specify the processing mode of a specific line within a referenced document."""
    tag: str = "DLI"
    schema: SegmentSchema = {
        "document_line_action_code": (EDocumentLineActionCode, False, "an..3"),
        "line_item_identifier": (ELineItemIdentifier, False, "an..6"),
    }


class DeliveryLimitationsSegment(Segment):
    """To specify limitations on deliveries. """
    tag: str = "DLM"
    schema: SegmentSchema = {
        "back_order_arrangement_type_code": (EBackOrderArrangementTypeCode, False, "an..3"),
        "instruction": (CUInstruction, False, 1),
        "special_services_identification": (CUSpecialServicesIdentification, False, 1),
        "substitution_condition_code": (ESubstitutionConditionCode, False, "an..3"),
    }


class DocumentmessageSummarySegment(Segment):
    """To specify summary information relating to the document/message. 010    C106 DOCUMENT/MESSAGE IDENTIFICATION            C    1 1004  Document identifier                       C      an..70 1056  Version identifier                        C      an..9 1060  Revision identifier                       C      an..6 020    C002 DOCUMENT/MESSAGE NAME                      C    1 1001  Document name code                        C      an..3 1131  Code list identification code             C      an..17 3055  Code list responsible agency code         C      an..3 1000  Document name                             C      an..35"""
    tag: str = "DMS"
    schema: SegmentSchema = {
        "item_total_quantity": (EItemTotalQuantity, False, "n..15"),
    }


class DocumentmessageDetailsSegment(Segment):
    """To identify documents and details directly related to it. 010    C002 DOCUMENT/MESSAGE NAME                      M    1 1001  Document name code                        C      an..3 1131  Code list identification code             C      an..17 3055  Code list responsible agency code         C      an..3 1000  Document name                             C      an..35 020    C503 DOCUMENT/MESSAGE DETAILS                   C    1 1004  Document identifier                       C      an..70 1373  Document status code                      C      an..3 1366  Document source description               C      an..70 3453  Language name code                        C      an..3 1056  Version identifier                        C      an..9 1060  Revision identifier                       C      an..6"""
    tag: str = "DOC"
    schema: SegmentSchema = {
        "communication_medium_type_code": (ECommunicationMediumTypeCode, False, "an..3"),
        "document_copies_required_quantity": (EDocumentCopiesRequiredQuantity, False, "n..2"),
        "document_originals_required_quantity": (EDocumentOriginalsRequiredQuantity, False, "n..2"),
    }


class DataRepresentationDetailsSegment(Segment):
    """To specify the details of the data representation."""
    tag: str = "DRD"
    schema: SegmentSchema = {
        "structure_component_identifier": (EStructureComponentIdentifier, False, "an..35"),
        "structure_type_code": (EStructureTypeCode, False, "an..3"),
        "data_representation_type_code": (EDataRepresentationTypeCode, False, "an..3"),
        "size_measure": (ESizeMeasure, False, "n..15"),
    }


class DosageAdministrationSegment(Segment):
    """To communicate how dose(s) are administered. """
    tag: str = "DSG"
    schema: SegmentSchema = {
        "dosage_administration_code_qualifier": (EDosageAdministrationCodeQualifier, False, "an..3"),
        "dosage_details": (CUDosageDetails, False, 1),
    }


class DataSetIdentificationSegment(Segment):
    """To identify a data set. """
    tag: str = "DSI"
    schema: SegmentSchema = {
        "data_set_identification": (CUDataSetIdentification, False, 1),
        "party_identification_details": (CUPartyIdentificationDetails, False, 1),
        "status_description_code": (EStatusDescriptionCode, False, "an..3"),
        "sequence_information": (CUSequenceInformation, False, 1),
        "revision_identifier": (ERevisionIdentifier, False, "an..6"),
    }


class DatetimeperiodSegment(Segment):
    """To specify date, and/or time, or period. 010    C507 DATE/TIME/PERIOD                           M    1 2005  Date or time or period function code qualifier                                 M      an..3 2380  Date or time or period text               C      an..35 2379  Date or time or period format code        C      an..3 
---------------------------------------------------------------------- EDT  EDITING DETAILS Function: To specify editing details."""
    tag: str = "DTM"
    schema: SegmentSchema = {
        "edit_field_length_measure": (EEditFieldLengthMeasure, False, "n..3"),
        "edit_mask_format_identifier": (EEditMaskFormatIdentifier, False, "an..35"),
        "edit_mask_representation_code": (EEditMaskRepresentationCode, False, "an..3"),
        "free_text_format_code": (EFreeTextFormatCode, False, "an..3"),
    }


class ExternalFileLinkIdentificationSegment(Segment):
    """To specify the link of one non-EDIFACT external file to an EDIFACT message."""
    tag: str = "EFI"
    schema: SegmentSchema = {
        "file_identification": (CUFileIdentification, False, 1),
        "file_details": (CUFileDetails, False, 1),
        "sequence_position_identifier": (ESequencePositionIdentifier, False, "an..10"),
        "file_compression_technique_name": (EFileCompressionTechniqueName, False, "an..35"),
    }


class SimpleDataElementDetailsSegment(Segment):
    """To identify a simple data element and give related details."""
    tag: str = "ELM"
    schema: SegmentSchema = {
        "simple_data_element_tag_identifier": (ESimpleDataElementTagIdentifier, False, "an..4"),
        "length_type_code": (ELengthTypeCode, False, "an..3"),
        "code_set_indicator_code": (ECodeSetIndicatorCode, False, "an..3"),
        "designated_class_code": (EDesignatedClassCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
        "significant_digits_quantity": (ESignificantDigitsQuantity, False, "n..2"),
    }


class DataElementUsageDetailsSegment(Segment):
    """To specify the usage of a data element. """
    tag: str = "ELU"
    schema: SegmentSchema = {
        "data_element_tag_identifier": (EDataElementTagIdentifier, False, "an..4"),
        "requirement_designator_code": (ERequirementDesignatorCode, False, "an..3"),
        "sequence_position_identifier": (ESequencePositionIdentifier, False, "an..10"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
        "occurrences_maximum_number": (EOccurrencesMaximumNumber, False, "n..7"),
        "code_value_source_code": (ECodeValueSourceCode, False, "an..3"),
        "validation_criteria_code": (EValidationCriteriaCode, False, "an..3"),
        "data_element_usage_type_code": (EDataElementUsageTypeCode, False, "an..3"),
    }


class ElementValueDefinitionSegment(Segment):
    """To define an element value. """
    tag: str = "ELV"
    schema: SegmentSchema = {
        "value_definition_code_qualifier": (EValueDefinitionCodeQualifier, False, "an..3"),
        "value_text": (EValueText, False, "an..512"),
        "requirement_designator_code": (ERequirementDesignatorCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


class EmploymentDetailsSegment(Segment):
    """To specify employment details. """
    tag: str = "EMP"
    schema: SegmentSchema = {
        "employment_details_code_qualifier": (EEmploymentDetailsCodeQualifier, False, "an..3"),
        "employment_category": (CUEmploymentCategory, False, 1),
        "occupation": (CUOccupation, False, 1),
        "qualification_classification": (CUQualificationClassification, False, 1),
        "person_job_title": (EPersonJobTitle, False, "an..35"),
        "qualification_application_area_code": (EQualificationApplicationAreaCode, False, "an..3"),
    }


class AttachedEquipmentSegment(Segment):
    """To specify attached or related equipment. """
    tag: str = "EQA"
    schema: SegmentSchema = {
        "equipment_type_code_qualifier": (EEquipmentTypeCodeQualifier, False, "an..3"),
        "equipment_identification": (CUEquipmentIdentification, False, 1),
    }


class EquipmentDetailsSegment(Segment):
    """To identify a unit of equipment. """
    tag: str = "EQD"
    schema: SegmentSchema = {
        "equipment_type_code_qualifier": (EEquipmentTypeCodeQualifier, False, "an..3"),
        "equipment_identification": (CUEquipmentIdentification, False, 1),
        "equipment_size_and_type": (CUEquipmentSizeAndType, False, 1),
        "equipment_supplier_code": (EEquipmentSupplierCode, False, "an..3"),
        "equipment_status_code": (EEquipmentStatusCode, False, "an..3"),
        "full_or_empty_indicator_code": (EFullOrEmptyIndicatorCode, False, "an..3"),
        "marking_instructions_code": (EMarkingInstructionsCode, False, "an..3"),
    }


class NumberOfUnitsSegment(Segment):
    """To specify the number of units. """
    tag: str = "EQN"
    schema: SegmentSchema = {
        "number_of_unit_details": (CUNumberOfUnitDetails, False, 1),
    }


class ApplicationErrorInformationSegment(Segment):
    """To identify the type of application error within a message."""
    tag: str = "ERC"
    schema: SegmentSchema = {
        "application_error_detail": (CUApplicationErrorDetail, False, 1),
    }


class ErrorPointDetailsSegment(Segment):
    """A segment to identify the location of an application error within a message."""
    tag: str = "ERP"
    schema: SegmentSchema = {
        "error_point_details": (CUErrorPointDetails, False, 1),
        "error_segment_point_details": (CUErrorSegmentPointDetails, False, 1),
    }


class EventSegment(Segment):
    """To specify details about events. """
    tag: str = "EVE"
    schema: SegmentSchema = {
        "event_details_code_qualifier": (EEventDetailsCodeQualifier, False, "an..3"),
        "event_category": (CUEventCategory, False, 1),
        "event_type": (CUEventType, False, 1),
        "event_identification": (CUEventIdentification, False, 5),
        "action_code": (EActionCode, False, "an..3"),
    }


class FinancialChargesAllocationSegment(Segment):
    """Description of allocation of charges. """
    tag: str = "FCA"
    schema: SegmentSchema = {
        "settlement_means_code": (ESettlementMeansCode, False, "an..3"),
        "chargeallowance_account": (CUChargeallowanceAccount, False, 1),
    }


class FinancialInstitutionInformationSegment(Segment):
    """To identify an account and a related financial institution."""
    tag: str = "FII"
    schema: SegmentSchema = {
        "party_function_code_qualifier": (EPartyFunctionCodeQualifier, False, "an..3"),
        "account_holder_identification": (CUAccountHolderIdentification, False, 1),
        "institution_identification": (CUInstitutionIdentification, False, 1),
        "country_identifier": (ECountryIdentifier, False, "an..3"),
    }


class FootnoteSetSegment(Segment):
    """To identify a set of footnotes. """
    tag: str = "FNS"
    schema: SegmentSchema = {
        "footnote_set_identification": (CUFootnoteSetIdentification, False, 1),
        "party_identification_details": (CUPartyIdentificationDetails, False, 1),
        "status_description_code": (EStatusDescriptionCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


class FootnoteSegment(Segment):
    """To identify a footnote. """
    tag: str = "FNT"
    schema: SegmentSchema = {
        "footnote_identification": (CUFootnoteIdentification, False, 1),
        "party_identification_details": (CUPartyIdentificationDetails, False, 1),
        "status_description_code": (EStatusDescriptionCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


class FormulaSegment(Segment):
    """To identify a formula. """
    tag: str = "FOR"
    schema: SegmentSchema = {
        "formula_type_code_qualifier": (EFormulaTypeCodeQualifier, False, "an..3"),
        "object_identifier": (EObjectIdentifier, False, "an..35"),
        "formula_name": (EFormulaName, False, "an..35"),
        "free_text": (EFreeText, False, "an..512"),
        "formula_complexity": (CUFormulaComplexity, False, 1),
    }


class FormulaSequenceSegment(Segment):
    """To provide a single operation within the sequence of operations of a formula."""
    tag: str = "FSQ"
    schema: SegmentSchema = {
        "formula_sequence_code_qualifier": (EFormulaSequenceCodeQualifier, False, "an..3"),
        "formula_sequence_operand_code": (EFormulaSequenceOperandCode, False, "an..17"),
        "sequence_position_identifier": (ESequencePositionIdentifier, False, "an..10"),
        "formula_sequence_name": (EFormulaSequenceName, False, "an..35"),
        "free_text": (EFreeText, False, "an..512"),
    }


class FreeTextSegment(Segment):
    """To provide free form or coded text information. """
    tag: str = "FTX"
    schema: SegmentSchema = {
        "text_subject_code_qualifier": (ETextSubjectCodeQualifier, False, "an..3"),
        "free_text_function_code": (EFreeTextFunctionCode, False, "an..3"),
        "text_reference": (CUTextReference, False, 1),
        "text_literal": (CUTextLiteral, False, 1),
        "language_name_code": (ELanguageNameCode, False, "an..3"),
        "free_text_format_code": (EFreeTextFormatCode, False, "an..3"),
    }


class NatureOfCargoSegment(Segment):
    """To indicate the type of cargo as a general classification."""
    tag: str = "GDS"
    schema: SegmentSchema = {
        "nature_of_cargo": (CUNatureOfCargo, False, 1),
        "product_group": (CUProductGroup, False, 1),
    }


class ProcessingInformationSegment(Segment):
    """To identify processing information. """
    tag: str = "GEI"
    schema: SegmentSchema = {
        "processing_information_code_qualifier": (EProcessingInformationCodeQualifier, False, "an..3"),
        "processing_indicator": (CUProcessingIndicator, False, 1),
        "process_type_description_code": (EProcessTypeDescriptionCode, False, "an..17"),
    }


class GoodsItemDetailsSegment(Segment):
    """To indicate totals of a goods item. """
    tag: str = "GID"
    schema: SegmentSchema = {
        "goods_item_number": (EGoodsItemNumber, False, "an..6"),
        "number_and_type_of_packages": (CUNumberAndTypeOfPackages, False, 1),
        "number_and_type_of_packages1": (CUNumberAndTypeOfPackages, False, 1),
        "number_and_type_of_packages2": (CUNumberAndTypeOfPackages, False, 1),
        "number_and_type_of_packages3": (CUNumberAndTypeOfPackages, False, 1),
        "number_and_type_of_packages4": (CUNumberAndTypeOfPackages, False, 1),
    }


class GoodsIdentityNumberSegment(Segment):
    """To give specific identification numbers, either as single numbers or ranges."""
    tag: str = "GIN"
    schema: SegmentSchema = {
        "object_identification_code_qualifier": (EObjectIdentificationCodeQualifier, False, "an..3"),
        "identity_number_range": (CUIdentityNumberRange, False, 1),
        "identity_number_range1": (CUIdentityNumberRange, False, 1),
        "identity_number_range2": (CUIdentityNumberRange, False, 1),
        "identity_number_range3": (CUIdentityNumberRange, False, 1),
        "identity_number_range4": (CUIdentityNumberRange, False, 1),
    }


class RelatedIdentificationNumbersSegment(Segment):
    """To specify a related set of identification numbers."""
    tag: str = "GIR"
    schema: SegmentSchema = {
        "set_type_code_qualifier": (ESetTypeCodeQualifier, False, "an..3"),
        "identification_number": (CUIdentificationNumber, False, 1),
        "identification_number1": (CUIdentificationNumber, False, 1),
        "identification_number2": (CUIdentificationNumber, False, 1),
        "identification_number3": (CUIdentificationNumber, False, 1),
        "identification_number4": (CUIdentificationNumber, False, 1),
    }


class GovernmentalRequirementsSegment(Segment):
    """To indicate the requirement for a specific governmental action and/or procedure or which specific procedure is valid for a specific part of the transport and cross-border transactions."""
    tag: str = "GOR"
    schema: SegmentSchema = {
        "transport_movement_code": (ETransportMovementCode, False, "an..3"),
        "government_action": (CUGovernmentAction, False, 1),
        "government_action1": (CUGovernmentAction, False, 1),
        "government_action2": (CUGovernmentAction, False, 1),
        "government_action3": (CUGovernmentAction, False, 1),
    }


class GeographicalPositionSegment(Segment):
    """To specify a geographical position. """
    tag: str = "GPO"
    schema: SegmentSchema = {
        "geographical_position_code_qualifier": (EGeographicalPositionCodeQualifier, False, "an..3"),
        "latitude_degree": (ELatitudeDegree, False, "an..10"),
        "longitude_degree": (ELongitudeDegree, False, "an..11"),
        "altitude": (EAltitude, False, "n..18"),
    }


class SegmentGroupUsageDetailsSegment(Segment):
    """To specify the usage of a segment group within a message type structure and its maintenance operation."""
    tag: str = "GRU"
    schema: SegmentSchema = {
        "group_identifier": (EGroupIdentifier, False, "an..4"),
        "requirement_designator_code": (ERequirementDesignatorCode, False, "an..3"),
        "occurrences_maximum_number": (EOccurrencesMaximumNumber, False, "n..7"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
        "sequence_position_identifier": (ESequencePositionIdentifier, False, "an..10"),
    }


class HandlingInstructionsSegment(Segment):
    """To specify handling and where necessary, notify hazards."""
    tag: str = "HAN"
    schema: SegmentSchema = {
        "handling_instructions": (CUHandlingInstructions, False, 1),
        "hazardous_material": (CUHazardousMaterial, False, 1),
    }


class HierarchyInformationSegment(Segment):
    """A segment to identify hierarchical connections from a given item to a higher or lower levelled item or to identify dependencies among the content of hierarchically related groups of data."""
    tag: str = "HYN"
    schema: SegmentSchema = {
        "hierarchy_object_code_qualifier": (EHierarchyObjectCodeQualifier, False, "an..3"),
        "hierarchical_structure_relationship_code": (EHierarchicalStructureRelationshipCode, False, "an..3"),
        "action_code": (EActionCode, False, "an..3"),
        "item_number_identification": (CUItemNumberIdentification, False, 1),
        "hierarchical_structure_parent_identifier": (EHierarchicalStructureParentIdentifier, False, "an..35"),
    }


class InsuranceCoverDescriptionSegment(Segment):
    """To describe the insurance cover. """
    tag: str = "ICD"
    schema: SegmentSchema = {
        "insurance_cover_type": (CUInsuranceCoverType, False, 1),
        "insurance_cover_details": (CUInsuranceCoverDetails, False, 1),
    }


class IdentitySegment(Segment):
    """To identify an object. """
    tag: str = "IDE"
    schema: SegmentSchema = {
        "object_type_code_qualifier": (EObjectTypeCodeQualifier, False, "an..3"),
        "identification_number": (CUIdentificationNumber, False, 1),
        "party_identification_details": (CUPartyIdentificationDetails, False, 1),
        "status_description_code": (EStatusDescriptionCode, False, "an..3"),
        "configuration_level_number": (EConfigurationLevelNumber, False, "n..2"),
        "position_identification": (CUPositionIdentification, False, 99),
        "characteristic_description": (CUCharacteristicDescription, False, 1),
    }


class InformationDetailSegment(Segment):
    """To specify details about items of information. """
    tag: str = "IFD"
    schema: SegmentSchema = {
        "information_details_code_qualifier": (EInformationDetailsCodeQualifier, False, "an..3"),
        "information_category": (CUInformationCategory, False, 1),
        "information_type": (CUInformationType, False, 1),
        "information_detail": (CUInformationDetail, False, 5),
        "status_description_code": (EStatusDescriptionCode, False, "an..3"),
    }


class PersonCharacteristicSegment(Segment):
    """To specify characteristics of a person such as ethnic origin."""
    tag: str = "IHC"
    schema: SegmentSchema = {
        "person_characteristic_code_qualifier": (EPersonCharacteristicCodeQualifier, False, "an..3"),
        "person_inherited_characteristic_details": (CUPersonInheritedCharacteristicDetails, False, 1),
    }


class ItemDescriptionSegment(Segment):
    """To describe an item in either an industry or free format."""
    tag: str = "IMD"
    schema: SegmentSchema = {
        "description_format_code": (EDescriptionFormatCode, False, "an..3"),
        "item_characteristic": (CUItemCharacteristic, False, 1),
        "item_description": (CUItemDescription, False, 1),
        "surface_or_layer_code": (ESurfaceOrLayerCode, False, "an..3"),
    }


class IndexDetailsSegment(Segment):
    """To specify an index. """
    tag: str = "IND"
    schema: SegmentSchema = {
        "index_identification": (CUIndexIdentification, False, 1),
        "index_value": (CUIndexValue, False, 1),
    }


class PartiesAndInstructionSegment(Segment):
    """To specify parties to an instruction, the instruction, or both."""
    tag: str = "INP"
    schema: SegmentSchema = {
        "parties_to_instruction": (CUPartiesToInstruction, False, 1),
        "instruction": (CUInstruction, False, 1),
        "status_of_instruction": (CUStatusOfInstruction, False, 1),
        "action_code": (EActionCode, False, "an..3"),
    }


class InventoryManagementRelatedDetailsSegment(Segment):
    """To provide the different information related to the inventory management functions and needed to process properly the inventory movements and the inventory balances."""
    tag: str = "INV"
    schema: SegmentSchema = {
        "inventory_movement_direction_code": (EInventoryMovementDirectionCode, False, "an..3"),
        "inventory_type_code": (EInventoryTypeCode, False, "an..3"),
        "inventory_movement_reason_code": (EInventoryMovementReasonCode, False, "an..3"),
        "inventory_balance_method_code": (EInventoryBalanceMethodCode, False, "an..3"),
        "instruction": (CUInstruction, False, 1),
    }


class InformationRequiredSegment(Segment):
    """To indicate which information is requested in a responding message."""
    tag: str = "IRQ"
    schema: SegmentSchema = {
        "information_request": (CUInformationRequest, False, 1),
    }


class LanguageSegment(Segment):
    """To specify a language. """
    tag: str = "LAN"
    schema: SegmentSchema = {
        "language_code_qualifier": (ELanguageCodeQualifier, False, "an..3"),
        "language_details": (CULanguageDetails, False, 1),
    }


class LineItemSegment(Segment):
    """To identify a line item and configuration. """
    tag: str = "LIN"
    schema: SegmentSchema = {
        "line_item_identifier": (ELineItemIdentifier, False, "an..6"),
        "action_code": (EActionCode, False, "an..3"),
        "item_number_identification": (CUItemNumberIdentification, False, 1),
        "subline_information": (CUSublineInformation, False, 1),
        "configuration_level_number": (EConfigurationLevelNumber, False, "n..2"),
        "configuration_operation_code": (EConfigurationOperationCode, False, "an..3"),
    }


class PlacelocationIdentificationSegment(Segment):
    """To identify a place or a location and/or related locations."""
    tag: str = "LOC"
    schema: SegmentSchema = {
        "location_function_code_qualifier": (ELocationFunctionCodeQualifier, False, "an..3"),
        "location_identification": (CULocationIdentification, False, 1),
        "related_location_one_identification": (CURelatedLocationOneIdentification, False, 1),
        "related_location_two_identification": (CURelatedLocationTwoIdentification, False, 1),
        "relation_code": (ERelationCode, False, "an..3"),
    }


class MeasurementsSegment(Segment):
    """To specify physical measurements, including dimension tolerances, weights and counts."""
    tag: str = "MEA"
    schema: SegmentSchema = {
        "measurement_purpose_code_qualifier": (EMeasurementPurposeCodeQualifier, False, "an..3"),
        "measurement_details": (CUMeasurementDetails, False, 1),
        "valuerange": (CUValuerange, False, 1),
        "surface_or_layer_code": (ESurfaceOrLayerCode, False, "an..3"),
    }


class MembershipDetailsSegment(Segment):
    """To specify details about membership. """
    tag: str = "MEM"
    schema: SegmentSchema = {
        "membership_type_code_qualifier": (EMembershipTypeCodeQualifier, False, "an..3"),
        "membership_category": (CUMembershipCategory, False, 1),
        "membership_status": (CUMembershipStatus, False, 1),
        "membership_level": (CUMembershipLevel, False, 1),
        "ratetariff_class": (CURatetariffClass, False, 1),
        "reason_for_change": (CUReasonForChange, False, 1),
    }


class MarketsalesChannelInformationSegment(Segment):
    """To specify to which market and/or through which sales distribution channel and/or for which end- use the sales of product/service have been made or are given as forecast."""
    tag: str = "MKS"
    schema: SegmentSchema = {
        "sector_area_identification_code_qualifier": (ESectorAreaIdentificationCodeQualifier, False, "an..3"),
        "sales_channel_identification": (CUSalesChannelIdentification, False, 1),
        "action_code": (EActionCode, False, "an..3"),
    }


class MonetaryAmountSegment(Segment):
    """To specify a monetary amount. """
    tag: str = "MOA"
    schema: SegmentSchema = {
        "monetary_amount": (CUMonetaryAmount, False, 1),
    }


class MessageTypeIdentificationSegment(Segment):
    """To identify a message type and to give its class and maintenance operation."""
    tag: str = "MSG"
    schema: SegmentSchema = {
        "message_identifier": (CUMessageIdentifier, False, 1),
        "designated_class_code": (EDesignatedClassCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
        "relationship": (CURelationship, False, 1),
    }


class MaintenanceOperationDetailsSegment(Segment):
    """To identify a maintenance operation and its responsible parties."""
    tag: str = "MTD"
    schema: SegmentSchema = {
        "object_type_code_qualifier": (EObjectTypeCodeQualifier, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
        "maintenance_operation_operator_code": (EMaintenanceOperationOperatorCode, False, "an..3"),
        "maintenance_operation_payer_code": (EMaintenanceOperationPayerCode, False, "an..3"),
    }


class NameAndAddressSegment(Segment):
    """To specify the name/address and their related function, either by C082 only and/or unstructured by C058 or structured by C080 thru 3207."""
    tag: str = "NAD"
    schema: SegmentSchema = {
        "party_function_code_qualifier": (EPartyFunctionCodeQualifier, False, "an..3"),
        "party_identification_details": (CUPartyIdentificationDetails, False, 1),
        "name_and_address": (CUNameAndAddress, False, 1),
        "party_name": (CUPartyName, False, 1),
        "street": (CUStreet, False, 1),
        "city_name": (ECityName, False, "an..35"),
        "country_subdivision_details": (CUCountrySubdivisionDetails, False, 1),
        "postal_identification_code": (EPostalIdentificationCode, False, "an..17"),
        "country_identifier": (ECountryIdentifier, False, "an..3"),
    }


class NationalitySegment(Segment):
    """To specify a nationality. """
    tag: str = "NAT"
    schema: SegmentSchema = {
        "nationality_code_qualifier": (ENationalityCodeQualifier, False, "an..3"),
        "nationality_details": (CUNationalityDetails, False, 1),
    }


class PackageSegment(Segment):
    """To describe the number and type of packages/physical units."""
    tag: str = "PAC"
    schema: SegmentSchema = {
        "package_quantity": (EPackageQuantity, False, "n..8"),
        "packaging_details": (CUPackagingDetails, False, 1),
        "package_type": (CUPackageType, False, 1),
        "package_type_identification": (CUPackageTypeIdentification, False, 1),
        "returnable_package_details": (CUReturnablePackageDetails, False, 1),
    }


class PaymentInstructionsSegment(Segment):
    """To specify the instructions for payment. """
    tag: str = "PAI"
    schema: SegmentSchema = {
        "payment_instruction_details": (CUPaymentInstructionDetails, False, 1),
    }


class AttendanceSegment(Segment):
    """To specify attendance information relating to an individual."""
    tag: str = "PAS"
    schema: SegmentSchema = {
        "attendance_type_code_qualifier": (EAttendanceTypeCodeQualifier, False, "an..3"),
        "attendee_category": (CUAttendeeCategory, False, 1),
        "attendance_admission_details": (CUAttendanceAdmissionDetails, False, 1),
        "attendance_discharge_details": (CUAttendanceDischargeDetails, False, 1),
    }


class PremiumCalculationComponentDetailsSegment(Segment):
    """To identify the component affecting a premium calculation and the value category of the component."""
    tag: str = "PCC"
    schema: SegmentSchema = {
        "premium_calculation_component": (CUPremiumCalculationComponent, False, 1),
    }


class PercentageDetailsSegment(Segment):
    """To specify percentage information. """
    tag: str = "PCD"
    schema: SegmentSchema = {
        "percentage_details": (CUPercentageDetails, False, 1),
        "status_description_code": (EStatusDescriptionCode, False, "an..3"),
    }


class PackageIdentificationSegment(Segment):
    """To specify markings and labels on individual packages or physical units."""
    tag: str = "PCI"
    schema: SegmentSchema = {
        "marking_instructions_code": (EMarkingInstructionsCode, False, "an..3"),
        "marks__labels": (CUMarksLabels, False, 1),
        "full_or_empty_indicator_code": (EFullOrEmptyIndicatorCode, False, "an..3"),
        "type_of_marking": (CUTypeOfMarking, False, 1),
    }


class PersonDemographicInformationSegment(Segment):
    """To specify items of person demographic information."""
    tag: str = "PDI"
    schema: SegmentSchema = {
        "gender_code": (EGenderCode, False, "an..3"),
        "marital_status_details": (CUMaritalStatusDetails, False, 1),
        "religion_details": (CUReligionDetails, False, 1),
    }


class PeriodRelatedDetailsSegment(Segment):
    """Specification of details relating to a period. """
    tag: str = "PER"
    schema: SegmentSchema = {
        "period_type_code_qualifier": (EPeriodTypeCodeQualifier, False, "an..3"),
        "period_detail": (CUPeriodDetail, False, 1),
    }


class ProductGroupInformationSegment(Segment):
    """To indicate the group in which a product belongs."""
    tag: str = "PGI"
    schema: SegmentSchema = {
        "product_group_type_code": (EProductGroupTypeCode, False, "an..3"),
        "product_group": (CUProductGroup, False, 1),
    }


class AdditionalProductIdSegment(Segment):
    """To specify additional or substitutional item identification codes."""
    tag: str = "PIA"
    schema: SegmentSchema = {
        "product_identifier_code_qualifier": (EProductIdentifierCodeQualifier, False, "an..3"),
        "item_number_identification": (CUItemNumberIdentification, False, 1),
        "item_number_identification1": (CUItemNumberIdentification, False, 1),
        "item_number_identification2": (CUItemNumberIdentification, False, 1),
        "item_number_identification3": (CUItemNumberIdentification, False, 1),
        "item_number_identification4": (CUItemNumberIdentification, False, 1),
    }


class PartyIdentificationSegment(Segment):
    """To specify information necessary to establish the identity of a party."""
    tag: str = "PNA"
    schema: SegmentSchema = {
        "party_function_code_qualifier": (EPartyFunctionCodeQualifier, False, "an..3"),
        "identification_number": (CUIdentificationNumber, False, 1),
        "party_identification_details": (CUPartyIdentificationDetails, False, 1),
        "name_type_code": (ENameTypeCode, False, "an..3"),
        "name_status_code": (ENameStatusCode, False, "an..3"),
        "name_component_details": (CUNameComponentDetails, False, 1),
        "name_component_details1": (CUNameComponentDetails, False, 1),
        "name_component_details2": (CUNameComponentDetails, False, 1),
        "name_component_details3": (CUNameComponentDetails, False, 1),
        "name_component_details4": (CUNameComponentDetails, False, 1),
        "action_code": (EActionCode, False, "an..3"),
    }


class PurposeOfConveyanceCallSegment(Segment):
    """To specify the purpose of the call of the conveyance."""
    tag: str = "POC"
    schema: SegmentSchema = {
        "purpose_of_conveyance_call": (CUPurposeOfConveyanceCall, False, 1),
    }


class ProcessIdentificationSegment(Segment):
    """To identify a process. """
    tag: str = "PRC"
    schema: SegmentSchema = {
        "process_type_and_description": (CUProcessTypeAndDescription, False, 1),
        "process_identification_details": (CUProcessIdentificationDetails, False, 1),
    }


class PriceDetailsSegment(Segment):
    """To specify price information. """
    tag: str = "PRI"
    schema: SegmentSchema = {
        "price_information": (CUPriceInformation, False, 1),
        "subline_item_price_change_operation_code": (ESublineItemPriceChangeOperationCode, False, "an..3"),
    }


class ProvisoDetailsSegment(Segment):
    """Details regarding the stipulation or limitation in a document."""
    tag: str = "PRV"
    schema: SegmentSchema = {
        "proviso_code_qualifier": (EProvisoCodeQualifier, False, "an..3"),
        "proviso_type": (CUProvisoType, False, 1),
        "proviso_calculation": (CUProvisoCalculation, False, 1),
    }


class PhysicalSampleDescriptionSegment(Segment):
    """To define the physical sample parameters associated with a test, resulting in discrete measurements."""
    tag: str = "PSD"
    schema: SegmentSchema = {
        "sample_process_step_code": (ESampleProcessStepCode, False, "an..3"),
        "sample_selection_method_code": (ESampleSelectionMethodCode, False, "an..3"),
        "frequency_details": (CUFrequencyDetails, False, 1),
        "sample_state_code": (ESampleStateCode, False, "an..3"),
        "sample_direction_code": (ESampleDirectionCode, False, "an..3"),
        "sample_location_details": (CUSampleLocationDetails, False, 1),
        "sample_location_details1": (CUSampleLocationDetails, False, 1),
        "sample_location_details2": (CUSampleLocationDetails, False, 1),
    }


class PrioritySegment(Segment):
    """The segment is used to communicate priority information."""
    tag: str = "PTY"
    schema: SegmentSchema = {
        "priority_type_code_qualifier": (EPriorityTypeCodeQualifier, False, "an..3"),
        "priority_details": (CUPriorityDetails, False, 1),
    }


class PaymentTermsSegment(Segment):
    """To specify the terms of payment. """
    tag: str = "PYT"
    schema: SegmentSchema = {
        "payment_terms_type_code_qualifier": (EPaymentTermsTypeCodeQualifier, False, "an..3"),
        "payment_terms": (CUPaymentTerms, False, 1),
        "event_time_reference_code": (EEventTimeReferenceCode, False, "an..3"),
        "terms_time_relation_code": (ETermsTimeRelationCode, False, "an..3"),
        "period_type_code": (EPeriodTypeCode, False, "an..3"),
        "period_count_quantity": (EPeriodCountQuantity, False, "n..3"),
    }


class QueryAndResponseSegment(Segment):
    """To provide a declaration in the form of a coded question and response."""
    tag: str = "QRS"
    schema: SegmentSchema = {
        "sector_area_identification_code_qualifier": (ESectorAreaIdentificationCodeQualifier, False, "an..3"),
        "question_details": (CUQuestionDetails, False, 1),
        "response_details": (CUResponseDetails, False, 1),
    }


class QuantitySegment(Segment):
    """To specify a pertinent quantity. """
    tag: str = "QTY"
    schema: SegmentSchema = {
        "quantity_details": (CUQuantityDetails, False, 1),
    }


class QualificationSegment(Segment):
    """To specify the qualification of a person. """
    tag: str = "QUA"
    schema: SegmentSchema = {
        "qualification_type_code_qualifier": (EQualificationTypeCodeQualifier, False, "an..3"),
        "qualification_classification": (CUQualificationClassification, False, 1),
    }


class QuantityVariancesSegment(Segment):
    """To specify item details relating to quantity variances."""
    tag: str = "QVR"
    schema: SegmentSchema = {
        "quantity_difference_information": (CUQuantityDifferenceInformation, False, 1),
        "discrepancy_nature_identification_code": (EDiscrepancyNatureIdentificationCode, False, "an..3"),
        "reason_for_change": (CUReasonForChange, False, 1),
    }


class RequirementsAndConditionsSegment(Segment):
    """To specify sector/subject requirements and conditions."""
    tag: str = "RCS"
    schema: SegmentSchema = {
        "sector_area_identification_code_qualifier": (ESectorAreaIdentificationCodeQualifier, False, "an..3"),
        "requirementcondition_identification": (CURequirementconditionIdentification, False, 1),
        "action_code": (EActionCode, False, "an..3"),
        "country_identifier": (ECountryIdentifier, False, "an..3"),
    }


class RelationshipSegment(Segment):
    """To identify relationships between objects. """
    tag: str = "REL"
    schema: SegmentSchema = {
        "relationship_type_code_qualifier": (ERelationshipTypeCodeQualifier, False, "an..3"),
        "relationship": (CURelationship, False, 1),
    }


class ReferenceSegment(Segment):
    """To specify a reference. """
    tag: str = "RFF"
    schema: SegmentSchema = {
        "reference": (CUReference, False, 1),
    }


class AccountingJournalIdentificationSegment(Segment):
    """To identify an accounting journal. """
    tag: str = "RJL"
    schema: SegmentSchema = {
        "accounting_journal_identification": (CUAccountingJournalIdentification, False, 1),
        "accounting_entry_type_details": (CUAccountingEntryTypeDetails, False, 1),
    }


class RangeDetailsSegment(Segment):
    """To identify a range. """
    tag: str = "RNG"
    schema: SegmentSchema = {
        "range_type_code_qualifier": (ERangeTypeCodeQualifier, False, "an..3"),
        "range": (CURange, False, 1),
    }


class RiskObjectTypeSegment(Segment):
    """To identify a type of object at risk. """
    tag: str = "ROD"
    schema: SegmentSchema = {
        "risk_object_type": (CURiskObjectType, False, 1),
        "risk_object_subtype": (CURiskObjectSubtype, False, 1),
    }


class ResultSegment(Segment):
    """To specify a discrete or non-discrete result as a value or value range."""
    tag: str = "RSL"
    schema: SegmentSchema = {
        "result_value_type_code_qualifier": (EResultValueTypeCodeQualifier, False, "an..3"),
        "result_representation_code": (EResultRepresentationCode, False, "an..3"),
        "result_details": (CUResultDetails, False, 1),
        "result_details1": (CUResultDetails, False, 1),
        "measurement_unit_details": (CUMeasurementUnitDetails, False, 1),
        "result_normalcy_code": (EResultNormalcyCode, False, "an..3"),
    }


class RateDetailsSegment(Segment):
    """To specify rate information. """
    tag: str = "RTE"
    schema: SegmentSchema = {
        "rate_details": (CURateDetails, False, 1),
        "status_description_code": (EStatusDescriptionCode, False, "an..3"),
    }


class RemunerationTypeIdentificationSegment(Segment):
    """Identification of a remuneration type. """
    tag: str = "SAL"
    schema: SegmentSchema = {
        "remuneration_type_identification": (CURemunerationTypeIdentification, False, 1),
    }


class SchedulingConditionsSegment(Segment):
    """To specify scheduling conditions. """
    tag: str = "SCC"
    schema: SegmentSchema = {
        "delivery_plan_commitment_level_code": (EDeliveryPlanCommitmentLevelCode, False, "an..3"),
        "delivery_instruction_code": (EDeliveryInstructionCode, False, "an..3"),
        "pattern_description": (CUPatternDescription, False, 1),
    }


class StructureComponentDefinitionSegment(Segment):
    """To specify a component of a data structure (e.g. an array or table). 010    7497 STRUCTURE COMPONENT FUNCTION CODE QUALIFIER                                  M    1 an..3"""
    tag: str = "SCD"
    schema: SegmentSchema = {
        "structure_component_identification": (CUStructureComponentIdentification, False, 1),
        "party_identification_details": (CUPartyIdentificationDetails, False, 1),
        "status_description_code": (EStatusDescriptionCode, False, "an..3"),
        "configuration_level_number": (EConfigurationLevelNumber, False, "n..2"),
        "position_identification": (CUPositionIdentification, False, 1),
        "characteristic_description": (CUCharacteristicDescription, False, 1),
    }


class SegmentIdentificationSegment(Segment):
    """To identify a segment and give its class and maintenance operation."""
    tag: str = "SEG"
    schema: SegmentSchema = {
        "segment_tag_identifier": (ESegmentTagIdentifier, False, "an..3"),
        "designated_class_code": (EDesignatedClassCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


class SealNumberSegment(Segment):
    """To specify the seal number or a range of seal numbers."""
    tag: str = "SEL"
    schema: SegmentSchema = {
        "transport_unit_seal_identifier": (ETransportUnitSealIdentifier, False, "an..35"),
        "seal_issuer": (CUSealIssuer, False, 1),
        "seal_condition_code": (ESealConditionCode, False, "an..3"),
        "identity_number_range": (CUIdentityNumberRange, False, 1),
        "seal_type_code": (ESealTypeCode, False, "an..3"),
    }


class SequenceDetailsSegment(Segment):
    """To provide details relating to the sequence. """
    tag: str = "SEQ"
    schema: SegmentSchema = {
        "action_code": (EActionCode, False, "an..3"),
        "sequence_information": (CUSequenceInformation, False, 1),
    }


class SafetyInformationSegment(Segment):
    """To identify regulatory safety information. """
    tag: str = "SFI"
    schema: SegmentSchema = {
        "hierarchical_structure_level_identifier": (EHierarchicalStructureLevelIdentifier, False, "an..35"),
        "safety_section": (CUSafetySection, False, 1),
        "additional_safety_information": (CUAdditionalSafetyInformation, False, 1),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


class SplitGoodsPlacementSegment(Segment):
    """To specify the placement of goods in relation to equipment."""
    tag: str = "SGP"
    schema: SegmentSchema = {
        "equipment_identification": (CUEquipmentIdentification, False, 1),
        "package_quantity": (EPackageQuantity, False, "n..8"),
    }


class SegmentUsageDetailsSegment(Segment):
    """To specify the details of the usage of a segment within a message type structure."""
    tag: str = "SGU"
    schema: SegmentSchema = {
        "segment_tag_identifier": (ESegmentTagIdentifier, False, "an..3"),
        "requirement_designator_code": (ERequirementDesignatorCode, False, "an..3"),
        "occurrences_maximum_number": (EOccurrencesMaximumNumber, False, "n..7"),
        "level_number": (ELevelNumber, False, "n..3"),
        "sequence_position_identifier": (ESequencePositionIdentifier, False, "an..10"),
        "message_section_code": (EMessageSectionCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


class OrganisationClassificationDetailsSegment(Segment):
    """To provide classification details relating to the activities of an organisation."""
    tag: str = "SPR"
    schema: SegmentSchema = {
        "sector_area_identification_code_qualifier": (ESectorAreaIdentificationCodeQualifier, False, "an..3"),
        "organisation_classification_code": (EOrganisationClassificationCode, False, "an..3"),
        "organisation_classification_detail": (CUOrganisationClassificationDetail, False, 1),
    }


class SamplingParametersForSummaryStatisticsSegment(Segment):
    """To define the sampling parameters associated with summary statistics reported."""
    tag: str = "SPS"
    schema: SegmentSchema = {
        "frequency_details": (CUFrequencyDetails, False, 1),
        "confidence_percent": (EConfidencePercent, False, "n..6"),
        "size_details": (CUSizeDetails, False, 1),
        "size_details1": (CUSizeDetails, False, 1),
        "size_details2": (CUSizeDetails, False, 1),
        "size_details3": (CUSizeDetails, False, 1),
        "size_details4": (CUSizeDetails, False, 1),
    }


class StatisticsSegment(Segment):
    """To transmit summary statistics related to a specified collection of test result values."""
    tag: str = "STA"
    schema: SegmentSchema = {
        "statistic_type_code_qualifier": (EStatisticTypeCodeQualifier, False, "an..3"),
        "statistical_details": (CUStatisticalDetails, False, 1),
    }


class StatisticalConceptSegment(Segment):
    """To specify a statistical concept. """
    tag: str = "STC"
    schema: SegmentSchema = {
        "statistical_concept_identification": (CUStatisticalConceptIdentification, False, 1),
        "party_identification_details": (CUPartyIdentificationDetails, False, 1),
        "status_description_code": (EStatusDescriptionCode, False, "an..3"),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


class StagesSegment(Segment):
    """To provide information related to the kind of stage in a process, the number of stages and the actual stage."""
    tag: str = "STG"
    schema: SegmentSchema = {
        "process_stage_code_qualifier": (EProcessStageCodeQualifier, False, "an..3"),
        "process_stages_quantity": (EProcessStagesQuantity, False, "n..2"),
        "process_stages_actual_quantity": (EProcessStagesActualQuantity, False, "n..2"),
    }


class StatusSegment(Segment):
    """To specify the status of an object or service, including its category and the reason(s) for the status."""
    tag: str = "STS"
    schema: SegmentSchema = {
        "status_category": (CUStatusCategory, False, 1),
        "status": (CUStatus, False, 1),
        "status_reason": (CUStatusReason, False, 1),
        "status_reason1": (CUStatusReason, False, 1),
        "status_reason2": (CUStatusReason, False, 1),
        "status_reason3": (CUStatusReason, False, 1),
        "status_reason4": (CUStatusReason, False, 1),
    }


class DutytaxfeeDetailsSegment(Segment):
    """To specify relevant duty/tax/fee information. """
    tag: str = "TAX"
    schema: SegmentSchema = {
        "dutytaxfee_type": (CUDutytaxfeeType, False, 1),
        "dutytaxfee_account_detail": (CUDutytaxfeeAccountDetail, False, 1),
        "dutytaxfee_detail": (CUDutytaxfeeDetail, False, 1),
        "duty_or_tax_or_fee_category_code": (EDutyOrTaxOrFeeCategoryCode, False, "an..3"),
        "party_tax_identifier": (EPartyTaxIdentifier, False, "an..20"),
        "calculation_sequence_code": (ECalculationSequenceCode, False, "an..3"),
        "tax_or_duty_or_fee_payment_due_date_code": (ETaxOrDutyOrFeePaymentDueDateCode, False, "an..3"),
    }


class ChargerateCalculationsSegment(Segment):
    """To specify charges. """
    tag: str = "TCC"
    schema: SegmentSchema = {
        "charge": (CUCharge, False, 1),
        "ratetariff_class": (CURatetariffClass, False, 1),
        "commodityrate_detail": (CUCommodityrateDetail, False, 1),
        "ratetariff_class_detail": (CURatetariffClassDetail, False, 1),
    }


class TransportInformationSegment(Segment):
    """To specify information regarding the transport such as mode of transport, means of transport, its conveyance reference number and the identification of the means of transport."""
    tag: str = "TDT"
    schema: SegmentSchema = {
        "transport_stage_code_qualifier": (ETransportStageCodeQualifier, False, "an..3"),
        "means_of_transport_journey_identifier": (EMeansOfTransportJourneyIdentifier, False, "an..17"),
        "mode_of_transport": (CUModeOfTransport, False, 1),
        "transport_means": (CUTransportMeans, False, 1),
        "carrier": (CUCarrier, False, 1),
        "transit_direction_indicator_code": (ETransitDirectionIndicatorCode, False, "an..3"),
        "excess_transportation_information": (CUExcessTransportationInformation, False, 1),
        "transport_identification": (CUTransportIdentification, False, 1),
        "transport_means_ownership_indicator_code": (ETransportMeansOwnershipIndicatorCode, False, "an..3"),
        "power_type": (CUPowerType, False, 1),
        "transport_service": (CUTransportService, False, 1),
    }


class TestMethodSegment(Segment):
    """To describe the nature of the test performed. """
    tag: str = "TEM"
    schema: SegmentSchema = {
        "test_method": (CUTestMethod, False, 1),
        "test_administration_method_code": (ETestAdministrationMethodCode, False, "an..3"),
        "test_medium_code": (ETestMediumCode, False, "an..3"),
        "measurement_purpose_code_qualifier": (EMeasurementPurposeCodeQualifier, False, "an..3"),
        "test_method_revision_identifier": (ETestMethodRevisionIdentifier, False, "an..30"),
        "test_reason": (CUTestReason, False, 1),
    }


class TransportMovementDetailsSegment(Segment):
    """To specify operational transport movement details for a goods item or equipment (which may differ from the contractual conditions)."""
    tag: str = "TMD"
    schema: SegmentSchema = {
        "movement_type": (CUMovementType, False, 1),
        "equipment_plan_description": (EEquipmentPlanDescription, False, "an..26"),
        "haulage_arrangements_code": (EHaulageArrangementsCode, False, "an..3"),
    }


class TemperatureSegment(Segment):
    """To specify the temperature setting. """
    tag: str = "TMP"
    schema: SegmentSchema = {
        "temperature_type_code_qualifier": (ETemperatureTypeCodeQualifier, False, "an..3"),
        "temperature_setting": (CUTemperatureSetting, False, 1),
    }


class TermsOfDeliveryOrTransportSegment(Segment):
    """To specify terms of delivery or transport. """
    tag: str = "TOD"
    schema: SegmentSchema = {
        "delivery_or_transport_terms_function_code": (EDeliveryOrTransportTermsFunctionCode, False, "an..3"),
        "transport_charges_payment_method_code": (ETransportChargesPaymentMethodCode, False, "an..3"),
        "terms_of_delivery_or_transport": (CUTermsOfDeliveryOrTransport, False, 1),
    }


class TransportPlacementSegment(Segment):
    """To specify placement of goods or equipment in relation to the transport used. The segment serves as a pointer to the TDT segment group."""
    tag: str = "TPL"
    schema: SegmentSchema = {
        "transport_identification": (CUTransportIdentification, False, 1),
    }


class TechnicalRulesSegment(Segment):
    """A segment specifying technical rules. """
    tag: str = "TRU"
    schema: SegmentSchema = {
        "object_identifier": (EObjectIdentifier, False, "an..35"),
        "version_identifier": (EVersionIdentifier, False, "an..9"),
        "release_identifier": (EReleaseIdentifier, False, "an..9"),
        "rule_part_identifier": (ERulePartIdentifier, False, "an..7"),
        "code_list_responsible_agency_code": (ECodeListResponsibleAgencyCode, False, "an..3"),
    }


class TransportServiceRequirementsSegment(Segment):
    """To specify the contract and carriage conditions and service and priority requirements for the transport."""
    tag: str = "TSR"
    schema: SegmentSchema = {
        "contract_and_carriage_condition": (CUContractAndCarriageCondition, False, 1),
        "service": (CUService, False, 1),
        "transport_priority": (CUTransportPriority, False, 1),
        "nature_of_cargo": (CUNatureOfCargo, False, 1),
    }


class ValueListIdentificationSegment(Segment):
    """To identify a coded or non coded value list. """
    tag: str = "VLI"
    schema: SegmentSchema = {
        "value_list_identification": (CUValueListIdentification, False, 1),
        "party_identification_details": (CUPartyIdentificationDetails, False, 1),
        "status_description_code": (EStatusDescriptionCode, False, "an..3"),
        "value_list_name": (EValueListName, False, "an..70"),
        "designated_class_code": (EDesignatedClassCode, False, "an..3"),
        "value_list_type_code": (EValueListTypeCode, False, "an..3"),
        "characteristic_description": (CUCharacteristicDescription, False, 1),
        "maintenance_operation_code": (EMaintenanceOperationCode, False, "an..3"),
    }


__all__ = [
    'DataElementErrorIndicationSegment',
    'GroupResponseSegment',
    'InterchangeResponseSegment',
    'MessagepackageResponseSegment',
    'SegmentErrorIndicationSegment',
    'AnticollisionSegmentGroupHeaderSegment',
    'AnticollisionSegmentGroupTrailerSegment',
    'InteractiveInterchangeHeaderSegment',
    'InteractiveMessageHeaderSegment',
    'InteractiveStatusSegment',
    'InteractiveMessageTrailerSegment',
    'InteractiveInterchangeTrailerSegment',
    'InterchangeHeaderSegment',
    'GroupTrailerSegment',
    'GroupHeaderSegment',
    'MessageHeaderSegment',
    'ObjectHeaderSegment',
    'ObjectTrailerSegment',
    'SectionControlSegment',
    'MessageTrailerSegment',
    'InterchangeTrailerSegment',
    'SecurityAlgorithmSegment',
    'SecuredDataIdentificationSegment',
    'CertificateSegment',
    'DataEncryptionHeaderSegment',
    'SecurityMessageRelationSegment',
    'KeyManagementFunctionSegment',
    'SecurityHeaderSegment',
    'SecurityListStatusSegment',
    'SecurityResultSegment',
    'SecurityTrailerSegment',
    'DataEncryptionTrailerSegment',
    'SecurityReferencesSegment',
    'SecurityOnReferencesSegment',
    'AddressSegment',
    'AgreementIdentificationSegment',
    'AdjustmentDetailsSegment',
    'AllowanceOrChargeSegment',
    'AdditionalInformationSegment',
    'ApplicabilitySegment',
    'AdditionalPriceInformationSegment',
    'MonetaryAmountFunctionSegment',
    'ArrayInformationSegment',
    'ArrayStructureIdentificationSegment',
    'AttributeSegment',
    'AuthenticationResultSegment',
    'BasisSegment',
    'BeginningOfMessageSegment',
    'StructureIdentificationSegment',
    'BusinessFunctionSegment',
    'CharacteristicValueSegment',
    'CreditCoverDetailsSegment',
    'CharacteristicclassIdSegment',
    'PhysicalOrLogicalStateSegment',
    'CodeSetIdentificationSegment',
    'CodeValueDefinitionSegment',
    'ComputerEnvironmentDetailsSegment',
    'ClinicalInformationSegment',
    'ClauseIdentificationSegment',
    'ClinicalInterventionSegment',
    'CompositeDataElementIdentificationSegment',
    'ConsignmentInformationSegment',
    'ControlTotalSegment',
    'ComponentDetailsSegment',
    'CommunicationContactSegment',
    'ContributionDetailsSegment',
    'ChargePaymentInstructionsSegment',
    'ConsignmentPackingSequenceSegment',
    'AccountIdentificationSegment',
    'CustomsStatusOfGoodsSegment',
    'ContactInformationSegment',
    'CurrenciesSegment',
    'DamageSegment',
    'DefinitionFunctionSegment',
    'DangerousGoodsSegment',
    'DirectoryIdentificationSegment',
    'DimensionsSegment',
    'DocumentLineIdentificationSegment',
    'DeliveryLimitationsSegment',
    'DocumentmessageSummarySegment',
    'DocumentmessageDetailsSegment',
    'DataRepresentationDetailsSegment',
    'DosageAdministrationSegment',
    'DataSetIdentificationSegment',
    'DatetimeperiodSegment',
    'ExternalFileLinkIdentificationSegment',
    'SimpleDataElementDetailsSegment',
    'DataElementUsageDetailsSegment',
    'ElementValueDefinitionSegment',
    'EmploymentDetailsSegment',
    'AttachedEquipmentSegment',
    'EquipmentDetailsSegment',
    'NumberOfUnitsSegment',
    'ApplicationErrorInformationSegment',
    'ErrorPointDetailsSegment',
    'EventSegment',
    'FinancialChargesAllocationSegment',
    'FinancialInstitutionInformationSegment',
    'FootnoteSetSegment',
    'FootnoteSegment',
    'FormulaSegment',
    'FormulaSequenceSegment',
    'FreeTextSegment',
    'NatureOfCargoSegment',
    'ProcessingInformationSegment',
    'GoodsItemDetailsSegment',
    'GoodsIdentityNumberSegment',
    'RelatedIdentificationNumbersSegment',
    'GovernmentalRequirementsSegment',
    'GeographicalPositionSegment',
    'SegmentGroupUsageDetailsSegment',
    'HandlingInstructionsSegment',
    'HierarchyInformationSegment',
    'InsuranceCoverDescriptionSegment',
    'IdentitySegment',
    'InformationDetailSegment',
    'PersonCharacteristicSegment',
    'ItemDescriptionSegment',
    'IndexDetailsSegment',
    'PartiesAndInstructionSegment',
    'InventoryManagementRelatedDetailsSegment',
    'InformationRequiredSegment',
    'LanguageSegment',
    'LineItemSegment',
    'PlacelocationIdentificationSegment',
    'MeasurementsSegment',
    'MembershipDetailsSegment',
    'MarketsalesChannelInformationSegment',
    'MonetaryAmountSegment',
    'MessageTypeIdentificationSegment',
    'MaintenanceOperationDetailsSegment',
    'NameAndAddressSegment',
    'NationalitySegment',
    'PackageSegment',
    'PaymentInstructionsSegment',
    'AttendanceSegment',
    'PremiumCalculationComponentDetailsSegment',
    'PercentageDetailsSegment',
    'PackageIdentificationSegment',
    'PersonDemographicInformationSegment',
    'PeriodRelatedDetailsSegment',
    'ProductGroupInformationSegment',
    'AdditionalProductIdSegment',
    'PartyIdentificationSegment',
    'PurposeOfConveyanceCallSegment',
    'ProcessIdentificationSegment',
    'PriceDetailsSegment',
    'ProvisoDetailsSegment',
    'PhysicalSampleDescriptionSegment',
    'PrioritySegment',
    'PaymentTermsSegment',
    'QueryAndResponseSegment',
    'QuantitySegment',
    'QualificationSegment',
    'QuantityVariancesSegment',
    'RequirementsAndConditionsSegment',
    'RelationshipSegment',
    'ReferenceSegment',
    'AccountingJournalIdentificationSegment',
    'RangeDetailsSegment',
    'RiskObjectTypeSegment',
    'ResultSegment',
    'RateDetailsSegment',
    'RemunerationTypeIdentificationSegment',
    'SchedulingConditionsSegment',
    'StructureComponentDefinitionSegment',
    'SegmentIdentificationSegment',
    'SealNumberSegment',
    'SequenceDetailsSegment',
    'SafetyInformationSegment',
    'SplitGoodsPlacementSegment',
    'SegmentUsageDetailsSegment',
    'OrganisationClassificationDetailsSegment',
    'SamplingParametersForSummaryStatisticsSegment',
    'StatisticsSegment',
    'StatisticalConceptSegment',
    'StagesSegment',
    'StatusSegment',
    'DutytaxfeeDetailsSegment',
    'ChargerateCalculationsSegment',
    'TransportInformationSegment',
    'TestMethodSegment',
    'TransportMovementDetailsSegment',
    'TemperatureSegment',
    'TermsOfDeliveryOrTransportSegment',
    'TransportPlacementSegment',
    'TechnicalRulesSegment',
    'TransportServiceRequirementsSegment',
    'ValueListIdentificationSegment',
]
