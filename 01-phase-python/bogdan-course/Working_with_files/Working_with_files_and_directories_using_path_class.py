# CREATE FEW FILES IN THE my_test_directory AFTER FIRST CODE RUN
from pathlib import Path

#Directory path
directory_path = Path('my_test_directory')
print(type(directory_path))
print(Path.__subclasses__())

#Check if directory exists
if not directory_path.exists():
    #Create directory
    directory_path.mkdir()
    print("Directory was created:", directory_path)
else:
    print("Directory already exists:", directory_path)

#creating path to the file
file_path = directory_path / 'my_file.txt'
#file_path = directory_path.joinpath('myfile.txt')
print("File path isL", file_path)

#Creating path to the file

