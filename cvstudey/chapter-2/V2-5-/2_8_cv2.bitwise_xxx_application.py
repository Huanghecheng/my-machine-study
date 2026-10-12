import cv2 as cv
import matplotlib.pyplot as plt

A_path = 'image/fireworks.jpg'
B_path = 'image/city.png'

A = cv.imread(A_path, cv.IMREAD_GRAYSCALE)
B = cv.imread(B_path, cv.IMREAD_GRAYSCALE)

# 与
bitwise_and = cv.bitwise_and(A, B)
# 或
bitwise_or = cv.bitwise_or(A, B)
# 非
bitwise_not = cv.bitwise_not(A)
# 异或
bitwise_xor = cv.bitwise_xor(A, B)

plt.figure(figsize = (10,10))
plt.subplot(3,2,1), plt.imshow(A, cmap = 'gray'), plt.title('A')
plt.subplot(3,2,2), plt.imshow(B, cmap = 'gray'), plt.title('B')
plt.subplot(3,2,3), plt.imshow(bitwise_and, cmap = 'gray'), plt.title('A and B')
plt.subplot(3,2,4), plt.imshow(bitwise_or, cmap = 'gray'), plt.title('A or B')
plt.subplot(3,2,5), plt.imshow(bitwise_not, cmap = 'gray'), plt.title('not A')
plt.subplot(3,2,6), plt.imshow(bitwise_xor, cmap = 'gray'), plt.title('xor A, B')
plt.show()