# universal_gui.py in global folder
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from UI.recycle_bin_gui import RecycleBinCleanerGUI

class UniversalGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.recycle_bin_gui = None

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        open_recycle_bin_btn = QPushButton("Open Recycle Bin Cleaner", self)
        open_recycle_bin_btn.clicked.connect(self.open_recycle_bin_gui)
        layout.addWidget(open_recycle_bin_btn)

        self.setLayout(layout)
        self.setGeometry(300, 300, 240, 120)
        self.setWindowTitle("Universal GUI")

    def open_recycle_bin_gui(self):
        if not self.recycle_bin_gui:
            self.recycle_bin_gui = RecycleBinCleanerGUI()
            self.recycle_bin_gui.move(self.geometry().center())
        self.recycle_bin_gui.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    universal_gui = UniversalGUI()
    universal_gui.show()
    sys.exit(app.exec_())
