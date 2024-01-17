import tkinter as tk
from tkinter import messagebox, simpledialog
from Scripts.cleaner import clean_recycle_bin, set_cleaning_frequency, get_cleaning_frequency

class RecycleBinCleanerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.title("Recycle Bin Cleaner")

        clean_btn = tk.Button(self, text="Clean Recycle Bin Now", command=self.clean_recycle_bin)
        clean_btn.pack(pady=10)

        add_days_btn = tk.Button(self, text="Add Days for Cleaning", command=self.add_days_dialog)
        add_days_btn.pack(pady=10)

        modify_days_btn = tk.Button(self, text="Modify Cleaning Frequency", command=self.modify_days_dialog)
        modify_days_btn.pack(pady=10)

    def clean_recycle_bin(self):
        result = clean_recycle_bin()
        self.show_popup(result)

    def add_days_dialog(self):
        days = simpledialog.askinteger("Add Days", "Enter how many days after you want to clean your recycle bin:")
        if days is not None:
            result = set_cleaning_frequency(days)
            self.show_popup(result)

    def modify_days_dialog(self):
        current_days = get_cleaning_frequency()
        days = simpledialog.askinteger("Modify Cleaning Frequency", "Enter how often you want to clean your recycle bin (in days):", initialvalue=current_days)
        if days is not None:
            result = set_cleaning_frequency(days)
            self.show_popup(result)

    def show_popup(self, message):
        messagebox.showinfo("Recycle Bin Cleaner", message)

if __name__ == '__main__':
    app = RecycleBinCleanerGUI()
    app.geometry("300x200")
    app.mainloop()
