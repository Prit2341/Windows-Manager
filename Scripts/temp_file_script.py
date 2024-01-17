# Scripts/temp_file_script.py
import tempfile
import os
from datetime import datetime, timedelta

def bytes_to_mb(bytes_value):
    mb_value = bytes_value / (1024 * 1024)
    return mb_value

def get_total_temp_file_size():
    temp_dir = tempfile.gettempdir()
    temp_files = [f for f in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, f))]
    total_size = sum(os.path.getsize(os.path.join(temp_dir, file)) for file in temp_files)
    return total_size

def is_file_running(file_path):
    try:
        with open(file_path, 'r'):
            return True
    except IOError:
        return False

def delete_temp_files():
    temp_dir = tempfile.gettempdir()
    temp_files = [f for f in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, f))]
    for file in temp_files:
        file_path = os.path.join(temp_dir, file)
        try:
            if is_file_running(file_path):
                pass
            else:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            pass

def get_cleanup_schedule():
    try:
        frequency_days = int(input("Enter how often you want to clean your temp files (in days): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None, None

    next_cleanup_date = datetime.now() + timedelta(days=frequency_days)
    return frequency_days, next_cleanup_date

def modify_cleanup_schedule(new_frequency=None):
    if new_frequency is not None:
        try:
            new_frequency = int(new_frequency)
            new_next_cleanup_date = datetime.now() + timedelta(days=new_frequency)
            return new_frequency, new_next_cleanup_date
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None, None
    else:
        try:
            # Use Tkinter for input in GUI
            import tkinter as tk
            from tkinter import simpledialog

            root = tk.Tk()
            root.withdraw()  # Hide the main window

            current_frequency = simpledialog.askinteger("Modify Cleaning Frequency", "Enter new cleaning frequency (in days):")
            current_next_cleanup_date = datetime.now() + timedelta(days=current_frequency)

            return current_frequency, current_next_cleanup_date
        except ValueError as e:
            print(f"Error: {e}")
            return None, None

if __name__ == "__main__":
    # You can add your main logic here or use this file as a module in other scripts.
    pass
