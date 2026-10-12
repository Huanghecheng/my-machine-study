import cv2
import numpy as np

def onChange(x):
    pass

# 读取灰度图
img_path = r'C:\Users\ASUS\PycharmProjects\PythonProject1\cvbook\images\llama_bw.tif'
img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)

# 统一缩小原图尺寸（控制整体大图大小，按需修改scale）
scale = 0.4  # 0.4就是缩小到原图40%，调大一点画面变大，调小更小
img = cv2.resize(img, None, fx=scale, fy=scale)

cv2.namedWindow('erosion')
cv2.createTrackbar('ksize', 'erosion', 1, 12, onChange)
cv2.namedWindow('dilation')
cv2.createTrackbar('ksize', 'dilation', 1, 12, onChange)

while (True):
    ksize_erosion = cv2.getTrackbarPos('ksize', 'erosion')
    kernel_erosion = np.ones((ksize_erosion, ksize_erosion), np.uint8)
    img_erosion = cv2.erode(img, kernel_erosion)

    ksize_dilation = cv2.getTrackbarPos('ksize', 'dilation')
    kernel_dilation = np.ones((ksize_dilation, ksize_dilation), np.uint8)
    img_dilation = cv2.dilate(img, kernel_dilation)

    # 横向拼接：原图 | 腐蚀 | 膨胀
    combined = np.hstack([img, img_erosion, img_dilation])
    cv2.imshow('Original-Erosion-Dilation', combined)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
