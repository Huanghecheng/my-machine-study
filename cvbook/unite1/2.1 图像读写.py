import cv2
import numpy as np
from matplotlib import rcParams
rcParams['font.family']='simHei'#设置中文字体


img = cv2.imread('../cv的学习/chapter-2/V2-5-/image/city.png')
# cv2.imwrite('../chapter-2/V2-5-/image/citrry.png', img) # 保存图片

# 图片读取
cv2.imshow('../chapter-2/V2-5-/image/city.png', img)
cv2.waitKey(0) #等待时间无限时间 点击其他 才能向下继续执行

# 访问图片数据 切片操作
img = cv2.imread('../cv的学习/chapter-2/V2-5-/image/city.png')
x,y = 240,150
roi_img = img[x:x+250,y:y+330]
cv2.imshow('../chapter-2/V2-5-/image/city.png', roi_img)
cv2.waitKey(0)

#访问图片数据 设置区域像素
img = cv2.imread('../cv的学习/chapter-2/V2-5-/image/city.png')
x,y = 240,150
img[x:x+250,y:y+330] = 0
cv2.imshow('../chapter-2/V2-5-/image/city.png', img)
cv2.waitKey(0)
