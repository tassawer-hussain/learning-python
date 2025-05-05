# write files using the built-in Python file methods

# # Open a file for writing and create it if it doesn't exist
# sample_file = open('textfile.txt', "w+")
# sample_file.write("This is some sample text in our sample file.")
# sample_file.close()

# Open the file for appending text to the end
sample_file = open('textfile.txt', "a+") # open the file with append mode.
sample_file.write("This is some another sample text in our sample file.\n")
sample_file.write("This is some another one sample text in our sample file.\n")
sample_file.close()