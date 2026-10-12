import cv2
cature = cv2.VideoCaptrue(r'C:\Users\ASUS\PycharmProjects\PythonProject1\cv的学习\chapter-2\resource\RocketLaunch.mp4')

# 设置写入视频的基本参数
fps = cature.fps.get(5)  # 获取原视频的帧率
width = int(cature.get(3)) # 原视频宽度
height = int(cature.get(4)) # 原视频高度
fourcc = int(cature.get(6)) # 获取原视频的编码格式
fourcc = cv2.Videowriter_fourcc('X','V','I','D')
size = (width, height) # 设置分辨率
writer = cv2.VideoWriter(r'/cvstudey\chapter-2\resource\RocketLaunch.mp4', fourcc, fps, size)

x,y = int((width/2)-55), int((height/2)-35)  # 设置字幕位置
