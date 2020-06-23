import sys
from ui_Test2 import Ui_Form as Ui_Test1
from ui_Test3 import Ui_Form as Ui_Test2
from PyQt5.QtWidgets import QApplication, QWidget


class MyClass1(QWidget, Ui_Test1):
    def __init__(self, parent=None):
        super(MyClass1, self).__init__(parent)
        self.setupUi(self)


class MyClass2(QWidget, Ui_Test2):
    def __init__(self, parent=None):
        super(MyClass2, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win1 = MyClass1()
    win2 = MyClass2()
    win1.show()
    win2.show()
    sys.exit(app.exec_())
