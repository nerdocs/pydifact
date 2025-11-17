import logging
import os
import re
import shutil
import sys
import black
import requests

import pydifact.syntax
import zipfile
import io

from datetime import datetime
from typing import Iterable, Iterator
from pydifact.exceptions import ParsingError
from pydifact.utils import (
    syntax_versions_from_directory,
    directory_from_syntax_version,
    is_valid_syntax_directory,
)
from .constants import download_directory
from .helpers import (
    _retrieve_or_get_cached_file,
    get_next_not_empty_line,
    processed_title,
    to_identifier,
)
from .specs import (
    SegmentSpec,
    data_element_specs,
    composite_specs,
    segment_specs,
    message_specs,
    DataElementSpec,
    CompositeElementSpec,
    SegmentDataElementUsage,
    SegmentCompositeElementUsage,
    SegmentInlineDataElementUsage,
    CompositeDataElementUsage,
    source_specs,
    MessageSpec,
    MessageSegmentUsage,
    MessageGroupUsage,
)

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# edi_directory: str = ""
base_url = "https://service.unece.org/trade/untdid"


def parse_url(line: str) -> str:
    """Parses a line from the EDIFACT documentation and extracts the URL.

    Arguments:
        line: str, the line containing the URL, like "#   https://service.unece.org/..."

    Returns:
        str, the URL extracted from the line
    """
    pattern = re.match(r"^\s*#\s*#.*(https://service.unece.org/.*)+s*", line)
    return pattern.group(1) if pattern else ""


def parse_multiline_until(
    regex: re.Pattern[str] | str, lines: Iterator[str], line_number: int
) -> tuple[str, int, str]:
    """Parses a multiline comment block, which is stripped and combined into a single
    string.

    Arguments:
        regex (re.Pattern|str), the regular expression to match the next pattern. If
            pattern is found, the parsing stops and returns to the caller. If the
            pattern is "", the parsing stops at the next empty line.
        lines: Iterable[str], the lines of the EDIFACT documentation
        line_number: int, the current line number (will be returned increased)

    Returns:
        tuple[str, int, str], the title, the line number after the description, and the last line

    """
    desc_lines = []
    if isinstance(regex, str):
        regex = re.compile(regex)
    while True:
        line = next(lines)
        line_number += 1
        line = line.strip()
        if not line:  # empty line
            # if regex was empty, meaning we search until the next empty line, break
            if not regex.pattern:
                break
            continue
        if regex.pattern and regex.match(line):  # type: ignore
            break
        if line.startswith("-"):
            line = "\n" + line
        desc_lines.append(line)
    return " ".join(desc_lines), line_number, line


def read_service_file(version: int, file: str) -> str:
    if not file:
        return ""
    path = download_directory / "service" / str(version) / f"{file}"
    with open(path, "r", encoding="iso8859") as f:
        return f.read()


# ------------------ Data Elements ------------------


def download_service_zipfile(
    url: str,
    version: int,
    check_existing: str | list[str] | None = None,
) -> None:
    """Downloads a service file from the specified URL, extracts it, and stores it in a directory
    based on the provided version.

    Args:
        url: The URL to download the service file from.
        version: The version number used to determine the destination directory.
        check_existing: A list of filenames to verify existence in the destination directory.
            If not provided, all files are downloaded regardless.
    """
    if not url:
        return
    response = requests.get(url)
    response.raise_for_status()
    dest_dir = download_directory / "service" / str(version)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)
    if isinstance(check_existing, str):
        check_existing = [check_existing]
    if not check_existing:
        check_existing = []
    all_files_exist = True
    for filename in check_existing:
        if not os.path.exists(dest_dir / filename):
            all_files_exist = False
    if not all_files_exist or not check_existing:
        logger.info(f"Downloading service file from {url}...")
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall(dest_dir)


def ensure_composite_spec_exists(code: str, title: str, segment_tag: str):

    if code not in composite_specs:
        logger.info(
            f"While parsing '{segment_tag}' segment, referenced element {code} was not "
            f"listed in the "
            f"composite data element list. Creating stub entry."
        )
        composite_specs[code] = CompositeElementSpec(
            code=code,
            title=title,
            schema=[],
            description=f"STUB - This composite element was referenced in {segment_tag}"
            f".{code}, but not listed in the composite data element list.",
            stub=True,
        )


def ensure_data_element_spec_exists(code: str, title: str, segment_tag: str):
    if code not in data_element_specs:
        logger.info(
            f"While parsing '{segment_tag}' segment, referenced element {code} "
            f"was not listed in the "
            f"data element list. Creating stub entry."
        )
        data_element_specs[code] = DataElementSpec(
            code=code,
            title=title,
            repr_line="",
            description=f"STUB - This element was referenced first in {segment_tag}"
            f".{code}, but not listed in the data element list.",
            stub=True,
        )


def get_data_element_directory_desc(edi_directory: str) -> str:
    """Returns the data element description text for the EDIFACT EDED list.

    Attributes:
        edi_directory: The service directory where the segment is found, e.g. "d11a",
            "d24a", "d11b"
    """
    edi_directory = edi_directory.lower()
    file_name = directories_map[edi_directory]["e"]["index"]
    if not file_name:
        return ""
    file_path = download_directory / edi_directory / file_name
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    raise FileNotFoundError(
        f"The file '{file_name}' was not found in the directory '{file_path}'"
    )


# def parse_data_element_directory_desc(text):
#     """
#     Parse the data element list description from EDIFACT documentation.
#
#     This function processes a text containing the data element list
#     description, extracts the data element codes and titles, and stores them
#     in the global data_element_specs dictionary.
#
#     Args:
#         text (str): The raw text containing the data element list description.
#
#     Returns:
#         None: This function doesn't return a value, but updates the global
#         data_element_specs dictionary with the parsed data elements.
#
#     Note:
#         The function expects the input text to contain lines in the format:
#         "00010   UNH Message header                           M   1"
#         where the first 5 characters are the data element code, followed by
#         the title, and ending with [B], [C], or [I] (which is ignored).
#     """
#     lines = iter(text.strip().splitlines())
#     line_number = 0
#     while True:
#         try:
#             # skip all empty lines
#             line, line_number = get_next_not_empty_line(lines, line_number)
#             # find lines like this:
#             # 00010   UNH Message header                           M   1        [B]
#             # 00020   BGM Beginning of message                     M   1        [C]
#             if pattern := re.match(r"^[ +*#|X]{5}(\d{4})\s{2}(.*?)\s+\[[BCI]\]$", line):
#                 code, title = pattern.groups()
#                 if not code in data_element_specs:
#                     data_element_specs[code] = DataElementSpec(
#                         code=code, title=title, description="", repr_line="", stub=True
#                     )
#         except StopIteration:
#             break


