import tempfile
import os
from tkinter import messagebox
from datetime import datetime, timedelta

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

def get_cleanup_schedule():
    try:
        frequency_days = int(input("Enter how often you want to clean your temp files (in days): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None, None

    next_cleanup_date = datetime.now() + timedelta(days=frequency_days)
    return frequency_days, next_cleanup_date

def modify_cleanup_schedule():
    current_frequency, current_next_cleanup_date = get_cleanup_schedule()

    if current_frequency and current_next_cleanup_date:
        print(f"Current cleaning frequency: {current_frequency} days")
        print(f"Next scheduled cleanup on: {current_next_cleanup_date.strftime('%Y-%m-%d %H:%M:%S')}")

        modify_choice = input("Do you want to modify the cleaning frequency? (y/n): ").lower()
        if modify_choice == 'y':
            new_frequency, new_next_cleanup_date = get_cleanup_schedule()
            return new_frequency, new_next_cleanup_date

    return None, None

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Clean temporary files")
        print("2. Modify cleaning frequency")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            frequency_days, next_cleanup_date = get_cleanup_schedule()

            total_temp_file_size = get_total_temp_file_size()
            mb_size = bytes_to_mb(total_temp_file_size)

            print(f"Current total size of all temporary files: {mb_size:.2f} MB")

            if frequency_days and next_cleanup_date:
                print(f"Next scheduled cleanup on: {next_cleanup_date.strftime('%Y-%m-%d %H:%M:%S')}")

                # Call the function to delete the temporary files
                delete_temp_files(mb_size)
                print("Temporary files cleaned successfully.")
            else:
                print("Cleanup schedule not set. Please enter a valid frequency for cleaning.")
        
        elif choice == '2':
            new_frequency, new_next_cleanup_date = modify_cleanup_schedule()

            if new_frequency and new_next_cleanup_date:
                print(f"Cleaning frequency modified to: {new_frequency} days")
                print(f"Next scheduled cleanup on: {new_next_cleanup_date.strftime('%Y-%m-%d %H:%M:%S')}")
        
        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
