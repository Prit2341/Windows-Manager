import os
import shutil
import datetime
from tkinter import messagebox


# Function to move files from source to destination
def move_file(source_file, destination_folder):
    try:
        shutil.move(source_file, destination_folder)
        print(f"Moved: {source_file} -> {destination_folder}")
    except Exception as e:
        print(f"Error moving {source_file}: {str(e)}")

# Function to check if a file is older than one month
def is_old_file(file_path):
    now = datetime.datetime.now()
    last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    delta = now - last_modified_time
    return delta.days >= 30

# Function to organize files in the D drive
def organize_files_in_d_drive():
    d_drive_path = "D:/"
    selected_folder = "D:/Unused"  # Replace this with your desired destination folder

    for root, _, files in os.walk(d_drive_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Check if the file is a PDF, image, doc, or excel file
            if file_path.lower().endswith((".pdf", ".png", ".jpg", ".jpeg", ".doc", ".docx", ".xls", ".xlsx")):
                # Check if the file is older than one month
                if is_old_file(file_path):
                    move_file(file_path, selected_folder)

if __name__ == "__main__":
    organize_files_in_d_drive()
    messagebox.showinfo("Info", "Temporary files cleaned successfully.")
