import cv2


# Image Pyramid # 图像金字塔

# PyrDown # 下采样
pyramiddown_0 = cv2.imread('girl.jpg')
pyramiddown_1 = cv2.pyrDown(pyramiddown_0)
pyramiddown_2 = cv2.pyrDown(pyramiddown_1)
cv2.imshow('pyramiddown0', pyramiddown_0)
cv2.imshow('pyramiddown1', pyramiddown_1)
cv2.imshow('pyramiddown2', pyramiddown_2)

# PyrUp # 上采样
pyramidup_0 = cv2.imread('male.jpg')
pyramidup_1 = cv2.pyrUp(pyramidup_0)
pyramidup_2 = cv2.pyrUp(pyramidup_1)
cv2.imshow('pyramidup0', pyramidup_0)
cv2.imshow('pyramidup1', pyramidup_1)
cv2.imshow('pyramidup2', pyramidup_2)

cv2.waitKey()