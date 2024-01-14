import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from datetime import datetime, timedelta
from tempcleaner import bytes_to_mb, get_total_temp_file_size, delete_temp_files, get_cleanup_schedule, modify_cleanup_schedule

class TempFileCleanerGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.info_label = QLabel("Welcome to Temp File Cleaner GUI!", self)
        layout.addWidget(self.info_label)

        clean_btn = QPushButton("Clean Temporary Files", self)
        clean_btn.clicked.connect(self.clean_temp_files)
        layout.addWidget(clean_btn)

        modify_btn = QPushButton("Modify Cleaning Schedule", self)
        modify_btn.clicked.connect(self.modify_cleanup_schedule)
        layout.addWidget(modify_btn)

        exit_btn = QPushButton("Exit", self)
        exit_btn.clicked.connect(self.exit_program)
        layout.addWidget(exit_btn)

        self.setLayout(layout)
        self.setWindowTitle("Temp File Cleaner GUI")

    def clean_temp_files(self):
        frequency_days, next_cleanup_date = get_cleanup_schedule()

        total_temp_file_size = get_total_temp_file_size()
        mb_size = bytes_to_mb(total_temp_file_size)

        info_text = f"Current total size of all temporary files: {mb_size:.2f} MB\n"

        if frequency_days and next_cleanup_date:
            info_text += f"Next scheduled cleanup on: {next_cleanup_date.strftime('%Y-%m-%d %H:%M:%S')}\n"

            # Call the function to delete the temporary files
            delete_temp_files(mb_size)
            info_text += "Temporary files cleaned successfully."
        else:
            info_text += "Cleanup schedule not set. Please enter a valid frequency for cleaning."

        self.show_info_popup("Cleaning Results", info_text)

    def modify_cleanup_schedule(self):
        new_frequency, new_next_cleanup_date = modify_cleanup_schedule()

        if new_frequency and new_next_cleanup_date:
            info_text = f"Cleaning frequency modified to: {new_frequency} days\n"
            info_text += f"Next scheduled cleanup on: {new_next_cleanup_date.strftime('%Y-%m-%d %H:%M:%S')}"
            self.show_info_popup("Modification Results", info_text)

    def exit_program(self):
        sys.exit()

    def show_info_popup(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    temp_file_cleaner_gui = TempFileCleanerGUI()
    temp_file_cleaner_gui.show()

    # Check if the application is not already running before starting the event loop
    if not app.exec_():
        sys.exit()
