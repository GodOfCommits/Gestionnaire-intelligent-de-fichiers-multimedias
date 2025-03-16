# Define a dictionary to map keywords to categories
import os
import shutil

category_mapping = {
    'attack on titans': 'Attack on Titan',
    'aot': 'Attack on Titan',
    'shingeki no kyojin': 'Attack on Titan',
    'naruto': 'Naruto',
    'one piece': 'One Piece',
    # Add more mappings as needed
}


def categorize_video(title):
    """
    Categorize a video based on its title.
    """
    for keyword, category in category_mapping.items():
        if keyword.lower() in title.lower():
            return category
    return 'Unknown'


def organize_videos(videos):
    """
    Organize videos into folders based on their categories.
    """
    categorized_videos = {}
    for video in videos:
        category = categorize_video(video['title'])
        if category not in categorized_videos:
            categorized_videos[category] = []
        categorized_videos[category].append(video)

    # Create folders and move videos into them
    for category, videos in categorized_videos.items():
        folder_path = os.path.join('categories', category)
        os.makedirs(folder_path, exist_ok=True)
        for video in videos:
            shutil.move(video['file_path'], os.path.join(folder_path, os.path.basename(video['file_path'])))
