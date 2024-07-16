import cv2
import numpy as np


def callBack():
    pass



img_path = 'cat.jpg'

img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_canny = cv2.Canny(img, 10, 100)
mask = np.zeros((img.shape[0],img.shape[1], 3), dtype ='uint8')


cv2.namedWindow("slider")
# cv2.createTrackbar('high_t', "slider", 1, 20, callBack)
cv2.createTrackbar('high_B', "slider", 0, 255, callBack)
cv2.createTrackbar('high_G', "slider", 0, 255, callBack)
cv2.createTrackbar('high_R', "slider", 0, 255, callBack)


while True:



    # high_t = cv2.getTrackbarPos("high_t", "slider")

    # img[:,:,0] = img[:,:,0]+cv2.getTrackbarPos("high_B", "slider")
    # img[:,:,1] = img[:,:,1]+cv2.getTrackbarPos("high_G", "slider")
    # img[:,:,2] = img[:,:,2]+cv2.getTrackbarPos("high_R", "slider")

    # img_blur = cv2.GaussianBlur(img_gray, (5,5), high_t)

    mask[:,:,0] = img[:,:,0]+cv2.getTrackbarPos("high_B", "slider")
    mask[:,:,1] = img[:,:,1]+cv2.getTrackbarPos("high_G", "slider")
    mask[:,:,2] = img[:,:,2]+cv2.getTrackbarPos("high_R", "slider")

    # img_add = cv2.add(img, mask)

    # cv2.imshow("cat_blur", img_blur)
    # cv2.imshow("cat_canny", img_canny)

    # cv2.imshow("cat",img)
    cv2.imshow("add_cat", mask)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
