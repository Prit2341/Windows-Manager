import os
import shutil
import datetime

def move_files(source_folder, destination_folder, date_threshold):
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.lower().endswith((".pdf", ".png", ".jpg", ".jpeg", ".doc", ".docx", ".xls", ".xlsx")):
                if is_old_file(file_path, date_threshold):
                    try:
                        shutil.move(file_path, destination_folder)
                        print(f"Moved: {file_path} -> {destination_folder}")
                    except Exception as e:
                        print(f"Error moving {file_path}: {str(e)}")

def is_old_file(file_path, date_threshold):
    last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    return last_modified_time < date_threshold
