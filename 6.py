import cv2 as cv
import numpy as np

img = cv.imread("img\img.jpg")
px = img[100, 100]
r = px[0]
g = px[1]
b = px[2]
print(px)
print("r,g,b =", r, g, b)
img[100] = 0
print("--------------------------------------")
print("shape=", img.shape)
print("size", img.size)
print("dtype=", img.dtype)
print(img.item(101, 101, 1), img[101, 101])
cv.namedWindow('image')
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
