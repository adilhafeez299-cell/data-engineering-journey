from datetime import datetime

future_datetime = datetime(2100, 10, 12, 20, 59, 20, 15)
print("Future date and time:", future_datetime)

print("Formatted date:", future_datetime.strftime("%B, %d, %Y"))
print("Formatted time:", future_datetime.strftime("%I:%M %p"))
print("Formatted date and time:",
      future_datetime.strftime("%A, %B, %d, %Y, %I:%M %p"))
# go over again