import cv2
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# img = cv2.imread('resource.jpg', cv2.IMREAD_UNCHANGED)
# 读取图像
img = cv2.imread('../resource/chongqing_bridge.jpg', cv2.IMREAD_COLOR_RGB)
# 转换灰度图
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# 存储图像
cv2.imwrite('cat_gray.tif', img2)

print(img2.shape)

plt.figure(figsize=(10, 10))

plt.subplot(1, 2, 1), plt.imshow(img), plt.title('原图像')
plt.subplot(1,2,2), plt.imshow(img2, cmap='gray'), plt.title('灰度图像')
plt.show()

# cv2.imshow('Original Image', img)
# cv2.waitKey(0)