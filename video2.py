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
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteFrame) = cv.threshold(grayFrame, 127, 255, cv.THRESH_BINARY)
    cv.imshow("video bw", blackAndWhiteFrame)
    cv.imshow("video original", frame)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break


capture.release()
cv.destroyAllWindows()
