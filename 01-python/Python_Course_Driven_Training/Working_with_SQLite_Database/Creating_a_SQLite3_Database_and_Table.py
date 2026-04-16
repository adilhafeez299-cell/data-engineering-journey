import sqlite3

DB_NAME = "courses.db"

# read records
with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty >= 30"
    sql_cursor = sqlite_conn.execute(sql_request)

    courses = sql_cursor.fetchall()
    print(courses)





# write multiple records

# courses = [
#     (456, "JS course", 235, 50),
#     (234, "Java course", 452, 20),
#     (567, "Node.js course", 753, 70)
# ]
#
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()
# go over again, query and code examples yourself

# Go over working with SQLlite Database again?
# Next week?
