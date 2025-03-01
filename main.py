from PySide6.QtWidgets import QApplication
import sys

from gui import AimTrackerUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AimTrackerUI()
    window.show()

    with open("style.qss", "r") as f:   
        app.setStyleSheet(f.read())

    sys.exit(app.exec())