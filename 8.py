import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("img\img.jpg")
r, g, b = cv.split(img)
src = img
dst = cv.merge([r, g, b])
plt.figure("OpenCV")
plt.axis("on")
plt.suptitle("Mat")
plt.subplot(2, 3, 1)
plt.imshow(r)
plt.subplot(2, 3, 2)
plt.imshow(g)
plt.subplot(2, 3, 3)
plt.imshow(b)
plt.subplot(2, 3, 4)
plt.imshow(src)
plt.subplot(2, 3, 5)
plt.imshow(dst)
plt.show()

cv.namedWindow("image")
imgs = np.hstack([r, g, b])
cv.imshow("image", imgs)
cv.waitKey(0)
cv.destroyAllWindows()
