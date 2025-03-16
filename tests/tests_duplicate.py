# Test
from src.core.duplicate import detect_duplicates

aFile = "./data_test/[Nanatsu no Taizai AMV] It Has Begun - Starset.mp4"
anotherSimilarFile = "./data_test/aDuplicateDirectory/[Nanatsu no Taizai AMV] It Has Begun - Starset.mp4"
yetAnotherFile = "./data_test/aDirectory/[Soul's Team IRON CHEF 09] Distorted Mind AMV (688p).mp4"

aBunchOfFiles = [aFile, anotherSimilarFile, yetAnotherFile]
print(f"Test detect_duplicate for {aBunchOfFiles}")
print(
    "Expected : {'./data_test/aDuplicateDirectory/[Nanatsu no Taizai AMV] It Has Begun - Starset.mp4': './data_test/[Nanatsu no Taizai AMV] It Has Begun - Starset.mp4'}")
print("Obtained : ", detect_duplicates(aBunchOfFiles))