# def get_data_element_desc(directory: str, code: str) -> str:
#     """Returns the description text for the provided data element.
#
#     Attributes:
#         directory: The service directory where the data element is found,
#                     e.g. "d11a", "d24a", "d11b"
#         code: The data element code as string, e.g. "1001"
#     """
#     # code must be convertible to an int.
#     assert int(code), "Invalid data element code"
#     return _retrieve_or_get_cached_file(
#         f"{base_url}/{directory.lower()}/tred/tred" f"{code}.htm",
#         f"{directory}/tred{code.lower()}.txt",
#     )


def read_file(edi_directory: str, file_name: str) -> str:
    """Returns the description text for the provided data element.

    Attributes:
        directory: The service directory where the data element is found,
                    e.g. "d11a", "d24a", "d11b"
        file_name: The name of the file containing the data element description.
    """
    global last_file_path
    file_path = download_directory / edi_directory / file_name
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            last_file_path = file_path
            return file.read()
    logger.warning(
        f"The file '{file_name}' was not found in the directory '{file_path}'"
    )
    return ""
    #     return _retrieve_or_get_cached_file(
    #     f"{base_url}/{directory.lower()}/tred/tred" f"{code}.htm",
    #     f"{directory}/tred{code.lower()}.txt",
    # )


# ------------------ Data Elements ------------------


def parse_data_elements_dir(text, only_one_code: str | None = None):
    """Parses a data element text (or list) and extracts the data element
    specification(s).

    Arguments:
        text: str, the raw text of the EDIFACT data element description
        only_one_code: str, the data element code, like "1001". If omitted, it parses all
        elements found in the text.
    """
    lines = iter(text.strip().splitlines())
    line_number = 0
    in_element = False
    in_description = False
    # if we should only parse one element, it must be (as a stub) in the cache before.
    if only_one_code:
        if only_one_code not in data_element_specs:
            raise KeyError(f"Data element {only_one_code} not found in the cache.")
        if not data_element_specs[only_one_code].stub:
            logger.warning(
                "Can't parse data element",
                only_one_code,
                "because it's already in the cache.",
            )
            return
        # get the item from the cache
        element = data_element_specs[only_one_code]
    else:
        # create an empty data element spec to start with
        element = DataElementSpec(
            code="", title="", description="", repr_line="", stub=False
        )
    while True:
        try:
            # skip all empty lines
            line, line_number = get_next_not_empty_line(lines, line_number)
            # first, if we parsed a description, it could be multiline, so check for
            # second/third line of desc., and if we find it, append it to description.
            if in_description and element.code:
                if pattern := re.match(r" {6,11}(.*?)$", line):
                    element.description += " " + pattern.group(1).strip()
                    continue
                else:
                    in_description = False

            if not in_element and not element.url:
                element.url = parse_url(line)

            # find lines like this:
            #      1000  Document name                                           [B]
            #   0007  Identification code qualifier
            # 8264 Means of transport                                     E    88.1
            # 8154 Unit load device size and type                         E(84)88.1
            if pattern := re.match(
                r"^[ +*#|X]*(\d{4})\s+(.*?)(?:\s+\[[BCI]\]|(E[\s(]+\d\d.*))?$", line
            ):
                code, title, _ = pattern.groups()
                title = processed_title(title)
                # if we should only parse ONE element, ignore all the others.
                if only_one_code:
                    if only_one_code != code:
                        continue
                    element.title = title
                    in_element = True
                else:
                    # New data element found!
                    # If there is already an old element, save it to the cache
                    # before creating a new one
                    if element.code:
                        # if (
                        #     element.code in data_element_specs
                        #     and data_element_specs[element.code].stub
                        # ):
                        data_element_specs[element.code] = element

                    # if the code is already in the list, we might have a title mismatch.
                    # don't set the title, as it is already taken from the global list
                    if code in data_element_specs and not data_element_specs[code].stub:
                        if not data_element_specs[code].title == title:
                            logger.warning(
                                f"{code} data element title mismatch: "
                                f"'{data_element_specs[code].title}' != '{title}'"
                            )  # TODO should be AFTER title and desc saving

                    # create a new element for the next cycle
                    element = DataElementSpec(
                        code=code, title=title, description="", repr_line="", stub=False
                    )
                    in_element = True
                    in_description = False
                    continue

            if in_element:
                # find lines like this:
                #      Desc: To identify an object.
                #           Desc: Goods item identification number.

                if pattern := re.match(r"^[ +*#|X]*Desc: (.*)$", line):
                    element.description = pattern.group(1)
                    in_description = True
                    continue
                # find lines like this:
                #      Repr: an..23
                # Repr: an..3                        Min: 1    Max: 3    Datatype: id
                if pattern := re.match(r"^[ +*#|X]*Repr: (.*?)(?:\s+Min.*)?$", line):
                    element.repr_line = pattern.group(1)
                    # after repr, we could stop processing to save time. Everything below
                    # this line is not needed anymore.
                    continue

                # possible ending codes
                if re.match(r"^\s+Data Element Cross Reference.*$", line):
                    # skip the rest of the file/description to avoid a textual mimikry
                    in_element = False
                    continue

            # TODO evtl. parse code values

        except StopIteration:
            break
        # save last constructed element

    if element.code:
        data_element_specs[element.code] = element


