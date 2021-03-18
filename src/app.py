from multiprocessing import Process
from os import times
from pathlib import Path
import time
from typing import Union
from filelib import File
import queue
import multiprocessing as mp
import logging


logging.basicConfig(format="%(asctime)s %(levelname)s : %(message)s",
                    filename="log_a.log", filemode="a+",
                    level=logging.DEBUG)


def e_p(a):
    while not a.empty():
        f = a.get()
        logging.info(f"{a.get()}")

        a.task_done()


def main():
    srcPath = Path(r"E:\Mipony")
    dstPath = [Path(r"E:\books\JAVA"), Path(r"E:\books\C#")]

    try:
        start = time.time()
        q: list = [File.get_files("pdf", "rar", "zip", "epub",
                                  filename="c#", directory=srcPath),
                   File.get_files("pdf", "rar", "zip", "epub",
                                                       filename="java[^script]", directory=srcPath)]

        for i in q:
            p = mp.Process(target=e_p, args=(i,))
            p.start()
            p.join()
            p.terminate()
        end = time.time()

        print(end-start)

    except ValueError as e:
        print(e)
    except KeyboardInterrupt as e:
        print(e)


if __name__ == '__main__':
    main()

    """ c = Manager.CopyManager() """
