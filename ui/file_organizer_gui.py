import os
import shutil
import datetime
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from tkcalendar import DateEntry
from Scripts.organize_flies import move_files, is_old_file

class FileOrganizerGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("File Organizer")

        self.source_label = Label(self, text="Source Folder:")
        self.source_label.grid(row=0, column=0, padx=10, pady=10)

        self.source_entry = Entry(self, width=40)
        self.source_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_source_btn = Button(self, text="Browse", command=self.browse_source_folder)
        self.browse_source_btn.grid(row=0, column=2, padx=10, pady=10)

        self.destination_label = Label(self, text="Destination Folder:")
        self.destination_label.grid(row=1, column=0, padx=10, pady=10)

        self.destination_entry = Entry(self, width=40)
        self.destination_entry.grid(row=1, column=1, padx=10, pady=10)

        self.browse_destination_btn = Button(self, text="Browse", command=self.browse_destination_folder)
        self.browse_destination_btn.grid(row=1, column=2, padx=10, pady=10)

        self.date_label = Label(self, text="Move files modified before:")
        self.date_label.grid(row=2, column=0, padx=10, pady=10)

        self.date_entry = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)

        self.save_btn = Button(self, text="Save Directories", command=self.save_directories)
        self.save_btn.grid(row=3, column=1, padx=10, pady=10)

        self.organize_btn = Button(self, text="Organize Files", command=self.organize_files)
        self.organize_btn.grid(row=4, column=1, padx=10, pady=10)

    def browse_source_folder(self):
        source_folder = filedialog.askdirectory()
        self.source_entry.delete(0, 'end')
        self.source_entry.insert(0, source_folder)

    def browse_destination_folder(self):
        destination_folder = filedialog.askdirectory()
        self.destination_entry.delete(0, 'end')
        self.destination_entry.insert(0, destination_folder)

    def save_directories(self):
        source_folder = self.source_entry.get()
        destination_folder = self.destination_entry.get()

        if source_folder and destination_folder:
            with open("directories.txt", "w") as file:
                file.write(f"Source Folder: {source_folder}\n")
                file.write(f"Destination Folder: {destination_folder}\n")
            messagebox.showinfo("Directories Saved", "Directories have been saved successfully.")
        else:
            messagebox.showerror("Error", "Both source and destination folders must be provided.")

    def organize_files(self):
        source_folder = self.source_entry.get()
        destination_folder = self.destination_entry.get()
        date_obj = self.date_entry.get_date()

        if source_folder and destination_folder and date_obj:
            date_threshold = datetime.datetime.combine(date_obj, datetime.datetime.min.time())
            move_files(source_folder, destination_folder, date_threshold)
            messagebox.showinfo("Organize Files", "Files organized successfully.")
        else:
            messagebox.showerror("Error", "Both source and destination folders must be provided, and a valid date must be selected.")

if __name__ == "__main__":
    root = Tk()
    gui = FileOrganizerGUI(root)
    root.mainloop()
