import numpy as np
import cv2

img = cv2.imread("opencv-logo.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval, thresh = cv2.threshold(imgray, 200, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#contours is a python list of all the contours in the image. Each element of the contours aray is a list of contour points

print("Number of contours", len(contours))

img = cv2.drawContours(img, contours, -1, [255, 255, 0], 3)

cv2.imshow("image", img)
cv2.imshow("image gray", imgray)
cv2.waitKey()
cv2.destroyAllWindows()