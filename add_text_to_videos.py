import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened() == True):
    (retval, frame) = cap.read()

    if (retval == True):
        datet = str(datetime.datetime.now())
        text = "Width: "+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+" Height: "+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame = cv2.putText(frame, datet, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 0), 2, cv2.LINE_AA)
        cv2.imshow("frame", frame)

        if(cv2.waitKey(1) == ord("q")):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()