import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = '../resource/write.jpg'

img = cv.imread(path, cv.IMREAD_GRAYSCALE)

# 创建结构元素 - (3, 3)
diamond_3 = cv.getStructuringElement(cv.MORPH_DIAMOND, (3, 3))
rect_3   = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
# 创建结构元素 - (6, 6)
diamond_5 = cv.getStructuringElement(cv.MORPH_DIAMOND, (5, 5))
rect_5   = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
# 自定义结构元素
diamond_custom = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
cross_custom = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
line_custom = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.uint8) # 线形结构元素 - k = -1 (-45°)


E_D_3 = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel=diamond_3, iterations=1)
E_C_3 = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel=rect_3, iterations=1)
# 闭运算
# 膨胀 + 腐蚀
dilate = cv.dilate(img, kernel=diamond_custom, iterations=1)
erode = cv.erode(dilate, kernel=diamond_custom, iterations=1)
E_L_3 = erode

E_D_6 = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel=diamond_5, iterations=1)
E_C_6 = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel=rect_5, iterations=1)


plt.figure(figsize=(13, 8))
plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray'), plt.title('原图像')
plt.subplot(2, 3, 2), plt.imshow(E_D_3, cmap='gray'), plt.title('闭运算 - 3x3 菱形结构元素')
plt.subplot(2, 3, 3), plt.imshow(E_C_3, cmap='gray'), plt.title('闭运算 - 3x3 矩形结构元素')
plt.subplot(2, 3, 4), plt.imshow(E_D_3, cmap='gray'), plt.title('闭运算 - 3x3 膨胀 + 腐蚀')
plt.subplot(2, 3, 5), plt.imshow(E_D_6, cmap='gray'), plt.title('闭运算 - 5x5 菱形结构元素')
plt.subplot(2, 3, 6), plt.imshow(E_C_6, cmap='gray'), plt.title('闭运算 - 5x5 矩形结构元素')
plt.show()

