from pydifact.syntax.common import DataElement, Code


# There are a few `DataElement`s that are not part of EDIFACT directories, as they
# seem to be fixed for all of them, or have special purposes that can/should not be
# versioned (`SyntaxVersionNumber`). They are defined here in one place.


class SyntaxVersionNumber(DataElement):
    """EDIFACT Syntax version number, as used in the UNB segment."""

    # we provide all version numbers here, as it does not make sense to only provide old
    # ones and have multiple versions of SyntaxVersionNumber. We have to decide anyway
    # which version we support, so we need the newest list.

    code: str = "0002"
    repr: str = "an1"
    title: str = "Syntax version number"
    codes = {
        "1": Code(
            name="Version 1",
            description="ISO 9735:1988.",
        ),
        "2": Code(
            name="Version 2",
            description="ISO 9735:1988 (amended and reprinted in 1990).",
        ),
        "3": Code(
            name="Version 3",
            description="ISO 9735:1988 and ISO 9735: 1988 / Amendment 1: 1992",
        ),
        "4": Code(
            name="Version 4",
            description="ISO 9735:1998 (all parts)",
        ),
    }
