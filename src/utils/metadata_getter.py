import os
from mutagen.mp4 import MP4


def get_metadata(file_path):
    """Extract metadata from a file."""
    try:
        video_meta = MP4(file_path)
        title = video_meta.tags.get("\xa9nam")[0]
        authors = video_meta.tags.get("\xa9ART", [])

    except Exception:
        authors = []
        title = os.path.basename(file_path).split('.')[0]

    return authors, title


# Tests
## Test get_file_hash
print("Test get_file_hash")
video_file_name = "(AMV) Man of Steel - Skillet (720p).mp4"
video_file_path = os.path.join("../../tests", video_file_name)
print(get_metadata(video_file_path))
