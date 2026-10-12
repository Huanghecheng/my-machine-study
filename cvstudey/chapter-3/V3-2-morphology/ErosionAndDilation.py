import cv2

import numpy as np

def onChange(x):
    pass

img = cv2.imread('write.jpg', 0)

cv2.namedWindow('erosion')
cv2.createTrackbar('ksize', 'erosion', 1, 12, onChange)

cv2.namedWindow('dilation')
cv2.createTrackbar('ksize', 'dilation', 1, 12, onChange)

while(True):

    ksize_erosion = cv2.getTrackbarPos('ksize', 'erosion')
    kernel_erosion = np.ones((ksize_erosion, ksize_erosion), np.uint8)
    img_erosion = cv2.erode(img, kernel_erosion)
    cv2.imshow('erosion', img_erosion)

    ksize_dilation = cv2.getTrackbarPos('ksize', 'dilation')
    kernel_dilation = np.ones((ksize_dilation,ksize_dilation), np.uint8)
    img_dilation = cv2.dilate(img, kernel_dilation)
    cv2.imshow('dilation', img_dilation)

    if cv2.waitKey(1) == 27:
        break