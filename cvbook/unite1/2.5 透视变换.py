import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from matplotlib import rcParams
rcParams['font.family']='simHei'#设置中文字体

img = cv.imread(r'/cvstudey\chapter-3\resource\chongqing_bridge.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('原图像')
plt.subplot(122),plt.imshow(dst),plt.title('透视变换')
plt.show()