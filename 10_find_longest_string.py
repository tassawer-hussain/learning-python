def find_largest(strings):
    count = 0
    for str in strings:
        if count < len(str):
            count = len(str)

    return count


test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]

print(find_largest(test_strings))