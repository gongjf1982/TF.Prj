import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("img\FIT.jpg")
# print(cv.getGaussianKernel())
kernel = np.ones((5, 5), np.float32) / 25
dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
gaussian = cv.GaussianBlur(img, (5, 5), 0)
median = cv.medianBlur(img, 5)
bilateral = cv.bilateralFilter(img, 9, 75, 75)
b, g, r = cv.split(img)
img = cv.merge([r, g, b])
b, g, r = cv.split(dst)
dst = cv.merge([r, g, b])
b, g, r = cv.split(blur)
blur = cv.merge([r, g, b])
b, g, r = cv.split(gaussian)
gaussian = cv.merge([r, g, b])
b, g, r = cv.split(median)
median = cv.merge([r, g, b])
b, g, r = cv.split(bilateral)
bilateral = cv.merge([r, g, b])
plt.subplot(3, 2, 1), plt.imshow(img), plt.title("Orig")
plt.subplot(3, 2, 2), plt.imshow(dst), plt.title("filter2D")
plt.subplot(3, 2, 3), plt.imshow(blur), plt.title("blur")
plt.subplot(3, 2, 4), plt.imshow(gaussian), plt.title("gaussian")
plt.subplot(3, 2, 5), plt.imshow(blur), plt.title("median")
plt.subplot(3, 2, 6), plt.imshow(gaussian), plt.title("bilateral")
plt.xticks([]), plt.yticks([])
plt.show()