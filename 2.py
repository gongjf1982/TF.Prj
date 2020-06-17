import cv2 as cv
import numpy as np

# img = np.zeros((512, 512, 3), np.uint8)
img = cv.imread("img\FIT.jpg")
font = cv.FONT_HERSHEY_COMPLEX_SMALL
cv.line(img, (20, 20), (250, 250), (255, 0, 0), 5)
cv.rectangle(img, (100, 100), (350, 350), (0, 255, 0), 3)
cv.putText(img, "OpenCV", (500, 500), font, 10, (0, 0, 255), 2, cv.LINE_AA)
cv.namedWindow("image", cv.WINDOW_NORMAL)
cv.resizeWindow("image", 600, 400)
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()