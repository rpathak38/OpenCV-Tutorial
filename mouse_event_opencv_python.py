import numpy as np
import cv2

event_list = [i for i in dir(cv2) if "EVENT" in i]
print(event_list)

img = cv2.imread("lena.jpg")


def click_event(event, x, y, flags, param):
    global img

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        my_color_image = np.zeros((512, 512, 3), np.uint8)
        my_color_image[:, :] = [blue, green, red]
        cv2.imshow("color", my_color_image)
        cv2.imshow("image", img)

    elif event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow("image", img)


points = []

cv2.imshow("image", img)

cv2.setMouseCallback("image", click_event)

if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
