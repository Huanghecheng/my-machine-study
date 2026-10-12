import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = '../resource/write.jpg'

img = cv.imread(path, cv.IMREAD_GRAYSCALE)

# 创建结构元素 - (3, 3)
kernel_size_3 = (3, 3)
diamond_3 = cv.getStructuringElement(cv.MORPH_DIAMOND, kernel_size_3)
cross_3   = cv.getStructuringElement(cv.MORPH_CROSS, kernel_size_3)
# 创建结构元素 - (5, 5)
kernel_size_5 = (5, 5)
diamond_5 = cv.getStructuringElement(cv.MORPH_DIAMOND, kernel_size_5)
cross_5   = cv.getStructuringElement(cv.MORPH_CROSS, kernel_size_5)
# 自定义结构元素
diamond_custom = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
cross_custom = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
line_custom = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.uint8) # 线形结构元素 - k = -1 (-45°)



E_D_3 = cv.dilate(img, kernel=diamond_3, iterations=1)
E_C_3 = cv.dilate(img, kernel=cross_3, iterations=1)
E_L_3 = cv.dilate(img, kernel=line_custom, iterations=1)

E_D_5 = cv.dilate(img, kernel=diamond_5, iterations=1)
E_C_5 = cv.dilate(img, kernel=cross_5, iterations=1)

plt.figure(figsize=(13, 8))
plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray'), plt.title('原图像')
plt.subplot(2, 3, 2), plt.imshow(E_D_3, cmap='gray'), plt.title('膨胀 - 3x3 菱形结构元素')
plt.subplot(2, 3, 3), plt.imshow(E_C_3, cmap='gray'), plt.title('膨胀 - 3x3 十字结构元素')
plt.subplot(2, 3, 4), plt.imshow(E_D_3, cmap='gray'), plt.title('膨胀 - 3x3 线性结构元素')
plt.subplot(2, 3, 5), plt.imshow(E_D_5, cmap='gray'), plt.title('膨胀 - 5x5 菱形结构元素')
plt.subplot(2, 3, 6), plt.imshow(E_C_5, cmap='gray'), plt.title('膨胀 - 5x5 十字结构元素')
plt.show()

