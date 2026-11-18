import sys
from PySide6.QtCore import Qt
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

    def move_to_corner(self):
        area = QApplication.primaryScreen().availableGeometry()
        x = area.x() + area.width() - self.SIZE
        y = area.y() + area.height() - self.SIZE
        self.move(x, y)

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

app = QApplication(sys.argv)
window = PetWindow()
window.show()
sys.exit(app.exec())
