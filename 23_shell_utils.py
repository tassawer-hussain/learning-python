## Example file for working with filesystem shell methods

import os
from os import path
import shutil
from zipfile import ZipFile

# make a duplicate of an existing file
# if path.exists("textfile.txt"):
if path.exists("newfile.txt"):

    # get the path to the file in the current directory
    src = path.realpath("newfile.txt")

    # ## Let's make a backup copy by appending "bak" to the name
    # dst = src + ".bak"

    # ## Now use the shell to make a copy of the file
    # shutil.copy(src, dst) # only copy the file content not file metadata
    # shutil.copy2(src, dst) # both copy the file content and file metadata

    # ## rename the original file
    # os.rename("textfile.txt", "newfile.txt")

    ## now put things into a ZIP archive
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)


    ## More fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("newfile.txt")
        newzip.write("textfile.txt.bak")