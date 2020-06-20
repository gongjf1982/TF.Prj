import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("img\FIT.jpg", cv.IMREAD_GRAYSCALE)

# img = cv.imread("img\FIT.jpg")  # 读取彩色图像
# b, g, r = cv.split(img)  # 通道分开
# img_rgb = cv.merge([r, g, b])  # 通道合并

ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
blur = cv.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ["Orginal noisy image", "histogram", "global threshoding v=127",
          "Orginal noisy image", "histogram", "otsu's threshoding",
          "Gaussian giltered image", "histogram", "otus's thresholding", ]
for i in range(3):
    plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3]), plt.title(titles[i * 3])
    plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1])
    plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2]), plt.title(titles[i * 3 + 2])
    plt.xticks([]), plt.yticks([])
plt.show()
