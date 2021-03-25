
from tkinter.filedialog import Directory, askdirectory
from tkinter.constants import CENTER, LEFT, Y
from tkinter import Frame, StringVar, Tk, ttk
import tkinter as tk
from pathlib import Path
from logging import disable

from typing import Text
import sys
import queue
import os
sys.path.append(os.path.abspath(os.path.join(os.curdir)))
from filelib.File import copy_files, get_files

class CopyManager:
    def __init__(self) -> None:
        self.init_components()
        self.Files = queue.Queue()

    def init_components(self):
        self.win = Tk()
        self.win.title("File Manager")
        self.win.geometry("600x400")
        self.win.configure()

        self.frame = tk.Frame(master=self.win)
        self.path_source = StringVar()
        self.path_target = StringVar()
        self.filename_target = StringVar()
        self.file_list = StringVar
        self.file_extension = StringVar()

        # SourceDirectory

        lbSource = ttk.Label(self.win, text="Source Folder", justify=LEFT).grid(
            column=1, row=0, columnspan=2)
        txtSourceDirectory = ttk.Entry(self.win, textvariable=self.path_source, justify=LEFT, width=60).grid(
            column=1, row=1, columnspan=2)
        btnSourceDirectpry = ttk.Button(self.win, text="Choose folder", command=lambda: self.open_dialog(self.path_source)).grid(
            column=4, row=1)

        # targetDirectory
        lbTarget = ttk.Label(self.win, text="Destionation Folder", justify=LEFT).grid(
            column=1, row=3, columnspan=2)

        txtTargetDirectory = ttk.Entry(self.win, textvariable=self.path_target, justify=LEFT, width=60).grid(
            column=1, row=4, columnspan=2)
        btnTargetDirectory = ttk.Button(self.win, text="Choose folder", command=lambda: self.open_dialog(self.path_target)).grid(
            column=4, row=4)

        # filename
        lbFilename = ttk.Label(self.win, text="Filename", justify=LEFT).grid(
            column=1, row=5, columnspan=2)

        txtFilename = ttk.Entry(self.win, textvariable=self.filename_target, justify=LEFT, width=60).grid(
            column=1, row=6, columnspan=2)

        # fileExtension
        lbFilenExtension = ttk.Label(self.win, text=f"Write extension(use \",\" or \"-\" to separeted", justify=LEFT).grid(
            column=1, row=7, columnspan=2)

        txtFileExtension = ttk.Entry(self.win, textvariable=self.file_extension, justify=LEFT, width=60).grid(
            column=1, row=8, columnspan=2)

        # btnScanDirectory
        btnScanDirectory = ttk.Button(self.win, text="scan", command=self.scan_file).grid(
            column=4, row=6)
        # FileList
        lbFileList = ttk.Label(self.win, text="Result", justify=CENTER).grid(
            column=1, row=9, columnspan=2)
        self.txtFileList = tk.Text(master=self.win, width=50, height=10)
        self.txtFileList.grid(column=1, row=10, columnspan=3)

        # btnMoveFile
        btnMoveFile = ttk.Button(self.win, text="move file(s)", command=self.move_file).grid(
            column=4, row=8)
        self.win.mainloop()

    def open_dialog(self, path: StringVar):
        directory = askdirectory()
        path.set(directory)

    def scan_file(self):

        import re
        regex = re.compile("\W+")
        ext = tuple(regex.split(self.file_extension.get()))
        sourceDirectory = Path(self.path_source.get())
        filename = Path(self.filename_target.get())

        self.Files = get_files(*ext, filename=filename,
                               directory=sourceDirectory)

        Popup("Info", f"Found {self.Files.qsize()}")

    def move_file(self):

        dst = Path(self.path_target.get())
        try:
            while not self.Files.empty():
                file = self.Files.get()
                copy_files(file, dst)
                self.txtFileList.insert(tk.INSERT, f"{file}\n")

            Popup("Info", "Successful")
        except Exception as e:
            Popup("Error", "Files cannot be moved: " + str(e))


class Popup:
    def __init__(self, title, msg) -> None:
        self.message = msg
        self.title_window = title
        self.initComponents()

    def initComponents(self):
        self.topWindow = tk.Toplevel()
        self.topWindow.wm_title(self.title_window)
        txtMessage = ttk.Label(master=self.topWindow,
                               text=self.message).grid(column=1, row=1)
        btnOk = ttk.Button(master=self.topWindow, text="Ok",
                           command=self.close).grid(column=1, row=2)
        self.topWindow.mainloop()

    def close(self):
        self.topWindow.destroy()
        self.topWindow.update()


if __name__ == '__main__':

    window = CopyManager()
