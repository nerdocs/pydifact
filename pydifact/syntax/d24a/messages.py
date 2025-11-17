# ------------------- Messages -------------------
# created from EDMD - the EDIFACT messages directory
# This file is auto-generated. Don't edit it manually.

# Copyright (c) 2017-2025 Christian González
# This file is licensed under the MIT license, see LICENSE file.

from pydifact.segmentcollection import Message, MessageSchema
from .data import *
from .composite import *


class AccountingEntriesMessage(Message):

    tag: str = "ENTREC"
    schema: MessageSchema = {
    }


class AdviceOnPendingWorksMessage(Message):

    tag: str = "CONAPW"
    schema: MessageSchema = {
    }


class AnnouncementForReturnsMessage(Message):

    tag: str = "RETANN"
    schema: MessageSchema = {
    }


class ApplicationErrorAndAcknowledgementMessage(Message):

    tag: str = "APERAK"
    schema: MessageSchema = {
    }


class ArrivalNoticeMessage(Message):

    tag: str = "IFTMAN"
    schema: MessageSchema = {
    }


class AuthorizationMessage(Message):

    tag: str = "AUTHOR"
    schema: MessageSchema = {
    }


class BalanceMessage(Message):

    tag: str = "BALANC"
    schema: MessageSchema = {
    }


class BankingStatusMessage(Message):

    tag: str = "BANSTA"
    schema: MessageSchema = {
    }


class BerthManagementMessage(Message):

    tag: str = "BERMAN"
    schema: MessageSchema = {
    }


class BookingConfirmationMessage(Message):

    tag: str = "IFTMBC"
    schema: MessageSchema = {
    }


class BulkMarineInspectionSummaryReportMessage(Message):

    tag: str = "BMISRM"
    schema: MessageSchema = {
    }


class BusinessCreditReportMessage(Message):

    tag: str = "BUSCRD"
    schema: MessageSchema = {
    }


class CargoInsuranceClaimsMessage(Message):

    tag: str = "IFTICL"
    schema: MessageSchema = {
    }


class CargogoodsHandlingAndMovementMessage(Message):

    tag: str = "HANMOV"
    schema: MessageSchema = {
    }


class ChartOfAccountsMessage(Message):

    tag: str = "CHACCO"
    schema: MessageSchema = {
    }


class ClassificationInformationSetMessage(Message):

    tag: str = "CLASET"
    schema: MessageSchema = {
    }


class CommercialAccountSummaryMessage(Message):

    tag: str = "COACSU"
    schema: MessageSchema = {
    }


class CommercialDisputeMessage(Message):

    tag: str = "COMDIS"
    schema: MessageSchema = {
    }


class ConsignmentAdviceMessage(Message):

    tag: str = "IFTMCA"
    schema: MessageSchema = {
    }


class ContainerAnnouncementMessage(Message):

    tag: str = "COPARN"
    schema: MessageSchema = {
    }


class ContainerDischargeloadingOrderMessage(Message):

    tag: str = "COPRAR"
    schema: MessageSchema = {
    }


class ContainerDischargeloadingReportMessage(Message):

    tag: str = "COARRI"
    schema: MessageSchema = {
    }


class ContainerGateingateoutReportMessage(Message):

    tag: str = "CODECO"
    schema: MessageSchema = {
    }


class ContainerPrenotificationMessage(Message):

    tag: str = "COPINO"
    schema: MessageSchema = {
    }


class ContainerReleaseOrderMessage(Message):

    tag: str = "COREOR"
    schema: MessageSchema = {
    }


class ContainerSpecialHandlingOrderMessage(Message):

    tag: str = "COHAOR"
    schema: MessageSchema = {
    }


class ContainerStuffingstrippingOrderMessage(Message):

    tag: str = "COSTOR"
    schema: MessageSchema = {
    }


class ContractualConditionsMessage(Message):

    tag: str = "CNTCND"
    schema: MessageSchema = {
    }


class ContributionsForPayment(Message):

    tag: str = "COPAYM"
    schema: MessageSchema = {
    }


class CreditAdviceMessage(Message):

    tag: str = "CREADV"
    schema: MessageSchema = {
    }


class CreditRiskCoverMessage(Message):

    tag: str = "RECECO"
    schema: MessageSchema = {
    }


