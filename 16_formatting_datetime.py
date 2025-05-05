from datetime import datetime

now = datetime.now()

# ## DATE FORMATTING
# print(now.strftime("The current year is: %Y"))
# print(now.strftime("%a, %d %B, %y"))

# print(now.strftime("Locale date and time: %c"))
# print(now.strftime("Locale date: %x"))
# print(now.strftime("Locale time: %X"))

## TIME FORMATTING
print(now.strftime("Current TIme: %I:%M:%S %p"))
print(now.strftime("Current TIme: %H:%M"))