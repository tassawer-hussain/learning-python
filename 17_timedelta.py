
from datetime import date
from datetime import datetime
from datetime import timedelta

# CONSTRUCT a basic timedelta and print it. Timedelta mean span of time it hold
# print(timedelta(days=365, hours=5, minutes=1))

# now = datetime.now()
# print("Today is", now)
# print("In one year it will be:", now + timedelta(days=365))

# print("In two weeks and 3 days it will be:", now + timedelta(weeks=2, days=3))

## One week ago
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was", s)

## How Many days until April Fool day
today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
    print(f"April fool's day already went by {(today-afd).days} days ago")
    afd = afd.replace(year=today.year+1)

time_to_afd = afd-today
print(f"It's just {time_to_afd.days} days away")