class CustomsCargoReportMessage(Message):

    tag: str = "CUSCAR"
    schema: MessageSchema = {
    }


class CustomsConveyanceReportMessage(Message):

    tag: str = "CUSREP"
    schema: MessageSchema = {
    }


class CustomsDeclarationMessage(Message):

    tag: str = "CUSDEC"
    schema: MessageSchema = {
    }


class CustomsExpressConsignmentDeclarationMessage(Message):

    tag: str = "CUSEXP"
    schema: MessageSchema = {
    }


class CustomsResponseMessage(Message):

    tag: str = "CUSRES"
    schema: MessageSchema = {
    }


class DangerousGoodsNotificationMessage(Message):

    tag: str = "IFTDGN"
    schema: MessageSchema = {
    }


class DangerousGoodsRecapitulationMessage(Message):

    tag: str = "DGRECA"
    schema: MessageSchema = {
    }


class DataMaintenanceRequestDefinitionMessage(Message):

    tag: str = "DMRDEF"
    schema: MessageSchema = {
    }


class DataMaintenanceStatusReportqueryMessage(Message):

    tag: str = "DMSTAT"
    schema: MessageSchema = {
    }


class DataPlotSheet(Message):

    tag: str = "DAPLOS"
    schema: MessageSchema = {
    }


class DebitAdviceMessage(Message):

    tag: str = "DEBADV"
    schema: MessageSchema = {
    }


class DebtsRecoveryMessage(Message):

    tag: str = "DEBREC"
    schema: MessageSchema = {
    }


class DeliveryJustInTimeMessage(Message):

    tag: str = "DELJIT"
    schema: MessageSchema = {
    }


class DeliveryScheduleMessage(Message):

    tag: str = "DELFOR"
    schema: MessageSchema = {
    }


class DespatchAdviceMessage(Message):

    tag: str = "DESADV"
    schema: MessageSchema = {
    }


class DirectBalanceOfPaymentDeclarationMessage(Message):

    tag: str = "BOPDIR"
    schema: MessageSchema = {
    }


class DirectDebitMessage(Message):

    tag: str = "DIRDEB"
    schema: MessageSchema = {
    }


class DirectPaymentValuationMessage(Message):

    tag: str = "CONDPV"
    schema: MessageSchema = {
    }


class DirectoryDefinitionMessage(Message):

    tag: str = "DIRDEF"
    schema: MessageSchema = {
    }


class DocumentaryCreditAdviceMessage(Message):

    tag: str = "DOCADV"
    schema: MessageSchema = {
    }


class DocumentaryCreditAmendmentInformationMessage(Message):

    tag: str = "DOCAMI"
    schema: MessageSchema = {
    }


class DocumentaryCreditApplicationMessage(Message):

    tag: str = "DOCAPP"
    schema: MessageSchema = {
    }


class DocumentaryCreditIssuanceInformationMessage(Message):

    tag: str = "DOCINF"
    schema: MessageSchema = {
    }


class DrawingAdministrationMessage(Message):

    tag: str = "CONDRA"
    schema: MessageSchema = {
    }


class DrawingOrganisationMessage(Message):

    tag: str = "CONDRO"
    schema: MessageSchema = {
    }


class EdiImplementationGuideDefinitionMessage(Message):

    tag: str = "IMPDEF"
    schema: MessageSchema = {
    }


class EnterpriseAccountingInformationMessage(Message):

    tag: str = "INFENT"
    schema: MessageSchema = {
    }


class EquipmentDamageAndRepairEstimateMessage(Message):

    tag: str = "DESTIM"
    schema: MessageSchema = {
    }


class EstablishmentOfContractMessage(Message):

    tag: str = "CONEST"
    schema: MessageSchema = {
    }


class ExtendedCreditAdviceMessage(Message):

    tag: str = "CREEXT"
    schema: MessageSchema = {
    }


class ExtendedPaymentOrderMessage(Message):

    tag: str = "PAYEXT"
    schema: MessageSchema = {
    }


class FinancialCancellationMessage(Message):

    tag: str = "FINCAN"
    schema: MessageSchema = {
    }


class FinancialStatementOfAnAccountMessage(Message):

    tag: str = "FINSTA"
    schema: MessageSchema = {
    }


class FirmBookingMessage(Message):

    tag: str = "IFTMBF"
    schema: MessageSchema = {
    }


