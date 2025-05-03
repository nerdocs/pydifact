class EDISyntaxError(Exception):

    def __init__(
        self, message: str, line_number: int = None, column_number: int = None
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
