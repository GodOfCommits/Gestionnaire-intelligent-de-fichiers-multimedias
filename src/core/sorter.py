# src/core/sorter.py

import os
import shutil
from src.core.database import get_all_files, update_file_database
from src.utils.metadata_getter import get_metadata


def sort_files_by_metadata(directory_path):
    """
    Sort files into folders based on their metadata.

    Args:
        directory_path (str): The path to the directory containing the files.
    """
    update_file_database(directory_path)
    files = get_all_files()

    for file in files:
        file_title, file_authors, file_path = file[1], file[2], file[3]

        if metadata_type == 'creator':
            metadata_value = metadata[0][0]  # Get the creator from the metadata tuple
        elif metadata_type == 'title':
            metadata_value = metadata[1]  # Get the title from the metadata tuple
        else:
            raise ValueError("Invalid metadata type")

        # Create the directory if it doesn't exist
        dir_path = os.path.join(os.path.dirname(file_path), metadata_value)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Move the file to the corresponding directory
        shutil.move(file_path, os.path.join(dir_path, os.path.basename(file_path)))


# Example usage:
sort_files_by_metadata('creator')