class ForwardingAndConsolidationSummaryMessage(Message):

    tag: str = "IFCSUM"
    schema: MessageSchema = {
    }


class GeneralPurposeMessage(Message):

    tag: str = "GENRAL"
    schema: MessageSchema = {
    }


class GenericStatisticalMessage(Message):

    tag: str = "GESMES"
    schema: MessageSchema = {
    }


class GovernmentCrossBorderRegulatoryMessage(Message):

    tag: str = "GOVCBR"
    schema: MessageSchema = {
    }


class InTransitReportDetailMessage(Message):

    tag: str = "ITRRPT"
    schema: MessageSchema = {
    }


class InfrastructureConditionMessage(Message):

    tag: str = "INFCON"
    schema: MessageSchema = {
    }


class InspectionReportMessage(Message):

    tag: str = "INSRPT"
    schema: MessageSchema = {
    }


class InspectionRequestMessage(Message):

    tag: str = "INSREQ"
    schema: MessageSchema = {
    }


class InstructionContractStatusMessage(Message):

    tag: str = "IFTMCS"
    schema: MessageSchema = {
    }


class InstructionForReturnsMessage(Message):

    tag: str = "RETINS"
    schema: MessageSchema = {
    }


class InstructionMessage(Message):

    tag: str = "IFTMIN"
    schema: MessageSchema = {
    }


class InstructionToDespatchMessage(Message):

    tag: str = "INSDES"
    schema: MessageSchema = {
    }


class InsuranceClaimAssessmentAndReportingMessage(Message):

    tag: str = "ICASRP"
    schema: MessageSchema = {
    }


class InsuranceClaimSolicitorsInstructionMessage(Message):

    tag: str = "ICSOLI"
    schema: MessageSchema = {
    }


class InsurancePolicyAdministrationMessage(Message):

    tag: str = "IPPOAD"
    schema: MessageSchema = {
    }


class InsurancePremiumMessage(Message):

    tag: str = "INSPRE"
    schema: MessageSchema = {
    }


class InsurancePremiumPaymentMessage(Message):

    tag: str = "PRPAID"
    schema: MessageSchema = {
    }


class InternationalMultimodalStatusReportMessage(Message):

    tag: str = "IFTSTA"
    schema: MessageSchema = {
    }


class InternationalMultimodalStatusRequestMessage(Message):

    tag: str = "IFTSTQ"
    schema: MessageSchema = {
    }


class InventoryReportMessage(Message):

    tag: str = "INVRPT"
    schema: MessageSchema = {
    }


class InvitationToTenderMessage(Message):

    tag: str = "CONITT"
    schema: MessageSchema = {
    }


class InvoiceMessage(Message):

    tag: str = "INVOIC"
    schema: MessageSchema = {
    }


class JobApplicationProposalMessage(Message):

    tag: str = "JOBAPP"
    schema: MessageSchema = {
    }


class JobApplicationResultMessage(Message):

    tag: str = "JAPRES"
    schema: MessageSchema = {
    }


class JobInformationDemandMessage(Message):

    tag: str = "JINFDE"
    schema: MessageSchema = {
    }


class JobOrderConfirmationMessage(Message):

    tag: str = "JOBCON"
    schema: MessageSchema = {
    }


class JobOrderMessage(Message):

    tag: str = "JOBOFF"
    schema: MessageSchema = {
    }


class JobOrderModificationMessage(Message):

    tag: str = "JOBMOD"
    schema: MessageSchema = {
    }


class JustifiedPaymentRequestMessage(Message):

    tag: str = "JUPREQ"
    schema: MessageSchema = {
    }


class LedgerMessage(Message):

    tag: str = "LEDGER"
    schema: MessageSchema = {
    }


class LifeReinsuranceActivityMessage(Message):

    tag: str = "LREACT"
    schema: MessageSchema = {
    }


class LifeReinsuranceClaimsMessage(Message):

    tag: str = "LRECLM"
    schema: MessageSchema = {
    }


class MedicalPrescriptionMessage(Message):

    tag: str = "MEDPRE"
    schema: MessageSchema = {
    }


class MedicalResourceUsageAndCostMessage(Message):

    tag: str = "MEDRUC"
    schema: MessageSchema = {
    }


