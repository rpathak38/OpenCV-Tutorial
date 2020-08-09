import cv2
import numpy as np

cap = cv2.VideoCapture("vtest.avi")

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    frame_temp = frame2.copy()

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    kernel = np.ones([3, 3], np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=3)

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame_temp, contours, -1, (0, 0, 255), 3)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if (cv2.contourArea(contour)) < 900:
            continue
        else:
            cv2.rectangle(frame_temp, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
            cv2.putText(frame_temp, "Status {0}".format("Movement"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow("video", frame_temp)

    if cv2.waitKey(40) == ord("q"):
        break

    frame1 = frame2
    ret, frame2 = cap.read()
    if ret == False:
        break

#     ret, frame = cap.read()
#
#     cv2.imshow("frame", frame)
#
#     if cv2.waitKey(60) == ord("q"):
#         break

cv2.destroyAllWindows()
cap.release()

