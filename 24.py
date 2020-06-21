import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class MyWin(QWidget):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.setWindowTitle("共产党灭亡")
        self.setGeometry(200, 200, 200, 200)
        btn = QPushButton("Click", self)
        btn.setGeometry(20, 20, 20, 60)
        btn.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWin()
    win.show()
    sys.exit(app.exec_())