class MedicalServiceReportMessage(Message):

    tag: str = "MEDRPT"
    schema: MessageSchema = {
    }


class MedicalServiceRequestMessage(Message):

    tag: str = "MEDREQ"
    schema: MessageSchema = {
    }


class MeteredServicesConsumptionReportMessage(Message):

    tag: str = "MSCONS"
    schema: MessageSchema = {
    }


class ModificationOfIdentityDetailsMessage(Message):

    tag: str = "SSIMOD"
    schema: MessageSchema = {
    }


class MotorInsurancePolicyMessage(Message):

    tag: str = "IPPOMO"
    schema: MessageSchema = {
    }


class MultipleCreditAdviceMessage(Message):

    tag: str = "CREMUL"
    schema: MessageSchema = {
    }


class MultipleDebitAdviceMessage(Message):

    tag: str = "DEBMUL"
    schema: MessageSchema = {
    }


class MultipleInterbankFundsTransferMessage(Message):

    tag: str = "FINPAY"
    schema: MessageSchema = {
    }


class MultiplePaymentOrderMessage(Message):

    tag: str = "PAYMUL"
    schema: MessageSchema = {
    }


class NotificationOfRegistrationOfAWorkerMessage(Message):

    tag: str = "SSREGW"
    schema: MessageSchema = {
    }


class OrderStatusEnquiryMessage(Message):

    tag: str = "OSTENQ"
    schema: MessageSchema = {
    }


class OrderStatusReportMessage(Message):

    tag: str = "OSTRPT"
    schema: MessageSchema = {
    }


class PartyInformationMessage(Message):

    tag: str = "PARTIN"
    schema: MessageSchema = {
    }


class PassengerListMessage(Message):

    tag: str = "PAXLST"
    schema: MessageSchema = {
    }


class PaymentOrderMessage(Message):

    tag: str = "PAYORD"
    schema: MessageSchema = {
    }


class PaymentValuationMessage(Message):

    tag: str = "CONPVA"
    schema: MessageSchema = {
    }


class PayrollDeductionsAdviceMessage(Message):

    tag: str = "PAYDUC"
    schema: MessageSchema = {
    }


class PeriodicCustomsDeclarationMessage(Message):

    tag: str = "CUSPED"
    schema: MessageSchema = {
    }


class PermitExpirationclearanceReadyNoticeMessage(Message):

    tag: str = "CODENO"
    schema: MessageSchema = {
    }


class PersonIdentificationMessage(Message):

    tag: str = "MEDPID"
    schema: MessageSchema = {
    }


class PricesalesCatalogueMessage(Message):

    tag: str = "PRICAT"
    schema: MessageSchema = {
    }


class PricingHistoryMessage(Message):

    tag: str = "PRIHIS"
    schema: MessageSchema = {
    }


class ProductDataMessage(Message):

    tag: str = "PRODAT"
    schema: MessageSchema = {
    }


class ProductExchangeReconciliationMessage(Message):

    tag: str = "PRODEX"
    schema: MessageSchema = {
    }


class ProductInquiryMessage(Message):

    tag: str = "PROINQ"
    schema: MessageSchema = {
    }


class ProductServiceMessage(Message):

    tag: str = "PROSRV"
    schema: MessageSchema = {
    }


class ProjectCostReportingMessage(Message):

    tag: str = "PROCST"
    schema: MessageSchema = {
    }


class ProjectTasksPlanningMessage(Message):

    tag: str = "PROTAP"
    schema: MessageSchema = {
    }


class ProvisionalBookingMessage(Message):

    tag: str = "IFTMBP"
    schema: MessageSchema = {
    }


class PurchaseOrderChangeRequestMessage(Message):

    tag: str = "ORDCHG"
    schema: MessageSchema = {
    }


class PurchaseOrderMessage(Message):

    tag: str = "ORDERS"
    schema: MessageSchema = {
    }


class PurchaseOrderResponseMessage(Message):

    tag: str = "ORDRSP"
    schema: MessageSchema = {
    }


class QualityDataMessage(Message):

    tag: str = "QALITY"
    schema: MessageSchema = {
    }


class QuantityValuationMessage(Message):

    tag: str = "CONQVA"
    schema: MessageSchema = {
    }


class QuoteMessage(Message):

    tag: str = "QUOTES"
    schema: MessageSchema = {
    }


