from pathlib import Path

file_path = Path('my_file.txt')

with open(file_path, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")

with open(file_path) as file:
    print(file.read())
    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     print(line.strip())

with open(file_path, 'a') as file:
    file.write("Third line\n")

with open(file_path) as file:
    print(file.read())

if file_path.exists():
    file_path.unlink()
else:
    print("there is no file path to remove")



  #.readline for big files
  #.readlines for small files
