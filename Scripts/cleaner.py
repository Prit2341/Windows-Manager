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

