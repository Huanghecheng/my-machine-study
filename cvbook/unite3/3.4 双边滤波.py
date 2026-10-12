import cv2
import numpy as np

def onChange(x):
    pass

img_path = r'C:\Users\ASUS\PycharmProjects\PythonProject1\cvstudey\chapter-2\resource\chongqing_bridge.jpg'
img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)

cv2.namedWindow('Blur')
cv2.createTrackbar('ksize', 'Blur', 1, 60, onChange)
cv2.createTrackbar('sigmaColor', 'Blur', 0, 60, onChange)
cv2.createTrackbar('sigmaSpace', 'Blur', 0, 60, onChange)

while (True):
    ksize = cv2.getTrackbarPos('ksize', 'Blur')
    sigmaColor = cv2.getTrackbarPos('sigmaColor', 'Blur')
    sigmaSpace = cv2.getTrackbarPos('sigmaSpace', 'Blur')

    if ksize == 0:
        ksize = 1

    blur = cv2.bilateralFilter(img, ksize, sigmaColor, sigmaSpace)
    cv2.imshow('Blur', blur)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
