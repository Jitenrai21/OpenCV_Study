import os, cv2

img = cv2.imread(os.path.join('.','data','bird.jpg'))
print(img.shape) #this helps estimate the height width

cropped = img[ 20:800, 420:1200] #height, width

cv2.imshow('img', img)
cv2.imshow('newimg', cropped)
cv2.waitKey(0)