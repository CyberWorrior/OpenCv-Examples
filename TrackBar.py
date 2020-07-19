import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

while True:

    cv.imshow('image', img)
    k = cv.waitKey(1) & 0XFF
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')

    img[:] = [b, g, r]

    if k == 27:
        break;


cv.destroyAllWindows()
