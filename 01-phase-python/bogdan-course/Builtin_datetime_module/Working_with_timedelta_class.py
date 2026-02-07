from datetime import datetime, timedelta

future_datetime = datetime(2100, 12, 10, 18, 10, 45)
print("Original date:", future_datetime)

print(future_datetime + timedelta(days=100))
print(future_datetime + timedelta(hours=3))
print(future_datetime + timedelta(days=3, hours=5, minutes=15))

print(future_datetime - timedelta(days=5))
print(future_datetime - timedelta(days=365, hours=24))
