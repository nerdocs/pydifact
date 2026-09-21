class EDISyntaxError(Exception):
    def __init__(
        self,
        message: str,
        line_number: int | None = None,
        column_number: int | None = None,
    ):
        if line_number is not None and column_number is not None:
            super().__init__(
                f"EDIFACT Syntax Error: {message} (line {line_number}, column "
                f"{column_number})"
            )
        else:
            super().__init__(f"EDIFACT Syntax Error: {message}")


class ValidationError(Exception):
    pass


# ---------------- Warnings ----------------
class MissingImplementationWarning(Warning):
    pass


class NonConformantEDIWarning(Warning):
    """Emitted when pydifact accepts input that deviates from the EDIFACT
    specification (e.g. content in front of the UNA segment, an empty
    segment, or an empty mandatory element).

    Suppress it with a standard `warnings` filter; the parser's own warnings
    can also be switched off with `Parser(warn_non_conformant=False)`.
    """
