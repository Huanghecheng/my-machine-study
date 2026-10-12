import cv2
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 设置负号显示

path = '../resource/chongqing_bridge.jpg'
img = cv2.imread(path, cv2.IMREAD_COLOR_RGB)

# 分离通道
r, g, b = cv2.split(img)
# 图像颜色转换
gray = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

plt.figure(figsize=(12, 12))
# 2行，2列，第 1 个位置
plt.subplot(2, 2, 1)
plt.imshow(img)    # plt.plot()
plt.title('原图像')
plt.subplot(2, 2, 2), plt.imshow(r, cmap='gray'), plt.title('红色通道')
plt.subplot(2, 2, 3), plt.imshow(g, cmap='gray'), plt.title('绿色通道')
plt.subplot(2, 2, 4), plt.imshow(b, cmap='gray'), plt.title('蓝色通道')

# cv2.imshow('Gray', gray)
plt.show()
# cv2.waitKey()