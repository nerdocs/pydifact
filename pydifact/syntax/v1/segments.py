from pydifact import Segment, Characters
from pydifact.constants import C, M
from pydifact.syntax.common.data import ServiceStringAdvice
from . import __version__
from .composite import *
from .data import *


class UNASegment(Segment):
    """Service String Advice."""

    tag = "UNA"
    version = __version__
    schema = [
        (ServiceStringAdvice, C, 1),
    ]

    def __init__(self, characters: Characters | str):  # noqa
        super().__init__()
        # in this special case, we need no super class, as we directly set the
        # Character string
        if isinstance(characters, str):
            characters = Characters.from_str(characters)
        else:
            # in syntax version 1, the UNA segment is mandatory
            if not isinstance(characters, Characters):
                raise TypeError("characters must be a str or Characters object")

        self.elements = [str(characters)]
        # provide shortcut handles to the separators
        self.component_separator = characters.component_separator
        self.data_separator = characters.data_separator
        self.decimal_point = characters.decimal_point
        self.escape_character = characters.escape_character
        self.reserved_character = characters.reserved_character
        self.segment_terminator = characters.segment_terminator

    def validate(self) -> None:
        super().validate()

    def __str__(self):
        return "".join(
            [
                self.component_separator,
                self.data_separator,
                self.decimal_point,
                self.escape_character,
                self.reserved_character,
                self.segment_terminator,
            ]
        )


class UNBSegment(Segment):
    """Interchange header.

    To start, identify and specify an interchange."""

    tag = "UNB"
    version = __version__
    schema = {
        "syntax_identifier": (CSyntaxIdentifier, True, 1),
        "interchange_sender": (CInterchangeSender, True, 1),
        "interchange_recipient": (CInterchangeRecipient, True, 1),
        "date_time_preparation": (CDateAndTimeOfPreparation, True, 1),
        "interchange_control_reference": (InterchangeControlReference, True, "an..14"),
        "recipients_reference": (CRecipientsReference, False, 1),
        "application_reference": (ApplicationReference, False, "an..14"),
        "processing_priority_code": (ProcessingPriorityCode, False, "a1"),
        "acknowledgement_request": (AcknowledgementRequest, False, "n1"),
        "communication_agreement_id": (CommunicationAgreementID, False, "an..35"),
        "test_indicator": (TestIndicator, False, "n1"),
    }


class UNZSegment(Segment):
    """Interchange trailer.

    To end and check the completeness of an interchange."""

    tag = "UNZ"
    version = __version__
    schema = {
        "interchange_control_count": (InterchangeControlCount, True, "n..6"),
        "interchange_control_reference": (InterchangeControlReference, True, "an..14"),
    }


class UNGSegment(Segment):
    """Functional Group Header.

    To head, identify and specify a Functional Group."""

    tag = "UNG"
    version = __version__
    schema = {
        "functional_group_identification": (
            FunctionalGroupIdentification,
            True,
            "an..6",
        ),
        "application_senders_identification": (
            CApplicationSendersIdentification,
            True,
            1,
        ),
        "application_recipients_identification": (
            CApplicationRecipientsIdentification,
            True,
            1,
        ),
        "date_time_of_preparation": (CDateAndTimeOfPreparation, True, 1),
        "functional_group_reference_number": (
            FunctionalGroupReferenceNumber,
            True,
            "an..14",
        ),
        "controlling_agency": (ControllingAgency, True, "an..2"),
        "message_version": (CMessageVersion, True, 1),
        "application_password": (ApplicationPassword, False, "an..14"),
    }
