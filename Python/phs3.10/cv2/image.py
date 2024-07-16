import cv2
import numpy as np

path = "dog.jpg"

image = cv2.imread(path)
print(image.shape)

y = image.shape[0]//2
x = image.shape[1]//2

cv2.circle(image, (x,y), 20, (0,0,255), -1)
cv2.rectangle()

#gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("dog", image)
#cv2.imshow("gray_dog", gray_image)

cv2.waitKey()
cv2.destroyAllWindows()