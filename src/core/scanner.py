import os


def scan_directory(root_path):
    """
    Scans the directory and returns the list of files
    """
    files = []

    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            files.append(file_path)

    return files


# Test
print("Test scan_directory")
directory_name = "tests"
directoy_path = os.path.join("../../", directory_name)
print(scan_directory(directoy_path))
# ['../../tests\\[Nanatsu no Taizai AMV] It Has Begun - Starset.mp4',
# "../../tests\\aDirectory\\[Soul's Team IRON CHEF 09] Distorted Mind AMV (688p).mp4"]
