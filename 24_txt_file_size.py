import os

def file_into():

    total_bytes = 0
    folder = "D:\python"

    #get a list of all the files in the current directory
    dirlist = os.listdir(folder)
    print(dirlist)
    for entry in dirlist:
        # make sure it's a file!
        if os.path.isfile(folder + "/" + entry) and entry.endswith(".txt"):

            # add the file size to the total
            filesize = os.path.getsize(folder + "/" + entry)
            total_bytes += filesize

    return total_bytes

print(file_into())