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


class ParsingError(Exception):
    def __init__(
        self, message: str, file_name: str = "", line_number: int = 0, line: str = ""
    ):
        self.line_number = line_number
        self.line = line
        self.file_name = file_name
        if not line and not line_number:
            super().__init__(f"Parsing Error: {message}")
        super().__init__(
            f"Parsing Error in {file_name}:{line_number}: {message}\n'{line}'"
        )


# ---------------- Warnings ----------------
class MissingImplementationWarning(Warning):
    pass
