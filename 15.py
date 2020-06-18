import cv2 as cv
import numpy as np

img1 = cv.imread("img\FIT.jpg")
e1 = cv.getTickCount()
print("e1= ", e1)
for i in range(5, 149, 2):
    img1 = cv.medianBlur(img1, i)
e2 = cv.getTickCount()
print("e2= ", e2)
time = (e2 - e1) / cv.getTickFrequency()
print(time)
print(cv.useOptimized())


