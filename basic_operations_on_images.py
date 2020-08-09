import numpy as np
import cv2

img = cv2.imread("messi5.jpg")
img2 = cv2.imread("opencv-logo.png")

print(img.shape)  # returns a tuple of number rows, columns, and channels
print(img.size)  # returns total number of pixels that are accessed
print(img.dtype) # returns Image datatype
(b, g, r) = cv2.split(img) # outputs a list with the value of each channel at each point on the array
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

dst = cv2.addWeighted(img, 0.1, img2, 0.9, 0)
cv2.imshow("image", dst)

if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
