import cv2

capture = cv2.VideoCapture('../resource/RocketLaunch.mp4')

fps = capture.get(5)

width = int(capture.get(3))

height = int(capture.get(4))

fourcc = int(capture.get(6))

size = (width, height)

writer = cv2.VideoWriter('../resource/RocketLaunchAddCaption.mp4', fourcc, fps, size)

x, y = int((width/2)-55), int(height-15)

captions = ['Ignition', 'Lift off']

lift_off_time = 3*fps

frame_cnt = 0

step = 0

print('=====Start And Caption=====')

while True:
    ret, frame = capture.read()
    frame_cnt = (int(capture.get(0))) / 1000 * fps
    if not ret or cv2.waitKey(1) == 27:
        break
    if frame_cnt == lift_off_time:
        step = 1
    cv2.putText(frame, captions[step], (x, y), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)

    writer.write(frame)

print('=====Process Done=====')
capture.release()
writer.release()
