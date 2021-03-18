from pathlib import Path
import tkinter as tk
from tkinter import Frame, StringVar, Tk, ttk
from tkinter.constants import CENTER, LEFT, Y
from tkinter.filedialog import askdirectory
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.curdir)))
from filelib.File import search_file


class CopyManager:
    def __init__(self) -> None:
        self.init_components()

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

        lbSource = ttk.Label(self.win, text="Source Folder", justify=LEFT).grid(
            column=1, row=0, columnspan=2)
        txtSourceDirectory = ttk.Entry(self.win, textvariable=self.path_source, justify=LEFT, width=60).grid(
            column=1, row=1, columnspan=2)
        btnSourceDirectpry = ttk.Button(self.win, text="Choose folder", command=lambda: self.open_dialog(self.path_source)).grid(
            column=4, row=1)
        lbTarget = ttk.Label(self.win, text="Destionation Folder", justify=LEFT).grid(
            column=1, row=3, columnspan=2)
        txtTargetDirectory = ttk.Entry(self.win, textvariable=self.path_target, justify=LEFT, width=60).grid(
            column=1, row=4, columnspan=2)
        btnTargetDirectory = ttk.Button(self.win, text="Choose folder", command=lambda: self.open_dialog(self.path_target)).grid(
            column=4, row=4)

        lbFilename = ttk.Label(self.win, text="Filename", justify=LEFT).grid(
            column=1, row=5, columnspan=2)
        txtFilename = ttk.Entry(self.win, textvariable=self.filename_target, justify=LEFT, width=60).grid(
            column=1, row=6, columnspan=2)
        btnScanDirectory = ttk.Button(self.win, text="scan", command=lambda: self.search_file(self.path_target)).grid(
            column=4, row=6)
        lbFileList = ttk.Label(self.win, text="Result", justify=CENTER).grid(
            column=1, row=7, columnspan=2)
        self.txtFileList = tk.Text(master=self.win, width=50, height=10)
        self.txtFileList.grid(column=1, row=8, columnspan=3)
        btnSearchFile = ttk.Button(self.win, text="move file(s)").grid(
            column=4, row=8)

        lbFrame = tk.LabelFrame(self.win, text="Choose extension", bg="#2a2a2a").grid(
            column=11, row=25, columnspan=5, rowspan=3)
        checkbox_extensions = ["rar", "zip", "pdf",
                               "epub", "part", "7zip", "iso", "mp4"]
        vars_extension = [tk.IntVar() for x in range(len(checkbox_extensions))]

        index = 1
        for check in range(len(checkbox_extensions)):
            ttk.Checkbutton(lbFrame, text=checkbox_extensions[check], variable=vars_extension[check]).grid(
                column=index, row=25)
            index += 1
        self.win.mainloop()

    def open_dialog(self, path: StringVar):
        directory = askdirectory()
        path.set(directory)

    def scan_file(self, file):
        pass
        # for file in search_file()

    def click(self):
        self.text.insert(tk.INSERT, "hola\n")


class Graph(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.initComponents()

    def initComponents(self):
        self.geometry("600x600")
        frame = Frame(master=self, bg="#AFAFAF").place(
            width=500, height=500, x=0, y=0)
        lbtext = tk.Label(frame, text="Hola").place(
            height=20, width=25, x=10, y=20)
        self.mainloop()


if __name__ == '__main__':

    window = CopyManager()
