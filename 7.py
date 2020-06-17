import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("img\img.jpg")
ball = img[20:140, 30:150]
# img[120:140, 130:150] = ball
plt.figure("image")
plt.imshow(ball)
plt.axis("on")
plt.title("Matplotlib")
plt.show()
# cv.namedWindow("image")
# cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()
