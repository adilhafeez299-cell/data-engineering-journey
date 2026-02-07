from datetime import datetime

formatted_datetime_str = "3000-11-20 14:25:45"
parsed_datetime = datetime.strptime(formatted_datetime_str, "%Y-%m-%d %H:%M:%S")

print(parsed_datetime)
print(parsed_datetime.year)

parsed_date = datetime.strptime("June 02, 2050", "%B %d, %Y")
print(parsed_date)
parsed_time = datetime.strptime("10:12 AM", "%I:%M %p")
print(parsed_time)
parsed_month = datetime.strptime("June", "%B")
print(parsed_month)
parsed_year = datetime.strptime("2050", "%Y")
print(parsed_year)
