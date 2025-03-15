# ----- 3rd Party Libraries -----
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QRect, Qt

# ----- Built-In Libraries ------

# -------- Local Files ----------
import utils

class Target(QWidget):
    def __init__(self, x, y, diameter=50, color=QColor(255, 0, 0), borderColor=QColor(0, 0, 0, 0), parent=None, window=None):
        QWidget.__init__(self, parent)
        self.x = x
        self.y = y

        self.diameter = diameter

        self.color = color
        self.borderColor = borderColor

        self.window = window

        self.setGeometry(x, y, self.diameter, self.diameter)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Target Drawing
        painter.setBrush(self.color)
        painter.setPen(QPen(self.borderColor))
        painter.drawEllipse(QRect(0, 0, self.diameter, self.diameter))
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.deleteTarget()
            utils.targetsOnScreen -= 1
            print("target removed")
            print(utils.targetsOnScreen)
    
    def deleteTarget(self):
        self.setParent(None)
        self.deleteLater()