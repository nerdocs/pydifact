from pydifact import Segment, Characters
from pydifact.constants import C, M
from pydifact.syntax.common.data import ServiceStringAdvice
from . import __version__


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


# class UNBSegment(Segment):
#     """Interchange header.
#
#     To start, identify and specify an interchange."""
#
#     tag = "UNB"
#     version = __version__
#     schema = [
#         (CSyntaxIdentifier, M, 1),
#         (CInterchangeSender, M, 1),
#         (CInterchangeRecipient, M, 1),
#         (CDateAndTimeOfPreparation, M, 1),
#         (InterchangeControlReference, M, 1),
#         (CRecipientsReference, C, 1),
#         (ApplicationReference, C, 1, "an..14"),
#         (ProcessingPriorityCode, C, 1, "a1"),
#         (AcknowledgementRequest, C, 1, "n1"),
#         (CommunicationAgreementID, C, 1, "an..35"),
#         (TestIndicator, C, 1, "n1"),
#     ]
