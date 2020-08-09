import numpy as np
import cv2

#img = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)
img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (255,255), (242, 144, 82), 5)
cv2.arrowedLine(img, (0, 255), (255,255), (255, 0, 0), 5)
'''
how a rectangle works:
x1,y1__________
|              |
|              |
|              |
|              |
____________x2,y2
'''
cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)
cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow("image", img)

if cv2.waitKey(0):
    cv2.destroyAllWindows()