class RawDataReportingMessage(Message):

    tag: str = "RDRMES"
    schema: MessageSchema = {
    }


class ReceivingAdviceMessage(Message):

    tag: str = "RECADV"
    schema: MessageSchema = {
    }


class RegistrationOfEnterpriseMessage(Message):

    tag: str = "REGENT"
    schema: MessageSchema = {
    }


class ReinsuranceBordereauMessage(Message):

    tag: str = "REBORD"
    schema: MessageSchema = {
    }


class ReinsuranceCalculationMessage(Message):

    tag: str = "RECALC"
    schema: MessageSchema = {
    }


class ReinsuranceClaimsMessage(Message):

    tag: str = "RECLAM"
    schema: MessageSchema = {
    }


class ReinsuranceCoreDataMessage(Message):

    tag: str = "RECORD"
    schema: MessageSchema = {
    }


class ReinsurancePremiumMessage(Message):

    tag: str = "REPREM"
    schema: MessageSchema = {
    }


class ReinsuranceSettlementMessage(Message):

    tag: str = "RESETT"
    schema: MessageSchema = {
    }


class ReinsuranceTechnicalAccountMessage(Message):

    tag: str = "RETACC"
    schema: MessageSchema = {
    }


class ReinsuredObjectsListMessage(Message):

    tag: str = "RELIST"
    schema: MessageSchema = {
    }


class RemittanceAdviceMessage(Message):

    tag: str = "REMADV"
    schema: MessageSchema = {
    }


class RepairCallMessage(Message):

    tag: str = "RPCALL"
    schema: MessageSchema = {
    }


class RequestForADocumentaryCollectionMessage(Message):

    tag: str = "COLREQ"
    schema: MessageSchema = {
    }


class RequestForDocumentMessage(Message):

    tag: str = "REQDOC"
    schema: MessageSchema = {
    }


class RequestForQuoteMessage(Message):

    tag: str = "REQOTE"
    schema: MessageSchema = {
    }


class ReservationMessage(Message):

    tag: str = "RESMSG"
    schema: MessageSchema = {
    }


class ResponseOfPendingWorksMessage(Message):

    tag: str = "CONRPW"
    schema: MessageSchema = {
    }


class SafetyAndHazardDataMessage(Message):

    tag: str = "SAFHAZ"
    schema: MessageSchema = {
    }


class SalesDataReportMessage(Message):

    tag: str = "SLSRPT"
    schema: MessageSchema = {
    }


class SalesForecastMessage(Message):

    tag: str = "SLSFCT"
    schema: MessageSchema = {
    }


class SettlementTransactionReportingMessage(Message):

    tag: str = "STLRPT"
    schema: MessageSchema = {
    }


class SocialAdministrationMessage(Message):

    tag: str = "SOCADE"
    schema: MessageSchema = {
    }


class StatementOfAccountMessage(Message):

    tag: str = "STATAC"
    schema: MessageSchema = {
    }


class StowageInstructionMessage(Message):

    tag: str = "MOVINS"
    schema: MessageSchema = {
    }


class SuperannuationContributionsAdviceMessage(Message):

    tag: str = "SUPCOT"
    schema: MessageSchema = {
    }


class SuperannuationMaintenanceMessage(Message):

    tag: str = "SUPMAN"
    schema: MessageSchema = {
    }


class SupplierResponseMessage(Message):

    tag: str = "SUPRES"
    schema: MessageSchema = {
    }


class TankStatusReportMessage(Message):

    tag: str = "TANSTA"
    schema: MessageSchema = {
    }


class TaxControlMessage(Message):

    tag: str = "TAXCON"
    schema: MessageSchema = {
    }


class TenderMessage(Message):

    tag: str = "CONTEN"
    schema: MessageSchema = {
    }


class TerminalPerformanceMessage(Message):

    tag: str = "TPFREP"
    schema: MessageSchema = {
    }


class UtilitiesMasterDataMessage(Message):

    tag: str = "UTILMD"
    schema: MessageSchema = {
    }


class UtilitiesTimeSeriesMessage(Message):

    tag: str = "UTILTS"
    schema: MessageSchema = {
    }


class ValueAddedTaxMessage(Message):

    tag: str = "VATDEC"
    schema: MessageSchema = {
    }


class VerifiedGrossMassMessage(Message):

    tag: str = "VERMAS"
    schema: MessageSchema = {
    }


