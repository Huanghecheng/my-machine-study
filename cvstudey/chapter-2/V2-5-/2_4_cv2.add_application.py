import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img_path = "image/noise/1.jpg"

img1 = cv.imread(img_path)

# 获取图像分辨率
h, w = img1.shape[:2]
# 创建零矩阵（黑色图像）
J = np.zeros((h, w, 3), dtype=np.double)

for i in range(1, 4):
    I = cv.imread(f"image/noise/{i}.jpg")
    I = I.astype(np.double)
    # 加法
    J = cv.add(I, J)

# 归一化
J4 = cv.normalize(J, None, 0, 255, cv.NORM_MINMAX, dtype=3)
# J4_2 = cv.convertScaleAbs(J / 4, alpha=255.0)


# 因为前面已经累加了4张图像，这里从5开始
for i in range(5, 8):
    I = cv.imread(f"image/noise/{i}.jpg")
    I = I.astype(np.double)
    # 加法
    J = cv.add(I, J)

# 归一化
J8 = cv.normalize(J, None, 0, 255, cv.NORM_MINMAX, dtype=3)

plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1), plt.imshow(img1), plt.title("Original")
plt.subplot(2, 2, 3), plt.imshow(J4), plt.title("Added 4 (normalize)")
plt.subplot(2, 2, 4), plt.imshow(J8), plt.title("Added 8 (normalize)")
plt.show()
