import cv2
import numpy as np

video_file = "ATIA Video.mp4"
video = cv2.VideoCapture(video_file) # cv2.VideoCapture(0)# video_file

while True:
    (grabbed, frame) = video.read()
    if not grabbed:
        break

    blur = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)  #Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255].

    lower = [22, 50, 50] #[22, 50, 50]
    upper = [35, 255, 255] #[35, 255, 255]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(hsv, lower, upper)

    output = cv2.bitwise_and(frame, hsv, mask=mask)
    cv2.imshow("Frame", frame)
    cv2.imshow("output", output)

    if cv2.waitKey(1) and  0xFF == ord('q'):    #&amp;
        break

cv2.destroyAllWindows()
video.release()
