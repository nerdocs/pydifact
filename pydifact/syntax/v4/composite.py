from pydifact.syntax.common.data import SyntaxVersionNumber
from pydifact.syntax.common.types import CompositeDataElement
import pydifact.syntax.v1.composite
import pydifact.syntax.v1.data
from pydifact.syntax.v4 import *


class CSyntaxIdentifier(v1.composite.CSyntaxIdentifier):
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
        (v1.data.SenderIdentification, M, "an..35"),
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
        (v1.data.Date, M, "n8"),  # CHANGED n6 to n8!!
        (v1.data.Time, M, "n4"),
    ]


class CRecipientReferencePassword(CompositeDataElement):
    code = "S005"
    schema = [
        (v1.data.RecipientReferencePassword, M, "an..14"),
        (v1.data.RecipientReferencePasswordQualifier, C, "an2"),
    ]
