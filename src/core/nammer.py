import os
import re


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

    return new_name


# Test
print(clean_filename("une_video_[HD].mp4", "1080p"))  # "une video (1080p).mp4"
