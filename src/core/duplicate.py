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


# Test
video_file_name = "[Nanatsu no Taizai AMV] It Has Begun - Starset.mp4"
video_file_path = os.path.join("../../tests", video_file_name)
print(get_file_hash(video_file_path))  # "c342ec81b9a40fcad970f8a6824732f37ea202fa5ff0ea1edd11a26a31a80143"
