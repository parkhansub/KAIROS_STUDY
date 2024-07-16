import cv2
cap = cv2.VideoCapture(0)
cap.set(4, 100)

while True:
    _, frame =cap.read() 

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow("live", hsv_frame)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows