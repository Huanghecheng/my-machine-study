import cv2 as cv
import matplotlib.pyplot as plt

imurl1 = "image/city.png"
imurl2 = "image/fireworks.jpg"

img1 = cv.imread(imurl1, cv.IMREAD_COLOR_RGB)
img2 = cv.imread(imurl2, cv.IMREAD_COLOR_RGB)

img_added = cv.add(img1,img2)

plt.figure(figsize=(10,7))
plt.subplot(221).imshow(img1)
plt.title("city")
plt.subplot(222).imshow(img2)
plt.title("fireworks")
plt.subplot(223).imshow(img_added)
plt.title("added result")
plt.show()