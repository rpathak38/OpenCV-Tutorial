import cv2
import numpy as np

img = cv2.imread("sudoku.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
cv2.imshow("edges", edges)
cv2.waitKey()
for line in lines:
    rho, theta = line[0]
    (x0, y0) = (np.cos(theta)*rho, np.sin(theta)*rho)
    (x1, y1) = (np.sin(theta)*1000+x0, -np.cos(theta) * 1000+y0)
    (x2, y2) = (np.sin(theta) * -1000 + x0, np.cos(theta) * 1000 + y0)
    cv2.line(img, (int(x2), int(y2)), (int(x1), int(y1)), (255, 255, 0))

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()
