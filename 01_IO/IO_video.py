import cv2
import os

video_path = os.path.join('.','data', 'ocean.mp4')

video = cv2.VideoCapture(video_path)

ret = True
while ret:
    ret, frame = video.read() #ret is the boolean value which will be true everytime until their is new frame
    if ret:    
        cv2.imshow('frame',frame)
        cv2.waitKey(33) #the video has frame rate of 30 frame/sec 1/30=0.033
        
video.release()
cv2.destroyAllWindows()