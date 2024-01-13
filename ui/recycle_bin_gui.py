import winshell
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class RecycleBinGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        recycle_bin_label = QLabel("Recycle Bin", self)
        layout.addWidget(recycle_bin_label)

        clean_btn = QPushButton("Clean Recycle Bin Now", self)
        clean_btn.clicked.connect(self.clean_recycle_bin)
        layout.addWidget(clean_btn)

        self.setLayout(layout)
        self.setGeometry(100, 100, 240, 240)
        self.setWindowTitle("Recycle Bin")

    def clean_recycle_bin(self):
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
            QMessageBox.information(self, "Recycle Bin", "Recycle bin is emptied now!")
        except Exception as e:
            QMessageBox.critical(self, "Recycle Bin", f"Error: {e}\nFailed to empty the recycle bin.")
