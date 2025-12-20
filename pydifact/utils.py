import re


def get_syntax_release_version(version: str):
    """Returns the extended syntax version from a given version.

    E.g., when you pass "4", you get the newest release version "402".
    For version 1/2/3, it returns 100/200/300.
    """
    if version == "4":
        return "402"
    if re.match(r"^4\d{4}$", version):
        return version[0:3]

    return f"{version}00"
