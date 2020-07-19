import cv2
import numpy as np

img1 = np.zeros((512,512,3),np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)

img2 = cv2.imread('messi5.jpg')
img2 = cv2.resize(img2,(512,512))

bitAnd = cv2.bitwise_and(img1,img2)


cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('image',bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()