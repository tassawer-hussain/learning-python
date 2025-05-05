# x = 10 / 0

try:
    x = 10 / 0
except:
    print("Well that didn't work")


try:
    answer = input("What should I devide 10 by?")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as e:
    print("You can't devide by zero")
except ValueError as e:
    print("You didn't give me a valid number")
    print(e)
finally:
    print("finally always run")