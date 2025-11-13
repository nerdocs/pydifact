import os
import requests

from pathlib import Path
from typing import Iterator

from bs4 import BeautifulSoup
from .constants import download_directory

last_file_path = Path("")


def _retrieve_or_get_cached_file(url: str, destination: Path | str) -> str:
    """Retrieve content from a URL or return cached file content if available."""

    global last_file_path
    file_path = download_directory / destination
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            # print(f"Using cached data for {destination} from {file_path}...")
            last_file_path = file_path
            return file.read()

    response = requests.get(url)
    if response.status_code == 200:
        print(f"Retrieved data for {destination} from {url}, saving {file_path}...")
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        os.makedirs(file_path.parent, exist_ok=True)
        with open(file_path, "w") as file:
            file.write(f"# Source: {url}")
            file.write(text)
            last_file_path = file_path
            return text
    else:
        print(f"Failed to retrieve data for {destination} from {url}")
        return ""


def to_class_name(name: str, prefix="", postfix="") -> str:
    """Returns a PascalCase version of the provided space separated string."""

    # remove certain characters
    for char in "-()&*@#$%^%+=[]{}|;:,.<>/?'":
        name = name.replace(char, "")
    return prefix + "".join(w.capitalize() for w in name.split()) + postfix


def to_identifier(name: str) -> str:
    """Converts a string with special chars into a valid Python identifier.

    Removes special characters and replaces spaces with underscores, etc.
    """

    for char in "-()&*@#$%^%+=[]{}|;:,.<>/?":
        name = name.replace(char, "")
    for char in " ":
        name = name.replace(char, "_")
    return name.lower()


def get_next_not_empty_line(lines: Iterator, line_number: int) -> tuple[str, int]:
    line = next(lines)
    line_number += 1
    while not line.strip():
        line = next(lines)
        line_number += 1
    return line, line_number


def processed_title(title: str):
    """Processes the given title to a PascalCase version that can be used as class
    name.

    It takes care of special cases like special patterns that are part of some
    EDIFACT titles and must be processed before converting into a class name."""
    replacements = {"(undg)": "(UNDG)"}
    title = title.strip().lower().capitalize()
    for search, replacement in replacements.items():
        title = title.replace(search, replacement)
    return title
