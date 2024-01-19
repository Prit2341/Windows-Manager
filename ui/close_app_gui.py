import tkinter as tk
from tkinter import ttk, messagebox
import threading
from Scripts.close_app_Script import close_inactive_apps

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Auto Close App")
        self.geometry("300x150")

        self.label = ttk.Label(self, text="Enter inactivity duration (minutes):")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(self)
        self.entry.pack(pady=10)

        self.button = ttk.Button(self, text="Start", command=self.start_thread)
        self.button.pack(pady=10)

    def start_thread(self):
        try:
            target_inactive_duration_minutes = int(self.entry.get())
            threading.Thread(target=self.run_in_background, args=(target_inactive_duration_minutes,), daemon=True).start()
            self.iconify()  # Minimize to system tray
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def run_in_background(self, target_inactive_duration_minutes):
        close_inactive_apps(target_inactive_duration_minutes)

if __name__ == "__main__":
    app = App()
    app.mainloop()
