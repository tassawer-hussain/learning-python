
x = 0

# # define a while loop
# while x < 5:
#     print(x)
#     x = x + 1

# answer = input("Should I stop?")
# while answer != "yes":
#     print(answer)
#     answer = input("Should I stop?")

# define a for loop
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# for d in days:
#     print(d)

# # Breaks & continue statements
# for d in days:
#     if(d == "Fri"):
#         break
#     if(d == "Tue"):
#         continue
#     print(d)

# using the enymerate() function to get an index and an item
for i, d in enumerate(days):
    print(i, d)