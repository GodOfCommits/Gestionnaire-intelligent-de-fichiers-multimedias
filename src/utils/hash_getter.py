import hashlib
import os


def get_file_hash(file_path):
    """
    Returns the hash of the file
    """
    hasher = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()
