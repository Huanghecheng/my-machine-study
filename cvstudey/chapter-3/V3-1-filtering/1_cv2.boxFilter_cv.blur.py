import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import scipy

# 使用 SimHei 黑体 (Windows)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

path = '../resource/chongqing_bridge.jpg'

img = cv.imread(path, cv.IMREAD_COLOR_RGB)
assert img is not None, '图片不存在，请检查路径是否正确'

# 滤波模板形状 （模板形状需要为奇数3，5，7，...）
kernel_3 = (3, 3)
kernel_5 = (5, 5)
kernel_7 = (7, 7)

# 使用 cv2.boxFilter()
# 均值滤波
A_i = cv.boxFilter(img, -1, kernel_3)
A_ii = cv.boxFilter(img, -1, kernel_5)
A_iii = cv.boxFilter(img, -1, kernel_7)

# 使用 cv2.blur()
# 均值滤波
B_i = cv.blur(img, kernel_3)    # kernel_3 = (3, 3)
B_ii = cv.blur(img, kernel_5)   # kernel_5 = (5, 5)
B_iii = cv.blur(img, kernel_7)  # kernel_7 = (7, 7)

plt.figure(figsize=(10, 10))
plt.subplot(3,3,1), plt.imshow(img), plt.title('Original')
plt.subplot(3,3,4), plt.imshow(A_i), plt.title('cv2.boxFilter - kernel 3×3')
plt.subplot(3,3,5), plt.imshow(A_ii), plt.title('cv2.boxFilter - kernel 5×5')
plt.subplot(3,3,6), plt.imshow(A_iii), plt.title('cv2.boxFilter - kernel 7×7')
plt.subplot(3,3,7), plt.imshow(B_i), plt.title('cv2.blur - kernel 3×3')
plt.subplot(3,3,8), plt.imshow(B_ii), plt.title('cv2.blur - kernel 5×5')
plt.subplot(3,3,9), plt.imshow(B_iii), plt.title('cv2.blur - kernel 7×7')
plt.show()