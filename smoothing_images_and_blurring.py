import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones([5, 5], np.float32)/25
homogenous = cv2.filter2D(img, -1, kernel)
# this function allows us to convolute our kernel over the image in question. We pass in -1 for depth as it is the default.

blur = cv2.blur(img, (5, 5))
# this function blurs a given image, weighting each pixel in the kernel equally

gblur = cv2.GaussianBlur(img, (5, 5), 0)
# this function blurs a given image, weighting the pixel in the center more

median = cv2.medianBlur(img, 5)
# this function blurs a given image by finding the median of the pixels in it's neighborhood. Thus, it is useful for
# removing salt and pepper noise

bilateral_filter = cv2.bilateralFilter(img, 9, 75, 75)
# an improved version of gaussian blur that preserves edges

titles = ["image", "homogenous", "blur", "Gaussian Blur", "Median Blur", "Bilateral Filter"]
images = [img, homogenous, blur, gblur, median, bilateral_filter]

for num, image in enumerate(images):
    plt.subplot(2, 3, num+1)
    plt.imshow(images[num])
    plt.title(titles[num])
    plt.xticks([]), plt.yticks([])

plt.show()