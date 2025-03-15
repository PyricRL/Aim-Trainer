# ----- 3rd Party Libraries -----
from PySide6.QtCore import QObject, Signal

# ----- Built-In Libraries ------
import random

# -------- Local Files ----------
import utils
from target import *

class Tracker(QObject):
    signal = Signal(int, int, name="positionsSent")

    def __init__(self, totalTime, window):
        super().__init__()
        self.totalTime = totalTime
        self.randx = 0
        self.randy = 0
        self.window = window

    def sendSpawnSignal(self):
        while utils.SessionState.sessionStarted == True:
            if utils.targetsOnScreen < 20:
                self.randx = random.randint(0, self.window.width() - 50)
                self.randy = random.randint(0, self.window.height() - 50)
                self.signal.emit(self.randx, self.randy)
                utils.targetsOnScreen += 1