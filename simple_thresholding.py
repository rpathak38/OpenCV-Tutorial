import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread("gradient.png")

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ["Image", "Binary", "Binary Inverse", "Truncated", "To Zero", "To Zero Inverse"]
images = [img, th1, th2, th3, th4, th5]

for num, image in enumerate(images):
    plt.subplot(2, 3, num+1)
    plt.imshow(images[num])
    plt.title(titles[num])
    plt.xticks([]), plt.yticks([])

plt.show()
# cv2.imshow("th1", th1)
# cv2.imshow("th2", th2)
# cv2.imshow("th3", th3)
# cv2.imshow("th4", th4)
# cv2.imshow("th5", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()