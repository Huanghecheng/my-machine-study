import cv2

def onChange(x):
    pass


path = '../resource/chongqing_bridge.jpg'

img = cv2.imread(path)

cv2.namedWindow('Blur')

cv2.createTrackbar('ksize', 'Blur', 1, 100, onChange)

while(True):
    ksize = cv2.getTrackbarPos('ksize', 'Blur')

    if ksize == 0:
        ksize = 1

    # Mean Filtering # 均值滤波
    blur = cv2.blur(img, (ksize, ksize))

    cv2.imshow('Blur', blur)

    if cv2.waitKey(1) == 27:
        break