import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tkinter import messagebox

# Set the source directory where WhatsApp downloads files to
source_dir = "C:/WhatsApp/"

# Set the destination directory where you want to move the downloaded files
destination_dir = "E:/Whatsapp Images/"

class WhatsAppDownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        # Get the path of the newly created file
        file_path = event.src_path

        # Move the file to the destination directory with the correct file name
        try:
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(destination_dir, file_name)
            shutil.move(file_path, destination_path)
            print(f"Moved file: {file_name}")
        except Exception as e:
            print(f"Error moving file: {e}")

if __name__ == "__main__":
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    event_handler = WhatsAppDownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=source_dir, recursive=False)
    observer.start()

    try:
        print(f"Watching {source_dir} for new files...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Observer stopped.")
    observer.join()


'''GUI Code Here'''
import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox

class WhatsAppDownloadHandler(FileSystemEventHandler):
    def __init__(self, source_dir, destination_dir):
        super().__init__()
        self.source_dir = source_dir
        self.destination_dir = destination_dir

    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        try:
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(self.destination_dir, file_name)

            # Add a delay to allow WhatsApp to finish writing to the file
            time.sleep(60)

            # Check if the file is not in use before moving
            if not self.is_file_in_use(file_path):
                shutil.move(file_path, destination_path)
                print(f"Moved file: {file_name}")
            else:
                print(f"Error moving file: {file_name} (file in use)")

        except FileNotFoundError:
            print(f"Error moving file: {file_name} (file not found)")
        except Exception as e:
            print(f"Error moving file: {file_name} ({e})")

    def is_file_in_use(self, file_path):
        # Check if the file is in use by attempting to open it
        try:
            with open(file_path, 'r'):
                return True
        except Exception:
            return False

class WhatsAppAutomationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Automation")

        self.source_label = Label(root, text="Source Directory:")
        self.source_label.grid(row=0, column=0, padx=10, pady=10)

        self.source_entry = Entry(root, width=40)
        self.source_entry.grid(row=0, column=1, padx=10, pady=10)

        self.browse_source_btn = Button(root, text="Browse", command=self.browse_source_directory)
        self.browse_source_btn.grid(row=0, column=2, padx=10, pady=10)

        self.destination_label = Label(root, text="Destination Directory:")
        self.destination_label.grid(row=1, column=0, padx=10, pady=10)

        self.destination_entry = Entry(root, width=40)
        self.destination_entry.grid(row=1, column=1, padx=10, pady=10)

        self.browse_destination_btn = Button(root, text="Browse", command=self.browse_destination_directory)
        self.browse_destination_btn.grid(row=1, column=2, padx=10, pady=10)

        self.save_btn = Button(root, text="Save Directories", command=self.save_directories)
        self.save_btn.grid(row=2, column=1, padx=10, pady=10)

        self.start_watch_btn = Button(root, text="Start Watching", command=self.start_watching)
        self.start_watch_btn.grid(row=3, column=1, padx=10, pady=10)

        self.observer = None  # Observer instance

        self.load_directories()

    def browse_source_directory(self):
        source_dir = filedialog.askdirectory()
        self.source_entry.delete(0, 'end')
        self.source_entry.insert(0, source_dir)

    def browse_destination_directory(self):
        destination_dir = filedialog.askdirectory()
        self.destination_entry.delete(0, 'end')
        self.destination_entry.insert(0, destination_dir)

    def save_directories(self):
        source_dir = self.source_entry.get()
        destination_dir = self.destination_entry.get()

        if source_dir and destination_dir:
            with open("directories.txt", "w") as file:
                file.write(f"Source Directory: {source_dir}\n")
                file.write(f"Destination Directory: {destination_dir}\n")
            messagebox.showinfo("Directories Saved", "Directories have been saved successfully.")
        else:
            messagebox.showerror("Error", "Both source and destination directories must be provided.")

    def load_directories(self):
        try:
            with open("directories.txt", "r") as file:
                lines = file.readlines()
                source_dir = lines[0].split(":")[1].strip()
                destination_dir = lines[1].split(":")[1].strip()

                self.source_entry.insert(0, source_dir)
                self.destination_entry.insert(0, destination_dir)
        except FileNotFoundError:
            pass

    def start_watching(self):
        source_dir = self.source_entry.get()
        destination_dir = self.destination_entry.get()

        if source_dir and destination_dir:
            event_handler = WhatsAppDownloadHandler(source_dir, destination_dir)
            self.observer = Observer()
            self.observer.schedule(event_handler, path=source_dir, recursive=False)
            self.observer.start()

            self.root.iconify()
            self.root.after(100, self.check_observer)
        else:
            messagebox.showerror("Error", "Both source and destination directories must be provided.")

    def check_observer(self):
        if self.observer and self.observer.is_alive():
            self.root.after(100, self.check_observer)
        else:
            print("Observer stopped.")
            self.root.deiconify()  # Restore the main window

if __name__ == "__main__":
    root = Tk()
    gui = WhatsAppAutomationGUI(root)
    root.mainloop()