class VesselCallInformationMessage(Message):

    tag: str = "CALINF"
    schema: MessageSchema = {
    }


class VesselDepartureMessage(Message):

    tag: str = "VESDEP"
    schema: MessageSchema = {
    }


class WasteDisposalInformationMessage(Message):

    tag: str = "WASDIS"
    schema: MessageSchema = {
    }


class WorkGrantDecisionMessage(Message):

    tag: str = "WKGRDC"
    schema: MessageSchema = {
    }


class WorkGrantRequestMessage(Message):

    tag: str = "WKGRRE"
    schema: MessageSchema = {
    }


class WorkItemQuantityDeterminationMessage(Message):

    tag: str = "CONWQD"
    schema: MessageSchema = {
    }


class WorkersInsuranceHistoryMessage(Message):

    tag: str = "SSRECH"
    schema: MessageSchema = {
    }


__all__ = [
    'AccountingEntriesMessage',
    'AdviceOnPendingWorksMessage',
    'AnnouncementForReturnsMessage',
    'ApplicationErrorAndAcknowledgementMessage',
    'ArrivalNoticeMessage',
    'AuthorizationMessage',
    'BalanceMessage',
    'BankingStatusMessage',
    'BerthManagementMessage',
    'BookingConfirmationMessage',
    'BulkMarineInspectionSummaryReportMessage',
    'BusinessCreditReportMessage',
    'CargoInsuranceClaimsMessage',
    'CargogoodsHandlingAndMovementMessage',
    'ChartOfAccountsMessage',
    'ClassificationInformationSetMessage',
    'CommercialAccountSummaryMessage',
    'CommercialDisputeMessage',
    'ConsignmentAdviceMessage',
    'ContainerAnnouncementMessage',
    'ContainerDischargeloadingOrderMessage',
    'ContainerDischargeloadingReportMessage',
    'ContainerGateingateoutReportMessage',
    'ContainerPrenotificationMessage',
    'ContainerReleaseOrderMessage',
    'ContainerSpecialHandlingOrderMessage',
    'ContainerStuffingstrippingOrderMessage',
    'ContractualConditionsMessage',
    'ContributionsForPayment',
    'CreditAdviceMessage',
    'CreditRiskCoverMessage',
    'CustomsCargoReportMessage',
    'CustomsConveyanceReportMessage',
    'CustomsDeclarationMessage',
    'CustomsExpressConsignmentDeclarationMessage',
    'CustomsResponseMessage',
    'DangerousGoodsNotificationMessage',
    'DangerousGoodsRecapitulationMessage',
    'DataMaintenanceRequestDefinitionMessage',
    'DataMaintenanceStatusReportqueryMessage',
    'DataPlotSheet',
    'DebitAdviceMessage',
    'DebtsRecoveryMessage',
    'DeliveryJustInTimeMessage',
    'DeliveryScheduleMessage',
    'DespatchAdviceMessage',
    'DirectBalanceOfPaymentDeclarationMessage',
    'DirectDebitMessage',
    'DirectPaymentValuationMessage',
    'DirectoryDefinitionMessage',
    'DocumentaryCreditAdviceMessage',
    'DocumentaryCreditAmendmentInformationMessage',
    'DocumentaryCreditApplicationMessage',
    'DocumentaryCreditIssuanceInformationMessage',
    'DrawingAdministrationMessage',
    'DrawingOrganisationMessage',
    'EdiImplementationGuideDefinitionMessage',
    'EnterpriseAccountingInformationMessage',
    'EquipmentDamageAndRepairEstimateMessage',
    'EstablishmentOfContractMessage',
    'ExtendedCreditAdviceMessage',
    'ExtendedPaymentOrderMessage',
    'FinancialCancellationMessage',
    'FinancialStatementOfAnAccountMessage',
    'FirmBookingMessage',
    'ForwardingAndConsolidationSummaryMessage',
    'GeneralPurposeMessage',
    'GenericStatisticalMessage',
    'GovernmentCrossBorderRegulatoryMessage',
    'InTransitReportDetailMessage',
    'InfrastructureConditionMessage',
    'InspectionReportMessage',
    'InspectionRequestMessage',
    'InstructionContractStatusMessage',
    'InstructionForReturnsMessage',
    'InstructionMessage',
    'InstructionToDespatchMessage',
    'InsuranceClaimAssessmentAndReportingMessage',
    'InsuranceClaimSolicitorsInstructionMessage',
    'InsurancePolicyAdministrationMessage',
    'InsurancePremiumMessage',
    'InsurancePremiumPaymentMessage',
    'InternationalMultimodalStatusReportMessage',
    'InternationalMultimodalStatusRequestMessage',
    'InventoryReportMessage',
    'InvitationToTenderMessage',
    'InvoiceMessage',
    'JobApplicationProposalMessage',
    'JobApplicationResultMessage',
    'JobInformationDemandMessage',
    'JobOrderConfirmationMessage',
    'JobOrderMessage',
    'JobOrderModificationMessage',
    'JustifiedPaymentRequestMessage',
    'LedgerMessage',
    'LifeReinsuranceActivityMessage',
    'LifeReinsuranceClaimsMessage',
    'MedicalPrescriptionMessage',
    'MedicalResourceUsageAndCostMessage',
    'MedicalServiceReportMessage',
    'MedicalServiceRequestMessage',
    'MeteredServicesConsumptionReportMessage',
    'ModificationOfIdentityDetailsMessage',
    'MotorInsurancePolicyMessage',
    'MultipleCreditAdviceMessage',
    'MultipleDebitAdviceMessage',
    'MultipleInterbankFundsTransferMessage',
    'MultiplePaymentOrderMessage',
    'NotificationOfRegistrationOfAWorkerMessage',
    'OrderStatusEnquiryMessage',
    'OrderStatusReportMessage',
    'PartyInformationMessage',
    'PassengerListMessage',
    'PaymentOrderMessage',
    'PaymentValuationMessage',
    'PayrollDeductionsAdviceMessage',
    'PeriodicCustomsDeclarationMessage',
    'PermitExpirationclearanceReadyNoticeMessage',
    'PersonIdentificationMessage',
    'PricesalesCatalogueMessage',
    'PricingHistoryMessage',
    'ProductDataMessage',
    'ProductExchangeReconciliationMessage',
    'ProductInquiryMessage',
    'ProductServiceMessage',
    'ProjectCostReportingMessage',
    'ProjectTasksPlanningMessage',
    'ProvisionalBookingMessage',
    'PurchaseOrderChangeRequestMessage',
    'PurchaseOrderMessage',
    'PurchaseOrderResponseMessage',
    'QualityDataMessage',
    'QuantityValuationMessage',
    'QuoteMessage',
    'RawDataReportingMessage',
    'ReceivingAdviceMessage',
    'RegistrationOfEnterpriseMessage',
    'ReinsuranceBordereauMessage',
    'ReinsuranceCalculationMessage',
    'ReinsuranceClaimsMessage',
    'ReinsuranceCoreDataMessage',
    'ReinsurancePremiumMessage',
    'ReinsuranceSettlementMessage',
    'ReinsuranceTechnicalAccountMessage',
    'ReinsuredObjectsListMessage',
    'RemittanceAdviceMessage',
    'RepairCallMessage',
    'RequestForADocumentaryCollectionMessage',
    'RequestForDocumentMessage',
    'RequestForQuoteMessage',
    'ReservationMessage',
    'ResponseOfPendingWorksMessage',
    'SafetyAndHazardDataMessage',
    'SalesDataReportMessage',
    'SalesForecastMessage',
    'SettlementTransactionReportingMessage',
    'SocialAdministrationMessage',
    'StatementOfAccountMessage',
    'StowageInstructionMessage',
    'SuperannuationContributionsAdviceMessage',
    'SuperannuationMaintenanceMessage',
    'SupplierResponseMessage',
    'TankStatusReportMessage',
    'TaxControlMessage',
    'TenderMessage',
    'TerminalPerformanceMessage',
    'UtilitiesMasterDataMessage',
    'UtilitiesTimeSeriesMessage',
    'ValueAddedTaxMessage',
    'VerifiedGrossMassMessage',
    'VesselCallInformationMessage',
    'VesselDepartureMessage',
    'WasteDisposalInformationMessage',
    'WorkGrantDecisionMessage',
    'WorkGrantRequestMessage',
    'WorkItemQuantityDeterminationMessage',
    'WorkersInsuranceHistoryMessage',
]
