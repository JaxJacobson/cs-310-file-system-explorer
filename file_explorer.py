import os
import mimetypes
from pathlib import Path

def list_dir(path = "."):                                           # path = "." allows us to list the files in the current directory everytime
                                                                    # without inserting an argument.

    for file in Path(path).iterdir():                               # iterdir() gives us an iterator to loop through the directories.

        file_type = "directory" if file.is_dir() else "file"        # Check if the path is connected to a directory or a file.

        size = file.stat().st_size if file.is_file() else 0         # .stat().st_size gives us the size of the file unless it's a directory.
        size_out = f"{size/(1048576):.1f}MB"                        # Size of file divided by 1024 squared and set to only 1 floating point number.

        if file.is_file():
            mime_type, encode = mimetypes.guess_type(file)          # The mimetypes module will guess what MIME type the file will be. 
            mime_type = mime_type or "don't know"                   # The module can't guess the MIME type sometimes, so we return "don't know".

        else:
            mime_type = "inode/directory"                           # It is not a file, so it doesn't really have a MIME type.

        print(f"{file_path:<10}[{file_type}]{size_out:>6}{mime_type}")  # Easy to read format to see the list of files in the current directory.