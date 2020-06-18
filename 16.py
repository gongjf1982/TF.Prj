import cv2 as cv
import numpy as np

flag = [i for i in dir(cv) if i.startswith("COLOR_")]
# print(flag)
green = np.uint8([[[77, 159, 213]]])
hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
print(hsv_green)

cap = cv.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([0, 100, 100])
    upper_blue = np.array([28, 255, 255])
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    k = cv.waitKey(10) & 0xFF
    if k == ord("q"):
        break
cv.destroyAllWindows()
