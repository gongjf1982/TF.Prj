import sys
from ui_Test2 import Ui_Form as Ui_Test1
from ui_Test3 import Ui_Form as Ui_Test2
from ui_Test4 import Ui_Form as Ui_Test3
from ui_Test5 import Ui_MainWindow as Ui_Test4
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyClass1(QWidget, Ui_Test1):
    def __init__(self, parent=None):
        super(MyClass1, self).__init__(parent)
        self.setupUi(self)


class MyClass2(QWidget, Ui_Test2):
    def __init__(self, parent=None):
        super(MyClass2, self).__init__(parent)
        self.setupUi(self)


class MyClass3(QWidget, Ui_Test3):
    def __init__(self, parent=None):
        super(MyClass3, self).__init__(parent)
        self.setupUi(self)


class MyClass4(QMainWindow, Ui_Test4):
    def __init__(self, parent=None):
        super(MyClass4, self).__init__(parent)
        self.setupUi(self)
        self.action_O.triggered.connect(self.close)
        self.action_N.triggered.connect(self.big)
        self.action_X.triggered.connect(self.xxoo)

    def big(self):
        print("你点击了新建按钮")
        self.statusbar.showMessage("状态栏，新建")

    def xxoo(self):
        print("XXOO")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win1 = MyClass1()
    win2 = MyClass2()
    win3 = MyClass3()
    win4 = MyClass4()
    # win1.show()
    # win2.show()
    # win3.show()
    win4.show()
    sys.exit(app.exec_())
