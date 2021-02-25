from os.path import join
from pathlib import Path
import os
import queue


""" 
note:  search all files only by extensions,

use queue, multiporcessing,db
"""


def search_file(filename: str = None, file_extension: tuple = ".*", directory: Path = Path.cwd()):
    """ Search file in a directory
        filename -> str
        directory -> str
        file_extension -> tuple
    """
    import re
    ext = str.join("|", file_extension)

    if not path_is_valid(directory):
        raise FileNotFoundError(
            f"Directory:\"{directory}\" not exist")

    if not filename is None:

        compile = re.compile(fr"{filename}*\.({ext})$")

        for file in directory.rglob("*.*"):
            if compile.search(file.name):
                yield file


def path_is_valid(path: str) -> bool:
    return os.path.exists(path)


def get_files(filename: str = None, file_extension: tuple = ".*", directory: Path = Path.cwd()) -> queue.Queue:
    list_files = queue.Queue()
    for file in search_file(filename, file_extension, directory):
        list_files.put(file)
    return list_files