def parse_composite_dir(text, only_code: str | None = None):
    """Parses a composite data element text (or list) and extracts the data element
    specification(s)."""

    lines = iter(text.strip().splitlines())
    line_number = 0
    in_composite = False
    in_description = False
    if only_code:
        if only_code not in composite_specs:
            raise KeyError(f"Data element {only_code} not found in the cache.")
        if not composite_specs[only_code].stub:
            logger.warning(
                "Can't parse composite data element",
                only_code,
                "because it's already in the cache.",
            )
            return
    composite = CompositeElementSpec(
        code=only_code or "", title="", schema=[], stub=False
    )
    while True:
        try:
            # skip all empty lines
            line, line_number = get_next_not_empty_line(lines, line_number)
            # first, if we parsed a description, it could be multiline, so check for
            # second/third line of desc., and if we find it, append it to description.
            if in_description and composite.code:
                if pattern := re.match(r" {11,15}(.*?)$", line):
                    if "Cont:" not in pattern.group(1).strip():
                        composite.description += " " + pattern.group(1).strip()
                        continue
                in_description = False

            if not in_composite and not composite.url:
                composite.url = parse_url(line)

            # find header lines like this:
            #       C001 TRANSPORT MEANS
            #       S005  RECIPIENT REFERENCE/PASSWORD DETAILS
            #   C002     DOCUMENT
            #        C002 DOCUMENT/MESSAGE NAME
            if pattern := re.match(r"^[ +*#|X]+([A-Z]\d{3})\s+(.*?)$", line):
                code, title = pattern.groups()
                title = processed_title(title)
                if only_code:
                    if only_code != code:
                        continue
                    composite.title = title
                    # in_composite = True
                else:
                    if composite.code:
                        composite_specs[composite.code] = composite

                    # just check if the title matches with the one from the list.
                    if code in composite_specs and not composite_specs[code].stub:
                        if not composite_specs[code].title == title:
                            logger.warning(
                                f"{code} composite element title mismatch: "
                                f"'{composite_specs[code].title}' != {title}'"
                            )

                    composite = CompositeElementSpec(
                        code=code, title=title, schema=[], stub=False
                    )

                in_composite = True
                in_description = False
                continue

            if in_composite:
                # find Description patterns:
                # Desc: Code and/or name identifying the type of means of
                #       transport.
                if pattern := re.match(r"^[ +*#|X]+Desc: (.*)$", line):
                    composite.description = pattern.group(1).strip()
                    in_description = True
                    continue

                # find sub data element reference pattern like:
                # 010    8179  Transport means description code          C      an..8
                # 020    1131  Code list identification code             C      an..17
                #            Cont: 1154  Reference number             C  an..35 an 1 35
                #                  1156  Line number                  C  an..6  an 1  6

                if pattern := re.match(
                    r"^(\d{3})\s+(\d{4})\s+(.*?)\s+([MC])\s+([an]+\.?\.?\d+)\s*$", line
                ):
                    pos, code, title, mandatory, repr_line = pattern.groups()
                else:
                    if pattern := re.match(
                        r"\s{10,18}(?:Cont: )?(\d{4})\s+(.*?)\s+([MC])\s+([an.\d]+)",
                        line,
                    ):
                        code, title, mandatory, repr_line = pattern.groups()
                        # TODO: count and create POS manually
                        pos = "000"
                if pattern:
                    is_mandatory = mandatory == "M"
                    # if the data element is not there, create a stub entry
                    if code not in data_element_specs:
                        data_element_specs[code] = DataElementSpec(
                            code=code,
                            title=title,
                            stub=True,
                            repr_line="",
                            description="",
                        )
                    if (
                        not data_element_specs[code].stub
                        and title != data_element_specs[code].title
                    ):
                        logger.warning(
                            f"{composite.code}.{code} reference title does not match"
                            f" {code} title: "
                            f"'{title}' != '{data_element_specs[code].title}'"
                        )

                    # If repr_line is the same as in the data element description,
                    # we skip it in the tuple
                    entry = CompositeDataElementUsage(
                        pos, data_element_specs[code], is_mandatory, repr_line
                    )
                    composite.schema.append(entry)
                    continue
        except StopIteration:
            break
    if composite.code:
        composite_specs[composite.code] = composite


# ------------------ Segment ------------------


class SegmentParserState:
    """State management for segment parsing."""

    def __init__(self):
        self.in_composite = False
        self.in_segment = False
        self.multiline = False
        self.keep_next_line = False
        self.url = ""
        self.last_toplevel_element = None
        self.sub_elements = []

    def reset_for_new_segment(self):
        self.in_composite = False
        self.last_toplevel_element = None
        self.sub_elements = []


def parse_segment_title(line: str) -> tuple[str, str] | None:
    """Extract segment tag and title from a line.

    Returns:
        A tuple containing the segment tag and title, if found.
        None if the line does not match the expected format.
    """
    # find pattern for these title lines
    #       IDE  IDENTITY
    #      UCD    DATA ELEMENT ERROR INDICATION
    #      UGH    ANTI-COLLISION SEGMENT GROUP HEADER
    # ACT  ALTERNATIVE CURRENCY TOTAL AMOUNT                           88.1
    # ACA  ALTERNATIVE CURRENCY AMOUNT                            88.1
    # first check, if it generally matches a title line
    if not re.match(r"\s*[A-Z]{3}\s+[A-Z,-].*$", line):
        return None

    # Try syntax v4 trsd.* file pattern
    pattern = re.match(r"^[ +*#|X]{5,8}([A-Z]{3})\s+([A-Z,-].*)$", line)
    if not pattern:
        # try syntax v1 edsd.* file pattern
        pattern = re.match(r"^([A-Z]{3})\s+([A-Z,-].*)\s+(?:[\d.]{2,4})?$", line)

    if pattern:
        tag, title = pattern.groups()
        return tag, processed_title(title)
    return None


def parse_segment_description(
    lines: Iterator[str], line: str, line_number: int, segment: SegmentSpec
) -> tuple[int, str]:
    """Parse the (e.g. multiline) Function description of a segment.

    Returns:
        A tuple of:
            * New line number after parsing the Function description,
            * Function description
    """
    pattern = re.match(r"^\s+Function:\s(.*?)\s*$", line)
    if pattern:
        desc_firstline = pattern.group(1)
        # collect multiline description string until we find one of these patterns:
        # Pos   TAG   Name                                        S R   Repr.    Notes
        #     5463  ALLOWANCE OR CHARGE INDICATOR             M  an..3  id 1  3
        #     C275  ALTERNATIVE CURRENCY                      C
        # 010    C817 ADDRESS USAGE                              C    1
        desc, line_number, line = parse_multiline_until(
            r"^(?:Pos\s+TAG\s+Name\s+S\s+R\s+Repr.*|\d{3}[ +*#|X]+[A-Z\d]\d{3}\s+[\w "
            r"]+?\s{2,}|\s+[A-Z\d]\d{3}\s+[\w ]+?\s{2,}[MC]).*",
            lines,
            line_number,
        )
        segment.description = " ".join([desc_firstline, desc])
        return line_number, line
    return line_number, ""


