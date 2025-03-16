import os

from src.core.scanner import scan_directory
from src.utils.hash_tools import get_file_hash


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

    return duplicates


# Tests
## Test detect_duplicates
print("Test detect_duplicates")
directory_name = "tests"
directoy_path = os.path.join("../../", directory_name)
print(detect_duplicates(scan_directory(directoy_path)))
# {'../../tests\\aDuplicateDirectory\\[Nanatsu no Taizai AMV] It Has Begun - Starset.mp4':
# '../../tests\\[Nanatsu no Taizai AMV] It Has Begun - Starset.mp4'}
