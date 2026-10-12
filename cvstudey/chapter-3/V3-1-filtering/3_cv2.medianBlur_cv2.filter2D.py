import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

# 定义图像路径并读取图像（彩色模式）
path = '../resource/chongqing_bridge.jpg'  # 椒盐噪声图像
img = cv.imread(path, cv.IMREAD_COLOR_RGB)
assert img is not None, "文件无法读取，请检查路径是否存在 (os.path.exists())"

#  定义卷积核大小
kernel_size = 3
# 自定义卷积核 参数 - 1/9
kernel_3 = np.ones((kernel_size, kernel_size), np.float32) / kernel_size ** 2

# 应用均值滤波
img_blurred_kernel_3 = cv.blur(img, (kernel_size, kernel_size))
# 应用高斯滤波
img_gaussian = cv.GaussianBlur(img, (kernel_size, kernel_size), 0)
# 应用中值滤波
img_midfielder = cv.medianBlur(img, kernel_size)

plt.figure(figsize=(10, 5))
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray'), plt.title('原图')
plt.subplot(2, 2, 2), plt.imshow(img_blurred_kernel_3, cmap='gray'), plt.title('均值滤波 3*3卷积核 1/9')
plt.subplot(2, 2, 3), plt.imshow(img_gaussian, cmap='gray'), plt.title('高斯滤波 3*3')
plt.subplot(2, 2, 4), plt.imshow(img_midfielder, cmap='gray'), plt.title('中值滤波 3*3')
plt.show()