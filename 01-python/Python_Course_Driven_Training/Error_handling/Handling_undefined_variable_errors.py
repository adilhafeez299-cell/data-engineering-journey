file = ''
try:
    file = open("file.txt", "r")
except FileNotFoundError as e:
    print(e)
else:
    print("File is ready for reading")
finally:
    if file and not file.closed:
       file.close()
       print("File was closed.")
       print(file.closed)
# file deleted
#name error 'file' not defined
# [Errno 2 No such file or directory: 'file.txt'