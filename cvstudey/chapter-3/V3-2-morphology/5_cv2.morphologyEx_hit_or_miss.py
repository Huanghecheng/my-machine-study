import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

path = "../resource/shape.tif"

img = cv.imread(path, cv.IMREAD_GRAYSCALE)

def hit_miss(img, SE_1, SE_2):
    # gray = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
    # 二值化
    _, binary = cv.threshold(img, 0, 255,
                             cv.THRESH_BINARY | cv.THRESH_OTSU)
    # hit
    # hit = cv.erode(binary, SE_1)
    hit = cv.morphologyEx(binary, cv.MORPH_HITMISS, SE_1)
    # miss
    binary_ = cv.bitwise_not(binary)
    # miss = cv.erode(binary_, SE_2)
    miss = cv.morphologyEx(binary_, cv.MORPH_HITMISS, SE_2)
    result = cv.bitwise_and(hit, miss)
    return hit, miss, result

# 创建结构元素 - hit
SE_1 = cv.getStructuringElement(shape=cv.MORPH_RECT,
                                ksize=(30, 30))
# 创建结构元素 - miss
SE_2 = np.ones((32, 32), np.uint8)
SE_2[1:31, 1:31] = 0
print(SE_2)
hit, miss, result = hit_miss(img, SE_1, SE_2)

position = np.where(result == 255)
r_coords, c_coords = position

img_rgb = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
for i in range(len(r_coords)):
    r = r_coords[i]
    c = c_coords[i]
    img_rgb[r, c] = [255, 0, 0]  # 红色点


plt.figure(figsize=(13, 8))
plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray'), plt.title('原图像')
plt.subplot(2, 3, 2), plt.imshow(hit, cmap='gray'), plt.title('Hit-Miss 运算 (hit)')
plt.subplot(2, 3, 3), plt.imshow(miss, cmap='gray'), plt.title('Hit-Miss 运算 (miss)')
plt.subplot(2, 3, 4), plt.imshow(result, cmap='gray'), plt.title('Hit-Miss 运算结果 (hit & miss)')
plt.subplot(2, 3, 5), plt.imshow(img_rgb), plt.title('Hit-Miss 运算结果展示')
plt.show()


