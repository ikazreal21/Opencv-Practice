import cv2 as cv
import numpy as np

capture = cv.VideoCapture("Videos/drive2.mp4")
# blank = np.zeros(capture.shape, dtype="uint8")

haar_cascade = cv.CascadeClassifier("cars.xml")

while True:
    isTrue, frame = capture.read()
    flipimg = cv.flip(frame, 1)
    grayFrame = cv.cvtColor(flipimg, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(grayFrame, (3, 3), cv.BORDER_DEFAULT)
    sabog_detection = haar_cascade.detectMultiScale(
        blur, scaleFactor=1.1, minNeighbors=3)
    for (x, y, w, h) in sabog_detection:
        cv.rectangle(flipimg, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    cv.imshow("video original", flipimg)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break


capture.release()
cv.destroyAllWindows()
