# ----- 3rd Party Libraries -----
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import QRect, Qt

# ----- Built-In Libraries ------

# -------- Local Files ----------

class Target(QWidget):
    def __init__(self, x, y, outerDiameter=50, diameter=50, color=QColor(255, 0, 0), borderColor=QColor(0, 0, 0, 0), parent=None):
        QWidget.__init__(self, parent)
        self.x = x
        self.y = y

        self.diameter = diameter

        self.color = color
        self.borderColor = borderColor

        self.setGeometry(x, y, outerDiameter * 2, outerDiameter * 2)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Target Drawing
        painter.setBrush(self.color)
        painter.setPen(QPen(self.borderColor))
        painter.drawEllipse(QRect(self.x, self.y, self.diameter, self.diameter))
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print(event.pos())