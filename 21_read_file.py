## Read & Write files using the built-in Python file methods

## Open the file and read the content
sample_file = open("textfile.txt", "r")
if sample_file.mode == "r":

    ## use the read() function to read the entire file
    # contents = sample_file.read()
    # print(contents)

    ## Read file line by line
    file_lines = sample_file.readlines()
    for line in file_lines:
        print(line)

