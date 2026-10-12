import cv2
import numpy as np


def onChange(val):
    pass


path = '../../images/chongqing_bridge.jpg'

img = cv2.imread(path)

cv2.imshow('Color Space II ', img)

B, G, R = cv2.split(img)


cv2.namedWindow('Color Space')

count = 200
val = 100

cv2.createTrackbar('R', 'Color Space', val, count, onChange)
cv2.createTrackbar('G', 'Color Space', val, count, onChange)
cv2.createTrackbar('B', 'Color Space', val, count, onChange)

while(True):
    r = cv2.getTrackbarPos('R', 'Color Space')
    g = cv2.getTrackbarPos('G', 'Color Space')
    b = cv2.getTrackbarPos('B', 'Color Space')

    RR = (r / val) * R
    GG = (g / val) * G
    BB = (b / val) * B

    img = cv2.merge([BB, GG, RR])

    img = cv2.convertScaleAbs(img)

    cv2.imshow('Color Space', img)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break