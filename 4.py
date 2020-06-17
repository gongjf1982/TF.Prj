import cv2 as cv
import numpy as np

drawing = False
mode = True
ix, iy = -1, -1


def deaw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        # print("drawing=", drawing, " ix,iy=", ix, iy)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        if drawing == True:
            # print("drawing=", drawing, " ix,iy=", ix, iy)
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), -1)
                print("矩形")
            else:
                cv.circle(img, (x, y), 1, (0, 255, 0), -1)
                print("圆形")
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False


img = cv.imread("img\FIT.jpg", cv.WINDOW_NORMAL)
cv.namedWindow("Button")
cv.setMouseCallback("Button", deaw_circle)
while (True):
    cv.resizeWindow("Button", 600, 400)
    cv.imshow("Button", img)
    k = cv.waitKey(1)
    if k == ord("m"):
        mode = not mode
    elif k == ord("q"):
        break
cv.destroyAllWindows()
