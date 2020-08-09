import cv2
import numpy as np

img = cv2.imread("messi5.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("messi_face.jpg", cv2.IMREAD_GRAYSCALE)

dimensions = template.shape[::-1]

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.95
location = np.where(result >= threshold)

for point in zip(*location[::-1]):
    cv2.rectangle(img, point, (point[0]+w, point[1]+h), (255, 255, 255), 3)

cv2.imshow("img", img)
cv2.waitKey()
