from zipfile import ZipFile 
from pathlib import Path

files_dir = Path('my-files')
if not files_dir.exists():
    files_dir.mkdir()
    print(f"Directory {files_dir} was created")
else:
    print(f"Directory {files_dir} already exists")

with open(files_dir / 'first.txt', 'w') as file:
    file.write("This is the first file\n")

with open(files_dir / 'second.txt', 'w') as file:
    file.write("This is the second file\n")

with ZipFile('my-files.zip', mode='w') as zip_file:
    for file in files_dir.iterdir():  # iterates over directory
        print(file)
        zip_file.write(file)

with ZipFile('my-files.zip') as zip_file:
    # print(zip_file)
    # print(type(zip_file))
    # print(zip_file.infolist())
    zip_file.extractall()