import cv2

capture = cv2.VideoCapture()
capture.open(r'/cvstudey\chapter-2\resource\RocketLaunch.mp4')

fps = 120 # 设置帧率
wait_time = int(1000/fps)
while True:
    ret,frame = capture.read()
    key = cv2.waitKey(wait_time)
    if key == 27 or not ret:
        break
    cv2.imshow('RocketLaunchVideo',frame)

capture.release()