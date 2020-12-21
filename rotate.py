import cv2 as cv
import numpy as np


img = cv.imread("Photos/dog3.jpeg")


def rotate(img, angle, rotpnt=None):
    (height, width) = img.shape[:2]

    if rotpnt is None:
        rotpnt = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotpnt, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

# rotate
rotate = rotate(img, 90)
cv.imshow("Rotate", rotate)

# resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resize", resize)

#Flip
flip = cv.flip(img, -1) 
cv.imshow('Flip',flip)

cv.waitKey(0)
