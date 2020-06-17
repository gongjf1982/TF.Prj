import cv2 as cv
import numpy as np


def nothin(x):
    pass


img = cv.imread("img\FIT.jpg", cv.WINDOW_NORMAL)
# img = np.zeros((255, 255, 255), np.uint8)
cv.namedWindow('image')
switch = "0:OFF\n1:ON"
cv.createTrackbar("R", 'image', 0, 255, nothin)
cv.createTrackbar("G", 'image', 0, 255, nothin)
cv.createTrackbar("B", 'image', 0, 255, nothin)
cv.createTrackbar(switch, 'image', 0, 1, nothin)
while (True):
    cv.resizeWindow('image', 400, 300)
    cv.imshow('image', img)
    k = cv.waitKey(1)
    if k == ord("q"):
        break
    r = cv.getTrackbarPos("R", 'image')
    g = cv.getTrackbarPos("G", 'image')
    b = cv.getTrackbarPos("B", 'image')
    s = cv.getTrackbarPos(switch, 'image')
    print("r=", r, " g=", g, " b=", b)
    if s == 0:
        print(0)
        # img[:] = 0
    else:
        print(1)
        # img[:] = [r, g, b]
cv.destroyAllWindows()
