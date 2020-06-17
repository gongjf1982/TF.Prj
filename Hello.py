import tensorflow as tf
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print(tf.__version__)
img = cv.imread("img\img.jpg")
cv.namedWindow("OpenCV", cv.WINDOW_NORMAL)
cv.imshow("OpenCV", img)
k = cv.waitKey(0) & 0xFF
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite("555.png", img)
    cv.destroyAllWindows()
plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([])
plt.yticks([])
plt.show()
