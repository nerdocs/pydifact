# commonly used constants and types in pydifact

EDI_DEFAULT_VERSION = 4
EDI_DEFAULT_SYNTAX_IDENTIFIER = "UNOA"
EDI_DEFAULT_DIRECTORY = "D24A"

# types
Element = str | list[str]
Elements = list[Element]

# Status
M = "M"  # Mandatory
C = "C"  # Conditional
