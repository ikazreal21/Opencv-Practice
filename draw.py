import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
cv.imshow("Blank", blank)

# print a certain color
# blank[200:300, 300:400] = 255, 0, 244
# cv.imshow("Green", blank)

# draw a rectangle
# cv.rectangle(blank, (25, 25), (250, 250), (250, 0, 0), thickness=3)
# cv.imshow('Rectangle', blank)


# draw a circle
# cv.circle(blank, (250, 250), 70, (250, 250, 0), thickness=2)
# cv.imshow("Circle", blank)

# # draw a line
# cv.line(blank, (0, 0), (250, 250), (250, 0, 0), thickness=2)
# cv.imshow("Line", blank)

# put a text
cv.putText(
    blank, "Hello", (50, 50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 255), thickness=2
)
cv.imshow("Text", blank)

cv.waitKey(0)

