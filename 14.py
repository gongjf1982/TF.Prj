import numpy as np
import cv2 as cv

x = np.uint8([250])
y = np.uint8([10])
print(x, type(x))
print(y, type(y))
print(cv.add(x, y), type(cv.add(x, y)))
print(x + y, type(x + y))

img1 = cv.imread("img\FIT.jpg")
img2 = cv.imread("img\win.jpg")
img3 = cv.imread("img\logo.png")
dst = cv.addWeighted(img1, 0.7, img2, 0.3, 2)
# cv.namedWindow("image")
# cv.imshow("image", dst)

rows, cols, channels = img3.shape
print(rows, cols, channels)
roi = img1[0:rows, 0:cols]
img2gray = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)
# cv.namedWindow("image")
# cv.imshow("image", img2gray)
ret, mask = cv.threshold(img2gray, 175, 255, cv.THRESH_BINARY)
print("---", ret, mask, "---")
# cv.namedWindow("mask")
# cv.imshow("mask", mask)
mask_inv = cv.bitwise_not(mask)
# cv.namedWindow("mask_inv")
# cv.imshow("mask_inv", mask_inv)
img1_bg = cv.bitwise_and(roi, roi, mask=mask)
# cv.namedWindow("img1_bg")
# cv.imshow("img1_bg", img1_bg)
img1_fg = cv.bitwise_and(img3, img3, mask=mask_inv)
# cv.namedWindow("img1_fg")
# cv.imshow("img1_fg", img1_fg)
dst = cv.add(img1_bg, img1_fg)
img1[0:rows, 0:cols] = dst
cv.namedWindow("dst")
cv.imshow("dst", img1)
cv.waitKey(0)
cv.destroyAllWindows()
