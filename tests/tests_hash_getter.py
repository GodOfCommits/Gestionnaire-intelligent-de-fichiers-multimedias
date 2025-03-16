# Test
from src.utils.hash_getter import get_file_hash

aFile = "./data_test/[Nanatsu no Taizai AMV] It Has Begun - Starset.mp4"
get_file_hash(aFile)
print("Test get_file_hash for [Nanatsu no Taizai AMV] It Has Begun - Starset.mp4")
print("Expected : c342ec81b9a40fcad970f8a6824732f37ea202fa5ff0ea1edd11a26a31a80143")
print("Obtained : " + get_file_hash(aFile))
