# import os
# import tempfile
# import ctypes
# from ctypes.wintypes import MAX_PATH
# from ctypes import wintypes
# from tkinter import messagebox
# from datetime import datetime, timedelta

# import winshell

# def get_recycle_bin_files():
#     try:
#         winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
#         print("Recycle bin is emptied now!")
#     except Exception as e:
#         print(f"Error: {e}")
#         print("Failed to empty the recycle bin.")

# def set_cleaning_frequency():
#     try:
#         while True:
#             days = int(input("Enter how often you want to clean your recycle bin (in days): "))
#             if days <= 0:
#                 print("Please enter a positive number of days.")
#                 continue

#             last_cleaned_date = datetime.now()
#             while True:
#                 current_date = datetime.now()
#                 if (current_date - last_cleaned_date).days >= days:
#                     get_recycle_bin_files()
#                     last_cleaned_date = current_date
#                     break
#                 else:
#                     print(f"Recycle bin will be cleaned next on {last_cleaned_date + timedelta(days=days)}.")

#                 modify_frequency = input("Do you want to modify the cleaning frequency? (yes/no): ").lower()
#                 if modify_frequency == 'yes':
#                     break

#             if modify_frequency == 'no':
#                 break

#     except ValueError:
#         print("Invalid input. Please enter a valid number of days.")

# if __name__ == "__main__":
#     set_cleaning_frequency()


# import os
# import tempfile
# import ctypes
# from ctypes.wintypes import MAX_PATH
# from ctypes import wintypes
# from tkinter import messagebox


# import winshell

# def get_recycle_bin_files():
#     try:
#         winshell.recycle_bin().empty(confirm=False,show_progress=True,sound=True)
#         print("Recycle bin is emptied now!")
#     except:
#         print("Recycle bin is already empty!")
    
# if __name__ == "__main__":
#     get_recycle_bin_files()
    
    
import winshell
import os

def clean_recycle_bin():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
        return "Recycle bin is emptied now!"
    except Exception as e:
        return f"Error: {e}\nFailed to empty the recycle bin."

def set_cleaning_frequency(days):
    try:
        with open("cleaning_frequency.txt", "w") as file:
            file.write(str(days))
        return f"Recycle bin will be cleaned every {days} days."
    except Exception as e:
        return f"Error: {e}\nFailed to set cleaning frequency."

def get_cleaning_frequency():
    try:
        with open("cleaning_frequency.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 1
    except Exception as e:
        return f"Error: {e}\nFailed to get cleaning frequency."

