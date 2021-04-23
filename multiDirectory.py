"""
Program to create multiple enumerated folders
Algorithm:
* read argument .txt file containing line-separated names of folder
* enumerate them and create folders
"""
import os


class MultiDirectory:

    def __init__(self):
        # When file address is not absolute, file is searched in directory of code
        self.rel_prefix = './'
        self.rel_postfix = '/'
        # default variables in absence of stdin arguments
        self.file_addr = ''
        self.rel_dir_addr = ''
        self.enum_flag = False
        self.sep = '_'

    def get_path(self, address):
        # open input text file file_address and store each line denoting folder name into a list using readlines()
        # enumerate the list and create folders using for loop
        if os.path.isabs(address):
            return address + self.rel_postfix if os.path.isdir(address) else address
        else:
            return self.rel_prefix + address

    def make_folders(self, in_file):
        try:
            if self.enum_flag is True:
                for index, name in enumerate(in_file.readlines()):
                    os.mkdir(self.get_path(self.rel_dir_addr) + str(index) + self.sep + name.strip())
            else:
                for name in in_file.readlines():
                    os.mkdir(self.get_path(self.rel_dir_addr) + name.strip())
        except OSError as e:
            print(e)

    # driver code
    def driver(self):
        try:
            if not os.path.isfile(self.file_addr):
                raise IOError("Provide input file")
            else:
                file = open(self.get_path(self.file_addr))
                self.make_folders(file)
        except IOError or FileNotFoundError as e:
            print(e)

    def browse_button(self, open_item, ui_function):
        """
        open_item: <string>, ui_function: <filedlog call for a file/ directory>
        This function browses system and store path of selected storage item into variable.
        If it is a directory; its absolute path returned by filedilog function is stored.
        If it is a file; string containing absolute path to file is extracted using 'name' key in returns
        of filedilog function.
        """
        if open_item is 'file':
            self.file_addr = ui_function().name
        if open_item is 'directory':
            self.rel_dir_addr = ui_function()

    def set_flag(self, flag):
        self.enum_flag = flag
