import cv2 as cv
import numpy as np


# events = [i for i in dir(cv) if "EVENT" in i]
# print(events)

def draw_cirle(event, x, y, flags, param):
    font = cv.FONT_HERSHEY_COMPLEX_SMALL
    if event == cv.EVENT_LBUTTONDBLCLK:
        # cv.circle(img, (x, y), 100, (255, 0, 0), -1)
        cv.putText(img, "OpenCV", (x, y), font, 4, (23, 234, 34))


# img = np.zeros((500, 500, 3), np.uint8)
img = cv.imread("img\FIT.jpg")
cv.namedWindow("image", cv.WINDOW_NORMAL)
cv.resizeWindow("image", 600, 400)
cv.setMouseCallback("image", draw_cirle)

while (True):
    cv.imshow("image", img)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
cv.destroyAllWindows()
