import cv2
import numpy as np

img = cv2.imread("lanes.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img, 50, 150, apertureSize=3)
cv2.imshow("edges", edges)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    (x0, y0, x1, y1) = line[0]
    cv2.line(img, (x0, y0), (x1, y1), (255, 255, 0), 2)

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()