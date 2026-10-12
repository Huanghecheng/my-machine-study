import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义图像路径并读取图像（灰度模式，边缘检测通常需要灰度图）
path = 'resource/tire.tif'
img = cv.imread(path, cv.IMREAD_GRAYSCALE)

assert img is not None, "文件无法读取，请检查路径是否存在 (os.path.exists())"

def gradient_filter(image, kernel):
    """
    实现多种梯度滤波算法
    参数:
    resource: 输入图像 (灰度图像)
    kernel: 梯度滤波算子 ('sobel', 'prewitt', 'roberts', 'scharr')
    返回:
    magnitude: 梯度幅值图像
    direction: 梯度方向图像
    x_gradient: X方向梯度
    y_gradient: Y方向梯度
    """

    # 转换为浮点数以避免溢出
    img_float = image.astype(np.float32)

    # 应用X方向和Y方向的梯度过滤器
    grad_x = cv.filter2D(img_float, -1, kernel, borderType=cv.BORDER_REPLICATE)
    grad_y = cv.filter2D(img_float, -1, kernel.T, borderType=cv.BORDER_REPLICATE)

    # 计算梯度幅值和方向
    magnitude = np.sqrt(grad_x ** 2 + grad_y ** 2)
    direction = np.arctan2(grad_y, grad_x)

    # 归一化到0-255范围
    magnitude = np.clip(magnitude, 0, 255).astype(np.uint8)

    return magnitude, direction, grad_x, grad_y

# 定义 Prewitt 算子核
# kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32) # 水平方向算子
# prewitt_kernel_y = np.array([[-1, -1, -1],
#                                     [0,  0,  0],
#                                     [1,  1,  1]], dtype=np.float32) # 垂直方向算子，垂直梯度滤波模板
# prewitt_kernel_x = prewitt_kernel_y.T # 转置, 水平梯度滤波模板
#
# # 垂直梯度滤波
# prewitt_img_y = cv.filter2D(img.astype(np.float32), -1, prewitt_kernel_y, cv.BORDER_REFLECT)
# # 水平梯度滤波
# prewitt_img_x = cv.filter2D(img.astype(np.float32), -1, prewitt_kernel_x, cv.BORDER_REFLECT)
# # 合并水平和垂直方向的梯度, 计算梯度幅值，得到锐化边缘
# prewitt_img = np.abs(prewitt_img_y) + np.abs(prewitt_img_x)
# # 将结果限制在0-255之间
# prewitt_img = np.clip(prewitt_img, 0, 255).astype(np.uint8)

# Sobel 水平梯度算子
sobel_kernel_x = np.array([[-1, 0, 1],
                                 [-2, 0, 2],
                                 [-1, 0, 1]], dtype=np.float32)
sobel_kernel_y = sobel_kernel_x.T # 转置, 获取水平梯度算子
# 垂直梯度滤波
sobel_img_y = cv.filter2D(img.astype(np.float32), -1, sobel_kernel_y, cv.BORDER_REFLECT)
# 水平梯度滤波
sobel_img_x = cv.filter2D(img.astype(np.float32), -1, sobel_kernel_x, cv.BORDER_REFLECT)

# 叠加 垂直梯度 和 水平梯度
sobel_img = np.sqrt(sobel_img_x ** 2 + sobel_img_y ** 2)
# 将值回归0-255区间
sobel_img = cv.convertScaleAbs(sobel_img, None,1, 0)

# sobel_img = cv.normalize(sobel_img, None, 0, 255)

# 使用 OpenCV 的 Sobel 函数
# sobel_img_x = cv.Sobel(img, cv.CV_32F, 1, 0, ksize=3)
# sobel_img_y = cv.Sobel(img, cv.CV_32F, 0, 1, ksize=3)
# sobel_img, sobel_img_ii, sobel_img_x, sobel_img_y, = gradient_filter(img, sobel_kernel_x)

# #合并水平和垂直方向的梯度, 获取边缘
# sobel_img = np.abs(sobel_img_y) + np.abs(sobel_img_x)
# # 将结果限制在0-255之间
# sobel_img = np.clip(sobel_img, 0, 255).astype(np.uint8)

# 显示结果
plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray'), plt.title('原图')
# plt.subplot(2, 3, 4), plt.imshow(prewitt_img, cmap='gray'), plt.title('Prewitt 边缘检测')
# plt.subplot(2, 3, 5), plt.imshow(prewitt_img_x, cmap='gray'), plt.title('Prewitt 水平梯度')
# plt.subplot(2, 3, 6), plt.imshow(prewitt_img_y, cmap='gray'),  plt.title('Prewitt 垂直梯度')
plt.subplot(2, 3, 4), plt.imshow(sobel_img, cmap='gray'), plt.title('Sobel 边缘检测')
plt.subplot(2, 3, 5), plt.imshow(sobel_img_x, cmap='gray'), plt.title('Sobel 水平梯度')
plt.subplot(2, 3, 6), plt.imshow(sobel_img_y, cmap='gray'), plt.title('Sobel 垂直梯度')
plt.show()


