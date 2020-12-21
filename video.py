import cv2 as cv
import numpy as np


def framresize(frame, scale=0.5):
    # Imgs, Vids and Live Videos
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)

    dimension = (w, h)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(0)
# blank = np.zeros(capture.shape, dtype="uint8")


while True:
    isTrue, frame = capture.read()
    rescale = framresize(frame, scale=0.4)
    cv.imshow("Video resize", rescale)
    cv.imshow("Video", frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
    canny = cv.Canny(blur, 125, 170)
    # cv.imshow("Canny", canny)
    contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    # print(f"{len(contours)} contours found")
    cv.drawContours(frame, contours, -1, (0, 0, 255), 2)
    cv.imshow("Contours Drawn", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break


capture.release()
cv.destroyAllWindows()