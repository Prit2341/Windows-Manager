import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from cleaner import get_recycle_bin_files
from tempcleaner import delete_temp_files
# Functions for the four features




def automate_whatsapp_files():
    # Implement the functionality for automating WhatsApp files here
    messagebox.showinfo("Info", "WhatsApp files automated successfully.")

def manage_files():
    # Implement the functionality for managing files here
    messagebox.showinfo("Info", "Files managed successfully.")

# Create the main application window
root = tk.Tk()
root.title("Windows Cleaner Application")

root.geometry("600x400") 

# Create and arrange GUI components
temp_cleaner_button = tk.Button(root, text="Clean Temporary Files", command=delete_temp_files)
recycle_bin_button = tk.Button(root, text="Automate Recycle Bin", command=get_recycle_bin_files)
whatsapp_automator_button = tk.Button(root, text="Automate WhatsApp Files", command=automate_whatsapp_files)
files_manager_button = tk.Button(root, text="Manage Files", command=manage_files)

temp_cleaner_button.pack(pady=10)
recycle_bin_button.pack(pady=10)
whatsapp_automator_button.pack(pady=10)
files_manager_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()
