import cv2
import numpy as np

img = cv2.imread("lena.jpg")
layer = img.copy()
gaussian_pyramid = []

#gaussian_pyramid
#biggest[0] -> smallest[5]
for i in range(5):
    gaussian_pyramid.append(layer)
    #cv2.imshow(str(i), layer)
    layer = cv2.pyrDown(layer)

gaussian_pyramid.reverse()
laplacian_pyramid = []
# laplacian pyramid, useful for image compression
for num, image in enumerate(gaussian_pyramid):
    try:
        expanded = cv2.pyrUp(gaussian_pyramid[num])
        lap = cv2.subtract(gaussian_pyramid[num + 1], expanded)
        cv2.imshow(str(num), lap)
        laplacian_pyramid.append(lap)
    except IndexError as e:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()