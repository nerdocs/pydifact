import os
from pathlib import Path

# TODO: use os independent home temp directory
download_directory = Path(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "download"))
)
