import cv2 as cv

img = cv.imread("D:\TF.Prj\img\FIT.jpg")
rows, cols, dims = img.shape[:]
res1 = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
res2 = cv.resize(img, dsize=(2 * cols, 2 * rows), interpolation=cv.INTER_CUBIC)
cv.imshow("image", img)
cv.imshow("res1", res1)
cv.imshow("res2", res2)
cv.waitKey(0)
cv.destroyAllWindows()
