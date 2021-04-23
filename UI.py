"""
Tkinter UI for application creating multi-folder structure
"""

from tkinter import *
from tkinter import filedialog

from multiDirectory import MultiDirectory


class App:

    def __init__(self, master, directory):
        self.flag = BooleanVar()
        self.file = 'file'
        self.directory = 'directory'
        self.open_file = filedialog.askopenfile
        self.open_dir = filedialog.askdirectory

        frame = Frame(master)
        frame.pack()

        self.file_button = Button(frame, text="input file",
                                  command=lambda: directory.browse_button(self.file, self.open_file))
        self.file_button.pack(side=LEFT)

        self.dir_button = Button(frame, text="destination folder", fg="red",
                                 command=lambda: directory.browse_button(self.directory, self.open_dir))
        self.dir_button.pack(side=LEFT)

        self.enum_radio = Radiobutton(root, text="enumerate", variable=self.flag, value=True,
                                      command=lambda: directory.set_flag(self.flag.get()))
        self.enum_radio.pack(side=LEFT)

        self.make_dir = Button(frame, text="make directories", command=directory.driver)
        self.make_dir.pack(side=LEFT)


root = Tk()
md = MultiDirectory()
app = App(root, md)
root.mainloop()
