# CREATE FEW FILES IN THE my_test_directory AFTER FIRST CODE RUN
from pathlib import Path

#Directory path (relative to script location, not cwd)
script_dir = Path(__file__).resolve().parent
directory_path = script_dir / 'my_test_directory'
print(type(directory_path))
print(Path.__subclasses__())

#Check if directory exists
if not directory_path.exists():
    #Create directory
    directory_path.mkdir()
    print("Directory was created:", directory_path)
else:
    print("Directory already exists:", directory_path)

#Creating path to the file 
file_path = directory_path / 'my_file.txt'
#file_path = directory_path.joinpath('my_file.txt')
print("File path is:", file_path)


#Getting parent directory
parent_dir = file_path.parent
print("Parent directory: ", parent_dir)

#Checking if the file is file path or dir path
is_file = file_path.is_file()
is_dir = directory_path.is_dir()
print(f"File {file_path} exists:", is_file)
print(f"Directory {directory_path} is directory:", is_dir)

#Listing files in the directory

files = [file for file in directory_path.iterdir() if file.is_file()]
print("Files in the directory:", files)

#Removing files in directory
if directory_path.exists():
    files = [file for file in directory_path.iterdir() if file.is_file()]
    for file in files:
        file.unlink()
    directory_path.rmdir()
    print(f"Directory {directory_path} was removed")