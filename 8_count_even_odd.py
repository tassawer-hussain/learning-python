# Python code​​​​​​‌‌​‌​​‌‌‌‌​‌‌‌‌​​‌‌​​​‌‌‌ below
# Use print("messages...") to debug your solution.

# ## MY CODE
# def count_numbers(which, numbers):
#     # Your code goes here
#     even = 0
#     odd = 0
#     for n in numbers:
#         if (n % 2 == 0 ):
#             even = even + 1
#         else:
#             odd = odd + 1

#     if which == "even":
#         return even
#     elif which == "odd":
#         return odd
#     else:
#         return -1
    
## INSTRUCTOR CODE
def count_numbers(which, numbers):
    # Your code goes here

    # early bail
    if which != "even" and which != "odd":
        return -1

    result = 0
    for n in numbers:
        if (which == "even" and n % 2 == 0 ):
            result += 1

        if (which == "odd" and n % 2 != 0 ):
            result += 1

    return result
    

numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]
result1 = count_numbers("even", numbers)
result2 = count_numbers("odd", numbers)
result3 = count_numbers("Blarg", numbers)

print( "even", result1)
print( "odd", result2)
print( "Wrong input", result3)