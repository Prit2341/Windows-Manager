import tempfile
import os
from datetime import datetime, timedelta
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QInputDialog

class TempFileCleanerGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        clean_direct_btn = QPushButton("Clean Temporary Files", self)
        clean_direct_btn.clicked.connect(self.clean_direct)
        layout.addWidget(clean_direct_btn)

        set_frequency_btn = QPushButton("Set Cleaning Frequency", self)
        set_frequency_btn.clicked.connect(self.set_frequency)
        layout.addWidget(set_frequency_btn)

        modify_schedule_btn = QPushButton("Modify Cleaning Schedule", self)
        modify_schedule_btn.clicked.connect(self.modify_schedule)
        layout.addWidget(modify_schedule_btn)

        self.setLayout(layout)
        self.setGeometry(300, 300, 240, 120)
        self.setWindowTitle("Temp File Cleaner")

    def bytes_to_mb(self, bytes_value):
        mb_value = bytes_value / (1024 * 1024)
        return mb_value

    def get_total_temp_file_size(self):
        temp_dir = tempfile.gettempdir()
        temp_files = [f for f in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, f))]
        total_size = 0
        for file in temp_files:
            file_path = os.path.join(temp_dir, file)
            total_size += os.path.getsize(file_path)
        return total_size

    def is_file_running(self, file_path):
        try:
            with open(file_path, 'r'):
                return True
        except IOError:
            return False

    def delete_temp_files(self):
        temp_dir = tempfile.gettempdir()
        temp_files = [f for f in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, f))]
        for file in temp_files:
            file_path = os.path.join(temp_dir, file)
            try:
                if self.is_file_running(file_path):
                    pass
                else:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
            except Exception as e:
                pass

    def clean_direct(self):
        total_temp_file_size = self.get_total_temp_file_size()
        mb_size = self.bytes_to_mb(total_temp_file_size)
        self.delete_temp_files()
        message = f"Temporary files cleaned successfully.\nTotal size of all temporary files: {mb_size:.2f} MB"
        self.show_popup("Clean Directly", message)

    def set_frequency(self):
        try:
            frequency_days, ok = QInputDialog.getInt(self, "Set Cleaning Frequency", "Enter how often you want to clean your temp files (in days):")
            if ok:
                next_cleanup_date = datetime.now() + timedelta(days=frequency_days)
                message = f"Cleaning frequency set to {frequency_days} days.\nNext scheduled cleanup on: {next_cleanup_date.strftime('%Y-%m-%d %H:%M:%S')}"
                self.show_popup("Set Cleaning Frequency", message)
        except ValueError:
            self.show_popup("Error", "Invalid input. Please enter a valid number.")

    def modify_schedule(self):
        try:
            frequency_days, ok = QInputDialog.getInt(self, "Modify Cleaning Schedule", "Enter how often you want to clean your temp files (in days):")
            if ok:
                next_cleanup_date = datetime.now() + timedelta(days=frequency_days)
                message = f"Cleaning schedule modified.\nNext scheduled cleanup on: {next_cleanup_date.strftime('%Y-%m-%d %H:%M:%S')}"
                self.show_popup("Modify Cleaning Schedule", message)
        except ValueError:
            self.show_popup("Error", "Invalid input. Please enter a valid number.")

    def show_popup(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__ == '__main__':
    app = QApplication([])
    temp_file_cleaner_gui = TempFileCleanerGUI()
    temp_file_cleaner_gui.show()
    app.exec_()
