import os
import tempfile
import ctypes
from ctypes.wintypes import MAX_PATH
from ctypes import wintypes
from tkinter import messagebox


import winshell

def get_recycle_bin_files():
    try:
        winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
        print("Recycle bin is emptied now!")
    except:
        print("Recycle bin is already empty!")
    messagebox.showinfo("Info", "Recycle Bin automated successfully.")
    
if __name__ == "__main__":
    get_recycle_bin_files()
    
    
