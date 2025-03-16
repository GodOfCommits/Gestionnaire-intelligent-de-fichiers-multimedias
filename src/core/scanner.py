import os

from src.core.duplicate import detect_duplicates
from src.utils.logger import log_info


def scan_directory(root_path):
    """
    Scans the directory and returns the list of files
    """
    files = []

    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            files.append(file_path)

    # TODO: show duplicates in the GUI
    # duplicates = detect_duplicates(files)
    # if duplicates:

    log_info(f"Scanned {len(files)} files.")
    return files
