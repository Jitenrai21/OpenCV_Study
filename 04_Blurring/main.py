import os, cv2
img = cv2.imread(os.path.join('.','data','bird.jpg'))
noisy_img = cv2.imread(os.path.join('.','data','noise.jpg'))

k_sz = 7
# img_blur = cv2.blur(img, (k_sz, k_sz)) #classical blur function
# img_gaussian_blur = cv2.GaussianBlur(img, (k_sz, k_sz), 5) 
# img_median_blur = cv2.medianBlur(img,  k_sz)

cv2.imshow('img', noisy_img)
# cv2.imshow('img_blur', img_blur)
# cv2.imshow('img_blurG', img_gaussian_blur)
# cv2.imshow('img_blurM', img_median_blur)

#to remove noise from image
noisy_img_median_blur = cv2.medianBlur(noisy_img,  k_sz)
cv2.imshow('img_blurM_noisy', noisy_img_median_blur)
cv2.waitKey(0)