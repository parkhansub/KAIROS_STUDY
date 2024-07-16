import cv2
import numpy as np

def callBack():
    pass

cap = cv2.VideoCapture(0)
cap.set(4, 100)

cv2.namedWindow("hsv_con", cv2.WINDOW_NORMAL)
cv2.createTrackbar('high_H', "hsv_con", 300, 300, callBack)
cv2.createTrackbar('low_H', "hsv_con", 0, 179, callBack)
cv2.createTrackbar('high_S', "hsv_con", 300, 300, callBack)
cv2.createTrackbar('low_S', "hsv_con", 0, 179, callBack)
cv2.createTrackbar('high_V', "hsv_con", 300, 300, callBack)
cv2.createTrackbar('low_V', "hsv_con", 0, 179, callBack)


while True :

    _, frame =cap.read() 

    low_h = cv2.getTrackbarPos("low_H", "hsv_con")
    low_s = cv2.getTrackbarPos("low_S", "hsv_con")
    low_v = cv2.getTrackbarPos("low_V", "hsv_con")
    high_h = cv2.getTrackbarPos("high_H", "hsv_con")
    high_s = cv2.getTrackbarPos("high_S", "hsv_con")
    high_v = cv2.getTrackbarPos("high_V", "hsv_con")

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low = np.array([low_h, low_s, low_v])
    high = np.array([high_h, high_s, high_v])

    mask = cv2.inRange(hsv_frame, low, high)

    # result_hsv = cv2.bitwise_and(hsv_frame, hsv_frame, mask=mask)
    # result = cv2.bitwise_and(frame, frame, mask=mask)


    #cv2.imshow("cam", frame)
    
    #cv2.imshow("cam", result_hsv)

    # cv2.imshow("bitwisexor",b_xor)

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


    if cv2.waitKey(10) :
        if 0xff == ord('q'):
            break

        elif 0xff == ord("s"):
            np.save()

    

cv2.destroyAllWindows()
