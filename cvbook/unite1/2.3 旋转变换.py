import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family']='simHei'#设置中文字体

img = cv.imread(r'/cv的学习/chapter-2\resource\chongqing_bridge.jpg', 0)
rows,cols = img.shape
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),70,1)
dst = cv.warpAffine(img,M,(cols,rows))
plt.figure(figsize=(10,10))

plt.subplot(1,2,1),plt.imshow(img),plt.title('原图像')
plt.subplot(1,2,2),plt.imshow(dst),plt.title('旋转')
plt.show()