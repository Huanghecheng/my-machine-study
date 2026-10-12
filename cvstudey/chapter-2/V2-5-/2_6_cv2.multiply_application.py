import cv2 as cv
import matplotlib.pyplot as plt

llama = "image/llama.tif"
llama_bw = "image/llama_bw.tif"

img = cv.imread(llama)
img_bw = cv.imread(llama_bw)

# 归一化 蒙板
normalize_bw = cv.normalize(img_bw, None, 0.0, 1.0, cv.NORM_MINMAX)

# 乘法
multiplied_img = cv.multiply(img, normalize_bw)

plt.figure(figsize = (10,7))
plt.subplot(2,2,1), plt.imshow(img, cmap = 'gray'), plt.title('Original')
plt.subplot(2,2,2), plt.imshow(img_bw, cmap = 'gray'), plt.title('Mask')
plt.subplot(2,2,3), plt.imshow(multiplied_img, cmap = 'gray'), plt.title('Llama')
plt.show()