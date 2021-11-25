from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor, QPainter
from PyQt5 import uic
import sys
import random


class MainP(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton1.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        y = random.randrange(10, 200, 10)
        qp.drawEllipse(random.randrange(10, 400, 10), random.randrange(10, 400, 10), y, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainP()
    ex.show()
    sys.exit(app.exec())