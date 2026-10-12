import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family']='simHei'#设置中文字体

img = cv.imread(r'/cvstudey\chapter-3\resource\chongqing_bridge.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()