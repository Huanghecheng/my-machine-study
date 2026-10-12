import cv2

path = '../resource/chongqing_bridge.jpg'

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

cv2.imshow('Gray', img)

print(img)

cv2.waitKey()


