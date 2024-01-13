import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from ui.recycle_bin_gui import RecycleBinGUI  # Updated import
from cleaner import clean_recycle_bin, set_cleaning_frequency, get_cleaning_frequency

class RecycleBinCleanerGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        clean_btn = QPushButton("Clean Recycle Bin Now", self)
        clean_btn.clicked.connect(self.clean_recycle_bin)
        layout.addWidget(clean_btn)

        add_days_btn = QPushButton("Add Days for Cleaning", self)
        add_days_btn.clicked.connect(self.add_days_dialog)
        layout.addWidget(add_days_btn)

        modify_days_btn = QPushButton("Modify Cleaning Frequency", self)
        modify_days_btn.clicked.connect(self.modify_days_dialog)
        layout.addWidget(modify_days_btn)

        recycle_bin_btn = QPushButton("Open Recycle Bin GUI", self)
        recycle_bin_btn.clicked.connect(self.open_recycle_bin_gui)
        layout.addWidget(recycle_bin_btn)

        self.setLayout(layout)
        self.setGeometry(100, 100, 240, 240)
        self.setWindowTitle("Recycle Bin Cleaner")

    def clean_recycle_bin(self):
        result = clean_recycle_bin()
        self.show_popup(result)

    def add_days_dialog(self):
        days, ok = QInputDialog.getInt(self, "Add Days", "Enter how many days after you want to clean your recycle bin:")
        if ok:
            result = set_cleaning_frequency(days)
            self.show_popup(result)

    def modify_days_dialog(self):
        current_days = get_cleaning_frequency()
        days, ok = QInputDialog.getInt(self, "Modify Cleaning Frequency", "Enter how often you want to clean your recycle bin (in days):", current_days)
        if ok:
            result = set_cleaning_frequency(days)
            self.show_popup(result)

    def open_recycle_bin_gui(self):
        recycle_bin_gui = RecycleBinGUI()
        recycle_bin_gui.show()

    def show_popup(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Recycle Bin Cleaner")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RecycleBinCleanerGUI()
    window.show()
    sys.exit(app.exec_())
