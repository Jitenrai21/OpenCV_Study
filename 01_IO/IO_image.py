import os
import cv2 

#read image
image_path = os.path.join('.','data','bird.jpg')
img = cv2.imread(image_path)

#write image
cv2.imwrite(os.path.join('.','data','bird_out.jpg'),img)

#visualize image
cv2.imshow('image', img)
cv2.waitKey(0) #very important for visualizing image tells to wait untill a key is pressed, number except 0 represent the millisecond the image is hold.