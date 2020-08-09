import cv2
import numpy as np
# load two images
apple = cv2.imread("apple.jpg")
orange = cv2.imread("orange.jpg")
cv2.imshow("apple_orange", np.hstack((apple[:, :256, :], orange[:, 256:, :])))

cv2.imshow("apple", apple)
cv2.imshow("orange", orange)

#Develop Gaussian Pyramid for apple and orange

apple_gp = []
orange_gp = []
# biggest[0] -> smallest[5]
for i in range(6):
    apple_gp.append(apple)
    apple = cv2.pyrDown(apple)

    orange_gp.append(orange)
    orange = cv2.pyrDown(orange)


# Generate Laplacian pyramids for apple and orange
apple_lp = []
orange_lp = []

for i in range(5, 0, -1):
    expanded = cv2.pyrUp(apple_gp[i])
    apple_lap = cv2.subtract(apple_gp[i-1], expanded)
    apple_lp.append(apple_lap)

    expanded = cv2.pyrUp(orange_gp[i])
    orange_lap = cv2.subtract(orange_gp[i - 1], expanded)
    orange_lp.append(orange_lap)

#smallest[0] -> biggest[4]

# Add left and right parts of both images in each level of the laplacian
apple_orange_pyramid = []
apple_lp.insert(0, apple_gp[5])
orange_lp.insert(0, orange_gp[5])

for (apple_lap, orange_lap) in zip(apple_lp, orange_lp):
    rows, columns, channels = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, :int(columns/2), :], orange_lap[:,int(columns/2):, :]))
    apple_orange_pyramid.append(laplacian)
# smallest[0] -> biggest[4]

apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, len(apple_orange_pyramid)):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow('blended image', apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()
