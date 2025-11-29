import os
import sys

import requests


def is_prehistoric(release: str) -> bool:
    """Returns True if the release is pre-historic (<99)"""
    return release == "99A" or (release[:2].isdigit() and 80 < int(release[:2]) < 99)


def download_file(url, output_file_path: os.PathLike | str) -> bool:
    """Download a file from a URL and save it to a local file.

    Returns:
        True if the file was downloaded successfully, False if it already exists.
    Raises:
        RequestException: If the download fails.
    """
    if not os.path.exists(output_file_path):
        response = requests.get(url, stream=True)
        if response.status_code == 403:  # Forbidden
            print(
                f"Cound not download {url} to {output_file_path}, as it is "
                f"forbidden."
            )
            print("Maybe there is a captcha on the page.")
            print(
                "Please manually download the file and place it into the zips "
                "folder."
            )
            sys.exit(1)

        response.raise_for_status()  # check if the request was successful
        with open(output_file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
        return True

    print(f"{output_file_path} already exists. Skipping download.")
    return False
