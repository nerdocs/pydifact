# commonly used constants and types in pydifact

EDI_DEFAULT_VERSION = "4"
EDI_DEFAULT_DIRECTORY = "d24a"
EDI_DEFAULT_SYNTAX = "UNOA"

# types
Element = str | list[str]
Elements = list[Element]

# Status
M = "M"  # Mandatory
C = "C"  # Conditional

service_segments = [
    "UCD",
    "UCF",
    "UCI",
    "UCM",
    "UCS",
    "UGH",
    "UGT",
    "UIB",
    "UIH",
    "UIR",
    "UIT",
    "UIZ",
    "UNB",
    "UNE",
    "UNG",
    "UNH",
    "UNO",
    "UNP",
    "UNS",
    "UNT",
    "UNZ",
    "USA",
    "USB",
    "USC",
    "USD",
    "USE",
    "USF",
    "USH",
    "USL",
    "USR",
    "UST",
    "USU",
    "USX",
    "USY",
    "TXT",
]
