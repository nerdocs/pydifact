from ..common.types import DataElement, Code

__version__ = 1


class SyntaxIdentifier(DataElement):
    code = "0001"
    title = "Syntax identifier"
    repr = "a4"
    codes = {
        "UNOA": Code(
            name="UN/ECE level A",
            description="Defined in ISO 646 basic code table with (exceptions) for "
            "lowercase letters, alternative graphic character allocations, and "
            "national/application-oriented allocations.",
        ),
        "UNOB": Code(
            name="UN/ECE level B",
            description="Defined in ISO 646 basic code table with exceptions for "
            "alternative graphic character allocations and "
            "national/application-oriented allocations.",
        ),
        "UNOC": Code(
            name="UN/ECE level C",
            description="Defined in ISO 8859-1: Information processing - Part 1: Latin alphabet No. 1.",
        ),
        "UNOD": Code(
            name="UN/ECE level D",
            description="Defined in ISO 8859-2: Information processing - Part 2: Latin alphabet No. 2.",
        ),
        "UNOE": Code(
            name="UN/ECE level E",
            description="Defined in ISO 8859-5: Information processing - Part 5: Latin/Cyrillic alphabet.",
        ),
        "UNOF": Code(
            name="UN/ECE level F",
            description="Defined in ISO 8859-7: Information processing - Part 7: Latin/Greek alphabet.",
        ),
    }
