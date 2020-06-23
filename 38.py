import sys
from ui_Test61 import Ui_ChildrenForm2 as Ui_Test1
from ui_Test62 import Ui_MainForm2 as Ui_Test2
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyClass1(QWidget, Ui_Test1):
    def __init__(self, parent=None):
        super(MyClass1, self).__init__(parent)
        self.setupUi(self)


class MyClass2(QMainWindow, Ui_Test2):
    def __init__(self, parent=None):
        super(MyClass2, self).__init__(parent)
        self.setupUi(self)
        self.Child = MyClass1()
        self.actionClose_X.triggered.connect(self.close)
        self.actionNew_N.triggered.connect(self.new)
        self.actionOpen_O.triggered.connect(self.open)

    def new(self):
        print("你点击了新建按钮")
        self.MaingridLayout.addWidget(self.Child)
        self.Child.show()
        self.statusbar.showMessage("状态栏，新建")

    def open(self):
        print("你点击了打开按钮")
        self.statusbar.showMessage("状态栏，打开")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # win1 = MyClass1()
    win2 = MyClass2()
    # win1.show()
    win2.show()
    sys.exit(app.exec_())
