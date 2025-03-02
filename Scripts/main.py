# ----- 3rd Party Libraries -----
from PySide6.QtWidgets import QApplication

# ----- Built-In Libraries ------
import sys

# -------- Local Files ----------
from gui import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Wait for user input and handle event
    sys.exit(app.exec())