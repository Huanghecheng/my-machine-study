import cv2

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

img = cv2.imread('xiaohe.jpg', cv2.IMREAD_COLOR_RGB)

x, y = 150, 240
w, h = 330 ,250
roi_img = img[ y:y+h,x:x+w]
# 图像翻转
roi_img = img[::-1,:] # 上下翻转
roi_img = img[:,::-1]# 左右翻转

plt.figure(figsize=(6, 4))

plt.subplot(1, 2, 1), plt.imshow(img), plt.title('原图像')
plt.subplot(1, 2, 2), plt.imshow(roi_img), plt.title('截取')

plt.show()



# cv2.imshow('ROI', roi_img)
# cv2.waitKey()