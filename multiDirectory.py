"""
Program to create multiple enumerated folders
Algorithm:
* read argument .txt file containing line-separated names of folder
* enumerate them and create folders
"""
import os

# When file address is not absolute, file is searched in directory of this code
rel_prefix = './'
rel_postfix = '/'
# default variables in absence of stdin arguments
file_addr = ''
rel_dir_addr = ''
enum_flag = False
sep = '_'


def get_path(address, prefix=rel_prefix, postfix=rel_postfix):
    # open input text file file_address and store each line denoting folder name into a list using readlines()
    # enumerate the list and create folders using for loop
    if os.path.isabs(address):
        return address + postfix if os.path.isdir(address) else address
    else:
        return prefix + address


def make_folders(in_file, flag, separator, rel_folder_address, prefix):
    try:
        print(flag)
        if flag is True:
            for index, name in enumerate(in_file.readlines()):
                os.mkdir(get_path(rel_folder_address, prefix) + str(index) + separator + name.strip())
        else:
            for name in in_file.readlines():
                os.mkdir(get_path(rel_folder_address, prefix) + name.strip())
    except OSError as e:
        print(e)


# driver code
def driver():
    global file_addr, enum_flag, sep, rel_dir_addr
    try:
        print(file_addr, rel_dir_addr)
        if not os.path.isfile(file_addr):
            raise IOError("Provide input file")
        else:
            file = open(get_path(file_addr, rel_prefix, rel_prefix))
            make_folders(file, enum_flag, sep, rel_dir_addr, rel_prefix)
    except IOError or FileNotFoundError as e:
        print(e)


def browse_button(open_item, ui_function):
    """
    open_item: <string>, ui_function: <filedlog call for a file/ directory>
    This function browses system and store path of selected storage item into variable.
    If it is a directory; its absolute path is stored.
    If it is a file;
    """
    global file_addr, rel_dir_addr
    if open_item is 'file':
        file_addr = ui_function().name
    if open_item is 'directory':
        rel_dir_addr = ui_function()


def set_flag(flag):
    global enum_flag
    enum_flag = flag