def parse_toplevel_data_element(
    line: str, segment_tag: str
) -> SegmentDataElementUsage | None:
    """Parse a top-level data element line."""
    # Search for a start of a top level data element, like this:
    # 030    3164 CITY NAME                                  C    1 an..35
    match = re.match(
        r"^(\d{3})[ +*#|X]+(\d{4})\s+(.*?)\s{2,30}([MC])\s+(\d+)\s+([an]+\.?\.?\d+)(?:\s+[\d,]+|\s*)?$",
        line,
    )
    if not match:
        return None

    pos, code, title, mandatory, repeat, repr_line = match.groups()
    title = processed_title(title)
    ensure_data_element_spec_exists(code, title, segment_tag)

    if title != data_element_specs[code].title:
        logger.warning(
            f"{segment_tag}.{code} title mismatch: '{title}' != '{data_element_specs[code].title}'"
        )

    return SegmentDataElementUsage(
        pos=pos,
        element=data_element_specs[code],
        mandatory=mandatory == "M",
        repeat=int(repeat),
        repr_line=repr_line,
    )


def parse_toplevel_composite_element(
    line: str, segment_tag: str
) -> tuple[SegmentCompositeElementUsage, list] | None:
    """Parse a top-level composite element line."""
    # New start of a top level composite element, like this:
    # 060    C819 COUNTRY SUBDIVISION DETAILS                C    5
    match = re.match(
        r"^(\d{3})[ +*#|X]+([A-Z]\d{3})\s+(.*?)\s+([MC])\s+(\d+)(?:\s+[\d,]+|\s*)?$",
        line,
    )
    if not match:
        return None

    pos, code, title, mandatory, repeat = match.groups()
    ensure_composite_spec_exists(code, processed_title(title), segment_tag)

    sub_elements = []
    element = SegmentCompositeElementUsage(
        pos=pos,
        element=composite_specs[code],
        mandatory=mandatory == "M",
        repeat=int(repeat),
        schema=sub_elements,
    )
    return element, sub_elements


def parse_sub_element(
    line: str, lines_iter, segment_tag: str
) -> SegmentInlineDataElementUsage | None:
    """Parse a sub-element of a composite."""
    # Start of composite sub element line, like:
    #     3299  Address purpose code                      C      an..3
    #  +  3131  Address type code                         C      an..3
    #     5105  Monetary amount function detail
    #           description code                          C      an..17
    # first check if it looks similar to a data sub element ("startswith"...)

    # Check if line looks like a sub-element
    if not re.match(r"^[ +*#|X]+(\d{4})\s+(.+)$", line):
        return None

    # Handle multiline titles
    if not re.search(r"([MC])\s{2,}([an]+\.?\.?\d+)\s*$", line):
        line = line + " " + next(lines_iter).strip()

    match = re.match(
        r"^[ +*#|X]+(\d{4})\s+(.+)\s+([MC])\s{2,}([an]+\.?\.?\d+)\s*$",
        line,
    )
    if not match:
        return None

    code, title, mandatory, repr_line = match.groups()
    title = processed_title(title)
    ensure_data_element_spec_exists(code, title, segment_tag)

    if not data_element_specs[code].stub and title != data_element_specs[code].title:
        logger.warning(
            f"{segment_tag}.{code} title mismatch: '{title}' != '{data_element_specs[code].title}'"
        )

    return SegmentInlineDataElementUsage(
        element=data_element_specs[code],
        mandatory=mandatory == "M",
        repr_line=repr_line,
    )


def parse_segment_dir(text: str, only_segment_tag: str = ""):
    """Parses the description text containing one or more segments.

    Refactored version with better structure and separation of concerns.
    """
    if not text:
        return

    lines = iter(text.strip().splitlines())
    line_number = 0
    state = SegmentParserState()
    segment = SegmentSpec(tag="", title="", schema=[], url="")

    def save_current_segment():
        """Helper to save the current segment."""
        if not segment.tag:
            return

        # Save any pending top-level element first
        save_toplevel_element()

        if segment.tag in segment_specs:
            logger.warning(f"Segment {segment.tag} already in schema!")

        segment_specs[segment.tag] = segment

    def save_toplevel_element():
        """Helper to save the current top-level element."""
        if state.last_toplevel_element:
            segment.schema.append(state.last_toplevel_element)
            state.reset_for_new_segment()

    line = ""
    while True:
        try:
            if not state.keep_next_line:
                line, line_number = get_next_not_empty_line(lines, line_number)
            else:
                state.keep_next_line = False

            # Parse URL if not in segment yet
            if not state.in_segment and not state.in_composite and not state.url:
                state.url = parse_url(line)

            # ---------------------------- parse title ---------------------------------
            if title_match := parse_segment_title(line):
                tag, title = title_match

                # Save previous segment
                if state.in_segment:
                    save_current_segment()

                    # Stop if we only want one segment and found another
                    if only_segment_tag:
                        break

                # Create new segment
                segment = SegmentSpec(tag=tag, title=title, url=state.url, schema=[])
                state.reset_for_new_segment()
                state.in_segment = True
                continue

            if not state.in_segment:
                continue

            # Parse function description
            if re.match(r"^\s+Function:\s", line):
                line_number, line = parse_segment_description(
                    lines, line, line_number, segment
                )
                state.keep_next_line = True
                continue

            # ----------------------- top level data element ---------------------------
            if data_elem := parse_toplevel_data_element(line, segment.tag):
                save_toplevel_element()
                state.last_toplevel_element = data_elem
                state.in_composite = False
                continue

            # ------------------- top level composite data element ---------------------
            if composite_result := parse_toplevel_composite_element(line, segment.tag):
                save_toplevel_element()
                state.last_toplevel_element, state.sub_elements = composite_result
                state.in_composite = True
                continue

            # ------------------------- sub element of a composite----------------------
            if state.in_composite:
                if sub_elem := parse_sub_element(line, lines, segment.tag):
                    state.sub_elements.append(sub_elem)
                    continue

        except StopIteration:
            break

    # Save last segment
    save_current_segment()


# ------------------ Message ------------------


