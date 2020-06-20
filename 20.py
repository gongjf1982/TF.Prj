import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("img\FIT.jpg")
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
title = ["Orig", "Binary", "Binary_inv", "Trunc", "toZero", "toZero_inv"]
imgs = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(imgs[i]), plt.title(title[i])
    plt.xticks([]), plt.yticks([])
plt.show()
cv.imshow("OpenCV", img)
cv.waitKey(0)
cv.destroyAllWindows()
