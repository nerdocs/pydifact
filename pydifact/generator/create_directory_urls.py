import sys

import black
from bs4 import BeautifulSoup

# This file parses the https://unece.org/trade/uncefact/unedifact/download page
# and creates a dict of all the directories -> download URL of their zip files
# However, the URL is protected by a captcha and can't be parsed directly, so you
# have to manually download the HTML page and place it somewhere in your filesystem.
#
# This is a quick-and-dirty hack for generating the dict
#
#   pydifact.generator.downloads.directories_urls
#
# It is only used once while developing pydifact.
#
# Usage: python create_directory_urls.py path/to/download.html


BASE = "https://unece.org"


def list_dirs(html) -> dict[str, str]:
    with open(html, "r", encoding="utf-8") as r:
        soup = BeautifulSoup(r, "html.parser")
        links = soup.select("a[href*='/trade/untdid/']")
        dirs = {}
        for a in links:
            href = str(a.get("href", ""))
            # find parts like /untdid/d96a/
            if not href:
                print("empty href")
                continue

            if href.startswith("/"):
                href = f"{BASE}{href}"

            parts = href.split("/")
            zipfile = parts[-1]
            if not zipfile.endswith(".zip"):
                raise ValueError(f"Expected zip file, got {zipfile}")

            release = zipfile[:-4].replace(".", "").replace("-", "")
            if not release.startswith("d"):
                release = f"d{release}"

            if "untdid" in parts:
                idx = parts.index("untdid")
                if idx + 1 < len(parts):
                    dirs[release] = href
        return dirs


if __name__ == "__main__":
    dirs = list_dirs(sys.argv[1])
    print(dirs)