def get_message_directory_desc(directory: str) -> str:
    """Returns the URL for the service directory for messages.

    Attributes:
        directory: The service directory as lowercase string, e.g. "d11a",
            "d24a", "d11b"
    """
    return _retrieve_or_get_cached_file(
        f"{base_url}/{directory}/trmd/trmdi2.htm",
        f"{directory}/trmdi2.txt",
    )


def parse_message_directory_desc(text: str):
    """Creates a basic messages dict from the given raw EDIFACT message directory.

    It just fills tag and title of the messages, and leaves the schema yet empty.
    """
    lines = iter(text.strip().splitlines())
    while True:
        try:
            line = next(lines)
            if pattern := re.match(
                r"^[ +*|XR]{3}([A-Z]{6})\s((?:.*?(?:\n\s{10}.*?)*)?)\s+(\d+)\s+$", line
            ):
                tag, desc, _rev = pattern.groups()
                desc = desc.replace("\n", " ").strip()
                message_specs[tag] = MessageSpec(
                    tag=tag, title=desc, description="", schema={}, stub=True
                )
        except StopIteration:
            break
    return message_specs


def get_message_desc(directory: str, tag: str) -> str:
    """Returns the URL for the service directory for messages.

    Attributes:
        directory: The service directory as lowercase string, e.g. "d11a",
            "d24a", "d11b"
        tag: The message code as string, e.g. "ENTREC", "PRIHIS", ...
    """
    return _retrieve_or_get_cached_file(
        f"{base_url}/{directory}/trmd/" f"{tag.lower()}_c.htm",
        f"{directory}/trmd{tag.lower()}_c.txt",
    )


def parse_message_desc(text, tag: str) -> MessageSpec:
    """Parses a message text and extracts the message specification.

    It creates all used segments, if they are not existing yet, in segments
    Arguments:
        text: str, the raw text of the EDIFACT message description
        tag: str, the message code, like "APERAK"
    """
    pos_segment_line_re = re.compile(r"^(\d{5})(\s+)(.*)\s*$")

    lines = iter(text.strip().splitlines())
    line_number = 0
    message = message_specs[tag]
    group_parent: MessageGroupUsage | MessageSpec = message
    expected_indent_level = 0
    in_message = False
    stay_on_next_line = False
    while True:
        try:
            if stay_on_next_line:
                stay_on_next_line = False
            else:
                line, line_number = get_next_not_empty_line(lines, line_number)
            title = ""

            if not in_message:
                # find lines like this and collect sources:
                # SOURCE: TBG16 Entry Point
                if pattern := re.match(r"^SOURCE:\s+([A-Z0-9]+)\s+(.*)\s*$", line):
                    abbr, _title = pattern.groups()
                    if not abbr in source_specs:
                        source_specs[abbr] = title
                    message.source = abbr

                # find message type and check if we are parsing correct file:
                if pattern := re.match(r"^\s+Message Type\s?: (.*)\s*$", line):
                    if pattern.group(1) != tag:
                        raise ParsingError(
                            f"Message type '{pattern.group(1)}' in file does not "
                            f"match expected tag: '{tag}'"
                        )
                message.url = parse_url(line)

            if re.match(r".*\s+Segment index\s.*$", line):
                # after the message block, find key word and skip the rest
                break

            # find lines like this  with a pos{5} start:
            # 00130   BGM, Beginning of message
            # 00150      RFF, Reference
            # 00070   Segment group 1:  IND-RCS-SG2
            # 00100      Segment group 2:  FOO-BAR-BAZ
            # 00110         Foo, Foo Bar Baz
            segment_start = False
            group_start = False
            pos = number = members = ""
            if pattern := pos_segment_line_re.match(line):
                in_message = True
                pos, spaces, rest = pattern.groups()
                # the indent level is correct
                current_indent_level = (len(spaces) - 3) // 3
                if pattern := re.match(r"Segment group\s+(\d+):\s+(.*)", rest):
                    number, members = pattern.groups()
                    # members could be too long for a line, so make sure all are
                    # recognized.
                    while members.endswith("-"):
                        members = members + next(lines).strip()

                    _tag = f"SG{number}"
                    group_start = True
                elif pattern := re.match(r"^([A-Z]{3}),\s(.*)\s*$", rest):
                    _tag, title = pattern.groups()
                    segment_start = True
                else:
                    raise ParsingError(
                        f"Error parsing message '{message.tag}': Unexpected "
                        f"line {line_number}:\n"
                        f"'{line}'"
                    )

                # check indent level correctness, if there are open members to tick off
                if isinstance(group_parent, MessageGroupUsage) and group_parent.members:
                    # this must be the next expected member of the current group
                    expected = group_parent.members.pop(0)
                    if not _tag == expected:
                        raise ParsingError(
                            f"Wrong segment reference '{_tag}' in line "
                            f"{line_number} (expected '{expected}'):\n"
                            f"'{line}'"
                        )
                    assert len(spaces) == 3 + expected_indent_level * 3, (
                        f"Wrong indent level {current_indent_level} (expected "
                        f"{expected_indent_level}) for line {line_number} while parsing '{tag}' "
                        f"message:\n"
                        f"'{line}'"
                    )
                    while (
                        not group_start
                        and group_parent is not message
                        and len(group_parent.members) == 0  # type:ignore
                    ):
                        expected_indent_level -= 1
                        group_parent = group_parent.parent  # type:ignore

                # ----------------- New group detected! -----------------
            if group_start:
                # We found a group header!
                # Get segments list
                # ...and add a new group of segments that need to be parsed next
                new_schema: dict[str, MessageSegmentUsage | MessageGroupUsage] = {}

                group_parent = MessageGroupUsage(
                    pos=pos,
                    title=f"Segment group {number}",
                    schema=new_schema,
                    members=members.split("-"),
                    parent=group_parent,  # the former one, or None
                )
                desc, line_number, line = parse_multiline_until(
                    pos_segment_line_re, lines, line_number
                )
                stay_on_next_line = True
                # for _tag in members.split("-"):  # type:str
                #     new_schema[_tag] = {}
                # _tag = f"SG{number}"
                # new_schema[_tag] = current_usage

                # and increase the indent level

                expected_indent_level += 1

                # ----------------- New segment detected! -----------------
                # find lines like this:
                # 00020   BGM, Beginning of message
                # 00060      RFF, Reference
            elif segment_start:

                desc, line_number, line = parse_multiline_until(
                    pos_segment_line_re, lines, line_number
                )
                stay_on_next_line = True
                group_parent.schema[_tag] = MessageSegmentUsage(  # type:ignore
                    pos=pos,
                    element=segment_specs[_tag],
                    parent=group_parent,
                    description=desc,
                )

            else:
                _tag = ""

        except StopIteration:
            break

    return message


