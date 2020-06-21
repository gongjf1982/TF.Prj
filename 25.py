import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# from matplotlib.font_manager import FontProperties

if __name__ == "__main__":
    img = cv.imread("img\FIT.jpg", cv.IMREAD_GRAYSCALE)
    kernel = np.ones((9, 9), np.uint8)
    erode = cv.erode(img, kernel, iterations=1)
    dilate = cv.dilate(img, kernel, iterations=1)
    open = cv.morphologyEx(img, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_OPEN, (5, 5)))
    close = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    gradiend = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
    tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
    blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
    print(cv.getStructuringElement(cv.MORPH_OPEN, (5, 5)))
    # cv.imshow("img", img)
    # cv.imshow("erode", erode)
    # cv.imshow("dilate", dilate)
    # cv.imshow("oepn", open)
    # cv.imshow("close", close)
    # cv.imshow("gradiend", gradiend)
    # cv.imshow("tophat", tophat)
    # cv.imshow("blackhat", blackhat)
    cv.waitKey(0)
    cv.destroyAllWindows()

    titles = ["img", "erode", "dilate", "oepn", "close", "gradiend", "tophat", "blackhat"]
    imgs = [img, erode, dilate, open, close, gradiend, tophat, blackhat]
    for i in range(8):
        # print(i)
        # print(titles[i], "'s Shape number:", imgs[i].shape[:])
        plt.subplot(3, 3, 1 + i), plt.imshow(imgs[i], cmap="gray"), plt.title([titles[i]], fontproperties="SimHei")
        plt.xticks([]), plt.yticks([])
        plt.xlabel("x"), plt.ylabel("y")
    plt.show()
