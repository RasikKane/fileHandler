"""
Tkinter UI for application creating multi-folder structure
"""

from tkinter import *
from tkinter import filedialog


class App:

    def __init__(self, master):
        self.flag = BooleanVar()
        self.file = 'file'
        self.directory = 'directory'
        self.open_file = filedialog.askopenfile
        self.open_dir = filedialog.askdirectory

        frame = Frame(master)
        frame.pack()

        self.file_button = Button(frame, text="input file")
        self.file_button.pack(side=LEFT)

        self.dir_button = Button(frame, text="destination folder", fg="red")
        self.dir_button.pack(side=LEFT)

        self.enum_radio = Radiobutton(root, text="Enumerate", variable=self.flag, value=True)
        self.enum_radio.pack(side=LEFT)

        self.make_dir = Button(frame, text="make directories")
        self.make_dir.pack(side=LEFT)


root = Tk()
app = App(root)
root.mainloop()
