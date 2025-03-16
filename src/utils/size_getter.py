import os


def calculate_size(file_path):
    """Returns the size of the file in Gb, Mb, or Kb based on the file size."""
    file_size = os.path.getsize(file_path)

    if file_size >= 1024 * 1024 * 1024:
        return f"{file_size / (1024 * 1024 * 1024):.2f} GB"
    elif file_size >= 1024 * 1024:
        return f"{file_size / (1024 * 1024):.2f} MB"
    else:
        return f"{file_size / 1024:.2f} KB"
