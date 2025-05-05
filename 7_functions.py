# # define a basic function
# def hello_func():
#     print("Hello World")
#     name = input("What is your name?")
#     print("Nice to meet you", name)
# hello_func()


# # function that takes a parameter
# def parameter_func(greeting):
#     name = input("What is your name?")
#     print( greeting, name)
# parameter_func("How are you doing toady")

# # function that return a parameter
# def find_cube( number ):
#     return number * number * number
# print(find_cube(5))


# # default value for parameter
# def default_parameter_func(greeting, name=None):
#     if name == None:
#         name = input("What is your name?")
#     print( greeting, name)
# # default_parameter_func("How are you doing toady")
# default_parameter_func("How are you doing toady", "Tassawer")
# # we can change the parameters order but have to provide the name of paraeters
# default_parameter_func(name="Tassawer", greeting="How are you doing toady")

# variable number of prameters
def multi_parameters(*args):
    result = 0
    for x in args:
        result = result + x
    return result
print(multi_parameters(1,2,3,4,5))
print(multi_parameters(1,2,3,4,5,6,7,8))

def multi_parameters_order( start, *args):
    result = start
    for x in args:
        result = result + x
    return result
print(multi_parameters_order(10, 1,2,3,4,5))
print(multi_parameters_order(100, 1,2,3,4,5,6,7,8))