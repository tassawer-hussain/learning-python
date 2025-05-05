import math
from math import pi
import random as r

from tabulate import tabulate

print("The square root of 16 is", math.sqrt(16))
print("Pi is", pi)

print(r.randint(100,200))


data = [
    ["Product", "Price", "Stock"],
    ["Laptop", 999.99, 45],
    ["Mouse", 24.99, 128],
    ["Keyboard", 59.99, 89],
]

# creata a formatted table
print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))