import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = r'/cv的学习/chapter-2/resource/chongqing_bridge.jpg'

img = cv2.imread(path, cv2.IMREAD_COLOR_RGB)

h, w = img.shape[:2]
x, y = 150,240

print('图像的宽度为：',w,'高度为：',h)

# 平移矩阵
M = np.array([[1,0,x],[0,1,y]],np.float32)
M2 = np.array([[1,0,-x],[0,1,y]],np.float32)
# 应用平移矩阵
B= cv2.warpAffine(img,M,(w,h))
C = cv2.warpAffine(img,M2,(w,h))

plt.figure(figsize=(8,6))
plt.subplot(1,2,1),plt.imshow(img),plt.title('原图像')
plt.subplot(1,2,2),plt.imshow(B),plt.title('图像平移')
# plt.subplot(1,2,1),plt.imshow(C),plt.title('图像平移')
plt.show()