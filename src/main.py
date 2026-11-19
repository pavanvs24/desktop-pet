import sys
import random
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QApplication, QWidget


class PetWindow(QWidget):
    SIZE = 200
    PADDING = 20

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.SIZE, self.SIZE)
        self.move_to_corner()

        self.eyes_open = True
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.toggle_eyes)
        self.timer.start(1000)
    

    def move_to_corner(self):
        area = QApplication.primaryScreen().availableGeometry()
        x = area.x() + area.width() - self.SIZE
        y = area.y() + area.height() - self.SIZE
        self.move(x, y)


    def toggle_eyes(self):
        self.eyes_open = not self.eyes_open

        if self.eyes_open:
            self.timer.start(random.randint(2000, 6000))
        else:
            self.timer.start(120)
        self.update()


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(255, 160, 60))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(
            self.PADDING // 2,
            self.PADDING,
            self.SIZE - self.PADDING,
            self.SIZE - self.PADDING,
        )
        print("opened") if self.eyes_open else print("closed")


app = QApplication(sys.argv)
window = PetWindow()
window.show()
sys.exit(app.exec())
