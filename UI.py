"""
Tkinter UI for application creating multi-directory structure
"""

from tkinter import *
from tkinter import filedialog

from multiDirectory import MultiDirectory

"""
App class wraps tkinter UI as a software application. Implemented widgets are:

file_button: opens a open-file dilog box; command function [MultiDirectory].browse_button() stores absolute
path of selected file in [MultiDirectory].file_addr

dir_button: opens a open-folder dilog box; command function [MultiDirectory].browse_button() stores absolute
path of selected directory in [MultiDirectory].rel_dir_addr

enumerate_button: radio button to enable enumeration for folders. Command function [MultiDirectory].set_flag()
stores [App].flag <that sets to TRUE after selection of radio button> [MultiDirectory].enum_flag

make_dir_button: Command function [MultiDirectory].driver() initiates process to read file containing directory names
and make folders
"""


class App:
    def __init__(self, master, directory):
        self.enum_flag = BooleanVar()
        self.del_zip_flag = BooleanVar()
        self.file = 'file'
        self.directory = 'directory'
        self.open_file = filedialog.askopenfile
        self.open_dir = filedialog.askdirectory

        frame1 = Frame(master)
        frame1.pack()

        self.file_button = Button(frame1, text="input file",
                                  command=lambda: directory.browse_button(self.file, self.open_file))
        self.file_button.pack(side=LEFT)

        self.dir_button = Button(frame1, text="input folder",
                                 command=lambda: directory.browse_button(self.directory, self.open_dir))
        self.dir_button.pack(side=LEFT)

        frame2 = Frame(master)
        frame2.pack()

        self.enum_radio = Radiobutton(frame2, text="enumerate", variable=self.enum_flag, value=True,
                                      command=lambda: directory.set_flag(flagname='enum'))
        self.enum_radio.pack(side=LEFT)

        self.make_dir_button = Button(frame2, text="make directories", command=directory.make_dirs)
        self.make_dir_button.pack(side=LEFT)

        frame3 = Frame(master)
        frame3.pack()

        self.enum_radio = Radiobutton(frame3, text="delete zips", variable=self.del_zip_flag, value=True,
                                      command=lambda: directory.set_flag(flagname='del_zip'))
        self.enum_radio.pack(side=LEFT)

        self.unzip_button = Button(frame3, text="unzip directories", command=directory.unzip_dirs)
        self.unzip_button.pack(side=LEFT)

root = Tk()
root.title("File Handler")
md = MultiDirectory()
app = App(root, md)
root.mainloop()
