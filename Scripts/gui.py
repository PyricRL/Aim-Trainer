# ----- 3rd Party Libraries -----
from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QStackedWidget
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt

# ----- Built-In Libraries ------


# -------- Local Files ----------
from utils import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up window settings
        self.setWindowTitle("Aim Trainer - Home")
        self.setMinimumSize(700, 700)
        self.showMaximized()
        self.setWindowIcon(QIcon("Images/Icon.png"))

        # Create stacked widget
        self.stackedWidget = QStackedWidget(self)
        self.setCentralWidget(self.stackedWidget)

        # Initialize pages
        self.addMainMenu()
        self.addGridPage()

        # Set current page to be index 0 (main menu)
        self.stackedWidget.setCurrentIndex(0)
    
    def addMainMenu(self):
        # Set main menu as a widget with a box layout
        mainMenu = QWidget()
        layout = QVBoxLayout()

        # Configure label
        self.titleLabel = QLabel("Session Not Started")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setFont(QFont("Arial", 40))

        # Configure button
        self.startSessionButton = QPushButton("Start Session")
        self.startSessionButton.setFixedSize(200, 50)
        self.startSessionButton.clicked.connect(self.startSessionClicked)
        
        # Add widgets to screeen
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.startSessionButton, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Apply layout
        mainMenu.setLayout(layout)

        # Add widget to stackedWidget (creating a page)
        self.stackedWidget.addWidget(mainMenu)
    
    def addGridPage(self):
        # Set gridPage as a widget with a box layout
        gridPage = QWidget()
        layout = QVBoxLayout()

        # Configure label
        self.gameLabel = QLabel("This is the game")
        self.gameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gameLabel.setFont(QFont("Arial", 40))

        # Configure button
        self.startSessionButton = QPushButton("Start Session")
        self.startSessionButton.setFixedSize(200, 50)
        self.startSessionButton.clicked.connect(self.startSessionClicked)

        # Add widgets to screen
        layout.addWidget(self.gameLabel)
        layout.addWidget(self.startSessionButton, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Apply layout
        gridPage.setLayout(layout)

        # Add widget to stackedWidget (creating a page)
        self.stackedWidget.addWidget(gridPage)
    
    def startSessionClicked(self):

        # If session is not started
        if SessionState.sessionStarted == False:

            self.titleLabel.setText("Session Started")
            self.startSessionButton.setText("End Session")
            SessionState.sessionStarted = True

            # Switch to game page
            self.stackedWidget.setCurrentIndex(1)

        # If session is started
        elif SessionState.sessionStarted == True:
            
            self.titleLabel.setText("Sesson Ended")
            self.startSessionButton.setText("Start Session")
            SessionState.sessionStarted = False

            # Switch to game page
            self.stackedWidget.setCurrentIndex(0)

        else:
            print("error")