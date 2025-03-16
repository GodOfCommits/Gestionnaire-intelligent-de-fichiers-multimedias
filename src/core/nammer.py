import os
import re

from src.utils.logger import log_info


def clean_filename(file_name, resolution):
    """
    Cleans the filename of any unwanted characters and adds the resolution to the end of the filename
    """
    name, ext = os.path.splitext(file_name)

    # Remplace special characters by whitespace
    name = re.sub(r"\[.*?\]|\(.*?\)|_", " ", name).strip()
    # Delete multiple whitespaces
    name = re.sub(r"\s+", " ", name)
    # Add resolution to the end of the filename
    new_name = f"{name} ({resolution}){ext}"

    log_info(f"File {name} has been renamed to {new_name}.")
    return new_name
