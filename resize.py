import cv2 as cv


def framresize(frame, scale=0.5):
    # Imgs, Vids and Live Videos
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)

    dimension = (w, h)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


# def changres(wid,high):
#     # Live vids online
#     capture.set(3,wid)
#     capture.set(4,high)


# img = cv.imread("Photos/dog2.jpeg")
# rescale_img = framresize(img)
# cv.imshow('Dog', img)
# cv.imshow('Dog resize', rescale_img)

# cv.waitKey(0)


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    rescale = framresize(frame, scale=0.4)
    cv.imshow("Video resize", rescale)
    cv.imshow("Video", frame)
    canny = cv.Canny(frame, 125, 170)
    cv.imshow("Canny", canny)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break


capture.release()
cv.destroyAllWindows()
