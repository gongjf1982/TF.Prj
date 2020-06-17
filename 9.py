import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("img\img.jpg")
red = [255, 0, 0]
p1 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REPLICATE)
p2 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT)
p3 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT101)
p4 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_WRAP)
p5 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=red)
plt.subplot(231), plt.imshow(p1, 'gray'), plt.title("p1")
plt.subplot(232), plt.imshow(p2, 'gray'), plt.title("p2")
plt.subplot(233), plt.imshow(p3, 'gray'), plt.title("p3")
plt.subplot(234), plt.imshow(p4, 'gray'), plt.title("p4")
plt.subplot(235), plt.imshow(p5, 'gray'), plt.title("p5")
plt.subplot(236), plt.imshow(img, 'gray'), plt.title("img")
plt.show()

# cv.namedWindow("image")
# cv.imshow("image", img)
# cv.waitKey(0)
# cv.destroyAllWindows()
