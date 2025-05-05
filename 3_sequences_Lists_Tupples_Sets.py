# Sequences: Lists[], Tuples()) & Sets{}

mylist = [0, 1, 2, "two", 3.2, False]

# print(len(mylist))
# print(mylist[2])
# print(mylist[-1])

# mylist[0] = 10
# print(mylist)

# # add a list to another
# another_list = [6, 7, 8]
# mylist = mylist + another_list
# print(mylist)

# mystr = "THis is a string"
# print(mystr[2])

# mystr[2] = "Z" # str are immutable

# use slices to get parts of a sequence
# print(mylist[1:4:2]) # 4 index not included. Third parameter determines the step
# print(mylist[::2]) # Default first to last index with step of 2
# print(mylist[1:4]) # 4 index not included. Step not included
# print(mylist[::-1]) # Reverse the list order


### TUPPLES are like lists, but they are immutable. Same kind of operations can be performmed on Tupples like lists
mytuple = (0,1,2, "three")
print(mytuple[2])


### Sets are also sequences, but they contain unique values. They don't support indexing
myset = {1, 2, 3, 4, "Five", 2} # 2 will be remove
print(myset)
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in mylist)
print(3 in mytuple)
print(5 in myset)