# Types of Morphological Transformations
# dilation
# erosion
# opening
# closing

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('smarties.png',cv.IMREAD_GRAYSCALE)

_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((2, 2), np.uint8)

# dilation: Removes the dot points in the masked image by flushing the np.ones() over it
# iterations: No of times dilation is performed
dilation = cv.dilate(mask, kernal, iterations=2)

# erosion: Erodes away the boundary of the foreground object
erosion = cv.erode(mask, kernal, iterations=1)

# opening: Erosion followed by dilation happens here
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)

# closing: Dilation followed by erosion happens here
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)

# MorphologicalGradient: Difference between dilation and erosion
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)

# Tophat: Difference between mask and opening morph
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(3, 3, 1+i), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
