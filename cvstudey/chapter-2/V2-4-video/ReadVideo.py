import cv2

capture = cv2.VideoCapture()

capture.open('../resource/RocketLaunch.mp4')

fps = 25

wait_time = int(1000/fps)

i = 0

while True:
    ret, frame = capture.read()
    key = cv2.waitKey(wait_time)
    if key == 27 or not ret:
        break
    cv2.imshow('RocketLaunchVideo', frame)
    cv2.imwrite('../resource/Rocket/Rocket'+str(i)+'.jpg', frame)
    i = i+1
capture.release()