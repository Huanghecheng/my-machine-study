import numpy as np
import cv2
from matplotlib import figure, pyplot as plt
from matplotlib import rcParams
rcParams['font.family']='simHei'#设置中文字体

img = cv2.imread(r'/cv的学习/chapter-2\resource\chongqing_bridge.jpg')
  # 通过设置图像缩放因子对图像进行放大
enlarge = cv2.resize(img,None,fx=4,fy=4,interpolation=cv2.INTER_CUBIC)
  # 通过设置图像像素大小对图像进行缩小
height, width = img.shape[:2]
reduce = cv2.resize(img,(int(0.5 * width),int(0.5 * height)),interpolation=cv2.INTER_AREA)
# cv2.imshow('enlarge',enlarge)
# cv2.imshow('reduce', reduce)
# cv2.waitKey(0)
plt.figure(figsize=(12,12))

plt.subplot(2, 2, 1), plt.imshow(img), plt.title('原图像')
plt.subplot(2, 2, 2), plt.imshow(enlarge), plt.title('放大')
plt.subplot(2, 2, 3), plt.imshow(reduce), plt.title('缩小')
plt.show()