def file_header():
    return """# Copyright (c) 2017-{year} Christian González
# This file is licensed under the MIT license, see LICENSE file.

""".format(
        year=datetime.now().year
        # TODO:, date=datetime.now().strftime("%Y-%M-%d %H:%M:%S")
    )


def export_all(_list: Iterable):
    output = "\n\n__all__ = [\n"
    for element in _list:
        output += f"    '{element.class_name()}',\n"
        pass
    output += "]\n"
    return output


# TODO:  add this to string above:
#
# Generated at {date} by pydifact-generator from the official
# UN descriptions at service.unece.org.


def render_data_elements(edi_directory: str, with_imports=True) -> str:
    output = "# ------------------- Data Elements -------------------\n"
    output += "# created from EDED - the EDIFACT data elements directory\n\n"
    output += "# This file is auto-generated. Don't edit it manually.\n\n"
    output += file_header()

    if with_imports:
        output += "from pydifact.syntax.common.types import DataElement"

    for code, element in data_element_specs.items():
        logger.info(
            f"Creating DataElement class for "
            f"{edi_directory}.{element.code}: {element.class_name()}"
        )
        # TODO: element.description|wordwrap:73 - use django filter
        output += f"""

class {element.class_name()}(DataElement):
    \"\"\"{element.description}\"\"\" 
    code: str = "{element.code}"
    title: str = "{element.title}"
    repr_line: str = "{element.repr_line}"
"""

    output += export_all(data_element_specs.values())
    return black.format_str(output, mode=black.Mode())


def render_composite_elements(edi_directory: str, with_imports=True) -> str:
    output = "# ------------------- Composite Data Elements -------------------\n"
    output += "# created from EDCD - the EDIFACT composite data elements directory\n"
    output += "# This file is auto-generated. Don't edit it manually.\n\n"
    output += file_header()
    if with_imports:
        output += (
            "from pydifact.syntax.common.types import CompositeDataElement, "
            "CompositeSchemaEntryList\n"
        )
        # output += "from .data import (\n"
        # for data_spec in data_element_specs.values():  # type: DataElementSpec
        #     output += f"    {data_spec.class_name()},\n"
        # output += ")\n"
        output += "from .data import *\n"

    for code, spec in composite_specs.items():
        logger.info(
            f"Creating CompositeDataElement class for "
            f"{edi_directory}.{spec.code}: {spec.class_name()}"
        )
        output += f"class {spec.class_name()}(CompositeDataElement):\n"
        output += f'    """{spec.description}"""\n'
        output += f'    code: str = "{code}"\n'
        output += f'    title: str = "{spec.title}"\n'
        output += "    schema: CompositeSchemaEntryList = [\n"
        for entry in spec.schema:
            comment = ""
            if entry.element.repr_line and entry.element.repr_line != entry.repr_line:
                comment = f"  # DataElement uses: '{entry.element.repr_line}'"
            output += (
                f"({entry.element.class_name()}, {entry.mandatory}, "
                f'"{entry.repr_line}"),{comment}\n'
            )
        output += "]\n"

    output += export_all(composite_specs.values())
    return black.format_str(output, mode=black.Mode())


def render_segments(edi_directory: str, with_imports=True) -> str:

    output = "# ------------------- Segments -------------------\n"
    output += "# created from EDSD - the EDIFACT segments directory\n"
    output += "# This file is auto-generated. Don't edit it manually.\n\n"
    output += file_header()
    if with_imports:
        output += "from pydifact import Segment\n"
        # output += (
        #     "from pydifact.syntax.specs import SegmentCompositeSpec, "
        #     "SegmentDataElementSpec\n"
        # )
        output += "from pydifact.syntax.common.types import SegmentSchema\n"
        output += "from .data import *\n"
        output += "from .composite import *\n"
    for tag, segment_spec in segment_specs.items():
        output += f"\n\nclass {segment_spec.class_name()}(Segment):\n"
        if segment_spec.description:
            output += f'    """{segment_spec.description}"""\n'
        output += f'    tag: str = "{segment_spec.tag}"\n'
        output += "    schema: SegmentSchema = {\n"
        #    version: str = "{segment_spec.version}"
        # TODO: if local schema differs from global, make a hint as comment
        identifiers: list[str] = []
        for entry in segment_spec.schema:

            # prevent multiple identifiers with same name
            identifier = entry.identifier
            counter = 0
            while identifier in identifiers:
                counter += 1
                identifier = f"{entry.identifier}{counter}"
            identifiers.append(identifier)

            output += f'        "{identifier}": '
            if isinstance(entry, SegmentCompositeElementUsage):
                output += (
                    f"({entry.element.class_name()}, "
                    f"{entry.mandatory=='M'}, {entry.repeat}"
                )
                differs = False
                subschema_output = ",("
                if entry.schema:
                    for subschema in entry.schema:
                        comment = ""
                        if (
                            subschema.element.repr_line
                            and subschema.element.repr_line != subschema.repr_line
                        ):
                            differs = True
                            comment = f"  # orig: '{subschema.element.repr_line}'"
                        subschema_output += (
                            f"({subschema.element.class_name()},"
                            f" {subschema.mandatory=='M'}, '{subschema.repr_line}'),{comment}\n"
                        )
                subschema_output += "),"
                if differs:
                    output += subschema_output
                output += "),\n"

            elif isinstance(entry, SegmentDataElementUsage):
                output += (
                    f"({entry.element.class_name()}, "
                    f'{entry.mandatory=="M"}, "{entry.repr_line}"),\n'
                )
        output += "    }\n"
        logger.info(
            f"Creating Segment class for "
            f"{edi_directory}.{segment_spec.tag}: {segment_spec.class_name()}"
        )
    output += export_all(segment_specs.values())
    return output  # black.format_str(output, mode=black.Mode())


