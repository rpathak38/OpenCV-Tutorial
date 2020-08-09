import cv2

img = cv2.imread("lena.jpg", -1)

cv2.imshow("lena", img)
key = cv2.waitKey(0)

if key == 27:
    cv2.destroyWindow("lena")
elif key == ord("s"):
    cv2.imwrite("lena_copy.png", img)
    cv2.destroyWindow("lena")