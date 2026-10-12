import cv2

def onChange(x):
    pass

img = cv2.imread('SaltPepperNoise.jpg')

cv2.namedWindow('Blur')

cv2.createTrackbar('ksize', 'Blur', 3, 100, onChange)

while(True):
    ksize = cv2.getTrackbarPos('ksize', 'Blur')

    if ksize <= 3:
        ksize = 3
    if ksize % 2 == 0:
        ksize = ksize + 1

    blur = cv2.GaussianBlur(img, (ksize, ksize), 0)
    cv2.imshow('Blur', blur)

    if cv2.waitKey(1) == 27:
        break

