import math

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

path = '../resource/chongqing_bridge.jpg'
img = cv.imread(path, cv.IMREAD_COLOR_RGB)
assert img is not None, "file could not be read, check with os.path.exists()"


kernel_3 = (3, 3)   # 使用的高斯核（滤波模板）的大小，必须是奇数
kernel_5 = (5, 5)
sigma_x = 0         # X 方向的标准差，如果为0，则根据核大小自动计算

# 高斯滤波
blurred_img = cv.GaussianBlur(img, kernel_3, sigma_x)
# 高斯滤波
blurred_img_ii = cv.GaussianBlur(img, kernel_5, sigma_x)


plt.figure(figsize=(12 , 8))
plt.subplot(2,2,1), plt.imshow(img), plt.title('Original')
plt.subplot(2,2,3), plt.imshow(blurred_img), plt.title('GaussianBlur kernel 3')
plt.subplot(2,2,4), plt.imshow(blurred_img_ii), plt.title('GaussianBlur kernel 5')
plt.show()


def gaussian_kernel(size, sigma):
    """
    生成高斯核
    :param size: 核的大小 (奇数)
    :param sigma: 高斯函数的标准差
    :return: 高斯核
    """
    kernel = np.zeros((size, size))
    center = size // 2

    # 计算高斯核的值
    for i in range(size):
        for j in range(size):
            x, y = i - center, j - center
            kernel[i][j] = (1 / (2 * math.pi * sigma ** 2)) * \
                           math.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))

    # 归一化核，使其总和为1
    kernel /= kernel.sum()
    return kernel


def apply_gaussian_filter(image, kernel_size=5, sigma=1.0):
    """
    应用高斯滤波器到图像
    :param image: 输入图像 (numpy array)
    :param kernel_size: 高斯核大小
    :param sigma: 高斯函数标准差
    :return: 滤波后的图像
    """
    if len(image.shape) == 3:
        # 彩色图像，分别处理每个通道
        channels = []
        for c in range(image.shape[2]):
            filtered_channel = apply_gaussian_to_channel(image[:, :, c], kernel_size, sigma)
            channels.append(filtered_channel)
        return np.stack(channels, axis=2)
    else:
        # 灰度图像
        return apply_gaussian_to_channel(image, kernel_size, sigma)


def apply_gaussian_to_channel(channel, kernel_size, sigma):
    """
    将高斯滤波应用到单个颜色通道
    """
    kernel = gaussian_kernel(kernel_size, sigma)
    height, width = channel.shape
    pad_size = kernel_size // 2

    # 填充图像边缘
    padded_image = np.pad(channel, ((pad_size, pad_size), (pad_size, pad_size)), mode='edge')
    output = np.zeros_like(channel)

    # 卷积操作
    for i in range(height):
        for j in range(width):
            # 提取当前像素周围的区域
            region = padded_image[i:i + kernel_size, j:j + kernel_size]
            # 应用高斯核
            output[i, j] = np.sum(region * kernel)

    return output