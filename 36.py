from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from ui_Test1 import Ui_MainWindow


class MyUi(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyUi, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyUi()
    win.show()
    sys.exit(app.exec_())
