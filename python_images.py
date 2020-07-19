import cv2
import numpy as np
#img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)
print(img)

img = cv2.line(img, (0, 0), (300, 255), (255, 0, 0), 10)
img = cv2.arrowedLine(img, (0, 0), (255, 255), (0, 0, 0), 10)
img = cv2.rectangle(img, (0, 0), (255, 500), (0, 0, 0), 10)
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_8)

cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_cpy.png', img)
    cv2.destroyAllWindows()
