import tkinter as tk
from tkinter import messagebox
from UI.recycle_bin_gui import RecycleBinCleanerGUI
from UI.temp_remover_gui import TempFileCleanerGUI

class UniversalGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.title("Universal GUI")

        open_recycle_bin_btn = tk.Button(self, text="Open Recycle Bin Cleaner", command=self.open_recycle_bin_gui)
        open_recycle_bin_btn.pack(pady=10)

        open_temp_file_btn = tk.Button(self, text="Open Temp File Cleaner", command=self.open_temp_file_gui)
        open_temp_file_btn.pack(pady=10)

    def open_recycle_bin_gui(self):
        recycle_bin_gui = RecycleBinCleanerGUI()
        recycle_bin_gui.geometry("300x200")
        recycle_bin_gui.mainloop()

    def open_temp_file_gui(self):
        temp_file_gui = TempFileCleanerGUI()
        temp_file_gui.geometry("300x200")
        temp_file_gui.mainloop()

if __name__ == '__main__':
    app = UniversalGUI()
    app.geometry("300x200")
    app.mainloop()
