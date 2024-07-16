import cv2
import numpy as np

frame_mask1 = np.zeros((300,300), dtype ='uint8')
frame_mask2 = np.zeros((300,300), dtype ='uint8')

x = 150
y = 150

frame_ciecle = cv2.circle(frame_mask1, (x,y), 150, 255, -1)
frame_rec = cv2.rectangle(frame_mask2, (25,25),(275,275),255,-1)

# b_and = cv2.bitwise_and(frame_rec, frame_ciecle)
# b_or = cv2.bitwise_or(frame_rec, frame_ciecle)
# b_not = cv2.bitwise_not(frame_rec, frame_ciecle)
b_xor = cv2.bitwise_xor(frame_rec, frame_ciecle)

while True :

    # cv2.imshow("circle",frame_ciecle)
    # cv2.imshow("rectangle",frame_rec)
    # cv2.imshow("bitwiseand", b_and)
    # cv2.imshow("bitwiseor", b_or)
    # cv2.imshow("bitwisenot", b_not)
    cv2.imshow("bitwisexor",b_xor)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
