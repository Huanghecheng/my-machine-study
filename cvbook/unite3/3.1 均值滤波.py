import cv2

# 回调函数，本例中无须使用，故为空
def onChange(x):
    pass

img = cv2.imread(r'C:\Users\ASUS\PycharmProjects\PythonProject1\cvstudey\chapter-2\resource\chongqing_bridge.jpg')

cv2.namedWindow('Blur')
cv2.createTrackbar('ksize', 'Blur', 1, 100, onChange)

while (True):
    ksize = cv2.getTrackbarPos('ksize', 'Blur')
    if ksize == 0:
        ksize = 1
    # 通过 cv2.blur() 函数返回值的方式获取处理后的图像数据
    blur = cv2.blur(img, (ksize, ksize))
    # 通过将目标图像以参数形式传给 cv2.blur() 函数的方式获取处理后的图像数据
    # blur = img.copy()
    # cv2.blur(img, (ksize, ksize), blur)

    cv2.imshow('Blur', blur)
    if cv2.waitKey(1) == 27:
        break

