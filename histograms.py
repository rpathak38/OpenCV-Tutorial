import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")
# img = np.zeros((200, 200), np.uint8)
# cv2.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv2.rectangle(img, (0, 50), (100, 100), (127), -1)
cv2.imshow("lena", img)

hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)

# (b, g, r) = cv2.split(img)
# plt.hist(b.flatten(), 256, [0, 256])
# plt.hist(g.flatten(), 256, [0, 256])
# plt.hist(r.flatten(), 256, [0, 256])
plt.show()

# cv2.imshow("b", b)
# cv2.imshow("g", g)
# cv2.imshow("r", r)

cv2.waitKey()
cv2.destroyAllWindows()