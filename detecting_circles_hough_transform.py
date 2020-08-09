import numpy as np
import cv2

img = cv2.imread("smarties.png")
output = img.copy()
gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=40, minRadius=0, maxRadius=0)
detected_circles = (np.round(circles)).astype(np.uint16)

for (x, y, r) in detected_circles[0]:
    cv2.circle(output, (x, y), r, (255, 0, 0), thickness=3)
    cv2.circle(output, (x, y), 2, (255, 0, 0), thickness=3)

cv2.imshow("output", output)
cv2.waitKey()
cv2.destroyAllWindows()