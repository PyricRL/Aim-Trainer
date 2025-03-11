# ----- 3rd Party Libraries -----
from PySide6.QtCore import QObject, Signal

# ----- Built-In Libraries ------
import random

# -------- Local Files ----------
from utils import *
from target import *

class Tracker(QObject):
    def __init__(self, totalTime, window):
        super().__init__()
        self.totalTime = totalTime
        self.randx = 0
        self.randy = 0
        self.window = window
        self.signal = Signal(int, int, name="positionsSent")

    def sendSpawnSignal(self):
        global targetsOnScreen
        while targetsOnScreen <= 20:
            self.randx = random.randint(50, self.window.width() - 50)
            self.randy = random.randint(50, self.window.height() - 50)
            self.signal.emit(self.randx, self.randy)
            targetsOnScreen += 1