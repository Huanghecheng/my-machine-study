import cv2

# 回调函数，本例中无须使用，故为空
def onChange(x):
    pass

img = cv2.imread(r'C:\Users\ASUS\PycharmProjects\PythonProject1\cvstudey\chapter-2\resource\chongqing_bridge.jpg')

cv2.namedWindow('Blur')
cv2.createTrackbar('ksize', 'Blur', 1, 20, onChange)

while(True):
    ksize = cv2.getTrackbarPos('ksize', 'Blur')
    if ksize % 2 == 0:
        ksize = ksize + 1
    # 通过 cv2.medianBlur() 函数返回值的方式获取处理后的图像数据
    blur = cv2.medianBlur(img, ksize)
    # 通过将目标图像传给 cv2.medianBlur() 函数的方式获取处理后的图像数据
    # blur = img.copy()

    cv2.imshow('Blur', blur)
    if cv2.waitKey(1) == 27:
        break