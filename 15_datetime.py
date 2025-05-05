from datetime import date
from datetime import datetime

## DATE OBJECTS
# today = date.today()
# print("Today's date is", today)

# print("Date Components:", today.day, today.month, today.year)

# # Retrieve today;s weekday (0=Monday 6=Sunday)
# print("Today's Weekday #:", today.weekday())

# days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
# print("which is a", days[today.weekday()])

today = datetime.now()
print("The current date & time is", today)

# Get the current time
t = datetime.time(today)
print("Current time is", t)