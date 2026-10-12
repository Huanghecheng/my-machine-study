import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 使用 SimHei 黑体 (Windows)
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# 读取图片
path = 'resource/city.png'
img = cv.imread(path, cv.IMREAD_COLOR_RGB)
assert img is not None, "文件无法读取，请检查路径是否存在 (os.path.exists())"

# 拉普拉斯 模板
laplacian_kernel = np.array([[0,  1, 0],
                                    [1, -4, 1],
                                    [0,  1, 0]], np.float32)
gauss_kernel = np.array([[2,   1, 2],
                                [1, -12, 1],
                                [2,  1, 2]], np.float32)

kernel = gauss_kernel

# 拉普拉斯变换 - 边缘检测
# laplacian = cv.filter2D(img, -1, kernel)
# laplacian = cv.Laplacian(img, delta=0, borderType=cv.BORDER_DEFAULT, ddepth=cv.CV_8U, ksize=3)
pos = cv.filter2D(img, -1, - kernel)
neg = cv.filter2D(img, -1,   kernel)

# 拉普拉斯锐化
sharp_a = cv.addWeighted(img, 1.5, pos, -0.5, 0)
sharp_b = cv.addWeighted(img, 1.5, neg, -0.5, 0)

plt.figure(figsize=(10, 5))
plt.subplot(2, 2, 1), plt.imshow(img), plt.title('原图')
plt.subplot(2, 2, 2), plt.imshow(sharp_a), plt.title('锐化 (- 边缘)')
plt.subplot(2, 2, 3), plt.imshow(pos), plt.title('边缘检测')
plt.subplot(2, 2, 4), plt.imshow(sharp_b), plt.title('锐化 (+ 边缘)')
plt.show()
