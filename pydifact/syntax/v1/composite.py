from pydifact.syntax.common.types import CompositeDataElement
from ..common.data import SyntaxVersionNumber
from .data import *


class CSyntaxIdentifier(CompositeDataElement):
    code = "S001"
    schema = [
        (SyntaxIdentifier, True, "a4"),
        (SyntaxVersionNumber, True, "n1"),
    ]


class CInterchangeSender(CompositeDataElement):
    code = "S002"
    schema = [
        (SenderIdentification, True, "an..35"),
        (IdentificationCodeQualifier, False, "an..4"),
        (AddressForReverseRouting, False, "an..14"),
    ]


class CInterchangeRecipient(CompositeDataElement):
    code = "S003"
    schema = [
        (RecipientIdentification, True, "an..35"),
        (IdentificationCodeQualifier, False, "an..4"),
        (RoutingAddress, False, "an..14"),
    ]


class CDateAndTimeOfPreparation(CompositeDataElement):
    code = "S004"
    schema = [
        (Date, True, "n6"),
        (Time, True, "n4"),
    ]


class CRecipientsReference(CompositeDataElement):
    code = "S005"
    schema = [
        (RecipientsReferencePassword, True, "an..14"),
        (RecipientsReferencePasswordQualifier, False, "an2"),
    ]
