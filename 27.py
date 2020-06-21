from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
import cv2 as cv
import sys

if __name__ == "__main__":
    img = cv.cvtColor(cv.imread("img\FIT.jpg"), cv.COLOR_BGR2RGB)
    # img = cv.imread("img\FIT.jpg")
    QtImg = QImage(img.data, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("OpenCV图片显示")
    win.resize(img.shape[1], img.shape[0])
    # btn = QPushButton("Close", win)
    label = QLabel("img", win)
    label.setPixmap(QPixmap(QtImg))
    win.show()
    sys.exit(app.exec_())
