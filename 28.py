import cv2 as cv
import sys
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QWidget()
    cap = cv.VideoCapture(0)
    # img = cv.imread("img\FIT.jpg")
    while (True):
        ret, img = cap.read()
        # cv.imshow("img", img)
        QtImg = QImage(img.data, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_BGR888)
        label = QLabel("img", win)
        label.setPixmap(QPixmap(QtImg))
        win.resize(img.shape[1], img.shape[0])
        win.show()
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv.destroyAllWindows()
    sys.exit(app.exec_())