def render_messages_group(group: MessageGroupUsage, indent=0) -> str:
    output = ""
    for entry in group.schema:
        if isinstance(entry, MessageGroupUsage):
            output += f"{'    ' * indent}{render_messages_group(entry, indent + 1)},\n"
        elif isinstance(entry, MessageSegmentUsage):
            output += f"{'    ' * indent}{entry.element.class_name()},\n"
    return output


def render_messages(with_imports=True) -> str:

    output = "# ------------------- Messages -------------------\n"
    output += "# created from EDMD - the EDIFACT messages directory\n"
    output += "# This file is auto-generated. Don't edit it manually.\n\n"
    output += file_header()
    if with_imports:
        output += "from pydifact.segmentcollection import Message, MessageSchema\n"
        output += "from .data import *\n"
        output += "from .composite import *\n"
    for tag, message_spec in message_specs.items():
        output += f"""

class {message_spec.class_name()}(Message):\n
    tag: str = "{message_spec.tag}"
    schema: MessageSchema = """
        output += "{\n"
        #    version: str = "{segment_spec.version}"
        # TODO: if local schema differs from global, make a hint as comment
        identifiers: list[str] = []
        for segment_tag, entry in message_spec.schema.items():

            # prevent multiple identifiers with same name
            identifier = entry.identifier
            counter = 0
            while identifier in identifiers:
                counter += 1
                identifier = f"{entry.identifier}{counter}"
            identifiers.append(identifier)

            output += f'        "{identifier}": '
            if isinstance(entry, MessageGroupUsage):
                output += render_messages_group(entry, 1)

            elif isinstance(entry, SegmentDataElementUsage):
                output += (
                    f"({entry.element.class_name()}, "
                    f'{entry.mandatory=="M"}, "{entry.repr_line}"),\n'
                )
            output += "),\n"

        output += "    }\n"

    output += export_all(message_specs.values())
    return output  # black.format_str(output, mode=black.Mode())


def write_python_code_to_file(directory: str, filename: str, content: str):
    global last_file_path
    # get path of pydifact.syntax module
    dirname = os.path.join(
        os.path.dirname(pydifact.syntax.__file__), to_identifier(directory)
    )
    os.makedirs(dirname, exist_ok=True)
    # if __init__.py does not exis, create it
    init_file = os.path.join(dirname, "__init__.py")
    if not os.path.exists(init_file):
        with open(init_file, "w", encoding="utf-8") as f:
            f.write("")
    current_file = os.path.join(dirname, filename)
    with open(current_file, "w", encoding="utf-8") as f:
        f.write(content)


def print_usage():
    print("Usage: pydifact-generator [version] [directory]")
    print("Parses online UNECE EDIFACT directory and generates Python classes from it.")
    print(
        "This program is NOT intended for end users, it is aimed at pydifact "
        "developers, as it modifies the pydifact source code.\n"
    )
    print("Attributes:")
    print(
        "    version         Optional EDIFACT syntax version number (1-4). If provided,\n"
        "                    it must match a corresponding directory."
    )
    print(
        "    directory       The EDIFACT directory to download spec descriptions "
        "                    from, e.g. d24a, d11b, 90-1 etc."
    )
    print(
        "                    If both (syntax version and directory) are provided, "
        "                    they must be compatible to each other."
    )

    print("    --help|-h       Shows this message.")
    print("    --clear-cache   Clears the temporary directory and exits.")


# we need the GEFEG site as base url for downloading the service files
# that are not included in the EDI directories
# https://service.gefeg.com/jwg1/Archive/v3/data/v3.html
# https://service.gefeg.com/jwg1/Archive/v4x/data/v4x.html
services_v3v4_base_url = "https://service.gefeg.com/jwg1/Archive/"

services_map: dict[int, dict[str, dict[str, str | list[str]]]] = {
    1: {
        "e": {"url": "", "index": "", "list": ""},  # "Sded.s1",  TODO
        "c": {"url": "", "index": "", "list": ""},  # "Sced.s1",  TODO
        "s": {
            "url": "",
            "index": "",
            "list": "Ssed.s1",
        },
        "m": {"url": "", "index": "", "list": ""},  # "Smed.s1",  TODO
    },
    3: {
        # Service simple data element directory
        "e": {
            "url": services_v3v4_base_url + "v3/data/v3-sded.zip",
            "index": "Sdedi1.s3",  # "Sdedi2.s3"
            "list": "Sded.s3",
        },
        # Service composite data element directory
        "c": {
            "url": services_v3v4_base_url + "v3/data/v3-sced.zip",
            "index": "Scedi1.s3",  # "Scedi2.s3"
            "list": "Sced.s3",
        },
        # Service segment directory
        "s": {
            "url": services_v3v4_base_url + "v3/data/v3-ssed.zip",
            "index": "Ssedi1.s3",  # "Ssedi2.s3"
            "list": "Ssed.s3",
        },
        # Service message type directory
        "m": {
            "url": services_v3v4_base_url + "v3/data/v3-smed.zip",
            "index": "Smedi1.s3",  # "Smedi2.s3"
            "list": "Contrl.s3",
        },
        # # Service code lists directory
        # "cl": {
        #     "url": services_v3v4_base_url + "cl/data/unsl{directory}a.zip",
        #     "list": ["UNSL.{directory}.txt"],
        # },
    },
    4: {
        # Service simple data element directory
        "e": {
            "url": services_v3v4_base_url + "v4x/data/e40200.zip",
            "index": "Ne40200.txt",  # "Te40200.txt"
            "list": "Se40200.txt",
        },
        # Service composite data element directory
        "c": {
            "url": services_v3v4_base_url + "v4x/data/c40200.zip",
            "index": "Nc40200.txt",  # Tc40200.txt"
            "list": "Sc40200.txt",
        },
        # Service segment directory
        "s": {
            "url": services_v3v4_base_url + "v4x/data/s40200.zip",
            "index": "Ns40200.txt",  # "Ts40200.txt"
            "list": "Ss40200.txt",
        },
        # Service message type directory
        "m": {
            "url": services_v3v4_base_url + "v4x/data/m40200.zip",
            "index": "Nm40200.txt",  # "Tm40200.txt",
            "list": ["Autack_0.txt", "Contrl_1.txt", "Keyman_0.txt"],
        },
        # # Service code lists directory
        # "cl": {
        #     "url": services_v3v4_base_url + "cl/data/sl40219.zip",
        #     "list": "sl40219.txt",
        # },
    },
}

