import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 200)
cap.set(4, 100)
low = 50
high = 150

while True:
    _, frame =cap.read()   

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    canny_frame = cv2.Canny(gray_frame, low, high)
    blur_frame = cv2.GaussianBlur(frame, (5,5),0)
    

    cv2.imshow("Video", frame )
    cv2.imshow("Gray", gray_frame)
    cv2.imshow("RGB", rgb_frame)
    cv2.imshow("canny", canny_frame)
    cv2.imshow("blur", blur_frame)
   

    if cv2.waitKey(10) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

