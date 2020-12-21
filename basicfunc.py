import cv2 as cv

img = cv.imread("Photos/park.jpeg")
# cv.imshow('Dog',img)

# image to greyscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", gray)

# blur image

blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# Edge cascade
canny = cv.Canny(blur, 125, 170)
# cv.imshow("Canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=1)
# cv.imshow("Dilated", dilated)

# eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow("Eroded", eroded)

# Resize
resize = cv.resize(img, (200, 200))
cv.imshow("Resize", resize)

# cropping
crop = img[50:200, 200:400]
cv.imshow("Crop", crop)



cv.waitKey(0)