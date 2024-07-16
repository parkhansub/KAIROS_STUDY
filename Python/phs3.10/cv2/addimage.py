import cv2
import numpy as np

path1 = "cat.jpg"
path2 = "dog.jpg"

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

img1 = cv2.resize(img1, (img2.shape[1],img2.shape[0]))#사이즈를 맞춰 주는 형식

img3 = cv2.add(img1, img2)#사진을 겹쳐서 합쳐준다.

mask = np.ones((img2.shape[0],img2.shape[1], 3), dtype ='uint8' )*60#mask에 1이 아닌 50이 뿌려진다.
# print(mask)

img_b = cv2.add(img1, mask)
img_d = cv2.subtract(img1, mask)

img_roi = img2[0:img2.shape[0]//2,:,:]



img_green = img1

img_green[img2.shape[0]//5:img2.shape[0]//2,img2.shape[1]//6:img2.shape[1]-img2.shape[1]//6,:] = [0,0,0]
# cv2.imshow("cat",img1)
# cv2.imshow("dog",img2)
# cv2.imshow("add", img3)
# cv2.imshow("b_dog", img_b)
# cv2.imshow("d_dog", img_d)
# cv2.imshow("roi_cat", img_roi)
cv2.imshow("roi_cat", img_green)

cv2.waitKey()
cv2.destroyAllWindows