import numpy as np
import cv2 as cv


def printer(x):
    print(x)


# Create a black image, a window
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow("image", cv.WINDOW_AUTOSIZE)

cv.createTrackbar("B", "image", 0, 255, printer)
cv.createTrackbar("G", "image", 0, 255, printer)
cv.createTrackbar("R", "image", 0, 255, printer)

switch = "0 : OFF\n 1 : ON"
cv.createTrackbar(switch, "image", 0, 1, printer)

while True:
    cv.imshow("image", img)
    k = cv.waitKey(1)
    if k == 27:
        break
    b = cv.getTrackbarPos("B", "image")
    g = cv.getTrackbarPos("G", "image")
    r = cv.getTrackbarPos("R", "image")
    s = cv.getTrackbarPos(switch, "image")

    if s == 0:
        img[:, :] = 0

    else:
        img[:, :] = [b, g, r]

cv.destroyAllWindows()
