import os
import shutil

def get_files(directory):
    files = []

    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)

        if os.path.isfile(full_path):
            files.append(full_path)

    return files

# Test

result = get_files("C:/Users/hafea/OneDrive/Documents")
print(result)

def get_category(filepath):
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()  # add this line

    extension_map = {
        ".jpg": "Images",
        ".png": "Images",
        ".gif": "Images",
        ".pdf": "Documents",
        ".docx": "Documents",
        ".txt": "Documents",
        ".mp4": "Videos",
        ".mov": "Videos",
        ".zip": "Archives",
        ".tar": "Archives",
    }

    return extension_map.get(ext, "Other")

# #test
# print(get_category("photo.jpg"))
# print(get_category("report.PDF"))
# print(get_category("movie.mp4"))
# print(get_category("archive.zip"))
# print(get_category("random.xyz"))


def organize_files(directory):
    files = get_files(directory)

    for file in files:
        category = get_category(file)

        category_folder 




