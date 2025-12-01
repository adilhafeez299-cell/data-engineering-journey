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
        # go over, get claude code to write out exercises for this example
