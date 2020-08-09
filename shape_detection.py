import numpy as np
import cv2

img = cv2.imread("shapes.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    print(contour)
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (255, 0, 0), 3)
    x = approx.flatten()[0]
    y = approx.flatten()[1]

    size = 0.5
    color = (255, 255, 255)
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, size, color, 3)
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        if 0.95<w/h<1.05:
            rec = "square"
        else:
            rec = "rectangle"
        cv2.putText(img, rec, (x, y), cv2.FONT_HERSHEY_SIMPLEX, size, color, 3)
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, size, color, 3)
    elif len(approx) == 6:
        cv2.putText(img, "Hexagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, size, color, 3)
    elif len(approx) == 8:
        cv2.putText(img, "Octagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, size, color, 3)
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, size, color, 3)


cv2.imshow("shapes", img)
cv2.imshow("thresh", thresh)
cv2.waitKey()
cv2.destroyAllWindows()