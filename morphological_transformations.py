import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("smarties.png", cv2.IMREAD_GRAYSCALE)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
(_, mask) = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones([2, 2], np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel=kernel, iterations=2)
#opening is erosion followed by dilatino, good for removing white noise

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel = kernel, iterations = 4)
# closing is a dilation followed by erosion. Useful for removing black dots in our whitespace

morphological_gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

titles = ["image", "mask", "dilation", "erosion", "opening", "closing", "gradient"]
images = [img, mask, dilation, erosion, opening, closing, morphological_gradient]

for num, image in enumerate(images):
    plt.subplot(2, 4, num + 1)
    plt.imshow(images[num])
    plt.title(titles[num])
    plt.xticks([]), plt.yticks([])

plt.show()