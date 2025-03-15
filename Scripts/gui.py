# ----- 3rd Party Libraries -----
from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QStackedWidget
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt

# ----- Built-In Libraries ------


# -------- Local Files ----------
from utils import *
from target import *
from tracker import Tracker
from grid import *

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

        self.tracker = Tracker(1000, window=self)

        # Initialize pages
        self.addMainMenu()
        self.addGridGamePage()
        self.addRandomGamePage()

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

        # Configure Grid Button
        self.startGridButton = QPushButton("Start Grid")
        self.startGridButton.setFixedSize(200, 50)
        self.startGridButton.clicked.connect(self.gameStarted)
        self.startGridButton.setObjectName("startGridButton")

        # Configure Random Button
        self.startRandomButton = QPushButton("Start Random")
        self.startRandomButton.setFixedSize(200, 50)
        self.startRandomButton.clicked.connect(self.gameStarted)
        self.startRandomButton.setObjectName("startRandomButton")
        
        # Add widgets to screeen
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.startGridButton, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.startRandomButton, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Apply layout
        mainMenu.setLayout(layout)

        # Add widget to stackedWidget (creating a page) index 0
        self.stackedWidget.addWidget(mainMenu)
    
    def addGridGamePage(self):
        # Set gridPage as a widget with a box layout
        gridPage = QWidget()
        layout = QVBoxLayout()

        # Configure button
        self.startSessionButton = QPushButton("End Session")
        self.startSessionButton.setFixedSize(200, 50)
        self.startSessionButton.clicked.connect(self.gameStarted)

        # Add widgets to screen
        layout.addWidget(self.startSessionButton, alignment=Qt.AlignmentFlag.AlignBottom)

        # Connect signal output to create circles
        self.tracker.signal.connect(lambda x, y: addTargetsToScreen(x, y, parent=gridPage, window=self))


        # Apply layout
        gridPage.setLayout(layout)

        # Add widget to stackedWidget (creating a page) index 1
        self.stackedWidget.addWidget(gridPage)
    
    def addRandomGamePage(self):
        # Set gridPage as a widget with a box layout
        randomPage = QWidget()
        layout = QVBoxLayout()

        # Configure label
        self.gameLabel = QLabel("This is the random game")
        self.gameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gameLabel.setFont(QFont("Arial", 40))

        # Configure button
        self.startSessionButton = QPushButton("End Session")
        self.startSessionButton.setFixedSize(200, 50)
        self.startSessionButton.clicked.connect(self.gameStarted)

        # Add widgets to screen
        layout.addWidget(self.gameLabel)
        layout.addWidget(self.startSessionButton, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Apply layout
        randomPage.setLayout(layout)

        # Add widget to stackedWidget (creating a page) index 2
        self.stackedWidget.addWidget(randomPage)
    
    def gameStarted(self):
        button = self.sender()

        if button == self.startGridButton:
            GameMode.switch(1)
            self.stackedWidget.setCurrentIndex(1)
            SessionState.sessionStarted = True
            self.tracker.sendSpawnSignal()
        
        elif button == self.startRandomButton:
            GameMode.switch(2)
            self.stackedWidget.setCurrentIndex(2)
            SessionState.sessionStarted = True
        
        else:
            GameMode.reset()
            self.stackedWidget.setCurrentIndex(0)
            SessionState.sessionStarted = False