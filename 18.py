import cv2 as cv

img = cv.imread("img\FIT.jpg")
rows, cols = img.shape[:2]
print(rows, cols)
cv.imshow("img", img)
M = cv.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.6)
cv.imshow("M", M)
dst = cv.warpAffine(img, M, (2 * cols, 2 * rows))
cv.imshow("dst", dst)
cv.waitKey(0)
cv.destroyAllWindows()
