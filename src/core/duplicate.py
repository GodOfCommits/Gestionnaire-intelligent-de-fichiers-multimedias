import os

from src.utils.hash_getter import get_file_hash
from src.utils.logger import log_info


def detect_duplicates(files):
    """
    Detects duplicate files in the list of files
    """
    duplicates = {}
    hashes = {}

    for file in files:
        file_hash = get_file_hash(file)

        if file_hash in hashes:
            duplicates[file] = hashes[file_hash]
        else:
            hashes[file_hash] = file

    log_info(f"Found {len(duplicates)} duplicates.")
    return duplicates
