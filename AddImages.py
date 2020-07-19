import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# final = cv2.add(img,img2)
final = cv2.addWeighted(img, .9, img2, 0.1, 0)

cv2.imshow('image', final)

cv2.waitKey(0)
cv2.destroyAllWindows()
