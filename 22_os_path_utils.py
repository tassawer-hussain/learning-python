## Example file for working with os.path module

import os
from os import path
import time
from datetime import date, datetime

# Print the name of the OS
# print(os.name)

# # check for item existence and type
# print("Item exists:", path.exists("textfile.txt"))
#
# print(f"It has been {td} since the file was modified") 
# print(f"or, {td.total_seconds()} seconds")print("Item is a file:", path.isfile("textfile.txt"))
# print("Item is a directory:", path.isdir("textfile.txt"))

# # Work with file paths
# print("Item's path:", path.realpath("textfile.txt"))
# print("Item's path and name:", path.split(path.realpath("textfile.txt")))

# Get the modification time
print(time.ctime(path.getmtime("textfile.txt")))
print(datetime.fromtimestamp(path.getmtime("textfile.txt")))


# Calculate how long ago the item was modified
td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
print(f"It has been {td} since the file was modified")
print(f"or, {td.total_seconds()} seconds")