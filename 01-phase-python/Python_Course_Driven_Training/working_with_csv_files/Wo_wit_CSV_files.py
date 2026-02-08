import csv

# -------------- WRITE TO CSV (with custom delimiter)
with open('test.csv', 'w', newline = '') as csv_file:
    writer = csv.writer(csv_file, delimiter =';')

    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([123, 'Adil', 1999])
    writer.writerow([124, 'Chib', 2004])
    writer.writerow([126, 'Idris', 1988])


    #--------------------------------- READ FROM CSV --------------------------------------
with open('test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')

    for index, line in enumerate(reader):
        print(index, line)
        if index == 0:
             header = line
        else:
            for idx, val in enumerate(line):
                print(f"{header[idx]}:{val}")
