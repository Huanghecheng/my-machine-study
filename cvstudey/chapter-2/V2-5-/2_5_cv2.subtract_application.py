import cv2 as cv
import matplotlib.pyplot as plt

rice = "image/rice.png"
rice_bg = "image/rice_bg.png"

img1 = cv.imread(rice, cv.IMREAD_GRAYSCALE)
img2 = cv.imread(rice_bg, cv.IMREAD_GRAYSCALE)

# 图像减法
subtracted_img = cv.subtract(img1, img2)

plt.figure(figsize = (10,7))
plt.subplot(2,2,1), plt.imshow(img1, cmap='gray'), plt.title('Rice')
plt.subplot(2,2,2), plt.imshow(img2, cmap='gray'), plt.title('Rice Background')
plt.subplot(2,2,3), plt.imshow(subtracted_img, cmap='gray'), plt.title('Subtracted')
plt.show()