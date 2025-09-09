# Jax Jacobson
# 9/8/25
# CS 310 - W2 Filesystem Explorer.\<ext\>
# List out all of the files and directories including their path, size, type, and MIME type using pathlib.


import os
import mimetypes
from pathlib import Path

def main(path = "."):                                                                       # path = "." allows us to list the files in the current 
                                                                                            # directory everytime without inserting an argument.

    for file in Path(path).iterdir():                                                       # iterdir() gives us an iterator to loop through the 
                                                                                            # directories/files.

        file_path = file.resolve()

        if file.is_dir():                                                                   # Check if the path is connected to a directory or a file.
            file_type = "directory" 
        else:
            file_type = "file"

        size = file.stat().st_size                                                          # .stat().st_size gives us the size of the file unless it's a 
                                                                                            # directory.
        if file.is_file(): 
            size_out = f"{size/(1048576):.1f}MB"                                            # Size of file divided by 1024 squared and set to only 1 
                                                                                            # floating point number.
        else:
            size_out = "0.0MB"                                                  

        if file.is_file():
            mime_type, encode = mimetypes.guess_type(file)                                  # The mimetypes module will guess what MIME type the file will
            mime_type = mime_type or "don't know"                                           # be. The module can't guess the MIME type sometimes, so we 
                                                                                            # return "don't know".
        else:
            mime_type = "inode/directory"                                                   # It is not a file, so it doesn't really have a MIME type.


        if file_type == "directory":
            print(f"{str(file_path):<80}[{file_type}]{size_out:>25}{mime_type:>35}")
        else:
            print(f"{str(file_path):<80}[{file_type}]{size_out:>30}{mime_type:>35}")        # Easy to read format to see the list of files in the current 
                                                                                            # directory. file_path has to be converted to a string, or it 
                                                                                            # will not work!

if __name__ == "__main__":
    main()