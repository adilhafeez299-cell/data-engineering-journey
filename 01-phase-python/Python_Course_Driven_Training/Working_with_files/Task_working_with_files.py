from pathlib import Path
import os

#create folders
files_dir = Path("Files")
files_dir.mkdir(exist_ok=True)

#File paths
file1 = files_dir / "file1.txt"
file2 = files_dir / "file2.txt"

#Write to first file
with open(file1, 'w') as file:
    file.write("First file - line one\n")
    file.write("First file - line two\n")

with open(file2, 'w') as file:
    file.write("Second file - line one\n")
    file.write("Second file - line two\n")

#Read All Lines from first file
# with open(file1) as file:
#     print(file.read())

with open(file1, "r") as file:
    lines = file.readlines()
print("First file lines:", lines)



#Read All Lines from second file
with open(file2, "r") as file:
    for line in file:
        print(line.strip())



#List directory contents:
dir_files = os.listdir(files_dir)
print(f"Files in the directory {files_dir}:")
print(dir_files)
for file in dir_files:
    print(file)

for path in files_dir.iterdir():
    if path.is_file():
        path.unlink()

if files_dir.exists():
    files_dir.rmdir()
    print("Directory removed successfully")
else:
    print("Directory does not exist",files_dir)

