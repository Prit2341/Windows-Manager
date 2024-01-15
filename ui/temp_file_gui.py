# UI/temp_remover_gui.py
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QInputDialog
from Scripts.tempcleaner import delete_temp_files, get_total_temp_file_size, bytes_to_mb, get_cleanup_schedule, modify_cleanup_schedule

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

    def clean_direct(self):
        total_temp_file_size = get_total_temp_file_size()
        mb_size = bytes_to_mb(total_temp_file_size)
        delete_temp_files()
        message = f"Temporary files cleaned successfully.\nTotal size of all temporary files: {mb_size:.2f} MB"
        self.show_popup("Clean Directly", message)

    def set_frequency(self):
        frequency_days, next_cleanup_date = get_cleanup_schedule()

        if frequency_days and next_cleanup_date:
            message = f"Cleaning frequency set to {frequency_days} days.\nNext scheduled cleanup on: {next_cleanup_date.strftime('%Y-%m-%d %H:%M:%S')}"
            self.show_popup("Set Cleaning Frequency", message)
        else:
            self.show_popup("Error", "Cleanup schedule not set. Please enter a valid frequency for cleaning.")

    def modify_schedule(self):
        new_frequency, new_next_cleanup_date = modify_cleanup_schedule()

        if new_frequency and new_next_cleanup_date:
            message = f"Cleaning schedule modified.\nNext scheduled cleanup on: {new_next_cleanup_date.strftime('%Y-%m-%d %H:%M:%S')}"
            self.show_popup("Modify Cleaning Schedule", message)

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
