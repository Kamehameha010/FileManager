from os.path import isfile, join
from pathlib import Path
from shutil import Error
from time import time
import os
import queue
from functools import lru_cache
import logging

""" 
note:  search all files only by extensions,

use queue, multiporcessing,db
"""


@lru_cache
def search_file(*file_extension, filename: str = None, directory: Path = Path.cwd()):
    """ Search file in a directory
        filename -> str
        directory -> str
        file_extension -> tuple
    """
    import re
    if len(file_extension) > 1:
        ext = str.join("|", file_extension)
    else:
        ext = file_extension
    if not path_is_valid(directory):
        raise FileNotFoundError(
            f"Directory:\"{directory}\" not exist")

    if not filename is None:

        regex = re.compile(fr".?{filename}.*\.({ext})$", re.IGNORECASE)

        for file in directory.rglob("*.*"):
           
            if regex.search(file.name):
                yield file


def path_is_valid(path: str) -> bool:
    return os.path.exists(path)


def get_files(*file_extension, **kwargs) -> queue.Queue:
    list_files = queue.Queue()

    for file in search_file(*file_extension, **kwargs):
        print(file)
        list_files.put(file)
    return list_files


def copy_files(src: str, dst: Path):
    import shutil
    if not dst.exists():
        dst.mkdir()
    try:
        shutil.move(fr"{src}", fr"{dst}")
    except OSError as e:
        logging.error(e)
    except Error as e:
        logging.error(e)
