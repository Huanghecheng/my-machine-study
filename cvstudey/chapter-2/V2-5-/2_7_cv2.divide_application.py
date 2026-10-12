import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

checkerboard = 'image/checkerboard_with_shadow.tif'
shadow = 'image/shadow.tif'

img = cv.imread(checkerboard)
img_shadow = cv.imread(shadow)

# 转换图片为 float / double 以满足除法需要
img_float = img.astype(np.double)
img_shadow_float = img_shadow.astype(np.double)

# 除法
divided_img = cv.divide(img_float, img_shadow_float)

# 归一化
result1 = cv.normalize(divided_img, None, 0.0, 255.0, cv.NORM_MINMAX, dtype=3)

result2 = cv.convertScaleAbs(divided_img, alpha=255.0)

plt.figure(figsize=(10,10))
plt.subplot(2,2,1), plt.imshow(img), plt.title('Checkerboard')
plt.subplot(2,2,2), plt.imshow(img_shadow), plt.title('Shadow')
plt.subplot(2,2,3), plt.imshow(result1), plt.title('Divided Image (normalize)')
plt.subplot(2,2,4), plt.imshow(result2), plt.title('Divided Image (convertScaleAbs)')
plt.show()