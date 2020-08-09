import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sudoku.png", cv2.IMREAD_GRAYSCALE)
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 2)
# whenever we encounter an edge in a picture, there is a great change in the intensity. For example, consider a
# marshmellow in a dark room. When we look at the edge of the marshmellow, we are able to identify it by noting the
# blackness on the outside of the marshmellow, This point, where the white pixels change to black produces a huge
# drop in intensity, or in otherwords a place where the rate of intensity change is at a maximum or minimum. Using
# this idea we develop the Laplacian and Sobel functions. These functions allow us to find the places where intensity
# changes.


lap = cv2.Laplacian(img, -1, ksize=1)
#The lower the kernel, the stronger the edge must be (larger change in intensity, as we are comparing directly to the next pixel)
#Use cv2.CV_64F as the values of the Laplacian can be pretty large or small

sobel = cv2.Sobel(img, -1, 1, 1, ksize=1)
#Uses a sobel derivative (directional derivative)

canny = cv2.Canny(img, 100, 200)
images = [img, lap, sobel, canny]
titles = ["Image","Laplacian", "sobel", "Canny"]
for (num, image) in enumerate(images):
    plt.subplot(2, 2, num+1)
    plt.imshow(image, "gray")
    plt.title(titles[num])
    plt.xticks([]), plt.yticks([])

plt.show()