import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(4, 100)

while True:

    _, frame =cap.read() 

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    load_track = np.load("tracksave.npy")

    high = load_track[1]
    low = load_track[0]

    print(high)
    print(low)

    mask = cv2.inRange(hsv_frame, low, high)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 100:
            cv2.drawContours(frame, [max_contour], -1, (0, 0, 255), 2)

    M = cv2.moments(max_contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    cv2.circle(frame, (cx, cy), 20, (0, 255, 0), -1)

           
            
    bitwise_and = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Masking", bitwise_and)


    if cv2.waitKey(10) & 0xff == ord('q'):
            break

    

cv2.destroyAllWindows()