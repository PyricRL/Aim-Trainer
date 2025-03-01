from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout
from PySide6 import QtCore

class AimTrackerUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyric Aim Tracker")
        self.setGeometry(200, 200, 800, 600)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.label = QLabel("Welcome to Pyric Aim Tracker", alignment=QtCore.Qt.AlignCenter)
        button = QPushButton("Start Session")
        button.clicked.connect(self.start_session)

        layout.addWidget(self.label)
        layout.addWidget(button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_session(self):
        self.label.setText("Session Started")