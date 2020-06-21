import sys
import cv2 as cv
import numpy as np
import matplotlib

matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from matplotlib.figure import Figure as fg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as fc
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout


class Fg(fc):
    def __init__(self, width, height, dpi):
        self.fig = fg(figsize=(width, height), dpi=dpi)
        super(Fg, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)


class MyWidget(QWidget):
    def __init__(self, prarent=None):
        super(MyWidget, self).__init__(prarent)
        self.F = Fg(width=4, height=3, dpi=100)
        self.countdot()  # 采集需要画的点位
        self.plotcos(self.t, self.s)  # 画 图

        # 在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）。
        # self.gridlayout = QGridLayout(self.groupBox)
        # self.gridlayout.addWidget(self.F)

    def countdot(self):
        self.t = np.arange(0.0, 5.0, 0.01)
        self.s = np.cos(2 * np.pi * self.t)
        # self.t = [0,1,2,3,4,5]
        # self.s = [0,1,2,3,4,5]

    def plotcos(self, x, y):
        self.F.axes.plot(x, y)
        self.F.fig.suptitle("cos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec_())
