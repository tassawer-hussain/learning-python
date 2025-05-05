# Basic data types
myint = 10
myfloat = 13.2567
mystr = "This is a string"
mybool = True

print(myint)
print(mybool)
print(myfloat)
print(mystr)

print(myint + myfloat)
print(myint * myfloat)
print(myint / myfloat)
print(myint % 3)

another_str = " This is another string"
print(mystr + another_str)
print( ( mystr + " " ) * 3)

# Logical & comparison operators
print( myint == 10)
print(myfloat != 20)
print(myint > 20)
print(myfloat < 10)

print(myint > 10 and myfloat < 25.0)
print(myint > 10 or myfloat < 25.0)

print( not( myint > 10 and myfloat < 25.0 ) )


# variable can be redeclare
myint = "abc"
print(myint)