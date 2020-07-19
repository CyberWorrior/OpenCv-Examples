import numpy as np
import cv2


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        clickedColorImage = np.zeros([512, 512, 3], np.uint8)  # black image using numpy zeros
        clickedColorImage[:] = [blue, green, red]
        cv2.imshow('color', clickedColorImage)


img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
