import cv2

def callBack1():
    pass

def callBack2():
    pass

path = "dog.jpg"

img1 = cv2.imread(path)
img1 = cv2.resize(img1, (400,400))

cv2.namedWindow("style", cv2.WINDOW_NORMAL)
cv2.createTrackbar('sig_S', "style", 1, 2000, callBack1)
cv2.createTrackbar('sig_R', "style", 1, 100, callBack2)




while True:

    s = cv2.getTrackbarPos("sig_S", "style")/10
    r = cv2.getTrackbarPos("sig_R", "style")/100

    img1_style = cv2.stylization(img1, sigma_s= s, sigma_r= r)

    #cv2.imshow("dog",img1)
    cv2.imshow("style", img1_style)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break


cv2.destroyAllWindows

