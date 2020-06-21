import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        # super(MyWidget, self).__init__()
        self.setWindowTitle("MyWidget")
        self.setGeometry(200, 200, 200, 200)
        btn = QPushButton("Okay", self)
        btn.clicked.connect(sys.exit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec_())
