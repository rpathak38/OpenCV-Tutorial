import cv2
import numpy


def nothing(x):
    pass


cv2.namedWindow("Tracking")
cv2.createTrackbar("Lower Hue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower Saturation", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower Value", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Upper Hue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper Saturation", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper Value", "Tracking", 255, 255, nothing)
# We use Hue, Saturation, and Value instead of Regular RBG as this method allows us to remove the effects of
# bright/dim light hitting an object


cap = cv2.VideoCapture(0)
while True:

    _, frame = cap.read()
    print(_)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Hue, Saturation, and Value
    l_b = numpy.array([cv2.getTrackbarPos("Lower Hue", "Tracking"), cv2.getTrackbarPos("Lower Saturation", "Tracking"),
                       cv2.getTrackbarPos("Lower Value", "Tracking")])
    u_b = numpy.array([cv2.getTrackbarPos("Upper Hue", "Tracking"), cv2.getTrackbarPos("Upper Saturation", "Tracking"),
                       cv2.getTrackbarPos("Upper Value", "Tracking")])
    print(l_b)
    print(u_b)
    # Defining the upper and lower bounds for our array of values (Basically how blue our blues will be)

    mask = cv2.inRange(hsv, l_b, u_b)
    # this allows us to see all the positions for which the colors are in the range specified

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)

    if key == ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        break
