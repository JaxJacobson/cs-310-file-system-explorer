import os
from pathlib import Path


def main(path = '.'):
    file_path = 0
    for file in Path(path).iterdir():
        file_path = file.resolve()

        print(str(file_path))

if __name__ == "__main__":
    main()