# This is a key-value map where the key is the edifact directory, and the value a
# list of files in this order:
# (e)lements, (c)omposite elements, (s)egments, (m)essages, (c)ode (l)ists.
directories_map: dict[str, dict[str, dict[str, str | list[str]]]] = {
    "90-1": {
        "e": {"index": "", "list": "EDED-901.ASC"},
        "c": {"index": "", "list": "EDCD-901.ASC"},
        "s": {"index": "", "list": "EDSD-901.ASC"},
        "m": {"index": "", "list": "EDMD-901.ASC"},
        "cl": {"list": "EDCL-901.ASC"},
    },
    "93-2": {
        "e": {"index": "", "list": "EDED.932"},
        "c": {"index": "", "list": "EDCD.932"},
        "s": {"index": "", "list": "EDSD.932"},
        "m": {"index": "", "list": "EDMD.932"},
        "cl": {"list": ["EDCL-1.932", "EDCL-2.932"]},
    },
    "d24a": {
        "e": {"index": "EDEDI1.24A", "list": "EDED.24A"},
        "c": {"index": "EDCD1.24A", "list": "EDCD.24A"},
        "s": {"index": "EDSDI1.24A", "list": "EDSD.24A"},
        "m": {"index": "EDMDI1.24A", "list": "EDMD.24A"},
        "cl": {"list": ["EDCL-1.932", "EDCL-2.932"]},
    },
}


def main():
    if len(sys.argv) not in (2, 3) or (sys.argv[1] in ["-h", "--help"]):
        print_usage()
        sys.exit(0)

    if sys.argv[1] == "--clear-cache":
        shutil.rmtree(download_directory, ignore_errors=True)
        sys.exit(0)

    if not os.path.exists(download_directory):
        os.mkdir(download_directory)

    # CLI accepts either <version> or <directory> or <version> <directory>

    # if only directory is given, auto-derive syntax version from it
    if len(sys.argv) == 2:
        if sys.argv[1] in ("1", "2", "3", "4"):
            syntax_version = int(sys.argv[1])
            # arg 1 is a syntax version number -> derive latest directory from it
            edi_directory = directory_from_syntax_version(syntax_version)
        else:
            # arg 1 is a directory str -> derive a syntax version from it
            edi_directory = sys.argv[1].lower()
            if not is_valid_syntax_directory(edi_directory):
                logger.error(f"Error: Invalid UN/EDIFACT directory: '{edi_directory}'")
                print_usage()
                sys.exit(1)
            syntax_version = syntax_versions_from_directory(edi_directory)[0]

        logger.info(
            f"Using EDI syntax version {syntax_version} for directory {edi_directory}"
        )

    # if both are given, perfect. Only check if they make sense.
    elif len(sys.argv) == 3:
        try:
            syntax_version = int(sys.argv[1])
        except ValueError:
            logger.error(f"Unknown syntax version: {sys.argv[1]}")
            print_usage()
            sys.exit(1)
        if syntax_version not in (1, 2, 3, 4):
            logger.error("Unsupported EDIFACT syntax version: %s", sys.argv[1])
            sys.exit(1)

        edi_directory = sys.argv[2].lower()
        possible_versions = syntax_versions_from_directory(edi_directory)
        if syntax_version not in possible_versions:
            logger.error(
                "Version mismatch: provided version %s does not match directory '%s' "
                "(detected: v%s)",
                syntax_version,
                edi_directory,
                possible_versions,
            )
            sys.exit(1)
    else:
        print_usage()
        sys.exit(1)

    if syntax_version not in services_map:
        logger.error(
            f"Unsupported EDIFACT syntax version '{edi_directory}': No service entry"
        )
        sys.exit(1)

    # first, download service files, as they are needed as the base for all others
    # There the UNB, UNE/UNH etc. base segments are defined.
    for _type, dct in services_map[syntax_version].items():
        download_service_zipfile(
            url=dct["url"],
            version=syntax_version,
            check_existing=dct["list"],
        )

    try:
        # ------------- Service elements -------------
        # Service Data Elements
        parse_data_elements_dir(
            read_service_file(syntax_version, services_map[syntax_version]["e"]["list"])
        )  # e.g. Se40200.txt

        # Service Composite Data Elements
        parse_composite_dir(
            read_service_file(syntax_version, services_map[syntax_version]["c"]["list"])
        )  # e.g.Sc40200.txt

        # Service Segments
        parse_segment_dir(
            read_service_file(syntax_version, services_map[syntax_version]["s"]["list"])
        )  # e.g. "Ss40200.txt"

        # ------------- User elements -------------
        if not os.path.exists(download_directory / edi_directory.lower()):
            logger.error(
                f"No downloaded directory '{edi_directory.lower()}' found.\n"
                "Please go to https://unece.org/trade/uncefact/unedifact/download, "
                f"download and extract all contents of the '{edi_directory}' "
                f"zip file manually into the following directory:\n"
                f"'{download_directory / edi_directory.lower()}'"
            )
            sys.exit(1)

        # Data Elements
        parse_data_elements_dir(
            read_file(edi_directory, directories_map[edi_directory]["e"]["list"])
        )
        # Composite Data Elements
        parse_composite_dir(
            read_file(edi_directory, directories_map[edi_directory]["c"]["list"]),
        )

        # Segments
        parse_segment_dir(
            read_file(edi_directory, directories_map[edi_directory]["s"]["list"])
        )  # e.g. Ss40200.txt

        # Messages
        parse_message_directory_desc(get_message_directory_desc(edi_directory))
        for _tag in message_specs:
            parse_message_desc(get_message_desc(edi_directory, _tag), _tag)

    except ParsingError as e:
        raise ParsingError(
            f"Error parsing EDIFACT directory '{edi_directory}' in "
            f"file '{last_file_path}':\n{e}"
        )

    write_python_code_to_file(
        edi_directory,
        "data.py",
        render_data_elements(edi_directory),
    )
    write_python_code_to_file(
        edi_directory,
        "composite.py",
        render_composite_elements(edi_directory),
    )
    write_python_code_to_file(
        edi_directory,
        "segments.py",
        render_segments(edi_directory),
    )
    write_python_code_to_file(
        edi_directory,
        "messages.py",
        render_messages(edi_directory),
    )


# TODO: EDCL - the EDIFACT codes list directory

if __name__ == "__main__":
    main()
