import tkinter as tk
from tkinter import messagebox, simpledialog
from Scripts.temp_file_script import delete_temp_files, get_total_temp_file_size, bytes_to_mb, modify_cleanup_schedule

class TempFileCleanerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.title("Temp File Cleaner")

        clean_direct_btn = tk.Button(self, text="Clean Temporary Files", command=self.clean_direct)
        clean_direct_btn.pack(pady=10)

        set_frequency_btn = tk.Button(self, text="Set Cleaning Frequency", command=self.set_frequency)
        set_frequency_btn.pack(pady=10)

        modify_schedule_btn = tk.Button(self, text="Modify Cleaning Schedule", command=self.modify_schedule)
        modify_schedule_btn.pack(pady=10)

    def clean_direct(self):
        total_temp_file_size = get_total_temp_file_size()
        mb_size = bytes_to_mb(total_temp_file_size)
        delete_temp_files()
        message = f"Temporary files cleaned successfully.\nTotal size of all temporary files: {mb_size:.2f} MB"
        self.show_popup("Clean Directly", message)

    def set_frequency(self):
        frequency_days = simpledialog.askinteger("Set Cleaning Frequency", "Enter cleaning frequency (in days):")
        if frequency_days is not None:
            message = f"Cleaning frequency set to {frequency_days} days."
            self.show_popup("Set Cleaning Frequency", message)
        else:
            self.show_popup("Error", "Invalid input. Please enter a valid frequency for cleaning.")

    def modify_schedule(self):
        current_frequency, _ = modify_cleanup_schedule()

        if current_frequency is not None:
            new_frequency = self.ask_integer_input("Modify Cleaning Frequency", "Enter new cleaning frequency (in days):", current_frequency)
            if new_frequency is not None:
                _, new_next_cleanup_date = modify_cleanup_schedule(new_frequency=new_frequency)

                if new_next_cleanup_date is not None:
                    message = f"Cleaning schedule modified.\nNext scheduled cleanup on: {new_next_cleanup_date.strftime('%Y-%m-%d %H:%M:%S')}"
                    self.show_popup("Modify Cleaning Schedule", message)
                else:
                    self.show_popup("Error", "Failed to modify cleaning schedule.")
            else:
                self.show_popup("Error", "Invalid input. Please enter a valid frequency for cleaning.")
        else:
            self.show_popup("Error", "Failed to retrieve current cleaning schedule.")

    def ask_integer_input(self, title, prompt, initial_value=0):
        answer = simpledialog.askstring(title, prompt, initialvalue=initial_value)
        try:
            return int(answer)
        except (ValueError, TypeError):
            return None

    def show_popup(self, title, message):
        messagebox.showinfo(title, message)

if __name__ == '__main__':
    app = TempFileCleanerGUI()
    app.geometry("300x200")
    app.mainloop()
