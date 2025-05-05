def is_palindrome(teststr):

    #convert the string to all lower case.
    temp = teststr.lower()

    newstr = ""
    for c in temp:
        if c.isalnum():
            newstr += c

    # now calculate the reverse of the string
    reversestr = ""
    strindex = len(newstr) - 1

    while strindex >= 0:
        reversestr += newstr[strindex]
        strindex -= 1

    if newstr == reversestr:
        return True
    
    return False


print(is_palindrome("My name Is TASSAWER"))

test_word = "Madam, I'm Adam."
# try using some of these other words:
# test_word = "RACE CAR!"
# test_word = "Hello, world"
# test_word = "Radar?"
# test_word = "A man, a plan, a canal Panama!"

print("Madam, I'm Adam:", "is palindrome?", is_palindrome("Madam, I'm Adam."))
print("RACE CAR!", "is palindrome?", is_palindrome("RACE CAR!"))
print("Hello, world", "is palindrome?", is_palindrome("Hello, world"))
print("Radar?", "is palindrome?", is_palindrome("Radar?"))
print("A man, a plan, a canal Panama", "is palindrome?", is_palindrome("A man, a plan, a canal Panama"))