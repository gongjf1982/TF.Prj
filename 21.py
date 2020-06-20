import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("img\FIT.jpg",0)
# cv.imshow("img", img)
img = cv.medianBlur(img, 5)
# cv.imshow("blir", img)

ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
titles = ["Orig image", "Global Threshold v=127", "Adaptive mean thresholding", "Adaptive Gaussian thresholding"]
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# cv.waitKey(0)
# cv.destroyAllWindows()
