import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
# blank = np.zeros(capture.shape, dtype="uint8")

haar_cascade = cv.CascadeClassifier('haar_face.xml')

while True:
    isTrue, frame = capture.read()
    flipimg = cv.flip(frame, 1)
    grayFrame = cv.cvtColor(flipimg, cv.COLOR_BGR2GRAY)
    face_detect = haar_cascade.detectMultiScale(grayFrame, scaleFactor=1.1, minNeighbors=3)
    for (x,y,w,h) in face_detect:
        cv.rectangle(flipimg, (x, y), (x+w, y+h), (0,255,0), thickness=2)
    cv.imshow("video bw", grayFrame)
    cv.imshow("video original", flipimg)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break




capture.release()
cv.destroyAllWindows()
