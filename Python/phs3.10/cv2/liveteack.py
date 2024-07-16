import cv2
import numpy as np

def callBack():
    pass

cap = cv2.VideoCapture(0)
cap.set(3, 200)
cap.set(4, 100)
low = 50
high = 150



cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.createTrackbar('high_B', "Live", 1, 255, callBack)
cv2.createTrackbar('high_G', "Live", 1, 255, callBack)
cv2.createTrackbar('high_R', "Live", 1, 255, callBack)

while True:
    _, frame =cap.read()  

    frame[:,:,0] = frame[:,:,0]+cv2.getTrackbarPos("high_B", "Live")
    frame[:,:,1] = frame[:,:,1]+cv2.getTrackbarPos("high_G", "Live")
    frame[:,:,2] = frame[:,:,2]+cv2.getTrackbarPos("high_R", "Live")


    cv2.imshow("Live", frame ) 


    if cv2.waitKey(10) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
