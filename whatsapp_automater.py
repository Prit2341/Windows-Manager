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
    messagebox.showinfo("Info", "Temporary files cleaned successfully.")
    observer.join()
