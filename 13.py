import sys
import tensorflow as tf
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import testUi
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    ui = testUi.Ui_Form()
    ui.setupUi(win)

    # win.resize(400, 200)
    # win.move(400, 400)
    # win.setWindowTitle("Tensorflow, Keras")

    win.show()
    sys.exit(app.exec_())
