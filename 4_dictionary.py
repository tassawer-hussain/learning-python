# Distionary: a key-value data structure
mydict = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    4 : "four",
    4.5 : ["four", "point", "five" ]
}

print(mydict)

# dictionaries are accessed via keys
# print(mydict["one"])
# print(mydict[4])
# print(mydict[4.5])

# # assign new values
# mydict["seven"] = 7
# print(mydict)

# # to avoid undefined key in dictionary error, we use "in" operator
# print("two" in mydict)
# print("blarge" in mydict)

# # retrive all keys & values
# print(mydict.keys())
# print(mydict.values())

# iterate over items. items() function return tuple
for key, val in mydict.items():
    print(key, val)