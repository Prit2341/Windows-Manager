import tempfile
import os
from tkinter import messagebox

def bytes_to_mb(bytes_value):
    mb_value = bytes_value / (1024 * 1024)
    return mb_value

def get_total_temp_file_size():
    # Get the path of the Windows temporary directory
    temp_dir = tempfile.gettempdir()

    # List all files in the temporary directory
    temp_files = [f for f in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, f))]

    # Calculate the total size of all files
    total_size = 0
    for file in temp_files:
        file_path = os.path.join(temp_dir, file)
        total_size += os.path.getsize(file_path)

    return total_size

def is_file_running(file_path):
    try:
        # Check if the file is in use by attempting to open it in read mode
        with open(file_path, 'r'):
            return True
    except IOError:
        return False
    

def delete_temp_files(mb_size):
    # Get the path of the Windows temporary directory
    temp_dir = tempfile.gettempdir()

    # List all files in the temporary directory
    temp_files = [f for f in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, f))]

    # Delete all files in the temporary directory
    for file in temp_files:
        file_path = os.path.join(temp_dir, file)
        try:
            # Check if the file is running before attempting to delete it
            if is_file_running(file_path):
                pass
            else:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            pass

if __name__ == "__main__":
    total_temp_file_size = get_total_temp_file_size()
    mb_size = bytes_to_mb(total_temp_file_size)
    
    print("Info", "Temporary files cleaned successfully.",f"Total size of all temporary files: {mb_size:.2f} MB")
    # Call the function to delete the temporary files
    delete_temp_files(mb_size)
    
