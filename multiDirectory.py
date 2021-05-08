"""
Program to create multiple enumerated folders
Algorithm:
* read argument .txt file containing line-separated names of folder
* enumerate them and create folders
"""

import fnmatch
import os
from os.path import isabs, isfile, isdir, abspath, join
from zipfile import ZipFile

"""
MultiDirectory class defines functions to crete multiple directories by reading a text file. Implemented widgets are:

get_path: If input argument address is valid absolute path: return it as file path [pad with '/' for directories]. 
Else, return the address after appending relative local path './'. 

make_dirs: Read lines of input text file in name and make individual directory at [MultiDirectory].rel-dir_addr.
Append name with enumerator if [MultiDirectory].enum_flag is set.

unzip_dirs: traverses all files inside self.rel_dir_addr and unzips them. If self.del_zip_flag is set, deletes zip files  

browse_button: Depending upon item argument; opens a open-file / open-directory dialog box and store absolute
path of selected file/ directory in [MultiDirectory].file_addr / [MultiDirectory].rel_dir_addr

set_flag: 
"""


class MultiDirectory:

    def __init__(self):
        # When file address is not absolute, file is searched in directory of code
        self.rel_prefix = './'
        self.rel_postfix = '/'
        # default variables in absence of stdin arguments
        self.file_addr = ''
        self.rel_dir_addr = ''
        self.enum_flag = False
        self.del_zip_flag = False
        self.sep = '_'
        self.pattern = '*.zip'

    def get_path(self, address):
        if isabs(address):
            return address + self.rel_postfix if isdir(address) else address
        else:
            return self.rel_prefix + address

    def open_file(self, file_addr):
        try:
            if not isfile(file_addr):
                raise IOError("Provide input file")
            else:
                file = open(self.get_path(file_addr))
                return file
        except IOError or FileNotFoundError as e:
            print(e)

    def make_dirs(self):
        try:
            in_file = self.open_file(self.file_addr)
            if self.enum_flag is True:
                for index, name in enumerate(in_file.readlines()):
                    os.mkdir(self.get_path(self.rel_dir_addr) + str(index) + self.sep + name.strip())
            else:
                for name in in_file.readlines():
                    os.mkdir(self.get_path(self.rel_dir_addr) + name.strip())
        except OSError as e:
            print(e)

    def unzip_dirs(self):
        a_file = open("sample.txt", "w")
        for root, dirs, files in os.walk(self.rel_dir_addr):
            for filename in fnmatch.filter(files, self.pattern):
                ZipFile(join(abspath(root), filename)).extractall(join(abspath(root), filename.partition(".zip")[0]))
                if self.del_zip_flag:
                    os.remove(join(abspath(root), filename))

    def browse_button(self, open_item, ui_function):
        """
        This function browses system and store path of selected storage item into variable.
        If it is a directory; its absolute path returned by filedialog function is stored.
        If it is a file; string containing absolute path to file is extracted using 'name' key in returns
        of filedialog function.
        open_item: <string>, ui_function: <filedialog call for a file/ directory>
        """
        if open_item is 'file':
            self.file_addr = ui_function().name
        if open_item is 'directory':
            self.rel_dir_addr = ui_function()

    def set_flag(self, flagname='enum'):
        if flagname == 'del_zip':
            self.del_zip_flag = True
        if flagname == 'enum':
            self.enum_flag = True
