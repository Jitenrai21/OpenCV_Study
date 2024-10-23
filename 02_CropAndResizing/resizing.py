import os, cv2

img = cv2.imread(os.path.join('.','data','bird.jpg'))
new_img = cv2.resize(img,(640,480))
print(img.shape)
print(new_img.shape)

cv2.imshow('img', img)
cv2.imshow('new_image', new_img)
cv2.waitKey(0)