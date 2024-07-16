import cv2
import numpy as np

def callBack():
    pass

path = "coca.jpg"

img1 = cv2.imread(path)

cv2.namedWindow("hsv_con")
cv2.createTrackbar('high_H', "hsv_con", 300, 300, callBack)
cv2.createTrackbar('low_H', "hsv_con", 0, 179, callBack)
cv2.createTrackbar('high_S', "hsv_con", 300, 300, callBack)
cv2.createTrackbar('low_S', "hsv_con", 0, 179, callBack)
cv2.createTrackbar('high_V', "hsv_con", 300, 300, callBack)
cv2.createTrackbar('low_V', "hsv_con", 0, 179, callBack)


while True :

    img = img1.copy()

    low_h = cv2.getTrackbarPos("low_H", "hsv_con")
    low_s = cv2.getTrackbarPos("low_S", "hsv_con")
    low_v = cv2.getTrackbarPos("low_V", "hsv_con")
    high_h = cv2.getTrackbarPos("high_H", "hsv_con")
    high_s = cv2.getTrackbarPos("high_S", "hsv_con")
    high_v = cv2.getTrackbarPos("high_V", "hsv_con")

    img_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

    low = np.array([low_h, low_s, low_v])
    high = np.array([high_h, high_s, high_v])

    

    mask = cv2.inRange(img_hsv, low, high)

    result = cv2.bitwise_and(img, img, mask=mask)
    result_hsv = cv2.bitwise_and(img_hsv, img_hsv, mask=mask)

    cv2.imshow("coca", img1)
    cv2.imshow("con_coca", result)

    # cv2.imshow("bitwisexor",b_xor)

    if cv2.waitKey(10) & 0xff == ord('q'):
            hsv = [low,high]
            np.save("hsvsave",hsv)
            print(hsv)
            break
        # elif 0xff == ord('s'):
        #     #np.save("hsvsave.py",hsv)
        #     break

cv2.destroyAllWindows()
