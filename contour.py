import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpeg")
cv.imshow("Img", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 170)
cv.imshow("Canny", canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contours found")

cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)